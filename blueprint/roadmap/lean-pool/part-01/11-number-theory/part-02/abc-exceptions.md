---
declaration: lemma
origin: cited
lean: abcConjecture_iff_countTriples, thm_4_point_3
statement: formalized
proof: formalized
---

# Exceptional Set in the abc Conjecture

> Formalizes reductions and optimization bounds for a power-saving estimate on exceptional triples in the abc conjecture.

*Quoted from the card [LeanPool/projects/abc-exceptions.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/abc-exceptions.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`abcConjecture_iff_countTriples`](https://leanpool.github.io/lean-pool/LeanPool/ABCExceptions/Section2.html#abcConjecture_iff_countTriples) (lemma; a main declaration), declared in [LeanPool/ABCExceptions/Section2.lean, line 188](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ABCExceptions/Section2.lean#L188): “Recasts the abc conjecture as a uniform big-O bound for bounded exceptional triples.”
- [`refinedCountTriplesStar_isBigO_B`](https://leanpool.github.io/lean-pool/LeanPool/ABCExceptions/Section2.html#refinedCountTriplesStar_isBigO_B) (theorem), declared in [LeanPool/ABCExceptions/Section2.lean, line 1553](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ABCExceptions/Section2.lean#L1553): “Bounds the refined exceptional-triple count by the dyadic structured-box supremum.”
- [`thm_4_point_3`](https://leanpool.github.io/lean-pool/LeanPool/ABCExceptions/Section4.html#thm_4_point_3) (theorem; a main declaration), declared in [LeanPool/ABCExceptions/Section4.lean, line 1574](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ABCExceptions/Section4.lean#L1574): “Derives the Section 4 optimization bound from the determinant, geometry, and Fourier hypotheses.”

## Project

- Authors: Bhavik Mehta, Arend Mellendijk.
- Source: *Bounds on the exceptional set in the abc conjecture* by Tim Browning, Jared Duker Lichtman, Joni Teräväinen, [arXiv:2410.12234](https://arxiv.org/abs/2410.12234).
- Project repository: [b-mehta/ABC-Exceptions](https://github.com/b-mehta/ABC-Exceptions).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 11D75, 11N37.
- In Lean Pool: [LeanPool/ABCExceptions](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ABCExceptions), from the card [LeanPool/projects/abc-exceptions.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/abc-exceptions.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/abc-exceptions.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/abc-exceptions.yaml)
- [Lean Pool at 2b205bf9: LeanPool/ABCExceptions](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ABCExceptions)
