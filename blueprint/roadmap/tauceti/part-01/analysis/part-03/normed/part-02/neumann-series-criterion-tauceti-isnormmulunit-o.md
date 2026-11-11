---
declaration: theorem
origin: cited
lean: TauCeti.IsNormMulUnit.of_norm_sub_lt
statement: formalized
proof: formalized
---

# Neumann series criterion (`TauCeti.IsNormMulUnit.of_norm_sub_lt`)

In an ultrametric ring with summable geometric series,
an element whose distance from a multiplicative unit `u` is less than `‖u‖` is a multiplicative
unit.

```lean
TauCeti.IsNormMulUnit.of_norm_sub_lt.{u_1} {A : Type u_1} [NormedRing A] [HasSummableGeomSeries A]
  [IsUltrametricDist A] {u f : A} (hu : TauCeti.IsNormMulUnit u) (hf : ‖f - u‖ < ‖u‖) :
  TauCeti.IsNormMulUnit f
```

## Depends on

- [TauCeti.IsNormMulUnit](../../../../ring-theory/part-01/restricted-power-series-and-tate-algebras/part-01/tauceti-isnormmulunit.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsNormMulUnit.of_norm_sub_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Ring/MulUnit.html#TauCeti.IsNormMulUnit.of_norm_sub_lt).

## Sources

- [Tau Ceti documentation: `TauCeti.IsNormMulUnit.of_norm_sub_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Ring/MulUnit.html#TauCeti.IsNormMulUnit.of_norm_sub_lt)
- [Source of `TauCeti.IsNormMulUnit.of_norm_sub_lt` in TauCeti/Analysis/Normed/Ring/MulUnit.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Ring/MulUnit.lean#L124)
