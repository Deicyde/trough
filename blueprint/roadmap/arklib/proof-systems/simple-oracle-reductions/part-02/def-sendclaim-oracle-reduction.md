---
declaration: definition
origin: cited
lean: SendClaim.oracleReduction, SendClaim.toORelOut
statement: formalized
---

# SendClaim Oracle Reduction

Fix a message type $M$ with an oracle interface, a map $f$ from statements and oracle statements to $M$, and a predicate $P$ on a statement, its oracle statements and a message. The SendClaim reduction is a one-round protocol with no witness:

- **Protocol specification**: $\mathsf{pSpec} := [(\mathsf{P \!\!\rightarrow\!\! V}, M)]$ (single oracle message)
- **Prover**: Sends $f(\mathsf{stmt}, \mathsf{o})$ as the message
- **Verifier**: A pure pass-through. It returns the input statement and performs no check
- **Output oracle statements**: The input oracle statements together with the message, indexed by $\iota_{\mathsf{in}} \oplus \mathsf{Fin}(1)$
- **Output relation**: The input oracle statements (at $\mathsf{inl}$) satisfy $R_{\mathsf{in}}$, and $P(\mathsf{stmt}, \mathsf{o}, m)$ holds for the message $m$ at $\mathsf{inr}(0)$

## Depends on

- [Interactive Oracle Reduction](../../../oracle-reductions/definitions/part-01/def-oracle-reduction.md)

## Lean

Formalized as [`SendClaim.oracleReduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/SendClaim.oracleReduction), [`SendClaim.toORelOut`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/SendClaim.toORelOut).

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 260](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L260)
