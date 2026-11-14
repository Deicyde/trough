---
declaration: definition
origin: cited
lean: MIPRE.sgn, MIPRE.sgn_add, MIPRE.star_sgn, MIPRE.norm_sgn, MIPRE.sum_sgn, MIPRE.Weyl.two_eq_zero, MIPRE.Weyl.add_self, MIPRE.Weyl.add_eq_zero_iff, MIPRE.Weyl.trDot, MIPRE.Weyl.trDot_comm, MIPRE.Weyl.trDot_add_left, MIPRE.Weyl.trDot_add_right, MIPRE.Weyl.trDotL, MIPRE.Weyl.wX, MIPRE.Weyl.wZ, MIPRE.Weyl.wX_mul_wX, MIPRE.Weyl.wZ_mul_wZ, MIPRE.Weyl.wX_mul_self, MIPRE.Weyl.wZ_mul_self, MIPRE.Weyl.wX_conjTranspose, MIPRE.Weyl.wZ_conjTranspose, MIPRE.Weyl.wX_isUnitary, MIPRE.Weyl.wZ_isUnitary, MIPRE.Weyl.wX_comm, MIPRE.Weyl.wZ_comm, MIPRE.Weyl.wX_mul_wZ, MIPRE.Weyl.wX_mul_wZ_of_ne, MIPRE.Weyl.wX_mul_wZ_of_eq, MIPRE.Weyl.trDotL_ne_zero, MIPRE.Weyl.sum_sgn_trDot, MIPRE.Weyl.sum_sgn_trDot_zero, MIPRE.Weyl.zProj, MIPRE.Weyl.sum_zProj, MIPRE.Weyl.wZ_eq_sum_zProj, MIPRE.Weyl.sum_sgn_smul_wZ, MIPRE.LowDegree.card_filter_ker_mul', MIPRE.Weyl.IsWeylFamily, MIPRE.Weyl.isWeylFamily_wZ, MIPRE.Weyl.isWeylFamily_wX, MIPRE.Weyl.proj, MIPRE.Weyl.proj_wZ, MIPRE.Weyl.proj_mul, MIPRE.Weyl.proj_mul_proj, MIPRE.Weyl.sum_proj, MIPRE.Weyl.eq_sum_proj, MIPRE.Weyl.proj_conjTranspose, MIPRE.Weyl.xProj, MIPRE.Weyl.sum_xProj, MIPRE.Weyl.wX_eq_sum_xProj, MIPRE.Weyl.xProj_mul_xProj, MIPRE.Weyl.xProj_conjTranspose, MIPRE.Weyl.dotF, MIPRE.Weyl.trDot_smul, MIPRE.Weyl.trMulL, MIPRE.Weyl.sum_sgn_linear, MIPRE.Weyl.sum_sgn_trMul, MIPRE.Weyl.syn, MIPRE.Weyl.sum_sgn_smul_line
statement: formalized
---

# Generalized Pauli observables in characteristic two

Let $q = 2^k$ be an admissible field size and let $n$ be a finite index set, so that $\mathbb{F}_q^n$ indexes a basis of $(\mathbb{C}^q)^{\otimes n}$. Write $\operatorname{tr} : \mathbb{F}_q \to \mathbb{F}_2$ for the field trace and, for $a, b \in \mathbb{F}_q^n$,

$$
\langle a, b \rangle \;=\; \operatorname{tr}\Bigl(\sum_{l \in n} a_l b_l\Bigr) \;\in\; \mathbb{F}_2\;.
$$

The *generalized Pauli*, or *Weyl*, *observables* are

$$
\tau^X(a) \;=\; \sum_{i \in \mathbb{F}_q^n} |i + a\rangle\langlei|\;, \qquad
\tau^Z(b) \;=\; \sum_{i \in \mathbb{F}_q^n} (-1)^{\langle b, i \rangle}\, |i\rangle\langlei|\;.
$$

They satisfy, for all $a, a', b, b' \in \mathbb{F}_q^n$:

1. $\tau^W(a) \tau^W(a') = \tau^W(a + a')$, so $\tau^W(0) = {I}$ and each family commutes;
2. $\tau^W(a)^\dagger = \tau^W(a)$ and $\tau^W(a)^2 = {I}$: each is a self-adjoint involution, hence a $\pm 1$-observable and a unitary;
3. (*twisted commutation*) $\tau^X(a)\, \tau^Z(b) = (-1)^{\langle a, b \rangle}\, \tau^Z(b)\, \tau^X(a)$; so the two commute when $\langle a, b\rangle = 0$ and anticommute when it is $1$.

For $W \in \{X, Z\}$ define the *spectral projectors* of the family by Fourier averaging,

$$
\tau^W_e \;=\; \mathop{\mathbb{E}}_{a \in \mathbb{F}_q^n} (-1)^{\langle a, e \rangle}\, \tau^W(a)\;.\qquad\text{(9)}
$$

For $W = Z$ these are the projectors onto the computational basis vectors. They form a projective measurement and invert (9):

$$
\tau^W_e \tau^W_{e'} = \delta_{e, e'}\, \tau^W_e\;, \qquad
\sum_e \tau^W_e = {I}\;, \qquad
\tau^W(a) \;=\; \sum_{e} (-1)^{\langle a, e\rangle}\, \tau^W_e\;.\qquad\text{(10)}
$$

Finally, for $v \in \mathbb{F}_q^n$ and $a \in \mathbb{F}_q$ write $v \cdot e = \sum_l v_l e_l \in \mathbb{F}_q$ for the pairing before the trace, and define the *syndrome projector* $\tau^W_{[\,\cdot\, v = a]} = \sum_{e \,:\, e \cdot v = a} \tau^W_e$. Averaging the family along the line $r \mapsto r v$ recovers it:

$$
\mathop{\mathbb{E}}_{r \in \mathbb{F}_q} (-1)^{\operatorname{tr}(a r)}\, \tau^W(r v) \;=\; \tau^W_{[\,\cdot\, v = a]}\;.\qquad\text{(11)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MIPRE.sgn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sgn), [`MIPRE.sgn_add`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sgn_add), [`MIPRE.star_sgn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.star_sgn), [`MIPRE.norm_sgn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.norm_sgn), [`MIPRE.sum_sgn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_sgn), [`MIPRE.Weyl.two_eq_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.two_eq_zero), [`MIPRE.Weyl.add_self`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.add_self), [`MIPRE.Weyl.add_eq_zero_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.add_eq_zero_iff), [`MIPRE.Weyl.trDot`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.trDot), [`MIPRE.Weyl.trDot_comm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.trDot_comm), [`MIPRE.Weyl.trDot_add_left`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.trDot_add_left), [`MIPRE.Weyl.trDot_add_right`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.trDot_add_right), [`MIPRE.Weyl.trDotL`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.trDotL), [`MIPRE.Weyl.wX`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wX), [`MIPRE.Weyl.wZ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wZ), [`MIPRE.Weyl.wX_mul_wX`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wX_mul_wX), [`MIPRE.Weyl.wZ_mul_wZ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wZ_mul_wZ), [`MIPRE.Weyl.wX_mul_self`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wX_mul_self), [`MIPRE.Weyl.wZ_mul_self`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wZ_mul_self), [`MIPRE.Weyl.wX_conjTranspose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wX_conjTranspose), [`MIPRE.Weyl.wZ_conjTranspose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wZ_conjTranspose), [`MIPRE.Weyl.wX_isUnitary`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wX_isUnitary), [`MIPRE.Weyl.wZ_isUnitary`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wZ_isUnitary), [`MIPRE.Weyl.wX_comm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wX_comm), [`MIPRE.Weyl.wZ_comm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wZ_comm), [`MIPRE.Weyl.wX_mul_wZ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wX_mul_wZ), [`MIPRE.Weyl.wX_mul_wZ_of_ne`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wX_mul_wZ_of_ne), [`MIPRE.Weyl.wX_mul_wZ_of_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wX_mul_wZ_of_eq), [`MIPRE.Weyl.trDotL_ne_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.trDotL_ne_zero), [`MIPRE.Weyl.sum_sgn_trDot`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.sum_sgn_trDot), [`MIPRE.Weyl.sum_sgn_trDot_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.sum_sgn_trDot_zero), [`MIPRE.Weyl.zProj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.zProj), [`MIPRE.Weyl.sum_zProj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.sum_zProj), [`MIPRE.Weyl.wZ_eq_sum_zProj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wZ_eq_sum_zProj), [`MIPRE.Weyl.sum_sgn_smul_wZ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.sum_sgn_smul_wZ), [`MIPRE.LowDegree.card_filter_ker_mul'`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.card_filter_ker_mul'), [`MIPRE.Weyl.IsWeylFamily`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.IsWeylFamily), [`MIPRE.Weyl.isWeylFamily_wZ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.isWeylFamily_wZ), [`MIPRE.Weyl.isWeylFamily_wX`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.isWeylFamily_wX), [`MIPRE.Weyl.proj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.proj), [`MIPRE.Weyl.proj_wZ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.proj_wZ), [`MIPRE.Weyl.proj_mul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.proj_mul), [`MIPRE.Weyl.proj_mul_proj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.proj_mul_proj), [`MIPRE.Weyl.sum_proj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.sum_proj), [`MIPRE.Weyl.eq_sum_proj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.eq_sum_proj), [`MIPRE.Weyl.proj_conjTranspose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.proj_conjTranspose), [`MIPRE.Weyl.xProj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.xProj), [`MIPRE.Weyl.sum_xProj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.sum_xProj), [`MIPRE.Weyl.wX_eq_sum_xProj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wX_eq_sum_xProj), [`MIPRE.Weyl.xProj_mul_xProj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.xProj_mul_xProj), [`MIPRE.Weyl.xProj_conjTranspose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.xProj_conjTranspose), [`MIPRE.Weyl.dotF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.dotF), [`MIPRE.Weyl.trDot_smul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.trDot_smul), [`MIPRE.Weyl.trMulL`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.trMulL), [`MIPRE.Weyl.sum_sgn_linear`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.sum_sgn_linear), [`MIPRE.Weyl.sum_sgn_trMul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.sum_sgn_trMul), [`MIPRE.Weyl.syn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.syn), [`MIPRE.Weyl.sum_sgn_smul_line`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.sum_sgn_smul_line).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 990](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L990)
