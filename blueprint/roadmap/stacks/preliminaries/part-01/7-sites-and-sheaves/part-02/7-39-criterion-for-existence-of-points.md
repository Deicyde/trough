---
declaration: section
origin: cited
lean: CategoryTheory.GrothendieckTopology.exists_refinement_of_ne, CategoryTheory.GrothendieckTopology.exists_refinement_forall_covering_of_ne, CategoryTheory.GrothendieckTopology.hasEnoughPoints_of_exists_finite_refinement, CategoryTheory.GrothendieckTopology.hasEnoughPoints_of_coversTop_of_exists_finite_refinement
statement: formalized
proof: formalized
---

# 7.39 Criterion for existence of points

Section 7.39 of the Stacks Project, [Tag 00YN](https://stacks.math.columbia.edu/tag/00YN). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00YO, a lemma

[Tag 00YO](https://stacks.math.columbia.edu/tag/00YO) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.exists_refinement_of_ne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/CriterionForExistenceOfPoints/RefinementStep.lean, line 520](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/CriterionForExistenceOfPoints/RefinementStep.lean#L520). The attribute's comment: “The inductive step of Deligne's criterion: a cofiltered system can be refined so as to keep two germs of a separated presheaf distinct while a given section of `u'(W)` becomes covered by a given finite covering of `W`.”. References: SGA 4 VI (9.3).

> **Stacks 00YO.** Let `(C, J)` be a site, let `F` be a separated presheaf of sets on `C` and let
> `p : N ⥤ C` be a cofiltered system in `C`, with associated fibre functor
> `u'(X) = colim_j Mor(p j, X)` and stalk functor `F ↦ F_{p'} = colim_j F(p j)`. Let `s ≠ s'` be two
> germs in `F_{p'}`, represented by `a, a' : F(p j₀)`, let `{g k : Y k ⟶ W}` be a finite covering of
> the site and let `f : p j₀ ⟶ W` represent a section of `u'(W)`.
>
> Then the system can be refined — there are a cofiltered system `q : M ⥤ C`, a fully faithful
> `e : N ⥤ M` and an isomorphism `ε : e ⋙ q ≅ p` exhibiting `p` as the restriction of `q` — in such a
> way that the two germs stay distinct in `F_p` and that the image of `f` in `u(W)` lies in the image
> of `u(Y k)` for one of the members `g k : Y k ⟶ W` of the covering.

```lean
public theorem exists_refinement_of_ne {C : Type u} [Category.{v} C] (J : GrothendieckTopology C)
    {F : Cᵒᵖ ⥤ Type w} (hF : Presieve.IsSeparated J F) {N : Type u₁} [SmallCategory N]
    [IsCofiltered N] (p : N ⥤ C) (j₀ : N) (a a' : F.obj (op (p.obj j₀)))
    (haa' : ∀ (j : N) (φ : j ⟶ j₀), F.map (p.map φ).op a ≠ F.map (p.map φ).op a') {W : C}
    {ι : Type t} [Finite ι] {Y : ι → C} (g : ∀ k, Y k ⟶ W) (hg : Sieve.ofArrows Y g ∈ J W)
    [∀ (X : C) (h : X ⟶ W) (k : ι), HasPullback h (g k)] (f : p.obj j₀ ⟶ W) :
    ∃ (M : Type u₁) (_ : SmallCategory M) (_ : IsCofiltered M) (q : M ⥤ C) (e : N ⥤ M) (_ : e.Full)
      (_ : e.Faithful) (ε : e ⋙ q ≅ p),
      (∀ (i : M) (ψ : i ⟶ e.obj j₀),
          F.map (q.map ψ ≫ ε.hom.app j₀).op a ≠ F.map (q.map ψ ≫ ε.hom.app j₀).op a') ∧
        ∃ (k : ι) (i : M) (ψ : i ⟶ e.obj j₀) (h : q.obj i ⟶ Y k),
          h ≫ g k = q.map ψ ≫ ε.hom.app j₀ ≫ f
```

## Tag 00YP, a lemma

[Tag 00YP](https://stacks.math.columbia.edu/tag/00YP) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.exists_refinement_forall_covering_of_ne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/CriterionForExistenceOfPoints/UniformRefinement.lean, line 669](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/CriterionForExistenceOfPoints/UniformRefinement.lean#L669). The attribute's comment: “The main step of Deligne's criterion: a cofiltered system can be refined so as to keep two germs of a separated presheaf distinct while every section of `u'` becomes covered by every finite covering of the site.”. References: SGA 4 VI (9.2); SGA 4 VI (9.4).

> **Stacks 00YP.** Let `(C, J)` be a site in which the members of a finite covering admit fibre
> products along arbitrary morphisms to its base (`hpb`), let `F` be a separated presheaf of sets on
> `C` and let `p : N ⥤ C` be a cofiltered system in `C`, with associated fibre functor
> `u'(X) = colim_j Mor(p j, X)` and stalk functor `F ↦ F_{p'} = colim_j F(p j)`. Let `s ≠ s'` be two
> germs in `F_{p'}`, represented by `a, a' : F(p j₀)`.
>
> Then the system can be refined — there are a cofiltered system `q : M ⥤ C`, a fully faithful
> `e : N ⥤ M` and an isomorphism `ε : e ⋙ q ≅ p` exhibiting `p` as the restriction of `q` — in such a
> way that the two germs stay distinct in `F_p` and that, for every finite covering `{g k : Y k ⟶ W}`
> of the site and every section `f : p j ⟶ W` of `u'(W)`, the image of `f` in `u(W)` lies in the
> image of `u(Y k)` for one of the members `g k` of the covering. Moreover the refined index category
> is no larger than the data it is assembled from: if `C` is `w'`-small with `w'`-small hom types and
> `N` is essentially `w'`-small, then so is `M`, so the refinement can in turn be fed back into the
> construction of a point of the site and the lemma iterated.
>
> Unlike `CategoryTheory.GrothendieckTopology.exists_refinement_of_ne` (Stacks 00YO), the covering
> and the section are not fixed in advance: one refinement works for all of them at once.

```lean
public theorem exists_refinement_forall_covering_of_ne {C : Type u} [Category.{v} C] [Small.{w'} C]
    [LocallySmall.{w'} C] (J : GrothendieckTopology C) {F : Cᵒᵖ ⥤ Type w}
    (hF : Presieve.IsSeparated J F)
    (hpb :
      ∀ {W : C} {ι : Type t} [Finite ι] {Y : ι → C} (g : ∀ k, Y k ⟶ W),
        Sieve.ofArrows Y g ∈ J W → ∀ (X : C) (h : X ⟶ W) (k : ι), HasPullback h (g k))
    {N : Type u₁} [SmallCategory N] [IsCofiltered N] [EssentiallySmall.{w'} N] (p : N ⥤ C) (j₀ : N)
    (a a' : F.obj (op (p.obj j₀)))
    (haa' : ∀ (j : N) (φ : j ⟶ j₀), F.map (p.map φ).op a ≠ F.map (p.map φ).op a') :
    ∃ (M : Type (max u₁ u v)) (_ : SmallCategory M) (_ : IsCofiltered M) (_ :
      EssentiallySmall.{w'} M) (q : M ⥤ C) (e : N ⥤ M) (_ : e.Full) (_ : e.Faithful) (ε :
      e ⋙ q ≅ p),
      (∀ (i : M) (ψ : i ⟶ e.obj j₀),
          F.map (q.map ψ ≫ ε.hom.app j₀).op a ≠ F.map (q.map ψ ≫ ε.hom.app j₀).op a') ∧
        ∀ {W : C} {ι : Type t} [Finite ι] {Y : ι → C} (g : ∀ k, Y k ⟶ W),
          Sieve.ofArrows Y g ∈ J W →
            ∀ (j : N) (f : p.obj j ⟶ W),
              ∃ (k : ι) (i : M) (ψ : i ⟶ e.obj j) (h : q.obj i ⟶ Y k),
                h ≫ g k = q.map ψ ≫ ε.hom.app j ≫ f
```

## Tag 00YQ, a proposition

[Tag 00YQ](https://stacks.math.columbia.edu/tag/00YQ) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.hasEnoughPoints_of_exists_finite_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/CriterionForExistenceOfPoints/DeligneCriterion.lean, line 735](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/CriterionForExistenceOfPoints/DeligneCriterion.lean#L735). The attribute's comment: “Deligne's criterion: a site with fibre products in which every covering has a finite refinement has enough points.”. References: SGA 4 VI (9.0); SGA 4 VI (9.5), “existence of points”; SGA 2 XIV (1.9), “special case”.

> **Stacks 00YQ** (Deligne's criterion for the existence of enough points). Let `(C, J)` be a
> site in which fibre products exist and in which every covering sieve `S` of an object `X` admits a
> refinement by a finite covering — a finite family `g k : Y k ⟶ X` of morphisms of `S` which is
> again a covering of `X`. Then the site has enough points: there is a small family of points of
> `(C, J)` whose fibre functors jointly reflect isomorphisms of sheaves of sets.
>
> The source asks for all finite limits in `C`; only the fibre products of the members of a finite
> covering along an arbitrary morphism are used, whence `HasPullbacks C`.

```lean
public theorem hasEnoughPoints_of_exists_finite_refinement {C : Type u} [Category.{v} C]
    [HasPullbacks C] [Small.{w} C] [LocallySmall.{w} C] (J : GrothendieckTopology C)
    [HasSheafify J (Type w)]
    (h :
      ∀ ⦃X : C⦄ (S : Sieve X),
        S ∈ J X →
          ∃ (ι : Type) (_ : Finite ι) (Y : ι → C) (g : ∀ k, Y k ⟶ X),
            Sieve.ofArrows Y g ≤ S ∧ Sieve.ofArrows Y g ∈ J X) :
    HasEnoughPoints.{w} J
```

## Tag 0DW0, a lemma

[Tag 0DW0](https://stacks.math.columbia.edu/tag/0DW0) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.hasEnoughPoints_of_coversTop_of_exists_finite_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/CriterionForExistenceOfPoints/DeligneCriterion.lean, line 897](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/CriterionForExistenceOfPoints/DeligneCriterion.lean#L897). The attribute's comment: “A site covered by objects whose localizations satisfy Deligne's criterion has enough points.”. References: SGA 2 XIV (1.9), “special case”; SGA 4 VI (4.12), “more general”; SGA 4 VI (9.0).

> **Stacks 0DW0**. Let `(C, J)` be a site and let `U : I → C` be a family of objects, indexed by
> a `w`-small type, which covers the final object of the topos of sheaves on `C`: for every object
> `W` of `C`, the sieve of morphisms `Z ⟶ W` whose source `Z` admits a morphism to some `U i` is a
> covering sieve. Assume that each localized site `C/U i` satisfies the hypotheses of Deligne's
> criterion Stacks 00YQ: fibre products exist in `C/U i`, and every covering sieve `S` of an object
> `X` of `C/U i` admits a refinement by a finite covering, i.e. contains a finite family
> `g k : Y k ⟶ X` which is again a covering of `X`. Then `(C, J)` has enough points.
>
> The finiteness condition is needed only on the localizations, so a site none of whose coverings
> admits a finite refinement can still have enough points, as soon as it is covered by objects whose
> localizations are coherent in Deligne's sense.

```lean
public theorem hasEnoughPoints_of_coversTop_of_exists_finite_refinement {C : Type u}
    [Category.{v} C] [LocallySmall.{w} C] {J : GrothendieckTopology C} {I : Type*} [Small.{w} I]
    {U : I → C} [∀ i, HasPullbacks (Over (U i))] [∀ i, Small.{w} (Over (U i))] (hU : J.CoversTop U)
    (h :
      ∀ (i : I) ⦃X : Over (U i)⦄ (S : Sieve X),
        S ∈ (J.over (U i)) X →
          ∃ (ι : Type) (_ : Finite ι) (Y : ι → Over (U i)) (g : ∀ k, Y k ⟶ X),
            Sieve.ofArrows Y g ≤ S ∧ Sieve.ofArrows Y g ∈ (J.over (U i)) X) :
    HasEnoughPoints.{w} J
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.39, Tag 00YN](https://stacks.math.columbia.edu/tag/00YN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
