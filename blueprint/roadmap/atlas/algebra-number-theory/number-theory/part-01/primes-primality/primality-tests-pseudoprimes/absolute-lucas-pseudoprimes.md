---
declaration: section
origin: cited
lean: MetaMathlibExt.jacobiSym_prime_add_mul_eq, MetaMathlibExt.mul_dvd_prod_sub_sign_iff, MetaMathlibExt.IsDCarmichael, MetaMathlibExt.IsDCarmichael.not_prime, MetaMathlibExt.not_isDCarmichael_five_nine, MetaMathlibExt.lucasDigitSum, MetaMathlibExt.lucasDigitSum_five_seven_6601, MetaMathlibExt.IsPrimaryDCarmichael
statement: formalized
---

# Absolute Lucas pseudoprimes

30 results, 12 proved and 18 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html).

## Jacobi symbols of a discriminant $D$ agree at odd primes congruent modulo $D$

Let $p$ and
$p'$ be odd primes and let $D$ be an integer with $D \equiv 0$ or $1 \pmod 4$ that is coprime to
$p$. If $p' = p + D x$ for some integer $x$, then the Jacobi symbols agree:
$\left(\frac{D}{p'}\right) = \left(\frac{D}{p}\right)$.

For an odd prime $p$ the Jacobi symbol $\left(\frac{D}{p}\right)$ is the Legendre symbol and agrees
with the Kronecker symbol.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Lemma 1.

Stated but not proved: `MetaMathlibExt.jacobiSym_prime_add_mul_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#jacobi-sym-prime-add-mul-eq).

## Ballot's Lemma 2: three divisibilities as one congruence

Let
$\varepsilon_1, \varepsilon_2, \varepsilon_3 \in \{1, -1\}$, let $c_1, c_2, c_3$ be pairwise coprime
positive integers, let $g \ne 0$ be an integer, and put
$n = (c_1 g + \varepsilon_1)(c_2 g + \varepsilon_2)(c_3 g + \varepsilon_3)$ and
$\varepsilon_n = \varepsilon_1 \varepsilon_2 \varepsilon_3$. Then $c_i g \mid n - \varepsilon_n$ for
$i = 1, 2, 3$ if and only if

$$c_1 c_2 c_3 \mid g (\varepsilon_3 c_1 c_2 + \varepsilon_2 c_1 c_3 + \varepsilon_1 c_2 c_3) +
\varepsilon_n (\varepsilon_1 c_1 + \varepsilon_2 c_2 + \varepsilon_3 c_3).$$

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Lemma 2.

Stated but not proved: `MetaMathlibExt.mul_dvd_prod_sub_sign_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#mul-dvd-prod-sub-sign-iff).

## $D$-Carmichael number

Let $D$ be an integer. A natural number $n$ is a $D$-Carmichael
number when $D \equiv 0$ or $1 \pmod 4$, $n > 1$ is odd and composite, $D$ and $n$ are coprime,
and for all integers $P$ and $Q \ne 0$ with $P$ and $Q$ coprime, $P^2 - 4Q = D$ and $Q$ coprime
to $n$, the number $n$ divides the term $U_{n - \varepsilon_n}(P, Q)$ of the Lucas sequence
$U(P, Q)$, where $\varepsilon_n = \left(\frac{D}{n}\right)$ is the Jacobi symbol.

These are Williams' absolute Lucas $D$-pseudoprimes. The condition on $D$ is the paper's standing
assumption; for other $D$ no Lucas sequence has discriminant $D$, so the last clause would be
vacuous.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Section 1 (definition of absolute Lucas `D`-pseudoprimes, after [17]).

Formalized by `MetaMathlibExt.IsDCarmichael`, a definition declared in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#is-dcarmichael).

## $D$-Carmichael numbers are not prime

For every integer $D$ and every natural number $n$,
if $n$ is a $D$-Carmichael number, then $n$ is not prime.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Section 1.

Formalized by `MetaMathlibExt.IsDCarmichael.not_prime`, a theorem declared in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#not-prime).

## $9$ is not a $5$-Carmichael number

The number $9$ is not a $D$-Carmichael number for
$D = 5$. Indeed, the Jacobi symbol $(5 \mid 9)$ equals $1$, and the Fibonacci sequence
$U(1, -1)$ has $F_8 = 21$, which $9$ does not divide.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Section 1.

Formalized by `MetaMathlibExt.not_isDCarmichael_five_nine`, a theorem declared in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#not-is-dcarmichael-five-nine).

## Extended digit sum

Let $D$ be an integer and let $p \ge 2$ and $n$ be natural numbers, with
base-$p$ expansion $n = \sum_i c_i p^i$, $0 \le c_i < p$. With
$\varepsilon_p = \left(\frac{D}{p}\right)$ the Jacobi symbol, the extended digit sum of $n$ is
$s_p(n) = \sum_i c_i \varepsilon_p^i$.

For $p \le 1$ the definition gives $s_p(n) = n$.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, equation (6).

Formalized by `MetaMathlibExt.lucasDigitSum`, a definition declared in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#lucas-digit-sum).

## The extended digit sum of $6601$ in base $7$ for $D = 5$

The base-$7$ expansion is
$6601 = 5 \cdot 7 + 7^2 + 5 \cdot 7^3 + 2 \cdot 7^4$ and the Jacobi symbol is
$\left(\frac{5}{7}\right) = -1$, so the extended digit sum with $D = 5$ is
$s_7(6601) = -5 + 1 - 5 + 2 = -7$.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, equation (6) and the example `m = 6601`.

Formalized by `MetaMathlibExt.lucasDigitSum_five_seven_6601`, a theorem declared in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#lucas-digit-sum-five-seven-6601).

## Primary $D$-Carmichael number

Let $D$ be an integer. A natural number $n$ is a primary
$D$-Carmichael number when $n$ is a $D$-Carmichael number and
$|s_p(n) - \varepsilon_n| \le p - \varepsilon_p$ for every prime $p \mid n$, where
$\varepsilon_m = \left(\frac{D}{m}\right)$ is the Jacobi symbol and $s_p(n) = \sum_i c_i
\varepsilon_p^i$ is the extended digit sum of the base-$p$ expansion $n = \sum_i c_i p^i$.

In the paper's terms, $n$ has degree at most one: the number $d_p$ with
$s_p(n) = \varepsilon_n + d_p (p - \varepsilon_p)$ satisfies $|d_p| \le 1$ for every prime
$p \mid n$.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Definition 3.

Formalized by `MetaMathlibExt.IsPrimaryDCarmichael`, a definition declared in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#is-primary-dcarmichael).

## Secondary $D$-Carmichael number

Let $D$ be an integer. A natural number $n$ is a
secondary $D$-Carmichael number when $n$ is a $D$-Carmichael number,
$|s_p(n) - \varepsilon_n| \le 2 (p - \varepsilon_p)$ for every prime $p \mid n$, and
$|s_p(n) - \varepsilon_n| > p - \varepsilon_p$ for some prime $p \mid n$, where
$\varepsilon_m = \left(\frac{D}{m}\right)$ is the Jacobi symbol and $s_p(n) = \sum_i c_i
\varepsilon_p^i$ is the extended digit sum of the base-$p$ expansion $n = \sum_i c_i p^i$.

In the paper's terms, $n$ has degree exactly two: the number $d_p$ with
$s_p(n) = \varepsilon_n + d_p (p - \varepsilon_p)$ satisfies $|d_p| \le 2$ for every prime
$p \mid n$ and $|d_p| > 1$ for some.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Definition 3.

Formalized by `MetaMathlibExt.IsSecondaryDCarmichael`, a definition declared in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#is-secondary-dcarmichael).

## Primary $D$-Carmichael numbers are $D$-Carmichael

For every integer $D$ and natural
number $n$, if $n$ is a primary $D$-Carmichael number, then $n$ is a $D$-Carmichael number.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Definition 3.

Formalized by `MetaMathlibExt.IsPrimaryDCarmichael.isDCarmichael`, a theorem declared in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#is-dcarmichael-2).

## Carmichael numbers of a signature

Let $\sigma = (\varepsilon_1, \dots, \varepsilon_r)$ be a
list of integers. A natural number $n$ is $\sigma$-Carmichael when every $\varepsilon_i$ is $1$ or
$-1$, $r \ge 2$, $n$ is odd and squarefree with exactly $r$ prime factors $p_1 < \dots < p_r$, and
$n$ is $D$-Carmichael for every integer $D \equiv 0$ or $1 \pmod 4$ whose Jacobi symbols satisfy
$\left(\frac{D}{p_i}\right) = \varepsilon_i$ for all $i$.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Definition 4.

Formalized by `MetaMathlibExt.IsSignatureCarmichael`, a definition declared in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#is-signature-carmichael).

## $4$ is not a signature Carmichael number

For every finite sequence $\sigma$ of integers,
$4$ is not a $\sigma$-Carmichael number, because $4$ is not squarefree.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Definition 4.

Formalized by `MetaMathlibExt.not_isSignatureCarmichael_four`, a theorem declared in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#not-is-signature-carmichael-four).

## Universal $D$-forms

Let $D$ be an integer, $\sigma$ a list of integers, and
$f(x) = (a_1 x + b_1) \cdots (a_k x + b_k)$ a product of linear factors with integer coefficients.
Then $f$ is a universal $D$-form with respect to $\sigma$ when: every factor has $a_i \ne 0$ and
$\gcd(a_i, b_i) = 1$; for every prime $\ell$ there is an integer $x$ with $\ell \nmid f(x)$; and
for every integer $x$ at which every factor $a_i x + b_i$ is a positive prime, the product $f(x)$
is $D$-Carmichael and the Jacobi symbols $\left(\frac{D}{p}\right)$, for $p$ running through the
prime factors of $f(x)$ in increasing order and counted with multiplicity, form the list $\sigma$.

Here $x$ ranges over all integers rather than $x \ge 0$, since forms such as $p + D x$ are
used with $D < 0$.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Section 1 (definition of a universal `D`-form).

Formalized by `MetaMathlibExt.IsUniversalLinearDForm`, a definition declared in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#is-universal-linear-dform).

## $x(x+1)$ is never a universal form

For every integer $D$ and every finite sequence
$\sigma$ of integers, the product of the linear factors $x$ and $x + 1$ is not a universal
$D$-form with respect to $\sigma$: since $x(x+1)$ is even for every integer $x$, the prime $2$
divides every value of the product.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Section 1 (definition of a universal `D`-form).

Formalized by `MetaMathlibExt.not_isUniversalLinearDForm_mul_succ`, a theorem declared in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#not-is-universal-linear-dform-mul-succ).

## Williams' Korselt criterion for $D$-Carmichael numbers

Let $D$ be an integer with
$D \equiv 0$ or $1 \pmod 4$, and let $n > 1$ be an odd composite natural number coprime to $D$.
Then $n$ is a $D$-Carmichael number if and only if $n$ is squarefree and
$p - \left(\frac{D}{p}\right)$ divides $n - \left(\frac{D}{n}\right)$ for every prime $p \mid n$,
where $\left(\frac{D}{m}\right)$ is the Jacobi symbol.

Primes and $1$ satisfy the condition on the right but are not $D$-Carmichael, which is why $n$ is
assumed composite; it is assumed coprime to $D$ as in the definition.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Theorem 1.

Stated but not proved: `MetaMathlibExt.isDCarmichael_iff_korselt` is written with `theorem_wanted` in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#is-dcarmichael-iff-korselt).

## Prime $k$-tuples give infinitely many primary Carmichael numbers (Wagstaff)

Suppose the
prime $k$-tuples conjecture holds in the following form: for every finite list of integer pairs
$(a_1, b_1), \dots, (a_k, b_k)$ with all $a_i \ge 1$ such that for every prime $\ell$ there is an
integer $x$ with $\ell \nmid \prod_i (a_i x + b_i)$, there are infinitely many natural numbers $x$
for which every $a_i x + b_i$ is a positive prime. Then there are infinitely many composite natural
numbers $n > 1$ such that $a^{n-1} \equiv 1 \pmod n$ for every natural number $a$ coprime to $n$,
$n$ has exactly three distinct prime factors, and for every prime $p \mid n$ the sum of the
base-$p$ digits of $n$ equals $p$.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Theorem 2.

Stated but not proved: `MetaMathlibExt.infinite_primary_carmichael_of_primeKTuples` is written with `theorem_wanted` in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#infinite-primary-carmichael-of-prime-ktu).

## Korselt criterion for $\sigma$-Carmichael numbers

Let
$\sigma = (\varepsilon_1, \dots, \varepsilon_r)$ be a list of signs $\varepsilon_i \in \{1, -1\}$ of
length $r \ge 2$, put $\varepsilon_\sigma = \varepsilon_1 \cdots \varepsilon_r$, and let $n$ be an
odd natural number. Then $n$ is $\sigma$-Carmichael if and only if $n$ is squarefree, has exactly
$r$ prime factors $p_1 < \dots < p_r$, and satisfies
$p_i - \varepsilon_i \mid n - \varepsilon_\sigma$ for every $i$.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Theorem 3.

Stated but not proved: `MetaMathlibExt.isSignatureCarmichael_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#is-signature-carmichael-iff).

## Two-prime-factor $D$-Carmichael numbers

Let $D$ be an integer and assume the prime
$k$-tuples conjecture (the paper's Conjecture 1) in the following form: for every finite list
of linear forms $a_i x + b_i$ with integers $a_i \ge 1$ and $b_i$ such that for every prime
$\ell$ there is an integer $x$ with $\ell \nmid \prod_i (a_i x + b_i)$, there are infinitely
many natural numbers $x$ at which every $a_i x + b_i$ is a positive prime.
Then, first, for all primes $p < q$ such that $pq$ is a $D$-Carmichael number: the product of
the linear factors $Dx + p$ and $Dx + q$ is a universal $D$-form with respect to the signature
$(-1, 1)$; $q = p + 2$; for every integer $x$ at which $p + Dx$ and $q + Dx$ are both positive
primes, their product is a primary $D$-Carmichael number; and there are infinitely many
primary $D$-Carmichael numbers $n$ whose Jacobi symbols $(D \mid \cdot)$ at the prime factors
of $n$, listed in increasing order with multiplicity, are $-1, 1$. Second, a natural number
$n$ is a $5$-Carmichael number with exactly two prime factors counted with multiplicity if and
only if $n = (10x + 7)(10x + 9)$ for some natural number $x \ge 1$ with $10x + 7$ and
$10x + 9$ both prime.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Theorem 4.

Stated but not proved: `MetaMathlibExt.twoFactor_isDCarmichael` is written with `theorem_wanted` in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#two-factor-is-dcarmichael).

## Chernick-type universal forms for three prime factors

Let $D$ be an integer and let
$3 < p_1 < p_2 < p_3$ be primes such that $p_1 p_2 p_3$ is $D$-Carmichael, and write
$\varepsilon_i = \left(\frac{D}{p_i}\right)$ for the Jacobi symbols. Let $g$ be the greatest common
divisor of $p_1 - \varepsilon_1$, $p_2 - \varepsilon_2$ and $p_3 - \varepsilon_3$, and let
$c_1, c_2, c_3$ be pairwise coprime integers with $g c_i = p_i - \varepsilon_i$ for each $i$. Then

$$(D c_1^2 c_2 c_3 x + p_1)(D c_1 c_2^2 c_3 x + p_2)(D c_1 c_2 c_3^2 x + p_3)$$

is a universal $D$-form with respect to the signature
$(\varepsilon_1, \varepsilon_2, \varepsilon_3)$.

Being $D$-Carmichael includes the condition $D \equiv 0$ or $1 \pmod 4$.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Theorem 5.

Stated but not proved: `MetaMathlibExt.isUniversalLinearDForm_chernick` is written with `theorem_wanted` in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#is-universal-linear-dform-chernick).

## Prime $k$-tuples give primary $5$-Carmichael numbers of every three-term signature

Suppose the prime $k$-tuples conjecture holds in the following form: for every finite list of
integer pairs $(a_1, b_1), \dots, (a_k, b_k)$ with all $a_i \ge 1$ such that for every prime
$\ell$ there is an integer $x$ with $\ell \nmid \prod_i (a_i x + b_i)$, there are infinitely many
natural numbers $x$ for which every $a_i x + b_i$ is a positive prime. Then for all signs
$\sigma_1, \sigma_2, \sigma_3 \in \{1, -1\}$ there are infinitely many primary $5$-Carmichael
numbers $n$ that have exactly three prime factors $p_1 \le p_2 \le p_3$ counted with multiplicity
and satisfy $\left(\frac{5}{p_i}\right) = \sigma_i$ for $i = 1, 2, 3$, where
$\left(\frac{5}{p}\right)$ is the Jacobi symbol.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Theorem 6.

Stated but not proved: `MetaMathlibExt.infinite_primary_fiveCarmichael_of_primeKTuples` is written with `theorem_wanted` in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#infinite-primary-five-carmichael-of-prim).

## The $D$-Carmichael numbers of the form $3qr$

Let $q < r$ be primes with $3 < q$. Then
$3qr$ is a $D$-Carmichael number for some integer $D$ if and only if $3qr$ is one of $105$,
$195$, $255$, $399$, $561$ and $2703$. Moreover, for all integers $D$ and $D'$ such that $3qr$
is both $D$-Carmichael and $D'$-Carmichael, the Jacobi symbols agree at $3$, $q$ and $r$:
$(D \mid 3) = (D' \mid 3)$, $(D \mid q) = (D' \mid q)$ and $(D \mid r) = (D' \mid r)$.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Theorem 7.

Stated but not proved: `MetaMathlibExt.threeQR_isDCarmichael_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#three-qr-is-dcarmichael-iff).

## Primary and secondary $5$-Carmichael numbers from prime quadruples

Assume the prime
$k$-tuples conjecture (the paper's Conjecture 1) in the following form: for every finite list
of linear forms $a_i x + b_i$ with integers $a_i \ge 1$ and $b_i$ such that for every prime
$\ell$ there is an integer $x$ with $\ell \nmid \prod_i (a_i x + b_i)$, there are infinitely
many natural numbers $x$ at which every $a_i x + b_i$ is a positive prime.
For a natural number $x$ put $p = 30x + 17$, $q = 30x + 19$, $r = 180x + 107$ and
$s = 180x + 109$. Then, first, for every natural number $x$ with $p$, $q$, $r$ and $s$ all
prime, $pqr$ and $pqs$ are primary $5$-Carmichael numbers and $pqrs$ is a secondary
$5$-Carmichael number; and second, there are infinitely many natural numbers $x$ with $p$,
$q$, $r$ and $s$ all prime.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Theorem 8.

Stated but not proved: `MetaMathlibExt.primaryFiveCarmichael_pairs_of_primeKTuples` is written with `theorem_wanted` in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#primary-five-carmichael-pairs-of-prime-k).

## Primary and secondary $13$-Carmichael numbers from prime quadruples

Assume the prime
$k$-tuples conjecture (the paper's Conjecture 1) in the following form: for every finite list
of linear forms $a_i x + b_i$ with integers $a_i \ge 1$ and $b_i$ such that for every prime
$\ell$ there is an integer $x$ with $\ell \nmid \prod_i (a_i x + b_i)$, there are infinitely
many natural numbers $x$ at which every $a_i x + b_i$ is a positive prime.
For a natural number $x$ put $p = 78x + 137$, $q = 78x + 139$, $r = 468x + 827$ and
$s = 468x + 829$. Then, first, for every natural number $x$ with $p$, $q$, $r$ and $s$ all
prime: $pqr$ and $pqs$ are primary $13$-Carmichael numbers; the Jacobi symbols
$(13 \mid \cdot)$ at the prime factors of $pqr$, listed in increasing order, are $-1, 1, -1$,
and those at the prime factors of $pqs$ are $-1, 1, 1$; and $pqrs$ is a secondary
$13$-Carmichael number. Second, there are infinitely many natural numbers $x$ with $p$, $q$,
$r$ and $s$ all prime.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Theorem 9.

Stated but not proved: `MetaMathlibExt.primaryThirteenCarmichael_pairs_of_primeKTuples` is written with `theorem_wanted` in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#primary-thirteen-carmichael-pairs-of-pri).

## Universal $5$- and $13$-forms from prime quadruples

Assume the prime
$k$-tuples conjecture (the paper's Conjecture 1) in the following form: for every finite list
of linear forms $a_i x + b_i$ with integers $a_i \ge 1$ and $b_i$ such that for every prime
$\ell$ there is an integer $x$ with $\ell \nmid \prod_i (a_i x + b_i)$, there are infinitely
many natural numbers $x$ at which every $a_i x + b_i$ is a positive prime.
Then, first, for $D = 5$ and for $D = 13$: the products of linear factors
$(390z + 137)(390z + 139)(2340z + 827)$ and $(390z + 137)(390z + 139)(2340z + 829)$ are
universal $D$-forms with respect to the signatures $(-1, 1, -1)$ and $(-1, 1, 1)$
respectively; the product $(390z + 137)(390z + 139)(2340z + 827)(2340z + 829)$ is a
universal $D$-form with respect to the signature $(-1, 1, -1, 1)$; and for every natural
number $z$ with $390z + 137$ and $390z + 139$ prime, the first product is a primary
$D$-Carmichael number if $2340z + 827$ is prime, the second is a primary $D$-Carmichael
number if $2340z + 829$ is prime, and the four-factor product is a secondary $D$-Carmichael
number if both are prime. Second, there are infinitely many natural numbers $z$ at which all
four factors are prime.

The paper (and the record) print "universal 7- and 13-forms"; $7 \not\equiv 0, 1 \pmod 4$ is
not a discriminant, and the next sentence and the proof (combining the $5$-form of Theorem 8
with the $13$-form of Theorem 9) fix it as $5$.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Theorem 10.

Stated but not proved: `MetaMathlibExt.universal_fiveThirteen_forms` is written with `theorem_wanted` in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 374](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#universal-five-thirteen-forms).

## Schinzel's Hypothesis H gives numbers that are primary $5$- and $(-11)$-Carmichael

Suppose Schinzel's Hypothesis H holds in the following form: for every finite set $F$ of integer
polynomials, each satisfying the Bunyakovsky condition, such that $F$ satisfies the Schinzel
condition, there are infinitely many natural numbers $n$ for which $|f(n)|$ is prime for every
$f \in F$. Then there are infinitely many natural numbers $n$ that are both primary
$5$-Carmichael and primary $(-11)$-Carmichael and have exactly three prime factors
$p_1 \le p_2 \le p_3$ counted with multiplicity, with Jacobi symbols
$\left(\frac{5}{p_1}\right) = 1$, $\left(\frac{5}{p_2}\right) = \left(\frac{5}{p_3}\right) = -1$,
$\left(\frac{-11}{p_1}\right) = \left(\frac{-11}{p_3}\right) = -1$ and
$\left(\frac{-11}{p_2}\right) = 1$.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Theorem 11.

Stated but not proved: `MetaMathlibExt.infinite_primary_five_negEleven_of_schinzelH` is written with `theorem_wanted` in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#infinite-primary-five-neg-eleven-of-schi).

## Bi-Carmichael numbers for signatures of opposite signs

Let $D$ and $D'$ be integers and
let $n$ be both a $D$-Carmichael and a $D'$-Carmichael number whose Jacobi symbols satisfy
$\left(\frac{D}{n}\right) \ne \left(\frac{D'}{n}\right)$. Then
$\left(\frac{D'}{p}\right) = -\left(\frac{D}{p}\right)$ for every prime $p \mid n$, the number of
distinct prime factors of $n$ is odd, and $3 \nmid n$.

This reads the paper's $n \in C(\sigma) \cap C(\sigma')$ as $n$ being $D$-Carmichael with
signature $\sigma$ and $D'$-Carmichael with signature $\sigma'$.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Theorem 12.

Stated but not proved: `MetaMathlibExt.isDCarmichael_opposite_signs` is written with `theorem_wanted` in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 418](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L418). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#is-dcarmichael-opposite-signs).

## Three-prime-factor $D$-Carmichael numbers have a single Jacobi sign

Let $D$ and $D'$ be
integers and let $n$ be a natural number with exactly three distinct prime factors. If $n$ is both
$D$-Carmichael and $D'$-Carmichael, then the Jacobi symbols agree:
$\left(\frac{D}{n}\right) = \left(\frac{D'}{n}\right)$.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Theorem 13.

Stated but not proved: `MetaMathlibExt.jacobiSym_eq_of_isDCarmichael_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 430](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L430). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#jacobi-sym-eq-of-is-dcarmichael-three).

## Ballot's Lemma 3: the three divisibilities persist modulo $c_1 c_2 c_3$

Let
$\varepsilon_1, \varepsilon_2, \varepsilon_3 \in \{1, -1\}$, let $c_1, c_2, c_3$ be pairwise coprime
positive integers, let $\varepsilon = \varepsilon_1 \varepsilon_2 \varepsilon_3$, and let $g \ne 0$
be an integer such that $c_i g$ divides
$(c_1 g + \varepsilon_1)(c_2 g + \varepsilon_2)(c_3 g + \varepsilon_3) - \varepsilon$ for
$i = 1, 2, 3$. Then every nonzero integer $h \equiv g \pmod{c_1 c_2 c_3}$ satisfies the same
divisibilities: $c_i h$ divides
$(c_1 h + \varepsilon_1)(c_2 h + \varepsilon_2)(c_3 h + \varepsilon_3) - \varepsilon$ for
$i = 1, 2, 3$.

The divisibility hypothesis on $g$ is needed: for $(c_1, c_2, c_3) = (1, 2, 3)$,
$\varepsilon_1 = \varepsilon_2 = \varepsilon_3 = 1$ and $g = h = 1$, the product is $24$ and
$2 \nmid 24 - 1$.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Lemma 3.

Stated but not proved: `MetaMathlibExt.mul_dvd_prod_sub_sign_of_modEq` is written with `theorem_wanted` in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#mul-dvd-prod-sub-sign-of-mod-eq).

## Divisibility conditions for $D$-Carmichael numbers $3qr$

Let $D$ be an integer, let
$q < r$ be primes with $3 < q$, and write $\alpha = (D \mid 3)$, $\beta = (D \mid q)$ and
$\gamma = (D \mid r)$ for the Jacobi symbols. If $3qr$ is a $D$-Carmichael number, then
$q - \beta$ divides $3r - \alpha\gamma$ and $r - \gamma$ divides $3q - \alpha\beta$; moreover
$r = 3q + 2\gamma$ if $\gamma = -\alpha\beta$, and $2r = 3q + \gamma$ if $\gamma = \alpha\beta$.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Lemma 4.

Stated but not proved: `MetaMathlibExt.threeQR_isDCarmichael_divisibility` is written with `theorem_wanted` in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 459](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L459). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#three-qr-is-dcarmichael-divisibility).

## Williams' characterization of two-prime $D$-Carmichael numbers

Let $D$ be an integer
with $D \equiv 0$ or $1 \pmod 4$ and let $p_1 < p_2$ be primes. Then $p_1 p_2$ is a
$D$-Carmichael number if and only if $p_2 = p_1 + 2$, $\left(\frac{D}{p_1}\right) = -1$ and
$\left(\frac{D}{p_2}\right) = 1$, where $\left(\frac{D}{p}\right)$ is the Jacobi symbol.

## Sources

- Christian Ballot, *On Absolute Lucas Pseudoprimes*, INTEGERS 26 (2026), Article A102, Proposition 1.

Stated but not proved: `MetaMathlibExt.isDCarmichael_mul_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean, line 472](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AbsoluteLucasPseudoprimesWanted.lean#L472). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html#is-dcarmichael-mul-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Absolute Lucas pseudoprimes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/absolute-lucas-pseudoprimes)
