---
declaration: section
origin: cited
lean: MathlibExt.Probability.WaldCrossTerms.cross_pair_integral_zero, MathlibExt.Probability.WaldCrossTerms.wald_cross_terms_zero, MathlibExt.Probability.WaldCrossTerms.sum_sq_expansion, MathlibExt.Probability.WaldCrossTerms.wald_cross_terms_zero_of_bounded, MeasureTheory.wald_integrable_stopped_sum, MeasureTheory.wald_equation, MathlibExt.Probability.WaldDiagonalTerms.integrable_stopped_sum_sq_diag, MathlibExt.Probability.WaldDiagonalTerms.wald_diagonal_terms
statement: formalized
proof: formalized
---

# Wald's equations

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/wald-s-equations/index.html).

## Vanishing of a single cross term in Wald's second equation

A single cross term `E[X_j · X_i · 1_{T > i}]` (with `j < i`) vanishes
when the `X_i` are identically distributed with zero mean and `X_i` is independent of
`(X_j, 1_{T > i})`.

Formalized by `MathlibExt.Probability.WaldCrossTerms.cross_pair_integral_zero`, a theorem declared in [MathlibExt/Probability/WaldCrossTerms.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/WaldCrossTerms.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/wald-s-equations/index.html#cross-pair-integral-zero).

## Vanishing of the cross terms in Wald's second equation

The full cross-term contribution to `E[(S_T)^2]` vanishes:
`E[∑_{i < T} ∑_{j < i} X_j X_i] = 0` for identically distributed, mean-zero variables,
with each `X_i` independent of the filtration at time `i` and measurable at time
`i + 1`, given absolute summability of the stopped cross-term series.

Formalized by `MathlibExt.Probability.WaldCrossTerms.wald_cross_terms_zero`, a theorem declared in [MathlibExt/Probability/WaldCrossTerms.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/WaldCrossTerms.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/wald-s-equations/index.html#wald-cross-terms-zero).

## Square of a finite sum as diagonal plus cross terms

Algebraic identity expanding the square of a finite sum into diagonal and
cross-term contributions: `(∑_{i<n} f i)^2 = ∑_{i<n} (f i)^2 + 2 ∑_{i<n} ∑_{j<i} f j · f i`.

Formalized by `MathlibExt.Probability.WaldCrossTerms.sum_sq_expansion`, a theorem declared in [MathlibExt/Probability/WaldCrossTerms.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/WaldCrossTerms.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/wald-s-equations/index.html#sum-sq-expansion).

## Cross terms vanish for a bounded stopping time

The total cross-term contribution vanishes for a stopping time bounded
by a constant, with no extra summability or measurability hypotheses:
the sums are finite, and every term past the bound is zero.

Formalized by `MathlibExt.Probability.WaldCrossTerms.wald_cross_terms_zero_of_bounded`, a theorem declared in [MathlibExt/Probability/WaldCrossTerms.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/WaldCrossTerms.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/wald-s-equations/index.html#wald-cross-terms-zero-of-bounded).

## Integrability of the stopped sum in Wald's equation

Under Wald's hypotheses, the stopped sum is integrable. This reuses
Wald's summable `L¹` series and applies Mathlib's sum measurability and norm bound.

Formalized by `MeasureTheory.wald_integrable_stopped_sum`, a theorem declared in [MathlibExt/Probability/WaldEquation.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/WaldEquation.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/wald-s-equations/index.html#wald-integrable-stopped-sum).

## Wald's equation

Let `Xᵢ` be identically distributed integrable real
random variables and `T` a stopping time with `E T < ∞`, with each `Xₖ`
independent of the filtration at time `k`. Then `E[S_T] = E[X₁] · E[T]`,
where `S_T = ∑_{i < T} Xᵢ`.

Formalized by `MeasureTheory.wald_equation`, a theorem declared in [MathlibExt/Probability/WaldEquation.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/WaldEquation.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/wald-s-equations/index.html#wald-equation).

## Integrability of the stopped sum of squares

The stopped sum of squares is integrable under the stated diagonal hypotheses.

Formalized by `MathlibExt.Probability.WaldDiagonalTerms.integrable_stopped_sum_sq_diag`, a theorem declared in [MathlibExt/Probability/WaldDiagonalTerms.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/WaldDiagonalTerms.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/wald-s-equations/index.html#integrable-stopped-sum-sq-diag).

## Diagonal identity in Wald's second equation

Wald's equation applied to the squared increments gives the diagonal identity.

Formalized by `MathlibExt.Probability.WaldDiagonalTerms.wald_diagonal_terms`, a theorem declared in [MathlibExt/Probability/WaldDiagonalTerms.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/WaldDiagonalTerms.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/wald-s-equations/index.html#wald-diagonal-terms).

## Wald's second equation

Let $(\Omega, \mathbb{P})$ be a probability space with a filtration
$(\mathcal{F}_k)_{k \ge 0}$, and let $X_0, X_1, \dots$ be identically distributed real random
variables with $\mathbb{E}|X_0| < \infty$, $\mathbb{E}[X_0] = 0$ and $\mathbb{E}[X_0^2] < \infty$.
Let $T$ be an $\mathbb{N}$-valued stopping time for $(\mathcal{F}_k)$ with $\mathbb{E}[T] < \infty$.
Suppose each $X_k$ is independent of $\mathcal{F}_k$ and is $\mathcal{F}_{k+1}$-measurable. Then
$\mathbb{E}\big[\big(\sum_{i < T} X_i\big)^2\big] = \mathbb{E}[X_0^2] \cdot \mathbb{E}[T]$.

Formalized by `MeasureTheory.wald_second_equation`, a theorem declared in [MathlibExt/Probability/WaldSecondEquation.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/WaldSecondEquation.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/wald-s-equations/index.html#wald-second-equation).

## Predictable filtration of a sequence

The "predictable" filtration associated to a sequence `X : ℕ → Ω → ℝ`:
`ℱ_k = σ(X_0, …, X_{k-1})`. Ported verbatim from v1 `WaldSecondEquation.lean`.

Formalized by `MathlibExt.Probability.StoppedSumMaximal.predictableFiltration`, a definition declared in [MathlibExt/Probability/StoppedSumMaximal.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/StoppedSumMaximal.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/wald-s-equations/index.html#predictable-filtration).

## Predictable filtration at time zero is trivial

The predictable filtration contains no observations at time zero.

Formalized by `MathlibExt.Probability.StoppedSumMaximal.predictableFiltration_zero`, a theorem declared in [MathlibExt/Probability/StoppedSumMaximal.lean, line 374](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/StoppedSumMaximal.lean#L374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/wald-s-equations/index.html#predictable-filtration-zero).

## Successor step of the predictable filtration

A successor step adds exactly the next observation to the predictable filtration.

Formalized by `MathlibExt.Probability.StoppedSumMaximal.predictableFiltration_succ`, a theorem declared in [MathlibExt/Probability/StoppedSumMaximal.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/StoppedSumMaximal.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/wald-s-equations/index.html#predictable-filtration-succ).

## Square-integrability of a stopped partial sum

**Square-integrability of a stopped partial sum**, general-filtration form.

Formalized by `MathlibExt.Probability.StoppedSumMaximal.integrable_stopped_partialSum_sq`, a theorem declared in [MathlibExt/Probability/StoppedSumMaximal.lean, line 410](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/StoppedSumMaximal.lean#L410). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/wald-s-equations/index.html#integrable-stopped-partial-sum-sq).

## Square-integrability of the maximal stopped partial sum

**Square-integrability of the maximal stopped partial sum**, in v1's form:
`max_{0 ≤ k ≤ T} Sₖ²` is integrable. This is v1's
`integrable_maximal_stopped_partial_sum_sq`, whose proof in v1 was left unproved.

Formalized by `MathlibExt.Probability.StoppedSumMaximal.integrable_maximal_stopped_partial_sum_sq`, a theorem declared in [MathlibExt/Probability/StoppedSumMaximal.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/StoppedSumMaximal.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/wald-s-equations/index.html#integrable-maximal-stopped-partial-sum-s).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Wald's equations](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/wald-s-equations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/martingales/wald-s-equations)
