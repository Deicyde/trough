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

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy_pfr.tex, line 79](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/entropy_pfr.tex#L79)
