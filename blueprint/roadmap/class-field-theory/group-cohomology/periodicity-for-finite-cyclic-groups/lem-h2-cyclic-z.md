---
declaration: lemma
origin: cited
lean: groupCohomology.evenTrivialInt, groupCohomology.isZero_odd_trivial_of_isAddTorsionFree
statement: formalized
proof: formalized
---

# H2 cyclic Z

Let $G$ be a finite cyclic group of order $n$. Then $H^1(G,{\mathbb Z}) \cong 0$ and $H^2(G,{\mathbb Z}) \cong {\mathbb Z}/n{\mathbb Z}$.

## Depends on

- [periodic cohomology](cor-periodic-cohomology.md)

## Proof

Since the module ${\mathbb Z}$ is trivial, we have $H^1(G,{\mathbb Z})\cong \mathrm{Hom}(G,{\mathbb Z}) \cong 0$.

It follows from [Tate cohomology is cohomology or homology](../tate-cohomology/lem-tate-cohomology-is-cohomology-or-homology.md) that $H^0_{\mathrm{Tate}}(G,{\mathbb Z}) \cong {\mathbb Z} /n{\mathbb Z}$. Hence by periodicity there is an isomorphism $H^2(G,{\mathbb Z}) \cong {\mathbb Z}/ n{\mathbb Z}$.

## Lean

Formalized as [`groupCohomology.evenTrivialInt`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.evenTrivialInt), [`groupCohomology.isZero_odd_trivial_of_isAddTorsionFree`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.isZero_odd_trivial_of_isAddTorsionFree).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 1612](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L1612)
