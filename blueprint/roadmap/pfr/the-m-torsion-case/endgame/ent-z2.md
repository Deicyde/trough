---
declaration: lemma
origin: cited
lean: entropy_of_Z_two_le
statement: formalized
proof: formalized
---

# Entropy of $Z_2$

We have $\mathbb{H}[Z_2] \leq (8m^2-16m+1) k + \frac{1}{m} \sum_{i=1}^m \mathbb{H}[X_i]$.

## Depends on

Its statement uses no other node that has an article here.

## Proof depends on

- [Sums of dilates II](../more-ruzsa-distance-estimates/sum-dilate-ii.md)
- [Kaimonovich–Vershik–Madiman inequality](../more-ruzsa-distance-estimates/klm-1.md)

## Proof

We observe

$$
\mathbb{H}[Z_2] = \mathbb{H}[\sum_{j \in \mathbb{Z}/m\mathbb{Z}} j Q_j].
$$

Applying [Kaimonovich–Vershik–Madiman inequality](../more-ruzsa-distance-estimates/klm-1.md) one has

$$
\begin{aligned}
\mathbb{H}[Z_2] &\leq \sum_{i=2}^{m-1} \mathbb{H}[Q_1 + i Q_i]  - (m-2) \mathbb{H}[S].
\end{aligned}
$$

Using [Sums of dilates II](../more-ruzsa-distance-estimates/sum-dilate-ii.md) and [(3)](ent-w.md) we get

$$
\begin{aligned}
\mathbb{H}[Z_2]
&\leq \mathbb{H}[S] + 4m (m-2) d[S;-S] \\
&\leq \mathbb{H}[S] + 8m (m-2) k.
\end{aligned}
$$

Applying [(4)](ent-w.md) gives the claim.

## Lean

Formalized as [`entropy_of_Z_two_le`](https://teorth.github.io/pfr/docs/find/#doc/entropy_of_Z_two_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 714](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L714)
