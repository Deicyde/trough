---
declaration: section
origin: cited
lean: MetaMathlibExt.kJacobsthalParams, MetaMathlibExt.lucasU_kJacobsthalParams_two, MetaMathlibExt.lucasV_kJacobsthalParams_two, MetaMathlibExt.companionKJacobsthal, MetaMathlibExt.companionKJacobsthal_add_two, MetaMathlibExt.companionKJacobsthal_two, MetaMathlibExt.companionKJacobsthal_zero_one, MetaMathlibExt.kJacobsthal_binet_identities
statement: formalized
---

# Integral representations of k-Jacobsthal numbers

23 results, 7 proved and 16 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html).

## Lucas parameters of the k-Jacobsthal numbers

For a natural number $k$, the Lucas-sequence
parameters $(P, Q) = (k, -2)$. The Lucas sequences $J_{k,n} = U_n(k, -2)$ and
$j_{k,n} = V_n(k, -2)$ with these parameters are the $k$-Jacobsthal numbers ($J_{k,0} = 0$,
$J_{k,1} = 1$) and the $k$-Jacobsthal–Lucas numbers ($j_{k,0} = 2$, $j_{k,1} = k$); both satisfy
$x_{n+2} = k x_{n+1} + 2 x_n$.

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, Section 1, recurrences (1) and (2).

Formalized by `MetaMathlibExt.kJacobsthalParams`, a definition declared in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#k-jacobsthal-params).

## The second k-Jacobsthal number

For every natural number $k$, the $k$-Jacobsthal number
$J_{k,2} = U_2(k, -2)$ equals $k$.

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, proof of Theorem 2.

Formalized by `MetaMathlibExt.lucasU_kJacobsthalParams_two`, a theorem declared in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#lucas-u-k-jacobsthal-params-two).

## The $k$-Jacobsthal-Lucas number $j_{k,2}$

For every natural number $k$, the
$k$-Jacobsthal-Lucas numbers $j_{k,n} = V_n(k, -2)$, the Lucas sequence $V$ with parameters
$(P, Q) = (k, -2)$, satisfy $j_{k,2} = k^2 + 4$.

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, proof of Theorem 2.

Formalized by `MetaMathlibExt.lucasV_kJacobsthalParams_two`, a theorem declared in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#lucas-v-k-jacobsthal-params-two).

## Companion $k$-Jacobsthal numbers

For a natural number $k$ and integers $a, b$, the
companion $k$-Jacobsthal numbers $\mathcal{J}_{k,n}(a, b)$, $n \in \mathbb{N}$, are the integers
defined by $\mathcal{J}_{k,0}(a, b) = a$, $\mathcal{J}_{k,1}(a, b) = b$ and
$\mathcal{J}_{k,n+2}(a, b) = k\,\mathcal{J}_{k,n+1}(a, b) + 2\,\mathcal{J}_{k,n}(a, b)$.

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, Section 4.

Formalized by `MetaMathlibExt.companionKJacobsthal`, a definition declared in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#companion-kjacobsthal).

## Recurrence of the companion $k$-Jacobsthal numbers

For every natural number $k$, all
integers $a, b$ and every natural number $n$, the companion $k$-Jacobsthal numbers satisfy
$\mathcal{J}_{k,n+2}(a, b) = k\,\mathcal{J}_{k,n+1}(a, b) + 2\,\mathcal{J}_{k,n}(a, b)$.

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, Section 4.

Formalized by `MetaMathlibExt.companionKJacobsthal_add_two`, a theorem declared in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#companion-kjacobsthal-add-two).

## The second companion $k$-Jacobsthal number

For every natural number $k$ and all integers
$a, b$, the companion $k$-Jacobsthal numbers satisfy $\mathcal{J}_{k,2}(a, b) = bk + 2a$.

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, Section 4, list of the first companion numbers.

Formalized by `MetaMathlibExt.companionKJacobsthal_two`, a theorem declared in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#companion-kjacobsthal-two).

## The $k$-Jacobsthal numbers as companion numbers

For a natural number $k$, let
$\mathcal{J}_{k,n}(a, b)$ denote the companion $k$-Jacobsthal numbers and $J_{k,n} = U_n(k, -2)$
the $k$-Jacobsthal numbers, the Lucas sequence with parameters $(k, -2)$. Then for every natural
number $n$, $\mathcal{J}_{k,n}(0, 1) = J_{k,n}$: the companion numbers with initial values $0$ and
$1$ are the $k$-Jacobsthal numbers.

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, Section 4, special cases of the companion numbers.

Formalized by `MetaMathlibExt.companionKJacobsthal_zero_one`, a theorem declared in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#companion-kjacobsthal-zero-one).

## Binet-type identities for k-Jacobsthal numbers

Let $k$ and $n$ be natural numbers, let
$J_{k,n} = U_n(k, -2)$ and $j_{k,n} = V_n(k, -2)$ be the $k$-Jacobsthal and
$k$-Jacobsthal–Lucas numbers, and let $\Delta_k = \sqrt{k^2 + 8}$ and $\sigma_k = (k + \Delta_k)/2$.
Then, in $\mathbb{R}$, $j_{k,n} + \Delta_k J_{k,n} = 2\sigma_k^n$ and
$j_{k,n} - \Delta_k J_{k,n} = 2(-2)^n / \sigma_k^n$, and, in $\mathbb{Z}$,
$j_{k,n}^2 - (k^2 + 8) J_{k,n}^2 = (-2)^{n+2}$.

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, Lemma 1.

Stated but not proved: `MetaMathlibExt.kJacobsthal_binet_identities` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#k-jacobsthal-binet-identities).

## Addition formulas for k-Jacobsthal numbers

Let $k$, $m$ and $n$ be natural numbers and
let $J_{k,n} = U_n(k, -2)$ and $j_{k,n} = V_n(k, -2)$ be the $k$-Jacobsthal and
$k$-Jacobsthal–Lucas numbers. Then $2J_{k,m+n} = J_{k,m} j_{k,n} + J_{k,n} j_{k,m}$ and
$2j_{k,m+n} = j_{k,m} j_{k,n} + (k^2 + 8) J_{k,m} J_{k,n}$.

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, Lemma 2.

Stated but not proved: `MetaMathlibExt.kJacobsthal_add_formulas` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#k-jacobsthal-add-formulas).

## Integral representation of k-Jacobsthal numbers at multiples

Let $k$, $\ell$ and $n$ be
natural numbers, let $J_{k,n} = U_n(k, -2)$ and $j_{k,n} = V_n(k, -2)$ be the $k$-Jacobsthal and
$k$-Jacobsthal–Lucas numbers, and let $\Delta_k = \sqrt{k^2 + 8}$. Then

$$J_{k,\ell n} = \frac{n J_{k,\ell}}{2^n} \int_{-1}^{1}
(j_{k,\ell} + \Delta_k J_{k,\ell} x)^{n-1} \, dx.$$

Here $n - 1$ is an integer exponent, so for $n = 0$ the power is a reciprocal.

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, Theorem 1.

Stated but not proved: `MetaMathlibExt.lucasU_kJacobsthal_mul_eq_integral` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#lucas-u-k-jacobsthal-mul-eq-integral).

## Integral representation of even- and odd-indexed k-Jacobsthal numbers

Let $k$ and $n$
be natural numbers, let $J_{k,n} = U_n(k, -2)$ be the $k$-Jacobsthal numbers and let
$\Delta_k = \sqrt{k^2 + 8}$. Then

$$J_{k,2n} = \frac{kn}{2^n} \int_{-1}^{1} (k^2 + 4 + k \Delta_k x)^{n-1} \, dx$$

and

$$J_{k,2n+1} = \frac{1}{2^{n+1}} \int_{-1}^{1} (nk^2 + k^2 + 4 + k(n+1) \Delta_k x)
(k^2 + 4 + k \Delta_k x)^{n-1} \, dx.$$

Here $n - 1$ is an integer exponent, so for $n = 0$ the power is a reciprocal.

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, Theorem 2.

Stated but not proved: `MetaMathlibExt.lucasU_kJacobsthal_even_odd_eq_integral` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#lucas-u-k-jacobsthal-even-odd-eq-integra).

## Integral representation of k-Jacobsthal–Lucas numbers at multiples

Let $k$, $\ell$ and
$n$ be natural numbers, let $J_{k,n} = U_n(k, -2)$ and $j_{k,n} = V_n(k, -2)$ be the
$k$-Jacobsthal and $k$-Jacobsthal–Lucas numbers, and let $\Delta_k = \sqrt{k^2 + 8}$. Then

$$j_{k,\ell n} = \frac{1}{2^n} \int_{-1}^{1} (j_{k,\ell} + (n+1) \Delta_k J_{k,\ell} x)
(j_{k,\ell} + \Delta_k J_{k,\ell} x)^{n-1} \, dx.$$

Here $n - 1$ is an integer exponent, so for $n = 0$ the power is a reciprocal.

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, Theorem 3.

Stated but not proved: `MetaMathlibExt.lucasV_kJacobsthal_mul_eq_integral` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#lucas-v-k-jacobsthal-mul-eq-integral).

## Integral representation of even- and odd-indexed k-Jacobsthal–Lucas numbers

Let $k$ and
$n$ be natural numbers, let $j_{k,n} = V_n(k, -2)$ be the $k$-Jacobsthal–Lucas numbers and let
$\Delta_k = \sqrt{k^2 + 8}$. Then

$$j_{k,2n} = \frac{1}{2^n} \int_{-1}^{1} (k^2 + 4 + k(n+1) \Delta_k x)
(k^2 + 4 + k \Delta_k x)^{n-1} \, dx$$

and

$$j_{k,2n+1} = \frac{k}{2^{n+1}} \int_{-1}^{1} (n(k^2 + 8) + k^2 + 4 + k(n+1) \Delta_k x)
(k^2 + 4 + k \Delta_k x)^{n-1} \, dx.$$

Here $n - 1$ is an integer exponent, so for $n = 0$ the power is a reciprocal.

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, Theorem 6.

Stated but not proved: `MetaMathlibExt.lucasV_kJacobsthal_even_odd_eq_integral` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#lucas-v-k-jacobsthal-even-odd-eq-integra).

## Integral representation of Jacobsthal numbers at multiples

Let $\ell$ and $n$ be natural
numbers and let $J_n = U_n(1, -2)$ and $j_n = V_n(1, -2)$ be the Jacobsthal and
Jacobsthal–Lucas numbers (the case $k = 1$). Then

$$J_{\ell n} = \frac{n J_\ell}{2^n} \int_{-1}^{1} (j_\ell + 3 J_\ell x)^{n-1} \, dx.$$

Here $n - 1$ is an integer exponent, so for $n = 0$ the power is a reciprocal.

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, Corollary 1.

Stated but not proved: `MetaMathlibExt.jacobsthal_mul_eq_integral` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#jacobsthal-mul-eq-integral).

## Integral formulas for even- and odd-indexed Jacobsthal numbers

Let $J_n = U_n(1, -2)$ be
the Jacobsthal numbers ($J_0 = 0$, $J_1 = 1$, $J_{n+2} = J_{n+1} + 2J_n$). For every natural
number $n$, in $\mathbb{R}$,

$$
J_{2n} = \frac{n}{2^n} \int_{-1}^{1} (5 + 3x)^{n-1}\,dx \quad\text{and}\quad
J_{2n+1} = \frac{1}{2^{n+1}} \int_{-1}^{1} \bigl(n + 5 + 3(n+1)x\bigr)(5 + 3x)^{n-1}\,dx,
$$

where $(5 + 3x)^{n-1}$ is an integer power (for $n = 0$ it is $(5 + 3x)^{-1}$).

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, Corollary 2.

Stated but not proved: `MetaMathlibExt.jacobsthal_even_odd_eq_integral` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#jacobsthal-even-odd-eq-integral).

## Integral representation of the Jacobsthal-Lucas numbers at multiples of an index

Let
$J_m = U_m(1, -2)$ be the Jacobsthal numbers and $j_m = V_m(1, -2)$ the Jacobsthal-Lucas numbers
($j_0 = 2$, $j_1 = 1$, $j_{m+2} = j_{m+1} + 2j_m$). For all natural numbers $\ell$ and $n$, in
$\mathbb{R}$,

$$
j_{\ell n} = \frac{1}{2^n} \int_{-1}^{1}
\bigl(j_\ell + 3(n+1) J_\ell\,x\bigr)(j_\ell + 3J_\ell x)^{n-1}\,dx,
$$

where $(j_\ell + 3J_\ell x)^{n-1}$ is an integer power (for $n = 0$ it is the reciprocal).

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, Corollary 3.

Stated but not proved: `MetaMathlibExt.jacobsthalLucas_mul_eq_integral` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#jacobsthal-lucas-mul-eq-integral).

## Integral representation of Jacobsthal numbers with an offset

Let $\ell$, $n$ and $r$ be
natural numbers and let $J_n = U_n(1, -2)$ and $j_n = V_n(1, -2)$ be the Jacobsthal and
Jacobsthal–Lucas numbers (the case $k = 1$). Then

$$J_{\ell n + r} = \frac{1}{2^{n+1}} \int_{-1}^{1}
(n J_\ell j_r + J_r j_\ell + 3(n+1) J_\ell J_r x) (j_\ell + 3 J_\ell x)^{n-1} \, dx.$$

Here $n - 1$ is an integer exponent, so for $n = 0$ the power is a reciprocal.

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, Corollary 4.

Stated but not proved: `MetaMathlibExt.jacobsthal_mul_add_eq_integral` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#jacobsthal-mul-add-eq-integral).

## Integral representation of the Jacobsthal-Lucas numbers along arithmetic progressions

Let $J_m = U_m(1, -2)$ be the Jacobsthal numbers and $j_m = V_m(1, -2)$ the Jacobsthal-Lucas
numbers ($j_0 = 2$, $j_1 = 1$, $j_{m+2} = j_{m+1} + 2j_m$). For all natural numbers $\ell$, $n$
and $r$, in $\mathbb{R}$,

$$
j_{\ell n + r} = \frac{1}{2^{n+1}} \int_{-1}^{1}
\bigl(9n J_\ell J_r + j_\ell j_r + 3(n+1) J_\ell j_r\,x\bigr)(j_\ell + 3J_\ell x)^{n-1}\,dx,
$$

where $(j_\ell + 3J_\ell x)^{n-1}$ is an integer power (for $n = 0$ it is the reciprocal).

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, Corollary 5.

Stated but not proved: `MetaMathlibExt.jacobsthalLucas_mul_add_eq_integral` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#jacobsthal-lucas-mul-add-eq-integral).

## Ratio of consecutive $k$-Jacobsthal numbers

For every positive integer $k$, the
$k$-Jacobsthal numbers $J_{k,n} = U_n(k, -2)$, the Lucas sequence $U$ with parameters
$(P, Q) = (k, -2)$, satisfy $J_{k,n+1}/J_{k,n} \to (k + \sqrt{k^2 + 8})/2$ as $n \to \infty$,
the quotients taken in $\mathbb{R}$.

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, Theorem 8.

Stated but not proved: `MetaMathlibExt.tendsto_lucasU_kJacobsthal_ratio` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#tendsto-lucas-u-k-jacobsthal-ratio).

## Companion $k$-Jacobsthal numbers via Lucas sequences

For a natural number $k$ and
integers $a, b$, let $\mathcal{J}_{k,n}(a, b)$ be the companion $k$-Jacobsthal numbers, and let
$J_{k,n} = U_n(k, -2)$ and $j_{k,n} = V_n(k, -2)$ be the $k$-Jacobsthal and $k$-Jacobsthal–Lucas
numbers, the Lucas sequences $U$ and $V$ with parameters $(P, Q) = (k, -2)$. Then for every
natural number $n$, $2\,\mathcal{J}_{k,n}(a, b) = a\,j_{k,n} + (2b - ak)\,J_{k,n}$.

The source states this as $\mathcal{J}_{k,n} = \tfrac{a}{2} j_{k,n} + \tfrac{2b - ak}{2} J_{k,n}$.

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, Theorem 9.

Stated but not proved: `MetaMathlibExt.two_mul_companionKJacobsthal` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#two-mul-companion-kjacobsthal).

## Generating function of the companion $k$-Jacobsthal numbers

For every natural number $k$
and all integers $a, b$, the companion $k$-Jacobsthal numbers $\mathcal{J}_{k,n} =
\mathcal{J}_{k,n}(a, b)$ satisfy, in the ring $\mathbb{Z}[[x]]$ of formal power series,

$$\Bigl(\sum_{n \ge 0} \mathcal{J}_{k,n} x^n\Bigr)(1 - kx - 2x^2) = a + (b - ak)x.$$

This is the identity $\sum_{n \ge 0} \mathcal{J}_{k,n} x^n = \frac{a + (b - ak)x}{1 - kx - 2x^2}$
with the denominator cleared.

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, Theorem 10.

Stated but not proved: `MetaMathlibExt.companionKJacobsthal_generatingFunction` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#companion-kjacobsthal-generating-functio).

## Catalan's identity for the companion $k$-Jacobsthal numbers

Let $k$ be a natural number,
$a, b$ integers, $\mathcal{J}_{k,m} = \mathcal{J}_{k,m}(a, b)$ the companion $k$-Jacobsthal numbers
and $J_{k,m} = U_m(k, -2)$ the $k$-Jacobsthal numbers. For all natural numbers $r \le n$,

$$
\mathcal{J}_{k,n-r}\,\mathcal{J}_{k,n+r} - \mathcal{J}_{k,n}^2 =
\bigl(a^2 (k^2 + 8) - (2b - ak)^2\bigr)\,(-2)^{n-r-2}\,J_{k,r}^2
$$

in $\mathbb{Q}$, where $(-2)^{n-r-2}$ is an integer power.

With $\Delta_k = \sqrt{k^2 + 8}$, the first factor on the right equals
$(2b - ak + a\Delta_k)(ak - 2b + a\Delta_k)$, the form in which the source states it.

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, Theorem 11.

Stated but not proved: `MetaMathlibExt.companionKJacobsthal_catalan` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#companion-kjacobsthal-catalan).

## Integral representation of the companion $k$-Jacobsthal numbers

Let $k$, $\ell$, $n$ be
natural numbers and $a, b$ integers. Write $\mathcal{J}_{k,m} = \mathcal{J}_{k,m}(a, b)$ for the
companion $k$-Jacobsthal numbers, $J_{k,m} = U_m(k, -2)$ and $j_{k,m} = V_m(k, -2)$ for the
$k$-Jacobsthal and $k$-Jacobsthal-Lucas numbers, and $\Delta_k = \sqrt{k^2 + 8}$. Then, in
$\mathbb{R}$,

$$
\mathcal{J}_{k,\ell n} = \frac{1}{2^{n+1}} \int_{-1}^{1}
\bigl(a\,j_{k,\ell} + (2b - ak)\,n\,J_{k,\ell} + a(n+1)\Delta_k J_{k,\ell}\,x\bigr)
\bigl(j_{k,\ell} + \Delta_k J_{k,\ell}\,x\bigr)^{n-1}\,dx,
$$

where the power $n - 1$ is an integer power (for $n = 0$ it is the reciprocal).

## Sources

- Weerayuth Nilsrakoo and Achariya Nilsrakoo, *An Integral Representation of k-Jacobsthal and k-Jacobsthal-Lucas Numbers*, INTEGERS 25 (2025), Article A74, Theorem 12.

Stated but not proved: `MetaMathlibExt.companionKJacobsthal_mul_eq_integral` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KJacobsthalIntegralWanted.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html#companion-kjacobsthal-mul-eq-integral).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integral representations of k-Jacobsthal numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integral-representations-of-k-jacobsthal-numbers)
