---
declaration: lemma
origin: cited
lean: dens2_antichain
statement: formalized
proof: formalized
---

# dens2 antichain

We have that

$$
\left|\int \overline{g(x)} \sum_{{\mathfrak p} \in \mathfrak{A}} T_{{\mathfrak p}} f(x)\, d\mu(x)\right|\le
2^{103a^3}({q}-1)^{-1} \operatorname{\operatorname{dens}}_2(\mathfrak{A})^{\frac 1{\tilde{q}}-\frac 12} \|f\|_2\|g\|_2\, .\qquad\text{(4)}
$$

## Depends on

- [Hardy–Littlewood](../proof-of-metric-space-carleson-overview/hardy-littlewood.md)
- [maximal bound antichain](maximal-bound-antichain.md)

## Proof

We have $f=\mathbf{1}_Ff$. Using Hölder's inequality, we obtain for each $x\in B'$ and each $B'\in \mathcal{B}$ using $1\lt \tilde{q}\le 2$

$$
\frac 1{\mu(B')}\int_{B'} |f(y)|\, d\mu(y)
$$

$$
\le
\left(\frac 1{\mu(B')}\int_{B'} |f(y)|^{\frac {2{\tilde{q}}}{3\tilde{q}-2}}\, d\mu(y)\right)^{\frac 32-\frac 1{\tilde{q}}}
\left(\frac 1{\mu(B')}\int_{B'} \mathbf{1}_F(y)\, d\mu(y)\right)^{\frac 1{\tilde{q}}-\frac 12}
$$

$$
\le \left(M_{\mathcal{B}} (|f|^{\frac {2{\tilde{q}}}{3{\tilde{q}}-2}})(x)\right)^{\frac 32-\frac 1{\tilde{q}}}
\operatorname{\operatorname{dens}}_2(\mathfrak{A})^{\frac 1{\tilde{q}}-\frac 12}\, .
$$

Taking the maximum over all $B'$ containing $x$, we obtain

$$
M_{\mathcal{B}}|f|\le
M_{\mathcal{B},\frac {2{\tilde{q}}}{3{\tilde{q}}-2} } |f|
\operatorname{\operatorname{dens}}_2(\mathfrak{A})^{\frac 1{\tilde{q}}-\frac 12}\, .\qquad\text{(5)}
$$

We have with [Hardy–Littlewood](../proof-of-metric-space-carleson-overview/hardy-littlewood.md)

$$
\left\|M_{\mathcal{B}, \frac {2{\tilde{q}}}{3{\tilde{q}}-2}} f\right\|_2\le 2^{2a}(3\tilde{q}-2)(2\tilde{q}-2)^{-1}\|f\|_2\, .
$$

Using $1\lt \tilde{q}\le 2$ estimates the last display by

$$
2^{2a+2} (\tilde{q}-1)^{-1} \|f\|_2\, .\qquad\text{(6)}
$$

We obtain with Cauchy-Schwarz and then [maximal bound antichain](maximal-bound-antichain.md)

$$
|\int \overline{g(x)} \sum_{{\mathfrak p} \in \mathfrak{A}} T_{{\mathfrak p}} f(x)\, d\mu(x)|
$$

$$
\le \|g\|_2 \Big\| \sum_{{\mathfrak p} \in \mathfrak{A}} T_{{\mathfrak p}} f \Big\|_2
$$

$$
\le 2^{102a^3}\|g\|_2 \| M_{\mathcal{B}}f \|_2
$$

With (5) and (6) we can estimate the last display by

$$
\le 2^{102a^3+2a+2}(\tilde{q}-1)^{-1} \|g\|_2 \|f\|_2\operatorname{\operatorname{dens}}_2(\mathfrak{A})^{\frac 1{\tilde{q}}-\frac 12}
$$

Using $a\ge 4$ and $(\tilde q - 1)^{-1} = (q+1)/(q-1) \le 3(q-1)^{-1}$ proves the lemma.

## Lean

Formalized as [`dens2_antichain`](https://fpvandoorn.github.io/carleson/docs/find/#doc/dens2_antichain).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 3522](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L3522)
