---
declaration: section
origin: cited
lean: Set.IsProductFree
statement: formalized
proof: formalized
---

# Sum-free sets: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/index.html).

Sets with no solution to x+y=z or similar: sum-free sets in abelian groups and intervals, counts of sum-free and maximal sum-free sets, large sum-free subsets, square-sum-free, divisor-sum-free and non-averaging sets.

## Product-free set

A set $S$ in a type $M$ with a multiplication is product-free if
$xy \notin S$ for all $x, y \in S$, where $x$ and $y$ need not be distinct.

Formalized by `Set.IsProductFree`, a definition declared in [MathlibExt/Algebra/Group/ProductFree.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Group/ProductFree.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/index.html#is-product-free).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sum-free sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/sum-free-sets)
