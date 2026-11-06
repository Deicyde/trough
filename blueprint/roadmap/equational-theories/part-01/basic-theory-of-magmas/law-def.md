---
declaration: definition
origin: cited
lean: Law.MagmaLaw
statement: formalized
---

# Law

Let $X$ be a set. A *law* with alphabet $X$ is a formal expression of the form $w \simeq w'$, where $w, w' \in M_X$ are words with alphabet $X$ (thus one can identify laws with alphabet $X$ with elements of $M_X \times M_X$). A magma $G$ *satisfies* the law $w \simeq w'$ if we have $\varphi_f( w ) = \varphi_f ( w' )$ for all $f: X \to G$, in which case we write $G \models w \simeq w'$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Law.MagmaLaw`](https://teorth.github.io/equational_theories/docs/find/#doc/Law.MagmaLaw).

## Sources

- [Equational Theories blueprint: chapter/intro.tex, line 61](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/intro.tex#L61)
