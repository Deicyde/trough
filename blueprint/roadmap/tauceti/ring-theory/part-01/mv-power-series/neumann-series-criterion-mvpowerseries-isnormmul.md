---
declaration: theorem
origin: cited
lean: MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt
statement: formalized
proof: formalized
---

# Neumann series criterion (`MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt`)

Over a complete ultrametric norm-one ring, a restricted series
whose distance from a constant multiplicative unit `a` is less than `‖a‖` is a multiplicative
unit.

```lean
MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt.{u_1, u_2} {σ : Type u_1} {R : Type u_2} [NormedRing R]
  [IsUltrametricDist R] {c : σ → ℝ} [∀ (i : σ), Fact (0 < c i)] [NormOneClass R] [CompleteSpace R]
  {a : R} (ha : TauCeti.IsNormMulUnit a) {f : ↥(MvPowerSeries.IsRestricted.subring c)}
  (hf : ‖f - ⟨MvPowerSeries.C a, ⋯⟩‖ < ‖a‖) : TauCeti.IsNormMulUnit f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Neumann series criterion (`TauCeti.IsNormMulUnit.of_norm_sub_lt`)](../../../analysis/part-02/normed/part-01/neumann-series-criterion-tauceti-isnormmulunit-o.md)

## Lean

Formalized in Tau Ceti as [`MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Units.html#MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt).

## Sources

- [Tau Ceti documentation: `MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Units.html#MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt)
- [Source of `MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt` in TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Units.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Units.lean#L93)
