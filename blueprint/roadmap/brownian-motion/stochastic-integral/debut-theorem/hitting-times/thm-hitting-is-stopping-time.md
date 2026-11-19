---
declaration: theorem
origin: cited
lean: MeasureTheory.IsStronglyProgressive.isStoppingTime_hittingAfter
statement: formalized
proof: formalized
---

# hitting_is_stopping_time

If $X : T \to \Omega \to E$ is a progressively measurable process with respect to a filtration satisfying the usual conditions and $B$ is a Borel-measurable subset of $E$, then the hitting time of $X$ in $B$ is a stopping time.

## Depends on

- [Stopping time](../../../../mathlib/overview/probability-theory/stochastic-processes/stopping-time.md)
- [Hitting time](../../filtrations-processes-and-martingales/basic-definitions/part-02/def-hittingafter.md)
- [Progressively measurable](../../filtrations-processes-and-martingales/basic-definitions/part-01/def-isstronglyprogressive.md)
- [Usual conditions](../../filtrations-processes-and-martingales/right-continuous-filtrations/def-hasusualconditions.md)

## Proof depends on

- [debut_of_progr_meas_is_stop_time](../debut-theorem/thm-debut-of-progr-meas-is-stop-time.md)

## Proof

Since $B$ is a Borel subset of $\mathcal{S}$ and $X$ is progressively measurable, then $\mathbf{1}_B(X_t)$ is also progressively measurable. The hitting time is then the debut of the set $E = \{(s,\omega) : \mathbf{1}_B(X_s(\omega)) = 1\}$, and therefore is a stopping time by Theorem [debut_of_progr_meas_is_stop_time](../debut-theorem/thm-debut-of-progr-meas-is-stop-time.md).

## Lean

Formalized as [`MeasureTheory.IsStronglyProgressive.isStoppingTime_hittingAfter`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.IsStronglyProgressive.isStoppingTime_hittingAfter).

## Sources

- [Brownian motion blueprint: chapters/debut.tex, line 738](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/debut.tex#L738)
