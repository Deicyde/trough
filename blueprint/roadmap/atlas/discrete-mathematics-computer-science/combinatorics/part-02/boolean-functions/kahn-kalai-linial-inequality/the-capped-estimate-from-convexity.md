---
declaration: section
origin: cited
lean: StatMech.Probability.cvg_convexGap_le, StatMech.Probability.cvg_convexOn_sum, StatMech.Probability.cvg_oneSubPow_convexOn, StatMech.Probability.cvg_L_convexOn, StatMech.Probability.cvg_Q_concaveOn, StatMech.Probability.cvg_R_concaveOn, StatMech.Probability.cvg_openResidue_of_concaveR, StatMech.Probability.cvg_maxInfl_le_one
statement: formalized
proof: formalized
---

# The capped estimate from convexity

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-from-convexity/index.html).

## Nonpositivity of a convex function from its endpoint values

A convex function on `[0, 1]` that is nonpositive at both endpoints is nonpositive on `[0, 1]`.
 See also `ConvexOn.le_max_of_mem_Icc`.

Formalized by `StatMech.Probability.cvg_convexGap_le`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-from-convexity/index.html#cvg-convex-gap-le).

## Finite sum of convex functions is convex

A finite sum of convex functions is convex.

Formalized by `StatMech.Probability.cvg_convexOn_sum`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-from-convexity/index.html#cvg-convex-on-sum).

## Convexity of $(1 - u)^k$ on $(0, 1)$

`u ↦ (1 - u)^k` is convex on `[0, 1]`.

Formalized by `StatMech.Probability.cvg_oneSubPow_convexOn`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-from-convexity/index.html#cvg-one-sub-pow-convex-on).

## Convexity of the damped total weight

The damped total weight `u ↦ ∑_S 4 |S| (1-u)^{|S|-1} f̂(S)²` is convex on `[0, 1]`.

Formalized by `StatMech.Probability.cvg_L_convexOn`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-from-convexity/index.html#cvg-l-convex-on).

## Concavity of $\exp(m u/(2-u))$ for $-1 \le m \le 0$

`u ↦ exp (m · u/(2-u))` is concave on `[0, 1]` for `-1 ≤ m ≤ 0`.

Formalized by `StatMech.Probability.cvg_Q_concaveOn`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-from-convexity/index.html#cvg-q-concave-on).

## Concavity of $\delta^{u/(2-u)} T$ for $e^{-1} \le \delta \le 1$

`u ↦ δ^{u/(2-u)} T` is concave on `[0, 1]` for `e^{-1} ≤ δ ≤ 1` and `T ≥ 0`.

Formalized by `StatMech.Probability.cvg_R_concaveOn`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-from-convexity/index.html#cvg-r-concave-on).

## Capped estimate on $(0, 1)$ from concavity of the right side

If the right side of the capped estimate is concave in `u`, the estimate holds on `(0, 1)`.

Formalized by `StatMech.Probability.cvg_openResidue_of_concaveR`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-from-convexity/index.html#cvg-open-residue-of-concave-r).

## Maximal influence of a Boolean function is at most one

The maximal influence of a Boolean function is at most `1`.

Formalized by `StatMech.Probability.cvg_maxInfl_le_one`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-from-convexity/index.html#cvg-max-infl-le-one).

## Capped estimate when the maximal influence is at least $e^{-1}$

The capped estimate holds for all `u ∈ (0, 1)` when the maximal influence is at least `e^{-1}`.

Formalized by `StatMech.Probability.cvg_openResidue_largeDelta`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-from-convexity/index.html#cvg-open-residue-large-delta).

## Small-influence residual case of the capped estimate

The capped estimate for all `p ∈ (1/2, q)` with `p < 1`, all Boolean functions with maximal
 influence `δ < e^{-1}`, and all `u ∈ (0, 1)`.

Formalized by `StatMech.Probability.cvg_smallDeltaResidue`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-from-convexity/index.html#cvg-small-delta-residue).

## Small-influence case implies the open-interval case

`cvg_smallDeltaResidue q` implies `frh_openResidue q`.

Formalized by `StatMech.Probability.cvg_openResidue_of_smallDelta`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-from-convexity/index.html#cvg-open-residue-of-small-delta).

## Small-influence case implies the full capped estimate on $(1/2, q)$

`cvg_smallDeltaResidue q` implies `mxd_martingaleHC_statement q`.

Formalized by `StatMech.Probability.cvg_martingaleHC_of_smallDelta`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/ConvexGapHC.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-from-convexity/index.html#cvg-martingale-hc-of-small-delta).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The capped estimate from convexity](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-from-convexity/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-from-convexity)
