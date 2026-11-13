---
declaration: theorem
origin: cited
lean: Wallace.commutativeTychonoffWallaceCounterexampleExists
statement: formalized
proof: formalized
---

# The Wallace problem in ZFC

> Formalizes in ZFC a Hausdorff countably compact group topology without nontrivial convergent sequences on every torsion-free Abelian group of cardinality continuum. It specializes the construction to the rational direct sum and the additive real group, and derives a commutative Tychonoff countably compact cancellative semigroup that is not a group.

*Quoted from the card [LeanPool/projects/wallace-problem.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/wallace-problem.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Wallace.torsionFreeAbelianGroup_mainTheorem_exact`](https://leanpool.github.io/lean-pool/LeanPool/Wallace/GeneralMain.html#Wallace.torsionFreeAbelianGroup_mainTheorem_exact) (theorem), declared in [LeanPool/Wallace/GeneralMain.lean, line 71](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Wallace/GeneralMain.lean#L71): “Every torsion-free Abelian group of cardinality continuum admits a Hausdorff countably compact group topology with no nontrivial convergent sequences.”
- [`Wallace.continuumRationalGroup_and_real_mainTheorem`](https://leanpool.github.io/lean-pool/LeanPool/Wallace/RealMain.html#Wallace.continuumRationalGroup_and_real_mainTheorem) (theorem), declared in [LeanPool/Wallace/RealMain.lean, line 58](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Wallace/RealMain.lean#L58): “Both the continuum-indexed rational direct sum and the additive group of real numbers admit such Hausdorff countably compact group topologies without nontrivial convergent sequences.”
- [`Wallace.commutativeTychonoffWallaceCounterexampleExists`](https://leanpool.github.io/lean-pool/LeanPool/Wallace/TychonoffWallace.html#Wallace.commutativeTychonoffWallaceCounterexampleExists) (theorem; a main declaration), declared in [LeanPool/Wallace/TychonoffWallace.lean, line 86](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Wallace/TychonoffWallace.lean#L86): “There exists a commutative Tychonoff countably compact topological semigroup with two-sided cancellation which is not a group.”

## Project

- Authors: Juliane Trianon Fraga, Vinicius de Oliveira Rodrigues.
- Source: *The Wallace problem and countably compact torsion-free Abelian groups in ZFC* by Juliane Trianon Fraga, Vinicius de Oliveira Rodrigues, [doi:10.48550/arXiv.2608.17317](https://doi.org/10.48550/arXiv.2608.17317), [arXiv:2608.17317](https://arxiv.org/abs/2608.17317).
- Project repository: [vo-rodrigues/wallace-problem-zfc-paper](https://github.com/vo-rodrigues/wallace-problem-zfc-paper), at commit [23756864](https://github.com/vo-rodrigues/wallace-problem-zfc-paper/tree/23756864de1f14e272dafb070b97fcdc7cbc75c5).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 22A05, 54D30, 20K20.
- In Lean Pool: [LeanPool/Wallace](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Wallace), from the card [LeanPool/projects/wallace-problem.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/wallace-problem.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/wallace-problem.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/wallace-problem.yaml)
- [Lean Pool at 701389c0: LeanPool/Wallace](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Wallace)
