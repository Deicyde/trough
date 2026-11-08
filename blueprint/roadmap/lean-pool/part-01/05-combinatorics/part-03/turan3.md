---
declaration: theorem
origin: cited
lean: Turan3.turans, Turan3.finale_bound, Turan3.Better_forms_clique
statement: formalized
proof: formalized
---

# Turán's theorem (the "Book" weighting proof)

> Formalizes the weighting/optimization proof of Turán's theorem from Proofs from THE BOOK, bounding the number of edges of a p-clique-free simple graph by (1/2)(1 - 1/(p-1)) n².

*Quoted from the card [LeanPool/projects/turan3.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/turan3.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`Turan3.turans`](https://leanpool.github.io/lean-pool/LeanPool/Turan3/Turans3rdProof.html#Turan3.turans) (theorem; a main declaration), declared in [LeanPool/Turan3/Turans3rdProof.lean, line 2577](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Turan3/Turans3rdProof.lean#L2577): “Turán's theorem — a p-clique-free simple graph on n vertices has at most (1/2)(1 - 1/(p-1)) n² edges.”
- [`Turan3.finale_bound`](https://leanpool.github.io/lean-pool/LeanPool/Turan3/Turans3rdProof.html#Turan3.finale_bound) (theorem; a main declaration), declared in [LeanPool/Turan3/Turans3rdProof.lean, line 2343](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Turan3/Turans3rdProof.lean#L2343): “For any weight distribution on a p-clique-free graph, the total edge weight is at most ((p-1)(p-2)/2)·(1/(p-1))², the bound used to derive the edge count.”
- [`Turan3.Better_forms_clique`](https://leanpool.github.io/lean-pool/LeanPool/Turan3/Turans3rdProof.html#Turan3.Better_forms_clique) (theorem; a main declaration), declared in [LeanPool/Turan3/Turans3rdProof.lean, line 532](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Turan3/Turans3rdProof.lean#L532): “Starting from any weight function, the minimal-support weight-non-decreasing improvement has support that forms a clique.”
- [`Turan3.Enhance_total_weight_stricinc`](https://leanpool.github.io/lean-pool/LeanPool/Turan3/Turans3rdProof.html#Turan3.Enhance_total_weight_stricinc) (theorem), declared in [LeanPool/Turan3/Turans3rdProof.lean, line 1545](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Turan3/Turans3rdProof.lean#L1545): “Equalizing weights between a maximum- and minimum-weight vertex in the clique support strictly increases the total edge weight.”

## Project

- Authors: Rodrigo Gutierrez, Yves Jäckle.
- Project repository: [ro-gut/turan3](https://github.com/ro-gut/turan3).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 05C35.
- In Lean Pool: [LeanPool/Turan3](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Turan3), from the card [LeanPool/projects/turan3.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/turan3.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/turan3.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/turan3.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Turan3](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Turan3)
