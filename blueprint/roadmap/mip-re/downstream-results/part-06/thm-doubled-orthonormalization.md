---
declaration: theorem
origin: cited
lean: MIPRE.LIDT.Co.SymModel.orthonormalization_of_isFinitePair, MIPRE.LIDT.Co.SymModel.orthonormalization_of_isFinitePair_sddRel, MIPRE.LIDT.Co.Doubling.orthonormalization_model, MIPRE.LIDT.Co.Doubling.orthonormalization_of_isDyadicPair, MIPRE.LIDT.Co.Doubling.orthonormalization_model_sddRel
statement: formalized
proof: formalized
---

# Orthonormalization in the doubled model

Let $M$ be a finite pair in a unit state whose two players' operators contain no nonzero abelian projection, for instance a dyadic pair, and let $D(M)$ be its doubled model (Definition [The doubled model](../part-05/def-doubled-model.md)). Let $X$ be a submeasurement in $\mathcal{P}$, with total $X_{\mathrm{total}} = \sum_a X_a$, whose bipartite strong self-consistency defect

$$
\max\Bigl(0,\ \mathrm{ev}\bigl(L(X_{\mathrm{total}})\bigr) - \sum_a \mathrm{ev}\bigl(L(X_a)\,
R(X_a)\bigr)\Bigr)
$$

is at most $\eta$, where $\eta > 0$ and $\mathrm{ev}$ is the expectation of the model's state (Definition [Symmetric models](../part-05/def-sym-model.md)). Then there is a projective submeasurement $P$ in $\mathcal{P}$ with

$$
\sum_a \bigl\| \bigl(L(X_a) - L(P_a)\bigr) \Psi \bigr\|^2 \leq 100\, \eta^{1/4}.
$$

This is the vendored orthonormalization step with its constant. The same holds in any symmetric model whose bipartite reading is a finite pair whose first player's operators contain no nonzero abelian projection; the doubled model is one by Lemmas [The doubled model is a finite pair, with the order of its parts](lem-doubled-model-finite-pair.md) and [No abelian projections in the doubled model](lem-doubled-model-no-abelian.md).

## Depends on

- [No abelian projections in the doubled model](lem-doubled-model-no-abelian.md)
- [Orthonormalization in a finite pair without abelian projections](../part-05/cor-orthonormalization-finite-pair.md)

## Proof depends on

- [The doubled model is a finite pair, with the order of its parts](lem-doubled-model-finite-pair.md)
- [Swap symmetry in a symmetric model](../part-05/lem-sym-model-swap.md)

## Proof

Complete $X$ to a positive operator valued measurement by one further outcome, $1 - X_{\mathrm{total}}$. In any symmetric model, $1 - \sum_o \|L(\tilde X_o) \Psi\|^2$ for the completion $\tilde X$ is at most twice the defect of $X$, using $\|R(y) \Psi\| = \|L(y) \Psi\|$ and the Cauchy–Schwarz inequality for $\langle \Psi, L(y) R(y) \Psi \rangle$; so it is less than $3 \min(\eta, 1)$. The doubled model is a finite pair without abelian projections (Lemmas [The doubled model is a finite pair, with the order of its parts](lem-doubled-model-finite-pair.md) and [No abelian projections in the doubled model](lem-doubled-model-no-abelian.md)), so Corollary [Orthonormalization in a finite pair without abelian projections](../part-05/cor-orthonormalization-finite-pair.md) gives a projective measurement $Q$ of the first player's algebra of $D(M)$ within $9 \cdot 3 \min(\eta, 1)$ of $\tilde X$. Dropping the added outcome gives $P$, and $27 \min(\eta, 1) \leq 100 \eta^{1/4}$ (`reports/c6b-paper-proofs.md`, Section 4, Theorem G). The case $\eta = 0$ is excluded because the hypothesis of Corollary [Orthonormalization in a finite pair without abelian projections](../part-05/cor-orthonormalization-finite-pair.md) is strict.

## Lean

Formalized as [`MIPRE.LIDT.Co.SymModel.orthonormalization_of_isFinitePair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.SymModel.orthonormalization_of_isFinitePair), [`MIPRE.LIDT.Co.SymModel.orthonormalization_of_isFinitePair_sddRel`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.SymModel.orthonormalization_of_isFinitePair_sddRel), [`MIPRE.LIDT.Co.Doubling.orthonormalization_model`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.orthonormalization_model), [`MIPRE.LIDT.Co.Doubling.orthonormalization_of_isDyadicPair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.orthonormalization_of_isDyadicPair), [`MIPRE.LIDT.Co.Doubling.orthonormalization_model_sddRel`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.orthonormalization_model_sddRel).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3539](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3539)
