---
declaration: section
origin: cited
lean: MetaMathlibExt.collatzAccelerated, MetaMathlibExt.collatzAccelerated_of_odd, MetaMathlibExt.collatzAccelerated_of_even, MetaMathlibExt.IsCompatibleSemiprimePair, MetaMathlibExt.isCompatibleSemiprimePair_71_1609, MetaMathlibExt.arithmeticDerivative_bounds, MetaMathlibExt.odd_of_arithmeticDerivative_collatz_comm, MetaMathlibExt.composite_of_arithmeticDerivative_collatz_comm
statement: formalized
---

# Arithmetic derivative and the Collatz map

19 results, 5 proved and 14 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map/index.html).

## The accelerated Collatz map

The accelerated Collatz map $C : \mathbb{N} \to \mathbb{N}$
sends a natural number $n$ to $n/2$ if $n$ is even and to $(3n + 1)/2$ if $n$ is odd.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Section 2.

Formalized by `MetaMathlibExt.collatzAccelerated`, a definition declared in [WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map/index.html#collatz-accelerated).

## The accelerated Collatz map on odd numbers

Let $C$ be the accelerated Collatz map and
$T$ the Collatz map. For every odd natural number $n$, $C(n) = T(T(n))$.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Section 2.

Formalized by `MetaMathlibExt.collatzAccelerated_of_odd`, a theorem declared in [WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map/index.html#collatz-accelerated-of-odd).

## The accelerated Collatz map on even numbers

Let $C$ be the accelerated Collatz map and
$T$ the Collatz map. For every even natural number $n$, $C(n) = T(n)$.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Section 2.

Formalized by `MetaMathlibExt.collatzAccelerated_of_even`, a theorem declared in [WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map/index.html#collatz-accelerated-of-even).

## Compatible semiprimes

Natural numbers $p, q, r, s$ form a compatible semiprime pair,
and the semiprimes $pq$ and $rs$ are called compatible, when $p, q, r, s$ are primes with
$2(r + s) = p + q$ and $2rs = 3pq + 1$; equivalently, $r$ and $s$ are the roots of
$2x^2 - (p + q)x + 3pq + 1 = 0$.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Section 3, definition after Proposition 7.

Formalized by `MetaMathlibExt.IsCompatibleSemiprimePair`, a definition declared in [WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map/index.html#is-compatible-semiprime-pair).

## An example of compatible semiprimes

The semiprimes $71 \cdot 1609 = 114239$ and
$349 \cdot 491$ are compatible.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Table 1.

Formalized by `MetaMathlibExt.isCompatibleSemiprimePair_71_1609`, a theorem declared in [WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map/index.html#is-compatible-semiprime-pair-71-1609).

## Bounds for the arithmetic derivative

Let $n \ge 2$ be a natural number, let $p$ be the
least prime factor of $n$, and let $\Omega(n)$ be the number of prime factors of $n$ counted with
multiplicity. Then the arithmetic derivative $D(n)$ satisfies

$$\Omega(n) \, n^{(\Omega(n) - 1)/\Omega(n)} \le D(n) \le \frac{n \log_p n}{p},$$

and each of the two inequalities is an equality if and only if $n$ is a prime power.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Lemma 1 (`jis-2025-25.1.8-lem-1`).

Stated but not proved: `MetaMathlibExt.arithmeticDerivative_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map/index.html#arithmetic-derivative-bounds).

## Positive solutions of the Collatz arithmetic differential equation are odd

Let $D$ be
the arithmetic derivative and $C$ the accelerated Collatz map. Every positive integer $n$ with
$D(C(n)) = C(D(n))$ is odd.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Proposition 2 (`jis-2025-25.1.8-prop-2`).

Stated but not proved: `MetaMathlibExt.odd_of_arithmeticDerivative_collatz_comm` is written with `theorem_wanted` in [WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map/index.html#odd-of-arithmetic-derivative-collatz-com).

## Positive solutions of the Collatz arithmetic differential equation are composite

Let
$D$ be the arithmetic derivative and $C$ the accelerated Collatz map. Every positive integer $n$
with $D(C(n)) = C(D(n))$ is composite, that is, $n > 1$ and $n$ is not prime.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Proposition 3 (`jis-2025-25.1.8-prop-3`).

Stated but not proved: `MetaMathlibExt.composite_of_arithmeticDerivative_collatz_comm` is written with `theorem_wanted` in [WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map/index.html#composite-of-arithmetic-derivative-colla).

## Prime tetrations where the arithmetic derivative and the Collatz map commute

Let $D$ be
the arithmetic derivative and $C$ the accelerated Collatz map. For a prime $p$,
$D(C(p^p)) = C(D(p^p))$ if and only if $C(p^p) = q^q$ for some prime $q$.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Proposition 4 (`jis-2025-25.1.8-prop-4`).

Stated but not proved: `MetaMathlibExt.arithmeticDerivative_collatz_comm_prime_tetration_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map/index.html#arithmetic-derivative-collatz-comm-prime).

## Prime gap bound for semiprime solutions

Let $D$ be the arithmetic derivative and let $C$
be the accelerated Collatz map, $C(n) = n/2$ for even $n$ and $C(n) = (3n + 1)/2$ for odd $n$.
If $p$ and $q$ are primes with $q < p$ and $D(C(pq)) = C(D(pq))$, then
$p - q \ge 2\sqrt{30p^2 + 2} - 10p$.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Proposition 5 (`jis-2025-25.1.8-prop-5`).

Stated but not proved: `MetaMathlibExt.prime_gap_bound_of_arithmeticDerivative_collatz_comm` is written with `theorem_wanted` in [WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map/index.html#prime-gap-bound-of-arithmetic-derivative).

## No special semiprime solves the derivative–Collatz equation

Let $D$ be the arithmetic
derivative and let $C$ be the accelerated Collatz map, $C(n) = n/2$ for even $n$ and
$C(n) = (3n + 1)/2$ for odd $n$. Let $n$ be a positive integer with $D(C(n)) = C(D(n))$ and let
$p$ be a prime. Then $n \ne p^2$; if $p + 2$ is prime then $n \ne p(p + 2)$; if $p + 4$ is prime
then $n \ne p(p + 4)$; and if $2p + 1$ is prime then $n \ne p(2p + 1)$. Thus no such $n$ is the
square of a prime, a product of twin primes, a product of cousin primes, or the product of a
Sophie Germain prime and its safe prime.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Corollary 6 (`jis-2025-25.1.8-cor-6`).

Stated but not proved: `MetaMathlibExt.not_special_semiprime_of_arithmeticDerivative_collatz_comm` is written with `theorem_wanted` in [WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map/index.html#not-special-semiprime-of-arithmetic-deri).

## Prime roots give semiprime solutions

Let $D$ be the arithmetic derivative and $C$ the
accelerated Collatz map. Let $p$ and $q$ be primes and let $t \ge 0$ be an integer with
$t^2 = p^2 - 22pq + q^2 - 8$. If $r = (p + q + t)/4$ and $s = (p + q - t)/4$ are both primes,
then $C(pq) = rs$ and $D(C(pq)) = C(D(pq))$.

The numbers $r$ and $s$ are the roots $(p + q \pm \sqrt{p^2 - 22pq + q^2 - 8})/4$ of
$2x^2 - (p + q)x + 3pq + 1 = 0$.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Proposition 7 (`jis-2025-25.1.8-prop-7`).

Stated but not proved: `MetaMathlibExt.collatzAccelerated_mul_eq_and_comm_of_roots_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map/index.html#collatz-accelerated-mul-eq-and-comm-of-r).

## Compatible semiprimes modulo 3

Let $p, q, r, s$ be primes with $2(r + s) = p + q$ and
$2rs = 3pq + 1$, so that the semiprimes $pq$ and $rs$ are compatible. Then
$pq \equiv rs \equiv 2 \pmod 3$; moreover one of $p, q$ is congruent to $1$ and the other to $2$
modulo $3$, and likewise one of $r, s$ is congruent to $1$ and the other to $2$ modulo $3$.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Proposition 8 (`jis-2025-25.1.8-prop-8`).

Stated but not proved: `MetaMathlibExt.IsCompatibleSemiprimePair.mod_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map/index.html#mod-three).

## Compatible semiprimes have odd prime factors

Let $p, q, r, s$ be primes with
$2(r + s) = p + q$ and $2rs = 3pq + 1$, so that the semiprimes $pq$ and $rs$ are compatible.
Then $p$, $q$, $r$ and $s$ are all odd.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Lemma 9 (`jis-2025-25.1.8-lem-9`).

Stated but not proved: `MetaMathlibExt.IsCompatibleSemiprimePair.odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map/index.html#odd).

## Compatible semiprimes modulo 4

Let $p, q, r, s$ be primes with $2(r + s) = p + q$ and
$2rs = 3pq + 1$, so that the semiprime $pq$ is compatible with the semiprime $rs$. Then
$pq \equiv 3 \pmod 4$, and one of $p, q$ is congruent to $1$ and the other to $3$ modulo $4$.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Proposition 10 (`jis-2025-25.1.8-prop-10`).

Stated but not proved: `MetaMathlibExt.IsCompatibleSemiprimePair.mod_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map/index.html#mod-four).

## Bounds on the factors of compatible semiprimes

Suppose the semiprimes $pq$ and $rs$ are
compatible, where $q < p$. Then $r \ge 241$, $s \ge 241$, $3q < r < 3p$ and $3q < s < 3p$.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Lemma 11 (`jis-2025-25.1.8-lem-11`).

Stated but not proved: `MetaMathlibExt.IsCompatibleSemiprimePair.bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map/index.html#bounds).

## Compatible semiprimes modulo 5

Let $p, q, r, s$ be primes with $2(r + s) = p + q$ and
$2rs = 3pq + 1$, so that the semiprimes $pq$ and $rs$ are compatible. Then one of $p, q$ is
congruent to $1$ and the other to $4$ modulo $5$, and likewise one of $r, s$ is congruent to $1$
and the other to $4$ modulo $5$.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Proposition 12 (`jis-2025-25.1.8-prop-12`).

Stated but not proved: `MetaMathlibExt.IsCompatibleSemiprimePair.mod_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map/index.html#mod-five).

## Compatible semiprimes modulo 10

Let $p, q, r, s$ be primes with $2(r + s) = p + q$ and
$2rs = 3pq + 1$, so that the semiprimes $pq$ and $rs$ are compatible. Then one of $p, q$ is
congruent to $1$ and the other to $9$ modulo $10$, and likewise one of $r, s$ is congruent to $1$
and the other to $9$ modulo $10$.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Proposition 13 (`jis-2025-25.1.8-prop-13`).

Stated but not proved: `MetaMathlibExt.IsCompatibleSemiprimePair.mod_ten` is written with `theorem_wanted` in [WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map/index.html#mod-ten).

## Reciprocals of compatible semiprimes have a finite sum

Call a natural number $n$ a
compatible semiprime if $n = pq$ for primes $p, q$ for which there are primes $r, s$ with
$2(r + s) = p + q$ and $2rs = 3pq + 1$. The sum of $1/n$ over all compatible semiprimes $n$
converges.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Theorem 14 (`jis-2025-25.1.8-thm-14`).

Stated but not proved: `MetaMathlibExt.summable_inv_compatibleSemiprimes` is written with `theorem_wanted` in [WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CollatzArithmeticDerivativeWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map/index.html#summable-inv-compatible-semiprimes).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arithmetic derivative and the Collatz map](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/integer-sequences/iterated-self-referential/arithmetic-derivative-and-the-collatz-map)
