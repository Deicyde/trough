---
declaration: section
origin: cited
lean: MetaMathlibExt.nonempty_mulEquiv_dihedralGroup_of_index_eq_two
statement: formalized
proof: formalized
---

# Group orders, element orders and spectra: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/index.html).

Arithmetic of finite groups through orders: cyclic numbers and groups of a given order (groups of order 10, dihedral groups from an index-two cyclic subgroup), counts of elements of each order, the spectrum (set of element orders), recognition of groups by spectrum or by order and spectrum, Thompson's type, and totient sums; conjugacy-class sizes go to Conjugacy classes.

## Dihedral groups from a cyclic subgroup of index two

Let $G$ be a finite group and let
$H$ be a cyclic subgroup of $G$ of index $2$. If $g^2 = 1$ for every element $g$ of $G$ that is
not in $H$, then $G$ is isomorphic to the dihedral group $D_n$ of order $2n$, where $n = |H|$.

Formalized by `MetaMathlibExt.nonempty_mulEquiv_dihedralGroup_of_index_eq_two`, a theorem declared in [MathlibExt/GroupTheory/SpecificGroups/Dihedral/IndexTwo.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SpecificGroups/Dihedral/IndexTwo.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/index.html#nonempty-mul-equiv-dihedral-group-of-ind).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Group orders, element orders and spectra](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/orders-and-spectra)
