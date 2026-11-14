---
declaration: lemma
origin: cited
lean: MIPRE.Weyl.binEquiv, MIPRE.Weyl.binEquiv_apply, MIPRE.Weyl.binEquiv_add, MIPRE.Weyl.binEquiv_injective, MIPRE.Weyl.binEquiv_eq_iff, MIPRE.Weyl.trDot_binEquiv, MIPRE.Weyl.wX_binEquiv, MIPRE.Weyl.wZ_binEquiv, MIPRE.Weyl.card_binEquiv, MIPRE.Weyl.proj_binEquiv, MIPRE.Weyl.proj_wZ_binEquiv, MIPRE.Weyl.proj_wX_binEquiv, MIPRE.Weyl.eprScale_binEquiv, MIPRE.Weyl.epr_binEquiv, MIPRE.Weyl.pauli_binary, MIPRE.Weyl.exists_binEquiv_pauli_binary, MIPRE.Weyl.trDot_two, MIPRE.Weyl.sgn_trDot_two, MIPRE.Weyl.wZ_two_diag, MIPRE.Weyl.wX_two_apply
statement: formalized
proof: formalized
---

# Qudits are qubits, in characteristic two

Let $q = 2^k$ be an admissible field size, let $L$ be a finite index set, and let $\{e_1, \ldots, e_k\}$ be a self-dual basis of $\mathbb{F}_q$ over $\mathbb{F}_2$, with coordinate map $\kappa$. Then the relabelling

$$
\phi : \mathbb{F}_q^L \to \mathbb{F}_2^{L \times k}\;, \qquad \phi(u)_{i j} \;=\; \kappa(u_i)_j\;,
$$

is a bijection, and conjugating by it carries the whole Weyl system over $\mathbb{F}_q$ on $L$ registers to the Weyl system over $\mathbb{F}_2$ on $L k$ registers: the form $\langle \cdot, \cdot \rangle$, the two operator families $\tau^X$ and $\tau^Z$, their spectral projectors, and $|\textsc{EPR}_q\rangle^{\otimes L} \mapsto |\textsc{EPR}_2\rangle^{\otimes L k}$. Such a basis exists whenever $k$ is odd.

## Depends on

- [Generalized Pauli observables in characteristic two](def-generalized-pauli.md)
- [The maximally entangled state of the Weyl system](def-weyl-epr.md)

## Proof depends on

- [Existence of a self-dual normal basis](../../background-results/part-04/lem-self-dual-basis-exists.md)
- [Self-dual coordinates are trace pairings](../../background-results/part-04/lem-downsize-field.md)

## Proof

Four steps, one per piece, and only the first uses self-duality. The form transports because $\operatorname{tr}(x y) = \kappa(x) \cdot \kappa(y)$, which is item 2 of the paper's `lem:downsize_field` and is exactly self-duality (`MIPRE.LowDegree.trace_mul_eq_dot`); summing over the $L$ registers is `trDot_binEquiv`. $\tau^Z$ transports because its entries are the characters of the form, so it transports as soon as the form does. $\tau^X$ transports because $\phi$ is *additive*, which is all a shift knows about — no self-duality. The projectors transport because the Fourier average of [(9)](def-generalized-pauli.md) reindexes along $\phi$ and the normalization is one cardinality counted on either side. The state transports because both sides are the normalized diagonal and a relabelling preserves the diagonal. Existence of the basis is the existence half of Lemma [Deterministic self-dual normal basis](../../background-results/part-04/lem-self-dual-basis.md).

## Lean

Formalized as [`MIPRE.Weyl.binEquiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.binEquiv), [`MIPRE.Weyl.binEquiv_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.binEquiv_apply), [`MIPRE.Weyl.binEquiv_add`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.binEquiv_add), [`MIPRE.Weyl.binEquiv_injective`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.binEquiv_injective), [`MIPRE.Weyl.binEquiv_eq_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.binEquiv_eq_iff), [`MIPRE.Weyl.trDot_binEquiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.trDot_binEquiv), [`MIPRE.Weyl.wX_binEquiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wX_binEquiv), [`MIPRE.Weyl.wZ_binEquiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wZ_binEquiv), [`MIPRE.Weyl.card_binEquiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.card_binEquiv), [`MIPRE.Weyl.proj_binEquiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.proj_binEquiv), [`MIPRE.Weyl.proj_wZ_binEquiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.proj_wZ_binEquiv), [`MIPRE.Weyl.proj_wX_binEquiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.proj_wX_binEquiv), [`MIPRE.Weyl.eprScale_binEquiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.eprScale_binEquiv), [`MIPRE.Weyl.epr_binEquiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.epr_binEquiv), [`MIPRE.Weyl.pauli_binary`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.pauli_binary), [`MIPRE.Weyl.exists_binEquiv_pauli_binary`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.exists_binEquiv_pauli_binary), [`MIPRE.Weyl.trDot_two`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.trDot_two), [`MIPRE.Weyl.sgn_trDot_two`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.sgn_trDot_two), [`MIPRE.Weyl.wZ_two_diag`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wZ_two_diag), [`MIPRE.Weyl.wX_two_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wX_two_apply).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 1157](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L1157)
