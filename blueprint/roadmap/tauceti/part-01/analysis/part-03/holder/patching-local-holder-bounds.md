---
declaration: theorem
origin: cited
lean: TauCeti.HolderSpace.norm_le_of_forall_eqOn_ball
statement: formalized
proof: formalized
---

# Patching local Hölder bounds

Let `r > 0`. If around every point `x` the bounded Hölder
function `f` agrees on `ball x r` with a bounded Hölder function of norm at most `M`, then
`‖f‖ ≤ 2 (1 + r^(-α)) M`.

```lean
TauCeti.HolderSpace.norm_le_of_forall_eqOn_ball.{u_1, u_2} {α : NNReal} {X : Type u_1}
  {Y : Type u_2} [MetricSpace X] [NormedAddCommGroup Y] [NormedSpace ℝ Y] [Nonempty X]
  {f : TauCeti.HolderSpace α X Y} {r M : ℝ} (hr : 0 < r)
  (h :
    ∀ (x : X),
      ∃ g, ‖g‖ ≤ M ∧ Set.EqOn (⇑↑f.toHolderSubmodule) (⇑↑g.toHolderSubmodule) (Metric.ball x r)) :
  ‖f‖ ≤ 2 * (1 + r ^ (-↑α)) * M
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HolderSpace.norm_le_of_forall_eqOn_ball`](https://taucetiproject.org/docs/TauCeti/Analysis/Holder/Patching.html#TauCeti.HolderSpace.norm_le_of_forall_eqOn_ball).

## Sources

- [Tau Ceti documentation: `TauCeti.HolderSpace.norm_le_of_forall_eqOn_ball`](https://taucetiproject.org/docs/TauCeti/Analysis/Holder/Patching.html#TauCeti.HolderSpace.norm_le_of_forall_eqOn_ball)
- [Source of `TauCeti.HolderSpace.norm_le_of_forall_eqOn_ball` in TauCeti/Analysis/Holder/Patching.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Holder/Patching.lean#L46)
