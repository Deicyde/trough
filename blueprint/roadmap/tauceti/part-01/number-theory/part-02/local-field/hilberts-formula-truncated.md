---
declaration: theorem
origin: cited
lean: TauCeti.sum_range_card_lowerRamificationGroup_sub_one_le_differentExponent, TauCeti.differentExponent_eq_finsum_lowerRamificationGroup, TauCeti.differentExponent_eq_sum_range_lowerRamificationGroup
statement: formalized
proof: formalized
---

# Hilbert's formula, truncated

for a finite Galois extension `L/K` of nonarchimedean local
fields, `∑_{i < m} (#G_i - 1) ≤ d(L/K)` for every `m`.

```lean
TauCeti.sum_range_card_lowerRamificationGroup_sub_one_le_differentExponent.{u_1, u_2} (K : Type u_1)
  (L : Type u_2) [Field K] [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K]
  [Field L] [ValuativeRel L] [TopologicalSpace L] [IsNonarchimedeanLocalField L] [Algebra K L]
  [ValuativeExtension K L] [Module.Finite K L] [IsGalois K L] (m : ℕ) :
  ∑ i ∈ Finset.range m,
      (Nat.card ↥(TauCeti.LocalFieldsRamification.lowerRamificationGroup K L ↑i) - 1) ≤
    TauCeti.differentExponent K L
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hilbert's counting identity](../../../ring-theory/part-01/local-ring/hilberts-counting-identity.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_range_card_lowerRamificationGroup_sub_one_le_differentExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Different/Hilbert.html#TauCeti.sum_range_card_lowerRamificationGroup_sub_one_le_differentExponent).

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

## Sources

- [Tau Ceti documentation: `TauCeti.sum_range_card_lowerRamificationGroup_sub_one_le_differentExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Different/Hilbert.html#TauCeti.sum_range_card_lowerRamificationGroup_sub_one_le_differentExponent)
- [Source of `TauCeti.sum_range_card_lowerRamificationGroup_sub_one_le_differentExponent` in TauCeti/NumberTheory/LocalField/Different/Hilbert.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/Different/Hilbert.lean#L119)
