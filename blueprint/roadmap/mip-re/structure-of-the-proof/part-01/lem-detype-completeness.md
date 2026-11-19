---
declaration: lemma
origin: cited
lean: MIPRE.CL.Detyping.DeciderProgram.verifier_hasPerfectPCC
statement: formalized
proof: formalized
---

# Detyping PCC completeness

A perfect PCC typed witness lifts on the same state to a perfect PCC detyped witness. Both players use the same combined rule: on an Alice-view pattern use the original Alice operator, on a Bob-view pattern use the original Bob operator, and otherwise use the identity measurement. The view patterns are disjoint. On valid edges this reproduces the typed strategy; on invalid edges one local measurement is trivial. Projectivity, consistency and the required commutation follow, as does the identical-operator property. This does not assert symmetry of the detyped question distribution.

## Depends on

- [PCC strategy](../../foundations/part-01/def-pcc.md)

## Proof depends on

- [Strategy transfer for the executable detyping verifier](lem-detype-program-strategies.md)

## Proof

This is Lemma [Finite-game detyping PCC completeness](lem-detype-game-completeness.md) for the finite games, transported to the executable detyped verifier by Lemma [Strategy transfer for the executable detyping verifier](lem-detype-program-strategies.md). The identity measurement on invalid views is a fixed deterministic answer.

## Lean

Formalized as [`MIPRE.CL.Detyping.DeciderProgram.verifier_hasPerfectPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.DeciderProgram.verifier_hasPerfectPCC).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 773](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L773)
