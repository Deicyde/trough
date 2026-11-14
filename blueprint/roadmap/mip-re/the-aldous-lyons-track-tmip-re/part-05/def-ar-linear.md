---
declaration: definition
origin: cited
lean: MIPRE.Tailored.AnsRed.Eqn, MIPRE.Tailored.AnsRed.pureEqn, MIPRE.Tailored.AnsRed.Tri, MIPRE.Tailored.AnsRed.triangle, MIPRE.Tailored.AnsRed.ext, MIPRE.Tailored.AnsRed.decInd, MIPRE.Tailored.AnsRed.DecSat
statement: formalized
---

# Purified, triangulated and decoupled systems

An equation over $\mathbb{F}_2$ is a list of variables and a right-hand side. The *purified equation* of a constraint $c$ of the canonical decider at answers $a^R a^L$, $b^R b^L$ (eq:purified\_equation, II:7762) is the equation on the linear answers, placed in a table of $2L$ entries ($a^L$ from $0$, $b^L$ from $L$), whose right-hand side absorbs the readable answers; a constraint of the wrong length becomes $0 = 1$. The *triangulation* of a list of equations (II:7952) replaces $X_{x_0} + \dots + X_{x_{k-1}} = b$ by $X_{x_0} = Y_0$, $Y_{i-1} + X_{x_i} = Y_i$ and $Y_{k-1} = b$, each row with its own fresh variables, and the *extension* of an assignment gives $Y_i$ the partial sum $\sum_{j \le i} X_{x_j}$, a linear map. The *decoupled system* (II:8193) on the blocks $S_A = [\ell_A]$, $S_B = [\ell_B]$ and three copies $S_1, S_2, S_3$ of $[\ell]$ has the equations $X_A = X^1$, $X_B = X^1(\ell_A + \cdot)$, $X^1 = X^2$, $X^2 = X^3$ and each triangulated equation on the three copies; it is given by the indicator of the equations $\varepsilon_A X_A(u_A) + \varepsilon_B X_B(u_B) + \sum_i \varepsilon_i X^i(u_i) = \varepsilon_0$ it contains (II:8128), a block of sign $0$ taking any index.

## Depends on

- [The low-degree code](../../structure-of-the-proof/part-07/def-ld-encoding.md)

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Eqn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Eqn), [`MIPRE.Tailored.AnsRed.pureEqn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.pureEqn), [`MIPRE.Tailored.AnsRed.Tri`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Tri), [`MIPRE.Tailored.AnsRed.triangle`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.triangle), [`MIPRE.Tailored.AnsRed.ext`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.ext), [`MIPRE.Tailored.AnsRed.decInd`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.decInd), [`MIPRE.Tailored.AnsRed.DecSat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.DecSat).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2332](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2332)
