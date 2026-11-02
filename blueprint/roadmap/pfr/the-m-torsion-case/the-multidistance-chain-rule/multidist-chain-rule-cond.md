---
declaration: lemma
origin: cited
lean: cond_multiDist_chainRule
statement: formalized
proof: formalized
---

# Conditional multidistance chain rule

Let $\pi \colon G \to H$ be a homomorphism of abelian groups. Let $I$ be a finite index set and let $X_{[m]}$ be a tuple of $G$-valued random variables. Let $Y_{[m]}$ be another tuple of random variables (not necessarily $G$-valued). Suppose that the pairs $(X_i, Y_i)$ are jointly independent of one another (but $X_i$ need not be independent of $Y_i$). Then

$$
\begin{aligned}
D[ X_{[m]} | Y_{[m]} ] &=  D[ X_{[m]} \,|\, \pi(X_{[m]}), Y_{[m]}] + D[ \pi(X_{[m]}) \,|\, Y_{[m]}] \\
&\quad\qquad + \mathbb{I}[ \sum_{i=1}^m X_i : \pi(X_{[m]}) \; \big| \;  \pi\bigl(\sum_{i=1}^m X_i \bigr), Y_{[m]} ].\qquad\text{(4)}\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Multidistance chain rule](multidist-chain-rule.md)

## Proof

For each $y_i$ in the support of $p_{Y_i}$, apply [Multidistance chain rule](multidist-chain-rule.md) with $X_i$ replaced by the conditioned random variable $(X_i|Y_i=y_i)$, and the claim (4) follows by averaging [(1)](multidist-chain-rule.md) in the $y_i$ using the weights $p_{Y_i}$.

## Lean

Formalized as [`cond_multiDist_chainRule`](https://teorth.github.io/pfr/docs/find/#doc/cond_multiDist_chainRule).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 405](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L405)
