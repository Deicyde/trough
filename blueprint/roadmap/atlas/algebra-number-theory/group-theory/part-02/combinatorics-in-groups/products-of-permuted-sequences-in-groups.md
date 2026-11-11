---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.PermutedProductsCountKourovka18Problem50Wanted.permutedProductsTakeEveryCount, MathlibExt.GroupTheory.PermutedProductsCountKourovka18Problem50Wanted.permutedProductsTakeEveryCount_holds
statement: formalized
---

# Products of permuted sequences in groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/products-of-permuted-sequences-in-groups/index.html).

## Kohl's permuted-products statement (Kourovka 18.50)

The assertion that for all natural
numbers $n$ and $k$ with $1 \le k \le n!$ there are a group $G$ and pairwise distinct elements
$g_1, \dots, g_n \in G$ such that the set
$\lbrace g_{\sigma(1)} g_{\sigma(2)} \cdots g_{\sigma(n)} : \sigma \in S_n \rbrace$ of products
obtained by permuting the factors has exactly $k$ elements.

Formalized by `MathlibExt.GroupTheory.PermutedProductsCountKourovka18Problem50Wanted.permutedProductsTakeEveryCount`, a definition declared in [WantedExt/GroupTheory/PermutedProductsCountKourovka18Problem50Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PermutedProductsCountKourovka18Problem50Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/products-of-permuted-sequences-in-groups/index.html#permuted-products-take-every-count).

## Every number of distinct permuted products occurs (Kourovka 18.50)

For all natural
numbers $n$ and $k$ with $1 \le k \le n!$ there are a group $G$ and pairwise distinct elements
$g_1, \dots, g_n \in G$ such that the set
$\lbrace g_{\sigma(1)} g_{\sigma(2)} \cdots g_{\sigma(n)} : \sigma \in S_n \rbrace$ of products
obtained by permuting the factors has exactly $k$ elements.

The Kourovka Notebook (21st issue) answers 18.50 "Yes, it is true", by an AI-generated solution
confirmed by S. Kohl (P. Monticone, 2026); van Doorn, Judin, Monticone and Morrison (2026) give
an independent account.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 18.50 (S. Kohl); resolution: P. Monticone, preprint, 2026 (AI solution confirmed by S. Kohl), https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/05/18_50.pdf; W. van Doorn, E. Judin, P. Monticone and D. Morrison, On some problems from the Kourovka Notebook, preprint, arXiv:2607.17477 (2026), arXiv:2607.17477 abstract: for every 1 ≤ k ≤ n! there is a group containing n distinct elements whose n! ordered products take exactly k distinct values (found and verified in Lean by the Aristotle agent); the Kourovka Notebook (21st issue) marks 18.50 solved, https://arxiv.org/abs/2607.17477.

Stated but not proved: `MathlibExt.GroupTheory.PermutedProductsCountKourovka18Problem50Wanted.permutedProductsTakeEveryCount_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/PermutedProductsCountKourovka18Problem50Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PermutedProductsCountKourovka18Problem50Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/products-of-permuted-sequences-in-groups/index.html#permuted-products-take-every-count-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Products of permuted sequences in groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/products-of-permuted-sequences-in-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/combinatorics-in-groups/products-of-permuted-sequences-in-groups)
