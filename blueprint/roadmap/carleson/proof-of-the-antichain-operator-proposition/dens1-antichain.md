---
declaration: lemma
origin: cited
lean: dens1_antichain
statement: formalized
proof: formalized
---

# dens1 antichain

Set $p:=4a^4$. We have

$$
\left|\int \overline{g(x)} \sum_{{\mathfrak p} \in \mathfrak{A}} T_{{\mathfrak p}} f(x)\, d\mu(x)\right|\le
2^{117a^3}\operatorname{\operatorname{dens}}_1(\mathfrak{A})^{\frac 1{2p}} \|f\|_2\|g\|_2\,.\qquad\text{(7)}
$$

## Depends on

- [Hardy–Littlewood](../proof-of-metric-space-carleson-overview/hardy-littlewood.md)
- [tile correlation](tile-correlation.md)
- [antichain tile count](antichain-tile-count.md)

## Proof

We write for the expression inside the absolute values on the left-hand side of (7)

$$
\sum_{{\mathfrak p} \in \mathfrak{A}}\iint \overline{g(x)} \mathbf{1}_{E({\mathfrak p})}(x)
{K_{{\mathrm{s}}({\mathfrak p})}(x,y)}e({Q}(x)(y) -
{Q}(x)(x))
f(y)\, d\mu(y)\,d\mu(x)
$$

$$
=\int \sum_{{\mathfrak p} \in \mathfrak{A}} \overline{T_{{\mathfrak p}} ^*g(y)} f(y)\, d\mu(y)
$$

with the adjoint operator

$$
T_{{\mathfrak p}}^*g(y)=\int_{E({\mathfrak p})} \overline{K_{{\mathrm{s}}({\mathfrak p})}(x,y)}e(-{Q}(x)(y)+
{Q}(x)(x))g(x)\, d\mu(x)\, .\qquad\text{(8)}
$$

We have by expanding the square

$$
\int \Big|\sum_{{\mathfrak p}\in \mathfrak{A}}T^*_{{\mathfrak p}}g(y)\Big|^2\, d\mu(y)=
\int \left(\sum_{{\mathfrak p}\in \mathfrak{A}} T^*_{{\mathfrak p}}g(y)\right)
\left(\sum_{{\mathfrak p}'\in \mathfrak{A}}\overline{T^*_{{\mathfrak p}'}g(y)}\right)\, d\mu(y)
$$

$$
\le \sum_{{\mathfrak p}\in \mathfrak{A}} \sum_{{\mathfrak p}'\in \mathfrak{A}}
\Big|\int T^*_{{\mathfrak p}}g(y)\overline{T^*_{{\mathfrak p}'}g(y)}\, d\mu(y)\Big|\,.\qquad\text{(9)}
$$

We split the sum into the terms with ${\mathrm{s}}({\mathfrak p}')\le {\mathrm{s}}({\mathfrak p})$ and ${\mathrm{s}}({\mathfrak p})< {\mathrm{s}}({\mathfrak p}')$. Using the symmetry of each summand, we may switch ${\mathfrak p}$ and ${\mathfrak p}'$ in the second sum. Using further positivity of each summand to replace the condition ${\mathrm{s}}({\mathfrak p}')< {\mathrm{s}}({\mathfrak p})$ by ${\mathrm{s}}({\mathfrak p}')\le {\mathrm{s}}({\mathfrak p})$ in the second sum, we estimate (9) by

$$
\le2 \sum_{{\mathfrak p}\in \mathfrak{A}} \sum_{{\mathfrak p}'\in \mathfrak{A}: {\mathrm{s}}({\mathfrak p}')\le {\mathrm{s}}({\mathfrak p})}
\Big|\int T^*_{{\mathfrak p}}g(y)\overline{T^*_{{\mathfrak p}'}g(y)}\, d\mu(y)\Big|\,.\qquad\text{(10)}
$$

Define for ${\mathfrak p}\in {\mathfrak P}$

$$
B({\mathfrak p}):=B({\mathrm{c}}({\mathfrak p}), 14D^{{\mathrm{s}}({\mathfrak p})})
$$

and define

$$
\mathfrak{A}({\mathfrak p}):=\{{\mathfrak p}'\in\mathfrak{A}: {\mathrm{s}}({\mathfrak p}')\leq {\mathrm{s}}({\mathfrak p}) \land {\mathcal{I}}({\mathfrak p}') \subset B({\mathfrak p})\}.\qquad\text{(11)}
$$

Note that by the squeezing property [(10)](../proof-of-metric-space-carleson-overview/README.md) and the doubling property [(5)](../introduction/README.md) applied $6$ times we have

$$
\mu(B({\mathfrak p}))\le 2^{6a} \mu({\mathcal{I}}({\mathfrak p}))\, .\qquad\text{(12)}
$$

Using [tile correlation](tile-correlation.md) and (12), we estimate (10) by

$$
\le 2^{232a^3+6a+1} \sum_{{\mathfrak p}\in \mathfrak{A}}
\int_{E({\mathfrak p})}|g|(y) h({\mathfrak p})\, d\mu(y)\qquad\text{(13)}
$$

with $h({\mathfrak p})$ defined as

$$
\frac 1{\mu(B({\mathfrak p}))}\int \sum_{{\mathfrak p}'\in \mathfrak{A}({\mathfrak p})}
{(1+d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), {\mathcal{Q}}({\mathfrak p}))^{-1/(2a^2+a^3)}}(\mathbf{1}_{E({\mathfrak p}')}|g|)(y')\, d\mu(y')\,.\qquad\text{(14)}
$$

Note that $p>4$ since $a\ge 4$. Let $p'$ be the dual exponent of $p$, satisfying $1/p+1/p'=1$. We estimate $h({\mathfrak p})$ as defined in (14) with Hölder using $|g|\le \mathbf{1}_G$ and $E({\mathfrak p}')\subset B({\mathfrak p})$ by

$$
\frac{\|g\mathbf{1}_{B({\mathfrak p})}\|_{p'}}{\mu(B({\mathfrak p}))}
\Big\|\sum_{{\mathfrak p}\in\mathfrak{A}({\mathfrak p})}(1+d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), {\mathcal{Q}}({\mathfrak p}'))^{-1/(2a^2+a^3)}\mathbf{1}_{E({\mathfrak p})}\mathbf{1}_G\Big\|_{p}\, .
$$

Then we apply [antichain tile count](antichain-tile-count.md) to estimate this by

$$
\le 2^{5a}
\frac{\|g\mathbf{1}_{B({\mathfrak p})}\|_{p'}}{\mu(B({\mathfrak p}))}
\operatorname{\operatorname{dens}}_1(\mathfrak{A})^{\frac 1p}\mu(B({\mathfrak p}))^{\frac 1p}\,.\qquad\text{(15)}
$$

Let $\mathcal{B}'$ be the collection of all balls $B({\mathfrak p})$ with ${\mathfrak p}\in \mathfrak{A}$. Then for each ${\mathfrak p}\in \mathfrak{A}$ and $x\in B({\mathfrak p})$ we have by definition [(48)](../proof-of-metric-space-carleson-overview/README.md) of $M_{\mathcal{B}',p'}$

$$
\|g\mathbf{1}_{B({\mathfrak p})}\|_{p'}\le
\mu(B({\mathfrak p}))^{\frac 1{p'}} M_{\mathcal{B}',p'}g(x) \, .
$$

Hence we can estimate (15) by

$$
\le
2^{5a}
(M_{\mathcal{B}', p'}g(x))
\operatorname{\operatorname{dens}}_1(\mathfrak{A})^{\frac 1p}\, .\qquad\text{(16)}
$$

With this estimate of $h({\mathfrak p})$, using $E({\mathfrak p})\subset B({\mathfrak p})$ by construction of $B({\mathfrak p})$, we estimate (13) by

$$
\le 2^{232a^3+11a + 1} { \operatorname{\operatorname{dens}}_1(\mathfrak{A})^{\frac 1p}}\sum_{{\mathfrak p}\in \mathfrak{A}}
\int_{E({\mathfrak p})}|g|(y)M_{\mathcal{B}', p'}g(y) \, dy\,.\qquad\text{(17)}
$$

Using [tile disjointness](tile-disjointness.md), the last display is observed to be

$$
\le 2^{232a^3+11a + 1}
{\operatorname{\operatorname{dens}}_1(\mathfrak{A})^{\frac 1p}} \int |g|(y)(M_{\mathcal{B}', p'}g)(y) \, dy\,.\qquad\text{(18)}
$$

Applying Cauchy-Schwarz and using [Hardy–Littlewood](../proof-of-metric-space-carleson-overview/hardy-littlewood.md) and $1\lt p'\lt \frac 32$ estimates the last display by

$$
\le 2^{232a^3+11a + 1} \operatorname{\operatorname{dens}}_1(\mathfrak{A})^{\frac 1p}
\|g\|_2 \|M_{\mathcal{B}', p'} g\|_2
$$

$$
\le 2^{232a^3+12a+3} \operatorname{\operatorname{dens}}_1(\mathfrak{A})^{\frac 1p}\|g\|_2 ^2\,.
$$

Now dens1 antichain follows by applying Cauchy-Schwarz on the left-hand side and using $a\ge 4$.

## Lean

Formalized as [`dens1_antichain`](https://fpvandoorn.github.io/carleson/docs/find/#doc/dens1_antichain).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 3585](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L3585)
