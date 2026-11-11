---
declaration: theorem
origin: cited
lean: TauCeti.ValuationSpectrum.isOpenImmersion_presentationLimitPreAdicSpaceComap_toCompletionLocHom
statement: formalized
proof: formalized
---

# The structure morphism of a rational localisation pair induces an open immersion

the
morphism `Spa(A⟨T/s⟩, A_U⁺) ⟶ Spa(A, A⁺)` induced by `(A, A⁺) → (A⟨T/s⟩, A_U⁺)` is an open
immersion, when `T` spans an open ideal and the structure presheaf of `Spa(A⟨T/s⟩, A_U⁺)` is a
sheaf. This is `isOpenImmersion_presentationLimitPreAdicSpaceComap_toCompletionLoc` for the
morphism of Huber pairs `TauCeti.Huber.PairOfDefinition.toCompletionLocHom`.

```lean
TauCeti.ValuationSpectrum.isOpenImmersion_presentationLimitPreAdicSpaceComap_toCompletionLocHom.{u}
  {A : Type u} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [TauCeti.Huber.IsHuberRing A]
  {U : TauCeti.Huber.Pair A} (P : TauCeti.Huber.PairOfDefinition A)
  (hP : P.ringOfDefinition ≤ U.plus) (T : Finset A) (s : A) (L : Type u) [CommRing L] [Algebra A L]
  [IsLocalization.Away s L] (hden : P.HasDenominatorPower (↑T) s L) (hT : IsOpen ↑(Ideal.span ↑T))
  (hsheafU :
    CategoryTheory.Presheaf.IsSheaf
      (Opens.grothendieckTopology
        ↑(TauCeti.ValuationSpectrum.spa (P.rationalLocalizationPair U hP T s L hden).plus))
      (TauCeti.ValuationSpectrum.presentationLimitPresheaf (P.completionLocalization (↑T) s L hden)
        (P.rationalLocalizationPair U hP T s L hden).plus)) :
  TauCeti.PreAdicSpace.IsOpenImmersion
    (TauCeti.ValuationSpectrum.presentationLimitPreAdicSpaceComap
      (P.toCompletionLocHom U hP T s L hden).toRingHom ⋯ ⋯ ⋯ ⋯ hP ⋯ hsheafU)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Ideals contained in supports](ideals-contained-in-supports.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ValuationSpectrum.isOpenImmersion_presentationLimitPreAdicSpaceComap_toCompletionLocHom`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/RationalOpen.html#TauCeti.ValuationSpectrum.isOpenImmersion_presentationLimitPreAdicSpaceComap_toCompletionLocHom).

## Sources

- [Tau Ceti documentation: `TauCeti.ValuationSpectrum.isOpenImmersion_presentationLimitPreAdicSpaceComap_toCompletionLocHom`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/RationalOpen.html#TauCeti.ValuationSpectrum.isOpenImmersion_presentationLimitPreAdicSpaceComap_toCompletionLocHom)
- [Source of `TauCeti.ValuationSpectrum.isOpenImmersion_presentationLimitPreAdicSpaceComap_toCompletionLocHom` in TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/RationalOpen.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/RationalOpen.lean#L933)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AdicSpaces/STATUS.md)
