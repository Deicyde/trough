---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.HarmonicVanishingOnPositiveMeasureWanted.eq_zero_of_harmonicOnNhd_of_vanishing_on_pos_volume, MathlibExt.Analysis.Complex.HarmonicConjugateSimplyConnectedWanted.exists_differentiableOn_re_eq_of_harmonicOnNhd_of_isSimplyConnected, MathlibExt.Analysis.Complex.NonnegHarmonicUpperHalfPlaneAxisIntegrableWanted.eq_zero_of_harmonicOnNhd_upperHalfPlane_of_nonneg_of_integrableOn_imagAxis
statement: formalized
---

# Potential theory: its own results

3 results, 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/index.html).

Harmonic and subharmonic functions in the plane and in R^n, harmonic conjugates, the Newton and logarithmic potentials and fundamental solutions of the Laplacian.

## A harmonic function vanishing on a set of positive measure is zero

Let
$\Omega \subseteq \mathbb{C}$ be a nonempty connected open set and let
$h : \mathbb{C} \to \mathbb{R}$ be harmonic on $\Omega$. If $h$ vanishes on some subset
$s \subseteq \Omega$ of positive (outer) Lebesgue measure, then $h(z) = 0$ for all $z \in \Omega$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functions of a complex variable; Miscellaneous topics of analysis in the complex plane), problem `ma_proofbench_l2_88`.

Stated but not proved: `MathlibExt.Analysis.Complex.HarmonicVanishingOnPositiveMeasureWanted.eq_zero_of_harmonicOnNhd_of_vanishing_on_pos_volume` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/HarmonicVanishingOnPositiveMeasureWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/HarmonicVanishingOnPositiveMeasureWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/index.html#eq-zero-of-harmonic-on-nhd-of-vanishing).

## Harmonic functions on simply connected domains are real parts

Let
$\Omega \subseteq \mathbb{C}$ be a simply connected open set and let $u : \mathbb{C} \to \mathbb{R}$
be harmonic on $\Omega$. Then there is a function $f$ holomorphic on $\Omega$ with
$\operatorname{Re} f(z) = u(z)$ for all $z \in \Omega$, and $f$ is unique up to an additive
constant: if $f$ and $g$ are holomorphic on $\Omega$ with $\operatorname{Re} f(z) = u(z)$ and
$\operatorname{Re} g(z) = u(z)$ for all $z \in \Omega$, then there is $c \in \mathbb{C}$ with
$f(z) = g(z) + c$ for all $z \in \Omega$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functions of a complex variable; General properties of functions of one complex variable), problem `ma_proofbench_l2_69`.

Stated but not proved: `MathlibExt.Analysis.Complex.HarmonicConjugateSimplyConnectedWanted.exists_differentiableOn_re_eq_of_harmonicOnNhd_of_isSimplyConnected` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/HarmonicConjugateSimplyConnectedWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/HarmonicConjugateSimplyConnectedWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/index.html#exists-differentiable-on-re-eq-of-harmon).

## Nonnegative harmonic functions on the upper half-plane integrable along the imaginary axis vanish

**Nonnegative harmonic functions on the upper half-plane integrable along the imaginary axis
vanish.** Let $\mathbb{C}_{+}=\{z\in\mathbb{C}:\Im z>0\}$ be the upper half-plane. Suppose
$f:\mathbb{C}_{+}\to\mathbb{R}$ is harmonic and non-negative, and satisfies
\[
\int_{0}^{\infty}\lvert f(iy)\rvert\,dy\lt \infty.
\]
Then $f(z)=0$ for every $z\in\mathbb{C}_{+}$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functions of a complex variable; General properties of functions of one complex variable), problem `ma_proofbench_l2_20`.

Stated but not proved: `MathlibExt.Analysis.Complex.NonnegHarmonicUpperHalfPlaneAxisIntegrableWanted.eq_zero_of_harmonicOnNhd_upperHalfPlane_of_nonneg_of_integrableOn_imagAxis` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/NonnegHarmonicUpperHalfPlaneAxisIntegrableWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/NonnegHarmonicUpperHalfPlaneAxisIntegrableWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/index.html#eq-zero-of-harmonic-on-nhd-upper-half-pl).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Potential theory](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/potential-theory)
