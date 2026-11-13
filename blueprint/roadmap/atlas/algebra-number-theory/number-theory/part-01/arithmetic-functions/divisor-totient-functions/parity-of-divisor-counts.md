---
declaration: section
origin: cited
lean: Finset.exists_sum_eq_two_mul_of_involution, Finset.even_card_of_involution, Finset.sum_div_two_mod_two_eq_card_filter, Nat.div_mem_divisors, Nat.div_div_self_of_mem_divisors, Nat.div_ne_of_mem_divisors_of_not_isSquare, Nat.card_divisors_two_mul_of_odd, Nat.even_card_divisors_of_not_isSquare
statement: formalized
proof: formalized
---

# Parity of divisor counts

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/parity-of-divisor-counts/index.html).

## Involutions and parity

## Sums invariant under a fixed-point-free involution are even

Let $s$ be a finite subset
of a type $\alpha$, let $f : \alpha \to \alpha$ satisfy $f(a) \in s$, $f(f(a)) = a$ and
$f(a) \neq a$ for every $a \in s$, and let $g : \alpha \to \mathbb{Z}$ satisfy $g(f(a)) = g(a)$
for every $a \in s$. Then $\sum_{a \in s} g(a) = 2k$ for some integer $k$.

Formalized by `Finset.exists_sum_eq_two_mul_of_involution`, a theorem declared in [MathlibExt/NumberTheory/DivisorCountParity.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DivisorCountParity.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/parity-of-divisor-counts/index.html#exists-sum-eq-two-mul-of-involution).

## A fixed-point-free involution forces even cardinality

Let $s$ be a finite subset of a
type $\alpha$ and let $f : \alpha \to \alpha$ satisfy $f(a) \in s$, $f(f(a)) = a$ and
$f(a) \neq a$ for every $a \in s$. Then $s$ has an even number of elements.

Formalized by `Finset.even_card_of_involution`, a theorem declared in [MathlibExt/NumberTheory/DivisorCountParity.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DivisorCountParity.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/parity-of-divisor-counts/index.html#even-card-of-involution).

## Half a sum of even numbers modulo 2

Let $s$ be a finite set of natural numbers and
let $f : \mathbb{N} \to \mathbb{N}$ be a function such that $f(k)$ is even for every
$k \in s$. Then the natural number $\frac{1}{2} \sum_{k \in s} f(k)$ is congruent modulo $2$
to the number of elements $k \in s$ with $f(k) \equiv 2 \pmod 4$.

Formalized by `Finset.sum_div_two_mod_two_eq_card_filter`, a theorem declared in [MathlibExt/NumberTheory/DivisorCountParity.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DivisorCountParity.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/parity-of-divisor-counts/index.html#sum-div-two-mod-two-eq-card-filter).

## Complementary divisor

If $n$ is a nonzero natural number and $d$ is a divisor of $n$,
then $n/d$ is also a divisor of $n$.

Formalized by `Nat.div_mem_divisors`, a theorem declared in [MathlibExt/NumberTheory/DivisorCountParity.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DivisorCountParity.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/parity-of-divisor-counts/index.html#div-mem-divisors).

## The complementary divisor of the complementary divisor

If $n$ is a nonzero natural
number and $d$ is a divisor of $n$, then $n/(n/d) = d$.

Formalized by `Nat.div_div_self_of_mem_divisors`, a theorem declared in [MathlibExt/NumberTheory/DivisorCountParity.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DivisorCountParity.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/parity-of-divisor-counts/index.html#div-div-self-of-mem-divisors).

## Complementary divisors of a nonsquare are distinct

If $n$ is a natural number that is
not a perfect square and $d$ is a divisor of $n$, then $n/d \neq d$.

Formalized by `Nat.div_ne_of_mem_divisors_of_not_isSquare`, a theorem declared in [MathlibExt/NumberTheory/DivisorCountParity.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DivisorCountParity.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/parity-of-divisor-counts/index.html#div-ne-of-mem-divisors-of-not-is-square).

## Divisor count of twice an odd number

If $u$ is an odd natural number, then $2u$ has
exactly twice as many positive divisors as $u$.

Formalized by `Nat.card_divisors_two_mul_of_odd`, a theorem declared in [MathlibExt/NumberTheory/DivisorCountParity.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DivisorCountParity.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/parity-of-divisor-counts/index.html#card-divisors-two-mul-of-odd).

## A nonsquare has an even number of divisors

If a natural number $n$ is not a perfect
square, then $n$ has an even number of positive divisors.

Formalized by `Nat.even_card_divisors_of_not_isSquare`, a theorem declared in [MathlibExt/NumberTheory/DivisorCountParity.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DivisorCountParity.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/parity-of-divisor-counts/index.html#even-card-divisors-of-not-is-square).

## Squares are exactly the numbers with an odd number of divisors

A nonzero natural number
$u$ has an odd number of positive divisors if and only if $u$ is a perfect square.

Formalized by `Nat.odd_card_divisors_iff_isSquare`, a theorem declared in [MathlibExt/NumberTheory/DivisorCountParity.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DivisorCountParity.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/parity-of-divisor-counts/index.html#odd-card-divisors-iff-is-square).

## The quadratic character mod 4 is ±1 on odd numbers

Let $\chi_4$ be the nontrivial
character modulo $4$ with values in $\mathbb{Z}$: $\chi_4(n) = 1$ for $n \equiv 1 \pmod 4$,
$\chi_4(n) = -1$ for $n \equiv 3 \pmod 4$, and $\chi_4(n) = 0$ for even $n$. For every odd
natural number $d$, $\chi_4(d) = 1$ or $\chi_4(d) = -1$.

Formalized by `ZMod.χ₄_nat_eq_one_or_neg_one_of_odd`, a theorem declared in [MathlibExt/NumberTheory/DivisorCountParity.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DivisorCountParity.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/parity-of-divisor-counts/index.html#nat-eq-one-or-neg-one-of-odd).

## The second quadratic character mod 8 is ±1 on odd numbers

Let $\chi_8'$ be the
primitive quadratic character modulo $8$ with values in $\mathbb{Z}$ (the character of
$\mathbb{Q}(\sqrt{-2})$): $\chi_8'(n) = 1$ for $n \equiv 1, 3 \pmod 8$, $\chi_8'(n) = -1$ for
$n \equiv 5, 7 \pmod 8$, and $\chi_8'(n) = 0$ for even $n$. For every odd natural number $d$,
$\chi_8'(d) = 1$ or $\chi_8'(d) = -1$.

Formalized by `ZMod.χ₈'_nat_eq_one_or_neg_one_of_odd`, a theorem declared in [MathlibExt/NumberTheory/DivisorCountParity.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DivisorCountParity.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/parity-of-divisor-counts/index.html#nat-eq-one-or-neg-one-of-odd-2).

## Character divisor sums modulo 4

Let $N$ be a natural number and let $\chi$ be a
multiplicative character on $\mathbb{Z}/N\mathbb{Z}$ with values in $\mathbb{Z}$, applied to
natural numbers through their residues modulo $N$. Let $n$ be a natural number that is not a
perfect square such that $\chi(n) = 1$ and $\chi(d) \in \{1, -1\}$ for every positive divisor
$d$ of $n$, and let $\tau(n)$ be the number of positive divisors of $n$. Then
$\sum_{d \mid n} \chi(d) \equiv \tau(n) \pmod 4$.

Formalized by `MulChar.sum_divisors_emod_four_eq_card`, a theorem declared in [MathlibExt/NumberTheory/DivisorCountParity.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DivisorCountParity.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/parity-of-divisor-counts/index.html#sum-divisors-emod-four-eq-card).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Parity of divisor counts](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/parity-of-divisor-counts/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/parity-of-divisor-counts)
