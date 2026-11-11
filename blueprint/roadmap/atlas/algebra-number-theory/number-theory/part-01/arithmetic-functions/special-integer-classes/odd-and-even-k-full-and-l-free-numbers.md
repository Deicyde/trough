---
declaration: section
origin: cited
lean: MetaMathlibExt.tendsto_card_odd_kFull_div_card_even_kFull, MetaMathlibExt.tendsto_card_odd_kFull_lFree_div_card_even_kFull_lFree, MetaMathlibExt.tendsto_card_odd_lFree_div_card_even_lFree
statement: formalized
---

# Odd and even k-full and l-free numbers

3 results, 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/odd-and-even-k-full-and-l-free-numbers/index.html).

## Odd-to-even ratio of $k$-full numbers

Let $k \ge 2$. For a natural number $N$ let
$K_o(N)$ and $K_e(N)$ be the numbers of odd and of even $k$-full numbers $n \le N$. Then
$K_o(N)/K_e(N) \to 2 - 2^{1 - 1/k}$ as $N \to \infty$.

The counts up to a real $x$ depend only on $\lfloor x \rfloor$, so this is the same as the limit
as $x \to \infty$ through the reals.

## Sources

- Sunanta Srisopha and Teerapat Srichan, *The Odd/Even Dichotomy for the Set of Numbers That Are Both k-Full and l-Free*, INTEGERS 24 (2024), Article A106, Corollary 2.

Stated but not proved: `MetaMathlibExt.tendsto_card_odd_kFull_div_card_even_kFull` is written with `theorem_wanted` in [WantedExt/NumberTheory/KFullOddEvenWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KFullOddEvenWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/odd-and-even-k-full-and-l-free-numbers/index.html#tendsto-card-odd-k-full-div-card-even-k).

## Odd-to-even ratio of $k$-full, $l$-free numbers

Let $2 \le k < l$. Call a natural number
$n$ a $[k, l]$-integer if it is $k$-full and $l$-free, that is, $n \ge 1$ and every prime $p$
dividing $n$ satisfies $p^k \mid n$ and $p^l \nmid n$. For a natural number $N$ let $O_{k,l}(N)$
and $E_{k,l}(N)$ be the numbers of odd and of even $[k, l]$-integers $n \le N$. Then
$O_{k,l}(N)/E_{k,l}(N) \to (2 - 2^{1 - 1/k})/(1 - 2^{1 - l/k})$ as $N \to \infty$.

The counts up to a real $x$ depend only on $\lfloor x \rfloor$, so this is the same as the limit
as $x \to \infty$ through the reals.

## Sources

- Sunanta Srisopha and Teerapat Srichan, *The Odd/Even Dichotomy for the Set of Numbers That Are Both k-Full and l-Free*, INTEGERS 24 (2024), Article A106, Theorem 1.

Stated but not proved: `MetaMathlibExt.tendsto_card_odd_kFull_lFree_div_card_even_kFull_lFree` is written with `theorem_wanted` in [WantedExt/NumberTheory/KFullOddEvenWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KFullOddEvenWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/odd-and-even-k-full-and-l-free-numbers/index.html#tendsto-card-odd-k-full-l-free-div-card).

## Odd-to-even ratio of $l$-free numbers

Let $l \ge 2$. For a natural number $N$ let $O(N)$
and $E(N)$ be the numbers of odd and of even $l$-free positive integers $n \le N$. Then
$O(N)/E(N) \to 2^l/(2^l - 2)$ as $N \to \infty$.

This is the case $k = 1$ of the odd-to-even ratio for $k$-full, $l$-free numbers, since every
positive integer is $1$-full.

## Sources

- Sunanta Srisopha and Teerapat Srichan, *The Odd/Even Dichotomy for the Set of Numbers That Are Both k-Full and l-Free*, INTEGERS 24 (2024), Article A106, Corollary 1.

Stated but not proved: `MetaMathlibExt.tendsto_card_odd_lFree_div_card_even_lFree` is written with `theorem_wanted` in [WantedExt/NumberTheory/KFullOddEvenWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KFullOddEvenWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/odd-and-even-k-full-and-l-free-numbers/index.html#tendsto-card-odd-l-free-div-card-even-l).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Odd and even k-full and l-free numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/odd-and-even-k-full-and-l-free-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/odd-and-even-k-full-and-l-free-numbers)
