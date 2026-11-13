---
declaration: section
origin: cited
lean: StatMech.SLE.positiveOn_Icc_of_deriv_nonneg_while_pos, StatMech.SLE.LoewnerForwardSolution, StatMech.SLE.LoewnerForwardSolution.restrict, StatMech.SLE.LoewnerForwardSolution.reflect, StatMech.SLE.LoewnerForwardSolution.timeShift, StatMech.SLE.LoewnerForwardSolution.appendCurve, StatMech.SLE.LoewnerForwardSolution.append, StatMech.SLE.IsLoewnerAdmissibleDuration
statement: formalized
proof: formalized
---

# Maximal solutions of the chordal Loewner equation and the Loewner hulls

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html).

## Positivity persists under a nonnegative derivative

A continuous function on `[0, T]` that is positive at `0` and has a nonnegative derivative at
every interior point where it is positive stays positive on `[0, T]`.

Formalized by `StatMech.SLE.positiveOn_Icc_of_deriv_nonneg_while_pos`, a theorem declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#positive-on-icc-of-deriv-nonneg-while-po).

## Forward solution of the Loewner equation

A solution `t ↦ g_t(z)` of the Loewner equation on `[0, T]` (one-sided derivatives at the
endpoints) with `g_0(z) = z` and `g_t(z) ∈ ℍ` for `t ∈ [0, T]`.

Formalized by `StatMech.SLE.LoewnerForwardSolution`, a structure declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#loewner-forward-solution).

## Restriction of a Loewner forward solution

The restriction of a forward solution to `[0, S]`, `S ≤ T`.

Formalized by `StatMech.SLE.LoewnerForwardSolution.restrict`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#restrict).

## Reflection of a Loewner forward solution

The reflected solution `-conj g_t(z)`, a forward solution for the driving function `-W`.

Formalized by `StatMech.SLE.LoewnerForwardSolution.reflect`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#reflect).

## Time shift of a Loewner forward solution

The solution restarted at time `s`: `u ↦ g_{s+u}(z)`, for the driving function
`u ↦ W(s + u)`.

Formalized by `StatMech.SLE.LoewnerForwardSolution.timeShift`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#time-shift).

## Concatenated curve of two Loewner solutions

The concatenation of `g` on `[0, S]` with a solution `h` started from `g_S(z)` at time `S`.

Formalized by `StatMech.SLE.LoewnerForwardSolution.appendCurve`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 389](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L389). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#append-curve).

## Concatenation of Loewner forward solutions

The concatenation of two forward solutions, a forward solution on `[0, S + T]`.

Formalized by `StatMech.SLE.LoewnerForwardSolution.append`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#append).

## Admissible duration for the Loewner equation

`T > 0` and there is a forward solution from `z` on `[0, T]`.

Formalized by `StatMech.SLE.IsLoewnerAdmissibleDuration`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 744](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L744). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#is-loewner-admissible-duration).

## Lifetime of a point under the Loewner flow

The lifetime `T_z ∈ [0, ∞]` of `z`: the supremum of admissible durations.

Formalized by `StatMech.SLE.loewnerLifetime`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 759](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L759). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#loewner-lifetime).

## Times before the Loewner lifetime

`0 ≤ t < T_z`.

Formalized by `StatMech.SLE.IsBeforeLoewnerLifetime`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 794](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L794). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#is-before-loewner-lifetime).

## Chosen admissible Loewner duration

A chosen admissible duration exceeding `t`, for `t` before the lifetime.

Formalized by `StatMech.SLE.selectedLoewnerDuration`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 810](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L810). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#selected-loewner-duration).

## Chosen Loewner forward solution

A chosen forward solution on `[0, selectedLoewnerDuration ht]`.

Formalized by `StatMech.SLE.selectedLoewnerSolution`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 821](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L821). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#selected-loewner-solution).

## Maximal Loewner trajectory

The maximal solution `t ↦ g_t(z)` for `0 ≤ t < T_z` (independent of choices by uniqueness);
it is `z` outside `[0, T_z)`.

Formalized by `StatMech.SLE.loewnerMaximalCurve`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 828](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L828). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#loewner-maximal-curve).

## Maximal solution of the chordal Loewner equation

For continuous `W` and `z ∈ ℍ`, the
lifetime `T_z` is positive, `g_0(z) = z`, `g_t(z) ∈ ℍ` for `0 ≤ t < T_z`, the equation holds at
`t = 0` from the right and at every `0 < t < T_z` (Lawler 2005, Chapter 4).

Formalized by `StatMech.SLE.loewner_maximal_forward_exists`, a theorem declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 947](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L947). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#loewner-maximal-forward-exists).

## Unswallowed domain of the Loewner flow

The domain `H_t = {z ∈ ℍ : t < T_z}` of points not swallowed by time `t`.

Formalized by `StatMech.SLE.loewnerUnswallowedDomain`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 964](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L964). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#loewner-unswallowed-domain).

## Maximal Loewner maps

The Loewner map `g_t(z)`, the maximal solution at time `t`.

Formalized by `StatMech.SLE.loewnerMaximalMaps`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 1033](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L1033). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#loewner-maximal-maps).

## Inverse of the maximal Loewner map

The inverse `g_t⁻¹ : ℍ → H_t` (`0` outside `ℍ`).

Formalized by `StatMech.SLE.loewnerMaximalMapsInverse`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 1165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L1165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#loewner-maximal-maps-inverse).

## Unswallowed domain equals the forward-extension domain

The lifetime-defined unswallowed domain is exactly the intrinsic forward-extension domain.

Formalized by `StatMech.SLE.loewnerUnswallowedDomain_eq_setOf_hasLoewnerForwardExtension`, a theorem declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 1353](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L1353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#loewner-unswallowed-domain-eq-set-of-has).

## Loewner map as a homeomorphism onto the half-plane

`g_t` as a homeomorphism `H_t ≃ₜ ℍ`.

Formalized by `StatMech.SLE.loewnerMaximalMapsHomeomorph`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 1690](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L1690). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#loewner-maximal-maps-homeomorph).

## The unswallowed domain is simply connected

The unswallowed domain is simply connected.

Formalized by `StatMech.SLE.isSimplyConnected_loewnerUnswallowedDomain`, a theorem declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 1738](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L1738). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#is-simply-connected-loewner-unswallowed).

## Maximal Loewner maps solve the maximal Loewner equation

The canonical maximal family has the exact lifetime domains and conformal Loewner maps.

Formalized by `StatMech.SLE.loewnerMaximalMaps_satisfiesMaximalLoewnerEquation`, a theorem declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 2187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L2187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#loewner-maximal-maps-satisfies-maximal-l).

## Loewner hull

The Loewner hull `K_t = ℍ \ H_t` of points swallowed by time `t`.

Formalized by `StatMech.SLE.loewnerSwallowedSet`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 2226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L2226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#loewner-swallowed-set).

## Loewner hulls are compact hulls

For continuous `W` and `t ≥ 0`, the Loewner hull `K_t` is a compact `ℍ`-hull (Lawler 2005,
Chapter 4; the capacity normalization is not proved).

Formalized by `StatMech.SLE.loewnerSwallowedSet_isCompactHull`, a theorem declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean, line 2360](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/Loewner/LoewnerMaximal.lean#L2360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html#loewner-swallowed-set-is-compact-hull).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Maximal solutions of the chordal Loewner equation and the Loewner hulls](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/maximal-solutions-of-the-chordal-loewner-equatio)
