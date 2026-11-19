---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.ArRoutine.argMgL_eq, MIPRE.Tailored.AnsRed.Typed.ArRoutine.marg_runs, MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpCore_runs, MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpD_lpIs
statement: formalized
proof: formalized
---

# The processor computes the presented constraints

At every index and every pair of detyped questions and readable answers, the processor halts with the presented answer-reduced game's constraints.

## Depends on

- [The linear-constraints processor of the answer-reduced verifier](def-ar-lp.md)
- [The constraints at two detyped questions, as a program](lem-ar-lp-final.md)

## Proof

Each stage halts with the expected output: the parameter program by the routine, the input sampler on its marginal queries, and the circuit function and the proof check, polynomial-time functions, on the encodings of their inputs. Then Lemma [The constraints at two detyped questions, as a program](lem-ar-lp-final.md).

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.argMgL_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.argMgL_eq), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.marg_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.marg_runs), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpCore_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpCore_runs), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpD_lpIs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpD_lpIs).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3855](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3855)
