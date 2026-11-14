---
declaration: definition
origin: cited
lean: MIPRE.Game
statement: formalized
---

# Nonlocal game

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] A *two-player one-round game* $\mathfrak{G}$ is a tuple $({\mathcal{X}}, {\mathcal{Y}}, {\mathcal{A}}, {\mathcal{B}}, \mu, D)$ where ${\mathcal{X}}, {\mathcal{Y}}$ are finite question alphabets, ${\mathcal{A}}, {\mathcal{B}}$ are finite answer alphabets, $\mu$ is a probability distribution on ${\mathcal{X}} \times {\mathcal{Y}}$, and $D : {\mathcal{X}} \times {\mathcal{Y}} \times {\mathcal{A}} \times {\mathcal{B}} \to \{0,1\}$ is the decision predicate ($1$ = accept).

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MIPRE.Game`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Game).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 21](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L21)
