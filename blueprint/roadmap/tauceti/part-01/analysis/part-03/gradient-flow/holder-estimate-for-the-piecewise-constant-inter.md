---
declaration: theorem
origin: cited
lean: TauCeti.edist_ceil_sq_le_of_forall_mem_moreauYosidaResolvent
statement: formalized
proof: formalized
---

# Hölder estimate for the piecewise constant interpolant

Under the hypotheses of
`TauCeti.edist_sq_le_of_forall_mem_moreauYosidaResolvent`, the piecewise constant interpolant
`t ↦ u ⌈t / τ⌉₊` of a minimizing movement sequence satisfies, for `0 ≤ s ≤ t`,
`d(u ⌈s / τ⌉₊, u ⌈t / τ⌉₊)² ≤ 2 (t - s + τ) (E - A) (1 + exp (8 (t + τ) / τ'))`.
As `τ → 0` this becomes a `1/2`-Hölder bound on bounded time intervals.

```lean
TauCeti.edist_ceil_sq_le_of_forall_mem_moreauYosidaResolvent.{u_1} {X : Type u_1}
  [PseudoEMetricSpace X] {φ : X → EReal} {τ τ' : NNReal} {u : ℕ → X}
  (hu : ∀ (n : ℕ), u (n + 1) ∈ TauCeti.moreauYosidaResolvent φ τ (u n)) (hτ : 0 < τ)
  (hττ' : 4 * τ ≤ τ') {A E : ℝ} (hA : TauCeti.moreauYosida φ τ' (u 0) = ↑A) (hE : φ (u 0) = ↑E)
  {s t : ℝ} (hs : 0 ≤ s) (hst : s ≤ t) :
  edist (u ⌈s / ↑τ⌉₊) (u ⌈t / ↑τ⌉₊) ^ 2 ≤
    ENNReal.ofReal (2 * (t - s + ↑τ) * (E - A) * (1 + Real.exp (8 * (t + ↑τ) / ↑τ')))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Discrete Grönwall bound under coercivity](../specific-limits/discrete-gronwall-bound-under-coercivity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.edist_ceil_sq_le_of_forall_mem_moreauYosidaResolvent`](https://taucetiproject.org/docs/TauCeti/Analysis/GradientFlow/MinimizingMovement.html#TauCeti.edist_ceil_sq_le_of_forall_mem_moreauYosidaResolvent).

## Sources

- [Tau Ceti documentation: `TauCeti.edist_ceil_sq_le_of_forall_mem_moreauYosidaResolvent`](https://taucetiproject.org/docs/TauCeti/Analysis/GradientFlow/MinimizingMovement.html#TauCeti.edist_ceil_sq_le_of_forall_mem_moreauYosidaResolvent)
- [Source of `TauCeti.edist_ceil_sq_le_of_forall_mem_moreauYosidaResolvent` in TauCeti/Analysis/GradientFlow/MinimizingMovement.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/GradientFlow/MinimizingMovement.lean#L270)
