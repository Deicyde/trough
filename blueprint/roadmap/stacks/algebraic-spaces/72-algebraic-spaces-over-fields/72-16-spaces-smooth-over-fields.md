---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isRegular_of_isSmooth_over_field, AlgebraicGeometry.Space.dense_setOf_class_finiteSeparable_of_isSmooth
statement: formalized
proof: formalized
---

# 72.16 Spaces smooth over fields

Section 72.16 of the Stacks Project, [Tag 06M0](https://stacks.math.columbia.edu/tag/06M0). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06M1, a lemma

[Tag 06M1](https://stacks.math.columbia.edu/tag/06M1) in the Stacks Project.

**`AlgebraicGeometry.Space.isRegular_of_isSmooth_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothOverField.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothOverField.lean#L98).

> **Stacks 06M1.** An algebraic space over `S` which is smooth over the spectrum of a field
> is regular.

```lean
theorem isRegular_of_isSmooth_over_field (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (k : Type u) [Field k] (T : BigFppfOver B S hS)
    (hT : (BigFppfOver.toScheme B S hS).obj T = Spec (.of k))
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F)
    (f : F ⟶ yoneda.obj T) (hf : IsSmooth B S hS f) :
    HasEtaleLocalProperty B S hS F (fun X : Scheme.{u} ↦ IsRegular X)
```

## Tag 07W4, a lemma

[Tag 07W4](https://stacks.math.columbia.edu/tag/07W4) in the Stacks Project.

**`AlgebraicGeometry.Space.dense_setOf_class_finiteSeparable_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothOverField.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothOverField.lean#L132).

> **Stacks 07W4.** Let `k` be a field and let `X` be an algebraic space over `Spec k` which is
> smooth over `Spec k`. The points of `|X|` represented by a morphism `Spec k' ⟶ X` over `Spec k`
> with `k'` a finite separable extension of `k` are dense in `|X|`.

```lean
theorem dense_setOf_class_finiteSeparable_of_isSmooth
    {X : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X)
    (f : X ⟶ yoneda.obj (Over.mk (𝟙 (B.obj hk))))
    (hf : IsSmooth B (Spec (.of k)) hk f) :
    Dense {x : points B (Spec (.of k)) hk X |
      ∃ p : FieldValuedPoint B (Spec (.of k)) hk X,
        p.class B (Spec (.of k)) hk X = x ∧
          ∃ alg : Algebra k p.carrier,
            letI := alg
            Module.Finite k p.carrier ∧ Algebra.IsSeparable k p.carrier ∧
              p.toBase = Spec.map (CommRingCat.ofHom (algebraMap k p.carrier))}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 72.16, Tag 06M0](https://stacks.math.columbia.edu/tag/06M0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
