---
declaration: theorem
origin: cited
lean: LeanPool.Erdos132N14.erdos132_for_fourteen_of_published_inputs
statement: formalized
proof: formalized
---

# A Conditional Fourteen-Point Case of Erdős Problem 132

> Formalizes the planar Hopf--Pannwitz diameter bound and proves the fourteen-point low-multiplicity conclusion conditional on exactly two remaining published interfaces: the known maximum-cardinality bound for planar sets with at most six distances and the Szöllősi--Östergård classification of thirteen-point planar six-distance sets. Internally derives the exact failure profile and endpoint deletion, constructs the three classified templates, eliminates the nonregular cases by multiplicity, and excludes the regular tridecagon extension by explicit second and fourth moments. The general Erdős problem remains open.

*Quoted from the card [LeanPool/projects/erdos132-n14.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos132-n14.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`LeanPool.Erdos132N14.hopfPannwitzLowMultiplicityDistance14`](https://leanpool.github.io/lean-pool/LeanPool/Erdos132N14/HopfPannwitz.html#LeanPool.Erdos132N14.hopfPannwitzLowMultiplicityDistance14) (theorem), declared in [LeanPool/Erdos132N14/HopfPannwitz.lean, line 292](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos132N14/HopfPannwitz.lean#L292): “Every injectively labelled fourteen-point planar configuration has a realized distance represented by at most fourteen unordered pairs; the proof chooses that distance to be a diameter.” Its source, as the card gives it: “The planar diameter bound, conventionally associated with Hopf--Pannwitz; Perles's clockwise-extreme endpoint proof.”
- [`LeanPool.Erdos132N14.erdos132_for_fourteen_of_published_inputs`](https://leanpool.github.io/lean-pool/LeanPool/Erdos132N14/Main.html#LeanPool.Erdos132N14.erdos132_for_fourteen_of_published_inputs) (theorem; a main declaration), declared in [LeanPool/Erdos132N14/Main.lean, line 468](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos132N14/Main.lean#L468): “Assuming precisely the published planar few-distance cardinality and Szöllősi--Östergård classification interfaces, every injectively labelled fourteen-point planar configuration realizes at least two distances whose unordered-pair multiplicities are at most fourteen.” Its source, as the card gives it: “Erdős Problem 132; Hopf--Pannwitz's planar diameter bound; Wei, "A Proof of Erdős--Fishburn's Conjecture for g(6)=13," EJC 19(4) P38 (2012), doi:10.37236/2917; Szöllősi--Östergård, EJC 27(1) P1.23 (2020), Table 1 and Theorem 16, doi:10.37236/8565.”

## Project

- Authors: Egor Lyfar.
- Source: *Constructions of maximum few-distance sets in Euclidean spaces* by Ferenc Szöllősi, Patric R. J. Östergård, [doi:10.37236/8565](https://doi.org/10.37236/8565), [https://www.erdosproblems.com/132](https://www.erdosproblems.com/132).
- Project repository: [lyfar/erdos-132-moment-obstruction-lean](https://github.com/lyfar/erdos-132-moment-obstruction-lean).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 52C10, 05D99.
- In Lean Pool: [LeanPool/Erdos132N14](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos132N14), from the card [LeanPool/projects/erdos132-n14.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos132-n14.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/erdos132-n14.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos132-n14.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Erdos132N14](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos132N14)
