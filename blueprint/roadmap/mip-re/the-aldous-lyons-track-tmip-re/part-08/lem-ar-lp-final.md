---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.edgeF, MIPRE.Tailored.AnsRed.Typed.lenOkF, MIPRE.Tailored.AnsRed.Typed.LpFin, MIPRE.Tailored.AnsRed.Typed.finBranchF, MIPRE.Tailored.AnsRed.Typed.lpFinal, MIPRE.Tailored.AnsRed.Typed.edgeOf_eq_selectedEdge, MIPRE.Tailored.AnsRed.Typed.LdFamily.sel_chi, MIPRE.Tailored.AnsRed.Typed.ArRoutine.circQ, MIPRE.Tailored.AnsRed.Typed.ArRoutine.prfInF, MIPRE.Tailored.AnsRed.Typed.ArRoutine.proof_lX, MIPRE.Tailored.AnsRed.Typed.ArRoutine.proof_lY, MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpFinal_eq
statement: formalized
proof: formalized
---

# The constraints at two detyped questions, as a program

A program decodes, by a finite table, the edge on which the graph views of two detyped questions lie, checks that the readable answers have their questions' readable lengths, and on the edge's pair of types concatenates the low-degree checks at one role, the consistency checks at one low-degree type, the indifference checks of both answers, and the proof checks of the oracle point answers, the last given as its input. When the proof checks given are those of the two questions at the circuits of their seeds, it outputs the presented answer-reduced game's constraints at the two questions.

## Depends on

- [The proof check's equations, as programs](lem-ar-proof-eqs.md)
- [The consistency and indifference checks, as programs](lem-ar-slot-cons.md)
- [The low-degree checks, as programs](lem-ar-ld-cons.md)
- [The answer-length calculator](../part-07/lem-ar-len.md)
- [The presented answer-reduced game, and meeting it](../part-07/def-ar-meets.md)
- [The parameter routine of the answer-reduced verifier](../part-07/def-ar-routine.md)

## Proof

Off an edge both are empty. On an edge, the typed questions are the vector parts of the two questions, and their types are the ones the views decode to, so the readable lengths are the calculator's (Lemma [The answer-length calculator](../part-07/lem-ar-len.md)). The low-degree bits of a question are the last bits of its vector part, and the selector of the family is the introspection stage's selector program, so each check's program computes the check (Lemmas [The low-degree checks, as programs](lem-ar-ld-cons.md), [The consistency and indifference checks, as programs](lem-ar-slot-cons.md) and [The proof check's equations, as programs](lem-ar-proof-eqs.md)).

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.edgeF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.edgeF), [`MIPRE.Tailored.AnsRed.Typed.lenOkF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.lenOkF), [`MIPRE.Tailored.AnsRed.Typed.LpFin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.LpFin), [`MIPRE.Tailored.AnsRed.Typed.finBranchF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.finBranchF), [`MIPRE.Tailored.AnsRed.Typed.lpFinal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.lpFinal), [`MIPRE.Tailored.AnsRed.Typed.edgeOf_eq_selectedEdge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.edgeOf_eq_selectedEdge), [`MIPRE.Tailored.AnsRed.Typed.LdFamily.sel_chi`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.LdFamily.sel_chi), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.circQ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.circQ), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.prfInF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.prfInF), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.proof_lX`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.proof_lX), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.proof_lY`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.proof_lY), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpFinal_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpFinal_eq).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3807](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3807)
