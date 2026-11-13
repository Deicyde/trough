---
declaration: section
origin: cited
lean: Finset.existsUnique_of_sum_comp, Fintype.exists_perm_of_fiber, Finset.card_filter_le_of_fibers
statement: formalized
proof: formalized
---

# Fibre and double counting

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/fibre-and-double-counting/index.html).

## Unique witnesses transported by finite-sum equality

If every integer-valued sum over `T` pulls back to the corresponding sum over `s`, then a
property with a unique witness in `T` pulls back to a property with a unique witness in `s`.

Formalized by `Finset.existsUnique_of_sum_comp`, a theorem declared in [MathlibExt/Data/Finset/ExistsUniqueOfSum.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Finset/ExistsUniqueOfSum.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/fibre-and-double-counting/index.html#exists-unique-of-sum-comp).

## Labelings with equal fiber sizes differ by a permutation

Two labelings of a finite type with equally sized fibers differ by a permutation.

Formalized by `Fintype.exists_perm_of_fiber`, a theorem declared in [MathlibExt/Data/Fintype/FiberTransport.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Fintype/FiberTransport.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/fibre-and-double-counting/index.html#exists-perm-of-fiber).

## Density bounds transfer through equal-fiber maps

A density bound transfers through a map whose fibers over the target carrier all have the
same cardinality.

Formalized by `Finset.card_filter_le_of_fibers`, a theorem declared in [MathlibExt/Data/Fintype/FiberTransport.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Fintype/FiberTransport.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/fibre-and-double-counting/index.html#card-filter-le-of-fibers).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fibre and double counting](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/fibre-and-double-counting/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/elementary-enumeration/fibre-and-double-counting)
