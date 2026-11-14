---
declaration: definition
origin: cited
lean: DirichletCharacter
statement: formalized
---

# dirichlet-character

A *Dirichlet character* modulo $N$ with values in a commutative ring $R$ is a multiplicative character of $(\mathbb{Z}/N\mathbb{Z})^\times$ with values in $R^\times$, extended by zero to all of $\mathbb{Z}/N\mathbb{Z}$. A character $\chi$ modulo $N > 1$ is *even* if $\chi(-1) = 1$ and *odd* if $\chi(-1) = -1$. In this chapter the modulus is the odd prime $p$, in which case every nontrivial character is primitive and exactly $(p-1)/2$ of the characters are odd.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`DirichletCharacter`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/DirichletCharacter).

## Sources

- [Kummer's criterion blueprint: subsections/hminus-formula.tex, line 15](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/hminus-formula.tex#L15)
