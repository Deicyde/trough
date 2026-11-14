---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.zAt, MIPRE.Tailored.AnsRed.Typed.zAt_eq, MIPRE.Tailored.AnsRed.Typed.asgLin, MIPRE.Tailored.AnsRed.Typed.sysLin, MIPRE.Tailored.AnsRed.Typed.proofEqs_eq, MIPRE.Tailored.AnsRed.Typed.asgEqF, MIPRE.Tailored.AnsRed.Typed.asgEqF_eq, MIPRE.Tailored.AnsRed.Typed.sysEqF, MIPRE.Tailored.AnsRed.Typed.sysEqF_eq, MIPRE.Tailored.AnsRed.Typed.proofEqsF, MIPRE.Tailored.AnsRed.Typed.proofEqsF_eq, MIPRE.Tailored.AnsRed.Typed.proofConsF, MIPRE.Tailored.AnsRed.Typed.proofConsF_eq
statement: formalized
proof: formalized
---

# The proof check's equations, as programs

A program computes, from the parameters, the offset and length of the answer bits, the coordinates of a point $p$, the oracle's readable answer and the gates of a well-formed circuit with the PCP's numbers of inputs and gates, the constraints of the proof check of the oracle's point answer: the readable checks of Lemma [The circuit polynomial and the proof check's readable part, as programs](lem-ar-proof-guard.md) as a guard, then the system check and the five linear assignment checks at $p$, as field equations in the answer bits.

## Depends on

- [The circuit polynomial and the proof check's readable part, as programs](lem-ar-proof-guard.md)
- [Field equations as constraints, and field arithmetic, as programs](lem-ar-field-cons.md)
- [The answer-reduced game as typed tailored data; defn:combi_ans_red](../part-06/def-ar-tailored-game.md)
- [The constraint lists of the auxiliary checks, as programs](../part-05/lem-intro-aux-progs.md)

## Proof

The value of each equation at the answer bits is a field expression in the point's coordinates, the readable value of $g_O$ and the linear values at the slots' positions, which the combinators of Lemma [Field equations as constraints, and field arithmetic, as programs](lem-ar-field-cons.md) compute; the positions of the linear slots follow the readable ones. Lemma [Field equations as constraints, and field arithmetic, as programs](lem-ar-field-cons.md) turns the values into the constraints.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.zAt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.zAt), [`MIPRE.Tailored.AnsRed.Typed.zAt_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.zAt_eq), [`MIPRE.Tailored.AnsRed.Typed.asgLin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.asgLin), [`MIPRE.Tailored.AnsRed.Typed.sysLin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sysLin), [`MIPRE.Tailored.AnsRed.Typed.proofEqs_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.proofEqs_eq), [`MIPRE.Tailored.AnsRed.Typed.asgEqF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.asgEqF), [`MIPRE.Tailored.AnsRed.Typed.asgEqF_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.asgEqF_eq), [`MIPRE.Tailored.AnsRed.Typed.sysEqF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sysEqF), [`MIPRE.Tailored.AnsRed.Typed.sysEqF_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sysEqF_eq), [`MIPRE.Tailored.AnsRed.Typed.proofEqsF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.proofEqsF), [`MIPRE.Tailored.AnsRed.Typed.proofEqsF_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.proofEqsF_eq), [`MIPRE.Tailored.AnsRed.Typed.proofConsF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.proofConsF), [`MIPRE.Tailored.AnsRed.Typed.proofConsF_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.proofConsF_eq).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3781](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3781)
