---
declaration: section
origin: cited
lean: MetaMathlibExt.IsAronszajnTreeAt, MetaMathlibExt.IsAronszajnTree, MetaMathlibExt.IsOmega1Tree
statement: formalized
proof: formalized
---

# Aronszajn trees

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/aronszajn-suslin-and-special-trees/aronszajn-trees/index.html).

## $\kappa$-Aronszajn tree

A κ-Aronszajn tree is a κ-tree such that there are no cofinal branch through the tree.

Formalized by `MetaMathlibExt.IsAronszajnTreeAt`, a definition declared in [MathlibExt/SetTheory/Tree/Aronszajn.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Tree/Aronszajn.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/aronszajn-suslin-and-special-trees/aronszajn-trees/index.html#kappa-aronszajn-tree).

## Aronszajn tree

An *Aronszajn tree* is a tree of height $\aleph_1}$ all of whose levels are at most countable
and which has no uncountable branches.

Formalized by `MetaMathlibExt.IsAronszajnTree`, a definition declared in [MathlibExt/SetTheory/Tree/Aronszajn.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Tree/Aronszajn.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/aronszajn-suslin-and-special-trees/aronszajn-trees/index.html#aronszajn-tree).

## $\omega_1$-tree

An *ω₁-tree* is a tree of height ω₁ all of whose levels are countable: every node has height <
ω₁, every level Lev_α(T) with α < ω₁ is nonempty, and every such level is countable.

Formalized by `MetaMathlibExt.IsOmega1Tree`, a definition declared in [MathlibExt/SetTheory/Tree/Aronszajn.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Tree/Aronszajn.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/aronszajn-suslin-and-special-trees/aronszajn-trees/index.html#omega-1-tree).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Aronszajn trees](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/aronszajn-suslin-and-special-trees/aronszajn-trees/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/SetTheory/infinitary-combinatorics/aronszajn-suslin-and-special-trees/aronszajn-trees)
