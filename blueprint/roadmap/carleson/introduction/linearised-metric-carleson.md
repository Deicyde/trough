---
declaration: theorem
origin: cited
lean: linearized_metric_carleson
statement: formalized
proof: formalized
---

# linearised metric Carleson

For all integers $a \ge 4$ and real numbers $1\lt q\le 2$ the following holds. Let $(X,\rho,\mu,a)$ be a doubling metric measure space. Let ${\Theta}$ be a cancellative compatible collection of functions. Let ${Q}:X\to {\Theta}$ be a Borel function with finite range. Let $K$ be a one-sided Calderón–Zygmund kernel on $(X,\rho,\mu,a)$. Assume that for every ${\vartheta}\in {\Theta}$ and every bounded measurable function $g$ on $X$ supported on a set of finite measure we have

$$
\|T_{{Q}}^{\vartheta} g\|_{2} \leq 2^{a^3} \|g\|_2\,,\qquad\text{(22)}
$$

where $T_{{Q}}^{\vartheta}$ is defined in [(20)](README.md). Then for all Borel sets $F$ and $G$ in $X$ and all Borel functions $f:X\to {\mathbb{C}}$ with $|f|\le \mathbf{1}_F$, we have, with $T_{Q}$ defined in [(21)](README.md),

$$
\left|\int_{G} T_{Q} f \, \mathrm{d}\mu\right| \le \frac{2^{443a^3}}{(q-1)^6} \mu(G)^{1-\frac{1}{q}} \mu(F)^{\frac{1}{q}}\, .\qquad\text{(23)}
$$

## Depends on

- [R truncation](../proof-of-metric-space-carleson/r-truncation.md)
- [int continuous](../proof-of-metric-space-carleson/int-continuous.md)

## Proof

*Proof of linearised metric Carleson.* Let Borel sets $F$, $G$ in $X$ with finite measure be given. Let a Borel function $f: X \to \mathbb{C}$ with $f \le \mathbf{1}_F$ be given.

For each $0 < R_1,R_2,R$, we define $T_{R_1,R_2,R}f$ as in [(2)](../proof-of-metric-space-carleson/r-truncation.md). By Lemma [int continuous](../proof-of-metric-space-carleson/int-continuous.md), $T_{R_1,R_2,R}f$ is measurable and bounded, and we clearly have for each $x \in X$

$$
T_Q f(x) = \lim_{n \to \infty} \sup_{2^{-n} < R_1 < R_2 < 2^n} T_{R_1, R_2, 2^n}f(x).
$$

For each $x$ and all $f$, the functions $\sup_{2^{-n} < R_1 < R_2 < 2^n} T_{R_1, R_2, 2^n} f(x)$ are measurable by Lemma [int continuous](../proof-of-metric-space-carleson/int-continuous.md) and form an increasing sequence in $n$. By the monotone convergence theorem, the claimed estimate (23) then follows from Lemma [R truncation](../proof-of-metric-space-carleson/r-truncation.md).

## Lean

Formalized as [`linearized_metric_carleson`](https://fpvandoorn.github.io/carleson/docs/find/#doc/linearized_metric_carleson).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 348](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L348)
