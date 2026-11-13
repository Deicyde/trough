---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.LacunarySeriesDiscWanted.f, MathlibExt.Analysis.Complex.LacunarySeriesDiscWanted.differentiableOn_ball_continuousOn_closedBall_lacunary
statement: formalized
---

# Lacunary power series on the unit disc

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/lacunary-power-series-on-the-unit-disc/index.html).

## A lacunary power series

For $z \in \mathbb{C}$, let
$f(z) = \sum_{j=0}^{\infty} 2^{-j} z^{2^j}$, where $f(z)$ is taken to be $0$ when the series is
not summable.

Formalized by `MathlibExt.Analysis.Complex.LacunarySeriesDiscWanted.f`, a definition declared in [WantedExt/Analysis/Complex/LacunarySeriesDiscWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Complex/LacunarySeriesDiscWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/lacunary-power-series-on-the-unit-disc/index.html#f).

## Regularity of a lacunary series on the unit disc

Let $f$ be the lacunary series
$f(z) = \sum_{j=0}^{\infty} 2^{-j} z^{2^j}$. Then $f$ is holomorphic on the open unit disc
$\{z \in \mathbb{C} : |z| < 1\}$ and continuous on its closure, the closed unit disc
$\{z \in \mathbb{C} : |z| \le 1\}$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functions of a complex variable; Series expansions of functions of one complex variable), problem `ma_proofbench_l1_09`.

Stated but not proved: `MathlibExt.Analysis.Complex.LacunarySeriesDiscWanted.differentiableOn_ball_continuousOn_closedBall_lacunary` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/LacunarySeriesDiscWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Complex/LacunarySeriesDiscWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/lacunary-power-series-on-the-unit-disc/index.html#differentiable-on-ball-continuous-on-clo).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lacunary power series on the unit disc](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/lacunary-power-series-on-the-unit-disc/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/analytic-function-spaces/lacunary-power-series-on-the-unit-disc)
