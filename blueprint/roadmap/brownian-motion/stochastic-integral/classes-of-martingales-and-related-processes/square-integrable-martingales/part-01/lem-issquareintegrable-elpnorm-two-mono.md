---
declaration: lemma
origin: cited
lean: ProbabilityTheory.IsSquareIntegrable.eLpNorm_mono
statement: formalized
proof: formalized
---

# IsSquareIntegrable.eLpNorm_two_mono

For $M$ a square integrable martingale, the function $t \mapsto \Vert M_t \Vert_{L^2}$ is non-decreasing.

## Depends on

- [Square integrable martingales](def-issquareintegrable.md)

## Proof depends on

- [IsSquareIntegrable.submartingale_sq](lem-issquareintegrable-submartingale-sq.md)

## Proof

By Lemma [IsSquareIntegrable.submartingale_sq](lem-issquareintegrable-submartingale-sq.md), $\Vert M_t \Vert^2$ is a submartingale. Thus, for $s \le t$ ,

$$
\begin{aligned}
\Vert M_s \Vert_{L^2}^2
&= \mathbb{E}[\Vert M_s \Vert^2]
\\
&\le \mathbb{E}[\Vert M_t \Vert^2]
\\
&= \Vert M_t \Vert_{L^2}^2
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.IsSquareIntegrable.eLpNorm_mono`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsSquareIntegrable.eLpNorm_mono).

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 235](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L235)
