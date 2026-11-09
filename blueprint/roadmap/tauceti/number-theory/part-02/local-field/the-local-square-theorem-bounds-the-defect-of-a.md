---
declaration: theorem
origin: cited
lean: TauCeti.defectExponent_le_two_mul_natCastValuation
statement: formalized
proof: formalized
---

# The local square theorem bounds the defect of a unit

A unit of `𝒪[K]` approximated by a
square to order `2 v_K(2) + 1` is a square, so the defect exponent of a nonsquare unit is at most
`2 v_K(2)`. In odd residue characteristic the bound is `0`.

```lean
TauCeti.defectExponent_le_two_mul_natCastValuation.{u_1} {K : Type u_1} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] (h2 : 2 ≠ 0) {u : Kˣ}
  (hu : (ValuativeRel.valuation K) ↑u = 1) (hsq : ¬IsSquare u) :
  TauCeti.defectExponent u ≤ ↑↑(2 * TauCeti.natCastValuation K 2 h2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.defectExponent_le_two_mul_natCastValuation`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/Defect/Basic.html#TauCeti.defectExponent_le_two_mul_natCastValuation).

## Sources

- [Tau Ceti documentation: `TauCeti.defectExponent_le_two_mul_natCastValuation`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/Defect/Basic.html#TauCeti.defectExponent_le_two_mul_natCastValuation)
- [Source of `TauCeti.defectExponent_le_two_mul_natCastValuation` in TauCeti/NumberTheory/LocalField/QuadraticForm/Defect/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/QuadraticForm/Defect/Basic.lean#L475)
