---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.MillerRabin.twoAdicSplit, Cslib.Algorithms.Lean.MillerRabin.witnessLoop, Cslib.Algorithms.Lean.MillerRabin.witness, Cslib.Algorithms.Lean.MillerRabin.millerRabin, Cslib.Algorithms.Lean.MillerRabin.witnessLoop_time_le, Cslib.Algorithms.Lean.MillerRabin.witness_time_le, Cslib.Algorithms.Lean.MillerRabin.witnessLoop_eq_false, Cslib.Algorithms.Lean.MillerRabin.witness_eq_false_of_prime
statement: formalized
proof: formalized
---

# Miller–Rabin primality test

27 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html).

## Splitting off the power of two

For a natural number $m > 0$, the two-adic split of $m$
is the pair $(t, u)$ of natural numbers with $m = 2^t u$ and $u$ odd. For $m = 0$ it is
$(0, 0)$.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.twoAdicSplit`, a definition declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#two-adic-split).

## The Miller–Rabin squaring loop

Fix a modulus $n$. With no squarings remaining, the loop
at the current value $x$ reports a witness exactly when $x \ne 1$, at no cost. With $k + 1$
squarings remaining, it costs one modular multiplication and computes $y = x^2 \bmod n$; it
reports a witness if $y = 1$, $x \ne 1$ and $x \ne n - 1$, and otherwise continues at $y$ with
$k$ squarings remaining.

Here $x^2 \bmod 0 = x^2$, and $n - 1$ is $0$ when $n = 0$.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.witnessLoop`, a definition declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#witness-loop).

## Miller–Rabin witness test

For natural numbers $a$ and $n$, write $n - 1 = 2^t u$ with $u$
odd (here $n - 1$ is truncated at $0$, and $t = u = 0$ when $n \le 1$). The test sets $x_0$ to the
result of modular exponentiation of $a$ to the power $u$ modulo $n$, which is $a^u \bmod n$ when
$u > 0$ and $1$ when $u = 0$. For $i = 1, \dots, t$ it computes $x_i = x_{i-1}^2 \bmod n$ and
returns true as soon as $x_i = 1$, $x_{i-1} \ne 1$ and $x_{i-1} \ne n - 1$. If no such step
occurs, it returns true exactly when $x_t \ne 1$. Its cost is the cost of the modular
exponentiation plus one for each squaring performed.

For a base with $0 < a < n$, the answer true proves that $n$ is composite; outside that range the
answer carries no such guarantee (for example, the test returns true for $a = n = 2$), as in CLRS,
whose bases are drawn from $1, \dots, n - 1$.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.witness`, a definition declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#witness).

## The Miller–Rabin test

Given a natural number $n$ and a list of bases
$a_1, \dots, a_s$, the test runs the witness test for $n$ on each base in turn. It answers
*composite* as soon as some base $a_i$ is a witness to the compositeness of $n$, and *prime* if
none is (in particular on the empty list). Its cost is the sum of the costs of the witness tests
it runs.

This is CLRS `MILLER-RABIN(n, s)` with the bases given explicitly instead of drawn by
`RANDOM(1, n - 1)`. A *composite* answer is guaranteed correct only when every base lies in
$1, \dots, n - 1$.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.millerRabin`, a definition declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#miller-rabin).

## Cost bound for the Miller–Rabin squaring loop

For all natural numbers $n$, $k$ and $x$,
the cost of the squaring loop modulo $n$ started at $x$ with $k$ squarings remaining is at most
$k$.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.witnessLoop_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#witness-loop-time-le).

## Cost of the Miller–Rabin witness test

For natural numbers $a$ and $n$, write
$n - 1 = 2^t u$ with $u$ odd (here $n - 1$ is truncated at $0$, and $t = u = 0$ when $n \le 1$).
The cost of the witness test on base $a$ and modulus $n$ is at most the cost of the modular
exponentiation of $a$ to the power $u$ modulo $n$ plus $t$: at most one multiplication for each
of the $t$ squarings.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.witness_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#witness-time-le).

## The squaring loop modulo a prime finds no witness when it ends at 1

Let $p$ be a prime
and let $k$ and $x$ be natural numbers with $x < p$ and $x^{2^k} \bmod p = 1$. Then the squaring
loop modulo $p$ started at $x$ with $k$ squarings remaining reports no witness.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.witnessLoop_eq_false`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#witness-loop-eq-false).

## A prime has no Miller–Rabin witnesses in range

Let $n$ be a prime and $a$ a natural
number with $0 < a < n$. Then the witness test does not report $a$ as a witness to the
compositeness of $n$.

## Sources

- CLRS Section 31.8.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.witness_eq_false_of_prime`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#witness-eq-false-of-prime).

## A Miller–Rabin witness in range proves compositeness

Let $n$ and $a$ be natural numbers
with $0 < a < n$. If the witness test reports $a$ as a witness to the compositeness of $n$, then
$n$ is not prime.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.not_prime_of_witness`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#not-prime-of-witness).

## The Miller–Rabin test never rejects a prime when its bases lie in range

Let $n$ be a
prime. For every list of bases $a_1, \dots, a_s$ (possibly empty) with $0 < a_i < n$ for each
$i$, the Miller–Rabin test run on $n$ with these bases answers *prime*.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.millerRabin_of_prime`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#miller-rabin-of-prime).

## With bases in range, a composite answer of the Miller–Rabin test is correct

Let $n$ be
a natural number and $a_1, \dots, a_s$ a list of bases with $0 < a_i < n$ for each $i$. If the
Miller–Rabin test run on $n$ with these bases answers *composite*, then $n$ is not prime.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.not_prime_of_millerRabin_eq_false`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#not-prime-of-miller-rabin-eq-false).

## The squaring loop reports a witness when it does not end at 1

Let $n$, $k$ and $x$ be
natural numbers with $n > 0$, $x < n$ and $x^{2^k} \bmod n \ne 1$. Then the squaring loop modulo
$n$ started at $x$ with $k$ squarings remaining reports a witness.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.witnessLoop_eq_true`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#witness-loop-eq-true).

## Fermat witnesses are Miller–Rabin witnesses

Let $a$ and $n$ be natural numbers with
$n > 1$. If $a^{n-1} \bmod n \ne 1$, that is, $a^{n-1} \not\equiv 1 \pmod{n}$, then the Miller–Rabin
witness test on base $a$ and modulus $n$ returns true.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.witness_of_pow_ne_one`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabin.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#witness-of-pow-ne-one).

## When the squaring loop finds no witness

Let $n$, $k$ and $x$ be natural numbers with
$x < n$. If the Miller–Rabin squaring loop modulo $n$, started at $x$ with $k$ squarings to
perform, reports no witness, then $x = 1$ or $x^{2^i} \equiv -1 \pmod n$ for some $i < k$.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.witnessLoop_eq_false_imp`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#witness-loop-eq-false-imp).

## What a non-witness satisfies

Let $n > 1$ and write $n - 1 = 2^t u$ with $u$ odd. If $a$ is
a natural number for which the Miller–Rabin witness test $\mathrm{WITNESS}(a, n)$ returns false,
then $a^u \equiv 1 \pmod n$, or $a^{2^i u} \equiv -1 \pmod n$ for some $i < t$.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.witness_eq_false_imp`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#witness-eq-false-imp).

## Non-witnesses pass Fermat's test and are units

Let $n > 1$ and let $a$ be a natural number
such that the witness test $\mathrm{WITNESS}(a, n)$ returns false. Then $a^{n-1} \equiv 1 \pmod n$
and $a$ is coprime to $n$.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.coprime_of_witness_eq_false`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#coprime-of-witness-eq-false).

## Non-witnesses of a number

For a natural number $n$, the non-witnesses of $n$ form the
finite set of bases $a$ with $0 < a < n$ for which the Miller–Rabin witness test
$\mathrm{WITNESS}(a, n)$ returns false, that is, the bases that do not witness the compositeness
of $n$.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.nonwitnesses`, a definition declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#nonwitnesses).

## At most half the bases are non-witnesses when some unit fails Fermat's test

Let $n > 1$,
and suppose some $x$ coprime to $n$ has $x^{n-1} \not\equiv 1 \pmod n$. Then at most $(n - 1)/2$
of the bases $1, \dots, n - 1$ are non-witnesses for $n$.

The proof shows that the non-witnesses lie in the proper subgroup $\{y : y^{n-1} = 1\}$ of
$(\mathbb{Z}/n\mathbb{Z})^\times$.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.card_nonwitnesses_le_of_pow_ne_one`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#card-nonwitnesses-le-of-pow-ne-one).

## At most half the bases are non-witnesses for a Carmichael number

Let $n$ be a Carmichael
number: $n > 2$, $n$ is not prime, and $b^{n-1} \equiv 1 \pmod n$ for every $b$ coprime to $n$.
Then at most $(n - 1)/2$ of the bases $1, \dots, n - 1$ are non-witnesses for $n$.

The proof shows that the non-witnesses lie in a proper subgroup of
$(\mathbb{Z}/n\mathbb{Z})^\times$.

## Sources

- CLRS, third edition, Theorem 31.38, case 2.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.card_nonwitnesses_le_of_carmichael`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#card-nonwitnesses-le-of-carmichael).

## At most half the bases are non-witnesses

Let $n > 1$ be odd and not prime. Then at most
$(n - 1)/2$ of the bases $1, \dots, n - 1$ are non-witnesses for $n$; equivalently, at least
$(n - 1)/2$ of them are witnesses to the compositeness of $n$.

## Sources

- CLRS, third edition, Theorem 31.38.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.card_nonwitnesses_le`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#card-nonwitnesses-le).

## Miller–Rabin answers prime exactly when no base is a witness

For every natural number
$n$ and every list of bases, the Miller–Rabin test on $n$ with these bases answers *prime* if and
only if, for every base $a$ in the list, the witness test $\mathrm{WITNESS}(a, n)$ returns false,
that is, $a$ is not a witness to the compositeness of $n$.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.millerRabin_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean, line 389](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean#L389). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#miller-rabin-eq-true-iff).

## Half error bound for Miller–Rabin with several bases

Let $n > 1$ be odd and not prime,
and let $s$ be a natural number. Among the $(n - 1)^s$ lists $(b_1, \dots, b_s)$ of bases with
$0 < b_i < n$, at most $((n - 1)/2)^s$ make the Miller–Rabin test of $n$ with bases
$b_1, \dots, b_s$ answer *prime*.

With uniformly random bases the error probability is therefore at most $2^{-s}$.

## Sources

- CLRS, third edition, Theorem 31.39, in counting form.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.card_millerRabin_errors_le`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean, line 411](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean#L411). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#card-miller-rabin-errors-le).

## At most a quarter of the bases are non-witnesses when some unit fails Fermat's test and the modulus is not a prime power

**At most a quarter of the bases are non-witnesses when some unit fails Fermat's test and the
modulus is not a prime power.** Let $n > 1$ be odd and not prime, and not of the form $p^e$ with
$p$ prime and $e \ge 2$. Suppose some $z$ coprime to $n$ has $z^{n-1} \not\equiv 1 \pmod n$. Then
at most $(n - 1)/4$ of the bases $1, \dots, n - 1$ are non-witnesses for $n$.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.card_nonwitnesses_le_quarter_of_pow_ne_one`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean, line 463](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean#L463). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#card-nonwitnesses-le-quarter-of-pow-ne-o).

## At most a quarter of the bases are non-witnesses for a Carmichael number

Let $n$ be a
Carmichael number: $n > 2$, $n$ is not prime, and $b^{n-1} \equiv 1 \pmod n$ for every $b$
coprime to $n$. Then at most $(n - 1)/4$ of the bases $1, \dots, n - 1$ are non-witnesses for
$n$.

The proof splits $n$ into three pairwise coprime factors greater than $1$ and finds four distinct
cosets of a subgroup of $(\mathbb{Z}/n\mathbb{Z})^\times$ that holds the non-witnesses.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.card_nonwitnesses_le_quarter_of_carmichael`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean, line 567](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean#L567). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#card-nonwitnesses-le-quarter-of-carmicha).

## At most a quarter of the bases are non-witnesses for an odd prime power

Let $p$ be a prime
and $k \ge 2$ with $p^k$ odd. Then at most $(p^k - 1)/4$ of the bases $1, \dots, p^k - 1$ are
non-witnesses for $p^k$.

The proof shows that there are at most $p - 1$ non-witnesses: they satisfy
$a^{p^k - 1} \equiv 1 \pmod{p^k}$, and two of them that agree modulo $p$ agree modulo $p^k$.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.card_nonwitnesses_le_quarter_of_prime_pow`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean, line 655](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean#L655). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#card-nonwitnesses-le-quarter-of-prime-po).

## At most a quarter of the bases are non-witnesses

Let $n > 1$ be odd and not prime. Then
at most $(n - 1)/4$ of the bases $1, \dots, n - 1$ are non-witnesses for $n$, so one uniformly
random base fails to expose $n$ as composite with probability at most $1/4$.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.card_nonwitnesses_le_quarter`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean, line 728](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean#L728). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#card-nonwitnesses-le-quarter).

## Quarter error bound for Miller–Rabin with several bases

Let $n > 1$ be odd and not
prime, and let $s$ be a natural number. Among the $(n - 1)^s$ lists $(b_1, \dots, b_s)$ of bases
with $0 < b_i < n$, at most $\lfloor (n - 1)/4 \rfloor^s$ make the Miller–Rabin test of $n$ with
bases $b_1, \dots, b_s$ answer *prime*.

With uniformly random bases the error probability is therefore at most $4^{-s}$.

Formalized by `Cslib.Algorithms.Lean.MillerRabin.card_millerRabin_errors_le_quarter`, a theorem declared in [CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean, line 743](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/NumberTheory/MillerRabinErrorBound.lean#L743). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html#card-miller-rabin-errors-le-quarter).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Miller–Rabin primality test](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/algebraic-and-numerical-algorithms/miller-rabin-primality-test)
