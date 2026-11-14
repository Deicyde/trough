---
declaration: lemma
origin: cited
lean: wiggle_order_11_10, wiggle_order_100, wiggle_order_500
statement: formalized
proof: formalized
---

# wiggle order 3

The following implications hold for all ${\mathfrak q}, {\mathfrak q}' \in {\mathfrak P}$:

$$
{\mathfrak q} \le {\mathfrak q}' \ \text{and} \ \lambda \ge 1.1 \implies \lambda {\mathfrak q} \lesssim \lambda {\mathfrak q}'\,,\qquad\text{(39)}
$$

$$
10{\mathfrak q} \lesssim {\mathfrak q}' \ \text{and} \ {\mathcal{I}}({\mathfrak q}) \ne {\mathcal{I}}({\mathfrak q}') \implies 100 {\mathfrak q} \lesssim 100 {\mathfrak q}'\,,\qquad\text{(40)}
$$

$$
2{\mathfrak q} \lesssim {\mathfrak q}' \ \text{and} \ {\mathcal{I}}({\mathfrak q}) \ne {\mathcal{I}}({\mathfrak q}') \implies 4 {\mathfrak q} \lesssim 500 {\mathfrak q}'\,.\qquad\text{(41)}
$$

## Depends on

- [wiggle order 1](wiggle-order-1.md)
- [wiggle order 2](wiggle-order-2.md)

## Proof

(40) and (41) are easy consequences of [wiggle order 1](wiggle-order-1.md), [wiggle order 2](wiggle-order-2.md) and the fact that $a \ge 4$. For (39), if ${\mathcal{I}}({\mathfrak q}) = {\mathcal{I}}({\mathfrak q}')$ then we get ${\mathfrak q} = {\mathfrak q}'$ by [(13)](../../proof-of-metric-space-carleson-overview/README.md) and [(22)](../../proof-of-metric-space-carleson-overview/README.md). If ${\mathcal{I}}({\mathfrak q}) \ne {\mathcal{I}}({\mathfrak q}')$, then from [(22)](../../proof-of-metric-space-carleson-overview/README.md), [(23)](../../proof-of-metric-space-carleson-overview/README.md) and [(15)](../../proof-of-metric-space-carleson-overview/README.md) it follows that ${\mathfrak q} \lesssim 0.2{\mathfrak q}'$, and (39) follows from an easy calculation using [wiggle order 2](wiggle-order-2.md).

## Lean

Formalized as [`wiggle_order_11_10`](https://fpvandoorn.github.io/carleson/docs/find/#doc/wiggle_order_11_10), [`wiggle_order_100`](https://fpvandoorn.github.io/carleson/docs/find/#doc/wiggle_order_100), [`wiggle_order_500`](https://fpvandoorn.github.io/carleson/docs/find/#doc/wiggle_order_500).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2682](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L2682)
