---
declaration: lemma
origin: cited
lean: S_truncation
statement: formalized
proof: formalized
---

# S truncation

Let $F$, $G$ be bounded Borel sets in $X$. Let $f:X\to {\mathbb{C}}$ be a Borel function with $|f|\le 1_F$. Then for all $S\in{\mathbb{Z}}$ we have

$$
\int \mathbf{1}_G(x) \sup_{-S\le s_1\le s_2\le S} |T_{s_1,s_2} f(x)|\, d\mu(x)
\le \frac{2^{442a^3+2}}{(q-1)^6} \mu(G)^{1-\frac{1}{q}} \mu(F)^{\frac{1}{q}},\qquad\text{(7)}
$$

where

$$
T_{s_1,s_2} f(x) = \sum_{s_1\le s \le s_2} \int_X K_s(x,y) f(y) e(Q(x)(y)) \, \mathrm{d}\mu(y).\qquad\text{(8)}
$$

## Depends on

- [Hardy–Littlewood](../proof-of-metric-space-carleson-overview/hardy-littlewood.md)
- [linearized truncation](linearized-truncation.md)

## Proof

*Proof of S truncation.* We reduce S truncation to [linearized truncation](linearized-truncation.md). For each $x$, let $\sigma_1(x)$ be the minimal element $s'\in [-S,S]$ such that

$$
\max_{s'\le s_2\le S} |T_{s',s_2} f(x)| = \max_{-S\le s_1\le s_2\le S} |T_{s_1,s_2} f(x)| =: T_{1,x}.
$$

Similarly, let ${\sigma}_2(x)$ be the minimal element $s''\in [-S,S]$ such that

$$
|T_{\sigma_2(x), s''} f(x)| = T_{1,x}\,.
$$

With these choices, and noting that with the definition of $T_{2, \sigma_1, \sigma_2}$ from [(10)](linearized-truncation.md)

$$
T_{\sigma_1(x),\sigma_2(x)} f(x)=T_{2,\sigma_1,\sigma_2} f(x),
$$

we conclude that the left-hand side of (7) and [(9)](linearized-truncation.md) are equal. Therefore, S truncation follows from [linearized truncation](linearized-truncation.md).

## Lean

Formalized as [`S_truncation`](https://fpvandoorn.github.io/carleson/docs/find/#doc/S_truncation).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 1143](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L1143)
