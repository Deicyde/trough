---
declaration: definition
origin: cited
lean: MIPRE.NCPoly, MIPRE.NCPoly.eval, MIPRE.NCPoly.relSpan, MIPRE.NCPoly.qmod, MIPRE.Tsirelson.Gen, MIPRE.Tsirelson.rels, MIPRE.Tsirelson.cone, MIPRE.Tsirelson.gamePoly, MIPRE.Tsirelson.IsConeState
statement: formalized
---

# The measurement algebra and its cone

Let $P$ be the complex polynomials in noncommuting variables $e_{xa}$ ($x \in {\mathcal{X}}$, $a \in {\mathcal{A}}$) and $f_{yb}$ ($y \in {\mathcal{Y}}$, $b \in {\mathcal{B}}$), with the involution that conjugates coefficients, reverses words and fixes the variables. The *relations* are $\sum_a e_{xa} - 1$, $\sum_b f_{yb} - 1$ and $e_{xa} f_{yb} - f_{yb} e_{xa}$; $I$ is the complex span of $u \rho v$ over relations $\rho$ and $u, v \in P$. The *cone* $M$ is the set of finite nonnegative real combinations of the elements $s^* s$, $s^* e_{xa} s$, $s^* f_{yb} s$ ($s \in P$), of the elements of $I$, and of the anti-hermitian elements of $P$. The game polynomial of $\mathfrak{G}$ is $W_\mathfrak{G} = \sum_{x,y,a,b} \mu(x,y) D(x,y,a,b)\, e_{xa} f_{yb}$. A *cone state* is a complex-linear $L : P \to \mathbb{C}$ with $L(1) = 1$ and $\mathrm{Re}\, L(m) \geq 0$ for every $m \in M$.

## Depends on

- [Nonlocal game](../../foundations/part-01/def-game.md)

## Lean

Formalized as [`MIPRE.NCPoly`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.NCPoly), [`MIPRE.NCPoly.eval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.NCPoly.eval), [`MIPRE.NCPoly.relSpan`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.NCPoly.relSpan), [`MIPRE.NCPoly.qmod`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.NCPoly.qmod), [`MIPRE.Tsirelson.Gen`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.Gen), [`MIPRE.Tsirelson.rels`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.rels), [`MIPRE.Tsirelson.cone`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.cone), [`MIPRE.Tsirelson.gamePoly`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.gamePoly), [`MIPRE.Tsirelson.IsConeState`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.IsConeState).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 151](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L151)
