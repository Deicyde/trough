---
declaration: theorem
origin: cited
lean: TauCeti.ae_eventually_ne_top_and_differentiableAt_toReal
statement: formalized
proof: formalized
---

# Rademacher's theorem for extended-real convex functions

Let `f : E → EReal` have convex
real epigraph and never take the value `⊥`, on a finite-dimensional real normed space `E` with an
additive Haar measure `μ`. Then at `μ`-almost every point `x` of the effective domain, `f` is
finite on a neighbourhood of `x` and its real representative `x ↦ (f x).toReal` is
differentiable at `x`.

```lean
TauCeti.ae_eventually_ne_top_and_differentiableAt_toReal.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {f : E → EReal} [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] (hf : Convex ℝ {p | f p.1 ≤ ↑p.2})
  (hbot : ∀ (x : E), f x ≠ ⊥) :
  ∀ᵐ (x : E) ∂μ,
    f x ≠ ⊤ → (∀ᶠ (x' : E) in nhds x, f x' ≠ ⊤) ∧ DifferentiableAt ℝ (fun x' => (f x').toReal) x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Rademacher's theorem for locally Lipschitz functions](../calculus/part-01/rademachers-theorem-for-locally-lipschitz-functi.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ae_eventually_ne_top_and_differentiableAt_toReal`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Differentiability.html#TauCeti.ae_eventually_ne_top_and_differentiableAt_toReal).

## Sources

- [Tau Ceti documentation: `TauCeti.ae_eventually_ne_top_and_differentiableAt_toReal`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Differentiability.html#TauCeti.ae_eventually_ne_top_and_differentiableAt_toReal)
- [Source of `TauCeti.ae_eventually_ne_top_and_differentiableAt_toReal` in TauCeti/Analysis/Convex/Differentiability.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Convex/Differentiability.lean#L84)
