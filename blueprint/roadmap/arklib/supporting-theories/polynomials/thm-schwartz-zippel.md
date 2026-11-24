---
declaration: theorem
origin: cited
lean: MvPolynomial.schwartz_zippel_sum_degreeOf
statement: formalized
---

# Schwartz-Zippel Lemma

Let $R$ be an integral domain, let $p\in R[X_1,\ldots,X_n]$ be nonzero, and let $S_1,\ldots,S_n\subseteq R$ be finite sets. Then

$$
\frac{\bigl|\{x\in S_1\times\cdots\times S_n : p(x)=0\}\bigr|}{\prod_{i}|S_i|}
\le\sum_{i=1}^{n}\frac{\deg_{X_i}p}{|S_i|}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Stated as [`MvPolynomial.schwartz_zippel_sum_degreeOf`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/MvPolynomial.schwartz_zippel_sum_degreeOf); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: polynomials/defs.tex, line 25](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/polynomials/defs.tex#L25)
