---
declaration: theorem
origin: cited
lean: LeanPool.Shannon1948Formalization.entropyNat_unique
statement: formalized
proof: formalized
---

# Shannon Entropy Characterization

> Formalizes Shannon's finite-alphabet characterization theorem for entropy from the 1948 paper.

*Quoted from the card [LeanPool/projects/shannon-1948-formalization.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/shannon-1948-formalization.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LeanPool.Shannon1948Formalization.entropyNat_unique`](https://leanpool.github.io/lean-pool/LeanPool/Shannon1948Formalization/Entropy/Final.html#LeanPool.Shannon1948Formalization.entropyNat_unique) (theorem; a main declaration), declared in [LeanPool/Shannon1948Formalization/Entropy/Final.lean, line 46](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Shannon1948Formalization/Entropy/Final.lean#L46): “Proves that any finite-alphabet uncertainty functional satisfying Shannon's conditions equals natural-log entropy up to a positive scale.”
- [`LeanPool.Shannon1948Formalization.entropyBase_unique`](https://leanpool.github.io/lean-pool/LeanPool/Shannon1948Formalization/Entropy/Final.html#LeanPool.Shannon1948Formalization.entropyBase_unique) (theorem), declared in [LeanPool/Shannon1948Formalization/Entropy/Final.lean, line 68](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Shannon1948Formalization/Entropy/Final.lean#L68): “Restates the characterization for any logarithm base greater than one.”
- [`LeanPool.Shannon1948Formalization.entropyNat_shannonAxioms`](https://leanpool.github.io/lean-pool/LeanPool/Shannon1948Formalization/Entropy/Converse.html#LeanPool.Shannon1948Formalization.entropyNat_shannonAxioms) (theorem), declared in [LeanPool/Shannon1948Formalization/Entropy/Converse.lean, line 94](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Shannon1948Formalization/Entropy/Converse.lean#L94): “Proves the converse, showing that Shannon entropy satisfies the formal condition bundle.”
- [`LeanPool.Shannon1948Formalization.chain_rule`](https://leanpool.github.io/lean-pool/LeanPool/Shannon1948Formalization/Entropy/Joint.html#LeanPool.Shannon1948Formalization.chain_rule) (theorem), declared in [LeanPool/Shannon1948Formalization/Entropy/Joint.lean, line 127](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Shannon1948Formalization/Entropy/Joint.lean#L127): “Proves the finite joint-entropy chain rule.”
- `LeanPool.Shannon1948Formalization.entropyNat_joint_le_add`, which the scan does not find declared in the project's files at this commit: “Proves subadditivity of finite joint entropy.”

## Project

- Authors: Samuel Schlesinger.
- Source: [doi:10.1002/j.1538-7305.1948.tb01338.x](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x).
- Project repository: [SamuelSchlesinger/shannon-1948-formalization](https://github.com/SamuelSchlesinger/shannon-1948-formalization).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0. Lean Pool's notice file notes: “The upstream MIT LICENSE file gives the copyright line as "Copyright (c) 2026" with no name; the repository owner of record is "SamuelSchlesinger".”
- MSC2020: 94A17, 60C05.
- In Lean Pool: [LeanPool/Shannon1948Formalization](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Shannon1948Formalization), from the card [LeanPool/projects/shannon-1948-formalization.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/shannon-1948-formalization.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/shannon-1948-formalization.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/shannon-1948-formalization.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Shannon1948Formalization](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Shannon1948Formalization)
