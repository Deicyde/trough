---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.derivedSheafHomTensorEquiv, Stacks.SheafOfModules.derivedSheafHomGlobalSectionsEquiv, Stacks.SheafOfModules.derivedSheafHomSectionsEquiv, Stacks.SheafOfModules.derivedCurryingData, Stacks.SheafOfModules.derivedSheafHomRestrictionIso, Stacks.SheafOfModules.derivedSheafHomRestrictionIso_natural_left, Stacks.SheafOfModules.derivedSheafHomRestrictionIso_natural_right, Stacks.SheafOfModules.sheafHomRestrictionComplexMap_isRestriction
statement: formalized
proof: formalized
---

# 20.42 Internal hom in the derived category

Section 20.42 of the Stacks Project, [Tag 08DH](https://stacks.math.columbia.edu/tag/08DH). 15 tags here are carried by 43 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08DI, an equation

[Tag 08DI](https://stacks.math.columbia.edu/tag/08DI) in the Stacks Project.

**`Stacks.SheafOfModules.derivedSheafHomTensorEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedInternalHom.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedInternalHom.lean#L144).

> **Stacks 08DI.** For objects `K`, `L`, `M` of `D(O_X)` on a ringed space, morphisms into the
> derived internal hom are canonically identified with morphisms out of the derived tensor
> product,
>
> `Hom_{D(O_X)}(K, RSheafHom(L, M)) = Hom_{D(O_X)}(K ⊗^L_{O_X} L, M)`,
>
> as an isomorphism of abelian groups.

```lean
def derivedSheafHomTensorEquiv (K L M : DerivedCategory (StructureSheafModules Rc)) :
    (K ⟶ ((derivedSheafHom Rc).obj (op L)).obj M) ≃+
      (((derivedTensor Rc).obj K).obj L ⟶ M)
```

## Tag 08DK, a lemma

[Tag 08DK](https://stacks.math.columbia.edu/tag/08DK) in the Stacks Project.

**`Stacks.SheafOfModules.derivedSheafHomGlobalSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedCategorySections.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedCategorySections.lean#L79). The attribute's comment: “global sections”.

> **Stacks 08DK globally.** For objects `L`, `M` of `D(O_X)` the degree-zero global
> hypercohomology of the derived internal Hom `RSheafHom(L, M)` is the group of morphisms
> `L ⟶ M` in the derived category of `O_X`-modules.

```lean
def derivedSheafHomGlobalSectionsEquiv (L M : DerivedCategory (StructureSheafModules Rc)) :
    ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
        ((derivedModuleGlobalSections (ringedSite Rc)).obj
          (((RingedSite.derivedSheafHomBifunctor (ringedSite Rc)).obj (op L)).obj M)) :
        Type u) ≃+ (L ⟶ M)
```

**`Stacks.SheafOfModules.derivedSheafHomSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedCategorySections.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedCategorySections.lean#L94). The attribute's comment: “sections over an open”.

> **Stacks 08DK over an open.** For objects `L`, `M` of `D(O_X)` and an open `U ⊆ X` the
> degree-zero hypercohomology over `U` of the derived internal Hom `RSheafHom(L, M)` is the group
> of morphisms `L|_U ⟶ M|_U` in the derived category of `O_U`-modules.

```lean
def derivedSheafHomSectionsEquiv (L M : DerivedCategory (StructureSheafModules Rc)) :
    ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
        ((Stacks.Cohomology.Localization.derivedSectionsOverObject (ringedSite Rc) U).obj
          (((RingedSite.derivedSheafHomBifunctor (ringedSite Rc)).obj (op L)).obj M)) :
        Type u) ≃+
      ((SheafOfModules.overFunctor.{u} (structureSheaf Rc) U).mapDerivedCategory.obj L ⟶
        (SheafOfModules.overFunctor.{u} (structureSheaf Rc) U).mapDerivedCategory.obj M)
```

## Tag 08DJ, a lemma

[Tag 08DJ](https://stacks.math.columbia.edu/tag/08DJ) in the Stacks Project.

**`Stacks.SheafOfModules.derivedCurryingData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedCurryingOnARingedSpace.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedCurryingOnARingedSpace.lean#L352). References: SGA 6 I (7.4), “first isomorphism”.

> **Stacks 08DJ.** Let `(X, O_X)` be a ringed space and let `K`, `L`, `M` be objects of
> `D(O_X)`. There is a canonical isomorphism
>
> `RSheafHom(K, RSheafHom(L, M)) ≅ RSheafHom(K ⊗^L_{O_X} L, M)`
>
> in `D(O_X)`, functorial in `K`, `L` and `M`, which recovers the tensor--internal-Hom bijection
> of Stacks 08DI on taking `H⁰(X, -)`.

```lean
def derivedCurryingData : DerivedCurryingData Rc
```

## Tag 08DL, a lemma

[Tag 08DL](https://stacks.math.columbia.edu/tag/08DL) in the Stacks Project.

**`Stacks.SheafOfModules.derivedSheafHomRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedRestrictionToOpens.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedRestrictionToOpens.lean#L129).

> **Stacks 08DL.** For objects `K`, `L` of `D(O_X)` the derived internal Hom commutes with
> restriction to an open `U`: restricting `RSheafHom(K, L)` to the opens contained in `U` gives the
> derived internal Hom `RSheafHom(K|_U, L|_U)` of the restrictions.

```lean
def derivedSheafHomRestrictionIso (K L : DerivedCategory (StructureSheafModules Rc)) :
    (derivedRestrict Rc U).obj
        (((RingedSite.derivedSheafHomBifunctor (ringedSite Rc)).obj (op K)).obj L) ≅
      ((RingedSite.derivedSheafHomBifunctor ((ringedSite Rc).over U)).obj
          (op ((derivedRestrict Rc U).obj K))).obj ((derivedRestrict Rc U).obj L)
```

**`Stacks.SheafOfModules.derivedSheafHomRestrictionIso_natural_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedRestrictionToOpens.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedRestrictionToOpens.lean#L158). The attribute's comment: “functoriality in the first variable”.

> The comparison of Stacks 08DL is natural in the contravariant variable: restricting the map
> `RSheafHom(K, L) ⟶ RSheafHom(K', L)` induced by `f : K' ⟶ K` gives the map induced by `f|_U`.

```lean
theorem derivedSheafHomRestrictionIso_natural_left
    {K K' L : DerivedCategory (StructureSheafModules Rc)} (f : K' ⟶ K) :
    (derivedRestrict Rc U).map
        (((RingedSite.derivedSheafHomBifunctor (ringedSite Rc)).map f.op).app L) ≫
        (derivedSheafHomRestrictionIso Rc U K' L).hom =
      (derivedSheafHomRestrictionIso Rc U K L).hom ≫
        ((RingedSite.derivedSheafHomBifunctor ((ringedSite Rc).over U)).map
          ((derivedRestrict Rc U).map f).op).app ((derivedRestrict Rc U).obj L)
```

**`Stacks.SheafOfModules.derivedSheafHomRestrictionIso_natural_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedRestrictionToOpens.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedRestrictionToOpens.lean#L171). The attribute's comment: “functoriality in the second variable”.

> The comparison of Stacks 08DL is natural in the covariant variable: restricting the map
> `RSheafHom(K, L) ⟶ RSheafHom(K, L')` induced by `g : L ⟶ L'` gives the map induced by `g|_U`.

```lean
theorem derivedSheafHomRestrictionIso_natural_right
    {K L L' : DerivedCategory (StructureSheafModules Rc)} (g : L ⟶ L') :
    (derivedRestrict Rc U).map
        (((RingedSite.derivedSheafHomBifunctor (ringedSite Rc)).obj (op K)).map g) ≫
        (derivedSheafHomRestrictionIso Rc U K L').hom =
      (derivedSheafHomRestrictionIso Rc U K L).hom ≫
        ((RingedSite.derivedSheafHomBifunctor ((ringedSite Rc).over U)).obj
          (op ((derivedRestrict Rc U).obj K))).map ((derivedRestrict Rc U).map g)
```

**`Stacks.SheafOfModules.sheafHomRestrictionComplexMap_isRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedRestrictionToOpens.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedRestrictionToOpens.lean#L202). The attribute's comment: “restriction of internal-Hom complexes”.

> On every local homogeneous cochain, the chain-level comparison of Stacks 08DL is the
> canonical restriction isomorphism of internal Homs of modules. This is what pins the comparison
> down: a cochain over `V ⊆ U` is sent to the cochain it already is, read along the identification
> of `Opens X / V` with the opens contained in `V` inside `Opens X / U`.

```lean
theorem sheafHomRestrictionComplexMap_isRestriction
    (A B : CochainComplex (StructureSheafModules Rc) ℤ) :
    RingedSite.IsInternalHomRestrictionMap (ringedSite Rc) U A B
      (sheafHomRestrictionComplexMap Rc U A B)
```

**`Stacks.SheafOfModules.derivedSheafHomRestrictionIso_model`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedRestrictionToOpens.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedRestrictionToOpens.lean#L212). The attribute's comment: “canonical model characterization”.

> On the classes of complexes `A` and `B` with `B` K-injective, both sides of Stacks 08DL are
> the class of an internal Hom complex, and the comparison is the class of the chain-level
> restriction map. Together with naturality this determines the comparison.

```lean
theorem derivedSheafHomRestrictionIso_model
    (A B : CochainComplex (SheafOfModules.{u} (Tensor.ringSheaf (ringedSite Rc).O)) ℤ)
    [B.IsKInjective] :
    letI : PreservesFiniteLimits
        (SheafOfModules.overFunctor.{u} (Tensor.ringSheaf (ringedSite Rc).O) U) :=
      ‹PreservesFiniteLimits (SheafOfModules.overFunctor.{u} (structureSheaf Rc) U)›
    letI : PreservesFiniteColimits
        (SheafOfModules.overFunctor.{u} (Tensor.ringSheaf (ringedSite Rc).O) U) :=
      ‹PreservesFiniteColimits (SheafOfModules.overFunctor.{u} (structureSheaf Rc) U)›
    (derivedSheafHomRestrictionIso Rc U
          (DerivedCategory.Q.obj A) (DerivedCategory.Q.obj B)).hom ≫
        (RingedSite.restrictionTargetComparison (ringedSite Rc) U A B).hom =
      (RingedSite.restrictionSourceComparison (ringedSite Rc) U A B).hom ≫
        DerivedCategory.Q.map (sheafHomRestrictionComplexMap Rc U A B)
```

## Tag 08I0, a lemma

[Tag 08I0](https://stacks.math.columbia.edu/tag/08I0) in the Stacks Project.

**`Stacks.SheafOfModules.exists_distinguished_derivedSheafHom_first`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedSheafHomExactness.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedSheafHomExactness.lean#L107). The attribute's comment: “exactness in the source”.

> **Stacks 08I0, exactness in the source.**  On a ringed space, the derived internal hom into a
> fixed object carries a distinguished triangle of `D(O_X)` to a distinguished triangle: the two
> morphisms `RSheafHom(T.obj₃, E) ⟶ RSheafHom(T.obj₂, E) ⟶ RSheafHom(T.obj₁, E)` induced by
> `T.mor₂` and `T.mor₁` extend by a connecting morphism to a distinguished triangle.
>
> The order of the two morphisms is reversed, which is the contravariance of the first variable.

```lean
theorem exists_distinguished_derivedSheafHom_first
    (E : DerivedCategory (StructureSheafModules Rc))
    (T : Triangle (DerivedCategory (StructureSheafModules Rc)))
    (hT : T ∈ distTriang (DerivedCategory (StructureSheafModules Rc))) :
    ∃ δ : ((derivedSheafHom Rc).flip.obj E).obj (op T.obj₁) ⟶
        (((derivedSheafHom Rc).flip.obj E).obj (op T.obj₃))⟦(1 : ℤ)⟧,
      Triangle.mk
        (((derivedSheafHom Rc).flip.obj E).map T.mor₂.op)
        (((derivedSheafHom Rc).flip.obj E).map T.mor₁.op)
        δ ∈ distTriang (DerivedCategory (StructureSheafModules Rc))
```

**`Stacks.SheafOfModules.exists_distinguished_derivedSheafHom_second`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedSheafHomExactness.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedSheafHomExactness.lean#L124). The attribute's comment: “exactness in the target”.

> **Stacks 08I0, exactness in the target.**  On a ringed space, the derived internal hom out of
> a fixed object carries a distinguished triangle of `D(O_X)` to a distinguished triangle: the two
> morphisms `RSheafHom(E, T.obj₁) ⟶ RSheafHom(E, T.obj₂) ⟶ RSheafHom(E, T.obj₃)` induced by
> `T.mor₁` and `T.mor₂` extend by a connecting morphism to a distinguished triangle.

```lean
theorem exists_distinguished_derivedSheafHom_second
    (E : DerivedCategory (StructureSheafModules Rc))
    (T : Triangle (DerivedCategory (StructureSheafModules Rc)))
    (hT : T ∈ distTriang (DerivedCategory (StructureSheafModules Rc))) :
    ∃ δ : ((derivedSheafHom Rc).obj (op E)).obj T.obj₃ ⟶
        (((derivedSheafHom Rc).obj (op E)).obj T.obj₁)⟦(1 : ℤ)⟧,
      Triangle.mk
        (((derivedSheafHom Rc).obj (op E)).map T.mor₁)
        (((derivedSheafHom Rc).obj (op E)).map T.mor₂)
        δ ∈ distTriang (DerivedCategory (StructureSheafModules Rc))
```

## Tag 0A8V, a lemma

[Tag 0A8V](https://stacks.math.columbia.edu/tag/0A8V) in the Stacks Project.

**`Stacks.SheafOfModules.derivedSheafHomComposition`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedComposition.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedComposition.lean#L100). The attribute's comment: “the canonical composition morphism”.

> For objects `K`, `L`, `M` of `D(O_X)` on a ringed space, the canonical composition morphism
>
> `RSheafHom(L, M) ⊗^L_{O_X} RSheafHom(K, L) ⟶ RSheafHom(K, M)`
>
> in `D(O_X)`, obtained from the composition morphism of internal Hom complexes after passing to
> K-injective representatives of `L` and `M` and a K-flat model of the internal Hom complex into
> the representative of `L`.

```lean
def derivedSheafHomComposition
    (K L M : DerivedCategory (_root_.SheafOfModules.{u} (Tensor.ringSheaf.{u, u, u} Rc))) :
    ((derivedTensor Rc).obj (((derivedSheafHom Rc).obj (op L)).obj M)).obj
        (((derivedSheafHom Rc).obj (op K)).obj L) ⟶
      ((derivedSheafHom Rc).obj (op K)).obj M
```

**`Stacks.SheafOfModules.derivedSheafHomComposition_natural_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedComposition.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedComposition.lean#L110). The attribute's comment: “functoriality in the source”.

> Derived composition is contravariant in the source object.

```lean
theorem derivedSheafHomComposition_natural_source
    {K K' : DerivedCategory (_root_.SheafOfModules.{u} (Tensor.ringSheaf.{u, u, u} Rc))}
    (k : K' ⟶ K)
    (L M : DerivedCategory (_root_.SheafOfModules.{u} (Tensor.ringSheaf.{u, u, u} Rc))) :
    derivedSheafHomComposition Rc K L M ≫ derivedSheafHomMap Rc k (𝟙 M) =
      derivedTensorMap Rc (𝟙 (((derivedSheafHom Rc).obj (op L)).obj M))
          (derivedSheafHomMap Rc k (𝟙 L)) ≫
        derivedSheafHomComposition Rc K' L M
```

**`Stacks.SheafOfModules.derivedSheafHomComposition_natural_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedComposition.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedComposition.lean#L123). The attribute's comment: “functoriality in the target”.

> Derived composition is covariant in the target object.

```lean
theorem derivedSheafHomComposition_natural_target
    (K L : DerivedCategory (_root_.SheafOfModules.{u} (Tensor.ringSheaf.{u, u, u} Rc)))
    {M M' : DerivedCategory (_root_.SheafOfModules.{u} (Tensor.ringSheaf.{u, u, u} Rc))}
    (m : M ⟶ M') :
    derivedSheafHomComposition Rc K L M ≫ derivedSheafHomMap Rc (𝟙 K) m =
      derivedTensorMap Rc (derivedSheafHomMap Rc (𝟙 L) m)
          (𝟙 (((derivedSheafHom Rc).obj (op K)).obj L)) ≫
        derivedSheafHomComposition Rc K L M'
```

**`Stacks.SheafOfModules.derivedSheafHomComposition_dinatural_middle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedComposition.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedComposition.lean#L138). The attribute's comment: “functoriality in the intermediate object”.

> Derived composition is dinatural in the intermediate object: a morphism `L ⟶ L'` may be
> absorbed covariantly into the left tensor factor or contravariantly into the right one, with the
> same result.

```lean
theorem derivedSheafHomComposition_dinatural_middle
    (K : DerivedCategory (_root_.SheafOfModules.{u} (Tensor.ringSheaf.{u, u, u} Rc)))
    {L L' : DerivedCategory (_root_.SheafOfModules.{u} (Tensor.ringSheaf.{u, u, u} Rc))}
    (l : L ⟶ L')
    (M : DerivedCategory (_root_.SheafOfModules.{u} (Tensor.ringSheaf.{u, u, u} Rc))) :
    derivedTensorMap Rc (𝟙 (((derivedSheafHom Rc).obj (op L')).obj M))
          (derivedSheafHomMap Rc (𝟙 K) l) ≫
        derivedSheafHomComposition Rc K L' M =
      derivedTensorMap Rc (derivedSheafHomMap Rc l (𝟙 M))
          (𝟙 (((derivedSheafHom Rc).obj (op K)).obj L)) ≫
        derivedSheafHomComposition Rc K L M
```

**`Stacks.SheafOfModules.derivedSheafHomComposition_kFlatModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedComposition.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedComposition.lean#L157). The attribute's comment: “comparison with composition of complexes”.

> On K-injective representatives `J` of `L` and `I` of `M` and any map `f` from a K-flat
> complex `H` to the internal Hom complex `SheafHom^•(K, J)`, derived composition is the class of
> the composition morphism of internal Hom complexes
> `Tot(SheafHom^•(J, I) ⊗_{O_X} SheafHom^•(K, J)) ⟶ SheafHom^•(K, I)`.

```lean
theorem derivedSheafHomComposition_kFlatModel
    (K J I H : CochainComplex (_root_.SheafOfModules.{u} (Tensor.ringSheaf.{u, u, u} Rc)) ℤ)
    [hJ : J.IsKInjective] [hI : I.IsKInjective] (hH : IsKFlat Rc H)
    (f : H ⟶ (sheafHomComplex Rc K J).obj) :
    ((derivedTensor Rc).obj
            (((derivedSheafHom Rc).obj (op (DerivedCategory.Q.obj J))).obj
              (DerivedCategory.Q.obj I))).map
          (DerivedCategory.Q.map f ≫
            (@RingedSite.derivedSheafHomComparison (ringedSite Rc) _ K J hJ).inv) ≫
        derivedSheafHomComposition Rc (DerivedCategory.Q.obj K) (DerivedCategory.Q.obj J)
          (DerivedCategory.Q.obj I) ≫
        (@RingedSite.derivedSheafHomComparison (ringedSite Rc) _ K I hI).hom =
      (RingedSite.derivedEvaluationSourceComparison (ringedSite Rc)
            (canonicalDerivedTensorProduct (ringedSite Rc)) (derivedInternalHom Rc)
            H J I hH).hom ≫
        DerivedCategory.Q.map (tensorTotalMap Rc (𝟙 (sheafHomComplex Rc J I).obj) f) ≫
        DerivedCategory.Q.map (RingedSite.compositionMap (ringedSite Rc) K J I)
```

## Tag 0BYS, a lemma

[Tag 0BYS](https://stacks.math.columbia.edu/tag/0BYS) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.derivedTensorHomDiagonal_natural_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonal.lean, line 519](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonal.lean#L519). The attribute's comment: “functoriality in the source of the internal Hom”.

> **Stacks 0BYS.** The diagonal morphism is contravariant in the source of the internal Hom,
> for an arbitrary morphism of `D(O)`.

```lean
theorem derivedTensorHomDiagonal_natural_hom (g : M' ⟶ M) :
    ((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K).map
          (((derivedSheafHomBifunctor X).map g.op).app L) ≫
        derivedTensorHomDiagonal X K L M' =
      derivedTensorHomDiagonal X K L M ≫
        ((derivedSheafHomBifunctor X).map g.op).app
          (((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K).obj L)
```

**`AlgebraicGeometry.RingedSite.derivedTensorHomDiagonal_natural_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonal.lean, line 684](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonal.lean#L684). The attribute's comment: “functoriality in the target of the internal Hom”.

> **Stacks 0BYS.** The diagonal morphism is covariant in the target of the internal Hom, for
> an arbitrary morphism of `D(O)`.

```lean
theorem derivedTensorHomDiagonal_natural_right (g : L ⟶ L') :
    ((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K).map
          (((derivedSheafHomBifunctor X).obj (op M)).map g) ≫
        derivedTensorHomDiagonal X K L' M =
      derivedTensorHomDiagonal X K L M ≫
        ((derivedSheafHomBifunctor X).obj (op M)).map
          (((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K).map g)
```

**`AlgebraicGeometry.RingedSite.derivedTensorHomDiagonal_natural_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonal.lean, line 930](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonal.lean#L930). The attribute's comment: “functoriality in the tensor factor”.

> **Stacks 0BYS.** The diagonal morphism is covariant in the tensor factor, for an arbitrary
> morphism of `D(O)`.
>
> A morphism of `D(O)` does not lift to the chosen K-flat representatives, which are not
> K-injective. It is instead written as a right fraction `inv (Q s₀) ≫ Q g₀`
> (`DerivedCategory.right_fac`) and the apex of that roof is replaced by a K-flat resolution of
> it (Stacks 06YS), giving a roof `A ⟵ P ⟶ A'` with all three complexes K-flat and the left leg
> invertible in `D(O)`. The one-sided K-flat comparison of Stacks 06YU is then available at all
> three vertices, which makes the tensored left leg invertible with no K-flatness of the other
> factor, and the square closes from the complex-level functoriality of Stacks 0BYR.

```lean
theorem derivedTensorHomDiagonal_natural_left (f : K ⟶ K') :
    ((Stacks.SheafOfModules.derivedTensorProductFunctor X).map f).app
          (((derivedSheafHomBifunctor X).obj (op M)).obj L) ≫
        derivedTensorHomDiagonal X K' L M =
      derivedTensorHomDiagonal X K L M ≫
        ((derivedSheafHomBifunctor X).obj (op M)).map
          (((Stacks.SheafOfModules.derivedTensorProductFunctor X).map f).app L)
```

**`Stacks.SheafOfModules.canonicalDerivedTensorHomDiagonal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonal.lean, line 1085](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonal.lean#L1085). The attribute's comment: “the canonical morphism”.

> **Stacks 0BYS.** The canonical morphism
>
> `K ⊗^L_{O_X} RSheafHom(M, L) ⟶ RSheafHom(M, K ⊗^L_{O_X} L)`
>
> in `D(O_X)` for objects `K`, `L`, `M` of the derived category of a ringed space.

```lean
def canonicalDerivedTensorHomDiagonal : DerivedTensorHomDiagonal Rc
```

**`Stacks.SheafOfModules.derivedTensorHomDiagonal_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonal.lean, line 1100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonal.lean#L1100). The attribute's comment: “the characterisation on representatives”.

> **Stacks 0BYS.** The canonical morphism is the class of the complex-level morphism of
> Stacks 0BYR between the chosen representatives, read through the K-flat and K-injective
> comparisons.

```lean
theorem derivedTensorHomDiagonal_eq (K L M : DerivedCategory (StructureSheafModules Rc)) :
    (RingedSite.derivedTensorHomSourceIso (ringedSite Rc) K L M).inv ≫
        derivedTensorHomDiagonal Rc K L M ≫
        (RingedSite.derivedTensorHomTargetIso (ringedSite Rc) K L M).hom =
      DerivedCategory.Q.map
        (RingedSite.derivedTensorHomModelMap (ringedSite Rc) K L M)
```

**`Stacks.SheafOfModules.derivedTensorHomDiagonal_natural_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonal.lean, line 1111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonal.lean#L1111). The attribute's comment: “functoriality in the source of the internal Hom”.

> **Stacks 0BYS.** The canonical morphism is contravariant in the source `M` of the internal
> Hom, for an arbitrary morphism of `D(O_X)`.

```lean
theorem derivedTensorHomDiagonal_natural_hom
    (K L : DerivedCategory (StructureSheafModules Rc))
    {M M' : DerivedCategory (StructureSheafModules Rc)} (g : M' ⟶ M) :
    ((derivedTensorProductFunctor (ringedSite Rc)).obj K).map
          (((RingedSite.derivedSheafHomBifunctor (ringedSite Rc)).map g.op).app L) ≫
        derivedTensorHomDiagonal Rc K L M' =
      derivedTensorHomDiagonal Rc K L M ≫
        ((RingedSite.derivedSheafHomBifunctor (ringedSite Rc)).map g.op).app
          (((derivedTensorProductFunctor (ringedSite Rc)).obj K).obj L)
```

**`Stacks.SheafOfModules.derivedTensorHomDiagonal_natural_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonal.lean, line 1125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonal.lean#L1125). The attribute's comment: “functoriality in the tensor factor”.

> **Stacks 0BYS.** The canonical morphism is covariant in the tensor factor `K`, for an
> arbitrary morphism of `D(O_X)`.

```lean
theorem derivedTensorHomDiagonal_natural_left
    {K K' : DerivedCategory (StructureSheafModules Rc)}
    (L M : DerivedCategory (StructureSheafModules Rc)) (f : K ⟶ K') :
    ((derivedTensorProductFunctor (ringedSite Rc)).map f).app
          (((RingedSite.derivedSheafHomBifunctor (ringedSite Rc)).obj (op M)).obj L) ≫
        derivedTensorHomDiagonal Rc K' L M =
      derivedTensorHomDiagonal Rc K L M ≫
        ((RingedSite.derivedSheafHomBifunctor (ringedSite Rc)).obj (op M)).map
          (((derivedTensorProductFunctor (ringedSite Rc)).map f).app L)
```

**`Stacks.SheafOfModules.derivedTensorHomDiagonal_natural_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonal.lean, line 1139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomDiagonal.lean#L1139). The attribute's comment: “functoriality in the target of the internal Hom”.

> **Stacks 0BYS.** The canonical morphism is covariant in the target `L` of the internal Hom,
> for an arbitrary morphism of `D(O_X)`.

```lean
theorem derivedTensorHomDiagonal_natural_right
    (K : DerivedCategory (StructureSheafModules Rc))
    {L L' : DerivedCategory (StructureSheafModules Rc)}
    (M : DerivedCategory (StructureSheafModules Rc)) (g : L ⟶ L') :
    ((derivedTensorProductFunctor (ringedSite Rc)).obj K).map
          (((RingedSite.derivedSheafHomBifunctor (ringedSite Rc)).obj (op M)).map g) ≫
        derivedTensorHomDiagonal Rc K L' M =
      derivedTensorHomDiagonal Rc K L M ≫
        ((RingedSite.derivedSheafHomBifunctor (ringedSite Rc)).obj (op M)).map
          (((derivedTensorProductFunctor (ringedSite Rc)).obj K).map g)
```

## Tag 0A8W, a lemma

[Tag 0A8W](https://stacks.math.columbia.edu/tag/0A8W) in the Stacks Project.

**`Stacks.SheafOfModules.derivedTensorHomUnit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomUnit.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomUnit.lean#L226). The attribute's comment: “the canonical morphism, as the unit of Stacks 08DI”.

> **Stacks 0A8W.** For objects `K`, `L` of `D(O_X)` on a ringed space, the canonical morphism
>
> `K ⟶ RSheafHom(L, K ⊗^L_{O_X} L)`
>
> in `D(O_X)`: the morphism corresponding to the identity of `K ⊗^L_{O_X} L` under the
> tensor–internal-Hom bijection of Stacks 08DI.

```lean
def derivedTensorHomUnit (K L : DerivedCategory (StructureSheafModules Rc)) :
    K ⟶ ((derivedSheafHom Rc).obj (op L)).obj (((derivedTensor Rc).obj K).obj L)
```

**`Stacks.SheafOfModules.canonicalDerivedTensorHomUnit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomUnit.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomUnit.lean#L265). The attribute's comment: “the canonical morphism, built as the source builds it”.

> **Stacks 0A8W.** For objects `K`, `L` of `D(O_X)` on a ringed space, the canonical morphism
>
> `K ⟶ RSheafHom(L, K ⊗^L_{O_X} L)`
>
> in `D(O_X)`, built the way the source builds it: on the chosen K-flat representative `A` of `K`
> and the chosen K-injective representative `B` of `L` it is the diagonal morphism of complexes of
> Stacks 0A93, `A ⟶ SheafHom(B, Tot(A ⊗_{O_X} B))`, followed by the augmentation of
> `Tot(A ⊗_{O_X} B)` into its chosen K-injective resolution, read through the comparisons
> identifying source and target with classes of complexes.
>
> A ringed space is a ringed site, so this is the morphism of Stacks 0A99 read off along
> `Stacks.SheafOfModules.ringedSite`. It is the construction that carries the functoriality of the
> tag, in `canonicalDerivedTensorHomUnit_natural_left` and
> `canonicalDerivedTensorHomUnit_natural_right` below.

```lean
def canonicalDerivedTensorHomUnit (K L : DerivedCategory (StructureSheafModules Rc)) :
    K ⟶ ((derivedSheafHom Rc).obj (op L)).obj (((derivedTensor Rc).obj K).obj L)
```

**`Stacks.SheafOfModules.canonicalDerivedTensorHomUnit_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomUnit.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomUnit.lean#L275). The attribute's comment: “the characterisation on representatives”.

> **Stacks 0A8W.** The canonical morphism built the source's way is the class of the diagonal
> morphism of complexes of Stacks 0A93 followed by the K-injective resolution augmentation, read
> through the comparisons of its source and target with classes of complexes. This is the equation
> that pins the morphism down; in particular it is not an arbitrary morphism between the two
> objects.

```lean
theorem canonicalDerivedTensorHomUnit_eq (K L : DerivedCategory (StructureSheafModules Rc)) :
    (RingedSite.kFlatModelIso (ringedSite Rc) K).hom ≫
        canonicalDerivedTensorHomUnit Rc K L ≫
        (RingedSite.diagonalTargetIso (ringedSite Rc) K L L).hom =
      DerivedCategory.Q.map (RingedSite.diagonalComplexMap (ringedSite Rc)
        (RingedSite.kFlatModel (ringedSite Rc) K)
        (RingedSite.kInjectiveModel (ringedSite Rc) L))
```

**`Stacks.SheafOfModules.canonicalDerivedTensorHomUnit_natural_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomUnit.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomUnit.lean#L292). The attribute's comment: “functoriality in K”.

> **Stacks 0A8W: the canonical morphism is functorial in `K`.** For a morphism `k : K ⟶ K'` of
> `D(O_X)` the square
>
> `k ≫ u_{K',L} = u_{K,L} ≫ RSheafHom(𝟙_L, k ⊗ 𝟙_L)`
>
> commutes in `D(O_X)`: the first variable of the morphism acts covariantly, both on the source
> and inside the derived tensor product.

```lean
theorem canonicalDerivedTensorHomUnit_natural_left
    (L : DerivedCategory (StructureSheafModules Rc))
    {K K' : DerivedCategory (StructureSheafModules Rc)} (k : K ⟶ K') :
    k ≫ canonicalDerivedTensorHomUnit Rc K' L =
      canonicalDerivedTensorHomUnit Rc K L ≫
        ((derivedSheafHom Rc).obj (op L)).map (((derivedTensor Rc).map k).app L)
```

**`Stacks.SheafOfModules.canonicalDerivedTensorHomUnit_natural_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomUnit.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorHomUnit.lean#L309). The attribute's comment: “functoriality in L”.

> **Stacks 0A8W: the canonical morphism is functorial in `L`.** For a morphism `l : L' ⟶ L` of
> `D(O_X)` the square
>
> `u_{K,L} ≫ RSheafHom(l, 𝟙) = u_{K,L'} ≫ RSheafHom(𝟙_{L'}, 𝟙_K ⊗ l)`
>
> commutes in `D(O_X)`: the second variable acts contravariantly in the source of the internal Hom
> and covariantly inside the derived tensor product, which is the dinaturality that the statement
> of the tag asserts.

```lean
theorem canonicalDerivedTensorHomUnit_natural_right
    (K : DerivedCategory (StructureSheafModules Rc))
    {L L' : DerivedCategory (StructureSheafModules Rc)} (l : L' ⟶ L) :
    canonicalDerivedTensorHomUnit Rc K L ≫
        ((derivedSheafHom Rc).map l.op).app (((derivedTensor Rc).obj K).obj L) =
      canonicalDerivedTensorHomUnit Rc K L' ≫
        ((derivedSheafHom Rc).obj (op L')).map (((derivedTensor Rc).obj K).map l)
```

## Tag 08I1, a lemma

[Tag 08I1](https://stacks.math.columbia.edu/tag/08I1) in the Stacks Project.

**`Stacks.SheafOfModules.derivedTensorDualToSheafHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorDual.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorDual.lean#L155). The attribute's comment: “the canonical map”.

> **Stacks 08I1: the canonical map `M ⊗^L_{O_X} L^∨ ⟶ RSheafHom(L, M)`.** It is the derived
> composition morphism of Stacks 0A8V, taken at intermediate object the structure sheaf, after the
> left tensor factor `M` has been identified with `RSheafHom(O_X, M)`.

```lean
def derivedTensorDualToSheafHom
    (L M : DerivedCategory (SheafOfModules.{u} (Tensor.ringSheaf.{u, u, u} Rc))) :
    ((derivedTensor Rc).obj M).obj (derivedDual Rc L) ⟶
      ((derivedSheafHom Rc).obj (op L)).obj M
```

**`Stacks.SheafOfModules.derivedTensorDualToSheafHom_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorDual.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorDual.lean#L181). The attribute's comment: “functoriality in M of the canonical map”.

> **The canonical map of Stacks 08I1 is functorial in `M`.** This is the covariant naturality
> of the derived composition morphism of Stacks 0A8V in its target, together with the naturality
> of the identification of `M` with `RSheafHom(O_X, M)`.

```lean
theorem derivedTensorDualToSheafHom_naturality
    (L : DerivedCategory (SheafOfModules.{u} (Tensor.ringSheaf.{u, u, u} Rc)))
    {M M' : DerivedCategory (SheafOfModules.{u} (Tensor.ringSheaf.{u, u, u} Rc))} (m : M ⟶ M') :
    ((derivedTensor Rc).map m).app (derivedDual Rc L) ≫
        derivedTensorDualToSheafHom Rc L M' =
      derivedTensorDualToSheafHom Rc L M ≫ ((derivedSheafHom Rc).obj (op L)).map m
```

**`Stacks.SheafOfModules.derivedTensorDualToSheafHom_naturality_tensorMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorDual.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorDual.lean#L194). The attribute's comment: “functoriality in M of the canonical map”.

> Functoriality in `M` of the canonical map of Stacks 08I1, in the `derivedTensorMap` and
> `derivedSheafHomMap` spelling of the induced maps on the derived tensor product and the derived
> internal Hom.

```lean
theorem derivedTensorDualToSheafHom_naturality_tensorMap
    (L : DerivedCategory (SheafOfModules.{u} (Tensor.ringSheaf.{u, u, u} Rc)))
    {M M' : DerivedCategory (SheafOfModules.{u} (Tensor.ringSheaf.{u, u, u} Rc))} (m : M ⟶ M') :
    derivedTensorMap Rc m (𝟙 (derivedDual Rc L)) ≫ derivedTensorDualToSheafHom Rc L M' =
      derivedTensorDualToSheafHom Rc L M ≫ derivedSheafHomMap Rc (𝟙 L) m
```

**`Stacks.SheafOfModules.derivedTensorDualGlobalSectionsMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorDual.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorDual.lean#L255). The attribute's comment: “the induced map on degree-zero global cohomology”.

> **Stacks 08I1: the induced map on degree-zero global cohomology.** The canonical map
> `M ⊗^L_{O_X} L^∨ ⟶ RSheafHom(L, M)` induces a map of abelian groups
>
> `H⁰(X, M ⊗^L_{O_X} L^∨) ⟶ Hom_{D(O_X)}(L, M)`,
>
> namely its degree-zero global hypercohomology followed by the identification
> `H⁰(X, RSheafHom(L, M)) ≅ Hom_{D(O_X)}(L, M)` of Stacks 08DK.

```lean
def derivedTensorDualGlobalSectionsMap
    (L M : DerivedCategory (SheafOfModules.{u} (Tensor.ringSheaf.{u, u, u} Rc))) :
    ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
        ((derivedModuleGlobalSections (ringedSite Rc)).obj
          (((derivedTensor Rc).obj M).obj (derivedDual Rc L))) : Type u) →+ (L ⟶ M)
```

**`Stacks.SheafOfModules.derivedTensorDualGlobalSectionsMap_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorDualGlobalFunctoriality.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorDualGlobalFunctoriality.lean#L143). The attribute's comment: “functoriality in M of the induced map on degree-zero global cohomology”.

> **Stacks 08I1: the induced map `H⁰(X, M ⊗^L_{O_X} L^∨) ⟶ Hom_{D(O_X)}(L, M)` is functorial
> in `M`.** For `m : M ⟶ M'` the degree-zero global hypercohomology of `m ⊗ 1` carries the induced
> map at `M` to the induced map at `M'` followed by postcomposition with `m`.
>
> This is the ringed-site statement
> `AlgebraicGeometry.RingedSite.derivedTensorDualGlobalSectionsMap_naturality`, read along
> `Stacks.SheafOfModules.ringedSite` for the canonical derived tensor product.

```lean
theorem derivedTensorDualGlobalSectionsMap_naturality
    (L : DerivedCategory (StructureSheafModules Rc))
    {M M' : DerivedCategory (StructureSheafModules Rc)} (m : M ⟶ M')
    (z : ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
      ((derivedModuleGlobalSections (ringedSite Rc)).obj
        (((derivedTensor Rc).obj M).obj (derivedDual Rc L))) : Type u)) :
    derivedTensorDualGlobalSectionsMap Rc L M'
        ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).map
          ((derivedModuleGlobalSections (ringedSite Rc)).map
            (((derivedTensor Rc).map m).app (derivedDual Rc L))) z) =
      derivedTensorDualGlobalSectionsMap Rc L M z ≫ m
```

**`Stacks.SheafOfModules.derivedTensorDualGlobalSectionsMap_naturality_tensorMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorDualGlobalFunctoriality.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorDualGlobalFunctoriality.lean#L160). The attribute's comment: “functoriality in M of the induced map on degree-zero global cohomology”.

> Functoriality in `M` of the induced map of Stacks 08I1, in the `derivedTensorMap` spelling of
> the map induced on the derived tensor product.

```lean
theorem derivedTensorDualGlobalSectionsMap_naturality_tensorMap
    (L : DerivedCategory (StructureSheafModules Rc))
    {M M' : DerivedCategory (StructureSheafModules Rc)} (m : M ⟶ M')
    (z : ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
      ((derivedModuleGlobalSections (ringedSite Rc)).obj
        (((derivedTensor Rc).obj M).obj (derivedDual Rc L))) : Type u)) :
    derivedTensorDualGlobalSectionsMap Rc L M'
        ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).map
          ((derivedModuleGlobalSections (ringedSite Rc)).map
            (derivedTensorMap Rc m (𝟙 (derivedDual Rc L)))) z) =
      derivedTensorDualGlobalSectionsMap Rc L M z ≫ m
```

## Tag 0A8U, a lemma

[Tag 0A8U](https://stacks.math.columbia.edu/tag/0A8U) in the Stacks Project.

**`Stacks.SheafOfModules.derivedSheafHomEvaluation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHomEvaluation/DerivedEvaluation.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHomEvaluation/DerivedEvaluation.lean#L91). The attribute's comment: “the canonical evaluation morphism”.

> **Stacks 0A8U.** For objects `K`, `L`, `M` of `D(O_X)` on a ringed space there is a canonical
> evaluation morphism
>
> `RSheafHom(L, M) ⊗^L_{O_X} K ⟶ RSheafHom(RSheafHom(K, L), M)`
>
> in `D(O_X)`, obtained from the evaluation morphism of internal Hom complexes after passing to a
> K-flat representative of `K` and K-injective representatives of `L` and `M`.

```lean
def derivedSheafHomEvaluation (K L M : DerivedCategory (SheafOfModules.{u} (Tensor.ringSheaf Rc))) :
    ((derivedTensor Rc).obj (((derivedSheafHom Rc).obj (op L)).obj M)).obj K ⟶
      ((derivedSheafHom Rc).obj (op (((derivedSheafHom Rc).obj (op K)).obj L))).obj M
```

**`Stacks.SheafOfModules.derivedSheafHomEvaluation_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHomEvaluation/DerivedEvaluation.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHomEvaluation/DerivedEvaluation.lean#L101). The attribute's comment: “functoriality in all three objects”.

> **Stacks 0A8U.** Derived evaluation is functorial in all three objects at once: covariant in
> the object being tensored, contravariant in the source of the inner internal hom, and covariant
> in its target.

```lean
theorem derivedSheafHomEvaluation_natural
    {K K' L L' M M' : DerivedCategory (SheafOfModules.{u} (Tensor.ringSheaf Rc))}
    (f : K ⟶ K') (g : L' ⟶ L) (h : M ⟶ M') :
    derivedTensorMap Rc (derivedSheafHomMap Rc g h) f ≫
        derivedSheafHomEvaluation Rc K' L' M' =
      derivedSheafHomEvaluation Rc K L M ≫
        derivedSheafHomMap Rc (derivedSheafHomMap Rc f g) h
```

**`Stacks.SheafOfModules.derivedSheafHomEvaluation_model`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHomEvaluation/DerivedEvaluation.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHomEvaluation/DerivedEvaluation.lean#L115). The attribute's comment: “comparison with evaluation of complexes”.

> **Stacks 0A8U.** On a K-flat representative `P` of `K` and K-injective representatives `J`
> of `L` and `I` of `M`, derived evaluation is the class of the evaluation morphism of internal
> Hom complexes `Tot(SheafHom^•(J, I) ⊗_{O_X} P) ⟶ SheafHom^•(SheafHom^•(P, J), I)`.

```lean
theorem derivedSheafHomEvaluation_model
    (P J I : CochainComplex (SheafOfModules.{u} (Tensor.ringSheaf Rc)) ℤ)
    (hP : IsKFlat Rc P) [J.IsKInjective] [I.IsKInjective] :
    derivedSheafHomEvaluation Rc (DerivedCategory.Q.obj P) (DerivedCategory.Q.obj J)
          (DerivedCategory.Q.obj I) ≫
        (RingedSite.derivedEvaluationTargetComparison (ringedSite Rc)
          (derivedInternalHom Rc) P J I).hom =
      (RingedSite.derivedEvaluationSourceComparison (ringedSite Rc)
          (canonicalDerivedTensorProduct (ringedSite Rc)) (derivedInternalHom Rc)
          P J I hP).hom ≫
        DerivedCategory.Q.map (RingedSite.evaluationMap (ringedSite Rc) P J I)
```

## Tag 0FXP, a remark

[Tag 0FXP](https://stacks.math.columbia.edu/tag/0FXP) in the Stacks Project.

**`Stacks.SheafOfModules.derivedSheafHomTensorMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorInternalHom.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedTensorInternalHom.lean#L177).

> **Stacks 0FXP.** For objects `K`, `K'`, `M`, `M'` of `D(O_X)` on a ringed space there is a
> canonical morphism
>
> `RSheafHom(K, K') ⊗^L_{O_X} RSheafHom(M, M') ⟶ RSheafHom(K ⊗^L_{O_X} M, K' ⊗^L_{O_X} M')`,
>
> the morphism adjoint under Stacks 08DI to the interchange of the two middle factors of
> `RSheafHom(K, K') ⊗^L RSheafHom(M, M') ⊗^L K ⊗^L M` followed by evaluation of each internal
> hom.

```lean
def derivedSheafHomTensorMap (K K' M M' : DerivedCategory (StructureSheafModules Rc)) :
    ((derivedTensor Rc).obj (((derivedSheafHom Rc).obj (op K)).obj K')).obj
        (((derivedSheafHom Rc).obj (op M)).obj M') ⟶
      ((derivedSheafHom Rc).obj (op (((derivedTensor Rc).obj K).obj M))).obj
        (((derivedTensor Rc).obj K').obj M')
```

## Tag 0B69, a remark

[Tag 0B69](https://stacks.math.columbia.edu/tag/0B69) in the Stacks Project.

**`Stacks.Cohomology.DerivedInternalHomPushforward.pushforwardSheafHomMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/InternalHomPushforwardMap.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/InternalHomPushforwardMap.lean#L113).

> **Stacks 0B69: the canonical map `Rf_*R𝓗om_{𝒪_X}(L, K) ⟶ R𝓗om_{𝒪_Y}(Rf_*L, Rf_*K)`** for a
> morphism of ringed spaces `f : (X, 𝒪_X) ⟶ (Y, 𝒪_Y)` and objects `K, L` of `D(𝒪_X)`.
>
> By the tensor–internal-hom bijection of Stacks 08DI it is the same datum as a map
> `Rf_*R𝓗om(L, K) ⊗^L_{𝒪_Y} Rf_*L ⟶ Rf_*K`, and that datum is the relative cup product of
> Stacks 0B68 followed by the derived pushforward of the evaluation map.

```lean
def pushforwardSheafHomMap (K L : DerivedCategory (Mod X.sheaf)) :
    (derivedPushforward f).obj (sheafHomObj X L K) ⟶
      sheafHomObj Y ((derivedPushforward f).obj L) ((derivedPushforward f).obj K)
```

## Tag 0G7A, a remark

[Tag 0G7A](https://stacks.math.columbia.edu/tag/0G7A) in the Stacks Project.

**`Stacks.Cohomology.DerivedInternalHomEvaluation.tensorMap_pushforwardSheafHomMap_sheafHomEval`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/InternalHomEvaluationSquare.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/InternalHomEvaluationSquare.lean#L262). The attribute's comment: “the square commutes, for every morphism of ringed spaces f and all K, M; this is the whole of the remark. The source states it for `K, M ∈ D(𝒪_Y)`, which is a slip — the diagram applies both `R𝓗om_{𝒪_X}` and `Rf_*` to `K` and `M`, so the arrows type-check only for `K, M ∈ D(𝒪_X)`, and that is the form here”.

> **Stacks 0G7A.**  For a morphism of ringed spaces `f : (X, 𝒪_X) ⟶ (Y, 𝒪_Y)` and objects
> `K, M` of `D(𝒪_X)` the square
>
> `Rf_*R𝓗om_{𝒪_X}(K, M) ⊗^L_{𝒪_Y} Rf_*K ⟶ Rf_*(R𝓗om_{𝒪_X}(K, M) ⊗^L_{𝒪_X} K) ⟶ Rf_*M`,
> `Rf_*R𝓗om_{𝒪_X}(K, M) ⊗^L_{𝒪_Y} Rf_*K ⟶ R𝓗om_{𝒪_Y}(Rf_*K, Rf_*M) ⊗^L_{𝒪_Y} Rf_*K ⟶ Rf_*M`
>
> commutes: the map of Stacks 0B69 tensored with the identity of `Rf_*K` followed by the
> evaluation on `Y` agrees with the relative cup product of Stacks 0B68 followed by the derived
> pushforward of the evaluation on `X`.
>
> That the bijection of Stacks 08DI on `Y` evaluates, which is the content of the square, is
> `tensorEquivIsEvaluation`.

```lean
theorem tensorMap_pushforwardSheafHomMap_sheafHomEval
    (K M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.sheaf))) :
    tensorMap Y (pushforwardSheafHomMap f M K) (𝟙 ((derivedPushforward f).obj K)) ≫
        sheafHomEval Y ((derivedPushforward f).obj K) ((derivedPushforward f).obj M) =
      Stacks.Cohomology.DerivedRelativeCupProduct.relativeCupProduct f (sheafHomObj X K M) K ≫
        (derivedPushforward f).map (sheafHomEval X K M)
```

## Tag 08I3, a remark

[Tag 08I3](https://stacks.math.columbia.edu/tag/08I3) in the Stacks Project.

**`Stacks.Cohomology.DerivedInternalHomPullback.derivedPullbackSheafHomMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/InternalHomPullbackMap.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/InternalHomPullbackMap.lean#L376).

> **Tag 08I3: the canonical map `Lh^*R𝓗om(K, L) ⟶ R𝓗om(Lh^*K, Lh^*L)`** for a morphism of
> ringed spaces `h : (X, 𝒪_X) ⟶ (Y, 𝒪_Y)` and objects `K, L` of `D(𝒪_Y)`.
>
> By the tensor–internal-hom bijection of Tag 08DI it is the same datum as a map
> `Lh^*R𝓗om(K,L) ⊗^L_{𝒪_X} Lh^*K ⟶ Lh^*L`, and that is the derived pullback of the evaluation
> `R𝓗om(K,L) ⊗^L_{𝒪_Y} K ⟶ L` preceded by the monoidality comparison of Tag 079U.

```lean
def derivedPullbackSheafHomMap :
    (derivedPullbackFunctor h).obj
        (((Stacks.SheafOfModules.derivedSheafHom Y.sheaf).obj (op K)).obj L) ⟶
      ((Stacks.SheafOfModules.derivedSheafHom X.sheaf).obj
          (op ((derivedPullbackFunctor h).obj K))).obj
        ((derivedPullbackFunctor h).obj L)
```

## Tag 08I4, a remark

[Tag 08I4](https://stacks.math.columbia.edu/tag/08I4) in the Stacks Project.

**`Stacks.Cohomology.DerivedInternalHomBaseChange.derivedBaseChangeSheafHomMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/InternalHomBaseChange.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/InternalHomBaseChange.lean#L116).

> **Tag 08I4: the base change map for a derived internal hom.**  For a commutative square of
> ringed spaces with `h : X' ⟶ X` over `g : S' ⟶ S` and objects `K, L` of `D(𝒪_X)`, the canonical
> map
>
> `Lg^* Rf_* R𝓗om_{𝒪_X}(K, L) ⟶ R(f')_* R𝓗om_{𝒪_{X'}}(Lh^*K, Lh^*L)`
>
> in `D(𝒪_{S'})`.  It is the derived base change map of Tag 08HY at `R𝓗om_{𝒪_X}(K, L)` followed
> by `R(f')_*` of the canonical map of Tag 08I3, which is the adjoint of the three-step
> composition the source describes.

```lean
def derivedBaseChangeSheafHomMap :
    (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback g).obj
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).obj
          (((Stacks.SheafOfModules.derivedSheafHom X.sheaf).obj (op K)).obj L)) ⟶
      (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f').obj
        (((Stacks.SheafOfModules.derivedSheafHom X'.sheaf).obj
            (op ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback h).obj
              K))).obj
          ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback h).obj L))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.42, Tag 08DH](https://stacks.math.columbia.edu/tag/08DH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
