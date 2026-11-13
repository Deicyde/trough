---
declaration: section
origin: cited
lean: MathlibExt.Biology.Dynamics.Logistic.logistic, MathlibExt.Biology.Dynamics.Logistic.logistic_zero, MathlibExt.Biology.Dynamics.Logistic.logistic_denom_pos, MathlibExt.Biology.Dynamics.Logistic.hasDerivAt_logistic, MathlibExt.Biology.Dynamics.Logistic.eqOn_logistic_of_hasDerivWithinAt, MathlibExt.Biology.Dynamics.Logistic.tendsto_logistic_atTop, MathlibExt.Biology.Dynamics.Logistic.tendsto_logistic_carryingCapacity_atTop, MathlibExt.Biology.Dynamics.Logistic.logit_logistic
statement: formalized
proof: formalized
---

# Logistic growth equation

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/logistic-growth-equation/index.html).

## Explicit solution of the logistic equation

Explicit solution of the logistic equation `x' = r x (1 - x / K)` with `x 0 = x₀`:
`K x₀ e^{r t} / (K + x₀ (e^{r t} - 1))`.

Formalized by `MathlibExt.Biology.Dynamics.Logistic.logistic`, a definition declared in [MathlibExt/Biology/Dynamics/Logistic.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/Logistic.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/logistic-growth-equation/index.html#logistic).

## Initial value of the logistic solution

The logistic solution starts at `x₀` (for `K ≠ 0`).

Formalized by `MathlibExt.Biology.Dynamics.Logistic.logistic_zero`, a theorem declared in [MathlibExt/Biology/Dynamics/Logistic.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/Logistic.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/logistic-growth-equation/index.html#logistic-zero).

## Positivity of the logistic solution's denominator

In the biological domain (`K > 0`, `x₀ > 0`, `r t ≥ 0`, or `x₀ ≤ K`) the denominator of the
logistic solution is positive.

Formalized by `MathlibExt.Biology.Dynamics.Logistic.logistic_denom_pos`, a theorem declared in [MathlibExt/Biology/Dynamics/Logistic.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/Logistic.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/logistic-growth-equation/index.html#logistic-denom-pos).

## The explicit solution solves the logistic equation

Wherever the denominator
`K + x₀ (e^{r t} - 1)` is nonzero, `x' = r x (1 - x / K)` (all real parameters, `K ≠ 0`).

Formalized by `MathlibExt.Biology.Dynamics.Logistic.hasDerivAt_logistic`, a theorem declared in [MathlibExt/Biology/Dynamics/Logistic.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/Logistic.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/logistic-growth-equation/index.html#has-deriv-at-logistic).

## Uniqueness of the logistic solution

**Uniqueness of the logistic solution** on `[0, T]`: in the biological domain
(`K > 0`, `x₀ > 0`, `r ≥ 0`), any function continuous on `[0, T]`, with right derivative
`r x (1 - x / K)` on `[0, T)` and `x 0 = x₀`, equals the explicit solution on `[0, T]`.

Formalized by `MathlibExt.Biology.Dynamics.Logistic.eqOn_logistic_of_hasDerivWithinAt`, a theorem declared in [MathlibExt/Biology/Dynamics/Logistic.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/Logistic.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/logistic-growth-equation/index.html#eq-on-logistic-of-has-deriv-within-at).

## Convergence to the carrying capacity

For `r > 0` and `x₀ > 0`, `x(t) → K` as
`t → ∞` (the identity needs no sign condition on `K`; biologically `K > 0`).

Formalized by `MathlibExt.Biology.Dynamics.Logistic.tendsto_logistic_atTop`, a theorem declared in [MathlibExt/Biology/Dynamics/Logistic.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/Logistic.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/logistic-growth-equation/index.html#tendsto-logistic-at-top).

## Exponential limit

For fixed `r`, `x₀`, `t`, the logistic solution tends to the
exponential-growth solution `x₀ e^{r t}` as the carrying capacity `K → ∞`.

Formalized by `MathlibExt.Biology.Dynamics.Logistic.tendsto_logistic_carryingCapacity_atTop`, a theorem declared in [MathlibExt/Biology/Dynamics/Logistic.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/Logistic.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/logistic-growth-equation/index.html#tendsto-logistic-carrying-capacity-at-to).

## Log-odds grow linearly

**Log-odds grow linearly** for a frequency (`K = 1`): for `0 < x₀ < 1` and all `r`, `t`,
`log (x(t) / (1 - x(t))) = log (x₀ / (1 - x₀)) + r t`.

Formalized by `MathlibExt.Biology.Dynamics.Logistic.logit_logistic`, a theorem declared in [MathlibExt/Biology/Dynamics/Logistic.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/Logistic.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/logistic-growth-equation/index.html#logit-logistic).

## Exact deterministic transit time

Starting from frequency `a ∈ (0, 1)` with `r ≠ 0`,
the logistic frequency reaches `1 - a` at time `(2 / r) log ((1 - a) / a)`.

Formalized by `MathlibExt.Biology.Dynamics.Logistic.logistic_transitTime`, a theorem declared in [MathlibExt/Biology/Dynamics/Logistic.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/Logistic.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/logistic-growth-equation/index.html#logistic-transit-time).

## Logistic transit time from $1/(2N)$ to $1 - 1/(2N)$

The transit time from `1 / (2N)` to `1 - 1 / (2N)` is `(2 / r) log (2N - 1)`, for
`N ≥ 1` and `r ≠ 0`.

Formalized by `MathlibExt.Biology.Dynamics.Logistic.logistic_transitTime_twoN`, a theorem declared in [MathlibExt/Biology/Dynamics/Logistic.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/Logistic.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/logistic-growth-equation/index.html#logistic-transit-time-two-n).

## Logistic solution is strictly increasing

For `r > 0` and `0 < x₀ < K` the logistic solution is strictly increasing, so the transit
time of `logistic_transitTime` is the unique time at which `1 - a` is reached.

Formalized by `MathlibExt.Biology.Dynamics.Logistic.strictMono_logistic`, a theorem declared in [MathlibExt/Biology/Dynamics/Logistic.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/Logistic.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/logistic-growth-equation/index.html#strict-mono-logistic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Logistic growth equation](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/logistic-growth-equation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/population-dynamics/logistic-growth-equation)
