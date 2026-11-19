---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.vars_toMv_subset, MIPRE.Tailored.AnsRed.Typed.get_ocs, MIPRE.Tailored.AnsRed.Typed.good_vars, MIPRE.Tailored.AnsRed.Typed.length_decStr_le, MIPRE.Tailored.AnsRed.Typed.card_filter_comp_castLE, MIPRE.Tailored.AnsRed.Typed.accepts_decO, MIPRE.Tailored.AnsRed.Typed.MAd_iso, MIPRE.Tailored.AnsRed.Typed.MBd_iso, MIPRE.Tailored.AnsRed.Typed.comp_decO, MIPRE.Tailored.AnsRed.Typed.gameCheck_decO, MIPRE.Tailored.AnsRed.Typed.condFail_OO_le, MIPRE.Tailored.AnsRed.Typed.condFail_Or_le, MIPRE.Tailored.AnsRed.Typed.condFail_rO_le, MIPRE.Tailored.AnsRed.Typed.condFail_rr_le, MIPRE.Tailored.AnsRed.Typed.condFail_rr'_le, MIPRE.Tailored.AnsRed.Typed.gcA_le, MIPRE.Tailored.AnsRed.Typed.gcB_le
statement: formalized
proof: formalized
---

# The checks of the decoded strategy

Under the hypotheses of Definition [The honest answers](../part-06/def-ar-honest-answers.md), the input game accepts an oracle's decoded pair whenever its polynomials are block-local and pass densely. So at a seed, the decoded strategy fails each of the nine ordered pairs of roles at most as often as an oracle's outcome is not block-local or does not pass densely, plus the disagreements of the polynomial measurements its two answers are decoded from.

## Depends on

- [The decoded strategy](def-ar-decoded-strategy.md)
- [Indifference, at two points of a line](lem-ar-sound-indifference.md)
- [The proof check, on the polynomials](lem-ar-sound-check.md)
- [The game accepts the decoded answers; cor:functional_viewpoint_final, item 2](../part-06/thm-ar-pcp-accepts.md)
- [The honest answers](../part-06/def-ar-honest-answers.md)

## Proof

Block-local polynomials of individual degree at most $d$ are a PCP of individual degree $d$ whose values at a point are their evaluations, and passing densely on $\mathbb{F}_q^M$ is passing on a set of density more than $m (5 + 6 (d + 1))/q$ in $\mathbb{F}_q^m$, every point of $\mathbb{F}_q^m$ having equally many preimages. Theorem [The game accepts the decoded answers; cor:functional_viewpoint_final, item 2](../part-06/thm-ar-pcp-accepts.md) then makes the input game accept the decodings of the PCP's input polynomials. The decoded measurements are coarse-grainings of projective measurements, so projective, and the decoding of the oracle's polynomials in an isolated role's slots is the oracle's answer in that role.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.vars_toMv_subset`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.vars_toMv_subset), [`MIPRE.Tailored.AnsRed.Typed.get_ocs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.get_ocs), [`MIPRE.Tailored.AnsRed.Typed.good_vars`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.good_vars), [`MIPRE.Tailored.AnsRed.Typed.length_decStr_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.length_decStr_le), [`MIPRE.Tailored.AnsRed.Typed.card_filter_comp_castLE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.card_filter_comp_castLE), [`MIPRE.Tailored.AnsRed.Typed.accepts_decO`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.accepts_decO), [`MIPRE.Tailored.AnsRed.Typed.MAd_iso`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.MAd_iso), [`MIPRE.Tailored.AnsRed.Typed.MBd_iso`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.MBd_iso), [`MIPRE.Tailored.AnsRed.Typed.comp_decO`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.comp_decO), [`MIPRE.Tailored.AnsRed.Typed.gameCheck_decO`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.gameCheck_decO), [`MIPRE.Tailored.AnsRed.Typed.condFail_OO_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.condFail_OO_le), [`MIPRE.Tailored.AnsRed.Typed.condFail_Or_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.condFail_Or_le), [`MIPRE.Tailored.AnsRed.Typed.condFail_rO_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.condFail_rO_le), [`MIPRE.Tailored.AnsRed.Typed.condFail_rr_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.condFail_rr_le), [`MIPRE.Tailored.AnsRed.Typed.condFail_rr'_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.condFail_rr'_le), [`MIPRE.Tailored.AnsRed.Typed.gcA_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.gcA_le), [`MIPRE.Tailored.AnsRed.Typed.gcB_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.gcB_le).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3378](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3378)
