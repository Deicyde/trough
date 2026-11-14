---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.eval_killCompl, MIPRE.LowDegree.degreeOf_killCompl_le, MIPRE.SAT.Circuit.inputRef_injective, MIPRE.SAT.Circuit.routedConsistent_iff, MIPRE.SAT.Circuit.eval_iff_routedConsistent, MIPRE.SAT.Circuit.degreeOf_routedArith_le, MIPRE.SAT.Circuit.eval_routedArith_iff, MIPRE.SAT.Circuit.eval_routedArith_bool, MIPRE.SAT.Circuit.degreeOf_finiteArith_le, MIPRE.SAT.Circuit.eval_finiteArith_bool, MIPRE.SAT.Circuit.eval_iff_exists_finiteArith
statement: formalized
proof: formalized
---

# Circuit arithmetization with bounded input use

Over a field of characteristic two, every well-formed circuit with $n$ inputs and $s$ gates has a Boolean-valued arithmetization on exactly $n+s$ coordinates, of individual degree at most five, hence at most six. An input is accepted exactly when it extends to a Boolean assignment at which this polynomial is one.

## Depends on

- [The low-degree code](def-ld-encoding.md)

## Proof

The current circuit interface bounds gate fan-out, but permits repeated reads of one external input. Route the first read through the external variable and each later read through its preceding input gate. These copy links use each variable at most once and preserve all Boolean gate values. In characteristic two, $1+w_g+\mathrm{rhs}_g$ indicates gate consistency. Multiply these factors and the output literal. A variable contributes at most one degree from its own factor, two from ordinary fan-out, one from a copy link, and one from the output literal. Restrict to the exact input and gate coordinates by setting all other variables to zero; this preserves degree and evaluation. The polynomial-time field evaluator for this expression is supplied by Lemma [Effective circuit polynomial evaluation](lem-pcp-circuit-evaluator.md).

## Lean

Formalized as [`MIPRE.LowDegree.eval_killCompl`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.eval_killCompl), [`MIPRE.LowDegree.degreeOf_killCompl_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.degreeOf_killCompl_le), [`MIPRE.SAT.Circuit.inputRef_injective`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.inputRef_injective), [`MIPRE.SAT.Circuit.routedConsistent_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.routedConsistent_iff), [`MIPRE.SAT.Circuit.eval_iff_routedConsistent`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.eval_iff_routedConsistent), [`MIPRE.SAT.Circuit.degreeOf_routedArith_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.degreeOf_routedArith_le), [`MIPRE.SAT.Circuit.eval_routedArith_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.eval_routedArith_iff), [`MIPRE.SAT.Circuit.eval_routedArith_bool`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.eval_routedArith_bool), [`MIPRE.SAT.Circuit.degreeOf_finiteArith_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.degreeOf_finiteArith_le), [`MIPRE.SAT.Circuit.eval_finiteArith_bool`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.eval_finiteArith_bool), [`MIPRE.SAT.Circuit.eval_iff_exists_finiteArith`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.Circuit.eval_iff_exists_finiteArith).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4850](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4850)
