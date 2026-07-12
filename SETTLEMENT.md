# Settlement and Payments

## Position

PactRide is payment-neutral. The base protocol records negotiated economic terms and optional settlement evidence but does not require a platform wallet, native token, cryptocurrency, card processor, escrow provider, or commission.

## Why settlement is separate

Payment methods have different laws, finality, privacy, chargeback, fraud, identity, and availability characteristics. Making one method mandatory would create a new central dependency or force every client into the same risk model.

## Base-protocol responsibilities

The base protocol may represent:

- Amount.
- Currency.
- Who is expected to pay.
- Accepted settlement methods.
- When payment is due.
- Cancellation terms.
- Optional tip handling.
- Optional external proof reference.
- Each party's declaration of settlement status.

It does not declare that a payment occurred unless method-specific evidence is independently verifiable.

## Terms example

```json
{
  "amount": "28.00",
  "currency": "USD",
  "settlement_methods": ["cash", "external-transfer"],
  "due": "at-completion",
  "platform_fee": "0.00",
  "additional_terms": {
    "tolls": "actual-cost-if-agreed",
    "tip": "optional"
  }
}
```

Money values must use decimal strings or integer minor units—never binary floating point.

## Settlement states

- `not-applicable`
- `not-started`
- `requested`
- `declared-sent`
- `declared-received`
- `externally-verified`
- `disputed`
- `refunded`
- `unknown`

A sender declaration and receiver declaration are separate events. A bilateral completion receipt may contain both declarations but still may not prove irreversible finality.

## Payment methods

### Cash

Advantages: direct, accessible, no processor, works offline.

Limitations: no cryptographic proof, safety risk, change handling, disputes.

### Bank or wallet transfer

Advantages: direct existing rails.

Limitations: regional availability, account linkage, privacy, reversal rules, external app dependency.

### Card payment

Advantages: familiar consumer protection.

Limitations: processor fees, identity requirements, chargebacks, central dependency, operator obligations.

### Cryptocurrency or Lightning

Advantages: optional direct programmable settlement.

Limitations: volatility, custody, loss, regulation, liquidity, UX, scams, and privacy. It must remain optional and must not become PactRide's identity or governance layer.

### Community credit or cooperative account

Advantages: useful in established communities.

Limitations: requires accounting, governance, default handling, and local trust.

## Extension profiles

Payment integrations should be separate profiles. A profile defines:

- Method identifier.
- Required fields.
- Invoice or request format.
- Proof semantics.
- Finality assumptions.
- Refund/dispute behavior.
- Privacy and metadata exposure.
- Failure states.

## Fees

Compatible clients and service providers may charge transparent fees. The protocol should represent fees separately from driver fare so users can inspect:

- Driver amount.
- Relay/service fee.
- Payment processing fee.
- Taxes or tolls where represented.
- Optional donation.

Hidden deductions violate PactRide principles even if technically possible.

## Escrow

The base protocol does not provide escrow. Escrow introduces custody, arbitration, capital, identity, and legal obligations. Communities may use optional external escrow services, but clients must identify the operator, rules, fees, and failure conditions.

## Payment privacy

Payment systems can link identity and travel patterns. Clients should disclose what payment data leaves the device and avoid publishing payment references in public discovery events.

## v0.1 recommendation

The first interoperable simulation should negotiate an amount and mark settlement as out-of-band. Do not delay protocol testing for payment integration.
