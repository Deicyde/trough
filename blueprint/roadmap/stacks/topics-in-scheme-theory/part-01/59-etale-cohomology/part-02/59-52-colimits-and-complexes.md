---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.EtaleComplexSystem.isSystemColimit_etaleHypercohomologyPullback, Stacks.EtaleCohomology.preservesColimit_rightDerivedFunctorPlus_Γ_smallEtale_of_isGE, Stacks.EtaleCohomology.isSystemColimit_etaleHypercohomologyMap_of_isLimit, Stacks.EtaleCohomology.LimitHigherDirectImage.pullbackProjectionMap, Stacks.EtaleCohomology.LimitHigherDirectImage.derivedPullbackHigherDirectImageColimit, Stacks.EtaleCohomology.LimitHigherDirectImage.complexHigherDirectImageColimit, Stacks.EtaleCohomology.LimitHigherDirectImage.complexProjectionMap, Stacks.EtaleCohomology.preservesColimit_etaleModuleDerivedDirectImage_of_isGE
statement: formalized
proof: formalized
---

# 59.52 Colimits and complexes

Section 59.52 of the Stacks Project, [Tag 0GIR](https://stacks.math.columbia.edu/tag/0GIR). 6 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EZM, a lemma

[Tag 0EZM](https://stacks.math.columbia.edu/tag/0EZM) in the Stacks Project.

**`Stacks.EtaleCohomology.EtaleComplexSystem.isSystemColimit_etaleHypercohomologyPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/ComplexSystemCohomologyColimit.lean, line 651](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/ComplexSystemCohomologyColimit.lean#L651).

> **Étale cohomology commutes with colimits of bounded below systems of complexes over a limit
> of schemes** ([Stacks, Tag 0EZM]). Let `X = lim X_i` be the limit of a directed inverse system of
> quasi-compact and quasi-separated schemes with affine transition morphisms, `(ℱ_i^•, φ_{i'i})` a
> system of complexes of abelian sheaves on the small étale sites of the `X_i` with `ℱ_i^n = 0` for
> `n < a`, `a` independent of `i`, and `ι_i : f_i⁻¹ℱ_i^• ⟶ ℱ^•` maps of complexes, compatible with
> the transition maps, which present every term `ℱ^n` as the colimit `colim f_i⁻¹ℱ_i^n`. Then for
> every `p ∈ ℤ` the pull back maps `H^p(X_i, ℱ_i^•) ⟶ H^p(X, ℱ^•)` exhibit `H^p(X, ℱ^•)` as the
> colimit of the system of the `H^p(X_i, ℱ_i^•)`.

```lean
theorem isSystemColimit_etaleHypercohomologyPullback (a : ℤ) [∀ i, (F.obj i).IsStrictlyGE a]
    (𝓕 : CochainComplex (Sheaf (smallEtaleTopology c.pt) Ab.{u + 1}) ℤ)
    (ι : ∀ i : Iᵒᵖ, ((smallEtalePullbackAb (c.π.app i)).mapHomologicalComplex _).obj (F.obj i) ⟶ 𝓕)
    (hι : F.IsPullbackCocone c ι)
    (hpres : ∀ n, LimitHigherDirectImage.IsPullbackColimitPresentation c (𝓕.X n) (F.term n)
      (fun i => (ι i).f n)) (p : ℤ) :
    IsSystemColimit
      (fun i => AddCommGrpCat.of
        (etaleHypercohomology (D.obj i) (DerivedCategory.Q.obj (F.obj i)) p))
      (fun a => AddCommGrpCat.ofHom (etaleHypercohomologyPullback (D.map a) (F.map a) p))
      (AddCommGrpCat.of (etaleHypercohomology c.pt (DerivedCategory.Q.obj 𝓕) p))
      (fun i => AddCommGrpCat.ofHom (etaleHypercohomologyPullback (c.π.app i) (ι i) p))
```

## Tag 0GIS, a lemma

[Tag 0GIS](https://stacks.math.columbia.edu/tag/0GIS) in the Stacks Project.

**`Stacks.EtaleCohomology.preservesColimit_rightDerivedFunctorPlus_Γ_smallEtale_of_isGE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BoundedBelowDirectSumsGlobalSections.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BoundedBelowDirectSumsGlobalSections.lean#L101). The attribute's comment: “RΓ(X, ⨁ K_i) = ⨁ RΓ(X, K_i) for a family of D⁺(X_étale) with common lower bound a, on a quasi-compact quasi-separated scheme. The global sections case of the machinery behind Tag 0GIW; unlike that tag nothing is carried, the input that H^q_étale(X, -) commutes with direct sums being `preservesColimitsOfShape_discrete_rightDerived_Γ_smallEtale`. The index type lies in Type (max (u+1) v), the universe at which the abelian sheaves on the small étale site are Grothendieck abelian: the termwise direct sum of the resolutions is formed inside that category, so the index universe and the Grothendieck universe are the same.”.

> **[Stacks, Tag 0GIS].** Let `X` be a quasi-compact and quasi-separated scheme, let
> `K : I → D⁺(X_étale)` be a family of objects of the bounded below derived category of abelian
> sheaves on the small étale site of `X` and let `a : ℤ` be such that `H^n(K i) = 0` for `n < a`
> and all `i`, that is `(K i).IsGE a`. Then `RΓ(X, ⨁ i, K i) = ⨁ i, RΓ(X, K i)`.
>
> Nothing is assumed: the one input of the argument beyond the injective resolutions bounded below
> by `a` of [Stacks, Tag 07D9] and Leray's acyclicity lemma [Stacks, Tag 015E] is that each
> `H^q_étale(X, -)` commutes with the direct sum, which is
> `Stacks.EtaleCohomology.preservesColimitsOfShape_discrete_rightDerived_Γ_smallEtale`, and that
> is where the quasi-compactness and quasi-separatedness of `X` are used.
>
> The source states the lemma in `D(X_étale)`; its hypothesis places every `K i` in `D⁺`, and the
> module docstring records why the statement is read there and why the index universe is
> `max (u + 1) v`.

```lean
theorem preservesColimit_rightDerivedFunctorPlus_Γ_smallEtale_of_isGE
    (X : Scheme.{u}) [CompactSpace X] [QuasiSeparatedSpace X] {I : Type (max (u + 1) v)}
    (K : I → DerivedCategory.Plus (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}))
    (a : ℤ) (hK : ∀ i, (K i).IsGE a) :
    PreservesColimit (Discrete.functor K)
      (Sheaf.Γ X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}).rightDerivedFunctorPlus
```

## Tag 0GIT, a lemma

[Tag 0GIT](https://stacks.math.columbia.edu/tag/0GIT) in the Stacks Project.

**`Stacks.EtaleCohomology.isSystemColimit_etaleHypercohomologyMap_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/ComplexSystemCohomologyColimit.lean, line 758](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/ComplexSystemCohomologyColimit.lean#L758).

> **Étale cohomology of a bounded below complex pulled back to a limit of schemes**
> ([Stacks, Tag 0GIT]). Let `S` be a scheme, `X = lim X_i` the limit of a directed inverse system of
> quasi-compact and quasi-separated schemes over `S`, with structure morphisms `ι_i : X_i ⟶ S`,
> `g : X ⟶ S` and affine transition morphisms, and `K ∈ D^+(S_étale)`. Then for every `p ∈ ℤ` the
> pull back maps `H^p(X_i, K|_{X_i}) ⟶ H^p(X, K|_X)` exhibit `H^p(X, K|_X)` as the colimit of the
> system of the `H^p(X_i, K|_{X_i})`. Here `K|_{X_i}` is the derived inverse image of `K` along
> `ι_i`, and the transition maps are induced by the comparisons `f_{i'i}⁻¹ ι_i⁻¹ ≅ ι_{i'}⁻¹` and
> `f_i⁻¹ ι_i⁻¹ ≅ g⁻¹` of inverse images along composites.

```lean
theorem isSystemColimit_etaleHypercohomologyMap_of_isLimit (ι : ∀ i, D.obj i ⟶ S)
    (hι : ∀ {i j : Iᵒᵖ} (a : i ⟶ j), D.map a ≫ ι j = ι i) (g : c.pt ⟶ S)
    (hg : ∀ i, c.π.app i ≫ ι i = g)
    (K : DerivedCategory.Plus (Sheaf (smallEtaleTopology S) Ab.{u + 1})) (p : ℤ) :
    IsSystemColimit
      (fun i => AddCommGrpCat.of (etaleHypercohomology (D.obj i)
        ((smallEtalePullbackAb (ι i)).mapDerivedCategory.obj K.obj) p))
      (fun {i j} a => AddCommGrpCat.ofHom (etaleHypercohomologyMap (D.map a)
        ((Functor.mapDerivedCategoryIsoComp _ _ _
          (smallEtalePullbackAbComp' (D.map a) (ι j) (ι i) (hι a).symm)).inv.app K.obj) p))
      (AddCommGrpCat.of (etaleHypercohomology c.pt
        ((smallEtalePullbackAb g).mapDerivedCategory.obj K.obj) p))
      (fun i => AddCommGrpCat.ofHom (etaleHypercohomologyMap (c.π.app i)
        ((Functor.mapDerivedCategoryIsoComp _ _ _
          (smallEtalePullbackAbComp' (c.π.app i) (ι i) g (hg i).symm)).inv.app K.obj) p))
```

## Tag 0GIU, a lemma

[Tag 0GIU](https://stacks.math.columbia.edu/tag/0GIU) in the Stacks Project.

**`Stacks.EtaleCohomology.LimitHigherDirectImage.pullbackProjectionMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitHigherDirectImageDerived.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitHigherDirectImageDerived.lean#L276). The attribute's comment: “the comparison maps `h_i^{-1} R^p g_{i, *} K_i ⟶ R^p g_* K` of the assertion, for all `p ∈ ℤ`, with `K_i` the derived pullback of `K_0 ∈ D^+(X_{0, étale})` to `X_i`, built from the derived base change comparison of Stacks 0F02 together with exactness of `h_i^{-1}`; their naturality in `K_0` is `derivedProjectionMap_naturality`. The colimit assertion `R^p g_* K = colim_{i ≥ 0} h_i^{-1} R^p g_{i, *} K_i` is NOT proved, and cannot be: it is a formal consequence (by the dimension-shifting induction of the source over the triangle `H^a(K_0)[-a] → K_0 → τ_{≥ a+1}K_0`) of the colimit assertion of Stacks 0EYM, which the carrier `Stacks.EtaleCohomology.LimitHigherDirectImage.projectionMap` of that tag states in its own clause string is not proved; indeed the colimit itself cannot be formed, since that needs the cocycle condition of Stacks 0E47 which 0EYM's carrier also leaves open. EXTRA HYPOTHESIS: the pullback `K` of `K_0` to `X` and the isomorphisms `κ_i : R f_i^{-1} K_i ≅ K` are taken as data, as `ℱ` and `ι_i` are in 0EYM's carrier and as `K` is given data in the source; this is a generalization, since in the source's situation those data exist.”.

> **The comparison map of Stacks 0GIU**, `h_i^{-1} R^p g_{i, *} K_i ⟶ R^p g_* K`, for
> `K_0 ∈ D^+(X_{0, étale})`, `K_i` the pullback of `K_0` to `X_i` and `K` the pullback of `K_0` to
> `X`: the derived comparison map `derivedProjectionMap` at `L = K_i`, `M = K` and
> `κ = κ_i : R f_i^{-1} K_i ≅ K`.

```lean
def pullbackProjectionMap (K₀ : PlusAb (DX.obj i₀)) (K : PlusAb cX.pt) {i : Iᵒᵖ} (a : i ⟶ i₀)
    (κ : (derivedPullbackAb (cX.π.app i)).obj (derivedLevelPullback a K₀) ≅ K) :
    (smallEtalePullbackAb (cS.π.app i)).obj
        ((homologyAb (DS.obj i) p).obj
          ((derivedPushforwardAb (γ.app i)).obj (derivedLevelPullback a K₀))) ⟶
      (homologyAb cS.pt p).obj
        ((derivedPushforwardAb (limitMorphism γ cX cS hcS)).obj K)
```

**`Stacks.EtaleCohomology.LimitHigherDirectImage.derivedPullbackHigherDirectImageColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitHigherDirectImageDerivedColimit.lean, line 510](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitHigherDirectImageDerivedColimit.lean#L510). References: SGA 4 VII (5.11), “more general”.

> Let `I` be a directed set, `g_i : X_i ⟶ S_i` an inverse system of
> quasi-compact and quasi-separated morphisms of schemes with affine transition morphisms
> `f_{i'i}`, `h_{i'i}`, and `g : X ⟶ S` its limit with projections `f_i`, `h_i`. Let `0 = i₀ ∈ I`,
> `K_0 ∈ D^+(X_{0, étale})`, `K_i = R f_{i0}^{-1}K_0` its pullback to `X_i` for `i ≥ 0` and
> `K = R f_0^{-1}K_0` its pullback to `X`. Then for every `p ∈ ℤ` the maps
> `h_{i'i}^{-1}R^pg_{i, *}K_i ⟶ R^pg_{i', *}K_{i'}` (the derived base change maps of the
> transition squares composed with `R^pg_{i', *}` of `R f_{i'i}^{-1}K_i ≅ K_{i'}`), pulled back to
> `S`, satisfy the cocycle condition, the maps `h_i^{-1}R^pg_{i, *}K_i ⟶ R^pg_*K` (the derived base
> change maps of the projection squares composed with `R^pg_*` of `R f_i^{-1}K_i ≅ K`) are
> compatible with them, and they present `R^pg_*K = colim_{i ≥ 0} h_i^{-1}R^pg_{i, *}K_i`.

```lean
theorem derivedPullbackHigherDirectImageColimit (K₀ : PlusAb (DX.obj (op i₀))) (p : ℤ) :
    (∀ {j j' j'' : (Set.Ici i₀)ᵒᵖ} (c : j ⟶ j') (c' : j' ⟶ j''),
        derivedPullbackTransition γ cS i₀ p K₀ (c ≫ c') =
          derivedPullbackTransition γ cS i₀ p K₀ c' ≫ derivedPullbackTransition γ cS i₀ p K₀ c) ∧
      (∀ {j j' : (Set.Ici i₀)ᵒᵖ} (c : j ⟶ j'),
        derivedPullbackTransition γ cS i₀ p K₀ c ≫ derivedPullbackLeg γ cX cS i₀ p K₀
            (limitMorphism γ cX cS hcS) (fun j => limitMorphism_comp_π γ cX cS hcS _) j =
          derivedPullbackLeg γ cX cS i₀ p K₀ (limitMorphism γ cX cS hcS)
            (fun j => limitMorphism_comp_π γ cX cS hcS _) j') ∧
      IsSystemColimit (derivedPullbackTerm γ cS i₀ p K₀)
        (fun {j j'} c => derivedPullbackTransition γ cS i₀ p K₀ (j := j) (j' := j') c)
        ((homologyAb cS.pt p).obj ((derivedPushforwardAb (limitMorphism γ cX cS hcS)).obj
          ((derivedPullbackAb (cX.π.app (op i₀))).obj K₀)))
        (derivedPullbackLeg γ cX cS i₀ p K₀ (limitMorphism γ cX cS hcS)
          (fun j => limitMorphism_comp_π γ cX cS hcS _))
```

## Tag 0GIV, a lemma

[Tag 0GIV](https://stacks.math.columbia.edu/tag/0GIV) in the Stacks Project.

**`Stacks.EtaleCohomology.LimitHigherDirectImage.complexHigherDirectImageColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/ComplexHigherDirectImageColimitTheorem.lean, line 438](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/ComplexHigherDirectImageColimitTheorem.lean#L438). References: SGA 4 VII (5.11), “more general”.

> **[Stacks, Tag 0GIV].** Let `I` be a directed set, `g_i : X_i ⟶ S_i` an inverse system of
> quasi-compact and quasi-separated morphisms of schemes with affine transition morphisms
> `f_{i'i}`, `h_{i'i}`, and `g : X ⟶ S` its limit with projections `f_i`, `h_i`. Let
> `(ℱ_i^•, φ_{i'i})` be a system of complexes of abelian sheaves on the `X_{i, étale}`, with
> `ℱ_i^n = 0` for `n < a` and all `i`, and `ℱ^• = colim f_i^{-1}ℱ_i^•`, presented by maps of
> complexes `ι_i : f_i^{-1}ℱ_i^• ⟶ ℱ^•` compatible with the transition maps and presenting every
> term `ℱ^n` as `colim f_i^{-1}ℱ_i^n`. Then for every `p ∈ ℤ` the maps
> `h_i^{-1}R^pg_{i, *}ℱ_i^• ⟶ R^pg_*ℱ^•` (the derived base change maps of the projection squares
> followed by `R^pg_*ι_i`) are compatible with the maps
> `h_{i'i}^{-1}R^pg_{i, *}ℱ_i^• ⟶ R^pg_{i', *}ℱ_{i'}^•` of the system of the
> `R^pg_{i, *}ℱ_i^•` and present `R^pg_*ℱ^• = colim_i h_i^{-1}R^pg_{i, *}ℱ_i^•`.

```lean
theorem complexHigherDirectImageColimit (F : EtaleComplexSystem DX) (a : ℤ)
    [∀ i, (F.obj i).IsStrictlyGE a]
    (𝓕 : CochainComplex (Sheaf (smallEtaleTopology cX.pt) Ab.{u + 1}) ℤ)
    (ι : ∀ i : Iᵒᵖ, ((smallEtalePullbackAb (cX.π.app i)).mapHomologicalComplex _).obj (F.obj i) ⟶ 𝓕)
    (hι : F.IsPullbackCocone cX ι)
    (hpres : ∀ n, IsPullbackColimitPresentation cX (𝓕.X n) (F.term n) (fun i => (ι i).f n))
    (p : ℤ) :
    haveI := F.isStrictlyGE_of_isPullbackColimitPresentation a hpres
    (∀ {i j : Iᵒᵖ} (c : i ⟶ j),
        (complexHigherDirectImageSystem γ p a F).pullbackDiagramMap cS (i := i) (j := j) c ≫
          complexLeg γ p a F cX cS hcS 𝓕 ι i = complexLeg γ p a F cX cS hcS 𝓕 ι j) ∧
      IsComplexHigherDirectImageColimit γ p a F cX cS hcS 𝓕 ι
```

**`Stacks.EtaleCohomology.LimitHigherDirectImage.complexProjectionMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitHigherDirectImageDerived.lean, line 368](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitHigherDirectImageDerived.lean#L368). The attribute's comment: “the comparison maps `h_i^{-1} R^p g_{i, *} ℱ_i^• ⟶ R^p g_* ℱ^•` of the assertion, for all `p ∈ ℤ`, where `R^p g_*` of a complex is the degree-`p` cohomology of the total right derived direct image of its class in `D^+`; built from the derived base change comparison of Stacks 0F02, exactness of `h_i^{-1}`, and — for the pullback of the complex — the invertibility of the right-derived-functor unit of the exact functor `f_i^{-1}`. The uniform lower bound `a` of the source (`ℱ_i^n = 0` for `n < a`, `a` independent of `i`) is carried as `CochainComplex.IsStrictlyGE`; naturality is `derivedProjectionMap_naturality`. The colimit assertion `R^p g_*(colim f_i^{-1}ℱ_i^•) = colim_{i ≥ 0} h_i^{-1} R^p g_{i, *} ℱ_i^•` is NOT proved, and cannot be: it is a formal consequence (by the two spectral sequences of a Cartan-Eilenberg resolution, Stacks 015J) of the colimit assertion of Stacks 0EYM, which the carrier `Stacks.EtaleCohomology.LimitHigherDirectImage.projectionMap` of that tag states in its own clause string is not proved; indeed the colimit itself cannot be formed, since that needs the cocycle condition of Stacks 0E47 which 0EYM's carrier also leaves open. EXTRA HYPOTHESIS: the complex `ℱ^• = colim f_i^{-1}ℱ_i^•` and the maps of complexes `ι_i : f_i^{-1}ℱ_i^• ⟶ ℱ^•` are taken as data, as `ℱ` and `ι_i` are in 0EYM's carrier and as the colimit is given data in the source; this is a generalization, since in the source's situation those data exist. The transition maps `φ_{i'i}` and their cocycle condition are the data of the system; the transition form of the comparison map is `derivedTransitionMap`.”.

> **The comparison map of Stacks 0GIV**, `h_i^{-1} R^p g_{i, *} ℱ_i^• ⟶ R^p g_* ℱ^•`, for a
> complex `ℱ_i^•` of abelian sheaves on `X_{i, étale}` vanishing in degrees `< a`, a complex `ℱ^•`
> on `X_étale` vanishing in degrees `< a`, and a map of complexes
> `ι_i : f_i^{-1}ℱ_i^• ⟶ ℱ^•`: the derived comparison map `derivedProjectionMap` at the classes of
> the two complexes in the bounded below derived categories, with `κ` the comparison
> `complexPullbackComparison`.

```lean
def complexProjectionMap (i : Iᵒᵖ)
    (F : CochainComplex (Sheaf (smallEtaleTopology (DX.obj i)) Ab.{u + 1}) ℤ) [F.IsStrictlyGE a]
    (G : CochainComplex (Sheaf (smallEtaleTopology cX.pt) Ab.{u + 1}) ℤ) [G.IsStrictlyGE a]
    (ι : complexPullbackObj cX i F ⟶ G) :
    (smallEtalePullbackAb (cS.π.app i)).obj
        ((homologyAb (DS.obj i) p).obj
          ((derivedPushforwardAb (γ.app i)).obj (plusComplexObj a F))) ⟶
      (homologyAb cS.pt p).obj
        ((derivedPushforwardAb (limitMorphism γ cX cS hcS)).obj (plusComplexObj a G))
```

## Tag 0GIW, a lemma

[Tag 0GIW](https://stacks.math.columbia.edu/tag/0GIW) in the Stacks Project.

**`Stacks.EtaleCohomology.preservesColimit_etaleModuleDerivedDirectImage_of_isGE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BoundedBelowDirectSums.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BoundedBelowDirectSums.lean#L316). The attribute's comment: “Rf_*(⨁ K_i) = ⨁ Rf_* K_i for a family of D⁺(X_étale, Λ) with common lower bound a. Tag 09Z1, that each R^q f_* on the small étale site commutes with direct sums, is carried as the hypothesis `hsums`, since it is not proved in this library; everything else the source cites is proved. The index type lies in Type (max (u+1) r), the universe at which the sheaves of Λ-modules on the small étale sites are Grothendieck abelian: the termwise direct sum of the resolutions is formed inside those categories, so the index universe and the Grothendieck universe are the same. For Λ a general ring.”.

> **[Stacks, Tag 0GIW].** Let `Λ` be a ring, let `f : X ⟶ Y` be a quasi-compact and
> quasi-separated morphism of schemes, let `K : I → D⁺(X_étale, Λ)` be a family of objects and
> let `a : ℤ` be such that `H^n(K i) = 0` for `n < a` and all `i`, that is `(K i).IsGE a`. Then
> `Rf_*(⨁ i, K i) = ⨁ i, Rf_*(K i)`.
>
> The one input that is carried rather than used is `hsums`: that each ordinary higher direct
> image `R^q f_*` on the small étale site commutes with the direct sum. That is
> [Stacks, Tag 09Z1], which is not proved in this repository, so it appears here as a hypothesis,
> in the shape in which the source cites it. Nothing else is assumed: that `f_*` itself commutes
> with the direct sum is *proved* from `hsums` at `q = 0`, and the rest of the argument of the
> source — the injective resolutions bounded below by `a` of [Stacks, Tag 07D9], the right
> acyclicity of their termwise direct sum, and Leray's acyclicity lemma [Stacks, Tag 015E]
> identifying `Rf_*` with the termwise image on each of them — is proved.
>
> Quasi-compactness and quasi-separatedness of `f` are the hypotheses under which the source's
> proof invokes [Stacks, Tag 09Z1]; they are carried here even though the argument consumes them
> only through `hsums`, so that the statement is the source's.
>
> The source states the lemma in `D(X_étale)`; its hypothesis places every `K_i` in `D⁺`, and the
> module docstring records why the statement is read there, why the coefficients are an arbitrary
> ring, and why the index universe is `max (u + 1) r`.

```lean
theorem preservesColimit_etaleModuleDerivedDirectImage_of_isGE
    {X Y : Scheme.{u}} (f : X ⟶ Y) [QuasiCompact f] [QuasiSeparated f]
    {I : Type (max (u + 1) r)}
    (hsums : ∀ p : ℕ, PreservesColimitsOfShape (Discrete I)
      ((etaleModuleDirectImage.{u, r} Λ f).rightDerived p))
    (K : I → DerivedCategory.Plus (EtaleModules.{u, r} Λ X)) (a : ℤ)
    (hK : ∀ i, (K i).IsGE a) :
    PreservesColimit (Discrete.functor K) (etaleModuleDerivedDirectImage.{u, r} Λ f)
```

**`Stacks.EtaleCohomology.preservesColimit_etaleAbelianDerivedDirectImage_of_isGE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedDirectImageBoundedBelowSums.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedDirectImageBoundedBelowSums.lean#L193).

> **[Stacks, Tag 0GIW].** Let `f : X ⟶ Y` be a quasi-compact and quasi-separated morphism of
> schemes, let `K : I → D(X_étale)` be a family of objects of the derived category of abelian
> sheaves on the small étale site of `X`, and let `a : ℤ` be such that `H^n(K i) = 0` for `n < a`
> and all `i`, that is `(K i).IsGE a`. Then `Rf_*(⨁ i, K i) = ⨁ i, Rf_*(K i)`: the unbounded
> derived direct image `Rf_* : D(X_étale) ⥤ D(Y_étale)` preserves the direct sum of the family.
>
> Nothing is assumed beyond the source's hypotheses. That each `R^q f_*` commutes with direct sums
> is `preservesColimitsOfShape_discrete_rightDerived_etaleAbelianDirectImage`, where
> quasi-compactness and quasi-separatedness of `f` are used.

```lean
theorem preservesColimit_etaleAbelianDerivedDirectImage_of_isGE
    {X Y : Scheme.{u}} (f : X ⟶ Y) [QuasiCompact f] [QuasiSeparated f]
    {I : Type (max (u + 1) v)}
    (K : I → DerivedCategory (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}))
    (a : ℤ) (hK : ∀ i, (K i).IsGE a) :
    PreservesColimit (Discrete.functor K) (etaleAbelianDerivedDirectImage.{u, v} f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.52, Tag 0GIR](https://stacks.math.columbia.edu/tag/0GIR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
