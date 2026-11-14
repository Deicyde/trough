---
declaration: lemma
origin: cited
lean: ArkLib.Lattices.CyclotomicModulus.mk_reverse_eq_galoisAutₛ_mul
statement: formalized
---

# The reverse identity

In $S$, with $\mathrm{mk}$ the quotient map and $\sigma_{-1} = \texttt{galoisAutₛ}$ of exponent $2^{\alpha+1}-1$,

$$
\mathrm{mk}(p^{\mathrm{rev}}) \;=\; \sigma_{-1}(\mathrm{mk}\,p)\cdot(\mathrm{mk}\,X)^{\deg p}.
$$

Since $\mathrm{mk}\,X$ is a unit, $\sigma_{-1}$ carries the ideal $(\mathrm{mk}\,p)$ onto $(\mathrm{mk}\,p^{\mathrm{rev}})$. Proved from Mathlib's `Polynomial.eval₂_reverse_mul_pow` at the point $(\mathrm{mk}\,X)^{-1} = (\mathrm{mk}\,X)^{c}$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Stated as [`ArkLib.Lattices.CyclotomicModulus.mk_reverse_eq_galoisAutₛ_mul`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ArkLib.Lattices.CyclotomicModulus.mk_reverse_eq_galoisAutₛ_mul); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: lattices/hachi_subfield.tex, line 164](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/lattices/hachi_subfield.tex#L164)
