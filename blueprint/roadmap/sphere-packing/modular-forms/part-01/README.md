---
navigation: transparent
---

# Gamma-generators to disc-pos

- [Gamma-generators](def-gamma-generators.md)

The following two lemmas tell us the group structure of $\Gamma(1) = \Gamma_1$ and $\Gamma(2)$, which we will use later on to define the theta forms.

- [Gamma-1-generators](lemma-gamma-1-generators.md)
- [Gamma-2-generators](lemma-gamma-2-generators.md)

Let $z\in\mathfrak{H}$, $k\in\mathbb{Z}$, and $\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\in\mathrm{SL}_2(\mathbb{Z})$. We omit many of the proofs below when they exist in Mathlib already.

- [automorphy-factor](def-automorphy-factor.md)
- [automorphy-factor-chain-rule](lemma-automorphy-factor-chain-rule.md)
- [slash-operator-chain-rule](lemma-slash-operator-chain-rule.md)

In particular, this lemma implies that if $\Gamma = \langle M_i \rangle_{i \in \mathcal{I}} \rangle$, then the slash action $F|\gamma$ is uniquely determined by the action of generators, i.e. $F|M_i$ and $F|M_i^{-1}$.

- [slash-negI-even-weight](lemma-slash-negi-even-weight.md)
- [Mk](def-mk.md)

By replacing condition $(3)$ above with (4) below defines the subspace of cusp forms, which we denote by $S_k(\Gamma)$.

3

1. For all $\gamma \in \mathrm{SL}_2(\mathbb{Z})$, and all $0 < \epsilon$, there exists $A \in \mathbb{R}$ such that for all $z \in \mathbb{H}$, with $A \le \mathrm{Im}(z)$, we have $|(f \mid_k \gamma) (z) |\le \epsilon$.

Let us consider several examples of modular forms.

- [Ek](def-ek.md)
- [Ek-is-modular-form](lemma-ek-is-modular-form.md)

Since modular forms are holomorphic and periodic they have a Fourier expansions. One thing that we will need is the growth of the Fourier coefficients, which is given by the following lemma.

For Eisenstein series, we can see this directly from the following:

- [Ek-Fourier](lemma-ek-fourier.md)

The infinite sum [(1)](def-ek.md) does not converge absolutely for $k=2$. On the other hand, the expression [(3)](lemma-ek-fourier.md) converges to a holomorphic function on the upper half-plane and we will take it as a definition of $E_2$ (See Definition [E2](def-e2.md) below).

The discriminant form is a unique normalized cusp form of weight 12, which can be defined as:

- [disc-definition](def-disc-definition.md)

This product formula allows us to prove positivity of $\Delta(it)$ for $t > 0$ later. But we need to first check its a modular form. For this we first need some definitions/ results.

We define it as a $q$-series, which gives a holomorphic function on $\mathfrak{H}$.

- [E2](def-e2.md)
- [E2-transform-S](lemma-e2-transform-s.md)

More generally, we have

- [E2-transform-general](lemma-e2-transform-general.md)
- [dedekind_eta](def-dedekind-eta.md)
- [dedekind_eta_transformation](lemma-dedekind-eta-transformation.md)
- [disc-cuspform](lemma-disc-cuspform.md)
- [disc-E4E6](lemma-disc-e4e6.md)
- [disc-pos](cor-disc-pos.md)
