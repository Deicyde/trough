---
declaration: theorem
origin: cited
lean: HypergraphLowerBound.thm_main_H_lower_bound
statement: formalized
proof: formalized
---

# FrontierMath Ramsey Hypergraphs

> Formalizes lower bounds for the Brian-Larson hypergraph extremal function H(n), including a uniform 26/25 improvement over the recursive benchmark k_n for n ≥ 15 and a Lubell-frame asymptotic lower bound.

*Quoted from the card [LeanPool/projects/frontiermath-open-hypergraphs.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/frontiermath-open-hypergraphs.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 7 main results, each with its informal statement quoted from the card. The scan finds 7 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`HypergraphLowerBound.thm_main_H_lower_bound`](https://leanpool.github.io/lean-pool/LeanPool/FrontierMathOpenHypergraphs/Uniform.html#HypergraphLowerBound.thm_main_H_lower_bound) (theorem; a main declaration), declared in [LeanPool/FrontierMathOpenHypergraphs/Uniform.lean, line 2487](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FrontierMathOpenHypergraphs/Uniform.lean#L2487): “Proves H(n) ≥ 26 \* k(n) / 25 for every n ≥ 15.” Its source, as the card gives it: “Epoch AI FrontierMath, A Ramsey-style Problem on Hypergraphs.”
- [`HypergraphLowerBound.uniform_26_25`](https://leanpool.github.io/lean-pool/LeanPool/FrontierMathOpenHypergraphs/Uniform.html#HypergraphLowerBound.uniform_26_25) (theorem), declared in [LeanPool/FrontierMathOpenHypergraphs/Uniform.lean, line 702](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FrontierMathOpenHypergraphs/Uniform.lean#L702): “Proves the uniform recursive construction bound A(n) ≥ 26 \* k(n) / 25 for every n ≥ 15.”
- [`HypergraphLowerBound.frame_recurrence`](https://leanpool.github.io/lean-pool/LeanPool/FrontierMathOpenHypergraphs/Substitution.html#HypergraphLowerBound.frame_recurrence) (theorem), declared in [LeanPool/FrontierMathOpenHypergraphs/Substitution.lean, line 705](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FrontierMathOpenHypergraphs/Substitution.lean#L705): “The substitution-frame recurrence that combines block witnesses and a valid support frame into a larger witness.”
- [`HypergraphLowerBound.lubell_is_frame`](https://leanpool.github.io/lean-pool/LeanPool/FrontierMathOpenHypergraphs/Lubell.html#HypergraphLowerBound.lubell_is_frame) (theorem), declared in [LeanPool/FrontierMathOpenHypergraphs/Lubell.lean, line 526](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FrontierMathOpenHypergraphs/Lubell.lean#L526): “Proves that the Lubell support family forms a valid frame for every arity t ≥ 2.”
- [`HypergraphLowerBound.fixed_t_bound`](https://leanpool.github.io/lean-pool/LeanPool/FrontierMathOpenHypergraphs/Lubell.html#HypergraphLowerBound.fixed_t_bound) (theorem), declared in [LeanPool/FrontierMathOpenHypergraphs/Lubell.lean, line 1264](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FrontierMathOpenHypergraphs/Lubell.lean#L1264): “Derives a fixed-t lower bound for the exact witness supremum from Lubell frames.”
- [`HypergraphLowerBound.asymptotic_lower_bound`](https://leanpool.github.io/lean-pool/LeanPool/FrontierMathOpenHypergraphs/Lubell.html#HypergraphLowerBound.asymptotic_lower_bound) (theorem), declared in [LeanPool/FrontierMathOpenHypergraphs/Lubell.lean, line 1935](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FrontierMathOpenHypergraphs/Lubell.lean#L1935): “Proves the asymptotic lower bound liminf H(n) / k(n) ≥ 2 \* log 2.”
- [`HypergraphLowerBound.thm_asymptotic`](https://leanpool.github.io/lean-pool/LeanPool/FrontierMathOpenHypergraphs/Lubell.html#HypergraphLowerBound.thm_asymptotic) (theorem), declared in [LeanPool/FrontierMathOpenHypergraphs/Lubell.lean, line 2012](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FrontierMathOpenHypergraphs/Lubell.lean#L2012): “States the asymptotic consequence in terms of H(n) divided by n log n.”

## Project

- Authors: Dean Cureton.
- Source: *Choosing between incompatible ideals* by Will Brian, Paul B. Larson, [doi:10.1016/j.ejc.2021.103349](https://doi.org/10.1016/j.ejc.2021.103349), [arXiv:1908.10914](https://arxiv.org/abs/1908.10914).
- Project repository: [math-inc/FrontierMathOpen-Hypergraphs](https://github.com/math-inc/FrontierMathOpen-Hypergraphs).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C65, 05D10, 03E02.
- In Lean Pool: [LeanPool/FrontierMathOpenHypergraphs](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FrontierMathOpenHypergraphs), from the card [LeanPool/projects/frontiermath-open-hypergraphs.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/frontiermath-open-hypergraphs.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/frontiermath-open-hypergraphs.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/frontiermath-open-hypergraphs.yaml)
- [Lean Pool at 701389c0: LeanPool/FrontierMathOpenHypergraphs](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FrontierMathOpenHypergraphs)
