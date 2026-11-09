---
declaration: theorem
origin: cited
lean: SyntheticEuclid4.pythagoras, SyntheticEuclid4.pythagoras_converse
statement: formalized
proof: formalized
---

# Synthetic Euclidean geometry: Euclid's Elements Book I

> Formalizes Book I of Euclid's Elements via an axiomatic synthetic-geometry system (incidence, betweenness, congruence, and area), culminating in the Pythagorean theorem and its converse.

*Quoted from the card [LeanPool/projects/synthetic-euclid.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/synthetic-euclid.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`SyntheticEuclid4.IncidenceGeometry`](https://leanpool.github.io/lean-pool/LeanPool/SyntheticEuclid4/Axioms.html#SyntheticEuclid4.IncidenceGeometry) (class), declared in [LeanPool/SyntheticEuclid4/Axioms.lean, line 26](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SyntheticEuclid4/Axioms.lean#L26): “The axiomatic class of synthetic Euclidean geometry, bundling points, lines, circles, and the incidence, betweenness, congruence, and area primitives with Euclid's axioms.”
- [`SyntheticEuclid4.square_of_len`](https://leanpool.github.io/lean-pool/LeanPool/SyntheticEuclid4/SyntheticEuclid4.html#SyntheticEuclid4.square_of_len) (theorem), declared in [LeanPool/SyntheticEuclid4/SyntheticEuclid4.lean, line 1922](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SyntheticEuclid4/SyntheticEuclid4.lean#L1922): “Constructs a square on a given segment off a given line.”
- [`SyntheticEuclid4.pythagoras_construct`](https://leanpool.github.io/lean-pool/LeanPool/SyntheticEuclid4/SyntheticEuclid4.html#SyntheticEuclid4.pythagoras_construct) (theorem), declared in [LeanPool/SyntheticEuclid4/SyntheticEuclid4.lean, line 1988](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SyntheticEuclid4/SyntheticEuclid4.lean#L1988): “Constructs the three squares and parallelograms on the sides of a triangle used in the proof of the Pythagorean theorem.”
- [`SyntheticEuclid4.pythagoras`](https://leanpool.github.io/lean-pool/LeanPool/SyntheticEuclid4/SyntheticEuclid4.html#SyntheticEuclid4.pythagoras) (theorem; a main declaration), declared in [LeanPool/SyntheticEuclid4/SyntheticEuclid4.lean, line 2007](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SyntheticEuclid4/SyntheticEuclid4.lean#L2007): “Euclid I.47, the Pythagorean theorem, that the square on the hypotenuse of a right triangle equals the sum of the squares on the other two sides.”
- [`SyntheticEuclid4.pythagoras_converse`](https://leanpool.github.io/lean-pool/LeanPool/SyntheticEuclid4/SyntheticEuclid4.html#SyntheticEuclid4.pythagoras_converse) (theorem; a main declaration), declared in [LeanPool/SyntheticEuclid4/SyntheticEuclid4.lean, line 2104](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SyntheticEuclid4/SyntheticEuclid4.lean#L2104): “Euclid I.48, the converse of the Pythagorean theorem, that a triangle whose square areas satisfy the Pythagorean relation has a right angle.”

## Project

- Authors: André Hernandez-Espiet, Vladimir Sedlacek.
- Source: *A formal system for Euclid's Elements* by Jeremy Avigad, Edward Dean, John Mumma, [doi:10.1017/S1755020309990098](https://doi.org/10.1017/S1755020309990098).
- Project repository: [ah1112/synthetic_euclid_4](https://github.com/ah1112/synthetic_euclid_4).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 51M04.
- In Lean Pool: [LeanPool/SyntheticEuclid4](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SyntheticEuclid4), from the card [LeanPool/projects/synthetic-euclid.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/synthetic-euclid.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/synthetic-euclid.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/synthetic-euclid.yaml)
- [Lean Pool at 2b205bf9: LeanPool/SyntheticEuclid4](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SyntheticEuclid4)
