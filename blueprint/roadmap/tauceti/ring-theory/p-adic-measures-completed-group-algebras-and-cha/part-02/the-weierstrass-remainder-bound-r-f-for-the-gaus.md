---
declaration: theorem
origin: cited
lean: TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_weierstrassMod_le
statement: formalized
proof: formalized
---

# The Weierstrass remainder bound `‖r‖ ≤ ‖f‖`, for the Gauss norm at `c`

```lean
TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_weierstrassMod_le.{u_1} {R : Type u_1}
  [NormedCommRing R] [IsUltrametricDist R] {c : ℝ} {s : ℕ}
  {g : ↥(PowerSeries.IsRestricted.subring c)} [CompleteSpace R]
  (hg : TauCeti.PowerSeries.IsMulDistinguished c s ↑g) (hc : 0 < c)
  (f : ↥(PowerSeries.IsRestricted.subring c)) :
  PowerSeries.gaussNorm norm c ↑((hg.weierstrassMod hc) f) ≤ PowerSeries.gaussNorm norm c ↑f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Weierstrass division estimate in several variables](../../mv-power-series/the-weierstrass-division-estimate-in-several-var.md)
- [The Weierstrass norm identity](the-weierstrass-norm-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_weierstrassMod_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.html#TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_weierstrassMod_le).

## Sources

- [Tau Ceti documentation: `TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_weierstrassMod_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.html#TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_weierstrassMod_le)
- [Source of `TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_weierstrassMod_le` in TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.lean#L297)
