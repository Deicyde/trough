---
declaration: theorem
origin: cited
lean: V0Model.ind_strengthened_v0, str_add_assoc_strengthened_v0
statement: formalized
proof: formalized
---

# Strengthened V0 Bounded Arithmetic Interfaces

> Formalizes first-order and two-sorted bounded-arithmetic model infrastructure, including arithmetic model laws and string-addition laws for strengthened bundled V0-style interfaces with propositional induction, order, cancellation, decidability, and algebraic laws assumed as fields rather than derived from a separate raw V0 class.

*Quoted from the card [LeanPool/projects/formalization-of-bounded-arithmetic.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/formalization-of-bounded-arithmetic.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 9 main results, each with its informal statement quoted from the card. The scan finds 9 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`IOPENModel.add_assoc`](https://leanpool.github.io/lean-pool/LeanPool/FormalizationOfBoundedArithmetic/IOPEN.html#IOPENModel.add_assoc) (theorem), declared in [LeanPool/FormalizationOfBoundedArithmetic/IOPEN.lean, line 60](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FormalizationOfBoundedArithmetic/IOPEN.lean#L60): “Proves associativity of addition in IOPEN models.”
- [`IOPENModel.add_comm`](https://leanpool.github.io/lean-pool/LeanPool/FormalizationOfBoundedArithmetic/IOPEN.html#IOPENModel.add_comm) (theorem), declared in [LeanPool/FormalizationOfBoundedArithmetic/IOPEN.lean, line 123](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FormalizationOfBoundedArithmetic/IOPEN.lean#L123): “Proves commutativity of addition in IOPEN models.”
- [`IDelta0Model.pred_exists`](https://leanpool.github.io/lean-pool/LeanPool/FormalizationOfBoundedArithmetic/IDelta0.html#IDelta0Model.pred_exists) (theorem), declared in [LeanPool/FormalizationOfBoundedArithmetic/IDelta0.lean, line 44](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FormalizationOfBoundedArithmetic/IDelta0.lean#L44): “Shows that nonzero elements in IDelta0 models have predecessors.”
- [`IDelta0Model.mul_cancel_right`](https://leanpool.github.io/lean-pool/LeanPool/FormalizationOfBoundedArithmetic/IDelta0.html#IDelta0Model.mul_cancel_right) (theorem), declared in [LeanPool/FormalizationOfBoundedArithmetic/IDelta0.lean, line 446](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FormalizationOfBoundedArithmetic/IDelta0.lean#L446): “Proves right cancellation for multiplication by a nonzero element in IDelta0 models.”
- [`V0Model.xind`](https://leanpool.github.io/lean-pool/LeanPool/FormalizationOfBoundedArithmetic/V0.html#V0Model.xind) (theorem), declared in [LeanPool/FormalizationOfBoundedArithmetic/V0.lean, line 423](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FormalizationOfBoundedArithmetic/V0.lean#L423): “Exposes string induction inside the strengthened bundled V0Model structure, whose fields include the comprehension and induction/order principles used downstream.”
- [`V0Model.ind_strengthened_v0`](https://leanpool.github.io/lean-pool/LeanPool/FormalizationOfBoundedArithmetic/V0.html#V0Model.ind_strengthened_v0) (theorem; a main declaration), declared in [LeanPool/FormalizationOfBoundedArithmetic/V0.lean, line 509](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FormalizationOfBoundedArithmetic/V0.lean#L509): “Exposes propositional induction inside the strengthened bundled V0Model structure, rather than deriving it from only the raw finite V0 axiom list.”
- [`str_add_comm_strengthened_v0`](https://leanpool.github.io/lean-pool/LeanPool/FormalizationOfBoundedArithmetic/V0StrAddComm.html#str_add_comm_strengthened_v0) (theorem), declared in [LeanPool/FormalizationOfBoundedArithmetic/V0StrAddComm.lean, line 76](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FormalizationOfBoundedArithmetic/V0StrAddComm.lean#L76): “Proves commutativity of string addition in V0 extension models extending the strengthened V0Model bundle.”
- [`str_add_assoc_strengthened_v0`](https://leanpool.github.io/lean-pool/LeanPool/FormalizationOfBoundedArithmetic/V0StrAddAssoc.html#str_add_assoc_strengthened_v0) (theorem; a main declaration), declared in [LeanPool/FormalizationOfBoundedArithmetic/V0StrAddAssoc.lean, line 126](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FormalizationOfBoundedArithmetic/V0StrAddAssoc.lean#L126): “Proves associativity of string addition in V0 extension models extending the strengthened V0Model bundle, using the bundled propositional induction field.”
- [`str_succ_assoc_strengthened_v0`](https://leanpool.github.io/lean-pool/LeanPool/FormalizationOfBoundedArithmetic/V0StrSuccAssoc.html#str_succ_assoc_strengthened_v0) (theorem), declared in [LeanPool/FormalizationOfBoundedArithmetic/V0StrSuccAssoc.lean, line 1039](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FormalizationOfBoundedArithmetic/V0StrSuccAssoc.lean#L1039): “Proves that string addition associates with string successor in V0 extension models extending the strengthened V0Model bundle.”

## Project

- Authors: ruplet.
- Source: *Logical Foundations of Proof Complexity* by Stephen Cook, Phuong Nguyen, [doi:10.1017/CBO9780511676277](https://doi.org/10.1017/CBO9780511676277).
- Project repository: [ruplet/formalization-of-bounded-arithmetic](https://github.com/ruplet/formalization-of-bounded-arithmetic).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0, keeping its copyright line: “The upstream MIT LICENSE file leaves the copyright line as the unfilled template text "Copyright (c) [year] [fullname]"; the repository owner of record is "ruplet".”.
- MSC2020: 03F30, 03D15.
- In Lean Pool: [LeanPool/FormalizationOfBoundedArithmetic](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FormalizationOfBoundedArithmetic), from the card [LeanPool/projects/formalization-of-bounded-arithmetic.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/formalization-of-bounded-arithmetic.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/formalization-of-bounded-arithmetic.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/formalization-of-bounded-arithmetic.yaml)
- [Lean Pool at 2b205bf9: LeanPool/FormalizationOfBoundedArithmetic](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FormalizationOfBoundedArithmetic)
