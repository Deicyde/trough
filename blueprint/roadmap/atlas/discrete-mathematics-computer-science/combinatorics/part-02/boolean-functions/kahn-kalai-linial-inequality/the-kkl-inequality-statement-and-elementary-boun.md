---
declaration: section
origin: cited
lean: StatMech.Probability.totalInfl, StatMech.Probability.maxInfl, StatMech.Probability.KKLHypercontractive, StatMech.Probability.kkl_inequality_total, StatMech.Probability.kkl_inequality_max, StatMech.Probability.kkl_hypercontractive_zero
statement: formalized
proof: formalized
---

# The KKL inequality: statement and elementary bounds

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-statement-and-elementary-boun/index.html).

## Total influence under a product weight

The total influence `∑ₑ Infₑ(g)` of `g` under the product weight `ν`.

Formalized by `StatMech.Probability.totalInfl`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLInequality.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLInequality.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-statement-and-elementary-boun/index.html#total-infl).

## Maximal influence under a product weight

The maximal influence `maxₑ Infₑ(g)` of `g` under the product weight `ν`.

Formalized by `StatMech.Probability.maxInfl`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLInequality.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLInequality.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-statement-and-elementary-boun/index.html#max-infl).

## KKL inequality with constant $c$ for the $p$-biased measure

The KKL inequality with constant `c` for the Bernoulli(`p`) product measure: for every finite
 nonempty index type `E` and every Boolean function `φ` on `{0, 1}^E`, `c · Var(φ) · log (1 /
 maxₑ Infₑ(φ)) ≤ ∑ₑ Infₑ(φ)`, with `Infₑ(φ)` the probability that `e` is pivotal.

Despite its name, this is the conclusion of the KKL theorem, not a hypercontractivity estimate.
 It holds trivially for `c = 0` (`kkl_hypercontractive_zero`) and is proved for `p = 1/2`, `c =
 2` in `fsr_pbiased_endpoint`. When `maxₑ Infₑ(φ) = 0`, `log (1 / 0) = 0` in Lean and the
 inequality is trivial.

Formalized by `StatMech.Probability.KKLHypercontractive`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLInequality.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLInequality.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-statement-and-elementary-boun/index.html#kklhypercontractive).

## Kahn–Kalai–Linial inequality

**Kahn–Kalai–Linial inequality**, total-influence form (J. Kahn, G. Kalai, N. Linial, *The
 influence of variables on Boolean functions*, FOCS 1988): under `KKLHypercontractive p c`, `c ·
 Var(φ) · log (1 / maxₑ Infₑ(φ)) ≤ ∑ₑ Infₑ(φ)`.

Formalized by `StatMech.Probability.kkl_inequality_total`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLInequality.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLInequality.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-statement-and-elementary-boun/index.html#kkl-inequality-total).

## Kahn–Kalai–Linial inequality

**Kahn–Kalai–Linial inequality**, maximal-influence form (J. Kahn, G. Kalai, N. Linial, *The
 influence of variables on Boolean functions*, FOCS 1988): under `KKLHypercontractive p c`, `c ·
 Var(φ) · log (1 / δ) ≤ |E| · δ` with `δ = maxₑ Infₑ(φ)`, so `δ` is at least of order `Var(φ) ·
 log |E| / |E|`.

Formalized by `StatMech.Probability.kkl_inequality_max`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLInequality.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLInequality.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-statement-and-elementary-boun/index.html#kkl-inequality-max).

## KKL inequality with constant 0 holds trivially

`KKLHypercontractive p 0` holds trivially, since total influence is nonnegative.

Formalized by `StatMech.Probability.kkl_hypercontractive_zero`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLInequality.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLInequality.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-statement-and-elementary-boun/index.html#kkl-hypercontractive-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The KKL inequality: statement and elementary bounds](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-statement-and-elementary-boun/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-statement-and-elementary-boun)
