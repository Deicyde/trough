---
declaration: alias
origin: cited
lean: PointwiseComposition.no_quotient_of_enumerable_axioms
statement: formalized
proof: formalized
---

# Pointwise provable equality and the failure of composition

> For every consistent recursively enumerable extension of Peano arithmetic, pointwise provable equality of unary programs fails to respect composition. Separate productive-set and Goedel incompleteness proofs establish the obstruction. For consistent extensions, compatibility is equivalent to Pi-one completeness. For every extension, the generated composition congruence is extensional equality in the Sigma-one sound case and universal otherwise. The development also proves weak-totality and range obstructions and identifies the sound generated quotient with actual unary partial recursive functions. Its coherent dependency closure preserves the concrete evaluator, arithmetization, first-order syntax, semantics and provability infrastructure. Main-result proofs were produced by AI agents under Florian Lengyel's direction; the Foundation dependency includes substantial human formalization by the Formalized Formal Logic contributors.

*Quoted from the card [LeanPool/projects/pointwise-provable-composition.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/pointwise-provable-composition.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`PointwiseComposition.no_quotient_of_enumerable_axioms`](https://leanpool.github.io/lean-pool/LeanPool/PointwiseComposition.html#PointwiseComposition.no_quotient_of_enumerable_axioms) (alias; a main declaration), declared in [LeanPool/PointwiseComposition.lean, line 48](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PointwiseComposition.lean#L48): “For every consistent extension T of Peano arithmetic with recursively enumerable axiom codes, no binary operation on the pointwise-provability quotient of actual natural-number program indices respects their actual composition.”
- [`PointwiseComposition.FailureOfComposition.ConcreteIndices.no_index_quotient_of_re_axioms`](https://leanpool.github.io/lean-pool/LeanPool/PointwiseComposition/FailureOfComposition/ConcreteIndexObstruction.html#PointwiseComposition.FailureOfComposition.ConcreteIndices.no_index_quotient_of_re_axioms) (theorem), declared in [LeanPool/PointwiseComposition/FailureOfComposition/ConcreteIndexObstruction.lean, line 159](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PointwiseComposition/FailureOfComposition/ConcreteIndexObstruction.lean#L159): “For every consistent extension T of Peano arithmetic with recursively enumerable axiom codes, no binary operation on the pointwise-provability quotient of actual natural-number program indices respects their actual composition.”
- [`PointwiseComposition.FailureOfComposition.ConcreteIndices.pi_one_characterization`](https://leanpool.github.io/lean-pool/LeanPool/PointwiseComposition/FailureOfComposition/ConcretePiOneCharacterization.html#PointwiseComposition.FailureOfComposition.ConcreteIndices.pi_one_characterization) (theorem), declared in [LeanPool/PointwiseComposition/FailureOfComposition/ConcretePiOneCharacterization.lean, line 81](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PointwiseComposition/FailureOfComposition/ConcretePiOneCharacterization.lean#L81): “For every consistent extension of Peano arithmetic, right compatibility, composition congruence, completeness for true Pi-one sentences, and agreement with extensional equality of partial functions are equivalent.”
- [`PointwiseComposition.FailureOfComposition.ConcreteIndices.generated_congruence_classification`](https://leanpool.github.io/lean-pool/LeanPool/PointwiseComposition/FailureOfComposition/ConcreteGeneratedCongruence.html#PointwiseComposition.FailureOfComposition.ConcreteIndices.generated_congruence_classification) (theorem), declared in [LeanPool/PointwiseComposition/FailureOfComposition/ConcreteGeneratedCongruence.lean, line 59](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PointwiseComposition/FailureOfComposition/ConcreteGeneratedCongruence.lean#L59): “For every extension of Peano arithmetic, with no consistency or enumerability hypothesis, the least composition congruence containing pointwise provable equality is extensional equality if the theory is Sigma-one sound and the universal relation otherwise.”
- [`PointwiseComposition.FailureOfComposition.ConcreteIndices.generatedQuotientPartialRecursiveEquiv`](https://leanpool.github.io/lean-pool/LeanPool/PointwiseComposition/FailureOfComposition/PartialRecursiveQuotient.html#PointwiseComposition.FailureOfComposition.ConcreteIndices.generatedQuotientPartialRecursiveEquiv) (def), declared in [LeanPool/PointwiseComposition/FailureOfComposition/PartialRecursiveQuotient.lean, line 119](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PointwiseComposition/FailureOfComposition/PartialRecursiveQuotient.lean#L119): “For every Sigma-one sound extension of Peano arithmetic, the generated quotient is a monoid isomorphic to actual unary partial recursive functions with partial-function composition.”

## Project

- Authors: Florian Lengyel.
- Contributors: Shogo Saitou, Mashu Noguchi, Formalized Formal Logic contributors.
- Source: *Pointwise provable equality and the failure of composition* by Florian Lengyel, [arXiv:2609.25556](https://arxiv.org/abs/2609.25556).
- Project repository: [flengyel/FailureOfComposition](https://github.com/flengyel/FailureOfComposition), at commit [506d1f14](https://github.com/flengyel/FailureOfComposition/tree/506d1f1494d6c05b0ba304edf5fe0bfa6c32864b).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 03D75, 03F40, 08A30, 18B10.
- In Lean Pool: [LeanPool/PointwiseComposition](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PointwiseComposition), from the card [LeanPool/projects/pointwise-provable-composition.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/pointwise-provable-composition.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/pointwise-provable-composition.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/pointwise-provable-composition.yaml)
- [Lean Pool at 2b205bf9: LeanPool/PointwiseComposition](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PointwiseComposition)
