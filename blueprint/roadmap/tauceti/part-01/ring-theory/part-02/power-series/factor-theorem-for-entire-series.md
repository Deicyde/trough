---
declaration: theorem
origin: cited
lean: PowerSeries.IsEntire.evalAt_eq_zero_iff
statement: formalized
proof: formalized
---

# Factor theorem for entire series

An entire series vanishes at `a` exactly when it is
`X - a` times an entire series.

```lean
PowerSeries.IsEntire.evalAt_eq_zero_iff.{u_1} {R : Type u_1} [NormedCommRing R] {f : PowerSeries R}
  [CompleteSpace R] (hf : f.IsEntire) {a : R} :
  f.evalAt a = 0 ↔ ∃ q, q.IsEntire ∧ f = (PowerSeries.X - PowerSeries.C a) * q
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PowerSeries.IsEntire.evalAt_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Entire/Division.html#PowerSeries.IsEntire.evalAt_eq_zero_iff).

## Sources

- [Tau Ceti documentation: `PowerSeries.IsEntire.evalAt_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Entire/Division.html#PowerSeries.IsEntire.evalAt_eq_zero_iff)
- [Source of `PowerSeries.IsEntire.evalAt_eq_zero_iff` in TauCeti/RingTheory/PowerSeries/Entire/Division.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/PowerSeries/Entire/Division.lean#L510)
