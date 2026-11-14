---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.exists_extR, MIPRE.Tailored.AnsRed.Typed.extR_proj, MIPRE.Tailored.AnsRed.Typed.extR_spec, MIPRE.Tailored.AnsRed.Typed.sum_deltaSimR_le
statement: formalized
proof: formalized
---

# The polynomial measurements

Let $\varepsilon_{r,y}$ be the failure of the per-role strategy at $(r, y)$. The evaluations of $G^\textsc{B}_{r,y}$ at a uniform point are inconsistent with Alice's point answers of the per-role strategy, those of $G^\textsc{A}_{r,y}$ with Bob's, and $G^\textsc{A}_{r,y}$ with $G^\textsc{B}_{r,y}$, each at most $\delta_r(\varepsilon_{r,y})$; and $\sum_{z} \delta_r(\varepsilon_{r, y_r(z)}) \leq |Z|\, \delta_r(9 \theta)$.

## Depends on

- [The polynomial measurements](def-ar-sound-extract.md)
- [The per-role failures](../part-06/lem-ar-sound-roles.md)
- [Common individual polynomial measurements](../../structure-of-the-proof/part-08/lem-ar-common-polynomials.md)

## Proof

The first part is the test's soundness in the model. The second is Jensen's inequality for the concave error (Lemma [Common individual polynomial measurements](../../structure-of-the-proof/part-08/lem-ar-common-polynomials.md)), with Lemma [The per-role failures](../part-06/lem-ar-sound-roles.md).

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.exists_extR`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.exists_extR), [`MIPRE.Tailored.AnsRed.Typed.extR_proj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.extR_proj), [`MIPRE.Tailored.AnsRed.Typed.extR_spec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.extR_spec), [`MIPRE.Tailored.AnsRed.Typed.sum_deltaSimR_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_deltaSimR_le).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3189](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3189)
