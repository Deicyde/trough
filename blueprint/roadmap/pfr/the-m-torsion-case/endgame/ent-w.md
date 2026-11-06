---
declaration: lemma
origin: cited
lean: entropy_of_W_le
statement: formalized
proof: formalized
---

# Entropy of $W$

We have $\mathbb{H}[W] \leq (2m-1)k + \frac1m \sum_{i=1}^m \mathbb{H}[X_i]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Multidistance](../multidistance/multidist-def.md)
- [Multidistance and Ruzsa distance, IV](../multidistance/multidist-ruzsa-iv.md)
- [Kaimonovich–Vershik–Madiman inequality](../more-ruzsa-distance-estimates/klm-1.md)

## Proof

Without loss of generality, we may take $X_1,\dots,X_m$ to be independent. Write $S = \sum_{i=1}^m X_i$. Note that for each $j \in \mathbb{Z}/m\mathbb{Z}$, the sum $Q_j$ from (pqr-defs) above has the same distribution as $S$. By [Kaimonovich–Vershik–Madiman inequality](../more-ruzsa-distance-estimates/klm-1.md) we have

$$
\begin{aligned}
\mathbb{H}[W] = \mathbb{H}[\sum_{j \in \mathbb{Z}/m\mathbb{Z}} Q_j]  & \leq \mathbb{H}[S] + \sum_{j=2}^m (\mathbb{H}[Q_1+Q_j] - \mathbb{H}[S]) \\ & = \mathbb{H}[S] + (m-1) d[S;-S].
\end{aligned}
$$

By [Multidistance and Ruzsa distance, IV](../multidistance/multidist-ruzsa-iv.md), we have

$$
d[S; -S] \leq 2 k\qquad\text{(3)}
$$

and hence

$$
\mathbb{H}[W] \leq 2 k (m-1) + \mathbb{H}[S].
$$

From [Multidistance](../multidistance/multidist-def.md) we have

$$
\mathbb{H}[S] = k + \frac1m \sum_{i=1}^m \mathbb{H}[X_i],\qquad\text{(4)}
$$

and the claim follows.

## Lean

Formalized as [`entropy_of_W_le`](https://teorth.github.io/pfr/docs/find/#doc/entropy_of_W_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 688](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L688)
