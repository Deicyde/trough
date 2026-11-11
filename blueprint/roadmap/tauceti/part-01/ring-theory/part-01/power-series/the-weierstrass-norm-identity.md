---
declaration: theorem
origin: cited
lean: TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_eq_max
statement: formalized
proof: formalized
---

# The Weierstrass norm identity

The Gauss norm of `f` at `c` is the larger of
`‖g‖ * ‖q‖` and `‖r‖`, for its Weierstrass quotient `q` and remainder `r`.

```lean
TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_eq_max.{u_1} {R : Type u_1} [NormedCommRing R]
  [IsUltrametricDist R] {c : ℝ} {s : ℕ} {g : ↥(PowerSeries.IsRestricted.subring c)}
  [CompleteSpace R] (hg : TauCeti.PowerSeries.IsMulDistinguished c s ↑g) (hc : 0 < c)
  (f : ↥(PowerSeries.IsRestricted.subring c)) :
  PowerSeries.gaussNorm norm c ↑f =
    max (PowerSeries.gaussNorm norm c ↑g * PowerSeries.gaussNorm norm c ↑((hg.weierstrassDiv hc) f))
      (PowerSeries.gaussNorm norm c ↑((hg.weierstrassMod hc) f))
```

## Depends on

- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/part-01/tauceti-powerseries-ismuldistinguished.md)

## Proof depends on

- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/part-01/tauceti-isnormmulunit.md)
- [The Weierstrass division estimate for a multiplicatively distinguished divisor](../restricted-power-series-and-tate-algebras/part-01/the-weierstrass-division-estimate-for-a-multipli.md)
- [The Weierstrass division identity](the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_eq_max`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.html#TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_eq_max).

## Sources

- [Tau Ceti documentation: `TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_eq_max`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.html#TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_eq_max)
- [Source of `TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_eq_max` in TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.lean#L279)
