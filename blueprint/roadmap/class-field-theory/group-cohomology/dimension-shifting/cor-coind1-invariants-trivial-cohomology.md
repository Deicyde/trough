---
declaration: corollary
origin: cited
lean: Rep.coind₁'_quotientToInvariants_trivialCohomology
statement: formalized
proof: formalized
---

# coind₁' invariants trivial cohomology

Let $S$ be a normal subgroup of $G$. Then $\mathrm{coind}_1'(M)^S$ has trivial cohomology as a representation of $G/S$.

## Depends on

- [coind₁ invariants](../coinduction-and-induction/lem-coind1-invariants.md)
- [coind₁' iso coind₁](lem-coind1-iso-coind1.md)
- [inflation restriction functors](../group-cohomology-and-homology/def-inflation-restriction-functors.md)

## Proof

We've seen in Lemma [coind₁' iso coind₁](lem-coind1-iso-coind1.md) that $\mathrm{coind}_1'(M)$ is isomorphic to $\mathrm{coind}_1(M)$. Applying the functor $\mathbf{invar}$, we obtain an isomorphism between $\mathrm{coind}_1'(M)^S$ and $\mathrm{coind}_1(M)^S$. The result then follows from Lemma [coind₁ invariants](../coinduction-and-induction/lem-coind1-invariants.md).

## Lean

Formalized as [`Rep.coind₁'_quotientToInvariants_trivialCohomology`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.coind₁'_quotientToInvariants_trivialCohomology).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 975](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L975)
