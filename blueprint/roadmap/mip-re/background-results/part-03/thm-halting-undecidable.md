---
declaration: theorem
origin: cited
lean: MIPRE.halting_undecidable, MIPRE.halting_re, MIPRE.Halting.exists_code_halts_of_isRE
statement: formalized
proof: formalized
---

# Turing

The halting problem is r.e. but not decidable; it is $\mathrm{RE}$-complete under many-one (indeed polynomial-time) reductions.

## Depends on

- [Recursively enumerable](../../foundations/part-02/def-re.md)

## Proof

Mathlib: `ComputablePred.halting_problem` and `halting_problem_re`, both at the empty input; the many-one reduction of an r.e. language to halting on the empty input is `MIPRE.IsRE.exists_code_halts`, by Mathlib's $S^m_n$ function `Nat.Partrec.Code.curry`. Polynomial-time computability of the reduction is not formalized (Section [Departures from the paper](../../introduction/README.md)).

## Lean

Formalized as [`MIPRE.halting_undecidable`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.halting_undecidable), [`MIPRE.halting_re`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.halting_re), [`MIPRE.Halting.exists_code_halts_of_isRE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.exists_code_halts_of_isRE).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 5945](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L5945)
