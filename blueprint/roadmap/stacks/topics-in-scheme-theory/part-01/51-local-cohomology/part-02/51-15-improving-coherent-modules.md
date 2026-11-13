---
declaration: section
origin: cited
lean: AlgebraicGeometry.depthOneQuotient_spec, AlgebraicGeometry.depthOneQuotient_unique_of_epi_of_depth, AlgebraicGeometry.isDepthOneQuotient_pullback, AlgebraicGeometry.depthOneQuotient_pullback_unique, AlgebraicGeometry.existsUnique_iso_pullback_pushforward_restrict_flat, AlgebraicGeometry.isCoherent_pushforward_restrict_pullback_of_flat, AlgebraicGeometry.isIso_pullback_map_unit, AlgebraicGeometry.two_le_depth_stalk_pushforward_restrict
statement: formalized
proof: formalized
---

# 51.15 Improving coherent modules

Section 51.15 of the Stacks Project, [Tag 0DX2](https://stacks.math.columbia.edu/tag/0DX2). 5 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DX3, a lemma

[Tag 0DX3](https://stacks.math.columbia.edu/tag/0DX3) in the Stacks Project.

**`AlgebraicGeometry.depthOneQuotient_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/DepthOneQuotient/Basic.lean, line 950](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/DepthOneQuotient/Basic.lean#L950). The attribute's comment: “depth\_one\_quotient”.

> The canonical quotient is coherent, surjective, unchanged away from `T`,
> and of depth at least one along `T`.

```lean
public theorem depthOneQuotient_spec (X : Scheme.{u}) [IsNoetherian X]
    (T : Set X) (hT : StableUnderSpecialization T)
    (F : X.Modules) [F.IsCoherent] :
    IsDepthOneQuotient T (toDepthOneQuotient X T hT F)
```

**`AlgebraicGeometry.depthOneQuotient_unique_of_epi_of_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/DepthOneQuotient/Basic.lean, line 1018](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/DepthOneQuotient/Basic.lean#L1018). The attribute's comment: “depth\_one\_quotient”.

> **Stacks Project, Tag 0DX3**, uniqueness. Let `X` be a Noetherian scheme, `T ⊆ X` stable under
> specialization and `F` a coherent `𝒪_X`-module. If `g : F ⟶ G` is a surjection onto a coherent
> module `G` such that the stalk map `F_x ⟶ G_x` is an isomorphism for `x ∉ T` and
> `depth_{𝒪_{X,x}}(G_x) ≥ 1` for `x ∈ T`, then `G` is identified with the canonical depth-one
> quotient `depthOneQuotient X T hT F` by a unique isomorphism over `F`.

```lean
public theorem depthOneQuotient_unique_of_epi_of_depth (X : Scheme.{u}) [IsNoetherian X]
    (T : Set X) (hT : StableUnderSpecialization T)
    (F : X.Modules) [F.IsCoherent]
    (G : X.Modules) [G.IsCoherent] (g : F ⟶ G) [Epi g]
    (hstalk : ∀ x : X, x ∉ T → IsIso ((TopCat.Presheaf.stalkFunctor Ab.{u} x).map
      g.mapPresheaf))
    (hdepth : ∀ x : X, x ∈ T →
      letI : Module (X.presheaf.stalk x)
          (TopCat.Presheaf.stalk (C := Ab.{u}) G.val.presheaf x) :=
        PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
          (R := X.presheaf) G.val x
      (1 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
        (TopCat.Presheaf.stalk (C := Ab.{u}) G.val.presheaf x)) :
    ∃! e : depthOneQuotient X T hT F ≅ G,
      toDepthOneQuotient X T hT F ≫ e.hom = g
```

**`AlgebraicGeometry.isDepthOneQuotient_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/DepthOneQuotient/FlatPullback.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/DepthOneQuotient/FlatPullback.lean#L186). The attribute's comment: “flat\_pullback”. References: EGA IV (5.9.4), “Noetherian, coherent F”.

> For a flat morphism `f : Y ⟶ X` of Noetherian schemes, the pullback of the canonical
> depth-one quotient of a coherent module along a specialization-closed set `T` is a depth-one
> quotient along `f ⁻¹' T`.

```lean
public theorem isDepthOneQuotient_pullback
    {X Y : Scheme.{u}} [IsNoetherian X] [IsNoetherian Y]
    (f : Y ⟶ X) [Flat f]
    (T : Set X) (hT : StableUnderSpecialization T)
    (F : X.Modules) [F.IsCoherent] :
    IsDepthOneQuotient (f.base ⁻¹' T)
      ((Scheme.Modules.pullback f).map
        (toDepthOneQuotient X T hT F))
```

**`AlgebraicGeometry.depthOneQuotient_pullback_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/DepthOneQuotient/FlatPullback.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/DepthOneQuotient/FlatPullback.lean#L261). The attribute's comment: “flat\_pullback”.

> **Stacks Project, Tag 0DX3**, flat pullback. For a flat morphism `f : Y ⟶ X` of Noetherian
> schemes, `f^*F ⟶ f^*F'` is the depth-one quotient of `f^*F` along `f ⁻¹' T`: the canonical
> depth-one quotient of the coherent module `f^*F` along `f ⁻¹' T` is identified with the pullback
> of the canonical depth-one quotient of `F` along `T` by a unique isomorphism over `f^*F`.

```lean
public theorem depthOneQuotient_pullback_unique
    {X Y : Scheme.{u}} [IsNoetherian X] [IsNoetherian Y]
    (f : Y ⟶ X) [Flat f]
    (T : Set X) (hT : StableUnderSpecialization T)
    (F : X.Modules) [F.IsCoherent] :
    letI : ((Scheme.Modules.pullback f).obj F).IsCoherent := isCoherent_pullback f F
    ∃! e : depthOneQuotient Y (f.base ⁻¹' T) (hT.preimage f.base.hom.continuous)
        ((Scheme.Modules.pullback f).obj F) ≅
        (Scheme.Modules.pullback f).obj (depthOneQuotient X T hT F),
      toDepthOneQuotient Y (f.base ⁻¹' T) (hT.preimage f.base.hom.continuous)
          ((Scheme.Modules.pullback f).obj F) ≫ e.hom =
        (Scheme.Modules.pullback f).map (toDepthOneQuotient X T hT F)
```

## Tag 0DX4, a lemma

[Tag 0DX4](https://stacks.math.columbia.edu/tag/0DX4) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_iso_pullback_pushforward_restrict_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/FlatPullbackDepth.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/FlatPullbackDepth.lean#L172). The attribute's comment: “flat pullback compatibility: the pullback of the canonical map is the canonical map for the inverse image of U”.

> For a flat morphism `f : Y ⟶ X` of Noetherian schemes, `f^*F → f^*j_*(F|_U)` is the
> canonical extension map for the open subscheme `f^{-1}(U) ⊆ Y`: there is a unique isomorphism
> between `f^*j_*(F|_U)` and `j'_*((f^*F)|_{f^{-1}(U)})` compatible with the two canonical maps out
> of `f^*F`.

```lean
public theorem existsUnique_iso_pullback_pushforward_restrict_flat
    {X Y : Scheme.{u}} [IsNoetherian X] [IsNoetherian Y]
    (f : Y ⟶ X) [Flat f] (F : X.Modules) [F.IsCoherent]
    (U : X.Opens)
    [((Scheme.Modules.pushforward U.ι).obj
      ((Scheme.Modules.pullback U.ι).obj F)).IsCoherent] :
    ∃! e : (Scheme.Modules.pullback f).obj
        ((Scheme.Modules.pushforward U.ι).obj
          ((Scheme.Modules.pullback U.ι).obj F)) ≅
        (Scheme.Modules.pushforward (f ⁻¹ᵁ U).ι).obj
          ((Scheme.Modules.pullback (f ⁻¹ᵁ U).ι).obj
            ((Scheme.Modules.pullback f).obj F)),
      (Scheme.Modules.pullback f).map
        ((Scheme.Modules.pullbackPushforwardAdjunction U.ι).unit.app F) ≫ e.hom =
        (Scheme.Modules.pullbackPushforwardAdjunction (f ⁻¹ᵁ U).ι).unit.app
          ((Scheme.Modules.pullback f).obj F)
```

**`AlgebraicGeometry.isCoherent_pushforward_restrict_pullback_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/FlatPullbackDepth.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/FlatPullbackDepth.lean#L197). The attribute's comment: “flat pullback compatibility: the coherence hypothesis of the source holds again for the inverse image of U, so the lemma applies verbatim downstairs”.

> For a flat morphism `f : Y ⟶ X` of Noetherian schemes, the coherence hypothesis of
> [Stacks, Tag 0DX4] holds again downstairs: `j'_*((f^*F)|_{f^{-1}(U)})` is a coherent
> `𝒪_Y`-module. With `f^*F` coherent (`AlgebraicGeometry.isCoherent_pullback`), [Stacks, Tag 0DX4]
> therefore applies to `f : Y ⟶ X`, `f^{-1}(U)` and `f^*F`.

```lean
public theorem isCoherent_pushforward_restrict_pullback_of_flat
    {X Y : Scheme.{u}} [IsNoetherian X] [IsNoetherian Y]
    (f : Y ⟶ X) [Flat f] (F : X.Modules) [F.IsCoherent]
    (U : X.Opens)
    [((Scheme.Modules.pushforward U.ι).obj
      ((Scheme.Modules.pullback U.ι).obj F)).IsCoherent] :
    ((Scheme.Modules.pushforward (f ⁻¹ᵁ U).ι).obj
      ((Scheme.Modules.pullback (f ⁻¹ᵁ U).ι).obj
        ((Scheme.Modules.pullback f).obj F))).IsCoherent
```

**`AlgebraicGeometry.isIso_pullback_map_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/OpenExtension.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/OpenExtension.lean#L130). The attribute's comment: “clause (1) for the canonical map: it restricts to an isomorphism over U”.

> The canonical map `F → j_*(F|_U)` becomes an isomorphism after restriction to the open
> subscheme `U`.
>
> This is the left unitality triangle of the pullback--pushforward adjunction together with
> invertibility of its counit along an open immersion.

```lean
public theorem isIso_pullback_map_unit {X : Scheme.{u}} (F : X.Modules) (U : X.Opens) :
    IsIso ((Scheme.Modules.pullback U.ι).map
      ((Scheme.Modules.pullbackPushforwardAdjunction U.ι).unit.app F))
```

**`AlgebraicGeometry.two_le_depth_stalk_pushforward_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/OpenExtension.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/OpenExtension.lean#L145). The attribute's comment: “clause (2) for the canonical map: the extension has depth at least two outside U”.

> The stalks of the extension `F' = j_*(F|_U)` of a module along an open subscheme have depth
> at least two at every point outside `U`.
>
> The module `F'` is canonically the pushforward of its own restriction to `U`, by
> `AlgebraicGeometry.isIso_unit_app_pushforward`, so the bound is [Stacks, Tag 0EY0] part (3) for
> the open immersion `U.ι`, which is
> `Stacks.AlgebraicGeometry.PushforwardRegularity.two_le_depth_stalk_of_isIso_unit_of_notMem`.
> Only finite type of `F'` is used, so coherence of `F` is not assumed.

```lean
public theorem two_le_depth_stalk_pushforward_restrict
    (X : Scheme.{u}) [IsNoetherian X] (F : X.Modules) (U : X.Opens)
    [((Scheme.Modules.pushforward U.ι).obj
      ((Scheme.Modules.pullback U.ι).obj F)).IsCoherent] :
    ∀ x : X, x ∉ (U : Set X) →
      let F' := (Scheme.Modules.pushforward U.ι).obj ((Scheme.Modules.pullback U.ι).obj F)
      letI : Module (X.presheaf.stalk x)
          (TopCat.Presheaf.stalk (C := Ab.{u}) F'.val.presheaf x) :=
        PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
          F'.val x
      (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
        (TopCat.Presheaf.stalk (C := Ab.{u}) F'.val.presheaf x)
```

**`AlgebraicGeometry.unique_iso_pushforward_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/OpenExtension.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/OpenExtension.lean#L169). The attribute's comment: “uniqueness under the original module”.

> A coherent module carrying a map from `F` which becomes an isomorphism over the open
> subscheme `U` and whose stalks have depth at least two outside `U` is uniquely isomorphic,
> under `F`, to the extension `j_*(F|_U)` of the restriction of `F`.

```lean
public theorem unique_iso_pushforward_restrict
    (X : Scheme.{u}) [IsNoetherian X] (F G : X.Modules)
    [F.IsCoherent] [G.IsCoherent] (U : X.Opens)
    [((Scheme.Modules.pushforward U.ι).obj
      ((Scheme.Modules.pullback U.ι).obj F)).IsCoherent]
    (φ : F ⟶ G)
    (hφ : IsIso ((Scheme.Modules.pullback U.ι).map φ))
    (hdepth : ∀ x : X, x ∉ (U : Set X) →
      let M := TopCat.Presheaf.stalk (C := Ab.{u}) G.val.presheaf x
      letI : Module (X.presheaf.stalk x) M :=
        PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
          G.val x
      (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x)) M) :
    ∃! e : G ≅ (Scheme.Modules.pushforward U.ι).obj
      ((Scheme.Modules.pullback U.ι).obj F),
      φ ≫ e.hom = (Scheme.Modules.pullbackPushforwardAdjunction U.ι).unit.app F
```

**`AlgebraicGeometry.flat_pullback_coherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/OpenExtension.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/OpenExtension.lean#L195). The attribute's comment: “flat pullback coherence”.

> The pullback of the extension `j_*(F|_U)` along a flat morphism is coherent.
>
> Flatness of `f` is not needed: coherence of a pullback needs only a locally Noetherian source,
> by [Stacks, Tag 0EBF].

```lean
public theorem flat_pullback_coherent
    {X Y : Scheme.{u}} [IsNoetherian X] [IsNoetherian Y]
    (f : Y ⟶ X) [Flat f] (F : X.Modules) [F.IsCoherent]
    (U : X.Opens)
    [((Scheme.Modules.pushforward U.ι).obj
      ((Scheme.Modules.pullback U.ι).obj F)).IsCoherent] :
    ((Scheme.Modules.pullback f).obj
      ((Scheme.Modules.pushforward U.ι).obj
        ((Scheme.Modules.pullback U.ι).obj F))).IsCoherent
```

## Tag 0DX5, a lemma

[Tag 0DX5](https://stacks.math.columbia.edu/tag/0DX5) in the Stacks Project.

**`AlgebraicGeometry.correctedImprovement_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/CorrectedImprovement.lean, line 466](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/CorrectedImprovement.lean#L466). The attribute's comment: “corrected form (conditions corrected so that existence holds; the source's existence clause is false, Stacks.ImprovementCounterexample.not\_exists\_isImprovement\_cexSheaf): the pullback of the corrected map along a Cohen-Macaulay morphism with Noetherian source satisfies (1), (2) and the corrected surjectivity-and-depth-one condition along f^\{-1}(Z), and the depth-two condition on the inverse image of the points of Z generalizing no point as in (2)”.

> **The Cohen–Macaulay pullback under the corrected conditions.**  Let `φ : F ⟶ G` satisfy the
> corrected conditions along `Z` and let `f : Y ⟶ X` be a Cohen–Macaulay morphism of Noetherian
> schemes.  Then `f^*φ` has coherent target, is an isomorphism on stalks off `f^{-1}(Z)`, satisfies
> condition (2) at the points of `f^{-1}(Z)` reached from outside `f^{-1}(Z)` for `f^*F` and
> condition (2') at the points generalizing those, intrinsically upstairs; and it has depth at
> least two at the points of `f^{-1}(Z)` lying over a point of `Z` generalizing no reached point.
>
> The last clause is not condition (3) for `f^*F`: that would ask depth two at every point of
> `f^{-1}(Z)` generalizing no point reached upstairs, and it fails already for the open immersion
> `D(w) ⊆ Spec k[u, v, w]` of the counterexample:
> `Stacks.ImprovementCounterexample.correctedImprovement_pullback_not_intrinsic`.
>
> This is `AlgebraicGeometry.isNestedImprovement_pullback` for the nested pair
> `NotGeneralizingReached Z F ⊆ Z`, with the points reached upstairs placed over points of `Z`
> generalizing a reached point by
> `AlgebraicGeometry.notMem_notGeneralizingReached_of_reachedFromOutside_pullback`.

```lean
public theorem correctedImprovement_pullback {X Y : Scheme.{u}} [IsNoetherian X]
    [IsNoetherian Y] {Z : Set X} {F G : X.Modules} (φ : F ⟶ G)
    (hφ : IsCorrectedImprovement Z φ) (f : Y ⟶ X)
    (hfib : ∀ x : X, IsLocallyNoetherian (f.fiber x)) (hcm : f.IsCohenMacaulay hfib) :
    ((Scheme.Modules.pullback f).obj G).IsCoherent ∧
      (∀ y : Y, y ∉ f.base ⁻¹' Z →
        IsIso ((TopCat.Presheaf.stalkFunctor Ab.{u} y).map
          ((Scheme.Modules.pullback f).map φ).mapPresheaf)) ∧
      (∀ y : Y, y ∈ f.base ⁻¹' Z →
        ReachedFromOutside (f.base ⁻¹' Z) ((Scheme.Modules.pullback f).obj F) y →
        Epi ((TopCat.Presheaf.stalkFunctor Ab.{u} y).map
          ((Scheme.Modules.pullback f).map φ).mapPresheaf) ∧
          (letI : Module (Y.presheaf.stalk y)
              (TopCat.Presheaf.stalk (C := Ab.{u})
                ((Scheme.Modules.pullback f).obj G).val.presheaf y) :=
            PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
              (R := Y.presheaf) ((Scheme.Modules.pullback f).obj G).val y
          Module.depth (Y.presheaf.stalk y) (IsLocalRing.maximalIdeal (Y.presheaf.stalk y))
            (TopCat.Presheaf.stalk (C := Ab.{u})
              ((Scheme.Modules.pullback f).obj G).val.presheaf y) = (1 : ℕ∞))) ∧
      (∀ y : Y, y ∈ f.base ⁻¹' Z →
        ¬ ReachedFromOutside (f.base ⁻¹' Z) ((Scheme.Modules.pullback f).obj F) y →
        GeneralizesReached (f.base ⁻¹' Z) ((Scheme.Modules.pullback f).obj F) y →
        Epi ((TopCat.Presheaf.stalkFunctor Ab.{u} y).map
          ((Scheme.Modules.pullback f).map φ).mapPresheaf) ∧
          (letI : Module (Y.presheaf.stalk y)
              (TopCat.Presheaf.stalk (C := Ab.{u})
                ((Scheme.Modules.pullback f).obj G).val.presheaf y) :=
            PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
              (R := Y.presheaf) ((Scheme.Modules.pullback f).obj G).val y
          (1 : ℕ∞) ≤ Module.depth (Y.presheaf.stalk y)
            (IsLocalRing.maximalIdeal (Y.presheaf.stalk y))
            (TopCat.Presheaf.stalk (C := Ab.{u})
              ((Scheme.Modules.pullback f).obj G).val.presheaf y))) ∧
      (∀ y : Y, y ∈ f.base ⁻¹' Z → ¬ GeneralizesReached Z F (f.base y) →
        letI : Module (Y.presheaf.stalk y)
            (TopCat.Presheaf.stalk (C := Ab.{u})
              ((Scheme.Modules.pullback f).obj G).val.presheaf y) :=
          PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
            (R := Y.presheaf) ((Scheme.Modules.pullback f).obj G).val y
        (2 : ℕ∞) ≤ Module.depth (Y.presheaf.stalk y)
          (IsLocalRing.maximalIdeal (Y.presheaf.stalk y))
          (TopCat.Presheaf.stalk (C := Ab.{u})
            ((Scheme.Modules.pullback f).obj G).val.presheaf y))
```

**`AlgebraicGeometry.existsUnique_isCorrectedImprovement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/CorrectedImprovement.lean, line 561](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/CorrectedImprovement.lean#L561). The attribute's comment: “corrected form (conditions corrected so that existence holds): the source's existence clause is false, refuted by Stacks.ImprovementCounterexample.not\_exists\_isImprovement\_cexSheaf; with condition (3) at the points of Z which generalize a point as in (2) without being one replaced by surjectivity on stalks and depth at least one, a map F -> F'' exists and is unique up to a unique isomorphism under F, at exactly the source's hypotheses”.

> **Stacks Project, Tag 0DX5, corrected form: the conditions corrected so that existence
> holds.**  The existence clause of the source is false
> (`Stacks.ImprovementCounterexample.not_exists_isImprovement_cexSheaf`).  Let `X` be a Noetherian,
> universally catenary scheme whose local rings have `(S₁)` formal fibres, `Z ⊆ X` closed and `F`
> coherent.  Then there is a map `F ⟶ G` satisfying the corrected conditions
> `AlgebraicGeometry.IsCorrectedImprovement` along `Z` — the source's (1), (2) and (3), except that
> at the points of `Z` which generalize a point as in (2) without being one, (3) is replaced by
> surjectivity on stalks and depth at least one — and any two such maps are isomorphic by a unique
> isomorphism under `F`.
>
> This is the theorem the source's construction proves once its closed subset is chosen as the
> closure of the bad locus.  Its pullback along a Cohen–Macaulay morphism is
> `AlgebraicGeometry.correctedImprovement_pullback`; the source's own conditions, whose existence is
> characterized by `AlgebraicGeometry.exists_isImprovement_iff_two_le_depth_depthOneQuotient`, are
> the primary corrected form, for the reason given in the module docstring.

```lean
public theorem existsUnique_isCorrectedImprovement (X : Scheme.{u}) [IsNoetherian X]
    (Z : Set X) (hZ : IsClosed Z) (F : X.Modules) [F.IsCoherent]
    (hX : Scheme.IsUniversallyCatenary X)
    (hFibres : ∀ z : X, ∀ q : PrimeSpectrum (X.presheaf.stalk z),
        HasSerreCondition
          (X.completedLocalRing z ⊗[X.presheaf.stalk z] q.asIdeal.ResidueField) 1) :
    ∃ (G : X.Modules) (φ : F ⟶ G), IsCorrectedImprovement Z φ ∧
      ∀ (H : X.Modules) (ψ : F ⟶ H), IsCorrectedImprovement Z ψ →
        ∃! e : G ≅ H, φ ≫ e.hom = ψ
```

**`AlgebraicGeometry.exists_isImprovement_iff_two_le_depth_depthOneQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/CorrectedImprovement.lean, line 601](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/CorrectedImprovement.lean#L601). The attribute's comment: “corrected form of the existence clause, which is false as stated (refuted by Stacks.ImprovementCounterexample.not\_exists\_isImprovement\_cexSheaf): at exactly the source's hypotheses, a map F -> F'' satisfying (1), (2) and (3) exists if and only if the depth-one quotient F' of Tag 0DX3 has depth at least two at every point of Z which generalizes a point as in (2) without being one; uniqueness and the Cohen-Macaulay pullback hold as stated”.

> **Stacks Project, Tag 0DX5, corrected form of the existence clause.**  The existence clause
> of the source is false: `Stacks.ImprovementCounterexample.not_exists_isImprovement_cexSheaf` of
> `ImprovementExistenceCounterexample.lean` refutes it for `X = Spec k[u, v, w]`, `Z = V(u, v)`,
> `F = (u, v)~ ⊕ (k[u, v, w]/(u, w))~`, with every hypothesis of the source witnessed.
>
> Let `X` be a Noetherian, universally catenary scheme whose local rings have `(S₁)` formal fibres,
> `Z ⊆ X` closed and `F` coherent, and let `F'` be the depth-one quotient of `F` along `Z`
> ([Stacks, Tag 0DX3]).  Then a map `F ⟶ F''` of coherent modules satisfying conditions (1), (2)
> and (3) of the source exists **if and only if** `depth(F'_x) ≥ 2` at every point `x ∈ Z` which
> generalizes a point as in (2) without being one.  In the counterexample this fails at `(u, v)`.
>
> The other assertions of the source hold as stated: uniqueness is
> `AlgebraicGeometry.improvement_unique` and the Cohen–Macaulay pullback is
> `AlgebraicGeometry.isImprovement_pullback`, so this is [Stacks, Tag 0DX5] with only its existence
> assertion corrected.  The criterion is equivalent to the disjointness criterion of
> `AlgebraicGeometry.existsUnique_improvement_of_disjoint_closure_lowDepthNotReached`, and is stated
> pointwise.
>
> For the forward direction an improvement satisfies the corrected conditions
> (`AlgebraicGeometry.isCorrectedImprovement_of_isImprovement`), so it is isomorphic to the map of
> `AlgebraicGeometry.exists_isCorrectedImprovement_and_depth_eq`, whose target has the depth of `F'`
> at the points in question, and condition (3) bounds that depth below by two.  Conversely, under
> the criterion that map satisfies condition (3) there as well.

```lean
public theorem exists_isImprovement_iff_two_le_depth_depthOneQuotient (X : Scheme.{u})
    [IsNoetherian X]
    (Z : Set X) (hZ : IsClosed Z) (F : X.Modules) [F.IsCoherent]
    (hX : Scheme.IsUniversallyCatenary X)
    (hFibres : ∀ z : X, ∀ q : PrimeSpectrum (X.presheaf.stalk z),
        HasSerreCondition
          (X.completedLocalRing z ⊗[X.presheaf.stalk z] q.asIdeal.ResidueField) 1) :
    (∃ (G : X.Modules) (φ : F ⟶ G), IsImprovement Z φ) ↔
      ∀ x : X, x ∈ Z → ¬ ReachedFromOutside Z F x → GeneralizesReached Z F x →
        letI : Module (X.presheaf.stalk x)
            (TopCat.Presheaf.stalk (C := Ab.{u})
              (depthOneQuotient X Z hZ.stableUnderSpecialization F).val.presheaf x) :=
          PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
            (R := X.presheaf) (depthOneQuotient X Z hZ.stableUnderSpecialization F).val x
        (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
          (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
          (TopCat.Presheaf.stalk (C := Ab.{u})
            (depthOneQuotient X Z hZ.stableUnderSpecialization F).val.presheaf x)
```

**`AlgebraicGeometry.exists_isImprovement_iff_and_unique_and_isImprovement_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/CorrectedImprovement.lean, line 659](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/CorrectedImprovement.lean#L659). The attribute's comment: “corrected form of the whole lemma, at exactly the source's hypotheses: the existence clause is false as stated (refuted by Stacks.ImprovementCounterexample.not\_exists\_isImprovement\_cexSheaf) and is corrected to a criterion, a map F -> F'' satisfying (1), (2) and (3) exists if and only if the depth-one quotient F' of Tag 0DX3 has depth at least two at every point of Z which generalizes a point as in (2) without being one; uniqueness up to a unique isomorphism under F, and the assertion that the pullback along a Cohen-Macaulay morphism with Noetherian source satisfies (1), (2) and (3) with respect to the inverse image of Z, as printed”.

> **Stacks Project, Tag 0DX5, the whole lemma in corrected form.**  Let `X` be a Noetherian,
> universally catenary scheme whose local rings have `(S₁)` formal fibres, `Z ⊆ X` closed and `F` a
> coherent `𝒪_X`-module, and let `F'` be the depth-one quotient of `F` along `Z`
> ([Stacks, Tag 0DX3]).  For maps `F ⟶ F''` satisfying conditions (1), (2) and (3) of the source
> (`AlgebraicGeometry.IsImprovement`, which includes coherence of `F''`):
>
> * **existence**, corrected: such a map exists if and only if `depth(F'_x) ≥ 2` at every point
>   `x ∈ Z` which generalizes a point as in (2) without being one.  The source asserts existence
>   unconditionally, which is false:
>   `Stacks.ImprovementCounterexample.not_exists_isImprovement_cexSheaf` refutes it at the source's
>   hypotheses, and the criterion fails there at `(u, v)`;
> * **uniqueness**, as printed: any two such maps are isomorphic by a unique isomorphism under `F`;
> * **the pullback**, as printed: for a Cohen–Macaulay morphism `f : Y ⟶ X` with `Y` Noetherian,
>   `f^*F ⟶ f^*F''` satisfies (1), (2) and (3) with respect to `f^{-1}(Z) ⊆ Y`.
>
> The three parts are `AlgebraicGeometry.exists_isImprovement_iff_two_le_depth_depthOneQuotient`,
> `AlgebraicGeometry.improvement_unique` and `AlgebraicGeometry.isImprovement_pullback`.  The
> correction is the one recorded for 0DX5 in `errata.md`.

```lean
public theorem exists_isImprovement_iff_and_unique_and_isImprovement_pullback (X : Scheme.{u})
    [IsNoetherian X] (Z : Set X) (hZ : IsClosed Z) (F : X.Modules) [F.IsCoherent]
    (hX : Scheme.IsUniversallyCatenary X)
    (hFibres : ∀ z : X, ∀ q : PrimeSpectrum (X.presheaf.stalk z),
        HasSerreCondition
          (X.completedLocalRing z ⊗[X.presheaf.stalk z] q.asIdeal.ResidueField) 1) :
    ((∃ (G : X.Modules) (φ : F ⟶ G), IsImprovement Z φ) ↔
      ∀ x : X, x ∈ Z → ¬ ReachedFromOutside Z F x → GeneralizesReached Z F x →
        letI : Module (X.presheaf.stalk x)
            (TopCat.Presheaf.stalk (C := Ab.{u})
              (depthOneQuotient X Z hZ.stableUnderSpecialization F).val.presheaf x) :=
          PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
            (R := X.presheaf) (depthOneQuotient X Z hZ.stableUnderSpecialization F).val x
        (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
          (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
          (TopCat.Presheaf.stalk (C := Ab.{u})
            (depthOneQuotient X Z hZ.stableUnderSpecialization F).val.presheaf x)) ∧
    (∀ (G H : X.Modules) (φ : F ⟶ G) (ψ : F ⟶ H), IsImprovement Z φ → IsImprovement Z ψ →
      ∃! e : G ≅ H, φ ≫ e.hom = ψ) ∧
    (∀ (G : X.Modules) (φ : F ⟶ G), IsImprovement Z φ →
      ∀ (Y : Scheme.{u}) [IsNoetherian Y] (f : Y ⟶ X)
        (hfib : ∀ x : X, IsLocallyNoetherian (f.fiber x)), f.IsCohenMacaulay hfib →
        IsImprovement (f.base ⁻¹' Z) ((Scheme.Modules.pullback f).map φ))
```

**`AlgebraicGeometry.isCoherent_pullback_of_isImprovement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/Improvement.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/Improvement.lean#L167). The attribute's comment: “coherence of the target of the pullback, in the assertion about the pullback along a Cohen-Macaulay morphism”.

> The target of the pullback of an improvement along a morphism with locally Noetherian
> source is again coherent.

```lean
public theorem isCoherent_pullback_of_isImprovement {X Y : Scheme.{u}} [IsLocallyNoetherian Y]
    (f : Y ⟶ X) {Z : Set X} {F G : X.Modules} (φ : F ⟶ G) (h : IsImprovement Z φ) :
    ((Scheme.Modules.pullback f).obj G).IsCoherent
```

**`AlgebraicGeometry.isIso_stalk_pullback_map_of_isImprovement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/Improvement.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/Improvement.lean#L177). The attribute's comment: “the isomorphism away from the inverse image of the closed subscheme, in the assertion about the pullback along a Cohen-Macaulay morphism”.

> The pullback of an improvement along any morphism of schemes is an isomorphism on stalks at
> every point outside the inverse image of the closed subset.

```lean
public theorem isIso_stalk_pullback_map_of_isImprovement {X Y : Scheme.{u}} (f : Y ⟶ X)
    {Z : Set X} {F G : X.Modules} (φ : F ⟶ G) (h : IsImprovement Z φ)
    (y : Y) (hy : y ∉ f.base ⁻¹' Z) :
    IsIso ((TopCat.Presheaf.stalkFunctor Ab.{u} y).map
      ((Scheme.Modules.pullback f).map φ).mapPresheaf)
```

**`AlgebraicGeometry.two_le_depth_stalk_pullback_of_notReachedFromOutside`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ImprovementPullback.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ImprovementPullback.lean#L269). The attribute's comment: “condition (3) for the pullback along a Cohen-Macaulay morphism: depth at least two at a point of the inverse image of Z which is not itself reached from outside that inverse image”.

> **The depth bound at a point not reached upstairs.** Let `F → F''` be an improvement of a
> coherent `𝒪_X`-module `F` along `Z` and let `f : Y ⟶ X` be a Cohen–Macaulay morphism of Noetherian
> schemes. At a point `y` of `f^{-1}(Z)` which is not reached from outside `f^{-1}(Z)` for `f^*F`,
> the stalk of `f^*F''` has depth at least two.
>
> By `AlgebraicGeometry.depth_stalk_pullback_eq` the depth upstairs is the depth of the stalk of
> `F''` at `f y` plus the depth of the fibre of the local ring. If `f y` is not reached from outside
> `Z` the first summand is already at least two. If it is reached, the first summand is exactly one,
> so it suffices that the fibre have positive depth; a fibre of depth zero would carry the point
> reaching `f y` up to a point reaching `y`, which is excluded by hypothesis.

```lean
public theorem two_le_depth_stalk_pullback_of_notReachedFromOutside {X Y : Scheme.{u}}
    [IsNoetherian X] [IsNoetherian Y] {Z : Set X} {F G : X.Modules} [F.IsCoherent] (φ : F ⟶ G)
    (hφ : IsImprovement Z φ) (f : Y ⟶ X)
    (hfib : ∀ x : X, IsLocallyNoetherian (f.fiber x)) (hcm : f.IsCohenMacaulay hfib)
    (y : Y) (hy : y ∈ f.base ⁻¹' Z)
    (hnr : ¬ ReachedFromOutside (f.base ⁻¹' Z) ((Scheme.Modules.pullback f).obj F) y) :
    letI : Module (Y.presheaf.stalk y)
        (TopCat.Presheaf.stalk (C := Ab.{u})
          ((Scheme.Modules.pullback f).obj G).val.presheaf y) :=
      PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
        (R := Y.presheaf) ((Scheme.Modules.pullback f).obj G).val y
    (2 : ℕ∞) ≤ Module.depth (Y.presheaf.stalk y)
      (IsLocalRing.maximalIdeal (Y.presheaf.stalk y))
      (TopCat.Presheaf.stalk (C := Ab.{u})
        ((Scheme.Modules.pullback f).obj G).val.presheaf y)
```

**`AlgebraicGeometry.isImprovement_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ImprovementPullback.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ImprovementPullback.lean#L320). The attribute's comment: “the final assertion: the pullback of the map along a Cohen-Macaulay morphism with Noetherian source satisfies conditions (1), (2) and (3) with respect to the inverse image of the closed subscheme”.

> **Stacks Project, Tag 0DX5, the assertion about the pullback.** The pullback of an improvement
> of a coherent module along a Cohen–Macaulay morphism of Noetherian schemes is an improvement along
> the inverse image of the closed subset: it satisfies conditions (1), (2) and (3) with respect to
> `f^{-1}(Z) ⊆ Y`.
>
> An improvement along `Z` is an improvement along the nested pair `Z ∖ {reached points} ⊆ Z`
> (`AlgebraicGeometry.isNestedImprovement_of_isImprovement`), whose pullback is an improvement along
> the inverse images of that pair (`AlgebraicGeometry.isNestedImprovement_pullback`). Those inverse
> images are the pair belonging to `f^*F` and `f^{-1}(Z)`, because the points of `f^{-1}(Z)` reached
> from outside `f^{-1}(Z)` for `f^*F` are exactly the points lying over points of `Z` reached from
> outside `Z` for `F`; that is the content of
> `AlgebraicGeometry.reachedFromOutside_base_of_reachedFromOutside_pullback` and
> `AlgebraicGeometry.two_le_depth_stalk_pullback_of_notReachedFromOutside`.

```lean
public theorem isImprovement_pullback {X Y : Scheme.{u}} [IsNoetherian X] [IsNoetherian Y]
    {Z : Set X} {F G : X.Modules} [F.IsCoherent] (φ : F ⟶ G) (hφ : IsImprovement Z φ) (f : Y ⟶ X)
    (hfib : ∀ x : X, IsLocallyNoetherian (f.fiber x)) (hcm : f.IsCohenMacaulay hfib) :
    IsImprovement (f.base ⁻¹' Z) ((Scheme.Modules.pullback f).map φ)
```

**`AlgebraicGeometry.epi_stalk_pullback_of_isImprovement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ImprovementPullback.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ImprovementPullback.lean#L338). The attribute's comment: “the surjectivity in condition (2) for the pullback along a Cohen-Macaulay morphism”.

> The pullback of an improvement along a Cohen–Macaulay morphism of Noetherian schemes is
> surjective on the stalk at every point of the inverse image of the closed subset which is reached
> from outside that inverse image: the surjectivity half of condition (2) upstairs.

```lean
public theorem epi_stalk_pullback_of_isImprovement {X Y : Scheme.{u}} [IsNoetherian X]
    [IsNoetherian Y] {Z : Set X} {F G : X.Modules} [F.IsCoherent] (φ : F ⟶ G)
    (hφ : IsImprovement Z φ) (f : Y ⟶ X)
    (hfib : ∀ x : X, IsLocallyNoetherian (f.fiber x)) (hcm : f.IsCohenMacaulay hfib)
    (y : Y) (hy : y ∈ f.base ⁻¹' Z)
    (hr : ReachedFromOutside (f.base ⁻¹' Z) ((Scheme.Modules.pullback f).obj F) y) :
    Epi ((TopCat.Presheaf.stalkFunctor Ab.{u} y).map
      ((Scheme.Modules.pullback f).map φ).mapPresheaf)
```

**`AlgebraicGeometry.depth_stalk_pullback_eq_one_of_isImprovement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ImprovementPullback.lean, line 353](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ImprovementPullback.lean#L353). The attribute's comment: “the depth equality in condition (2) for the pullback along a Cohen-Macaulay morphism: the depth is exactly one, not merely at least one”.

> The target of the pullback of an improvement along a Cohen–Macaulay morphism of Noetherian
> schemes has stalk of depth exactly one at every point of the inverse image of the closed subset
> which is reached from outside that inverse image: the depth half of condition (2) upstairs.

```lean
public theorem depth_stalk_pullback_eq_one_of_isImprovement {X Y : Scheme.{u}} [IsNoetherian X]
    [IsNoetherian Y] {Z : Set X} {F G : X.Modules} [F.IsCoherent] (φ : F ⟶ G)
    (hφ : IsImprovement Z φ) (f : Y ⟶ X)
    (hfib : ∀ x : X, IsLocallyNoetherian (f.fiber x)) (hcm : f.IsCohenMacaulay hfib)
    (y : Y) (hy : y ∈ f.base ⁻¹' Z)
    (hr : ReachedFromOutside (f.base ⁻¹' Z) ((Scheme.Modules.pullback f).obj F) y) :
    letI : Module (Y.presheaf.stalk y)
        (TopCat.Presheaf.stalk (C := Ab.{u})
          ((Scheme.Modules.pullback f).obj G).val.presheaf y) :=
      PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
        (R := Y.presheaf) ((Scheme.Modules.pullback f).obj G).val y
    Module.depth (Y.presheaf.stalk y) (IsLocalRing.maximalIdeal (Y.presheaf.stalk y))
      (TopCat.Presheaf.stalk (C := Ab.{u})
        ((Scheme.Modules.pullback f).obj G).val.presheaf y) = (1 : ℕ∞)
```

**`AlgebraicGeometry.improvement_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ImprovementUniqueness.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ImprovementUniqueness.lean#L171). The attribute's comment: “uniqueness of the map F → F'': two maps satisfying conditions (1), (2) and (3) are isomorphic by a unique isomorphism under F”.

> **Stacks Project, Tag 0DX5, uniqueness.** Two improvements of a coherent module along the same
> closed subset are isomorphic by a unique isomorphism compatible with the two maps.
>
> Each is an improvement along the nested pair `NotReachedFromOutside Z F ⊆ Z`, a subset determined
> by `Z` and `F` alone, so the comparison is the one of [Stacks, Tag 0EI4]. Neither the universal
> catenarity of `X` nor the `(S₁)` condition on the formal fibres of its local rings is used: those
> hypotheses of the source enter only its existence proof.

```lean
public theorem improvement_unique (X : Scheme.{u}) [IsNoetherian X] (Z : Set X) (hZ : IsClosed Z)
    (F G H : X.Modules) [F.IsCoherent] (φ : F ⟶ G) (ψ : F ⟶ H)
    (hφ : IsImprovement Z φ) (hψ : IsImprovement Z ψ) :
    ∃! e : G ≅ H, φ ≫ e.hom = ψ
```

## Tag 0EI3, a lemma

[Tag 0EI3](https://stacks.math.columbia.edu/tag/0EI3) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_isDepthTwoExtension_and_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/DepthTwoExtensionUniquePullback.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/DepthTwoExtensionUniquePullback.lean#L44). The attribute's comment: “existence, uniqueness and the Cohen-Macaulay pullback clause, at the source's hypotheses”.

> **Stacks Project, Tag 0EI3.**  Let `X` be a Noetherian scheme which locally has a dualizing
> complex, let `T ⊆ X` be stable under specialization and let `F` be a coherent `𝒪_X`-module with
> `depth(F_x) ≥ 1` at every immediate specialization `x ⤳ x'` with `x' ∈ T` and `x ∉ T`.  Then there
> is a map `φ : F ⟶ F''` to a coherent module which is an isomorphism on the stalks off `T` and
> whose stalks on `T` have depth at least two; it is unique, in that any other such map is carried
> to it by a unique isomorphism under `F`; and for every Cohen–Macaulay morphism `f : Y ⟶ X` with
> `Y` Noetherian, `f^*φ` has the same properties along `f⁻¹(T)` (and so is the unique such map).

```lean
public theorem existsUnique_isDepthTwoExtension_and_pullback
    (X : Scheme.{u}) [IsNoetherian X] (hdual : HasDualizingComplexOnAffineCover X)
    (T : Set X) (hT : StableUnderSpecialization T) (F : X.Modules) [F.IsCoherent]
    (himm : ∀ x x' : X, IsImmediateSpecialization x x' → x' ∈ T → x ∉ T →
      (1 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x)) (F.presheaf.stalk x)) :
    ∃ (G : X.Modules) (φ : F ⟶ G), IsDepthTwoExtension T φ ∧
      (∀ (H : X.Modules) (ψ : F ⟶ H), IsDepthTwoExtension T ψ →
        ∃! e : G ≅ H, φ ≫ e.hom = ψ) ∧
      ∀ (Y : Scheme.{u}) [IsNoetherian Y] (f : Y ⟶ X),
        f.IsCohenMacaulay (fun x ↦ isLocallyNoetherian_fiber f x) →
        IsDepthTwoExtension (f ⁻¹' T) ((Scheme.Modules.pullback f).map φ) ∧
          ∀ (H : Y.Modules) (ψ : (Scheme.Modules.pullback f).obj F ⟶ H),
            IsDepthTwoExtension (f ⁻¹' T) ψ →
              ∃! e : (Scheme.Modules.pullback f).obj G ≅ H,
                (Scheme.Modules.pullback f).map φ ≫ e.hom = ψ
```

## Tag 0EI4, a lemma

[Tag 0EI4](https://stacks.math.columbia.edu/tag/0EI4) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_isNestedImprovement_and_pullback_of_hasDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/NestedImprovementCohenMacaulay.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/NestedImprovementCohenMacaulay.lean#L55). The attribute's comment: “existence and uniqueness, up to a unique isomorphism under F, of the map F to F'' with conditions (1), (2), (3), together with the assertion that its pullback along a Cohen-Macaulay morphism with Noetherian source satisfies (1), (2), (3) with respect to the inverse images of T' and T; at the hypotheses of the source”.

> **Stacks Project, Tag 0EI4.** Let `X` be a Noetherian scheme which locally has a dualizing
> complex, let `T' ⊆ T ⊆ X` be stable under specialization and such that every immediate
> specialization `x ⤳ x'` with `x' ∈ T'` has `x ∈ T`, and let `F` be a coherent `𝒪_X`-module.
> Then there is a map `φ : F ⟶ F''` to a coherent module such that
>
> 1. `F_x ⟶ F''_x` is an isomorphism for `x ∉ T`,
> 2. `F_x ⟶ F''_x` is surjective and `depth F''_x ≥ 1` for `x ∈ T`, `x ∉ T'`,
> 3. `depth F''_x ≥ 2` for `x ∈ T'`,
>
> (this is `AlgebraicGeometry.IsNestedImprovement T T' φ`); it is unique, in that any other such
> map `F ⟶ H` is carried to it by a unique isomorphism `F'' ≅ H` under `F`; and for every
> Cohen-Macaulay morphism `f : Y ⟶ X` with `Y` Noetherian, the pullback `f^* F ⟶ f^* F''` has the
> same properties with respect to `f⁻¹ T' ⊆ f⁻¹ T`.
>
> The Cohen-Macaulay hypothesis is `AlgebraicGeometry.Scheme.Hom.IsCohenMacaulay` of
> [Stacks, Tag 045R], whose definition presupposes, as the source's does, that the fibres of `f`
> are locally Noetherian; that is the argument `hfib`.

```lean
public theorem existsUnique_isNestedImprovement_and_pullback_of_hasDualizingComplex
    (X : Scheme.{u}) [IsNoetherian X] (hdual : HasDualizingComplexOnAffineCover X)
    (T T' : Set X) (hTT' : T' ⊆ T)
    (hT : StableUnderSpecialization T) (hT' : StableUnderSpecialization T')
    (himm : ∀ x x' : X, IsImmediateSpecialization x x' → x' ∈ T' → x ∈ T)
    (F : X.Modules) [F.IsCoherent] :
    ∃ (G : X.Modules) (φ : F ⟶ G), IsNestedImprovement T T' φ ∧
      (∀ (H : X.Modules) (ψ : F ⟶ H), IsNestedImprovement T T' ψ →
        ∃! e : G ≅ H, φ ≫ e.hom = ψ) ∧
      ∀ (Y : Scheme.{u}) [IsNoetherian Y] (f : Y ⟶ X)
        (hfib : ∀ x : X, IsLocallyNoetherian (f.fiber x)), f.IsCohenMacaulay hfib →
        IsNestedImprovement (f.base ⁻¹' T) (f.base ⁻¹' T')
          ((Scheme.Modules.pullback f).map φ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.15, Tag 0DX2](https://stacks.math.columbia.edu/tag/0DX2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
