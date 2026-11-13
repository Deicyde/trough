---
declaration: theorem
origin: cited
lean: ZetaZeros.simple_proportion_d4
statement: formalized
proof: formalized
---

# Simple zeros of the Riemann zeta function

> Formalizes Lamzouri's Hilbert-space proof of lower bounds for simple and distinct zeros of the Riemann zeta function. From explicit Riemann--von Mangoldt and unconditional pair-correlation hypotheses, the development proves that eventually more than 67.25% of nontrivial zeros are simple and on the critical line and more than 83.625% are distinct. It includes the finite-multiset Hilbert-space inequality, zeta-zero multiplicity symmetries, an admissible cutoff construction, and certified trigonometric estimates.

*Quoted from the card [LeanPool/projects/zeta-zeros.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/zeta-zeros.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`ZetaZeros.simple_proportion_d4`](https://leanpool.github.io/lean-pool/LeanPool/ZetaZeros/Main.html#ZetaZeros.simple_proportion_d4) (theorem; a main declaration), declared in [LeanPool/ZetaZeros/Main.lean, line 110](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ZetaZeros/Main.lean#L110): “Assuming the stated Riemann--von Mangoldt and unconditional pair-correlation formulas, beyond some height more than 67.25% of nontrivial zeta zeros are simple and lie on the critical line.”
- [`ZetaZeros.distinct_proportion_d5`](https://leanpool.github.io/lean-pool/LeanPool/ZetaZeros/Main.html#ZetaZeros.distinct_proportion_d5) (theorem), declared in [LeanPool/ZetaZeros/Main.lean, line 129](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ZetaZeros/Main.lean#L129): “Under the same two explicit analytic hypotheses, beyond some height more than 83.625% of nontrivial zeta zeros are distinct.”
- [`ZetaZeros.card_simpleRealPart_lower`](https://leanpool.github.io/lean-pool/LeanPool/ZetaZeros/Hilbert/AlphaExpansion.html#ZetaZeros.card_simpleRealPart_lower) (theorem), declared in [LeanPool/ZetaZeros/Hilbert/AlphaExpansion.lean, line 2473](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ZetaZeros/Hilbert/AlphaExpansion.lean#L2473): “Bounds from below the number of multiplicity-one real points in a finite nonempty conjugation-invariant multiset using the squared test-kernel sum of any admissible function.”
- [`ZetaZeros.card_lower`](https://leanpool.github.io/lean-pool/LeanPool/ZetaZeros/Hilbert/AlphaExpansion.html#ZetaZeros.card_lower) (theorem), declared in [LeanPool/ZetaZeros/Hilbert/AlphaExpansion.lean, line 2603](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ZetaZeros/Hilbert/AlphaExpansion.lean#L2603): “Bounds from below the number of distinct points in a finite nonempty conjugation-invariant multiset using the same Hilbert-space kernel method.”

## Project

- Authors: Kenny Lau.
- Source: *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line* by Youness Lamzouri, [doi:10.48550/arXiv.2609.02882](https://doi.org/10.48550/arXiv.2609.02882), [arXiv:2609.02882](https://arxiv.org/abs/2609.02882).
- Project repository: [AxiomMath/ZetaZeros](https://github.com/AxiomMath/ZetaZeros), at commit [4bcaf70e](https://github.com/AxiomMath/ZetaZeros/tree/4bcaf70e544506c311d83a5a5b143a134b9fc5f7).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11M06, 11M26.
- In Lean Pool: [LeanPool/ZetaZeros](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ZetaZeros), from the card [LeanPool/projects/zeta-zeros.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/zeta-zeros.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/zeta-zeros.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/zeta-zeros.yaml)
- [Lean Pool at 701389c0: LeanPool/ZetaZeros](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ZetaZeros)
