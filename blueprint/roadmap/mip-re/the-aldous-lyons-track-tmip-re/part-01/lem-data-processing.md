---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.pvmObs_coarse_affine, MIPRE.Tailored.isDiag_coarse
statement: formalized
proof: formalized
---

# Data processing; Claims II:2902 and II:2918

Coarse-graining the Fourier transform of commuting self-adjoint involutions $U$ along the affine map $a \mapsto c + \langle \alpha, a\rangle$ gives the measurement with outcomes in $\mathbb{F}_2$ whose observable is $(-1)^c U^\alpha$. Coarse-graining a diagonal measurement along any map gives a diagonal measurement.

## Depends on

- [The Fourier transform; II:974–1006](lem-fourier-pvm.md)

## Proof

The observable of the coarse-graining is $\sum_a (-1)^{c + \langle \alpha, a\rangle} P_a = (-1)^c U^\alpha$, by Lemma [The Fourier transform; II:974–1006](lem-fourier-pvm.md). Sums of diagonal matrices are diagonal.

## Lean

Formalized as [`MIPRE.Tailored.pvmObs_coarse_affine`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.pvmObs_coarse_affine), [`MIPRE.Tailored.isDiag_coarse`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isDiag_coarse).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 212](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L212)
