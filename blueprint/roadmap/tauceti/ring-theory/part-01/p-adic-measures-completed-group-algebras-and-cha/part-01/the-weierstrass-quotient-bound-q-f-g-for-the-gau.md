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

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](the-weierstrass-division-estimate-bosch-guntzer.md)
- [The Weierstrass norm identity](the-weierstrass-norm-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_weierstrassDiv_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.html#TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_weierstrassDiv_le).

## Sources

- [Tau Ceti documentation: `TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_weierstrassDiv_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.html#TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_weierstrassDiv_le)
- [Source of `TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_weierstrassDiv_le` in TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.lean#L290)
