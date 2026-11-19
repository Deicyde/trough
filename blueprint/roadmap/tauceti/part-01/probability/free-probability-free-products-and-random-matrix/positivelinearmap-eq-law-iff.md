---
declaration: theorem
origin: cited
lean: PositiveLinearMap.eq_law_iff
statement: formalized
proof: formalized
---

# PositiveLinearMap.eq_law_iff

The law `μ_a` of an element `a` is the unique finite measure on `ℝ` that
represents `f ↦ φ (f(a))` on continuous functions.

```lean
PositiveLinearMap.eq_law_iff.{u_1} {A : Type u_1} [CStarAlgebra A] [PartialOrder A]
  [StarOrderedRing A] {φ : A →ₚ[ℂ] ℂ} {a : A} {μ : MeasureTheory.Measure ℝ}
  [MeasureTheory.IsFiniteMeasure μ] :
  μ = φ.law a ↔ ∀ (f : ℝ → ℝ), Continuous f → ↑(∫ (x : ℝ), f x ∂μ) = φ (cfc f a)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PositiveLinearMap.eq_law_iff`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Law/Basic.html#PositiveLinearMap.eq_law_iff).

## Sources

- [Tau Ceti documentation: `PositiveLinearMap.eq_law_iff`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Law/Basic.html#PositiveLinearMap.eq_law_iff)
- [Source of `PositiveLinearMap.eq_law_iff` in TauCeti/Probability/FreeProbability/Law/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/FreeProbability/Law/Basic.lean#L196)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FreeProbability/STATUS.md)
