---
declaration: lemma
origin: cited
lean: ProbabilityTheory.DivFunction.convex_taylor_one_right', ProbabilityTheory.DivFunction.convex_taylor_one_left'
statement: formalized
proof: formalized
---

# convex_taylor

(In Lean, this is proved for a `DivFunction` and $x = 1$, by the fundamental theorem of calculus and Tonelli's theorem, without integration by parts.) For $f: \mathbb{R} \to \mathbb{R}$ a convex function and $x,y \in \mathbb{R}$,

$$
\begin{aligned}
f(y) - f(x) - (y - x)f'_+(x) &= \int_{z \in (x,y]} (y - z) \partial \gamma_f & \text{ if } x \le y \: ,
\\
f(y) - f(x) - (y - x)f'_+(x) &= \int_{z \in (y,x]} (z - y) \partial \gamma_f & \text{ if } y \le x \: .
\end{aligned}
$$

## Depends on

- [Curvature measure](def-curvaturemeasure.md)

## Proof

Let $\Lambda$ be the Lebesgue measure and let $x < y$. Since $f$ has right derivative $f'_+$ in $(x,y)$ and $f'_+$ is integrable on that interval,

$$
\begin{aligned}
f(y) - f(x) = \int_{z \in (x, y]} f'_+(z) \partial \Lambda
\: .
\end{aligned}
$$

We now integrate by parts, using Theorem [integration_by_parts](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L599). $\Lambda$ is the measure obtained from the Stieltjes function $z \mapsto z - y$.

$$
\begin{aligned}
\int_{z \in (x, y]} f'_+(z) \partial \Lambda
&= - \int_{z \in (x,y]} (z - y)\partial \gamma_f + f'_+(y)(y - y) - f'_+(x)(x - y)
\\
&= \int_{z \in (x,y]} (y - z)\partial \gamma_f + f'_+(x)(y - x)
\: .
\end{aligned}
$$

Putting the two equalities together, we get the result for $x < y$. The proof for $x > y$ is similar, and for $x = y$ both sides of both equations are zero.

## Lean

Formalized as [`ProbabilityTheory.DivFunction.convex_taylor_one_right'`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.DivFunction.convex_taylor_one_right'), [`ProbabilityTheory.DivFunction.convex_taylor_one_left'`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.DivFunction.convex_taylor_one_left').

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 617](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L617)
