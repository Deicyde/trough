---
declaration: definition
origin: cited
lean: MIPRE.BipartiteModel, MIPRE.BipartiteModel.tensor, MIPRE.StateModel, MIPRE.StateModel.mat, MIPRE.CommutingOperatorStrategy.toModel, MIPRE.CommutingOperatorStrategy.commute_of_mem
statement: formalized
---

# Bipartite model

A *bipartite model* consists of a complex Hilbert space $\mathcal{H}$, a vector $\psi \in \mathcal{H}$, a unital $*$-algebra ${\mathscr{A}}$ over $\mathbb{C}$ represented on $\mathcal{H}$ by a unital $*$-homomorphism $\pi : {\mathscr{A}} \to B(\mathcal{H})$, and two unital $*$-algebras ${\mathscr{A}}_A$ and ${\mathscr{A}}_B$ over $\mathbb{C}$ with unital $*$-homomorphisms $\pi_A : {\mathscr{A}}_A \to {\mathscr{A}}$ and $\pi_B : {\mathscr{A}}_B \to {\mathscr{A}}$ such that $\pi_A(a)$ and $\pi_B(b)$ commute for all $a \in {\mathscr{A}}_A$ and $b \in {\mathscr{A}}_B$. The first player's operators are elements of ${\mathscr{A}}_A$, the second player's elements of ${\mathscr{A}}_B$, and a state quantity of $a$ is computed on the vector $\pi(\pi_A(a))\psi$. That $\psi$ is a unit vector is a hypothesis of each statement that needs it, not part of the model. It has two instances.

1. The *tensor-product model* of a vector $\psi \in \mathbb{C}^{d_A} \otimes \mathbb{C}^{d_B}$ has ${\mathscr{A}} = M_{d_A d_B}(\mathbb{C})$ acting on $\mathbb{C}^{d_A} \otimes \mathbb{C}^{d_B}$, ${\mathscr{A}}_A = M_{d_A}(\mathbb{C})$, ${\mathscr{A}}_B = M_{d_B}(\mathbb{C})$, $\pi_A(X) = X \otimes {I}$ and $\pi_B(Y) = {I} \otimes Y$. Its products and sums are the matrix ones, so the matrix calculus is the model's with nothing to translate.
2. The *commuting-operator model* of a commuting-operator strategy $(\mathcal{H}, \psi, E, F)$ has ${\mathscr{A}} = B(\mathcal{H})$, ${\mathscr{A}}_A$ the commutant of the $F^y_b$ and ${\mathscr{A}}_B$ the commutant of ${\mathscr{A}}_A$, with the inclusions. They commute by construction and contain the $E^x_a$ and the $F^y_b$. A commutant contains the square roots of its positive elements, so positivity in ${\mathscr{A}}_A$ and in ${\mathscr{A}}_B$ is positivity in $B(\mathcal{H})$, which is what the measurements of the analyses need.

## Depends on

- [Commuting-operator strategy](../../parallel-repetition/def-co-strategy-bipartite.md)

## Lean

Formalized as [`MIPRE.BipartiteModel`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel), [`MIPRE.BipartiteModel.tensor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.tensor), [`MIPRE.StateModel`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.StateModel), [`MIPRE.StateModel.mat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.StateModel.mat), [`MIPRE.CommutingOperatorStrategy.toModel`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy.toModel), [`MIPRE.CommutingOperatorStrategy.commute_of_mem`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy.commute_of_mem).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1193](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1193)
