---
declaration: theorem
origin: cited
lean: card_noncrossingPairing_eq_catalan, Pairing.genus_zero_count
statement: formalized
proof: formalized
---

# Genus-Zero Pairings and Catalan Numbers

> Formalizes the finite combinatorics behind the genus-zero term of the Wigner semicircle law: a pairing of Fin (2n), viewed as a fixed-point-free involution, has genus zero (total cycle count of the rotation product maximal) exactly when it is noncrossing, and these genus-zero pairings are counted by the Catalan number Cₙ. The Catalan recurrence is obtained from an explicit equivalence decomposing a noncrossing pairing by the partner of vertex 0 into independent inside and outside pairings.

*Quoted from the card [LeanPool/projects/semicircle-catalan.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/semicircle-catalan.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`card_noncrossingPairing_eq_catalan`](https://leanpool.github.io/lean-pool/LeanPool/SemicircleCheck/CatalanRecurrence.html#card_noncrossingPairing_eq_catalan) (theorem; a main declaration), declared in [LeanPool/SemicircleCheck/CatalanRecurrence.lean, line 2053](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SemicircleCheck/CatalanRecurrence.lean#L2053): “The number of noncrossing pairings on 2n points equals the Catalan number catalan n.”
- [`Pairing.genus_zero_count`](https://leanpool.github.io/lean-pool/LeanPool/SemicircleCheck/CatalanRecurrence.html#Pairing.genus_zero_count) (theorem; a main declaration), declared in [LeanPool/SemicircleCheck/CatalanRecurrence.lean, line 2081](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SemicircleCheck/CatalanRecurrence.lean#L2081): “The number of genus-zero pairings of Fin (2n) equals the Catalan number catalan n.”
- [`Pairing.genus_zero_iff_noncrossing`](https://leanpool.github.io/lean-pool/LeanPool/SemicircleCheck/GenusNoncrossing.html#Pairing.genus_zero_iff_noncrossing) (theorem), declared in [LeanPool/SemicircleCheck/GenusNoncrossing.lean, line 1096](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SemicircleCheck/GenusNoncrossing.lean#L1096): “A pairing has genus zero if and only if it is noncrossing.”

## Project

- Authors: Wondermonger-daydreaming.
- Source: *semicircle-catalan: genus-zero pairings and the Catalan moments of the Wigner semicircle law* by Wondermonger-daydreaming.
- Project repository: [Wondermonger-daydreaming/semicircle-catalan](https://github.com/Wondermonger-daydreaming/semicircle-catalan).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05A15, 05A18.
- In Lean Pool: [LeanPool/SemicircleCheck](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SemicircleCheck), from the card [LeanPool/projects/semicircle-catalan.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/semicircle-catalan.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/semicircle-catalan.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/semicircle-catalan.yaml)
- [Lean Pool at 2b205bf9: LeanPool/SemicircleCheck](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SemicircleCheck)
