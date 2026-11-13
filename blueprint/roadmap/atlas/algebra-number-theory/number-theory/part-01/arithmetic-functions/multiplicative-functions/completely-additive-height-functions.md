---
declaration: section
origin: cited
lean: MetaMathlibExt.IsCompletelyAdditiveNat, MetaMathlibExt.IsCompletelyAdditiveNat.map_one, MetaMathlibExt.IsHeightFunction, MetaMathlibExt.nthPrimeOne, MetaMathlibExt.nthPrimeOne_one_two_three, MetaMathlibExt.additiveOfPrimeValues, MetaMathlibExt.additiveOfPrimeValues_one, MetaMathlibExt.additiveOfPrimeValues_prime
statement: formalized
---

# Completely additive height functions

43 results, 21 proved and 22 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html).

## Completely additive functions on the positive integers

A function
$H : \mathbb{N} \to \mathbb{N}$ is completely additive on the positive integers if
$H(ab) = H(a) + H(b)$ for all integers $a, b \ge 1$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Section 2 (definition of a height function).

Formalized by `MetaMathlibExt.IsCompletelyAdditiveNat`, a definition declared in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#is-completely-additive-nat).

## A completely additive function vanishes at one

If $H : \mathbb{N} \to \mathbb{N}$ is
completely additive on the positive integers, that is, $H(ab) = H(a) + H(b)$ for all $a, b \ge 1$,
then $H(1) = 0$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Section 2 (definition of a height function).

Formalized by `MetaMathlibExt.IsCompletelyAdditiveNat.map_one`, a theorem declared in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#map-one).

## Height functions

A function $H : \mathbb{N} \to \mathbb{N}$ is a height function if it is
completely additive on the positive integers, that is $H(ab) = H(a) + H(b)$ for all integers
$a, b \ge 1$; if $H(p) \ge 1$ for every prime $p$; and if for every $n \ge 1$ only finitely many
primes $p$ have $H(p) = n$.

Complete additivity forces $H(1) = 0$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Section 2 (definition of a height function).

Formalized by `MetaMathlibExt.IsHeightFunction`, a structure declared in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#is-height-function).

## The $i$-th prime

For a natural number $i \ge 1$, $p_i$ denotes the $i$-th prime in
increasing order, so that $p_1 = 2$. For $i = 0$ the definition also gives $p_0 = 2$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Section 2 (notation `pᵢ`).

Formalized by `MetaMathlibExt.nthPrimeOne`, a definition declared in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#nth-prime-one).

## The first three primes

With primes indexed from one, the first three primes are
$p_1 = 2$, $p_2 = 3$ and $p_3 = 5$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Section 2 (notation `pᵢ`).

Formalized by `MetaMathlibExt.nthPrimeOne_one_two_three`, a theorem declared in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#nth-prime-one-one-two-three).

## Completely additive function with prescribed prime values

Given a function
$v : \mathbb{N} \to \mathbb{N}$, this is the function $\mathbb{N} \to \mathbb{N}$ that sends each
$m \ge 1$ with prime factorization $m = \prod_p p^{a_p}$ to $\sum_p a_p\, v(p)$, and sends $0$
to $0$. Only the values of $v$ at primes matter.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Proposition 3 (extension by complete additivity).

Formalized by `MetaMathlibExt.additiveOfPrimeValues`, a definition declared in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#additive-of-prime-values).

## The completely additive extension vanishes at one

For every function
$v : \mathbb{N} \to \mathbb{N}$, the completely additive function with prime values $v$ (which
sends $m = \prod_p p^{a_p}$ to $\sum_p a_p\, v(p)$) takes the value $0$ at $1$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Proposition 3 (extension by complete additivity).

Formalized by `MetaMathlibExt.additiveOfPrimeValues_one`, a theorem declared in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#additive-of-prime-values-one).

## The completely additive extension at a prime

For every function
$v : \mathbb{N} \to \mathbb{N}$ and every prime $p$, the completely additive function with prime
values $v$ (which sends $m = \prod_q q^{a_q}$ to $\sum_q a_q\, v(q)$) takes the value $v(p)$
at $p$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Proposition 3 (extension by complete additivity).

Formalized by `MetaMathlibExt.additiveOfPrimeValues_prime`, a theorem declared in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#additive-of-prime-values-prime).

## The extension from prime values is completely additive

For every function
$v : \mathbb{N} \to \mathbb{N}$, let $H_v$ be the function with $H_v(m) = \sum_p a_p v(p)$ for
$m = \prod_p p^{a_p}$. Then $H_v$ is completely additive on the positive integers:
$H_v(ab) = H_v(a) + H_v(b)$ for all integers $a, b \ge 1$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Proposition 3 (extension by complete additivity).

Formalized by `MetaMathlibExt.isCompletelyAdditiveNat_additiveOfPrimeValues`, a theorem declared in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#is-completely-additive-nat-additive-of-p).

## Level construction for a height function

Let $H$ be a height function and let $n \ge 1$,
and for $k \ge 0$ write $\mathcal{H}_k = \{m \ge 1 : H(m) = k\}$. Then $\mathcal{H}_n$ is the union
of two sets: the set of products $p m'$, where $p$ is a prime with $H(p) = \ell$ for some integer
$\ell$ with $1 \le \ell \le \lfloor n/2 \rfloor$ and $m' \in \mathcal{H}_{n - \ell}$; and the set
of primes $p$ with $H(p) = n$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Theorem 1.

Stated but not proved: `MetaMathlibExt.heightLevel_eq_products_union_primes` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#height-level-eq-products-union-primes).

## Height levels are counted by coloured partitions

Let $H$ be a height function and, for
$\ell \ge 1$, let $\pi_\ell$ be the number of primes $p$ with $H(p) = \ell$. For every $n \ge 0$,
the number of positive integers $m$ with $H(m) = n$ equals the number of families
$(\alpha_{\ell,j})$ of nonnegative integers indexed by $1 \le \ell \le n$ and $0 \le j < \pi_\ell$
with $\sum_{\ell,j} \ell\, \alpha_{\ell,j} = n$, that is, the number of partitions of $n$ in which
a part of size $\ell$ comes in $\pi_\ell$ colours.

This is the level-by-level form of the statement that $H$ induces a height-preserving bijection
between the positive integers and such coloured partitions.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Proposition 1.

Stated but not proved: `MetaMathlibExt.heightLevel_card_eq_multipartitions` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#height-level-card-eq-multipartitions).

## Realizing a prescribed profile

Let $(\pi_k)_{k \ge 1}$ be nonnegative integers with
$\pi_k \ne 0$ for infinitely many $k$ (equivalently, $\sum_k \pi_k = \infty$). Then there is a
height function $H$ such that for every $k \ge 1$ exactly $\pi_k$ primes $p$ satisfy $H(p) = k$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Proposition 2.

Stated but not proved: `MetaMathlibExt.exists_heightFunction_with_profile` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#exists-height-function-with-profile).

## Height functions with prescribed values at the primes

Let $f : \mathbb{N} \to \mathbb{N}$
satisfy $f(i) \ge 1$ for every $i \ge 1$, and suppose that for every $t \ge 1$ only finitely many
$i \ge 1$ have $f(i) = t$. Let $H$ be the completely additive function on the positive integers
with $H(p) = f(i)$ when $p$ is the $i$-th prime (so $H(2) = f(1)$). Then $H$ is a height function,
and for every $n \ge 1$ the number of primes $p$ with $H(p) = n$ equals the number of integers
$i \ge 1$ with $f(i) = n$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Proposition 3.

Stated but not proved: `MetaMathlibExt.isHeightFunction_of_finite_fibers` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#is-height-function-of-finite-fibers).

## The largest integer at each height for the prime-index height

Let $H$ be the completely
additive function on the positive integers with $H(p) = i$ when $p$ is the $i$-th prime, so that
$H(2) = 1$, $H(3) = 2$ and $H(5) = 3$. For every natural number $n$, $2^n$ is the largest integer
$m \ge 1$ with $H(m) = n$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Proposition 4.

Stated but not proved: `MetaMathlibExt.isGreatest_primeIndexHeight_level` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#is-greatest-prime-index-height-level).

## Gutman–Ivić maximal Matula numbers

Write $p_i$ for the $i$-th prime, indexed from one
($p_1 = 2$). For a natural number $n$, $P(n)$ is the result of applying $i \mapsto p_i$ to $8$
exactly $n - 3$ times, so $P(4) = p_8$ and $P(n) = p_{P(n-1)}$ for $n \ge 5$. For $n \le 3$ there
are no applications and $P(n) = 8$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Section 3.2 (definition of `P(n)`).

Formalized by `MetaMathlibExt.matulaMax`, a definition declared in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#matula-max).

## The first maximal Matula number

The Gutman–Ivić maximal Matula number $P(4)$ equals
$p_8$, the eighth prime.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Section 3.2 (definition of `P(n)`).

Formalized by `MetaMathlibExt.matulaMax_four`, a theorem declared in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#matula-max-four).

## Recursion for the maximal Matula numbers

Write $p_i$ for the $i$-th prime, indexed from
one ($p_1 = 2$). For every $n \ge 4$ the Gutman–Ivić maximal Matula numbers satisfy
$P(n + 1) = p_{P(n)}$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Section 3.2 (definition of `P(n)`).

Formalized by `MetaMathlibExt.matulaMax_succ`, a theorem declared in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#matula-max-succ).

## Largest number at a given Matula height

Write $p_i$ for the $i$-th prime, indexed from
one ($p_1 = 2$), and let $H$ be a function from the natural numbers to themselves that is
completely additive on the positive integers and satisfies $H(p_i) = H(i) + 1$ for every $i \ge 1$
(Matula's height function). Then for every $n \ge 4$ the largest positive integer $m$ with
$H(m) = n$ is the Gutman–Ivić maximal Matula number $P(n)$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Proposition 5.

Stated but not proved: `MetaMathlibExt.matula_isGreatest_level` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#matula-is-greatest-level).

## Smallest number at a given Matula height

Write $p_i$ for the $i$-th prime, indexed from
one ($p_1 = 2$), and let $H$ be a function from the natural numbers to themselves that is
completely additive on the positive integers and satisfies $H(p_i) = H(i) + 1$ for every $i \ge 1$
(Matula's height function). Then for every $n > 1$ the smallest positive integer $m$ with
$H(m) = n$ is $3 \cdot 5^{(n-2)/3}$ if $n \equiv 2 \pmod 3$, $5^{n/3}$ if $n \equiv 0 \pmod 3$, and
$9 \cdot 5^{(n-4)/3}$ if $n \equiv 1 \pmod 3$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Proposition 6.

Stated but not proved: `MetaMathlibExt.matula_isLeast_level` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#matula-is-least-level).

## Rosser–Schoenfeld bounds for the $k$-th prime

Write $p_k$ for the $k$-th prime, indexed
from one ($p_1 = 2$). There is a natural number $k_0$ such that every $k \ge k_0$ satisfies
$k (\log k + \log \log k - 1) \le p_k \le k (\log k + \log \log k)$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Lemma 1, quoting Rosser and Schoenfeld.

Stated but not proved: `MetaMathlibExt.nthPrimeOne_rosser_schoenfeld` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#nth-prime-one-rosser-schoenfeld).

## The $k$-th prime exceeds $2k$ for $k \ge 6$

For every natural number $k \ge 6$, the
$k$-th prime $p_k$, indexed from one so that $p_1 = 2$, satisfies $p_k > 2k$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Lemma 2.

Stated but not proved: `MetaMathlibExt.two_mul_lt_nthPrimeOne` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#two-mul-lt-nth-prime-one).

## Prime-power decomposition of summatory heights

Let $H : \mathbb{N} \to \mathbb{N}$ be
completely additive on the positive integers, and let $x \ge 2$ be a natural number. Then

$$\sum_{m=1}^{x} H(m) = \sum_{p \le x} \sum_{\alpha \ge 1,\ p^\alpha \le x} H(p)
\left\lfloor \frac{x}{p^\alpha} \right\rfloor,$$

where $p$ runs over the primes $p \le x$.

The paper states this for real $x \ge 2$; both sides depend on $x$ only through $\lfloor x \rfloor$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Proposition 7, Equation (6).

Stated but not proved: `MetaMathlibExt.sum_height_eq_sum_prime_powers` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#sum-height-eq-sum-prime-powers).

## Prime reduction for summatory heights

Let $H : \mathbb{N} \to \mathbb{N}$ be completely
additive on the positive integers, and for real $x$ let $F(x) = \sum_{1 \le m \le x} H(m)$. Then
there is a real constant $C$ such that for every real $x \ge 2$,

$$\Bigl| F(x) - x \sum_{p \le x} \frac{H(p)}{p - 1} \Bigr| \le C \log x \sum_{p \le x} H(p),$$

where both sums run over the primes $p \le x$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Proposition 7, "In particular" display.

Stated but not proved: `MetaMathlibExt.sum_height_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#sum-height-asymptotic).

## Iteratively defined height functions

Write $p_i$ for the $i$-th prime, so $p_1 = 2$. Let
$f : \mathbb{N} \to \mathbb{N}$ satisfy $f(1) = 1$; suppose that for all integers $i, r \ge 1$, if
$p_r$ divides $f(i)$ then $r < i$ (this forces $f(i) \ge 1$ for $i \ge 1$); and suppose that for
every $t \ge 1$ only finitely many $i \ge 1$ have $f(i) = t$. Let $j \ge 1$. Then there is a
function $H : \mathbb{N} \to \mathbb{N}$ that is completely additive on the positive integers and
satisfies $H(p_i) = H(f(i)) + j$ for every $i \ge 1$, and every such $H$ is a height function.

The case $i = 1$ gives $H(2) = j$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Theorem 2.

Stated but not proved: `MetaMathlibExt.isHeightFunction_of_iterative` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#is-height-function-of-iterative).

## Weighted partition coefficients

Given real weights $(b_k)_{k \ge 0}$, the coefficients
$a_n$ of the weighted partition product $\prod_{k \ge 1} (1 - q^k)^{-b_k}$ are defined by $a_0 = 1$
and, for $n \ge 1$, the logarithmic-derivative recurrence
$n a_n = \sum_{m=1}^{n} \big(\sum_{k \mid m} k b_k\big) a_{n-m}$ (valid for real exponents $b_k$).
The value $b_0$ is unused.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Section 6.1 (weighted partitions `F(q) = ∑ aₙ qⁿ`).

Formalized by `MetaMathlibExt.weightedPartitionCoeff`, a definition declared in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#weighted-partition-coeff).

## Zeroth weighted partition coefficient

For every sequence of real weights $(b_k)$, the
weighted partition coefficient $a_0$ attached to $(b_k)$ equals $1$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Section 6.1 (weighted partitions `F(q) = ∑ aₙ qⁿ`).

Formalized by `MetaMathlibExt.weightedPartitionCoeff_zero`, a theorem declared in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#weighted-partition-coeff-zero).

## First weighted partition coefficient

For every sequence of real weights $(b_k)$, the
weighted partition coefficient $a_1$ attached to $(b_k)$ equals $b_1$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Section 6.1 (weighted partitions `F(q) = ∑ aₙ qⁿ`).

Formalized by `MetaMathlibExt.weightedPartitionCoeff_one`, a theorem declared in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#weighted-partition-coeff-one).

## Meinardus' hypotheses

Let $b_1, b_2, \dots$ be real weights (the value $b_0$ is unused),
let $\alpha$ and $A$ be reals and let $G : \mathbb{C} \to \mathbb{C}$. The weights satisfy
Meinardus' hypotheses (M1)–(M3) with exponent $\alpha$, residue $A$ and continuation $G$ if there
is $C_0$ with $0 < C_0 < 1$ such that: (M1) for $\operatorname{Re} s > \alpha$ the Dirichlet series
$B(s) = \sum_{k \ge 1} b_k k^{-s}$ converges absolutely and equals $G(s)$, and there is a function
$R : \mathbb{C} \to \mathbb{C}$ that is complex differentiable at every point of the closed
half-plane $\{s : \operatorname{Re} s \ge -C_0\}$ relative to that half-plane, with
$G(s) = A/(s - \alpha) + R(s)$ for all $s \ne \alpha$ with $\operatorname{Re} s \ge -C_0$; (M2)
there are $c > 0$ and reals $K$, $T$ with $|G(s)| \le K (1 + |\operatorname{Im} s|)^c$ whenever
$\operatorname{Re} s \ge -C_0$ and $|\operatorname{Im} s| \ge T$; (M3) there are
$\varepsilon > 0$, $C_3 > 0$ and $y_0 > 0$ such that, with
$g(\tau) = \sum_{k \ge 1} b_k e^{-k\tau}$, the inequality
$\operatorname{Re} g(y + 2\pi i x) - g(y) \le -C_3 y^{-\varepsilon}$ holds for all reals
$x$, $y$ with $0 < y < y_0$ and $y^{1 + \varepsilon/2} \le |x| \le 1/2$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Section 6.1 (hypotheses of Theorem 3).

Formalized by `MetaMathlibExt.MeinardusHypotheses`, a definition declared in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#meinardus-hypotheses).

## Meinardus' theorem

Let $b_0, b_1, b_2, \dots$ be nonnegative reals with $b_k \ne 0$ for
some $k \ge 1$, and let $a_n$ be the coefficients of the weighted partition product
$\prod_{k \ge 1} (1 - q^k)^{-b_k}$. Suppose that the weights satisfy Meinardus' hypotheses
(M1)–(M3) with exponent $\alpha > 0$, residue $A > 0$ and continuation $G$, and put
$\kappa = (\operatorname{Re} G(0) - 1 - \alpha/2)/(\alpha + 1)$ and
$C_2 = (1 + 1/\alpha)\,(A\,\Gamma(\alpha + 1)\,\zeta(\alpha + 1))^{1/(\alpha + 1)}$. Then there is
$C_1 > 0$ with $a_n \sim C_1 n^{\kappa} \exp(C_2 n^{\alpha/(\alpha + 1)})$ as $n \to \infty$, and
$\log a_n \sim C_2 n^{\alpha/(\alpha + 1)}$ as $n \to \infty$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Theorem 3, quoting Meinardus.

Stated but not proved: `MetaMathlibExt.meinardus_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#meinardus-asymptotic).

## A simple pole of a Dirichlet series from the growth of its partial sums

Let
$(\pi_k)_{k \ge 0}$ be nonnegative real numbers and let $C$, $\alpha$, $\eta$ be positive reals.
Suppose there is a constant $K$ with
$\bigl|\sum_{k=1}^{\lfloor x \rfloor} \pi_k - (C/\alpha) x^{\alpha}\bigr| \le K x^{\alpha - \eta}$
for every real $x \ge 1$. Then the Dirichlet series $B(s) = \sum_{k \ge 1} \pi_k k^{-s}$ converges
absolutely for $\operatorname{Re} s > \alpha$, and there is a function $R$, holomorphic on the
half-plane $\operatorname{Re} s > \alpha - \eta$, with $B(s) = C/(s - \alpha) + R(s)$ for
$\operatorname{Re} s > \alpha$. Moreover, for every $\delta$ with $0 < \delta < \eta$ there is a
constant $K'$ with $|C/(s - \alpha) + R(s)| \le K'(1 + |\operatorname{Im} s|)$ for all complex $s$
with $\operatorname{Re} s \ge \alpha - \eta + \delta$ and $|\operatorname{Im} s| \ge 1$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Lemma 3.

Stated but not proved: `MetaMathlibExt.lseries_profile_simple_pole` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#lseries-profile-simple-pole).

## Meinardus asymptotics for the levels of a height function

Let $H$ be a height function,
for $k \ge 0$ let $\pi_k$ be the number of primes $p$ with $H(p) = k$, and for $n \ge 0$ let $N_n$
be the number of integers $m \ge 1$ with $H(m) = n$. Let $\alpha > 0$ and $C > 0$ be real numbers
and suppose that the weights $(\pi_k)$ satisfy Meinardus' hypotheses with exponent $\alpha$,
residue $C$ and some continuation $G$. Put
$C_2 = (1 + 1/\alpha)\bigl(C\,\Gamma(\alpha + 1)\,\zeta(\alpha + 1)\bigr)^{1/(\alpha+1)}$. Then
there are real numbers $C_1 > 0$ and $\kappa$ with
$N_n \sim C_1 n^{\kappa} \exp\bigl(C_2 n^{\alpha/(\alpha+1)}\bigr)$ as $n \to \infty$, and
$\log N_n \sim C_2 n^{\alpha/(\alpha+1)}$ as $n \to \infty$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Theorem 4.

Stated but not proved: `MetaMathlibExt.heightLevel_card_meinardus` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#height-level-card-meinardus).

## Identifying the profile from the growth of the levels

Let $H$ be a height function, for
$k \ge 0$ let $\pi_k$ be the number of primes $p$ with $H(p) = k$, and for $n \ge 0$ let $N_n$ be
the number of integers $m \ge 1$ with $H(m) = n$. Let $r > 0$ and $A > 0$ be real numbers and
suppose that the weights $(\pi_k)$ satisfy Meinardus' hypotheses with exponent $r$, residue $A$
and some continuation $G$. Suppose further that $N_n \sim C_1 n^{\kappa} \exp(C_2 n^{\beta})$ as
$n \to \infty$ for real numbers $C_1 > 0$, $C_2 > 0$, $\kappa$ and $\beta$ with $0 < \beta < 1$.
Then $\beta = r/(r + 1)$, $r = \beta/(1 - \beta)$,
$C_2 = (1 + 1/r)\bigl(A\,\Gamma(r + 1)\,\zeta(r + 1)\bigr)^{1/(r+1)}$, and
$\sum_{k=1}^{\lfloor x \rfloor} \pi_k \sim (A/r)\, x^r$ as the real number $x$ tends to $\infty$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Corollary 1.

Stated but not proved: `MetaMathlibExt.heightProfile_identification` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#height-profile-identification).

## Cumulative profile

For a sequence $\pi : \mathbb{N} \to \mathbb{N}$ and a natural number
$k$, the cumulative profile is $\Pi_k = \sum_{j=1}^{k} \pi_j$. The value $\pi_0$ is not used, and
$\Pi_0 = 0$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Section 7.2 (canonical sequential realization).

Formalized by `MetaMathlibExt.profilePartialSum`, a definition declared in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#profile-partial-sum).

## Recursion for the cumulative profile

For every sequence $\pi : \mathbb{N} \to \mathbb{N}$
with cumulative profile $\Pi_k = \sum_{j=1}^{k} \pi_j$ and every natural number $k$,
$\Pi_{k+1} = \Pi_k + \pi_{k+1}$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Section 7.2 (canonical sequential realization).

Formalized by `MetaMathlibExt.profilePartialSum_succ`, a theorem declared in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 428](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L428). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#profile-partial-sum-succ).

## Block index of a profile

Let $\pi : \mathbb{N} \to \mathbb{N}$ be a sequence with
cumulative profile $\Pi_k = \sum_{j=1}^{k} \pi_j$. For a natural number $i$, the block index $k(i)$
is the least natural number $k$ with $i \le \Pi_k$, and $k(i) = 0$ if there is no such $k$. When
$i \ge 1$ and $\Pi$ is unbounded, $k(i)$ is the unique $k$ with $\Pi_{k-1} < i \le \Pi_k$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Section 7.2 (canonical sequential realization).

Formalized by `MetaMathlibExt.seqHeightIndex`, a definition declared in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 438](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#seq-height-index).

## Block index of the constant profile

For the constant profile $\pi_k = 1$, whose cumulative
profile is $\Pi_k = \sum_{j=1}^{k} \pi_j = k$, the block index $k(i)$, the least $k$ with
$i \le \Pi_k$, equals $i$ for every natural number $i$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Section 7.2 (canonical sequential realization).

Formalized by `MetaMathlibExt.seqHeightIndex_const_one`, a theorem declared in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 446](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L446). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#seq-height-index-const-one).

## Canonical sequential realization of a profile

Let $(\pi_k)_{k \ge 1}$ be a sequence of
nonnegative integers with partial sums $\Pi_k = \sum_{1 \le j \le k} \pi_j$. For $i \ge 1$ let
$k(i)$ be the least $k \ge 0$ with $i \le \Pi_k$, or $0$ if there is none, and let
$p_1 = 2, p_2 = 3, \dots$ be the primes in increasing order. The canonical sequential realization
$H_{\mathrm{seq}}$ of $\pi$ is the function $\mathbb{N} \to \mathbb{N}$ that sends $m \ge 1$ to
$\sum_{i \ge 1} a_i\, k(i)$, where $a_i$ is the exponent of $p_i$ in $m$, and sends $0$ to $0$;
thus $H_{\mathrm{seq}}$ is completely additive with $H_{\mathrm{seq}}(p_i) = k(i)$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Definition 2 (canonical sequential realization, Section 7.2).

Formalized by `MetaMathlibExt.canonicalSeqHeight`, a definition declared in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#canonical-seq-height).

## Inverting a polynomial profile

Let $\pi : \mathbb{N} \to \mathbb{N}$ be a sequence with
cumulative profile $\Pi_k = \sum_{j=1}^{k} \pi_j$, let $k(i)$ be its block index (the least $k$
with $i \le \Pi_k$, and $0$ if there is none), let $H_{\mathrm{seq}}$ be its canonical sequential
realization, and write $p_i$ for the $i$-th prime, indexed from one. Let $C > 0$ and $\alpha > 0$
be real numbers with $\Pi_k \sim C k^\alpha$ as $k \to \infty$. Then $k(i) \sim (i/C)^{1/\alpha}$
as $i \to \infty$, and $H_{\mathrm{seq}}(p_i) = k(i)$ for every $i \ge 1$.

The paper also assumes that $\Pi_k$ is eventually strictly increasing; that hypothesis is dropped
here, since $\Pi$ is nondecreasing, which suffices.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Lemma 4.

Stated but not proved: `MetaMathlibExt.seqHeightIndex_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 467](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L467). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#seq-height-index-is-equivalent).

## A logarithmic-integral sum

For every real $\beta > 0$,

$$\sum_{i=2}^{m} \frac{i^{\beta - 1}}{\log i} \sim \frac{m^\beta}{\beta \log m}$$

as $m \to \infty$ through the natural numbers.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Lemma 5.

Stated but not proved: `MetaMathlibExt.sum_rpow_div_log_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 480](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L480). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#sum-rpow-div-log-is-equivalent).

## Prime-harmonic growth of the canonical sequential realization

Let $(\pi_k)_{k \ge 1}$ be
a sequence of nonnegative integers with partial sums $\Pi_k = \sum_{1 \le j \le k} \pi_j$, let
$H_{\mathrm{seq}}$ be its canonical sequential realization, and suppose that $C > 0$ and
$\alpha > 0$ are real numbers with $\Pi_k \sim C k^\alpha$ as $k \to \infty$. Write
$S(x) = \sum_{p \le x} H_{\mathrm{seq}}(p)/p$, the sum over primes $p \le x$, and let $m(x)$ be
the number of primes $p \le x$. Then, as $x \to \infty$ over the reals,
$S(x) \sim \frac{\alpha}{C^{1/\alpha}} \cdot \frac{m(x)^{1/\alpha}}{\log m(x)}$ and
$S(x) = \Theta\bigl(x^{1/\alpha} / (\log x)^{1+1/\alpha}\bigr)$, where $f = \Theta(g)$ means
$f = O(g)$ and $g = O(f)$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Theorem 5.

Stated but not proved: `MetaMathlibExt.canonicalSeq_primeHarmonicSum` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 491](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L491). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#canonical-seq-prime-harmonic-sum).

## Average order of the canonical sequential realization

Let $(\pi_k)_{k \ge 1}$ be a
sequence of nonnegative integers with partial sums $\Pi_k = \sum_{1 \le j \le k} \pi_j$, let
$H_{\mathrm{seq}}$ be its canonical sequential realization, and suppose that $C > 0$ and
$\alpha > 0$ are real numbers with $\Pi_k \sim C k^\alpha$ as $k \to \infty$. Then, as
$x \to \infty$ over the reals, each of the three functions
$x \sum_{p \le x} H_{\mathrm{seq}}(p)/p$, $\sum_{p \le x} H_{\mathrm{seq}}(p) \log x / \log p$
(both sums over primes $p \le x$) and $\sum_{1 \le n \le x} H_{\mathrm{seq}}(n)$ is
$\Theta\bigl(x^{1+1/\alpha} / (\log x)^{1+1/\alpha}\bigr)$, where $f = \Theta(g)$ means
$f = O(g)$ and $g = O(f)$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Corollary 2, statement read from the journal PDF (the corpus record carries the prose of Section 7.6 that follows it).

Stated but not proved: `MetaMathlibExt.canonicalSeq_averageOrder` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 513](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L513). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#canonical-seq-average-order).

## Growth for the ordinary partition profile

Let $H_{\mathrm{seq}}$ be the canonical
sequential realization of the constant profile $\pi_k = 1$ for all $k \ge 1$ (so
$H_{\mathrm{seq}}(p_i) = i$ for the $i$-th prime $p_i$). Then, as $x \to \infty$ over the reals,
$\sum_{p \le x} H_{\mathrm{seq}}(p)/p = \Theta\bigl(x / (\log x)^2\bigr)$, the sum running over
primes $p \le x$, and
$\sum_{1 \le n \le x} H_{\mathrm{seq}}(n) = \Theta\bigl(x^2 / (\log x)^2\bigr)$, where
$f = \Theta(g)$ means $f = O(g)$ and $g = O(f)$.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Corollary 3.

Stated but not proved: `MetaMathlibExt.canonicalSeq_partitionProfile_growth` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 531](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L531). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#canonical-seq-partition-profile-growth).

## Growth for the plane partition profile

Let $H_{\mathrm{seq}}$ be the canonical
sequential realization of the profile $\pi_k = k$ for $k \ge 1$, let
$S(x) = \sum_{p \le x} H_{\mathrm{seq}}(p)/p$ (the sum over primes $p \le x$) and
$F(x) = \sum_{1 \le n \le x} H_{\mathrm{seq}}(n)$, and let $m(x)$ be the number of primes
$p \le x$. Then, as $x \to \infty$ over the reals,
$S(x) \sim 2\sqrt{2}\, \sqrt{m(x)} / \log m(x)$,
$S(x) = \Theta\bigl(x^{1/2} / (\log x)^{3/2}\bigr)$, $F(x) = \Theta\bigl(x\, S(x)\bigr)$ and
$F(x) = \Theta\bigl(x^{3/2} / (\log x)^{3/2}\bigr)$, where $f = \Theta(g)$ means $f = O(g)$ and
$g = O(f)$.

Here the partial sums are $k(k+1)/2 \sim k^2/2$, so this is the case $\alpha = 2$, $C = 1/2$ of
the general growth laws.

## Sources

- Hartosh Singh Bal, *Completely Additive Height Functions: Profile Laws, Matula Bounds, and Inverse Growth*, INTEGERS 26 (2026), Article A116, Corollary 4.

Stated but not proved: `MetaMathlibExt.canonicalSeq_planePartitionProfile_growth` is written with `theorem_wanted` in [WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean, line 544](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CompletelyAdditiveHeightWanted.lean#L544). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html#canonical-seq-plane-partition-profile-gr).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Completely additive height functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-additive-height-functions)
