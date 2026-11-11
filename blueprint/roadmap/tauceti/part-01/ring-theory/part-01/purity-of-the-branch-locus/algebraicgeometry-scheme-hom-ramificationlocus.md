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
- [Source of `AlgebraicGeometry.Scheme.Hom.ramificationLocus` in TauCeti/AlgebraicGeometry/Morphisms/RamificationLocus.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Morphisms/RamificationLocus.lean#L101)
- [Tau Ceti roadmap status: Purity of the branch locus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PurityOfBranchLocus/STATUS.md)
