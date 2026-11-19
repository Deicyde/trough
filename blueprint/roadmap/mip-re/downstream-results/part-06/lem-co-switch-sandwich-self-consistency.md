---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Co.Preliminaries.switchSandwich, MIPRE.LIDT.Co.Preliminaries.twoNotionsOfSelfConsistency, MIPRE.LIDT.Co.Preliminaries.bipartiteSSC_implies_localSSC_liftLeft, MIPRE.LIDT.Co.Preliminaries.otherTwoNotionsOfSelfConsistency, MIPRE.LIDT.Co.Preliminaries.selfConsistencyImpliesDataProcessing, MIPRE.LIDT.Co.Preliminaries.completingToMeasurement
statement: formalized
proof: formalized
---

# The switch sandwich and self-consistency, in a symmetric model

Let $S$ be a symmetric model over $\mathcal{P}$ (Definition [Symmetric models](../part-05/def-sym-model.md)), with state $\Psi$, expectation $\mathrm{ev}$ and placements $L$ and $R$, and let $\mathop{\mathbb{E}}_x$ be the average over a distribution of questions $x$ of total weight at most $1$. For a family of submeasurements $A^x$ in $\mathcal{P}$ write $A^x = \sum_a A^x_a$ for the total, and say that $A$ is *$\delta$-self-consistent across the players* if

$$
\mathop{\mathbb{E}}_x \max\Bigl(0,\ \mathrm{ev}\bigl(L(A^x)\bigr) - \sum_a \mathrm{ev}\bigl(L(A^x_a)\, R(A^x_a)\bigr)\Bigr)
\leq \delta.
$$

1. *Switch sandwich.* Let the $A^x$ be projective and $0 \leq B \leq 1$ in $\mathcal{P}$. If $\mathop{\mathbb{E}}_x \sum_a \| (L(A^x_a) - R(A^x_a)) \Psi \|^2 \leq \delta$, then

    $$
    \Bigl| \mathop{\mathbb{E}}_x \sum_a \mathrm{ev}\bigl(L(A^x_a B A^x_a)\bigr) - \mathop{\mathbb{E}}_x \sum_a
    \mathrm{ev}\bigl(L(B)\, R(A^x_a)\bigr) \Bigr| \leq 2 \sqrt{\delta}, \qquad
    \Bigl| \mathop{\mathbb{E}}_x \sum_a \mathrm{ev}\bigl(L(B)\, R(A^x_a)\bigr) - \mathop{\mathbb{E}}_x \sum_a
    \mathrm{ev}\bigl(L(B A^x_a)\bigr) \Bigr| \leq \sqrt{\delta}.
    $$

2. *Two notions of self-consistency.* If $A$ is $\delta$-self-consistent across the players, then $\mathop{\mathbb{E}}_x \sum_a \| (L(A^x_a) - R(A^x_a)) \Psi \|^2 \leq 2 \delta$; $L(A)$ is $\delta$-self-consistent on one space, $\mathop{\mathbb{E}}_x \max(0, \mathrm{ev}(L(A^x)) - \sum_a \mathrm{ev}(L(A^x_a)^2)) \leq \delta$; and $A$ is $\delta$-consistent with itself, $\mathop{\mathbb{E}}_x \max(0, \mathrm{ev}(L(A^x)\, R(A^x)) - \sum_a \mathrm{ev}(L(A^x_a)\, R(A^x_a))) \leq \delta$.

3. *Data processing.* If moreover the $P^x$ are projective submeasurements in $\mathcal{P}$ with $\mathop{\mathbb{E}}_x \sum_a \| L(P^x_a - A^x_a) \Psi \|^2 \leq \varepsilon$, then for all maps $f_x$ on the outcomes, $\mathop{\mathbb{E}}_x \sum_b \| L(P^x_{[f_x = b]} - A^x_{[f_x = b]}) \Psi \|^2 \leq 8 \delta + 8 \sqrt{\varepsilon}$, where $A_{[f = b]} = \sum_{a : f(a) = b} A_a$.

4. *Completing to a measurement.* For a single question, let $A$ be a measurement that is $\eta$-self-consistent across the players and $B$ a submeasurement with $\sum_a \| L(A_a - B_a) \Psi \|^2 \leq \delta$. Adding $1 - \sum_a B_a$ to one outcome of $B$ gives a measurement $C$ with $\sum_a \| L(A_a - C_a) \Psi \|^2 \leq 2 \delta + 4 \sqrt{\delta} + 2 \eta$.

## Depends on

- [Symmetric models](../part-05/def-sym-model.md)
- [Swap symmetry in a symmetric model](../part-05/lem-sym-model-swap.md)

## Proof depends on

- [Bipartite model](../part-02/def-bipartite-model.md)

## Proof

The proofs are the vendored ones, in `MIPRE/Background/LIDT/MIPStarRE/LDT/Preliminaries/`, rewritten over the symmetric model declaration by declaration (`planning/c6b-plan.md`, milestone M3 and “Port conventions”). Each estimate is a Cauchy–Schwarz inequality for the vector state read as a state model (Definition [Bipartite model](../part-02/def-bipartite-model.md)), $|\mathrm{ev}(X^* Y)|^2 \leq \mathrm{ev}(X^* X)\, \mathrm{ev}(Y^* Y)$, applied question by question and averaged with $\mathop{\mathbb{E}}_x \sqrt{f} \leq \sqrt{\mathop{\mathbb{E}}_x f}$, which needs the total weight to be at most $1$. The Kronecker identities of the vendored proofs are the commutation of $L(x)$ with $R(y)$ and the multiplicativity of $L$ and $R$. Swap symmetry enters items 2 and 3 through $\mathrm{ev}(L(x)) = \mathrm{ev}(R(x))$ (Lemma [Swap symmetry in a symmetric model](../part-05/lem-sym-model-swap.md)): it expands $\| (L(x) - R(x)) \Psi \|^2 = 2 (\mathrm{ev}(L(x^2)) - \mathrm{ev}(L(x)\, R(x)))$ for self-adjoint $x$. The vendored statements assume it, with the normalization of the state; here both are theorems of the model.

## Lean

Formalized as [`MIPRE.LIDT.Co.Preliminaries.switchSandwich`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Preliminaries.switchSandwich), [`MIPRE.LIDT.Co.Preliminaries.twoNotionsOfSelfConsistency`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Preliminaries.twoNotionsOfSelfConsistency), [`MIPRE.LIDT.Co.Preliminaries.bipartiteSSC_implies_localSSC_liftLeft`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Preliminaries.bipartiteSSC_implies_localSSC_liftLeft), [`MIPRE.LIDT.Co.Preliminaries.otherTwoNotionsOfSelfConsistency`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Preliminaries.otherTwoNotionsOfSelfConsistency), [`MIPRE.LIDT.Co.Preliminaries.selfConsistencyImpliesDataProcessing`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Preliminaries.selfConsistencyImpliesDataProcessing), [`MIPRE.LIDT.Co.Preliminaries.completingToMeasurement`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Preliminaries.completingToMeasurement).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3672](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3672)
