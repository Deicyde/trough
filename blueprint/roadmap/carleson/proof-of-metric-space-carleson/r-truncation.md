---
declaration: lemma
origin: cited
lean: R_truncation
statement: formalized
proof: formalized
---

# R truncation

Let $F$, $G$ be Borel sets in $X$. Let $f:X\to {\mathbb{C}}$ be a Borel function with $|f|\le 1_F$. Then for all $R\in 2^{\mathbb{N}}$ we have

$$
\int \mathbf{1}_G \sup_{1/R\lt R_1\lt R_2\lt R} |T_{R_1,R_2,R} f(x)|\, d\mu(x) \le \frac{2^{443a^3}}{(q-1)^6} \mu(G)^{1-\frac{1}{q}} \mu(F)^{\frac{1}{q}},\qquad\text{(1)}
$$

where

$$
T_{R_1,R_2,R} f(x)= \mathbf{1}_{B(o,R)}(x)
\int_{R_1 < \rho(x,y) < R_2} K(x,y) f(y) e(Q(x)(y)) \, \mathrm{d}\mu(y) .\qquad\text{(2)}
$$

## Depends on

- [S truncation](s-truncation.md)

## Proof

Let $F,G,f$ as in the lemma be given. Let $R\in 2^{\mathbb{N}}$ be given. By replacing $G$ with $G\cap B(o,R)$ if necessary, a replacement that does not change the conclusion of the Lemma R truncation, it suffices to show (1) under the assumption that $G$ is contained in $B(o,R)$ and thus bounded. We make this assumption. For every $x\in G$ and $R_2 < R$, the domain of integration in (2) is contained in $B(o,2R)$. By replacing $F$ with $F\cap B(o,2R)$ if necessary, and correspondingly restricting $f$ to $B(o, 2R)$, it suffices to show (1) under the assumption that $F$ is contained in $B(o,2R)$ and thus bounded. We make this assumption.

Using the definition [(5)](../proof-of-metric-space-carleson-overview/README.md) of $K_s$ and the partition of unity [(4)](../proof-of-metric-space-carleson-overview/README.md), we observe that for fixed $R_1\lt R_2$ we have

$$
K(x,y)\mathbf{1}_{R_1\lt \rho(x,y)\lt R_2}=\sum_{s=s_1-2}^{s_2+2} K_s(x,y) \mathbf{1}_{R_1\lt \rho(x,y)\lt R_2},\qquad\text{(3)}
$$

where $s_1=\lfloor\log_D 2R_1\rfloor+3$ and $s_2=\lceil\log_D 4R_2\rceil-2$. To obtain the identity (3), we have used that on the set where $R_1\lt \rho(x,y)\lt R_2$ the kernels $K_s$ vanish unless $s$ is inside the interval of summation in (3). Similarly, we observe

$$
\sum_{s=s_1}^{s_2} K_s(x,y) \mathbf{1}_{R_1\lt \rho(x,y)\lt R_2} = \sum_{s=s_1}^{s_2} K_s(x,y),\qquad\text{(4)}
$$

because on the support of $K_s$ with $s_1\le s\le s_2$ we have necessarily $R_1\lt \rho(x,y)\lt R_2$. We thus express (2) as the sum of

$$
T_{s_1,s_2}f(x):=\sum_{s_1 \le s\le s_2}
\int K_s(x,y) f(y) e(Q(x)(y)) \, \mathrm{d}\mu(y)\qquad\text{(5)}
$$

and

$$
\sum_{s=s_1-2,s_1-1, s_2+1, s_2+2}
\int_{R_1 < \rho(x,y) < R_2} K_s(x,y) f(y) e(Q(x)(y)) \,
\mathrm{d}\mu(y),\qquad\text{(6)}
$$

We apply the triangle inequality and estimate (1) separately with $T_{R_1,R_2,R}$ replaced by (5) and by (6). To handle the case (5), we employ [S truncation](s-truncation.md). Here, we utilize the fact that if $\frac 1R\le R_1\le R_2\le R$, then $s_1$ and $s_2$ as in (5) are in an interval $[-S,S]$ for some sufficiently large $S$ depending on $R$. To handle the case (6), we use the triangle inequality and the properties [(65)](../proof-of-metric-space-carleson-overview/kernel-summand.md), [(66)](../proof-of-metric-space-carleson-overview/kernel-summand.md) of $K_s$ and $|f| \le \mathbf{1}_F$ to obtain for arbitrary $s$ the inequality

$$
\begin{gathered}
\left|\int_{R_1 < \rho(x,y) < R_2} K_s(x,y) f(y) e(Q(x)(y)) \, \mathrm{d}\mu(y)\right|\\
\leq \frac{2^{102 a^3}}{\mu(B(x, D^{s}))}
\int_{B(x, D^s)} \mathbf{1}_F(y) \, \mathrm{d}\mu(y)
\leq 2^{102 a^3} M\mathbf{1}_F(x),
\end{gathered}
$$

where $M\mathbf{1}_F$ is as defined in [Hardy–Littlewood](../proof-of-metric-space-carleson-overview/hardy-littlewood.md). Now the left-hand side of (1), with $T_{R_1,R_2,R}$ replaced by (6), can be estimated using Hölder's inequality and [Hardy–Littlewood](../proof-of-metric-space-carleson-overview/hardy-littlewood.md) by

$$
2^{102a^3+2}\int \mathbf{1}_{G}(x) M\mathbf{1}_F(x)\, d\mu(x)
\le \frac{2^{102a^3+4a+3}q}{q-1}\mu(G)^{1-\frac{1}{q}} \mu(F)^{\frac{1}{q}}\,.
$$

Summing the contributions from (5) and (6) completes the proof.

## Lean

Formalized as [`R_truncation`](https://fpvandoorn.github.io/carleson/docs/find/#doc/R_truncation).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 1078](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L1078)
