---
declaration: section
origin: cited
lean: MetaMathlibExt.abs_exp_approx_sub_dvd_indicator_le, MetaMathlibExt.divisorCountApprox_sub_isBigO, MetaMathlibExt.primeCountingApprox_sub_lt, MetaMathlibExt.one_le_pi_sq_mul_sq_div_two_mul_sin_sq, MetaMathlibExt.divisorCountApprox_one_sub_isBigO, MetaMathlibExt.primeCountingApprox_abs_sub_lt, MetaMathlibExt.divisorSumApprox_sub_lt
statement: formalized
---

# Prime-counting formulas from divisor functions

7 results, 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-counting-formulas-from-divisor-functions/index.html).

## Exponential approximation of the divisibility indicator

Let $A$ be a real-valued
function of two natural numbers such that $A(k, n) \sin^2(n\pi/k) \ge 1$ for all natural numbers
$k, n$ with $1 \le k \le n$ and $k \nmid n$. Then for all natural numbers $k, n$ with
$1 \le k \le n$,

$$\left| e^{-nkA(k, n)\sin^2(n\pi/k)} - \delta_{k \mid n} \right| \le e^{-nk},$$

where $\delta_{k \mid n}$ is $1$ if $k$ divides $n$ and $0$ otherwise.

When $k \mid n$ the difference is $0$; otherwise it lies in $(0, e^{-nk}]$.

## Sources

- Carlos M. Alberto and Mavacala N. Saidi, *A New Asymptotic Formula for π(n) with the Divisor Counting Function*, INTEGERS 26 (2026), Article A46, Lemma 1.

Stated but not proved: `MetaMathlibExt.abs_exp_approx_sub_dvd_indicator_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisorApproximantPrimeCountingWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DivisorApproximantPrimeCountingWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-counting-formulas-from-divisor-functions/index.html#abs-exp-approx-sub-dvd-indicator-le).

## Exponential approximation of the divisor-counting function

Let $A$ be a real-valued
function of two natural numbers such that $A(k, n) \sin^2(n\pi/k) \ge 1$ for all natural numbers
$k, n$ with $1 \le k \le n$ and $k \nmid n$. For a natural number $n$ let $\tau(n)$ be the number
of positive divisors of $n$ and

$$\tilde\tau(n) = \sum_{k=1}^{n} e^{-nkA(k, n)\sin^2(n\pi/k)}.$$

Then $\tilde\tau(n) - \tau(n) = O\left(\frac{1}{e^n - 1}\right)$ as $n \to \infty$.

## Sources

- Carlos M. Alberto and Mavacala N. Saidi, *A New Asymptotic Formula for π(n) with the Divisor Counting Function*, INTEGERS 26 (2026), Article A46, Lemma 2.

Stated but not proved: `MetaMathlibExt.divisorCountApprox_sub_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisorApproximantPrimeCountingWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DivisorApproximantPrimeCountingWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-counting-formulas-from-divisor-functions/index.html#divisor-count-approx-sub-is-big-o).

## Prime counting from the exact divisor count

For every natural number $n \ge 2$,

$$\sum_{m=2}^{n} e^{-m(\tau(m) - 2)} - \pi(n) < \frac{1}{e^3(e - 1)},$$

where $\tau(m)$ is the number of positive divisors of $m$ and $\pi(n)$ is the number of primes at
most $n$.

## Sources

- Carlos M. Alberto and Mavacala N. Saidi, *A New Asymptotic Formula for π(n) with the Divisor Counting Function*, INTEGERS 26 (2026), Article A46, Lemma 3.

Stated but not proved: `MetaMathlibExt.primeCountingApprox_sub_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisorApproximantPrimeCountingWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DivisorApproximantPrimeCountingWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-counting-formulas-from-divisor-functions/index.html#prime-counting-approx-sub-lt).

## Sine lower bound at non-divisors

For all positive integers $k$ and $n$ with $k \nmid n$,

$$\frac{\pi^2 k^2}{2} \sin^2\frac{n\pi}{k} \ge 1.$$

In other words, $A(k, n) = \pi^2 k^2 / 2$ satisfies the hypothesis
$A(k, n) \sin^2(n\pi/k) \ge 1$ of the exponential approximation of the divisibility indicator.

## Sources

- Carlos M. Alberto and Mavacala N. Saidi, *A New Asymptotic Formula for π(n) with the Divisor Counting Function*, INTEGERS 26 (2026), Article A46, Lemma 4.

Stated but not proved: `MetaMathlibExt.one_le_pi_sq_mul_sq_div_two_mul_sin_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisorApproximantPrimeCountingWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DivisorApproximantPrimeCountingWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-counting-formulas-from-divisor-functions/index.html#one-le-pi-sq-mul-sq-div-two-mul-sin-sq).

## Trigonometric approximation of the divisor-counting function

For a natural number $k$
let $\tau(k)$ be the number of positive divisors of $k$ and

$$\tilde\tau(k) = \sum_{j=1}^{k} \exp\left(-\frac{\pi^2}{2} k j^3 \sin^2\frac{k\pi}{j}\right).$$

Then $\tilde\tau(k) - \tau(k) = O\left(\frac{1}{e^k - 1}\right)$ as $k \to \infty$.

This is the exponential approximation of the divisor-counting function with
$A(j, k) = \pi^2 j^2 / 2$.

## Sources

- Carlos M. Alberto and Mavacala N. Saidi, *A New Asymptotic Formula for π(n) with the Divisor Counting Function*, INTEGERS 26 (2026), Article A46, Theorem 1.

Stated but not proved: `MetaMathlibExt.divisorCountApprox_one_sub_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisorApproximantPrimeCountingWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DivisorApproximantPrimeCountingWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-counting-formulas-from-divisor-functions/index.html#divisor-count-approx-one-sub-is-big-o).

## Prime-counting function from the smooth divisor count

For a natural number $k$ let

$$\tilde\tau(k) = \sum_{j=1}^{k} \exp\left(-\frac{\pi^2}{2} k j^3 \sin^2\frac{k\pi}{j}\right),$$

and for $n \ge 2$ let $\tilde\pi(n) = \sum_{k=2}^{n} e^{-k(\tilde\tau(k) - 2)}$. Then for every
natural number $n \ge 2$, $|\tilde\pi(n) - \pi(n)| < 0.7129749140934$, where $\pi(n)$ is the
number of primes at most $n$.

The constant is $0.684 + 1/(e^3(e - 1))$ truncated to thirteen decimal places, the sum of the
two one-sided bounds, as the two-sided bound requires.

## Sources

- Carlos M. Alberto and Mavacala N. Saidi, *A New Asymptotic Formula for π(n) with the Divisor Counting Function*, INTEGERS 26 (2026), Article A46, Theorem 2.

Stated but not proved: `MetaMathlibExt.primeCountingApprox_abs_sub_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisorApproximantPrimeCountingWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DivisorApproximantPrimeCountingWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-counting-formulas-from-divisor-functions/index.html#prime-counting-approx-abs-sub-lt).

## Exponential approximation of the sum-of-divisors function

Let $A$ be a real-valued
function of two natural numbers such that $A(k, n) \sin^2(n\pi/k) \ge 1$ for all natural numbers
$k, n$ with $1 \le k \le n$ and $k \nmid n$. For a natural number $n \ge 1$ let $\sigma(n)$
be the sum of the positive divisors of $n$ and

$$\tilde\sigma(n) = \sum_{k=1}^{n} k\, e^{-nkA(k, n)\sin^2(n\pi/k)}.$$

Then $\tilde\sigma(n) - \sigma(n) < \frac{n}{e^n - 1}$.

## Sources

- Carlos M. Alberto and Mavacala N. Saidi, *A New Asymptotic Formula for π(n) with the Divisor Counting Function*, INTEGERS 26 (2026), Article A46, Theorem 3.

Stated but not proved: `MetaMathlibExt.divisorSumApprox_sub_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisorApproximantPrimeCountingWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DivisorApproximantPrimeCountingWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-counting-formulas-from-divisor-functions/index.html#divisor-sum-approx-sub-lt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Prime-counting formulas from divisor functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-counting-formulas-from-divisor-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-counting-formulas-from-divisor-functions)
