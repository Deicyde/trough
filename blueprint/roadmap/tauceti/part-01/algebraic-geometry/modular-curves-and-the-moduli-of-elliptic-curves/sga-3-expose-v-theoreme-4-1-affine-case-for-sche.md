---
declaration: def
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.isColimitAffineCoequalizerCofork
statement: formalized
---

# SGA 3, Exposé V, Théorème 4.1, affine case, for schemes

If `p₁ p₂ : R ⟶ X` is an
equivalence relation of schemes with `X` affine and `p₁` finite locally free, then the projection
`X ⟶ X/R` to the affine coequalizer is the coequalizer of `p₁` and `p₂` in schemes.

```lean
AlgebraicGeometry.Scheme.Hom.isColimitAffineCoequalizerCofork.{u} {R X : AlgebraicGeometry.Scheme}
  (p₁ p₂ : R ⟶ X) [AlgebraicGeometry.IsAffine X] [CategoryTheory.IsEquivalenceRelation p₁ p₂]
  [AlgebraicGeometry.IsFinite p₁] [AlgebraicGeometry.Flat p₁]
  [AlgebraicGeometry.LocallyOfFinitePresentation p₁] :
  CategoryTheory.Limits.IsColimit
    (CategoryTheory.Limits.Cofork.ofπ (AlgebraicGeometry.Scheme.Hom.affineCoequalizerπ p₁ p₂) ⋯)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cayley–Hamilton on a finite projective module](../../linear-algebra/part-02/other-results/cayley-hamilton-on-a-finite-projective-module.md)

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.Hom.isColimitAffineCoequalizerCofork`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Quotient/EquivalenceRelation.html#AlgebraicGeometry.Scheme.Hom.isColimitAffineCoequalizerCofork).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.Hom.isColimitAffineCoequalizerCofork`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Quotient/EquivalenceRelation.html#AlgebraicGeometry.Scheme.Hom.isColimitAffineCoequalizerCofork)
- [Source of `AlgebraicGeometry.Scheme.Hom.isColimitAffineCoequalizerCofork` in TauCeti/AlgebraicGeometry/Quotient/EquivalenceRelation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Quotient/EquivalenceRelation.lean#L303)
- [Tau Ceti roadmap status: Modular curves and the moduli of elliptic curves with level structure](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ModularCurves/STATUS.md)
