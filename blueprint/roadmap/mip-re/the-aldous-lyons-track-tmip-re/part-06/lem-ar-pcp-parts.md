---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.readable_induce, MIPRE.Tailored.AnsRed.linear_induce_add, MIPRE.Tailored.AnsRed.res_encB, MIPRE.Tailored.AnsRed.resZ_encZ
statement: formalized
proof: formalized
---

# The readable and the linear parts of the honest PCP

The readable part of the honest PCP, the readable assignments and their helpers, depends only on the readable tables. Its linear part is $\mathbb{F}_2$-affine in the linear tables: the linear assignments and their helpers are additive, and the helpers of the system check affine. The tables of the encodings on the cube are the encoded tables.

## Depends on

- [The honest PCP; $\mathsf{Induce}_C$](def-ar-induce.md)

## Proof

The encodings are linear, the system polynomial is affine in the linear assignments, and $g \mapsto g(1 - g)$ is additive in characteristic two; the certificates are values of a linear map.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.readable_induce`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.readable_induce), [`MIPRE.Tailored.AnsRed.linear_induce_add`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.linear_induce_add), [`MIPRE.Tailored.AnsRed.res_encB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.res_encB), [`MIPRE.Tailored.AnsRed.resZ_encZ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.resZ_encZ).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2765](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2765)
