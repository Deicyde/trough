---
declaration: definition
origin: cited
lean: MIPRE.Tailored.TailoredGame, MIPRE.Tailored.TailoredGame.len, MIPRE.Tailored.TailoredGame.maxLen, MIPRE.Tailored.TailoredGame.Accepts, MIPRE.Tailored.TailoredGame.toGame, MIPRE.Tailored.TailoredGame.valStar, MIPRE.Tailored.TailoredGame.doubled, MIPRE.Tailored.Satisfies, MIPRE.Tailored.rejectConstraint
statement: formalized
---

# Tailored game; II:1243

A *tailored game* on a finite question set $X$ is a distribution $\mu$ on $X \times X$ together with, at each question $x$, a set $S_x = S_x^R \cup S_x^L$, a disjoint union, of $\ell^R(x)$ *readable* and $\ell^L(x)$ *linear* formal variables, and, for each pair of questions $(x, y)$ and each assignment $\gamma^R$ of the readable variables at $x$ and $y$, a finite list $L_{xy}(\gamma^R)$ of vectors over the disjoint union $S_x \cup S_y \cup \{J\}$, the *controlled linear constraints*. The answer at $x$ is an assignment $a \in \mathbb{F}_2^{S_x}$, readable bits first. The *canonical decider* (II:1757–1787) accepts $(a, b)$ at $(x, y)$ when every $c \in L_{xy}(a^R, b^R)$ satisfies $\langle c, (a, b, 1)\rangle = 0$ over $\mathbb{F}_2$, the coordinate $J$ being set to $1$; the empty list accepts every answer pair, and the list $\{J\}$ rejects every one. The tailored game defines a game (Definition [Nonlocal game](../../foundations/part-01/def-game.md)) with answers the bit strings of bounded length, those of the wrong length losing, and its quantum value $\mathrm{val}^*$. Its *doubled* game asks $(\mathsf{false}, x)$ and $(\mathsf{true}, y)$ with the weight of $(x, y)$ and no weight elsewhere; it is again a tailored game.

## Depends on

- [Nonlocal game](../../foundations/part-01/def-game.md)
- [Quantum value](../../foundations/part-01/def-q-value.md)
- [Normal form verifier in the ambient model](../../foundations/part-03/def-normal-verifier.md)

## Lean

Formalized as [`MIPRE.Tailored.TailoredGame`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame), [`MIPRE.Tailored.TailoredGame.len`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.len), [`MIPRE.Tailored.TailoredGame.maxLen`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.maxLen), [`MIPRE.Tailored.TailoredGame.Accepts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.Accepts), [`MIPRE.Tailored.TailoredGame.toGame`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.toGame), [`MIPRE.Tailored.TailoredGame.valStar`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.valStar), [`MIPRE.Tailored.TailoredGame.doubled`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.doubled), [`MIPRE.Tailored.Satisfies`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Satisfies), [`MIPRE.Tailored.rejectConstraint`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.rejectConstraint).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 46](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L46)
