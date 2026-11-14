---
declaration: definition
origin: cited
lean: MIPRE.LowDegree.lineRestrict, MIPRE.LowDegree.lineRestrict_zero, MIPRE.LowDegree.eval_lineRestrict, MIPRE.LowDegree.natDegree_lineRestrict_le, MIPRE.LowDegree.sum_coeff_lineRestrict
statement: formalized
---

# Restriction to a line

For $p \in \mathbb{F}_q[x_1, \ldots, x_m]$ and a line $t \mapsto u_0 + t w$, the *restriction of $p$ to the line* is the univariate polynomial $p|_\ell(t) = p(u_0 + t w)$, obtained by substituting the affine parametrization into $p$. Its degree is at most the total degree of $p$, and its coefficients, read at any degree bound $n$ that the degree does not exceed, evaluate back to $p(u_0 + t w)$. So the low-degree encoding $g_h$, being multilinear, restricts to a polynomial of degree at most $m$ on any line, which fits the degree-$md$ answer format of Definition [Seeded CL low individual degree test](../../background-results/part-01/def-lidt-cl.md) whenever $d \geq 1$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MIPRE.LowDegree.lineRestrict`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.lineRestrict), [`MIPRE.LowDegree.lineRestrict_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.lineRestrict_zero), [`MIPRE.LowDegree.eval_lineRestrict`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.eval_lineRestrict), [`MIPRE.LowDegree.natDegree_lineRestrict_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.natDegree_lineRestrict_le), [`MIPRE.LowDegree.sum_coeff_lineRestrict`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.sum_coeff_lineRestrict).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4717](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4717)
