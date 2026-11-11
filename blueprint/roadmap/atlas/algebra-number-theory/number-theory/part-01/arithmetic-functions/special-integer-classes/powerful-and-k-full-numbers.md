---
declaration: section
origin: cited
lean: Nat.IsKFull, Nat.powerfulPart, Nat.powerfulPart_factorization, Nat.powerfulPart_dvd, Nat.isKFull_iff_factorization, Nat.not_isKFull_zero, Nat.isKFull_one, Nat.isKFull_k_eq_zero
statement: formalized
proof: formalized
---

# Powerful and k-full numbers

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-and-k-full-numbers/index.html).

## $k$-full numbers

Let $k$ be a natural number. A natural number $n$ is $k$-full if
$n \ne 0$ and $p^k$ divides $n$ for every prime $p$ dividing $n$.

The definition makes sense for every $k$; the source considers only $k \ge 2$.

Formalized by `Nat.IsKFull`, a definition declared in [MathlibExt/NumberTheory/KFull.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/KFull.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-and-k-full-numbers/index.html#is-kfull).

## Powerful part of a natural number

For a natural number $n \ge 1$ and a prime $p$, let
$v_p(n)$ be the exponent of $p$ in $n$. The powerful (or $2$-full) part of $n$ is the product of
the prime powers $p^{v_p(n)}$ over the primes $p$ dividing $n$ with $v_p(n) \ge 2$ (and $1$ if
there are none). The powerful part of $0$ is defined to be $1$.

Formalized by `Nat.powerfulPart`, a definition declared in [MathlibExt/NumberTheory/KFull.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/KFull.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-and-k-full-numbers/index.html#powerful-part).

## Prime exponents of the powerful part

For natural numbers $n$ and $p$, write $v_p(n)$ for
the exponent of $p$ in the prime factorization of $n$ (it is $0$ when $p$ is not a prime factor
of $n$). Then the exponent of $p$ in the powerful part of $n$ equals $v_p(n)$ if $v_p(n) \ge 2$,
and $0$ otherwise.

Formalized by `Nat.powerfulPart_factorization`, a theorem declared in [MathlibExt/NumberTheory/KFull.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/KFull.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-and-k-full-numbers/index.html#powerful-part-factorization).

## The powerful part of $n$ divides $n$

For every natural number $n$, the powerful part
of $n$ divides $n$.

Formalized by `Nat.powerfulPart_dvd`, a theorem declared in [MathlibExt/NumberTheory/KFull.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/KFull.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-and-k-full-numbers/index.html#powerful-part-dvd).

## Factorization criterion for $k$-full numbers

Let $k$ and $n$ be natural numbers with
$n \ne 0$, and write $v_p(n)$ for the exponent of a prime $p$ in the prime factorization of
$n$. Then $n$ is $k$-full if and only if $k \le v_p(n)$ for every prime $p$ dividing $n$.

Formalized by `Nat.isKFull_iff_factorization`, a theorem declared in [MathlibExt/NumberTheory/KFull.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/KFull.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-and-k-full-numbers/index.html#is-kfull-iff-factorization).

## Zero is not $k$-full

For every natural number $k$, the number $0$ is not $k$-full.

The source works with positive integers.

Formalized by `Nat.not_isKFull_zero`, a theorem declared in [MathlibExt/NumberTheory/KFull.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/KFull.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-and-k-full-numbers/index.html#not-is-kfull-zero).

## One is $k$-full

For every natural number $k$, the number $1$ is $k$-full: it is nonzero
and has no prime divisors.

Formalized by `Nat.isKFull_one`, a theorem declared in [MathlibExt/NumberTheory/KFull.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/KFull.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-and-k-full-numbers/index.html#is-kfull-one).

## The $0$-full numbers

A natural number $n$ is $0$-full if and only if $n \ne 0$, since
$p^0 = 1$ divides $n$ for every prime $p$.

The source considers only $k$-full numbers with $k \ge 2$.

Formalized by `Nat.isKFull_k_eq_zero`, a theorem declared in [MathlibExt/NumberTheory/KFull.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/KFull.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-and-k-full-numbers/index.html#is-kfull-k-eq-zero).

## The $1$-full numbers

A natural number $n$ is $1$-full if and only if $n \ne 0$, since
$p^1 = p$ divides $n$ for every prime $p$ dividing $n$.

The source considers only $k$-full numbers with $k \ge 2$.

Formalized by `Nat.isKFull_k_eq_one`, a theorem declared in [MathlibExt/NumberTheory/KFull.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/KFull.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-and-k-full-numbers/index.html#is-kfull-k-eq-one).

## Monotonicity of $k$-fullness in $k$

Let $j \le k$ be natural numbers. Every $k$-full
natural number is $j$-full.

Formalized by `Nat.isKFull_mono`, a theorem declared in [MathlibExt/NumberTheory/KFull.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/KFull.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-and-k-full-numbers/index.html#is-kfull-mono).

## For $k \ge 2$, $k$-full numbers are $2$-full

Let $k \ge 2$ be a natural number. Every
$k$-full natural number is $2$-full.

Formalized by `Nat.isKFull_of_two_le`, a theorem declared in [MathlibExt/NumberTheory/KFull.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/KFull.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-and-k-full-numbers/index.html#is-kfull-of-two-le).

## The $2$-full numbers

A natural number $n$ is $2$-full if and only if $n \ne 0$ and $p^2$
divides $n$ for every prime $p$ dividing $n$. These are the squarefull (also called powerful)
numbers.

Formalized by `Nat.isKFull_two`, a theorem declared in [MathlibExt/NumberTheory/KFull.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/KFull.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-and-k-full-numbers/index.html#is-kfull-two).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Powerful and k-full numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-and-k-full-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-and-k-full-numbers)
