---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Fourier.FastFourierTransformWanted.dftSum, MathlibExt.Analysis.Fourier.FastFourierTransformWanted.dftSum_two_mul, MathlibExt.Analysis.Fourier.FastFourierTransformWanted.dftSum_mod, MathlibExt.Analysis.Fourier.FastFourierTransformWanted.cooley_tukey, MathlibExt.Analysis.Fourier.FastFourierTransformWanted.fftCost, MathlibExt.Analysis.Fourier.FastFourierTransformWanted.fftCost_recurrence, Cslib.Algorithms.Lean.TimeM.fftSplit, Cslib.Algorithms.Lean.TimeM.fftButterfly
statement: formalized
proof: formalized
---

# Fast Fourier transform

90 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html).

## Discrete Fourier sum

For a natural number $N$, a complex number $\omega$, a sequence
$f : \mathbb{N} \to \mathbb{C}$ and a natural number $k$, the unnormalized discrete Fourier sum of
length $N$ at frequency $k$ is $\sum_{j=0}^{N-1} \omega^{jk} f(j)$.

No condition is placed on $\omega$; the usual DFT takes $\omega = e^{-2\pi i/N}$.

Formalized by `MathlibExt.Analysis.Fourier.FastFourierTransformWanted.dftSum`, a definition declared in [MathlibExt/Analysis/Fourier/FastFourierTransform.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FastFourierTransform.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#dft-sum).

## Even–odd splitting of the DFT sum

For every natural number $n$, every
$\omega \in \mathbb{C}$, every $f : \mathbb{N} \to \mathbb{C}$ and every natural number $K$,

$$\sum_{j < 2n} \omega^{jK} f(j) = \sum_{t < n} (\omega^2)^{tK} f(2t)
  + \omega^K \sum_{t < n} (\omega^2)^{tK} f(2t + 1).$$

Formalized by `MathlibExt.Analysis.Fourier.FastFourierTransformWanted.dftSum_two_mul`, a theorem declared in [MathlibExt/Analysis/Fourier/FastFourierTransform.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FastFourierTransform.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#dft-sum-two-mul).

## The DFT sum at a root of unity depends only on the frequency modulo the length

Let $n$
be a natural number and let $\omega \in \mathbb{C}$ satisfy $\omega^n = 1$. Then for every
$f : \mathbb{N} \to \mathbb{C}$ and every natural number $K$, the discrete Fourier sum of length $n$
at frequency $K$ equals the one at frequency $K \bmod n$:

$$\sum_{j < n} \omega^{jK} f(j) = \sum_{j < n} \omega^{j (K \bmod n)} f(j),$$

where $K \bmod n$ is the remainder of $K$ on division by $n$ (with $K \bmod 0 = K$).

Formalized by `MathlibExt.Analysis.Fourier.FastFourierTransformWanted.dftSum_mod`, a theorem declared in [MathlibExt/Analysis/Fourier/FastFourierTransform.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FastFourierTransform.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#dft-sum-mod).

## Radix-2 Cooley–Tukey splitting

For $\omega \in \mathbb{C}$, $f : \mathbb{N} \to \mathbb{C}$
and natural numbers $N$ and $k$, write $D_N(\omega, f, k) = \sum_{j < N} \omega^{jk} f(j)$ for the
discrete Fourier sum. Let $n$ be a natural number and let $\omega \in \mathbb{C}$ satisfy
$\omega^{2n} = 1$. Then for every $f : \mathbb{N} \to \mathbb{C}$ and every natural number $K$,

$$D_{2n}(\omega, f, K) = D_n(\omega^2, f_0, K \bmod n)
  + \omega^K D_n(\omega^2, f_1, K \bmod n),$$

where $f_0(t) = f(2t)$, $f_1(t) = f(2t + 1)$, and $K \bmod n$ is the remainder of $K$ on division
by $n$ (with $K \bmod 0 = K$). So a length-$2n$ transform is two length-$n$ transforms on the
even and odd samples, combined with the twiddle factor $\omega^K$.

Proof: Split the range into even and odd indices, rewrite the powers, and use
root-of-unity periodicity to reduce the frequency modulo $n$, as in the
section "The radix-2 DIT case" of Wikipedia, "Cooley–Tukey FFT algorithm".

## Sources

- J. W. Cooley and J. W. Tukey, Math. Comp. 19 (1965) (decimation in time).

Formalized by `MathlibExt.Analysis.Fourier.FastFourierTransformWanted.cooley_tukey`, a theorem declared in [MathlibExt/Analysis/Fourier/FastFourierTransform.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FastFourierTransform.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#cooley-tukey).

## FFT operation count

For a natural number $n$, the closed-form FFT operation count is
$n \lfloor \log_2 n \rfloor$, where $\lfloor \log_2 n \rfloor$ is the largest $m$ with $2^m \le n$
(taken to be $0$ when $n = 0$).

Formalized by `MathlibExt.Analysis.Fourier.FastFourierTransformWanted.fftCost`, a definition declared in [MathlibExt/Analysis/Fourier/FastFourierTransform.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FastFourierTransform.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-cost).

## The FFT cost satisfies the radix-2 recurrence

Let $C(n) = n \lfloor \log_2 n \rfloor$ be the
closed-form FFT operation count. For every natural number $n > 0$, $C(2n) = 2\,C(n) + 2n$.

Proof: Since $n > 0$, $\lfloor \log_2 (2n) \rfloor = \lfloor \log_2 n \rfloor + 1$; expand the
product.

## Sources

- J. W. Cooley and J. W. Tukey, Math. Comp. 19 (1965) (`n log n` operation count).

Formalized by `MathlibExt.Analysis.Fourier.FastFourierTransformWanted.fftCost_recurrence`, a theorem declared in [MathlibExt/Analysis/Fourier/FastFourierTransform.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FastFourierTransform.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-cost-recurrence).

## Even–odd split for the FFT

For a commutative ring $R$, a natural number $m$ and a vector
$x = (x_0, \dots, x_{2m-1}) \in R^{2m}$, the split returns the pair of vectors
$(x_0, x_2, \dots, x_{2m-2})$ and $(x_1, x_3, \dots, x_{2m-1})$ in $R^m$ of the entries of $x$ at
even and at odd indices, in order, at a time cost of $4m$ (the charged reads and writes).

Formalized by `Cslib.Algorithms.Lean.TimeM.fftSplit`, a definition declared in [CSLibExt/Algorithms/Lean/Fourier/FFT.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-split).

## One FFT butterfly

For a commutative ring $R$, an element $\omega \in R$, vectors
$q, r \in R^m$, a state $(w, y)$ with $w \in R$ and $y \in R^{2m}$, and an index $k < m$, the
butterfly at $k$ returns the state $(w \omega, y')$, where $y'$ is obtained from $y$ by setting
entry $k$ to $q_k + w r_k$ and entry $k + m$ to $q_k - w r_k$, at a time cost of $8$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftButterfly`, a definition declared in [CSLibExt/Algorithms/Lean/Fourier/FFT.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-butterfly).

## FFT butterfly pass

For a commutative ring $R$, an element $\omega \in R$ and vectors
$q, r \in R^m$ and $y \in R^{2m}$, the butterfly pass starts from the state $(1, y)$, applies the
FFT butterfly with $\omega$, $q$ and $r$ at the indices $k = 0, 1, \dots, m - 1$ in increasing
order, and returns the final state; its time cost is the sum of the costs of these $m$
butterflies.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftButterflies`, a definition declared in [CSLibExt/Algorithms/Lean/Fourier/FFT.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-butterflies).

## Radix-two fast Fourier transform

For a commutative ring $R$, a natural number $d$, an
element $\omega \in R$ and a vector $x \in R^{2^d}$, the FFT of $x$ with root $\omega$ is defined
by recursion on $d$. For $d = 0$ it returns $x$ at cost $0$. For $d + 1$ it splits $x$ into its
even- and odd-indexed subvectors $e, o \in R^{2^d}$ (cost $4 \cdot 2^d$), computes $\omega^2$
(cost $1$), computes the FFTs $q$ of $e$ and $r$ of $o$ with root $\omega^2$, writes a zero vector
$y \in R^{2^{d+1}}$ (cost $2^{d+1}$), and returns the vector part of the result of the butterfly
pass with $\omega$, $q$ and $r$ on $y$. Its time cost is the sum of the costs of all these steps.

The two transformed halves are stored once and combined with a running twiddle factor. No
assumption on $\omega$ is needed to run the algorithm; one is needed only for its correctness.

Formalized by `Cslib.Algorithms.Lean.TimeM.fft`, a definition declared in [CSLibExt/Algorithms/Lean/Fourier/FFT.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft).

## Radix-two FFT on arrays

Let $R$ be a commutative ring, $\omega \in R$ and $x$ an array
over $R$ of length $n$, and let $d = \lfloor \log_2 n \rfloor$ (with $d = 0$ when $n = 0$). If
$n = 2^d$, the array FFT runs the radix-two FFT with root $\omega$ on $x$, viewed as a vector of
length $2^d$, and returns its output as an array, with the cost of that run. Otherwise it returns
no result, at cost $0$; the length check itself is free.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftArray`, a definition declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Array.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Array.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-array).

## The array FFT rejects exactly the non-powers of two

Let $R$ be a commutative ring,
$\omega \in R$ and $x$ an array over $R$. The array FFT of $x$ with root $\omega$ returns no
result if and only if the length of $x$ is different from $2^d$ for every natural number $d$.

In particular the empty array is rejected and an array of length $1 = 2^0$ is accepted.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftArray_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Array.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Array.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-array-eq-none-iff).

## Lower write of a butterfly step

Let $R$ be a commutative ring, $\omega \in R$, $m$ a
natural number, $q, r$ vectors over $R$ of length $m$, $w \in R$ a twiddle, $o$ an output vector
over $R$ of length $2m$, and $k < m$. Then the butterfly step at index $k$ applied to the state
$(w, o)$ produces an output vector whose entry at index $k$ is $q_k + w r_k$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftButterfly_ret_low`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Butterfly.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Butterfly.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-butterfly-ret-low).

## Upper write of a butterfly step

Let $R$ be a commutative ring, $\omega \in R$, $m$ a
natural number, $q, r$ vectors over $R$ of length $m$, $w \in R$ a twiddle, $o$ an output vector
over $R$ of length $2m$, and $k < m$. Then the butterfly step at index $k$ applied to the state
$(w, o)$ produces an output vector whose entry at index $k + m$ is $q_k - w r_k$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftButterfly_ret_high`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Butterfly.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Butterfly.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-butterfly-ret-high).

## A butterfly step leaves other entries unchanged

Let $R$ be a commutative ring,
$\omega \in R$, $m$ a natural number, $q, r$ vectors over $R$ of length $m$, $w \in R$ a twiddle,
$o$ an output vector over $R$ of length $2m$, and $k < m$. Then for every index $i < 2m$ with
$i \ne k$ and $i \ne k + m$, the butterfly step at index $k$ applied to the state $(w, o)$
produces an output vector whose entry at index $i$ is $o_i$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftButterfly_ret_other`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Butterfly.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Butterfly.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-butterfly-ret-other).

## Result of the butterfly loop

Let $R$ be a commutative ring, $\omega \in R$, $m$ a natural
number, $q = (q_0, \dots, q_{m-1})$ and $r = (r_0, \dots, r_{m-1})$ vectors over $R$, and $o$ a
vector over $R$ of length $2m$. The butterfly loop with root $\omega$ on $q$ and $r$, started
from twiddle $1$ and output vector $o$, ends with twiddle $\omega^m$ and an output vector $y$
such that $y_k = q_k + \omega^k r_k$ and $y_{k+m} = q_k - \omega^k r_k$ for every $k < m$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftButterflies_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Butterfly.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Butterfly.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-butterflies-ret).

## The FFT split extracts the even-indexed entries

Let $R$ be a type, $m$ a natural number
and $x = (x_0, \dots, x_{2m-1})$ a vector of length $2m$ over $R$. For every $k < m$, entry $k$
of the first (even) vector returned by the FFT split of $x$ is $x_{2k}$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftSplit_ret_even`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Correctness.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Correctness.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-split-ret-even).

## The FFT split extracts the odd-indexed entries

Let $R$ be a type, $m$ a natural number
and $x = (x_0, \dots, x_{2m-1})$ a vector of length $2m$ over $R$. For every $k < m$, entry $k$
of the second (odd) vector returned by the FFT split of $x$ is $x_{2k+1}$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftSplit_ret_odd`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Correctness.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Correctness.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-split-ret-odd).

## The FFT of depth zero returns its input

Let $R$ be a commutative ring. For every
$\omega \in R$ and every vector $x \in R^{2^0}$, the vector returned by the radix-two FFT of
depth $0$ with root $\omega$ on $x$ is $x$ itself.

Formalized by `Cslib.Algorithms.Lean.TimeM.fft_ret_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Correctness.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Correctness.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-ret-zero).

## Low half of the FFT butterfly recurrence

Let $R$ be a commutative ring, $d$ a natural
number, $\omega \in R$ and $x \in R^{2^{d+1}}$, with entries indexed from $0$. Let
$e, o \in R^{2^d}$ be the even- and odd-indexed subsequences of $x$ returned by the FFT split,
and let $E$ and $O$ be the vectors returned by the radix-two FFT of depth $d$ with root
$\omega \cdot \omega$ on $e$ and on $o$. Then for every $k < 2^d$, entry $k$ of the vector
returned by the radix-two FFT of depth $d + 1$ with root $\omega$ on $x$ equals
$E_k + \omega^k O_k$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fft_ret_succ_low`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Correctness.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Correctness.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-ret-succ-low).

## High half of the FFT butterfly recurrence

Let $R$ be a commutative ring, $d$ a natural
number, $\omega \in R$ and $x \in R^{2^{d+1}}$, with entries indexed from $0$. Let
$e, o \in R^{2^d}$ be the even- and odd-indexed subsequences of $x$ returned by the FFT split,
and let $E$ and $O$ be the vectors returned by the radix-two FFT of depth $d$ with root
$\omega \cdot \omega$ on $e$ and on $o$. Then for every $k < 2^d$, entry $k + 2^d$ of the
vector returned by the radix-two FFT of depth $d + 1$ with root $\omega$ on $x$ equals
$E_k - \omega^k O_k$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fft_ret_succ_high`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Correctness.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Correctness.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-ret-succ-high).

## Cost of the FFT even/odd split

For every natural number $m$ and every vector $x$ of length
$2m$, splitting $x$ into its even-indexed and its odd-indexed subsequences costs exactly $4m$
charged operations: two reads and two writes for each of the $m$ even/odd pairs.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftSplit_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Cost.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Cost.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-split-time).

## Cost of one FFT butterfly

Let $R$ be a commutative ring and $m$ a natural number. For every
$\omega \in R$, all vectors $q, r \in R^m$, every current twiddle $w \in R$ and output vector of
length $2m$ over $R$, and every index $k < m$, one butterfly step costs exactly $8$ charged
operations: two reads, four scalar operations and two writes.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftButterfly_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Cost.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Cost.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-butterfly-time).

## Cost of the FFT butterfly pass

Let $R$ be a commutative ring and $m$ a natural number. For
every $\omega \in R$, all vectors $q, r \in R^m$ and every output vector of length $2m$ over $R$,
the pass that, starting from twiddle $1$, applies one butterfly for each index $k < m$ in
increasing order costs exactly $8m$ charged operations.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftButterflies_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Cost.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Cost.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-butterflies-time).

## Exact cost of the radix-two FFT

Let $R$ be a commutative ring. For every natural number
$d$, every $\omega \in R$ and every vector $x \in R^{2^d}$, the radix-two FFT of $x$ with root
$\omega$ costs $T$ charged operations, where $T + 1 = (7d + 1) \cdot 2^d$; that is,
$T = (7d + 1) \cdot 2^d - 1$.

The count includes the charged reads and writes of the even/odd splits and the writes that
initialize each output vector.

Formalized by `Cslib.Algorithms.Lean.TimeM.fft_time_add_one`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Cost.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Cost.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-time-add-one).

## Exact cost of the radix-two FFT in terms of the input length

Let $R$ be a commutative
ring. For every natural number $d$, every $\omega \in R$ and every vector $x$ over $R$ of length
$n = 2^d$, the radix-two FFT of $x$ with root $\omega$ costs $T$ charged operations, where
$T + 1 = (7 \log_2 n + 1) \cdot n$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fft_time_add_one_log2`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Cost.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Cost.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-time-add-one-log2).

## Cost bound for the radix-two FFT

Let $R$ be a commutative ring. For every natural number
$d$, every $\omega \in R$ and every vector $x \in R^{2^d}$, the radix-two FFT of $x$ with root
$\omega$ costs at most $8 \cdot 2^d \cdot d$ charged operations, that is, at most eight per entry
per recursion level.

Formalized by `Cslib.Algorithms.Lean.TimeM.fft_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Cost.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Cost.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-time-le).

## Correctness of the radix-two FFT

For every natural number $d$, every primitive $2^d$-th
root of unity $\omega \in \mathbb{C}$, every vector $x = (x_0, \dots, x_{2^d - 1})$ in
$\mathbb{C}^{2^d}$ and every $k < 2^d$, the $k$-th entry of the radix-two FFT of $x$ with root
$\omega$ equals the discrete Fourier sum $\sum_{j=0}^{2^d - 1} \omega^{jk} x_j$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fft_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/DFTCorrectness.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/DFTCorrectness.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-correct).

## The array FFT agrees with the vector FFT

Let $R$ be a commutative ring, $d$ a natural
number, $\omega \in R$ and $x$ a vector over $R$ of length $2^d$. Then the array FFT of $x$,
viewed as an array, with root $\omega$ returns a result, namely the output of the radix-two FFT
of the length-$2^d$ vector $x$ with root $\omega$, viewed as an array.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftArray_ret_of_vector`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/ArrayCorrectness.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/ArrayCorrectness.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-array-ret-of-vector).

## The array FFT costs the same as the vector FFT

Let $R$ be a commutative ring, $d$ a
natural number, $\omega \in R$ and $x$ a vector over $R$ of length $2^d$. Then the cost of the
array FFT of $x$, viewed as an array, with root $\omega$ equals the cost of the radix-two FFT of
the length-$2^d$ vector $x$ with root $\omega$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftArray_time_of_vector`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/ArrayCorrectness.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/ArrayCorrectness.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-array-time-of-vector).

## The array FFT computes the discrete Fourier transform

Let $d$ be a natural number,
$\omega \in \mathbb{C}$ a primitive $2^d$-th root of unity, $x_0, \dots, x_{2^d - 1}$ complex
numbers and $k < 2^d$. Then the array FFT of the array $(x_0, \dots, x_{2^d - 1})$ with root
$\omega$ returns an array $y$ of length $2^d$ whose entry at index $k$ is the discrete Fourier
sum $\sum_{j=0}^{2^d - 1} \omega^{jk} x_j$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftArray_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/ArrayCorrectness.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/ArrayCorrectness.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-array-correct).

## Exact cost of the array FFT

Let $R$ be a commutative ring, $d$ a natural number,
$\omega \in R$ and $x$ a vector over $R$ of length $2^d$. Then the cost $T$ of the array FFT of
$x$, viewed as an array, with root $\omega$ satisfies $T + 1 = (7d + 1) \cdot 2^d$.

Costs are counted in the scalar-operation and array-access model of the radix-two FFT.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftArray_time_add_one`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/ArrayCorrectness.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/ArrayCorrectness.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-array-time-add-one).

## The radix-two FFT with root $e^{-2\pi i/n}$ computes the DFT

Let $n = 2^d$ and let
$x_0, \dots, x_{n-1}$ be complex numbers, indexed by $\mathbb{Z}/n\mathbb{Z}$. Run the radix-two
FFT on $x$ with sample root $\omega = e^{-2\pi i/n}$, the value at $-1$ of the standard additive
character of $\mathbb{Z}/n\mathbb{Z}$. Then for every $k < n$, entry $k$ of the returned vector
equals the discrete Fourier transform coefficient
$\sum_{j \in \mathbb{Z}/n\mathbb{Z}} e^{-2\pi i jk/n} x_j$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fft_stdAddChar_neg_one`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/CanonicalDFT.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/CanonicalDFT.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-std-add-char-neg-one).

## The radix-two FFT with root $e^{2\pi i/n}$, divided by $n$, computes the inverse DFT

Let
$n = 2^d$ and let $x_0, \dots, x_{n-1}$ be complex numbers, indexed by $\mathbb{Z}/n\mathbb{Z}$.
Run the radix-two FFT on $x$ with sample root $\omega = e^{2\pi i/n}$, the value at $1$ of the
standard additive character of $\mathbb{Z}/n\mathbb{Z}$. Then for every $k < n$, entry $k$ of
the returned vector multiplied by $1/n$ equals the inverse discrete Fourier transform coefficient
$\frac{1}{n} \sum_{j \in \mathbb{Z}/n\mathbb{Z}} e^{2\pi i jk/n} x_j$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fft_stdAddChar_one_normalized`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/CanonicalDFT.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/CanonicalDFT.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-std-add-char-one-normalized).

## Charged entrywise conjugation

For a type with a star operation $z \mapsto \bar z$ and a
vector $x = (x_0, \dots, x_{n-1})$ of length $n$ over it, this costed computation returns
$(\bar x_0, \dots, \bar x_{n-1})$ and charges $3n$ operations: one read, one conjugation and one
write per entry.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftConjugate`, a definition declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Inverse.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Inverse.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-conjugate).

## Charged entrywise scaling

For a type with a multiplication, a scalar $c$ and a vector
$x = (x_0, \dots, x_{n-1})$ of length $n$ over it, this costed computation returns
$(c x_0, \dots, c x_{n-1})$ and charges $3n$ operations: one read, one multiplication and one
write per entry.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftScale`, a definition declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Inverse.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Inverse.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-scale).

## Inverse FFT by conjugation

Let $R$ be a field that is a star ring, with star operation
$z \mapsto \bar z$. For a natural number $d$, an element $\omega \in R$ and a vector
$x \in R^{2^d}$, the inverse FFT conjugates every entry of $x$, applies the radix-two FFT with
root $\omega$, conjugates every entry of the result, and multiplies every entry by the inverse
$(2^d)^{-1}$ of $2^d$ in $R$ (which is $0$ when $2^d = 0$ in $R$). It charges $3 \cdot 2^d$
operations for each of the two conjugation passes and for the scaling pass, one operation for
computing $(2^d)^{-1}$, and the cost of the FFT.

Formalized by `Cslib.Algorithms.Lean.TimeM.ifft`, a definition declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Inverse.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Inverse.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#ifft).

## Timed pointwise product

For a type $R$ with a multiplication and vectors $x, y$ of
length $n$ over $R$, the pointwise product returns the vector of length $n$ whose $i$-th entry
is $x_i \cdot y_i$ for every $i < n$, and charges $4n$ time units: two reads, one multiplication
and one write per entry.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftPointwise`, a definition declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Convolution.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Convolution.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-pointwise).

## Zero padding to twice the length

For a type $R$ with a zero, a natural number $d$ and a
vector $x$ of length $2^d$ over $R$, padding returns the vector of length $2^{d+1}$ whose $i$-th
entry is $x_i$ for $i < 2^d$ and $0$ for $2^d \le i < 2^{d+1}$, and charges $3 \cdot 2^d$ time
units.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftPad`, a definition declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Convolution.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Convolution.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-pad).

## FFT circular convolution

Let $R$ be a field that is a star ring, $d$ a natural number,
$\omega \in R$, and $x, y$ vectors of length $2^d$ over $R$. Circular convolution runs the timed
radix-two FFT of length $2^d$ with root $\omega$ on $x$ and then on $y$, multiplies the two
transforms pointwise, and applies the timed inverse FFT of length $2^d$ with root $\omega$ to the
product. It returns the result of the inverse transform, and its cost is the sum of the costs of
these four steps.

The definition imposes no condition on $\omega$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftCircular`, a definition declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Convolution.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Convolution.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-circular).

## FFT linear convolution

Let $R$ be a field that is a star ring, $d$ a natural number,
$\omega \in R$, and $x, y$ vectors of length $2^d$ over $R$. Linear convolution zero-pads $x$ and
$y$ to length $2^{d+1}$ and returns the FFT circular convolution of the two padded vectors at
length $2^{d+1}$ with root $\omega$. Its cost is the cost of the two paddings plus the cost of
the circular convolution.

The root $\omega$ is used for the padded length $2^{d+1}$, twice the input length.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftLinear`, a definition declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Convolution.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Convolution.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-linear).

## FFT circular convolution on arrays

Let $R$ be a field that is a star ring, $\omega \in R$,
and $x, y$ arrays over $R$, where $x$ has length $n$. If $n = 2^d$ for some natural number $d$
and $y$ also has length $n$, the procedure returns the FFT circular convolution of $x$ and $y$
(read as vectors of length $2^d$) with root $\omega$, converted to an array, at the cost of that
convolution. Otherwise it returns no result, at cost $0$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftCircularArray`, a definition declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Convolution.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Convolution.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-circular-array).

## FFT linear convolution on arrays

Let $R$ be a field that is a star ring, $\omega \in R$,
and $x, y$ arrays over $R$, where $x$ has length $n$. If $n = 2^d$ for some natural number $d$
and $y$ also has length $n$, the procedure returns the FFT linear convolution of $x$ and $y$
(read as vectors of length $2^d$) with root $\omega$, an array of length $2n$, at the cost of
that convolution. Otherwise it returns no result, at cost $0$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftLinearArray`, a definition declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Convolution.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Convolution.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-linear-array).

## Entries of the pointwise product

Let $R$ be a type with a multiplication, let $n$ be a
natural number and let $x$ and $y$ be vectors of length $n$ over $R$. For every index $i < n$,
entry $i$ of the pointwise product of $x$ and $y$ equals $x_i y_i$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftPointwise_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionCharacteristic.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionCharacteristic.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-pointwise-ret).

## Zero padding keeps the input prefix

Let $R$ be a type with a zero, let $d$ be a natural
number and let $x$ be a vector of length $2^d$ over $R$. For every index $i < 2^d$, entry $i$
of the zero-padded vector of length $2^{d+1}$ produced from $x$ equals $x_i$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftPad_ret_low`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionCharacteristic.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionCharacteristic.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-pad-ret-low).

## Zero padding fills the second half with zeros

Let $R$ be a type with a zero, let $d$
be a natural number and let $x$ be a vector of length $2^d$ over $R$. For every index $i$ with
$2^d \le i < 2^{d+1}$, entry $i$ of the zero-padded vector of length $2^{d+1}$ produced from
$x$ is $0$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftPad_ret_high`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionCharacteristic.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionCharacteristic.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-pad-ret-high).

## Rejection by array circular convolution

Let $R$ be a field with a star-ring
structure, let $\omega \in R$, and let $x$ and $y$ be arrays over $R$. The array
circular-convolution procedure with root $\omega$ returns no result on $x$ and $y$ if and only
if it is not the case that the length of $x$ is a power of two $2^k$ with $k \ge 0$ and $y$ has
the same length as $x$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftCircularArray_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionCharacteristic.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionCharacteristic.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-circular-array-eq-none-iff).

## Rejection by array linear convolution

Let $R$ be a field with a star-ring structure,
let $\omega \in R$, and let $x$ and $y$ be arrays over $R$. The array zero-padded
linear-convolution procedure with root $\omega$ returns no result on $x$ and $y$ if and only if
it is not the case that the length of $x$ is a power of two $2^k$ with $k \ge 0$ and $y$ has the
same length as $x$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftLinearArray_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionCharacteristic.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionCharacteristic.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-linear-array-eq-none-iff).

## Conjugating around the FFT conjugates the root

Let $N = 2^d$, let $\omega \in \mathbb{C}$
be a primitive $N$-th root of unity and let $x \in \mathbb{C}^N$. Conjugating every entry of $x$,
running the FFT procedure with root $\omega$ and conjugating every entry of the result gives the
same vector as running the FFT procedure on $x$ with root $\overline{\omega}$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fft_conjugate_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/InverseCorrectness.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/InverseCorrectness.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-conjugate-ret).

## The inverse FFT is a normalized FFT at the conjugate root

Let $N = 2^d$, let
$\omega \in \mathbb{C}$ be a primitive $N$-th root of unity and let $x \in \mathbb{C}^N$. The
output of the inverse FFT procedure on $x$ with root $\omega$ is the output of the FFT procedure
on $x$ with root $\overline{\omega}$ with every entry multiplied by $N^{-1}$.

Formalized by `Cslib.Algorithms.Lean.TimeM.ifft_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/InverseCorrectness.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/InverseCorrectness.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#ifft-ret).

## Correctness of the inverse FFT

Let $N = 2^d$, let $\omega \in \mathbb{C}$ be a primitive
$N$-th root of unity and let $x \in \mathbb{C}^N$. For every $k < N$, entry $k$ of the output of
the inverse FFT procedure on $x$ with root $\omega$ equals $N^{-1}$ times the discrete Fourier sum
of length $N$ with root $\overline{\omega}$ at frequency $k$ of the sequence $j \mapsto x_j$ (set
to $0$ for $j \ge N$), that is, $N^{-1} \sum_{j=0}^{N-1} \overline{\omega}^{jk} x_j$.

Formalized by `Cslib.Algorithms.Lean.TimeM.ifft_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/InverseCorrectness.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/InverseCorrectness.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#ifft-correct).

## Inverse FFT at the negative-sign root computes the inverse DFT

Let $N = 2^d$ and
$x \in \mathbb{C}^N$, and run the inverse FFT procedure on $x$ with root $e^{-2\pi i/N}$, the value
at $-1$ of the standard additive character of $\mathbb{Z}/N\mathbb{Z}$. For every $k < N$, entry $k$
of its output equals the canonical inverse discrete Fourier transform of the function on
$\mathbb{Z}/N\mathbb{Z}$ sending the class of $j < N$ to $x_j$, evaluated at the class of $k$;
that is, it equals $N^{-1} \sum_{j=0}^{N-1} e^{2\pi i jk/N} x_j$.

Formalized by `Cslib.Algorithms.Lean.TimeM.ifft_stdAddChar_neg_one`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/InverseCanonicalDFT.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/InverseCanonicalDFT.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#ifft-std-add-char-neg-one).

## Inverse FFT at the positive-sign root computes the normalized forward DFT

Let $N = 2^d$
and $x \in \mathbb{C}^N$, and run the inverse FFT procedure on $x$ with root $e^{2\pi i/N}$, the
value at $1$ of the standard additive character of $\mathbb{Z}/N\mathbb{Z}$. For every $k < N$,
entry $k$ of its output equals $N^{-1}$ times the canonical discrete Fourier transform of the
function on $\mathbb{Z}/N\mathbb{Z}$ sending the class of $j < N$ to $x_j$, evaluated at the class
of $k$; that is, it equals $N^{-1} \sum_{j=0}^{N-1} e^{-2\pi i jk/N} x_j$.

Formalized by `Cslib.Algorithms.Lean.TimeM.ifft_stdAddChar_one`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/InverseCanonicalDFT.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/InverseCanonicalDFT.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#ifft-std-add-char-one).

## Inverse FFT after FFT is the identity at the negative-sign root

Let $N = 2^d$ and let
$\omega = e^{-2\pi i/N}$, the value at $-1$ of the standard additive character of
$\mathbb{Z}/N\mathbb{Z}$. For every $x \in \mathbb{C}^N$, running the FFT procedure on $x$ with
root $\omega$ and then the inverse FFT procedure on its output with root $\omega$ returns $x$.

Formalized by `Cslib.Algorithms.Lean.TimeM.ifft_fft_stdAddChar_neg_one`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/InverseCanonicalDFT.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/InverseCanonicalDFT.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#ifft-fft-std-add-char-neg-one).

## FFT after inverse FFT is the identity at the negative-sign root

Let $N = 2^d$ and let
$\omega = e^{-2\pi i/N}$, the value at $-1$ of the standard additive character of
$\mathbb{Z}/N\mathbb{Z}$. For every $x \in \mathbb{C}^N$, running the inverse FFT procedure on $x$
with root $\omega$ and then the FFT procedure on its output with root $\omega$ returns $x$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fft_ifft_stdAddChar_neg_one`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/InverseCanonicalDFT.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/InverseCanonicalDFT.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-ifft-std-add-char-neg-one).

## Output of FFT circular convolution

Let $R$ be a field with a star-ring conjugation, let
$n = 2^d$, $\omega \in R$ and $x, y \in R^n$. The vector returned by FFT circular convolution of
$x$ and $y$ with root $\omega$ equals the vector returned by the inverse FFT with root $\omega$
applied to the vector returned by pointwise multiplication of $\hat{x}$ and $\hat{y}$, where
$\hat{x}$ and $\hat{y}$ are the vectors returned by the radix-two FFT of $x$ and of $y$ with
root $\omega$.

Only returned values are compared; operation counts are not.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftCircular_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/CircularCorrectness.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/CircularCorrectness.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-circular-ret).

## Output of FFT linear convolution

Let $R$ be a field with a star-ring conjugation, let
$\omega \in R$ and $x, y \in R^{2^d}$. The vector returned by FFT linear convolution of $x$ and
$y$ with root $\omega$ equals the vector returned by FFT circular convolution, at length
$2^{d+1}$ with root $\omega$, of the vectors returned by zero-padding $x$ and $y$ to length
$2^{d+1}$.

Only returned values are compared; operation counts are not.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftLinear_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/CircularCorrectness.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/CircularCorrectness.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-linear-ret).

## FFT circular convolution with root $e^{-2\pi i/n}$ computes the cyclic convolution

Let
$n = 2^d$ and $x, y \in \mathbb{C}^n$. Run FFT circular convolution of $x$ and $y$ with root
$\omega = e^{-2\pi i/n}$, the value at $-1$ of the standard additive character of
$\mathbb{Z}/n\mathbb{Z}$. Then for every $k < n$, entry $k$ of the returned vector equals
$\sum_{j \in \mathbb{Z}/n\mathbb{Z}} x_j \, y_{k - j}$, with indices taken modulo $n$.

This root is the sign convention of the Princeton (Sedgewick–Wayne) source.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftCircular_stdAddChar_neg_one`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/CircularCorrectness.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/CircularCorrectness.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-circular-std-add-char-neg-one).

## FFT circular convolution with root $e^{2\pi i/n}$ computes the cyclic convolution

Let
$n = 2^d$ and $x, y \in \mathbb{C}^n$. Run FFT circular convolution of $x$ and $y$ with root
$\omega = e^{2\pi i/n}$, the value at $1$ of the standard additive character of
$\mathbb{Z}/n\mathbb{Z}$. Then for every $k < n$, entry $k$ of the returned vector equals
$\sum_{j \in \mathbb{Z}/n\mathbb{Z}} x_j \, y_{k - j}$, with indices taken modulo $n$.

This root is the sign convention of the MIT and CLRS sources.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftCircular_stdAddChar_one`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/CircularCorrectness.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/CircularCorrectness.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-circular-std-add-char-one).

## Exact operation count of the inverse FFT

Let $R$ be a field with a star ring structure,
let $d$ be a natural number, $N = 2^d$, $\omega \in R$ arbitrary and $x \in R^N$. The number $T$ of
operations charged by the inverse FFT procedure on $x$ with root $\omega$ satisfies
$T + 1 = (7d + 10) \cdot 2^d + 1$, equivalently $T = (7d + 10) \cdot 2^d$.

Beyond the FFT, the two conjugation passes and the scaling pass each charge $3N$ operations and
computing $1/N$ charges one, for $9N + 1$ in total.

Formalized by `Cslib.Algorithms.Lean.TimeM.ifft_time_add_one`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/InverseCost.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/InverseCost.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#ifft-time-add-one).

## Operation bound for the inverse FFT

Let $R$ be a field with a star ring structure, let
$d$ be a natural number, $N = 2^d$, $\omega \in R$ arbitrary and $x \in R^N$. The number of
operations charged by the inverse FFT procedure on $x$ with root $\omega$ is at most
$8 \cdot 2^d \cdot d + 9 \cdot 2^d + 1$.

Formalized by `Cslib.Algorithms.Lean.TimeM.ifft_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/InverseCost.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/InverseCost.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#ifft-time-le).

## Exact cost of FFT circular convolution

Let $R$ be a field with a star-ring structure,
let $d$ be a natural number, let $\omega \in R$, and let $x$ and $y$ be vectors of length $2^d$
over $R$. The cost charged by circular convolution of $x$ and $y$ with root $\omega$, plus $2$,
equals $(21d + 16) \cdot 2^d$.

The cost is the sum of the costs of the two forward transforms, the pointwise product and the
inverse transform.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftCircular_time_add_two`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionCost.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionCost.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-circular-time-add-two).

## Cost bound for FFT circular convolution

Let $R$ be a field with a star-ring structure,
let $d$ be a natural number, let $\omega \in R$, and let $x$ and $y$ be vectors of length $2^d$
over $R$. The cost charged by circular convolution of $x$ and $y$ with root $\omega$ is at most
$(21d + 16) \cdot 2^d$, that is, $21 n \log_2 n + 16 n$ for the input length $n = 2^d$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftCircular_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionCost.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionCost.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-circular-time-le).

## Exact cost of FFT linear convolution

Let $R$ be a field with a star-ring structure,
let $d$ be a natural number, let $\omega \in R$, and let $x$ and $y$ be vectors of length $2^d$
over $R$. The cost charged by zero-padded linear convolution of $x$ and $y$ with root $\omega$,
plus $2$, equals $(42d + 80) \cdot 2^d$.

The cost is that of zero padding both inputs to length $2^{d+1}$ plus that of circular
convolution at length $2^{d+1}$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftLinear_time_add_two`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionCost.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionCost.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-linear-time-add-two).

## Cost bound for FFT linear convolution

Let $R$ be a field with a star-ring structure,
let $d$ be a natural number, let $\omega \in R$, and let $x$ and $y$ be vectors of length $2^d$
over $R$. The cost charged by zero-padded linear convolution of $x$ and $y$ with root $\omega$
is at most $(42d + 80) \cdot 2^d$, that is, $42 n \log_2 n + 80 n$ for the input length
$n = 2^d$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftLinear_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionCost.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionCost.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-linear-time-le).

## Array circular FFT convolution agrees with the vector version

Let $R$ be a field
with a star-ring structure, let $d$ be a natural number, let $\omega \in R$ be arbitrary, and
let $x, y$ be vectors over $R$ of length $2^d$. Then array circular FFT convolution with root
$\omega$, run on the arrays underlying $x$ and $y$, succeeds and returns the array underlying
the output of vector circular FFT convolution of $x$ and $y$ at size $2^d$ with root $\omega$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftCircularArray_ret_of_vector`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionArrayCorrectness.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionArrayCorrectness.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-circular-array-ret-of-vector).

## Array circular FFT convolution costs the same as the vector version

Let $R$ be a
field with a star-ring structure, let $d$ be a natural number, let $\omega \in R$, and let
$x, y$ be vectors over $R$ of length $2^d$. The time charged by array circular FFT convolution
with root $\omega$ on the arrays underlying $x$ and $y$ equals the time charged by vector
circular FFT convolution of $x$ and $y$ at size $2^d$ with root $\omega$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftCircularArray_time_of_vector`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionArrayCorrectness.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionArrayCorrectness.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-circular-array-time-of-vector).

## Exact cost of array circular FFT convolution

Let $R$ be a field with a star-ring
structure, let $d$ be a natural number, let $\omega \in R$, and let $x, y$ be vectors over $R$
of length $2^d$. The time charged by array circular FFT convolution with root $\omega$ on the
arrays underlying $x$ and $y$, plus $2$, equals $(21d + 16) \cdot 2^d$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftCircularArray_time_add_two`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionArrayCorrectness.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionArrayCorrectness.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-circular-array-time-add-two).

## Output length of array circular FFT convolution

Let $R$ be a field with a star-ring
structure, let $\omega \in R$, and let $x, y$ be arrays over $R$. If array circular FFT
convolution with root $\omega$ on $x$ and $y$ returns an array $z$, then $z$ has the same
length as $x$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftCircularArray_size_of_eq_some`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionArrayCorrectness.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionArrayCorrectness.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-circular-array-size-of-eq-some).

## Array linear FFT convolution agrees with the vector version

Let $R$ be a field with
a star-ring structure, let $d$ be a natural number, let $\omega \in R$ be arbitrary, and let
$x, y$ be vectors over $R$ of length $2^d$. Then array zero-padded linear FFT convolution with
root $\omega$, run on the arrays underlying $x$ and $y$, succeeds and returns the array
underlying the output (of length $2^{d+1}$) of vector zero-padded linear FFT convolution of
$x$ and $y$ at size $2^d$ with root $\omega$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftLinearArray_ret_of_vector`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionArrayCorrectness.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionArrayCorrectness.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-linear-array-ret-of-vector).

## Array linear FFT convolution costs the same as the vector version

Let $R$ be a field
with a star-ring structure, let $d$ be a natural number, let $\omega \in R$, and let $x, y$ be
vectors over $R$ of length $2^d$. The time charged by array zero-padded linear FFT convolution
with root $\omega$ on the arrays underlying $x$ and $y$ equals the time charged by vector
zero-padded linear FFT convolution of $x$ and $y$ at size $2^d$ with root $\omega$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftLinearArray_time_of_vector`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionArrayCorrectness.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionArrayCorrectness.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-linear-array-time-of-vector).

## Exact cost of array linear FFT convolution

Let $R$ be a field with a star-ring
structure, let $d$ be a natural number, let $\omega \in R$, and let $x, y$ be vectors over $R$
of length $2^d$. The time charged by array zero-padded linear FFT convolution with root
$\omega$ on the arrays underlying $x$ and $y$, plus $2$, equals $(42d + 80) \cdot 2^d$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftLinearArray_time_add_two`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionArrayCorrectness.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionArrayCorrectness.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-linear-array-time-add-two).

## Output length of array linear FFT convolution

Let $R$ be a field with a star-ring
structure, let $\omega \in R$, and let $x, y$ be arrays over $R$. If array zero-padded linear
FFT convolution with root $\omega$ on $x$ and $y$ returns an array $z$, then the length of $z$
is twice the length of $x$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftLinearArray_size_of_eq_some`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionArrayCorrectness.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/ConvolutionArrayCorrectness.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-linear-array-size-of-eq-some).

## Polynomial of a coefficient vector

The polynomial of a vector
$x = (x_0, \dots, x_{n-1}) \in \mathbb{C}^n$ is $\sum_{j=0}^{n-1} x_j X^j \in \mathbb{C}[X]$, the
complex polynomial whose coefficient of $X^j$ is $x_j$ for $j < n$ and $0$ for $j \ge n$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftPolynomial`, a definition declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Polynomial.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Polynomial.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-polynomial).

## Coefficients of the polynomial of a vector

For every vector
$x = (x_0, \dots, x_{n-1}) \in \mathbb{C}^n$ and every natural number $k$, the coefficient of
$X^k$ in the polynomial of $x$ is $x_k$ if $k < n$ and $0$ if $k \ge n$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftPolynomial_coeff`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Polynomial.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Polynomial.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-polynomial-coeff).

## Zero padding preserves the polynomial

For every natural number $d$ and every vector
$x \in \mathbb{C}^{2^d}$, the zero padding of $x$ (the vector of length $2^{d+1}$ whose first
$2^d$ entries are those of $x$ and whose remaining entries are $0$) has the same polynomial
as $x$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftPolynomial_fftPad`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Polynomial.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Polynomial.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-polynomial-fft-pad).

## Coefficients of a product of vector polynomials

Let $x, y \in \mathbb{C}^n$, and set
$x_i = y_i = 0$ for $i \ge n$. For every natural number $k$, the coefficient of $X^k$ in the
product of the polynomials of $x$ and $y$ is $\sum_{j=0}^{k} x_j y_{k-j}$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftPolynomial_mul_coeff`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Polynomial.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Polynomial.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-polynomial-mul-coeff).

## The last coefficient of a doubled-length product vanishes

For every natural number $d$
and all vectors $x, y \in \mathbb{C}^{2^d}$, the coefficient of $X^{2 \cdot 2^d - 1}$ in the
product of the polynomials of $x$ and $y$ is $0$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftPolynomial_mul_last`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Polynomial.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Polynomial.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-polynomial-mul-last).

## Coefficients of a product beyond twice the length vanish

For all vectors
$x, y \in \mathbb{C}^n$ and every natural number $k \ge 2n$, the coefficient of $X^k$ in the
product of the polynomials of $x$ and $y$ is $0$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftPolynomial_mul_coeff_eq_zero_of_two_mul_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/Polynomial.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/Polynomial.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-polynomial-mul-coeff-eq-zero-of-two).

## Zero padding turns cyclic convolution into the polynomial product

Let $d$ be a natural
number and $N = 2^{d+1}$. For vectors $x, y \in \mathbb{C}^{2^d}$, write
$P_x = \sum_{j < 2^d} x_j X^j$ and $P_y = \sum_{j < 2^d} y_j X^j$, and let $x', y' \in \mathbb{C}^N$
be their zero paddings to length $N$ ($x'_j = x_j$ for $j < 2^d$ and $x'_j = 0$ otherwise, and
likewise for $y'$), with indices of $x'$ and $y'$ read modulo $N$. Then for every $k < N$, the
coefficient of $X^k$ in $P_x P_y$ equals

$$\sum_{j \in \mathbb{Z}/N\mathbb{Z}} x'_j \, y'_{k - j}.$$

Formalized by `Cslib.Algorithms.Lean.TimeM.fftPad_circular_coeff_eq_polynomial`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/PaddingCircular.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/PaddingCircular.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-pad-circular-coeff-eq-polynomial).

## FFT linear convolution gives the product coefficients (Princeton sign)

Let $d$ be a
natural number, $N = 2^{d+1}$ and $\omega = e^{-2\pi i/N}$. For vectors $x, y \in \mathbb{C}^{2^d}$,
write $P_x = \sum_{j < 2^d} x_j X^j$ and $P_y = \sum_{j < 2^d} y_j X^j$, and let
$z \in \mathbb{C}^N$ be the output of the FFT linear convolution of $x$ and $y$ with root $\omega$,
which pads both vectors with zeros to length $N$ and convolves them circularly by FFT. Then for
every $k < N$, the entry $z_k$ is the coefficient of $X^k$ in $P_x P_y$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftLinear_stdAddChar_neg_one_coeff`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/LinearCorrectness.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/LinearCorrectness.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-linear-std-add-char-neg-one-coeff).

## FFT linear convolution computes the convolution sums (Princeton sign)

Let $d$ be a
natural number, $N = 2^{d+1}$ and $\omega = e^{-2\pi i/N}$. For vectors $x, y \in \mathbb{C}^{2^d}$,
extended by $x_j = y_j = 0$ for $j \ge 2^d$, let $z \in \mathbb{C}^N$ be the output of the FFT
linear convolution of $x$ and $y$ with root $\omega$, which pads both vectors with zeros to length
$N$ and convolves them circularly by FFT. Then for every $k < N$,

$$z_k = \sum_{j=0}^{k} x_j \, y_{k-j}.$$

Formalized by `Cslib.Algorithms.Lean.TimeM.fftLinear_stdAddChar_neg_one_sum`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/LinearCorrectness.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/LinearCorrectness.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-linear-std-add-char-neg-one-sum).

## FFT linear convolution returns the product polynomial (Princeton sign)

Let $d$ be a
natural number, $N = 2^{d+1}$ and $\omega = e^{-2\pi i/N}$. For vectors $x, y \in \mathbb{C}^{2^d}$,
write $P_x = \sum_{j < 2^d} x_j X^j$ and $P_y = \sum_{j < 2^d} y_j X^j$, and let
$z \in \mathbb{C}^N$ be the output of the FFT linear convolution of $x$ and $y$ with root $\omega$,
which pads both vectors with zeros to length $N$ and convolves them circularly by FFT. Then
$\sum_{k < N} z_k X^k = P_x P_y$ as polynomials over $\mathbb{C}$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftPolynomial_fftLinear_stdAddChar_neg_one`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/LinearCorrectness.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/LinearCorrectness.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-polynomial-fft-linear-std-add-char-n).

## The last entry of FFT linear convolution is zero (Princeton sign)

Let $d$ be a natural
number, $N = 2^{d+1}$ and $\omega = e^{-2\pi i/N}$. For vectors $x, y \in \mathbb{C}^{2^d}$, let
$z \in \mathbb{C}^N$ be the output of the FFT linear convolution of $x$ and $y$ with root $\omega$,
which pads both vectors with zeros to length $N$ and convolves them circularly by FFT. Then the
last entry $z_{N-1}$ is $0$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftLinear_stdAddChar_neg_one_last`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/LinearCorrectness.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/LinearCorrectness.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-linear-std-add-char-neg-one-last).

## FFT linear convolution gives the product coefficients (MIT/CLRS sign)

Let $d$ be a
natural number, $N = 2^{d+1}$ and $\omega = e^{2\pi i/N}$. For vectors $x, y \in \mathbb{C}^{2^d}$,
write $P_x = \sum_{j < 2^d} x_j X^j$ and $P_y = \sum_{j < 2^d} y_j X^j$, and let
$z \in \mathbb{C}^N$ be the output of the FFT linear convolution of $x$ and $y$ with root $\omega$,
which pads both vectors with zeros to length $N$ and convolves them circularly by FFT. Then for
every $k < N$, the entry $z_k$ is the coefficient of $X^k$ in $P_x P_y$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftLinear_stdAddChar_one_coeff`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/LinearCorrectness.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/LinearCorrectness.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-linear-std-add-char-one-coeff).

## FFT linear convolution computes the convolution sums (MIT/CLRS sign)

Let $d$ be a
natural number, $N = 2^{d+1}$ and $\omega = e^{2\pi i/N}$. For vectors $x, y \in \mathbb{C}^{2^d}$,
extended by $x_j = y_j = 0$ for $j \ge 2^d$, let $z \in \mathbb{C}^N$ be the output of the FFT
linear convolution of $x$ and $y$ with root $\omega$, which pads both vectors with zeros to length
$N$ and convolves them circularly by FFT. Then for every $k < N$,

$$z_k = \sum_{j=0}^{k} x_j \, y_{k-j}.$$

Formalized by `Cslib.Algorithms.Lean.TimeM.fftLinear_stdAddChar_one_sum`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/LinearCorrectness.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/LinearCorrectness.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-linear-std-add-char-one-sum).

## FFT linear convolution returns the product polynomial (MIT/CLRS sign)

Let $d$ be a
natural number, $N = 2^{d+1}$ and $\omega = e^{2\pi i/N}$. For vectors $x, y \in \mathbb{C}^{2^d}$,
write $P_x = \sum_{j < 2^d} x_j X^j$ and $P_y = \sum_{j < 2^d} y_j X^j$, and let
$z \in \mathbb{C}^N$ be the output of the FFT linear convolution of $x$ and $y$ with root $\omega$,
which pads both vectors with zeros to length $N$ and convolves them circularly by FFT. Then
$\sum_{k < N} z_k X^k = P_x P_y$ as polynomials over $\mathbb{C}$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftPolynomial_fftLinear_stdAddChar_one`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/LinearCorrectness.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/LinearCorrectness.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-polynomial-fft-linear-std-add-char-o).

## The last entry of FFT linear convolution is zero (MIT/CLRS sign)

Let $d$ be a natural
number, $N = 2^{d+1}$ and $\omega = e^{2\pi i/N}$. For vectors $x, y \in \mathbb{C}^{2^d}$, let
$z \in \mathbb{C}^N$ be the output of the FFT linear convolution of $x$ and $y$ with root $\omega$,
which pads both vectors with zeros to length $N$ and convolves them circularly by FFT. Then the
last entry $z_{N-1}$ is $0$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fftLinear_stdAddChar_one_last`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/LinearCorrectness.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/LinearCorrectness.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-linear-std-add-char-one-last).

## Inverse FFT after FFT at the positive root is the identity

Let $d$ be a natural number,
$N = 2^d$ and $\omega = e^{2\pi i/N}$. For every vector $x \in \mathbb{C}^N$, running the
radix-two FFT with root $\omega$ on $x$ and then the inverse FFT with root $\omega$ on its output
returns $x$.

Formalized by `Cslib.Algorithms.Lean.TimeM.ifft_fft_stdAddChar_one`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/PositiveRoundtrip.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/PositiveRoundtrip.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#ifft-fft-std-add-char-one).

## FFT after inverse FFT at the positive root is the identity

Let $d$ be a natural number,
$N = 2^d$ and $\omega = e^{2\pi i/N}$. For every vector $x \in \mathbb{C}^N$, running the inverse
FFT with root $\omega$ on $x$ and then the radix-two FFT with root $\omega$ on its output
returns $x$.

Formalized by `Cslib.Algorithms.Lean.TimeM.fft_ifft_stdAddChar_one`, a theorem declared in [CSLibExt/Algorithms/Lean/Fourier/FFT/PositiveRoundtrip.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Fourier/FFT/PositiveRoundtrip.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html#fft-ifft-std-add-char-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fast Fourier transform](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/algebraic-and-numerical-algorithms/fast-fourier-transform)
