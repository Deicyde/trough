---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Fourier.AddCircle.FourierUniqueness.eq_zero_of_fourierCoeff_eq_zero_Lp, MathlibExt.Analysis.Fourier.AddCircle.FourierUniqueness.eq_zero_of_fourierCoeff_eq_zero, MathlibExt.Analysis.Fourier.AddCircle.FourierUniqueness.eq_of_fourierCoeff_eq, MathlibExt.Analysis.Fourier.AddCircle.FourierUniqueness.fourierCoeff_injective, MathlibExt.Analysis.Fourier.AddCircle.FourierUniqueness.eq_zero_of_fourierCoeffOn_eq_zero
statement: formalized
proof: formalized
---

# Uniqueness of Fourier coefficients

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/uniqueness-of-fourier-coefficients/index.html).

## Uniqueness of Fourier coefficients in L²

Let $T > 0$ and let $\mu$ be the Haar
probability measure on the circle $\mathbb{R}/T\mathbb{Z}$. If an element $F$ of
$L^2(\mathbb{R}/T\mathbb{Z}, \mu; \mathbb{C})$ has Fourier coefficients
$\hat F(n) = \int e^{-2\pi i n t / T} F(t)\,d\mu(t)$ equal to $0$ for every $n \in \mathbb{Z}$,
then $F = 0$ in $L^2(\mathbb{R}/T\mathbb{Z}, \mu; \mathbb{C})$.

Formalized by `MathlibExt.Analysis.Fourier.AddCircle.FourierUniqueness.eq_zero_of_fourierCoeff_eq_zero_Lp`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/FourierUniqueness.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FourierUniqueness.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/uniqueness-of-fourier-coefficients/index.html#eq-zero-of-fourier-coeff-eq-zero-lp).

## Uniqueness of Fourier coefficients for continuous functions

Let $T > 0$ and let $\mu$
be the Haar probability measure on the circle $\mathbb{R}/T\mathbb{Z}$. If a continuous function
$f : \mathbb{R}/T\mathbb{Z} \to \mathbb{C}$ has Fourier coefficients
$\hat f(n) = \int e^{-2\pi i n t / T} f(t)\,d\mu(t)$ equal to $0$ for every $n \in \mathbb{Z}$,
then $f = 0$.

Formalized by `MathlibExt.Analysis.Fourier.AddCircle.FourierUniqueness.eq_zero_of_fourierCoeff_eq_zero`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/FourierUniqueness.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FourierUniqueness.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/uniqueness-of-fourier-coefficients/index.html#eq-zero-of-fourier-coeff-eq-zero).

## Fourier coefficients determine a continuous function

Let $T > 0$ and let $\mu$ be the
Haar probability measure on the circle $\mathbb{R}/T\mathbb{Z}$. For a function
$h : \mathbb{R}/T\mathbb{Z} \to \mathbb{C}$ and $n \in \mathbb{Z}$, let
$\hat h(n) = \int e^{-2\pi i n t / T} h(t)\,d\mu(t)$ be the $n$-th Fourier coefficient of $h$. If
two continuous functions $f, g : \mathbb{R}/T\mathbb{Z} \to \mathbb{C}$ satisfy
$\hat f(n) = \hat g(n)$ for every $n \in \mathbb{Z}$, then $f = g$.

Formalized by `MathlibExt.Analysis.Fourier.AddCircle.FourierUniqueness.eq_of_fourierCoeff_eq`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/FourierUniqueness.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FourierUniqueness.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/uniqueness-of-fourier-coefficients/index.html#eq-of-fourier-coeff-eq).

## Injectivity of the Fourier-coefficient map

Let $T > 0$ and let $\mu$ be the Haar
probability measure on the circle $\mathbb{R}/T\mathbb{Z}$. The map sending a continuous function
$f : \mathbb{R}/T\mathbb{Z} \to \mathbb{C}$ to its sequence of Fourier coefficients
$(\hat f(n))_{n \in \mathbb{Z}}$, where $\hat f(n) = \int e^{-2\pi i n t / T} f(t)\,d\mu(t)$, is
injective.

Formalized by `MathlibExt.Analysis.Fourier.AddCircle.FourierUniqueness.fourierCoeff_injective`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/FourierUniqueness.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FourierUniqueness.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/uniqueness-of-fourier-coefficients/index.html#fourier-coeff-injective).

## Uniqueness of Fourier coefficients on an interval

Let $a, T \in \mathbb{R}$ with
$T > 0$, and let $f : \mathbb{R} \to \mathbb{C}$ be continuous with $f(a) = f(a + T)$. If the
Fourier coefficients of $f$ on $[a, a + T]$,

$$\hat f(n) = \frac{1}{T} \int_a^{a+T} e^{-2\pi i n x / T} f(x)\,dx,$$

are $0$ for every $n \in \mathbb{Z}$, then $f(x) = 0$ for every $x \in [a, a + T]$.

This is a corollary of uniqueness on the circle: the endpoint condition makes $f$ on
$[a, a + T]$ descend to a continuous function on $\mathbb{R}/T\mathbb{Z}$.

Formalized by `MathlibExt.Analysis.Fourier.AddCircle.FourierUniqueness.eq_zero_of_fourierCoeffOn_eq_zero`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/FourierUniqueness.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FourierUniqueness.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/uniqueness-of-fourier-coefficients/index.html#eq-zero-of-fourier-coeff-on-eq-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Uniqueness of Fourier coefficients](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/uniqueness-of-fourier-coefficients/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/harmonic-analysis/fourier-series/uniqueness-of-fourier-coefficients)
