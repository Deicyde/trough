---
declaration: lemma
origin: cited
lean: geometric_series_estimate
statement: formalized
proof: formalized
---

# geometric series estimate

For all real numbers $x\ge 4$,

$$
\sum_{n=0}^\infty 2^{-\frac{n}{x}} \le 2^x.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By convexity, for all $0\le\lambda\le1$

$$
2^{\lambda(-\frac{1}{4})} \le \lambda 2^{-\frac{1}{4}} + (1-\lambda)2^0.
$$

For $\lambda:=\frac{4}{x}$, we obtain

$$
2^{-\frac 1 x} \le 1 - (1-2^{-\frac 1 4}) \frac{4}{x}.
$$

We conclude

$$
\sum_{n=0}^\infty 2^{-\frac{n}{x}} = \frac{1}{1-2^{-\frac 1 x}} \le \frac{1}{4(1-2^{-\frac 1 4})} x \le 2^x.
$$

## Lean

Formalized as [`geometric_series_estimate`](https://fpvandoorn.github.io/carleson/docs/find/#doc/geometric_series_estimate).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 7093](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L7093)
