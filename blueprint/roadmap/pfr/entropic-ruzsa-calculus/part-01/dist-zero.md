---
declaration: lemma
origin: cited
lean: rdist_zero_eq_half_ent
statement: formalized
proof: formalized
---

# Distance from zero

If $X$ is a $G$-valued random variable and $0$ is the random variable taking the value $0$ everywhere then

$$
d[X;0]=\mathbb{H}(X)/2.
$$

## Depends on

- [Ruzsa distance](ruz-dist-def.md)

## Proof

This is an immediate consequence of the definitions and $X-0\equiv X$ and $\mathbb{H}(0)=0$.

## Lean

Formalized as [`rdist_zero_eq_half_ent`](https://teorth.github.io/pfr/docs/find/#doc/rdist_zero_eq_half_ent).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 94](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/distance.tex#L94)
