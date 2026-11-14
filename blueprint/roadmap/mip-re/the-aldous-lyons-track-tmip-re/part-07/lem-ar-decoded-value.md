---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.errAR, MIPRE.Tailored.AnsRed.Typed.deltaSim_mono, MIPRE.Tailored.AnsRed.Typed.dS_mono, MIPRE.Tailored.AnsRed.Typed.errP_mono, MIPRE.Tailored.AnsRed.Typed.errAR_lt, MIPRE.Tailored.AnsRed.Typed.errAR_nonneg, MIPRE.Tailored.AnsRed.Typed.le_errAR, MIPRE.Tailored.AnsRed.Typed.errAR_pos, MIPRE.Tailored.AnsRed.Typed.sum_roles_condFail_le, MIPRE.Tailored.AnsRed.Typed.one_sub_value_decoded_le
statement: formalized
proof: formalized
---

# The failure of the decoded strategy

If $q \geq 2 (M + 1) d$ and $q \geq 2 m (5 + 6 (d + 1))$, the decoded strategy fails the typed oracularized game of the input with probability at most

$$
e(\theta) = 6 \bigl(2M (12\, \delta_\textsc{O}(9\theta) + 1782\, \theta) + 2\,
\delta_\textsc{O}(9\theta) + 162\, \theta\bigr) + 4\, \delta_\textsc{O}(9\theta) +
\delta_\textsc{A}(9\theta) + \delta_\textsc{B}(9\theta) + 2 e_\textsc{A}(\theta) + 2 e_\textsc{B}(\theta),
$$

which is strictly increasing in $\theta \geq 0$ and at least $\theta$.

## Depends on

- [The checks of the decoded strategy](lem-ar-decoded-accepts.md)
- [The polynomials of the roles agree](lem-ar-sound-poly.md)
- [The polynomial measurements](lem-ar-sound-extract.md)
- [Indifference, at two points of a line](lem-ar-sound-indifference.md)
- [The proof check, on the polynomials](lem-ar-sound-check.md)
- [Full-seed indexing for answer reduction](../../structure-of-the-proof/part-08/def-ar-seed-index.md)

## Proof

The typed oracularized game's failure is the average over the seeds of its failures at the nine pairs of roles (Definition [Full-seed indexing for answer reduction](../../structure-of-the-proof/part-08/def-ar-seed-index.md)). Lemma [The checks of the decoded strategy](lem-ar-decoded-accepts.md) bounds each by the weight of the oracle's outcomes that are not block-local or do not pass densely, which Lemmas [Indifference, at two points of a line](lem-ar-sound-indifference.md) and [The proof check, on the polynomials](lem-ar-sound-check.md) bound, and by disagreements of polynomial measurements, which Lemmas [The polynomial measurements](lem-ar-sound-extract.md) and [The polynomials of the roles agree](lem-ar-sound-poly.md) bound.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.errAR`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.errAR), [`MIPRE.Tailored.AnsRed.Typed.deltaSim_mono`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.deltaSim_mono), [`MIPRE.Tailored.AnsRed.Typed.dS_mono`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.dS_mono), [`MIPRE.Tailored.AnsRed.Typed.errP_mono`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.errP_mono), [`MIPRE.Tailored.AnsRed.Typed.errAR_lt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.errAR_lt), [`MIPRE.Tailored.AnsRed.Typed.errAR_nonneg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.errAR_nonneg), [`MIPRE.Tailored.AnsRed.Typed.le_errAR`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.le_errAR), [`MIPRE.Tailored.AnsRed.Typed.errAR_pos`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.errAR_pos), [`MIPRE.Tailored.AnsRed.Typed.sum_roles_condFail_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_roles_condFail_le), [`MIPRE.Tailored.AnsRed.Typed.one_sub_value_decoded_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.one_sub_value_decoded_le).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3410](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3410)
