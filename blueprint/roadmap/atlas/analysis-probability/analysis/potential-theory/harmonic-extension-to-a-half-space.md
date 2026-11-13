---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Fourier.HalfSpaceLaplaceDecayEstimateWanted.R2, MathlibExt.Analysis.Fourier.HalfSpaceLaplaceDecayEstimateWanted.R3, MathlibExt.Analysis.Fourier.HalfSpaceLaplaceDecayEstimateWanted.LowerHalfSpace, MathlibExt.Analysis.Fourier.HalfSpaceLaplaceDecayEstimateWanted.OpenLowerHalfSpace, MathlibExt.Analysis.Fourier.HalfSpaceLaplaceDecayEstimateWanted.point3, MathlibExt.Analysis.Fourier.HalfSpaceLaplaceDecayEstimateWanted.exists_abs_le_inv_one_add_abs_of_harmonic_lowerHalfSpace
statement: formalized
---

# Harmonic extension to a half-space

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/harmonic-extension-to-a-half-space/index.html).

## The Euclidean plane

The Euclidean plane $\mathbb{R}^2$ is the space of pairs of real
numbers with the Euclidean inner product and norm.

Formalized by `MathlibExt.Analysis.Fourier.HalfSpaceLaplaceDecayEstimateWanted.R2`, an abbreviation declared in [WantedExt/Analysis/Fourier/HalfSpaceLaplaceDecayEstimateWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Fourier/HalfSpaceLaplaceDecayEstimateWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/harmonic-extension-to-a-half-space/index.html#r2).

## Euclidean three-space

Euclidean three-space $\mathbb{R}^3$ is the space of triples of
real numbers with the Euclidean inner product and norm.

Formalized by `MathlibExt.Analysis.Fourier.HalfSpaceLaplaceDecayEstimateWanted.R3`, an abbreviation declared in [WantedExt/Analysis/Fourier/HalfSpaceLaplaceDecayEstimateWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Fourier/HalfSpaceLaplaceDecayEstimateWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/harmonic-extension-to-a-half-space/index.html#r3).

## Closed lower half-space

The closed lower half-space is the set of points
$(p_1, p_2, p_3)$ of Euclidean three-space $\mathbb{R}^3$ with $p_3 \le 0$.

Formalized by `MathlibExt.Analysis.Fourier.HalfSpaceLaplaceDecayEstimateWanted.LowerHalfSpace`, an abbreviation declared in [WantedExt/Analysis/Fourier/HalfSpaceLaplaceDecayEstimateWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Fourier/HalfSpaceLaplaceDecayEstimateWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/harmonic-extension-to-a-half-space/index.html#lower-half-space).

## Open lower half-space

The open lower half-space is the set of points $(p_1, p_2, p_3)$
of Euclidean three-space $\mathbb{R}^3$ with $p_3 < 0$.

Formalized by `MathlibExt.Analysis.Fourier.HalfSpaceLaplaceDecayEstimateWanted.OpenLowerHalfSpace`, an abbreviation declared in [WantedExt/Analysis/Fourier/HalfSpaceLaplaceDecayEstimateWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Fourier/HalfSpaceLaplaceDecayEstimateWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/harmonic-extension-to-a-half-space/index.html#open-lower-half-space).

## Appending a third coordinate

For a point $x = (x_1, x_2)$ of the Euclidean plane
$\mathbb{R}^2$ and a real number $z$, this is the point $(x_1, x_2, z)$ of Euclidean three-space
$\mathbb{R}^3$.

Formalized by `MathlibExt.Analysis.Fourier.HalfSpaceLaplaceDecayEstimateWanted.point3`, a definition declared in [WantedExt/Analysis/Fourier/HalfSpaceLaplaceDecayEstimateWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Fourier/HalfSpaceLaplaceDecayEstimateWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/harmonic-extension-to-a-half-space/index.html#point3).

## Decay of bounded harmonic extensions of Schwartz data in a half-space

Write a point of
$\mathbb{R}^3$ as $(x, z)$ with $x = (x_1, x_2) \in \mathbb{R}^2$ and $z \in \mathbb{R}$. Let
$\phi : \mathbb{R}^2 \to \mathbb{R}$ be a Schwartz function and let
$u : \mathbb{R}^3 \to \mathbb{R}$ be harmonic at every point of the open lower half-space
$\{(x, z) : z < 0\}$, continuous on the closed lower half-space $\{(x, z) : z \le 0\}$ and bounded
there, with $u(x, 0) = \phi(x)$ for every $x \in \mathbb{R}^2$. Suppose that $u(x, z) \to 0$ as
$z \to -\infty$ uniformly in $x$: for every $\varepsilon > 0$ there is $z_0$ such that
$|u(x, z)| < \varepsilon$ for all $z \le z_0$ and all $x \in \mathbb{R}^2$. Then there is a
constant $C > 0$ such that $|u(x, z)| \le C (1 + |z|)^{-1}$ for all $z \le 0$ and all
$x \in \mathbb{R}^2$.

Boundedness of $u$ is not among the hypotheses of the source problem, but the bound fails without
it: adding to the Poisson extension of $\phi$ the harmonic function $\operatorname{Im} G(x_1 + iz)$
built from Newman's entire function $G$, which vanishes on $z = 0$ and as $z \to -\infty$ but is
unbounded near the boundary, gives a counterexample.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Operator theory; Integral, integro-differential, and pseudodifferential operators), problem `ma_proofbench_l2_72`, with the change above.

Stated but not proved: `MathlibExt.Analysis.Fourier.HalfSpaceLaplaceDecayEstimateWanted.exists_abs_le_inv_one_add_abs_of_harmonic_lowerHalfSpace` is written with `theorem_wanted` in [WantedExt/Analysis/Fourier/HalfSpaceLaplaceDecayEstimateWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Fourier/HalfSpaceLaplaceDecayEstimateWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/harmonic-extension-to-a-half-space/index.html#exists-abs-le-inv-one-add-abs-of-harmoni).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Harmonic extension to a half-space](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/harmonic-extension-to-a-half-space/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/potential-theory/harmonic-extension-to-a-half-space)
