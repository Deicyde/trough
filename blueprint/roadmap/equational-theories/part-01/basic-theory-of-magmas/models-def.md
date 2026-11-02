---
declaration: definition
origin: cited
lean: models
statement: formalized
---

# Models

A *theory* is a set $\Gamma$ of laws. Given a theory $\Gamma$, a magma $G$ is a *model* of $\Gamma$ with the (overloaded) notation $G\models\Gamma$ if $G\models w\simeq w'$ for every $w\simeq w'$ in $\Gamma$; we also say that $G$ *satisfies* $\Gamma$. Given a law $E$, we write $\Gamma \models E$ if every magma $G$ that models $\Gamma$, also models $E$.

## Depends on

- [Law](law-def.md)

## Lean

Formalized as [`models`](https://teorth.github.io/equational_theories/docs/find/#doc/models).

## Sources

- [Equational Theories blueprint: chapter/intro.tex, line 82](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/intro.tex#L82)
