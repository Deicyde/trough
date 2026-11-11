---
declaration: section
origin: cited
lean: MetaMathlibExt.IsUnionOfOmegaAntichains, MetaMathlibExt.IsSpecial
statement: formalized
proof: formalized
---

# Special partial orders

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/aronszajn-suslin-and-special-trees/special-partial-orders/index.html).

## Partial order that is a union of countably many antichains

A partial order (P, ≤) is a *union of ω antichains* if P = ⋃_{n<ω} Aₙ where each Aₙ ⊆ P is an
antichain (a set of pairwise ≤-incomparable elements).

Formalized by `MetaMathlibExt.IsUnionOfOmegaAntichains`, a definition declared in [MathlibExt/SetTheory/Tree/Special.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Tree/Special.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/aronszajn-suslin-and-special-trees/special-partial-orders/index.html#partial-order-that-is-a-union-of-countab).

## Special partial order

A partial order (α,≤) is *special* if there is a map
f : α → ℚ that is strictly increasing, i.e.\
x < y implies f(x) < f(y).  Note that f need not be injective:
nothing is required of incomparable elements.

Formalized by `MetaMathlibExt.IsSpecial`, a definition declared in [MathlibExt/SetTheory/Tree/Special.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Tree/Special.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/aronszajn-suslin-and-special-trees/special-partial-orders/index.html#special-partial-order).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Special partial orders](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/aronszajn-suslin-and-special-trees/special-partial-orders/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/SetTheory/infinitary-combinatorics/aronszajn-suslin-and-special-trees/special-partial-orders)
