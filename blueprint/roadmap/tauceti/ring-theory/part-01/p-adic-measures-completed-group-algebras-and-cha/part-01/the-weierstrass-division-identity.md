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

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](the-weierstrass-division-estimate-bosch-guntzer.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsMulDistinguished.mul_weierstrassDiv_add_weierstrassMod`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.html#TauCeti.PowerSeries.IsMulDistinguished.mul_weierstrassDiv_add_weierstrassMod).

## Sources

- [Tau Ceti documentation: `TauCeti.PowerSeries.IsMulDistinguished.mul_weierstrassDiv_add_weierstrassMod`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.html#TauCeti.PowerSeries.IsMulDistinguished.mul_weierstrassDiv_add_weierstrassMod)
- [Source of `TauCeti.PowerSeries.IsMulDistinguished.mul_weierstrassDiv_add_weierstrassMod` in TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/PowerSeries/Weierstrass/DivMod.lean#L188)
