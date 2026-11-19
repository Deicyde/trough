---
declaration: lemma
origin: cited
lean: maximal_theorem
statement: formalized
proof: formalized
---

# Maximal theorem

Let $f: X \to {\mathbb{C}}$ be bounded, measurable, supported on a set of finite measure, and let $\alpha > 0$. Then

$$
\mu(\{x\in X : Mf(x) > \alpha\}) \le \frac{2^{2a}}{\alpha} \int |f(y)|\, d\mu(y).\qquad\text{(42)}
$$

## Depends on

- [Hardy–Littlewood](../proof-of-metric-space-carleson-overview/hardy-littlewood.md)

## Proof

By definition, for each $x\in X$ with $Mf(x) > \alpha$, there exists a ball $B_x$ such that $x\in B_x$ and

$$
\alpha \mu(B_x) < \int_{B_x} |f(y)|\, d\mu(y).\qquad\text{(43)}
$$

Since $\{x\in X : Mf(x) > \alpha\}$ is open and $\mu$ is inner regular on open sets, it suffices to show that

$$
\mu(E) \le \frac{2^{2a}}{\alpha} \int |f(y)|\, d\mu(y)
$$

for every compact $E\subset \{x\in X : Mf(x) > \alpha\}$. For such an $E$, by compactness, we can select a finite subcollection $\mathcal{B} \subset \{B_x: x\in E\}$ that covers $E$. By [(50)](../proof-of-metric-space-carleson-overview/hardy-littlewood.md) applied to (43),

$$
\alpha \mu(\bigcup \mathcal{B}) \le 2^{2a} \int |f(y)|\,d\mu(y)
$$

and hence

$$
\mu(E) \le \mu(\bigcup \mathcal{B}) \le \frac{2^{2a}}{\alpha} \int |f(y)|\,d\mu(y).
$$

## Lean

Formalized as [`maximal_theorem`](https://fpvandoorn.github.io/carleson/docs/find/#doc/maximal_theorem).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 7542](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L7542)
