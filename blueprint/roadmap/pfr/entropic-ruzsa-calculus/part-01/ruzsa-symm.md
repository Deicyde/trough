---
declaration: lemma
origin: cited
lean: rdist_symm
statement: formalized
proof: formalized
---

# Distance symmetric

If $X,Y$ are $G$-valued random variables, then

$$
d[X ;Y] = d[Y;X].
$$

## Depends on

- [Ruzsa distance](ruz-dist-def.md)

## Proof depends on

- [Negation preserves entropy](neg-ent.md)

## Proof

Immediate from [Negation preserves entropy](neg-ent.md) and [Ruzsa distance](ruz-dist-def.md).

## Lean

Formalized as [`rdist_symm`](https://teorth.github.io/pfr/docs/find/#doc/rdist_symm).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 123](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/distance.tex#L123)
