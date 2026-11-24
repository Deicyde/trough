---
declaration: lemma
origin: cited
lean: condMultiDist_eq
statement: formalized
proof: formalized
---

# Alternate form of conditional multidistance

If the $(X_i,Y_i)$ are independent,

$$
D[ X_{[m]} | Y_{[m]}] := \mathbb{H}[\sum_{i=1}^m X_i \big| (Y_j)_{1 \leq j \leq m} ] - \frac{1}{m} \sum_{i=1}^m \mathbb{H}[ X_i | Y_i].\qquad\text{(2)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Conditional entropy](../../shannon-entropy-inequalities/part-01/conditional-entropy-def.md)
- [Multidistance](../multidistance/multidist-def.md)
- [Conditional multidistance](cond-multidist-def.md)

## Proof

This is routine from [Conditional entropy](../../shannon-entropy-inequalities/part-01/conditional-entropy-def.md) and Definitions [Multidistance](../multidistance/multidist-def.md) and [Conditional multidistance](cond-multidist-def.md).

## Lean

Formalized as [`condMultiDist_eq`](https://teorth.github.io/pfr/docs/find/#doc/condMultiDist_eq).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 337](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/torsion.tex#L337)
