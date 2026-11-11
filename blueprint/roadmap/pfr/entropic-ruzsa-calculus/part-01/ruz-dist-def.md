---
declaration: definition
origin: cited
lean: rdist_def
statement: formalized
---

# Ruzsa distance

Let $X,Y$ be $G$-valued random variables (not necessarily on the same sample space). The *Ruzsa distance* $d[X ;Y]$ between $X$ and $Y$ is defined to be

$$
d[X ;Y] := \mathbb{H}[X' - Y'] - \mathbb{H}[X']/2 - \mathbb{H}[Y']/2
$$

where $X',Y'$ are (the canonical) independent copies of $X,Y$ from [Existence of independent copies](independent-exist.md).

## Depends on

- [Entropy](../../shannon-entropy-inequalities/part-01/entropy-def.md)
- [Existence of independent copies](independent-exist.md)

## Lean

Formalized as [`rdist_def`](https://teorth.github.io/pfr/docs/find/#doc/rdist_def).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 85](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/distance.tex#L85)
