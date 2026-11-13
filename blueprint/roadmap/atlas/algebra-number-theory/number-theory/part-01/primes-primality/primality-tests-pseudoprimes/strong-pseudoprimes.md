---
declaration: section
origin: cited
lean: MetaMathlibExt.IsStrongPseudoprime, MetaMathlibExt.isStrongPseudoprime_2047_two, MetaMathlibExt.isStrongPseudoprime_one, MetaMathlibExt.isStrongPseudoprime_iff, MetaMathlibExt.IsStrongPseudoprime.one_lt, MetaMathlibExt.IsStrongPseudoprime.not_prime, MetaMathlibExt.IsStrongPseudoprime.odd, MetaMathlibExt.card_fermatPsp_bases_eq_prod_gcd
statement: formalized
---

# Strong pseudoprimes

19 results, 7 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes/index.html).

## Strong pseudoprime

Let $n$ be a natural number and $b$ a residue class modulo $n$. Then
$n$ is a strong pseudoprime to the base $b$ if $n$ is an odd composite number (that is, $n > 1$,
$n$ is odd and $n$ is not prime) and there are natural numbers $k$ and $d$ with $d$ odd and
$n - 1 = 2^k d$ such that either $b^d = 1$ or $b^{2^i d} = -1$ for some $i < k$, where the
powers are computed in $\mathbb{Z}/n\mathbb{Z}$.

For odd composite $n$ the decomposition $n - 1 = 2^k d$ with $d$ odd is unique, so the
existential agrees with the usual definition for the fixed $k$ and $d$. An integer base is used
through its residue class modulo $n$.

## Sources

- Samuel S. Wagstaff, Jr., *Pseudoprimes and Fermat Numbers*, INTEGERS 24 (2024), Article A23, Section 1, Congruences (2) and (3).

Formalized by `MetaMathlibExt.IsStrongPseudoprime`, a definition declared in [MathlibExt/NumberTheory/StrongPseudoprime.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/StrongPseudoprime.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes/index.html#is-strong-pseudoprime).

## 2047 is a strong pseudoprime to base 2

The number $2047 = 23 \cdot 89$ is a strong
pseudoprime to the base $2$.

Indeed $2046 = 2 \cdot 1023$ with $1023$ odd, and $2^{1023} = (2^{11})^{93} = 1$ modulo $2047$.

## Sources

- Samuel S. Wagstaff, Jr., *Pseudoprimes and Fermat Numbers*, INTEGERS 24 (2024), Article A23, Section 1 (first strong pseudoprime to base 2 in the list given there).

Formalized by `MetaMathlibExt.isStrongPseudoprime_2047_two`, a theorem declared in [MathlibExt/NumberTheory/StrongPseudoprime.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/StrongPseudoprime.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes/index.html#is-strong-pseudoprime-2047-two).

## Every odd composite is a strong pseudoprime to base 1

Every odd composite number $n$
is a strong pseudoprime to the base $1$.

## Sources

- Samuel S. Wagstaff, Jr., *Pseudoprimes and Fermat Numbers*, INTEGERS 24 (2024), Article A23, proof of Theorem 6 ("every composite `n` is spsp(1)").

Formalized by `MetaMathlibExt.isStrongPseudoprime_one`, a theorem declared in [MathlibExt/NumberTheory/StrongPseudoprime.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/StrongPseudoprime.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes/index.html#is-strong-pseudoprime-one).

## Unfolded definition of strong pseudoprimes

Let $n$ be a natural number and $b$ a residue
class modulo $n$. Then $n$ is a strong pseudoprime to the base $b$ if and only if $n > 1$, $n$ is
not prime, $n$ is odd, and there are natural numbers $k$ and $d$ with $n - 1 = 2^k d$ and $d$ odd
such that $b^d = 1$ or $b^{2^i d} = -1$ in $\mathbb{Z}/n\mathbb{Z}$ for some $i < k$.

Formalized by `MetaMathlibExt.isStrongPseudoprime_iff`, a theorem declared in [MathlibExt/NumberTheory/StrongPseudoprime.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/StrongPseudoprime.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes/index.html#is-strong-pseudoprime-iff).

## Strong pseudoprimes exceed one

If $n$ is a strong pseudoprime to some base $b$ modulo
$n$, then $n > 1$.

Formalized by `MetaMathlibExt.IsStrongPseudoprime.one_lt`, a theorem declared in [MathlibExt/NumberTheory/StrongPseudoprime.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/StrongPseudoprime.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes/index.html#one-lt).

## Strong pseudoprimes are not prime

If $n$ is a strong pseudoprime to some base $b$
modulo $n$, then $n$ is not prime.

Formalized by `MetaMathlibExt.IsStrongPseudoprime.not_prime`, a theorem declared in [MathlibExt/NumberTheory/StrongPseudoprime.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/StrongPseudoprime.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes/index.html#not-prime).

## Strong pseudoprimes are odd

If $n$ is a strong pseudoprime to some base $b$ modulo $n$,
then $n$ is odd.

Formalized by `MetaMathlibExt.IsStrongPseudoprime.odd`, a theorem declared in [MathlibExt/NumberTheory/StrongPseudoprime.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/StrongPseudoprime.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes/index.html#odd).

## Number of Fermat pseudoprime bases (Monier; Baillie–Wagstaff)

Let $n > 1$ be a
composite natural number. Then the number of integers $b$ with $1 \le b < n$ such that $n$ is a
Fermat pseudoprime to the base $b$, that is, $b^{n-1} \equiv 1 \pmod{n}$, equals
$\prod_p \gcd(n - 1, p - 1)$, where $p$ runs over the distinct prime divisors of $n$.

## Sources

- Samuel S. Wagstaff, Jr., *Pseudoprimes and Fermat Numbers*, INTEGERS 24 (2024), Article A23, Theorem 2.

Stated but not proved: `MetaMathlibExt.card_fermatPsp_bases_eq_prod_gcd` is written with `theorem_wanted` in [WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes/index.html#card-fermat-psp-bases-eq-prod-gcd).

## Products of two distinct primes have a square number of Fermat pseudoprime bases

Let
$p$ and $q$ be distinct primes. Then the number of integers $b$ with $1 \le b < pq$ such that
$pq$ is a Fermat pseudoprime to the base $b$, that is, $b^{pq-1} \equiv 1 \pmod{pq}$, is a perfect
square.

## Sources

- Samuel S. Wagstaff, Jr., *Pseudoprimes and Fermat Numbers*, INTEGERS 24 (2024), Article A23, Corollary 1.

Stated but not proved: `MetaMathlibExt.isSquare_card_fermatPsp_bases_mul_of_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes/index.html#is-square-card-fermat-psp-bases-mul-of-p).

## Monier's formula for the number of strong pseudoprime bases

Let $n$ be an odd composite
natural number, let $r$ be the number of distinct prime divisors of $n$, and let $v$ be the least
of the $2$-adic valuations of $p - 1$ over the prime divisors $p$ of $n$. Write $d$ for the odd
part of $n - 1$ and $d_p$ for the odd part of $p - 1$. Then the number of integers $b$ with
$1 \le b < n$ such that $n$ is a strong pseudoprime to the base $b$ equals, as a rational number,

$$\left(1 + \frac{2^{vr} - 1}{2^r - 1}\right) \prod_p \gcd(d, d_p),$$

where the product runs over the distinct prime divisors $p$ of $n$.

## Sources

- Samuel S. Wagstaff, Jr., *Pseudoprimes and Fermat Numbers*, INTEGERS 24 (2024), Article A23, Theorem 3, Formula (5).

Stated but not proved: `MetaMathlibExt.card_strongPseudoprime_bases` is written with `theorem_wanted` in [WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes/index.html#card-strong-pseudoprime-bases).

## When the strong pseudoprime bases form a subgroup

Let $n > 1$ be an odd number that is
not prime, let $r$ be the number of distinct prime factors of $n$, and let $v$ be the least
exponent of $2$ in $p - 1$ over the prime factors $p$ of $n$. Then the following are equivalent:
(a) there is a subgroup of the unit group $(\mathbb{Z}/n\mathbb{Z})^\times$ whose elements are
exactly the units $u$ such that $n$ is a strong pseudoprime to the base $u$; (b) the number of
$b$ with $1 \le b < n$ such that $n$ is a strong pseudoprime to the base $b$ divides the number
of $b$ with $1 \le b < n$ such that $n$ is a Fermat pseudoprime to the base $b$, that is,
$n \mid b^{n-1} - 1$; (c) $v = 1$ or $r = 1$; (d) some prime $p \equiv 3 \pmod 4$ divides $n$,
or $n$ is a prime power.

## Sources

- Samuel S. Wagstaff, Jr., *Pseudoprimes and Fermat Numbers*, INTEGERS 24 (2024), Article A23, Theorem 4.

Stated but not proved: `MetaMathlibExt.strongPseudoprime_bases_subgroup_tfae` is written with `theorem_wanted` in [WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes/index.html#strong-pseudoprime-bases-subgroup-tfae).

## Strong pseudoprime bases almost always form a subgroup

The set of odd composite natural
numbers $n$ for which the units $b$ of $\mathbb{Z}/n\mathbb{Z}$ such that $n$ is a strong
pseudoprime to the base $b$ do not form a subgroup of the unit group has natural density $0$.

## Sources

- Samuel S. Wagstaff, Jr., *Pseudoprimes and Fermat Numbers*, INTEGERS 24 (2024), Article A23, Corollary 2.

Stated but not proved: `MetaMathlibExt.hasDensity_zero_strongPseudoprime_bases_not_subgroup` is written with `theorem_wanted` in [WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes/index.html#has-density-zero-strong-pseudoprime-base).

## The subgroup criteria for strong pseudoprime bases hold almost always

For an odd
composite natural number $n$, let $r$ be the number of distinct prime divisors of $n$, let $v$ be
the least of the $2$-adic valuations of $p - 1$ over the prime divisors $p$ of $n$, and consider
the conditions: (a) the units $b$ of $\mathbb{Z}/n\mathbb{Z}$ such that $n$ is a strong
pseudoprime to the base $b$ form a subgroup of the unit group; (b) the number of integers $b$
with $1 \le b < n$ to which $n$ is a strong pseudoprime divides the number of integers $b$ with
$1 \le b < n$ to which $n$ is a Fermat pseudoprime; (c) $v = 1$ or $r = 1$; (d) some prime
$p \equiv 3 \pmod 4$ divides $n$, or $n$ is a prime power. Then the set of odd composite natural
numbers $n$ for which at least one of (a)–(d) fails has natural density $0$.

## Sources

- Samuel S. Wagstaff, Jr., *Pseudoprimes and Fermat Numbers*, INTEGERS 24 (2024), Article A23, Corollary 3.

Stated but not proved: `MetaMathlibExt.hasDensity_zero_strongPseudoprime_bases_conditions_fail` is written with `theorem_wanted` in [WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes/index.html#has-density-zero-strong-pseudoprime-base-2).

## Composite divisors of primitive parts without their intrinsic factor are strong pseudoprimes

**Composite divisors of primitive parts without their intrinsic factor are strong
pseudoprimes.** Let $b > 1$ and $m > 2$ be natural numbers, and let $\Phi_j$ denote the $j$-th
cyclotomic polynomial. If a composite natural number $c > 1$ divides
$\Phi_m(b) / \gcd(\Phi_m(b), m)$ or $\Phi_{2m}(b) / \gcd(\Phi_{2m}(b), m)$, then $c$ is a strong
pseudoprime to the base $b$.

Here $\Phi_m(b)$ and $\Phi_{2m}(b)$ are the primitive parts of $b^m - 1$ and $b^m + 1$, and
dividing by the greatest common divisor with $m$ removes the intrinsic prime factor, if any.

## Sources

- Samuel S. Wagstaff, Jr., *Pseudoprimes and Fermat Numbers*, INTEGERS 24 (2024), Article A23, Theorem 5.

Stated but not proved: `MetaMathlibExt.isStrongPseudoprime_of_dvd_primitivePart` is written with `theorem_wanted` in [WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes/index.html#is-strong-pseudoprime-of-dvd-primitive-p).

## Composite divisors of primitive parts without the intrinsic factor are strong pseudoprimes to every power of the base

**Composite divisors of primitive parts without the intrinsic factor are strong pseudoprimes to
every power of the base.** Let $b > 1$ and $m > 2$ be natural numbers, write $\Phi_j(b)$ for the
value at $b$ of the $j$-th cyclotomic polynomial over $\mathbb{Z}$, and let $c > 1$ be a natural
number that is not prime. If $c$ divides $\Phi_m(b) / \gcd(\Phi_m(b), m)$ or
$\Phi_{2m}(b) / \gcd(\Phi_{2m}(b), m)$, then for every unit $u$ of $\mathbb{Z}/c\mathbb{Z}$ equal
to the residue class of $b$ and every integer $t$, $c$ is a strong pseudoprime to the base $u^t$.

These two quotients are the primitive parts of $b^m - 1$ and $b^m + 1$ with the intrinsic factor
removed.

## Sources

- Samuel S. Wagstaff, Jr., *Pseudoprimes and Fermat Numbers*, INTEGERS 24 (2024), Article A23, Corollary 4.

Stated but not proved: `MetaMathlibExt.isStrongPseudoprime_zpow_of_dvd_primitivePart` is written with `theorem_wanted` in [WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes/index.html#is-strong-pseudoprime-zpow-of-dvd-primit).

## Strong pseudoprime bases are closed under powers and negation

Let $n$ be a natural
number and $b$ a unit of $\mathbb{Z}/n\mathbb{Z}$ such that $n$ is a strong pseudoprime to the
base $b$. Then for every integer $t$, $n$ is a strong pseudoprime to the base $b^t$, and $n$ is a
strong pseudoprime to the base $-b$.

Requiring $b$ to be a unit loses nothing, since every strong pseudoprime base $b$ satisfies
$b^{n-1} = 1$; it also gives meaning to negative exponents.

## Sources

- Samuel S. Wagstaff, Jr., *Pseudoprimes and Fermat Numbers*, INTEGERS 24 (2024), Article A23, Theorem 6.

Stated but not proved: `MetaMathlibExt.isStrongPseudoprime_zpow_and_neg` is written with `theorem_wanted` in [WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes/index.html#is-strong-pseudoprime-zpow-and-neg).

## Composite Fermat numbers are strong pseudoprimes to every power of $2$

Let $k$ be a
natural number such that the Fermat number $F_k = 2^{2^k} + 1$ is composite. Then for every
integer $t$, $F_k$ is a strong pseudoprime to the base $2^t$, where the power is taken in the
unit group of $\mathbb{Z}/F_k\mathbb{Z}$ (in which $2$ is a unit because $F_k$ is odd).

## Sources

- Samuel S. Wagstaff, Jr., *Pseudoprimes and Fermat Numbers*, INTEGERS 24 (2024), Article A23, Corollary 5.

Stated but not proved: `MetaMathlibExt.fermatNumber_isStrongPseudoprime_two_zpow` is written with `theorem_wanted` in [WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes/index.html#fermat-number-is-strong-pseudoprime-two).

## Strong pseudoprime bases $2^{2^{k-1}+t} \pm 2^t$ of composite Fermat numbers

Let $k$ be a
natural number such that the Fermat number $F_k = 2^{2^k} + 1$ is composite. Then for every
natural number $t$, $F_k$ is a strong pseudoprime to both bases $2^{2^{k-1}+t} + 2^t$ and
$2^{2^{k-1}+t} - 2^t$, computed modulo $F_k$.

## Sources

- Samuel S. Wagstaff, Jr., *Pseudoprimes and Fermat Numbers*, INTEGERS 24 (2024), Article A23, Theorem 7.

Stated but not proved: `MetaMathlibExt.fermatNumber_isStrongPseudoprime_two_pow_add_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes/index.html#fermat-number-is-strong-pseudoprime-two-2).

## A subgroup of strong pseudoprime bases of a composite Fermat number

Let $k$ be a natural
number such that the Fermat number $F_k = 2^{2^k} + 1$ is composite, and let $S_k$ be the set of
residues modulo $F_k$ of the form $2^t$, $2^{2^{k-1}+t} + 2^t$ or $2^{2^{k-1}+t} - 2^t$ with $t$ a
natural number. Then the units of $\mathbb{Z}/F_k\mathbb{Z}$ that lie in $S_k$ form a subgroup of
the unit group of order $2^{k+2}$, and $F_k$ is a strong pseudoprime to every base in $S_k$.

The source also asserts that this subgroup is isomorphic to $C_{2^{k+1}} \times C_2$. This is
false: the residue $2^{16} + 1$ has multiplicative order $128 = 2^{k+2}$ modulo $F_5$, so the
subgroup is cyclic for $k = 5$.

## Sources

- Samuel S. Wagstaff, Jr., *Pseudoprimes and Fermat Numbers*, INTEGERS 24 (2024), Article A23, Theorem 8.

Stated but not proved: `MetaMathlibExt.fermatNumber_strongPseudoprime_bases_subgroup` is written with `theorem_wanted` in [WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PseudoprimeBasesFermatNumbersWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes/index.html#fermat-number-strong-pseudoprime-bases-s).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Strong pseudoprimes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/strong-pseudoprimes)
