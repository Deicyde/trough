---
declaration: section
origin: cited
lean: Nat.IsSophieGermainPrime, Nat.isSophieGermainPrime_iff, Nat.IsSophieGermainPrime.prime, Nat.IsSophieGermainPrime.prime_two_mul_add_one, MetaMathlibExt.infinite_setOf_prime_not_isSophieGermainPrime, MetaMathlibExt.setOf_prime_not_isSophieGermainPrime_eq_inter, MetaMathlibExt.isSophieGermainPrime_ne_two_iff_factorial_modEq
statement: formalized
---

# Sophie Germain primes

7 results, 4 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sophie-germain-primes/index.html).

## Sophie Germain primes

A natural number $p$ is a Sophie Germain prime if $p$ is prime and
$2p + 1$ is prime. The case $p = 2$ is not excluded.

## Sources

- arXiv:2311.13375, lines 83–85.

Formalized by `Nat.IsSophieGermainPrime`, a definition declared in [MathlibExt/NumberTheory/SophieGermainPrime.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SophieGermainPrime.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sophie-germain-primes/index.html#is-sophie-germain-prime).

## Characterization of Sophie Germain primes

A natural number $p$ is a Sophie Germain prime
if and only if $p$ is prime and $2p + 1$ is prime.

Formalized by `Nat.isSophieGermainPrime_iff`, a theorem declared in [MathlibExt/NumberTheory/SophieGermainPrime.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SophieGermainPrime.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sophie-germain-primes/index.html#is-sophie-germain-prime-iff).

## Sophie Germain primes are prime

If $p$ is a Sophie Germain prime, then $p$ is prime.

Formalized by `Nat.IsSophieGermainPrime.prime`, a theorem declared in [MathlibExt/NumberTheory/SophieGermainPrime.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SophieGermainPrime.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sophie-germain-primes/index.html#prime).

## Safe prime of a Sophie Germain prime

If $p$ is a Sophie Germain prime, then $2p + 1$ is
prime.

Formalized by `Nat.IsSophieGermainPrime.prime_two_mul_add_one`, a theorem declared in [MathlibExt/NumberTheory/SophieGermainPrime.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SophieGermainPrime.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sophie-germain-primes/index.html#prime-two-mul-add-one).

## Infinitely many primes are not Sophie Germain primes

The set of primes $q$ that are not
Sophie Germain primes, that is, the primes $q$ for which $2q + 1$ is not prime, is infinite.

## Sources

- Takashi Agoh, *A Note on Sophie Germain Primes*, INTEGERS 25 (2025), Article A83, Theorem 3.1.

Stated but not proved: `MetaMathlibExt.infinite_setOf_prime_not_isSophieGermainPrime` is written with `theorem_wanted` in [WantedExt/NumberTheory/NonSophieGermainPrimesWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/NonSophieGermainPrimesWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sophie-germain-primes/index.html#infinite-set-of-prime-not-is-sophie-germ).

## Primes that are not Sophie Germain primes

For an odd prime $p$, let
$A(p) = \{pr + (p - 1)/2 : r = 1, 2, 3, \dots\}$, and let $A$ be the union of the sets $A(p)$ over
all odd primes $p$. A prime is not a Sophie Germain prime if and only if it lies in $A$;
equivalently, the Sophie Germain primes are exactly the primes outside $A$.

## Sources

- Takashi Agoh, *A Note on Sophie Germain Primes*, INTEGERS 25 (2025), Article A83, Theorem 2.1.

Stated but not proved: `MetaMathlibExt.setOf_prime_not_isSophieGermainPrime_eq_inter` is written with `theorem_wanted` in [WantedExt/NumberTheory/NonSophieGermainPrimesWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/NonSophieGermainPrimesWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sophie-germain-primes/index.html#set-of-prime-not-is-sophie-germain-prime).

## Wilson-type characterization of Sophie Germain primes

Let $a \ge 2$ be a natural number.
Then $a$ is a Sophie Germain prime other than $2$ if and only if
$(a - 1)! \equiv 2a - 1 \pmod{a(2a + 1)}$ or $(a - 1)! \equiv -(6a + 1) \pmod{a(2a + 1)}$, the
congruences being taken in the integers.

The paper states this for all positive integers $a$; at $a = 1$ the first congruence holds
($0! = 1 \equiv 1 \pmod 3$) while $1$ is not prime (the proof's appeal to Wilson's theorem modulo
$a$ needs $a \ge 2$).

## Sources

- Takashi Agoh, *A Note on Sophie Germain Primes*, INTEGERS 25 (2025), Article A83, Theorem 5.3.

Stated but not proved: `MetaMathlibExt.isSophieGermainPrime_ne_two_iff_factorial_modEq` is written with `theorem_wanted` in [WantedExt/NumberTheory/NonSophieGermainPrimesWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/NonSophieGermainPrimesWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sophie-germain-primes/index.html#is-sophie-germain-prime-ne-two-iff-facto).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sophie Germain primes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sophie-germain-primes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/primes-primality/special-primes/sophie-germain-primes)
