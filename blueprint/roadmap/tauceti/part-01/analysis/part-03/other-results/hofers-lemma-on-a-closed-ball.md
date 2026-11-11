---
declaration: theorem
origin: cited
lean: TauCeti.hofer_of_continuousOn_closedBall, TauCeti.exists_tendsto_hofer
statement: formalized
proof: formalized
---

# Hofer's lemma on a closed ball

Let `ϕ` be continuous and nonnegative on the closed ball
of radius `3 ε` about `x`. Then there are `0 < ε' ≤ ε` and a point `x'` within `2 ε` of `x` with
`ε ϕ(x) ≤ ε' ϕ(x')` and `ϕ ≤ 2 ϕ(x')` on the closed ball of radius `ε'` about `x'`.

```lean
TauCeti.hofer_of_continuousOn_closedBall.{u_1} {X : Type u_1} [MetricSpace X] [CompleteSpace X]
  (x : X) {ε : ℝ} (hε : 0 < ε) {ϕ : X → ℝ} (hϕ : ContinuousOn ϕ (Metric.closedBall x (3 * ε)))
  (hϕ₀ : ∀ y ∈ Metric.closedBall x (3 * ε), 0 ≤ ϕ y) :
  ∃ ε' > 0,
    ∃ x',
      ε' ≤ ε ∧ dist x' x ≤ 2 * ε ∧ ε * ϕ x ≤ ε' * ϕ x' ∧ ∀ (y : X), dist x' y ≤ ε' → ϕ y ≤ 2 * ϕ x'
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.hofer_of_continuousOn_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/Hofer.html#TauCeti.hofer_of_continuousOn_closedBall).

## Other forms

**Hofer's lemma along a sequence blowing up at a point.** Formalized in Tau Ceti as [`TauCeti.exists_tendsto_hofer`](https://taucetiproject.org/docs/TauCeti/Analysis/Hofer.html#TauCeti.exists_tendsto_hofer).

```lean
TauCeti.exists_tendsto_hofer.{u_1, u_2} {X : Type u_1} [MetricSpace X] [CompleteSpace X]
  {ι : Type u_2} {l : Filter ι} {ϕ : ι → X → ℝ} {x : ι → X} {x₀ : X} {r : ℝ} (hr : 0 < r)
  (hϕ : ∀ (i : ι), ContinuousOn (ϕ i) (Metric.closedBall x₀ r))
  (hϕ₀ : ∀ (i : ι), ∀ y ∈ Metric.closedBall x₀ r, 0 ≤ ϕ i y) (hx : Filter.Tendsto x l (nhds x₀))
  (hϕx : Filter.Tendsto (fun i => ϕ i (x i)) l Filter.atTop) :
  ∃ c ρ,
    (∀ (i : ι), 0 < ρ i) ∧
      Filter.Tendsto c l (nhds x₀) ∧
        Filter.Tendsto ρ l (nhds 0) ∧
          Filter.Tendsto (fun i => ρ i * ϕ i (c i)) l Filter.atTop ∧
            ∀ᶠ (i : ι) in l,
              ϕ i (x i) ≤ ϕ i (c i) ∧ ∀ (y : X), dist (c i) y ≤ ρ i → ϕ i y ≤ 2 * ϕ i (c i)
```

## Sources

- [Tau Ceti documentation: `TauCeti.hofer_of_continuousOn_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/Hofer.html#TauCeti.hofer_of_continuousOn_closedBall)
- [Source of `TauCeti.hofer_of_continuousOn_closedBall` in TauCeti/Analysis/Hofer.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Hofer.lean#L67)
