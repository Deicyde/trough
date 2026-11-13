---
declaration: theorem
origin: cited
lean: LeanPool.CencovPetz.MonotoneMetricFamily.eq_smul_fisher_of_continuous
statement: formalized
proof: formalized
---

# Finite Čencov-Petz Uniqueness

> Formalizes the finite/discrete Čencov-Petz uniqueness theorem, showing that any continuous metric family on finite probability simplexes that is monotone under Markov morphisms is a scalar multiple of the Fisher information metric.

*Quoted from the card [LeanPool/projects/cencov-petz.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/cencov-petz.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LeanPool.CencovPetz.MonotoneMetricFamily.eq_smul_fisher_of_continuous`](https://leanpool.github.io/lean-pool/LeanPool/CencovPetz/CencovFinite.html#LeanPool.CencovPetz.MonotoneMetricFamily.eq_smul_fisher_of_continuous) (theorem; a main declaration), declared in [LeanPool/CencovPetz/CencovFinite.lean, line 46](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CencovPetz/CencovFinite.lean#L46): “Proves that every continuous monotone metric family on a finite probability simplex is a scalar multiple of the Fisher information metric.” Its source, as the card gives it: “N. N. Chentsov, Statistical Decision Rules and Optimal Inference, AMS Translations of Mathematical Monographs 53, 1982.”
- [`LeanPool.CencovPetz.MonotoneMetricFamily.eq_smul_fisher_of_isRational`](https://leanpool.github.io/lean-pool/LeanPool/CencovPetz/CencovSplitPoint.html#LeanPool.CencovPetz.MonotoneMetricFamily.eq_smul_fisher_of_isRational) (theorem), declared in [LeanPool/CencovPetz/CencovSplitPoint.lean, line 225](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CencovPetz/CencovSplitPoint.lean#L225): “Establishes the scalar Fisher-form identity at rational simplex points using split representations.”
- [`LeanPool.CencovPetz.MonotoneMetricFamily.eq_smul_fisher_of_isSplitRepresentable`](https://leanpool.github.io/lean-pool/LeanPool/CencovPetz/CencovSplitPoint.html#LeanPool.CencovPetz.MonotoneMetricFamily.eq_smul_fisher_of_isSplitRepresentable) (theorem), declared in [LeanPool/CencovPetz/CencovSplitPoint.lean, line 48](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CencovPetz/CencovSplitPoint.lean#L48): “Proves the scalar Fisher-form identity for simplex points represented as pushforwards of uniform distributions under splitting maps.”
- [`LeanPool.CencovPetz.MonotoneMetricFamily.uniformScalar_eq_uniformScalar_two`](https://leanpool.github.io/lean-pool/LeanPool/CencovPetz/UniformScalarConstant.html#LeanPool.CencovPetz.MonotoneMetricFamily.uniformScalar_eq_uniformScalar_two) (theorem), declared in [LeanPool/CencovPetz/UniformScalarConstant.lean, line 220](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CencovPetz/UniformScalarConstant.lean#L220): “Shows that the uniform-point scalar is independent of simplex dimension once the dimension is at least two.”
- [`LeanPool.CencovPetz.TangentFin.Bilin.B_eq_smul_fisherBilin_uniform`](https://leanpool.github.io/lean-pool/LeanPool/CencovPetz/UniformScalarMultiple.html#LeanPool.CencovPetz.TangentFin.Bilin.B_eq_smul_fisherBilin_uniform) (lemma), declared in [LeanPool/CencovPetz/UniformScalarMultiple.lean, line 366](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CencovPetz/UniformScalarMultiple.lean#L366): “Proves that the permutation-invariant bilinear form at a uniform finite simplex point is a scalar multiple of the Fisher bilinear form.”

## Project

- Authors: Adam Benenson.
- Source: *Statistical Decision Rules and Optimal Inference* by N. N. Chentsov, [https://bookstore.ams.org/mmono-53](https://bookstore.ams.org/mmono-53).
- Project repository: [abenenson/cencov-petz](https://github.com/abenenson/cencov-petz).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 62B10, 53C21.
- In Lean Pool: [LeanPool/CencovPetz](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CencovPetz), from the card [LeanPool/projects/cencov-petz.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/cencov-petz.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/cencov-petz.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/cencov-petz.yaml)
- [Lean Pool at 701389c0: LeanPool/CencovPetz](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CencovPetz)
