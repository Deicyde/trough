---
declaration: lemma
origin: cited
lean: estimate_x_shift
statement: formalized
proof: formalized
---

# estimate x shift

Let $0\lt r$ and $x\in X$. Let $g:X\to{\mathbb{C}}$ be a bounded measurable function supported on a set of finite measure. Then for all $x'$ with $\rho(x,x')\le r$.

$$
\left| T_r g(x) - T_r g(x') \right|
\le 2^{a^3 + 2a + 2} Mg(x)\, .
$$

## Depends on

- [geometric series estimate](geometric-series-estimate.md)

## Proof

By definition,

$$
\left| T_r g(x) - T_r g(x') \right|
=\left|\int_{r\le\rho(x,y)} K(x,y) g(y) \,d\mu(y)
-\int_{r\le\rho(x',y)}
K(x',y) g(y)\, d\mu(y)
\right| \, .\qquad\text{(14)}
$$

We split the first integral in (14) into the domains $r\le\rho(x,y)<2r$ and $2r\le\rho(x,y)$. The integral over the first domain we estimate by $\eqref{firstxx'}$ below. For the second domain, we observe with $\rho(x,x')\le r$ and the triangle inequality that $r\le\rho(x',y)$. We therefore combine on this domain with the corresponding part of the second integral in (14) and estimate that by $\eqref{secondxx'}$ below. The remaining part of the second integral in (14) we estimate by $\eqref{thirdxx'}$. Overall, we have estimated (14) by

$$
\int_{r\le\rho(x,y)< 2r} |K(x,y)| |g(y)| \,d\mu(y)\qquad\text{(15)}
$$

$$
+  \left|\int_{2r\le\rho(x,y)} (K(x,y)-K(x',y)) g(y) \,d\mu(y)
\right|\qquad\text{(16)}
$$

$$
+\int_{r\le\rho(x',y), r\le\rho(x,y)<2r}
|K(x',y)| |g(y)|\, d\mu(y)\,.\qquad\text{(17)}
$$

Using the bound on $K$ in [(14)](../introduction/README.md) and the doubling condition [(5)](../introduction/README.md), we estimate (15) by

$$
\begin{aligned}
\int_{r\le\rho(x,y)<2r} \frac{2^{a^3}}{V(x,y)} |g(y)| \,d\mu(y)\,
&\le
\frac{2^{a^3}}{\mu(B(x,r))} \int_{r\le\rho(x,y)<2r}
|g(y)| \, d\mu(y)\, \\
&\le
\frac{2^{a^3} \cdot 2^a}{\mu(B(x,2r))} \int_{\rho(x,y)<2r}
|g(y)| \, d\mu(y)\,
.\qquad\text{(18)}\end{aligned}
$$

Using the definition of $Mg$, we estimate (18) by

$$
\le 2^{a^3 + a} {Mg(x)}\, .\qquad\text{(19)}
$$

Similarly, in the domain of (17) we note by the triangle inequality and assumption on $x'$ that $\rho(x',y)<3r$ and thus we estimate (17) by

$$
\frac{2^{a^3}}{\mu(B(x',r))} \int_{\rho(x',y)<4r}
|g(y)| \, d\mu(y)\le 2^{a^3 + 2a} Mg(x)\qquad\text{(20)}
$$

We turn to the remaining term. Using [(1)](README.md), we estimate (16) by

$$
\int_{2r\le\rho(x,y)} \left(\frac{\rho(x,x')}{\rho(x,y)}\right)^{\frac{1}{a}}\frac{2^{a^3}}{V(x,y)} |g(y)| \,d\mu(y)\qquad\text{(21)}
$$

We decompose and estimate (16) with the triangle inequality by

$$
\begin{aligned}
&\sum_{j=1}^\infty  \int_{2^jr\le\rho(x,y)< 2^{j+1}r}
\left(\frac{\rho(x,x')}{\rho(x,y)}\right)^{\frac{1}{a}}\frac{2^{a^3}}{V(x,y)} |g(y)| \,d\mu(y)\, \\
\le&
\sum_{j=1}^\infty \left( 2^{-j} \right)^{\frac{1}{a}} \int_{2^jr\le\rho(x,y)< 2^{j+1}r} \frac{2^{a^3}}{\mu(B(x,2^j r))} |g(y)| \,d\mu(y) \\
\le&
\sum_{j=1}^\infty 2^{-\frac{j}{a}} \frac{2^{a^3 + a}}{\mu(B(x,2^{j+1} r))} \int_{\rho(x,y)<2^{j+1}r}
|g(y)| \, d\mu(y) \\
\le& 2^{a^3 + a} \sum_{j=1}^\infty 2^{-\frac{j}{a}} Mg(x)\,.\qquad\text{(22)}\end{aligned}
$$

Using [geometric series estimate](geometric-series-estimate.md), we estimate (22) by

$$
\le 2^{a^3 + 2a} Mg(x) \,.\qquad\text{(23)}
$$

Summing the estimates for (15), (16), and (17) proves the lemma.

## Lean

Formalized as [`estimate_x_shift`](https://fpvandoorn.github.io/carleson/docs/find/#doc/estimate_x_shift).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 7118](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L7118)
