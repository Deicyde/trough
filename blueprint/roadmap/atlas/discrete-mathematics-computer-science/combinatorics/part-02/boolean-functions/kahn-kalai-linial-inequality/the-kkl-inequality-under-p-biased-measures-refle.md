---
declaration: section
origin: cited
lean: StatMech.Probability.kpb_flipAll, StatMech.Probability.kpb_weight_flip, StatMech.Probability.kpb_kkl_reflect, StatMech.Probability.kpb_PBiasedHC, StatMech.Probability.kpb_residue_c0, StatMech.Probability.kpb_Hbkkkl, StatMech.Probability.kpb_sharpThreshold, StatMech.Probability.kpb_sharpThreshold_window
statement: formalized
proof: formalized
---

# The KKL inequality under p-biased measures: reflection and threshold consequences

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-under-p-biased-measures-refle/index.html).

## Coordinatewise complement of a configuration

The coordinatewise complement `ω ↦ ¬ω` of a configuration.

Formalized by `StatMech.Probability.kpb_flipAll`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLpBiased.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLpBiased.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-under-p-biased-measures-refle/index.html#kpb-flip-all).

## Complement swaps the Bernoulli $p$ and $1 - p$ weights

Complementing sends the Bernoulli(`p`) weight to the Bernoulli(`1 - p`) weight.

Formalized by `StatMech.Probability.kpb_weight_flip`, a lemma declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLpBiased.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLpBiased.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-under-p-biased-measures-refle/index.html#kpb-weight-flip).

## Reflection of the KKL inequality from $p$ to $1 - p$

The KKL inequality with constant `2` at `p` implies it at `1 - p`.

Formalized by `StatMech.Probability.kpb_kkl_reflect`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLpBiased.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLpBiased.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-under-p-biased-measures-refle/index.html#kpb-kkl-reflect).

## KKL inequality with constant 2 on $(1/2, q)$

The KKL inequality with constant `2` for every Bernoulli parameter `p ∈ (1/2, q)`.

Formalized by `StatMech.Probability.kpb_PBiasedHC`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLpBiased.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLpBiased.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-under-p-biased-measures-refle/index.html#kpb-pbiased-hc).

## KKL inequality with constant 0 holds trivially on $(1/2, q)$

The KKL inequality with constant `0` holds for every `p`; this is trivial.

Formalized by `StatMech.Probability.kpb_residue_c0`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLpBiased.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLpBiased.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-under-p-biased-measures-refle/index.html#kpb-residue-c0).

## KKL hypothesis on $(1/2, q)$ restated on the interior of $(1/2, q)$

`kpb_PBiasedHC q` in the form used by `StatMech.TwoDim.kklw_sharpThreshold`.

Formalized by `StatMech.Probability.kpb_Hbkkkl`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLpBiased.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLpBiased.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-under-p-biased-measures-refle/index.html#kpb-hbkkkl).

## Sharp-threshold bound under the $p$-biased KKL hypothesis

`StatMech.TwoDim.kklw_sharpThreshold` under `kpb_PBiasedHC q`.

Formalized by `StatMech.Probability.kpb_sharpThreshold`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLpBiased.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLpBiased.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-under-p-biased-measures-refle/index.html#kpb-sharp-threshold).

## Sharp-threshold window under the $p$-biased KKL hypothesis

`StatMech.TwoDim.kklw_sharpThreshold_window` under `kpb_PBiasedHC q`.

Formalized by `StatMech.Probability.kpb_sharpThreshold_window`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLpBiased.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLpBiased.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-under-p-biased-measures-refle/index.html#kpb-sharp-threshold-window).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The KKL inequality under p-biased measures: reflection and threshold consequences](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-under-p-biased-measures-refle/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-under-p-biased-measures-refle)
