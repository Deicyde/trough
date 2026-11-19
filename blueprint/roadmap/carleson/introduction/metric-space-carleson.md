---
declaration: theorem
origin: cited
lean: metric_carleson
statement: formalized
proof: formalized
---

# metric space Carleson

For all integers $a \ge 4$ and real numbers $1\lt q\le 2$ the following holds. Let $(X,\rho,\mu,a)$ be a doubling metric measure space. Let ${\Theta}$ be a cancellative compatible collection of functions and let $K$ be a one-sided Calderón–Zygmund kernel on $(X,\rho,\mu,a)$. Assume that for every bounded measurable function $g$ on $X$ supported on a set of finite measure we have

$$
\|T_{*}g\|_{2} \leq 2^{a^3} \|g\|_2\,,\qquad\text{(18)}
$$

where $T_{*}$ is defined in [(16)](README.md). Then for all Borel sets $F$ and $G$ in $X$ and all Borel functions $f:X\to {\mathbb{C}}$ with $|f|\le \mathbf{1}_F$, we have, with $T$ defined in [(17)](README.md),

$$
\left|\int_{G} T f \, \mathrm{d}\mu\right| \leq \frac{2^{443a^3}}{(q-1)^6} \mu(G)^{1-\frac{1}{q}} \mu(F)^{\frac{1}{q}}\, .\qquad\text{(19)}
$$

## Depends on

- [linearised metric Carleson](linearised-metric-carleson.md)
- [int continuous](../proof-of-metric-space-carleson/int-continuous.md)

## Proof

*Proof of metric space Carleson.* Let Borel sets $F$, $G$ in $X$ be given. Let a Borel function $f: X \to \mathbb{C}$ with $f \le \mathbf{1}_F$ be given.

Let ${\Theta}' \subset {\Theta}$ be a countable dense set. By Lemma [int continuous](../proof-of-metric-space-carleson/int-continuous.md) we have

$$
\sup_{{\vartheta}\in{\Theta}} \sup_{0 < R_1 < R_2}\left| \int_{R_1 < \rho(x,y) < R_2} K(x,y) f(y) e({\vartheta}(y)) \, \mathrm{d}\mu(y) \right|
$$

$$
= \sup_{{\vartheta}\in{\Theta}'} \sup_{0 < R_1 < R_2, R_i \in \mathbb{Q}}\left| \int_{R_1 < \rho(x,y) < R_2} K(x,y) f(y) e({\vartheta}(y)) \, \mathrm{d}\mu(y) \right|.
$$

Consider an enumeration of ${\Theta}'$ and let ${\Theta}_n$ be the finite set consisting of the first $n+1$ functions in the enumeration. Then by the monotone convergence theorem

$$
\Big| \int_G Tf \, \mathrm{d}\mu\Big|
$$

$$
= \int_G \sup_{{\vartheta}\in{\Theta}'} \sup_{0 < R_1 < R_2, R_i \in \mathbb{Q}}\left| \int_{R_1 < \rho(x,y) < R_2} K(x,y) f(y) e({\vartheta}(y)) \, \mathrm{d}\mu(y) \right| \, \mathrm{d}\mu(x)
$$

$$
= \lim_{n \to \infty} \int_G \sup_{{\vartheta}\in{\Theta}_n} \sup_{0 < R_1 < R_2, R_i \in \mathbb{Q}}\left| \int_{R_1 < \rho(x,y) < R_2} K(x,y) f(y) e({\vartheta}(y)) \, \mathrm{d}\mu(y) \right| \, \mathrm{d}\mu(x).
$$

For each $n$, let $Q_n(x)$ be the measurable function specifying the maximizer in the supremum in ${\vartheta}$ in the previous line. It is possible to construct such a measurable function of $x$, because the function inside the supremum is measurable in $x$, being a countable supremum of measurable functions, and because ${\Theta}_n$ is finite. (For example one may fix some order on the finite set ${\Theta}_n$ and pick the smallest maximizer with respect to that order. This is a measurable choice function.) Then the previous display becomes

$$
\le \lim_{n \to \infty} \int_G \sup_{0 < R_1 < R_2} \left| \int_{R_1 < \rho(x,y) < R_2} K(x,y) f(y) e(Q_n(x)(y)) \, \mathrm{d}\mu(y) \right| \, \mathrm{d}\mu(x).
$$

$$
= \lim_{n \to \infty} \int_G T_{Q_n} f \, \mathrm{d}\mu.
$$

It remains to verify the assumptions of Theorem [linearised metric Carleson](linearised-metric-carleson.md), which when applied here completes the proof.

The assumptions of Theorem metric space Carleson and Theorem [linearised metric Carleson](linearised-metric-carleson.md) are the same, with the exception of the assumption [(22)](linearised-metric-carleson.md). The assumption [(22)](linearised-metric-carleson.md) however is weaker than the assumption (18) of Theorem metric space Carleson. Indeed, setting for fixed $x, {\vartheta}$ the outer radius $R_2$ in [(16)](README.md) to $\min\{R_2', R_Q({\vartheta}, x')\}$, where $R_2'$ is the outer radius in [(20)](README.md), shows that [(20)](README.md) is smaller than or equal to [(16)](README.md). Thus we can apply Theorem [linearised metric Carleson](linearised-metric-carleson.md), which completes the proof.

## Lean

Formalized as [`metric_carleson`](https://fpvandoorn.github.io/carleson/docs/find/#doc/metric_carleson).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 305](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L305)
