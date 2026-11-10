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

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 123](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/distance.tex#L123)
