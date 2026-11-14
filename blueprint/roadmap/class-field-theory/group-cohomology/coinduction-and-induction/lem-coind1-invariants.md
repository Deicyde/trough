---
declaration: lemma
origin: cited
lean: Rep.coind₁_quotientToInvariants_iso, Rep.coind₁_quotientToInvariants_trivialCohomology
statement: formalized
proof: formalized
---

# coind₁ invariants

Let $S$ be a normal subgroup of $G$. Then $\mathrm{coind}_1(G,A)^S$ is isomorphic to $\mathrm{coind}_1(G/S,A)$. In particular $\mathrm{coind}_1(G,A)^S$ is has trivial cohomology as a representation of $G/S$.

## Depends on

- [induced](def-induced.md)
- [coind₁ trivial cohomology](lem-coind1-trivial-cohomology.md)

## Proof

Let $f : G \to A$. Then $f$ is in the subspace $\mathrm{coind}_1(G,A)^S$ if $f$ is constant on cosets of $S$, i.e. it descends to a function $G/S \to A$. This gives a linear bijection $\mathrm{coind}_1(G,A)^S \cong \mathrm{coind}_1(G/S,A)$, and it's trivial to check that this map is compatible with the action of $G / S$.

## Lean

Formalized as [`Rep.coind₁_quotientToInvariants_iso`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.coind₁_quotientToInvariants_iso), [`Rep.coind₁_quotientToInvariants_trivialCohomology`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.coind₁_quotientToInvariants_trivialCohomology).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 815](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L815)
