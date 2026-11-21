---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.exists_isQuasiCompactFieldValuedPoint_iff_forall
statement: formalized
proof: formalized
---

# 100.14 Finiteness conditions and points

Section 100.14 of the Stacks Project, [Tag 0DTJ](https://stacks.math.columbia.edu/tag/0DTJ). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf).

## Tag 0DTK, a lemma

[Tag 0DTK](https://stacks.math.columbia.edu/tag/0DTK) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_isQuasiCompactFieldValuedPoint_iff_forall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactPointRepresentative.lean, line 239](https://github.com/AxiomMath/Stacks/blob/f56a316ddf7a930906d88b78d6f9a2668cffd0cf/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactPointRepresentative.lean#L239).

> **Stacks 0DTK.** Let `𝒳` be an algebraic stack over `S` and let `x` be a point of `𝒳`. Some
> morphism `Spec k ⟶ 𝒳` in the equivalence class of `x` is quasi-compact if and only if every
> morphism `Spec k ⟶ 𝒳` in the equivalence class of `x` is quasi-compact.
>
> Two field-valued representatives of `x` admit a common refinement (**Stacks 04XF**), and the
> arrow to each of them carries quasi-compactness from the refinement and to it.

```lean
theorem exists_isQuasiCompactFieldValuedPoint_iff_forall (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (x : points B S hS 𝒳.val.val 𝒳.val.isFiberedInGroupoids) :
    (∃ p : FieldValuedPoint B S hS 𝒳.val.val,
        pointClass B S hS 𝒳.val.val 𝒳.val.isFiberedInGroupoids p = x ∧
          IsQuasiCompactFieldValuedPoint B S hS 𝒳.val p) ↔
      ∀ p : FieldValuedPoint B S hS 𝒳.val.val,
        pointClass B S hS 𝒳.val.val 𝒳.val.isFiberedInGroupoids p = x →
          IsQuasiCompactFieldValuedPoint B S hS 𝒳.val p
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 100.14, Tag 0DTJ](https://stacks.math.columbia.edu/tag/0DTJ)
- [AxiomMath/Stacks at f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf)
