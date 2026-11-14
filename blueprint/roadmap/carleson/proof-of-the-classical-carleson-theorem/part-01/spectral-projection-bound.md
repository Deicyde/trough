---
declaration: lemma
origin: cited
lean: spectral_projection_bound
statement: formalized
proof: formalized
---

# spectral projection bound

Let $f$ be a bounded $2\pi$-periodic measurable function. Then, for all $N\ge 0$

$$
\|S_Nf\|_{L^2[0, 2\pi]} \le \|f\|_{L^2[0, 2\pi]}.\qquad\text{(17)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

*Proof of spectral projection bound.* The functions $e_n:x\mapsto e^{inx}$ form an orthonormal basis in $L^2[-\pi, \pi]$ (this is already in Mathlib). Therefore we have

$$
\begin{aligned}
\|S_Nf\|^2_{L^2[-\pi, \pi]}
&= \|\sum_{n=-N}^N \langle\widehat{f}_n, e_n\rangle_{L^2[-\pi, \pi]}\|^2_{L^2[-\pi, \pi]} \\
&= \sum_{n=-N}^N |\widehat{f}_n| \\
&\le \sum_{n\in \mathbb{Z}} |\widehat{f}_n| \\
&= \|f\|_{L^2[-\pi, \pi]}.
\end{aligned}
$$

This completes the proof of the lemma.

## Lean

Formalized as [`spectral_projection_bound`](https://fpvandoorn.github.io/carleson/docs/find/#doc/spectral_projection_bound).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8417](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L8417)
