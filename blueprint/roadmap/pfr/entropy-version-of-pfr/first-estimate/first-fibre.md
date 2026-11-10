---
declaration: lemma
origin: cited
lean: rdist_add_rdist_add_condMutual_eq
statement: formalized
proof: formalized
---

# Fibring identity for first estimate

We have

$$
\begin{aligned}
&   d[X_1+\tilde X_2;X_2+\tilde X_1] + d[X_1|X_1+\tilde X_2; X_2|X_2+\tilde X_1] \\
&\quad + \mathbb{I}[X_1+ X_2 : \tilde X_1 + X_2 \,|\, X_1 + X_2 + \tilde X_1 + \tilde X_2] = 2k.
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Specific fibring identity](../../the-fibring-lemma/cor-fibre.md)

## Proof

Immediate from [Specific fibring identity](../../the-fibring-lemma/cor-fibre.md).

## Lean

Formalized as [`rdist_add_rdist_add_condMutual_eq`](https://teorth.github.io/pfr/docs/find/#doc/rdist_add_rdist_add_condMutual_eq).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy_pfr.tex, line 79](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy_pfr.tex#L79)
