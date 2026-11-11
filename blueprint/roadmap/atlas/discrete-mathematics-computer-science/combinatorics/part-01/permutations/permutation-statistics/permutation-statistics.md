---
declaration: section
origin: cited
lean: MetaMathlibExt.sum_mul_numDerangements_eq_floor, MetaMathlibExt.zagier_probability_product_two_cyclic_permutations
statement: formalized
---

# Permutation statistics and cycle structure: its own results

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/index.html).

Descents, peaks, major index, left-to-right maxima, fixed points and derangements, cycle counts and the smallest cycle of a random permutation, products of cyclic permutations, Stirling and flattened Stirling permutations, Josephus permutations and permutation-guessing puzzles.

## A sum rule for derangements

For every natural number $p$,
$\sum_{n=0}^{p} n\, D(n) = \lfloor (p + 1)!/e \rfloor$, where $D(n)$ is the number of
derangements of $n$ objects.

## Sources

- Jean-Christophe Pain, *A Sum Rule for Derangements*, INTEGERS 25 (2025), Article A84, Theorem 1.

Stated but not proved: `MetaMathlibExt.sum_mul_numDerangements_eq_floor` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DerangementSumRuleWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DerangementSumRuleWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/index.html#sum-mul-num-derangements-eq-floor).

## Zagier's formula for products of two cyclic permutations

Let $n$ and $k$ be integers
with $n \ge 1$ and $1 \le k \le n$. Call a permutation of an $n$-element set cyclic when it has
exactly one cycle, fixed points counted as cycles. Write $c(n+1, k)$ for the unsigned Stirling
number of the first kind, the number of permutations of $n + 1$ elements with exactly $k$
cycles. If $\sigma$ and $\tau$ are chosen independently and uniformly among the cyclic
permutations of an $n$-element set, then the probability that $\sigma\tau$ has exactly $k$
cycles, fixed points included, is

$$\frac{1 + (-1)^{n-k}}{(n+1)!} \, c(n+1, k).$$

Proof: We formalize the plane-permutation transposition and reflection bijections of
Chen and Reidys, arXiv:1502.07674, lines 786-1074, and their specialization to Zagier's
recurrence, lines 1167-1370. A generating-polynomial coefficient identity supplies the
matching Stirling recurrence; descending induction on the cycle count finishes.

## Sources

- R. Cori and G. Hetyei, *On Reduced Unicellular Hypermonopoles*, Journal of Integer Sequences 28 (2025), Article 25.3.3, Theorem [Zagier], lines 351-359, <https://cs.uwaterloo.ca/journals/JIS/VOL28/Hetyei/hetyei2.tex>, quoting D. Zagier.

Formalized by `MetaMathlibExt.zagier_probability_product_two_cyclic_permutations`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/ZagierCyclicPermutationProduct.lean, line 6184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/ZagierCyclicPermutationProduct.lean#L6184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/index.html#zagier-probability-product-two-cyclic-pe).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Permutation statistics and cycle structure](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/permutations/permutation-statistics)
