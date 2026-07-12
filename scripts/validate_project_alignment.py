#!/usr/bin/env python3
"""Validate PactRide's public identity, privacy, completion, and licensing posture."""

from __future__ import annotations

import json
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://wpgglabs.github.io/PactRide/"
APACHE_URL = "https://www.apache.org/licenses/LICENSE-2.0"
TEXT_SUFFIXES = {
    ".cff", ".css", ".html", ".js", ".json", ".md", ".py", ".svg",
    ".toml", ".txt", ".xml", ".yaml", ".yml",
}
PRIVATE_NAME_TOKENS = (
    ("mi" + "raz").casefold(),
    ("meh" + "bub").casefold(),
)


class StructuredDataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.canonical: list[str] = []
        self.json_ld: list[str] = []
        self._capture = False
        self._buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if tag == "link" and values.get("rel") == "canonical":
            self.canonical.append(values.get("href", ""))
        if tag == "script" and values.get("type") == "application/ld+json":
            self._capture = True
            self._buffer = []

    def handle_data(self, data: str) -> None:
        if self._capture:
            self._buffer.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._capture:
            self.json_ld.append("".join(self._buffer).strip())
            self._capture = False
            self._buffer = []


def read(path: str) -> str:
    target = ROOT / path
    if not target.is_file():
        raise AssertionError(f"required file is missing: {path}")
    return target.read_text(encoding="utf-8")


def require(text: str, phrase: str, context: str) -> None:
    if phrase.casefold() not in text.casefold():
        raise AssertionError(f"{context} must contain {phrase!r}")


def validate_license() -> None:
    license_text = read("LICENSE")
    for phrase in (
        "Apache License",
        "Version 2.0, January 2004",
        "Grant of Copyright License",
        "Grant of Patent License",
        "END OF TERMS AND CONDITIONS",
    ):
        require(license_text, phrase, "LICENSE")


def validate_documents() -> None:
    required_documents = (
        "README.md",
        "STATUS.md",
        "FOUNDER_VISION.md",
        "COMMONPACT_RELATIONSHIP.md",
        "ROADMAP.md",
        "MAINTAINERS.md",
        "GOVERNANCE.md",
        "LICENSING.md",
        "MONETIZATION.md",
        "CONTRIBUTOR_POLICY.md",
        "FAQ.md",
    )

    for filename in required_documents:
        text = read(filename)
        require(text, "PactRide", filename)

    require(read("README.md"), "Apache License 2.0", "README.md")
    require(read("README.md"), "Founder-vision documentation: complete", "README.md")
    require(read("STATUS.md"), "Founder-vision status", "STATUS.md")
    require(read("STATUS.md"), "Implementation maturity", "STATUS.md")
    require(read("STATUS.md"), "COMMONPACT_RELATIONSHIP.md", "STATUS.md")
    require(read("FOUNDER_VISION.md"), 'Meaning of "100% documented"', "FOUNDER_VISION.md")
    require(read("FOUNDER_VISION.md"), "pre-implementation", "FOUNDER_VISION.md")
    require(read("COMMONPACT_RELATIONSHIP.md"), "PactRide implementations need only", "COMMONPACT_RELATIONSHIP.md")
    require(read("COMMONPACT_RELATIONSHIP.md"), "Safety preservation rule", "COMMONPACT_RELATIONSHIP.md")
    require(read("MAINTAINERS.md"), "`wpggLabs`", "MAINTAINERS.md")
    require(read("LICENSING.md"), "Apache License 2.0", "LICENSING.md")
    require(read("LICENSING.md"), "does **not** automatically require", "LICENSING.md")
    require(read("MONETIZATION.md"), "does not create an automatic right", "MONETIZATION.md")


def validate_website() -> None:
    html = read("docs/index.html")
    parser = StructuredDataParser()
    parser.feed(html)

    if parser.canonical != [SITE_URL]:
        raise AssertionError(f"website canonical URL must be exactly {SITE_URL!r}")
    if len(parser.json_ld) != 1:
        raise AssertionError("website must contain exactly one JSON-LD object")

    structured = json.loads(parser.json_ld[0])
    if structured.get("url") != SITE_URL:
        raise AssertionError("website JSON-LD URL is not canonical")
    if structured.get("license") != APACHE_URL:
        raise AssertionError("website JSON-LD must identify Apache-2.0")

    author = structured.get("author", {})
    if author.get("name") != "wpggLabs":
        raise AssertionError("website JSON-LD must identify wpggLabs")

    for phrase in (
        "Founder vision documented",
        "Pre-implementation research RFC",
        "COMMONPACT_RELATIONSHIP.md",
        "Open specification. Optional commercial value.",
    ):
        require(html, phrase, "docs/index.html")


def validate_citation() -> None:
    citation = read("CITATION.cff")
    require(citation, "cff-version: 1.2.0", "CITATION.cff")
    require(citation, 'name: "wpggLabs"', "CITATION.cff")
    require(citation, "license: Apache-2.0", "CITATION.cff")
    if "family-names:" in citation or "given-names:" in citation:
        raise AssertionError("CITATION.cff must not contain personal-name author fields")


def validate_public_identity_privacy() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in {".git", ".venv", "__pycache__"} for part in path.parts):
            continue
        if path.suffix.casefold() not in TEXT_SUFFIXES and path.name != "CITATION.cff":
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        folded = content.casefold()
        for token in PRIVATE_NAME_TOKENS:
            if token in folded:
                raise AssertionError(
                    f"{path.relative_to(ROOT)} contains a private personal-name token"
                )

    codemeta = json.loads(read("codemeta.json"))
    author = codemeta.get("author", {})
    if author.get("@type") != "Organization" or author.get("name") != "wpggLabs":
        raise AssertionError("codemeta.json must identify wpggLabs as an organization")


def main() -> int:
    checks = (
        ("Apache-2.0 license", validate_license),
        ("public documents", validate_documents),
        ("website metadata", validate_website),
        ("citation metadata", validate_citation),
        ("public identity privacy", validate_public_identity_privacy),
    )

    failures: list[str] = []
    for name, check in checks:
        try:
            check()
        except (AssertionError, json.JSONDecodeError) as exc:
            failures.append(f"FAIL {name}: {exc}")
        else:
            print(f"PASS {name}")

    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1

    print("PASS PactRide public identity privacy, founder-vision completion, and licensing claims are aligned")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
