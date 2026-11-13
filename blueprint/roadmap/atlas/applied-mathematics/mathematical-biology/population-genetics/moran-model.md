---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Moran.moranUp, MathlibExt.Biology.PopulationGenetics.Moran.moranDown, MathlibExt.Biology.PopulationGenetics.Moran.moranFixation, MathlibExt.Biology.PopulationGenetics.Moran.moranProb, MathlibExt.Biology.PopulationGenetics.Moran.moranUp_last, MathlibExt.Biology.PopulationGenetics.Moran.moranDown_zero, MathlibExt.Biology.PopulationGenetics.Moran.mul_moranDown, MathlibExt.Biology.PopulationGenetics.Moran.moranUp_nonneg
statement: formalized
proof: formalized
---

# Moran model

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html).

## Up-step probability of the Moran process

Probability that one step of the Moran process with `N` individuals and mutant relative
fitness `r` takes the mutant count from `i` to `i + 1`: a mutant is chosen to reproduce
(probability `r i / (r i + N - i)`) and a wild type is chosen to die (probability
`(N - i) / N`). Meaningful for `0 < r` and `i ≤ N` (the real subtraction `N - i` is negative
for `i > N`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Moran.moranUp`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Moran.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Moran.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html#moran-up).

## Down-step probability of the Moran process

Probability that one step of the Moran process takes the mutant count from `i` to `i - 1`:
a wild type is chosen to reproduce (probability `(N - i) / (r i + N - i)`) and a mutant is
chosen to die (probability `i / N`). Meaningful for `0 < r` and `i ≤ N`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Moran.moranDown`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Moran.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Moran.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html#moran-down).

## Fixation probability of the Moran process

The fixation probability of the Moran process started from `i` mutants out of `N`:
`(1 - r⁻¹ ^ i) / (1 - r⁻¹ ^ N)` for `r ≠ 1`, and `i / N` in the neutral case `r = 1`.
The model's domain is `0 < r`, `N ≥ 1`, `i ≤ N`; outside it the value is the closed formula
evaluated with Lean's total division (e.g. `x / 0 = 0`) and carries no meaning.

Formalized by `MathlibExt.Biology.PopulationGenetics.Moran.moranFixation`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Moran.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Moran.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html#moran-fixation).

## One-step transition probabilities of the Moran process

One-step transition probabilities of the Moran process on the states `Fin (N + 1)`:
`a_i` to `i + 1`, `b_i` to `i - 1`, `1 - a_i - b_i` to `i`, and `0` elsewhere.

Formalized by `MathlibExt.Biology.PopulationGenetics.Moran.moranProb`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Moran.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Moran.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html#moran-prob).

## No up-step from the fixed state of the Moran process

No mutant can be added when the mutant type is fixed.

Formalized by `MathlibExt.Biology.PopulationGenetics.Moran.moranUp_last`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Moran.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Moran.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html#moran-up-last).

## No down-step from the empty state of the Moran process

No mutant can be removed when the mutant type is absent.

Formalized by `MathlibExt.Biology.PopulationGenetics.Moran.moranDown_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Moran.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Moran.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html#moran-down-zero).

## Ratio of Moran down- and up-step probabilities

The ratio of the down- and up-step probabilities is `1 / r`: `r · b_i = a_i`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Moran.mul_moranDown`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Moran.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Moran.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html#mul-moran-down).

## Nonnegativity of the Moran up-step probability

The up-step probability is nonnegative on the states `0 ≤ i ≤ N`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Moran.moranUp_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Moran.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Moran.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html#moran-up-nonneg).

## Nonnegativity of the Moran down-step probability

The down-step probability is nonnegative on the states `0 ≤ i ≤ N`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Moran.moranDown_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Moran.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Moran.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html#moran-down-nonneg).

## Moran up- and down-step probabilities sum to at most one

On the states `0 ≤ i ≤ N` the up- and down-step probabilities sum to at most `1`, so
the probability `1 - a_i - b_i` of staying is nonnegative.

Formalized by `MathlibExt.Biology.PopulationGenetics.Moran.moranUp_add_moranDown_le_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Moran.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Moran.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html#moran-up-add-moran-down-le-one).

## One-step expectation under the Moran process

One-step expectation of a function `f` of the mutant count from state `i`:
`∑ j, P i j f j = a_i f (i + 1) + b_i f (i - 1) + (1 - a_i - b_i) f i` (the boundary terms
vanish at `i = 0` and `i = N`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Moran.sum_moranProb_mul`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Moran.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Moran.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html#sum-moran-prob-mul).

## Moran process as a stochastic matrix

The Moran process with `N` individuals and mutant relative fitness `r > 0`, as a stochastic
matrix on the mutant counts `Fin (N + 1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Moran.moranMatrix`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Moran.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Moran.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html#moran-matrix).

## An absent mutant is never fixed

A mutant that is absent is never fixed: `φ_0 = 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Moran.moranFixation_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Moran.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Moran.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html#moran-fixation-zero).

## A fixed mutant stays fixed

A mutant that is already fixed stays fixed: `φ_N = 1` (for `N ≠ 0`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Moran.moranFixation_self`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Moran.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Moran.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html#moran-fixation-self).

## First-step equation (Moran 1958)

The fixation probability satisfies
`φ_i = a_i φ_{i+1} + b_i φ_{i-1} + (1 - a_i - b_i) φ_i`. This is the first-step equation of the
chain for the interior states `0 < i < N`; the identity is algebraic (it follows from
`r · b_i = a_i`), so it is stated for every `i ≥ 1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Moran.moranFixation_eq_firstStep`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Moran.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Moran.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html#moran-fixation-eq-first-step).

## Uniqueness of the fixation probability

Any `ψ` with `ψ 0 = 0`, `ψ N = 1` that satisfies
the first-step equation `ψ i = a_i ψ (i+1) + b_i ψ (i-1) + (1 - a_i - b_i) ψ i` at every
`0 < i < N` equals `moranFixation r N` on `0 ≤ i ≤ N`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Moran.eq_moranFixation`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Moran.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Moran.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html#eq-moran-fixation).

## Fixation probability of the chain

For `N ≠ 0`, the probability that the Moran chain
started at `i` is in state `N` after `t` steps tends to `φ_i` as `t → ∞`. Since `N` absorbs,
this `t`-step probability is the probability of fixation by time `t`, so its limit is the
probability of eventual fixation.

Formalized by `MathlibExt.Biology.PopulationGenetics.Moran.tendsto_matPow_moranMatrix_last`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Moran.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Moran.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html#tendsto-mat-pow-moran-matrix-last).

## Loss probability of the chain

For `N ≠ 0`, the probability that the Moran chain
started at `i` is in state `0` after `t` steps tends to `1 - φ_i`; together with
`tendsto_matPow_moranMatrix_last`, absorption at `0` or `N` is certain.

Formalized by `MathlibExt.Biology.PopulationGenetics.Moran.tendsto_matPow_moranMatrix_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Moran.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Moran.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html#tendsto-mat-pow-moran-matrix-zero).

## Closed form of Kimura's fixation probability

Kimura's diffusion fixation probability at scaled selection `σ / 2` is
`(1 - e^{-σ x}) / (1 - e^{-σ})` (for `σ ≠ 0`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Moran.kimuraFixation_half`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Moran.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Moran.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html#kimura-fixation-half).

## Diffusion limit of the Moran fixation probability

With relative fitness
`r_N = 1 + σ / N` and initial count `i_N = ⌊x N⌋`, the fixation probability `φ^{(N)}_{i_N}`
tends to Kimura's `kimuraFixation (σ / 2) x`, which is `(1 - e^{-σ x}) / (1 - e^{-σ})` for
`σ ≠ 0` (`kimuraFixation_half`) and `x` for `σ = 0`. The initial frequency `x` is meaningful in
`[0, 1]`; the limit of the closed formula holds for every `x ≥ 0`, so only `0 ≤ x` is assumed
(for negative `x`, `⌊x N⌋₊ = 0` is a junk value of the truncated floor).

Formalized by `MathlibExt.Biology.PopulationGenetics.Moran.tendsto_moranFixation_diffusion`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Moran.lean, line 470](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Moran.lean#L470). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html#tendsto-moran-fixation-diffusion).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Moran model](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/moran-model/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/population-genetics/moran-model)
