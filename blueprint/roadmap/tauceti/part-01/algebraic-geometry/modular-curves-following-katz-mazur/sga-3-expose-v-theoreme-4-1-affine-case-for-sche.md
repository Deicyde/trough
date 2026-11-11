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

- [Cayley–Hamilton on a finite projective module](../../linear-algebra/other-results/cayley-hamilton-on-a-finite-projective-module.md)

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.Hom.isColimitAffineCoequalizerCofork`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Quotient/EquivalenceRelation.html#AlgebraicGeometry.Scheme.Hom.isColimitAffineCoequalizerCofork).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.Hom.isColimitAffineCoequalizerCofork`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Quotient/EquivalenceRelation.html#AlgebraicGeometry.Scheme.Hom.isColimitAffineCoequalizerCofork)
- [Source of `AlgebraicGeometry.Scheme.Hom.isColimitAffineCoequalizerCofork` in TauCeti/AlgebraicGeometry/Quotient/EquivalenceRelation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Quotient/EquivalenceRelation.lean#L303)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ModularCurves/STATUS.md)
