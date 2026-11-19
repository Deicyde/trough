---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.exists_cubeZero_division, MIPRE.LowDegree.exists_zero_basis
statement: formalized
proof: formalized
---

# Boolean-cube zero certificates

Let $f$ be a polynomial over a field, of individual degree at most $d$, vanishing on $\{0,1\}^m$. There are polynomials $c_i$, each of individual degree at most $d$, such that the polynomial identity $f=\sum_i c_i X_i(1-X_i)$ holds. Division in a single coordinate can be performed without increasing the degree in any coordinate, leaving degree at most one in the selected coordinate.

## Depends on

- [The low-degree code](def-ld-encoding.md)

## Proof

Repeatedly replace the part divisible by $X_i^2$ with the corresponding multiple of $X_i$. This decreases the degree in coordinate $i$ while preserving all other coordinate bounds. Eliminate each coordinate in turn. The remaining multilinear polynomial vanishes on the Boolean cube and is therefore zero. The general Nullstellensatz total-degree bound alone does not give the individual-degree bounds required here.

## Lean

Formalized as [`MIPRE.LowDegree.exists_cubeZero_division`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.exists_cubeZero_division), [`MIPRE.LowDegree.exists_zero_basis`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.exists_zero_basis).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 5011](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5011)
