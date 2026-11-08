---
declaration: theorem
origin: cited
lean: PalomarHS.main_result, PalomarHS.nbc_region_real_volume_le_fork_factor
statement: formalized
proof: formalized
---

# Hard-sphere Mayer NBC identity and fork-packing volume bound

> A kernel-checked Lean formalization of the exact no-broken-circuit volume identity for hard-sphere Mayer cluster integrals and the stronger dimension-three fork-packing upper bound for each tree-owned NBC region. The development proves finite broken-circuit cancellation, the measurable finite-region decomposition, the anchored Euclidean product-measure theorem, and its explicit flat-coordinate transport. Its geometric result is the attachment-aware estimate Vol(NBC_T) <= (17/32)^hardSphereNu T \* hardSphereKappa^(k-1), where hardSphereNu T is the maximum cardinality of a packing of pairwise vertex-disjoint, order-compatible forks in T. A formal fork is an ordered triple (a,b,c) with a < b < c, center a, leaves b,c, and tree edges {a,b} and {a,c}. The central contribution is the complete pointwise-to-integral bridge together with the orientation-aware measure-preserving factorization that realizes the per-fork volume suppression.

*Quoted from the card [LeanPool/projects/hs-virial-nbc-identity.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/hs-virial-nbc-identity.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`PalomarHS.main_result`](https://leanpool.github.io/lean-pool/LeanPool/HardSphereNBC/Solution.html#PalomarHS.main_result) (theorem; a main declaration), declared in [LeanPool/HardSphereNBC/Solution.lean, line 28](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HardSphereNBC/Solution.lean#L28): “The absolute hard-sphere Mayer coefficient, multiplied by the factorial, equals the sum of nonnegative no-broken-circuit region volumes over spanning trees.”
- [`PalomarHS.nbc_region_real_volume_le_fork_factor`](https://leanpool.github.io/lean-pool/LeanPool/HardSphereNBC/Solution.html#PalomarHS.nbc_region_real_volume_le_fork_factor) (theorem; a main declaration), declared in [LeanPool/HardSphereNBC/Solution.lean, line 107](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HardSphereNBC/Solution.lean#L107): “For a spanning tree in three dimensions, its no-broken-circuit region has volume at most (17/32) to the maximum disjoint compatible-fork packing size times the unit-ball volume to the number of tree edges.”

## Project

- Authors: ukiyois, OpenCode agent sessions.
- Project repository: [ukiyois/hs-virial-nbc-identity](https://github.com/ukiyois/hs-virial-nbc-identity), at commit [fd0a1e73](https://github.com/ukiyois/hs-virial-nbc-identity/tree/fd0a1e73c336574fa9655f9ab3c0cd9ce5c4fcce).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C15, 82B05.
- In Lean Pool: [LeanPool/HardSphereNBC](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HardSphereNBC), from the card [LeanPool/projects/hs-virial-nbc-identity.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/hs-virial-nbc-identity.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/hs-virial-nbc-identity.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/hs-virial-nbc-identity.yaml)
- [Lean Pool at 2b205bf9: LeanPool/HardSphereNBC](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HardSphereNBC)
