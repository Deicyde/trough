---
declaration: section
origin: cited
lean: StatMech.Probability.esd_Phi, StatMech.Probability.esd_Phi_eq_neg_negMulLog, StatMech.Probability.esd_ent, StatMech.Probability.esd_entCoord, StatMech.Probability.esd_PosWeight, StatMech.Probability.esd_dpi, StatMech.Probability.esd_subadditivity
statement: formalized
proof: formalized
---

# Sub-additivity of entropy for Bernoulli product measures

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/sub-additivity-of-entropy-for-bernoulli-product/index.html).

## Function $x \log x$ with $0 \log 0 = 0$

The function `x ↦ x log x` (with `0 log 0 = 0`). It equals `-Real.negMulLog x`
 (`esd_Phi_eq_neg_negMulLog`).

Formalized by `StatMech.Probability.esd_Phi`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/EntropySubadd.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/EntropySubadd.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/sub-additivity-of-entropy-for-bernoulli-product/index.html#esd-phi).

## $x \log x$ is the negation of Mathlib's $-x \log x$

`esd_Phi` is the negative of Mathlib's `Real.negMulLog`.

Formalized by `StatMech.Probability.esd_Phi_eq_neg_negMulLog`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/EntropySubadd.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/EntropySubadd.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/sub-additivity-of-entropy-for-bernoulli-product/index.html#esd-phi-eq-neg-neg-mul-log).

## Entropy of a function under a product weight

The entropy `Ent_ν(g) = 𝔼_ν[g log g] - 𝔼_ν[g] log 𝔼_ν[g]` of `g` under the product weight `ν`.

Formalized by `StatMech.Probability.esd_ent`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/EntropySubadd.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/EntropySubadd.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/sub-additivity-of-entropy-for-bernoulli-product/index.html#esd-ent).

## Conditional entropy in one coordinate

The conditional entropy of `g` in coordinate `e` given the other coordinates, under the
 Bernoulli(`p`) weight: `p Φ(g(ω^{e↦1})) + (1-p) Φ(g(ω^{e↦0})) - Φ(𝔼[g | ω_{≠e}])`, with `Φ(x) =
 x log x`.

Formalized by `StatMech.Probability.esd_entCoord`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/EntropySubadd.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/EntropySubadd.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/sub-additivity-of-entropy-for-bernoulli-product/index.html#esd-ent-coord).

## Strictly positive coordinate weights

Every coordinate weight of `ν` is strictly positive.

Formalized by `StatMech.Probability.esd_PosWeight`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/EntropySubadd.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/EntropySubadd.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/sub-additivity-of-entropy-for-bernoulli-product/index.html#esd-pos-weight).

## Data-processing inequality for entropy under a two-point mixture

Data-processing inequality for entropy under a two-point mixture: for nonnegative `g₀, g₁`, `p
 Φ(𝔼 g₁) + (1-p) Φ(𝔼 g₀) - Φ(p 𝔼 g₁ + (1-p) 𝔼 g₀) ≤ 𝔼[p Φ(g₁) + (1-p) Φ(g₀) - Φ(p g₁ + (1-p)
 g₀)]`.

Formalized by `StatMech.Probability.esd_dpi`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/EntropySubadd.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/EntropySubadd.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/sub-additivity-of-entropy-for-bernoulli-product/index.html#esd-dpi).

## Sub-additivity (tensorization) of entropy

**Sub-additivity (tensorization) of entropy** for the Bernoulli(`p`) product measure on `{0,
 1}^n` (see S. Boucheron, G. Lugosi, P. Massart, *Concentration Inequalities*, 2013, Theorem
 4.10): for nonnegative `g`, `Ent(g) ≤ ∑ₑ 𝔼[Entₑ(g)]`.

Formalized by `StatMech.Probability.esd_subadditivity`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/EntropySubadd.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/EntropySubadd.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/sub-additivity-of-entropy-for-bernoulli-product/index.html#esd-subadditivity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sub-additivity of entropy for Bernoulli product measures](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/sub-additivity-of-entropy-for-bernoulli-product/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/sub-additivity-of-entropy-for-bernoulli-product)
