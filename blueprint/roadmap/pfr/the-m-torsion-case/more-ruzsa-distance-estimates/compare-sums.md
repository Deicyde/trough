---
declaration: lemma
origin: cited
lean: ent_of_sum_le_ent_of_sum
statement: formalized
proof: formalized
---

# Comparing sums

Let $(X_i)_{1 \leq i \leq m}$ and $(Y_j)_{1 \leq j \leq l}$ be tuples of jointly independent random variables (so the $X$'s and $Y$'s are also independent of each other), and let $f: \{1,\dots,l\} \to \{1,\dots,m\}$ be a function, then

$$
\mathbb{H}[\sum_{j=1}^l Y_j] \leq \mathbb{H}[ \sum_{i=1}^m X_i ] + \sum_{j=1}^l (\mathbb{H}[ Y_j - X_{f(j)}] - \mathbb{H}[X_{f(j)}]).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Kaimonovich–Vershik–Madiman inequality](klm-1.md)
- [Kaimanovich-Vershik-Madiman inequality](../../entropic-ruzsa-calculus/part-02/kv.md)
- [Negation preserves entropy](../../entropic-ruzsa-calculus/part-01/neg-ent.md)
- [Independent lower bound on sumset](../../entropic-ruzsa-calculus/part-01/sumset-lower.md)

## Proof

Write $W := \sum_{i=1}^m X_i$. From [Independent lower bound on sumset](../../entropic-ruzsa-calculus/part-01/sumset-lower.md) we have

$$
\mathbb{H}[\sum_{j=1}^l Y_j]  \leq \mathbb{H}[-W + \sum_{j=1}^l Y_j]
$$

while from [Kaimonovich–Vershik–Madiman inequality](klm-1.md) one has

$$
\mathbb{H}[-W + \sum_{j=1}^l Y_j] \leq \mathbb{H}[-W] + \sum_{j=1}^l \mathbb{H}[-W + Y_j] - \mathbb{H}[-W].
$$

From [Kaimanovich-Vershik-Madiman inequality](../../entropic-ruzsa-calculus/part-02/kv.md) one has

$$
\mathbb{H}[-W + Y_j] - \mathbb{H}[-W] \leq \mathbb{H}[-X_{f(j)} + Y_j] - \mathbb{H}[-X_{f(j)}].
$$

The claim now follows from [Negation preserves entropy](../../entropic-ruzsa-calculus/part-01/neg-ent.md) and some elementary algebra.

## Lean

Formalized as [`ent_of_sum_le_ent_of_sum`](https://teorth.github.io/pfr/docs/find/#doc/ent_of_sum_le_ent_of_sum).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 112](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L112)
