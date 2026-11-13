---
declaration: section
origin: cited
lean: MetaMathlibExt.carmichaelIndex, MetaMathlibExt.carmichaelIndex_one, MetaMathlibExt.carmichaelIndex_four_and_sixtySix, MetaMathlibExt.carmichaelIndex_eq_prod, MetaMathlibExt.carmichaelIndex_ne_sub_one
statement: formalized
---

# Carmichael index

5 results, 3 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/carmichael-index/index.html).

## Carmichael index

For a natural number $n$, the Carmichael index $N(n)$ is the number of
integers $a$ with $0 \le a \le n - 1$ and $a^n \equiv a \pmod{n}$.

## Sources

- Atsushi Yamagami and Youichi Inaba, *On a Formula and Some Properties of Carmichael Indices*, INTEGERS 24 (2024), Article A40, Definition 1.

Formalized by `MetaMathlibExt.carmichaelIndex`, a definition declared in [WantedExt/NumberTheory/CarmichaelIndexWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CarmichaelIndexWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/carmichael-index/index.html#carmichael-index).

## The Carmichael index of 1

The Carmichael index of $1$ is $N(1) = 1$.

## Sources

- Yamagami and Inaba, *On a Formula and Some Properties of Carmichael Indices*, INTEGERS 24 (2024), Article A40, Section 1.

Formalized by `MetaMathlibExt.carmichaelIndex_one`, a theorem declared in [WantedExt/NumberTheory/CarmichaelIndexWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CarmichaelIndexWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/carmichael-index/index.html#carmichael-index-one).

## The Carmichael indices of 4 and 66

The Carmichael index satisfies $N(4) = 2$ and
$N(66) = 24$.

## Sources

- Yamagami and Inaba, *On a Formula and Some Properties of Carmichael Indices*, INTEGERS 24 (2024), Article A40, Example 1 (Table 1) and Example 3.

Formalized by `MetaMathlibExt.carmichaelIndex_four_and_sixtySix`, a theorem declared in [WantedExt/NumberTheory/CarmichaelIndexWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CarmichaelIndexWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/carmichael-index/index.html#carmichael-index-four-and-sixty-six).

## Product formula for the Carmichael index

Let $n \ge 2$ and, for each prime $p$ dividing
$n$, let $p^{e_p}$ be the largest power of $p$ dividing $n$. Then the Carmichael index of $n$ is
$N(n) = \prod_p \bigl(N(n; p^{e_p}) + 1\bigr)$, the product running over the primes $p$ dividing
$n$, where $N(n; p^{e_p})$ is the number of units of $\mathbb{Z}/p^{e_p}\mathbb{Z}$ whose
multiplicative order divides $\gcd(p - 1, n/p^{e_p} - 1)$.

## Sources

- Yamagami and Inaba, *On a Formula and Some Properties of Carmichael Indices*, INTEGERS 24 (2024), Article A40, Theorem 1.

Stated but not proved: `MetaMathlibExt.carmichaelIndex_eq_prod` is written with `theorem_wanted` in [WantedExt/NumberTheory/CarmichaelIndexWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CarmichaelIndexWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/carmichael-index/index.html#carmichael-index-eq-prod).

## The Carmichael index of $n$ is never $n - 1$

For every positive integer $n$, the
Carmichael index $N(n)$, the number of integers $a$ with $0 \le a \le n - 1$ and
$a^n \equiv a \pmod{n}$, is not equal to $n - 1$.

## Sources

- Yamagami and Inaba, *On a Formula and Some Properties of Carmichael Indices*, INTEGERS 24 (2024), Article A40, Theorem 2.

Stated but not proved: `MetaMathlibExt.carmichaelIndex_ne_sub_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/CarmichaelIndexWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CarmichaelIndexWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/carmichael-index/index.html#carmichael-index-ne-sub-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Carmichael index](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/carmichael-index/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/carmichael-index)
