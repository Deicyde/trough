---
declaration: theorem
origin: cited
lean: MIPRE.Orthonormalization.povm_orthogonalization_of_isCenterValuedTrace, MIPRE.Orthonormalization.povm_orthogonalization_vecTrace
statement: formalized
proof: formalized
---

# Orthonormalization in algebras without abelian projections

Let $\mathcal{M}$ be a von Neumann algebra with no nonzero abelian projection and a faithful tracial state given by finitely many vectors, as in Lemma [A centre-valued trace from a vector trace](lem-center-valued-trace.md). Then the conclusion of Theorem [Orthonormalization](thm-orthonormalization.md) holds in $\mathcal{M}$ for every vector state, and more generally for every positive normalized functional of trace-class form: a POVM $\{M_a\}$ in $\mathcal{M}$ with $\varphi(\sum_a M_a^2) > 1 - \varepsilon$ is within $\varphi(\sum_a (M_a - P_a)^*(M_a - P_a)) < 9\varepsilon$ of a projective measurement $\{P_a\}$ in $\mathcal{M}$.

## Depends on

- [A centre-valued trace from a vector trace](lem-center-valued-trace.md)

## Proof

The vendored proof of the theorem for II$_1$ factors uses its factor hypothesis only to build its centre-valued trace, the scalar trace $x \mapsto \tau(x)\,1$; it reads the centre-valued trace only through the clauses of the interface, and the state only through positivity, normalization and its trace-class form. With the centre-valued trace of Lemma [A centre-valued trace from a vector trace](lem-center-valued-trace.md) the same proof applies: the selection lemma on the type II$_1$ part, which is all of $\mathcal{M}$, then the polar decomposition in $M_n(\mathcal{M})$ and the three-term estimate.

## Lean

Formalized as [`MIPRE.Orthonormalization.povm_orthogonalization_of_isCenterValuedTrace`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Orthonormalization.povm_orthogonalization_of_isCenterValuedTrace), [`MIPRE.Orthonormalization.povm_orthogonalization_vecTrace`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Orthonormalization.povm_orthogonalization_vecTrace).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 390](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L390)
