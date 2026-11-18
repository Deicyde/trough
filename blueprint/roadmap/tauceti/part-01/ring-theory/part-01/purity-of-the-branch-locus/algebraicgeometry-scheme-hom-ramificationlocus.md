---
declaration: def
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.ramificationLocus
statement: formalized
---

# AlgebraicGeometry.Scheme.Hom.ramificationLocus

The **ramification locus** of `f`: the points of `X` at which `f` is not unramified, with
"unramified at `x`" meaning that the stalk map `𝒪_{Y, f x} → 𝒪_{X, x}` is formally unramified.
For `f` locally of finite type it is the complement of the set of points at which `f` is
unramified in the sense of Stacks, Definition 29.36.1 (02G4); see
`ramificationLocus_eq_setOf_not_exists`.

```lean
AlgebraicGeometry.Scheme.Hom.ramificationLocus.{u} {X Y : AlgebraicGeometry.Scheme} (f : X ⟶ Y) :
  Set ↥X
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.Hom.ramificationLocus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Morphisms/RamificationLocus.html#AlgebraicGeometry.Scheme.Hom.ramificationLocus).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.Hom.ramificationLocus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Morphisms/RamificationLocus.html#AlgebraicGeometry.Scheme.Hom.ramificationLocus)
- [Source of `AlgebraicGeometry.Scheme.Hom.ramificationLocus` in TauCeti/AlgebraicGeometry/Morphisms/RamificationLocus.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Morphisms/RamificationLocus.lean#L101)
- [Tau Ceti roadmap status: Purity of the branch locus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PurityOfBranchLocus/STATUS.md)
