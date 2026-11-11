---
declaration: section
origin: cited
lean: StatMech.Probability.mxd_maxE, StatMech.Probability.mxd_fiber, StatMech.Probability.mxd_fiberWeight, StatMech.Probability.mxd_var_decomp, StatMech.Probability.mxd_dampFiber, StatMech.Probability.mxd_dampFiber_le_perCoord, StatMech.Probability.mxd_logSum_gain, StatMech.Probability.mxd_martingaleHC_statement
statement: formalized
proof: formalized
---

# Decomposition of the variance by maximal element

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/decomposition-of-the-variance-by-maximal-element/index.html).

## Maximal element of a finite set

The maximal element of `S`, or an arbitrary element if `S` is empty.

Formalized by `StatMech.Probability.mxd_maxE`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/MaxElementDecomp.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/MaxElementDecomp.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/decomposition-of-the-variance-by-maximal-element/index.html#mxd-max-e).

## Nonempty subsets with a given maximal element

The nonempty subsets of `ι` whose maximal element is `e`.

Formalized by `StatMech.Probability.mxd_fiber`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/MaxElementDecomp.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/MaxElementDecomp.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/decomposition-of-the-variance-by-maximal-element/index.html#mxd-fiber).

## Fourier weight of a maximal-element fiber

The `p`-biased Fourier weight `Wₑ = ∑_{S : max S = e} f̂(S)²` of the fiber of `e`.

Formalized by `StatMech.Probability.mxd_fiberWeight`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/MaxElementDecomp.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/MaxElementDecomp.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/decomposition-of-the-variance-by-maximal-element/index.html#mxd-fiber-weight).

## Variance decomposition by maximal element

The variance of a Boolean function is the sum of the fiber weights.

Formalized by `StatMech.Probability.mxd_var_decomp`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/MaxElementDecomp.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/MaxElementDecomp.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/decomposition-of-the-variance-by-maximal-element/index.html#mxd-var-decomp).

## Noise-damped fiber weight

The noise-damped fiber weight `∑_{S : max S = e} ρ^{2|S|} f̂(S)²`.

Formalized by `StatMech.Probability.mxd_dampFiber`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/MaxElementDecomp.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/MaxElementDecomp.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/decomposition-of-the-variance-by-maximal-element/index.html#mxd-damp-fiber).

## Hypercontractive bound on the damped fiber weight

Hypercontractive bound on the damped fiber weight.

Formalized by `StatMech.Probability.mxd_dampFiber_le_perCoord`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/MaxElementDecomp.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/MaxElementDecomp.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/decomposition-of-the-variance-by-maximal-element/index.html#mxd-damp-fiber-le-per-coord).

## Log-sum estimate for the fiber weights

The variance log-sum estimate for the fiber weights against their damped versions.

Formalized by `StatMech.Probability.mxd_logSum_gain`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/MaxElementDecomp.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/MaxElementDecomp.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/decomposition-of-the-variance-by-maximal-element/index.html#mxd-log-sum-gain).

## Capped influence estimate for all $p$ in $(1/2, q)$

The capped estimate `∑_S 4 |S| (1-u)^{|S|-1} f̂(S)² ≤ δ^{u/(2-u)} ∑ₑ Infₑ` for all `p ∈ (1/2,
 q)` with `p < 1` and all `u ∈ [0, 1]`.

Formalized by `StatMech.Probability.mxd_martingaleHC_statement`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/MaxElementDecomp.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/MaxElementDecomp.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/decomposition-of-the-variance-by-maximal-element/index.html#mxd-martingale-hc-statement).

## Capped estimate implies KKL with constant 2 on $(1/2, q)$

`mxd_martingaleHC_statement q` implies `ptn_RhoOptimise q`, hence the KKL inequality with
 constant `2` on `(1/2, q)`.

Formalized by `StatMech.Probability.mxd_rhoOptimise_of_martingaleHC`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/MaxElementDecomp.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/MaxElementDecomp.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/decomposition-of-the-variance-by-maximal-element/index.html#mxd-rho-optimise-of-martingale-hc).

## Capped estimate with zero weights holds trivially

The capped estimate with all weights multiplied by `0` holds trivially.

Formalized by `StatMech.Probability.mxd_martingaleHC_c0`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/MaxElementDecomp.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/MaxElementDecomp.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/decomposition-of-the-variance-by-maximal-element/index.html#mxd-martingale-hc-c0).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Decomposition of the variance by maximal element](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/decomposition-of-the-variance-by-maximal-element/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/decomposition-of-the-variance-by-maximal-element)
