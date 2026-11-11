---
declaration: section
origin: cited
lean: MathlibExt.Analysis.WienerAtomWanted.Analysis.fourierCoeffMeasure, MathlibExt.Analysis.WienerAtomWanted.Analysis.wiener_atom_detection, MathlibExt.MeasureTheory.CircleMeasureFourierDecayIntegrableWanted.tendsto_integral_pow_mul_of_tendsto_integral_pow
statement: formalized
---

# Fourier coefficients of measures on the circle

3 results, 1 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fourier-coefficients-of-measures-on-the-circle/index.html).

## Fourier coefficients of a measure on the circle

For a measure $\mu$ on the circle
$\mathbb{T} = \mathbb{R}/2\pi\mathbb{Z}$ and an integer $k$, the $k$-th Fourier coefficient of
$\mu$ is $\hat\mu_k = \int_{\mathbb{T}} e^{ikx} \, d\mu(x)$.

Formalized by `MathlibExt.Analysis.WienerAtomWanted.Analysis.fourierCoeffMeasure`, a definition declared in [WantedExt/Analysis/WienerAtomWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/WienerAtomWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fourier-coefficients-of-measures-on-the-circle/index.html#fourier-coeff-measure).

## Wiener's atom-detection formula

Let $\mu$ be a probability measure on the circle
$\mathbb{T} = \mathbb{R}/2\pi\mathbb{Z}$, with Fourier coefficients
$\hat\mu_k = \int_{\mathbb{T}} e^{ikx} \, d\mu(x)$. Then
$\frac{1}{N} \sum_{k=1}^{N} \lvert \hat\mu_k \rvert^2 \to \sum_{x \in \mathbb{T}} \mu(\{x\})^2$
as $N \to \infty$.

## Sources

- N. Wiener, The Fourier Integral and Certain of its Applications (1933). Listed as §66 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `wiener_atom_detection` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.WienerAtomWanted.Analysis.wiener_atom_detection` is written with `theorem_wanted` in [WantedExt/Analysis/WienerAtomWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/WienerAtomWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fourier-coefficients-of-measures-on-the-circle/index.html#wiener-atom-detection).

## Fourier decay of a circle measure passes to integrable densities

Let $\mu$ be a finite
Borel measure on $\mathbb{C}$ concentrated on the unit circle $T = \{z \in \mathbb{C} : |z| = 1\}$,
that is, $\mu$-almost every $z$ lies in $T$, and suppose that $\int z^n \, d\mu(z) \to 0$ as
$n \to \infty$ through $\mathbb{N}$. Then for every $\mu$-integrable function
$f : \mathbb{C} \to \mathbb{C}$,

$$
\lim_{n \to \infty} \int z^n f(z) \, d\mu(z) = 0.
$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Measure and integration; Set functions and measures on spaces with additional structure), problem `ma_proofbench_l2_13`.

Stated but not proved: `MathlibExt.MeasureTheory.CircleMeasureFourierDecayIntegrableWanted.tendsto_integral_pow_mul_of_tendsto_integral_pow` is written with `theorem_wanted` in [WantedExt/MeasureTheory/CircleMeasureFourierDecayIntegrableWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/CircleMeasureFourierDecayIntegrableWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fourier-coefficients-of-measures-on-the-circle/index.html#tendsto-integral-pow-mul-of-tendsto-inte).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fourier coefficients of measures on the circle](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fourier-coefficients-of-measures-on-the-circle/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/harmonic-analysis/fourier-series/fourier-coefficients-of-measures-on-the-circle)
