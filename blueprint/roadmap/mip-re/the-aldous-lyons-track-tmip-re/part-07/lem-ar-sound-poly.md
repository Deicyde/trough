---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.sum_uniform_tuple_eq_le, MIPRE.Tailored.AnsRed.Typed.sum_uniform_evalR_eq_le, MIPRE.Tailored.AnsRed.Typed.dis_le_avg_evalR_add, MIPRE.Tailored.AnsRed.Typed.errP, MIPRE.Tailored.AnsRed.Typed.sum_dis_le_of_evalR, MIPRE.Tailored.AnsRed.Typed.sum_dis_GAr_GBO_poly_le, MIPRE.Tailored.AnsRed.Typed.sum_dis_GAO_GBr_poly_le
statement: formalized
proof: formalized
---

# The polynomials of the roles agree

Two measurements of tuples of polynomials of individual degree at most $d$ in $M$ variables disagree at most as often as their evaluations at a uniform point do, plus $M d / q$. So for an isolated role $r$, $\sum_z \mathrm{dis}(G^\textsc{A}_r, \mathrm{res}_r G^\textsc{B}_\textsc{O}) \leq |Z|\, e_r(\theta)$, and the same with the players exchanged, where $e_r(\theta) = 11 (\delta_r(9\theta) + 81\theta + \delta_\textsc{O}(9\theta)) + M d / q$.

## Depends on

- [The point relations](lem-ar-sound-relations.md)
- [Extracting exactly linear combined codewords](../../background-results/part-01/lem-lidt-ldc-extraction.md)

## Proof depends on

- [Separating the two point variables](../../background-results/part-03/lem-qld-global-separate.md)

## Proof

Two distinct tuples agree at a uniform point with probability at most $M d / q$, by Schwartz–Zippel (Lemma [Extracting exactly linear combined codewords](../../background-results/part-01/lem-lidt-ldc-extraction.md)), and the registers of a uniform vector carry a uniform point. Lemma [The point relations](lem-ar-sound-relations.md) concludes. Every polynomial of the game lives on the same $M$ variables, an isolated role's codewords being the oracle's in the role's slots, so no lifting between sets of variables is needed.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.sum_uniform_tuple_eq_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_uniform_tuple_eq_le), [`MIPRE.Tailored.AnsRed.Typed.sum_uniform_evalR_eq_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_uniform_evalR_eq_le), [`MIPRE.Tailored.AnsRed.Typed.dis_le_avg_evalR_add`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.dis_le_avg_evalR_add), [`MIPRE.Tailored.AnsRed.Typed.errP`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.errP), [`MIPRE.Tailored.AnsRed.Typed.sum_dis_le_of_evalR`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_dis_le_of_evalR), [`MIPRE.Tailored.AnsRed.Typed.sum_dis_GAr_GBO_poly_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_dis_GAr_GBO_poly_le), [`MIPRE.Tailored.AnsRed.Typed.sum_dis_GAO_GBr_poly_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_dis_GAO_GBr_poly_le).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3250](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3250)
