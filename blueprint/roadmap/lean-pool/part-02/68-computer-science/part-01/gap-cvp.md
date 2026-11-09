---
declaration: theorem
origin: cited
lean: GapCVP.Comparator.gapCVP400IsNPHard
statement: formalized
proof: formalized
---

# Polynomial-factor hardness of the closest vector problem

> Formalizes polynomial-factor NP-hardness of the closest vector problem through an explicit reduction from 3-SAT. The development also derives NP-hardness of binary nearest codeword, binary syndrome decoding, and finite p-norm variants of GapCVP. It includes machine-level polynomial-time bounds, binary encodings, affine systems, Reed--Solomon-style interpolation, and the lattice and coding-theory reductions needed by the final results.

*Quoted from the card [LeanPool/projects/gap-cvp.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/gap-cvp.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`GapCVP.Comparator.gapCVP400IsNPHard`](https://leanpool.github.io/lean-pool/LeanPool/GapCVP/Part18.html#GapCVP.Comparator.gapCVP400IsNPHard) (theorem; a main declaration), declared in [LeanPool/GapCVP/Part18.lean, line 746](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GapCVP/Part18.lean#L746): “GapCVP in the Euclidean norm with approximation factor n^(1/400), where n is the lattice dimension, is NP-hard as a promise problem: every NP language reduces in polynomial time to the promise problem on encoded well-formed instances (positive dimension, nonsingular integer basis, positive rational radius) with an integer target, whose YES instances have a lattice vector within the radius of the target and whose NO instances have every lattice vector at distance greater than n^(1/400) times the radius.”
- [`GapCVP.Comparator.binaryNearestCodewordIsNPHard`](https://leanpool.github.io/lean-pool/LeanPool/GapCVP/Part18.html#GapCVP.Comparator.binaryNearestCodewordIsNPHard) (theorem), declared in [LeanPool/GapCVP/Part18.lean, line 750](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GapCVP/Part18.lean#L750): “Binary nearest codeword is NP-hard as a promise problem.”
- [`GapCVP.Comparator.binarySyndromeDecodingIsNPHard`](https://leanpool.github.io/lean-pool/LeanPool/GapCVP/Part18.html#GapCVP.Comparator.binarySyndromeDecodingIsNPHard) (theorem), declared in [LeanPool/GapCVP/Part18.lean, line 757](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GapCVP/Part18.lean#L757): “Binary syndrome decoding is NP-hard as a promise problem.”
- [`GapCVP.Comparator.finitePNormGapCVPIsNPHard`](https://leanpool.github.io/lean-pool/LeanPool/GapCVP/Part18.html#GapCVP.Comparator.finitePNormGapCVPIsNPHard) (theorem), declared in [LeanPool/GapCVP/Part18.lean, line 764](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GapCVP/Part18.lean#L764): “For every rational p at least one, the finite p-norm version of GapCVP is NP-hard as a promise problem.”

## Project

- Authors: OpenAI, Dean Cureton.
- Source: *Ten Advances in Mathematics and Theoretical Computer Science* by OpenAI.
- Project repository: [openai/ten-proofs](https://github.com/openai/ten-proofs), at commit [94bc0feb](https://github.com/openai/ten-proofs/tree/94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 68Q17, 68Q25, 11H06, 94B35.
- In Lean Pool: [LeanPool/GapCVP](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GapCVP), from the card [LeanPool/projects/gap-cvp.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/gap-cvp.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/gap-cvp.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/gap-cvp.yaml)
- [Lean Pool at 2b205bf9: LeanPool/GapCVP](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GapCVP)
