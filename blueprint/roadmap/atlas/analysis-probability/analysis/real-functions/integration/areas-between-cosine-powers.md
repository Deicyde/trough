---
declaration: section
origin: cited
lean: MetaMathlibExt.cosPowArea, MetaMathlibExt.cosPowArea_zero_left, MetaMathlibExt.cosPowArea_one_right, MetaMathlibExt.tendsto_cosPowArea_of_odd, MetaMathlibExt.tendsto_cosPowArea_of_even, MetaMathlibExt.cosPowArea_limit_recursion, MetaMathlibExt.tendsto_cosPowArea_doubleFactorial, MetaMathlibExt.iteratedDeriv_arcsin_div_one_sub_doubleFactorial
statement: formalized
---

# Areas between cosine powers

16 results, 3 proved and 13 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/areas-between-cosine-powers/index.html).

## Area between powers of cosines

For natural numbers $n$ and $k$, the area between the
curves $y = \cos^n x$ and $y = \cos^n(kx)$ on $[0, \pi]$ is
$A_n(k) = \int_0^\pi |\cos^n x - \cos^n(kx)|\,dx$, where $\cos^n x$ means $(\cos x)^n$.

The paper's $A_n$ is the limit of $A_n(k)$ as $k \to \infty$ (Eq. (1)), with $k$ running over
the natural numbers.

## Sources

- Muhammad Adam Dombrowski and Gregory Dresden, *Areas Between Cosines*, Journal of Integer Sequences 28 (2025), Article 25.2.3, Eq. (1).

Formalized by `MetaMathlibExt.cosPowArea`, a definition declared in [WantedExt/Analysis/AreasBetweenCosinesWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AreasBetweenCosinesWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/areas-between-cosine-powers/index.html#cos-pow-area).

## The area between cosine powers vanishes for exponent zero

For natural numbers $n$ and
$k$, let $A_n(k) = \int_0^\pi |\cos^n x - \cos^n(kx)|\,dx$ be the area between $\cos^n x$ and
$\cos^n(kx)$ on $[0, \pi]$. Then $A_0(k) = 0$ for every natural number $k$, since both curves are
then the constant $1$.

## Sources

- Muhammad Adam Dombrowski and Gregory Dresden, *Areas Between Cosines*, Journal of Integer Sequences 28 (2025), Article 25.2.3, Eq. (1).

Formalized by `MetaMathlibExt.cosPowArea_zero_left`, a theorem declared in [WantedExt/Analysis/AreasBetweenCosinesWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AreasBetweenCosinesWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/areas-between-cosine-powers/index.html#cos-pow-area-zero-left).

## The area between cosine powers vanishes at frequency one

For natural numbers $n$ and $k$,
let $A_n(k) = \int_0^\pi |\cos^n x - \cos^n(kx)|\,dx$ be the area between $\cos^n x$ and
$\cos^n(kx)$ on $[0, \pi]$. Then $A_n(1) = 0$ for every natural number $n$, since the two curves
then coincide.

## Sources

- Muhammad Adam Dombrowski and Gregory Dresden, *Areas Between Cosines*, Journal of Integer Sequences 28 (2025), Article 25.2.3, Eq. (1).

Formalized by `MetaMathlibExt.cosPowArea_one_right`, a theorem declared in [WantedExt/Analysis/AreasBetweenCosinesWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AreasBetweenCosinesWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/areas-between-cosine-powers/index.html#cos-pow-area-one-right).

## Area between $\cos^n x$ and $\cos^n(kx)$ in the limit, odd $n$

Let $n$ be an odd natural
number. As $k \to \infty$ through the natural numbers, the area
$\int_0^\pi |\cos^n x - \cos^n(kx)|\,dx$ between $\cos^n x$ and $\cos^n(kx)$ on $[0, \pi]$
converges to

$$\frac{8}{2^{n-1}\pi} \sum_{j=0}^{(n-1)/2} \frac{\binom{n}{j}}{(n-2j)^2}.$$

## Sources

- Muhammad Adam Dombrowski and Gregory Dresden, *Areas Between Cosines*, Journal of Integer Sequences 28 (2025), Article 25.2.3, Theorem 1 (`jis-2025-25.2.3-thm-1`).

Stated but not proved: `MetaMathlibExt.tendsto_cosPowArea_of_odd` is written with `theorem_wanted` in [WantedExt/Analysis/AreasBetweenCosinesWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AreasBetweenCosinesWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/areas-between-cosine-powers/index.html#tendsto-cos-pow-area-of-odd).

## Limiting area between even cosine powers

For natural numbers $n$ and $k$, let
$A_n(k) = \int_0^\pi |\cos^n x - \cos^n(kx)|\,dx$. As $k \to \infty$ through the natural numbers:
if $n \equiv 2 \pmod 4$, then

$$A_n(k) \to \frac{16}{2^n \pi} \sum_{j=0}^{(n-2)/4} \frac{\binom{n}{2j}}{(n/2 - 2j)^2},$$

and if $n \equiv 0 \pmod 4$, then

$$A_n(k) \to \frac{16}{2^n \pi} \sum_{j=0}^{(n-4)/4} \frac{\binom{n}{2j+1}}{(n/2 - 2j - 1)^2}.$$

For $n = 0$ the right-hand side is $0$, as is $A_0(k)$ for every $k$, so no positivity hypothesis
is needed.

## Sources

- Muhammad Adam Dombrowski and Gregory Dresden, *Areas Between Cosines*, Journal of Integer Sequences 28 (2025), Article 25.2.3, Theorem 2 (`jis-2025-25.2.3-thm-2`).

Stated but not proved: `MetaMathlibExt.tendsto_cosPowArea_of_even` is written with `theorem_wanted` in [WantedExt/Analysis/AreasBetweenCosinesWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AreasBetweenCosinesWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/areas-between-cosine-powers/index.html#tendsto-cos-pow-area-of-even).

## Recursion for the limiting areas between cosine powers

For natural numbers $n$ and $k$,
let $A_n(k) = \int_0^\pi |\cos^n x - \cos^n(kx)|\,dx$. For every natural number $n \ge 3$ there
are real numbers $L$ and $L'$ such that $A_n(k) \to L$ and $A_{n-2}(k) \to L'$ as $k \to \infty$
through the natural numbers, and $L = \frac{n-1}{n} L' + \frac{c}{n^2 \pi}$, where $c = 8$ if $n$
is odd and $c = 16$ if $n$ is even.

## Sources

- Muhammad Adam Dombrowski and Gregory Dresden, *Areas Between Cosines*, Journal of Integer Sequences 28 (2025), Article 25.2.3, Theorem 3 (`jis-2025-25.2.3-thm-3`).

Stated but not proved: `MetaMathlibExt.cosPowArea_limit_recursion` is written with `theorem_wanted` in [WantedExt/Analysis/AreasBetweenCosinesWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AreasBetweenCosinesWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/areas-between-cosine-powers/index.html#cos-pow-area-limit-recursion).

## Limiting area between cosine powers via double factorials

For natural numbers $n$ and
$k$, let $A_n(k) = \int_0^\pi |\cos^n x - \cos^n(kx)|\,dx$. As $k \to \infty$ through the natural
numbers: if $n$ is odd, then

$$A_n(k) \to \frac{8 \, n!}{\pi (n!!)^2} \sum_{j=0}^{(n-1)/2} \frac{(2j-1)!!}{(2j)!! (2j+1)},$$

and if $n \ge 2$ is even, then

$$A_n(k) \to \frac{16 \, n!}{\pi (n!!)^2} \sum_{j=0}^{(n-2)/2} \frac{(2j)!!}{(2j+1)!! (2j+2)}.$$

Here $(-1)!! = 1$ and $0!! = 1$.

## Sources

- Muhammad Adam Dombrowski and Gregory Dresden, *Areas Between Cosines*, Journal of Integer Sequences 28 (2025), Article 25.2.3, Theorem 4 (`jis-2025-25.2.3-thm-4`).

Stated but not proved: `MetaMathlibExt.tendsto_cosPowArea_doubleFactorial` is written with `theorem_wanted` in [WantedExt/Analysis/AreasBetweenCosinesWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AreasBetweenCosinesWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/areas-between-cosine-powers/index.html#tendsto-cos-pow-area-double-factorial).

## Double-factorial sums as derivatives of arcsine quotients

Let $n$ be a natural number.
If $n$ is odd, the $n$th derivative at $0$ of $x \mapsto \arcsin x / (1 - x)$ is

$$n! \sum_{j=0}^{(n-1)/2} \frac{(2j-1)!!}{(2j)!!\,(2j+1)},$$

and if $n \ge 2$ is even, the $n$th derivative at $0$ of $x \mapsto (\arcsin x)^2 / (2(1 - x))$ is

$$n! \sum_{j=0}^{(n-2)/2} \frac{(2j)!!}{(2j+1)!!\,(2j+2)},$$

where $(-1)!! = 1$ and $0!! = 1$.

These are the $n$th terms of the exponential generating functions of $\arcsin x / (1 - x)$
(OEIS A296726) and of $(\arcsin x)^2 / (2(1 - x))$ (OEIS A372324).

## Sources

- Muhammad Adam Dombrowski and Gregory Dresden, *Areas Between Cosines*, Journal of Integer Sequences 28 (2025), Article 25.2.3, Theorem 4 (`jis-2025-25.2.3-thm-4`).

Stated but not proved: `MetaMathlibExt.iteratedDeriv_arcsin_div_one_sub_doubleFactorial` is written with `theorem_wanted` in [WantedExt/Analysis/AreasBetweenCosinesWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AreasBetweenCosinesWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/areas-between-cosine-powers/index.html#iterated-deriv-arcsin-div-one-sub-double).

## Half-period sine sum for even modulus

Let $N$ be a positive even natural number. For
every natural number $q$, $\sum_{\ell=1}^{N/2} \sin(2\pi q \ell / N)$ equals $0$ if $q$ is even
and $\cot(q\pi / N)$ if $q$ is odd.

The paper also assumes $q > 0$; for $q = 0$ both sides are $0$.

## Sources

- Muhammad Adam Dombrowski and Gregory Dresden, *Areas Between Cosines*, Journal of Integer Sequences 28 (2025), Article 25.2.3, Lemma 5 (`jis-2025-25.2.3-lem-5`).

Stated but not proved: `MetaMathlibExt.sum_sin_two_pi_mul_div_of_even` is written with `theorem_wanted` in [WantedExt/Analysis/AreasBetweenCosinesWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AreasBetweenCosinesWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/areas-between-cosine-powers/index.html#sum-sin-two-pi-mul-div-of-even).

## Half-period sine sum for odd modulus

Let $N$ be an odd natural number. For every
natural number $q$, $\sum_{\ell=1}^{(N-1)/2} \sin(2\pi q \ell / N)$ equals
$-\frac{1}{2} \tan\frac{q\pi}{2N}$ if $q$ is even and $\frac{1}{2} \cot\frac{q\pi}{2N}$ if $q$ is
odd.

The paper also assumes $q > 0$; for $q = 0$ both sides are $0$.

## Sources

- Muhammad Adam Dombrowski and Gregory Dresden, *Areas Between Cosines*, Journal of Integer Sequences 28 (2025), Article 25.2.3, Lemma 6 (`jis-2025-25.2.3-lem-6`).

Stated but not proved: `MetaMathlibExt.sum_sin_two_pi_mul_div_of_odd` is written with `theorem_wanted` in [WantedExt/Analysis/AreasBetweenCosinesWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AreasBetweenCosinesWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/areas-between-cosine-powers/index.html#sum-sin-two-pi-mul-div-of-odd).

## Half-step sine sum for even modulus and even multiplier

Let $N$ be a positive even
natural number and $q$ an even natural number. Then $\sum_{\ell=1}^{N/2} \sin(q \ell \pi / N)$
equals $0$ if $q \equiv 0 \pmod 4$ and $\cot(q\pi / (2N))$ if $q \equiv 2 \pmod 4$.

The paper also assumes $q > 0$; that hypothesis is dropped here.

## Sources

- Muhammad Adam Dombrowski and Gregory Dresden, *Areas Between Cosines*, Journal of Integer Sequences 28 (2025), Article 25.2.3, Lemma 7 (`jis-2025-25.2.3-lem-7`).

Stated but not proved: `MetaMathlibExt.sum_sin_pi_mul_div_of_even_of_even` is written with `theorem_wanted` in [WantedExt/Analysis/AreasBetweenCosinesWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AreasBetweenCosinesWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/areas-between-cosine-powers/index.html#sum-sin-pi-mul-div-of-even-of-even).

## The cotangent limit $4/x$

For every nonzero real number $x$, as $k \to \infty$ through the
natural numbers,

$$\left(\frac{1}{k} - 1\right)\cot\frac{x}{k-1} + \left(\frac{1}{k} + 1\right)\cot\frac{x}{k+1}
\to \frac{4}{x}.$$

The paper states this for every real number $x$; the hypothesis $x \neq 0$ is added because at
$x = 0$ the cotangents and $4/x$ are undefined.

## Sources

- Muhammad Adam Dombrowski and Gregory Dresden, *Areas Between Cosines*, Journal of Integer Sequences 28 (2025), Article 25.2.3, Lemma 8 (`jis-2025-25.2.3-lem-8`).

Stated but not proved: `MetaMathlibExt.tendsto_cot_div_pred_add_cot_div_succ` is written with `theorem_wanted` in [WantedExt/Analysis/AreasBetweenCosinesWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AreasBetweenCosinesWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/areas-between-cosine-powers/index.html#tendsto-cot-div-pred-add-cot-div-succ).

## Integral sums of $\cos qkx - \cos qx$ for odd $q$ and odd $k$

Let $q$ be an odd natural
number, and for each natural number $m$ put $k = 2m + 1$. Then, as $m \to \infty$,

$$\sum_{\ell=1}^{m} \int_{2\pi\ell/(k+1)}^{2\pi\ell/(k-1)} \bigl(\cos(qkx) - \cos(qx)\bigr)\,dx
\to \frac{4}{q^2\pi}.$$

## Sources

- Muhammad Adam Dombrowski and Gregory Dresden, *Areas Between Cosines*, Journal of Integer Sequences 28 (2025), Article 25.2.3, Lemma 9 (`jis-2025-25.2.3-lem-9`).

Stated but not proved: `MetaMathlibExt.tendsto_sum_integral_cos_sub_cos_odd_odd` is written with `theorem_wanted` in [WantedExt/Analysis/AreasBetweenCosinesWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AreasBetweenCosinesWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/areas-between-cosine-powers/index.html#tendsto-sum-integral-cos-sub-cos-odd-odd).

## Alternating integral sums of $\cos qx - \cos qkx$ for even $q$ and odd $k$

Let $q$ be an
even natural number, for each natural number $m$ put $k = 2m + 1$, and let
$f(x) = \cos(qx) - \cos(qkx)$. Then, as $m \to \infty$,

$$\sum_{\ell=1}^{m} \left(\int_{(\ell-1)\pi/(k-1)}^{\ell\pi/(k+1)} f(x)\,dx -
\int_{\ell\pi/(k+1)}^{\ell\pi/(k-1)} f(x)\,dx\right)$$

tends to $0$ if $q \equiv 0 \pmod 4$ and to $16/(q^2\pi)$ if $q \equiv 2 \pmod 4$.

## Sources

- Muhammad Adam Dombrowski and Gregory Dresden, *Areas Between Cosines*, Journal of Integer Sequences 28 (2025), Article 25.2.3, Lemma 10 (`jis-2025-25.2.3-lem-10`).

Stated but not proved: `MetaMathlibExt.tendsto_sum_integral_cos_sub_cos_odd_even` is written with `theorem_wanted` in [WantedExt/Analysis/AreasBetweenCosinesWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AreasBetweenCosinesWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/areas-between-cosine-powers/index.html#tendsto-sum-integral-cos-sub-cos-odd-eve).

## Alternating integral sums of $\cos qx - \cos qkx$ for odd $q$ and even $k$

Let $q$ be an
odd natural number, for each natural number $m$ put $k = 2m$, and let
$f(x) = \cos(qx) - \cos(qkx)$. Then, as $m \to \infty$,

$$\sum_{\ell=1}^{m} \left(\int_{2(\ell-1)\pi/(k-1)}^{2\ell\pi/(k+1)} f(x)\,dx -
\int_{2\ell\pi/(k+1)}^{2\ell\pi/(k-1)} f(x)\,dx\right) \to \frac{8}{q^2\pi}.$$

## Sources

- Muhammad Adam Dombrowski and Gregory Dresden, *Areas Between Cosines*, Journal of Integer Sequences 28 (2025), Article 25.2.3, Lemma 11 (`jis-2025-25.2.3-lem-11`).

Stated but not proved: `MetaMathlibExt.tendsto_sum_integral_cos_sub_cos_even_odd` is written with `theorem_wanted` in [WantedExt/Analysis/AreasBetweenCosinesWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AreasBetweenCosinesWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/areas-between-cosine-powers/index.html#tendsto-sum-integral-cos-sub-cos-even-od).

## Alternating integral sums of $\cos qx - \cos qkx$ for even $q$ and even $k$

Let $q$ be an
even natural number, for each natural number $m$ put $k = 2m$, and let
$f(x) = \cos(qx) - \cos(qkx)$. Then, as $m \to \infty$,

$$\sum_{\ell=1}^{m} \left(\int_{(\ell-1)\pi/(k-1)}^{\ell\pi/(k+1)} f(x)\,dx -
\int_{\ell\pi/(k+1)}^{\ell\pi/(k-1)} f(x)\,dx\right)$$

tends to $0$ if $q \equiv 0 \pmod 4$ and to $16/(q^2\pi)$ if $q \equiv 2 \pmod 4$.

## Sources

- Muhammad Adam Dombrowski and Gregory Dresden, *Areas Between Cosines*, Journal of Integer Sequences 28 (2025), Article 25.2.3, Lemma 12 (`jis-2025-25.2.3-lem-12`).

Stated but not proved: `MetaMathlibExt.tendsto_sum_integral_cos_sub_cos_even_even` is written with `theorem_wanted` in [WantedExt/Analysis/AreasBetweenCosinesWanted.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/AreasBetweenCosinesWanted.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/areas-between-cosine-powers/index.html#tendsto-sum-integral-cos-sub-cos-even-ev).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Areas between cosine powers](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/areas-between-cosine-powers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/real-functions/integration/areas-between-cosine-powers)
