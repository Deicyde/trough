---
declaration: definition
origin: cited
lean: MIPRE.Tailored.AnsRed.PcpDims, MIPRE.Tailored.AnsRed.Pcp, MIPRE.Tailored.AnsRed.AssignCheck, MIPRE.Tailored.AnsRed.FormulaCheck, MIPRE.Tailored.AnsRed.SystemCheck, MIPRE.Tailored.AnsRed.Pcp.Passes, MIPRE.Tailored.AnsRed.Pcp.Identities, MIPRE.Tailored.AnsRed.Pcp.IndDeg
statement: formalized
---

# The PCP and its thirteen checks

Let $\ell, \delta, r, s$ be the exponents of the table size and of the copy size, the width of the witness indices and the number of gates, let $|S_0| = 2\ell + 3\delta + 6$, and let $m = 2(\ell + 1) + (|S_0| + 1) + 3r + 6 + s$. A *PCP* over a field $\mathbb{F}$ consists of eleven *assignments*, polynomials $g_A, g_B$ on $\ell$ variables, $g_O$ on $|S_0|$ and three $g_{W,k}$ on $r$ (readable), $g_{La}, g_{Lb}$ on $\ell$ and three $g_{L,k}$ on $\delta$ (linear), and of *helpers*: $\alpha^R_X$ on the $m$ variables, $\alpha^L_X$ on $|S_0|$, and for each assignment a $\beta_X$ on its variables. At a point $p \in \mathbb{F}^m$, for the circuit polynomial $T$, it passes the *formula check* when

$$
T(p) \bigl(p_{\pi_A} g_A(p_A) - p_{\varepsilon_A}\bigr)
\bigl(p_{\pi_B} g_B(p_B) - p_{\varepsilon_B}\bigr)
\bigl(p_{\pi_C} g_O(p_O) - p_{\varepsilon_C}\bigr)
\prod_{k} \bigl(g_{W,k}(p_{W,k}) - p_{\varepsilon_{W,k}}\bigr)
= \sum_X p_X (1 - p_X)\, \alpha^R_X(p),
$$

the *system check* when, at $x = p_O$,

$$
g_O(x) \Bigl(x_{\varepsilon_A} g_{La}(x_A) + x_{\varepsilon_B} g_{Lb}(x_B)
+ \sum_k x_{\varepsilon_k} g_{L,k}(x_k) - x_{\varepsilon_0}\Bigr)
= \sum_X x_X (1 - x_X)\, \alpha^L_X(x),
$$

and the *assignment check* of each assignment $g$ when $g(1 - g) = \sum_X x_X (1 - x_X)\, \beta_X$ at the point $x$ of its block. It satisfies the checks *identically* when each holds at every point of its own space, and it has *degree* $d$ when all its polynomials have individual degree at most $d$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.PcpDims`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.PcpDims), [`MIPRE.Tailored.AnsRed.Pcp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Pcp), [`MIPRE.Tailored.AnsRed.AssignCheck`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.AssignCheck), [`MIPRE.Tailored.AnsRed.FormulaCheck`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.FormulaCheck), [`MIPRE.Tailored.AnsRed.SystemCheck`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.SystemCheck), [`MIPRE.Tailored.AnsRed.Pcp.Passes`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Pcp.Passes), [`MIPRE.Tailored.AnsRed.Pcp.Identities`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Pcp.Identities), [`MIPRE.Tailored.AnsRed.Pcp.IndDeg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Pcp.IndDeg).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2585](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2585)
