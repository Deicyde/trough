---
declaration: theorem
origin: cited
lean: Nock.Verb.runProgram_adequate_complete, Nock.NPR.collision_prob_le
statement: formalized
proof: formalized
---

# Pure Nock semantics, trace certificates, and polynomial fingerprints

> Formalizes Pure Nock nouns with natural-number leaves, operational semantics, evaluator soundness and completeness, verifiable crash behavior, modular evaluation and guarded natural-number bridges, execution trace certificates, and polynomial fingerprints over arbitrary finite fields. Distinct field-valued noun data have bounded fingerprint collision probability, with a union bound for tables sharing one random evaluation point. A computable Horner evaluator agrees with the polynomial fingerprint. The language and fingerprint closure excludes the framework's zkVM, AIR, RAP, table security theorem, and concrete Goldilocks field. Manuscript line references concern the upstream bundled draft v0.1.6, rather than the posted ePrint revision.

*Quoted from the card [LeanPool/projects/pure-nock.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/pure-nock.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 7 main results, each with its informal statement quoted from the card. The scan finds 7 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`Nock.Verb.runProgram_adequate_complete`](https://leanpool.github.io/lean-pool/LeanPool/PureNock/PureComplete.html#Nock.Verb.runProgram_adequate_complete) (theorem; a main declaration), declared in [LeanPool/PureNock/PureComplete.lean, line 1156](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PureNock/PureComplete.lean#L1156): “A subject and formula evaluate to a result under the small-step program machine with some finite fuel if and only if the derived paper evaluator produces that result with some finite fuel.”
- [`Nock.Verb.runTraceProgram_certificate`](https://leanpool.github.io/lean-pool/LeanPool/PureNock/TraceCertificate.html#Nock.Verb.runTraceProgram_certificate) (theorem), declared in [LeanPool/PureNock/TraceCertificate.lean, line 225](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PureNock/TraceCertificate.lean#L225): “Every successfully emitted program trace is consistent and complete, every adjacent transition passes the Nock checker, and the final state is either terminal or has a crash edge accepted by the checker.”
- [`Nock.paper_field_bridge`](https://leanpool.github.io/lean-pool/LeanPool/PureNock/PaperFieldBridge.html#Nock.paper_field_bridge) (theorem), declared in [LeanPool/PureNock/PaperFieldBridge.lean, line 253](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PureNock/PaperFieldBridge.lean#L253): “For a modulus greater than one and inputs whose atoms are below the modulus, successful guarded evaluation produces the same bounded result under natural-number paper evaluation, modular paper evaluation, the full modular evaluator, the natural-number reference evaluator, and the small-step program machine with some finite fuel.”
- [`Nock.NPR.collision_prob_le`](https://leanpool.github.io/lean-pool/LeanPool/PureNock/NPR.html#Nock.NPR.collision_prob_le) (theorem; a main declaration), declared in [LeanPool/PureNock/NPR.lean, line 521](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PureNock/NPR.lean#L521): “For nouns with at most Lambda leaves and distinct field-valued coefficient data or tree shapes, a uniformly selected point of a finite field makes their polynomial fingerprints coincide with probability at most 2 times (2 Lambda minus 1) divided by the field cardinality.”
- [`Nock.NPR.fnHorner_eq_fn`](https://leanpool.github.io/lean-pool/LeanPool/PureNock/Fingerprint.html#Nock.NPR.fnHorner_eq_fn) (theorem), declared in [LeanPool/PureNock/Fingerprint.lean, line 57](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PureNock/Fingerprint.lean#L57): “The computable Horner fingerprint of every noun at every field evaluation point equals its polynomial fingerprint.”
- [`Nock.Verb.eval_crash_iff_invalid`](https://leanpool.github.io/lean-pool/LeanPool/PureNock/Trace.html#Nock.Verb.eval_crash_iff_invalid) (theorem), declared in [LeanPool/PureNock/Trace.lean, line 513](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PureNock/Trace.lean#L513): “The three-valued evaluator reports a crash at some finite fuel exactly when the initial verb has a complete trace ending at a stuck nonterminal state.”
- [`Nock.NPR.collision_table_prob_le`](https://leanpool.github.io/lean-pool/LeanPool/PureNock/NPR.html#Nock.NPR.collision_table_prob_le) (theorem), declared in [LeanPool/PureNock/NPR.lean, line 641](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PureNock/NPR.lean#L641): “For a finite table of bounded-length nouns evaluated at one shared random field point, the probability that some pair with distinct field-valued data collides is at most the single-pair error times k times (k minus 1) divided by 2.”

## Project

- Authors: Pure Nock formalization contributors.
- Contributors: Assimakis A. Kattis.
- Source: *A Generic Compilation Framework for Efficiently Verifiable Virtual Machine Architectures (draft v0.1.6)* by Assimakis A. Kattis, Brian Klatt, Philip Quirk, Logan Allen.
- Project repository: [nockchain/pure-nock-lean](https://github.com/nockchain/pure-nock-lean), at commit [4838863b](https://github.com/nockchain/pure-nock-lean/tree/4838863baa2d49e38573efa3474e77bf1154f300).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 68Q55, 68Q60, 11T71.
- In Lean Pool: [LeanPool/PureNock](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PureNock), from the card [LeanPool/projects/pure-nock.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/pure-nock.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/pure-nock.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/pure-nock.yaml)
- [Lean Pool at 2b205bf9: LeanPool/PureNock](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PureNock)
