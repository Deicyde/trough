---
declaration: theorem
origin: cited
lean: Sundog.SATReductionMain.sat_iff_decodes, Sundog.Certificate.accept_sound
statement: formalized
proof: formalized
---

# Sundog certificates

> A referee-free, axiom-clean Lean development of coding-theory certificates: syndrome decoding soundness and lossiness bounds for GF(2) parity-check schemes (with a Reed–Solomon evaluation-dual variant), and a fully machine-checked correctness proof of the Karp reduction chain 3SAT ≤ 3DM ≤ X3C ≤ bounded-weight syndrome decoding. Only the logical iff of each reduction is formalized; polynomial-time bounds, NP classes, and Cook–Levin are unformalized external inputs, so NP-hardness of decoding is conditional on those standard facts.

*Quoted from the card [LeanPool/projects/sundogcert.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/sundogcert.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`Sundog.SATReductionMain.sat_iff_decodes`](https://leanpool.github.io/lean-pool/LeanPool/Sundogcert/SATReductionMain.html#Sundog.SATReductionMain.sat_iff_decodes) (theorem; a main declaration), declared in [LeanPool/Sundogcert/SATReductionMain.lean, line 81](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Sundogcert/SATReductionMain.lean#L81): “The end-to-end reduction correctness: a formula is satisfiable iff its image under the composed 3SAT-to-decoding reduction is a yes-instance of bounded-weight syndrome decoding.”
- [`Sundog.MatchingNPHard.threeDM_iff_X3C`](https://leanpool.github.io/lean-pool/LeanPool/Sundogcert/MatchingNPHard.html#Sundog.MatchingNPHard.threeDM_iff_X3C) (theorem), declared in [LeanPool/Sundogcert/MatchingNPHard.lean, line 139](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Sundogcert/MatchingNPHard.lean#L139): “The 3-dimensional matching instance has a perfect matching iff the reduced exact-cover-by-3-sets instance has an exact cover, both directions machine-checked.”
- [`Sundog.Certificate.accept_sound`](https://leanpool.github.io/lean-pool/LeanPool/Sundogcert/Certificate.html#Sundog.Certificate.accept_sound) (theorem; a main declaration), declared in [LeanPool/Sundogcert/Certificate.lean, line 115](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Sundogcert/Certificate.lean#L115): “Soundness of the cheap syndrome-decoding verifier when it accepts: an exhibited light same-syndrome witness certifies the body is safe within the decoding radius.”
- [`Sundog.Certificate.reject_sound`](https://leanpool.github.io/lean-pool/LeanPool/Sundogcert/Certificate.html#Sundog.Certificate.reject_sound) (theorem), declared in [LeanPool/Sundogcert/Certificate.lean, line 138](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Sundogcert/Certificate.lean#L138): “Soundness of the verifier when it rejects: a sound column-weight lower bound on the minimum same-syndrome weight rules out every light witness, so the body is genuinely unsafe.”

## Project

- Authors: Humiliati.
- Source: *Sundog certificates* by Humiliati.
- Project repository: [humiliati/sundogcert](https://github.com/humiliati/sundogcert).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 68Q17, 94B35.
- In Lean Pool: [LeanPool/Sundogcert](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Sundogcert), from the card [LeanPool/projects/sundogcert.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/sundogcert.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/sundogcert.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/sundogcert.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Sundogcert](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Sundogcert)
