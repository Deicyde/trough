---
declaration: theorem
origin: cited
lean: TauCeti.ValuationSpectrum.exists_spaComap_preimage_rationalSubset
statement: formalized
proof: formalized
---

# Rational subsets of the adic spectrum of a colimit come from a finite stage

For finite
`T ⊆ L` and `s ∈ L`, there are a stage `i`, a finite `T' ⊆ Aᵢ` and `s' ∈ Aᵢ` such that the
rational subset `R(T/s)` of `Spa(L, L⁺)` is the preimage of `R(T'/s')` under
`Spa(L, L⁺) → Spa(Aᵢ, Aᵢ⁺)`. If `T` generates the unit ideal of `L`, then `T'` can be chosen to
generate the unit ideal of `Aᵢ`.

```lean
TauCeti.ValuationSpectrum.exists_spaComap_preimage_rationalSubset.{u_1, u_2, u_3} {ι : Type u_1}
  [Preorder ι] {A : ι → Type u_2} [(i : ι) → CommRing (A i)] [(i : ι) → TopologicalSpace (A i)]
  {t : (i j : ι) → i ≤ j → A i →+* A j} {L : Type u_3} [CommRing L] [TopologicalSpace L]
  {φ : (i : ι) → A i →+* L} [IsDirectedOrder ι]
  (hφt : ∀ (i j : ι) (h : i ≤ j) (a : A i), (φ j) ((t i j h) a) = (φ i) a)
  (hcover : ∀ (x : L), ∃ i a, (φ i) a = x)
  (hker : ∀ (i : ι) (a b : A i), (φ i) a = (φ i) b → ∃ j, ∃ (h : i ≤ j), (t i j h) a = (t i j h) b)
  (Aplus : (i : ι) → Subring (A i)) (Lplus : Subring L) (hφc : ∀ (i : ι), Continuous ⇑(φ i))
  (hφplus : ∀ (i : ι), ∀ a ∈ Aplus i, (φ i) a ∈ Lplus) (T : Finset L) (s : L) :
  ∃ i T' s',
    (Ideal.span ↑T = ⊤ → Ideal.span ↑T' = ⊤) ∧
      Subtype.val ⁻¹' TauCeti.ValuationSpectrum.rationalSubset Lplus T s =
        TauCeti.ValuationSpectrum.spaComap (φ i) ⋯ (Aplus i) Lplus ⋯ ⁻¹'
          Subtype.val ⁻¹' TauCeti.ValuationSpectrum.rationalSubset (Aplus i) T' s'
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ValuationSpectrum.exists_spaComap_preimage_rationalSubset`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/DirectLimit.html#TauCeti.ValuationSpectrum.exists_spaComap_preimage_rationalSubset).

## Sources

- [Tau Ceti documentation: `TauCeti.ValuationSpectrum.exists_spaComap_preimage_rationalSubset`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/DirectLimit.html#TauCeti.ValuationSpectrum.exists_spaComap_preimage_rationalSubset)
- [Source of `TauCeti.ValuationSpectrum.exists_spaComap_preimage_rationalSubset` in TauCeti/AlgebraicGeometry/AdicSpace/Spa/DirectLimit.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/AdicSpace/Spa/DirectLimit.lean#L252)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
