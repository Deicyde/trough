---
declaration: theorem
origin: cited
lean: ArkLib.Lattices.CyclotomicModulus.galoisAutₛ_fixed_isUnit
statement: formalized
proof: formalized
---

# Core unit lemma

In $S = \mathbb{F}_q[X]/(X^{2^\alpha}+1)$ every nonzero $\sigma_{-1}$-fixed element is a unit.

## Depends on

- [The reverse identity](lem-conj-reverse.md)
- [No self-reciprocal factor](lem-no-selfreciprocal.md)
- [Factor existence](lem-factorization.md)

## Proof

Write the element as $\mathrm{mk}\,g$. If it is not a unit then $g$ is not coprime to $X^{2^\alpha}+1 = p_1 p_2$, so (WLOG) $p_1 \mid g$. The reverse identity (Lemma [The reverse identity](lem-conj-reverse.md)) together with $p_1^{\mathrm{rev}} \sim p_2$ (Lemma [No self-reciprocal factor](lem-no-selfreciprocal.md)) gives $\mathrm{mk}\,p_2 \mid \sigma_{-1}(\mathrm{mk}\,p_1) \mid \sigma_{-1}(\mathrm{mk}\,g) = \mathrm{mk}\,g$, hence $p_2 \mid g$. With $p_1 \mid g$ and $p_1, p_2$ coprime, $X^{2^\alpha}+1 \mid g$, so $\mathrm{mk}\,g = 0$, a contradiction.

## Lean

Formalized as [`ArkLib.Lattices.CyclotomicModulus.galoisAutₛ_fixed_isUnit`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ArkLib.Lattices.CyclotomicModulus.galoisAutₛ_fixed_isUnit).

## Sources

- [ArkLib blueprint: lattices/hachi_subfield.tex, line 196](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/lattices/hachi_subfield.tex#L196)
