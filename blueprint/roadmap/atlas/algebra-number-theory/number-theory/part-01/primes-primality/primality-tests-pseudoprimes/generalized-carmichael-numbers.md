---
declaration: section
origin: cited
lean: MetaMathlibExt.IsAACarmichael, MetaMathlibExt.isAACarmichael_of_prime, MetaMathlibExt.aaCarmichael_count_ge_of_least_prime_in_progression_bound, MetaMathlibExt.rpow_log_le_prime_of_eq_mul_add_one_of_dvd_prod_primes, MetaMathlibExt.carmichael_prod_primes_eq_mul_add_one_le_exp, MetaMathlibExt.int_gcd_sub_eq_of_eq_mul_mul_add
statement: formalized
---

# Generalized Carmichael numbers

6 results, 2 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/generalized-carmichael-numbers/index.html).

## $(a, a)$-Carmichael numbers

Let $a$ be an integer. A natural number $n$ is an
$(a, a)$-Carmichael number if $n$ is squarefree and $p - a$ divides $n - a$ in $\mathbb{Z}$ for
every prime $p$ dividing $n$.

## Sources

- Thomas Wright, *(a,a)-Carmichael Numbers and Greatest Common Divisors of p-a*, INTEGERS 26 (2026), Article A123, abstract and Section 1 (definition read from the arXiv version, arXiv:2607.02738; the journal display could not be checked).

Formalized by `MetaMathlibExt.IsAACarmichael`, a definition declared in [WantedExt/NumberTheory/AACarmichaelGcdWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AACarmichaelGcdWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/generalized-carmichael-numbers/index.html#is-aacarmichael).

## Primes are $(a, a)$-Carmichael numbers

For every integer $a$, every prime $p$ is an
$(a, a)$-Carmichael number.

## Sources

- Thomas Wright, *(a,a)-Carmichael Numbers and Greatest Common Divisors of p-a*, INTEGERS 26 (2026), Article A123, characteristic lemma of the definition in Section 1.

Formalized by `MetaMathlibExt.isAACarmichael_of_prime`, a theorem declared in [WantedExt/NumberTheory/AACarmichaelGcdWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AACarmichaelGcdWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/generalized-carmichael-numbers/index.html#is-aacarmichael-of-prime).

## Conditional lower bound for $(a, a)$-Carmichael numbers with prescribed gcd

Assume
Conjecture 2: there are a real number $A \ge 2$ and a natural number $l_0$ such that for every
natural number $l \ge l_0$ and every integer $b$ with $\gcd(b, l) = 1$ there is a prime $p$ with
$p \equiv b \pmod{l}$ and $p < l (\log l)^A$. Let $a$ be an integer and $\nu$ a positive integer
with $\gcd(a, \nu) = 1$ and $a + \nu$ odd. For real $X$ let $C_\nu(X, a)$ be the number of
$(a, a)$-Carmichael numbers $n \le X$ for which the nonnegative greatest common divisor of the
integers $p - a$, over the primes $p$ dividing $n$, equals $\nu$. Then for every $\varepsilon > 0$
and all sufficiently large real $X$,

$$C_\nu(X, a) \ge X^{1 - (2 + \varepsilon) \log\log\log\log X / \log\log\log X}.$$

This is the paper's bound $C_\nu(X, a) \ge X^{1 - (2 + o(1)) \log\log\log\log X / \log\log\log X}$,
with $2 + \varepsilon$ in place of $2 + o(1)$.

## Sources

- definitions of $C_\nu(X, a)$ and Conjecture 2 read from the arXiv version (arXiv:2607.02738); the theorem's journal wording matches it.
- Thomas Wright, *(a,a)-Carmichael Numbers and Greatest Common Divisors of p-a*, INTEGERS 26 (2026), Article A123, Theorem 1.

Stated but not proved: `MetaMathlibExt.aaCarmichael_count_ge_of_least_prime_in_progression_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/AACarmichaelGcdWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AACarmichaelGcdWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/generalized-carmichael-numbers/index.html#aa-carmichael-count-ge-of-least-prime-in).

## Size of the auxiliary primes in the construction

For a natural number $z$, let $J$ be the
product of the primes $r$ with $z/2 \le r \le z$, and write $\omega(g)$ for the number of distinct
prime factors of $g$. For every real $A$ and all sufficiently large natural numbers $z$ the
following holds: if $j$, $g$ and $q$ are natural numbers with $1 \le j \le (\log z)^{2A}$,
$g \mid J$, $\omega(g) = \lfloor \log z \rfloor$, $q$ prime and $q = gj + 1$, then

$$(z/6)^{\log z} \le q \le 2 z^{\log z} (\log z)^{2A}.$$

In the paper the bound is stated for the primes $q$ of a chosen set $\mathcal{Q}_i$ of such primes
with a fixed $j = j_0$, and $A \ge 2$ is the constant of Conjecture 2; the statement here covers
every such $j$ and $q$, and every real $A$.

## Sources

- Thomas Wright, *(a,a)-Carmichael Numbers and Greatest Common Divisors of p-a*, INTEGERS 26 (2026), Article A123, Section 3 (definitions of `J`, `𝓡_j`, `𝒬ᵢ`) and Lemma 1.

Stated but not proved: `MetaMathlibExt.rpow_log_le_prime_of_eq_mul_add_one_of_dvd_prod_primes` is written with `theorem_wanted` in [WantedExt/NumberTheory/AACarmichaelGcdWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AACarmichaelGcdWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/generalized-carmichael-numbers/index.html#rpow-log-le-prime-of-eq-mul-add-one-of-d).

## The Carmichael function of a product of auxiliary primes is small

For a natural number
$z$, let $J$ be the product of the primes $r$ with $z/2 \le r \le z$, and write $\omega(g)$ for the
number of distinct prime factors of $g$. For every real $A$ and all sufficiently large natural
numbers $z$ the following holds: for every natural number $j$ with $1 \le j \le (\log z)^{2A}$
and every finite set $S$ of primes such that each $q \in S$ equals $gj + 1$ for some natural
number $g$ with $g \mid J$ and $\omega(g) = \lfloor \log z \rfloor$, the Carmichael function
$\lambda$ satisfies $\lambda\bigl(\prod_{q \in S} q\bigr) \le e^{4z/5}$.

In the paper this is stated for $L_1 L_2$, the product of the primes in two disjoint chosen sets
of such primes for a fixed $j = j_0$; the statement here covers every finite set of such primes,
for every such $j$ and every real $A$.

## Sources

- Thomas Wright, *(a,a)-Carmichael Numbers and Greatest Common Divisors of p-a*, INTEGERS 26 (2026), Article A123, Section 3 and Lemma 3.

Stated but not proved: `MetaMathlibExt.carmichael_prod_primes_eq_mul_add_one_le_exp` is written with `theorem_wanted` in [WantedExt/NumberTheory/AACarmichaelGcdWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AACarmichaelGcdWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/generalized-carmichael-numbers/index.html#carmichael-prod-primes-eq-mul-add-one-le).

## Exact gcd of two shifted values in the construction

Let $a$ be an integer and let $\nu$,
$L_1$, $L_2$, $k_1$, $k_2$, $d_1$, $d_2$ be natural numbers with $\gcd(L_1, L_2) = 1$,
$\gcd(k_1, \nu L_1 L_2) = \gcd(k_2, \nu L_1 L_2) = 1$, $\gcd(k_1, k_2) = 1$, $d_1 \mid L_1$ and
$d_2 \mid L_2$. If $p_1 = d_1 k_1 \nu + a$ and $p_2 = d_2 k_2 \nu + a$, then
$\gcd(p_1 - a, p_2 - a) = \nu$.

In the paper $p_1, p_2$ are primes, $d_1, d_2$ have a prescribed number of prime factors,
$L_1, L_2$ are the products of two disjoint sets of primes, and $k_1, k_2$ come from Lemmas 4 and
5; the statement keeps only the hypotheses the conclusion uses.

## Sources

- Thomas Wright, *(a,a)-Carmichael Numbers and Greatest Common Divisors of p-a*, INTEGERS 26 (2026), Article A123, Section 5 (definition of `𝒫^i_k`) and Lemma 6.

Stated but not proved: `MetaMathlibExt.int_gcd_sub_eq_of_eq_mul_mul_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/AACarmichaelGcdWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/AACarmichaelGcdWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/generalized-carmichael-numbers/index.html#int-gcd-sub-eq-of-eq-mul-mul-add).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized Carmichael numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/generalized-carmichael-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/generalized-carmichael-numbers)
