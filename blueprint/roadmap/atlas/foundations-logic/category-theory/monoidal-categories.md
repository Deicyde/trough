---
declaration: section
origin: cited
lean: CategoryTheory.MonoidalCategory.nonempty_iso_of_tensor_iso_tensorUnit
statement: formalized
proof: formalized
---

# Monoidal categories

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/CategoryTheory/monoidal-categories/index.html).

Monoidal categories equip a category with a tensor product and unit object, with braided and symmetric variants governing how tensor factors may be exchanged.

## Tensor inverses are unique up to isomorphism in braided categories

In a braided monoidal category, tensoring with the unit is cancellative
up to isomorphism: if `M ⊗ N ≅ 𝟙`, `M' ⊗ N' ≅ 𝟙`, and `M ≅ M'`, then
`N ≅ N'`.

Formalized by `CategoryTheory.MonoidalCategory.nonempty_iso_of_tensor_iso_tensorUnit`, a theorem declared in [MathlibExt/CategoryTheory/Monoidal/Braided.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/CategoryTheory/Monoidal/Braided.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/CategoryTheory/monoidal-categories/index.html#nonempty-iso-of-tensor-iso-tensor-unit).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monoidal categories](https://deicyde.github.io/atlas-lean/roadmap/CategoryTheory/monoidal-categories/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/CategoryTheory/monoidal-categories)
