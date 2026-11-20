---
declaration: theorem
origin: cited
lean: OAI.TuringRigidity.TwoConeMain.cones_orderIso_iff, OAI.TuringRigidity.TwoConeMain.cone_iso_apply_val
statement: formalized
proof: formalized
---

# Pairwise rigidity of principal upper cones of the Turing degrees

> Proves that principal upper cones of ordinary Turing degrees are order-isomorphic exactly when their base degrees agree, and that every such isomorphism fixes every underlying degree. Includes the required computability, degree coding, countable-model, forcing, persistence, and Baire-category infrastructure inherited from OpenAI's degree-rigidity development, together with the cone-specific extensions. No determinacy or regularity premise is imposed. The separate historical truth-table-degree project is outside this import.

*Quoted from the card [LeanPool/projects/turing-cone-rigidity.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/turing-cone-rigidity.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`OAI.TuringRigidity.TwoConeMain.cones_orderIso_iff`](https://leanpool.github.io/lean-pool/LeanPool/TuringConeRigidity/TuringTwoConeMain.html#OAI.TuringRigidity.TwoConeMain.cones_orderIso_iff) (theorem; a main declaration), declared in [LeanPool/TuringConeRigidity/TuringTwoConeMain.lean, line 99](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/TuringConeRigidity/TuringTwoConeMain.lean#L99): “For ordinary Turing degrees a and b, an order isomorphism between their principal upper cones exists if and only if a = b.” Its source, as the card gives it: “Upstream RequestProject/TuringTwoConeMain.lean, theorem cones_orderIso_iff, at commit 99621af8867a5d272b16eb1454a15f59fb43e9ea; Palomar PALOMAR-2026-11-09-000019 v2.”
- [`OAI.TuringRigidity.TwoConeMain.cone_iso_apply_val`](https://leanpool.github.io/lean-pool/LeanPool/TuringConeRigidity/TuringTwoConeMain.html#OAI.TuringRigidity.TwoConeMain.cone_iso_apply_val) (theorem; a main declaration), declared in [LeanPool/TuringConeRigidity/TuringTwoConeMain.lean, line 104](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/TuringConeRigidity/TuringTwoConeMain.lean#L104): “Every order isomorphism between principal upper cones sends each degree to itself, without continuity, measurability, determinacy, or model-existence assumptions.” Its source, as the card gives it: “Upstream RequestProject/TuringTwoConeMain.lean, theorem cone_iso_apply_val, at commit 99621af8867a5d272b16eb1454a15f59fb43e9ea; Palomar PALOMAR-2026-11-09-000019 v2.”

## Project

- Authors: Bjørn Kjos-Hanssen, OpenAI.
- Source: *Pairwise rigidity of principal Turing cones* by Bjørn Kjos-Hanssen.
- Project repository: [bjoernkjoshanssen/tt-auto](https://github.com/bjoernkjoshanssen/tt-auto), at commit [99621af8](https://github.com/bjoernkjoshanssen/tt-auto/tree/99621af8867a5d272b16eb1454a15f59fb43e9ea).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 03D28, 03B35.
- In Lean Pool: [LeanPool/TuringConeRigidity](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/TuringConeRigidity), from the card [LeanPool/projects/turing-cone-rigidity.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/turing-cone-rigidity.yaml).

## Sources

- [Lean Pool at 307e3125: LeanPool/projects/turing-cone-rigidity.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/turing-cone-rigidity.yaml)
- [Lean Pool at 307e3125: LeanPool/TuringConeRigidity](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/TuringConeRigidity)
