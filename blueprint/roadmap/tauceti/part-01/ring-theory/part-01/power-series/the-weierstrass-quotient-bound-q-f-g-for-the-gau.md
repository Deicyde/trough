---
declaration: theorem
origin: cited
lean: TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_weierstrassDiv_le
statement: formalized
proof: formalized
---

# The Weierstrass quotient bound `‖q‖ ≤ ‖f‖ / ‖g‖`, for the Gauss norm at `c`

```lean
TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_weierstrassDiv_le.{u_1} {R : Type u_1}
  [NormedCommRing R] [IsUltrametricDist R] {c : ℝ} {s : ℕ}
  {g : ↥(PowerSeries.IsRestricted.subring c)} [CompleteSpace R]
  (hg : TauCeti.PowerSeries.IsMulDistinguished c s ↑g) (hc : 0 < c)
  (f : ↥(PowerSeries.IsRestricted.subring c)) :
  PowerSeries.gaussNorm norm c ↑((hg.weierstrassDiv hc) f) ≤
    PowerSeries.gaussNorm norm c ↑f / PowerSeries.gaussNorm norm c ↑g
```

## Depends on

- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/part-01/tauceti-powerseries-ismuldistinguished.md)

## Proof depends on

- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/part-01/tauceti-isnormmulunit.md)
- [The Weierstrass division estimate for a multiplicatively distinguished divisor](../restricted-power-series-and-tate-algebras/part-01/the-weierstrass-division-estimate-for-a-multipli.md)
- [The Weierstrass norm identity](the-weierstrass-norm-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_weierstrassDiv_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.html#TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_weierstrassDiv_le).

## Sources

- [Tau Ceti documentation: `TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_weierstrassDiv_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.html#TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_weierstrassDiv_le)
- [Source of `TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_weierstrassDiv_le` in TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.lean#L290)
