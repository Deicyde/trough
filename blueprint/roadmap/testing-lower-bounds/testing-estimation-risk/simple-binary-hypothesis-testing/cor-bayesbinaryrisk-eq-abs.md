---
declaration: corollary
origin: cited
lean: ProbabilityTheory.toReal_bayesBinaryRisk_eq_integral_abs
statement: formalized
proof: formalized
---

# bayesBinaryRisk_eq_abs

$$
\begin{aligned}
\mathcal B_\xi(\mu, \nu) = \frac{1}{2}\left((P \circ \xi)(\mathcal X) -  (P \circ \xi)\left[x \mapsto \left\vert \xi_0\frac{d \mu}{d(P \circ \xi)}(x) - \xi_1\frac{d \nu}{d(P \circ \xi)}(x)\right\vert\right] \right)
\: .
\end{aligned}
$$

## Depends on

- [bayesBinaryRisk](def-bayesbinaryrisk.md)

## Proof depends on

- [bayesBinaryRisk_eq](thm-bayesbinaryrisk-eq.md)

## Proof

Use Theorem [bayesBinaryRisk_eq](thm-bayesbinaryrisk-eq.md) and the equality $\min\{a,b\} = \frac{1}{2}(a + b - \vert a - b \vert)$.

## Lean

Formalized as [`ProbabilityTheory.toReal_bayesBinaryRisk_eq_integral_abs`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.toReal_bayesBinaryRisk_eq_integral_abs).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 778](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L778)
