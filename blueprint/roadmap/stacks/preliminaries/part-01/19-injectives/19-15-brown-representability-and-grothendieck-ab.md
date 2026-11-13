---
declaration: section
origin: cited
lean: Stacks.Injectives.isRepresentable_of_isHomological_of_isGrothendieckAbelian, Stacks.Injectives.exists_exact_rightAdjoint_of_isGrothendieckAbelian
statement: formalized
proof: formalized
---

# 19.15 Brown representability and Grothendieck abelian categories

Section 19.15 of the Stacks Project, [Tag 0F5W](https://stacks.math.columbia.edu/tag/0F5W). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0F5X, a lemma

[Tag 0F5X](https://stacks.math.columbia.edu/tag/0F5X) in the Stacks Project.

**`Stacks.Injectives.isRepresentable_of_isHomological_of_isGrothendieckAbelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/BrownRepresentability.lean, line 469](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Injectives/BrownRepresentability.lean#L469). The attribute's comment: “Brown representability: a contravariant cohomological functor D(A) → Ab, A a Grothendieck abelian category, which transforms direct sums into products is representable”.

> **Brown representability for Grothendieck abelian categories**, with the Grothendieck
> condition `IsGrothendieckAbelian.{v} A` in the universe `v` of the morphisms of `A`: for a
> Grothendieck abelian category `A`, a contravariant cohomological functor
> `H : D(A)ᵒᵖ ⥤ AddCommGrpCat.{v}` which transforms direct sums indexed by `Type v` into products
> is representable.
>
> This is the statement of [Stacks, Tag 0F5X] for every ordinary Grothendieck abelian category,
> e.g. `ModuleCat.{v} R`. The model of `D(A)` is arbitrary; in the model with morphisms in `Type v`
> (which exists by `hasDerivedCategory_of_isGrothendieckAbelian`) the functors
> `Hom(-, X) = preadditiveYoneda.obj X` themselves satisfy the hypotheses.

```lean
public theorem isRepresentable_of_isHomological_of_isGrothendieckAbelian (A : Type u)
    [Category.{v} A] [Abelian A] [IsGrothendieckAbelian.{v} A] [HasDerivedCategory.{z} A]
    (H : (DerivedCategory A)ᵒᵖ ⥤ AddCommGrpCat.{v}) [H.IsHomological]
    [∀ J : Type v, PreservesLimitsOfShape (Discrete J) H] :
    (H ⋙ forget AddCommGrpCat).IsRepresentable
```

## Tag 0F5Y, a proposition

[Tag 0F5Y](https://stacks.math.columbia.edu/tag/0F5Y) in the Stacks Project.

**`Stacks.Injectives.exists_exact_rightAdjoint_of_isGrothendieckAbelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/BrownRepresentabilityRightAdjoint.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Injectives/BrownRepresentabilityRightAdjoint.lean#L121). The attribute's comment: “A Grothendieck abelian relative to its morphism universe v, direct sums indexed by Type v, Hom(F W, Y) Type v-small (the source's convention that morphisms form sets); D may be any pretriangulated category”.

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
