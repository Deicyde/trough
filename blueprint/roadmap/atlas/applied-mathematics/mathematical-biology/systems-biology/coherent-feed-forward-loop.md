---
declaration: section
origin: cited
lean: MathlibExt.Biology.Dynamics.FeedForwardLoop.relaxation, MathlibExt.Biology.Dynamics.FeedForwardLoop.hasDerivAt_relaxation, MathlibExt.Biology.Dynamics.FeedForwardLoop.andGate, MathlibExt.Biology.Dynamics.FeedForwardLoop.simpleGate, MathlibExt.Biology.Dynamics.FeedForwardLoop.yOn, MathlibExt.Biology.Dynamics.FeedForwardLoop.onDelay, MathlibExt.Biology.Dynamics.FeedForwardLoop.hasDerivAt_yOn, MathlibExt.Biology.Dynamics.FeedForwardLoop.onDelay_pos
statement: formalized
proof: formalized
---

# Coherent feed-forward loop

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/coherent-feed-forward-loop/index.html).

## Variation-of-constants solution of a linear relaxation equation

The variation-of-constants solution of `z' = P(t) - α z`, `z(0) = z₀`:
`z(t) = z₀ e^{-α t} + ∫₀ᵗ e^{-α (t - s)} P(s) ds`. Used for `t ≥ 0`.

Formalized by `MathlibExt.Biology.Dynamics.FeedForwardLoop.relaxation`, a definition declared in [MathlibExt/Biology/Dynamics/FeedForwardLoop.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FeedForwardLoop.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/coherent-feed-forward-loop/index.html#relaxation).

## Relaxation solution satisfies its differential equation

The relaxation solves `z' = P - α z` at every time where the (locally integrable) production
rate `P` is continuous.

Formalized by `MathlibExt.Biology.Dynamics.FeedForwardLoop.hasDerivAt_relaxation`, a theorem declared in [MathlibExt/Biology/Dynamics/FeedForwardLoop.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FeedForwardLoop.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/coherent-feed-forward-loop/index.html#has-deriv-at-relaxation).

## AND-gate production rate in the logic approximation

AND-gate production in the logic approximation: rate `β` when `K_x < x` and `K_y < y`,
else `0`.

Formalized by `MathlibExt.Biology.Dynamics.FeedForwardLoop.andGate`, a definition declared in [MathlibExt/Biology/Dynamics/FeedForwardLoop.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FeedForwardLoop.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/coherent-feed-forward-loop/index.html#and-gate).

## Single-input production rate in the logic approximation

Single-input production in the logic approximation: rate `β` when `K_x < x`, else `0`.

Formalized by `MathlibExt.Biology.Dynamics.FeedForwardLoop.simpleGate`, a definition declared in [MathlibExt/Biology/Dynamics/FeedForwardLoop.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FeedForwardLoop.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/coherent-feed-forward-loop/index.html#simple-gate).

## Intermediate factor after an ON step

`Y` after an ON step of `Sx` from `Y(0) = 0`: `Y(t) = (β_y/α_y)(1 - e^{-α_y t})`.

Formalized by `MathlibExt.Biology.Dynamics.FeedForwardLoop.yOn`, a definition declared in [MathlibExt/Biology/Dynamics/FeedForwardLoop.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FeedForwardLoop.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/coherent-feed-forward-loop/index.html#y-on).

## ON-step delay of the feed-forward loop

The ON-step delay `T_on = (1/α_y) log(1 / (1 - K_yz / Y_st))`, `Y_st = β_y/α_y`: the time
at which `Y` crosses the activation threshold `K_yz` of `Z`. Meaningful for
`0 < K_yz < Y_st`.

Formalized by `MathlibExt.Biology.Dynamics.FeedForwardLoop.onDelay`, a definition declared in [MathlibExt/Biology/Dynamics/FeedForwardLoop.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FeedForwardLoop.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/coherent-feed-forward-loop/index.html#on-delay).

## Intermediate factor solves its production–decay equation

`yOn` solves `Y' = β_y - α_y Y` with `Y(0) = 0` (for `α_y ≠ 0`; at `α_y = 0` Lean's
`β_y / 0 = 0` makes `yOn` identically `0`, which is not a solution).

Formalized by `MathlibExt.Biology.Dynamics.FeedForwardLoop.hasDerivAt_yOn`, a theorem declared in [MathlibExt/Biology/Dynamics/FeedForwardLoop.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FeedForwardLoop.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/coherent-feed-forward-loop/index.html#has-deriv-at-y-on).

## Positivity of the ON delay

The ON delay is positive.

Formalized by `MathlibExt.Biology.Dynamics.FeedForwardLoop.onDelay_pos`, a theorem declared in [MathlibExt/Biology/Dynamics/FeedForwardLoop.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FeedForwardLoop.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/coherent-feed-forward-loop/index.html#on-delay-pos).

## Intermediate factor exceeds the threshold exactly after the ON delay

`Y` exceeds `K_yz` exactly after the ON delay: `K_yz < Y(t) ↔ T_on < t`.

Formalized by `MathlibExt.Biology.Dynamics.FeedForwardLoop.yOn_gt_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/FeedForwardLoop.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FeedForwardLoop.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/coherent-feed-forward-loop/index.html#y-on-gt-iff).

## Feed-forward loop target after an ON step

The FFL target after an ON step of `Sx` at `t = 0` from `Y(0) = Z(0) = 0`, with `X* = 1`
and `K_xz < 1`.

Formalized by `MathlibExt.Biology.Dynamics.FeedForwardLoop.fflOn`, a definition declared in [MathlibExt/Biology/Dynamics/FeedForwardLoop.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FeedForwardLoop.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/coherent-feed-forward-loop/index.html#ffl-on).

## Simple-regulation target after an ON step

The simple-regulation target after an ON step of `Sx` at `t = 0` from `Z(0) = 0`.

Formalized by `MathlibExt.Biology.Dynamics.FeedForwardLoop.simpleOn`, a definition declared in [MathlibExt/Biology/Dynamics/FeedForwardLoop.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FeedForwardLoop.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/coherent-feed-forward-loop/index.html#simple-on).

## ON delay

The FFL target stays at `0` until `T_on`.

Formalized by `MathlibExt.Biology.Dynamics.FeedForwardLoop.ffl_on_eq_zero`, a theorem declared in [MathlibExt/Biology/Dynamics/FeedForwardLoop.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FeedForwardLoop.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/coherent-feed-forward-loop/index.html#ffl-on-eq-zero).

## Delayed rise

After `T_on` the FFL target relaxes from `0` towards `β_z/α_z`:
`Z(t) = (β_z/α_z)(1 - e^{-α_z (t - T_on)})` (for `α_z > 0`, `K_xz < 1`).

Formalized by `MathlibExt.Biology.Dynamics.FeedForwardLoop.ffl_on_eq`, a theorem declared in [MathlibExt/Biology/Dynamics/FeedForwardLoop.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FeedForwardLoop.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/coherent-feed-forward-loop/index.html#ffl-on-eq).

## Simple regulation responds without delay

Simple regulation responds without delay: `Z(t) = (β_z/α_z)(1 - e^{-α_z t}) > 0` for all
`t > 0`.

Formalized by `MathlibExt.Biology.Dynamics.FeedForwardLoop.simple_on_pos`, a theorem declared in [MathlibExt/Biology/Dynamics/FeedForwardLoop.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FeedForwardLoop.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/coherent-feed-forward-loop/index.html#simple-on-pos).

## Feed-forward loop target after an OFF step

The FFL target after `Sx` is removed at `t = 0` (`X* = 0`), starting from `Z(0) = z₀`, for
an arbitrary trajectory `Y` of the intermediate factor.

Formalized by `MathlibExt.Biology.Dynamics.FeedForwardLoop.fflOff`, a definition declared in [MathlibExt/Biology/Dynamics/FeedForwardLoop.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FeedForwardLoop.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/coherent-feed-forward-loop/index.html#ffl-off).

## Simple-regulation target after an OFF step

The simple-regulation target after `Sx` is removed at `t = 0`, from `Z(0) = z₀`.

Formalized by `MathlibExt.Biology.Dynamics.FeedForwardLoop.simpleOff`, a definition declared in [MathlibExt/Biology/Dynamics/FeedForwardLoop.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FeedForwardLoop.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/coherent-feed-forward-loop/index.html#simple-off).

## No OFF delay

For a nonnegative threshold `K_xz`, whatever `Y` does, the FFL and simple
regulation decay identically after an OFF step: `Z(t) = z₀ e^{-α_z t}`.

Formalized by `MathlibExt.Biology.Dynamics.FeedForwardLoop.ffl_off_eq_simple_off`, a theorem declared in [MathlibExt/Biology/Dynamics/FeedForwardLoop.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/FeedForwardLoop.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/coherent-feed-forward-loop/index.html#ffl-off-eq-simple-off).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Coherent feed-forward loop](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/coherent-feed-forward-loop/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/systems-biology/coherent-feed-forward-loop)
