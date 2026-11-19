---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.isPVMIn_fourierFactor, MIPRE.Tailored.isPVMIn_fourierProj, MIPRE.Tailored.mul_fourierProj, MIPRE.Tailored.obsChar_mul_fourierProj, MIPRE.Tailored.pvmObs_fourierProj_bit, MIPRE.Tailored.pvmObs_fourierProj_dotBit, MIPRE.Tailored.isDiag_fourierProj
statement: formalized
proof: formalized
---

# The Fourier transform; II:974–1006

Let $U_1, \dots, U_k$ be commuting self-adjoint involutions. Then $(P_a)_{a \in \mathbb{F}_2^k}$ is a projective measurement. $P_a$ lies in the $(-1)^{\langle \alpha, a\rangle}$-eigenspace of $U^\alpha$, so that $U^\alpha = \sum_a (-1)^{\langle \alpha, a\rangle} P_a$, and in particular $U_i = \sum_a (-1)^{a_i} P_a$. An element commuting with every $U_i$ commutes with every $P_a$, and diagonal observables have diagonal projections.

## Depends on

- [The three forms of a measurement with outcomes in $\mathbb{F}_2^k$; II:972–1006](def-fourier-forms.md)

## Proof

For one involution, $\frac12({I} \pm U)$ are complementary projections. If every element of one projective measurement commutes with every element of another, their products form a projective measurement on the product of the outcome sets; the Fourier transform of $k + 1$ observables is the product of that of the first and that of the other $k$, reindexed, which proves the first claim by induction on $k$. $U_i$ commutes with the factors of $P_a$ other than the $i$-th, on which it acts as $(-1)^{a_i}$; multiplying over the $i$ with $\alpha_i = 1$ gives the eigenvalue relation, and summing it over $a$ the inverse transform. A product of diagonal matrices is diagonal.

## Lean

Formalized as [`MIPRE.Tailored.isPVMIn_fourierFactor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isPVMIn_fourierFactor), [`MIPRE.Tailored.isPVMIn_fourierProj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isPVMIn_fourierProj), [`MIPRE.Tailored.mul_fourierProj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.mul_fourierProj), [`MIPRE.Tailored.obsChar_mul_fourierProj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.obsChar_mul_fourierProj), [`MIPRE.Tailored.pvmObs_fourierProj_bit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.pvmObs_fourierProj_bit), [`MIPRE.Tailored.pvmObs_fourierProj_dotBit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.pvmObs_fourierProj_dotBit), [`MIPRE.Tailored.isDiag_fourierProj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isDiag_fourierProj).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 185](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L185)
