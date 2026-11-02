---
declaration: lemma
origin: cited
lean: sum_of_conditional_distance_le
statement: formalized
proof: formalized
---

# Distance bound

We have $\sum_{i=1}^m d[X_i;Z_2|W] \leq 4(m^3-m^2) k$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Kaimonovich–Vershik–Madiman inequality, III](../more-ruzsa-distance-estimates/klm-3.md)
- [Upper bound on conditioned Ruzsa distance](../../entropic-ruzsa-calculus/part-02/cond-dist-fact.md)
- [Mutual information bound](mutual-w-z2.md)
- [Entropy of $Z_2$](ent-z2.md)
- [Multidistance and Ruzsa distance, II](../multidistance/multidist-ruzsa-ii.md)

## Proof

For each $i \in \{1,\dots, m\}$, using [Kaimonovich–Vershik–Madiman inequality, III](../more-ruzsa-distance-estimates/klm-3.md) (noting the sum $Z_2$ contains $X_i$ as a summand) we have

$$
d[X_i;Z_2] \leq d[X_i;X_i] + \tfrac12 (\mathbb{H}[Z_2] - \mathbb{H}[X_i])
$$

and using [Upper bound on conditioned Ruzsa distance](../../entropic-ruzsa-calculus/part-02/cond-dist-fact.md) we have

$$
d[X_i;Z_2 | W] \leq d[X_i;Z_2] + \tfrac12 \mathbb{I}[W : Z_2].
$$

Combining with (in-a-bit-6) and [Mutual information bound](mutual-w-z2.md) gives

$$
d[X_i;Z_2 | W] \leq d[X_i;X_i] + \tfrac12 (\mathbb{H}[Z_2] - \mathbb{H}[X_i]) + (m-1)k.
$$

Summing over $i$ and applying [Entropy of $Z_2$](ent-z2.md) gives

$$
\sum_{i = 1}^m d[X_i;Z_2 | W] \leq \sum_{i = 1}^m d[X_i;X_i] + m(8m^2-16m+1) k/2 + m(m-1) k.
$$

Finally, applying [Multidistance and Ruzsa distance, II](../multidistance/multidist-ruzsa-ii.md) (and dropping some lower order terms) gives the claim.

## Lean

Formalized as [`sum_of_conditional_distance_le`](https://teorth.github.io/pfr/docs/find/#doc/sum_of_conditional_distance_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 750](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L750)
