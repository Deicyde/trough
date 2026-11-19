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
- [Source of `Module.Grassmannian.hopfIdealLocusEquivClosedSubgroupScheme` in TauCeti/AlgebraicGeometry/Grassmannian/SubgroupScheme.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Grassmannian/SubgroupScheme.lean#L143)
- [Tau Ceti roadmap status: Modular curves and the moduli of elliptic curves with level structure](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ModularCurves/STATUS.md)
