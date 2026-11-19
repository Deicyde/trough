---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.AnswerParser.field_append_injective, MIPRE.Introspection.AnswerParser.pairCheck_iff, MIPRE.Introspection.AnswerParser.tripleCheck_iff, MIPRE.Introspection.AnswerParser.pairCheck_pairBits, MIPRE.Introspection.AnswerParser.tripleCheck_tripleBits, MIPRE.Introspection.AnswerParser.pairBits_lt_outer, MIPRE.Introspection.AnswerParser.readBits_lt_outer, MIPRE.Introspection.AnswerParser.hideBits_lt_outer, MIPRE.Introspection.AnswerParser.pairCheck_original_cutoff, MIPRE.Introspection.AnswerParser.readCheck_original_cutoff, MIPRE.Introspection.AnswerParser.guardedProg_closed, MIPRE.Introspection.AnswerParser.guardedProg_reject, MIPRE.Introspection.AnswerParser.guardedProg_halts, MIPRE.Introspection.AnswerParser.guardedProg_haltsWithin, MIPRE.Introspection.AnswerParser.callReady_fields, MIPRE.Introspection.AnswerParser.guardedProg_accepts_iff
statement: formalized
proof: formalized
---

# Executable answer parsing and guarded source calls

For fixed register length $Q$ and original-answer bound $R$, actual polynomial time programs parse the paper's pair and triple answer encodings. They check all register lengths and the separate original-answer cutoff. The encoding uses $00,01$ for bits and $10$ for component termination; exact re-encoding rejects extra fields, malformed delimiters and trailing bits. Under $Q\geq4$ and $3R\leq Q$, honest encodings fit strictly below the outer $8Q$ bound. A guarded source-call program rejects invalid pairs before evaluating the source. On valid pairs, acceptance is exactly source acceptance on the parsed fields, with halting and polynomial runtime transfer for total bounded sources. This component retains the input index and the full register questions. Index-dependent parameter generation and projection to the original question space are supplied by Lemma [Uniform executable cross-introspection compiler](lem-intro-dynamic-source-compiler.md). The complete auxiliary-test dispatch remains a separate obligation.

## Depends on

- [Decider](../../foundations/part-03/def-decider.md)
- [Effective indexing and padding arithmetic](../part-07/lem-pcp-padding-programs.md)

## Proof

Implement doubling and candidate decoding with list folds, then compare the input against the re-encoded candidates. Injectivity follows from the first delimiter. The checked one-call routing program tests the format and inner cutoffs first, and calls the source only on its accepting route. Determinism gives the acceptance equivalence, and the routing cost theorem bounds the complete execution.

## Lean

Formalized as [`MIPRE.Introspection.AnswerParser.field_append_injective`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AnswerParser.field_append_injective), [`MIPRE.Introspection.AnswerParser.pairCheck_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AnswerParser.pairCheck_iff), [`MIPRE.Introspection.AnswerParser.tripleCheck_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AnswerParser.tripleCheck_iff), [`MIPRE.Introspection.AnswerParser.pairCheck_pairBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AnswerParser.pairCheck_pairBits), [`MIPRE.Introspection.AnswerParser.tripleCheck_tripleBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AnswerParser.tripleCheck_tripleBits), [`MIPRE.Introspection.AnswerParser.pairBits_lt_outer`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AnswerParser.pairBits_lt_outer), [`MIPRE.Introspection.AnswerParser.readBits_lt_outer`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AnswerParser.readBits_lt_outer), [`MIPRE.Introspection.AnswerParser.hideBits_lt_outer`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AnswerParser.hideBits_lt_outer), [`MIPRE.Introspection.AnswerParser.pairCheck_original_cutoff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AnswerParser.pairCheck_original_cutoff), [`MIPRE.Introspection.AnswerParser.readCheck_original_cutoff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AnswerParser.readCheck_original_cutoff), [`MIPRE.Introspection.AnswerParser.guardedProg_closed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AnswerParser.guardedProg_closed), [`MIPRE.Introspection.AnswerParser.guardedProg_reject`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AnswerParser.guardedProg_reject), [`MIPRE.Introspection.AnswerParser.guardedProg_halts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AnswerParser.guardedProg_halts), [`MIPRE.Introspection.AnswerParser.guardedProg_haltsWithin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AnswerParser.guardedProg_haltsWithin), [`MIPRE.Introspection.AnswerParser.callReady_fields`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AnswerParser.callReady_fields), [`MIPRE.Introspection.AnswerParser.guardedProg_accepts_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.AnswerParser.guardedProg_accepts_iff).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1906](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1906)
