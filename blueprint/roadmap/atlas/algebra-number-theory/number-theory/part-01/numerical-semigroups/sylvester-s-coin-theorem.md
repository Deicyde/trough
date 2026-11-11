---
declaration: section
origin: cited
lean: MetaMathlibExt.sylvester_coin_distinct_odd_primes, MetaMathlibExt.sylvester_coin_theorem
statement: formalized
proof: formalized
---

# Sylvester's coin theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/sylvester-s-coin-theorem/index.html).

## Sylvester's coin theorem for two distinct odd primes

Let $p$ and $q$ be distinct odd
primes. Then the number of natural numbers $n$ that cannot be written as $n = px + qy$ with
natural numbers $x, y$ is $(p-1)(q-1)/2$.

Distinct odd primes are coprime, so this is a special case of Sylvester's count for coprime
$p$ and $q$.

## Sources

- Damanvir Singh Binner, "Generalization of a Result of Sylvester Related to the Frobenius Coin Problem", Journal of Integer Sequences 24 (2021), Article 21.8.4, Theorem `Sylvester'` (the Special Case of Sylvester's theorem), source lines 123–127, <https://cs.uwaterloo.ca/journals/JIS/VOL24/Binner/binner13.tex>. The paper attributes the general coprime statement to Sylvester (1882).

Formalized by `MetaMathlibExt.sylvester_coin_distinct_odd_primes`, a theorem declared in [MathlibExt/NumberTheory/SylvesterCoinDistinctOddPrimes.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterCoinDistinctOddPrimes.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/sylvester-s-coin-theorem/index.html#sylvester-coin-distinct-odd-primes).

## Sylvester's coin theorem

Let $a$ and $b$ be coprime natural numbers. Then the number of
natural numbers $n$ that cannot be written as $n = ax + by$ with natural numbers $x, y$ is
$(a - 1)(b - 1)/2$.

Subtraction here is truncated at $0$: if $a = 0$ or $b = 0$, coprimality forces the other number
to be $1$, every natural number is representable, and both sides are $0$.

## Sources

- J. J. Sylvester on the Frobenius coin problem (1882); the count of gaps is `(a - 1) * (b - 1) / 2` for coprime `a b`.

Formalized by `MetaMathlibExt.sylvester_coin_theorem`, a theorem declared in [MathlibExt/NumberTheory/SylvesterCoinTheorem.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterCoinTheorem.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/sylvester-s-coin-theorem/index.html#sylvester-coin-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sylvester's coin theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/sylvester-s-coin-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/numerical-semigroups/sylvester-s-coin-theorem)
