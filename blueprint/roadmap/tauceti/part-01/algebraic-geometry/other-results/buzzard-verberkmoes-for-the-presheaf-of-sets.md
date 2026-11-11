---
declaration: theorem
origin: cited
lean: TauCeti.ValuationSpectrum.isSheaf_underlying_presentationLimitPresheaf_of_isStablyUniform, TauCeti.ValuationSpectrum.isSheaf_presentationLimitPresheaf_of_isStablyUniform
statement: formalized
proof: formalized
---

# Buzzard–Verberkmoes for the presheaf of sets

Let `A` be a stably uniform Tate ring, `P` a
pair of definition whose ring of definition lies in `A⁺`, and `A⁺` a subring of power-bounded
elements. The presheaf of sets underlying the presentation-limit structure presheaf of
`Spa(A, A⁺)` is a sheaf on all opens. The ring need not be complete or Hausdorff.

```lean
TauCeti.ValuationSpectrum.isSheaf_underlying_presentationLimitPresheaf_of_isStablyUniform.{v}
  {A : Type v} [CommRing A] [UniformSpace A] [IsTopologicalRing A] [TauCeti.Huber.IsTateRing A]
  [TauCeti.Huber.IsStablyUniform A] (P : TauCeti.Huber.PairOfDefinition A) {Aplus : Subring A}
  (hP : P.ringOfDefinition ≤ Aplus)
  (hAplus : ∀ ⦃a : A⦄, a ∈ Aplus → TauCeti.Huber.IsPowerBounded a) :
  CategoryTheory.Presheaf.IsSheaf
    (Opens.grothendieckTopology ↑(TauCeti.ValuationSpectrum.spa Aplus))
    ((TauCeti.ValuationSpectrum.presentationLimitPresheaf P Aplus).comp
      (TauCeti.TopCommRingCat.isCompleteSeparated.ι.comp (CategoryTheory.forget TopCommRingCat)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Ideals contained in supports](../foundations-of-adic-spaces/ideals-contained-in-supports.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ValuationSpectrum.isSheaf_underlying_presentationLimitPresheaf_of_isStablyUniform`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/StructurePresheaf/Rational/StableUniform.html#TauCeti.ValuationSpectrum.isSheaf_underlying_presentationLimitPresheaf_of_isStablyUniform).

## Other forms

**Buzzard–Verberkmoes: stably uniform Tate pairs are sheafy.** Formalized in Tau Ceti as [`TauCeti.ValuationSpectrum.isSheaf_presentationLimitPresheaf_of_isStablyUniform`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/StructurePresheaf/Rational/StableUniform.html#TauCeti.ValuationSpectrum.isSheaf_presentationLimitPresheaf_of_isStablyUniform).

```lean
TauCeti.ValuationSpectrum.isSheaf_presentationLimitPresheaf_of_isStablyUniform.{v} {A : Type v}
  [CommRing A] [UniformSpace A] [IsTopologicalRing A] [TauCeti.Huber.IsTateRing A]
  [TauCeti.Huber.IsStablyUniform A] (P : TauCeti.Huber.PairOfDefinition A) {Aplus : Subring A}
  (hP : P.ringOfDefinition ≤ Aplus)
  (hAplus : ∀ ⦃a : A⦄, a ∈ Aplus → TauCeti.Huber.IsPowerBounded a) :
  CategoryTheory.Presheaf.IsSheaf
    (Opens.grothendieckTopology ↑(TauCeti.ValuationSpectrum.spa Aplus))
    (TauCeti.ValuationSpectrum.presentationLimitPresheaf P Aplus)
```

## Sources

- [Tau Ceti documentation: `TauCeti.ValuationSpectrum.isSheaf_underlying_presentationLimitPresheaf_of_isStablyUniform`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/StructurePresheaf/Rational/StableUniform.html#TauCeti.ValuationSpectrum.isSheaf_underlying_presentationLimitPresheaf_of_isStablyUniform)
- [Source of `TauCeti.ValuationSpectrum.isSheaf_underlying_presentationLimitPresheaf_of_isStablyUniform` in TauCeti/AlgebraicGeometry/AdicSpace/Spa/StructurePresheaf/Rational/StableUniform.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/AdicSpace/Spa/StructurePresheaf/Rational/StableUniform.lean#L78)
