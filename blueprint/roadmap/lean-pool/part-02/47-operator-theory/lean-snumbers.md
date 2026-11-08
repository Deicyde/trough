---
declaration: theorem
origin: cited
lean: SNumbers.approximationNumber_le_e_mul_hilbertNumber
statement: formalized
proof: formalized
---

# Pietsch s-numbers and the maximal difference theorem

> Formalizes the five classical s-number sequences, their comparison inequalities, the maximal difference theorem, compact-operator singular value decomposition, John ellipsoids, entropy numbers, and compactness characterizations.

*Quoted from the card [LeanPool/projects/lean-snumbers.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lean-snumbers.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`SNumbers.approximationNumber_le_e_mul_hilbertNumber`](https://leanpool.github.io/lean-pool/LeanPool/SNumbers/SNumbers/MaxDifference.html#SNumbers.approximationNumber_le_e_mul_hilbertNumber) (theorem; a main declaration), declared in [LeanPool/SNumbers/SNumbers/MaxDifference.lean, line 900](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SNumbers/SNumbers/MaxDifference.lean#L900): “For a bounded operator, its nth approximation number is at most e times (n+1) times its nth Hilbert number.”
- [`SNumbers.allSNumbers_eq_on_HilbertSpace`](https://leanpool.github.io/lean-pool/LeanPool/SNumbers/SNumbers/Uniqueness.html#SNumbers.allSNumbers_eq_on_HilbertSpace) (theorem), declared in [LeanPool/SNumbers/SNumbers/Uniqueness.lean, line 132](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SNumbers/SNumbers/Uniqueness.lean#L132): “Every s-number sequence agrees with the approximation numbers on operators between Hilbert spaces.”
- [`John.john_decomposition`](https://leanpool.github.io/lean-pool/LeanPool/SNumbers/BasicResults/John.html#John.john_decomposition) (theorem), declared in [LeanPool/SNumbers/BasicResults/John.lean, line 852](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SNumbers/BasicResults/John.lean#L852): “In John position, the identity decomposes into a positive weighted sum of rank-one operators from contact points.”

## Project

- Authors: Mario Ullrich.
- Project repository: [mario-ullrich/lean-snumbers](https://github.com/mario-ullrich/lean-snumbers), at commit [d984f39b](https://github.com/mario-ullrich/lean-snumbers/tree/d984f39b53eb1579920fe987de10382dcf553f4e).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 47B06, 46B20.
- In Lean Pool: [LeanPool/SNumbers](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SNumbers), from the card [LeanPool/projects/lean-snumbers.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lean-snumbers.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/lean-snumbers.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lean-snumbers.yaml)
- [Lean Pool at 2b205bf9: LeanPool/SNumbers](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SNumbers)
