---
declaration: lemma
origin: cited
lean: MIPRE.CL.Detyping.ClockProgram.constant, MIPRE.CL.Detyping.ClockProgram.ofPolyTimeFun, MIPRE.CL.Detyping.ClockProgram.clockedResult_eq_iff, MIPRE.CL.Detyping.ClockProgram.wrapProg_halts, MIPRE.CL.Detyping.ClockProgram.wrapProg_accepts_iff, MIPRE.CL.Detyping.ClockProgram.wrap, MIPRE.CL.Detyping.ClockProgram.wrap_total, MIPRE.CL.Detyping.ClockProgram.wrap_accepts_iff_of_bounded, MIPRE.CL.Detyping.ClockProgram.decider, MIPRE.CL.Detyping.ClockProgram.decider_total, MIPRE.CL.Detyping.ClockProgram.decider_accepts_iff, MIPRE.CL.Detyping.ClockProgram.wrapProg_haltsWithin
statement: formalized
proof: formalized
---

# Total clocking of arbitrary typed decision programs

An executable index routine producing a unary cost budget gives a total typed decider from arbitrary source code, even if that code does not halt. The wrapper accepts exactly when the source returns the canonical Boolean true within the supplied budget. It preserves the acceptance predicate on inputs whose source evaluation is known to fit. The default construction uses the proved clocked self-interpreter. An explicit wrapper-cost bound combines the actual index-clock cost, interpreter polynomial and routing overhead. This supplies the totality mechanism; instantiating the appropriate growing clock and proving the final compiler's time, size and answer-format bounds remain separate obligations.

## Depends on

- [Typed decider and normal verifier](def-typed-normal-interface.md)
- [Effective indexing and padding arithmetic](../part-07/lem-pcp-padding-programs.md)

## Proof

Run the index clock, invoke the clocked universal interpreter on the complete original input, and inspect its success tag and Boolean result. The interpreter halts for every source program. Evaluation determinism identifies its tagged result with precisely an in-budget source evaluation, proving both directions of the acceptance law without a source-termination assumption.

## Lean

Formalized as [`MIPRE.CL.Detyping.ClockProgram.constant`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.ClockProgram.constant), [`MIPRE.CL.Detyping.ClockProgram.ofPolyTimeFun`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.ClockProgram.ofPolyTimeFun), [`MIPRE.CL.Detyping.ClockProgram.clockedResult_eq_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.ClockProgram.clockedResult_eq_iff), [`MIPRE.CL.Detyping.ClockProgram.wrapProg_halts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.ClockProgram.wrapProg_halts), [`MIPRE.CL.Detyping.ClockProgram.wrapProg_accepts_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.ClockProgram.wrapProg_accepts_iff), [`MIPRE.CL.Detyping.ClockProgram.wrap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.ClockProgram.wrap), [`MIPRE.CL.Detyping.ClockProgram.wrap_total`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.ClockProgram.wrap_total), [`MIPRE.CL.Detyping.ClockProgram.wrap_accepts_iff_of_bounded`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.ClockProgram.wrap_accepts_iff_of_bounded), [`MIPRE.CL.Detyping.ClockProgram.decider`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.ClockProgram.decider), [`MIPRE.CL.Detyping.ClockProgram.decider_total`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.ClockProgram.decider_total), [`MIPRE.CL.Detyping.ClockProgram.decider_accepts_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.ClockProgram.decider_accepts_iff), [`MIPRE.CL.Detyping.ClockProgram.wrapProg_haltsWithin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.ClockProgram.wrapProg_haltsWithin).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 716](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L716)
