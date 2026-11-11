---
declaration: lemma
origin: cited
lean: condRuzsaDist_of_copy, condRuzsaDist'_of_copy, condRuzsaDist_of_indep, condRuzsaDist'_of_indep
statement: formalized
proof: formalized
---

# Alternate form of distance

The expression $d[X | Z;Y | W]$ is unchanged if $(X,Z)$ or $(Y,W)$ is replaced by a copy. Furthermore, if $(X,Z)$ and $(Y,W)$ are independent, then

$$
d[X  | Z;Y | W] = \mathbb{H}[X-Y|Z,W] - \mathbb{H}[X|Z]/2 - \mathbb{H}[Y|W]/2
$$

and similarly

$$
d[X ;Y | W] = \mathbb{H}[X-Y|W] - \mathbb{H}[X]/2 - \mathbb{H}[Y|W]/2.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Copy preserves entropy](copy-ent.md)
- [Copy preserves Ruzsa distance](ruz-copy.md)
- [Ruzsa distance in independent case](ruz-indep.md)
- [Conditioned Ruzsa distance](cond-dist-def.md)
- [Conditional entropy](../../shannon-entropy-inequalities/part-01/conditional-entropy-def.md)

## Proof

Straightforward thanks to [Copy preserves entropy](copy-ent.md), [Copy preserves Ruzsa distance](ruz-copy.md), [Ruzsa distance in independent case](ruz-indep.md), [Conditioned Ruzsa distance](cond-dist-def.md), [Conditional entropy](../../shannon-entropy-inequalities/part-01/conditional-entropy-def.md).

## Lean

Formalized as [`condRuzsaDist_of_copy`](https://teorth.github.io/pfr/docs/find/#doc/condRuzsaDist_of_copy), [`condRuzsaDist'_of_copy`](https://teorth.github.io/pfr/docs/find/#doc/condRuzsaDist'_of_copy), [`condRuzsaDist_of_indep`](https://teorth.github.io/pfr/docs/find/#doc/condRuzsaDist_of_indep), [`condRuzsaDist'_of_indep`](https://teorth.github.io/pfr/docs/find/#doc/condRuzsaDist'_of_indep).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 231](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/distance.tex#L231)
