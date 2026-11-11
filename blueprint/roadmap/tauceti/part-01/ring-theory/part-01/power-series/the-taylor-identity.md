---
declaration: theorem
origin: cited
lean: PowerSeries.IsEntire.evalAt_taylor, PowerSeries.IsRestricted.evalAt_taylor, PowerSeries.evalAt_taylor_of_summable, PowerSeries.OnOpenDisc.evalAt_taylor
statement: formalized
proof: formalized
---

# The Taylor identity

For an entire series `f`, the Taylor translate at `a` evaluated at
`b` is `f(b + a)`.

```lean
PowerSeries.IsEntire.evalAt_taylor.{u_1} {R : Type u_1} [NormedCommRing R] {f : PowerSeries R}
  [CompleteSpace R] (hf : f.IsEntire) (a b : R) :
  (PowerSeries.taylor a f).evalAt b = f.evalAt (b + a)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PowerSeries.IsEntire.evalAt_taylor`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Entire/Taylor.html#PowerSeries.IsEntire.evalAt_taylor).

## Other forms

**The Taylor identity for restricted series.** Formalized in Tau Ceti as [`PowerSeries.IsRestricted.evalAt_taylor`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Restricted/Taylor.html#PowerSeries.IsRestricted.evalAt_taylor).

```lean
PowerSeries.IsRestricted.evalAt_taylor.{u_1} {R : Type u_1} [NormedCommRing R] [IsUltrametricDist R]
  {c : ℝ} {f : PowerSeries R} {a b : R} [CompleteSpace R] (hf : PowerSeries.IsRestricted c f)
  (ha : ‖a‖ ≤ c) (hb : ‖b‖ ≤ c) : (PowerSeries.taylor a f).evalAt b = f.evalAt (b + a)
```

**The Taylor identity from the double series.** Formalized in Tau Ceti as [`PowerSeries.evalAt_taylor_of_summable`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Taylor.html#PowerSeries.evalAt_taylor_of_summable).

```lean
PowerSeries.evalAt_taylor_of_summable.{u_1} {R : Type u_1} [CommRing R] [TopologicalSpace R]
  [IsTopologicalRing R] [T2Space R] {f : PowerSeries R} {a b : R}
  (hF :
    Summable fun p => (PowerSeries.coeff p.2) ((PowerSeries.hasseDeriv p.1) f) * a ^ p.2 * b ^ p.1)
  (hrow :
    ∀ (n : ℕ),
      HasSum (fun m => (PowerSeries.coeff m) ((PowerSeries.hasseDeriv n) f) • a ^ m)
        (((PowerSeries.hasseDeriv n) f).evalAt a)) :
  (PowerSeries.taylor a f).evalAt b = f.evalAt (b + a)
```

**The Taylor identity on an open disc at a point of the base ring.** Formalized in Tau Ceti as [`PowerSeries.OnOpenDisc.evalAt_taylor`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/OpenDisc/Taylor.html#PowerSeries.OnOpenDisc.evalAt_taylor).

```lean
PowerSeries.OnOpenDisc.evalAt_taylor.{u_1} {R : Type u_1} [NormedCommRing R] [IsUltrametricDist R]
  {f : PowerSeries R} {R₀ : ℝ} {a : R} [CompleteSpace R] {b : R} (hf : PowerSeries.OnOpenDisc R₀ f)
  (ha : ‖a‖ < R₀) (hb : ‖b‖ < R₀) : (PowerSeries.taylor a f).evalAt b = f.evalAt (b + a)
```

## Sources

- [Tau Ceti documentation: `PowerSeries.IsEntire.evalAt_taylor`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Entire/Taylor.html#PowerSeries.IsEntire.evalAt_taylor)
- [Source of `PowerSeries.IsEntire.evalAt_taylor` in TauCeti/RingTheory/PowerSeries/Entire/Taylor.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/PowerSeries/Entire/Taylor.lean#L111)
