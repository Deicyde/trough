---
declaration: theorem
origin: cited
lean: TauCeti.norm_inverse_one_sub, TauCeti.norm_inverse_one_sub_sub_one
statement: formalized
proof: formalized
---

# Ultrametric Neumann estimate

In a normed ring with `‖1‖ = 1`, convergent geometric
series and an ultrametric norm, the inverse of `1 - x` has norm one whenever `‖x‖ < 1`.

```lean
TauCeti.norm_inverse_one_sub.{u_1} {R : Type u_1} [NormedRing R] [NormOneClass R]
  [HasSummableGeomSeries R] [IsUltrametricDist R] {x : R} (hx : ‖x‖ < 1) :
  ‖Ring.inverse (1 - x)‖ = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.IsNormMulUnit](../../../../ring-theory/part-01/restricted-power-series-and-tate-algebras/part-01/tauceti-isnormmulunit.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.norm_inverse_one_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Ring/UnitBall.html#TauCeti.norm_inverse_one_sub).

## Other forms

**Ultrametric Neumann estimate.** Formalized in Tau Ceti as [`TauCeti.norm_inverse_one_sub_sub_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Ring/UnitBall.html#TauCeti.norm_inverse_one_sub_sub_one).

```lean
TauCeti.norm_inverse_one_sub_sub_one.{u_1} {R : Type u_1} [NormedRing R] [HasSummableGeomSeries R]
  [IsUltrametricDist R] {x : R} (hx : ‖x‖ < 1) : ‖Ring.inverse (1 - x) - 1‖ = ‖x‖
```

## Sources

- [Tau Ceti documentation: `TauCeti.norm_inverse_one_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Ring/UnitBall.html#TauCeti.norm_inverse_one_sub)
- [Source of `TauCeti.norm_inverse_one_sub` in TauCeti/Analysis/Normed/Ring/UnitBall.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Ring/UnitBall.lean#L157)
