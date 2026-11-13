---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ErdosProblem429Wanted.erdos429_refuted, MetaMathlibExt.exists_sparse_subset_pow_no_prime_translate
statement: formalized
---

# Admissible sets with no prime translate

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/admissible-sets-with-no-prime-translate/index.html).

## Sparse admissible sets without prime translates (Erdős Problem 429)

For every function
$f : \mathbb{N} \to \mathbb{N}$ with $f(N) \to \infty$ as $N \to \infty$, there is an infinite set
$A$ of natural numbers such that $|A \cap \{1, \ldots, N\}| \le f(N)$ for every natural number
$N$, for every prime $p$ some residue class modulo $p$ contains no element of $A$, and for every
integer $n$ some $a \in A$ makes $n + a$ not a positive prime.

Resolved false: Disproved by Weisenberg (2024); ported as a formal statement. Source: D.
Weisenberg, Sparse Admissible Sets and a Problem of Erdős and Graham, Integers (2024). Moved
from `OpenConjectures/NumberTheory/ErdosProblem429`.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem429Wanted.erdos429_refuted` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem429Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem429Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/admissible-sets-with-no-prime-translate/index.html#erdos429-refuted).

## Sparse subsets of powers with no prime translate

Let $a$ be a natural number that is a
primitive root modulo infinitely many primes, and let $S = \{a^k : k \ge 1\}$. For every
non-decreasing unbounded function $f : \mathbb{N} \to \mathbb{N}$ there is an infinite set
$A \subseteq S$ such that $|A \cap \{1, \dots, N\}| \le f(N)$ for every natural number $N$, and
such that no translate $A + n$ with $n \in \mathbb{Z}$ consists entirely of (positive) primes.

The hypothesis forces $a \ge 2$. The exponent range $k \ge 1$ is the reading in which the
paper's remark "$S$ is admissible" holds: with $k = 0$ and $a$ even, $S$ contains $1$ and $a$,
which meet both residue classes modulo $2$.

## Sources

- Desmond Weisenberg, *Sparse Admissible Sets and a Problem of Erdős and Graham*, INTEGERS 24 (2024), Article A89, Theorem 1.

Stated but not proved: `MetaMathlibExt.exists_sparse_subset_pow_no_prime_translate` is written with `theorem_wanted` in [WantedExt/NumberTheory/SparseAdmissiblePowerSetsWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SparseAdmissiblePowerSetsWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/admissible-sets-with-no-prime-translate/index.html#exists-sparse-subset-pow-no-prime-transl).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Admissible sets with no prime translate](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/admissible-sets-with-no-prime-translate/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-patterns/admissible-sets-with-no-prime-translate)
