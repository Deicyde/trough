---
declaration: lemma
origin: cited
lean: MIPRE.CL.Detyping.DeciderProgram.prog_closed, MIPRE.CL.Detyping.DeciderProgram.prog_halts, MIPRE.CL.Detyping.DeciderProgram.decider, MIPRE.CL.Detyping.DeciderProgram.raw_accepts_iff, MIPRE.CL.Detyping.DeciderProgram.accepts_iff, MIPRE.CL.Detyping.DeciderProgram.verifier, MIPRE.CL.Detyping.DeciderProgram.verifier_rejectsLong, MIPRE.CL.Detyping.DeciderProgram.bounded_acceptance, MIPRE.CL.Detyping.DeciderProgram.bounded_acceptance_edge, MIPRE.CL.Detyping.DeciderProgram.verifier_game_D
statement: formalized
proof: formalized
---

# Executable detyping decider with two answer cuts

Given an actual typed sampler, an all-input terminating typed decider and an executable index routine returning inner and outer answer cuts, construct an ambient detyped verifier. It rejects malformed raw encodings, wrong question lengths and answers beyond the outer cut. Within that cut, a nonedge accepts; a genuine edge additionally enforces the source typed-answer cut and calls the typed decider on the unchanged answers and content questions. On the outer finite answer alphabet its predicate is exactly the finite detyping predicate with the inner rejection included. The inner cut bounds the whole typed answer; an introspection implementation must separately check the original answer component before calling the original decider.

## Depends on

- [Executable detyping sampler](lem-detype-functional-sampler.md)
- [Normal form verifier in the ambient model](../../foundations/part-03/def-normal-verifier.md)
- [Typed decider and normal verifier](def-typed-normal-interface.md)

## Proof

Use actual dimension and cutoff calls followed by a total finite-graph router. Only the canonical Boolean true result accepts. Evaluation determinism gives the exact acceptance equivalence, and the coordinate-numbering identities give the finite predicate equality. These statements prove no runtime bound for the supplied cutoff routine and assume no implicit inequality between the two cuts. Such bounds and the appropriate cut comparison remain explicit requirements when constructing a bounded compiler and transferring completeness.

## Lean

Formalized as [`MIPRE.CL.Detyping.DeciderProgram.prog_closed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.DeciderProgram.prog_closed), [`MIPRE.CL.Detyping.DeciderProgram.prog_halts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.DeciderProgram.prog_halts), [`MIPRE.CL.Detyping.DeciderProgram.decider`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.DeciderProgram.decider), [`MIPRE.CL.Detyping.DeciderProgram.raw_accepts_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.DeciderProgram.raw_accepts_iff), [`MIPRE.CL.Detyping.DeciderProgram.accepts_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.DeciderProgram.accepts_iff), [`MIPRE.CL.Detyping.DeciderProgram.verifier`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.DeciderProgram.verifier), [`MIPRE.CL.Detyping.DeciderProgram.verifier_rejectsLong`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.DeciderProgram.verifier_rejectsLong), [`MIPRE.CL.Detyping.DeciderProgram.bounded_acceptance`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.DeciderProgram.bounded_acceptance), [`MIPRE.CL.Detyping.DeciderProgram.bounded_acceptance_edge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.DeciderProgram.bounded_acceptance_edge), [`MIPRE.CL.Detyping.DeciderProgram.verifier_game_D`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.DeciderProgram.verifier_game_D).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 647](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L647)
