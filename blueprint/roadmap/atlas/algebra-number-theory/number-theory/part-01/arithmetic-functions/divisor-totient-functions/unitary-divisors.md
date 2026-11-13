---
declaration: section
origin: cited
lean: Nat.unitaryDivisors, Nat.sigmaStar, Set.IsPrimitiveByDivisibility
statement: formalized
proof: formalized
---

# Unitary divisors

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/unitary-divisors/index.html).

## Unitary divisors

## Unitary divisors

For a natural number $n$, the unitary divisors of $n$ are the divisors
$d$ of $n$ that are coprime to the complementary divisor $n/d$, that is, with $\gcd(d, n/d) = 1$.
For $n = 0$ there are no unitary divisors.

Formalized by `Nat.unitaryDivisors`, a definition declared in [MathlibExt/NumberTheory/UnitaryDivisor.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/UnitaryDivisor.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/unitary-divisors/index.html#unitary-divisors).

## Sum of unitary divisors

For a natural number $n$, $\sigma^*(n)$ denotes the sum of the
unitary divisors of $n$.

Formalized by `Nat.sigmaStar`, a definition declared in [MathlibExt/NumberTheory/UnitaryDivisor.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/UnitaryDivisor.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/unitary-divisors/index.html#sigma-star).

## Elements primitive under divisibility

Let $S$ be a set of natural numbers. A natural
number $n$ is primitive in $S$ under divisibility when $n \in S$ and no proper divisor of $n$,
that is, no divisor $d$ of $n$ with $d < n$, belongs to $S$.

Formalized by `Set.IsPrimitiveByDivisibility`, a definition declared in [MathlibExt/NumberTheory/UnitaryDivisor.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/UnitaryDivisor.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/unitary-divisors/index.html#is-primitive-by-divisibility).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Unitary divisors](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/unitary-divisors/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/unitary-divisors)
