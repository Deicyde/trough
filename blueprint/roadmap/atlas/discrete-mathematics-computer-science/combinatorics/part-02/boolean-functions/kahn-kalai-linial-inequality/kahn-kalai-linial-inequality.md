---
declaration: section
origin: cited
lean: MathlibExt.Complexity.BooleanFunctions.KKLPBiasedWanted.kkl_pbiased
statement: formalized
---

# Kahn–Kalai–Linial inequality: its own results

1 result, 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/index.html).

## KKL inequality for `p`-biased measures

**KKL inequality for `p`-biased measures** (Bourgain–Kahn–Kalai–Katznelson–Linial;
Talagrand). For every `p ∈ (0, 1)` there is `c > 0` such that for every finite nonempty `E` and
every Boolean function `φ` on `{0, 1}^E`,
`c · Var_p(φ) · log (1 / maxₑ Infₑ^p(φ)) ≤ ∑ₑ Infₑ^p(φ)`, where `Infₑ^p(φ)` is the probability
under the Bernoulli(`p`) product measure that `e` is pivotal for `φ`.

Talagrand's inequality `Var_p(φ) ≤ K(p) ∑ₑ Infₑ / log (1 / (p (1 - p) Infₑ))` gives this with
`c = 1 / K(p)`, since each `Infₑ ≤ maxₑ Infₑ`.

## Sources

- M. Talagrand, *On Russo's approximate zero-one law*, Ann. Probab. 22 (1994); J. Bourgain, J. Kahn, G. Kalai, Y. Katznelson, N. Linial, *The influence of variables in product spaces*, Israel J. Math. 77 (1992).

Stated but not proved: `MathlibExt.Complexity.BooleanFunctions.KKLPBiasedWanted.kkl_pbiased` is written with `theorem_wanted` in [WantedExt/Complexity/BooleanFunctions/KKLPBiasedWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/BooleanFunctions/KKLPBiasedWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/index.html#kkl-pbiased).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kahn–Kalai–Linial inequality](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality)
