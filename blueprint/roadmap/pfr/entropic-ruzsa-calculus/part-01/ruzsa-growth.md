---
declaration: lemma
origin: cited
lean: diff_ent_le_rdist', diff_ent_le_rdist''
statement: formalized
proof: formalized
---

# Distance controls entropy growth

If $X,Y$ are independent $G$-valued random variables, then

$$
\mathbb{H}[X-Y] - \mathbb{H}[X], \mathbb{H}[X-Y] - \mathbb{H}[Y] \leq 2d[X ;Y].
$$

## Depends on

- [Ruzsa distance](ruz-dist-def.md)

## Proof depends on

- [Independent lower bound on sumset](sumset-lower.md)
- [Negation preserves entropy](neg-ent.md)

## Proof

Immediate from [Independent lower bound on sumset](sumset-lower.md) and [Ruzsa distance](ruz-dist-def.md), and also [Negation preserves entropy](neg-ent.md).

## Lean

Formalized as [`diff_ent_le_rdist'`](https://teorth.github.io/pfr/docs/find/#doc/diff_ent_le_rdist'), [`diff_ent_le_rdist''`](https://teorth.github.io/pfr/docs/find/#doc/diff_ent_le_rdist'').

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 143](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/distance.tex#L143)
