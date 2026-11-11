---
declaration: section
origin: cited
lean: Set.IsProductFree
statement: formalized
proof: formalized
---

# Sum-free sets: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/index.html).

Sets with no solution to x+y=z or similar: sum-free sets in abelian groups and intervals, counts of sum-free and maximal sum-free sets, large sum-free subsets, square-sum-free, divisor-sum-free and non-averaging sets.

## Product-free set

A set $S$ in a type $M$ with a multiplication is product-free if
$xy \notin S$ for all $x, y \in S$, where $x$ and $y$ need not be distinct.

Formalized by `Set.IsProductFree`, a definition declared in [MathlibExt/Algebra/Group/ProductFree.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Group/ProductFree.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/index.html#is-product-free).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sum-free sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sum-free-sets)
