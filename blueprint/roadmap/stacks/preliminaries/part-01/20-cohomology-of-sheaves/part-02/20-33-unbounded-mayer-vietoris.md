---
declaration: section
origin: cited
lean: Stacks.ExtensionByZero.distinguished_extensionRestriction_triangle, Stacks.ExtensionByZero.distinguished_derivedExtensionRestriction_triangle, Stacks.Duality.Coherator.isMayerVietorisApex_restrictPushforward_sup, Stacks.Duality.Coherator.isMayerVietorisApex_self, Stacks.Cohomology.MayerVietoris.exists_distinguished_triangle_of_cover, Stacks.Cohomology.MayerVietoris.exists_distinguished_triangle_of_cover_rightDerived, Stacks.ExtensionByZero.exists_mayerVietoris_ext_longExactSequence, Stacks.ExtensionByZero.exists_mayerVietoris_hom_longExactSequence
statement: formalized
proof: formalized
---

# 20.33 Unbounded Mayer-Vietoris

Section 20.33 of the Stacks Project, [Tag 08BR](https://stacks.math.columbia.edu/tag/08BR). 7 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08BU, a lemma

[Tag 08BU](https://stacks.math.columbia.edu/tag/08BU) in the Stacks Project.

**`Stacks.ExtensionByZero.distinguished_extensionRestriction_triangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/ExtensionByZero/MayerVietorisTriangle.lean, line 1386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/ExtensionByZero/MayerVietorisTriangle.lean#L1386). The attribute's comment: “the whole statement: the distinguished triangle, for every choice of the three derived functors `R(j_!j^*)` and their units — the degreewise one of Section 20.32 included — with the two maps out of the intersection term pinned by the adjunction counits, the second with the Mayer--Vietoris sign”.

> **Stacks 08BU.** For a cover by two open subspaces, extension by zero of the
> restrictions to their intersection and to the two opens forms a distinguished triangle,
> naturally in the object of the unbounded derived category.

```lean
public theorem distinguished_extensionRestriction_triangle {X : TopCat.{u}}
    (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u})
    (U V : Opens X) (hUV : U ⊔ V = ⊤)
    (DU DV DUV : DerivedCategory (SheafOfModules.{u} O) ⥤
      DerivedCategory (SheafOfModules.{u} O))
    (aU : homotopyExtensionRestriction O U ⟶ DerivedCategory.Qh ⋙ DU)
    (aV : homotopyExtensionRestriction O V ⟶ DerivedCategory.Qh ⋙ DV)
    (aUV : homotopyExtensionRestriction O (U ⊓ V) ⟶ DerivedCategory.Qh ⋙ DUV)
    [DU.IsRightDerivedFunctor aU
      (HomotopyCategory.quasiIso (SheafOfModules.{u} O) (ComplexShape.up ℤ))]
    [DV.IsRightDerivedFunctor aV
      (HomotopyCategory.quasiIso (SheafOfModules.{u} O) (ComplexShape.up ℤ))]
    [DUV.IsRightDerivedFunctor aUV
      (HomotopyCategory.quasiIso (SheafOfModules.{u} O) (ComplexShape.up ℤ))] :
    ∃ (iU : DUV ⟶ DU) (iV : DUV ⟶ DV)
      (δ : 𝟭 (DerivedCategory (SheafOfModules.{u} O)) ⟶
        DUV ⋙ shiftFunctor (DerivedCategory (SheafOfModules.{u} O)) (1 : ℤ)),
      (iU ≫ derivedExtensionRestrictionCounit O U DU aU =
          derivedExtensionRestrictionCounit O (U ⊓ V) DUV aUV) ∧
      (iV ≫ derivedExtensionRestrictionCounit O V DV aV =
          -derivedExtensionRestrictionCounit O (U ⊓ V) DUV aUV) ∧
      (∀ E, Triangle.mk (biprod.lift (iU.app E) (iV.app E))
        (biprod.desc ((derivedExtensionRestrictionCounit O U DU aU).app E)
          ((derivedExtensionRestrictionCounit O V DV aV).app E)) (δ.app E) ∈
          distTriang (DerivedCategory (SheafOfModules.{u} O)))
```

**`Stacks.ExtensionByZero.distinguished_derivedExtensionRestriction_triangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/ExtSequence.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/ExtSequence.lean#L383). The attribute's comment: “the whole statement at the presentation built in this file: the three clauses of `distinguished_extensionRestriction_triangle` for `derivedExtensionRestriction`, `derivedExtensionRestrictionFactorsh` and the instance `derivedExtensionRestriction_isRightDerivedFunctor`, with the maps to the identity functor the canonical derived adjunction counits of Stacks 08BT and the two maps out of the intersection term pinned by composing them with those counits, the second with the Mayer--Vietoris sign”.

> Let `X` be a ringed space which is the union of two open subspaces `U` and `V`. Then there
> are comparison maps out of `D(j_!)D(j^*)` for `U ∩ V` into the ones for `U` and for `V`, and a
> connecting transformation, such that for every object of `D(𝒪_X)` the resulting triangle is
> distinguished. The three derived functors are `derivedExtensionRestriction`, the maps to the
> identity functor are the canonical derived adjunction counits
> `derivedExtensionRestrictionCanonicalCounit`, and the two comparison maps are determined by
> composing them with those counits, the second with a sign.

```lean
public theorem distinguished_derivedExtensionRestriction_triangle {X : TopCat.{u}}
    (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u}) (U V : Opens X)
    (hUV : U ⊔ V = ⊤) :
    ∃ (iU : derivedExtensionRestriction O (U ⊓ V) ⟶ derivedExtensionRestriction O U)
      (iV : derivedExtensionRestriction O (U ⊓ V) ⟶ derivedExtensionRestriction O V)
      (δ : 𝟭 (DerivedCategory (SheafOfModules.{u} O)) ⟶
        derivedExtensionRestriction O (U ⊓ V) ⋙
          shiftFunctor (DerivedCategory (SheafOfModules.{u} O)) (1 : ℤ)),
      (iU ≫ derivedExtensionRestrictionCanonicalCounit O U =
          derivedExtensionRestrictionCanonicalCounit O (U ⊓ V)) ∧
      (iV ≫ derivedExtensionRestrictionCanonicalCounit O V =
          -derivedExtensionRestrictionCanonicalCounit O (U ⊓ V)) ∧
      (∀ E, Triangle.mk (biprod.lift (iU.app E) (iV.app E))
        (biprod.desc ((derivedExtensionRestrictionCanonicalCounit O U).app E)
          ((derivedExtensionRestrictionCanonicalCounit O V).app E)) (δ.app E) ∈
          distTriang (DerivedCategory (SheafOfModules.{u} O)))
```

## Tag 08BV, a lemma

[Tag 08BV](https://stacks.math.columbia.edu/tag/08BV) in the Stacks Project.

**`Stacks.Duality.Coherator.isMayerVietorisApex_restrictPushforward_sup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/UnboundedMayerVietoris.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/UnboundedMayerVietoris.lean#L77). The attribute's comment: “the scheme-level form: `U`, `V` opens of a scheme inside their union, with the terms `Rj_{W,*}(K|_W)` of `D(𝒪_X)` at the locally small model”.

> **[Stacks, Tag 08BV] for a scheme.** For opens `U`, `V` of a scheme `X` and any object `K` of
> the unbounded derived category `D(𝒪_X)` there is a distinguished triangle
>
> `Rj_{U ∪ V,*}(K|_{U ∪ V}) ⟶ Rj_{U,*}(K|_U) ⊕ Rj_{V,*}(K|_V) ⟶ Rj_{U ∩ V,*}(K|_{U ∩ V}) ⟶`
>
> in `D(𝒪_X)`, where `j_W : W → X` are the inclusions of the open subschemes.
>
> This is `Stacks.Duality.Coherator.exists_distTriang_restrictPushforward_sup`, read in the
> vocabulary of `Stacks.Duality.Coherator.IsMayerVietorisApex`.

```lean
theorem isMayerVietorisApex_restrictPushforward_sup (K : DerivedCategory X.Modules) :
    IsMayerVietorisApex X U V K (restrictPushforward (U ⊔ V) K)
```

**`Stacks.Duality.Coherator.isMayerVietorisApex_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/UnboundedMayerVietoris.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/UnboundedMayerVietoris.lean#L90). The attribute's comment: “the scheme-level form for a cover of the whole scheme, with `K` itself as the first term of the triangle”.

> **[Stacks, Tag 08BV] for a scheme, in the form of the source.** If the opens `U`, `V` cover the
> scheme `X`, then every object `K` of `D(𝒪_X)` itself sits in a distinguished triangle
>
> `K ⟶ Rj_{U,*}(K|_U) ⊕ Rj_{V,*}(K|_V) ⟶ Rj_{U ∩ V,*}(K|_{U ∩ V}) ⟶ K⟦1⟧`.
>
> This is `Stacks.Duality.Coherator.exists_distTriang_self`, read in the vocabulary of
> `Stacks.Duality.Coherator.IsMayerVietorisApex`.

```lean
theorem isMayerVietorisApex_self (hUV : U ⊔ V = ⊤) (K : DerivedCategory X.Modules) :
    IsMayerVietorisApex X U V K K
```

**`Stacks.Cohomology.MayerVietoris.exists_distinguished_triangle_of_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/MayerVietoris.lean, line 442](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/MayerVietoris.lean#L442).

> **Stacks 08BV.** A two-open cover gives a distinguished Mayer--Vietoris triangle, naturally
> in every object of the unbounded derived category of modules.

```lean
theorem exists_distinguished_triangle_of_cover
    (U V : Opens X) (hUV : U ⊔ V = ⊤)
    (RU RV RUV : DerivedCategory (SheafOfModules.{u} O) ⥤
      DerivedCategory (SheafOfModules.{u} O))
    (aU : homotopyToDerived O U ⟶ DerivedCategory.Qh ⋙ RU)
    (aV : homotopyToDerived O V ⟶ DerivedCategory.Qh ⋙ RV)
    (aUV : homotopyToDerived O (U ⊓ V) ⟶ DerivedCategory.Qh ⋙ RUV)
    [RU.IsRightDerivedFunctor aU
      (HomotopyCategory.quasiIso (SheafOfModules.{u} O) (ComplexShape.up ℤ))]
    [RV.IsRightDerivedFunctor aV
      (HomotopyCategory.quasiIso (SheafOfModules.{u} O) (ComplexShape.up ℤ))]
    [RUV.IsRightDerivedFunctor aUV
      (HomotopyCategory.quasiIso (SheafOfModules.{u} O) (ComplexShape.up ℤ))] :
    ∃ (qU : homotopyToDerived O U ⟶ homotopyToDerived O (U ⊓ V))
      (qV : homotopyToDerived O V ⟶ homotopyToDerived O (U ⊓ V))
      (rU : (CategoryTheory.Functor.id (DerivedCategory (SheafOfModules.{u} O)) :
        DerivedCategory (SheafOfModules.{u} O) ⥤
          DerivedCategory (SheafOfModules.{u} O)) ⟶ RU)
      (rV : (CategoryTheory.Functor.id (DerivedCategory (SheafOfModules.{u} O)) :
        DerivedCategory (SheafOfModules.{u} O) ⥤
          DerivedCategory (SheafOfModules.{u} O)) ⟶ RV)
      (dU : RU ⟶ RUV) (dV : RV ⟶ RUV)
      (δ : RUV ⟶ (CategoryTheory.Functor.id (DerivedCategory (SheafOfModules.{u} O)) :
          DerivedCategory (SheafOfModules.{u} O) ⥤
            DerivedCategory (SheafOfModules.{u} O)) ⋙
        shiftFunctor (DerivedCategory (SheafOfModules.{u} O)) (1 : ℤ)),
      homotopyRestriction O U ≫ qU = homotopyRestriction O (U ⊓ V) ∧
      homotopyRestriction O V ≫ qV = homotopyRestriction O (U ⊓ V) ∧
      homotopyRestriction O U ≫ aU = Functor.whiskerLeft DerivedCategory.Qh rU ∧
      homotopyRestriction O V ≫ aV = Functor.whiskerLeft DerivedCategory.Qh rV ∧
      qU ≫ aUV = aU ≫ Functor.whiskerLeft DerivedCategory.Qh dU ∧
      -(qV ≫ aUV) = aV ≫ Functor.whiskerLeft DerivedCategory.Qh dV ∧
      ∀ E, Triangle.mk (biprod.lift (rU.app E) (rV.app E))
        (biprod.desc (dU.app E) (dV.app E)) (δ.app E) ∈
          distTriang (DerivedCategory (SheafOfModules.{u} O))
```

**`Stacks.Cohomology.MayerVietoris.exists_distinguished_triangle_of_cover_rightDerived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/MayerVietorisCanonical.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/MayerVietorisCanonical.lean#L144). The attribute's comment: “the ringed-space form with the three derived pushforwards constructed by `rightDerivedRestrictPush`, at the standard model of `D(O)`: no derived functor, comparison map or derived-functor hypothesis is taken as a parameter”.

> **Stacks 08BV.** A two-open cover of a space carrying a sheaf of rings `O` gives a
> distinguished Mayer--Vietoris triangle
>
> `E ⟶ Rj_{U*}(E|_U) ⊞ Rj_{V*}(E|_V) ⟶ Rj_{(U ∩ V)*}(E|_{U ∩ V}) ⟶ E⟦1⟧`
>
> naturally in the object `E` of the unbounded derived category of `O`-modules, where the three
> derived pushforwards are the ones constructed by `rightDerivedRestrictPush`. The restriction maps
> `rU`, `rV`, the two difference maps `dU`, `dV` and the connecting map `δ` are maps of functors on
> `D(O)`, which is the naturality in `E`, and the equations preceding the triangle identify them
> with the restriction and transition maps of the cover through the canonical comparisons, so that
> the triangle's maps and its Mayer--Vietoris sign are retained rather than merely asserted to
> exist.

```lean
theorem exists_distinguished_triangle_of_cover_rightDerived
    (U V : Opens X) (hUV : U ⊔ V = ⊤) :
    ∃ (qU : homotopyToDerived O U ⟶ homotopyToDerived O (U ⊓ V))
      (qV : homotopyToDerived O V ⟶ homotopyToDerived O (U ⊓ V))
      (rU : (CategoryTheory.Functor.id (DerivedCategory (SheafOfModules.{u} O)) :
        DerivedCategory (SheafOfModules.{u} O) ⥤
          DerivedCategory (SheafOfModules.{u} O)) ⟶ rightDerivedRestrictPush O U)
      (rV : (CategoryTheory.Functor.id (DerivedCategory (SheafOfModules.{u} O)) :
        DerivedCategory (SheafOfModules.{u} O) ⥤
          DerivedCategory (SheafOfModules.{u} O)) ⟶ rightDerivedRestrictPush O V)
      (dU : rightDerivedRestrictPush O U ⟶ rightDerivedRestrictPush O (U ⊓ V))
      (dV : rightDerivedRestrictPush O V ⟶ rightDerivedRestrictPush O (U ⊓ V))
      (δ : rightDerivedRestrictPush O (U ⊓ V) ⟶
        (CategoryTheory.Functor.id (DerivedCategory (SheafOfModules.{u} O)) :
          DerivedCategory (SheafOfModules.{u} O) ⥤
            DerivedCategory (SheafOfModules.{u} O)) ⋙
        shiftFunctor (DerivedCategory (SheafOfModules.{u} O)) (1 : ℤ)),
      homotopyRestriction O U ≫ qU = homotopyRestriction O (U ⊓ V) ∧
      homotopyRestriction O V ≫ qV = homotopyRestriction O (U ⊓ V) ∧
      homotopyRestriction O U ≫ rightDerivedRestrictPushUnit O U =
        Functor.whiskerLeft DerivedCategory.Qh rU ∧
      homotopyRestriction O V ≫ rightDerivedRestrictPushUnit O V =
        Functor.whiskerLeft DerivedCategory.Qh rV ∧
      qU ≫ rightDerivedRestrictPushUnit O (U ⊓ V) =
        rightDerivedRestrictPushUnit O U ≫ Functor.whiskerLeft DerivedCategory.Qh dU ∧
      -(qV ≫ rightDerivedRestrictPushUnit O (U ⊓ V)) =
        rightDerivedRestrictPushUnit O V ≫ Functor.whiskerLeft DerivedCategory.Qh dV ∧
      ∀ E, Triangle.mk (biprod.lift (rU.app E) (rV.app E))
        (biprod.desc (dU.app E) (dV.app E)) (δ.app E) ∈
          distTriang (DerivedCategory (SheafOfModules.{u} O))
```

## Tag 08BW, a lemma

[Tag 08BW](https://stacks.math.columbia.edu/tag/08BW) in the Stacks Project.

**`Stacks.ExtensionByZero.exists_mayerVietoris_ext_longExactSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/ExtSequence.lean, line 426](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/ExtSequence.lean#L426). The attribute's comment: “long exact sequence of the Ext groups on the two opens and their intersection”.

> Let `X` be a ringed space covered by two open subspaces `U` and `V`, and let `E` and `F` be
> objects of `D(𝒪_X)`. There are restriction, difference and connecting homomorphisms making the
> Mayer--Vietoris sequence
>
> `⋯ ⟶ Ext^\{n-1}(E|\_\{U∩V}, F|\_\{U∩V}) ⟶ Ext^n(E, F) ⟶
>   Ext^n(E|\_U, F|\_U) × Ext^n(E|\_V, F|\_V) ⟶ Ext^n(E|\_\{U∩V}, F|\_\{U∩V}) ⟶ ⋯`
>
> exact at each of its three kinds of spot and in every integer degree, the Ext groups of the
> restrictions being taken in the derived categories of the open subspaces.

```lean
public theorem exists_mayerVietoris_ext_longExactSequence {X : TopCat.{u}}
    (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u}) (U V : Opens X) (hUV : U ⊔ V = ⊤)
    (E F : DerivedCategory (SheafOfModules.{u} O)) :
    ∃ (restriction : ∀ n : ℤ, (E ⟶ F⟦n⟧) →+
          (((derivedRestriction O U).obj E ⟶ ((derivedRestriction O U).obj F)⟦n⟧) ×
            ((derivedRestriction O V).obj E ⟶ ((derivedRestriction O V).obj F)⟦n⟧)))
      (difference : ∀ n : ℤ,
        (((derivedRestriction O U).obj E ⟶ ((derivedRestriction O U).obj F)⟦n⟧) ×
            ((derivedRestriction O V).obj E ⟶ ((derivedRestriction O V).obj F)⟦n⟧)) →+
          ((derivedRestriction O (U ⊓ V)).obj E ⟶
            ((derivedRestriction O (U ⊓ V)).obj F)⟦n⟧))
      (boundary : ∀ n : ℤ,
        ((derivedRestriction O (U ⊓ V)).obj E ⟶
          ((derivedRestriction O (U ⊓ V)).obj F)⟦n⟧) →+ (E ⟶ F⟦n + 1⟧)),
      ∀ n : ℤ, Function.Exact (restriction n) (difference n) ∧
        Function.Exact (difference n) (boundary n) ∧
        Function.Exact (boundary n) (restriction (n + 1))
```

**`Stacks.ExtensionByZero.exists_mayerVietoris_hom_longExactSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/ExtSequence.lean, line 491](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/ExtSequence.lean#L491). The attribute's comment: “long exact sequence, extension-by-zero form of the Ext groups”.

> Let `X` be a ringed space covered by two open subspaces `U` and `V`, and let `E` and `F` be
> objects of `D(𝒪_X)`. For every choice of the three derived functors of extension by zero of the
> restrictions there are comparison maps `iU` and `iV` out of the functor attached to `U ∩ V`,
> compatible with the canonical derived adjunction counits and carrying the Mayer--Vietoris sign,
> and connecting homomorphisms, such that the Mayer--Vietoris sequence
>
> `⋯ ⟶ Ext^\{n-1}(j\_\{U∩V,!}E|\_\{U∩V}, F) ⟶ Ext^n(E, F) ⟶
>   Ext^n(j\_\{U!}E|\_U, F) × Ext^n(j\_\{V!}E|\_V, F) ⟶ Ext^n(j\_\{U∩V,!}E|\_\{U∩V}, F) ⟶ ⋯`
>
> is exact at each of its three kinds of spot and in every integer degree.

```lean
public theorem exists_mayerVietoris_hom_longExactSequence {X : TopCat.{u}}
    (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u})
    (U V : Opens X) (hUV : U ⊔ V = ⊤)
    (DU DV DUV : DerivedCategory (SheafOfModules.{u} O) ⥤
      DerivedCategory (SheafOfModules.{u} O))
    (aU : homotopyExtensionRestriction O U ⟶ DerivedCategory.Qh ⋙ DU)
    (aV : homotopyExtensionRestriction O V ⟶ DerivedCategory.Qh ⋙ DV)
    (aUV : homotopyExtensionRestriction O (U ⊓ V) ⟶ DerivedCategory.Qh ⋙ DUV)
    [DU.IsRightDerivedFunctor aU
      (HomotopyCategory.quasiIso (SheafOfModules.{u} O) (ComplexShape.up ℤ))]
    [DV.IsRightDerivedFunctor aV
      (HomotopyCategory.quasiIso (SheafOfModules.{u} O) (ComplexShape.up ℤ))]
    [DUV.IsRightDerivedFunctor aUV
      (HomotopyCategory.quasiIso (SheafOfModules.{u} O) (ComplexShape.up ℤ))] :
    ∃ (iU : DUV ⟶ DU) (iV : DUV ⟶ DV)
      (boundary : ∀ (E F : DerivedCategory (SheafOfModules.{u} O)) (n : ℤ),
        (DUV.obj E ⟶ F⟦n⟧) →+ (E ⟶ F⟦n + 1⟧)),
      (iU ≫ derivedExtensionRestrictionCounit O U DU aU =
          derivedExtensionRestrictionCounit O (U ⊓ V) DUV aUV) ∧
      (iV ≫ derivedExtensionRestrictionCounit O V DV aV =
          -derivedExtensionRestrictionCounit O (U ⊓ V) DUV aUV) ∧
      ∀ (E F : DerivedCategory (SheafOfModules.{u} O)) (n : ℤ),
        Function.Exact
            (fun x : E ⟶ F⟦n⟧ =>
              ((derivedExtensionRestrictionCounit O U DU aU).app E ≫ x,
                (derivedExtensionRestrictionCounit O V DV aV).app E ≫ x))
            (fun w : (DU.obj E ⟶ F⟦n⟧) × (DV.obj E ⟶ F⟦n⟧) =>
              iU.app E ≫ w.1 + iV.app E ≫ w.2) ∧
          Function.Exact
            (fun w : (DU.obj E ⟶ F⟦n⟧) × (DV.obj E ⟶ F⟦n⟧) =>
              iU.app E ≫ w.1 + iV.app E ≫ w.2)
            (boundary E F n) ∧
          Function.Exact (boundary E F n)
            (fun x : E ⟶ F⟦n + 1⟧ =>
              ((derivedExtensionRestrictionCounit O U DU aU).app E ≫ x,
                (derivedExtensionRestrictionCounit O V DV aV).app E ≫ x))
```

**`Stacks.ExtensionByZero.exists_mayerVietoris_ext_longExactSequence_restrictions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/ExtSequenceRestrictions.lean, line 495](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/ExtSequenceRestrictions.lean#L495). The attribute's comment: “the long exact sequence, with its first map the pair of the restrictions to the two opens and its second map the difference of two restrictions to their intersection”.

> **Stacks 08BW, with every map of the sequence named.** For a ringed space covered by two
> open subspaces `U` and `V` and objects `E`, `F` of `D(𝒪_X)`, the Mayer--Vietoris sequence
>
> `⋯ ⟶ Ext^\{n-1}(E|\_\{U∩V}, F|\_\{U∩V}) ⟶ Ext^n(E, F) ⟶
>   Ext^n(E|\_U, F|\_U) × Ext^n(E|\_V, F|\_V) ⟶ Ext^n(E|\_\{U∩V}, F|\_\{U∩V}) ⟶ ⋯`
>
> is exact at each of its three kinds of spot and in every integer degree, its first map is
> the pair of the two restrictions and its second map is the difference of two further
> restrictions to the intersection.

```lean
theorem exists_mayerVietoris_ext_longExactSequence_restrictions (hUV : U ⊔ V = ⊤) :
    ∃ (restriction : ∀ (E F : DerivedCategory (SheafOfModules.{u} O)) (n : ℤ),
          (E ⟶ F⟦n⟧) →+
            (ShiftedHom ((derivedRestriction O U).obj E) ((derivedRestriction O U).obj F) n ×
              ShiftedHom ((derivedRestriction O V).obj E)
                ((derivedRestriction O V).obj F) n))
      (restrictionUW : ∀ (E F : DerivedCategory (SheafOfModules.{u} O)) (n : ℤ),
          ShiftedHom ((derivedRestriction O U).obj E) ((derivedRestriction O U).obj F) n →+
            ShiftedHom ((derivedRestriction O (U ⊓ V)).obj E)
              ((derivedRestriction O (U ⊓ V)).obj F) n)
      (restrictionVW : ∀ (E F : DerivedCategory (SheafOfModules.{u} O)) (n : ℤ),
          ShiftedHom ((derivedRestriction O V).obj E) ((derivedRestriction O V).obj F) n →+
            ShiftedHom ((derivedRestriction O (U ⊓ V)).obj E)
              ((derivedRestriction O (U ⊓ V)).obj F) n)
      (difference : ∀ (E F : DerivedCategory (SheafOfModules.{u} O)) (n : ℤ),
          (ShiftedHom ((derivedRestriction O U).obj E) ((derivedRestriction O U).obj F) n ×
              ShiftedHom ((derivedRestriction O V).obj E)
                ((derivedRestriction O V).obj F) n) →+
            ShiftedHom ((derivedRestriction O (U ⊓ V)).obj E)
              ((derivedRestriction O (U ⊓ V)).obj F) n)
      (boundary : ∀ (E F : DerivedCategory (SheafOfModules.{u} O)) (n : ℤ),
          ShiftedHom ((derivedRestriction O (U ⊓ V)).obj E)
              ((derivedRestriction O (U ⊓ V)).obj F) n →+ (E ⟶ F⟦n + 1⟧)),
      (∀ (E F : DerivedCategory (SheafOfModules.{u} O)) (n : ℤ) (x : E ⟶ F⟦n⟧),
          restriction E F n x =
            (ShiftedHom.map x (derivedRestriction O U),
              ShiftedHom.map x (derivedRestriction O V))) ∧
      (∀ (E F : DerivedCategory (SheafOfModules.{u} O)) (n : ℤ) (x : E ⟶ F⟦n⟧),
          restrictionUW E F n (ShiftedHom.map x (derivedRestriction O U)) =
            ShiftedHom.map x (derivedRestriction O (U ⊓ V))) ∧
      (∀ (E F : DerivedCategory (SheafOfModules.{u} O)) (n : ℤ) (x : E ⟶ F⟦n⟧),
          restrictionVW E F n (ShiftedHom.map x (derivedRestriction O V)) =
            ShiftedHom.map x (derivedRestriction O (U ⊓ V))) ∧
      (∀ (E F : DerivedCategory (SheafOfModules.{u} O)) (n : ℤ)
          (xU : ShiftedHom ((derivedRestriction O U).obj E)
            ((derivedRestriction O U).obj F) n)
          (xV : ShiftedHom ((derivedRestriction O V).obj E)
            ((derivedRestriction O V).obj F) n),
          difference E F n (xU, xV) =
            restrictionUW E F n xU - restrictionVW E F n xV) ∧
      (∀ (E F : DerivedCategory (SheafOfModules.{u} O)) (n : ℤ),
          Function.Exact (restriction E F n) (difference E F n)) ∧
      (∀ (E F : DerivedCategory (SheafOfModules.{u} O)) (n : ℤ),
          Function.Exact (difference E F n) (boundary E F n)) ∧
      (∀ (E F : DerivedCategory (SheafOfModules.{u} O)) (n : ℤ),
          Function.Exact (boundary E F n) (restriction E F (n + 1)))
```

## Tag 08BX, a lemma

[Tag 08BX](https://stacks.math.columbia.edu/tag/08BX) in the Stacks Project.

**`Stacks.Cohomology.LinearMayerVietoris.linearUnboundedMayerVietoris`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/LinearUnboundedTriangle.lean, line 849](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/LinearUnboundedTriangle.lean#L849). The attribute's comment: “the triangle in D(A), A = Γ(X, 𝒪\_X)”.

> Let `X` be a ringed space covered by two open subsets `U` and `V`, and let `A = Γ(X, 𝒪_X)`.
> The restriction maps of the `A`-linear derived sections functors, with the usual sign on the
> overlap, fit into a distinguished triangle in the derived category of `A`-modules, naturally in
> the object of `D(𝒪_X)`: the connecting map is a natural transformation and the other four maps
> are the right-derived restrictions.

```lean
theorem linearUnboundedMayerVietoris (hUV : U ⊔ V = ⊤) :
    ∃ δ : derivedLinearSections X (U ⊓ V) ⟶ derivedLinearSections X ⊤ ⋙
          shiftFunctor (DerivedCategory (ModuleCat.{u} (baseRing X))) (1 : ℤ),
      ∀ E, Triangle.mk
        (biprod.lift ((derivedLinearRestriction X (le_top : U ≤ ⊤)).app E)
          ((derivedLinearRestriction X (le_top : V ≤ ⊤)).app E))
        (biprod.desc ((derivedLinearRestriction X (inf_le_left : U ⊓ V ≤ U)).app E)
          (-((derivedLinearRestriction X (inf_le_right : U ⊓ V ≤ V)).app E)))
        (δ.app E) ∈ distTriang (DerivedCategory (ModuleCat.{u} (baseRing X)))
```

**`Stacks.Cohomology.SpaceMayerVietoris.relativeUnboundedMayerVietoris`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/UnboundedDerivedSections.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/UnboundedDerivedSections.lean#L283). The attribute's comment: “for a pair of opens covering an arbitrary open, not only the whole space”.

> **Stacks 08BX for a cover of an arbitrary open.** Let `X` be a ringed space and let
> `W = U ∪ V` be an open subset written as the union of two open subsets.  For any choice of
> derived sections functors over `W`, `U`, `V` and `U ∩ V` — that is, any right derived functors
> of degreewise sections along the quasi-isomorphisms — the right-derived restriction maps, with
> the usual sign on the overlap, fit into a distinguished triangle in the derived category of
> abelian groups, naturally in the object of `D(𝒪_X)`: the connecting map is a natural
> transformation and the other four maps are natural transformations of the given functors.
> Applying the cohomological functors gives the functorial Mayer--Vietoris long exact
> sequence.

```lean
public theorem relativeUnboundedMayerVietoris (X : RingedSpace.{u, u})
    (U V W : Opens X.carrier) (hUV : U ⊔ V = W)
    (RW RU RV RUV : DerivedCategory (ModuleSheaves X) ⥤ DerivedCategory AddCommGrpCat.{u})
    (aW : sectionsComplexDerived X W ⟶ DerivedCategory.Q ⋙ RW)
    (aU : sectionsComplexDerived X U ⟶ DerivedCategory.Q ⋙ RU)
    (aV : sectionsComplexDerived X V ⟶ DerivedCategory.Q ⋙ RV)
    (aUV : sectionsComplexDerived X (U ⊓ V) ⟶ DerivedCategory.Q ⋙ RUV)
    [RW.IsRightDerivedFunctor aW
      (HomologicalComplex.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))]
    [RU.IsRightDerivedFunctor aU
      (HomologicalComplex.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))]
    [RV.IsRightDerivedFunctor aV
      (HomologicalComplex.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))]
    [RUV.IsRightDerivedFunctor aUV
      (HomologicalComplex.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))] :
    ∃ δ : RUV ⟶ RW ⋙ shiftFunctor (DerivedCategory AddCommGrpCat.{u}) (1 : ℤ),
      ∀ E, Triangle.mk
        (biprod.lift
          ((RW.rightDerivedNatTrans RU aW aU
            (HomologicalComplex.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))
            (sectionsRestrictionDerived X (homOfLE (le_sup_left.trans hUV.le : U ≤ W)))).app E)
          ((RW.rightDerivedNatTrans RV aW aV
            (HomologicalComplex.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))
            (sectionsRestrictionDerived X (homOfLE (le_sup_right.trans hUV.le : V ≤ W)))).app E))
        (biprod.desc
          ((RU.rightDerivedNatTrans RUV aU aUV
            (HomologicalComplex.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))
            (sectionsRestrictionDerived X (homOfLE (inf_le_left : U ⊓ V ≤ U)))).app E)
          (-((RV.rightDerivedNatTrans RUV aV aUV
            (HomologicalComplex.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))
            (sectionsRestrictionDerived X (homOfLE (inf_le_right : U ⊓ V ≤ V)))).app E)))
        (δ.app E) ∈ distTriang (DerivedCategory AddCommGrpCat.{u})
```

**`Stacks.Cohomology.SpaceMayerVietoris.unboundedMayerVietoris`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/UnboundedDerivedSections.lean, line 431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/UnboundedDerivedSections.lean#L431).

> **Stacks 08BX.** Let `X` be a ringed space covered by two open subsets `U` and `V`.  For
> any choice of derived sections functors over `X`, `U`, `V` and `U ∩ V` — that is, any right
> derived functors of degreewise sections along the quasi-isomorphisms — the right-derived
> restriction maps, with the usual sign on the overlap, fit into a distinguished triangle in the
> derived category of abelian groups, naturally in the object of `D(𝒪_X)`: the connecting map is
> a natural transformation and the other four maps are natural transformations of the given
> functors.  Applying the cohomological functors gives the functorial Mayer--Vietoris long exact
> sequence.

```lean
public theorem unboundedMayerVietoris (X : RingedSpace.{u, u}) (U V : Opens X.carrier)
    (hUV : U ⊔ V = ⊤)
    (RX RU RV RUV : DerivedCategory (ModuleSheaves X) ⥤ DerivedCategory AddCommGrpCat.{u})
    (aX : sectionsComplexDerived X ⊤ ⟶ DerivedCategory.Q ⋙ RX)
    (aU : sectionsComplexDerived X U ⟶ DerivedCategory.Q ⋙ RU)
    (aV : sectionsComplexDerived X V ⟶ DerivedCategory.Q ⋙ RV)
    (aUV : sectionsComplexDerived X (U ⊓ V) ⟶ DerivedCategory.Q ⋙ RUV)
    [RX.IsRightDerivedFunctor aX
      (HomologicalComplex.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))]
    [RU.IsRightDerivedFunctor aU
      (HomologicalComplex.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))]
    [RV.IsRightDerivedFunctor aV
      (HomologicalComplex.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))]
    [RUV.IsRightDerivedFunctor aUV
      (HomologicalComplex.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))] :
    ∃ δ : RUV ⟶ RX ⋙ shiftFunctor (DerivedCategory AddCommGrpCat.{u}) (1 : ℤ),
      ∀ E, Triangle.mk
        (biprod.lift
          ((RX.rightDerivedNatTrans RU aX aU
            (HomologicalComplex.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))
            (sectionsRestrictionDerived X (homOfLE (le_top : U ≤ ⊤)))).app E)
          ((RX.rightDerivedNatTrans RV aX aV
            (HomologicalComplex.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))
            (sectionsRestrictionDerived X (homOfLE (le_top : V ≤ ⊤)))).app E))
        (biprod.desc
          ((RU.rightDerivedNatTrans RUV aU aUV
            (HomologicalComplex.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))
            (sectionsRestrictionDerived X (homOfLE (inf_le_left : U ⊓ V ≤ U)))).app E)
          (-((RV.rightDerivedNatTrans RUV aV aUV
            (HomologicalComplex.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))
            (sectionsRestrictionDerived X (homOfLE (inf_le_right : U ⊓ V ≤ V)))).app E)))
        (δ.app E) ∈ distTriang (DerivedCategory AddCommGrpCat.{u})
```

## Tag 08HZ, a lemma

[Tag 08HZ](https://stacks.math.columbia.edu/tag/08HZ) in the Stacks Project.

**`Stacks.Cohomology.RelativeMayerVietoris.canonicalPushforwardTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/RelativeMayerVietoris/CanonicalDerivedTriangle.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/RelativeMayerVietoris/CanonicalDerivedTriangle.lean#L139). The attribute's comment: “the triangle with no choices: the canonical derived functors of `canonicalRightDerived` and the canonical sequence of Tag 01EC, which is the form in which two such triangles can be compared”.

> The relative Mayer--Vietoris triangle built from the canonical derived functors and the
> canonical relative Mayer--Vietoris sequence is distinguished at every object of the unbounded
> derived category.

```lean
public theorem canonicalPushforwardTriangle_distinguished
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    canonicalPushforwardTriangle f iU iV iW cover intersection E ∈
      distTriang (DerivedCategory (SheafOfModules.{u} (structureSheafRing Y)))
```

**`Stacks.Cohomology.RelativeMayerVietoris.unboundedRelativeMayerVietoris`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/RelativeMayerVietoris/UnboundedDerivedPushforward.lean, line 906](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/RelativeMayerVietoris/UnboundedDerivedPushforward.lean#L906).

> **Stacks 08HZ.** For a morphism of ringed spaces and a cover of its source by two open
> subsets, the four derived pushforwards attached to the cover fit into a distinguished triangle,
> naturally in the object of the unbounded derived category.  The four derived pushforwards are
> hypothesised only through `CategoryTheory.Functor.IsRightDerivedFunctor`, so the statement
> applies to every choice of them; applying a cohomological functor to the triangle gives the
> relative Mayer--Vietoris long exact sequence.

```lean
public theorem unboundedRelativeMayerVietoris (f : X ⟶ Y) (U V : Opens X) (hUV : U ⊔ V = ⊤)
    (Rf RU RV RUV : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)) ⥤
      DerivedCategory (SheafOfModules.{u} (structureSheafRing Y)))
    (af : homotopyToDerived (modulePushforward f) ⟶ DerivedCategory.Qh ⋙ Rf)
    (aU : homotopyToDerived (restrictedPushforward f U) ⟶ DerivedCategory.Qh ⋙ RU)
    (aV : homotopyToDerived (restrictedPushforward f V) ⟶ DerivedCategory.Qh ⋙ RV)
    (aUV : homotopyToDerived (restrictedPushforward f (U ⊓ V)) ⟶ DerivedCategory.Qh ⋙ RUV)
    [Rf.IsRightDerivedFunctor af (HomotopyCategory.quasiIso _ (ComplexShape.up ℤ))]
    [RU.IsRightDerivedFunctor aU (HomotopyCategory.quasiIso _ (ComplexShape.up ℤ))]
    [RV.IsRightDerivedFunctor aV (HomotopyCategory.quasiIso _ (ComplexShape.up ℤ))]
    [RUV.IsRightDerivedFunctor aUV (HomotopyCategory.quasiIso _ (ComplexShape.up ℤ))] :
    ∃ (rU : Rf ⟶ RU) (rV : Rf ⟶ RV) (dU : RU ⟶ RUV) (dV : RV ⟶ RUV)
      (δ : RUV ⟶ Rf ⋙ shiftFunctor
        (DerivedCategory (SheafOfModules.{u} (structureSheafRing Y))) (1 : ℤ)),
      ∀ E, Triangle.mk (biprod.lift (rU.app E) (rV.app E))
        (biprod.desc (dU.app E) (dV.app E)) (δ.app E) ∈
          distTriang (DerivedCategory (SheafOfModules.{u} (structureSheafRing Y)))
```

**`Stacks.Cohomology.RelativeMayerVietoris.pushforwardTriangleMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/RelativeMayerVietoris/UnboundedDerivedPushforward.lean, line 1046](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/RelativeMayerVietoris/UnboundedDerivedPushforward.lean#L1046). The attribute's comment: “functoriality of the triangle in `E`: the lemma's second assertion, which the existential form above cannot express because it hides the morphisms”.

> The relative Mayer--Vietoris triangle is functorial in the derived object: a morphism
> `e : E ⟶ E'` induces a morphism of triangles whose components are the four derived functors
> applied to `e`.

```lean
public def pushforwardTriangleMap
    {E E' : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))} (e : E ⟶ E') :
    pushforwardTriangle f iU iV iW S Rf RU RV RUV af aU aV aUV E ⟶
      pushforwardTriangle f iU iV iW S Rf RU RV RUV af aU aV aUV E'
```

## Tag 08DF, a lemma

[Tag 08DF](https://stacks.math.columbia.edu/tag/08DF) in the Stacks Project.

**`Stacks.Cohomology.PushforwardRestriction.isIso_derivedOpenPushforward_restrictionUnit_app_of_supported`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/PushforwardAndRestriction.lean, line 1067](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/PushforwardAndRestriction.lean#L1067). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 08DF, part (1).** Let `j : U → X` be the inclusion of an open
> subspace of a ringed space and `T ⊆ U` a closed subset of `X`. If every cohomology sheaf of
> `E ∈ D(O_X)` is supported on `T`, then the canonical map `E ⟶ Rj_*(E|_U)` is an
> isomorphism.

```lean
theorem isIso_derivedOpenPushforward_restrictionUnit_app_of_supported
    {X : TopCat.{u}} (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u})
    (U : Opens X) (T : Set X) (hT : IsClosed T) (hTU : T ⊆ U)
    [HasDerivedCategory (SheafOfModules.{u} O)]
    [HasDerivedCategory (SheafOfModules.{u} (resRing U O))]
    (E : DerivedCategory (SheafOfModules.{u} O))
    (hE : CohomologySupportedOn O T E) :
    IsIso ((derivedPushforwardRestrictionUnit O U (derivedOpenPushforward O U)
      (derivedOpenPushforwardUnit O U)).app E)
```

**`Stacks.Cohomology.PushforwardRestriction.isIso_extensionByZeroToDerivedOpenPushforward_app_of_supported`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/PushforwardAndRestriction.lean, line 1084](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/PushforwardAndRestriction.lean#L1084). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 08DF, part (2).** Let `j : U → X` be the inclusion of an open
> subspace of a ringed space and `T ⊆ U` a closed subset of `X`. If every cohomology sheaf of
> `F ∈ D(O_U)` is supported on `T`, then the canonical map `j_! F ⟶ Rj_* F` is an
> isomorphism.

```lean
theorem isIso_extensionByZeroToDerivedOpenPushforward_app_of_supported
    {X : TopCat.{u}} (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u})
    (U : Opens X) (T : Set X) (hT : IsClosed T) (hTU : T ⊆ U)
    [HasDerivedCategory (SheafOfModules.{u} O)]
    [HasDerivedCategory (SheafOfModules.{u} (resRing U O))]
    (F : DerivedCategory (SheafOfModules.{u} (resRing U O)))
    (hF : CohomologySupportedOn (resRing U O)
      ((fun x : Usp U ↦ x.1) ⁻¹' T) F) :
    IsIso ((extensionByZeroToDerivedPushforward O U (derivedOpenPushforward O U)
      (derivedOpenPushforwardUnit O U)).app F)
```

## Tag 0G6X, a lemma

[Tag 0G6X](https://stacks.math.columbia.edu/tag/0G6X) in the Stacks Project.

**`Stacks.Cohomology.LinearCupProductTriangle.linearCupProductMayerVietoris`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/LinearCupProductTriangle.lean, line 717](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/LinearCupProductTriangle.lean#L717). The attribute's comment: “the map of triangles, with the vertices read on the chosen representatives”.

> **Stacks 0G6X.**  Let `(X, 𝒪_X)` be a ringed space, `A = Γ(X, 𝒪_X)`, and let
> `X = U ∪ V` be a union of two open subsets.  For a choice of resolutions of two complexes `K`
> and `M` of `𝒪_X`-modules there is a map of distinguished triangles in `D(A)` from the
> Mayer--Vietoris triangle of `RΓ(X, K) ⊗^𝐋_A RΓ(-, M)` to the Mayer--Vietoris triangle of
> `RΓ(-, K ⊗^𝐋_{𝒪_X} M)` whose three vertical maps are the cup products over `X`, over `U` and
> `V`, and over `U ∩ V`.

```lean
theorem linearCupProductMayerVietoris (hUV : U ⊔ V = ⊤) :
    cupSourceTriangle U V d hUV ∈ distTriang (DerivedCategory (ModuleCat.{u} (baseRing X))) ∧
      cupTargetTriangle U V d hUV ∈
          distTriang (DerivedCategory (ModuleCat.{u} (baseRing X))) ∧
        (tensorRepresentative d).map
              (DerivedCategory.Q.map (coverFirstComplex X U V d.inj)) ≫
            derivedCupMiddle U V d =
          derivedCupMap d ⊤ ≫ DerivedCategory.Q.map (coverFirstComplex X U V d.tgt) ∧
        (tensorRepresentative d).map
              (DerivedCategory.Q.map (coverSecondComplex X U V d.inj)) ≫
            derivedCupMap d (U ⊓ V) =
          derivedCupMiddle U V d ≫ DerivedCategory.Q.map (coverSecondComplex X U V d.tgt) ∧
        cupBoundary U V d hUV ≫
            (shiftFunctor (DerivedCategory (ModuleCat.{u} (baseRing X))) (1 : ℤ)).map
              (derivedCupMap d ⊤) =
          derivedCupMap d (U ⊓ V) ≫
            DerivedCategory.triangleOfSESδ (shortExact_cupTarget U V d hUV)
```

**`Stacks.Cohomology.LinearCupProductTriangle.exists_cupData_linearCupProductMayerVietoris`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/LinearCupProductTriangle.lean, line 742](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/LinearCupProductTriangle.lean#L742). The attribute's comment: “for arbitrary complexes, after replacing K by a K-injective resolution”.

> **Stacks 0G6X for arbitrary complexes.**  Every complex `K` of `𝒪_X`-modules admits a
> quasi-isomorphism into a complex carrying a choice of resolutions, so that the map of
> Mayer--Vietoris triangles above exists for every object of `D(𝒪_X)`.

```lean
theorem exists_cupData_linearCupProductMayerVietoris (hUV : U ⊔ V = ⊤)
    (K M : CochainComplex (Modules X) ℤ) :
    ∃ (K' : CochainComplex (Modules X) ℤ) (e : K ⟶ K') (d : CupData X K' M), QuasiIso e ∧
      cupSourceTriangle U V d hUV ∈
          distTriang (DerivedCategory (ModuleCat.{u} (baseRing X))) ∧
        cupTargetTriangle U V d hUV ∈
            distTriang (DerivedCategory (ModuleCat.{u} (baseRing X))) ∧
          (tensorRepresentative d).map
                (DerivedCategory.Q.map (coverFirstComplex X U V d.inj)) ≫
              derivedCupMiddle U V d =
            derivedCupMap d ⊤ ≫ DerivedCategory.Q.map (coverFirstComplex X U V d.tgt) ∧
          (tensorRepresentative d).map
                (DerivedCategory.Q.map (coverSecondComplex X U V d.inj)) ≫
              derivedCupMap d (U ⊓ V) =
            derivedCupMiddle U V d ≫ DerivedCategory.Q.map (coverSecondComplex X U V d.tgt) ∧
          cupBoundary U V d hUV ≫
              (shiftFunctor (DerivedCategory (ModuleCat.{u} (baseRing X))) (1 : ℤ)).map
                (derivedCupMap d ⊤) =
            derivedCupMap d (U ⊓ V) ≫
              DerivedCategory.triangleOfSESδ (shortExact_cupTarget U V d hUV)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.33, Tag 08BR](https://stacks.math.columbia.edu/tag/08BR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
