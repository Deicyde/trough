---
declaration: lemma
origin: cited
lean: MIPRE.ancillaProj, MIPRE.ancillaProj_conjTranspose, MIPRE.ancillaProj_mul_self, MIPRE.sum_ancillaProj, MIPRE.exists_isometry_of_povm, MIPRE.ancillaEmbed, MIPRE.ancillaEmbed_isometry, MIPRE.exists_unitary_extending, MIPRE.exists_projective_dilation, MIPRE.dotProduct_mulVec_submatrix, MIPRE.dotProduct_comp_equiv, MIPRE.dotProduct_mulVec_conj
statement: formalized
proof: formalized
---

# Naimark dilation of a question-indexed family

Let $\{E^x_a\}$ be a family of POVMs on $\mathbb{C}^d$, indexed by questions $x$ and outcomes $a \in {\mathcal{A}}$. Then there is a family of *projective* measurements $\{P^x_a\}$ on $\mathbb{C}^d \otimes \mathbb{C}^{{\mathcal{A}}}$ and a *single*, question-independent isometry $V : \mathbb{C}^d \to \mathbb{C}^d \otimes \mathbb{C}^{{\mathcal{A}}}$, $|v\rangle \mapsto |v\rangle \otimes |a_0\rangle$, such that $V^\dagger P^x_a V = E^x_a$ for every $x$ and $a$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The columns of the matrix $V^x$ whose $(q, j)$ entry is $\sqrt{E^x}$-like — concretely, the square root of $E^x_a$ read off in the $a$-th block — form an isometry $\mathbb{C}^d \to \mathbb{C}^d \otimes \mathbb{C}^{{\mathcal{A}}}$ compressing the block-diagonal projectors $\Pi_a = {I} \otimes |a\rangle\langlea|$ back to $E^x_a$. Extending each $V^x$ to a unitary $U^x$ of the larger space that agrees with it on the $a_0$-slice — the completion of an orthonormal family to an orthonormal basis — makes $P^x_a = (U^x)^\dagger \Pi_a U^x$ projective with the compression along the *fixed* isometry $|v\rangle \mapsto |v\rangle \otimes |a_0\rangle$. The question-independence of that isometry is the whole point: the expectations are taken against a shared state, which must not depend on the question.

## Lean

Formalized as [`MIPRE.ancillaProj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ancillaProj), [`MIPRE.ancillaProj_conjTranspose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ancillaProj_conjTranspose), [`MIPRE.ancillaProj_mul_self`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ancillaProj_mul_self), [`MIPRE.sum_ancillaProj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_ancillaProj), [`MIPRE.exists_isometry_of_povm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.exists_isometry_of_povm), [`MIPRE.ancillaEmbed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ancillaEmbed), [`MIPRE.ancillaEmbed_isometry`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ancillaEmbed_isometry), [`MIPRE.exists_unitary_extending`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.exists_unitary_extending), [`MIPRE.exists_projective_dilation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.exists_projective_dilation), [`MIPRE.dotProduct_mulVec_submatrix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.dotProduct_mulVec_submatrix), [`MIPRE.dotProduct_comp_equiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.dotProduct_comp_equiv), [`MIPRE.dotProduct_mulVec_conj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.dotProduct_mulVec_conj).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 718](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L718)
