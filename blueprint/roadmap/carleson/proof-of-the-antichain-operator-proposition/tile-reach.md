---
declaration: lemma
origin: cited
lean: Antichain.tile_reach
statement: formalized
proof: formalized
---

# tile reach

Let ${\vartheta}\in {\Theta}$ and $N\ge0$ be an integer. Let ${\mathfrak p}, {\mathfrak p}'\in {\mathfrak P}$ with

$$
d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), {\vartheta}))\le 2^N\,\qquad\text{(41)}
$$

$$
d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), {\vartheta}))\le 2^N\, .\qquad\text{(42)}
$$

Assume ${\mathcal{I}}({\mathfrak p})\subset {\mathcal{I}}({\mathfrak p}')$ and ${\mathrm{s}}({\mathfrak p})<{\mathrm{s}}({\mathfrak p}')$. Then

$$
2^{N+2}{\mathfrak p}\lesssim 2^{N+2} {\mathfrak p}'\, .\qquad\text{(43)}
$$

## Depends on

- [monotone cube metrics](../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md)

## Proof

By [monotone cube metrics](../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md), we have

$$
d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}'),{\vartheta})
\le d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'),{\vartheta})
\le 2^{N} \, .
$$

Together with (41) and the triangle inequality, we obtain

$$
d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}'),{\mathcal{Q}}({\mathfrak p}))\le 2^{N+1} \, .\qquad\text{(44)}
$$

Now assume

$$
{\vartheta}'\in B_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'),2^{N+2}).
$$

By the doubling property [(8)](../introduction/README.md), applied five times, we have

$$
d_{B({\mathrm{c}}({\mathfrak p}'),8D^{{\mathrm{s}}({\mathfrak p}')})}({\mathcal{Q}}({\mathfrak p}'),{\vartheta}') < 2^{5a+N+2}\, .\qquad\text{(45)}
$$

We have by the squeezing property [(10)](../proof-of-metric-space-carleson-overview/README.md)

$$
{\mathrm{c}}({\mathfrak p})\in
B({\mathrm{c}}({\mathfrak p}'),4D^{{\mathrm{s}}({\mathfrak p}')})\, .
$$

Hence by the triangle inequality

$$
B({\mathrm{c}}({\mathfrak p}), 4D^{{\mathrm{s}}({\mathfrak p}')})
\subseteq
B({\mathrm{c}}({\mathfrak p}'),8D^{{\mathrm{s}}({\mathfrak p}')})\, .
$$

Together with (45) and monotonicity [(9)](../introduction/README.md) of $d$

$$
d_{B({\mathrm{c}}({\mathfrak p}),4D^{{\mathrm{s}}({\mathfrak p}')})}({\mathcal{Q}}({\mathfrak p}'),{\vartheta}') < 2^{5a+N+2}\, .
$$

Using the doubling property [(10)](../introduction/README.md) $5a+2$ times gives

$$
d_{B({\mathrm{c}}({\mathfrak p}),2^{2-5a^2-2a}D^{{\mathrm{s}}({\mathfrak p}')})}({\mathcal{Q}}({\mathfrak p}'),{\vartheta}') < 2^{N}\, .
$$

Using ${\mathrm{s}}({\mathfrak p})<{\mathrm{s}}({\mathfrak p}')$ and $D=2^{100a^2}$ and $a\ge 4$ gives

$$
d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}'),{\vartheta}') < 2^{N}\, .
$$

With the triangle inequality and (44),

$$
d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}),{\vartheta}') < 2^{N+2}\, .
$$

This shows

$$
B_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'),2^{N+2})\subset B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}),2^{N+2})\, .
$$

This implies (43) and completes the proof of the lemma.

## Lean

Formalized as [`Antichain.tile_reach`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Antichain.tile_reach).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 4016](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L4016)
