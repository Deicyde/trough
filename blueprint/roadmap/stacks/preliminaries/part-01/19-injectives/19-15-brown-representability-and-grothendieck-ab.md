---
declaration: section
origin: cited
lean: Stacks.Injectives.isRepresentable_of_isGrothendieckAbelian, Stacks.Injectives.exists_exact_rightAdjoint, Stacks.Injectives.exists_exact_rightAdjoint_of_isGrothendieckAbelian
statement: formalized
proof: formalized
---

# 19.15 Brown representability and Grothendieck abelian categories

Section 19.15 of the Stacks Project, [Tag 0F5W](https://stacks.math.columbia.edu/tag/0F5W). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F5X, a lemma

[Tag 0F5X](https://stacks.math.columbia.edu/tag/0F5X) in the Stacks Project.

**`Stacks.Injectives.isRepresentable_of_isGrothendieckAbelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/BrownRepresentability.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/BrownRepresentability.lean#L454).

> **Stacks 0F5X (Brown representability for Grothendieck abelian categories).** Let `A` be a
> Grothendieck abelian category and `H : D(A) ⥤ Ab` a contravariant cohomological functor which
> transforms direct sums into products. Then `H` is representable.

```lean
public theorem isRepresentable_of_isGrothendieckAbelian (A : Type u) [Category.{v} A] [Abelian A]
    [IsGrothendieckAbelian.{max w u v} A] [HasDerivedCategory.{z} A]
    (H : (DerivedCategory A)ᵒᵖ ⥤ AddCommGrpCat.{max u v}) [H.IsHomological]
    [∀ J : Type (max w u v), PreservesLimitsOfShape (Discrete J) H] :
    (H ⋙ forget AddCommGrpCat).IsRepresentable
```

## Tag 0F5Y, a proposition

[Tag 0F5Y](https://stacks.math.columbia.edu/tag/0F5Y) in the Stacks Project.

**`Stacks.Injectives.exists_exact_rightAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/BrownRepresentability.lean, line 478](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/BrownRepresentability.lean#L478).

> **Stacks 0F5Y.** Let `A` be a Grothendieck abelian category and `D` a triangulated category.
> An exact functor `F : D(A) ⥤ D` which transforms direct sums into direct sums has an exact right
> adjoint: a functor `G`, an adjunction `F ⊣ G`, and a commutation of `G` with the shift making `G`
> triangulated.

```lean
public theorem exists_exact_rightAdjoint (A : Type u) [Category.{v} A] [Abelian A]
    [IsGrothendieckAbelian.{max w u v} A] [HasDerivedCategory.{z} A]
    (D : Type u') [Category.{max u v} D] [HasZeroObject D] [HasShift D ℤ] [Preadditive D]
    [∀ n : ℤ, (shiftFunctor D n).Additive] [Pretriangulated D]
    (F : DerivedCategory A ⥤ D) [F.CommShift ℤ] [F.IsTriangulated]
    [∀ J : Type (max w u v), PreservesColimitsOfShape (Discrete J) F] :
    ∃ (G : D ⥤ DerivedCategory A) (_ : F ⊣ G) (commShift : G.CommShift ℤ),
      let := commShift
      G.IsTriangulated
```

**`Stacks.Injectives.exists_exact_rightAdjoint_of_isGrothendieckAbelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/BrownRepresentabilityRightAdjoint.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/BrownRepresentabilityRightAdjoint.lean#L121). The attribute's comment: “A Grothendieck abelian relative to its morphism universe, direct sums indexed by it; the base `exists_exact_rightAdjoint` assumes IsGrothendieckAbelian at the object universe, which no nonzero category satisfies”.

> **[Stacks, Tag 0F5Y].** Let `A` be a Grothendieck abelian category and `D` a pretriangulated
> category. An exact functor `F : D(A) ⥤ D` which transforms direct sums into direct sums, and whose
> morphism groups `Hom(F W, Y)` are small, has an exact right adjoint: a functor `G`, an adjunction
> `F ⊣ G`, and a commutation of `G` with the shift making `G` triangulated.
>
> Here `A` is Grothendieck abelian relative to its morphism universe `v` and the direct sums are
> indexed by `Type v`. The smallness of `Hom(F W, Y)` is the source's standing convention that
> morphisms form sets, read at that universe. It is also necessary: if `F ⊣ G`, then
> `Hom(F W, Y) ≃ Hom(W, G Y)`, and the derived category of `A` is locally `Type v`-small.

```lean
theorem exists_exact_rightAdjoint_of_isGrothendieckAbelian
    (hsmall : ∀ (W : DerivedCategory A) (Y : D), Small.{v} (F.obj W ⟶ Y)) :
    ∃ (G : D ⥤ DerivedCategory A) (_ : F ⊣ G) (commShift : G.CommShift ℤ),
      letI := commShift
      G.IsTriangulated
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 19.15, Tag 0F5W](https://stacks.math.columbia.edu/tag/0F5W)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
