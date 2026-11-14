---
declaration: theorem
origin: cited
lean: two_sided_metric_carleson
statement: formalized
proof: formalized
---

# two-sided metric space Carleson

For all integers $a \ge 4$ and real numbers $1\lt q\le 2$ the following holds. Let $(X,\rho,\mu,a)$ be a doubling metric measure space. Let ${\Theta}$ be a cancellative compatible collection of functions and let $K$ be a two-sided Calderón–Zygmund kernel on $(X,\rho,\mu,a)$. Assume that for every bounded measurable function $g$ on $X$ supported on a set of finite measure and all $r>0$ we have

$$
\|T_r g\|_{2} \leq 2^{a^3} \|g\|_2\,.\qquad\text{(3)}
$$

Then for all Borel sets $F$ and $G$ in $X$ and all Borel functions $f:X\to {\mathbb{C}}$ with $|f|\le \mathbf{1}_F$, we have, with $T$ defined in [(17)](../introduction/README.md),

$$
\left|\int_{G} T f \, \mathrm{d}\mu\right| \leq \frac{2^{474a^3}}{(q-1)^6} \mu(G)^{1-\frac{1}{q}} \mu(F)^{\frac{1}{q}}\, .\qquad\text{(4)}
$$

## Depends on

- [metric space Carleson](../introduction/metric-space-carleson.md)
- [nontangential-from-simple](nontangential-from-simple.md)

## Proof

*Proof of two-sided metric space Carleson.* Let $1\lt q\le 2$ be a real number. Let $\Theta$ be a cancellative compatible collection of functions. By the assumption (3), we can apply [nontangential-from-simple](nontangential-from-simple.md) to obtain for every bounded measurable $g:X\to{\mathbb{C}}$ supported on a set of finite measure,

$$
\|T_*g\|_2\le 2^{3a^3}\|g\|_2.\qquad\text{(5)}
$$

Define

$$
K'(x,y):= 2^{-2a^3} K(x,y) \,.
$$

Then $K'$ is a two-sided Calderón–Zygmund kernel on $(X,\rho,\mu,a)$. Denote the corresponding maximally truncated non-tangential singular operator by $T_*'$ and the corresponding generalized Carleson operator by $T'$. With (5), we obtain for $g$ as above,

$$
\|T_*'g\|_2\le 2^{a^3}\|g\|_2.\qquad\text{(6)}
$$

Applying [metric space Carleson](../introduction/metric-space-carleson.md) for $K'$ yields that for all Borel sets $F$ and $G$ in $X$ and all Borel functions $f:X\to {\mathbb{C}}$ with $|f|\le \mathbf{1}_F$, we have

$$
\left|\int_{G} T' f \, \mathrm{d}\mu\right| \leq \frac{2^{450a^3}}{(q-1)^6} \mu(G)^{1-\frac{1}{q}} \mu(F)^{\frac{1}{q}}\, .
$$

This finishes the proof since for all $x\in X$,

$$
T'f(x) = 2^{-2a^3} Tf(x) \,.
$$

## Lean

Formalized as [`two_sided_metric_carleson`](https://fpvandoorn.github.io/carleson/docs/find/#doc/two_sided_metric_carleson).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 7003](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L7003)
