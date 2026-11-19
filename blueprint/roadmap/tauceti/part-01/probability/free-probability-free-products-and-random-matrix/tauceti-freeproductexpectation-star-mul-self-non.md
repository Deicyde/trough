---
declaration: theorem
origin: cited
lean: TauCeti.freeProductExpectation_star_mul_self_nonneg
statement: formalized
proof: formalized
---

# TauCeti.freeProductExpectation_star_mul_self_nonneg

The canonical free-product expectation is positive on algebraic squares whenever each
normalized factor functional is positive on algebraic squares. No norm or trace is required.

```lean
TauCeti.freeProductExpectation_star_mul_self_nonneg.{u_1, u_2} {I : Type u_1} [DecidableEq I]
  {A : I → Type u_2} [(i : I) → Ring (A i)] [(i : I) → Algebra ℂ (A i)] [(i : I) → StarRing (A i)]
  [∀ (i : I), StarModule ℂ (A i)] (φ : (i : I) → A i →ₗ[ℂ] ℂ) (hφ : ∀ (i : I), (φ i) 1 = 1)
  (hpos : ∀ (i : I) (a : A i), 0 ≤ (φ i) (star a * a)) (x : LinearAlgebra.FreeProduct ℂ A) :
  0 ≤ (TauCeti.freeProductExpectation φ hφ) (star x * x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.freeProductExpectation_star_mul_self_nonneg`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/FreeProduct/Positive.html#TauCeti.freeProductExpectation_star_mul_self_nonneg).

## Sources

- [Tau Ceti documentation: `TauCeti.freeProductExpectation_star_mul_self_nonneg`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/FreeProduct/Positive.html#TauCeti.freeProductExpectation_star_mul_self_nonneg)
- [Source of `TauCeti.freeProductExpectation_star_mul_self_nonneg` in TauCeti/Probability/FreeProbability/FreeProduct/Positive.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/FreeProbability/FreeProduct/Positive.lean#L171)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FreeProbability/STATUS.md)
