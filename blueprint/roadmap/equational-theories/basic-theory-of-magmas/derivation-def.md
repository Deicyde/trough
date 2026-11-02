---
declaration: definition
origin: cited
lean: derive
statement: formalized
---

# Derivation

Given a theory $\Gamma$ and a law $w\simeq w'$ over a fixed alphabet $X$, we say that $\Gamma$ *derives* $w\simeq w'$, and write $\Gamma\vdash w\simeq w'$, if the law can be obtained using a finite number of applications of the following rules:

1. if $w\simeq w' \in \Gamma$, then $\Gamma\vdash w\simeq w'$.
2. $\Gamma\vdash w\simeq w$ for any word $w$.
3. if $\Gamma\vdash w\simeq w'$, then $\Gamma\vdash w'\simeq w$.
4. if $\Gamma\vdash w\simeq w'$ and $\Gamma\vdash w'\simeq w''$, then $\Gamma\vdash w\simeq w''$.
5. if $\Gamma\vdash w\simeq w'$, then $\Gamma\vdash \varphi_f(w) \simeq \varphi_f(w')$ for every $f: X \to M_X$.
6. if $\Gamma\vdash w_1\simeq w_2$ and $\Gamma\vdash w_3\simeq w_4$, then $\Gamma\vdash w_1 \diamond w_3\simeq w_2\diamond w_4$.

## Depends on

- [Law](law-def.md)

## Lean

Formalized as [`derive`](https://teorth.github.io/equational_theories/docs/find/#doc/derive).

## Sources

- [Equational Theories blueprint: chapter/intro.tex, line 91](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/intro.tex#L91)
