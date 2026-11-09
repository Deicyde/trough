---
declaration: theorem
origin: cited
lean: Distributed2Coloring.pStar_ge_23879, Distributed2Coloring.pStar_lt_24118
statement: formalized
proof: formalized
---

# 2-Coloring Cycles in One Round

> Formalizes certified upper and lower bounds for one-round randomized algorithms that 2-color cycles.

*Quoted from the card [LeanPool/projects/2-coloring-1-round.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/2-coloring-1-round.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Distributed2Coloring.pStar_ge_23879`](https://leanpool.github.io/lean-pool/LeanPool/TwoColoringOneRound/MainResults.html#Distributed2Coloring.pStar_ge_23879) (theorem; a main declaration), declared in [LeanPool/TwoColoringOneRound/MainResults.lean, line 70](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/TwoColoringOneRound/MainResults.lean#L70): “Proves that every one-round classical algorithm has monochromatic-edge probability at least 0.23879.”
- [`Distributed2Coloring.pStar_lt_24118`](https://leanpool.github.io/lean-pool/LeanPool/TwoColoringOneRound/MainResults.html#Distributed2Coloring.pStar_lt_24118) (theorem; a main declaration), declared in [LeanPool/TwoColoringOneRound/MainResults.lean, line 79](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/TwoColoringOneRound/MainResults.lean#L79): “Proves that an explicit one-round algorithm attains monochromatic-edge probability strictly below 0.24118.”

## Project

- Authors: Jukka Suomela.
- Source: [arXiv:2603.04235](https://arxiv.org/abs/2603.04235).
- Project repository: [suomela/2-coloring-1-round](https://github.com/suomela/2-coloring-1-round).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0, keeping its copyright line: “Copyright (c) 2026 Jukka Suomela”.
- MSC2020: 68W15, 05C15.
- In Lean Pool: [LeanPool/TwoColoringOneRound](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/TwoColoringOneRound), from the card [LeanPool/projects/2-coloring-1-round.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/2-coloring-1-round.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/2-coloring-1-round.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/2-coloring-1-round.yaml)
- [Lean Pool at 2b205bf9: LeanPool/TwoColoringOneRound](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/TwoColoringOneRound)
