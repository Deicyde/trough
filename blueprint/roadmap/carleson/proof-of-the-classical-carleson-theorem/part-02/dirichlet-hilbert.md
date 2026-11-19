---
declaration: lemma
origin: cited
lean: Dirichlet_Hilbert_diff
statement: formalized
proof: formalized
---

# Dirichlet kernel - Hilbert kernel relation

For all $N\in{\mathbb{Z}}$ and $x\in [-\pi,\pi] \setminus \{0\}$,

$$
\left|K_N(x) - (e^{-iNx}\kappa(x) + \overline{e^{-iNx}\kappa(x)})\right| \le \pi \,.
$$

## Depends on

- [Dirichlet kernel](../part-01/dirichlet-kernel.md)
- [lower secant bound](../part-01/lower-secant-bound.md)

## Proof

Let $N\in{\mathbb{Z}}$ and $x\in [-\pi,\pi] \setminus \{0\}$. With [Dirichlet kernel](../part-01/dirichlet-kernel.md), we obtain

$$
K_N(x) - (e^{-iNx}\kappa(x) + \overline{e^{-iNx}\kappa(x)})
= e^{-iNx} \frac{\min(|x|, 1) }{1 - e^{ix}} + e^{iNx} \frac{\min(|x|, 1) }{1 - e^{-ix}} \,.
$$

Using [lower secant bound](../part-01/lower-secant-bound.md) with $\eta = \min(|x|, 1)$, we bound

$$
\left|K_N(x) - (e^{-iNx}\kappa(x) + \overline{e^{-iNx}\kappa(x)})\right|
\le \frac{\min(|x|, 1) }{|1 - e^{ix}|} + \frac{\min(|x|, 1)}{|1 - e^{-ix}|}
\le \frac{\pi}{2} + \frac{\pi}{2} = \pi \,.
$$

## Lean

Formalized as [`Dirichlet_Hilbert_diff`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Dirichlet_Hilbert_diff).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 9031](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L9031)
