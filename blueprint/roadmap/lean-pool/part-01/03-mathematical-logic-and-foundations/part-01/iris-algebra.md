---
declaration: theorem
origin: cited
lean: Iris.IProp.fold_unfold, Iris.IProp.unfold_fold
statement: formalized
proof: formalized
---

# Ordered resource algebras and the Iris recursive domain model

> Constructs the algebraic core of the Iris proposition model from complete step-indexed spaces, ordered resource algebras, finite-support ghost maps, and monotone predicates. Proves guarded fixed-point unfolding and uniqueness, solves contractive mixed-variance domain equations, and constructs mutually inverse folding and unfolding maps for the recursive proposition model. Includes the October 2026 ordered-resource generalization and reusable morphism, product, optional-resource, and frame-preserving update infrastructure. The import is the mathematical dependency closure of IProp; it does not include the proof mode, HeapLang, program logics, or claims about their soundness.

*Quoted from the card [LeanPool/projects/iris-algebra.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/iris-algebra.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Iris.fixpoint_unfold`](https://leanpool.github.io/lean-pool/LeanPool/IrisAlgebra/Algebra/OFE.html#Iris.fixpoint_unfold) (theorem), declared in [LeanPool/IrisAlgebra/Algebra/OFE.lean, line 1584](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/IrisAlgebra/Algebra/OFE.lean#L1584): “Every contractive endomorphism of an inhabited complete ordered family of equivalences has a constructed fixed point satisfying its unfolding equation.”
- [`Iris.fixpoint_unique`](https://leanpool.github.io/lean-pool/LeanPool/IrisAlgebra/Algebra/OFE.html#Iris.fixpoint_unique) (theorem), declared in [LeanPool/IrisAlgebra/Algebra/OFE.lean, line 1588](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/IrisAlgebra/Algebra/OFE.lean#L1588): “Any fixed point of a contractive endomorphism of an inhabited complete ordered family of equivalences equals the constructed fixed point.”
- [`Iris.COFE.OFunctor.Fix.fold_unfold`](https://leanpool.github.io/lean-pool/LeanPool/IrisAlgebra/Algebra/COFESolver.html#Iris.COFE.OFunctor.Fix.fold_unfold) (theorem), declared in [LeanPool/IrisAlgebra/Algebra/COFESolver.lean, line 313](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/IrisAlgebra/Algebra/COFESolver.lean#L313): “For a contractive mixed-variance functor preserving complete step-indexed spaces, with an inhabited value at the lifted unit space, folding after unfolding is the identity on its constructed recursive domain.”
- [`Iris.COFE.OFunctor.Fix.unfold_fold`](https://leanpool.github.io/lean-pool/LeanPool/IrisAlgebra/Algebra/COFESolver.html#Iris.COFE.OFunctor.Fix.unfold_fold) (theorem), declared in [LeanPool/IrisAlgebra/Algebra/COFESolver.lean, line 314](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/IrisAlgebra/Algebra/COFESolver.lean#L314): “Under the same functor, completeness, and inhabitation hypotheses, unfolding after folding is the identity on the functor applied to the recursive domain.”
- [`Iris.IProp.fold_unfold`](https://leanpool.github.io/lean-pool/LeanPool/IrisAlgebra/Algebra/IProp.html#Iris.IProp.fold_unfold) (theorem; a main declaration), declared in [LeanPool/IrisAlgebra/Algebra/IProp.lean, line 99](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/IrisAlgebra/Algebra/IProp.lean#L99): “For every family of contractive affine resource functors, folding after unfolding is the identity on the associated monotone proposition model.”
- [`Iris.IProp.unfold_fold`](https://leanpool.github.io/lean-pool/LeanPool/IrisAlgebra/Algebra/IProp.html#Iris.IProp.unfold_fold) (theorem; a main declaration), declared in [LeanPool/IrisAlgebra/Algebra/IProp.lean, line 102](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/IrisAlgebra/Algebra/IProp.lean#L102): “For every such family of resource functors, unfolding after folding is the identity on the associated guarded recursive pre-proposition domain.”

## Project

- Authors: The Iris-Lean Contributors.
- Contributors: Mario Carneiro, Sebastian Graf, Sergei Stepanenko, Markus de Medeiros, Zongyuan Liu, Puming Liu, Janine Lohse, Сухарик (@suhr).
- Source: *Iris in Lean and the ordered resource algebra extension*, [arXiv:2609.24252](https://arxiv.org/abs/2609.24252).
- Project repository: [leanprover-community/iris-lean](https://github.com/leanprover-community/iris-lean), at commit [81bc3508](https://github.com/leanprover-community/iris-lean/tree/81bc35088ba67d465db008f5261a9b341eb6cf6c).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 03B70, 68Q55, 68N30.
- In Lean Pool: [LeanPool/IrisAlgebra](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/IrisAlgebra), from the card [LeanPool/projects/iris-algebra.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/iris-algebra.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/iris-algebra.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/iris-algebra.yaml)
- [Lean Pool at 2b205bf9: LeanPool/IrisAlgebra](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/IrisAlgebra)
