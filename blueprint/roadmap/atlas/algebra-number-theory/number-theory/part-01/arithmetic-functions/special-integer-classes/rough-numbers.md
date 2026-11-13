---
declaration: section
origin: cited
lean: Nat.IsRough, Nat.isRough_iff, Nat.IsRough.ne_zero, Nat.IsRough.pos, Nat.IsRough.lt_of_prime_dvd, Nat.isRough_iff_primeFactorsList, Nat.isRough_one, Nat.Prime.isRough_iff
statement: formalized
proof: formalized
---

# Rough numbers

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/rough-numbers/index.html).

## Rough numbers

Let $n$ and $k$ be natural numbers. Then $n$ is $k$-rough if $n \neq 0$
and every prime $p$ dividing $n$ satisfies $k < p$; that is, $n$ is positive and has no prime
factor at most $k$.

In particular $0$ is not rough, and $1$ is $k$-rough for every $k$ by vacuity.

## Sources

- Pandey, arXiv 2307.14890v1, footnote definition (`hybrid.tex` line 91).

Formalized by `Nat.IsRough`, a definition declared in [MathlibExt/NumberTheory/RoughNumbers.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RoughNumbers.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/rough-numbers/index.html#is-rough).

## Characterization of rough numbers

For natural numbers $n$ and $k$, $n$ is $k$-rough
if and only if $n \neq 0$ and every prime $p$ dividing $n$ satisfies $k < p$.

Formalized by `Nat.isRough_iff`, a theorem declared in [MathlibExt/NumberTheory/RoughNumbers.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RoughNumbers.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/rough-numbers/index.html#is-rough-iff).

## Rough numbers are nonzero

For every natural number $k$, every $k$-rough natural number $n$
satisfies $n \ne 0$.

Formalized by `Nat.IsRough.ne_zero`, a theorem declared in [MathlibExt/NumberTheory/RoughNumbers.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RoughNumbers.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/rough-numbers/index.html#ne-zero).

## Rough numbers are positive

For every natural number $k$, every $k$-rough natural number
$n$ satisfies $n > 0$.

Formalized by `Nat.IsRough.pos`, a theorem declared in [MathlibExt/NumberTheory/RoughNumbers.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RoughNumbers.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/rough-numbers/index.html#pos).

## Prime divisors of a rough number exceed the bound

Let $n$, $k$ and $p$ be natural
numbers. If $n$ is $k$-rough and $p$ is a prime dividing $n$, then $k < p$.

Formalized by `Nat.IsRough.lt_of_prime_dvd`, a theorem declared in [MathlibExt/NumberTheory/RoughNumbers.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RoughNumbers.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/rough-numbers/index.html#lt-of-prime-dvd).

## Roughness through the list of prime factors

For natural numbers $n$ and $k$, $n$ is
$k$-rough if and only if $n \neq 0$ and every prime in the list of prime factors of $n$
(with multiplicity) is greater than $k$.

Formalized by `Nat.isRough_iff_primeFactorsList`, a theorem declared in [MathlibExt/NumberTheory/RoughNumbers.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RoughNumbers.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/rough-numbers/index.html#is-rough-iff-prime-factors-list).

## The number $1$ is rough

For every natural number $k$, the number $1$ is $k$-rough.

This holds vacuously, since $1$ has no prime divisors.

Formalized by `Nat.isRough_one`, a theorem declared in [MathlibExt/NumberTheory/RoughNumbers.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RoughNumbers.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/rough-numbers/index.html#is-rough-one).

## A prime is rough exactly above the bound

For natural numbers $p$ and $k$ with $p$
prime, $p$ is $k$-rough if and only if $k < p$.

Formalized by `Nat.Prime.isRough_iff`, a theorem declared in [MathlibExt/NumberTheory/RoughNumbers.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RoughNumbers.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/rough-numbers/index.html#is-rough-iff-2).

## Divisors of rough numbers are rough

Let $k$ be a natural number. If a natural number $m$
is $k$-rough and $d$ is a nonzero divisor of $m$, then $d$ is $k$-rough.

Formalized by `Nat.IsRough.of_dvd`, a theorem declared in [MathlibExt/NumberTheory/RoughNumbers.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RoughNumbers.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/rough-numbers/index.html#of-dvd).

## A product is rough exactly when both factors are

For natural numbers $m$, $n$ and
$k$, the product $mn$ is $k$-rough if and only if both $m$ and $n$ are $k$-rough.

Formalized by `Nat.isRough_mul`, a theorem declared in [MathlibExt/NumberTheory/RoughNumbers.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RoughNumbers.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/rough-numbers/index.html#is-rough-mul).

## Products of rough numbers are rough

For natural numbers $m$, $n$ and $k$, if $m$ and
$n$ are both $k$-rough, then $mn$ is $k$-rough.

Formalized by `Nat.IsRough.mul`, a theorem declared in [MathlibExt/NumberTheory/RoughNumbers.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RoughNumbers.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/rough-numbers/index.html#mul).

## Roughness is antitone in the bound

Let $k$ and $l$ be natural numbers with $l \le k$.
Every $k$-rough natural number is $l$-rough.

Formalized by `Nat.IsRough.of_le`, a theorem declared in [MathlibExt/NumberTheory/RoughNumbers.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RoughNumbers.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/rough-numbers/index.html#of-le).

## Only $1$ is rough and smooth at the same bound

Let $n$ and $k$ be natural
numbers. If $n$ is $k$-rough and $n$ is positive with every prime factor less than
$k + 1$, then $n = 1$.

Formalized by `Nat.IsRough.eq_one_of_mem_smoothNumbers`, a theorem declared in [MathlibExt/NumberTheory/RoughNumbers.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RoughNumbers.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/rough-numbers/index.html#eq-one-of-mem-smooth-numbers).

## Rough numbers other than $1$ lie in Mathlib's rough numbers up to a bound

Let $n$,
$N$ and $k$ be natural numbers. If $n$ is $k$-rough, $n \le N$ and $n \ne 1$, then $n$ belongs
to the set of natural numbers $m$ with $1 \le m \le N$ that are not $(k+1)$-smooth, where $m$ is
$(k+1)$-smooth when $m > 0$ and every prime factor of $m$ is less than $k + 1$; for $m \ge 1$,
not being $(k+1)$-smooth means having a prime factor $p \ge k + 1$.

This set is Mathlib's set of rough numbers up to $N$ at bound $k + 1$. It asks only for some
prime factor $p \ge k + 1$, while $k$-roughness asks that every prime factor exceed $k$.

Formalized by `Nat.IsRough.mem_roughNumbersUpTo`, a theorem declared in [MathlibExt/NumberTheory/RoughNumbers.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RoughNumbers.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/rough-numbers/index.html#mem-rough-numbers-up-to).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rough numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/rough-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/rough-numbers)
