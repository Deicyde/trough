---
declaration: definition
origin: cited
lean: MvPolynomial.MLE
statement: formalized
---

# Multilinear Extension

For a commutative ring $R$ and a function $v:\{0,1\}^{\sigma}\to R$, the multilinear extension of $v$ is $\widetilde{v}:=\sum_{x\in\{0,1\}^{\sigma}}\mathsf{eq}(x,X)\cdot v(x)$, where $\mathsf{eq}(x,X)=\prod_{i}\bigl((1-x_i)(1-X_i)+x_iX_i\bigr)$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MvPolynomial.MLE`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/MvPolynomial.MLE).

## Sources

- [ArkLib blueprint: polynomials/defs.tex, line 5](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/polynomials/defs.tex#L5)
