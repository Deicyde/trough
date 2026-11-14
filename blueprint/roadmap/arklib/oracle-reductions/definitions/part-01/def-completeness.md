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

- [ArkLib blueprint: oracle_reductions/defs.tex, line 447](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L447)
