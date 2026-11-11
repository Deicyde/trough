---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ErdosSupersingularPrimesWanted.ErdosSupersingularPrimes.Solution, MathlibExt.NumberTheory.ErdosSupersingularPrimesWanted.ErdosSupersingularPrimes.k₀, MathlibExt.NumberTheory.ErdosSupersingularPrimesWanted.ErdosSupersingularPrimes.theorem_2
statement: formalized
---

# Perfect powers in products of arithmetic progressions

3 results, 1 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/perfect-powers-in-products-of-arithmetic-progres/index.html).

## Solutions of the Erdős equation for products of arithmetic progressions

For a natural
number $k$, a solution consists of a natural number $l$ and integers $n$, $d$, $y$ such that
$\gcd(n, d) = 1$ and

$$\prod_{i=0}^{k-1} (n + i d) = y^l,$$

that is, $n (n + d) (n + 2d) \cdots (n + (k - 1)d) = y^l$.

Formalized by `MathlibExt.NumberTheory.ErdosSupersingularPrimesWanted.ErdosSupersingularPrimes.Solution`, a structure declared in [WantedExt/NumberTheory/ErdosSupersingularPrimesWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosSupersingularPrimesWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/perfect-powers-in-products-of-arithmetic-progres/index.html#solution).

## The threshold constant $k_0$ in the Bennett–Siksek theorem

A natural number $k_0$, to
be supplied: the absolute constant from which Theorem 2 holds, that is, for every natural
number $k \ge k_0$, every solution in integers $n$, $d$, $y$ and a prime natural number $l$ of
$\prod_{i=0}^{k-1} (n + i d) = y^l$ with $\gcd(n, d) = 1$ has $y = 0$ or $d = 0$ or
$l \le \exp(10^k)$.

The source requires $k_0$ to be effectively computable; the formal statement does not enforce
this.

## Sources

- M. Bennett and S. Siksek, `A conjecture of Erdős, supersingular primes and short character sums`, Annals of Math, 191 (2) 2020. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_erdos_supersingular_primes` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.ErdosSupersingularPrimesWanted.ErdosSupersingularPrimes.k₀` is written with `def_wanted` in [WantedExt/NumberTheory/ErdosSupersingularPrimesWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosSupersingularPrimesWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/perfect-powers-in-products-of-arithmetic-progres/index.html#k).

## Bennett–Siksek theorem on perfect powers in arithmetic progressions

Let $k_0$ be the
threshold constant of this module. For every natural number $k \ge k_0$, every natural number
$l$ that is prime, and all integers $n$, $d$, $y$ with $\gcd(n, d) = 1$ and

$$\prod_{i=0}^{k-1} (n + i d) = y^l,$$

we have $y = 0$ or $d = 0$ or $l \le \exp(10^k)$.

The source asserts that $k_0$ is an effectively computable absolute constant; the formal
statement leaves $k_0$ to be supplied and does not enforce computability.

## Sources

- M. Bennett and S. Siksek, `A conjecture of Erdős, supersingular primes and short character sums`, Annals of Math, 191 (2) 2020. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_erdos_supersingular_primes` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.ErdosSupersingularPrimesWanted.ErdosSupersingularPrimes.theorem_2` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosSupersingularPrimesWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosSupersingularPrimesWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/perfect-powers-in-products-of-arithmetic-progres/index.html#theorem-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Perfect powers in products of arithmetic progressions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/perfect-powers-in-products-of-arithmetic-progres/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/perfect-powers-in-products-of-arithmetic-progres)
