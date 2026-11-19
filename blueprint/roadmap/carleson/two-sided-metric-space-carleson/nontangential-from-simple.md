---
declaration: lemma
origin: cited
lean: nontangential_from_simple
statement: formalized
proof: formalized
---

# nontangential-from-simple

Assume [(3)](two-sided-metric-space-carleson.md) holds. Then, for every bounded measurable function $g : X \to {\mathbb{C}}$ supported on a set of finite measure we have

$$
\|T_*g\|_2\le 2^{3a^3}\|g\|_2.\qquad\text{(7)}
$$

## Depends on

- [simple nontangential operator](simple-nontangential-operator.md)
- [nontangential operator boundary](nontangential-operator-boundary.md)

## Proof

*Proof of nontangential-from-simple.* Fix $g$ as in the Lemma. Applying [simple nontangential operator](simple-nontangential-operator.md) with a sequence of $r$ tending to $0$ and using Lebesgue monotone convergence shows

$$
\|T_*^{0}g\|_2\le 2^{a^3+24a+6}\|g\|_2,\qquad\text{(8)}
$$

where

$$
T_*^{0} g(x):=\sup_{0\lt R}\sup_{x'\in B(x,R)} \left|\int_{X\setminus B(x',R)}
K(x',y) g(y)\, d\mu(y)\right|\, .\qquad\text{(9)}
$$

We now write using [nontangential operator boundary](nontangential-operator-boundary.md) and the triangle inequality,

$$
\begin{alignedat}{3}
T_* g(x)\le&&&\sup_{0\lt R_1\lt R_2}\sup_{x'\in B(x,R_1)} \left|\int_{X\setminus B(x',R_1)}K(x',y) g(y)\, d\mu(y)\right|\qquad\text{(10)}\\
&+&&\sup_{0\lt R_1\lt R_2}\sup_{x'\in B(x,R_1)} \left|\int_{X\setminus B(x',R_2)} K(x',y) g(y)\, d\mu(y)\right|\, .
\end{alignedat}
$$

Noting that the first integral does not depend on $R_2$ and estimating the second summand by the larger supremum over all $x'\in B(x,R_2)$, at which time the integral does not depend on $R_1$, we estimate further

$$
\begin{alignedat}{3}
\le&&&\sup_{0\lt R_1}\sup_{x'\in B(x,R_1)} \left|\int_{X\setminus B(x',R_1)}K(x',y) g(y)\, d\mu(y)\right| \\
&+  &&\sup_{0\lt R_2}\sup_{x'\in B(x,R_2)} \left|\int_{X\setminus B(x',R_2)} K(x',y) g(y)\, d\mu(y)\right|\, .
\end{alignedat}
$$

Applying the triangle inequality on the left-hand side of (7) and applying (8) twice proves (7). This completes the proof of nontangential-from-simple.

## Lean

Formalized as [`nontangential_from_simple`](https://fpvandoorn.github.io/carleson/docs/find/#doc/nontangential_from_simple).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 7027](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L7027)
