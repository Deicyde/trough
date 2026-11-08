---
declaration: def
origin: cited
lean: Lean4Itree.ITree, Lean4Itree.ITree.ieq_iff_eq, Lean4Itree.plfp_acc
statement: formalized
---

# Coinductive Interaction Trees using QPFs

> Formalizes coinductive interaction trees as the M-type of a polynomial functor (via Mathlib QPFs), proving the lawful functor and monad structure, a bisimulation equality coinciding with propositional equality, and iteration and effect-handler interpretation combinators, supported by a vendored parameterized-coinduction (Paco) library.

*Quoted from the card [LeanPool/projects/lean4-itree.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lean4-itree.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 7 main results, each with its informal statement quoted from the card. The scan finds 7 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`Lean4Itree.ITree`](https://leanpool.github.io/lean-pool/LeanPool/Lean4Itree/ITree/Basic.html#Lean4Itree.ITree) (def; a main declaration), declared in [LeanPool/Lean4Itree/ITree/Basic.lean, line 56](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Lean4Itree/ITree/Basic.lean#L56): “Defines the coinductive interaction tree as the final coalgebra (M-type) of the interaction-tree polynomial functor.”
- [`Lean4Itree.ITree.IEq`](https://leanpool.github.io/lean-pool/LeanPool/Lean4Itree/ITree/Basic.html#Lean4Itree.ITree.IEq) (def), declared in [LeanPool/Lean4Itree/ITree/Basic.lean, line 286](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Lean4Itree/ITree/Basic.lean#L286): “Defines bisimulation equality between interaction trees as a coinductive fixed point.”
- [`Lean4Itree.ITree.ieq_iff_eq`](https://leanpool.github.io/lean-pool/LeanPool/Lean4Itree/ITree/Basic.html#Lean4Itree.ITree.ieq_iff_eq) (theorem; a main declaration), declared in [LeanPool/Lean4Itree/ITree/Basic.lean, line 291](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Lean4Itree/ITree/Basic.lean#L291): “Proves that bisimulation equality of interaction trees coincides with propositional equality.”
- [`Lean4Itree.ITree.bind_assoc`](https://leanpool.github.io/lean-pool/LeanPool/Lean4Itree/ITree/Monad.html#Lean4Itree.ITree.bind_assoc) (theorem), declared in [LeanPool/Lean4Itree/ITree/Monad.lean, line 182](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Lean4Itree/ITree/Monad.lean#L182): “Proves associativity of monadic bind for interaction trees, part of the LawfulMonad instance.”
- [`Lean4Itree.ITree.iter`](https://leanpool.github.io/lean-pool/LeanPool/Lean4Itree/ITree/EffectAlgebra.html#Lean4Itree.ITree.iter) (def), declared in [LeanPool/Lean4Itree/ITree/EffectAlgebra.lean, line 90](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Lean4Itree/ITree/EffectAlgebra.lean#L90): “Defines the iteration combinator producing an interaction tree from a step function.”
- [`Lean4Itree.ITree.interp`](https://leanpool.github.io/lean-pool/LeanPool/Lean4Itree/ITree/EffectAlgebra.html#Lean4Itree.ITree.interp) (def), declared in [LeanPool/Lean4Itree/ITree/EffectAlgebra.lean, line 110](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Lean4Itree/ITree/EffectAlgebra.lean#L110): “Defines interpretation of an interaction tree against an effect handler into an arbitrary iterable monad.”
- [`Lean4Itree.plfp_acc`](https://leanpool.github.io/lean-pool/LeanPool/Lean4Itree/Paco/PacoDefs.html#Lean4Itree.plfp_acc) (theorem; a main declaration), declared in [LeanPool/Lean4Itree/Paco/PacoDefs.lean, line 185](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Lean4Itree/Paco/PacoDefs.lean#L185): “Proves the accumulation principle for the parameterized least fixed point underlying the Paco coinduction library.” Its source, as the card gives it: “C.-K. Hur, G. Neis, D. Dreyer, V. Vafeiadis, The Power of Parameterization in Coinductive Proof, POPL 2013, doi:10.1145/2429069.2429093.”

## Project

- Authors: Paul Mure, Joonhyup Lee.
- Source: [doi:10.1145/3371119](https://doi.org/10.1145/3371119), [arXiv:1906.00046](https://arxiv.org/abs/1906.00046).
- Project repository: [mit-plv/lean4-itree](https://github.com/mit-plv/lean4-itree).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0, keeping its copyright line: “Copyright (c) 2025 the choice-tree authors (see the AUTHORS file)”.
- MSC2020: 68Q55, 18C50, 68N18.
- In Lean Pool: [LeanPool/Lean4Itree](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Lean4Itree), from the card [LeanPool/projects/lean4-itree.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lean4-itree.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/lean4-itree.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lean4-itree.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Lean4Itree](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Lean4Itree)
