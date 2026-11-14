---
declaration: lemma
origin: cited
lean: MIPRE.ValueApprox.IsPVM, MIPRE.ValueApprox.IsPVM.exists_unitary_pattern, MIPRE.ValueApprox.cayley, MIPRE.ValueApprox.cayley_mem_unitaryGroup, MIPRE.ValueApprox.exists_isSkewHermitian_cayley_eq, MIPRE.ValueApprox.exists_norm_eq_one_isUnit_one_add_smul, MIPRE.ValueApprox.norm_cayley_sub_cayley_le, MIPRE.ValueApprox.GaussianRat, MIPRE.ValueApprox.exists_unitary_entriesIn_norm_smul_sub_le, MIPRE.ValueApprox.IsPVM.exists_entriesIn_norm_sub_le
statement: formalized
proof: formalized
---

# Gaussian-rational projective measurements are dense

Let $\{M_a\}_{a \in \mathcal{A}}$ be a projective measurement on $\mathbb{C}^d$ and $\eta > 0$. There is a projective measurement $\{M'_a\}_{a \in \mathcal{A}}$ on $\mathbb{C}^d$ with all entries in $\mathbb{Q}(i)$ such that $\left\| {M_a - M'_a} \right\| \leq \eta$ for every $a$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Diagonalize a Hermitian combination $\sum_a w_a M_a$ with distinct real weights $w_a$: $M_a = U \Pi_a U^*$ for a unitary $U$ and the coordinate projections $\Pi_a$ of a pattern $r : [d] \to \mathcal{A}$. For a unit scalar $z$, $(zU) \Pi_a (zU)^* = U \Pi_a U^*$, and $\det({I} + zU)$ is a polynomial in $z$ with constant term $1$, so some unit $z$ makes ${I} + zU$ invertible; then $zU = ({I} - S)({I} + S)^{-1}$ is the Cayley transform of the skew-Hermitian matrix $S = 2({I} + zU)^{-1} - {I}$. Round $S$ entrywise to $R$ with entries in $\mathbb{Q}(i)$ and re-symmetrize, $S' = (R - R^*)/2$: $S'$ is skew-Hermitian, has entries in $\mathbb{Q}(i)$, and $\left\vert {S_{ij} - S'_{ij}} \right\vert$ is at most the rounding precision. Its Cayley transform $U' = ({I} - S')({I} + S')^{-1}$ is unitary with entries in $\mathbb{Q}(i)$, and $\left\| {zU - U'} \right\| \leq 2 \left\| {S - S'} \right\|$, since $zU - U' = 2({I} + S)^{-1}(S' - S)({I} + S')^{-1}$ and $\left\| {({I} + S)^{-1}} \right\| \leq 1$ for skew-Hermitian $S$ (the cross term of $\left\| {x + Sx} \right\|^2$ vanishes). Finally $M'_a = U' \Pi_a U'^*$ satisfies $\left\| {M_a - M'_a} \right\| \leq 2 \left\| {zU - U'} \right\|$.

## Lean

Formalized as [`MIPRE.ValueApprox.IsPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.IsPVM), [`MIPRE.ValueApprox.IsPVM.exists_unitary_pattern`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.IsPVM.exists_unitary_pattern), [`MIPRE.ValueApprox.cayley`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.cayley), [`MIPRE.ValueApprox.cayley_mem_unitaryGroup`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.cayley_mem_unitaryGroup), [`MIPRE.ValueApprox.exists_isSkewHermitian_cayley_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.exists_isSkewHermitian_cayley_eq), [`MIPRE.ValueApprox.exists_norm_eq_one_isUnit_one_add_smul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.exists_norm_eq_one_isUnit_one_add_smul), [`MIPRE.ValueApprox.norm_cayley_sub_cayley_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.norm_cayley_sub_cayley_le), [`MIPRE.ValueApprox.GaussianRat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.GaussianRat), [`MIPRE.ValueApprox.exists_unitary_entriesIn_norm_smul_sub_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.exists_unitary_entriesIn_norm_smul_sub_le), [`MIPRE.ValueApprox.IsPVM.exists_entriesIn_norm_sub_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.IsPVM.exists_entriesIn_norm_sub_le).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 7356](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L7356)
