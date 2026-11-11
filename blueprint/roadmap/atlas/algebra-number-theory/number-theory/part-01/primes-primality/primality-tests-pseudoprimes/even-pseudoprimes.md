---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.IsEvenPseudoprime, MathlibExt.NumberTheory.evenPseudoprimes, MathlibExt.NumberTheory.IsEvenPseudoprime.even, MathlibExt.NumberTheory.IsEvenPseudoprime.two_lt, MathlibExt.NumberTheory.IsEvenPseudoprime.modeq, MathlibExt.NumberTheory.IsEvenPseudoprime.not_prime, MetaMathlibExt.evenPseudoprime_modEq_and_orderOf_odd, MetaMathlibExt.evenPseudoprime_mod_sixteen
statement: formalized
---

# Even pseudoprimes

17 results, 6 proved and 11 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/even-pseudoprimes/index.html).

## Even pseudoprime

A natural number $N$ is an even pseudoprime if $N$ is even, $N > 2$
and $2^N \equiv 2 \pmod{N}$.

Formalized by `MathlibExt.NumberTheory.IsEvenPseudoprime`, a definition declared in [MathlibExt/NumberTheory/EvenPseudoprime.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/EvenPseudoprime.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/even-pseudoprimes/index.html#is-even-pseudoprime).

## The set of even pseudoprimes

The set of even pseudoprimes is the set of natural
numbers $N$ such that $N$ is even, $N > 2$ and $2^N \equiv 2 \pmod{N}$.

Formalized by `MathlibExt.NumberTheory.evenPseudoprimes`, a definition declared in [MathlibExt/NumberTheory/EvenPseudoprime.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/EvenPseudoprime.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/even-pseudoprimes/index.html#even-pseudoprimes).

## Even pseudoprimes are even

Every even pseudoprime $N$ is an even natural number.

Formalized by `MathlibExt.NumberTheory.IsEvenPseudoprime.even`, a theorem declared in [MathlibExt/NumberTheory/EvenPseudoprime.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/EvenPseudoprime.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/even-pseudoprimes/index.html#even).

## Even pseudoprimes exceed two

Every even pseudoprime $N$ satisfies $N > 2$.

Formalized by `MathlibExt.NumberTheory.IsEvenPseudoprime.two_lt`, a theorem declared in [MathlibExt/NumberTheory/EvenPseudoprime.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/EvenPseudoprime.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/even-pseudoprimes/index.html#two-lt).

## Fermat congruence for even pseudoprimes

If $N$ is an even pseudoprime, then
$2^N \equiv 2 \pmod{N}$.

Formalized by `MathlibExt.NumberTheory.IsEvenPseudoprime.modeq`, a theorem declared in [MathlibExt/NumberTheory/EvenPseudoprime.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/EvenPseudoprime.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/even-pseudoprimes/index.html#modeq).

## Even pseudoprimes are not prime

No even pseudoprime is a prime number: the only even
prime is $2$, and every even pseudoprime is greater than $2$.

Formalized by `MathlibExt.NumberTheory.IsEvenPseudoprime.not_prime`, a theorem declared in [MathlibExt/NumberTheory/EvenPseudoprime.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/EvenPseudoprime.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/even-pseudoprimes/index.html#not-prime).

## Odd prime divisors of an even pseudoprime

Let $N$ be an even pseudoprime and $p$ an
odd prime dividing $N$, and write $\ell_2(p)$ for the multiplicative order of $2$ modulo $p$.
Then $N \equiv p \pmod{p\,\ell_2(p)}$, $\ell_2(p)$ is odd, $p \equiv 1$ or $7 \pmod 8$, and
$14p \le N$.

## Sources

- Cheng, Kinlaw and Nguyen, *The Reciprocal Sum of Even Pseudoprimes*, Journal of Integer Sequences 29 (2026), Article 26.1.3, Lemma 2 (`jis-2026-26.1.3-lem-2`).

Stated but not proved: `MetaMathlibExt.evenPseudoprime_modEq_and_orderOf_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/EvenPseudoprimeWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EvenPseudoprimeWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/even-pseudoprimes/index.html#even-pseudoprime-mod-eq-and-order-of-odd).

## Even pseudoprimes modulo 16

Every even pseudoprime $N$ satisfies
$N \equiv 2 \pmod{16}$ or $N \equiv 14 \pmod{16}$.

## Sources

- Cheng, Kinlaw and Nguyen, *The Reciprocal Sum of Even Pseudoprimes*, Journal of Integer Sequences 29 (2026), Article 26.1.3, Corollary 4 (`jis-2026-26.1.3-cor-4`).

Stated but not proved: `MetaMathlibExt.evenPseudoprime_mod_sixteen` is written with `theorem_wanted` in [WantedExt/NumberTheory/EvenPseudoprimeWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EvenPseudoprimeWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/even-pseudoprimes/index.html#even-pseudoprime-mod-sixteen).

## Square prime factors of even pseudoprimes are Wieferich primes

Let $N$ be an even
pseudoprime and $p$ a prime with $p^2 \mid N$. Then $p$ is a Wieferich prime, that is
$2^{p-1} \equiv 1 \pmod{p^2}$, and $p \ge 3511$.

## Sources

- Cheng, Kinlaw and Nguyen, *The Reciprocal Sum of Even Pseudoprimes*, Journal of Integer Sequences 29 (2026), Article 26.1.3, Lemma 5 (`jis-2026-26.1.3-lem-5`).

Stated but not proved: `MetaMathlibExt.evenPseudoprime_wieferich_of_sq_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/EvenPseudoprimeWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EvenPseudoprimeWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/even-pseudoprimes/index.html#even-pseudoprime-wieferich-of-sq-dvd).

## Reciprocal sum over a residue class in an exponential window

Write $\ell_2(p)$ for the
multiplicative order of $2$ modulo a prime $p$. Let $p$ be an odd prime and $k$ a natural
number, and let $F_p(k)$ be the sum of $1/N$ over the integers $N$ with $e^k < N \le e^{k+1}$,
$N \equiv p \pmod{p\,\ell_2(p)}$ and $N > p$. Then $F_p(k) \le 2 / (p\,\ell_2(p))$.

The bound holds for every $k$, since the terms are $1/N$ with $N = p + j\,p\,\ell_2(p)$ and
$j \ge 1$.

## Sources

- Cheng, Kinlaw and Nguyen, *The Reciprocal Sum of Even Pseudoprimes*, Journal of Integer Sequences 29 (2026), Article 26.1.3, Proposition 11 (`jis-2026-26.1.3-prop-11`).

Stated but not proved: `MetaMathlibExt.sum_inv_modEq_orderOf_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/EvenPseudoprimeWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EvenPseudoprimeWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/even-pseudoprimes/index.html#sum-inv-mod-eq-order-of-le).

## Reciprocal sum over a residue class restricted modulo 16

Write $\ell_2(p)$ for the
multiplicative order of $2$ modulo a prime $p$. Let $p$ be an odd prime with $\ell_2(p)$ odd,
let $k$ be a natural number, and let $S$ be the sum of $1/N$ over the integers $N$ with
$e^k < N \le e^{k+1}$, $N \equiv p \pmod{p\,\ell_2(p)}$ and $N \equiv \pm 2 \pmod{16}$. Then
$S \le 1 / (4p\,\ell_2(p))$ whenever $16p\,\ell_2(p) \le e^k$, and in all cases
$S \le (1/8 + 4e^{-k} p\,\ell_2(p)) / (p\,\ell_2(p))$.

The paper's further clauses, involving $z_k$, $c_k$ and $d_k$, are not stated here.

## Sources

- Cheng, Kinlaw and Nguyen, *The Reciprocal Sum of Even Pseudoprimes*, Journal of Integer Sequences 29 (2026), Article 26.1.3, Proposition 12 (`jis-2026-26.1.3-prop-12`).

Stated but not proved: `MetaMathlibExt.sum_inv_modEq_orderOf_mod_sixteen_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/EvenPseudoprimeWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EvenPseudoprimeWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/even-pseudoprimes/index.html#sum-inv-mod-eq-order-of-mod-sixteen-le).

## Rankin's bound for reciprocal sums of smooth numbers

Let $x, y, s$ be real numbers with
$2 \le y < x$ and $0 < s < 1$. Call a positive integer $y$-smooth if all its prime factors are
at most $y$ (so $1$ is $y$-smooth). Let $S(x, y)$ be the sum of $1/n$ over the $y$-smooth
integers $n > x$, and let $\zeta(\sigma, y)$ be the sum of $n^{-\sigma}$ over all $y$-smooth
integers $n$. Then $S(x, y) \le x^{-s} \zeta(1 - s, y)$, where both series converge.

## Sources

- Cheng, Kinlaw and Nguyen, *The Reciprocal Sum of Even Pseudoprimes*, Journal of Integer Sequences 29 (2026), Article 26.1.3, Lemma 8, display (smooth1) (`jis-2026-26.1.3-lem-8`).

Stated but not proved: `MetaMathlibExt.smoothReciprocalTail_le_rpow_mul_smoothZeta` is written with `theorem_wanted` in [WantedExt/NumberTheory/EvenPseudoprimeWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EvenPseudoprimeWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/even-pseudoprimes/index.html#smooth-reciprocal-tail-le-rpow-mul-smoot).

## Nguyen–Pomerance bound for reciprocal sums of smooth numbers

Let $x, y$ be real numbers
with $2 \le y < x$. Call a positive integer $y$-smooth if all its prime factors are at most $y$,
let $S(x, y)$ be the sum of $1/n$ over the $y$-smooth integers $n > x$, and let
$\zeta(\sigma, y)$ be the sum of $n^{-\sigma}$ over all $y$-smooth integers $n$. Put
$u = \log x / \log y$ and $s = \log(u \log u) / \log y$. If $u \ge 3$ and $s \le 1/3$, then

$$
S(x, y) \le x^{-s} \zeta(1 - s, y) < 25\, e^{(1 + \varepsilon) u} (u \log u)^{-u} (2^s - 1)^{-1}
$$

with $\varepsilon = 2.3 \cdot 10^{-8}$.

## Sources

- Cheng, Kinlaw and Nguyen, *The Reciprocal Sum of Even Pseudoprimes*, Journal of Integer Sequences 29 (2026), Article 26.1.3, Lemma 8, display (smooth2) (`jis-2026-26.1.3-lem-8`).

Stated but not proved: `MetaMathlibExt.smoothReciprocalTail_lt_nguyenPomerance` is written with `theorem_wanted` in [WantedExt/NumberTheory/EvenPseudoprimeWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EvenPseudoprimeWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/even-pseudoprimes/index.html#smooth-reciprocal-tail-lt-nguyen-pomeran).

## Primes with odd order of 2 of small size

Write $\ell_2(p)$ for the multiplicative
order of $2$ modulo a prime $p$. For every real $x > 0$, the number of primes $p$ with
$2 < p \le x$ such that $\ell_2(p)$ is odd and $1 < \ell_2(p) \le p^{2/5}$ is less than
$0.00754\, x^{4/5}$.

The hypothesis $x > 0$ cannot be dropped: at $x = 0$ both sides are $0$, so the strict
inequality fails.

## Sources

- Cheng, Kinlaw and Nguyen, *The Reciprocal Sum of Even Pseudoprimes*, Journal of Integer Sequences 29 (2026), Article 26.1.3, Lemma 10 (`jis-2026-26.1.3-lem-10`).

Stated but not proved: `MetaMathlibExt.orderOfTwo_odd_small_count_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/EvenPseudoprimeWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EvenPseudoprimeWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/even-pseudoprimes/index.html#order-of-two-odd-small-count-lt).

## Primes with odd order of 2 of medium size

Write $\ell_2(p)$ for the multiplicative
order of $2$ modulo a prime $p$. For every real $x \ge 337$, the number of primes $p$ with
$2 < p \le x$ such that $\ell_2(p)$ is odd and $p^{2/5} < \ell_2(p) \le p^{12/25}$ is less than
$0.00754\, x^{24/25}$.

## Sources

- Cheng, Kinlaw and Nguyen, *The Reciprocal Sum of Even Pseudoprimes*, Journal of Integer Sequences 29 (2026), Article 26.1.3, Lemma 10 (`jis-2026-26.1.3-lem-10`).

Stated but not proved: `MetaMathlibExt.orderOfTwo_odd_medium_count_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/EvenPseudoprimeWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EvenPseudoprimeWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/even-pseudoprimes/index.html#order-of-two-odd-medium-count-lt).

## Beeger's theorem

There are infinitely many even pseudoprimes.

## Sources

- N. G. W. H. Beeger, "On even numbers `m` dividing `2 ^ m - 2`," American Mathematical Monthly 58 (1951), 553–555.

Stated but not proved: `MathlibExt.NumberTheory.EvenPseudoprimesWanted.evenPseudoprimes_infinite` is written with `theorem_wanted` in [WantedExt/NumberTheory/EvenPseudoprimesWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EvenPseudoprimesWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/even-pseudoprimes/index.html#even-pseudoprimes-infinite).

## Cheng–Kinlaw–Nguyen reciprocal-sum bounds

The sum of the
reciprocals of all even pseudoprimes lies strictly between `0.000011`
and `0.0059`.

## Sources

- Xuyan Cheng, Paul Kinlaw, and Duc Nguyen, "The Reciprocal Sum of Even Pseudoprimes," Journal of Integer Sequences 29 (2026), main theorem, <https://cs.uwaterloo.ca/journals/JIS/VOL29/Kinlaw/kinlaw11.tex>.

Stated but not proved: `MathlibExt.NumberTheory.EvenPseudoprimesWanted.evenPseudoprime_reciprocal_sum_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/EvenPseudoprimesWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EvenPseudoprimesWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/even-pseudoprimes/index.html#even-pseudoprime-reciprocal-sum-bounds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Even pseudoprimes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/even-pseudoprimes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/even-pseudoprimes)
