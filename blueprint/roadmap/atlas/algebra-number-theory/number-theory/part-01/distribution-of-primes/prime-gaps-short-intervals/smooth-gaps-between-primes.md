---
declaration: section
origin: cited
lean: MetaMathlibExt.IsDifferenceSmooth, MetaMathlibExt.isDifferenceSmooth_singleton, MetaMathlibExt.infinite_prime_pairs_smooth_47_gap, MetaMathlibExt.maynard_tao_admissible_tuples, MetaMathlibExt.infinite_prime_tuples_smooth_gaps, MetaMathlibExt.infinite_prime_pairs_smooth_5_gap_of_elliottHalberstam, MetaMathlibExt.exists_admissible_differenceSmooth, MetaMathlibExt.not_isDifferenceSmooth_of_isAdmissibleFinset
statement: formalized
---

# Smooth gaps between primes

8 results, 2 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/smooth-gaps-between-primes/index.html).

## Difference-smooth sets of integers

Let $y$ be a natural number. A finite set $H$ of
integers is difference $y$-smooth if for all distinct $h, h' \in H$ every prime factor of
$h - h'$ is at most $y$.

## Sources

- Carol Wu, *On Smooth Gaps between Primes Using the Maynard-Tao Sieve*, INTEGERS 25 (2025), Article A44, Definition 3.

Formalized by `MetaMathlibExt.IsDifferenceSmooth`, a definition declared in [WantedExt/NumberTheory/SmoothPrimeGapsWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SmoothPrimeGapsWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/smooth-gaps-between-primes/index.html#is-difference-smooth).

## One-element sets are difference smooth

For every natural number $y$ and every integer
$a$, the set $\{a\}$ is difference $y$-smooth.

## Sources

- Carol Wu, *On Smooth Gaps between Primes Using the Maynard-Tao Sieve*, INTEGERS 25 (2025), Article A44, Definition 3.

Formalized by `MetaMathlibExt.isDifferenceSmooth_singleton`, a theorem declared in [WantedExt/NumberTheory/SmoothPrimeGapsWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SmoothPrimeGapsWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/smooth-gaps-between-primes/index.html#is-difference-smooth-singleton).

## Infinitely many prime pairs with $47$-smooth difference

There are infinitely many pairs
of primes $p > q$ such that every prime factor of $p - q$ is at most $47$.

## Sources

- Carol Wu, *On Smooth Gaps between Primes Using the Maynard-Tao Sieve*, INTEGERS 25 (2025), Article A44, Theorem 1.

Stated but not proved: `MetaMathlibExt.infinite_prime_pairs_smooth_47_gap` is written with `theorem_wanted` in [WantedExt/NumberTheory/SmoothPrimeGapsWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SmoothPrimeGapsWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/smooth-gaps-between-primes/index.html#infinite-prime-pairs-smooth-47-gap).

## Maynard–Tao theorem

For every natural number $m \ge 2$ there is a natural number $k$
such that for every admissible finite set $H$ of at least $k$ integers there are infinitely many
integers $n$ for which $n + h$ is a (positive) prime for at least $m$ elements $h \in H$.

## Sources

- Carol Wu, *On Smooth Gaps between Primes Using the Maynard-Tao Sieve*, INTEGERS 25 (2025), Article A44, Theorem 2, citing J. Maynard, *Small gaps between primes*, Ann. of Math. 181 (2015).

Stated but not proved: `MetaMathlibExt.maynard_tao_admissible_tuples` is written with `theorem_wanted` in [WantedExt/NumberTheory/SmoothPrimeGapsWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SmoothPrimeGapsWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/smooth-gaps-between-primes/index.html#maynard-tao-admissible-tuples).

## Prime $m$-tuples with smooth gaps

Let $m \ge 2$ and $k$ be natural numbers such that
every admissible finite set $H$ of at least $k$ integers has infinitely many integers $n$ for
which $n + h$ is a (positive) prime for at least $m$ elements $h \in H$. Then there are
infinitely many $m$-tuples of primes $p_1 < p_2 < \dots < p_m$ such that for all $j < i$ every
prime factor of $p_i - p_j$ is at most $k$.

Equivalently, every gap is $y$-smooth for $y$ the largest prime at most $k$; the paper applies
this with the admissible values $k_m$ of the Maynard–Tao theorem listed in its Table 1.

## Sources

- Carol Wu, *On Smooth Gaps between Primes Using the Maynard-Tao Sieve*, INTEGERS 25 (2025), Article A44, Theorem 3.

Stated but not proved: `MetaMathlibExt.infinite_prime_tuples_smooth_gaps` is written with `theorem_wanted` in [WantedExt/NumberTheory/SmoothPrimeGapsWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SmoothPrimeGapsWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/smooth-gaps-between-primes/index.html#infinite-prime-tuples-smooth-gaps).

## Prime pairs with $5$-smooth difference under Elliott–Halberstam

If the
Elliott–Halberstam conjecture holds, then there are infinitely many pairs of primes $p > q$ such
that every prime factor of $p - q$ is at most $5$.

## Sources

- Carol Wu, *On Smooth Gaps between Primes Using the Maynard-Tao Sieve*, INTEGERS 25 (2025), Article A44, Theorem 4.

Stated but not proved: `MetaMathlibExt.infinite_prime_pairs_smooth_5_gap_of_elliottHalberstam` is written with `theorem_wanted` in [WantedExt/NumberTheory/SmoothPrimeGapsWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SmoothPrimeGapsWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/smooth-gaps-between-primes/index.html#infinite-prime-pairs-smooth-5-gap-of-ell).

## Admissible difference-smooth sets of every size

For every natural number $k$ there is
an admissible set $H$ of exactly $k$ integers that is difference $k$-smooth: for all distinct
$h, h' \in H$, every prime factor of $h - h'$ is at most $k$.

## Sources

- Carol Wu, *On Smooth Gaps between Primes Using the Maynard-Tao Sieve*, INTEGERS 25 (2025), Article A44, Theorem 5.

Stated but not proved: `MetaMathlibExt.exists_admissible_differenceSmooth` is written with `theorem_wanted` in [WantedExt/NumberTheory/SmoothPrimeGapsWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SmoothPrimeGapsWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/smooth-gaps-between-primes/index.html#exists-admissible-difference-smooth).

## Admissible sets are not difference smooth at small bounds

Let $H$ be an admissible
finite set of $k \ge 2$ integers, let $z \le k$ be a prime and let $\ell < z$ be a natural
number. Then $H$ is not difference $\ell$-smooth. Equivalently, $H$ is not difference
$\ell$-smooth for any $\ell$ less than the largest prime at most $k$.

## Sources

- Carol Wu, *On Smooth Gaps between Primes Using the Maynard-Tao Sieve*, INTEGERS 25 (2025), Article A44, Proposition 1.

Stated but not proved: `MetaMathlibExt.not_isDifferenceSmooth_of_isAdmissibleFinset` is written with `theorem_wanted` in [WantedExt/NumberTheory/SmoothPrimeGapsWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SmoothPrimeGapsWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/smooth-gaps-between-primes/index.html#not-is-difference-smooth-of-is-admissibl).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Smooth gaps between primes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/smooth-gaps-between-primes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/smooth-gaps-between-primes)
