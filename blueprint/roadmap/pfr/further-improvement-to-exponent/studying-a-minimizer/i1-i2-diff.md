---
declaration: lemma
origin: cited
lean: rdist_add_rdist_eq
statement: formalized
proof: formalized
---

# I1-I2-diff

$d[X_1;X_1]+d[X_2;X_2]= 2d[X_1;X_2]+(I_2-I_1)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Fibring identity for first estimate](../../entropy-version-of-pfr/first-estimate/first-fibre.md)
- [Specific fibring identity](../../the-fibring-lemma/cor-fibre.md)

## Proof

Compare [Fibring identity for first estimate](../../entropy-version-of-pfr/first-estimate/first-fibre.md) with the identity obtained from applying [Specific fibring identity](../../the-fibring-lemma/cor-fibre.md) on $(X_1,\tilde X_1, X_2, \tilde X_2)$.

## Lean

Formalized as [`rdist_add_rdist_eq`](https://teorth.github.io/pfr/docs/find/#doc/rdist_add_rdist_eq).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 241](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/further_improvement.tex#L241)
