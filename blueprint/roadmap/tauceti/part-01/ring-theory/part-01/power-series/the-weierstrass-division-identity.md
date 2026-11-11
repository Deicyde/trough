---
declaration: theorem
origin: cited
lean: TauCeti.PowerSeries.IsMulDistinguished.mul_weierstrassDiv_add_weierstrassMod
statement: formalized
proof: formalized
---

# The Weierstrass division identity

`f = g * q + r` for the Weierstrass quotient `q` and
remainder `r` of `f`.

```lean
TauCeti.PowerSeries.IsMulDistinguished.mul_weierstrassDiv_add_weierstrassMod.{u_1} {R : Type u_1}
  [NormedCommRing R] [IsUltrametricDist R] {c : ℝ} {s : ℕ}
  {g : ↥(PowerSeries.IsRestricted.subring c)} [CompleteSpace R]
  (hg : TauCeti.PowerSeries.IsMulDistinguished c s ↑g) (hc : 0 < c)
  (f : ↥(PowerSeries.IsRestricted.subring c)) :
  g * (hg.weierstrassDiv hc) f +
      (TauCeti.PowerSeries.polynomialToRestricted c) ((hg.weierstrassMod hc) f) =
    f
```

## Depends on

- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/part-01/tauceti-powerseries-ismuldistinguished.md)

## Proof depends on

- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/part-01/tauceti-isnormmulunit.md)
- [The Weierstrass division estimate for a multiplicatively distinguished divisor](../restricted-power-series-and-tate-algebras/part-01/the-weierstrass-division-estimate-for-a-multipli.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsMulDistinguished.mul_weierstrassDiv_add_weierstrassMod`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.html#TauCeti.PowerSeries.IsMulDistinguished.mul_weierstrassDiv_add_weierstrassMod).

## Sources

- [Tau Ceti documentation: `TauCeti.PowerSeries.IsMulDistinguished.mul_weierstrassDiv_add_weierstrassMod`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.html#TauCeti.PowerSeries.IsMulDistinguished.mul_weierstrassDiv_add_weierstrassMod)
- [Source of `TauCeti.PowerSeries.IsMulDistinguished.mul_weierstrassDiv_add_weierstrassMod` in TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.lean#L188)
