---
declaration: inductive
origin: cited
lean: Computability.RecursiveIn, Computability.TuringDegree
statement: formalized
---

# Oracle Computability and Turing Degrees

> Formalizes oracle-relative computability via partial recursive functions, Turing reducibility and the Turing degrees as an upper semilattice, a Gödel numbering with a universal oracle machine, the jump operator, and the arithmetical hierarchy.

*Quoted from the card [LeanPool/projects/computability.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/computability.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Computability.RecursiveIn`](https://leanpool.github.io/lean-pool/LeanPool/Computability/Oracle.html#Computability.RecursiveIn) (inductive; a main declaration), declared in [LeanPool/Computability/Oracle.lean, line 54](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Computability/Oracle.lean#L54): “The inductive relation `RecursiveIn O f` stating that `f : ℕ →. ℕ` is partial recursive relative to a set of oracle functions `O`.”
- [`Computability.exists_code_rel`](https://leanpool.github.io/lean-pool/LeanPool/Computability/Encoding.html#Computability.exists_code_rel) (theorem), declared in [LeanPool/Computability/Encoding.lean, line 413](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Computability/Encoding.lean#L413): “Universality of the oracle evaluator `evalo`, that is, `RecursiveIn (Set.range g) f` holds iff there is a code `c` with `evalo g c = f`.”
- [`Computability.TuringReducible`](https://leanpool.github.io/lean-pool/LeanPool/Computability/TuringDegree.html#Computability.TuringReducible) (abbrev), declared in [LeanPool/Computability/TuringDegree.lean, line 73](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Computability/TuringDegree.lean#L73): “`f` is Turing reducible to `g` (`f ≤ᵀ g`) when `f` is recursive in the singleton oracle set `{g}`.”
- [`Computability.TuringDegree`](https://leanpool.github.io/lean-pool/LeanPool/Computability/TuringDegree.html#Computability.TuringDegree) (abbrev; a main declaration), declared in [LeanPool/Computability/TuringDegree.lean, line 135](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Computability/TuringDegree.lean#L135): “The type of Turing degrees, the antisymmetrization of partial functions under Turing reducibility.”
- [`Computability.jump_recIn`](https://leanpool.github.io/lean-pool/LeanPool/Computability/Jump.html#Computability.jump_recIn) (theorem), declared in [LeanPool/Computability/Jump.lean, line 74](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Computability/Jump.lean#L74): “The original function is Turing reducible to its jump, `f ≤ᵀ f⌜`.”
- [`Computability.TuringDegree.instSemilatticeSup`](https://leanpool.github.io/lean-pool/LeanPool/Computability/TuringDegree.html#Computability.TuringDegree.instSemilatticeSup) (instance), declared in [LeanPool/Computability/TuringDegree.lean, line 508](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Computability/TuringDegree.lean#L508): “The Turing degrees form an upper semilattice with the Turing join as supremum.”

## Project

- Authors: Tanner Duve, Elan Roth.
- Project repository: [tannerduve/computability](https://github.com/tannerduve/computability).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 03D30, 03D28.
- In Lean Pool: [LeanPool/Computability](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Computability), from the card [LeanPool/projects/computability.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/computability.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/computability.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/computability.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Computability](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Computability)
