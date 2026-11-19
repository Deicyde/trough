---
declaration: theorem
origin: cited
lean: MIPRE.fourierOf, MIPRE.fourierOf_conjTranspose, MIPRE.fourierOf_posSemidef, MIPRE.sum_sgn_smul_fourierOf_sq, MIPRE.sum_fourierOf_sq, MIPRE.exists_exactly_linear, MIPRE.extVecA, MIPRE.ancillaEmbed_kron_isometry, MIPRE.norm_evec_extVecA, MIPRE.kron_one_mul_ancillaEmbed, MIPRE.ancillaEmbed_conjTranspose_mul_kron_one, MIPRE.compress_mul_kron_one, MIPRE.compress_kron_one_mul, MIPRE.qform_extVecA, MIPRE.stateSqNorm_sub_of_isometry, MIPRE.conjTranspose_mul_self_of_involution, MIPRE.exists_exactly_linear_close
statement: formalized
proof: formalized
---

# Exact linearity from approximate linearity

Let $\{O^u\}_{u \in V}$, $V = \mathbb{F}_q^n$, be observables on the first party's space — self-adjoint involutions — and let $|\psi\rangle$ be a state. Then, on the space extended by an ancilla register $\mathbb{C}^V$ on the *first party only*, with the extended state $|\psi'\rangle = |\psi\rangle \otimes |0\rangle$, there are observables $\{L^u\}$ that are *exactly* linear,

$$
L^u L^{u'} \;=\; L^{u + u'}\;, \qquad L^0 \;=\; {I}\;,
$$

such that the average squared distance to the original family is *equal* to the average linearity defect:

$$
\mathop{\mathbb{E}}_{u \in V} \left\| {\bigl(L^u - O^u \otimes {I}\bigr) |\psi'\rangle} \right\|^2
\;=\; \mathop{\mathbb{E}}_{a, b \in V} \left\| {\bigl(O^a O^b - O^{a + b}\bigr) |\psi\rangle} \right\|^2\;.
$$

In particular, if the family is $\delta$-approximately linear on average then $L^u \approx_\delta O^u$ on average over $u$: the error is linear in $\delta$, with no loss in the exponent and no change of constant.

## Depends on

- [State-dependent POVM distance](../../foundations/part-02/def-state-distance.md)
- [Generalized Pauli observables in characteristic two](../../foundations/part-02/def-generalized-pauli.md)
- [Naimark dilation of a question-indexed family](../../foundations/part-02/lem-naimark-dilation.md)

## Proof depends on

- [Bipartite model](../../downstream-results/part-02/def-bipartite-model.md)

## Proof

The Fourier argument, in three exact steps and one identity.

**Parseval.** Let $A_e = \left\vert {V} \right\vert^{-1} \sum_a (-1)^{\operatorname{tr}(a \cdot e)} O^a$ be the Fourier transform of the family against the characters of the trace form (Definition [Generalized Pauli observables in characteristic two](../../foundations/part-02/def-generalized-pauli.md)). Merging the characters and summing over $e$ collapses the double sum, because $\sum_e (-1)^{\operatorname{tr}(c \cdot e)}$ is $\left\vert {V} \right\vert$ at $c = 0$ and $0$ otherwise:

$$
\sum_e (-1)^{\operatorname{tr}(u \cdot e)} A_e^2 \;=\; \left\vert {V} \right\vert^{-1} \sum_a O^a O^{a + u}\;.\qquad\text{(2)}
$$

At $u = 0$ the right-hand side is $\left\vert {V} \right\vert^{-1} \sum_a (O^a)^2 = {I}$, so $\{A_e^2\}$ is a POVM — *exactly*, with no appeal to the approximate linearity. That is the only place the involution property is used.

**Naimark.** Dilate that POVM to a projective measurement $\{P_e\}$ on $\mathbb{C}^{d} \otimes \mathbb{C}^{V}$, compressed back by the isometry $|v\rangle \mapsto |v\rangle \otimes |0\rangle$ (Lemma [Naimark dilation of a question-indexed family](../../foundations/part-02/lem-naimark-dilation.md)). One isometry serves the whole family of families, which is what lets the estimate be taken against the single state $|\psi'\rangle$.

**Inversion.** Put $L^u = \sum_e (-1)^{\operatorname{tr}(u \cdot e)} P_e$. Mutual orthogonality of the $P_e$ gives $L^u L^{u'} = L^{u + u'}$ and $L^0 = \sum_e P_e = {I}$, and the compression of $L^u$ is the left-hand side of (2), hence $\left\vert {V} \right\vert^{-1} \sum_a O^a O^{a+u}$.

**The identity.** Expanding both squared distances — each is $2$ minus the two orders of an overlap, the operators involved being unitary — and compressing, the $u$-th term on the left is the average over $a$ of the $(a, a+u)$-th term on the right, after reindexing that average by $a \mapsto a + u$. Summing over $u$ and reindexing once more, by $u \mapsto a + u$ for each fixed $a$, gives the stated equality. No inequality is used anywhere, which is why the constant is exactly $1$.

## Lean

Formalized as [`MIPRE.fourierOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.fourierOf), [`MIPRE.fourierOf_conjTranspose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.fourierOf_conjTranspose), [`MIPRE.fourierOf_posSemidef`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.fourierOf_posSemidef), [`MIPRE.sum_sgn_smul_fourierOf_sq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_sgn_smul_fourierOf_sq), [`MIPRE.sum_fourierOf_sq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_fourierOf_sq), [`MIPRE.exists_exactly_linear`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.exists_exactly_linear), [`MIPRE.extVecA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.extVecA), [`MIPRE.ancillaEmbed_kron_isometry`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ancillaEmbed_kron_isometry), [`MIPRE.norm_evec_extVecA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.norm_evec_extVecA), [`MIPRE.kron_one_mul_ancillaEmbed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.kron_one_mul_ancillaEmbed), [`MIPRE.ancillaEmbed_conjTranspose_mul_kron_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ancillaEmbed_conjTranspose_mul_kron_one), [`MIPRE.compress_mul_kron_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.compress_mul_kron_one), [`MIPRE.compress_kron_one_mul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.compress_kron_one_mul), [`MIPRE.qform_extVecA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.qform_extVecA), [`MIPRE.stateSqNorm_sub_of_isometry`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.stateSqNorm_sub_of_isometry), [`MIPRE.conjTranspose_mul_self_of_involution`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.conjTranspose_mul_self_of_involution), [`MIPRE.exists_exactly_linear_close`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.exists_exactly_linear_close).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 2752](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L2752)
