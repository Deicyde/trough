---
declaration: lemma
origin: cited
lean: mutual_of_W_Z_two_le
statement: formalized
proof: formalized
---

# Mutual information bound

We have $\mathbb{I}[W : Z_2] \leq 2 (m-1) k$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Alternative formulae for mutual information](../../shannon-entropy-inequalities/part-01/alternative-mutual.md)
- [Entropy of $W$](ent-w.md)

## Proof

From [Alternative formulae for mutual information](../../shannon-entropy-inequalities/part-01/alternative-mutual.md) we have $\mathbb{I}[W : Z_2] = \mathbb{H}[W] - \mathbb{H}[W | Z_2]$, and since $Z_2 = \sum_{j=1}^{m-1} j Q_j$ and $W = \sum_{j=1}^m Q_j$,

$$
\mathbb{H}[W | Z_2] \geq \mathbb{H}[W \,|\, Q_1,\dots,Q_{m-1}] = \mathbb{H}[Q_m] = \mathbb{H}[S].
$$

Hence, by [Entropy of $W$](ent-w.md),

$$
\mathbb{I}[W : Z_2] \leq \mathbb{H}[W] - \mathbb{H}[S] \leq 2 (m-1) k,
$$

as claimed.

## Lean

Formalized as [`mutual_of_W_Z_two_le`](https://teorth.github.io/pfr/docs/find/#doc/mutual_of_W_Z_two_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 735](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L735)
