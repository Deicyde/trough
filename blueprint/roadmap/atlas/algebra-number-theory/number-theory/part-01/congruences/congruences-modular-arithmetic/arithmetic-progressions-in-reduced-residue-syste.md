---
declaration: section
origin: cited
lean: MetaMathlibExt.reducedResidueWindow, MetaMathlibExt.longestAPLengthWithDiff, MetaMathlibExt.longestAPLength, MetaMathlibExt.absLeastAPLength, MetaMathlibExt.apLength_le, MetaMathlibExt.longestAPLength_le, MetaMathlibExt.mem_reducedResidueWindow_neg_three_five, MetaMathlibExt.absLeastAPLength_five
statement: formalized
---

# Arithmetic progressions in reduced residue systems

23 results, 8 proved and 15 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html).

## The reduced residue system $R_m(n)$

For an integer $m$ and a natural number $n$, the
reduced residue system $R_m(n)$ modulo $n$ is the finite set
$R_m(n) = \{a \in \mathbb{Z} : m + 1 \le a \le m + n,\ \gcd(a, n) = 1\}$.

## Sources

- Phothila, Thoket and Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6, Section 1.

Formalized by `MetaMathlibExt.reducedResidueWindow`, a definition declared in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#reduced-residue-window).

## Longest progression with a given common difference

For an integer $m$ and natural numbers
$n$ and $d$, let $R_m(n)$ be the set of integers $a$ with $m + 1 \le a \le m + n$ and
$\gcd(a, n) = 1$. Then $f_m(d, n)$ is the supremum of the natural numbers $s$ for which some
integer $b$ has $b + i d \in R_m(n)$ for every natural number $i < s$. For $d > 0$ every such $s$
is at most $n$, so $f_m(d, n)$ is the length of the longest arithmetic progression with common
difference $d$ contained in $R_m(n)$; the paper uses it only for $d > 0$, and for $d = 0$ the
definition gives $0$.

## Sources

- Phothila, Thoket and Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6, Section 2.

Formalized by `MetaMathlibExt.longestAPLengthWithDiff`, a definition declared in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#longest-aplength-with-diff).

## Length of the longest arithmetic progression in a reduced residue system

For an
integer $m$ and a natural number $n$, let $R_m(n)$ be the reduced residue system of the
integers $a$ with $m + 1 \le a \le m + n$ and $\gcd(a, n) = 1$. Then $f_m(n)$ is the largest
natural number $s$ for which there are an integer $b$ and a positive integer $d$ such that
$b, b + d, \dots, b + (s - 1)d$ all lie in $R_m(n)$. So it is the length of the longest
arithmetic progression with positive common difference contained in $R_m(n)$, where a single
term counts as a progression of length $1$, and $f_m(n) = 0$ when $R_m(n)$ is empty.

## Sources

- Phothila, Thoket and Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6, Section 1.

Formalized by `MetaMathlibExt.longestAPLength`, a definition declared in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#longest-aplength).

## Longest progression in the absolute least reduced residues

For a natural number $n$,
let $R(n)$ be the set of integers $a$ with $1 - \lceil n/2 \rceil \le a \le n - \lceil n/2 \rceil$
and $\gcd(a, n) = 1$, the system of absolute least reduced residues modulo $n$. Then $g(n)$ is
the largest $s \ge 0$ for which there are an integer $b$ and a positive integer $d$ with
$b + i d \in R(n)$ for every $0 \le i < s$: the length of the longest arithmetic progression
with positive common difference contained in $R(n)$. Equivalently,
$g(n) = f_{-\lceil n/2 \rceil}(n)$, where $f_m(n)$ is the same length for the set
$R_m(n)$ of integers $a$ with $m + 1 \le a \le m + n$ and $\gcd(a, n) = 1$.

## Sources

- Phothila, Thoket and Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6, Section 1.

Formalized by `MetaMathlibExt.absLeastAPLength`, a definition declared in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#abs-least-aplength).

## Length bound for progressions in a reduced residue window

Let $m$ be an integer and $n$
a natural number, and let $R_m(n)$ be the set of integers $a$ with $m + 1 \le a \le m + n$ and
$\gcd(a, n) = 1$. If $b$ is an integer, $d$ a positive integer and $s$ a natural number such
that $b + i d \in R_m(n)$ for every $0 \le i < s$, then $s \le n$.

## Sources

- Phothila, Thoket and Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6 (`R_m(n) ⊆ [m + 1, m + n]`).

Formalized by `MetaMathlibExt.apLength_le`, a theorem declared in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#ap-length-le).

## The longest progression length is at most the modulus

For every integer $m$ and natural
number $n$, $f_m(n) \le n$, where $f_m(n)$ is the length of the longest arithmetic progression
with positive common difference contained in the set $R_m(n)$ of integers $a$ with
$m + 1 \le a \le m + n$ and $\gcd(a, n) = 1$.

## Sources

- Phothila, Thoket and Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6 (`R_m(n)` has at most `n` elements).

Formalized by `MetaMathlibExt.longestAPLength_le`, a theorem declared in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#longest-aplength-le).

## The reduced residue system $R_{-3}(5)$

The reduced residue system $R_{-3}(5)$ of the
integers $a$ with $-2 \le a \le 2$ and $\gcd(a, 5) = 1$ is $\{-2, -1, 1, 2\}$: an integer $a$
lies in $R_{-3}(5)$ if and only if $a$ is one of $-2$, $-1$, $1$, $2$.

Since $\lceil 5/2 \rceil = 3$, this is the system $R(5) = R_{-\lceil 5/2 \rceil}(5)$ of absolute
least reduced residues modulo $5$.

## Sources

- Phothila, Thoket and Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6, Example 1(i).

Formalized by `MetaMathlibExt.mem_reducedResidueWindow_neg_three_five`, a theorem declared in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#mem-reduced-residue-window-neg-three-fiv).

## Longest progressions of absolute least residues modulo 5

The length $g(5)$ of the
longest arithmetic progression in the absolute least reduced residue system modulo $5$ is $2$.

## Sources

- Phothila, Thoket and Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6, Example 1(i).

Formalized by `MetaMathlibExt.absLeastAPLength_five`, a theorem declared in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#abs-least-aplength-five).

## Prime bound for progressions with a fixed difference

Let $m$ be an integer, $n > 1$ and
$d > 0$ natural numbers, and $p$ a prime that divides $n$ but not $d$. Then $f_m(d, n) \le p - 1$,
where $f_m(d, n)$ is the length of the longest arithmetic progression with common difference $d$
contained in the set $R_m(n)$ of integers $a$ with $m + 1 \le a \le m + n$ and $\gcd(a, n) = 1$.

## Sources

- Chaninat Phothila, Natthakan Thoket and Narakorn Rompurk Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6, Lemma 1(i).

Stated but not proved: `MetaMathlibExt.longestAPLengthWithDiff_le_prime_sub_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#longest-aplength-with-diff-le-prime-sub).

## Squarefree bound for progressions with a fixed difference

Let $m$ be an integer, $n > 1$
a squarefree natural number with largest prime factor $\operatorname{gpf}(n)$, and $d > 0$ a
natural number. Then $f_m(d, n) \le \operatorname{gpf}(n) - 1$, where $f_m(d, n)$ is the length of
the longest arithmetic progression with common difference $d$ contained in the set $R_m(n)$ of
integers $a$ with $m + 1 \le a \le m + n$ and $\gcd(a, n) = 1$.

## Sources

- Chaninat Phothila, Natthakan Thoket and Narakorn Rompurk Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6, Lemma 1(ii).

Stated but not proved: `MetaMathlibExt.longestAPLengthWithDiff_le_gpf_sub_one_of_squarefree` is written with `theorem_wanted` in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#longest-aplength-with-diff-le-gpf-sub-on).

## Longest progressions of absolute least residues: primes congruent to 1 mod 4

For a
prime $p \equiv 1 \pmod 4$, the length $g(p)$ of the longest arithmetic progression in the
absolute least reduced residue system modulo $p$ is $(p - 1)/2$.

## Sources

- Chaninat Phothila, Natthakan Thoket and Narakorn Rompurk Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6, Theorem 1.

Stated but not proved: `MetaMathlibExt.absLeastAPLength_prime_of_mod_four_eq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#abs-least-aplength-prime-of-mod-four-eq).

## Longest progressions of absolute least residues: primes congruent to 3 mod 4

For a
prime $p \equiv 3 \pmod 4$, the length $g(p)$ of the longest arithmetic progression in the
absolute least reduced residue system modulo $p$ is $(p + 1)/2$.

## Sources

- Chaninat Phothila, Natthakan Thoket and Narakorn Rompurk Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6, Theorem 1.

Stated but not proved: `MetaMathlibExt.absLeastAPLength_prime_of_mod_four_eq_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#abs-least-aplength-prime-of-mod-four-eq-2).

## Longest progressions of absolute least residues: prime powers

Let $p$ be a prime and
$r \ge 1$, with $r \ge 2$ when $p$ is odd. Then the length $g(p^r)$ of the longest arithmetic
progression in the absolute least reduced residue system modulo $p^r$ is $p^{r-1}$.

## Sources

- Chaninat Phothila, Natthakan Thoket and Narakorn Rompurk Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6, Theorem 1.

Stated but not proved: `MetaMathlibExt.absLeastAPLength_prime_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#abs-least-aplength-prime-pow).

## Longest progressions of absolute least residues: odd squarefree composite moduli

Let
$n > 1$ be an odd squarefree natural number that is not prime, let $P$ be its largest prime
factor and $d = n / P$, and let $g(n)$ be the length of the longest arithmetic progression in the
absolute least reduced residue system modulo $n$. Then
$g(n) = \lfloor P - (P + 1)/(2d) \rfloor$.

## Sources

- Chaninat Phothila, Natthakan Thoket and Narakorn Rompurk Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6, Theorem 1.

Stated but not proved: `MetaMathlibExt.absLeastAPLength_odd_squarefree` is written with `theorem_wanted` in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#abs-least-aplength-odd-squarefree).

## Longest progressions of absolute least residues: twice an odd prime

For an odd prime
$p$, the length $g(2p)$ of the longest arithmetic progression in the absolute least reduced
residue system modulo $2p$ is $p - 1$.

## Sources

- Chaninat Phothila, Natthakan Thoket and Narakorn Rompurk Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6, Theorem 1.

Stated but not proved: `MetaMathlibExt.absLeastAPLength_two_mul_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#abs-least-aplength-two-mul-prime).

## Longest progressions of absolute least residues: neither squarefree nor prime power

Let
$n > 1$ be a natural number that is neither squarefree nor a prime power, let
$\operatorname{rad}(n)$ be the product of the distinct primes dividing $n$ and $P$ the largest
prime factor of $n$, and let $g(n)$ be the length of the longest arithmetic progression in the
absolute least reduced residue system modulo $n$. Then
$g(n) = \max(n / \operatorname{rad}(n), P - 1)$.

## Sources

- Chaninat Phothila, Natthakan Thoket and Narakorn Rompurk Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6, Theorem 1.

Stated but not proved: `MetaMathlibExt.absLeastAPLength_of_not_squarefree_of_not_isPrimePow` is written with `theorem_wanted` in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#abs-least-aplength-of-not-squarefree-of).

## Longest progressions of absolute least residues: even squarefree, three or more primes

Let $n$ be an even squarefree natural number with at least three prime factors, let $P$ be its
largest prime factor and $d = n / P$, and let $g(n)$ be the length of the longest arithmetic
progression in the absolute least reduced residue system modulo $n$. Then
$\lfloor P - 2P/d \rfloor \le g(n) \le P - 1$, and if $d \ge 2P$ then $g(n) = P - 1$.

## Sources

- Chaninat Phothila, Natthakan Thoket and Narakorn Rompurk Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6, Theorem 1.

Stated but not proved: `MetaMathlibExt.absLeastAPLength_even_squarefree_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#abs-least-aplength-even-squarefree-bound).

## Maximum longest progression length over all reduced residue windows

Let $n > 1$ be a
natural number, $\operatorname{rad}(n)$ the product of its distinct prime factors and
$\operatorname{gpf}(n)$ its largest prime factor. For an integer $m$ let $f_m(n)$ be the length of
the longest arithmetic progression with positive common difference contained in the set $R_m(n)$
of integers $a$ with $m + 1 \le a \le m + n$ and $\gcd(a, n) = 1$. Then the largest value of
$f_m(n)$ over all integers $m$ is $\max(n / \operatorname{rad}(n), \operatorname{gpf}(n) - 1)$.

## Sources

- Chaninat Phothila, Natthakan Thoket and Narakorn Rompurk Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6, Theorem 2.

Stated but not proved: `MetaMathlibExt.isGreatest_longestAPLength` is written with `theorem_wanted` in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#is-greatest-longest-aplength).

## Minimum longest progression length modulo a prime $p \equiv 1 \pmod 4$

Let $p$ be a prime
with $p \equiv 1 \pmod 4$. For an integer $m$ let $f_m(p)$ be the length of the longest arithmetic
progression with positive common difference contained in the set $R_m(p)$ of integers $a$ with
$m + 1 \le a \le m + p$ and $\gcd(a, p) = 1$. Then the least value of $f_m(p)$ over all integers
$m$ is $(p - 1) / 2$.

## Sources

- Chaninat Phothila, Natthakan Thoket and Narakorn Rompurk Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6, Theorem 3.

Stated but not proved: `MetaMathlibExt.isLeast_longestAPLength_prime_of_mod_four_eq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#is-least-longest-aplength-prime-of-mod-f).

## Minimum longest progression length modulo a prime $p \equiv 3 \pmod 4$

Let $p$ be a prime
with $p \equiv 3 \pmod 4$. For an integer $m$ let $f_m(p)$ be the length of the longest arithmetic
progression with positive common difference contained in the set $R_m(p)$ of integers $a$ with
$m + 1 \le a \le m + p$ and $\gcd(a, p) = 1$. Then the least value of $f_m(p)$ over all integers
$m$ is $(p + 1) / 2$.

## Sources

- Chaninat Phothila, Natthakan Thoket and Narakorn Rompurk Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6, Theorem 3.

Stated but not proved: `MetaMathlibExt.isLeast_longestAPLength_prime_of_mod_four_eq_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#is-least-longest-aplength-prime-of-mod-f-2).

## Minimum longest progression length modulo a prime power

Let $p$ be a prime and $r > 1$ a
natural number. For an integer $m$ let $f_m(p^r)$ be the length of the longest arithmetic
progression with positive common difference contained in the set $R_m(p^r)$ of integers $a$ with
$m + 1 \le a \le m + p^r$ and $\gcd(a, p^r) = 1$. Then the least value of $f_m(p^r)$ over all
integers $m$ is $p^{r-1}$.

## Sources

- Chaninat Phothila, Natthakan Thoket and Narakorn Rompurk Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6, Theorem 3.

Stated but not proved: `MetaMathlibExt.isLeast_longestAPLength_prime_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#is-least-longest-aplength-prime-pow).

## Minimum longest progression length when $n$ is neither squarefree nor a prime power

Let
$n > 1$ be a natural number that is neither squarefree nor a prime power, $\operatorname{rad}(n)$
the product of its distinct prime factors and $\operatorname{gpf}(n)$ its largest prime factor.
For an integer $m$ let $f_m(n)$ be the length of the longest arithmetic progression with positive
common difference contained in the set $R_m(n)$ of integers $a$ with $m + 1 \le a \le m + n$ and
$\gcd(a, n) = 1$. Then $f_m(n) \ge n / \operatorname{rad}(n)$ for every integer $m$, and
$f_m(n) \le \max(n / \operatorname{rad}(n), \operatorname{gpf}(n) - 1)$ for some integer $m$.
If moreover $\operatorname{gpf}(n) - 1 \le n / \operatorname{rad}(n)$, then the least value of
$f_m(n)$ over all integers $m$ is $n / \operatorname{rad}(n)$.

## Sources

- Chaninat Phothila, Natthakan Thoket and Narakorn Rompurk Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6, Theorem 3.

Stated but not proved: `MetaMathlibExt.longestAPLength_min_of_not_squarefree_of_not_isPrimePow` is written with `theorem_wanted` in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#longest-aplength-min-of-not-squarefree-o).

## Average longest progression length for non-squarefree moduli

Let $n > 1$ be a natural
number that is not squarefree, $\operatorname{rad}(n)$ the product of its distinct prime factors
and $\operatorname{gpf}(n)$ its largest prime factor, and suppose that
$\operatorname{gpf}(n) - 1 \le n / \operatorname{rad}(n)$. For an integer $m$ let $f_m(n)$ be the
length of the longest arithmetic progression with positive common difference contained in the
set $R_m(n)$ of integers $a$ with $m + 1 \le a \le m + n$ and $\gcd(a, n) = 1$. Then
$\frac{1}{n} \sum_{m=0}^{n-1} f_m(n) = \frac{n}{\operatorname{rad}(n)}$.

## Sources

- Chaninat Phothila, Natthakan Thoket and Narakorn Rompurk Kanasri, *Length of the Longest Arithmetic Progressions in a Certain Reduced Residue System*, INTEGERS 26 (2026), Article A6, Corollary 1.

Stated but not proved: `MetaMathlibExt.average_longestAPLength_of_not_squarefree` is written with `theorem_wanted` in [WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ReducedResidueLongestAPWanted.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html#average-longest-aplength-of-not-squarefr).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arithmetic progressions in reduced residue systems](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/arithmetic-progressions-in-reduced-residue-syste)
