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

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](the-weierstrass-division-estimate-bosch-guntzer.md)
- [The Weierstrass division identity](the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_eq_max`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.html#TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_eq_max).

## Sources

- [Tau Ceti documentation: `TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_eq_max`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.html#TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_eq_max)
- [Source of `TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_eq_max` in TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.lean#L279)
