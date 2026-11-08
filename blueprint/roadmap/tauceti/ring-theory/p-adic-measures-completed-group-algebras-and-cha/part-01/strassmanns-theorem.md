---
declaration: theorem
origin: cited
lean: TauCeti.PowerSeries.IsDistinguished.encard_setOf_evalAt_eq_zero_le
statement: formalized
proof: formalized
---

# Strassmann's theorem

Let `f` be a power series over a complete ultrametric normed field
`K`, restricted at a radius `c > 0` and distinguished of degree `s` there, that is, `s` is the
largest index at which the weighted coefficient norm `‖aₙ‖ cⁿ` attains the Gauss norm. Then `f` has
at most `s` zeros of norm at most `c` in any complete normed field extension `L` of `K`.

```lean
TauCeti.PowerSeries.IsDistinguished.encard_setOf_evalAt_eq_zero_le.{u_1, u_2} {K : Type u_1}
  {L : Type u_2} [NormedField K] [IsUltrametricDist K] [CompleteSpace K] [NormedField L]
  [NormedAlgebra K L] [CompleteSpace L] {c : ℝ} {s : ℕ} {f : PowerSeries K}
  (hf : TauCeti.PowerSeries.IsDistinguished c s f) (hc : 0 < c)
  (hfr : PowerSeries.IsRestricted c f) : {x | ‖x‖ ≤ c ∧ f.evalAt x = 0}.encard ≤ ↑s
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Weierstrass preparation (Bosch–Güntzer–Remmert §5.2.2, Theorem 1)](../part-02/weierstrass-preparation-bosch-guntzer-remmert-5.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsDistinguished.encard_setOf_evalAt_eq_zero_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Strassmann.html#TauCeti.PowerSeries.IsDistinguished.encard_setOf_evalAt_eq_zero_le).

## Sources

- [Tau Ceti documentation: `TauCeti.PowerSeries.IsDistinguished.encard_setOf_evalAt_eq_zero_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Strassmann.html#TauCeti.PowerSeries.IsDistinguished.encard_setOf_evalAt_eq_zero_le)
- [Source of `TauCeti.PowerSeries.IsDistinguished.encard_setOf_evalAt_eq_zero_le` in TauCeti/RingTheory/PowerSeries/Weierstrass/Strassmann.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/PowerSeries/Weierstrass/Strassmann.lean#L61)
