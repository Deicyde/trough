---
declaration: section
origin: cited
lean: StatMech.Probability.bph_deriv, StatMech.Probability.bph_perCoord_hc, StatMech.Probability.bph_summed_hc, StatMech.Probability.bph_cap_term, StatMech.Probability.bph_cap_sum, StatMech.Probability.bph_capped_hc, StatMech.Probability.bph_RhoOptimise, StatMech.Probability.bph_rhoOptimise_zero
statement: formalized
proof: formalized
---

# Hypercontractivity applied to discrete derivatives

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-applied-to-discrete-derivativ/index.html).

## Discrete derivative in a coordinate

The discrete derivative `∂ₑ f (ω) = f(ω^{e ↦ 1}) - f(ω^{e ↦ 0})`.

Formalized by `StatMech.Probability.bph_deriv`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/BourgainPerCoord.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/BourgainPerCoord.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-applied-to-discrete-derivativ/index.html#bph-deriv).

## Bonami–Beckner applied to a discrete derivative

Bonami–Beckner applied to `∂ₑ 1_A`: `∑_{S ∋ e} ρ^{2|S \ {e}|} · 4 f̂(S)² ≤
 Infₑ(1_A)^{2/(1+ρ²)}`.

Formalized by `StatMech.Probability.bph_perCoord_hc`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/BourgainPerCoord.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/BourgainPerCoord.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-applied-to-discrete-derivativ/index.html#bph-per-coord-hc).

## Summed per-coordinate Bonami–Beckner bound

`bph_perCoord_hc` summed over all coordinates.

Formalized by `StatMech.Probability.bph_summed_hc`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/BourgainPerCoord.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/BourgainPerCoord.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-applied-to-discrete-derivativ/index.html#bph-summed-hc).

## Termwise cap $x^\theta \le \delta^{\theta-1} x$

`x^θ ≤ δ^{θ-1} x` for `0 ≤ x ≤ δ` and `θ ≥ 1`.

Formalized by `StatMech.Probability.bph_cap_term`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/BourgainPerCoord.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/BourgainPerCoord.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-applied-to-discrete-derivativ/index.html#bph-cap-term).

## Sum of influence powers capped by the maximal influence

`∑ₑ Infₑ^{θ} ≤ (maxₑ Infₑ)^{θ-1} ∑ₑ Infₑ` with `θ = 2/(1+ρ²)`.

Formalized by `StatMech.Probability.bph_cap_sum`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/BourgainPerCoord.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/BourgainPerCoord.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-applied-to-discrete-derivativ/index.html#bph-cap-sum).

## Capped per-coordinate hypercontractive estimate

The capped per-coordinate hypercontractive estimate: `∑_S 4 |S| ρ^{2(|S|-1)} f̂(S)² ≤
 δ^{2/(1+ρ²) - 1} ∑_S 4 |S| f̂(S)²`, with `δ = maxₑ Infₑ(1_A)`.

Formalized by `StatMech.Probability.bph_capped_hc`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/BourgainPerCoord.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/BourgainPerCoord.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-applied-to-discrete-derivativ/index.html#bph-capped-hc).

## Fourier-form KKL at $p = 1/2$ conditional on the capped estimate

The KKL inequality at `p = 1/2` in Fourier form, with the capped estimate `bph_capped_hc` (for
 all `ρ ∈ [0, 1]`) as a hypothesis. It holds with `c = 2` (`cro2_rhoOptimise`).

Formalized by `StatMech.Probability.bph_RhoOptimise`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/BourgainPerCoord.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/BourgainPerCoord.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-applied-to-discrete-derivativ/index.html#bph-rho-optimise).

## Conditional Fourier-form KKL holds trivially with constant zero

`bph_RhoOptimise 0` holds trivially.

Formalized by `StatMech.Probability.bph_rhoOptimise_zero`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/BourgainPerCoord.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/BourgainPerCoord.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-applied-to-discrete-derivativ/index.html#bph-rho-optimise-zero).

## Capped-estimate form of KKL implies the indicator-bound form

`bph_RhoOptimise c` implies `kls_LogOptimisation c`.

Formalized by `StatMech.Probability.bph_logOptimisation_of_rho`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/BourgainPerCoord.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/BourgainPerCoord.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-applied-to-discrete-derivativ/index.html#bph-log-optimisation-of-rho).

## KKL inequality at $p = 1/2$ from the conditional statement

`bph_RhoOptimise c` implies the KKL inequality `KKLHypercontractive (1/2) c`.

Formalized by `StatMech.Probability.bph_KKL`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/BourgainPerCoord.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/BourgainPerCoord.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-applied-to-discrete-derivativ/index.html#bph-kkl).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hypercontractivity applied to discrete derivatives](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-applied-to-discrete-derivativ/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-applied-to-discrete-derivativ)
