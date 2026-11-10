---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSpaceThickening.firstOrderExtensionAction, CategoryTheory.Abelian.YonedaExtension, AlgebraicGeometry.RingedSpaceThickening.ExtensionPair.extensionAction_naturality, AlgebraicGeometry.RingedSpaceThickening.ExtensionPair.exists_compatibleMap_translate, AlgebraicGeometry.RingedSpaceThickening.ExtensionPair.existsUnique_translate, AlgebraicGeometry.RingedSpaceThickening.mapLiftingObstruction, AlgebraicGeometry.RingedSpaceThickening.extensionClassesWithAction_principalHomogeneous, AlgebraicGeometry.RingedSpaceThickening.exists_extClass_add_of_essImage
statement: formalized
proof: formalized
---

# 91.4 Modules on first order thickenings of ringed spaces

Section 91.4 of the Stacks Project, [Tag 08L3](https://stacks.math.columbia.edu/tag/08L3). 12 tags here are carried by 38 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08L4, an equation

[Tag 08L4](https://stacks.math.columbia.edu/tag/08L4) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.firstOrderExtensionAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/ModuleExtension.lean, line 616](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/ModuleExtension.lean#L616). The attribute's comment: “the canonical map”.

> **Stacks Project, Tag 08L4.** The canonical map `c_{ℱ'} : i^* ℐ ⊗_{𝒪_X} ℱ ⟶ 𝒦` of an
> extension `0 ⟶ i_* 𝒦 ⟶ ℱ' ⟶ i_* ℱ ⟶ 0` of `𝒪_{X'}`-modules across a first order thickening
> `i`.
>
> The bundled equation is the local lifting characterisation from the source: on an open set of
> `X'` over which a section `s` of `i_* ℱ` lifts to a section `s'` of `ℱ'`, the image in `ℱ'` of
> `c_{ℱ'}(a ⊗ s)` is the scalar multiple `a · s'`.

```lean
noncomputable def firstOrderExtensionAction
    (F K : SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} ⟨X.presheaf, X.IsSheaf⟩))
        (hi : IsFirstOrderThickening i)
    (E : CategoryTheory.Abelian.YonedaExtension
      ((modulePushforward i).obj F) ((modulePushforward i).obj K) 0) :
    { c : (((Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u}
        ⟨((X)).presheaf, ((X)).IsSheaf⟩).obj ((idealSheafPullback i))).obj (F)) ⟶ K //
      ∀ (U : Opens X') (a : (AlgebraicGeometry.SheafOfModules.idealSheaf i).val.obj (op U))
        (s : ((modulePushforward i).obj F).val.obj (op U)) (s' : E.Z.left.val.obj (op U)),
        (E.g.val.app (op U)).hom s' = s →
          (E.f.val.app (op U)).hom
              ((((modulePushforward i).map c).val.app (op U)).hom
                (((extensionTensorComparison i F).val.app (op U)).hom
                  (toTensorSheafSection X' (AlgebraicGeometry.SheafOfModules.idealSheaf i)
                    ((modulePushforward i).obj F) (op U)
                    (a ⊗ₜ[X'.presheaf.obj (op U)] s)))) =
            (show ((Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u}
                ⟨X'.presheaf, X'.IsSheaf⟩).obj.obj (op U) : Type u) from
              ((idealSheafι i).val.app (op U)).hom a) • s' }
```

Declarations registered for the tag:

- [`CategoryTheory.Abelian.YonedaExtension`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/ExtAndYonedaExtensions.lean#L82), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/RingedSpaceThickening/ModuleExtension.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/ModuleExtension.lean#L122) (StacksFrontier): “the short exact sequence”.

## Tag 08L5, a lemma

[Tag 08L5](https://stacks.math.columbia.edu/tag/08L5) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.ExtensionPair.extensionAction_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/ExtensionActionNaturality.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/ExtensionActionNaturality.lean#L249). The attribute's comment: “part (1): compatibility of the canonical maps”.

> **Stacks Project, Tag 08L5**, part (1). If the middle terms of two extensions across a
> first order thickening are linked by a map `φ'` compatible with `φ : ℱ ⟶ 𝒢` and `ψ : 𝒦 ⟶ ℒ`,
> then the canonical maps of the two extensions commute with `1 ⊗ φ` and `ψ`.

```lean
theorem extensionAction_naturality (S : ExtensionPair.{u}) (c : CompatibleMap S) :
    (firstOrderExtensionAction S.i S.F S.K S.firstOrder S.firstExtension).val ≫ S.kernelMap =
      ((Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor ⟨((S.X)).presheaf, ((S.X)).IsSheaf⟩)).map (((𝟙 (idealSheafPullback S.i)), S.quotientMap) : (_, _) ⟶ (_, _))) ≫
        (firstOrderExtensionAction S.i S.G S.L S.firstOrder S.secondExtension).val
```

**`AlgebraicGeometry.RingedSpaceThickening.ExtensionPair.exists_compatibleMap_translate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/ExtensionMaps.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/ExtensionMaps.lean#L143). The attribute's comment: “the action on compatible maps”.

> **Stacks Project, Tag 08L5.** Translating a compatible map `φ'` by a map `α : ℱ ⟶ ℒ`, that
> is adding the composite `ℱ' ⟶ i_* ℱ ⟶ i_* ℒ ⟶ 𝒢'`, again gives a compatible map. This is the
> action of `Hom_{𝒪_X}(ℱ, ℒ)` on the set of compatible maps.

```lean
theorem exists_compatibleMap_translate (c : CompatibleMap S) (α : S.F ⟶ S.L) :
    ∃ d : CompatibleMap S,
      d.hom = c.hom +
        S.firstExtension.g ≫ (modulePushforward S.i).map α ≫ S.secondExtension.f
```

**`AlgebraicGeometry.RingedSpaceThickening.ExtensionPair.existsUnique_translate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/ExtensionMaps.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/ExtensionMaps.lean#L190). The attribute's comment: “freeness and transitivity of the action”.

> **Stacks Project, Tag 08L5.** Any two compatible maps differ by a unique
> `α : ℱ ⟶ ℒ`. Together with `exists_compatibleMap_translate` this says that the set of
> compatible maps is, when nonempty, a principal homogeneous space under
> `Hom_{𝒪_X}(ℱ, ℒ)`.

```lean
theorem existsUnique_translate (c d : CompatibleMap S) :
    ∃! α : S.F ⟶ S.L,
      d.hom = c.hom +
        S.firstExtension.g ≫ (modulePushforward S.i).map α ≫ S.secondExtension.f
```

## Tag 08L6, a lemma

[Tag 08L6](https://stacks.math.columbia.edu/tag/08L6) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.mapLiftingObstruction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/LiftingObstruction.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/LiftingObstruction.lean#L155). The attribute's comment: “the obstruction class and its vanishing criterion”.

> The obstruction `o(φ, ψ) ∈ Ext¹_{𝒪_X}(ℱ, ℒ)` to lifting a pair of maps `φ : ℱ ⟶ 𝒢` and
> `ψ : 𝒦 ⟶ ℒ`, compatible with the canonical maps of two extensions across a first order
> thickening, to a map of the extensions themselves: the class vanishes exactly when an
> `𝒪_{X'}`-module map `φ' : ℱ' ⟶ 𝒢'` inducing `ψ` on kernels and `φ` on quotients exists.

```lean
noncomputable def mapLiftingObstruction
    [HasExt (SheafOfModules.{u} (structureSheafRing X))]
    [HasDerivedCategory (SheafOfModules.{u} (structureSheafRing X))]
    (hi : IsFirstOrderThickening i) (F K G L : SheafOfModules.{u} (structureSheafRing X))
    (E : CategoryTheory.Abelian.YonedaExtension
      ((modulePushforward i).obj F) ((modulePushforward i).obj K) 0)
    (E' : CategoryTheory.Abelian.YonedaExtension
      ((modulePushforward i).obj G) ((modulePushforward i).obj L) 0)
    (φ : F ⟶ G) (ψ : K ⟶ L)
    (hcompat : (firstOrderExtensionAction i F K hi E).val ≫ ψ =
      ((Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor
          ⟨((X)).presheaf, ((X)).IsSheaf⟩)).map (((𝟙 (idealSheafPullback i)), φ) :
          ((idealSheafPullback i), F) ⟶ ((idealSheafPullback i), G))) ≫
        (firstOrderExtensionAction i G L hi E').val) :
    { o : CategoryTheory.Abelian.zExt F L 1 //
      o = 0 ↔ ∃ φ' : E.Z.left ⟶ E'.Z.left,
        E.f ≫ φ' = (modulePushforward i).map ψ ≫ E'.f ∧
          φ' ≫ E'.g = E.g ≫ (modulePushforward i).map φ }
```

## Tag 08L7, a lemma

[Tag 08L7](https://stacks.math.columbia.edu/tag/08L7) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.extensionClassesWithAction_principalHomogeneous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/ExtensionClassesPrincipalHomogeneous.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/ExtensionClassesPrincipalHomogeneous.lean#L83). The attribute's comment: “the whole lemma, for a first order thickening of ringed spaces: the isomorphism classes of extensions as in 08L4 with `c_{ℱ'} = c`, represented by their classes in `Ext¹_{𝒪_{X'}}(i_* ℱ, i_* 𝒦)`, form a principal homogeneous space under `Ext¹_{𝒪_X}(ℱ, 𝒦)` acting through `i_*` by Baer sum”.

> **Stacks 08L7.** Let `i : (X, 𝒪_X) ⟶ (X', 𝒪_{X'})` be a first order thickening of ringed
> spaces, `ℱ`, `𝒦` two `𝒪_X`-modules and `c : ℐ ⊗_{𝒪_X} ℱ ⟶ 𝒦` an `𝒪_X`-linear map. The
> isomorphism classes of extensions `0 ⟶ i_* 𝒦 ⟶ ℱ' ⟶ i_* ℱ ⟶ 0` of `𝒪_{X'}`-modules with
> `c_{ℱ'} = c` (the set `extensionClassesWithAction i F K hi c ⊆ Ext¹_{𝒪_{X'}}(i_* ℱ, i_* 𝒦)`)
> form a principal homogeneous space under `Ext¹_{𝒪_X}(ℱ, 𝒦)`, acting by `ξ • η = η + i_* ξ`:
>
> * the action preserves the set;
> * it is an action of the group `Ext¹_{𝒪_X}(ℱ, 𝒦)`: `0` acts trivially and `ξ + ξ'` acts as
>   `ξ` followed by `ξ'`;
> * it is simply transitive: any two elements `η`, `η'` of the set satisfy `η' = η + i_* ξ` for
>   exactly one `ξ ∈ Ext¹_{𝒪_X}(ℱ, 𝒦)`.
>
> So as soon as the set is nonempty (the source's hypothesis that some sequence (08L4) with
> `c_{ℱ'} = c` exists, `hc`), every point `η₀` of it identifies it with `Ext¹_{𝒪_X}(ℱ, 𝒦)` via
> `ξ ↦ η₀ + i_* ξ`.

```lean
theorem extensionClassesWithAction_principalHomogeneous
    {X X' : RingedSpace.{u, u}} (i : X ⟶ X')
    (hi : AlgebraicGeometry.RingedSpaceThickening.IsFirstOrderThickening i)
    (F K : SheafOfModules.{u} (structureSheafRing X))
    [HasExt.{e} (SheafOfModules.{u} (structureSheafRing X))]
    [HasExt.{e} (SheafOfModules.{u} (structureSheafRing X'))]
    (c : (((Stacks.SheafOfModules.Tensor.sheafTensor ⟨((X)).presheaf, ((X)).IsSheaf⟩).obj
      ((idealSheafPullback i))).obj (F)) ⟶ K)
    (hc : ∃ E : CategoryTheory.Abelian.YonedaExtension
        ((modulePushforward i).obj F) ((modulePushforward i).obj K) 0,
      (firstOrderExtensionAction i F K hi E).val = c) :
    haveI := preservesFiniteColimits_modulePushforward i hi.1
    haveI := preservesFiniteLimits_modulePushforward i
    (extensionClassesWithAction.{e} i F K hi c).Nonempty ∧
      (∀ η ∈ extensionClassesWithAction.{e} i F K hi c, ∀ ξ : Abelian.Ext.{e} F K 1,
        η + ξ.mapExactFunctor (modulePushforward i) ∈ extensionClassesWithAction.{e} i F K hi c) ∧
      (∀ η : Abelian.Ext.{e} ((modulePushforward i).obj F) ((modulePushforward i).obj K) 1,
        η + (0 : Abelian.Ext.{e} F K 1).mapExactFunctor (modulePushforward i) = η ∧
          ∀ ξ ξ' : Abelian.Ext.{e} F K 1,
            η + (ξ + ξ').mapExactFunctor (modulePushforward i) =
              (η + ξ.mapExactFunctor (modulePushforward i)) +
                ξ'.mapExactFunctor (modulePushforward i)) ∧
      ∀ η ∈ extensionClassesWithAction.{e} i F K hi c,
        ∀ η' ∈ extensionClassesWithAction.{e} i F K hi c,
          ∃! ξ : Abelian.Ext.{e} F K 1, η + ξ.mapExactFunctor (modulePushforward i) = η'
```

**`AlgebraicGeometry.RingedSpaceThickening.exists_extClass_add_of_essImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/ExtensionClassification.lean, line 666](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/ExtensionClassification.lean#L666). The attribute's comment: “the action of `Ext¹_{𝒪_X}(ℱ, 𝒦)`: adding an extension of `𝒪_X`-modules, read on `X'` as one whose middle term is a direct image, does not change the canonical map. SCOPE: this clause only; the simple transitivity of the action is `existsUnique_extClass_sub_of_firstOrderExtensionAction_eq`, and the identification of the subgroup of such classes with `Ext¹_{𝒪_X}(ℱ, 𝒦)` itself is not formalized here”.

> **Stacks 08L7, the action.** Adding to an extension one whose middle term is a direct
> image does not change the canonical map: such an extension has vanishing canonical map
> (**Stacks 08KS**) and the canonical map is additive for Baer sums
> (`AlgebraicGeometry.RingedSpaceThickening.exists_baerSum_firstOrderExtensionAction`).
>
> This is the source's "conversely, given such an extension `ℰ` we can add the extension `ℰ` to
> the `𝒪_{X'}`-extension `ℱ'` without affecting the map `c_{ℱ'}`". By **Stacks 08KS** the
> extensions whose middle term is a direct image are exactly the extensions of `𝒪_X`-modules,
> which is how `Ext¹_{𝒪_X}(ℱ, 𝒦)` acts.

```lean
theorem exists_extClass_add_of_essImage (hi : IsFirstOrderThickening i)
    (E₀ D : CategoryTheory.Abelian.YonedaExtension
      ((modulePushforward i).obj F) ((modulePushforward i).obj K) 0)
    (hD : (modulePushforward i).essImage D.Z.left) :
    ∃ E : CategoryTheory.Abelian.YonedaExtension
        ((modulePushforward i).obj F) ((modulePushforward i).obj K) 0,
      (CategoryTheory.Abelian.YonedaExtension.shortExact E).extClass =
          (CategoryTheory.Abelian.YonedaExtension.shortExact E₀).extClass +
            (CategoryTheory.Abelian.YonedaExtension.shortExact D).extClass ∧
        (firstOrderExtensionAction i F K hi E).val =
          (firstOrderExtensionAction i F K hi E₀).val
```

**`AlgebraicGeometry.RingedSpaceThickening.existsUnique_extClass_sub_of_firstOrderExtensionAction_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/ExtensionClassification.lean, line 693](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/ExtensionClassification.lean#L693). The attribute's comment: “simple transitivity: two extensions with the same canonical map differ by the class of exactly one extension whose middle term is a direct image, i.e. of an extension of `𝒪_X`-modules. SCOPE: this clause only; the identification of the group of such classes with `Ext¹_{𝒪_X}(ℱ, 𝒦)` itself is not formalized here”.

> **Stacks 08L7, simple transitivity.** Two extensions across the thickening with the same
> canonical map differ, in `Ext¹_{𝒪_{X'}}(i_* ℱ, i_* 𝒦)`, by the class of exactly one extension
> whose middle term is a direct image — hence, by **Stacks 08KS**, by the class of an extension of
> `𝒪_X`-modules.
>
> This is the source's "the difference is an extension `0 → 𝒦 → ℰ → ℱ → 0` where `ℰ` is
> annihilated by `ℐ`, hence is an extension of `𝒪_X`-modules". Uniqueness is uniqueness of a
> difference in the group `Ext¹_{𝒪_{X'}}(i_* ℱ, i_* 𝒦)`.

```lean
theorem existsUnique_extClass_sub_of_firstOrderExtensionAction_eq (hi : IsFirstOrderThickening i)
    (E₀ E : CategoryTheory.Abelian.YonedaExtension
      ((modulePushforward i).obj F) ((modulePushforward i).obj K) 0)
    (h : (firstOrderExtensionAction i F K hi E).val =
      (firstOrderExtensionAction i F K hi E₀).val) :
    ∃! ξ : CategoryTheory.Abelian.Ext.{w}
        ((modulePushforward i).obj F) ((modulePushforward i).obj K) 1,
      (CategoryTheory.Abelian.YonedaExtension.shortExact E).extClass =
          (CategoryTheory.Abelian.YonedaExtension.shortExact E₀).extClass + ξ ∧
        ∃ D : CategoryTheory.Abelian.YonedaExtension
            ((modulePushforward i).obj F) ((modulePushforward i).obj K) 0,
          (CategoryTheory.Abelian.YonedaExtension.shortExact D).extClass = ξ ∧
            (modulePushforward i).essImage D.Z.left
```

**`AlgebraicGeometry.RingedSpaceThickening.existsUnique_ext_mapExactFunctor_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/FlatLift.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/FlatLift.lean#L295). The attribute's comment: “the identification of the group of classes whose extensions have a direct image as middle term with `Ext¹_{𝒪_X}(ℱ, 𝒦)` itself: such a class is `i_*` of exactly one class on `X`. SCOPE: this clause only; the action of those classes is `exists_extClass_add_of_essImage` and the simple transitivity is `existsUnique_extClass_sub_of_firstOrderExtensionAction_eq`”.

> The classes in `Ext¹_{𝒪_{X'}}(i_* ℱ, i_* 𝒦)` whose extensions have a direct image as middle
> term are exactly the images of `Ext¹_{𝒪_X}(ℱ, 𝒦)` under `i_*`, each attained by exactly one
> class.

```lean
theorem existsUnique_ext_mapExactFunctor_eq (hi : IsThickening i)
    (ξ' : CategoryTheory.Abelian.Ext.{w}
      ((modulePushforward i).obj F) ((modulePushforward i).obj K) 1)
    (h : ∃ D : CategoryTheory.Abelian.YonedaExtension
        ((modulePushforward i).obj F) ((modulePushforward i).obj K) 0,
      (CategoryTheory.Abelian.YonedaExtension.shortExact D).extClass = ξ' ∧
        (modulePushforward i).essImage D.Z.left) :
    ∃! ξ : CategoryTheory.Abelian.Ext.{w} F K 1,
      ξ.mapExactFunctor (modulePushforward i) = ξ'
```

## Tag 08L8, a lemma

[Tag 08L8](https://stacks.math.columbia.edu/tag/08L8) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.extensionExistenceObstruction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/ExistenceObstruction.lean, line 1055](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/ExistenceObstruction.lean#L1055).

> **Stacks Project, Tag 08L8.** The obstruction `o(ℱ, 𝒦, c) ∈ Ext²_{𝒪_X}(ℱ, 𝒦)` to the
> existence of an extension of `𝒪_{X'}`-modules `0 ⟶ i_* 𝒦 ⟶ ℱ' ⟶ i_* ℱ ⟶ 0` as in Tag 08L4 whose
> canonical map `c_{ℱ'}` is a prescribed `𝒪_X`-linear map `c : ℐ ⊗_{𝒪_X} ℱ ⟶ 𝒦`.
>
> The class is `AlgebraicGeometry.RingedSpaceThickening.obstructionClass`, and the bundled property
> is the content of the lemma: it vanishes exactly when such an extension exists.

```lean
noncomputable def extensionExistenceObstruction
    [HasExt (SheafOfModules.{u} (structureSheafRing X))]
    [HasDerivedCategory (SheafOfModules.{u} (structureSheafRing X))]
    (hi : IsFirstOrderThickening i) (F K : SheafOfModules.{u} (structureSheafRing X))
    (c : (((Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u} ⟨((X)).presheaf, ((X)).IsSheaf⟩).obj ((idealSheafPullback i))).obj (F)) ⟶ K) :
    { o : CategoryTheory.Abelian.zExt F K 2 //
      o = 0 ↔ ∃ E : CategoryTheory.Abelian.YonedaExtension
          ((modulePushforward i).obj F) ((modulePushforward i).obj K) 0,
        (firstOrderExtensionAction i F K hi E).val = c }
```

## Tag 08L9, a remark

[Tag 08L9](https://stacks.math.columbia.edu/tag/08L9) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.structureSheafSplitEpi`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean#L345). The attribute's comment: “a trivialization splits the structure-sheaf map”.

> **Stacks 08L9.** A trivialization of a thickening splits its structure-sheaf map: the
> structure-sheaf map `𝒪_X ⟶ π_* 𝒪_{X'}` of the retraction, reindexed along
> `AlgebraicGeometry.RingedSpaceThickening.retraction_opens_obj`, is a section of
> `i^♯ : 𝒪_{X'} ⟶ i_* 𝒪_X`.
>
> This is the step the source phrases as "using `π^♯` to split the surjection
> `𝒪_{X'} ⟶ 𝒪_X`". It is the converse of `Deformation.RingThickening.retractionFromSplitting`,
> and it supplies the `CategoryTheory.SplitMono` that
> `Deformation.RingThickening.splittingFromTrivialization` takes as a hypothesis — so the two
> together, and neither alone, give the source's "given `π` we obtain a splitting".

```lean
noncomputable def structureSheafSplitEpi : SplitEpi i.hom.c
```

**`AlgebraicGeometry.RingedSpaceThickening.trivializedThickeningEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/TrivializedThickeningEquivalence.lean, line 946](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/TrivializedThickeningEquivalence.lean#L946). The attribute's comment: “the category of trivialized first order thickenings of (X, 𝒪\_X) is equivalent to the category of 𝒪\_X-modules; morphisms of thickenings run in the geometric direction (X'₁ ⟶ X'₂ of ringed spaces, Stacks 08LD), so the module side carries ᵒᵖ”.

> The category of trivialized first order thickenings of a ringed space `(X, 𝒪_X)` is
> equivalent to the opposite of the category of `𝒪_X`-modules.
>
> A trivialization `π` of a first order thickening `i : X ⟶ X'` splits the surjection
> `𝒪_{X'} ⟶ 𝒪_X`, giving `𝒪_{X'} = 𝒪_X ⊕ ℐ` as sheaves of algebras on `X`, and conversely such a
> splitting determines `π`. The equivalence sends an `𝒪_X`-module `𝒢` to the trivial square-zero
> extension `(X, 𝒪_X ⋉ 𝒢)` with the zero section as trivialization, and a trivialized thickening
> back to its ideal read along the trivialization.
>
> It is contravariant for the source's own convention for morphisms: `TrivializedThickening X`
> has its Hom in the geometric direction, a morphism of thickenings of `(X, 𝒪_X)` being a
> morphism `X'₁ ⟶ X'₂` of ringed spaces (Stacks 08LD), and that is a morphism
> `𝒪_{X'₂} ⟶ 𝒪_{X'₁}` of sheaves of algebras on `X`, hence a morphism `ℐ₂ ⟶ ℐ₁` of the ideals
> (Stacks 08LC).

```lean
noncomputable def trivializedThickeningEquivalence (X : RingedSpace.{u, u}) :
    (SheafOfModules.{u} (structureSheafRing X))ᵒᵖ ≌ TrivializedThickening X
```

**`Deformation.RingThickening.splittingFromTrivialization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingThickening/TrivialThickening.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingThickening/TrivialThickening.lean#L126). The attribute's comment: “splitting\_from\_trivialization”. References: EGA 0 (18.2.3), “special case”.

> A trivialization identifies a first order thickening with the trivial square-zero extension
> by its kernel ideal.

```lean
noncomputable def splittingFromTrivialization
    (split : A ⟶ A') (π : SplitMono split)
    (h_sq : ∀ U : C, RingHom.ker (π.retraction.app U).hom ^ 2 = ⊥) :
  PresheafTrivialSquareZeroEquiv A' A π.retraction split
```

**`Deformation.RingThickening.retractionFromSplitting`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingThickening/TrivialThickening.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingThickening/TrivialThickening.lean#L174). The attribute's comment: “trivialization\_from\_splitting”.

> The section of the structure-sheaf map, transported along the inverse homeomorphism of the
> base map, defines a morphism of ringed spaces in the opposite direction.

```lean
noncomputable abbrev retractionFromSplitting {X X' : RingedSpace.{u, v}}
    (i : X ⟶ X') [IsIso i.hom.base]
    (splitting : SplitEpi i.hom.c) : X' ⟶ X
```

**`Deformation.RingThickening.retractionFromSplitting_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingThickening/TrivialThickening.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingThickening/TrivialThickening.lean#L183). The attribute's comment: “trivialization\_from\_splitting”.

> The morphism induced by a splitting of the structure-sheaf map retracts the original
> morphism.

```lean
theorem retractionFromSplitting_comp {X X' : RingedSpace.{u, v}}
    (i : X ⟶ X') [IsIso i.hom.base]
    (splitting : SplitEpi i.hom.c) :
    i ≫ retractionFromSplitting i splitting = 𝟙 X
```

Declarations registered for the tag:

- [`CategoryTheory.SplitMono`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.SplitMono#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/RingThickening/TrivialThickening.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingThickening/TrivialThickening.lean#L58) (StacksFrontier): “trivial\_thickening\_and\_trivialization”.
- [`CategoryTheory.IsSplitMono`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.IsSplitMono#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/RingThickening/TrivialThickening.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingThickening/TrivialThickening.lean#L59) (StacksFrontier): “trivial\_thickening\_and\_trivialization”. References: SGA 4 I (10.6).

## Tag 08LA, an equation

[Tag 08LA](https://stacks.math.columbia.edu/tag/08LA) in the Stacks Project.

Declarations registered for the tag:

- [`Deformation.RingThickening.splittingFromTrivialization`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingThickening/TrivialThickening.lean#L126), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/RingThickening/TrivialThickening.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingThickening/TrivialThickening.lean#L202) (StacksFrontier): “the splitting determined by a trivialization”.
- [`Deformation.RingThickening.PresheafTrivialSquareZeroEquiv`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingThickening/TrivialThickening.lean#L98), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/RingThickening/TrivialThickening.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingThickening/TrivialThickening.lean#L204) (StacksFrontier): “the split square-zero extension it lands in”.

## Tag 08LB, a remark

[Tag 08LB](https://stacks.math.columbia.edu/tag/08LB) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.trivialExtensionModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean, line 779](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean#L779). The attribute's comment: “part (1): the trivial extension `ℱ'_{c,triv} = ℱ ⊕ 𝒦`”.

> **Stacks Project, Tag 08LB, part (1).** The *trivial extension* `ℱ'_{c,triv}` of `ℱ` by
> `𝒦` attached to `c` and a trivialization `π`: the direct sum `ℱ ⊕ 𝒦`, carried to `X'` by `i_*`,
> with the `𝒪_{X'}`-module structure built from the splitting of **Stacks 08LA** and the map `c`,
>
>     r · (m, n) = (r m, r n + c(d r ⊗ m)),
>
> where `d r = r - π^♯(i^♯ r)` is the derivation of the trivialization.

```lean
noncomputable def trivialExtensionModule : SheafOfModules.{u} (structureSheafRing X')
```

**`AlgebraicGeometry.RingedSpaceThickening.trivialExtensionModule_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean, line 799](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean#L799). The attribute's comment: “part (1): the action of `𝒪_{X'}` on `ℱ ⊕ 𝒦`”.

> **Stacks Project, Tag 08LB, part (1).** The `𝒪_{X'}`-module structure of the trivial
> extension: a section of `𝒪_{X'}` acts diagonally on `ℱ ⊕ 𝒦` and moves the `ℱ`-coordinate into
> the `𝒦`-coordinate through `c` and the derivation of the trivialization. Together with
> `AlgebraicGeometry.RingedSpaceThickening.trivialExtensionModule`, whose sections over `U` are
> by construction the pairs `ℱ(i^{-1}U) × 𝒦(i^{-1}U)`, this is the whole content of part (1).

```lean
theorem trivialExtensionModule_smul (U : (Opens X'.carrier)ᵒᵖ)
    (r : (structureSheafRing X').obj.obj U)
    (z : (trivialExtensionModule i π F K c hi).val.obj U) :
    r • z = (r • z.1, r • z.2 +
      extensionPairing i F K c U (trivializationDerivation i π hi.1.1 U r) z.1)
```

**`AlgebraicGeometry.RingedSpaceThickening.trivialExtensionShortComplex_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean, line 916](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean#L916). The attribute's comment: “part (2): the trivial extension is an extension as in 08L4”.

> **Stacks Project, Tag 08LB, part (2).** The trivial extension sits in a short exact
> sequence `0 ⟶ i_* 𝒦 ⟶ ℱ'_{c,triv} ⟶ i_* ℱ ⟶ 0` of `𝒪_{X'}`-modules: the inclusion of the
> second summand is a kernel of the projection onto the first.

```lean
theorem trivialExtensionShortComplex_shortExact :
    (trivialExtensionShortComplex i π F K c hi).ShortExact
```

**`AlgebraicGeometry.RingedSpaceThickening.trivialYonedaExtension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean, line 932](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean#L932). The attribute's comment: “part (2): the trivial extension as a Yoneda extension”.

> **Stacks Project, Tag 08LB, part (2).** The trivial extension, read as an extension of
> `i_* ℱ` by `i_* 𝒦` in the sense of **Stacks 08L4**.

```lean
noncomputable def trivialYonedaExtension :
    CategoryTheory.Abelian.YonedaExtension ((modulePushforward i).obj F)
      ((modulePushforward i).obj K) 0
```

**`AlgebraicGeometry.RingedSpaceThickening.trivialYonedaExtension_action`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean, line 954](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean#L954). The attribute's comment: “part (2'): the canonical map of the trivial extension is `c`”.

> **Stacks Project, Tag 08LB, part (2').** The canonical map of the trivial extension is the
> prescribed one: `c_{ℱ'_{c,triv}} = c`. This is what places `ℱ'_{c,triv}` in the set of
> extensions with `c = c_{ℱ'}` that part (4) of the remark puts in bijection with
> `Ext¹_{𝒪_X}(ℱ, 𝒦)`.

```lean
theorem trivialYonedaExtension_action :
    (firstOrderExtensionAction i F K hi (trivialYonedaExtension i π F K c hi)).1 = c
```

**`AlgebraicGeometry.RingedSpaceThickening.splitRestriction`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean, line 1002](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean#L1002). The attribute's comment: “part (3): reading an extension as an `𝒪_X`-module along the trivialization”.

> **Stacks Project, Tag 08LB, part (3).** Reading a sheaf of `𝒪_{X'}`-modules as a sheaf of
> `𝒪_X`-modules along a trivialization: pushforward along the retraction.
>
> This is the ringed-space form of the source's "use `π^♯ : 𝒪_X ⟶ 𝒪_{X'}` to think of `ℱ'` as an
> `𝒪_X`-module". On a single site one would restrict scalars along `π^♯`
> (`Stacks.SheafOfModules.restrictScalarsSplitIso`), but here `X` and `X'` carry different sites
> `Opens X` and `Opens X'`, so the reindexing of opens along the homeomorphism `π` has to be
> carried along with the restriction of scalars — which is exactly what `π_*` does.

```lean
noncomputable abbrev splitRestriction :
    SheafOfModules.{u} (structureSheafRing X') ⥤ SheafOfModules.{u} (structureSheafRing X)
```

**`AlgebraicGeometry.RingedSpaceThickening.splitExtension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean, line 1048](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean#L1048). The attribute's comment: “part (3): an extension read as a sequence of `𝒪_X`-modules”.

> **Stacks Project, Tag 08LB, part (3).** The extension `0 ⟶ i_* 𝒦 ⟶ ℱ' ⟶ i_* ℱ ⟶ 0` of
> `𝒪_{X'}`-modules, read as a short complex of `𝒪_X`-modules along the trivialization. Its outer
> terms are `𝒦` and `ℱ` themselves, by
> `AlgebraicGeometry.RingedSpaceThickening.splitRestrictionIso`.

```lean
noncomputable def splitExtension : ShortComplex (SheafOfModules.{u} (structureSheafRing X))
```

**`AlgebraicGeometry.RingedSpaceThickening.splitExtension_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean, line 1077](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean#L1077). The attribute's comment: “part (3): the sequence read over `𝒪_X` is short exact”.

> **Stacks Project, Tag 08LB, part (3).** An extension across the thickening, read along the
> trivialization, is again short exact — which is what makes the class `ξ_{ℱ'}` available.
>
> Pushforward along `π.retraction` is left exact because it is a right adjoint
> (`RingedSpaceModuleAdjunction.modulePushforward_isRightAdjoint`) and right exact because the
> base map of a trivialization is a homeomorphism
> (`Stacks.ClosedImmersion.preservesFiniteColimits_modulePushforward_of_isIso_base`), so the
> sequence maps across by `CategoryTheory.ShortComplex.ShortExact.map_of_exact`; the outer terms
> are then only reindexed by isomorphisms.

```lean
theorem splitExtension_shortExact : (splitExtension i π F K E).ShortExact
```

**`AlgebraicGeometry.RingedSpaceThickening.underlyingExtensionClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean, line 1093](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean#L1093). The attribute's comment: “part (3): the class `ξ_{ℱ'}` of an extension”.

> **Stacks Project, Tag 08LB, part (3).** The class `ξ_{ℱ'} ∈ Ext¹_{𝒪_X}(ℱ, 𝒦)` of an
> extension of `ℱ` by `𝒦` across a trivialized first order thickening of ringed spaces: the
> trivialization lets the extension be read as an extension of `𝒪_X`-modules, and this is the
> class of that extension.

```lean
noncomputable def underlyingExtensionClass
    [HasExt.{e} (SheafOfModules.{u} (structureSheafRing X))] :
    CategoryTheory.Abelian.Ext F K 1
```

**`AlgebraicGeometry.RingedSpaceThickening.underlyingExtensionClass_trivialYonedaExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean, line 1197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean#L1197). The attribute's comment: “part (5): the trivial extension has class `ξ_{ℱ'_{c,triv}} = 0`”.

> **Stacks Project, Tag 08LB, part (5).** The trivial extension maps to the zero class:
> `ξ_{ℱ'_{c,triv}} = 0` in `Ext¹_{𝒪_X}(ℱ, 𝒦)`.
>
> Read along the trivialization the sequence `0 ⟶ 𝒦 ⟶ ℱ ⊕ 𝒦 ⟶ ℱ ⟶ 0` splits, because the
> derivation `d` kills every scalar pulled back along `π` and so the correction term `c(d r ⊗ m)`
> in the action disappears — the projection onto the `𝒦`-summand, which is not `𝒪_{X'}`-linear,
> becomes `𝒪_X`-linear. A split short exact sequence has zero class by
> `AlgebraicGeometry.RingedSpaceThickening.extClass_eq_zero_of_retraction`.

```lean
theorem underlyingExtensionClass_trivialYonedaExtension
    [HasExt.{e} (SheafOfModules.{u} (structureSheafRing X))] :
    underlyingExtensionClass i π hi.1.1 F K (trivialYonedaExtension i π F K c hi) = 0
```

**`AlgebraicGeometry.RingedSpaceThickening.exists_iso_of_underlyingExtensionClass_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean, line 1380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean#L1380). The attribute's comment: “part (4): injectivity of `ℱ' ↦ ξ_{ℱ'}` — two extensions as in 08L4 with the same canonical map `c` and the same class `ξ` are isomorphic as extensions”.

> **Stacks Project, Tag 08LB, part (4).** *Injectivity of `ℱ' ↦ ξ_{ℱ'}` on isomorphism
> classes:* two extensions across the thickening with the same canonical map and the same class
> `ξ` are isomorphic as extensions, by an isomorphism of their middle terms compatible with both
> end terms.
>
> This is `AlgebraicGeometry.RingedSpaceThickening.extClass_eq_of_underlyingExtensionClass_eq`
> together with the fact that two short exact sequences with the same class in `Ext¹` are
> isomorphic over the identity of both end terms
> (`CategoryTheory.Abelian.Ext.extClass_surjective_and_eq_iff_iso_and_baerSum`).

```lean
theorem exists_iso_of_underlyingExtensionClass_eq
    (E E' : Abelian.YonedaExtension ((modulePushforward i).obj F)
      ((modulePushforward i).obj K) 0)
    (hact : (firstOrderExtensionAction i F K hi E).val =
      (firstOrderExtensionAction i F K hi E').val)
    (hξ : underlyingExtensionClass i π hi.1.1 F K E =
      underlyingExtensionClass i π hi.1.1 F K E') :
    ∃ φ : E.Z.left ≅ E'.Z.left, E.f ≫ φ.hom = E'.f ∧ φ.hom ≫ E'.g = E.g
```

**`AlgebraicGeometry.RingedSpaceThickening.exists_yonedaExtension_underlyingExtensionClass_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean, line 1406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean#L1406). The attribute's comment: “part (4): surjectivity of `ℱ' ↦ ξ_{ℱ'}` — every class in `Ext¹_{𝒪_X}(ℱ, 𝒦)` is the class of an extension as in 08L4 with canonical map `c`”.

> **Stacks Project, Tag 08LB, part (4).** *Surjectivity of `ℱ' ↦ ξ_{ℱ'}`:* every class
> `η ∈ Ext¹_{𝒪_X}(ℱ, 𝒦)` is the class `ξ_{ℱ'}` of an extension `ℱ'` as in **Stacks 08L4** whose
> canonical map is the prescribed `c`.
>
> Realize `η` as an extension of `𝒪_X`-modules and push it forward along the thickening: its
> middle term is a direct image, so by **Stacks 08L7** it can be added to the trivial extension
> `ℱ'_{c,triv}` of part (1) without changing the canonical map, which is `c` by part (2'). The
> class of the sum is `0 + η = η` by part (5) and additivity.

```lean
theorem exists_yonedaExtension_underlyingExtensionClass_eq
    (c : (((Stacks.SheafOfModules.Tensor.sheafTensor ⟨((X)).presheaf, ((X)).IsSheaf⟩).obj
      ((idealSheafPullback i))).obj (F)) ⟶ K) (η : Abelian.Ext.{e} F K 1) :
    ∃ E : Abelian.YonedaExtension ((modulePushforward i).obj F)
        ((modulePushforward i).obj K) 0,
      (firstOrderExtensionAction i F K hi E).val = c ∧
        underlyingExtensionClass i π hi.1.1 F K E = η
```

**`AlgebraicGeometry.RingedSpaceThickening.bijective_underlyingExtensionClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean, line 1470](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/TrivialExtension.lean#L1470). The attribute's comment: “part (4): `ℱ' ↦ ξ_{ℱ'}` is a bijection from the isomorphism classes of extensions as in 08L4 with `c = c_{ℱ'}` onto `Ext¹_{𝒪_X}(ℱ, 𝒦)`, the isomorphism classes being represented by their classes in `Ext¹_{𝒪_{X'}}(i_* ℱ, i_* 𝒦)`”.

> **Stacks Project, Tag 08LB, part (4).** `ℱ' ↦ ξ_{ℱ'}` *is a bijection* from the isomorphism
> classes of extensions `0 ⟶ i_* 𝒦 ⟶ ℱ' ⟶ i_* ℱ ⟶ 0` as in **Stacks 08L4** with
> `c = c_{ℱ'}` onto `Ext¹_{𝒪_X}(ℱ, 𝒦)`.
>
> The isomorphism classes are the elements of
> `AlgebraicGeometry.RingedSpaceThickening.extensionClassesWithAction`, i.e. are represented by
> their classes in `Ext¹_{𝒪_{X'}}(i_* ℱ, i_* 𝒦)`, and the map is
> `AlgebraicGeometry.RingedSpaceThickening.splitRestrictionExtHom`, which on the class of `ℱ'` is
> `ξ_{ℱ'}` by
> `AlgebraicGeometry.RingedSpaceThickening.underlyingExtensionClass_eq_splitRestrictionExtHom`.
> The two halves of the statement, read on extensions rather than on classes, are
> `AlgebraicGeometry.RingedSpaceThickening.exists_yonedaExtension_underlyingExtensionClass_eq` and
> `AlgebraicGeometry.RingedSpaceThickening.exists_iso_of_underlyingExtensionClass_eq`.

```lean
theorem bijective_underlyingExtensionClass
    (c : (((Stacks.SheafOfModules.Tensor.sheafTensor ⟨((X)).presheaf, ((X)).IsSheaf⟩).obj
      ((idealSheafPullback i))).obj (F)) ⟶ K) :
    Function.Bijective (fun ξ : ↥(extensionClassesWithAction i F K hi c) =>
      splitRestrictionExtHom i π hi.1.1 F K ξ.1)
```

## Tag 08LC, a remark

[Tag 08LC](https://stacks.math.columbia.edu/tag/08LC) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.PushoutDescentData.extensionOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/ExtensionPushoutDescent.lean, line 1383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/ExtensionPushoutDescent.lean#L1383). The attribute's comment: “the canonical map on extensions, by pushout along the map of kernel modules”.

> **Stacks Project, Tag 08LC.** The extension over the first thickening produced from an
> extension over the second: the pushout `ℱ'₂ ⊔_{𝒦₂} 𝒦₁` carries an `𝒪_{X'}`-module structure,
> built by descending the action of `T = 𝒪'₂ ⋉ ℐ₁` twisted by `c₁` along the locally surjective
> `q : T ⟶ 𝒪_{X'}`, and sits in a short exact sequence `0 → i_* 𝒦₁ → ℱ'₁ → i_* ℱ → 0` of
> `𝒪_{X'}`-modules. Its middle term restricted along `q` is identified with the pushout by
> `middleIso`, compatibly with the two maps by `restrictScalars_extInclOne` and
> `restrictScalars_extQuotOne`.

```lean
noncomputable def extensionOne :
    CategoryTheory.Abelian.YonedaExtension ((modulePushforward i).obj dat.F)
      ((modulePushforward i).obj dat.K₁) 0
```

**`AlgebraicGeometry.RingedSpaceThickening.PushoutDescentData.extensionOne_action`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/ExtensionPushoutDescent.lean, line 1471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/ExtensionPushoutDescent.lean#L1471). The attribute's comment: “the canonical map of the pushed-out extension is c₁”.

> **Stacks Project, Tag 08LC.** The canonical map of Tag 08L4 of the extension produced over
> the first thickening is the prescribed `c₁`.

```lean
theorem extensionOne_action :
    (firstOrderExtensionAction i dat.F dat.K₁ hi (dat.extensionOne E₂ hi hE₂)).val = dat.c₁
```

## Tag 08LD, a remark

[Tag 08LD](https://stacks.math.columbia.edu/tag/08LD) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.PushoutDescentData.underlyingExtensionClass_extensionOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/PushoutDescentClass.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/PushoutDescentClass.lean#L233). The attribute's comment: “the square commutes for the extension Tag 08LC produces”.

> **Stacks Project, Tag 08LD.** The square of the remark commutes for the extension that
> Tag 08LC produces: let `h = SecondThickening.spaceHom` be the morphism of first order
> thickenings of `(X, 𝒪_X)` that `h^♯` presents, let both thickenings be trivialized by `π₁` and
> `π₂` with `π₁ = h ≫ π₂`, so that `h` is a morphism of *trivialized* thickenings, and let the
> square relating `c₁`, `c₂`, `κ` and `ℐ₂ ⟶ ℐ₁` commute. If `ℱ'₂` is an extension as in Tag 08L4
> whose canonical map is `c₂`, then the class `ξ` of Tag 08LB of the extension
> `AlgebraicGeometry.RingedSpaceThickening.PushoutDescentData.extensionOne` that Tag 08LC produces
> from it is the image of `ξ_{ℱ'₂}` under functoriality of `Ext¹_{𝒪_X}(ℱ, -)` along `κ`.
>
> Both extensions are members of the two sets the square relates: `hE₂` says that the canonical
> map of `ℱ'₂` is `c₂`, and `PushoutDescentData.extensionOne_action` says that the canonical map
> of the extension produced from it is `c₁`.
>
> The hypothesis `hc` is the remark's commuting square, written with the induced map of ideals
> `AlgebraicGeometry.RingedSpaceThickening.thickeningIdealMap`. The field
> `AlgebraicGeometry.RingedSpaceThickening.PushoutDescentData.comm` of `dat` is the same square of
> the same remark, written on local pure tensors, which is the form the construction of Tag 08LC
> consumes; no cross-thickening comparison of the two canonical maps is available to pass between
> the two forms, so the square is assumed in both.

```lean
theorem underlyingExtensionClass_extensionOne
    [HasExt.{e} (SheafOfModules.{u} (structureSheafRing X))]
    (π₁ : SplitMono i) (π₂ : SplitMono S.hom)
    (hπ : π₁.retraction = S.spaceHom ≫ π₂.retraction)
    (hc : dat.c₂ ≫ dat.kernelMap =
      (Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor ⟨X.presheaf, X.IsSheaf⟩)).map
        ((thickeningIdealMap i S.hom S.spaceHom S.comp_spaceHom, 𝟙 dat.F) : (_, _) ⟶ (_, _)) ≫
          dat.c₁) :
    underlyingExtensionClass i π₁ hi.1.1 dat.F dat.K₁ (dat.extensionOne E₂ hi hE₂) =
      (underlyingExtensionClass S.hom π₂ S.firstOrder.1.1 dat.F dat.K₂ E₂).comp
        (CategoryTheory.Abelian.Ext.mk₀ dat.kernelMap) (add_zero 1)
```

**`AlgebraicGeometry.RingedSpaceThickening.underlyingExtensionClass_eq_of_pushedExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/TrivializedFunctoriality.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/TrivializedFunctoriality.lean#L394). The attribute's comment: “the commutative square relating the two extension classes”.

> For a morphism `h : X'₁ ⟶ X'₂` of trivialized first order thickenings of `(X, 𝒪_X)` the square
> relating the extension classes commutes: if `ℱ'₁` is the extension that the functoriality of Tag
> 08LC produces from `ℱ'₂` and `k : 𝒦₂ ⟶ 𝒦₁`, then the class `ξ_{ℱ'₁}` of Tag 08LB is the image of
> `ξ_{ℱ'₂}` under functoriality of `Ext¹_{𝒪_X}(ℱ, -)` along `k`.
>
> The hypotheses `hc`, `hE₂` and `hE₁` say that the two extensions are members of the two sets the
> square relates — that their canonical maps of Tag 08L4 are `c₂` and `c₁`, compatibly with `k`.
> The identity of classes uses only the map of extensions `w`.

```lean
theorem underlyingExtensionClass_eq_of_pushedExtension (i₁ : X ⟶ X₁) (i₂ : X ⟶ X₂)
    (h : X₁ ⟶ X₂) (comm : i₁ ≫ h = i₂)
    (hi₁ : IsFirstOrderThickening i₁) (hi₂ : IsFirstOrderThickening i₂)
    (π₁ : SplitMono i₁) (π₂ : SplitMono i₂)
    (hπ : π₁.retraction = h ≫ π₂.retraction)
    (F K₁ K₂ : SheafOfModules.{u} (structureSheafRing X)) (k : K₂ ⟶ K₁)
    (c₁ : (((Stacks.SheafOfModules.Tensor.sheafTensor ⟨((X)).presheaf, ((X)).IsSheaf⟩).obj
      ((idealSheafPullback i₁))).obj (F)) ⟶ K₁)
    (c₂ : (((Stacks.SheafOfModules.Tensor.sheafTensor ⟨((X)).presheaf, ((X)).IsSheaf⟩).obj
      ((idealSheafPullback i₂))).obj (F)) ⟶ K₂)
    (_hc : c₂ ≫ k = ((Functor.uncurry.obj
      (Stacks.SheafOfModules.Tensor.sheafTensor ⟨((X)).presheaf, ((X)).IsSheaf⟩)).map
        (((thickeningIdealMap i₁ i₂ h comm), (𝟙 F)) : (_, _) ⟶ (_, _))) ≫ c₁)
    (E₂ : CategoryTheory.Abelian.YonedaExtension ((modulePushforward i₂).obj F)
      ((modulePushforward i₂).obj K₂) 0)
    (_hE₂ : (firstOrderExtensionAction i₂ F K₂ hi₂ E₂).val = c₂)
    (E₁ : CategoryTheory.Abelian.YonedaExtension ((modulePushforward i₁).obj F)
      ((modulePushforward i₁).obj K₁) 0)
    (_hE₁ : (firstOrderExtensionAction i₁ F K₁ hi₁ E₁).val = c₁)
    (w : PushedExtension i₁ i₂ h comm F K₁ K₂ k E₂ E₁) :
    underlyingExtensionClass i₁ π₁ hi₁.1.1 F K₁ E₁ =
      (underlyingExtensionClass i₂ π₂ hi₂.1.1 F K₂ E₂).comp
        (CategoryTheory.Abelian.Ext.mk₀ k) (add_zero 1)
```

## Tag 08LE, a remark

[Tag 08LE](https://stacks.math.columbia.edu/tag/08LE) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.IsComplex`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/RingedSpace/ThickeningSequence.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/RingedSpace/ThickeningSequence.lean#L176). The attribute's comment: “complex of first order thickenings”.

> **Stacks Project, Tag 08LE.** A sequence of first order thickenings of `X` is a *complex*
> when its induced maps on ideal modules compose to zero.

```lean
noncomputable abbrev IsComplex (S : FirstOrderThickeningSequence.{u}) : Prop
```

**`AlgebraicGeometry.RingedSpaceThickening.IsShortExact`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/RingedSpace/ThickeningSequence.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/RingedSpace/ThickeningSequence.lean#L183). The attribute's comment: “short exact sequence of first order thickenings”.

> **Stacks Project, Tag 08LE.** A sequence of first order thickenings of `X` is a *short
> exact sequence* when `0 ⟶ ℐ₃ ⟶ ℐ₂ ⟶ ℐ₁ ⟶ 0` is short exact as a sequence of
> `𝒪_X`-modules.

```lean
noncomputable abbrev IsShortExact (S : FirstOrderThickeningSequence.{u}) : Prop
```

**`AlgebraicGeometry.RingedSpaceThickening.FirstOrderThickeningSequence.existsUnique_trivialization_of_isComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/RingedSpace/ThickeningTrivialization.lean, line 461](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/RingedSpace/ThickeningTrivialization.lean#L461). The attribute's comment: “canonical trivialization of a complex”.

> **Stacks Project, Tag 08LE.** A complex of first order thickenings of `(X, 𝒪_X)` canonically
> trivializes its first thickening: the composite `X₁ ⟶ X₃` factors uniquely through
> `i₃ : X ⟶ X₃`, and the factor `π : X₁ ⟶ X` is a retraction of `i₁`.

```lean
theorem existsUnique_trivialization_of_isComplex (hS : IsComplex S) :
    ∃! π : S.X₁ ⟶ S.X, (S.i₁ ≫ π = 𝟙 S.X) ∧ (π ≫ S.i₃ = S.f₁₂ ≫ S.f₂₃)
```

## Tag 08LF, a remark

[Tag 08LF](https://stacks.math.columbia.edu/tag/08LF) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.boundary_underlyingExtensionClass_eq_obstructionClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/RestrictedExtensionAction.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/RestrictedExtensionAction.lean#L356).

> **Stacks Project, Tag 08LF.** Let `(X, 𝒪_X)` be a ringed space, `ℱ` an `𝒪_X`-module and
> `X'₁ ⟶ X'₂ ⟶ X'₃` a complex of first order thickenings of `(X, 𝒪_X)` (Tag 08LE), with ideals
> `ℐᵢ`. Let `cᵢ : ℐᵢ ⊗_{𝒪_X} ℱ ⟶ 𝒦ᵢ` be maps and `0 ⟶ 𝒦₃ ⟶ 𝒦₂ ⟶ 𝒦₁ ⟶ 0` a short exact sequence of
> `𝒪_X`-modules for which the two squares of the remark commute. Let `ℱ'₂` be an extension
> `0 ⟶ 𝒦₂ ⟶ ℱ'₂ ⟶ ℱ ⟶ 0` as in Tag 08L4 over `X'₂` with `c_{ℱ'₂} = c₂`, and let `ℱ'₁` be the
> extension over `X'₁` that the functoriality of Tag 08LC produces from it. That functoriality
> carries `ℱ'₂` to an extension as in Tag 08L4 over `X'₁` together with a map of extensions `w`
> from `ℱ'₂`, which is `𝒦₂ ⟶ 𝒦₁` on kernels and the identity on `ℱ`; the statement is made for
> every extension `ℱ'₁` over `X'₁` receiving such a map, so in particular for the one of Tag 08LC
> (which in addition has `c_{ℱ'₁} = c₁`, a property the identity of classes does not use).
>
> Then the boundary map `∂ : Ext¹_{𝒪_X}(ℱ, 𝒦₁) ⟶ Ext²_{𝒪_X}(ℱ, 𝒦₃)` of
> `0 ⟶ 𝒦₃ ⟶ 𝒦₂ ⟶ 𝒦₁ ⟶ 0` — Yoneda composition with the class of that sequence — sends the class
> `ξ_{ℱ'₁}` of Tag 08LB, formed with the canonical splitting `π` of Tag 08LE, to the obstruction
> class `o(ℱ, 𝒦₃, c₃)` of Tag 08L8.
>
> The first compatibility square of the remark, relating `c₂`, `c₁` and `𝒦₂ ⟶ 𝒦₁`, is what makes
> Tag 08LC applicable; once `ℱ'₁` and `w` are given it is not needed for the identity of classes,
> so it is not a hypothesis here. It is a hypothesis of the version for the extension that Tag 08LC
> constructs, `boundary_underlyingExtensionClass_extensionOne_eq_obstructionClass`, where it is the
> input of that construction; the map `c₁` enters only through that square, so it does not appear
> here either.

```lean
theorem boundary_underlyingExtensionClass_eq_obstructionClass
    (S : FirstOrderThickeningSequence.{u})
    [HasExt (SheafOfModules.{u} (structureSheafRing S.X))]
    [HasDerivedCategory (SheafOfModules.{u} (structureSheafRing S.X))]
    (hS : IsComplex S) (F K₁ K₂ K₃ : SheafOfModules.{u} (structureSheafRing S.X))
    (k₃₂ : K₃ ⟶ K₂) (k₂₁ : K₂ ⟶ K₁) (hk : k₃₂ ≫ k₂₁ = 0)
    (hK : (ShortComplex.mk k₃₂ k₂₁ hk).ShortExact)
    (c₂ : (((Stacks.SheafOfModules.Tensor.sheafTensor ⟨S.X.presheaf, S.X.IsSheaf⟩).obj
      (idealSheafPullback S.i₂)).obj F) ⟶ K₂)
    (c₃ : (((Stacks.SheafOfModules.Tensor.sheafTensor ⟨S.X.presheaf, S.X.IsSheaf⟩).obj
      (idealSheafPullback S.i₃)).obj F) ⟶ K₃)
    (hc₃₂ : c₃ ≫ k₃₂ =
      ((Functor.uncurry.obj
        (Stacks.SheafOfModules.Tensor.sheafTensor ⟨S.X.presheaf, S.X.IsSheaf⟩)).map
        (((thickeningIdealMap S.i₂ S.i₃ S.f₂₃ S.comm₂₃), (𝟙 F)) : (_, _) ⟶ (_, _))) ≫ c₂)
    (E₂ : CategoryTheory.Abelian.YonedaExtension ((modulePushforward S.i₂).obj F)
      ((modulePushforward S.i₂).obj K₂) 0)
    (hE₂ : (firstOrderExtensionAction S.i₂ F K₂ S.firstOrder₂ E₂).val = c₂)
    (E₁ : CategoryTheory.Abelian.YonedaExtension ((modulePushforward S.i₁).obj F)
      ((modulePushforward S.i₁).obj K₁) 0)
    (w : PushedExtension S.i₁ S.i₂ S.f₁₂ S.comm₁₂ F K₁ K₂ k₂₁ E₂ E₁) :
    (underlyingExtensionClass S.i₁ (S.trivialization hS) S.firstOrder₁.1.1 F K₁ E₁).comp
        hK.extClass (by decide) =
      obstructionClass S.i₃ S.firstOrder₃ F K₃ c₃
```

**`AlgebraicGeometry.RingedSpaceThickening.boundary_underlyingExtensionClass_extensionOne_eq_obstructionClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/RestrictedExtensionAction.lean, line 601](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/RestrictedExtensionAction.lean#L601).

> **Stacks Project, Tag 08LF**, for the extension `ℱ'₁` that Tag 08LC constructs. Let
> `X'₁ ⟶ X'₂ ⟶ X'₃` be a complex of first order thickenings of `(X, 𝒪_X)` (Tag 08LE), with
> `X'₂` presented on the space of `X'₁` as in Tag 08LC, and let `(𝒦ᵢ, cᵢ)`, a short exact sequence
> `0 ⟶ 𝒦₃ ⟶ 𝒦₂ ⟶ 𝒦₁ ⟶ 0` and the two commutative squares be as in the remark. For an extension
> `ℱ'₂` over `X'₂` as in Tag 08L4 with `c_{ℱ'₂} = c₂`, let `ℱ'₁` be the extension over `X'₁` that the
> functoriality of Tag 08LC produces (`PushoutDescentData.extensionOne`). Then the boundary map
> `Ext¹_{𝒪_X}(ℱ, 𝒦₁) ⟶ Ext²_{𝒪_X}(ℱ, 𝒦₃)` sends `ξ_{ℱ'₁}`, formed with the canonical splitting of
> Tag 08LE, to the obstruction class `o(ℱ, 𝒦₃, c₃)` of Tag 08L8.

```lean
theorem boundary_underlyingExtensionClass_extensionOne_eq_obstructionClass
    {X₁ : RingedSpace.{u, u}} {i : X ⟶ X₁} (hi : IsFirstOrderThickening i)
    (ST : SecondThickening i) (i₃ : X ⟶ X₃) (hi₃ : IsFirstOrderThickening i₃)
    (f₂₃ : ST.space ⟶ X₃) (comm₂₃ : ST.hom ≫ f₂₃ = i₃)
    (idealMap₂₁ : (modulePullback ST.hom).obj (AlgebraicGeometry.SheafOfModules.idealSheaf ST.hom) ⟶
      (modulePullback i).obj (AlgebraicGeometry.SheafOfModules.idealSheaf i))
    (idealMap₃₂ : (modulePullback i₃).obj (AlgebraicGeometry.SheafOfModules.idealSheaf i₃) ⟶
      (modulePullback ST.hom).obj (AlgebraicGeometry.SheafOfModules.idealSheaf ST.hom))
    [HasExt (SheafOfModules.{u} (structureSheafRing X))]
    [HasDerivedCategory (SheafOfModules.{u} (structureSheafRing X))]
    (hS : IsComplex (ST.thickeningSequence hi i₃ hi₃ f₂₃ comm₂₃ idealMap₂₁ idealMap₃₂))
    (F K₁ K₂ K₃ : SheafOfModules.{u} (structureSheafRing X))
    (k₃₂ : K₃ ⟶ K₂) (k₂₁ : K₂ ⟶ K₁) (hk : k₃₂ ≫ k₂₁ = 0)
    (hK : (ShortComplex.mk k₃₂ k₂₁ hk).ShortExact)
    (c₁ : (((Stacks.SheafOfModules.Tensor.sheafTensor ⟨X.presheaf, X.IsSheaf⟩).obj
      (idealSheafPullback i)).obj F) ⟶ K₁)
    (c₂ : (((Stacks.SheafOfModules.Tensor.sheafTensor ⟨X.presheaf, X.IsSheaf⟩).obj
      (idealSheafPullback ST.hom)).obj F) ⟶ K₂)
    (c₃ : (((Stacks.SheafOfModules.Tensor.sheafTensor ⟨X.presheaf, X.IsSheaf⟩).obj
      (idealSheafPullback i₃)).obj F) ⟶ K₃)
    (hc₂₁ : c₂ ≫ k₂₁ =
      ((Functor.uncurry.obj
        (Stacks.SheafOfModules.Tensor.sheafTensor ⟨X.presheaf, X.IsSheaf⟩)).map
        (((thickeningIdealMap i ST.hom ST.toSpace ST.comp_toSpace), (𝟙 F)) :
          (_, _) ⟶ (_, _))) ≫ c₁)
    (hc₃₂ : c₃ ≫ k₃₂ =
      ((Functor.uncurry.obj
        (Stacks.SheafOfModules.Tensor.sheafTensor ⟨X.presheaf, X.IsSheaf⟩)).map
        (((thickeningIdealMap ST.hom i₃ f₂₃ comm₂₃), (𝟙 F)) : (_, _) ⟶ (_, _))) ≫ c₂)
    (E₂ : CategoryTheory.Abelian.YonedaExtension ((modulePushforward ST.hom).obj F)
      ((modulePushforward ST.hom).obj K₂) 0)
    (hE₂ : (firstOrderExtensionAction ST.hom F K₂ ST.firstOrder E₂).val = c₂) :
    (underlyingExtensionClass i
        ((ST.thickeningSequence hi i₃ hi₃ f₂₃ comm₂₃ idealMap₂₁ idealMap₃₂).trivialization hS)
        hi.1.1 F K₁
        ((PushoutDescentData.ofSquare ST F K₁ K₂ c₁ c₂ k₂₁ hc₂₁).extensionOne E₂ hi hE₂)).comp
        hK.extClass (by decide) =
      obstructionClass i₃ hi₃ F K₃ c₃
```

**`AlgebraicGeometry.RingedSpaceThickening.boundary_underlyingExtensionClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/ThickeningComplexBoundary.lean, line 704](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/ThickeningComplexBoundary.lean#L704). The attribute's comment: “the boundary of the extension class is the obstruction class”.

> **Stacks Project, Tag 08LF.** Let `(X, 𝒪_X)` be a ringed space, `ℱ` an `𝒪_X`-module, and let
> `X'₁ ⟶ X'₂ ⟶ X'₃` be a complex of first order thickenings of `(X, 𝒪_X)`, with `π` the canonical
> trivialization of `i₁` (Tag 08LE). Let `(𝒦ᵢ, cᵢ)` be pairs with `cᵢ : ℐᵢ ⊗_{𝒪_X} ℱ ⟶ 𝒦ᵢ` and
> let `0 ⟶ 𝒦₃ ⟶ 𝒦₂ ⟶ 𝒦₁ ⟶ 0` be a short exact sequence of `𝒪_X`-modules making the two squares
> `_hc₂₁` and `hc₃₂` of the remark commute. Let `ℱ'₂` be an extension as in Tag 08L4 over `X'₂`
> with `c_{ℱ'₂} = c₂` and let `ℱ'₁` be the extension over `X'₁` that Tag 08LC produces from it,
> exhibited by the map of extensions `w` and the pushout square `hw`.
>
> Then the boundary map `∂ : Ext¹_{𝒪_X}(ℱ, 𝒦₁) ⟶ Ext²_{𝒪_X}(ℱ, 𝒦₃)` of
> `0 ⟶ 𝒦₃ ⟶ 𝒦₂ ⟶ 𝒦₁ ⟶ 0` — Yoneda composition with the class of that sequence — carries
> `ξ_{ℱ'₁}` of Tag 08LB to the obstruction class `o(ℱ, 𝒦₃, c₃)` of Tag 08L8.
>
> The hypothesis `hrestrict` is not derived in this development; see the Scope section of the
> module docstring. The hypotheses `_hS`, `_hc₂₁`, `_hE₂` and `_hE₁` are part of the situation of
> the remark but are not used: the complex condition enters only through `hπ`, which is what the
> canonical trivialization of Tag 08LE supplies, and the canonical maps of `ℱ'₂` and `ℱ'₁` enter
> only through `hrestrict` and `w`.

```lean
theorem boundary_underlyingExtensionClass (S : FirstOrderThickeningSequence.{u})
    [HasExt (SheafOfModules.{u} (structureSheafRing S.X))]
    [HasDerivedCategory (SheafOfModules.{u} (structureSheafRing S.X))]
    (_hS : IsComplex S) (π : SplitMono S.i₁)
    (hπ : π.retraction ≫ S.i₃ = S.f₁₂ ≫ S.f₂₃)
    (F K₁ K₂ K₃ : SheafOfModules.{u} (structureSheafRing S.X))
    (k₃₂ : K₃ ⟶ K₂) (k₂₁ : K₂ ⟶ K₁) (hk : k₃₂ ≫ k₂₁ = 0)
    (hK : (ShortComplex.mk k₃₂ k₂₁ hk).ShortExact)
    (c₁ : (((Stacks.SheafOfModules.Tensor.sheafTensor ⟨((S.X)).presheaf, ((S.X)).IsSheaf⟩).obj
      ((idealSheafPullback S.i₁))).obj (F)) ⟶ K₁)
    (c₂ : (((Stacks.SheafOfModules.Tensor.sheafTensor ⟨((S.X)).presheaf, ((S.X)).IsSheaf⟩).obj
      ((idealSheafPullback S.i₂))).obj (F)) ⟶ K₂)
    (c₃ : (((Stacks.SheafOfModules.Tensor.sheafTensor ⟨((S.X)).presheaf, ((S.X)).IsSheaf⟩).obj
      ((idealSheafPullback S.i₃))).obj (F)) ⟶ K₃)
    (_hc₂₁ : c₂ ≫ k₂₁ =
      ((Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor
        ⟨((S.X)).presheaf, ((S.X)).IsSheaf⟩)).map
        (((thickeningIdealMap S.i₁ S.i₂ S.f₁₂ S.comm₁₂), (𝟙 F)) : (_, _) ⟶ (_, _))) ≫ c₁)
    (hc₃₂ : c₃ ≫ k₃₂ =
      ((Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor
        ⟨((S.X)).presheaf, ((S.X)).IsSheaf⟩)).map
        (((thickeningIdealMap S.i₂ S.i₃ S.f₂₃ S.comm₂₃), (𝟙 F)) : (_, _) ⟶ (_, _))) ≫ c₂)
    (E₂ : CategoryTheory.Abelian.YonedaExtension ((modulePushforward S.i₂).obj F)
      ((modulePushforward S.i₂).obj K₂) 0)
    (_hE₂ : (firstOrderExtensionAction S.i₂ F K₂ S.firstOrder₂ E₂).val = c₂)
    (E₁ : CategoryTheory.Abelian.YonedaExtension ((modulePushforward S.i₁).obj F)
      ((modulePushforward S.i₁).obj K₁) 0)
    (_hE₁ : (firstOrderExtensionAction S.i₁ F K₁ S.firstOrder₁ E₁).val = c₁)
    (w : PushedExtension S.i₁ S.i₂ S.f₁₂ S.comm₁₂ F K₁ K₂ k₂₁ E₂ E₁)
    (hw : IsPushout E₂.f ((modulePushforward S.i₂).map k₂₁ ≫
        (thickeningPushforwardComp S.i₁ S.i₂ S.f₁₂ S.comm₁₂).inv.app K₁) w.hom
        ((modulePushforward S.f₁₂).map E₁.f))
    (hrestrict : (firstOrderExtensionAction S.i₃ F K₂ S.firstOrder₃
        (sequenceRestrictedExtension S F K₂ E₂)).val =
      ((Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor
        ⟨((S.X)).presheaf, ((S.X)).IsSheaf⟩)).map
        (((thickeningIdealMap S.i₂ S.i₃ S.f₂₃ S.comm₂₃), (𝟙 F)) : (_, _) ⟶ (_, _))) ≫ c₂) :
    (underlyingExtensionClass S.i₁ π S.firstOrder₁.1.1 F K₁ E₁).comp hK.extClass (by decide) =
      obstructionClass S.i₃ S.firstOrder₃ F K₃ c₃
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 91.4, Tag 08L3](https://stacks.math.columbia.edu/tag/08L3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
