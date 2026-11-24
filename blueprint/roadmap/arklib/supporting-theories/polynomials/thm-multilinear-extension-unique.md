---
declaration: theorem
origin: cited
lean: MvPolynomial.eq_MLE_of_degreeOf_le_one_of_eval_zeroOne_eq
statement: formalized
---

# Multilinear Extension is Unique

Let $R$ be a commutative ring and $v:\{0,1\}^n\to R$. If $p\in R[X_1,\ldots,X_n]$ has degree at most one in each variable and $p(x)=v(x)$ for every $x\in\{0,1\}^n$, then $p=\widetilde{v}$.

## Depends on

- [Multilinear Extension](def-multilinear-extension.md)

## Lean

Stated as [`MvPolynomial.eq_MLE_of_degreeOf_le_one_of_eval_zeroOne_eq`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/MvPolynomial.eq_MLE_of_degreeOf_le_one_of_eval_zeroOne_eq); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: polynomials/defs.tex, line 14](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/polynomials/defs.tex#L14)
