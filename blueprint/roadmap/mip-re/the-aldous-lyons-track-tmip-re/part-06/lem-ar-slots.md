---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.passes_iff_passesV, MIPRE.Tailored.AnsRed.passesV_iff, MIPRE.Tailored.AnsRed.passesR_congr, MIPRE.Tailored.AnsRed.rename_ofPolys_slot, MIPRE.Tailored.AnsRed.slotEval_ofPolys, MIPRE.Tailored.AnsRed.indDeg_ofPolys, MIPRE.Tailored.AnsRed.idxO_lt_of_readable, MIPRE.Tailored.AnsRed.readable_getElem_slotsOf
statement: formalized
proof: formalized
---

# Slot values and block-local polynomials

The checks of a PCP at a point hold exactly when the checks on its slot values there do, which are the readable checks and the linear checks; the readable checks read only readable values. If each of a family of polynomials on $N$ variables depends only on the image of its slot's block, then the slots of the PCP of the polynomials, renamed back, are the polynomials: its values are theirs, and its degree is at most theirs. A readable slot sits among the oracle's readable codewords.

## Depends on

- [The slots of a PCP](def-ar-slots.md)

## Proof

The checks on slot values are the checks of the PCP with each evaluation replaced by the value of its slot. A polynomial whose variables lie in the range of an injection is the renaming of one on its domain, which the left inverse of renaming recovers; renaming along an injection keeps the individual degrees.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.passes_iff_passesV`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.passes_iff_passesV), [`MIPRE.Tailored.AnsRed.passesV_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.passesV_iff), [`MIPRE.Tailored.AnsRed.passesR_congr`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.passesR_congr), [`MIPRE.Tailored.AnsRed.rename_ofPolys_slot`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.rename_ofPolys_slot), [`MIPRE.Tailored.AnsRed.slotEval_ofPolys`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.slotEval_ofPolys), [`MIPRE.Tailored.AnsRed.indDeg_ofPolys`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.indDeg_ofPolys), [`MIPRE.Tailored.AnsRed.idxO_lt_of_readable`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.idxO_lt_of_readable), [`MIPRE.Tailored.AnsRed.readable_getElem_slotsOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.readable_getElem_slotsOf).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2845](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2845)
