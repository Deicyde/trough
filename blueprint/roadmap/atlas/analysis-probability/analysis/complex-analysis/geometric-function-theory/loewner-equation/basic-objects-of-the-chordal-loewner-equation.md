---
declaration: section
origin: cited
lean: StatMech.SLE.closedUpperHalfPlane, StatMech.SLE.realLine, StatMech.SLE.IsCompactHull, StatMech.SLE.IsCompactHull.complement_connected, StatMech.SLE.isSimplyConnected_upperHalfPlane, StatMech.SLE.HasHalfPlaneCapacity, StatMech.SLE.loewnerField, StatMech.SLE.IsLoewnerSolutionAt
statement: formalized
proof: formalized
---

# Basic objects of the chordal Loewner equation

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/basic-objects-of-the-chordal-loewner-equation/index.html).

## Closed upper half-plane

The closed upper half-plane `{z : 0 ≤ Im z}`.

Formalized by `StatMech.SLE.closedUpperHalfPlane`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/Defs.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/Defs.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/basic-objects-of-the-chordal-loewner-equation/index.html#closed-upper-half-plane).

## Real axis in the complex plane

The real axis `{z : Im z = 0}` in `ℂ`.

Formalized by `StatMech.SLE.realLine`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/Defs.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/Defs.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/basic-objects-of-the-chordal-loewner-equation/index.html#real-line).

## Compact hull in the upper half-plane

A compact `ℍ`-hull: a bounded subset `K` of `ℍ`, relatively closed in `ℍ`, whose complement
`ℍ \ K` is open and simply connected.

Formalized by `StatMech.SLE.IsCompactHull`, a structure declared in [MathlibExt/Analysis/Complex/Loewner/Defs.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/Defs.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/basic-objects-of-the-chordal-loewner-equation/index.html#is-compact-hull).

## Complement of a compact hull is connected

The complement of a compact `ℍ`-hull is connected.

Formalized by `StatMech.SLE.IsCompactHull.complement_connected`, a lemma declared in [MathlibExt/Analysis/Complex/Loewner/Defs.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/Defs.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/basic-objects-of-the-chordal-loewner-equation/index.html#complement-connected).

## The upper half-plane is simply connected

The complex upper half-plane is simply connected.

Formalized by `StatMech.SLE.isSimplyConnected_upperHalfPlane`, a lemma declared in [MathlibExt/Analysis/Complex/Loewner/Defs.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/Defs.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/basic-objects-of-the-chordal-loewner-equation/index.html#is-simply-connected-upper-half-plane).

## Hydrodynamic normalization with half-plane capacity

`g` is hydrodynamically normalized at infinity with half-plane capacity `a`: `g(z) - z → 0`
and `z (g(z) - z) → a` as `z → ∞`, i.e. `g(z) = z + a/z + o(1/z)`.

Formalized by `StatMech.SLE.HasHalfPlaneCapacity`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/Defs.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/Defs.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/basic-objects-of-the-chordal-loewner-equation/index.html#has-half-plane-capacity).

## Chordal Loewner vector field

The chordal Loewner vector field `w ↦ 2 / (w - W_t)` at time `t`.

Formalized by `StatMech.SLE.loewnerField`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/Defs.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/Defs.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/basic-objects-of-the-chordal-loewner-equation/index.html#loewner-field).

## Solution of the Loewner equation at a time

`t ↦ g_t(z)` satisfies the Loewner equation `∂_t g_t(z) = 2 / (g_t(z) - W_t)` at time `t`.

Formalized by `StatMech.SLE.IsLoewnerSolutionAt`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/Defs.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/Defs.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/basic-objects-of-the-chordal-loewner-equation/index.html#is-loewner-solution-at).

## Solution of the Loewner equation on a set of times

`t ↦ g_t(z)` satisfies the Loewner equation on `s` (derivatives within `s`).

Formalized by `StatMech.SLE.IsLoewnerSolutionOn`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/Defs.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/Defs.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/basic-objects-of-the-chordal-loewner-equation/index.html#is-loewner-solution-on).

## Forward extension of a Loewner trajectory

The Loewner trajectory from `z` extends in `ℍ` beyond time `t`. This is the intrinsic
maximal-lifetime condition used to determine the unswallowed domain.

Formalized by `StatMech.SLE.HasLoewnerForwardExtension`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/Defs.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/Defs.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/basic-objects-of-the-chordal-loewner-equation/index.html#has-loewner-forward-extension).

## Loewner equation without domain restriction

`g_0 = id` and `t ↦ g_t(z)` solves the Loewner equation for every `z ∈ ℂ` and every `t ≥ 0`,
with no domain restriction (compare `SatisfiesMaximalLoewnerEquation`, where `z` ranges over the
unswallowed domain `D_t`).

Formalized by `StatMech.SLE.SatisfiesLoewnerEquation`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/Defs.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/Defs.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/basic-objects-of-the-chordal-loewner-equation/index.html#satisfies-loewner-equation).

## Maximal chordal Loewner evolution

The maximal chordal Loewner evolution with domains `D_t`. The domains are exactly the points
whose trajectories extend beyond `t`, and `g_t : D_t → ℍ` is a conformal bijection.

Formalized by `StatMech.SLE.SatisfiesMaximalLoewnerEquation`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/Defs.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/Defs.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/basic-objects-of-the-chordal-loewner-equation/index.html#satisfies-maximal-loewner-equation).

## Standard real Brownian motion

A standard real Brownian motion indexed by `ℝ` (used for `t ≥ 0`): `B_0 = 0` a.s., continuous
paths a.s., Gaussian, with independent increments `B_t - B_s ~ N(0, t - s)`.

See also Mathlib's `ProbabilityTheory.IsPreBrownianReal` (time `ℝ≥0`, finite-dimensional laws).

Formalized by `StatMech.SLE.IsStandardBrownianMotion`, a structure declared in [MathlibExt/Analysis/Complex/Loewner/Defs.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/Defs.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/basic-objects-of-the-chordal-loewner-equation/index.html#is-standard-brownian-motion).

## SLE driving function

The SLE`_κ` driving function `W_t = √κ B_t(ω)`.

Formalized by `StatMech.SLE.sleDriving`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/Defs.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/Defs.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/basic-objects-of-the-chordal-loewner-equation/index.html#sle-driving).

## Chordal Schramm–Loewner evolution

`(D, g)` is chordal SLE`_κ` in `ℍ` from `0` to `∞`: `κ ≥ 0`, `B` is a standard Brownian
motion and almost surely `g` solves the maximal Loewner equation with driving function `√κ B`.
This is a definition only; existence of SLE is not proved.

Formalized by `StatMech.SLE.IsChordalSLE`, a structure declared in [MathlibExt/Analysis/Complex/Loewner/Defs.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/Defs.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/basic-objects-of-the-chordal-loewner-equation/index.html#is-chordal-sle).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Basic objects of the chordal Loewner equation](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/basic-objects-of-the-chordal-loewner-equation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/basic-objects-of-the-chordal-loewner-equation)
