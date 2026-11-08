---
declaration: theorem
origin: cited
lean: PowerSeries.IsRestricted.norm_evalAt_add_le_max
statement: formalized
proof: formalized
---

# The Taylor remainder estimate

Over a complete ultrametric normed ring, let `f` be
restricted at a radius `c > 0` and let `‖a‖ ≤ c`, `‖y‖ ≤ c`. If `ε` bounds the first `T` terms
`‖(Δᵗ f)(a)‖ ‖y‖ᵗ`, `t < T`, of the expansion of `f` at `a`, then

```text
‖f(y + a)‖ ≤ max ε (‖f‖_c * (‖y‖ / c) ^ T).
```

For `ε = 0` this is the Schwarz lemma at a single zero of order `T`.

```lean
PowerSeries.IsRestricted.norm_evalAt_add_le_max.{u_1} {R : Type u_1} [NormedCommRing R]
  [IsUltrametricDist R] {c : ℝ} {f : PowerSeries R} {a : R} [CompleteSpace R]
  (hf : PowerSeries.IsRestricted c f) (hc : 0 < c) (ha : ‖a‖ ≤ c) {y : R} (hy : ‖y‖ ≤ c) {T : ℕ}
  {ε : ℝ} (h : ∀ t < T, ‖((PowerSeries.hasseDeriv t) f).evalAt a‖ * ‖y‖ ^ t ≤ ε) :
  ‖f.evalAt (y + a)‖ ≤ max ε (PowerSeries.gaussNorm norm c f * (‖y‖ / c) ^ T)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Taylor identity](../../analysis/part-01/compact-operators-and-nonarchimedean-fredholm-th/the-taylor-identity.md)

## Lean

Formalized in Tau Ceti as [`PowerSeries.IsRestricted.norm_evalAt_add_le_max`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Restricted/Taylor.html#PowerSeries.IsRestricted.norm_evalAt_add_le_max).

## Sources

- [Tau Ceti documentation: `PowerSeries.IsRestricted.norm_evalAt_add_le_max`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Restricted/Taylor.html#PowerSeries.IsRestricted.norm_evalAt_add_le_max)
- [Source of `PowerSeries.IsRestricted.norm_evalAt_add_le_max` in TauCeti/RingTheory/PowerSeries/Restricted/Taylor.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/PowerSeries/Restricted/Taylor.lean#L198)
