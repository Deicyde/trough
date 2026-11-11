---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.SelfAdjointPositiveSpectrum.spectrum_re_nonneg_of_reApplyInnerSelf_nonneg, MathlibExt.Analysis.InnerProductSpace.SelfAdjointPositiveSpectrum.positive_iff_spectrum_nonneg, MathlibExt.Analysis.InnerProductSpace.SelfAdjointSpectrumBounds.rayleighQuotient_algebraMap_sub, MathlibExt.Analysis.InnerProductSpace.SelfAdjointSpectrumBounds.selfAdjoint_spectrum_subset_Icc_nonzero, MathlibExt.Analysis.InnerProductSpace.SelfAdjointSpectrumBounds.selfAdjoint_spectrum_subset_Icc
statement: formalized
proof: formalized
---

# Spectrum of self-adjoint operators

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-self-adjoint-operators/index.html).

## Spectrum of an accretive operator has nonnegative real part

Let $T$ be a bounded linear
operator on a Hilbert space $H$ over $\mathbb{R}$ or $\mathbb{C}$. If
$\operatorname{Re}\langle Tu, u\rangle \ge 0$ for every $u \in H$, then every element $\mu$ of
the spectrum of $T$ satisfies $\operatorname{Re}\mu \ge 0$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.SelfAdjointPositiveSpectrum.spectrum_re_nonneg_of_reApplyInnerSelf_nonneg`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/SelfAdjointPositiveSpectrum.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/SelfAdjointPositiveSpectrum.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-self-adjoint-operators/index.html#spectrum-re-nonneg-of-re-apply-inner-sel).

## Positivity iff spectrum nonnegative

Let $T$ be a self-adjoint bounded linear operator on a
nonzero Hilbert space $H$ over $\mathbb{R}$ or $\mathbb{C}$. Then
$\operatorname{Re}\langle Tu, u\rangle \ge 0$ for every $u \in H$ if and only if every element
$\mu$ of the spectrum of $T$ satisfies $\operatorname{Re}\mu \ge 0$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.SelfAdjointPositiveSpectrum.positive_iff_spectrum_nonneg`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/SelfAdjointPositiveSpectrum.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/SelfAdjointPositiveSpectrum.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-self-adjoint-operators/index.html#positive-iff-spectrum-nonneg).

## Rayleigh quotient of a shifted operator

Let $T$ be a bounded linear operator on an inner
product space $H$ over $\mathbb{R}$ or $\mathbb{C}$, let $I$ be the identity operator on $H$, and
write $R_S(x) = \operatorname{Re}\langle Sx, x\rangle / \|x\|^2$ for the Rayleigh quotient of an
operator $S$. Then for every real number $t$ and every nonzero $x \in H$,
$R_{tI - T}(x) = t - R_T(x)$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.SelfAdjointSpectrumBounds.rayleighQuotient_algebraMap_sub`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/SelfAdjointSpectrumBounds.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/SelfAdjointSpectrumBounds.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-self-adjoint-operators/index.html#rayleigh-quotient-algebra-map-sub).

## Spectrum bounds over nonzero vectors

Let $T$ be a self-adjoint bounded linear operator on
a nonzero Hilbert space $H$ over $\mathbb{R}$ or $\mathbb{C}$, with Rayleigh quotient
$R_T(x) = \operatorname{Re}\langle Tx, x\rangle / \|x\|^2$. Then every $\mu$ in the spectrum of
$T$ satisfies $\inf_{x \ne 0} R_T(x) \le \operatorname{Re}\mu \le \sup_{x \ne 0} R_T(x)$, where
the infimum and supremum range over the nonzero vectors $x \in H$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.SelfAdjointSpectrumBounds.selfAdjoint_spectrum_subset_Icc_nonzero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/SelfAdjointSpectrumBounds.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/SelfAdjointSpectrumBounds.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-self-adjoint-operators/index.html#self-adjoint-spectrum-subset-icc-nonzero).

## Spectrum bounds over all vectors

Let $T$ be a self-adjoint bounded linear operator on a
nonzero Hilbert space $H$ over $\mathbb{R}$ or $\mathbb{C}$, with Rayleigh quotient
$R_T(x) = \operatorname{Re}\langle Tx, x\rangle / \|x\|^2$ for $x \ne 0$ and $R_T(0) = 0$. Then
every $\mu$ in the spectrum of $T$ satisfies
$\inf_{x \in H} R_T(x) \le \operatorname{Re}\mu \le \sup_{x \in H} R_T(x)$.

Unlike the bounds over nonzero vectors, these extrema also take into account the value $0$ of the
quotient at $x = 0$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.SelfAdjointSpectrumBounds.selfAdjoint_spectrum_subset_Icc`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/SelfAdjointSpectrumBounds.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/SelfAdjointSpectrumBounds.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-self-adjoint-operators/index.html#self-adjoint-spectrum-subset-icc).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Spectrum of self-adjoint operators](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-self-adjoint-operators/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-self-adjoint-operators)
