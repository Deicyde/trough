---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.circValF, MIPRE.Tailored.AnsRed.Typed.circValF_eq, MIPRE.Tailored.AnsRed.Typed.PrfIn, MIPRE.Tailored.AnsRed.Typed.formF, MIPRE.Tailored.AnsRed.Typed.formF_eq, MIPRE.Tailored.AnsRed.Typed.guardF, MIPRE.Tailored.AnsRed.Typed.guardF_eq
statement: formalized
proof: formalized
---

# The circuit polynomial and the proof check's readable part, as programs

A program computes, from the coordinates of a point $p \in \mathbb{F}_q^m$ and the gates of a well-formed circuit with $n_{\mathrm{in}}$ inputs and $s$ gates, $n_{\mathrm{in}} + s = m$, the value at $p$ of the circuit's polynomial. A program computes, from the parameters, the coordinates of $p$, the oracle's readable answer and the gates of such a circuit with the PCP's numbers of inputs and gates, whether the readable values the answer decodes to pass the formula check and the six assignment checks at $p$.

## Depends on

- [Field equations as constraints, and field arithmetic, as programs](lem-ar-field-cons.md)
- [Effective circuit polynomial evaluation](../../structure-of-the-proof/part-07/lem-pcp-circuit-evaluator.md)
- [The slots of a PCP](../part-06/def-ar-slots.md)
- [The parameter routine of the answer-reduced verifier](../part-07/def-ar-routine.md)

## Proof

The circuit evaluator computes the circuit's polynomial on the Shoup bits of the coordinates (Lemma [Effective circuit polynomial evaluation](../../structure-of-the-proof/part-07/lem-pcp-circuit-evaluator.md)). Each readable check compares two field expressions in the point's coordinates and the readable values at the slots' positions, and these are computed with the combinators of Lemma [Field equations as constraints, and field arithmetic, as programs](lem-ar-field-cons.md).

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.circValF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.circValF), [`MIPRE.Tailored.AnsRed.Typed.circValF_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.circValF_eq), [`MIPRE.Tailored.AnsRed.Typed.PrfIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.PrfIn), [`MIPRE.Tailored.AnsRed.Typed.formF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.formF), [`MIPRE.Tailored.AnsRed.Typed.formF_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.formF_eq), [`MIPRE.Tailored.AnsRed.Typed.guardF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.guardF), [`MIPRE.Tailored.AnsRed.Typed.guardF_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.guardF_eq).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3757](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3757)
