---
declaration: section
origin: cited
lean: MetaMathlibExt.kPellLucas, MetaMathlibExt.kPellLucas_zero, MetaMathlibExt.kPellLucas_one, MetaMathlibExt.kPellLucas_add_two, MetaMathlibExt.kPellLucas_two, MetaMathlibExt.kPellLucas_three_small, MetaMathlibExt.kPellLucas_eq_two_pow_iff, MetaMathlibExt.kPellLucas_dominantRoot_bounds
statement: formalized
---

# k-Pell–Lucas numbers close to powers of two

16 results, 6 proved, 9 stated but not proved and 1 without a declaration, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/k-pell-lucas-numbers-close-to-powers-of-two/index.html).

## $k$-generalized Pell–Lucas numbers

For natural numbers $k$ and $n$, the $k$-generalized
Pell–Lucas number $Q^{(k)}_n$ is the natural number defined by $Q^{(k)}_0 = Q^{(k)}_1 = 2$ and

$$Q^{(k)}_{n+2} = 2 Q^{(k)}_{n+1} + \sum_{j} Q^{(k)}_{n-j},$$

where $j$ runs over the integers with $0 \le j \le n$ and $j \le k - 2$. For $k \ge 2$ and
$n \ge k - 2$ this reads $Q^{(k)}_{n+2} = 2 Q^{(k)}_{n+1} + Q^{(k)}_n + \cdots + Q^{(k)}_{n+2-k}$;
for smaller $n$ the terms of negative index (the $k - 2$ initial zeros of the sequence) are
dropped, and for $k \le 1$ the sum is empty.

## Sources

- Mohamadou Bachabi, Bakary Kourouma, and Alain Togbé, *On k-Pell-Lucas Numbers Close to a Power of 2*, INTEGERS 25 (2025), Article A67, Introduction.

Formalized by `MetaMathlibExt.kPellLucas`, a definition declared in [WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/k-pell-lucas-numbers-close-to-powers-of-two/index.html#k-pell-lucas).

## Initial value of the generalized Pell–Lucas numbers

For every natural number $k$, the
$k$-generalized Pell–Lucas number $Q^{(k)}_0$ equals $2$.

## Sources

- Mohamadou Bachabi, Bakary Kourouma, and Alain Togbé, *On k-Pell-Lucas Numbers Close to a Power of 2*, INTEGERS 25 (2025), Article A67, Introduction.

Formalized by `MetaMathlibExt.kPellLucas_zero`, a theorem declared in [WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/k-pell-lucas-numbers-close-to-powers-of-two/index.html#k-pell-lucas-zero).

## The $k$-Pell–Lucas number of index one

For every natural number $k$, the $k$-Pell–Lucas
number $Q^{(k)}_1$ equals $2$.

## Sources

- Mohamadou Bachabi, Bakary Kourouma, and Alain Togbé, *On k-Pell-Lucas Numbers Close to a Power of 2*, INTEGERS 25 (2025), Article A67, Introduction.

Formalized by `MetaMathlibExt.kPellLucas_one`, a theorem declared in [WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/k-pell-lucas-numbers-close-to-powers-of-two/index.html#k-pell-lucas-one).

## Recurrence for the $k$-Pell–Lucas numbers

Let $Q^{(k)}_n$ denote the $k$-generalized
Pell–Lucas numbers. For all natural numbers $k$ and $n$ with $k \le n + 2$,
$Q^{(k)}_{n+2} = 2 Q^{(k)}_{n+1} + \sum_{j=0}^{k-2} Q^{(k)}_{n-j}$, where the sum is empty when
$k < 2$. So once all $k - 1$ earlier terms have nonnegative index, the full recurrence holds.

## Sources

- Mohamadou Bachabi, Bakary Kourouma, and Alain Togbé, *On k-Pell-Lucas Numbers Close to a Power of 2*, INTEGERS 25 (2025), Article A67, Introduction.

Formalized by `MetaMathlibExt.kPellLucas_add_two`, a theorem declared in [WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/k-pell-lucas-numbers-close-to-powers-of-two/index.html#k-pell-lucas-add-two).

## The $2$-generalized Pell–Lucas numbers are the Pell–Lucas numbers

For every natural number
$n$, the $2$-generalized Pell–Lucas number $Q^{(2)}_n$ equals the $n$th Pell–Lucas number $Q_n$;
this is the sequence $2, 2, 6, 14, 34, \ldots$.

## Sources

- Mohamadou Bachabi, Bakary Kourouma, and Alain Togbé, *On k-Pell-Lucas Numbers Close to a Power of 2*, INTEGERS 25 (2025), Article A67, Introduction.

Formalized by `MetaMathlibExt.kPellLucas_two`, a theorem declared in [WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/k-pell-lucas-numbers-close-to-powers-of-two/index.html#k-pell-lucas-two).

## Two values of the $3$-generalized Pell–Lucas numbers

The $3$-generalized Pell–Lucas
numbers $Q^{(3)}_n$ satisfy $Q^{(3)}_3 = 16$ and $Q^{(3)}_6 = 260$.

## Sources

- Mohamadou Bachabi, Bakary Kourouma, and Alain Togbé, *On k-Pell-Lucas Numbers Close to a Power of 2*, INTEGERS 25 (2025), Article A67, Theorem 1.

Formalized by `MetaMathlibExt.kPellLucas_three_small`, a theorem declared in [WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/k-pell-lucas-numbers-close-to-powers-of-two/index.html#k-pell-lucas-three-small).

## $k$-Pell–Lucas numbers that are powers of two (Corollary 1)

Let $k \ge 2$, $n \ge 1$ and
$m \ge 1$ be natural numbers, and let $Q^{(k)}_n$ be the $n$th $k$-Pell–Lucas number. Then
$Q^{(k)}_n = 2^m$ if and only if either $n = 1$ and $m = 1$, or $n = 3$, $m = 4$ and $k \ge 3$.

## Sources

- Mohamadou Bachabi, Bakary Kourouma, and Alain Togbé, *On k-Pell-Lucas Numbers Close to a Power of 2*, INTEGERS 25 (2025), Article A67, Corollary 1.

Stated but not proved: `MetaMathlibExt.kPellLucas_eq_two_pow_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/k-pell-lucas-numbers-close-to-powers-of-two/index.html#k-pell-lucas-eq-two-pow-iff).

## Bounds for the dominant root of the $k$-Pell–Lucas polynomial (Lemma 1)

Let $k \ge 2$ be
a natural number and let $\alpha > 0$ be a real number with
$\alpha^k = 2\alpha^{k-1} + \sum_{i=0}^{k-2} \alpha^i$, that is, a positive real root of
$\Phi_k(x) = x^k - 2x^{k-1} - \sum_{i=0}^{k-2} x^i$. Write
$g_k(z) = (z - 1) / ((k + 1) z^2 - 3kz + k - 1)$ and let $\varphi$ be the golden ratio. Then
(a) $0.276 < g_k(\alpha) < 0.5$, and $|g_k(\beta)| < 1$ for every complex root $\beta \ne \alpha$
of $\Phi_k$; and (b) $\varphi^2 (1 - \varphi^{-k}) < \alpha < \varphi^2$.

## Sources

- Mohamadou Bachabi, Bakary Kourouma, and Alain Togbé, *On k-Pell-Lucas Numbers Close to a Power of 2*, INTEGERS 25 (2025), Article A67, Lemma 1.

Stated but not proved: `MetaMathlibExt.kPellLucas_dominantRoot_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/k-pell-lucas-numbers-close-to-powers-of-two/index.html#k-pell-lucas-dominant-root-bounds).

## Golden-ratio approximations at the dominant root (Lemma 2)

Let $\varphi$ be the golden
ratio, let $k$ and $n$ be natural numbers with $k \ge 50$ and $1 < n < \varphi^{k/2}$, and let
$\alpha > 0$ be a real number with $\alpha^k = 2\alpha^{k-1} + \sum_{i=0}^{k-2} \alpha^i$. Write
$g_k(z) = (z - 1) / ((k + 1) z^2 - 3kz + k - 1)$. Then
(i) $|(2\alpha - 2)\alpha^n - 2\varphi^{2n+1}| < 4\varphi^{2n} / \varphi^{k/2}$ and
(ii) $|g_k(\alpha) - g_k(\varphi^2)| < 4k / \varphi^k$.

## Sources

- Mohamadou Bachabi, Bakary Kourouma, and Alain Togbé, *On k-Pell-Lucas Numbers Close to a Power of 2*, INTEGERS 25 (2025), Article A67, Lemma 2.

Stated but not proved: `MetaMathlibExt.kPellLucas_dominantRoot_golden_approx` is written with `theorem_wanted` in [WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/k-pell-lucas-numbers-close-to-powers-of-two/index.html#k-pell-lucas-dominant-root-golden-approx).

## Main term of the dominant root (Lemma 3)

Let $\varphi$ be the golden ratio, let $k$ and
$n$ be natural numbers with $k \ge 50$ and $n < \varphi^{k/2}$, and let $\alpha > 0$ be a real
number with $\alpha^k = 2\alpha^{k-1} + \sum_{i=0}^{k-2} \alpha^i$. Write
$g_k(z) = (z - 1) / ((k + 1) z^2 - 3kz + k - 1)$. Then there is a real number $\xi$ with
$|\xi| < 1.25 / \varphi^{k/2}$ such that
$(2\alpha - 2) \, g_k(\alpha) \, \alpha^n = \frac{2\varphi^{2n+1}}{\varphi + 2} (1 + \xi)$.

## Sources

- Mohamadou Bachabi, Bakary Kourouma, and Alain Togbé, *On k-Pell-Lucas Numbers Close to a Power of 2*, INTEGERS 25 (2025), Article A67, Lemma 3.

Stated but not proved: `MetaMathlibExt.kPellLucas_dominantRoot_main_term` is written with `theorem_wanted` in [WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/k-pell-lucas-numbers-close-to-powers-of-two/index.html#k-pell-lucas-dominant-root-main-term).

## Continued-fraction lower bound for rational approximations

Let $\tau$ be an irrational real
number with simple continued fraction expansion $[a_0; a_1, a_2, \ldots]$, so that
$a_0 = \lfloor \tau \rfloor$, and let $q_0, q_1, \ldots$ be the denominators of its convergents. Let
$M > 0$ be a real number, let $N$ be the least positive integer with $q_N > M$, and put
$a(M) = \max \{a_k : 0 \le k \le N\}$. Then

$$\left|\tau - \frac{y}{x}\right| > \frac{1}{(a(M) + 2)\, x^2}$$

for all integers $x$ and $y$ with $0 < x < M$.

## Sources

- Mohamadou Bachabi, Bakary Kourouma, and Alain Togbé, *On k-Pell-Lucas Numbers Close to a Power of 2*, INTEGERS 25 (2025), Article A67, Lemma 5.

Stated but not proved: `MetaMathlibExt.lt_abs_sub_div_of_max_partialQuotient` is written with `theorem_wanted` in [WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/k-pell-lucas-numbers-close-to-powers-of-two/index.html#lt-abs-sub-div-of-max-partial-quotient).

## Linear bounds for the logarithm and the exponential near zero (Lemma 6)

Let $a$ and $x$
be real numbers with $0 < a < 1$ and $0 < |x| < a$. Then
$|\log(1 + x)| < \frac{-\log(1 - a)}{a} |x|$ and $|x| < \frac{a}{1 - e^{-a}} |e^x - 1|$.

The case $x = 0$, where both strict inequalities read $0 < 0$, is excluded.

## Sources

- Mohamadou Bachabi, Bakary Kourouma, and Alain Togbé, *On k-Pell-Lucas Numbers Close to a Power of 2*, INTEGERS 25 (2025), Article A67, Lemma 6.

Stated but not proved: `MetaMathlibExt.abs_log_one_add_lt_and_abs_lt_exp_sub_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/k-pell-lucas-numbers-close-to-powers-of-two/index.html#abs-log-one-add-lt-and-abs-lt-exp-sub-on).

## Lemma 7

If `ℓ ≥ 1`, `T > (4ℓ²)^ℓ` and `T > x / (log x)^ℓ`, then
`x < 2^ℓ T (log T)^ℓ`; stated for `x > 1`, where `(log x)^ℓ` is a real power of a positive
number.

## Sources

- Mohamadou Bachabi, Bakary Kourouma, and Alain Togbé, *On k-Pell-Lucas Numbers Close to a Power of 2*, INTEGERS 25 (2025), Article A67, Lemma 7.

The vault records no Lean declaration for it. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/k-pell-lucas-numbers-close-to-powers-of-two/index.html#lt-two-rpow-mul-mul-log-rpow).

## Exponent bounds for $k$-Pell–Lucas numbers close to a power of two (Lemma 8)

Let $k$, $n$
and $m$ be natural numbers with $k \ge 2$, $n \ge 1$, $m \ge 2$ and $n \ge k + 1$, and let
$Q^{(k)}_n$ be the $n$th $k$-Pell–Lucas number. If $|Q^{(k)}_n - 2^m| < 2^{m/2}$, then
$0.69n - 1.69 < m < 1.39n + 3.78$.

## Sources

- Mohamadou Bachabi, Bakary Kourouma, and Alain Togbé, *On k-Pell-Lucas Numbers Close to a Power of 2*, INTEGERS 25 (2025), Article A67, Lemma 8.

Stated but not proved: `MetaMathlibExt.kPellLucas_close_two_pow_exponent_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/k-pell-lucas-numbers-close-to-powers-of-two/index.html#k-pell-lucas-close-two-pow-exponent-boun).

## Absolute bounds for $k$-Pell–Lucas numbers close to a power of two (Lemma 9)

Let $k$, $n$
and $m$ be natural numbers with $k \ge 2$, $m \ge 1$ and $n \ge k + 1$, and let $Q^{(k)}_n$ be
the $n$th $k$-Pell–Lucas number. If $|Q^{(k)}_n - 2^m| < 2^{m/2}$, then
$n < 1.7 \cdot 10^{15} \, k^4 (\log k)^3$ and $m < 2.37 \cdot 10^{15} \, k^4 (\log k)^3$.

## Sources

- Mohamadou Bachabi, Bakary Kourouma, and Alain Togbé, *On k-Pell-Lucas Numbers Close to a Power of 2*, INTEGERS 25 (2025), Article A67, Lemma 9.

Stated but not proved: `MetaMathlibExt.kPellLucas_close_two_pow_lt_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/k-pell-lucas-numbers-close-to-powers-of-two/index.html#k-pell-lucas-close-two-pow-lt-bounds).

## No $k$-Pell–Lucas number with $k > 350$ and index $n \ge k + 1$ is close to a power of two (Lemma 10)

**No $k$-Pell–Lucas number with $k > 350$ and index $n \ge k + 1$ is close to a power of
two (Lemma 10).** For all natural numbers $k$, $n$ and $m$ with $k > 350$ and $n \ge k + 1$, the
$n$th $k$-Pell–Lucas number $Q^{(k)}_n$ satisfies $|Q^{(k)}_n - 2^m| \ge 2^{m/2}$.

## Sources

- Mohamadou Bachabi, Bakary Kourouma, and Alain Togbé, *On k-Pell-Lucas Numbers Close to a Power of 2*, INTEGERS 25 (2025), Article A67, Lemma 10.

Stated but not proved: `MetaMathlibExt.kPellLucas_not_close_two_pow_of_large_order` is written with `theorem_wanted` in [WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KPellLucasCloseToPowerOfTwoWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/k-pell-lucas-numbers-close-to-powers-of-two/index.html#k-pell-lucas-not-close-two-pow-of-large).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: k-Pell–Lucas numbers close to powers of two](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/k-pell-lucas-numbers-close-to-powers-of-two/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/k-pell-lucas-numbers-close-to-powers-of-two)
