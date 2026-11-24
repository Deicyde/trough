---
declaration: definition
origin: cited
lean: Reduction.completeness
statement: formalized
---

# Completeness

A reduction satisfies **completeness** with error $\epsilon \geq 0$ and with respect to input relation $R_{\text{in}}$ and output relation $R_{\text{out}}$, if for all valid statement-witness pair $(x_{\text{in}}, w_{\text{in}})$ for $R_{\text{in}}$, the execution between the honest prover and the honest verifier will result in a tuple $((x_{\text{out}}^P, w_{\text{out}}), x_{\text{out}}^V)$ such that:

- $R_{\text{out}}(x_{\text{out}}^V, w_{\text{out}}) = \text{True}$ (the output statement-witness pair is valid), and
- $x_{\text{out}}^P = x_{\text{out}}^V$ (the output statements are the same from both prover and verifier)

except with probability $\epsilon$.

## Depends on

- [Interactive Reduction](def-reduction.md)
- [Interactive Reduction Execution](def-reduction-run.md)

## Lean

Formalized as [`Reduction.completeness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Reduction.completeness).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 447](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/oracle_reductions/defs.tex#L447)
