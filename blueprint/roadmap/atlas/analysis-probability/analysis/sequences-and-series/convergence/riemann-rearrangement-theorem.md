---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Series.RiemannRearrangementWanted.OrderedHasSum, MathlibExt.Analysis.Series.RiemannRearrangementWanted.orderedHasSum_iff, MathlibExt.Analysis.Series.RiemannRearrangementWanted.orderedHasSum_tendsto_zero, MathlibExt.Analysis.Series.RiemannRearrangementWanted.riemann_rearrangement
statement: formalized
proof: formalized
---

# Riemann rearrangement theorem

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/riemann-rearrangement-theorem/index.html).

## Convergence of a series in order

For a sequence $f : \mathbb{N} \to \mathbb{R}$ and
$a \in \mathbb{R}$, the series $\sum_n f(n)$ converges in order to $a$ when its partial sums
$\sum_{n=0}^{N-1} f(n)$ tend to $a$ as $N \to \infty$.

Formalized by `MathlibExt.Analysis.Series.RiemannRearrangementWanted.OrderedHasSum`, a definition declared in [MathlibExt/Analysis/Series/RiemannRearrangement.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Series/RiemannRearrangement.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/riemann-rearrangement-theorem/index.html#ordered-has-sum).

## Convergence in order via partial sums

For a sequence $f : \mathbb{N} \to \mathbb{R}$ and
$a \in \mathbb{R}$, the series $\sum_n f(n)$ converges in order to $a$ if and only if its partial
sums $\sum_{n=0}^{N-1} f(n)$ tend to $a$ as $N \to \infty$.

Formalized by `MathlibExt.Analysis.Series.RiemannRearrangementWanted.orderedHasSum_iff`, a theorem declared in [MathlibExt/Analysis/Series/RiemannRearrangement.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Series/RiemannRearrangement.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/riemann-rearrangement-theorem/index.html#ordered-has-sum-iff).

## Terms of a convergent series tend to zero

If $f : \mathbb{N} \to \mathbb{R}$ and the
series $\sum_n f(n)$ converges in order to some $s \in \mathbb{R}$, then $f(n) \to 0$ as
$n \to \infty$.

Formalized by `MathlibExt.Analysis.Series.RiemannRearrangementWanted.orderedHasSum_tendsto_zero`, a theorem declared in [MathlibExt/Analysis/Series/RiemannRearrangement.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Series/RiemannRearrangement.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/riemann-rearrangement-theorem/index.html#ordered-has-sum-tendsto-zero).

## Riemann rearrangement theorem

Let $f : \mathbb{N} \to \mathbb{R}$ be such that the series
$\sum_n f(n)$ converges in order to some real number, while the series $\sum_n |f(n)|$ is not
summable. Then for every $a \in \mathbb{R}$ there is a permutation $\sigma$ of $\mathbb{N}$ such
that the rearranged series $\sum_n f(\sigma(n))$ converges in order to $a$.

## Sources

- B. Riemann, Über die Darstellbarkeit einer Function durch eine trigonometrische Reihe, Habilitationsschrift (1854; published 1867).

Formalized by `MathlibExt.Analysis.Series.RiemannRearrangementWanted.riemann_rearrangement`, a theorem declared in [MathlibExt/Analysis/Series/RiemannRearrangement.lean, line 1146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Series/RiemannRearrangement.lean#L1146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/riemann-rearrangement-theorem/index.html#riemann-rearrangement).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Riemann rearrangement theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/riemann-rearrangement-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/sequences-and-series/convergence/riemann-rearrangement-theorem)
