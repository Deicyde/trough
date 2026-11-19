---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.sgn_eq_bitSign, MIPRE.Tailored.wX_eq_signedPermMatrix, MIPRE.Tailored.isSignedPerm_wX, MIPRE.Tailored.wZ_eq_diagonal_bitSign, MIPRE.Tailored.isSignedPerm_wZ, MIPRE.Tailored.isDiag_wZ, MIPRE.Tailored.trDotDual, MIPRE.Tailored.exists_trDotL_eq, MIPRE.Tailored.encObs_proj_trDot, MIPRE.Tailored.exists_encObs_proj_linear, MIPRE.Tailored.isSignedPerm_encObs_xProj, MIPRE.Tailored.isSignedPerm_encObs_zProj
statement: formalized
proof: formalized
---

# Weyl measurements are read out by signed permutations; II:2938

$X(a)$ is the permutation matrix of the translation by $a$, and $Z(b)$ the diagonal of the signs $(-1)^{\operatorname{tr}(b \cdot e)}$. Every $\mathbb{F}_2$-linear functional on $\mathbb{F}_q^n$ is $e \mapsto \operatorname{tr}(c \cdot e)$ for some $c$, and the observable of an $\mathbb{F}_2$-linear bit $\varphi$ of the outcome of the eigenbasis measurement of $X$ (of $Z$) is $X(c)$ ($Z(c)$) for the $c$ representing $\varphi$. So every $\mathbb{F}_2$-linear encoding of the outcome of the $X$-basis measurement has signed-permutation bit observables, and every encoding whatsoever of the outcome of the $Z$-basis measurement has diagonal $\pm 1$ bit observables.

## Depends on

- [Generalized Pauli observables in characteristic two](../../foundations/part-02/def-generalized-pauli.md)
- [Signed permutation matrices](../part-01/lem-signed-perm.md)
- [The bit observables of an encoded measurement](lem-encoded-pvm-obs.md)

## Proof

The first two claims are the definitions. The trace form is nondegenerate (a nonzero $c$ gives a nonzero functional, since the trace is onto), so $c \mapsto \operatorname{tr}(c \cdot -)$ is an injective linear map between spaces of equal finite dimension over $\mathbb{F}_2$, hence onto. The observable of the bit $\operatorname{tr}(c \cdot -)$ is $\sum_e (-1)^{\operatorname{tr}(c \cdot e)} P_e = W(c)$, the expansion of a Weyl operator in its eigenbasis projectors. The $Z$-basis projectors are the diagonal matrix units, so any $\pm 1$ combination of them is a $\pm 1$ diagonal.

## Lean

Formalized as [`MIPRE.Tailored.sgn_eq_bitSign`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.sgn_eq_bitSign), [`MIPRE.Tailored.wX_eq_signedPermMatrix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.wX_eq_signedPermMatrix), [`MIPRE.Tailored.isSignedPerm_wX`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isSignedPerm_wX), [`MIPRE.Tailored.wZ_eq_diagonal_bitSign`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.wZ_eq_diagonal_bitSign), [`MIPRE.Tailored.isSignedPerm_wZ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isSignedPerm_wZ), [`MIPRE.Tailored.isDiag_wZ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isDiag_wZ), [`MIPRE.Tailored.trDotDual`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.trDotDual), [`MIPRE.Tailored.exists_trDotL_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.exists_trDotL_eq), [`MIPRE.Tailored.encObs_proj_trDot`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.encObs_proj_trDot), [`MIPRE.Tailored.exists_encObs_proj_linear`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.exists_encObs_proj_linear), [`MIPRE.Tailored.isSignedPerm_encObs_xProj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isSignedPerm_encObs_xProj), [`MIPRE.Tailored.isSignedPerm_encObs_zProj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isSignedPerm_encObs_zProj).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1375](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1375)
