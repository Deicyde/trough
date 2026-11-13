---
declaration: section
origin: cited
lean: Nat.SylvesterSchur.consecutive_two, Nat.SylvesterSchur.consecutive_three, Nat.SylvesterSchur.consecutive_four, Nat.SylvesterSchur.consecutive_five, Nat.SylvesterSchur.consecutive_six, Nat.SylvesterSchur.consecutive_of_factorial_mul_top_pow_primeCounting_lt_start_pow, Nat.SylvesterSchur.consecutive_of_factorial_mul_top_pow_half_add_one_lt_start_pow, Nat.SylvesterSchur.consecutive_of_quadratic_start
statement: formalized
proof: formalized
---

# Conditional Sylvester-Schur consequences

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/conditional-sylvester-schur-consequences/index.html).

## Sylvester–Schur theorem for two consecutive integers

For every natural number $k > 2$,
one of the two integers $k$, $k + 1$ is divisible by a prime $p > 2$.

Formalized by `Nat.SylvesterSchur.consecutive_two`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/conditional-sylvester-schur-consequences/index.html#consecutive-two).

## Sylvester–Schur theorem for three consecutive integers

For every natural number
$k > 3$, one of the three integers $k$, $k + 1$, $k + 2$ is divisible by a prime $p > 3$.

Formalized by `Nat.SylvesterSchur.consecutive_three`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/conditional-sylvester-schur-consequences/index.html#consecutive-three).

## Four consecutive integers above four have a prime factor above four

For every natural
number $k > 4$, some prime $p > 4$ divides one of $k$, $k+1$, $k+2$, $k+3$.

Formalized by `Nat.SylvesterSchur.consecutive_four`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/conditional-sylvester-schur-consequences/index.html#consecutive-four).

## Five consecutive integers above five have a prime factor above five

For every natural
number $k > 5$, some prime $p > 5$ divides one of $k$, $k+1$, $k+2$, $k+3$, $k+4$.

Formalized by `Nat.SylvesterSchur.consecutive_five`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/conditional-sylvester-schur-consequences/index.html#consecutive-five).

## Six consecutive integers above six have a prime factor above six

For every natural
number $k > 6$, some prime $p > 6$ divides one of $k$, $k+1$, $k+2$, $k+3$, $k+4$, $k+5$.

Formalized by `Nat.SylvesterSchur.consecutive_six`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/conditional-sylvester-schur-consequences/index.html#consecutive-six).

## Prime-counting criterion for a large prime in a consecutive block

Let $1 \le n < k$ be
natural numbers and let $\pi(n)$ be the number of primes at most $n$. If
$n! \cdot (k+n-1)^{\pi(n)} < k^n$, then some prime $p > n$ divides one of the integers
$k, k+1, \dots, k+n-1$.

Formalized by `Nat.SylvesterSchur.consecutive_of_factorial_mul_top_pow_primeCounting_lt_start_pow`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/conditional-sylvester-schur-consequences/index.html#consecutive-of-factorial-mul-top-pow-pri).

## Half-exponent criterion for a large prime in a consecutive block

Let $1 \le n < k$ be
natural numbers. If $n! \cdot (k+n-1)^{\lfloor n/2 \rfloor + 1} < k^n$, then some prime $p > n$
divides one of the integers $k, k+1, \dots, k+n-1$.

The exponent comes from the bound $\pi(n) \le \lfloor n/2 \rfloor + 1$ on the prime-counting
function $\pi$.

Formalized by `Nat.SylvesterSchur.consecutive_of_factorial_mul_top_pow_half_add_one_lt_start_pow`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/conditional-sylvester-schur-consequences/index.html#consecutive-of-factorial-mul-top-pow-hal).

## Quadratic starts give a large prime in a consecutive block

Let $n \ge 38$ and $k > n^2$
be natural numbers. Then some prime $p > n$ divides one of the integers
$k, k+1, \dots, k+n-1$.

Formalized by `Nat.SylvesterSchur.consecutive_of_quadratic_start`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/conditional-sylvester-schur-consequences/index.html#consecutive-of-quadratic-start).

## Square-root and primorial criterion for a large prime in a consecutive block

Let
$1 \le n < k$ be natural numbers, write $N = k + n - 1$, and let $P(n)$ denote the product of all
primes at most $n$. If $n! \cdot N^{\lfloor \sqrt{N} \rfloor + 1} \cdot P(n) < k^n$, then some prime
$p > n$ divides one of the integers $k, k+1, \dots, k+n-1$.

Formalized by `Nat.SylvesterSchur.consecutive_of_factorial_mul_top_pow_sqrt_mul_primorial_lt_start_pow`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/conditional-sylvester-schur-consequences/index.html#consecutive-of-factorial-mul-top-pow-sqr).

## Erdős layer criterion for a large prime in a consecutive block

Let $1 \le n < k$ be
natural numbers, write $N = k + n - 1$ and $L = \lfloor \log_2 N \rfloor$, and for a natural number
$m$ let $P(m)$ denote the product of all primes at most $m$. If
$n! \cdot P(n) \cdot \prod_{i=2}^{L} P(\lfloor N^{1/i} \rfloor) < k^n$, then some prime $p > n$
divides one of the integers $k, k+1, \dots, k+n-1$.

Formalized by `Nat.SylvesterSchur.consecutive_of_factorial_mul_prod_erdos_layers_lt_start_pow`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/conditional-sylvester-schur-consequences/index.html#consecutive-of-factorial-mul-prod-erdos).

## Erdős layer criterion with a one-third first layer for a large prime in a consecutive block

Let $n < k$ be natural numbers, write $N = k + n - 1$ and $L = \lfloor \log_2 N \rfloor$, assume
$N \ge 6$, and for a natural number $m$ let $P(m)$ denote the product of all primes at most $m$.
If $n! \cdot P(\lfloor N/3 \rfloor) \cdot \prod_{i=2}^{L} P(\lfloor N^{1/i} \rfloor) < k^n$, then
some prime $p > n$ divides one of the integers $k, k+1, \dots, k+n-1$.

Formalized by `Nat.SylvesterSchur.consecutive_of_factorial_mul_prod_erdos_div_three_layers_lt_start_pow`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/conditional-sylvester-schur-consequences/index.html#consecutive-of-factorial-mul-prod-erdos-2).

## Large starts give a large prime in a consecutive block

Let $n \ge 2$ and $k > n$ be
natural numbers with $n! \cdot 2^{n-1} < k$. Then some prime $p > n$ divides one of the integers
$k, k+1, \dots, k+n-1$.

Formalized by `Nat.SylvesterSchur.consecutive_of_large_start`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SylvesterSchur/Conditional.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/conditional-sylvester-schur-consequences/index.html#consecutive-of-large-start).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conditional Sylvester-Schur consequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/conditional-sylvester-schur-consequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/conditional-sylvester-schur-consequences)
