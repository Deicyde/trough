---
declaration: section
origin: cited
lean: IntegerSequence.IsPrimitiveDivisor, IntegerSequence.IsPrimitivePrimeDivisor, IntegerSequence.IsPrimitiveDivisor.le_of_dvd, IntegerSequence.IsPrimitiveDivisor.unique, IntegerSequence.IsPrimitivePrimeDivisor.unique, LucasSequence.IsPrimitiveDivisor, MetaMathlibExt.exists_isPrimitiveDivisor_fib, MetaMathlibExt.somer_eventually_has_primitive_prime_divisor
statement: formalized
---

# Primitive divisors

8 results, 7 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/primitive-divisors/index.html).

## Primitive divisor of an integer sequence

Let $(a_s)_{s \ge 0}$ be a sequence of integers
and let $m$ and $u$ be natural numbers. Then $u$ is a primitive divisor of $a_m$ when $m \ge 1$,
$u \ge 2$, $u$ divides $a_m$, and $u$ divides no $a_s$ with $1 \le s < m$.

Formalized by `IntegerSequence.IsPrimitiveDivisor`, a definition declared in [MathlibExt/NumberTheory/PrimitiveDivisor.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimitiveDivisor.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/primitive-divisors/index.html#is-primitive-divisor).

## Primitive prime divisor of an integer sequence

Let $(a_s)_{s \ge 0}$ be a sequence of
integers and let $m$ and $u$ be natural numbers. Then $u$ is a primitive prime divisor of $a_m$ when
$u$ is prime and $u$ is a primitive divisor of $a_m$.

Formalized by `IntegerSequence.IsPrimitivePrimeDivisor`, a definition declared in [MathlibExt/NumberTheory/PrimitiveDivisor.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimitiveDivisor.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/primitive-divisors/index.html#is-primitive-prime-divisor).

## A primitive divisor appears at the least positive index

Let $(a_s)_{s \ge 0}$ be a sequence
of integers and let the natural number $u$ be a primitive divisor of $a_m$. If $n \ge 1$ and $u$
divides $a_n$, then $m \le n$.

Formalized by `IntegerSequence.IsPrimitiveDivisor.le_of_dvd`, a theorem declared in [MathlibExt/NumberTheory/PrimitiveDivisor.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimitiveDivisor.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/primitive-divisors/index.html#le-of-dvd).

## A primitive divisor occurs at only one index

Let $(a_s)_{s \ge 0}$ be a sequence of
integers. If a natural number $u$ is a primitive divisor of both $a_m$ and $a_n$, then $m = n$.

Formalized by `IntegerSequence.IsPrimitiveDivisor.unique`, a theorem declared in [MathlibExt/NumberTheory/PrimitiveDivisor.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimitiveDivisor.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/primitive-divisors/index.html#unique).

## A primitive prime divisor occurs at only one index

Let $(a_s)_{s \ge 0}$ be a sequence of
integers. If a natural number $u$ is a primitive prime divisor of both $a_m$ and $a_n$, then
$m = n$.

Formalized by `IntegerSequence.IsPrimitivePrimeDivisor.unique`, a theorem declared in [MathlibExt/NumberTheory/PrimitiveDivisor.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimitiveDivisor.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/primitive-divisors/index.html#unique-2).

## Primitive divisor relative to a discriminant

Let $u_0, u_1, u_2, \dots$ be a sequence
of integers and let $D$ be an integer (for a Lucas pair $(\alpha, \beta)$, the discriminant
$D = (\alpha - \beta)^2$). A natural number $p$ is a primitive divisor of $u_n$ when $n \ge 1$, $p$
is prime, $p$ divides $u_n$, and $p$ does not divide $D \, u_1 u_2 \cdots u_{n-1}$ (for $n = 1$ the
product is empty, and the condition is that $p$ does not divide $D$).

Formalized by `LucasSequence.IsPrimitiveDivisor`, a definition declared in [MathlibExt/NumberTheory/Recurrences/PrimitiveDivisor.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/PrimitiveDivisor.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/primitive-divisors/index.html#is-primitive-divisor-2).

## Primitive divisors of Fibonacci numbers

Write $F_j$ for the $j$-th Fibonacci number.
For every natural number $n \ge 7$ with $n \ne 12$, $F_n$ has a primitive divisor with respect
to the discriminant $5$: there is a prime $p$ that divides $F_n$ but does not divide
$5 F_1 F_2 \cdots F_{n-1}$.

This is the Fibonacci case of Carmichael's theorem on Lucas sequences, with
$\alpha = (1 + \sqrt{5})/2$ and $\beta = (1 - \sqrt{5})/2$, so that $(\alpha - \beta)^2 = 5$.

## Sources

- Haojie Hong, *On big primitive divisors of Fibonacci numbers*, arXiv:2312.04354v1, `bigPFn.tex` lines 153–158 (<https://arxiv.org/abs/2312.04354>); R. D. Carmichael, *On the numerical factors of the arithmetic forms αⁿ±βⁿ*, Ann. of Math. (2) 15 (1913), 30–70.

Formalized by `MetaMathlibExt.exists_isPrimitiveDivisor_fib`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/FibonacciPrimitiveDivisor.lean, line 1291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/FibonacciPrimitiveDivisor.lean#L1291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/primitive-divisors/index.html#exists-is-primitive-divisor-fib).

## Somer's primitive divisor theorem

Let $P$ and $Q$ be integers with $Q \ne 0$, and let
$(u_n)_{n \ge 0}$ be the integer sequence with $u_0 = 0$, $u_1 = 1$ and
$u_{n+2} = Pu_{n+1} - Qu_n$ (the Lucas sequence of the first kind). Suppose the sequence is
nondegenerate: whenever complex numbers $\alpha$ and $\beta$ satisfy $\alpha + \beta = P$,
$\alpha\beta = Q$ and $\beta \ne 0$, no power $(\alpha / \beta)^k$ with $k \ge 1$ equals
$1$. Then for all sufficiently large $n$ the term $u_n$ has a primitive prime divisor: a
prime $p$ that divides $u_n$ but divides no $u_m$ with $0 < m < n$.

Nondegeneracy also excludes the double-root case $\alpha = \beta$.

## Sources

- Chris Smyth, *The Terms in Lucas Sequences Divisible by Their Indices*, Journal of Integer Sequences 13 (2010), Article 10.2.4, invoking Somer's Theorem 1, lines 632–634, <https://cs.uwaterloo.ca/journals/JIS/VOL13/Smyth/smyth2.tex>.

Stated but not proved: `MetaMathlibExt.somer_eventually_has_primitive_prime_divisor` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/SomerPrimitiveDivisorWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/SomerPrimitiveDivisorWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/primitive-divisors/index.html#somer-eventually-has-primitive-prime-div).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Primitive divisors](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/primitive-divisors/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/primitive-divisors)
