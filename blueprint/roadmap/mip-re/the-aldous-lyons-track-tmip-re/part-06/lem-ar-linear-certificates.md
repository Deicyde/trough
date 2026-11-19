---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.cubeVanishing, MIPRE.LowDegree.mem_cubeVanishing, MIPRE.LowDegree.cert, MIPRE.LowDegree.degreeOf_cert_le, MIPRE.LowDegree.cert_sum
statement: formalized
proof: formalized
---

# Linear certificates for vanishing on the cube

For every $m$ and $d$ there is a linear map $f \mapsto (c_i(f))_i$ from polynomials in $m$ variables over a field to $m$-tuples of polynomials of individual degree at most $d$ such that $f = \sum_i c_i(f) X_i (1 - X_i)$ whenever $f$ has individual degree at most $d$ and vanishes on $\{0, 1\}^m$.

## Depends on

- [Boolean-cube zero certificates](../../structure-of-the-proof/part-07/lem-pcp-zero-basis.md)

## Proof

The map $c \mapsto \sum_i c_i X_i (1 - X_i)$, restricted to the tuples whose image vanishes on the cube, maps onto the polynomials of individual degree at most $d$ vanishing on the cube, by Lemma [Boolean-cube zero certificates](../../structure-of-the-proof/part-07/lem-pcp-zero-basis.md). Compose a linear right inverse of it with a linear projection onto that subspace.

## Lean

Formalized as [`MIPRE.LowDegree.cubeVanishing`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.cubeVanishing), [`MIPRE.LowDegree.mem_cubeVanishing`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.mem_cubeVanishing), [`MIPRE.LowDegree.cert`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.cert), [`MIPRE.LowDegree.degreeOf_cert_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.degreeOf_cert_le), [`MIPRE.LowDegree.cert_sum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.cert_sum).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2702](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2702)
