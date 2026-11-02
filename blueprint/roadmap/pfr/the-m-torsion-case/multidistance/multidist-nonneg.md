---
declaration: lemma
origin: cited
lean: multiDist_nonneg
statement: formalized
proof: formalized
---

# Nonnegativity

For any such tuple, we have $D[X_{[m]}] \geq 0$.

## Depends on

- [Multidistance](multidist-def.md)

## Proof depends on

- [Independent lower bound on sumset](../../entropic-ruzsa-calculus/part-01/sumset-lower.md)

## Proof

From [Independent lower bound on sumset](../../entropic-ruzsa-calculus/part-01/sumset-lower.md) one has

$$
\mathbb{H}[\sum_{i =1}^m \tilde X_i] \geq \mathbb{H}[\tilde X_i]
$$

for each $1 \leq i \leq m$. Averaging over $i$, we obtain the claim.

## Lean

Formalized as [`multiDist_nonneg`](https://teorth.github.io/pfr/docs/find/#doc/multiDist_nonneg).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 191](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L191)
