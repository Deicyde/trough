---
declaration: section
origin: cited
lean: MetaMathlibExt.product_theorem_special_linear
statement: formalized
---

# Combinatorics in groups: its own results

1 result, 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/index.html).

Additive and Ramsey-type combinatorics inside groups: approximate subgroups and product theorems, small doubling, partitions and colourings of groups, dense and coset-free partitions, subset factorizations, products of large normal subsets.

## Product theorem for special linear groups

Let $n$ be a natural number. For every real
$\varepsilon$ with $0 < \varepsilon < 1$ there is a real $\delta > 0$ such that the following
holds for every finite field $k$: if $A$ is a subset of $\mathrm{SL}(n, k)$ with $A^{-1} = A$ and
$1 \in A$ that generates $\mathrm{SL}(n, k)$, then $|A|^{1+\delta} \le |A^3|$ or
$|\mathrm{SL}(n, k)|^{1-\varepsilon} \le |A|$, where $A^3 = \{abc : a, b, c \in A\}$. Thus
$\delta$ depends only on $n$ and $\varepsilon$.

## Sources

- S. Machado, *Topics in Geometric Group Theory* lecture notes, <https://sites.google.com/view/simonmachado/teaching>, Theorem 1.9; originals B. Breuillard, B. Green, T. Tao, *Approximate subgroups of linear groups*, Geom. Funct. Anal. 21 (2011), and L. Pyber, E. Szabó, *Growth in finite simple groups of Lie type*, J. Amer. Math. Soc. 29 (2016).

Stated but not proved: `MetaMathlibExt.product_theorem_special_linear` is written with `theorem_wanted` in [WantedExt/GroupTheory/ProductTheoremSpecialLinearWanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ProductTheoremSpecialLinearWanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/index.html#product-theorem-special-linear).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Combinatorics in groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/combinatorics-in-groups)
