---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.gradedRelativeSpecEquiv
statement: formalized
---

# TauCeti.AlgebraicGeometry.gradedRelativeSpecEquiv

Graded relative Spec is an anti-equivalence between graded quasicoherent algebras and graded
affine schemes over `X`. The functor sends `A` to the relative spectrum of `⨁ₙ Aₙ`, graded through
the relative-Spec unit `p_* 𝒪 ≅ ⨁ₙ Aₙ`, and the inverse reads off the grading. The unit is the
identity, and the counit is, on underlying schemes, relative Spec of the grading isomorphism
followed by the relative-Spec counit.

```lean
TauCeti.AlgebraicGeometry.gradedRelativeSpecEquiv.{u} (X : AlgebraicGeometry.Scheme) :
  (TauCeti.AlgebraicGeometry.GradedQuasicoherentAlgebra X)ᵒᵖ ≌
    TauCeti.AlgebraicGeometry.GradedAffineSchemeOver X
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.AlgebraicGeometry.relativeSpecEquiv](tauceti-algebraicgeometry-relativespecequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.gradedRelativeSpecEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/RelativeSpec/Graded.html#TauCeti.AlgebraicGeometry.gradedRelativeSpecEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.gradedRelativeSpecEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/RelativeSpec/Graded.html#TauCeti.AlgebraicGeometry.gradedRelativeSpecEquiv)
- [Source of `TauCeti.AlgebraicGeometry.gradedRelativeSpecEquiv` in TauCeti/AlgebraicGeometry/RelativeSpec/Graded.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/RelativeSpec/Graded.lean#L71)
- [Tau Ceti roadmap status: Algebraic vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicVectorBundles/STATUS.md)
