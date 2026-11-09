---
declaration: def
origin: cited
lean: hoareTripleUp, S_SEQ, proof_otp
statement: formalized
---

# MRiscX

> A Hoare logic for verifying unstructured RISC-V-like assembly in Lean, following Lundberg et al. (SEFM 2020), with a certified interpreter, proved structural Hoare rules, per-instruction specifications, custom elaborators and tactics, and a complete One-Time-Pad correctness proof.

*Quoted from the card [LeanPool/projects/mriscx.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/mriscx.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`hoareTripleUp`](https://leanpool.github.io/lean-pool/LeanPool/MRiscX/Hoare/HoareCore.html#hoareTripleUp) (def; a main declaration), declared in [LeanPool/MRiscX/Hoare/HoareCore.lean, line 91](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MRiscX/Hoare/HoareCore.lean#L91): “Defines the MRiscX Hoare triple, asserting that from any state satisfying the precondition the code reaches a successor state satisfying the postcondition while respecting the line whitelist and blacklist.” Its source, as the card gives it: “D. Lundberg, R. Guanciale, A. Lindner, M. Dam, Hoare-Style Logic for Unstructured Programs, SEFM 2020, doi:10.1007/978-3-030-58768-0_11.”
- [`S_SEQ`](https://leanpool.github.io/lean-pool/LeanPool/MRiscX/Hoare/HoareRules.html#S_SEQ) (theorem; a main declaration), declared in [LeanPool/MRiscX/Hoare/HoareRules.lean, line 134](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MRiscX/Hoare/HoareRules.lean#L134): “Proves the sequencing Hoare rule, peeling off the last instruction of a code block.” Its source, as the card gives it: “D. Lundberg, R. Guanciale, A. Lindner, M. Dam, Hoare-Style Logic for Unstructured Programs, SEFM 2020, doi:10.1007/978-3-030-58768-0_11.”
- [`PRE_STR`](https://leanpool.github.io/lean-pool/LeanPool/MRiscX/Hoare/HoareRules.html#PRE_STR) (theorem), declared in [LeanPool/MRiscX/Hoare/HoareRules.lean, line 207](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MRiscX/Hoare/HoareRules.lean#L207): “Proves the precondition-strengthening rule for MRiscX Hoare triples.”
- [`POST_WEAK`](https://leanpool.github.io/lean-pool/LeanPool/MRiscX/Hoare/HoareRules.html#POST_WEAK) (theorem), declared in [LeanPool/MRiscX/Hoare/HoareRules.lean, line 224](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MRiscX/Hoare/HoareRules.lean#L224): “Proves the postcondition-weakening rule for MRiscX Hoare triples.”
- [`specification_LoadImmediate`](https://leanpool.github.io/lean-pool/LeanPool/MRiscX/Semantics/Specification.html#specification_LoadImmediate) (theorem), declared in [LeanPool/MRiscX/Semantics/Specification.lean, line 66](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MRiscX/Semantics/Specification.lean#L66): “Proves the per-instruction Hoare specification of the load-immediate instruction.”
- [`proof_otp`](https://leanpool.github.io/lean-pool/LeanPool/MRiscX/Examples/OtpProof.html#proof_otp) (theorem; a main declaration), declared in [LeanPool/MRiscX/Examples/OtpProof.lean, line 393](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MRiscX/Examples/OtpProof.lean#L393): “Proves the full correctness of a One-Time-Pad implementation written in MRiscX assembly.”

## Project

- Authors: Julius Marx.
- Source: [doi:10.1007/978-3-030-58768-0_11](https://doi.org/10.1007/978-3-030-58768-0_11).
- Project repository: [JulsDE/MRiscX](https://github.com/JulsDE/MRiscX).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 68Q60.
- In Lean Pool: [LeanPool/MRiscX](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MRiscX), from the card [LeanPool/projects/mriscx.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/mriscx.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/mriscx.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/mriscx.yaml)
- [Lean Pool at 2b205bf9: LeanPool/MRiscX](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MRiscX)
