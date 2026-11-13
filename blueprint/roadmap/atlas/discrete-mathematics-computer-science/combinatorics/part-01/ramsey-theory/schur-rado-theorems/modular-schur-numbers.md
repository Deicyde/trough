---
declaration: section
origin: cited
lean: MetaMathlibExt.IsSumFreeMod, MetaMathlibExt.HasSumFreePartitionMod, MetaMathlibExt.modularSchurNumber, MetaMathlibExt.hasSumFreePartitionMod_zero, MetaMathlibExt.not_isSumFreeMod_of_dvd_mem, MetaMathlibExt.isSumFreeMod_three_two_singleton_one, MetaMathlibExt.not_isSumFreeMod_singleton_one_iff, MetaMathlibExt.modularSchurNumber_eq_zero_iff
statement: formalized
---

# Modular Schur numbers

25 results, 6 proved and 19 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html).

## Sum-free sets modulo $m$

For natural numbers $m$ and $l$, a set $A$ of integers is
$l$-sum-free modulo $m$ if there are no $x_1, \dots, x_l, y \in A$ (repetitions allowed) with
$x_1 + \dots + x_l \equiv y \pmod{m}$.

## Sources

- J. Chappelon, M. P. Revuelta Marchena, M. I. Sanz Domínguez, *Modular Schur numbers*, Electron. J. Combin. 20(2) (2013), Section 1.1, as used in Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Section 1.

Formalized by `MetaMathlibExt.IsSumFreeMod`, a definition declared in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#is-sum-free-mod).

## Sum-free partitions modulo $m$

For natural numbers $m$, $k$, $l$ and $n$, the range
$\{1, \dots, n\}$ admits a partition into $k$ classes that are $l$-sum-free modulo $m$ if there
is a coloring $c$ of the natural numbers with $k$ colors such that, for each color $j$, the set
of integers $a$ with $1 \le a \le n$ and $c(a) = j$ is $l$-sum-free modulo $m$. Classes may be
empty; for $k = 0$ there is no coloring, so the property fails for every $n$, including $n = 0$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Section 1.

Formalized by `MetaMathlibExt.HasSumFreePartitionMod`, a definition declared in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#has-sum-free-partition-mod).

## Modular Schur number

For natural numbers $m$, $k$ and $l$, the generalized Schur number
modulo $m$, written $S_m(k, l)$, is the largest natural number $n$ such that $\{1, \dots, n\}$
admits a partition into $k$ (possibly empty) classes that are each $l$-sum-free modulo $m$; it is
$0$ when there is no largest such $n$.

For $m \ge 1$ and $k \ge 1$ such a largest $n$ exists, since $n = 0$ is admissible and every
admissible $n$ is at most $m - 1$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Section 1.

Formalized by `MetaMathlibExt.modularSchurNumber`, a definition declared in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#modular-schur-number).

## The empty range has a sum-free partition

For all natural numbers $m$, $l$ and
$k \ge 1$, the empty range $\{1, \dots, 0\}$ admits a partition into $k$ classes that are
$l$-sum-free modulo $m$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Section 1 (`0 ≤ S_m(k, l)`).

Formalized by `MetaMathlibExt.hasSumFreePartitionMod_zero`, a theorem declared in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#has-sum-free-partition-mod-zero).

## Sets containing a multiple of the modulus are not sum-free

Let $m$ and $l$ be natural
numbers and let $A$ be a set of integers. If $A$ contains an integer $a$ divisible by $m$, then
$A$ is not $l$-sum-free modulo $m$: the sum of $l$ copies of $a$ is congruent to $a$ modulo $m$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Section 1 (the bound `S_m(k, l) ≤ m - 1`).

Formalized by `MetaMathlibExt.not_isSumFreeMod_of_dvd_mem`, a theorem declared in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#not-is-sum-free-mod-of-dvd-mem).

## $\{1\}$ is $2$-sum-free modulo $3$

The singleton $\{1\}$ is $2$-sum-free modulo $3$,
since $1 + 1 \not\equiv 1 \pmod{3}$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Theorem 2 context.

Formalized by `MetaMathlibExt.isSumFreeMod_three_two_singleton_one`, a theorem declared in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#is-sum-free-mod-three-two-singleton-one).

## When the singleton $\{1\}$ is sum-free

Let $m \ge 1$ and $l$ be natural
numbers. The singleton $\{1\}$ is not $l$-sum-free modulo $m$ if and only if
$l \equiv 1 \pmod{m}$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Corollary 1.

Stated but not proved: `MetaMathlibExt.not_isSumFreeMod_singleton_one_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#not-is-sum-free-mod-singleton-one-iff).

## Vanishing of modular Schur numbers

Let $m$, $k$ and $l$ be positive integers. The
generalized Schur number $S_m(k, l)$, the largest $n$ such that $\{1, \dots, n\}$ admits a
partition into $k$ classes that are $l$-sum-free modulo $m$, equals $0$ if and only if
$l \equiv 1 \pmod{m}$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Corollary 2.

Stated but not proved: `MetaMathlibExt.modularSchurNumber_eq_zero_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#modular-schur-number-eq-zero-iff).

## Congruence upper bound for modular Schur numbers

Let $m$, $k$, $l$ and $a$ be natural
numbers with $k \ge 1$, $l \ge 1$ and $1 \le a \le m - 1$, and let $d = \gcd(a, m)$. If
$l \equiv 1 \pmod{m/d}$, then the generalized Schur number $S_m(k, l)$ modulo $m$ satisfies
$S_m(k, l) < a$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Corollary 3.

Stated but not proved: `MetaMathlibExt.modularSchurNumber_lt_of_modEq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#modular-schur-number-lt-of-mod-eq).

## Modular Schur numbers modulo an even number

Let $k$, $l$ and $n$ be natural numbers with
$k \ge 2$, $n \ge 2$, $l \ge 1$ and $l \not\equiv 1 \pmod{2n}$, and let $S_{2n}(k, l)$ be the
generalized Schur number modulo $2n$. If $l \equiv n + 1 \pmod{2n}$, then $S_{2n}(k, l) = 1$;
otherwise $S_{2n}(k, l) \ge 2$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Corollary 4.

Stated but not proved: `MetaMathlibExt.modularSchurNumber_two_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#modular-schur-number-two-mul).

## Modular Schur numbers attaining $m - 1$

Let $l \ge 2$ and $m \ge 2$ be natural numbers
such that $l \not\equiv 1 \pmod{d}$ for every divisor $d \ne 1$ of $m$, and let $k \ge m - 1$.
Then the generalized Schur number $S_m(k, l)$, the largest $n$ such that $\{1, \dots, n\}$
admits a partition into $k$ classes that are $l$-sum-free modulo $m$, equals $m - 1$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Corollary 5.

Stated but not proved: `MetaMathlibExt.modularSchurNumber_eq_sub_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#modular-schur-number-eq-sub-one).

## Lower bound for modular Schur numbers modulo a prime power

Let $p$ be a prime, let $i$
and $l$ be positive integers with $l \not\equiv 1 \pmod{p}$, and let $1 \le k \le p - 1$. Then
the generalized Schur number $S_{p^i}(k, l)$, the largest $n$ such that $\{1, \dots, n\}$ admits
a partition into $k$ classes that are $l$-sum-free modulo $p^i$, is at least $k$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Corollary 6.

Stated but not proved: `MetaMathlibExt.le_modularSchurNumber_prime_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#le-modular-schur-number-prime-pow).

## Modular Schur numbers modulo a prime power for many classes

Let $p$ be a prime, let $i$
and $l$ be positive integers with $l \not\equiv 1 \pmod p$, and let $k$ be a natural number with
$k \ge p^i - 1$. Then the generalized Schur number modulo $p^i$ satisfies
$S_{p^i}(k, l) = p^i - 1$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Corollary 7.

Stated but not proved: `MetaMathlibExt.modularSchurNumber_prime_pow_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#modular-schur-number-prime-pow-eq).

## Modular Schur numbers modulo a prime

Let $p$ be a prime and let $l$ be a positive integer
with $l \ge p - 1$ and $l \not\equiv 1 \pmod p$. Then the generalized Schur number modulo $p$
satisfies $S_p(k, l) = k$ for every natural number $k$ with $1 \le k \le p - 1$, and
$S_p(k, l) = p - 1$ for every natural number $k \ge p - 1$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Corollary 8.

Stated but not proved: `MetaMathlibExt.modularSchurNumber_prime` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#modular-schur-number-prime).

## Singletons are sum-free modulo a prime power

Let $p$ be a prime, let $i$ and $l$ be
positive integers with $l \not\equiv 1 \pmod{p}$, and let $a$ be a natural number not divisible
by $p^i$. Then the singleton $\{a\}$ is $l$-sum-free modulo $p^i$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Lemma 1.

Stated but not proved: `MetaMathlibExt.isSumFreeMod_singleton_prime_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#is-sum-free-mod-singleton-prime-pow).

## Elements of a sum-free pair are congruent modulo $p$

Let $p$ be a prime, let $i$ be a
positive integer, and let $l$ be a natural number with $l \ge p^i - 1$ and
$l \not\equiv 1 \pmod{p}$. If $a$ and $b$ are natural numbers such that $\{a, b\}$ is
$l$-sum-free modulo $p^i$, then $a \equiv b \pmod{p}$.

Since subsets of $l$-sum-free sets are $l$-sum-free, the hypothesis says exactly that $a$ and
$b$ lie in a common $l$-sum-free set modulo $p^i$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Lemma 2, part 1.

Stated but not proved: `MetaMathlibExt.modEq_of_isSumFreeMod_pair` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#mod-eq-of-is-sum-free-mod-pair).

## Modular Schur numbers modulo $2$

For all positive integers $k$ and $l$, the modular
Schur number $S_2(k, l)$ equals $0$ when $l$ is odd and equals $1$ when $l$ is even.

The source quotes this result from its reference [4], Chappelon, Revuelta Marchena and Sanz
Domínguez, *Modular Schur numbers* (2013).

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Theorem 1.

Stated but not proved: `MetaMathlibExt.modularSchurNumber_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#modular-schur-number-two).

## Modular Schur numbers modulo 3

Let $k$ and $l$ be positive integers and let $S_3(k, l)$
be the generalized Schur number modulo $3$. If $l \equiv 1 \pmod 3$, then $S_3(k, l) = 0$.
Otherwise $S_3(1, l) = 1$, and $S_3(k, l) = 2$ for every $k \ge 2$.

The paper quotes this result from Chappelon, Revuelta Marchena, and Sanz Domínguez,
*Modular Schur numbers* (2013).

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Theorem 2.

Stated but not proved: `MetaMathlibExt.modularSchurNumber_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#modular-schur-number-three).

## Solutions of a linear congruence

Let $a$ and $b$ be integers, let $m$ be a positive
integer, and let $d = \gcd(a, m)$. The congruence $a x \equiv b \pmod{m}$ has an integer
solution if and only if $d \mid b$. If $d \mid b$, then exactly $d$ of the numbers
$x \in \{0, 1, \dots, m - 1\}$ are solutions. Moreover, if $x_0$ is a solution, then an integer
$x$ is a solution if and only if $x \equiv x_0 + u \cdot (m / d) \pmod{m}$ for some integer $u$
with $0 \le u \le d - 1$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Theorem 3, quoting a textbook result ([3]).

Stated but not proved: `MetaMathlibExt.linear_congruence_solutions` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#linear-congruence-solutions).

## When a singleton set is sum-free

Let $a$, $l$ and $m$ be natural numbers with
$l \ge 1$, $m \ge 1$ and $m \nmid a$, and let $d = \gcd(a, m)$. If $d = 1$, then $\{a\}$ is not
$l$-sum-free modulo $m$ if and only if $l \equiv 1 \pmod{m}$. If $d > 1$, then $\{a\}$ is not
$l$-sum-free modulo $m$ if and only if $l \equiv 1 \pmod{m/d}$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Theorem 4.

Stated but not proved: `MetaMathlibExt.not_isSumFreeMod_singleton_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#not-is-sum-free-mod-singleton-iff).

## When the one-class modular Schur number equals one

Let $l$ and $m$ be natural numbers with
$l \ge 2$, $m \ge 2$ and $l \not\equiv 1 \pmod m$. Then the generalized Schur number $S_m(1, l)$
modulo $m$ equals $1$ if and only if $l = 2$ or $2l \ge m + 1$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Theorem 5.

Stated but not proved: `MetaMathlibExt.modularSchurNumber_one_eq_one_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#modular-schur-number-one-eq-one-iff).

## Modular Schur numbers modulo 4

Let $k$ and $l$ be positive integers and let $S_4(k, l)$
be the generalized Schur number modulo $4$. If $l \equiv 1 \pmod 4$, then $S_4(k, l) = 0$.
Otherwise, if $k = 1$, or if $k \ge 2$ and $l \equiv 3 \pmod 4$, then $S_4(k, l) = 1$; and if
$k \ge 2$ and $l \equiv 0$ or $2 \pmod 4$, then $S_4(k, l) = 3$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Theorem 6.

Stated but not proved: `MetaMathlibExt.modularSchurNumber_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#modular-schur-number-four).

## Modular Schur numbers modulo 6

Let $k$ and $l$ be positive integers and let $S_6(k, l)$
be the generalized Schur number modulo $6$. If $l \equiv 1 \pmod 6$, then $S_6(k, l) = 0$.
Otherwise $S_6(k, l) = 1$ if $k = 1$ and $l \ne 3$, or $k \ge 2$ and $l \equiv 4 \pmod 6$;
$S_6(k, l) = 2$ if $k = 1$ and $l = 3$, or $k \ge 2$ and $l \equiv 3$ or $5 \pmod 6$;
$S_6(k, l) = 3$ if $k = 2$, $l \equiv 0$ or $2 \pmod 6$, and $l \ge 6$; $S_6(k, l) = 4$ if
$k = l = 2$; and $S_6(k, l) = 5$ if $k \ge 3$ and $l \equiv 0$ or $2 \pmod 6$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Theorem 7.

Stated but not proved: `MetaMathlibExt.modularSchurNumber_six` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#modular-schur-number-six).

## Modular Schur numbers modulo 5

Let $k$ and $l$ be positive integers and let $S_5(k, l)$
be the generalized Schur number modulo $5$. If $l \equiv 1 \pmod 5$, then $S_5(k, l) = 0$.
Otherwise $S_5(1, l) = 1$; if $k \in \{2, 3\}$ and $l \ne 2$, then $S_5(k, l) = k$; and if
$k \in \{2, 3\}$ and $l = 2$, or if $k \ge 4$, then $S_5(k, l) = 4$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Theorem 9.

Stated but not proved: `MetaMathlibExt.modularSchurNumber_five` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#modular-schur-number-five).

## Modular Schur numbers modulo 7

Let $k$ and $l$ be positive integers and let $S_7(k, l)$
be the generalized Schur number modulo $7$. If $l \equiv 1 \pmod 7$, then $S_7(k, l) = 0$.
Otherwise $S_7(k, l) = 1$ if $k = 1$ and $l \ne 3$; $S_7(k, l) = 2$ if $k = 1$ and $l = 3$, or
$k = 2$ and $l \ge 4$; $S_7(k, l) = 3$ if $k = 2$ and $l \in \{2, 3\}$, or $k = 3$ and $l \ge 5$;
$S_7(k, l) = 4$ if $k = 4$ and $l \ge 5$; $S_7(k, l) = 5$ if $k = 3$ and $l = 3$, or $k = 5$ and
$l \ge 5$; and $S_7(k, l) = 6$ if $k = 3$ and $l \in \{2, 4\}$, or $k \in \{4, 5\}$ and
$2 \le l \le 4$, or $k \ge 6$.

## Sources

- Jourdan D'orville, Kai An Sim, Kok Bin Wong, and Chee Kit Ho, *Modular Generalizations of Schur Numbers*, INTEGERS 25 (2025), Article A62, Theorem 10.

Stated but not proved: `MetaMathlibExt.modularSchurNumber_seven` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/ModularSchurNumbersWanted.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html#modular-schur-number-seven).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Modular Schur numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/modular-schur-numbers)
