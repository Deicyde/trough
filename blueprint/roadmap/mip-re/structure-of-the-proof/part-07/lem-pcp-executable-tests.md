---
declaration: lemma
origin: cited
lean: MIPRE.SAT.validProg_true_iff, MIPRE.SAT.viewFormatProg_true_iff, MIPRE.SAT.shoupRoot_equation, MIPRE.SAT.shoupRoot_eval_toBits, MIPRE.SAT.shoupRoot_eval_eq_iff, MIPRE.SAT.PcpFieldTests.checksProg_true_iff, MIPRE.SAT.PcpViewTests.checks_typed_iff, MIPRE.TM.CookLevin.Pad.verifyPcp_reject_invalid, MIPRE.TM.CookLevin.Pad.verifyPcp_time_le, MIPRE.TM.CookLevin.Pad.verifyPcp_rawView_iff
statement: formalized
proof: formalized
---

# The executable PCP tests

A uniform ambient program checks specification validity and all view dimensions, constructs the padded circuit within the view's unary output budget, and performs both polynomial tests. On a represented low-degree proof it accepts exactly when the typed algebraic tests hold. Invalid specifications and malformed views are rejected. Its runtime on valid formatted inputs is polynomial in $\log n+\log T+Q+\sigma$.

## Depends on

- [Effective circuit polynomial evaluation](lem-pcp-circuit-evaluator.md)
- [PCP semantics for a circuit describer](lem-pcp-circuit-semantics.md)
- [Encoded PCP view size and source runtime](lem-pcp-view-size.md)
- [Effective polynomial-basis field arithmetic](../../background-results/part-05/lem-effective-binary-field-arithmetic.md)

## Proof

Use binary comparisons for the parameters and list scans for the shape checks. Evaluate the circuit and both field identities using coefficient-vector arithmetic. Fixed-width evaluation at the Shoup quotient's root is injective, so raw bit equality is field equality. The clause coordinates and answer blocks agree with the typed proof view. Apply Lemma [Encoded PCP view size and source runtime](lem-pcp-view-size.md) to the assembled program.

## Lean

Formalized as [`MIPRE.SAT.validProg_true_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.validProg_true_iff), [`MIPRE.SAT.viewFormatProg_true_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.viewFormatProg_true_iff), [`MIPRE.SAT.shoupRoot_equation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupRoot_equation), [`MIPRE.SAT.shoupRoot_eval_toBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupRoot_eval_toBits), [`MIPRE.SAT.shoupRoot_eval_eq_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupRoot_eval_eq_iff), [`MIPRE.SAT.PcpFieldTests.checksProg_true_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpFieldTests.checksProg_true_iff), [`MIPRE.SAT.PcpViewTests.checks_typed_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.PcpViewTests.checks_typed_iff), [`MIPRE.TM.CookLevin.Pad.verifyPcp_reject_invalid`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.verifyPcp_reject_invalid), [`MIPRE.TM.CookLevin.Pad.verifyPcp_time_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.verifyPcp_time_le), [`MIPRE.TM.CookLevin.Pad.verifyPcp_rawView_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TM.CookLevin.Pad.verifyPcp_rawView_iff).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4962](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4962)
