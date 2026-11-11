---
declaration: section
origin: cited
lean: SheafTheoreticallyEmpty, StacksSheafTheoreticallyEmpty.tfae_sheafTheoreticallyEmpty, StacksSheafTheoreticallyEmpty.isIso_map_emptyPresheafTo_of_hom, IsAlmostCocontinuous, isIso_sheafificationAdjunction_homEquiv_symm, CategoryTheory.Functor.preservesColimitsOfShape_sheafPushforwardContinuous_of_isAlmostCocontinuous, CategoryTheory.Functor.IsMorphismOfSites.preservesColimitsOfShape_pushforward_morphismOfTopoi_of_isAlmostCocontinuous
statement: formalized
proof: formalized
---

# 7.42 Almost cocontinuous functors

Section 7.42 of the Stacks Project, [Tag 04B4](https://stacks.math.columbia.edu/tag/04B4). 6 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04B5, a definition

[Tag 04B5](https://stacks.math.columbia.edu/tag/04B5) in the Stacks Project.

**`SheafTheoreticallyEmpty`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/SheafTheoreticallyEmpty.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/SheafTheoreticallyEmpty.lean#L28).

> **Stacks 04B5.** An object `U` of a site is *sheaf theoretically empty* if the
> sheafification of the canonical map `∅ ⟶ h_U` from the initial presheaf to the presheaf
> represented by `U` is an isomorphism of sheaves.

```lean
def SheafTheoreticallyEmpty [HasWeakSheafify J (Type v)] (U : C) : Prop
```

## Tag 04B6, a lemma

[Tag 04B6](https://stacks.math.columbia.edu/tag/04B6) in the Stacks Project.

**`StacksSheafTheoreticallyEmpty.tfae_sheafTheoreticallyEmpty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/EmptyPresheaf.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/EmptyPresheaf.lean#L159).

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

**`StacksSheafTheoreticallyEmpty.isIso_map_emptyPresheafTo_of_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/EmptyPresheaf.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/EmptyPresheaf.lean#L177).

> **Stacks 04B6**, final assertion.  If `U` is sheaf theoretically empty, then so is `U'` for
> every morphism `U' ⟶ U` of `C`.

```lean
theorem isIso_map_emptyPresheafTo_of_hom [HasWeakSheafify J (Type u)] {U U' : C} (f : U' ⟶ U)
    (h : IsIso ((presheafToSheaf J (Type u)).map (emptyPresheafTo (yoneda.obj U)))) :
    IsIso ((presheafToSheaf J (Type u)).map (emptyPresheafTo (yoneda.obj U')))
```

## Tag 04B7, a definition

[Tag 04B7](https://stacks.math.columbia.edu/tag/04B7) in the Stacks Project.

**`IsAlmostCocontinuous`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/AlmostCocontinuousDefs.lean, line 35](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/AlmostCocontinuousDefs.lean#L35).

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

**`isIso_sheafificationAdjunction_homEquiv_symm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/AlmostCocontinuousCore.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/AlmostCocontinuousCore.lean#L76).

> **Formal core of Stacks 04B8.** Suppose a sheaf `E` together with a
> presheaf morphism `η₀ : F ⟶ (sheafToPresheaf J _).obj E` satisfies the
> universal property of the sheafification of `F`: every presheaf morphism
> from `F` into the underlying presheaf of any sheaf `H` lifts uniquely
> through `η₀`. Then the canonical morphism
> `(presheafToSheaf J).obj F ⟶ E` obtained from `η₀` via the sheafification
> adjunction's `homEquiv` is an isomorphism.
>
> The Stacks 04B8 conclusion `(u^p G)^# ≅ u^p (G^#)` reduces to this
> purely formal statement once one verifies, using continuity and almost
> cocontinuity of `u` together with the "singleton on empty" hypothesis
> on `G`, that `u.sheafPushforwardContinuous` applied to `G^#` provides a
> solution to the universal property of the sheafification of `u^p G`.
> The Čech-cohomology argument establishing that universal property is
> the Stacks-side content of 04B8 and is not formalized here.

```lean
theorem isIso_sheafificationAdjunction_homEquiv_symm
    (J : GrothendieckTopology C)
    [HasWeakSheafify J (Type v)]
    (F : Cᵒᵖ ⥤ Type v)
    (E : Sheaf J (Type v))
    (η₀ : F ⟶ (sheafToPresheaf J (Type v)).obj E)
    (h_exists : ∀ (H : Sheaf J (Type v))
                  (α : F ⟶ (sheafToPresheaf J (Type v)).obj H),
        ∃ β : E ⟶ H, η₀ ≫ (sheafToPresheaf J (Type v)).map β = α)
    (h_unique : ∀ (H : Sheaf J (Type v)) (β₁ β₂ : E ⟶ H),
        η₀ ≫ (sheafToPresheaf J (Type v)).map β₁ =
          η₀ ≫ (sheafToPresheaf J (Type v)).map β₂ → β₁ = β₂) :
    IsIso (((sheafificationAdjunction J (Type v)).homEquiv _ _).symm η₀)
```

## Tag 04B9, a lemma

[Tag 04B9](https://stacks.math.columbia.edu/tag/04B9) in the Stacks Project.

**`CategoryTheory.Functor.preservesColimitsOfShape_sheafPushforwardContinuous_of_isAlmostCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/AlmostCocontinuousFunctors.lean, line 418](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/AlmostCocontinuousFunctors.lean#L418). The attribute's comment: “For `u` continuous and almost cocontinuous, `u^s = u^p : Sh(D) → Sh(C)` commutes with pushouts and coequalizers, and more generally with finite connected colimits.”.

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

**`CategoryTheory.Functor.IsMorphismOfSites.preservesColimitsOfShape_pushforward_morphismOfTopoi_of_isAlmostCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/AlmostCocontinuousFunctors.lean, line 535](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/AlmostCocontinuousFunctors.lean#L535). The attribute's comment: “For a morphism of sites `f : D → C` whose continuous functor `u : C → D` is almost cocontinuous, `f_*` commutes with pushouts and coequalizers, and more generally with finite connected colimits.”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
