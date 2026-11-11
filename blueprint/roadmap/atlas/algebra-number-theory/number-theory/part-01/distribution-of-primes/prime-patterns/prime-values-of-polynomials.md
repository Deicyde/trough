---
declaration: section
origin: cited
lean: Polynomial.BunyakovskyCondition, Polynomial.SchinzelCondition, MetaMathlibExt.conjectureA_prime_values_four_square
statement: formalized
---

# Prime values of polynomials

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/prime-values-of-polynomials/index.html).

## Bunyakovsky condition

An integer polynomial $f \in \mathbb{Z}[x]$ satisfies the
Bunyakovsky condition when it has degree at least $1$, is irreducible in $\mathbb{Z}[x]$, and has
positive leading coefficient.

Unlike the hypothesis of Bunyakovsky's conjecture, this condition does not require the values of
$f$ to have no common prime divisor.

Formalized by `Polynomial.BunyakovskyCondition`, a definition declared in [MathlibExt/Algebra/Polynomial/PrimeValueConditions.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/PrimeValueConditions.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/prime-values-of-polynomials/index.html#bunyakovsky-condition).

## Schinzel condition

A finite set $F$ of integer polynomials satisfies the Schinzel
condition when it has no fixed prime divisor: for every prime $p$ there is a natural number $n$
such that $p$ divides none of the values $f(n)$ for $f \in F$.

Formalized by `Polynomial.SchinzelCondition`, a definition declared in [MathlibExt/Algebra/Polynomial/PrimeValueConditions.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Polynomial/PrimeValueConditions.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/prime-values-of-polynomials/index.html#schinzel-condition).

## Infinitely many primes of the form $4k^2 + 2k + 1$

There are infinitely many natural
numbers $k$ such that $4k^2 + 2k + 1$ is prime.

The source derives this from its Conjecture A (Bunyakovsky's conjecture). Only this polynomial
is stated here, not the full Bunyakovsky conjecture nor the companion polynomial $9k^2 + 6k + 2$.

## Sources

- Jean-Marie De Koninck and Matthieu Moineau, "Consecutive Integers Divisible by a Power of their Largest Prime Factor", Journal of Integer Sequences 21 (2018), Article 18.9.3, lines 239–242, <https://cs.uwaterloo.ca/journals/JIS/VOL21/DeKoninck/dek22.tex>.

Stated but not proved: `MetaMathlibExt.conjectureA_prime_values_four_square` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/ConjectureAFourSquarePrimeValuesWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/ConjectureAFourSquarePrimeValuesWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/prime-values-of-polynomials/index.html#conjecture-a-prime-values-four-square).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Prime values of polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/prime-values-of-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-patterns/prime-values-of-polynomials)
