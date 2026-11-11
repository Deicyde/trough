---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.RankOneSpectrum.smulRight_mul_self, MathlibExt.Analysis.FunctionalAnalysis.RankOneSpectrum.not_mem_spectrum_smulRight, MathlibExt.Analysis.FunctionalAnalysis.RankOneSpectrum.hasEigenvalue_smulRight, MathlibExt.Analysis.FunctionalAnalysis.RankOneSpectrum.mem_spectrum_smulRight, MathlibExt.Analysis.FunctionalAnalysis.RankOneSpectrum.hasEigenvalue_zero_smulRight, MathlibExt.Analysis.FunctionalAnalysis.RankOneSpectrum.mem_spectrum_smulRight_zero, MathlibExt.Analysis.FunctionalAnalysis.RankOneSpectrum.spectrum_smulRight, MathlibExt.Analysis.FunctionalAnalysis.RankOneSpectrum.spectrum_smulRight_of_apply_eq_zero
statement: formalized
proof: formalized
---

# Spectrum of rank-one operators

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-rank-one-operators/index.html).

## Square of the operator $x \mapsto f(x)\,y$

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $E$ be a normed space over $\mathbb{K}$, let $f \colon E \to \mathbb{K}$ be a
continuous linear functional, let $y \in E$, and let $T$ be the bounded operator on $E$ given by
$T x = f(x)\,y$. Then $T^2 = f(y)\,T$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RankOneSpectrum.smulRight_mul_self`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RankOneSpectrum.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RankOneSpectrum.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-rank-one-operators/index.html#smul-right-mul-self).

## The spectrum of $x \mapsto f(x)\,y$ lies in $\{0, f(y)\}$

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $E$ be a normed space over $\mathbb{K}$, let
$f \colon E \to \mathbb{K}$ be a continuous linear functional, let $y \in E$, and let $T$ be the
bounded operator on $E$ given by $T x = f(x)\,y$. If $\mu \in \mathbb{K}$ satisfies $\mu \neq 0$
and $\mu \neq f(y)$, then $\mu$ is not in the spectrum of $T$ in the algebra of bounded operators
on $E$.

Explicitly, the inverse of $\mu I - T$, where $I$ is the identity operator, is
$\mu^{-1} I + \mu^{-1} (\mu - f(y))^{-1}\,T$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RankOneSpectrum.not_mem_spectrum_smulRight`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RankOneSpectrum.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RankOneSpectrum.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-rank-one-operators/index.html#not-mem-spectrum-smul-right).

## $f(y)$ is an eigenvalue of $x \mapsto f(x)\,y$

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $E$ be a normed space over $\mathbb{K}$, let $f \colon E \to \mathbb{K}$ be a
continuous linear functional, and let $y \in E$ with $y \neq 0$. Then $f(y)$ is an eigenvalue of
the linear operator $T x = f(x)\,y$ on $E$.

An eigenvector is $y$ itself, since $T y = f(y)\,y$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RankOneSpectrum.hasEigenvalue_smulRight`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RankOneSpectrum.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RankOneSpectrum.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-rank-one-operators/index.html#has-eigenvalue-smul-right).

## $f(y)$ lies in the spectrum of $x \mapsto f(x)\,y$

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $E$ be a Banach space over $\mathbb{K}$, let $f \colon E \to \mathbb{K}$ be a
continuous linear functional, and let $y \in E$ with $y \neq 0$. Then $f(y)$ lies in the spectrum
of the bounded operator $T x = f(x)\,y$ on $E$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RankOneSpectrum.mem_spectrum_smulRight`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RankOneSpectrum.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RankOneSpectrum.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-rank-one-operators/index.html#mem-spectrum-smul-right).

## $0$ is an eigenvalue of $x \mapsto f(x)\,y$ when $f$ has a nontrivial kernel

Let
$\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, let $E$ be a normed space over $\mathbb{K}$, let
$f \colon E \to \mathbb{K}$ be a continuous linear functional, and let $y \in E$. If some
$w \in E$ with $w \neq 0$ satisfies $f(w) = 0$, then $0$ is an eigenvalue of the linear operator
$T x = f(x)\,y$ on $E$.

An eigenvector is $w$ itself, since $T w = f(w)\,y = 0$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RankOneSpectrum.hasEigenvalue_zero_smulRight`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RankOneSpectrum.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RankOneSpectrum.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-rank-one-operators/index.html#has-eigenvalue-zero-smul-right).

## $0$ lies in the spectrum of $x \mapsto f(x)\,y$ when $f$ has a nontrivial kernel

Let
$\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, let $E$ be a Banach space over $\mathbb{K}$, let
$f \colon E \to \mathbb{K}$ be a continuous linear functional, and let $y \in E$. If some
$w \in E$ with $w \neq 0$ satisfies $f(w) = 0$, then $0$ lies in the spectrum of the bounded
operator $T x = f(x)\,y$ on $E$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RankOneSpectrum.mem_spectrum_smulRight_zero`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RankOneSpectrum.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RankOneSpectrum.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-rank-one-operators/index.html#mem-spectrum-smul-right-zero).

## Spectrum of the operator $x \mapsto f(x)\,y$

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $E$ be a Banach space over $\mathbb{K}$, let
$f \colon E \to \mathbb{K}$ be a continuous linear functional, and let $y \in E$ with $y \neq 0$.
If some $w \in E$ with $w \neq 0$ satisfies $f(w) = 0$, then the spectrum of the bounded
operator $T x = f(x)\,y$ on $E$ is exactly $\{0, f(y)\}$.

Here $y$ is an eigenvector for $f(y)$ and $w$ is an eigenvector for $0$; the zero functional is
allowed. Without the kernel hypothesis this fails: on a one-dimensional space a nonzero operator
of this form is a nonzero multiple of the identity, whose spectrum is a single point.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RankOneSpectrum.spectrum_smulRight`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RankOneSpectrum.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RankOneSpectrum.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-rank-one-operators/index.html#spectrum-smul-right).

## Spectrum of $x \mapsto f(x)\,y$ when $f(y) = 0$

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $E$ be a Banach space over $\mathbb{K}$, let $f \colon E \to \mathbb{K}$ be a
continuous linear functional, and let $y \in E$ with $y \neq 0$ and $f(y) = 0$. Then the
spectrum of the bounded operator $T x = f(x)\,y$ on $E$ is $\{0\}$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RankOneSpectrum.spectrum_smulRight_of_apply_eq_zero`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RankOneSpectrum.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RankOneSpectrum.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-rank-one-operators/index.html#spectrum-smul-right-of-apply-eq-zero).

## Spectrum of the operator $z \mapsto \langle y, z \rangle\,x$ on a Hilbert space

Let
$\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, let $H$ be a Hilbert space over $\mathbb{K}$ whose
inner product $\langle \cdot, \cdot \rangle$ is linear in the second argument, let $x, y \in H$
with $x \neq 0$, and let $T$ be the bounded operator on $H$ given by
$T z = \langle y, z \rangle\,x$. If some $w \in H$ with $w \neq 0$ satisfies
$\langle y, w \rangle = 0$, then the spectrum of $T$ is $\{0, \langle y, x \rangle\}$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RankOneSpectrum.spectrum_rankOne`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RankOneSpectrum.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RankOneSpectrum.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-rank-one-operators/index.html#spectrum-rank-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Spectrum of rank-one operators](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-rank-one-operators/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-rank-one-operators)
