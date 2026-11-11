---
declaration: def
origin: cited
lean: Module.Grassmannian.hopfIdealLocusEquivClosedSubgroupScheme
statement: formalized
---

# The Hopf-ideal locus classifies subgroup schemes of rank `k`

For a commutative Hopf
algebra `H` over `R` and an `R`-algebra `A`, the points of `G(k, A ⊗[R] H; A)` on the Hopf-ideal
locus correspond to the closed subgroup schemes of `Spec (A ⊗[R] H)` which are finite locally free
of constant rank `k` over `Spec A`. A point `N` goes to `N.subgroupScheme hN`.

```lean
Module.Grassmannian.hopfIdealLocusEquivClosedSubgroupScheme.{u} {R : Type u} [CommRing R] {k : ℕ}
  {A : Type u} [CommRing A] [Algebra R A] {H : Type u} [CommRing H] [HopfAlgebra R H] :
  { N // N.hopfIdealLocus = ⊥ } ≃
    { P //
      AlgebraicGeometry.IsFinite (CategoryTheory.Subobject.underlying.obj ↑P).X.hom ∧
        AlgebraicGeometry.Flat (CategoryTheory.Subobject.underlying.obj ↑P).X.hom ∧
          AlgebraicGeometry.LocallyOfFinitePresentation
              (CategoryTheory.Subobject.underlying.obj ↑P).X.hom ∧
            ∀ (s : ↥(AlgebraicGeometry.Spec ↧A)),
              AlgebraicGeometry.Scheme.Hom.finrank
                  (CategoryTheory.Subobject.underlying.obj ↑P).X.hom s =
                k }
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Module.Grassmannian.hopfIdealLocusEquivClosedSubgroupScheme`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Grassmannian/SubgroupScheme.html#Module.Grassmannian.hopfIdealLocusEquivClosedSubgroupScheme).

## Sources

- [Tau Ceti documentation: `Module.Grassmannian.hopfIdealLocusEquivClosedSubgroupScheme`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Grassmannian/SubgroupScheme.html#Module.Grassmannian.hopfIdealLocusEquivClosedSubgroupScheme)
- [Source of `Module.Grassmannian.hopfIdealLocusEquivClosedSubgroupScheme` in TauCeti/AlgebraicGeometry/Grassmannian/SubgroupScheme.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Grassmannian/SubgroupScheme.lean#L143)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ModularCurves/STATUS.md)
