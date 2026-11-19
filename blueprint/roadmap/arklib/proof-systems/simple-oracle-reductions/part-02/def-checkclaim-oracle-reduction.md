---
declaration: definition
origin: cited
lean: CheckClaim.oracleReduction, CheckClaim.oracleRelOut
statement: formalized
---

# CheckClaim Oracle Reduction

The oracle version checks a predicate $P(\mathsf{stmt}, \mathsf{o})$ on the statement and the oracle statements. Its verifier is a pure pass-through: it returns the statement and oracle statements unchanged and runs no check. The check is carried by the output relation:

- **Input relation**: any relation $R_{\mathsf{in}}$ on statements and oracle statements, with unit witness
- **Output relation**: $R_{\mathsf{out}} := R_{\mathsf{in}} \cap \{(\mathsf{stmt}, \mathsf{o}) \mid P(\mathsf{stmt}, \mathsf{o})\}$

A pure verifier can be the left factor of a coordinate-wise special-soundness composition, which a verifier that rejects at runtime cannot.

## Depends on

- [Interactive Oracle Reduction](../../../oracle-reductions/definitions/part-01/def-oracle-reduction.md)
- [CheckClaim Reduction](def-checkclaim-reduction.md)

## Lean

Formalized as [`CheckClaim.oracleReduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/CheckClaim.oracleReduction), [`CheckClaim.oracleRelOut`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/CheckClaim.oracleRelOut).

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 386](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L386)
