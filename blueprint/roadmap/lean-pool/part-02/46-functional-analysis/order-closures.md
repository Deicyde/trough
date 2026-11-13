---
declaration: theorem
origin: cited
lean: OrderClosures.exists_weaklyFatou_not_equivalent_fatou
statement: formalized
proof: formalized
---

# Order closure, order adherence and Fatou norms

> Formalizes order and unbounded-order adherence in vector lattices, the Gao-Leung characterization of order-continuous norms on sigma-order-complete Banach lattices, and the Solovay/Stone-space construction of order-complete C(K) spaces with arbitrarily large density and norm-closed separable sublattices whose only order-closed vector-sublattice extension is the whole C(K) space. Constructs solid sets with a prescribed infinite number kappa of solid generators whose adherence towers are strict below any ordinal at most kappa's successor cardinal. Constructs a complete weakly Fatou lattice norm with constant 2 that is not equivalent to any Fatou lattice norm. Includes reusable vector-lattice, net-convergence, sublattice, seminorm, Boolean-algebra and transfinite-iteration infrastructure.

*Quoted from the card [LeanPool/projects/order-closures.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/order-closures.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`OrderClosures.gaoLeung_orderContinuous_characterization`](https://leanpool.github.io/lean-pool/LeanPool/OrderClosures/GaoLeungCharacterization.html#OrderClosures.gaoLeung_orderContinuous_characterization) (theorem), declared in [LeanPool/OrderClosures/GaoLeungCharacterization.lean, line 1012](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/OrderClosures/GaoLeungCharacterization.lean#L1012): “For a sigma-order-complete Banach lattice X, the following are equivalent: every vector sublattice has order-closed order adherence; every vector sublattice has equal order and unbounded-order adherence; and the norm of X is order continuous.” Its source, as the card gives it: “Paper Theorem 1.1, recalling Gao-Leung Theorem 2.7.”
- [`OrderClosures.gao_counterexample`](https://leanpool.github.io/lean-pool/LeanPool/OrderClosures/GaoLeungProblem/Counterexample.html#OrderClosures.gao_counterexample) (theorem), declared in [LeanPool/OrderClosures/GaoLeungProblem/Counterexample.lean, line 45](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/OrderClosures/GaoLeungProblem/Counterexample.lean#L45): “For every cardinal kappa there is a compact Hausdorff space K such that C(K, R) is order complete and has density at least kappa, with a norm-closed separable vector sublattice Y whose only order-closed vector-sublattice extension is all of C(K, R).” Its source, as the card gives it: “Paper Proposition 2.1, via the Solovay Boolean algebra.”
- [`OrderClosures.solid_sets_require_arbitrarily_many_iterations`](https://leanpool.github.io/lean-pool/LeanPool/OrderClosures/GaoLeungProblem/Iterations.html#OrderClosures.solid_sets_require_arbitrarily_many_iterations) (theorem), declared in [LeanPool/OrderClosures/GaoLeungProblem/Iterations.lean, line 625](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/OrderClosures/GaoLeungProblem/Iterations.lean#L625): “For every infinite cardinal kappa and ordinal xi at most the initial ordinal of kappa's successor cardinal, there is a vector lattice and a solid set with solid generator number kappa whose order-adherence tower has a proper step at every stage below xi. The witness and cardinal/ordinal parameters are lifted one universe in Lean.” Its source, as the card gives it: “Paper Theorem 2.6, with its explicit infinite-cardinal hypothesis. Lean strengthens the stated size-kappa generating-set conclusion to minimum solid generator number exactly kappa; this exact-minimum conclusion is proved in the formalization, not stated in the paper.”
- [`OrderClosures.exists_weaklyFatou_not_equivalent_fatou`](https://leanpool.github.io/lean-pool/LeanPool/OrderClosures/WeaklyFatou/FinalSpace.html#OrderClosures.exists_weaklyFatou_not_equivalent_fatou) (theorem; a main declaration), declared in [LeanPool/OrderClosures/WeaklyFatou/FinalSpace.lean, line 588](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/OrderClosures/WeaklyFatou/FinalSpace.lean#L588): “There is a real vector lattice with a complete lattice norm p satisfying the weak Fatou property with constant 2, such that no lattice norm q with the Fatou property is equivalent to p. Norms, completeness and equivalence are represented explicitly by PaperLatticeNorm, IsCompleteFor and EquivalentNorms.” Its source, as the card gives it: “Paper Theorem 3.1; self-contained construction of the result previously announced by Anthony Wickstead and credited to Michael Elliott. The paper credits Jaume de Dios Pont for an earlier Lean formalization of this result.”

## Project

- Authors: Antonio Avilés, Mitchell A. Taylor, Pedro Tradacete, David Muñoz-Lahoz.
- Source: *Order closure, order adherence and Fatou norms*, [arXiv:2609.06689](https://arxiv.org/abs/2609.06689).
- Project repository: [pedrotradacete/OrderClosures](https://github.com/pedrotradacete/OrderClosures), at commit [6189ba71](https://github.com/pedrotradacete/OrderClosures/tree/6189ba7134f6975e7d8e4c8c093a9869d03a769c).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 46B42, 46A40, 46A19.
- In Lean Pool: [LeanPool/OrderClosures](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/OrderClosures), from the card [LeanPool/projects/order-closures.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/order-closures.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/order-closures.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/order-closures.yaml)
- [Lean Pool at 701389c0: LeanPool/OrderClosures](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/OrderClosures)
