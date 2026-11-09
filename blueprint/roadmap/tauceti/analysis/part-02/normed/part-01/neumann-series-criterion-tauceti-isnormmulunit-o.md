---
declaration: theorem
origin: cited
lean: TauCeti.IsNormMulUnit.of_norm_sub_lt
statement: formalized
proof: formalized
---

# Neumann series criterion (`TauCeti.IsNormMulUnit.of_norm_sub_lt`)

In an ultrametric norm-one ring with summable geometric series,
an element whose distance from a multiplicative unit `u` is less than `‖u‖` is a multiplicative
unit.

```lean
TauCeti.IsNormMulUnit.of_norm_sub_lt.{u_1} {A : Type u_1} [NormedRing A] [NormOneClass A]
  [HasSummableGeomSeries A] [IsUltrametricDist A] {u f : A} (hu : TauCeti.IsNormMulUnit u)
  (hf : ‖f - u‖ < ‖u‖) : TauCeti.IsNormMulUnit f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsNormMulUnit.of_norm_sub_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Ring/MulUnit.html#TauCeti.IsNormMulUnit.of_norm_sub_lt).

## Sources

- [Tau Ceti documentation: `TauCeti.IsNormMulUnit.of_norm_sub_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Ring/MulUnit.html#TauCeti.IsNormMulUnit.of_norm_sub_lt)
- [Source of `TauCeti.IsNormMulUnit.of_norm_sub_lt` in TauCeti/Analysis/Normed/Ring/MulUnit.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Ring/MulUnit.lean#L119)
