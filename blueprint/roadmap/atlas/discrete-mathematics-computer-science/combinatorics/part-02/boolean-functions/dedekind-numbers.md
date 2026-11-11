---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.DedekindAntichainCountErdosProblem497Wanted.antichainCount, MathlibExt.Combinatorics.DedekindAntichainCountErdosProblem497Wanted.antichainCountLogAsymptotic, MathlibExt.Combinatorics.DedekindAntichainCountErdosProblem497Wanted.antichainCountLogAsymptotic_holds
statement: formalized
---

# Dedekind numbers

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/dedekind-numbers/index.html).

## Dedekind numbers

For a natural number $n$, the Dedekind number $M(n)$ is the number of
antichains with respect to inclusion among the subsets of the $n$-element set
$\{0, 1, \dots, n-1\}$, that is, of families of subsets in which no member is contained in a
different member; the empty family and the family $\{\emptyset\}$ are counted.

Formalized by `MathlibExt.Combinatorics.DedekindAntichainCountErdosProblem497Wanted.antichainCount`, a definition declared in [WantedExt/Combinatorics/DedekindAntichainCountErdosProblem497Wanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/DedekindAntichainCountErdosProblem497Wanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/dedekind-numbers/index.html#antichain-count).

## Erdős Problem 497: the asymptotic statement for Dedekind numbers

Let $M(n)$ be the
number of antichains with respect to inclusion among the subsets of an $n$-element set (the
Dedekind number). The statement is that $\log_2 M(n) / \binom{n}{\lfloor n/2 \rfloor} \to 1$
as $n \to \infty$; equivalently, $M(n) = 2^{(1 + o(1)) \binom{n}{\lfloor n/2 \rfloor}}$.

Formalized by `MathlibExt.Combinatorics.DedekindAntichainCountErdosProblem497Wanted.antichainCountLogAsymptotic`, a definition declared in [WantedExt/Combinatorics/DedekindAntichainCountErdosProblem497Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/DedekindAntichainCountErdosProblem497Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/dedekind-numbers/index.html#antichain-count-log-asymptotic).

## Kleitman's theorem on Dedekind numbers

Let $M(n)$ be the number of antichains with respect
to inclusion among the subsets of an $n$-element set. Then
$\log_2 M(n) / \binom{n}{\lfloor n/2 \rfloor} \to 1$ as $n \to \infty$; that is,
$M(n) = 2^{(1 + o(1)) \binom{n}{\lfloor n/2 \rfloor}}$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #497, https://www.erdosproblems.com/497 (status SOLVED (LEAN)); resolution: D. Kleitman, On Dedekind's problem: the number of monotone Boolean functions, Proc. Amer. Math. Soc. (1969), 677-682, erdosproblems.com/497: resolved by Kleitman, the number is 2^{(1 + o(1)) C(n, ⌊n/2⌋)}, https://www.erdosproblems.com/497.

Stated but not proved: `MathlibExt.Combinatorics.DedekindAntichainCountErdosProblem497Wanted.antichainCountLogAsymptotic_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/DedekindAntichainCountErdosProblem497Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/DedekindAntichainCountErdosProblem497Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/dedekind-numbers/index.html#antichain-count-log-asymptotic-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dedekind numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/dedekind-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/boolean-functions/dedekind-numbers)
