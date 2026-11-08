---
declaration: theorem
origin: cited
lean: IsDedekindDomain.HeightOneSpectrum.multiplicity_differentIdeal_eq_finsum_card_ramificationGroup_sub_one, TauCeti.differentExponent_eq_finsum_lowerRamificationGroup, TauCeti.differentExponent_eq_sum_range_lowerRamificationGroup, TauCeti.sum_range_card_lowerRamificationGroup_sub_one_le_differentExponent
statement: formalized
proof: formalized
---

# Hilbert's formula for a number-field different exponent

For a finite Galois extension
`L/K`, the multiplicity of a prime `w` in the global different is the sum of the orders of the
nonnegative-index lower ramification groups, minus one in each degree.

```lean
IsDedekindDomain.HeightOneSpectrum.multiplicity_differentIdeal_eq_finsum_card_ramificationGroup_sub_one.{u_1,
    u_2}
  {K : Type u_1} {L : Type u_2} [Field K] [NumberField K] [Field L] [NumberField L] [Algebra K L]
  (w : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers L)) [IsGalois K L] :
  multiplicity w.asIdeal
      (differentIdeal (NumberField.RingOfIntegers K) (NumberField.RingOfIntegers L)) =
    ∑ᶠ (i : ℕ), (Nat.card ↥(Ideal.ramificationGroup Gal(L/K) w.asIdeal i) - 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hilbert's counting identity](../../../ring-theory/local-ring/hilberts-counting-identity.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`IsDedekindDomain.HeightOneSpectrum.multiplicity_differentIdeal_eq_finsum_card_ramificationGroup_sub_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/LocalGlobal/Different/Exponent.html#IsDedekindDomain.HeightOneSpectrum.multiplicity_differentIdeal_eq_finsum_card_ramificationGroup_sub_one).

## Other forms

**Hilbert's formula for the different exponent.** Formalized in Tau Ceti as [`TauCeti.differentExponent_eq_finsum_lowerRamificationGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Different/Hilbert.html#TauCeti.differentExponent_eq_finsum_lowerRamificationGroup).

```lean
TauCeti.differentExponent_eq_finsum_lowerRamificationGroup.{u_1, u_2} (K : Type u_1) (L : Type u_2)
  [Field K] [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] [Field L]
  [ValuativeRel L] [TopologicalSpace L] [IsNonarchimedeanLocalField L] [Algebra K L]
  [ValuativeExtension K L] [Module.Finite K L] [IsGalois K L] :
  TauCeti.differentExponent K L =
    ∑ᶠ (i : ℕ), (Nat.card ↥(TauCeti.LocalFieldsRamification.lowerRamificationGroup K L ↑i) - 1)
```

**Hilbert's formula, as a finite sum.** Formalized in Tau Ceti as [`TauCeti.differentExponent_eq_sum_range_lowerRamificationGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Different/Hilbert.html#TauCeti.differentExponent_eq_sum_range_lowerRamificationGroup).

```lean
TauCeti.differentExponent_eq_sum_range_lowerRamificationGroup.{u_1, u_2} (K : Type u_1)
  (L : Type u_2) [Field K] [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K]
  [Field L] [ValuativeRel L] [TopologicalSpace L] [IsNonarchimedeanLocalField L] [Algebra K L]
  [ValuativeExtension K L] [Module.Finite K L] [IsGalois K L] {N : ℕ}
  (hN : TauCeti.LocalFieldsRamification.lowerRamificationGroup K L ↑N = ⊥) :
  TauCeti.differentExponent K L =
    ∑ i ∈ Finset.range N,
      (Nat.card ↥(TauCeti.LocalFieldsRamification.lowerRamificationGroup K L ↑i) - 1)
```

**Hilbert's formula, truncated.** Formalized in Tau Ceti as [`TauCeti.sum_range_card_lowerRamificationGroup_sub_one_le_differentExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Different/Hilbert.html#TauCeti.sum_range_card_lowerRamificationGroup_sub_one_le_differentExponent).

```lean
TauCeti.sum_range_card_lowerRamificationGroup_sub_one_le_differentExponent.{u_1, u_2} (K : Type u_1)
  (L : Type u_2) [Field K] [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K]
  [Field L] [ValuativeRel L] [TopologicalSpace L] [IsNonarchimedeanLocalField L] [Algebra K L]
  [ValuativeExtension K L] [Module.Finite K L] [IsGalois K L] (m : ℕ) :
  ∑ i ∈ Finset.range m,
      (Nat.card ↥(TauCeti.LocalFieldsRamification.lowerRamificationGroup K L ↑i) - 1) ≤
    TauCeti.differentExponent K L
```

## Sources

- [Tau Ceti documentation: `IsDedekindDomain.HeightOneSpectrum.multiplicity_differentIdeal_eq_finsum_card_ramificationGroup_sub_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/LocalGlobal/Different/Exponent.html#IsDedekindDomain.HeightOneSpectrum.multiplicity_differentIdeal_eq_finsum_card_ramificationGroup_sub_one)
- [Source of `IsDedekindDomain.HeightOneSpectrum.multiplicity_differentIdeal_eq_finsum_card_ramificationGroup_sub_one` in TauCeti/NumberTheory/NumberField/LocalGlobal/Different/Exponent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/LocalGlobal/Different/Exponent.lean#L236)
- [Tau Ceti roadmap status: Number fields, ramification, Frobenius, and the LMFDB invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/NumberFieldArithmetic/STATUS.md)
