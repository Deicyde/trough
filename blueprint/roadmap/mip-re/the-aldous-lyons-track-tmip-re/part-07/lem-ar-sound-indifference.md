---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.sum_ite_ne_le_dis_add, MIPRE.Tailored.AnsRed.Typed.sum_ite_read_le, MIPRE.Tailored.AnsRed.Typed.sum_ite_read_le', MIPRE.Tailored.AnsRed.Typed.sum_swap_ite, MIPRE.Tailored.AnsRed.Typed.dirIdx, MIPRE.Tailored.AnsRed.Typed.shiftW, MIPRE.Tailored.AnsRed.Typed.shiftEquiv, MIPRE.Tailored.AnsRed.Typed.ldq_aline_shiftW, MIPRE.Tailored.AnsRed.Typed.maskI, MIPRE.Tailored.AnsRed.Typed.kv, MIPRE.Tailored.AnsRed.Typed.kv_eq_pv_of_arDt, MIPRE.Tailored.AnsRed.Typed.pv_eq_kv_of_arDt, MIPRE.Tailored.AnsRed.Typed.Good, MIPRE.Tailored.AnsRed.Typed.card_differ_ge, MIPRE.Tailored.AnsRed.Typed.card_steps_ge, MIPRE.Tailored.AnsRed.Typed.sum_differ_le, MIPRE.Tailored.AnsRed.Typed.badGood_le, MIPRE.Tailored.AnsRed.Typed.sum_badGood_le
statement: formalized
proof: formalized
---

# Indifference, at two points of a line

An outcome of the oracle's polynomial measurement is *block-local* if each codeword's polynomial involves only the variables of its slot's block. If $q \geq 2 (M + 1) d$, the outcomes of $G^\textsc{A}_{\textsc{O}}$ that are not block-local weigh, summed over the seeds, at most $2M |Z| (12\, \delta_\textsc{O}(9\theta) + 1782\, \theta)$.

## Depends on

- [The point relations](lem-ar-sound-relations.md)
- [Shifting a polynomial along an axis](lem-ar-sound-shift.md)
- [The per-role failures](../part-06/lem-ar-sound-roles.md)
- [The slots of a PCP](../part-06/def-ar-slots.md)

## Proof

The test's question of type $\mathrm{ALine}$ that the registers of a vector carry is the same at every point of its line: moving the vector's point along the line's direction keeps it. At the pair of types $(\textsc{O}, \mathrm{ALine}), (\textsc{O}, \mathrm{Point})$, the low-degree check and the indifference check make the point values, in the codewords whose blocks miss the line's direction, the constant coefficients of the line answer's polynomials. So Bob's point values at two points $u$ and $u + s e_i$ of one line agree, through the line answer, in those codewords, and so do Alice's polynomials evaluated at $u$ and at $u + s e_i$, up to the disagreements of Lemma [The point relations](lem-ar-sound-relations.md) and the failures at that pair of types. A polynomial with a monomial in a variable outside its block changes value along at least half of the steps in that direction (Lemma [Shifting a polynomial along an axis](lem-ar-sound-shift.md), as $q \geq 2 (M + 1) d$), and a uniform line has that direction with probability $1/M$.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.sum_ite_ne_le_dis_add`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_ite_ne_le_dis_add), [`MIPRE.Tailored.AnsRed.Typed.sum_ite_read_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_ite_read_le), [`MIPRE.Tailored.AnsRed.Typed.sum_ite_read_le'`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_ite_read_le'), [`MIPRE.Tailored.AnsRed.Typed.sum_swap_ite`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_swap_ite), [`MIPRE.Tailored.AnsRed.Typed.dirIdx`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.dirIdx), [`MIPRE.Tailored.AnsRed.Typed.shiftW`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.shiftW), [`MIPRE.Tailored.AnsRed.Typed.shiftEquiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.shiftEquiv), [`MIPRE.Tailored.AnsRed.Typed.ldq_aline_shiftW`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldq_aline_shiftW), [`MIPRE.Tailored.AnsRed.Typed.maskI`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.maskI), [`MIPRE.Tailored.AnsRed.Typed.kv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.kv), [`MIPRE.Tailored.AnsRed.Typed.kv_eq_pv_of_arDt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.kv_eq_pv_of_arDt), [`MIPRE.Tailored.AnsRed.Typed.pv_eq_kv_of_arDt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.pv_eq_kv_of_arDt), [`MIPRE.Tailored.AnsRed.Typed.Good`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.Good), [`MIPRE.Tailored.AnsRed.Typed.card_differ_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.card_differ_ge), [`MIPRE.Tailored.AnsRed.Typed.card_steps_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.card_steps_ge), [`MIPRE.Tailored.AnsRed.Typed.sum_differ_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_differ_le), [`MIPRE.Tailored.AnsRed.Typed.badGood_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.badGood_le), [`MIPRE.Tailored.AnsRed.Typed.sum_badGood_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_badGood_le).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3300](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3300)
