---
declaration: section
origin: cited
lean: Nat.SylvesterSchur.Internal.bertrand_base, Nat.SylvesterSchur.Internal.prime_dvd_seq_implies_choose, Nat.SylvesterSchur.Internal.prime_dvd_choose_of_mem_interval, Nat.SylvesterSchur.Internal.exists_prime_dvd_choose_of_large_prime_dvd_block, Nat.SylvesterSchur.Internal.exists_dvd_block_of_succ_succ_prime_not_dvd_pred, Nat.SylvesterSchur.Internal.exists_prime_dvd_choose_of_large_start, Nat.SylvesterSchur.Internal.exists_prime_dvd_choose_of_half_bound, Nat.SylvesterSchur.Internal.start_le_quadratic_of_no_large_prime_dvd_block
statement: formalized
proof: formalized
---

# Block-level reductions for the Sylvester-Schur theorem

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/block-level-reductions-for-the-sylvester-schur-t/index.html).

## Bertrand's postulate in block form

For every natural number $n \ge 1$ there are $i < n$
and a prime $p > n$ such that $p$ divides $n + 1 + i$. Thus one of the $n$ consecutive integers
$n + 1, \dots, 2n$ has a prime divisor greater than $n$.

Formalized by `Nat.SylvesterSchur.Internal.bertrand_base`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/block-level-reductions-for-the-sylvester-schur-t/index.html#bertrand-base).

## Prime divisors above $n$ of a block term divide the binomial coefficient

Let $n$, $k$
and $j$ be natural numbers with $j < n$, and let $r$ be a prime with $r > n$. If $r$ divides
$k + j$, then $r$ divides $\binom{k+n-1}{n}$.

Formalized by `Nat.SylvesterSchur.Internal.prime_dvd_seq_implies_choose`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/block-level-reductions-for-the-sylvester-schur-t/index.html#prime-dvd-seq-implies-choose).

## Primes above $n$ in the block divide the block binomial coefficient

Let $n$ and $k$
be natural numbers and let $p$ be a prime with $p > n$ and $k \le p \le k + n - 1$. Then $p$
divides $\binom{k+n-1}{n}$.

Formalized by `Nat.SylvesterSchur.Internal.prime_dvd_choose_of_mem_interval`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/block-level-reductions-for-the-sylvester-schur-t/index.html#prime-dvd-choose-of-mem-interval).

## Large prime divisors pass from a block to its binomial coefficient

Let $n$ and $k$ be
natural numbers. If some prime $p > n$ divides $k + i$ for some $i < n$, then some prime $q > n$
divides $\binom{k + n - 1}{n}$.

Formalized by `Nat.SylvesterSchur.Internal.exists_prime_dvd_choose_of_large_prime_dvd_block`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/block-level-reductions-for-the-sylvester-schur-t/index.html#exists-prime-dvd-choose-of-large-prime-d).

## A block term divisible by the block length plus two

Let $n \ge 1$ and $k$ be natural
numbers and let $s = n + 2$. If $s$ divides neither $k - 1$ nor $k - 2$ (natural-number
differences, truncated at $0$), then $s$ divides $k + i$ for some $i < n$.

The number $s$ is not assumed to be prime.

Formalized by `Nat.SylvesterSchur.Internal.exists_dvd_block_of_succ_succ_prime_not_dvd_pred`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/block-level-reductions-for-the-sylvester-schur-t/index.html#exists-dvd-block-of-succ-succ-prime-not).

## Sylvester–Schur criterion for blocks with a large start

Let $2 \le n < k$ be natural
numbers with $n! \cdot 2^{n-1} < k$. Then some prime $p > n$ divides $\binom{k + n - 1}{n}$.

Formalized by `Nat.SylvesterSchur.Internal.exists_prime_dvd_choose_of_large_start`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/block-level-reductions-for-the-sylvester-schur-t/index.html#exists-prime-dvd-choose-of-large-start).

## Sylvester–Schur criterion from the half-exponent bound

Let $1 \le n < k$ be natural
numbers and put $N = k + n - 1$. If $n! \cdot N^{\lfloor n/2 \rfloor + 1} < k^n$, then some prime
$p > n$ divides $\binom{N}{n}$.

Formalized by `Nat.SylvesterSchur.Internal.exists_prime_dvd_choose_of_half_bound`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/block-level-reductions-for-the-sylvester-schur-t/index.html#exists-prime-dvd-choose-of-half-bound).

## Blocks without large prime divisors start at most at $n^2$

Let $n \ge 38$ and $k$ be
natural numbers. If none of the $n$ consecutive integers $k, k+1, \dots, k+n-1$ has a prime
divisor greater than $n$, then $k \le n^2$.

Formalized by `Nat.SylvesterSchur.Internal.start_le_quadratic_of_no_large_prime_dvd_block`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/block-level-reductions-for-the-sylvester-schur-t/index.html#start-le-quadratic-of-no-large-prime-dvd).

## Sylvester–Schur criterion from the prime-counting bound

Let $1 \le n < k$ be natural
numbers, put $N = k + n - 1$, and let $\pi(n)$ be the number of primes at most $n$. If
$n! \cdot N^{\pi(n)} < k^n$, then some prime $p > n$ divides $\binom{N}{n}$.

Formalized by `Nat.SylvesterSchur.Internal.exists_prime_dvd_choose_of_primeCounting_bound`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/block-level-reductions-for-the-sylvester-schur-t/index.html#exists-prime-dvd-choose-of-prime-countin).

## Large prime divisor of the block binomial coefficient from the square-root primorial bound

**Large prime divisor of the block binomial coefficient from the square-root primorial
bound.** Let $n \ge 1$ and $k > n$ be natural numbers, write $N = k + n - 1$, let
$\lfloor\sqrt{N}\rfloor$ be the integer square root of $N$ and let $P$ be the product of all
primes at most $n$. If $n! \cdot N^{\lfloor\sqrt{N}\rfloor + 1} \cdot P < k^n$, then some prime
$p > n$ divides $\binom{N}{n}$.

Formalized by `Nat.SylvesterSchur.Internal.exists_prime_dvd_choose_of_sqrt_primorial_bound`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/block-level-reductions-for-the-sylvester-schur-t/index.html#exists-prime-dvd-choose-of-sqrt-primoria).

## Sylvester–Schur criterion from the Erdős layer bound

Let $1 \le n < k$ be natural
numbers, put $N = k + n - 1$ and $L = \lfloor \log_2 N \rfloor$, and write $m\#$ for the product
of the primes at most $m$. If

$$n! \cdot n\# \cdot \prod_{i=2}^{L} \lfloor N^{1/i} \rfloor\# < k^n,$$

then some prime $p > n$ divides $\binom{N}{n}$.

Formalized by `Nat.SylvesterSchur.Internal.exists_prime_dvd_choose_of_erdos_layers_bound`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/block-level-reductions-for-the-sylvester-schur-t/index.html#exists-prime-dvd-choose-of-erdos-layers).

## Sylvester–Schur criterion from the Erdős layer bound with a one-third first layer

Let
$n < k$ be natural numbers, put $N = k + n - 1$ and $L = \lfloor \log_2 N \rfloor$, and assume
$N \ge 6$. Write $m\#$ for the product of the primes at most $m$. If

$$n! \cdot \lfloor N/3 \rfloor\# \cdot \prod_{i=2}^{L} \lfloor N^{1/i} \rfloor\# < k^n,$$

then some prime $p > n$ divides $\binom{N}{n}$.

Formalized by `Nat.SylvesterSchur.Internal.exists_prime_dvd_choose_of_erdos_div_three_layers_bound`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/block-level-reductions-for-the-sylvester-schur-t/index.html#exists-prime-dvd-choose-of-erdos-div-thr).

## Sylvester–Schur criterion from the coarse power-of-four Erdős bound

Let $1 \le n < k$ be
natural numbers and put $N = k + n - 1$. If

$$n! \cdot 4^{n + \lfloor \sqrt N \rfloor \lfloor \log_2 N \rfloor} < k^n,$$

then some prime $p > n$ divides $\binom{N}{n}$.

Formalized by `Nat.SylvesterSchur.Internal.exists_prime_dvd_choose_of_erdos_layers_four_pow_bound`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/block-level-reductions-for-the-sylvester-schur-t/index.html#exists-prime-dvd-choose-of-erdos-layers-2).

## Sylvester–Schur criterion from the three-layer power-of-four Erdős bound

Let
$1 \le n < k$ be natural numbers and put $N = k + n - 1$. If

$$n! \cdot 4^{n+\lfloor\sqrt N\rfloor+\lfloor N^{1/3}\rfloor\lfloor\log_2 N\rfloor} < k^n,$$

then some prime $p > n$ divides $\binom{N}{n}$.

Formalized by `Nat.SylvesterSchur.Internal.exists_prime_dvd_choose_of_erdos_layers_three_layers_bound`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/block-level-reductions-for-the-sylvester-schur-t/index.html#exists-prime-dvd-choose-of-erdos-layers-3).

## Large prime divisor of the block binomial coefficient from the smooth-number count

Let $n$ and $k$ be natural numbers, let $\pi(n)$ be the number of primes at most $n$, and let
$\lfloor\sqrt{k+n-1}\rfloor$ be the integer square root. If
$2^{\pi(n)} \lfloor\sqrt{k+n-1}\rfloor < n$, then some prime $p > n$ divides
$\binom{k+n-1}{n}$.

Otherwise all $n$ integers $k, \dots, k+n-1$ would be positive, at most $k+n-1$ and free of
prime factors greater than $n$, and there are at most $2^{\pi(n)} \lfloor\sqrt{k+n-1}\rfloor$
such integers.

Formalized by `Nat.SylvesterSchur.Internal.exists_prime_dvd_choose_of_smooth_count_bound`, a lemma declared in [MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/BlockReductions.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/block-level-reductions-for-the-sylvester-schur-t/index.html#exists-prime-dvd-choose-of-smooth-count).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Block-level reductions for the Sylvester-Schur theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/block-level-reductions-for-the-sylvester-schur-t/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/block-level-reductions-for-the-sylvester-schur-t)
