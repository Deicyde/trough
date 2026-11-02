---
declaration: lemma
origin: cited
lean: multiDist_chainRule
statement: formalized
proof: formalized
---

# Multidistance chain rule

Let $\pi \colon G \to H$ be a homomorphism of abelian groups and let $X_{[m]}$ be a tuple of jointly independent $G$-valued random variables. Then $D[X_{[m]}]$ is equal to

$$
D[ X_{[m]} | \pi(X_{[m]}) ]  +D[ \pi(X_{[m]}) ]  + \mathbb{I}[ \sum_{i=1}^m X_i  : \pi(X_{[m]}) \; \big| \; \pi\bigl(\sum_{i=1}^m X_i\bigr) ]\qquad\text{(1)}
$$

where $\pi(X_{[m]}) := (\pi(X_i))_{1 \leq i \leq m}$.

## Depends on

- [Multidistance](../multidistance/multidist-def.md)

## Proof depends on

- [Alternate formula for conditional mutual information](../../shannon-entropy-inequalities/part-02/conditional-mutual-alt.md)
- [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md)
- [Chain rule](../../shannon-entropy-inequalities/part-01/chain-rule.md)

## Proof

For notational brevity during this proof, write $S := \sum_{i=1}^m X_i$.

From [Alternate formula for conditional mutual information](../../shannon-entropy-inequalities/part-02/conditional-mutual-alt.md) and [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md), noting that $\pi(S)$ is determined both by $S$ and by $\pi(X_{[m]})$, we have

$$
\mathbb{I}[S:\pi(X_{[m]})|\pi(S)] = \mathbb{H}[S]+\mathbb{H}[\pi(X_{[m]})]-\mathbb{H}[S,\pi(X_{[m]})]-\mathbb{H}[\pi(S)],
$$

and by [Chain rule](../../shannon-entropy-inequalities/part-01/chain-rule.md) the right-hand side is equal to

$$
\mathbb{H}[S]-\mathbb{H}[S|\pi(X_{[m]})]-\mathbb{H}[\pi(S)].
$$

Therefore,

$$
\mathbb{H}[S]=\mathbb{H}[S|\pi(X_{[m]})]+\mathbb{H}[\pi(S)]+\mathbb{I}[S:\pi(X_{[m]})|\pi(S)].\qquad\text{(2)}
$$

From a further application of [Chain rule](../../shannon-entropy-inequalities/part-01/chain-rule.md) and [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md) we have

$$
\mathbb{H}[X_i] = \mathbb{H}[X_i \, | \, \pi(X_i)] + \mathbb{H}[\pi(X_i)]\qquad\text{(3)}
$$

for all $1 \leq i \leq m$. Averaging (3) in $i$ and subtracting this from (2), we obtain the claim from [Multidistance](../multidistance/multidist-def.md).

## Lean

Formalized as [`multiDist_chainRule`](https://teorth.github.io/pfr/docs/find/#doc/multiDist_chainRule).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 375](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L375)
