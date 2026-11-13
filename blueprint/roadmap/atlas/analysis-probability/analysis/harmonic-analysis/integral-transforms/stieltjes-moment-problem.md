---
declaration: section
origin: cited
lean: MetaMathlibExt.summable_geometric_means, MetaMathlibExt.StieltjesMomentDeterminate, MetaMathlibExt.carleman_stieltjes_criterion
statement: formalized
proof: formalized
---

# Stieltjes moment problem

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/stieltjes-moment-problem/index.html).

## Carleman's inequality, summability form

If $(a_n)_{n \ge 0}$ is a summable sequence of
nonnegative real numbers, then the sequence of geometric means $(a_0 a_1 \cdots a_n)^{1/(n+1)}$,
$n \ge 0$, is summable.

Formalized by `MetaMathlibExt.summable_geometric_means`, a theorem declared in [MathlibExt/MeasureTheory/Integral/CarlemanStieltjesCriterion.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Integral/CarlemanStieltjesCriterion.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/stieltjes-moment-problem/index.html#summable-geometric-means).

## Stieltjes moment determinacy

A measure $\mu$ on $\mathbb{R}$ is Stieltjes moment
determinate when every probability measure $\nu$ on $\mathbb{R}$ such that $\nu((-\infty, 0)) = 0$,
$\int |x|^k \, d\nu(x) < \infty$ for every integer $k \ge 1$, and
$\int x^k \, d\nu(x) = \int x^k \, d\mu(x)$ for every integer $k \ge 1$ is equal to $\mu$.

The moments of $\mu$ are Bochner integrals, which are $0$ when $x^k$ is not $\mu$-integrable, and
the definition places no condition on $\mu$ itself.

## Sources

- Gwo Dong Lin, "Recent Developments on the Moment Problem", Journal of Statistical Distributions and Applications (2017), DOI 10.1186/s40488-017-0059-2, arXiv:1703.01027v3. Definition lines 57-75, criterion lines 297-321. JIS application, lines 152-177.

Formalized by `MetaMathlibExt.StieltjesMomentDeterminate`, a definition declared in [MathlibExt/MeasureTheory/Integral/CarlemanStieltjesCriterion.lean, line 1420](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Integral/CarlemanStieltjesCriterion.lean#L1420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/stieltjes-moment-problem/index.html#stieltjes-moment-determinate).

## Carleman's criterion for the Stieltjes moment problem

Let $\mu$ be a probability measure
on $\mathbb{R}$ with $\mu((-\infty, 0)) = 0$ such that $\int |x|^k \, d\mu(x) < \infty$ for every
integer $k \ge 1$, and write $m_k = \int x^k \, d\mu(x)$. If
$\sum_{k \ge 1} m_k^{-1/(2k)} = \infty$, where the terms are taken in $[0, \infty]$ (so a term
with $m_k = 0$ equals $\infty$), then $\mu$ is Stieltjes moment determinate.

Proof: Symmetrize through the square-root map, apply Denjoy--Carleman quasi-analytic
uniqueness to the difference of characteristic functions, then push forward by squaring.

## Sources

- Gwo Dong Lin, "Recent Developments on the Moment Problem" (2017), Theorem 2, (s6) implies (s7). Source spans: definition lines 57-75, criterion lines 297-321; JIS application lines 152-177.

Formalized by `MetaMathlibExt.carleman_stieltjes_criterion`, a theorem declared in [MathlibExt/MeasureTheory/Integral/CarlemanStieltjesCriterion.lean, line 1444](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Integral/CarlemanStieltjesCriterion.lean#L1444). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/stieltjes-moment-problem/index.html#carleman-stieltjes-criterion).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stieltjes moment problem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/stieltjes-moment-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/harmonic-analysis/integral-transforms/stieltjes-moment-problem)
