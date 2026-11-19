---
declaration: lemma
origin: cited
lean: cotlar_estimate
statement: formalized
proof: formalized
---

# Cotlar estimate

Assume that [(3)](two-sided-metric-space-carleson.md) holds. Let $0\lt r\le R$ and $x\in X$. Let $g:X\to{\mathbb{C}}$ be a bounded measurable function supported on a set of finite measure. Then

$$
|T_Rg(x)| \le 2^{2}M(T_rg)(x)+ 2^{a^3+20a+3} Mg(x)
\, .\qquad\text{(32)}
$$

## Depends on

- [Cotlar control](cotlar-control.md)
- [Cotlar sets](cotlar-sets.md)

## Proof

By [Cotlar sets](cotlar-sets.md), the set of all $x'\in B(x,\frac {R} 4)$ such that at least one of the conditions [(30)](cotlar-sets.md) and [(31)](cotlar-sets.md) is satisfied has measure less than or equal to $\mu(B(x,\frac{R}{4}))/2$ and hence is not all of $B(x,\frac {R} 4)$. Pick an $x'\in B(x,\frac {R} 4)$ such that both conditions are not satisfied. Applying [Cotlar control](cotlar-control.md) for this $x'$ and using the triangle inequality estimates the left-hand side of (32) by

$$
4 M(T_rg)(x) + 2^{a^3 + 20a + 2} Mg(x) + 2^{a^3 + 4a + 1} Mg(x)\, .
$$

This proves the lemma.

## Lean

Formalized as [`cotlar_estimate`](https://fpvandoorn.github.io/carleson/docs/find/#doc/cotlar_estimate).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 7345](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L7345)
