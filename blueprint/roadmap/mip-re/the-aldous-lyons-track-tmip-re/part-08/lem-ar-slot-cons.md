---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Slot.lo, MIPRE.Tailored.AnsRed.Slot.val_emb, MIPRE.Tailored.AnsRed.Slot.exists_emb_iff, MIPRE.Tailored.AnsRed.slotsOf_alice, MIPRE.Tailored.AnsRed.slotsOf_bob, MIPRE.Tailored.AnsRed.Typed.copyF, MIPRE.Tailored.AnsRed.Typed.copyF_eq, MIPRE.Tailored.AnsRed.Typed.consConsF, MIPRE.Tailored.AnsRed.Typed.consConsF_eq, MIPRE.Tailored.AnsRed.Typed.indF, MIPRE.Tailored.AnsRed.Typed.indF_eq, MIPRE.Tailored.AnsRed.Typed.ivsOf, MIPRE.Tailored.AnsRed.Typed.ivF, MIPRE.Tailored.AnsRed.Typed.ivF_eq, MIPRE.Tailored.AnsRed.Typed.indConsF, MIPRE.Tailored.AnsRed.Typed.indConsF_eq
statement: formalized
proof: formalized
---

# The consistency and indifference checks, as programs

Programs compute, from the parameters and the layout of the answers, the constraints of the consistency checks, that the isolated player's two codewords are the oracle's codewords in the same slots; and those of the indifference checks at an axis-parallel line, that the coefficients $1, \ldots, d$ of the codewords whose blocks miss the direction the seed selects vanish.

## Depends on

- [The low-degree checks, as programs](lem-ar-ld-cons.md)
- [The slots of a PCP](../part-06/def-ar-slots.md)
- [The answer-reduced game as typed tailored data; defn:combi_ans_red](../part-06/def-ar-tailored-game.md)
- [The parameter routine of the answer-reduced verifier](../part-07/def-ar-routine.md)

## Proof

The positions of an isolated player's slots in the oracle's answer are their indices in the oracle's list of slots, computed from the parameters. The blocks of the slots are intervals of wires, read off a table computed from the parameters. Lemma [Field equations as constraints, and field arithmetic, as programs](lem-ar-field-cons.md) turns the equations' values into the constraints.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Slot.lo`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Slot.lo), [`MIPRE.Tailored.AnsRed.Slot.val_emb`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Slot.val_emb), [`MIPRE.Tailored.AnsRed.Slot.exists_emb_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Slot.exists_emb_iff), [`MIPRE.Tailored.AnsRed.slotsOf_alice`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.slotsOf_alice), [`MIPRE.Tailored.AnsRed.slotsOf_bob`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.slotsOf_bob), [`MIPRE.Tailored.AnsRed.Typed.copyF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.copyF), [`MIPRE.Tailored.AnsRed.Typed.copyF_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.copyF_eq), [`MIPRE.Tailored.AnsRed.Typed.consConsF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.consConsF), [`MIPRE.Tailored.AnsRed.Typed.consConsF_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.consConsF_eq), [`MIPRE.Tailored.AnsRed.Typed.indF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.indF), [`MIPRE.Tailored.AnsRed.Typed.indF_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.indF_eq), [`MIPRE.Tailored.AnsRed.Typed.ivsOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ivsOf), [`MIPRE.Tailored.AnsRed.Typed.ivF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ivF), [`MIPRE.Tailored.AnsRed.Typed.ivF_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ivF_eq), [`MIPRE.Tailored.AnsRed.Typed.indConsF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.indConsF), [`MIPRE.Tailored.AnsRed.Typed.indConsF_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.indConsF_eq).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3731](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3731)
