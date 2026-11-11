---
declaration: section
origin: cited
lean: Nat.IsCarmichaelNumber, Nat.isCarmichaelNumber_iff_zmod, Nat.isCarmichaelNumber_iff_korselt, MetaMathlibExt.infinite_carmichael_prime_cardFactors_of_heathBrown, MetaMathlibExt.choose_le_choose_mul_card_prod_eq_one, MetaMathlibExt.exists_prime_modEq_le_rpow_five_point_two, MetaMathlibExt.exists_card_smooth_shifted_primes_ge, MetaMathlibExt.exists_carmichael_prime_cardFactors_between_of_heathBrown
statement: formalized
---

# Carmichael numbers

8 results, 3 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/carmichael-numbers/index.html).

## Carmichael numbers

A natural number $n$ is a Carmichael number if $n > 1$, $n$ is not
prime, and $a^n \equiv a \pmod{n}$ for every natural number $a$.

Formalized by `Nat.IsCarmichaelNumber`, a definition declared in [MathlibExt/NumberTheory/CarmichaelNumber.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/CarmichaelNumber.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/carmichael-numbers/index.html#is-carmichael-number).

## Carmichael numbers via the residue ring

A natural number $n$ is a Carmichael number if
and only if $n > 1$, $n$ is not prime, and $x^n = x$ for every element $x$ of
$\mathbb{Z}/n\mathbb{Z}$.

Formalized by `Nat.isCarmichaelNumber_iff_zmod`, a theorem declared in [MathlibExt/NumberTheory/CarmichaelNumber.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/CarmichaelNumber.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/carmichael-numbers/index.html#is-carmichael-number-iff-zmod).

## Korselt's criterion

A natural number $n > 1$ is a Carmichael number if and only if
$n$ is squarefree, $p - 1$ divides $n - 1$ for every prime divisor $p$ of $n$, and $n$ is not
prime.

Formalized by `Nat.isCarmichaelNumber_iff_korselt`, a theorem declared in [MathlibExt/NumberTheory/CarmichaelNumber.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/CarmichaelNumber.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/carmichael-numbers/index.html#is-carmichael-number-iff-korselt).

## Infinitely many Carmichael numbers with a prime number of prime factors (conditional)

Suppose there is a real constant $C$ such that for every natural number $d \ge 2$ and every
natural number $c$ coprime to $d$ there is a prime $p \equiv c \pmod{d}$ with
$p \le C d (\log d)^2$ (Heath-Brown's conjecture on the least prime in an arithmetic
progression). Then there are infinitely many Carmichael numbers $n$ whose number of prime
factors counted with multiplicity, $\Omega(n)$, is prime.

## Sources

- Thomas Wright, *Carmichael Numbers with a Prime Number of Prime Factors*, INTEGERS 24 (2024), Article A97, Theorem 1; the hypothesis is the paper's Conjecture 3.

Stated but not proved: `MetaMathlibExt.infinite_carmichael_prime_cardFactors_of_heathBrown` is written with `theorem_wanted` in [WantedExt/NumberTheory/CarmichaelPrimeOmegaWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CarmichaelPrimeOmegaWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/carmichael-numbers/index.html#infinite-carmichael-prime-card-factors-o).

## Alford–Granville–Pomerance count of zero-sum subsequences

Let $G$ be an abelian group
and let $n$ be the least natural number $m$ such that every sequence of $m$ elements of $G$ has a
nonempty subsequence with product $1$ (the Davenport constant of $G$). Let $r$ and $t$ be natural
numbers with $n < t < r$. Then for every sequence $s_1, \dots, s_r$ of elements of $G$, the number
$M$ of sets $S \subseteq \{1, \dots, r\}$ with $t - n \le |S| \le t$ and $\prod_{i \in S} s_i = 1$
satisfies $\binom{r}{t} \le \binom{r}{n} M$.

## Sources

- Thomas Wright, *Carmichael Numbers with a Prime Number of Prime Factors*, INTEGERS 24 (2024), Article A97, Proposition 1, quoting Alford, Granville, and Pomerance, Theorem 2.1.

Stated but not proved: `MetaMathlibExt.choose_le_choose_mul_card_prod_eq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/CarmichaelPrimeOmegaWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CarmichaelPrimeOmegaWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/carmichael-numbers/index.html#choose-le-choose-mul-card-prod-eq-one).

## Linnik's theorem with exponent 5.2 (Xylouris)

There is a real constant $C$ such that for
every natural number $d \ge 1$ and every natural number $c$ coprime to $d$, there is a prime
$p \equiv c \pmod{d}$ with $p \le C d^{5.2}$.

## Sources

- Thomas Wright, *Carmichael Numbers with a Prime Number of Prime Factors*, INTEGERS 24 (2024), Article A97, Theorem 4, quoting Xylouris.

Stated but not proved: `MetaMathlibExt.exists_prime_modEq_le_rpow_five_point_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/CarmichaelPrimeOmegaWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CarmichaelPrimeOmegaWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/carmichael-numbers/index.html#exists-prime-mod-eq-le-rpow-five-point-t).

## Many primes $q$ with $q - 1$ smooth

Let $1 < \theta < 2$. There are real constants
$\gamma > 0$ and $Y$ such that for every real $y > Y$, the number of primes $q$ with
$y^\theta / \log y \le q \le y^\theta$ such that every prime divisor of $q - 1$ is at most $y$
is at least $\gamma y^\theta / \log(y^\theta)$.

## Sources

- Thomas Wright, *Carmichael Numbers with a Prime Number of Prime Factors*, INTEGERS 24 (2024), Article A97, Lemma 1, quoting Lemma 5.1 of Matomäki and Lemma 2.1 of Wright.

Stated but not proved: `MetaMathlibExt.exists_card_smooth_shifted_primes_ge` is written with `theorem_wanted` in [WantedExt/NumberTheory/CarmichaelPrimeOmegaWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CarmichaelPrimeOmegaWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/carmichael-numbers/index.html#exists-card-smooth-shifted-primes-ge).

## Carmichael numbers with a prime number of prime factors in a range

Assume Heath-Brown's
conjecture in the following form: there is a real constant $C$ such that for every natural
number $d \ge 2$ and every natural number $c$ coprime to $d$ there is a prime $p \equiv c
\pmod{d}$ with $p \le C d (\log d)^2$. Let $1 < \theta < 2$, and let $\gamma > 0$ be such that
for all sufficiently large real $y$, the number of primes $q$ with
$y^\theta / \log y \le q \le y^\theta$ such that every prime divisor of $q - 1$ is at most $y$
is at least $\gamma y^\theta / \log(y^\theta)$. Then there is a real $Y$ such that for every real
$y > Y$ there is a Carmichael number $n$ with $e^{(\gamma/4) y^\theta \log y} \le n \le
e^{e^{19 \theta y}}$ whose number of prime factors counted with multiplicity, $\Omega(n)$, is
prime.

The paper's proof uses its Lemma 2, which assumes Heath-Brown's conjecture (the paper's
Conjecture 3); here that assumption is an explicit hypothesis, as in Theorem 1.

## Sources

- Thomas Wright, *Carmichael Numbers with a Prime Number of Prime Factors*, INTEGERS 24 (2024), Article A97, Theorem 3.

Stated but not proved: `MetaMathlibExt.exists_carmichael_prime_cardFactors_between_of_heathBrown` is written with `theorem_wanted` in [WantedExt/NumberTheory/CarmichaelPrimeOmegaWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CarmichaelPrimeOmegaWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/carmichael-numbers/index.html#exists-carmichael-prime-card-factors-bet).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Carmichael numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/carmichael-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/carmichael-numbers)
