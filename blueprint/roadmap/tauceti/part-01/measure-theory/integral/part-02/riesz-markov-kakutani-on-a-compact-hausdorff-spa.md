---
declaration: theorem
origin: cited
lean: LinearMap.exists_regular_integral_eq
statement: formalized
proof: formalized
---

# Riesz–Markov–Kakutani on a compact Hausdorff space

a linear functional on `C(X, ℝ)`
that is nonnegative on nonnegative functions is integration against a regular measure.

```lean
LinearMap.exists_regular_integral_eq.{u_1} {X : Type u_1} [TopologicalSpace X] [CompactSpace X]
  [T2Space X] [MeasurableSpace X] [BorelSpace X] (L : C(X, ℝ) →ₗ[ℝ] ℝ)
  (hL : ∀ (h : C(X, ℝ)), 0 ≤ h → 0 ≤ L h) :
  ∃ μ, μ.Regular ∧ ∀ (h : C(X, ℝ)), ∫ (x : X), h x ∂μ = L h
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.exists_regular_integral_eq`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/RieszMarkovKakutani/Compact.html#LinearMap.exists_regular_integral_eq).

## Sources

- [Tau Ceti documentation: `LinearMap.exists_regular_integral_eq`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/RieszMarkovKakutani/Compact.html#LinearMap.exists_regular_integral_eq)
- [Source of `LinearMap.exists_regular_integral_eq` in TauCeti/MeasureTheory/Integral/RieszMarkovKakutani/Compact.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Integral/RieszMarkovKakutani/Compact.lean#L40)
