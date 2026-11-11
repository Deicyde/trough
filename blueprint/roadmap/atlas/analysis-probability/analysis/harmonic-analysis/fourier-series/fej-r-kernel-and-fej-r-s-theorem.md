---
declaration: section
origin: cited
lean: AddCircle.fejerKernel, AddCircle.fourier_integrable, AddCircle.integral_fourier, AddCircle.integral_dirichlet_sum, AddCircle.fejerKernel_symmetric, AddCircle.integral_fejerKernel, AddCircle.norm_fejerKernel_le, AddCircle.fejerKernel_continuous
statement: formalized
proof: formalized
---

# Fejér kernel and Fejér's theorem

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html).

## The Fejér kernel

Let $T > 0$ and, for $n \in \mathbb{Z}$, let
$e_n(x) = e^{2\pi i n x / T}$ be the $n$-th Fourier character on the circle
$\mathbb{R}/T\mathbb{Z}$. For a natural number $N$, the $N$-th Fejér kernel is the function
$K_N : \mathbb{R}/T\mathbb{Z} \to \mathbb{C}$ given by the Cesàro mean of the Dirichlet kernels,
$K_N(x) = \frac{1}{N+1} \sum_{k=0}^{N} \sum_{n=-k}^{k} e_n(x)$.

Writing $x$ also for a real representative, when $\sin(\pi x / T) \ne 0$ the kernel has the closed
form $K_N(x) = \frac{1}{N+1} \left(\frac{\sin((N+1)\pi x / T)}{\sin(\pi x / T)}\right)^2$.
This normalization is for the Haar probability measure on $\mathbb{R}/T\mathbb{Z}$; for $T = 2\pi$,
the kernel for integration against Lebesgue measure is $K_N / (2\pi)$.

Formalized by `AddCircle.fejerKernel`, a definition declared in [MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#fejer-kernel).

## Integrability of Fourier characters

Let $T > 0$. For every integer $n$, the Fourier
character $e_n(x) = e^{2\pi i n x / T}$ is integrable on the circle $\mathbb{R}/T\mathbb{Z}$ with
respect to the normalized Haar measure, the Haar measure of total mass $1$.

Formalized by `AddCircle.fourier_integrable`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#fourier-integrable).

## Integral of a Fourier character

Let $T > 0$ and, for $n \in \mathbb{Z}$, let
$e_n(t) = e^{2\pi i n t / T}$ be the $n$-th Fourier character on the circle
$\mathbb{R}/T\mathbb{Z}$. With respect to the Haar probability measure on the circle,
$\int e_n = 1$ if $n = 0$ and $\int e_n = 0$ otherwise. This is the orthogonality of the
Fourier basis.

Formalized by `AddCircle.integral_fourier`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#integral-fourier).

## The Dirichlet kernel has integral one

Let $T > 0$, let
$e_n(t) = e^{2\pi i n t / T}$ be the $n$-th Fourier character on the circle
$\mathbb{R}/T\mathbb{Z}$, and for $k \in \mathbb{N}$ let $D_k = \sum_{n=-k}^{k} e_n$ be the
$k$-th Dirichlet kernel. With respect to the Haar probability measure on the circle,
$\int D_k = 1$; only the term $n = 0$ contributes, by orthogonality.

Formalized by `AddCircle.integral_dirichlet_sum`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#integral-dirichlet-sum).

## Symmetry of the Fejér kernel

Let $T > 0$. For every natural number $N$ and every
$x \in \mathbb{R}/T\mathbb{Z}$, the $N$-th Fejér kernel satisfies $K_N(-x) = K_N(x)$.

Formalized by `AddCircle.fejerKernel_symmetric`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#fejer-kernel-symmetric).

## The Fejér kernel has integral one

Let $T > 0$ and $N \in \mathbb{N}$. The $N$-th Fejér
kernel $K_N$ on the circle $\mathbb{R}/T\mathbb{Z}$ satisfies $\int K_N = 1$ with respect to the
Haar probability measure on the circle. This is one of the defining properties of an
approximation to the identity.

Formalized by `AddCircle.integral_fejerKernel`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#integral-fejer-kernel).

## Pointwise bound for the Fejér kernel

Let $T > 0$ and $N \in \mathbb{N}$. For every point
$x$ of the circle $\mathbb{R}/T\mathbb{Z}$, the $N$-th Fejér kernel satisfies
$|K_N(x)| \le N + 1$.

This follows from the triangle inequality applied to the iterated Dirichlet sum defining
$K_N$, together with $\sum_{k=0}^{N} (2k+1) = (N+1)^2$.

Formalized by `AddCircle.norm_fejerKernel_le`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#norm-fejer-kernel-le).

## Continuity of the Fejér kernel

Let $T > 0$. For every natural number $N$, the $N$-th
Fejér kernel $K_N$ is a continuous function from the circle $\mathbb{R}/T\mathbb{Z}$ to
$\mathbb{C}$.

Formalized by `AddCircle.fejerKernel_continuous`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#fejer-kernel-continuous).

## Integrability of the Fejér kernel

Let $T > 0$. For every natural number $N$, the $N$-th
Fejér kernel $K_N$ is integrable on the circle $\mathbb{R}/T\mathbb{Z}$ with respect to the
normalized Haar measure, the Haar measure of total mass $1$.

Formalized by `AddCircle.fejerKernel_integrable`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#fejer-kernel-integrable).

## Products of Fourier characters

Let $T$ be a real number and, for $n \in \mathbb{Z}$, let
$e_n$ be the $n$-th Fourier character on $\mathbb{R}/T\mathbb{Z}$, given by
$e_n(x) = e^{2\pi i n x / T}$ (the constant $1$ when $T = 0$). For every integer $n$ and all
$x, t \in \mathbb{R}/T\mathbb{Z}$, we have $e_{-n}(t)\, e_n(x) = e_n(x - t)$.

Formalized by `AddCircle.fourier_neg_mul_fourier_eq`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#fourier-neg-mul-fourier-eq).

## Reindexing a sum of Fourier characters, negative range

Let $T > 0$, let
$e_n(t) = e^{2\pi i n t / T}$ be the $n$-th Fourier character on the circle
$\mathbb{R}/T\mathbb{Z}$, and let $N \in \mathbb{N}$. For every point $x$ of the circle,
$\sum_{k=0}^{N} e_{k-(N+1)}(x) = \sum_{n=-(N+1)}^{-1} e_n(x)$.

It is used in the proof that the iterated Dirichlet sum defining the Fejér kernel equals
$\left|\sum_{k=0}^{N} e_k(x)\right|^2$.

Formalized by `AddCircle.sum_range_fourier_shift_neg`, a lemma declared in [MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#sum-range-fourier-shift-neg).

## Reindexing a sum of Fourier characters, positive range

Let $T > 0$, let
$e_n(t) = e^{2\pi i n t / T}$ be the $n$-th Fourier character on the circle
$\mathbb{R}/T\mathbb{Z}$, and let $N \in \mathbb{N}$. For every point $x$ of the circle,
$\sum_{k=0}^{N} e_{(N+1)-k}(x) = \sum_{n=1}^{N+1} e_n(x)$.

Formalized by `AddCircle.sum_range_fourier_shift_pos`, a lemma declared in [MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#sum-range-fourier-shift-pos).

## The sum of Dirichlet kernels is a squared modulus

Let $T > 0$ and, for $n \in \mathbb{Z}$,
let $e_n(x) = e^{2\pi i n x / T}$ be the $n$-th Fourier character on the circle
$\mathbb{R}/T\mathbb{Z}$. For every natural number $N$ and every $x \in \mathbb{R}/T\mathbb{Z}$,
put $G = \sum_{k=0}^{N} e_k(x)$. Then the iterated sum of Dirichlet kernels satisfies
$\sum_{k=0}^{N} \sum_{n=-k}^{k} e_n(x) = G\,\overline{G} = |G|^2$.

Formalized by `AddCircle.fejer_dirichlet_sum_eq_sq`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#fejer-dirichlet-sum-eq-sq).

## Nonnegativity of the Fejér kernel

Let $T > 0$. For every natural number $N$ and every
$x \in \mathbb{R}/T\mathbb{Z}$, the real part of the $N$-th Fejér kernel at $x$ is nonnegative:
$\operatorname{Re} K_N(x) \ge 0$.

Formalized by `AddCircle.fejerKernel_nonneg`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#fejer-kernel-nonneg).

## The Fejér kernel as a squared modulus

Let $T > 0$ and, for $k \in \mathbb{Z}$, let
$e_k(x) = e^{2\pi i k x / T}$ be the $k$-th Fourier character on the circle
$\mathbb{R}/T\mathbb{Z}$. For every natural number $N$ and every $x \in \mathbb{R}/T\mathbb{Z}$,
the $N$-th Fejér kernel satisfies $K_N(x) = \frac{1}{N+1} \left|\sum_{k=0}^{N} e_k(x)\right|^2$.

In particular $K_N(x)$ is a nonnegative real number, so $|K_N(x)| = \operatorname{Re} K_N(x)$.

Formalized by `AddCircle.fejerKernel_eq_ofReal`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#fejer-kernel-eq-of-real).

## Properties of the Fejér kernel

Let $T > 0$, let $N$ be a natural number, let $K_N$ be
the $N$-th Fejér kernel on the circle $\mathbb{R}/T\mathbb{Z}$, let $\mu$ be the normalized Haar
measure on $\mathbb{R}/T\mathbb{Z}$ (of total mass $1$), and let $e_1(x) = e^{2\pi i x / T}$.
Then $\operatorname{Re} K_N(x) \ge 0$ for every $x \in \mathbb{R}/T\mathbb{Z}$;
$K_N(-x) = K_N(x)$ for every $x \in \mathbb{R}/T\mathbb{Z}$; the function on $\mathbb{R}$ sending
$t$ to $K_N$ evaluated at the class of $t$ in $\mathbb{R}/T\mathbb{Z}$ is $T$-periodic;
$\int K_N \, d\mu = 1$; and for every $\delta > 0$ and every $x \in \mathbb{R}/T\mathbb{Z}$ with
$\delta \le |1 - e_1(x)|$ we have $|K_N(x)| \le \frac{4}{(N+1)\delta^2}$.

Formalized by `AddCircle.fejer_kernel_properties`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FejerKernel.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#fejer-kernel-properties).

## Partial Fourier sums

Let $T > 0$ and $f : \mathbb{R}/T\mathbb{Z} \to \mathbb{C}$. For
$N \in \mathbb{N}$, the $N$-th partial Fourier sum of $f$ is the function

$$S_N f(x) = \sum_{n=-N}^{N} \hat f(n)\, e_n(x),$$

where $e_n(x) = e^{2\pi i n x / T}$ is the $n$-th Fourier character and
$\hat f(n) = \int_{\mathbb{R}/T\mathbb{Z}} e_{-n}(t)\, f(t)\, dt$ is the $n$-th Fourier coefficient,
the integral taken against the Haar probability measure on the circle.

Formalized by `AddCircle.partialFourierSum`, a definition declared in [MathlibExt/Analysis/Fourier/AddCircle/CesaroMean.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/CesaroMean.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#partial-fourier-sum).

## Cesàro–Fourier means

Let $T > 0$ and $f : \mathbb{R}/T\mathbb{Z} \to \mathbb{C}$. For
$N \in \mathbb{N}$, the $N$-th Cesàro–Fourier mean of $f$ is the average of its first $N + 1$
partial Fourier sums,

$$\sigma_N f(x) = \frac{1}{N+1} \sum_{k=0}^{N} S_k f(x),$$

where $S_k f$ is the $k$-th partial Fourier sum of $f$.

Formalized by `AddCircle.cesaroFourierMean`, a definition declared in [MathlibExt/Analysis/Fourier/AddCircle/CesaroMean.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/CesaroMean.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#cesaro-fourier-mean).

## Fourier characters at a difference

Let $T > 0$ and for $n \in \mathbb{Z}$ let
$e_n(x) = e^{2\pi i n x / T}$ be the $n$-th Fourier character on $\mathbb{R}/T\mathbb{Z}$. Then
for every $n \in \mathbb{Z}$ and all $x, t \in \mathbb{R}/T\mathbb{Z}$,
$e_n(x - t) = e_{-n}(t)\, e_n(x)$.

Formalized by `AddCircle.fourier_sub_eq`, a lemma declared in [MathlibExt/Analysis/Fourier/AddCircle/CesaroMean.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/CesaroMean.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#fourier-sub-eq).

## Integrability of a function twisted by a Fourier character

Let $T > 0$ and let
$f : \mathbb{R}/T\mathbb{Z} \to \mathbb{C}$ be integrable with respect to the Haar probability
measure on the circle. Then for every $n \in \mathbb{Z}$ and every $x \in \mathbb{R}/T\mathbb{Z}$,
the function $t \mapsto e^{2\pi i n t / T} f(x - t)$ is integrable with respect to the same
measure.

This is used to interchange sums and integrals in the convolution computation.

Formalized by `AddCircle.fourier_smul_integrable`, a lemma declared in [MathlibExt/Analysis/Fourier/AddCircle/CesaroMean.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/CesaroMean.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#fourier-smul-integrable).

## Convolution of a function with a Fourier character

Let $T > 0$, let
$f : \mathbb{R}/T\mathbb{Z} \to \mathbb{C}$ be integrable with respect to the Haar probability
measure $dt$ on the circle, for $n \in \mathbb{Z}$ let $e_n(x) = e^{2\pi i n x / T}$ be the
$n$-th Fourier character, and let $\hat f(n) = \int_{\mathbb{R}/T\mathbb{Z}} e_{-n}(t)\, f(t)\, dt$
be the $n$-th Fourier coefficient of $f$. Then for every $n \in \mathbb{Z}$ and every
$x \in \mathbb{R}/T\mathbb{Z}$,

$$\int_{\mathbb{R}/T\mathbb{Z}} e_n(t)\, f(x - t)\, dt = \hat f(n)\, e_n(x).$$

Thus the $n$-th term of the partial Fourier sum of $f$ at $x$ is the convolution of $f$ with
the Fourier character $e_n$.

Formalized by `AddCircle.fourier_integral_convolution`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/CesaroMean.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/CesaroMean.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#fourier-integral-convolution).

## Cesàro–Fourier means are convolutions with the Fejér kernel

Let $T > 0$ and let
$f : \mathbb{R}/T\mathbb{Z} \to \mathbb{C}$ be integrable with respect to the Haar probability
measure $dt$ on the circle. Then for every $N \in \mathbb{N}$ and every
$x \in \mathbb{R}/T\mathbb{Z}$, the $N$-th Cesàro–Fourier mean of $f$ satisfies

$$\sigma_N f(x) = \int_{\mathbb{R}/T\mathbb{Z}} K_N(t)\, f(x - t)\, dt,$$

where $K_N$ is the $N$-th Fejér kernel.

This is the bridge from the definition of $\sigma_N f$ to the kernel-theoretic analysis
underlying Fejér's theorem.

Formalized by `AddCircle.cesaroMean_eq_fejer_convolution`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/CesaroMean.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/CesaroMean.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#cesaro-mean-eq-fejer-convolution).

## The Fejér kernel has $L^1$ norm one

Let $T > 0$. For every $N \in \mathbb{N}$, the
$N$-th Fejér kernel $K_N$ on $\mathbb{R}/T\mathbb{Z}$ satisfies

$$\int_{\mathbb{R}/T\mathbb{Z}} |K_N(t)|\, dt = 1,$$

where $dt$ is the Haar probability measure on the circle.

Since $K_N \ge 0$, this is the normalization $\int K_N = 1$; it is used to control
convolutions with $K_N$ in the proof of Fejér's theorem.

Formalized by `AddCircle.integral_norm_fejerKernel`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/CesaroMean.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/CesaroMean.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#integral-norm-fejer-kernel).

## Quantitative Fejér theorem

Let $T > 0$, let $f$ be a continuous complex-valued function
on the circle $\mathbb{R}/T\mathbb{Z}$, and write $\sigma_N f$ for its $N$-th Cesàro–Fourier
mean. Let $\varepsilon > 0$ and $\delta > 0$ be such that $|f(a) - f(b)| < \varepsilon / 2$ for
all points $a, b$ of the circle at distance less than $\delta$. Then there is
$N_0 \in \mathbb{N}$ such that $|f(x) - \sigma_N f(x)| < \varepsilon$ for every $N \ge N_0$ and
every point $x$ of the circle.

The proof writes $f(x) - \sigma_N f(x) = \int K_N(t)\,(f(x) - f(x - t))\,dt$, where $K_N$ is the
$N$-th Fejér kernel and the integral is against the Haar probability measure, and splits it
into the points $t$ at distance less than $\delta$ from $0$, where $f(x) - f(x - t)$ is small,
and the remaining points, where the Fejér kernel is $O(1/((N+1)\delta^2))$.

Formalized by `AddCircle.cesaroMean_uniform_bound`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/FejerTheorem.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FejerTheorem.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#cesaro-mean-uniform-bound).

## Fejér's theorem: uniform convergence of Cesàro–Fourier means

Let $T > 0$ and let $f$ be
a continuous complex-valued function on the circle $\mathbb{R}/T\mathbb{Z}$ (equivalently, a
continuous $T$-periodic function on $\mathbb{R}$). Then the Cesàro–Fourier means $\sigma_N f$
converge to $f$ uniformly on the circle as $N \to \infty$.

Formalized by `AddCircle.fejer_uniform_convergence`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/FejerTheorem.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/FejerTheorem.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html#fejer-uniform-convergence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fejér kernel and Fejér's theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/harmonic-analysis/fourier-series/fej-r-kernel-and-fej-r-s-theorem)
