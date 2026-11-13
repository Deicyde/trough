---
declaration: section
origin: cited
lean: CategoryTheory.isClosedEmbedding_componentEmbedding, CategoryTheory.isProfiniteGrp_functorAutomorphismTopology, CategoryTheory.exists_forget_fiberFunctor_contActionFintypeCat, CategoryTheory.equiv_finiteContinuousGSet, CategoryTheory.continuous_actionOnForget, CategoryTheory.canonicalHom_apply, CategoryTheory.profiniteCompletionEquiv_forgetAut, CategoryTheory.nonempty_iso_forget_of_preservesFiniteLimits_and_colimits
statement: formalized
proof: formalized
---

# 58.3 Galois categories

Section 58.3 of the Stacks Project, [Tag 0BMQ](https://stacks.math.columbia.edu/tag/0BMQ). 10 tags here are carried by 22 declarations of the repository (all in StacksFrontier) and 8 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BMR, a lemma

[Tag 0BMR](https://stacks.math.columbia.edu/tag/0BMR) in the Stacks Project.

**`CategoryTheory.isClosedEmbedding_componentEmbedding`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/AutomorphismTopology.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/AutomorphismTopology.lean#L101). The attribute's comment: “closed subgroup”.

> The componentwise map identifies the automorphism group of a set-valued functor with a
> closed subgroup of the product of the automorphism groups of its values.

```lean
public lemma isClosedEmbedding_componentEmbedding (F : C ⥤ Type w) :
    @IsClosedEmbedding (Aut F) (∀ X, Equiv.Perm (F.obj X))
      (functorAutomorphismTopology F) (automorphismProductTopology F)
      (componentEmbedding F)
```

**`CategoryTheory.isProfiniteGrp_functorAutomorphismTopology`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/AutomorphismTopology.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/AutomorphismTopology.lean#L150). The attribute's comment: “profinite group”.

> If every value of a set-valued functor is finite, its automorphism group with the topology
> induced by componentwise evaluation is a profinite group.

```lean
public lemma isProfiniteGrp_functorAutomorphismTopology (F : C ⥤ Type w)
    [∀ X, Finite (F.obj X)] :
    @Stacks.Chapter05.Tag_0BR1.IsProfiniteTop (Aut F)
      (functorAutomorphismTopology F)
```

## Tag 0BMS, an example

[Tag 0BMS](https://stacks.math.columbia.edu/tag/0BMS) in the Stacks Project.

**`CategoryTheory.exists_forget_fiberFunctor_contActionFintypeCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/FiniteGSetsForget.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/FiniteGSetsForget.lean#L72). The attribute's comment: “the forgetful functor from finite `G`-sets”. References: SGA 1 V (5.1), “partial”.

> **Stacks 0BMS**, the forgetful functor. For a topological group `G` there is a functor from
> the category of continuous actions of `G` on finite sets to finite sets which is a fibre functor,
> preserves finite limits and finite colimits, and which becomes the forgetful functor to sets after
> composing with the inclusion of finite sets into sets.

```lean
theorem exists_forget_fiberFunctor_contActionFintypeCat
    (G : Type v) [Group G] [TopologicalSpace G] :
    ∃ F : ContAction FintypeCat.{u} G ⥤ FintypeCat.{u},
      PreGaloisCategory.FiberFunctor F ∧
      PreservesFiniteLimits F ∧ PreservesFiniteColimits F ∧
      Nonempty (F ⋙ FintypeCat.incl ≅ forget (ContAction FintypeCat.{u} G))
```

**`CategoryTheory.equiv_finiteContinuousGSet`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/FiniteGSetsForget.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/FiniteGSetsForget.lean#L84). The attribute's comment: “the full subcategory of `G`-Sets on the finite objects”.

> **Stacks 0BMS**, the subcategory. The full subcategory of the category `G-Sets` of
> [Stacks, Tag 04JJ] on the finite objects is the category of continuous actions of `G` on finite
> sets.

```lean
theorem equiv_finiteContinuousGSet (G : Type u) [Group G] [TopologicalSpace G] :
    Nonempty (AlgebraicGeometry.FiniteContinuousGSet.{u, u} G ≌ ContAction FintypeCat.{u} G)
```

## Tag 0BMU, a lemma

[Tag 0BMU](https://stacks.math.columbia.edu/tag/0BMU) in the Stacks Project.

**`CategoryTheory.continuous_actionOnForget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/ProfiniteCompletion.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/ProfiniteCompletion.lean#L118). The attribute's comment: “continuity of the canonical homomorphism”.

> The canonical action homomorphism is continuous for the componentwise topology.

```lean
public theorem continuous_actionOnForget (G : Type u) [Group G]
    [TopologicalSpace G] [IsTopologicalGroup G] :
    let _ : TopologicalSpace (Aut (forget (ContAction FintypeCat.{u} G))) :=
      functorAutomorphismTopology _
    Continuous (actionOnForget G)
```

**`CategoryTheory.canonicalHom_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/ProfiniteCompletion.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/ProfiniteCompletion.lean#L153). The attribute's comment: “component action of the canonical homomorphism”.

> On every finite continuous action, the canonical homomorphism acts by the given action.

```lean
public theorem canonicalHom_apply (G : Type u) [Group G] [TopologicalSpace G]
    [IsTopologicalGroup G] (g : G) (X : ContAction FintypeCat.{u} G)
    (x : X.obj.V.obj) :
    let _ : TopologicalSpace (Aut (forget (ContAction FintypeCat.{u} G))) :=
      functorAutomorphismTopology _
    ConcreteCategory.hom (((canonicalHom G) g).asIso.hom.app X) x =
      ConcreteCategory.hom (X.obj.ρ g).asHom x
```

**`CategoryTheory.profiniteCompletionEquiv_forgetAut`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/ProfiniteCompletion.lean, line 517](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/ProfiniteCompletion.lean#L517). The attribute's comment: “profinite completion universal property”.

> The automorphism group of the forgetful functor on finite continuous `G`-sets, with its
> componentwise topology, is canonically the profinite completion of `G`.

```lean
public theorem profiniteCompletionEquiv_forgetAut
    (G : Type u) [Group G] [TopologicalSpace G] [IsTopologicalGroup G] :
    let _ : TopologicalSpace (Aut (forget (ContAction FintypeCat.{u} G))) :=
      functorAutomorphismTopology _
    let _ : IsTopologicalGroup (Aut (forget (ContAction FintypeCat.{u} G))) :=
      functorAutomorphismIsTopologicalGroup _
    IsProfiniteCompletion.{u, u + 1, w} (canonicalHom G)
```

## Tag 0BMV, a lemma

[Tag 0BMV](https://stacks.math.columbia.edu/tag/0BMV) in the Stacks Project.

**`CategoryTheory.nonempty_iso_forget_of_preservesFiniteLimits_and_colimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/Exactness.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/Exactness.lean#L156). References: SGA 1 V (5.7), “Finite-G-Sets case”.

> **Stacks Project, Tag 0BMV.** An exact set-valued functor on finite continuous actions of a
> topological group, with finite values, is naturally isomorphic to the underlying-set functor.

```lean
public theorem nonempty_iso_forget_of_preservesFiniteLimits_and_colimits
    {G : Type v} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
    (F : ContAction FintypeCat.{u} G ⥤ Type u)
    [PreservesFiniteLimits F] [PreservesFiniteColimits F]
    [∀ X, Finite (F.obj X)] :
    Nonempty (F ≅ forget (ContAction FintypeCat.{u} G))
```

## Tag 0BMW, an example

[Tag 0BMW](https://stacks.math.columbia.edu/tag/0BMW) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.PreGaloisCategory.functorToAction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.PreGaloisCategory.functorToAction#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch58.lean, line 18](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch58.lean#L18) (StacksFrontier): “the functor `X ↦ F(X)` to finite `Aut(F)`-sets”. References: SGA 1 V (5.1), “partial”.
- [`CategoryTheory.PreGaloisCategory.instTopologicalSpaceAutFunctorFintypeCat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.PreGaloisCategory.instTopologicalSpaceAutFunctorFintypeCat#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch58.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch58.lean#L20) (StacksFrontier): “the topology on `Aut(F)`”.
- [`CategoryTheory.PreGaloisCategory.instIsTopologicalGroupAutFunctorFintypeCat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.PreGaloisCategory.instIsTopologicalGroupAutFunctorFintypeCat#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch58.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch58.lean#L22) (StacksFrontier): “`Aut(F)` is a topological group”. References: SGA 1 V (4.1), “partial”.
- [`CategoryTheory.PreGaloisCategory.instCompactSpaceAutFunctorFintypeCat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.PreGaloisCategory.instCompactSpaceAutFunctorFintypeCat#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch58.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch58.lean#L24) (StacksFrontier): “`Aut(F)` is compact”.
- [`CategoryTheory.PreGaloisCategory.instT2SpaceAutFunctorFintypeCat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.PreGaloisCategory.instT2SpaceAutFunctorFintypeCat#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch58.lean, line 26](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch58.lean#L26) (StacksFrontier): “`Aut(F)` is Hausdorff”.
- [`CategoryTheory.PreGaloisCategory.instTotallyDisconnectedSpaceAutFunctorFintypeCat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.PreGaloisCategory.instTotallyDisconnectedSpaceAutFunctorFintypeCat#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch58.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch58.lean#L28) (StacksFrontier): “`Aut(F)` is totally disconnected”.
- [`CategoryTheory.PreGaloisCategory.continuousSMul_aut_fiber`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.PreGaloisCategory.continuousSMul_aut_fiber#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch58.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch58.lean#L30) (StacksFrontier): “the action of `Aut(F)` on `F(X)` is continuous”. References: SGA 1 V (4.1), “partial”.

## Tag 0BMY, a definition

[Tag 0BMY](https://stacks.math.columbia.edu/tag/0BMY) in the Stacks Project.

**`CategoryTheory.IsGaloisCategory`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/Defs.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/Defs.lean#L51).

> The Galois category axioms for a category `C` equipped with a fixed functor from `C` to
> sets.

```lean
public class IsGaloisCategory {C : Type u} [Category.{v, u} C] (F : C ⥤ Type w) : Prop
```

## Tag 0BN0, a lemma

[Tag 0BN0](https://stacks.math.columbia.edu/tag/0BN0) in the Stacks Project.

**`CategoryTheory.isInitial_iff_isEmpty_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/FiberFunctor.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/FiberFunctor.lean#L56). The attribute's comment: “initial\_iff\_empty”.

> An object of a Galois category is initial if and only if its fibre is empty.

```lean
public theorem isInitial_iff_isEmpty_fiber {C : Type u} [Category.{v, u} C]
    (F : C ⥤ Type w) [IsGaloisCategory F] (A : C) :
    Nonempty (IsInitial A) ↔ IsEmpty (F.obj A)
```

**`CategoryTheory.isTerminal_iff_unique_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/FiberFunctor.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/FiberFunctor.lean#L64). The attribute's comment: “terminal\_iff\_singleton”.

> An object of a Galois category is terminal if and only if its fibre is a singleton.

```lean
public theorem isTerminal_iff_unique_fiber {C : Type u} [Category.{v, u} C]
    (F : C ⥤ Type w) [IsGaloisCategory F] (Z : C) :
    Nonempty (IsTerminal Z) ↔ Nonempty (Unique (F.obj Z))
```

**`CategoryTheory.IsGaloisCategory.mono_iff_injective`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/FiberFunctor.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/FiberFunctor.lean#L74). The attribute's comment: “mono\_iff\_injective”.

> A morphism in a Galois category is mono if and only if its map on fibres is injective.

```lean
public lemma mono_iff_injective {C : Type u} [Category.{v, u} C] (F : C ⥤ Type w)
    [IsGaloisCategory F] {X Y : C} (f : X ⟶ Y) :
    Mono f ↔ Function.Injective (F.map f)
```

**`CategoryTheory.epi_iff_surjective_on_fiber`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/FiberFunctor.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/FiberFunctor.lean#L84). The attribute's comment: “epi\_iff\_surjective”.

> A morphism in a Galois category is an epimorphism if and only if its map on fibres is
> surjective.

```lean
public lemma epi_iff_surjective_on_fiber {C : Type u} [Category.{v, u} C]
    (F : C ⥤ Type w) [IsGaloisCategory F] {X Y : C} (f : X ⟶ Y) :
    Epi f ↔ Function.Surjective (F.map f)
```

**`CategoryTheory.fiberFunctor_faithful`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/FiberFunctor.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/FiberFunctor.lean#L94). The attribute's comment: “faithful”.

> The fibre functor of a Galois category is faithful.

```lean
public instance fiberFunctor_faithful {C : Type u} [Category.{v, u} C]
    (F : C ⥤ Type w) [IsGaloisCategory F] : F.Faithful
```

**`CategoryTheory.hom_ext_of_isConnected`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/FiberFunctor.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/FiberFunctor.lean#L119). The attribute's comment: “one\_element”.

> Two morphisms from a connected object agree if their maps on fibres agree at one point.

```lean
public lemma hom_ext_of_isConnected {C : Type u} [Category.{v, u} C]
    (F : C ⥤ Type w) [IsGaloisCategory F] {X Y : C}
    [PreGaloisCategory.IsConnected X] (a b : X ⟶ Y) (x : F.obj X)
    (h : F.map a x = F.map b x) : a = b
```

**`CategoryTheory.epi_of_connected`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/FiberFunctor.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/FiberFunctor.lean#L130). The attribute's comment: “connected\_epi”.

> Every morphism between connected objects in a Galois category is an epimorphism.

```lean
public theorem epi_of_connected {C : Type u} [Category.{v, u} C]
    (F : C ⥤ Type w) [IsGaloisCategory F] {X Y : C}
    [PreGaloisCategory.IsConnected X] [PreGaloisCategory.IsConnected Y]
    (f : X ⟶ Y) : Epi f
```

**`CategoryTheory.exists_component_maps`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/FiberFunctor.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/FiberFunctor.lean#L144). The attribute's comment: “component\_maps”.

> A map from a coproduct of connected objects to a finite coproduct factors componentwise
> through a map of indexing types.

```lean
public theorem exists_component_maps {C : Type u} [Category.{v, u} C]
    (F : C ⥤ Type w) [IsGaloisCategory F]
    {I : Type x} {J : Type y} [Finite J]
    (A : I → C) (B : J → C) (X Y : C)
    (a : (i : I) → A i ⟶ X) (b : (j : J) → B j ⟶ Y)
    (_ha : IsColimit (Cofan.mk X a)) (hb : IsColimit (Cofan.mk Y b))
    (hA : ∀ i, PreGaloisCategory.IsConnected (A i)) (f : X ⟶ Y) :
    ∃ (α : I → J) (g : (i : I) → A i ⟶ B (α i)),
      ∀ i, g i ≫ b (α i) = a i ≫ f
```

## Tag 0BN2, a lemma

[Tag 0BN2](https://stacks.math.columbia.edu/tag/0BN2) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.PreGaloisCategory.exists_hom_from_galois_of_connected`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.PreGaloisCategory.exists_hom_from_galois_of_connected#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch58.lean, line 33](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch58.lean#L33) (StacksFrontier).

## Tag 0BN3, a lemma

[Tag 0BN3](https://stacks.math.columbia.edu/tag/0BN3) in the Stacks Project.

**`Stacks.FundamentalGroup.exists_aut_app_eq_of_isConnected`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategoryTransitivity.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategoryTransitivity.lean#L51). References: SGA 1 V (5.3), “connected => transitive”.

> **Stacks Project, Tag 0BN3.** The automorphism group of the fibre functor of a Galois
> category acts transitively on the fibre of a connected object.

```lean
theorem exists_aut_app_eq_of_isConnected (F : C ⥤ Type w) [hG : IsGaloisCategory F] (X : C)
    [PreGaloisCategory.IsConnected X] (x y : F.obj X) :
    ∃ σ : Aut F, σ.asIso.hom.app X x = y
```

## Tag 0BN5, a lemma

[Tag 0BN5](https://stacks.math.columbia.edu/tag/0BN5) in the Stacks Project.

**`CategoryTheory.nonempty_fiberIso_of_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/Functoriality.lean, line 310](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/Functoriality.lean#L310). The attribute's comment: “existence of the fibre-functor isomorphism”. References: SGA 1 V (6.2), “existence of t”; SGA 1 V (6.3), “U(F')=F'∘H lies in Γ”; SGA 1 V (5.7), “more general”.

> An exact functor between Galois categories admits an isomorphism of fibre functors.

```lean
public theorem nonempty_fiberIso_of_exact
    (F : C ⥤ FintypeCat.{w}) (F' : C' ⥤ FintypeCat.{w})
    [IsGaloisCategory (setValuedFiberFunctor F)]
    [IsGaloisCategory (setValuedFiberFunctor F')]
    (H : C ⥤ C') (hH : exactFunctor C C' H) :
    Nonempty (H ⋙ F' ≅ F)
```

**`CategoryTheory.nonempty_galoisFunctorData_of_fiberIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/Functoriality.lean, line 395](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/Functoriality.lean#L395). The attribute's comment: “continuous homomorphism and 2-commutative square”.

> For every chosen isomorphism of fibre functors, transport of structure gives a continuous
> homomorphism and a 2-isomorphism between the two routes around the finite-action square.

```lean
public theorem nonempty_galoisFunctorData_of_fiberIso
    (F : C ⥤ FintypeCat.{w}) (F' : C' ⥤ FintypeCat.{w})
    (H : C ⥤ C') (t : H ⋙ F' ≅ F) :
    Nonempty (GaloisFunctorData F F' H t)
```

**`CategoryTheory.galoisFunctorData_hom_innerConjugate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/Functoriality.lean, line 453](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/Functoriality.lean#L453). The attribute's comment: “independence up to inner conjugacy”. References: SGA 1 V (6.2), “h indep. of t”.

> The homomorphisms obtained from two choices of fibre-functor isomorphism differ by an inner
> automorphism of the target automorphism group.

```lean
public theorem galoisFunctorData_hom_innerConjugate
    {F : C ⥤ FintypeCat.{w}} {F' : C' ⥤ FintypeCat.{w}} {H : C ⥤ C'}
    {t₁ t₂ : H ⋙ F' ≅ F} (d₁ : GaloisFunctorData F F' H t₁)
    (d₂ : GaloisFunctorData F F' H t₂) :
    IsInnerConjugate d₁.hom.toMonoidHom d₂.hom.toMonoidHom
```

**`CategoryTheory.nonempty_exactFunctorInducingData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/Functoriality.lean, line 490](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/GaloisCategories/Functoriality.lean#L490). The attribute's comment: “converse construction”. References: SGA 1 V (6.2), “converse direction”; SGA 1 V (6.3), “essential surjectivity”.

> Every continuous homomorphism between the automorphism groups of two Galois fibre functors is
> induced by an exact functor and an isomorphism of fibre functors.

```lean
public theorem nonempty_exactFunctorInducingData
    (F : C ⥤ FintypeCat.{w}) (F' : C' ⥤ FintypeCat.{w})
    [IsGaloisCategory (setValuedFiberFunctor F)]
    [IsGaloisCategory (setValuedFiberFunctor F')]
    (h : Aut F' →ₜ* Aut F) :
    Nonempty (ExactFunctorInducingData F F' h)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.3, Tag 0BMQ](https://stacks.math.columbia.edu/tag/0BMQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
