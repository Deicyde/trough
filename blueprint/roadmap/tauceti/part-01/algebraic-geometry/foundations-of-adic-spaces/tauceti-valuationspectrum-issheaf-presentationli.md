---
declaration: theorem
origin: cited
lean: TauCeti.ValuationSpectrum.isSheaf_presentationLimitPresheaf_rationalLocalizationPair
statement: formalized
proof: formalized
---

# TauCeti.ValuationSpectrum.isSheaf_presentationLimitPresheaf_rationalLocalizationPair

If `T` spans an open ideal and the structure presheaf of `Spa(A, A⁺)` is a sheaf, then so is the
structure presheaf of `Spa` of the rational localisation `(A⟨T/s⟩, A_U⁺)`, as a pair
(`PairOfDefinition.rationalLocalizationPair`).

```lean
TauCeti.ValuationSpectrum.isSheaf_presentationLimitPresheaf_rationalLocalizationPair.{u}
  {A : Type u} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [TauCeti.Huber.IsHuberRing A]
  (P : TauCeti.Huber.PairOfDefinition A) (U : TauCeti.Huber.Pair A)
  (hP : P.ringOfDefinition ≤ U.plus) (T : Finset A) (s : A) (L : Type u) [CommRing L] [Algebra A L]
  [IsLocalization.Away s L] (hden : P.HasDenominatorPower (↑T) s L) (hT : IsOpen ↑(Ideal.span ↑T))
  (hsheaf :
    CategoryTheory.Presheaf.IsSheaf
      (Opens.grothendieckTopology ↑(TauCeti.ValuationSpectrum.spa U.plus))
      (TauCeti.ValuationSpectrum.presentationLimitPresheaf P U.plus)) :
  CategoryTheory.Presheaf.IsSheaf
    (Opens.grothendieckTopology
      ↑(TauCeti.ValuationSpectrum.spa (P.rationalLocalizationPair U hP T s L hden).plus))
    (TauCeti.ValuationSpectrum.presentationLimitPresheaf (P.completionLocalization (↑T) s L hden)
      (P.rationalLocalizationPair U hP T s L hden).plus)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ValuationSpectrum.isSheaf_presentationLimitPresheaf_rationalLocalizationPair`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/Adic.html#TauCeti.ValuationSpectrum.isSheaf_presentationLimitPresheaf_rationalLocalizationPair).

## Sources

- [Tau Ceti documentation: `TauCeti.ValuationSpectrum.isSheaf_presentationLimitPresheaf_rationalLocalizationPair`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/Adic.html#TauCeti.ValuationSpectrum.isSheaf_presentationLimitPresheaf_rationalLocalizationPair)
- [Source of `TauCeti.ValuationSpectrum.isSheaf_presentationLimitPresheaf_rationalLocalizationPair` in TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/Adic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/Adic.lean#L316)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/AdicSpaces/STATUS.md)
