---
declaration: section
origin: cited
lean: SheafTheoreticallyEmpty, StacksSheafTheoreticallyEmpty.tfae_sheafTheoreticallyEmpty, StacksSheafTheoreticallyEmpty.isIso_map_emptyPresheafTo_of_hom, IsAlmostCocontinuous, CategoryTheory.Functor.isIso_homEquiv_symm_whiskerLeft_toSheafify_of_isAlmostCocontinuous, CategoryTheory.Functor.preservesColimitsOfShape_sheafPushforwardContinuous_of_isAlmostCocontinuous, CategoryTheory.Functor.IsMorphismOfSites.preservesColimitsOfShape_pushforward_morphismOfTopoi_of_isAlmostCocontinuous
statement: formalized
proof: formalized
---

# 7.42 Almost cocontinuous functors

Section 7.42 of the Stacks Project, [Tag 04B4](https://stacks.math.columbia.edu/tag/04B4). 6 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04B5, a definition

[Tag 04B5](https://stacks.math.columbia.edu/tag/04B5) in the Stacks Project.

**`SheafTheoreticallyEmpty`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/SheafTheoreticallyEmpty.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cocontinuous/SheafTheoreticallyEmpty.lean#L28).

> **Stacks 04B5.** An object `U` of a site is *sheaf theoretically empty* if the
> sheafification of the canonical map `∅ ⟶ h_U` from the initial presheaf to the presheaf
> represented by `U` is an isomorphism of sheaves.

```lean
def SheafTheoreticallyEmpty [HasWeakSheafify J (Type v)] (U : C) : Prop
```

## Tag 04B6, a lemma

[Tag 04B6](https://stacks.math.columbia.edu/tag/04B6) in the Stacks Project.

**`StacksSheafTheoreticallyEmpty.tfae_sheafTheoreticallyEmpty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/EmptyPresheaf.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cocontinuous/EmptyPresheaf.lean#L159).

> **Stacks 04B6.**  For an object `U` of a site `(C, J)` the following are equivalent:
> (1) `U` is sheaf theoretically empty, i.e. `∅^# ⟶ h_U^#` is an isomorphism of sheaves;
> (2) every sheaf of sets has exactly one section over `U`;
> (3) `∅^#(U)` has exactly one element;
> (4) `∅^#(U)` is nonempty;
> (5) the empty sieve is a covering sieve of `U`.

```lean
theorem tfae_sheafTheoreticallyEmpty [HasWeakSheafify J (Type u)] (U : C) :
    TFAE [IsIso ((presheafToSheaf J (Type u)).map (emptyPresheafTo (yoneda.obj U))),
      ∀ F : Sheaf J (Type u), Subsingleton (F.obj.obj (op U)) ∧ Nonempty (F.obj.obj (op U)),
      Subsingleton ((sheafify J (emptyPresheaf (C := C))).obj (op U)) ∧
        Nonempty ((sheafify J (emptyPresheaf (C := C))).obj (op U)),
      Nonempty ((sheafify J (emptyPresheaf (C := C))).obj (op U)),
      (⊥ : Sieve U) ∈ J U]
```

**`StacksSheafTheoreticallyEmpty.isIso_map_emptyPresheafTo_of_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/EmptyPresheaf.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cocontinuous/EmptyPresheaf.lean#L177).

> **Stacks 04B6**, final assertion.  If `U` is sheaf theoretically empty, then so is `U'` for
> every morphism `U' ⟶ U` of `C`.

```lean
theorem isIso_map_emptyPresheafTo_of_hom [HasWeakSheafify J (Type u)] {U U' : C} (f : U' ⟶ U)
    (h : IsIso ((presheafToSheaf J (Type u)).map (emptyPresheafTo (yoneda.obj U)))) :
    IsIso ((presheafToSheaf J (Type u)).map (emptyPresheafTo (yoneda.obj U')))
```

## Tag 04B7, a definition

[Tag 04B7](https://stacks.math.columbia.edu/tag/04B7) in the Stacks Project.

**`IsAlmostCocontinuous`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/AlmostCocontinuousDefs.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cocontinuous/AlmostCocontinuousDefs.lean#L35).

> **Stacks 04B7.** A functor `u : C ⥤ D` between sites `(C, J)` and `(D, K)` is *almost
> cocontinuous* if for every object `U` of `C` and every covering sieve `S` of `u U` there is a
> covering sieve `T` of `U` such that each arrow `f : V ⟶ U` in `T` either has `u V` sheaf
> theoretically empty, or has `u f` in `S`.

```lean
def IsAlmostCocontinuous (u : C ⥤ D) (J : GrothendieckTopology C)
    (K : GrothendieckTopology D) : Prop
```

## Tag 04B8, a lemma

[Tag 04B8](https://stacks.math.columbia.edu/tag/04B8) in the Stacks Project.

**`CategoryTheory.Functor.isIso_homEquiv_symm_whiskerLeft_toSheafify_of_isAlmostCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/AlmostCocontinuousFunctors.lean, line 427](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cocontinuous/AlmostCocontinuousFunctors.lean#L427). The attribute's comment: “For `u` continuous and almost cocontinuous and `G` a presheaf of sets on `D` with `G(V)` a singleton for every sheaf theoretically empty `V`, the canonical morphism `(u^p G)^# ⟶ u^p(G^#)` is an isomorphism.”.

> **Stacks 04B8.** Let `(C, J)` and `(D, K)` be sites and let `u : C ⥤ D` be continuous and
> almost cocontinuous (Stacks 04B7). Let `G` be a presheaf of sets on `D` such that `G(V)` is a
> singleton whenever `V` is sheaf theoretically empty. Then `(u^p G)^# = u^p(G^#)`: the canonical
> morphism of sheaves `(u^p G)^# ⟶ u^s(G^#)`, the transpose under the sheafification adjunction of
> `u^p` of the unit `G ⟶ G^#`, is an isomorphism.
>
> Sheaves are of sets in the universe `max u₁ v₁` of a site whose objects lie in `Type u₁` and whose
> morphisms lie in `Type v₁`, as for Mathlib's sheafification of presheaves of types; in particular
> this covers small sites with sheaves of sets. In that setting sheafification exists on both sites
> and inverts exactly the locally bijective morphisms
> (`CategoryTheory.GrothendieckTopology.WEqualsLocallyBijective`), both by instances.

```lean
public theorem isIso_homEquiv_symm_whiskerLeft_toSheafify_of_isAlmostCocontinuous
    {C : Type u₁} [Category.{v₁} C] {D : Type u₁} [Category.{v₁} D] (u : C ⥤ D)
    (J : GrothendieckTopology C) (K : GrothendieckTopology D) [u.IsContinuous J K]
    (hu : IsAlmostCocontinuous u J K) (G : Dᵒᵖ ⥤ Type (max u₁ v₁))
    (hG : ∀ V : D, SheafTheoreticallyEmptySite K V → Nonempty (Unique (G.obj (op V)))) :
    IsIso (((sheafificationAdjunction J (Type (max u₁ v₁))).homEquiv (u.op ⋙ G)
      ((u.sheafPushforwardContinuous (Type (max u₁ v₁)) J K).obj
        ((presheafToSheaf K (Type (max u₁ v₁))).obj G))).symm
      (Functor.whiskerLeft u.op (toSheafify K G)))
```

## Tag 04B9, a lemma

[Tag 04B9](https://stacks.math.columbia.edu/tag/04B9) in the Stacks Project.

**`CategoryTheory.Functor.preservesColimitsOfShape_sheafPushforwardContinuous_of_isAlmostCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/AlmostCocontinuousFunctors.lean, line 457](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cocontinuous/AlmostCocontinuousFunctors.lean#L457). The attribute's comment: “For `u` continuous and almost cocontinuous, `u^s = u^p : Sh(D) → Sh(C)` commutes with pushouts and coequalizers, and more generally with finite connected colimits.”.

> **Stacks 04B9.** Let `(C, J)` and `(D, K)` be sites and let `u : C ⥤ D` be continuous and
> almost cocontinuous, and assume sheafification of `Type w`-valued presheaves on `(D, K)` inverts
> exactly the locally bijective morphisms. Then `u^s = u^p : Sh(D) ⥤ Sh(C)`, restriction of sheaves
> of sets along `u.op`, preserves colimits of every connected shape `I` for which `I`-shaped colimits
> of sets exist — in particular pushouts (`WalkingSpan`) and coequalizers (`WalkingParallelPair`),
> and more generally every finite connected shape.

```lean
public theorem preservesColimitsOfShape_sheafPushforwardContinuous_of_isAlmostCocontinuous
    {C : Type u₁} [Category.{v₁} C] {D : Type u₂} [Category.{v₂} D] (u : C ⥤ D)
    (J : GrothendieckTopology C) (K : GrothendieckTopology D) [u.IsContinuous J K]
    (hu : IsAlmostCocontinuous u J K) [HasWeakSheafify J (Type w)] [HasWeakSheafify K (Type w)]
    [K.WEqualsLocallyBijective (Type w)] (I : Type t) [Category.{t'} I] [IsConnected I]
    [HasColimitsOfShape I (Type w)] :
    PreservesColimitsOfShape I (u.sheafPushforwardContinuous (Type w) J K)
```

## Tag 04BA, a lemma

[Tag 04BA](https://stacks.math.columbia.edu/tag/04BA) in the Stacks Project.

**`CategoryTheory.Functor.IsMorphismOfSites.preservesColimitsOfShape_pushforward_morphismOfTopoi_of_isAlmostCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/AlmostCocontinuousFunctors.lean, line 574](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cocontinuous/AlmostCocontinuousFunctors.lean#L574). The attribute's comment: “For a morphism of sites `f : D → C` whose continuous functor `u : C → D` is almost cocontinuous, `f_*` commutes with pushouts and coequalizers, and more generally with finite connected colimits.”.

> **Stacks 04BA.** Let `f : D → C` be a morphism of sites (Stacks 00X1) associated to the
> continuous functor `u : C ⥤ D`, so that `f_* : Sh(D) ⥤ Sh(C)` is the pushforward of the morphism
> of topoi attached to `f` (Stacks 00XC), namely restriction of sheaves of sets along `u.op`. If `u`
> is almost cocontinuous (Stacks 04B7), then `f_*` preserves colimits of every connected shape whose
> colimits exist — in particular pushouts and coequalizers, which are connected shapes.

```lean
public theorem preservesColimitsOfShape_pushforward_morphismOfTopoi_of_isAlmostCocontinuous
    {C : Type w} [SmallCategory C] {D : Type w} [SmallCategory D] {J : GrothendieckTopology C}
    {K : GrothendieckTopology D} {u : C ⥤ D} (hf : u.IsMorphismOfSites J K)
    (hu : IsAlmostCocontinuous u J K) (I : Type t) [Category.{t'} I] [IsConnected I]
    [HasColimitsOfShape I (Type w)] :
    PreservesColimitsOfShape I hf.morphismOfTopoi.pushforward
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.42, Tag 04B4](https://stacks.math.columbia.edu/tag/04B4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
