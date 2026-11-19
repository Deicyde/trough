---
declaration: theorem
origin: cited
lean: TauCeti.PowerSeries.IsDistinguished.encard_setOf_evalAt_eq_zero_le, TauCeti.PowerSeries.IsDistinguished.sum_le_of_isGoodZero
statement: formalized
proof: formalized
---

# Strassmann's theorem

Let `f` be a power series over an ultrametric normed field
`K`, restricted at a radius `c` and distinguished of degree `s` there, that is, `s` is the
largest index at which the weighted coefficient norm `‖aₙ‖ cⁿ` attains the Gauss norm. Then `f` has
at most `s` zeros of norm at most `c` in any complete normed field extension `L` of `K`. For
`c ≤ 0` there are none.

```lean
TauCeti.PowerSeries.IsDistinguished.encard_setOf_evalAt_eq_zero_le.{u_1, u_2} {K : Type u_1}
  {L : Type u_2} [NormedField K] [IsUltrametricDist K] [NormedField L] [NormedAlgebra K L]
  [CompleteSpace L] {c : ℝ} {s : ℕ} {f : PowerSeries K}
  (hf : TauCeti.PowerSeries.IsDistinguished c s f) (hfr : PowerSeries.IsRestricted c f) :
  {x | ‖x‖ ≤ c ∧ f.evalAt x = 0}.encard ≤ ↑s
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Weierstrass preparation](../../part-02/power-series/weierstrass-preparation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsDistinguished.encard_setOf_evalAt_eq_zero_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Strassmann.html#TauCeti.PowerSeries.IsDistinguished.encard_setOf_evalAt_eq_zero_le).

## Other forms

**Strassmann's theorem with multiplicities.** Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsDistinguished.sum_le_of_isGoodZero`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Strassmann.html#TauCeti.PowerSeries.IsDistinguished.sum_le_of_isGoodZero).

```lean
TauCeti.PowerSeries.IsDistinguished.sum_le_of_isGoodZero.{u_1} {K : Type u_1} [NormedField K]
  [IsUltrametricDist K] {c : ℝ} {s : ℕ} {f : PowerSeries K} [CompleteSpace K]
  (hfd : TauCeti.PowerSeries.IsDistinguished c s f) (hfr : PowerSeries.IsRestricted c f)
  {S : Finset K} {h : K → ℕ} (hS : ∀ a ∈ S, ‖a‖ ≤ c ∧ f.IsGoodZero a (h a)) : ∑ a ∈ S, h a ≤ s
```

## Sources

- [Tau Ceti documentation: `TauCeti.PowerSeries.IsDistinguished.encard_setOf_evalAt_eq_zero_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Strassmann.html#TauCeti.PowerSeries.IsDistinguished.encard_setOf_evalAt_eq_zero_le)
- [Source of `TauCeti.PowerSeries.IsDistinguished.encard_setOf_evalAt_eq_zero_le` in TauCeti/RingTheory/PowerSeries/Weierstrass/Strassmann.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/PowerSeries/Weierstrass/Strassmann.lean#L159)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
