---
declaration: section
origin: cited
lean: AlgebraicStructureType, isTypeOfAlgebraicStructure_pointed, isTypeOfAlgebraicStructure_addCommGrpCat, isTypeOfAlgebraicStructure_grpCat, isTypeOfAlgebraicStructure_monCat, isTypeOfAlgebraicStructure_commRingCat, isTypeOfAlgebraicStructure_moduleCat, isTypeOfAlgebraicStructure_lieAlgCat
statement: formalized
proof: formalized
---

# 6.15 Algebraic structures

Section 6.15 of the Stacks Project, [Tag 007L](https://stacks.math.columbia.edu/tag/007L). 6 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 007M, a definition

[Tag 007M](https://stacks.math.columbia.edu/tag/007M) in the Stacks Project.

**`AlgebraicStructureType`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/Defs.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/Defs.lean#L58).

> A *type of algebraic structure* is a category `C` together with a functor
> `F : C ⥤ Type v` to the category of sets which is faithful, preserves all
> (small) limits, preserves filtered colimits, and reflects isomorphisms.
>
> The objects of `C` live in universe `u` and its homs in universe `v`, and the target is
> `Type v` so that the two size conditions are indexed by the same universe — see the module
> docstring.

```lean
structure AlgebraicStructureType
```

## Tag 007N, a lemma

[Tag 007N](https://stacks.math.columbia.edu/tag/007N) in the Stacks Project.

**`isTypeOfAlgebraicStructure_pointed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/Examples.lean, line 900](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/Examples.lean#L900). The attribute's comment: “(1)”.

> **Item (1).** The category of pointed sets is a type of
> algebraic structures (with the forgetful functor to `Type`).

```lean
theorem isTypeOfAlgebraicStructure_pointed :
    IsTypeOfAlgebraicStructure Pointed.{w} (forget Pointed.{w})
```

**`isTypeOfAlgebraicStructure_addCommGrpCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/Examples.lean, line 912](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/Examples.lean#L912). The attribute's comment: “(2)”.

> **Item (2).** The category of abelian groups is a type of
> algebraic structures.

```lean
theorem isTypeOfAlgebraicStructure_addCommGrpCat :
    IsTypeOfAlgebraicStructure AddCommGrpCat.{w} (forget AddCommGrpCat.{w})
```

**`isTypeOfAlgebraicStructure_grpCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/Examples.lean, line 924](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/Examples.lean#L924). The attribute's comment: “(3)”.

> **Item (3).** The category of groups is a type of algebraic
> structures.

```lean
theorem isTypeOfAlgebraicStructure_grpCat :
    IsTypeOfAlgebraicStructure GrpCat.{w} (forget GrpCat.{w})
```

**`isTypeOfAlgebraicStructure_monCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/Examples.lean, line 936](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/Examples.lean#L936). The attribute's comment: “(4)”.

> **Item (4).** The category of monoids is a type of algebraic
> structures.

```lean
theorem isTypeOfAlgebraicStructure_monCat :
    IsTypeOfAlgebraicStructure MonCat.{w} (forget MonCat.{w})
```

**`isTypeOfAlgebraicStructure_commRingCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/Examples.lean, line 949](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/Examples.lean#L949). The attribute's comment: “(5)”.

> **Item (5).** The category of commutative rings is a type of
> algebraic structures. (In the Stacks Project, a ring is a commutative ring with
> unit, so the appropriate Mathlib category is `CommRingCat`.)

```lean
theorem isTypeOfAlgebraicStructure_commRingCat :
    IsTypeOfAlgebraicStructure CommRingCat.{w} (forget CommRingCat.{w})
```

**`isTypeOfAlgebraicStructure_moduleCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/Examples.lean, line 961](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/Examples.lean#L961). The attribute's comment: “(6)”.

> **Item (6).** For any fixed commutative ring `R`, the category
> of `R`-modules is a type of algebraic structures.

```lean
theorem isTypeOfAlgebraicStructure_moduleCat (R : Type w) [CommRing R] :
    IsTypeOfAlgebraicStructure (ModuleCat.{w} R) (forget (ModuleCat.{w} R))
```

**`isTypeOfAlgebraicStructure_lieAlgCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/Examples.lean, line 973](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/Examples.lean#L973). The attribute's comment: “(7)”.

> **Item (7).** For any fixed field `K`, the category of `K`-Lie
> algebras is a type of algebraic structures.

```lean
theorem isTypeOfAlgebraicStructure_lieAlgCat (K : Type w) [Field K] :
    IsTypeOfAlgebraicStructure (LieAlgCat K) (forget (LieAlgCat K))
```

## Tag 007O, a lemma

[Tag 007O](https://stacks.math.columbia.edu/tag/007O) in the Stacks Project.

**`AlgebraicStructureType.has_terminal_and_F_terminal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/Consequences.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/Consequences.lean#L78). The attribute's comment: “(1)”.

> **Stacks 007O, Item (1).** `C` has a terminal (final) object and the value of `F` at
> the terminal object is a one-element (singleton, i.e. `Unique`) set.

```lean
theorem has_terminal_and_F_terminal :
    HasTerminal S.C ∧ Nonempty (Unique (S.F.obj (⊤_ S.C)))
```

**`AlgebraicStructureType.has_products_and_F_preserves_products`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/Consequences.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/Consequences.lean#L89). The attribute's comment: “(2)”.

> **Stacks 007O, Item (2).** `C` has all (small) products, and for every small family
> `{A i}` the canonical comparison map `F (∏ A i) ⟶ ∏ (F ∘ A)` is an isomorphism (a
> bijection of sets).

```lean
theorem has_products_and_F_preserves_products :
    HasProducts.{v} S.C ∧
      ∀ {β : Type v} (f : β → S.C)
        [HasProduct f] [HasProduct fun b => S.F.obj (f b)],
        IsIso (piComparison S.F f)
```

**`AlgebraicStructureType.has_pullbacks_and_F_preserves_pullbacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/Consequences.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/Consequences.lean#L101). The attribute's comment: “(3)”.

> **Stacks 007O, Item (3).** `C` has all fibre products (pullbacks), and the canonical
> comparison map `F (A ×_B C) ⟶ F A ×_{F B} F C` is an isomorphism (a bijection of sets).

```lean
theorem has_pullbacks_and_F_preserves_pullbacks :
    HasPullbacks S.C ∧
      ∀ {X Y Z : S.C} (f : X ⟶ Z) (g : Y ⟶ Z)
        [HasPullback f g] [HasPullback (S.F.map f) (S.F.map g)],
        IsIso (pullbackComparison S.F f g)
```

**`AlgebraicStructureType.has_equalizers_and_F_preserves_equalizers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/Consequences.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/Consequences.lean#L114). The attribute's comment: “(4)”.

> **Stacks 007O, Item (4).** `C` has all equalizers, and if `e : E ⟶ A` is the
> equalizer of `a b : A ⟶ B` in `C`, then `F e` is the equalizer of `F a, F b` in
> `Type v` (the canonical comparison map is an isomorphism).

```lean
theorem has_equalizers_and_F_preserves_equalizers :
    HasEqualizers S.C ∧
      ∀ {X Y : S.C} (f g : X ⟶ Y)
        [HasEqualizer f g] [HasEqualizer (S.F.map f) (S.F.map g)],
        IsIso (equalizerComparison f g S.F)
```

**`AlgebraicStructureType.mono_iff_F_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/Consequences.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/Consequences.lean#L129). The attribute's comment: “(5)”.

> **Stacks 007O, Item (5).** A morphism `a : A ⟶ B` in `C` is a monomorphism iff
> the underlying function `F a : F A ⟶ F B` is injective.
>
> `F` preserves pullbacks and is faithful, so `Mono a ↔ Mono (F.map a)`, and in
> `Type v`, `Mono ↔ Injective`.

```lean
theorem mono_iff_F_injective {A B : S.C} (a : A ⟶ B) :
    Mono a ↔ Function.Injective (S.F.map a)
```

**`AlgebraicStructureType.epi_of_F_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/Consequences.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/Consequences.lean#L141). The attribute's comment: “(6)”.

> **Stacks 007O, Item (6).** If the underlying function `F a : F A ⟶ F B` is
> surjective, then `a : A ⟶ B` is an epimorphism in `C`.
>
> Note: this is only a one-way implication; the converse generally fails
> (e.g. `ℤ → ℚ` is an epimorphism of rings whose underlying map is not surjective).

```lean
theorem epi_of_F_surjective {A B : S.C} (a : A ⟶ B)
    (h : Function.Surjective (S.F.map a)) : Epi a
```

**`AlgebraicStructureType.has_filtered_colimits_and_F_preserves`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/Consequences.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/Consequences.lean#L160). The attribute's comment: “(7)”.

> **Stacks 007O, Item (7).** For any filtered category `I` and any functor
> `D : I ⥤ C`, the colimit of `D` exists in `C`, and the canonical comparison map
> `colim (F ∘ D) ⟶ F (colim D)` (induced by the universal property) is an
> isomorphism (a bijection of sets).
>
> In particular this applies to sequential colimits along `ℕ`, which is a special
> case of a filtered colimit.

```lean
theorem has_filtered_colimits_and_F_preserves :
    ∀ {I : Type v} [Category.{v} I] [IsFiltered I] (D : I ⥤ S.C),
      HasColimit D ∧ HasColimit (D ⋙ S.F) ∧
        PreservesColimit D S.F
```

## Tag 007P, a lemma

[Tag 007P](https://stacks.math.columbia.edu/tag/007P) in the Stacks Project.

**`factor_through_injective_image_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/FactorThroughInjective.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/FactorThroughInjective.lean#L34). The attribute's comment: “f factors through g when F(g) is injective and Im F(f) ⊆ Im F(g)”.

> **Stacks Project, Tag 007P (Lemma 6.15.4).**
> Let `(C, F)` be a type of algebraic structure. Let `A`, `B`, `C` be objects of `C` and
> let `f : A ⟶ B`, `g : C ⟶ B`. If `F.map g` is injective and the range of `F.map f` is
> contained in the range of `F.map g`, then `f` factors through `g`: there is a morphism
> `t : A ⟶ C` with `f = t ≫ g`.

```lean
theorem factor_through_injective_image_subset
    (S : AlgebraicStructureType.{v, u})
    (A B C : S.C) (f : A ⟶ B) (g : C ⟶ B)
    (hg : Function.Injective (S.F.map g))
    (hsub : Set.range (S.F.map f) ⊆ Set.range (S.F.map g)) :
    ∃ t : A ⟶ C, f = t ≫ g
```

## Tag 007Q, an example

[Tag 007Q](https://stacks.math.columbia.edu/tag/007Q) in the Stacks Project.

**`algebraicStructure_factor_exists`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/Pullback.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/Pullback.lean#L148).

> Stacks Project Example 6.15.5 (tag 007Q).
>
> Given a type of algebraic structure `(C, F)`, objects `A, B, C, D` and morphisms
> `f : A ⟶ B`, `h : B ⟶ D`, `g : C ⟶ D`, such that:
>
> * `F(g)` is injective (`g` is injective on underlying sets); and
> * the image of `F(f ≫ h)` is contained in the image of `F(g)`
>   (here `f ≫ h : A ⟶ D` is the composite `A → B → D`, i.e. `h ∘ f`),
>
> there exists a morphism `t : A ⟶ C` making the square commute, i.e.
> `t ≫ g = f ≫ h` (equivalently `g ∘ t = h ∘ f`).

```lean
theorem algebraicStructure_factor_exists (S : AlgebraicStructureTypeBundled.{v, u, w})
    (A B C D : S.C) (f : A ⟶ B) (h : B ⟶ D) (g : C ⟶ D)
    (hg : Function.Injective (S.F.map g))
    (himg : Set.range (S.F.map (f ≫ h)) ⊆ Set.range (S.F.map g)) :
    ∃ t : A ⟶ C, t ≫ g = f ≫ h
```

## Tag 007R, an example

[Tag 007R](https://stacks.math.columbia.edu/tag/007R) in the Stacks Project.

**`pointwiseProductPresheaf_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/AlgebraicStructure/PointwiseProduct.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/AlgebraicStructure/PointwiseProduct.lean#L126).

> **Stacks 007R.** Let `C` have all small limits and let `F : C ⥤ Type v` preserve all small
> limits and reflect isomorphisms. Let `X` be a topological space and `A : X → C` a family of
> objects of `C`. Then the pointwise-product presheaf `Π`, with `Π(U) = ∏_{x ∈ U} A_x`, is a sheaf
> with values in `C`.
>
> The underlying presheaf of sets `Π ⋙ F` is naturally isomorphic to the set-valued sheaf
> `TopCat.sheafToTypes X (fun x => F (A x))` of tag 006X, so the bridge lemma
> `TopCat.Presheaf.isSheaf_iff_isSheaf_comp'` (tag 0073) makes `Π` a sheaf.

```lean
theorem pointwiseProductPresheaf_isSheaf
    {C : Type u} [Category.{v} C] [HasLimits C]
    (F : C ⥤ Type v) [F.ReflectsIsomorphisms] [PreservesLimits F]
    {X : TopCat} (A : X → C) :
    (pointwiseProductPresheaf A).IsSheaf
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.15, Tag 007L](https://stacks.math.columbia.edu/tag/007L)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
