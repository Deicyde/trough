---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SymmetricGroupProductOrdersKourovka18Problem49Wanted.symmetricGroupHasProductWithOrders, MathlibExt.GroupTheory.SymmetricGroupProductOrdersKourovka18Problem49Wanted.symmetricGroupHasProductWithOrders_holds
statement: formalized
---

# Orders of products in symmetric groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/orders-of-products-in-symmetric-groups/index.html).

## Kohl's question on orders of products in symmetric groups

For every natural number $n$
and all natural numbers $a, b, c$ with $1 < a \le n - 2$, $1 < b \le n - 2$ and $1 < c \le n - 2$,
the symmetric group $S_n$ contains permutations $x$ and $y$ such that $x$ has order $a$, $y$ has
order $b$ and $xy$ has order $c$.

Formalized by `MathlibExt.GroupTheory.SymmetricGroupProductOrdersKourovka18Problem49Wanted.symmetricGroupHasProductWithOrders`, a definition declared in [WantedExt/GroupTheory/SymmetricGroupProductOrdersKourovka18Problem49Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SymmetricGroupProductOrdersKourovka18Problem49Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/orders-of-products-in-symmetric-groups/index.html#symmetric-group-has-product-with-orders).

## Permutations of prescribed orders with product of prescribed order

For every natural
number $n$ and all natural numbers $a, b, c$ with $1 < a \le n - 2$, $1 < b \le n - 2$ and
$1 < c \le n - 2$, the symmetric group $S_n$ contains permutations $x$ and $y$ of orders $a$ and
$b$ whose product $xy$ has order $c$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 18.49 (S. Kohl); resolution: G. A. Miller, Amer. J. Math. 22 (1900), no. 2, 185-190; J. König, European J. Combin. 57 (2016), 50-56, Kourovka Archive, Problem 18.49: Yes, it is (Miller); another solution by König, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.SymmetricGroupProductOrdersKourovka18Problem49Wanted.symmetricGroupHasProductWithOrders_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SymmetricGroupProductOrdersKourovka18Problem49Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SymmetricGroupProductOrdersKourovka18Problem49Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/orders-of-products-in-symmetric-groups/index.html#symmetric-group-has-product-with-orders-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Orders of products in symmetric groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/orders-of-products-in-symmetric-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/orders-of-products-in-symmetric-groups)
