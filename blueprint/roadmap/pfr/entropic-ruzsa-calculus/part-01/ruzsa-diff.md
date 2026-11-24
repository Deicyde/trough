---
declaration: lemma
origin: cited
lean: diff_ent_le_rdist
statement: formalized
proof: formalized
---

# Distance controls entropy difference

If $X,Y$ are $G$-valued random variables, then

$$
|\mathbb{H}[X]-H[Y]| \leq 2 d[X ;Y].
$$

## Depends on

- [Ruzsa distance](ruz-dist-def.md)

## Proof depends on

- [Independent lower bound on sumset](sumset-lower.md)
- [Negation preserves entropy](neg-ent.md)

## Proof

Immediate from [Independent lower bound on sumset](sumset-lower.md) and [Ruzsa distance](ruz-dist-def.md), and also [Negation preserves entropy](neg-ent.md).

## Lean

Formalized as [`diff_ent_le_rdist`](https://teorth.github.io/pfr/docs/find/#doc/diff_ent_le_rdist).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 133](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/distance.tex#L133)
