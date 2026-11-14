---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.ocs, MIPRE.Tailored.AnsRed.Typed.PassV, MIPRE.Tailored.AnsRed.Typed.Dense, MIPRE.Tailored.AnsRed.Typed.passV_of_arDt, MIPRE.Tailored.AnsRed.Typed.sum_notPass_le, MIPRE.Tailored.AnsRed.Typed.badDense_le, MIPRE.Tailored.AnsRed.Typed.sum_badDense_le
statement: formalized
proof: formalized
---

# The proof check, on the polynomials

An outcome of the oracle's polynomial measurement at a seed *passes densely* if its evaluations pass the thirteen checks of the seed's circuit on more than a fraction $m (5 + 6 (d + 1)) / q$ of the points of $\mathbb{F}_q^M$. If $q \geq 2 m (5 + 6 (d + 1))$, the outcomes of $G^\textsc{A}_\textsc{O}$ that do not pass densely weigh, summed over the seeds, at most $|Z| (2\, \delta_\textsc{O}(9\theta) + 162\, \theta)$.

## Depends on

- [The point relations](lem-ar-sound-relations.md)
- [The per-role failures](../part-06/lem-ar-sound-roles.md)
- [The slots of a PCP](../part-06/def-ar-slots.md)
- [Reading the answer-reduced constraints](../part-06/lem-ar-tailored-reading.md)

## Proof depends on

- [Indifference, at two points of a line](lem-ar-sound-indifference.md)

## Proof

The typed data checks Bob's point answer at the oracle's point question against the seed's circuit. An outcome's evaluations at a point pass whenever Bob's point answer passes and agrees with them, so an outcome that does not pass densely meets, with probability at least one half, a point where Bob's answer fails or disagrees with it; the event moves between the two players' measurements at the cost of their disagreement, as in Lemma [Indifference, at two points of a line](lem-ar-sound-indifference.md). Those points weigh at most the extraction's error at the oracle and the failure at the pair of types $(\textsc{O}, \mathrm{Point}), (\textsc{O}, \mathrm{Point})$.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.ocs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ocs), [`MIPRE.Tailored.AnsRed.Typed.PassV`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.PassV), [`MIPRE.Tailored.AnsRed.Typed.Dense`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.Dense), [`MIPRE.Tailored.AnsRed.Typed.passV_of_arDt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.passV_of_arDt), [`MIPRE.Tailored.AnsRed.Typed.sum_notPass_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_notPass_le), [`MIPRE.Tailored.AnsRed.Typed.badDense_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.badDense_le), [`MIPRE.Tailored.AnsRed.Typed.sum_badDense_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_badDense_le).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3335](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3335)
