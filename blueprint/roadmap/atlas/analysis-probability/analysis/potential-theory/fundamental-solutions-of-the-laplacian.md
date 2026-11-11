---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Calculus.NormPowTwoSubDimHarmonicWanted.harmonicOnNhd_one_div_norm_pow_sub_two, MathlibExt.Analysis.Complex.LogNormHarmonicPlaneWanted.harmonicOnNhd_log_norm_euclideanSpace_two, MathlibExt.Analysis.Distribution.NewtonPotentialWanted.exists_fundamental_solution_laplacian, MathlibExt.Analysis.Distribution.NewtonPotentialWanted.newton_potential_harmonic
statement: formalized
---

# Fundamental solutions of the Laplacian

4 results, 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/fundamental-solutions-of-the-laplacian/index.html).

## The Newtonian kernel is harmonic away from the origin

Let $m > 2$ be a natural number.
The function $x \mapsto 1/|x|^{m-2}$ on the Euclidean space $\mathbb{R}^m$, where $|x|$ is the
Euclidean norm, is harmonic on $\mathbb{R}^m \setminus \{0\}$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of several variables), problem `ma_proofbench_l1_81`.

Stated but not proved: `MathlibExt.Analysis.Calculus.NormPowTwoSubDimHarmonicWanted.harmonicOnNhd_one_div_norm_pow_sub_two` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/NormPowTwoSubDimHarmonicWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/NormPowTwoSubDimHarmonicWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/fundamental-solutions-of-the-laplacian/index.html#harmonic-on-nhd-one-div-norm-pow-sub-two).

## The logarithm of the norm is harmonic on the punctured plane

The function
$g(x) = \log|x|$, where $|x|$ is the Euclidean norm of $x \in \mathbb{R}^2$, is harmonic on
$\mathbb{R}^2 \setminus \{0\}$: near every point $x \ne 0$ it is twice continuously
differentiable and its Laplacian vanishes.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functions of a complex variable; Geometric function theory), problem `ma_proofbench_l1_50`.

Stated but not proved: `MathlibExt.Analysis.Complex.LogNormHarmonicPlaneWanted.harmonicOnNhd_log_norm_euclideanSpace_two` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/LogNormHarmonicPlaneWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/LogNormHarmonicPlaneWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/fundamental-solutions-of-the-laplacian/index.html#harmonic-on-nhd-log-norm-euclidean-space).

## Fundamental solution of the Laplacian in dimension three

Let $E$ be a real inner product
space of dimension $3$. Then there is a complex-valued tempered distribution $N$ on $E$ such that
$\Delta N = \delta_0$, where $\Delta$ is the Laplacian in the sense of distributions and
$\delta_0$ is the Dirac delta at the origin.

## Sources

- L. Evans, *Partial Differential Equations*, §2.2.

Stated but not proved: `MathlibExt.Analysis.Distribution.NewtonPotentialWanted.exists_fundamental_solution_laplacian` is written with `theorem_wanted` in [WantedExt/Analysis/Distribution/NewtonPotentialWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Distribution/NewtonPotentialWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/fundamental-solutions-of-the-laplacian/index.html#exists-fundamental-solution-laplacian).

## The Newton potential is harmonic away from the origin

Let $E$ be a real inner product space
of dimension $3$, and define $N : E \to \mathbb{R}$ by $N(y) = -1/(4\pi\|y\|)$ for $y \neq 0$ and
$N(0) = 0$. Then the Laplacian of $N$ vanishes at every point $x \neq 0$ of $E$.

## Sources

- L. Evans, *Partial Differential Equations*, §2.2.

Stated but not proved: `MathlibExt.Analysis.Distribution.NewtonPotentialWanted.newton_potential_harmonic` is written with `theorem_wanted` in [WantedExt/Analysis/Distribution/NewtonPotentialWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Distribution/NewtonPotentialWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/fundamental-solutions-of-the-laplacian/index.html#newton-potential-harmonic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fundamental solutions of the Laplacian](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/fundamental-solutions-of-the-laplacian/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/potential-theory/fundamental-solutions-of-the-laplacian)
