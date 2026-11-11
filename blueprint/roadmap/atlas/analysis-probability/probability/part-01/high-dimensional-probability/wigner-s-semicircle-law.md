---
declaration: section
origin: cited
lean: MathlibExt.Analysis.WignerSemicircleWanted.Analysis.WignerSemicircleProblem.empiricalSpectralMeasureHerm, MathlibExt.Analysis.WignerSemicircleWanted.Analysis.WignerSemicircleProblem.semicircleLaw, MathlibExt.Analysis.WignerSemicircleWanted.Analysis.WignerSemicircleProblem.wignerMatrix, MathlibExt.Analysis.WignerSemicircleWanted.Analysis.WignerSemicircleProblem.wignerMatrix_isHermitian, MathlibExt.Analysis.WignerSemicircleWanted.Analysis.WignerSemicircleProblem.wigner_semicircle
statement: formalized
---

# Wigner's semicircle law

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/wigner-s-semicircle-law/index.html).

## Empirical spectral measure of a Hermitian matrix

Let $W$ be a Hermitian $n \times n$
complex matrix with real eigenvalues $\lambda_1, \dots, \lambda_n$, listed with multiplicity. The
empirical spectral measure of $W$ is the measure $\frac{1}{n} \sum_{j=1}^{n} \delta_{\lambda_j}$
on $\mathbb{R}$, where $\delta_\lambda$ is the Dirac measure at $\lambda$; for $n = 0$ it is the
zero measure.

Formalized by `MathlibExt.Analysis.WignerSemicircleWanted.Analysis.WignerSemicircleProblem.empiricalSpectralMeasureHerm`, a definition declared in [WantedExt/Analysis/WignerSemicircleWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/WignerSemicircleWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/wigner-s-semicircle-law/index.html#empirical-spectral-measure-herm).

## Semicircle distribution

The semicircle distribution is the measure $\sigma$ on
$\mathbb{R}$ given by $\sigma(A) = \int_{A \cap [-2, 2]} \frac{\sqrt{4 - x^2}}{2\pi} \, dx$ for
every measurable set $A \subseteq \mathbb{R}$.

Since $\int_{-2}^{2} \sqrt{4 - x^2} \, dx = 2\pi$, it is a probability measure.

Formalized by `MathlibExt.Analysis.WignerSemicircleWanted.Analysis.WignerSemicircleProblem.semicircleLaw`, a definition declared in [WantedExt/Analysis/WignerSemicircleWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/WignerSemicircleWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/wigner-s-semicircle-law/index.html#semicircle-law).

## Wigner matrix

Let $X_{ij} : \Omega \to \mathbb{R}$, for $i, j \in \mathbb{N}$, be real
functions on a set $\Omega$. For $n \in \mathbb{N}$ and $\omega \in \Omega$, the Wigner matrix
$W_n(\omega)$ is the $n \times n$ complex matrix, with rows and columns indexed by
$\{0, \dots, n - 1\}$, whose entry at $(i, j)$ is the real number
$X_{\min(i, j)\, \max(i, j)}(\omega)$. Only the $X_{ij}$ with $i \le j$ are used, and the matrix
is real symmetric.

Formalized by `MathlibExt.Analysis.WignerSemicircleWanted.Analysis.WignerSemicircleProblem.wignerMatrix`, a definition declared in [WantedExt/Analysis/WignerSemicircleWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/WignerSemicircleWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/wigner-s-semicircle-law/index.html#wigner-matrix).

## Wigner matrices are Hermitian

For every family of real functions
$X_{ij} : \Omega \to \mathbb{R}$, $i, j \in \mathbb{N}$, on a set $\Omega$, every $n \in \mathbb{N}$
and every $\omega \in \Omega$, the Wigner matrix $W_n(\omega)$ is Hermitian.

The matrix is in fact real symmetric: its entry at $(i, j)$ is the real number
$X_{\min(i, j)\, \max(i, j)}(\omega)$, and $\min$ and $\max$ are symmetric in their arguments.

Formalized by `MathlibExt.Analysis.WignerSemicircleWanted.Analysis.WignerSemicircleProblem.wignerMatrix_isHermitian`, a lemma declared in [WantedExt/Analysis/WignerSemicircleWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/WignerSemicircleWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/wigner-s-semicircle-law/index.html#wigner-matrix-is-hermitian).

## Wigner's semicircle law

Let $(\Omega, \mu)$ be a probability space and let
$X_{ij} : \Omega \to \mathbb{R}$, for $i, j \in \mathbb{N}$, be measurable functions. Suppose that
the family $(X_{ij})_{i \le j}$ is mutually independent, that all $X_{ij}$ with $i \le j$ have the
same distribution, and that for $i \le j$ both $X_{ij}$ and $X_{ij}^2$ are integrable with
$\mathbb{E}[X_{ij}] = 0$ and $\mathbb{E}[X_{ij}^2] = 1$. For $n \in \mathbb{N}$ and
$\omega \in \Omega$, let $W_n(\omega)$ be the Wigner matrix of $X$ and let $L_n(\omega)$ be the
image of its empirical spectral measure under $x \mapsto x / \sqrt{n}$ (for $n \ge 1$, the
empirical spectral measure of $W_n(\omega) / \sqrt{n}$). Then for $\mu$-almost every $\omega$,
every bounded continuous function $f : \mathbb{R} \to \mathbb{R}$ satisfies

$$\int f \, dL_n(\omega) \to \int f \, d\sigma \quad (n \to \infty),$$

where $\sigma$ is the semicircle distribution.

## Sources

- E. Wigner, 'Characteristic vectors of bordered matrices with infinite dimensions', Ann. of Math. (2) 62 (1955) 548–564 (Gaussian case). Pastur's universality extending to all variances with finite second moments: L. Pastur, 'On the spectrum of random matrices', Teor. Mat. Fiz. 10 (1972) 102–112. Listed as §102 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `wigner_semicircle` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.WignerSemicircleWanted.Analysis.WignerSemicircleProblem.wigner_semicircle` is written with `theorem_wanted` in [WantedExt/Analysis/WignerSemicircleWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/WignerSemicircleWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/wigner-s-semicircle-law/index.html#wigner-semicircle).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Wigner's semicircle law](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/wigner-s-semicircle-law/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/high-dimensional-probability/wigner-s-semicircle-law)
