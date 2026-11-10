---
declaration: section
origin: cited
lean: Stacks.Cohomology.GlueingComplexes.exists_glueing, Stacks.Cohomology.GlueingComplexes.exists_hom_of_compatible, Stacks.Cohomology.UnboundedHigherDirectImage.isZero_homologyDerivedPushforward_of_isBasis, Stacks.Cohomology.UnboundedHigherDirectImage.isZero_homologyDerivedPreimageSections_of_isBasis, Stacks.Cohomology.UnboundedHigherDirectImage.isSheaf_zerothDerivedPreimageCohomologyPresheaf, Stacks.Cohomology.UnboundedHigherDirectImage.subsingleton_shiftedHom_preimageRestrict_of_isBasis, Stacks.Cohomology.UnboundedHigherDirectImage.isSheaf_derivedPreimageHomPresheaf, Stacks.DerivedGlueing.LocallyGiven
statement: formalized
proof: formalized
---

# 20.45 Glueing complexes

Section 20.45 of the Stacks Project, [Tag 0D65](https://stacks.math.columbia.edu/tag/0D65). 8 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08DG, a lemma

[Tag 08DG](https://stacks.math.columbia.edu/tag/08DG) in the Stacks Project.

**`Stacks.Cohomology.GlueingComplexes.exists_glueing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/GlueingComplexes/TwoOpens.lean, line 1051](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/GlueingComplexes/TwoOpens.lean#L1051). The attribute's comment: “existence of a glueing”.

> **Stacks Project, Tag 08DG.** Let `X` be a ringed space, let `jU : U ⟶ X` and `jV : V ⟶ X`
> be open immersions and let `W` be their intersection. An object `A` of `D(𝒪_U)`, an object `B`
> of `D(𝒪_V)` and an isomorphism `c : A|_W ≅ B|_W` come from an object of `D(𝒪_X)`.
>
> No hypothesis that `U` and `V` cover `X` is needed for the glued object to exist; a cover is
> what makes it unique.

```lean
theorem exists_glueing {X U V W : RingedSpace.{u, u}} (jU : U ⟶ X) (jV : V ⟶ X) (iU : W ⟶ U)
    (iV : W ⟶ V) [SheafedSpace.IsOpenImmersion jU] [SheafedSpace.IsOpenImmersion jV]
    (h : IsPullback iU iV jU jV) (A : DerivedModules U) (B : DerivedModules V)
    (c : (derivedRestrict iU).obj A ≅ (derivedRestrict iV).obj B) :
    Nonempty (Glueing jU jV iU iV h.w A B c)
```

**`Stacks.Cohomology.GlueingComplexes.exists_hom_of_compatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/GlueingComplexes/TwoOpens.lean, line 1441](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/GlueingComplexes/TwoOpens.lean#L1441). The attribute's comment: “a compatible pair of maps comes from the glued object”.

> **Stacks Project, Tag 08DG.** Let `X` be a ringed space covered by the images of two open
> immersions `jU : U ⟶ X` and `jV : V ⟶ X`, let `W` be their intersection, and let `F` be a
> glueing of the glueing data `(A, B, c)`, with identifications `f : F|_U ≅ A` and
> `g : F|_V ≅ B`. Let `E` be an object of `D(𝒪_X)` and let `a : A ⟶ E|_U` and `b : B ⟶ E|_V`
> agree on `W` through `c`. Then there is a morphism `F ⟶ E` restricting to `a ∘ f` on `U` and
> to `b ∘ g` on `V`.
>
> Unlike the existence of the glued object, this needs `U` and `V` to cover `X`: it is
> Mayer--Vietoris for `Hom`, and the covering hypothesis enters only through
> `isIso_of_restrict_isIso`.

```lean
theorem exists_hom_of_compatible {X U V W : RingedSpace.{u, u}} (jU : U ⟶ X) (jV : V ⟶ X)
    (iU : W ⟶ U) (iV : W ⟶ V) [SheafedSpace.IsOpenImmersion jU]
    [SheafedSpace.IsOpenImmersion jV] (h : IsPullback iU iV jU jV)
    (cover : Set.range jU.hom.base ∪ Set.range jV.hom.base = Set.univ)
    {A : DerivedModules U} {B : DerivedModules V}
    {c : (derivedRestrict iU).obj A ≅ (derivedRestrict iV).obj B}
    (G : Glueing jU jV iU iV h.w A B c) (E : DerivedModules X)
    (a : A ⟶ (derivedRestrict jU).obj E) (b : B ⟶ (derivedRestrict jV).obj E)
    (hab : (derivedRestrict iU).map a ≫ (overlapIso jU jV iU iV h.w).hom.app E =
      c.hom ≫ (derivedRestrict iV).map b) :
    ∃ φ : G.F ⟶ E, (derivedRestrict jU).map φ = G.f.hom ≫ a ∧
      (derivedRestrict jV).map φ = G.g.hom ≫ b
```

## Tag 0D66, a lemma

[Tag 0D66](https://stacks.math.columbia.edu/tag/0D66) in the Stacks Project.

**`Stacks.Cohomology.UnboundedHigherDirectImage.isZero_homologyDerivedPushforward_of_isBasis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ConnectivityOnABasis.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ConnectivityOnABasis.lean#L105). The attribute's comment: “negative\_sheaves”.

> **Vanishing of the cohomology sheaves of `Rf_* K`.** If the degree-`i` hypercohomology
> `H^i(f⁻¹ V, K)` vanishes for every `V` in a basis of the topology of `Y`, then the degree-`i`
> cohomology sheaf of `Rf_* K` vanishes.

```lean
theorem isZero_homologyDerivedPushforward_of_isBasis (i : ℤ)
    (hK : ∀ V ∈ B, IsZero ((DerivedCategory.homologyFunctor
      (ModuleCat.{u} ((structureSheafRing Y).obj.obj (op V))) i).obj
        ((derivedPreimageSections f V).obj K))) :
    IsZero ((DerivedCategory.homologyFunctor (SheafOfModules.{u} (structureSheafRing Y)) i).obj
      ((derivedPushforward f).obj K))
```

**`Stacks.Cohomology.UnboundedHigherDirectImage.isZero_homologyDerivedPreimageSections_of_isBasis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ConnectivityOnABasis.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ConnectivityOnABasis.lean#L120). The attribute's comment: “negative\_hypercohomology”.

> **Negative hypercohomology over every inverse image.** If `H^i(f⁻¹ V, K) = 0` for `i < 0` and
> every `V` in a basis of the topology of `Y`, then `H^i(f⁻¹ V, K) = 0` for `i < 0` and *every* open
> `V ⊆ Y`.

```lean
theorem isZero_homologyDerivedPreimageSections_of_isBasis
    (hK : ∀ V ∈ B, ∀ i : ℤ, i < 0 → IsZero ((DerivedCategory.homologyFunctor
      (ModuleCat.{u} ((structureSheafRing Y).obj.obj (op V))) i).obj
        ((derivedPreimageSections f V).obj K)))
    (V : Opens Y.carrier) (i : ℤ) (hi : i < 0) :
    IsZero ((DerivedCategory.homologyFunctor
      (ModuleCat.{u} ((structureSheafRing Y).obj.obj (op V))) i).obj
        ((derivedPreimageSections f V).obj K))
```

**`Stacks.Cohomology.UnboundedHigherDirectImage.isSheaf_zerothDerivedPreimageCohomologyPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ConnectivityOnABasis.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ConnectivityOnABasis.lean#L139). The attribute's comment: “zeroth\_sheaf”.

> **The rule `V ↦ H^0(f⁻¹ V, K)` is a sheaf.** If `H^i(f⁻¹ V, K) = 0` for `i < 0` and every `V`
> in a basis of the topology of `Y`, then the presheaf of `𝒪_Y`-modules `V ↦ H^0(f⁻¹ V, K)` — that
> is `derivedPreimageCohomologyPresheaf f K 0`, whose values are identified with `H^0(f⁻¹ V, K)` by
> `preimageCohomologyEvaluationIso` — satisfies the sheaf condition.

```lean
theorem isSheaf_zerothDerivedPreimageCohomologyPresheaf
    (hK : ∀ V ∈ B, ∀ i : ℤ, i < 0 → IsZero ((DerivedCategory.homologyFunctor
      (ModuleCat.{u} ((structureSheafRing Y).obj.obj (op V))) i).obj
        ((derivedPreimageSections f V).obj K))) :
    Presheaf.IsSheaf (Opens.grothendieckTopology Y.carrier)
      (derivedPreimageCohomologyPresheaf f K 0).presheaf
```

**`Stacks.Cohomology.UnboundedHigherDirectImage.subsingleton_shiftedHom_preimageRestrict_of_isBasis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ConnectivityOnABasis.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ConnectivityOnABasis.lean#L268). The attribute's comment: “hom\_negative\_ext”.

> **Negative `Ext` over every inverse image.** If `Ext^i(K|_{f⁻¹ V}, L|_{f⁻¹ V}) = 0` for
> `i < 0` and every `V` in a basis of the topology of `Y`, then the same vanishing holds for `i < 0`
> and *every* open `V ⊆ Y`.

```lean
theorem subsingleton_shiftedHom_preimageRestrict_of_isBasis
    (hExt : ∀ V ∈ B, ∀ i : ℤ, i < 0 →
      Subsingleton (ShiftedHom ((preimageRestrict f V).obj K)
        ((preimageRestrict f V).obj L) i))
    (V : Opens Y.carrier) (i : ℤ) (hi : i < 0) :
    Subsingleton (ShiftedHom ((preimageRestrict f V).obj K)
      ((preimageRestrict f V).obj L) i)
```

**`Stacks.Cohomology.UnboundedHigherDirectImage.isSheaf_derivedPreimageHomPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ConnectivityOnABasis.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ConnectivityOnABasis.lean#L289). The attribute's comment: “hom\_sheaf”.

> **The rule `V ↦ Hom(K|_{f⁻¹ V}, L|_{f⁻¹ V})` is a sheaf.** If
> `Ext^i(K|_{f⁻¹ V}, L|_{f⁻¹ V}) = 0` for `i < 0` and every `V` in a basis of the topology of `Y`,
> then the presheaf of `𝒪_Y`-modules `V ↦ Hom(K|_{f⁻¹ V}, L|_{f⁻¹ V})` satisfies the sheaf
> condition. Here the presheaf is `derivedPreimageCohomologyPresheaf f (RSheafHom(K, L)) 0`, whose
> value on `V` is identified with `Hom(K|_{f⁻¹ V}, L|_{f⁻¹ V})` by
> `derivedPreimageHomPresheafValueEquiv`.

```lean
theorem isSheaf_derivedPreimageHomPresheaf
    (hExt : ∀ V ∈ B, ∀ i : ℤ, i < 0 →
      Subsingleton (ShiftedHom ((preimageRestrict f V).obj K)
        ((preimageRestrict f V).obj L) i)) :
    Presheaf.IsSheaf (Opens.grothendieckTopology Y.carrier)
      (derivedPreimageCohomologyPresheaf f (homSheafObject X.sheaf K L) 0).presheaf
```

## Tag 0D67, a situation

[Tag 0D67](https://stacks.math.columbia.edu/tag/0D67) in the Stacks Project.

**`Stacks.DerivedGlueing.LocallyGiven`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/LocallyGivenObjects.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/LocallyGivenObjects.lean#L120).

> A system of locally given derived objects on a ringed space.
>
> The `restrictionComp` field is the canonical identification between direct restriction and
> restriction in two steps. With this identification inserted, `cocycle` says exactly
> `ρ W U = ρ W V ∘ (ρ V U)|_W`.

```lean
structure LocallyGiven (X : RingedSpace.{u})
```

## Tag 0D68, a lemma

[Tag 0D68](https://stacks.math.columbia.edu/tag/0D68) in the Stacks Project.

**`Stacks.DerivedGlueing.subsingleton_shiftedHom_self_of_covers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/SelfExtOnACollectionOfOpens.lean, line 494](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/SelfExtOnACollectionOfOpens.lean#L494). The attribute's comment: “the vanishing of negative self-Ext, for an arbitrary object `K` of `D(𝒪_X)` and an arbitrary collection of opens covering `X` with intersections covered by members, such that `K|_U` has no negative self-Ext for every member `U`”.

> **Stacks 0D68, the vanishing of negative self-Ext.** Let `(X, 𝒪_X)` be a ringed space and
> let `ℬ` be a collection of open subsets covering `X` such that the intersection of two members
> of `ℬ` is the union of the members of `ℬ` contained in it. If `K` is an object of `D(𝒪_X)` with
> `Ext^i(K|_U, K|_U) = 0` for `i < 0` and every `U ∈ ℬ`, then `Ext^i(K, K) = 0` for `i < 0`.
>
> The members of `ℬ` need not form a basis; by Tag 0D5Q there is a continuous `f : X → Y` whose
> images of the members of `ℬ` do form a basis of `Y` and satisfy `f⁻¹(f(U)) = U`, and Tag 0D66
> part (2) applied to `f` with `𝒪_Y = f_* 𝒪_X` gives the vanishing over every open of `Y`,
> including `⊤`.
>
> Here `K` is an arbitrary object of `D(𝒪_X)` and `ℬ` an arbitrary collection;
> `Stacks.DerivedGlueing.Solution.subsingleton_shiftedHom_self` is this statement applied to the
> global object of a `Stacks.DerivedGlueing.Solution` of a system of locally given objects.

```lean
theorem subsingleton_shiftedHom_self_of_covers {X : RingedSpace.{u, u}}
    (ℬ : Set (Opens X.carrier)) (hcover : sSup ℬ = ⊤)
    (hinter : ∀ U ∈ ℬ, ∀ V ∈ ℬ, U ⊓ V = sSup {W | W ∈ ℬ ∧ W ≤ U ⊓ V})
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (hExt : ∀ U ∈ ℬ, ∀ i : ℤ, i < 0 → Subsingleton (ShiftedHom
      ((SheafOfModules.overFunctor.{u} (structureSheafRing X) U).mapDerivedCategory.obj K)
      ((SheafOfModules.overFunctor.{u} (structureSheafRing X) U).mapDerivedCategory.obj K) i))
    (i : ℤ) (hi : i < 0) :
    Subsingleton (ShiftedHom K K i)
```

**`Stacks.DerivedGlueing.Solution.subsingleton_shiftedHom_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/SelfExtOnACollectionOfOpens.lean, line 652](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/SelfExtOnACollectionOfOpens.lean#L652). The attribute's comment: “the vanishing of negative self-Ext of the global object of a solution”.

> **Stacks 0D68, the vanishing of negative self-Ext.** In Situation 0D67, suppose that the
> displayed opens cover `X` and that the intersection of two of them is the union of the members
> of the collection it contains, and that the prescribed local objects have no negative
> self-Ext.  Then the global object of a solution has no negative self-Ext either.
>
> The restrictions of the global object are the prescribed local objects, by
> `Stacks.DerivedGlueing.Solution.restrictionIso`, so this is
> `Stacks.DerivedGlueing.subsingleton_shiftedHom_self_of_covers` read through the equivalences
> comparing the models of restriction of modules to an open.

```lean
theorem Solution.subsingleton_shiftedHom_self {S : LocallyGiven X} (A : Solution S)
    (hcover : sSup S.opens = ⊤)
    (hinter : ∀ U ∈ S.opens, ∀ V ∈ S.opens, U ⊓ V = sSup {W | W ∈ S.opens ∧ W ≤ U ⊓ V})
    (hExt : ∀ (U : Opens X.carrier) (hU : U ∈ S.opens), ∀ i : ℤ, i < 0 →
      Subsingleton (ShiftedHom (S.obj U hU) (S.obj U hU) i))
    (i : ℤ) (hi : i < 0) :
    Subsingleton (ShiftedHom A.obj A.obj i)
```

**`Stacks.DerivedGlueing.exists_unique_solutionIso_of_covers_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/UniquenessOfASolutionUnconditional.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/UniquenessOfASolutionUnconditional.lean#L146). The attribute's comment: “the uniqueness of a solution up to unique isomorphism, under the tag's conditions (1) and (2); the vanishing of negative self-Ext is `subsingleton_shiftedHom_self_of_covers` and `Solution.subsingleton_shiftedHom_self`”.

> **The uniqueness clause of [Stacks, Tag 0D68]**: in Situation 0D67, if
> the displayed opens cover `X`, if the intersection of two of them is the union of the members of
> the collection it contains, and if the prescribed local objects have no negative self-`Ext`, then
> any two solutions are identified by exactly one isomorphism of solutions.
>
> The three conditions are (1) and (2) of the tag, as in
> `Stacks.DerivedGlueing.Solution.subsingleton_shiftedHom_self`, the tag's other clause.  The proof
> applies `Stacks.DerivedGlueing.exists_unique_solutionIso_of_covers_of_coherence`, its coherence
> input being `Stacks.DerivedGlueing.restrictHomBelow_eq_restrictDerivedHom`.
>
> The conclusion `Stacks.DerivedGlueing.Solution.IsCompatibleHom A B ψ.hom` is by definition
> `∀ (U : Opens X.carrier) (hU : U ∈ S.opens), (S.restriction U ⊤ le\_top).map ψ.hom ≫
> (B.rho U hU).hom = (A.rho U hU).hom`, which is the clause as the source states it.

```lean
theorem exists_unique_solutionIso_of_covers_unconditional (S : LocallyGiven X)
    (hcover : sSup S.opens = ⊤)
    (hinter : ∀ U ∈ S.opens, ∀ V ∈ S.opens, U ⊓ V = sSup {W | W ∈ S.opens ∧ W ≤ U ⊓ V})
    (hExt : ∀ (U : Opens X.carrier) (hU : U ∈ S.opens), ∀ i : ℤ, i < 0 →
      Subsingleton (ShiftedHom (S.obj U hU) (S.obj U hU) i))
    (A B : Solution S) :
    ∃! ψ : A.obj ≅ B.obj, A.IsCompatibleHom B ψ.hom
```

## Tag 0D69, a remark

[Tag 0D69](https://stacks.math.columbia.edu/tag/0D69) in the Stacks Project.

**`Stacks.DerivedGlueing.exists_unique_overlapIso_of_covers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/HomVanishingOverASubcollection.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/HomVanishingOverASubcollection.lean#L457). The attribute's comment: “the comparison isomorphism over an overlap: for `U, V ∈ ℬ` a unique isomorphism `K_U|_{U ⊓ V} ≅ K_V|_{U ⊓ V}` compatible with the prescribed transitions on the members of `ℬ` contained in `U ⊓ V`, for a collection satisfying `hinter` (condition (1) of 0D68) and `hExt` (condition (2) of 0D68)”.

> **The comparison isomorphism over an overlap.**  For members `U` and `V` of the collection
> there is a unique isomorphism `ρ_{U,V} : K_U|_{U ∩ V} ≅ K_V|_{U ∩ V}` compatible with the
> prescribed transitions on the members contained in `U ∩ V`.  Here `hinter` is hypothesis (1) of
> [Stacks, Tag 0D68] and `hExt` is its hypothesis (2); the collection need not cover `X`.

```lean
theorem exists_unique_overlapIso_of_covers (S : LocallyGiven X)
    (hinter : ∀ U ∈ S.opens, ∀ V ∈ S.opens, U ⊓ V = sSup {W | W ∈ S.opens ∧ W ≤ U ⊓ V})
    (hExt : ∀ (U : Opens X.carrier) (hU : U ∈ S.opens), ∀ i : ℤ, i < 0 →
      Subsingleton (ShiftedHom (S.obj U hU) (S.obj U hU) i))
    (U V : Opens X.carrier) (hU : U ∈ S.opens) (hV : V ∈ S.opens) :
    ∃! φ : (S.restriction (U ⊓ V) U inf_le_left).obj (S.obj U hU) ≅
        (S.restriction (U ⊓ V) V inf_le_right).obj (S.obj V hV),
      IsOverlapHom S hU hV inf_le_left inf_le_right φ.hom
```

**`Stacks.DerivedGlueing.restrictOverlapHom_cocycle_of_covers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/HomVanishingOverASubcollection.lean, line 477](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/HomVanishingOverASubcollection.lean#L477). The attribute's comment: “the cocycle condition `ρ_{U,W} = ρ_{V,W} ∘ ρ_{U,V}` over a triple intersection, for any three compatible isomorphisms over the three overlaps -- which by `exists_unique_overlapIso_of_covers` are the source's own `ρ_{U,V}`, `ρ_{V,W}` and `ρ_{U,W}`, being the unique compatible ones -- for a collection satisfying `hinter` (condition (1) of 0D68) and `hExt` (condition (2) of 0D68)”.

> **The cocycle condition over a triple intersection.**  For members `U`, `V` and `W` and
> compatible isomorphisms over the three overlaps, `ρ_{U,W} = ρ_{V,W} ∘ ρ_{U,V}` over `U ∩ V ∩ W`.
> By `Stacks.DerivedGlueing.exists_unique_overlapIso_of_covers` the compatible isomorphisms over the
> overlaps are unique.

```lean
theorem restrictOverlapHom_cocycle_of_covers (S : LocallyGiven X)
    (hinter : ∀ U ∈ S.opens, ∀ V ∈ S.opens, U ⊓ V = sSup {W | W ∈ S.opens ∧ W ≤ U ⊓ V})
    (hExt : ∀ (U : Opens X.carrier) (hU : U ∈ S.opens), ∀ i : ℤ, i < 0 →
      Subsingleton (ShiftedHom (S.obj U hU) (S.obj U hU) i))
    (U V W : Opens X.carrier) (hU : U ∈ S.opens) (hV : V ∈ S.opens) (hW : W ∈ S.opens)
    (φUV : (S.restriction (U ⊓ V) U inf_le_left).obj (S.obj U hU) ≅
      (S.restriction (U ⊓ V) V inf_le_right).obj (S.obj V hV))
    (hφUV : IsOverlapHom S hU hV inf_le_left inf_le_right φUV.hom)
    (φVW : (S.restriction (V ⊓ W) V inf_le_left).obj (S.obj V hV) ≅
      (S.restriction (V ⊓ W) W inf_le_right).obj (S.obj W hW))
    (hφVW : IsOverlapHom S hV hW inf_le_left inf_le_right φVW.hom)
    (φUW : (S.restriction (U ⊓ W) U inf_le_left).obj (S.obj U hU) ≅
      (S.restriction (U ⊓ W) W inf_le_right).obj (S.obj W hW))
    (hφUW : IsOverlapHom S hU hW inf_le_left inf_le_right φUW.hom) :
    restrictOverlapHom S hU hW inf_le_left inf_le_right
        (le_inf (inf_le_left.trans inf_le_left) inf_le_right : U ⊓ V ⊓ W ≤ U ⊓ W) φUW.hom =
      restrictOverlapHom S hU hV inf_le_left inf_le_right
          (inf_le_left : U ⊓ V ⊓ W ≤ U ⊓ V) φUV.hom ≫
        restrictOverlapHom S hV hW inf_le_left inf_le_right
          (le_inf (inf_le_left.trans inf_le_right) inf_le_right : U ⊓ V ⊓ W ≤ V ⊓ W) φVW.hom
```

**`Stacks.DerivedGlueing.restrictedSystemOverInf_covers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/OverlapRestrictedSystem.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/OverlapRestrictedSystem.lean#L99). The attribute's comment: “the restricted system covers the overlap: condition (1) of 0D68 for the subsystem on the members contained in `U ⊓ V`, from the condition that the intersection of two members is the union of the members contained in it”.

> **[Stacks, Tag 0D69], the restricted system covers the overlap.** The overlap of two members
> is the union of the members of the restricted collection contained in it — which is condition
> (1) of [Stacks, Tag 0D68] for the restricted system, read at `U ⊓ V`.  It is the condition that
> intersections of members are unions of members, read at the pair `U, V`.

```lean
theorem restrictedSystemOverInf_covers (S : LocallyGiven X)
    (hinter : ∀ U ∈ S.opens, ∀ V ∈ S.opens, U ⊓ V = sSup {W | W ∈ S.opens ∧ W ≤ U ⊓ V})
    (U V : Opens X.carrier) (hU : U ∈ S.opens) (hV : V ∈ S.opens) :
    U ⊓ V = sSup {W | W ∈ (restrictedSystemOverInf S U V).opens ∧ W ≤ U ⊓ V}
```

**`Stacks.DerivedGlueing.restrictedSystemOverInf_intersections_covered`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/OverlapRestrictedSystem.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/OverlapRestrictedSystem.lean#L114). The attribute's comment: “the restricted system's intersection condition: condition (1) of 0D68 for the subsystem on the members contained in `U ⊓ V`, at an arbitrary pair of its members”.

> **[Stacks, Tag 0D69], the restricted system's intersection condition.** The intersection of
> two members of the restricted collection is the union of the members of the restricted
> collection contained in it — condition (1) of [Stacks, Tag 0D68] for the restricted system, at
> an arbitrary pair of its members.
>
> The members of the restricted collection contained in `A ⊓ B` are exactly the members of the
> whole collection contained in it, because `A ⊓ B ≤ A ≤ U ⊓ V`.

```lean
theorem restrictedSystemOverInf_intersections_covered (S : LocallyGiven X)
    (hinter : ∀ U ∈ S.opens, ∀ V ∈ S.opens, U ⊓ V = sSup {W | W ∈ S.opens ∧ W ≤ U ⊓ V})
    (U V : Opens X.carrier) :
    ∀ A ∈ (restrictedSystemOverInf S U V).opens, ∀ B ∈ (restrictedSystemOverInf S U V).opens,
      A ⊓ B = sSup {W | W ∈ (restrictedSystemOverInf S U V).opens ∧ W ≤ A ⊓ B}
```

**`Stacks.DerivedGlueing.restrictedSystemOverInf_ext`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/OverlapRestrictedSystem.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/OverlapRestrictedSystem.lean#L129). The attribute's comment: “the restricted system's `Ext` condition: condition (2) of 0D68 for the subsystem on the members contained in `U ⊓ V`, from the vanishing of negative self-`Ext` of the prescribed objects”.

> **[Stacks, Tag 0D69], the restricted system's `Ext` condition.** The prescribed objects of
> the restricted system have no negative self-`Ext`, since they are prescribed objects of the
> whole system — condition (2) of [Stacks, Tag 0D68] for the restricted system.

```lean
theorem restrictedSystemOverInf_ext (S : LocallyGiven X)
    (hExt : ∀ (W : Opens X.carrier) (hW : W ∈ S.opens), ∀ i : ℤ, i < 0 →
      Subsingleton (ShiftedHom (S.obj W hW) (S.obj W hW) i))
    (U V : Opens X.carrier) :
    ∀ (W : Opens X.carrier) (hW : W ∈ (restrictedSystemOverInf S U V).opens), ∀ i : ℤ, i < 0 →
      Subsingleton (ShiftedHom ((restrictedSystemOverInf S U V).obj W hW)
        ((restrictedSystemOverInf S U V).obj W hW) i)
```

**`Stacks.DerivedGlueing.exists_solutionOver_inf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/OverlapRestrictedSystem.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/OverlapRestrictedSystem.lean#L149). The attribute's comment: “the two restricted objects are solutions over the overlap: `K_U|_{U ∩ V}` and `K_V|_{U ∩ V}` are each a solution for the system over `U ∩ V`, for every `U, V ∈ ℬ`”.

> **[Stacks, Tag 0D69], both restrictions are solutions over the overlap.** The prescribed
> object on a member is a solution over that member,
> `Stacks.DerivedGlueing.selfSolutionOver`, and a solution over an open restricts to a solution
> over a smaller one, `Stacks.DerivedGlueing.SolutionOver.restrictOpen`.  So `K_U|_{U ∩ V}` and
> `K_V|_{U ∩ V}` are each a solution for the system over `U ∩ V`, and these are the two solutions
> the source feeds to the uniqueness clause of [Stacks, Tag 0D68].  This holds for all
> `U, V ∈ ℬ`.

```lean
theorem exists_solutionOver_inf (S : LocallyGiven X) (U V : Opens X.carrier)
    (hU : U ∈ S.opens) (hV : V ∈ S.opens) :
    (∃ A : SolutionOver S (U ⊓ V),
        A.obj = (S.restriction (U ⊓ V) U inf_le_left).obj (S.obj U hU)) ∧
      ∃ B : SolutionOver S (U ⊓ V),
        B.obj = (S.restriction (U ⊓ V) V inf_le_right).obj (S.obj V hV)
```

## Tag 0D6A, a lemma

[Tag 0D6A](https://stacks.math.columbia.edu/tag/0D6A) in the Stacks Project.

**`Stacks.DerivedGlueing.exists_solution_of_finite_cover_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/GlueingForHomsWithoutCovering.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/GlueingForHomsWithoutCovering.lean#L113). The attribute's comment: “existence: for X = U\_1 ∪ … ∪ U\_n with U\_i in the collection, intersections of members covered by members, and no negative self-Ext of the prescribed objects, the system has a solution”.

> **[Stacks, Tag 0D6A], existence.**
> In Situation 0D67, suppose that `X = U_1 ∪ … ∪ U_n` with the `U_i` in the displayed collection,
> that the intersection of two members of the collection is the union of the members contained in
> it, and that the prescribed objects have no negative self-`Ext`.  Then the system has a solution.
>
> The proof applies `Stacks.DerivedGlueing.exists_solution_of_finite_cover_of_homs`; the sheaf
> condition of [Stacks, Tag 0D66] part (2) for every subsystem is
> `Stacks.DerivedGlueing.hasGluingForHomsOver_of_covers`, a theorem with no binder beyond the
> system.  The nonemptiness `hs` of the cover is
> used here: the induction of `Stacks.DerivedGlueing.exists_solutionOver_finsetSup` runs on
> `Finset.Nonempty.cons_induction` and starts from a single member.

```lean
theorem exists_solution_of_finite_cover_unconditional (S : LocallyGiven X)
    (s : Finset (Opens X.carrier)) (hs : s.Nonempty) (hmem : ∀ U ∈ s, U ∈ S.opens)
    (hcover : s.sup id = ⊤)
    (hinter : ∀ U ∈ S.opens, ∀ V ∈ S.opens, U ⊓ V = sSup {W | W ∈ S.opens ∧ W ≤ U ⊓ V})
    (hExt : ∀ (U : Opens X.carrier) (hU : U ∈ S.opens), ∀ i : ℤ, i < 0 →
      Subsingleton (ShiftedHom (S.obj U hU) (S.obj U hU) i)) :
    Nonempty (Solution S)
```

**`Stacks.DerivedGlueing.exists_solution_and_unique_solutionIso_of_finite_cover_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/GlueingForHomsWithoutCovering.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/GlueingForHomsWithoutCovering.lean#L137). The attribute's comment: “the whole tag: for X = U\_1 ∪ … ∪ U\_n with U\_i in the collection, intersections of members covered by members, and no negative self-Ext of the prescribed objects, a solution exists and is unique up to unique isomorphism”.

> **[Stacks, Tag 0D6A] in full**: under the conditions (1), (2) and (3) of the tag the
> system has a solution, and any two solutions are identified by exactly one isomorphism of
> solutions.
>
> Both clauses of the tag in one statement, the existence clause above together with the
> uniqueness clause of [Stacks, Tag 0D68] over the finite cover.  The conclusion
> `Stacks.DerivedGlueing.Solution.IsCompatibleHom A B ψ.hom` is by definition
> `∀ (U : Opens X.carrier) (hU : U ∈ S.opens), (S.restriction U ⊤ le\_top).map ψ.hom ≫
> (B.rho U hU).hom = (A.rho U hU).hom`, which is "compatible with the `ρ\_U`" as the source means
> it.

```lean
theorem exists_solution_and_unique_solutionIso_of_finite_cover_unconditional (S : LocallyGiven X)
    (s : Finset (Opens X.carrier)) (hs : s.Nonempty) (hmem : ∀ U ∈ s, U ∈ S.opens)
    (hcover : s.sup id = ⊤)
    (hinter : ∀ U ∈ S.opens, ∀ V ∈ S.opens, U ⊓ V = sSup {W | W ∈ S.opens ∧ W ≤ U ⊓ V})
    (hExt : ∀ (U : Opens X.carrier) (hU : U ∈ S.opens), ∀ i : ℤ, i < 0 →
      Subsingleton (ShiftedHom (S.obj U hU) (S.obj U hU) i)) :
    Nonempty (Solution S) ∧
      ∀ A B : Solution S, ∃! ψ : A.obj ≅ B.obj, A.IsCompatibleHom B ψ.hom
```

**`Stacks.DerivedGlueing.exists_solution_of_top_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/GlueingOverAFiniteCover.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/GlueingOverAFiniteCover.lean#L290). The attribute's comment: “existence when a single member of the collection is all of X”.

> **[Stacks, Tag 0D6A] when the cover has a single member.** If the whole of `X` belongs to
> the collection, then the system has a solution: the prescribed object on `⊤` is one.
>
> This is the case `n = 1` of the tag.

```lean
theorem exists_solution_of_top_mem (S : LocallyGiven X) (htop : ⊤ ∈ S.opens) :
    Nonempty (Solution S)
```

**`Stacks.DerivedGlueing.exists_unique_solutionIso_of_top_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/UniquenessOverACover.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/UniquenessOverACover.lean#L172). The attribute's comment: “uniqueness up to unique isomorphism when a single member of the collection is all of X, the case n = 1”.

> **[Stacks, Tag 0D6A] when the cover has a single member: uniqueness up to unique
> isomorphism.** If the whole of `X` belongs to the collection, then any two solutions are
> identified by exactly one isomorphism of solutions.
>
> This is the case `n = 1` of the tag: restriction from `⊤` to `⊤` is the identity functor, by
> `Stacks.DerivedGlueing.restrictionSelfIso`, so the identifications over `⊤` of the two solutions
> compose to the required isomorphism and determine it; and compatibility over `⊤` forces
> compatibility over every member, by `Stacks.DerivedGlueing.Solution.isCompatibleHom_of_top`.
>
> Together with `Stacks.DerivedGlueing.exists_solution_of_top_mem` this is the whole of Tag 0D6A
> for `n = 1`.

```lean
theorem exists_unique_solutionIso_of_top_mem (S : LocallyGiven X) (htop : ⊤ ∈ S.opens)
    (A B : Solution S) :
    ∃! φ : A.obj ≅ B.obj, A.IsCompatibleHom B φ.hom
```

## Tag 0D6B, a lemma

[Tag 0D6B](https://stacks.math.columbia.edu/tag/0D6B) in the Stacks Project.

**`Stacks.DerivedGlueing.exists_glueing_of_wellOrderedCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/WellOrderedCoverRecursion.lean, line 1180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/WellOrderedCoverRecursion.lean#L1180). The attribute's comment: “the glued object `G` over `⊤` with identifications `sigma α` of its restrictions with the `K α`, compatible with the prescribed `ρ^α_β` for every `β < α`, for a well ordered covering with `hsucc` (`W_α ⊆ W_{α+1}`), `hlimit` (continuity at the stages that are not successors), `hcover`, `hExt` (no negative self-Ext) and the cocycle condition `hcocycle`”.

> **[Stacks, Tag 0D6B].** Let `X` be a ringed space, let `E` be a well ordered set and let
> `X = ⋃_{α ∈ E} W_α` be an open covering with `W_α ⊆ W_{α+1}` and `W_α = ⋃_{β < α} W_β` when `α`
> is not a successor.  Let `K_α` be an object of `D(𝒪_{W_α})` with `Ext^i(K_α, K_α) = 0` for
> `i < 0`, and let `ρ^α_β : K_α|_{W_β} ≅ K_β` for `β < α` satisfy
> `ρ^α_γ = ρ^β_γ ∘ ρ^α_β|_{W_γ}` for `γ < β < α`.  Then there is an object `K` of `D(𝒪_X)` and
> isomorphisms `K|_{W_α} ≅ K_α` compatible with the `ρ^α_β`.
>
> "`β` is the immediate predecessor of `α`" is rendered as "`β < α` and every `γ < α` satisfies
> `γ ≤ β`", so `hsucc` is the inclusion `W_α ⊆ W_{α+1}` and `hlimit` the continuity at the stages
> that are not successors; `Stacks.DerivedGlueing.le_of_succ_of_limit` derives from them the
> inclusion `W_β ⊆ W_α` for every `β < α` along which the transitions are stated.
>
> The system `S : Stacks.DerivedGlueing.LocallyGiven X` (the structure of
> `StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/LocallyGivenObjects.lean`, not
> `RingedSite.LocallyGiven`) is exactly Situation 0D67 and carries no further data: its restriction
> functors `S.restriction V U` are the canonical derived restrictions `j^*` along the inclusions
> `V ⊆ U`, since the field `restrictionFactors` identifies each with the derived functor of the
> restriction of complexes `openModuleRestriction` through the localization, and its comparisons
> `S.restrictionComp` are the canonical ones, by the field `restrictionCompFactors`.

```lean
theorem exists_glueing_of_wellOrderedCover (S : Stacks.DerivedGlueing.LocallyGiven X)
    (E : Type v) [LinearOrder E] [WellFoundedLT E]
    (W : E → Opens X.carrier)
    (hsucc : ∀ β α : E, β < α → (∀ γ : E, γ < α → γ ≤ β) → W β ≤ W α)
    (hlimit : ∀ α : E, (¬ ∃ β : E, β < α ∧ ∀ γ : E, γ < α → γ ≤ β) →
      W α = ⨆ (β : E) (_ : β < α), W β)
    (hcover : (⨆ α : E, W α) = ⊤) (K : ∀ α : E, OpenDerivedCategory X (W α))
    (hExt : ∀ (α : E) (i : ℤ), i < 0 → Subsingleton (ShiftedHom (K α) (K α) i))
    (rho : ∀ (β α : E) (h : β < α),
      (S.restriction (W β) (W α) (le_of_succ_of_limit W hsucc hlimit β α h)).obj (K α) ≅ K β)
    (hcocycle : ∀ (γ β α : E) (hγβ : γ < β) (hβα : β < α),
      (rho γ α (hγβ.trans hβα)).hom =
        (S.restrictionComp (W γ) (W β) (W α) (le_of_succ_of_limit W hsucc hlimit γ β hγβ)
            (le_of_succ_of_limit W hsucc hlimit β α hβα)).hom.app (K α) ≫
          (S.restriction (W γ) (W β)
            (le_of_succ_of_limit W hsucc hlimit γ β hγβ)).map (rho β α hβα).hom ≫
            (rho γ β hγβ).hom) :
    ∃ (G : OpenDerivedCategory X ⊤)
      (sigma : ∀ α : E, (S.restriction (W α) ⊤ le_top).obj G ≅ K α),
      ∀ (β α : E) (h : β < α),
        (S.restrictionComp (W β) (W α) ⊤
              (le_of_succ_of_limit W hsucc hlimit β α h) le_top).hom.app G ≫
            (S.restriction (W β) (W α)
              (le_of_succ_of_limit W hsucc hlimit β α h)).map (sigma α).hom ≫ (rho β α h).hom =
          (sigma β).hom
```

## Tag 0D6C, a theorem

[Tag 0D6C](https://stacks.math.columbia.edu/tag/0D6C) in the Stacks Project.

**`Stacks.DerivedGlueing.exists_solution_and_unique_solutionIso_of_covers_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/BBDGlueing.lean, line 433](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/BBDGlueing.lean#L433). The attribute's comment: “existence of a solution `(K, ρ_U)` and its uniqueness up to unique isomorphism, for a collection satisfying (1) `hcover`, (2) `hinter` and (3) `hExt`”.

> **[Stacks, Tag 0D6C] (BBD gluing lemma).** In Situation 0D67 suppose that the members of the
> collection cover `X`, that for two members `U, V` the intersection `U ∩ V` is the union of the
> members contained in it, and that `Ext^i(K_U, K_U) = 0` for `i < 0` and every member `U`.  Then
> the system has a solution, and any two solutions are identified by exactly one isomorphism of
> solutions.
>
> A solution is a `Stacks.DerivedGlueing.Solution`: an object `K` of `D(𝒪_X)` with isomorphisms
> `ρ_U : K|_U ≅ K_U` satisfying `ρ^U_V ∘ ρ_U|_V = ρ_V`.  The conclusion
> `Stacks.DerivedGlueing.Solution.IsCompatibleHom A B ψ.hom` says that `ψ` is compatible with the
> `ρ_U` of the two solutions.

```lean
theorem exists_solution_and_unique_solutionIso_of_covers_unconditional (S : LocallyGiven X)
    (hcover : sSup S.opens = ⊤)
    (hinter : ∀ U ∈ S.opens, ∀ V ∈ S.opens, U ⊓ V = sSup {W | W ∈ S.opens ∧ W ≤ U ⊓ V})
    (hExt : ∀ (U : Opens X.carrier) (hU : U ∈ S.opens), ∀ i : ℤ, i < 0 →
      Subsingleton (ShiftedHom (S.obj U hU) (S.obj U hU) i)) :
    Nonempty (Solution S) ∧
      ∀ A B : Solution S, ∃! ψ : A.obj ≅ B.obj, A.IsCompatibleHom B ψ.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.45, Tag 0D65](https://stacks.math.columbia.edu/tag/0D65)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
