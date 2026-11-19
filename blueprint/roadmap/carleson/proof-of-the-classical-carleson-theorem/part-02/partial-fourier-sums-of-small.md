---
declaration: lemma
origin: cited
lean: control_approximation_effect
statement: formalized
proof: formalized
---

# partial Fourier sums of small

Let $g:{\mathbb{R}}\to{\mathbb{C}}$ be a measurable $2\pi$-periodic function such that for some $\delta>0$ and every $x\in{\mathbb{R}}$,

$$
|g(x)|\le \delta \,.\qquad\text{(41)}
$$

Then for every $\epsilon>0$, there exists a measurable set $E\subset [0,2\pi]$ with $|E|\lt \epsilon$ such that for every $x\in [0,2\pi]\setminus E$ and $N>0$,

$$
|S_N g(x)|\le C_\epsilon \delta,\qquad\text{(42)}
$$

where

$$
C_\epsilon = \left(\frac{8}{\pi\epsilon}\right)^\frac{1}{2} C_{4,2} + \pi \,.\qquad\text{(43)}
$$

## Depends on

- [real Carleson operator measurable](real-carleson-operator-measurable.md)
- [real Carleson](../part-01/real-carleson.md)
- [partial Fourier sum bound](partial-fourier-sum-bound.md)

## Proof

Define

$$
E := \{x \in [0, 2\pi] \ : \ \sup_{N > 0} |S_N g (x)| > C_\epsilon \delta \} \,.
$$

Then (42) clearly holds, and it remains to show that $|E| \le \epsilon$. With [partial Fourier sum bound](partial-fourier-sum-bound.md), we obtain

$$
E \subset \{x\in [0,2\pi] \ : \ C_\epsilon \delta < \frac{1}{2\pi} (Tg(x) + T\bar{g}(x)) + \pi\delta\} \subset E_1 \cup E_2,
$$

where

$$
\begin{aligned}
E_1 :=& \{x\in [0,2\pi] \ : \ \pi(C_\epsilon - \pi) \delta < Tg(x)\} \\
E_2 :=& \{x\in [0,2\pi] \ : \ \pi(C_\epsilon - \pi) \delta < T\bar{g}(x)\}.
\end{aligned}
$$

By [real Carleson operator measurable](real-carleson-operator-measurable.md), $E_1$ and $E_2$ are measurable. Thus,

$$
\pi(C_\epsilon - \pi) \delta |E_1| \le \int_{E_1} Tg(x) \, dx = \delta \int_{E_1} T(\delta^{-1} g\mathbf{1}_{[-\pi,3\pi]})(x) \, dx \,.
$$

Applying [real Carleson](../part-01/real-carleson.md) with $F = [-\pi, 3\pi]$ and $G = E'$, it follows that this is

$$
\le \delta \cdot C_{4,2} |F|^{\frac{1}{2}} |E_1|^{\frac{1}{2}} \le (4\pi)^\frac{1}{2} C_{4,2} \delta \cdot |E'|^{\frac{1}{2}}\,.
$$

Rearranging, we obtain

$$
|E_1| \le \left(\frac{(4\pi)^\frac{1}{2} C_{4,2}}{\pi(C_\epsilon - \pi)}\right)^2 = \frac{\epsilon}{2}\,.
$$

Analogously, we get the same estimate for $|E_2|$. This completes the proof using $|E| \le |E_1| + |E_2|$.

## Lean

Formalized as [`control_approximation_effect`](https://fpvandoorn.github.io/carleson/docs/find/#doc/control_approximation_effect).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 9153](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L9153)
