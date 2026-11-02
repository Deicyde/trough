---
declaration: definition
origin: cited
lean: condRuzsaDist
statement: formalized
---

# Conditioned Ruzsa distance

If $(X, Z)$ and $(Y, W)$ are random variables (where $X$ and $Y$ are $G$-valued) we define

$$
d[X  | Z; Y | W] := \sum_{z,w}  \mathbb{P}[Z=z]  \mathbb{P}[W=w] d[(X|Z=z); (Y|(W=w))].
$$

similarly

$$
d[X ; Y | W] := \sum_{w}  \mathbb{P}[W=w] d[X ; (Y|(W=w))].
$$

## Depends on

- [Ruzsa distance](ruz-dist-def.md)

## Lean

Formalized as [`condRuzsaDist`](https://teorth.github.io/pfr/docs/find/#doc/condRuzsaDist).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 222](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/distance.tex#L222)
