---
declaration: def
origin: cited
lean: TauCeti.ValuationSpectrum.spaDirectLimitHomeomorph
statement: formalized
---

# The adic spectrum of a directed colimit of Huber pairs is the inverse limit of the adic spectra of the stages

Under the hypotheses of `range_pi_spaComap`, pulling back along the
`φᵢ` is a homeomorphism of `Spa(L, L⁺)` onto the space of compatible families of points of the
`Spa(Aᵢ, Aᵢ⁺)`.

```lean
TauCeti.ValuationSpectrum.spaDirectLimitHomeomorph.{u_1, u_2, u_3} {ι : Type u_1} [Preorder ι]
  {A : ι → Type u_2} [(i : ι) → CommRing (A i)] [(i : ι) → TopologicalSpace (A i)]
  {t : (i j : ι) → i ≤ j → A i →+* A j} {L : Type u_3} [CommRing L] [TopologicalSpace L]
  {φ : (i : ι) → A i →+* L} (Aplus : (i : ι) → Subring (A i)) (Lplus : Subring L)
  (hφc : ∀ (i : ι), Continuous ⇑(φ i)) (hφplus : ∀ (i : ι), ∀ a ∈ Aplus i, (φ i) a ∈ Lplus)
  [IsDirectedOrder ι] (hφt : ∀ (i j : ι) (h : i ≤ j) (a : A i), (φ j) ((t i j h) a) = (φ i) a)
  (hcover : ∀ (x : L), ∃ i a, (φ i) a = x) [∀ (i : ι), ContinuousConstSMul (A i)ᵐᵒᵖ (A i)]
  [SeparatelyContinuousAdd L] (ht : ∀ (i j : ι) (h : i ≤ j), Continuous ⇑(t i j h))
  (htplus : ∀ (i j : ι) (h : i ≤ j), ∀ a ∈ Aplus i, (t i j h) a ∈ Aplus j)
  [DirectedSystem A fun i j h => ⇑(t i j h)]
  (hker : ∀ (i : ι) (a b : A i), (φ i) a = (φ i) b → ∃ j, ∃ (h : i ≤ j), (t i j h) a = (t i j h) b)
  (P : TauCeti.Huber.PairOfDefinition L)
  (hP : ∀ a ∈ P.idealOfDefinition, ∃ i y, IsTopologicallyNilpotent y ∧ (φ i) y = ↑a)
  (hLplus : ∀ x ∈ Lplus, ∃ i, ∃ a ∈ Aplus i, (φ i) a = x) :
  ↑(TauCeti.ValuationSpectrum.spa Lplus) ≃ₜ
    ↑{w |
        ∀ (i j : ι) (h : i ≤ j),
          TauCeti.ValuationSpectrum.spaComap (t i j h) ⋯ (Aplus i) (Aplus j) ⋯ (w j) = w i}
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ValuationSpectrum.spaDirectLimitHomeomorph`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/DirectLimit.html#TauCeti.ValuationSpectrum.spaDirectLimitHomeomorph).

## Sources

- [Tau Ceti documentation: `TauCeti.ValuationSpectrum.spaDirectLimitHomeomorph`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/DirectLimit.html#TauCeti.ValuationSpectrum.spaDirectLimitHomeomorph)
- [Source of `TauCeti.ValuationSpectrum.spaDirectLimitHomeomorph` in TauCeti/AlgebraicGeometry/AdicSpace/Spa/DirectLimit.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/AdicSpace/Spa/DirectLimit.lean#L212)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
