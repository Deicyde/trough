---
declaration: section
origin: cited
lean: Nat.IsSocialistPrime, Nat.IsSocialistPrime.factorial_mod_ne
statement: formalized
proof: formalized
---

# Socialist primes

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/socialist-primes/index.html).

## Socialist primes

A natural number $p$ is a socialist prime if $p$ is prime, $p > 5$, and
the factorials $2!, 3!, \ldots, (p-1)!$ have pairwise distinct remainders modulo $p$.

## Sources

- Trudgian, arXiv:1310.6403v2, line 24.

Formalized by `Nat.IsSocialistPrime`, a definition declared in [MathlibExt/NumberTheory/SocialistPrime.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SocialistPrime.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/socialist-primes/index.html#is-socialist-prime).

## Distinct factorial residues modulo a socialist prime

Let $p$ be a socialist prime. If $a$
and $b$ are distinct natural numbers with $2 \le a \le p - 1$ and $2 \le b \le p - 1$, then
$a!$ and $b!$ have different remainders modulo $p$.

Formalized by `Nat.IsSocialistPrime.factorial_mod_ne`, a theorem declared in [MathlibExt/NumberTheory/SocialistPrime.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SocialistPrime.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/socialist-primes/index.html#factorial-mod-ne).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Socialist primes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/socialist-primes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/primes-primality/special-primes/socialist-primes)
