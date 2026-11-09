---
declaration: theorem
origin: cited
lean: SteinhausThreeGap.three_gap_card_le_three
statement: formalized
proof: formalized
---

# The Three-Gap (Steinhaus) Theorem

> Formalizes the three-gap (Steinhaus, three-distance) theorem: for every real `a` and every `N`, the `N`-point orbit `{i·a mod 1 : i < N}` partitions `[0,1)` into gaps taking at most three distinct lengths, and when exactly three occur the largest is the sum of the other two. The proof works in `[0,1)` via `Int.fract` (not `AddCircle`) through the two first-return times `η⁺` and `η⁻`, and is uniform in the rotation number, covering rational and irrational `a` with no case split.

*Quoted from the card [LeanPool/projects/three-gap-theorem.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/three-gap-theorem.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`SteinhausThreeGap.three_gap_card_le_three`](https://leanpool.github.io/lean-pool/LeanPool/SteinhausThreeGap/Basic.html#SteinhausThreeGap.three_gap_card_le_three) (theorem; a main declaration), declared in [LeanPool/SteinhausThreeGap/Basic.lean, line 1471](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SteinhausThreeGap/Basic.lean#L1471): “For every real `a` and natural `N`, the gaps of the orbit `{i·a mod 1 : i < N}` take at most three distinct lengths.”
- [`SteinhausThreeGap.three_gap_lengths_eq`](https://leanpool.github.io/lean-pool/LeanPool/SteinhausThreeGap/Basic.html#SteinhausThreeGap.three_gap_lengths_eq) (theorem), declared in [LeanPool/SteinhausThreeGap/Basic.lean, line 1485](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SteinhausThreeGap/Basic.lean#L1485): “When the gaps take exactly three distinct lengths, those lengths are precisely the two first returns `η⁺`, `η⁻`, and their sum `η⁺ + η⁻`; in particular the largest gap is the sum of the other two.”

## Project

- Authors: Dirk Kunert.
- Source: *The Three Gap Theorem (Steinhaus Conjecture)* by Tony van Ravenstein, [doi:10.1017/S1446788700031062](https://doi.org/10.1017/S1446788700031062).
- Project repository: [dkunert/three-gap-theorem-lean](https://github.com/dkunert/three-gap-theorem-lean).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0, keeping its copyright line: “Copyright (c) 2026 Dirk Kunert”.
- MSC2020: 11K06.
- In Lean Pool: [LeanPool/SteinhausThreeGap](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SteinhausThreeGap), from the card [LeanPool/projects/three-gap-theorem.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/three-gap-theorem.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/three-gap-theorem.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/three-gap-theorem.yaml)
- [Lean Pool at 2b205bf9: LeanPool/SteinhausThreeGap](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SteinhausThreeGap)
