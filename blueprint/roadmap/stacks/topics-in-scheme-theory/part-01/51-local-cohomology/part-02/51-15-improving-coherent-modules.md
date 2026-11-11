---
declaration: section
origin: cited
lean: AlgebraicGeometry.depthOneQuotient_spec, AlgebraicGeometry.depthOneQuotient_unique, AlgebraicGeometry.isDepthOneQuotient_pullback, AlgebraicGeometry.existsUnique_iso_pullback_pushforward_restrict_flat, AlgebraicGeometry.isCoherent_pushforward_restrict_pullback_of_flat, AlgebraicGeometry.isIso_pullback_map_unit, AlgebraicGeometry.two_le_depth_stalk_pushforward_restrict, AlgebraicGeometry.unique_iso_pushforward_restrict
statement: formalized
proof: formalized
---

# 51.15 Improving coherent modules

Section 51.15 of the Stacks Project, [Tag 0DX2](https://stacks.math.columbia.edu/tag/0DX2). 5 tags here are carried by 40 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DX3, a lemma

[Tag 0DX3](https://stacks.math.columbia.edu/tag/0DX3) in the Stacks Project.

**`AlgebraicGeometry.depthOneQuotient_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/DepthOneQuotient/Basic.lean, line 948](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/DepthOneQuotient/Basic.lean#L948). The attribute's comment: “depth\_one\_quotient”.

> The canonical quotient is coherent, surjective, unchanged away from `T`,
> and of depth at least one along `T`.

```lean
public theorem depthOneQuotient_spec (X : Scheme.{u}) [IsNoetherian X]
    (T : Set X) (hT : StableUnderSpecialization T)
    (F : X.Modules) [F.IsCoherent] :
    IsDepthOneQuotient T (toDepthOneQuotient X T hT F)
```

**`AlgebraicGeometry.depthOneQuotient_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/DepthOneQuotient/Basic.lean, line 978](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/DepthOneQuotient/Basic.lean#L978). The attribute's comment: “depth\_one\_quotient”.

> Every other quotient satisfying the defining properties is uniquely
> isomorphic to the canonical one over its source.

```lean
public theorem depthOneQuotient_unique (X : Scheme.{u}) [IsNoetherian X]
    (T : Set X) (hT : StableUnderSpecialization T)
    (F : X.Modules) [F.IsCoherent]
    (G : X.Modules) (g : F ⟶ G) (hg : IsDepthOneQuotient T g) :
    ∃! e : depthOneQuotient X T hT F ≅ G,
      toDepthOneQuotient X T hT F ≫ e.hom = g
```

**`AlgebraicGeometry.isDepthOneQuotient_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/DepthOneQuotient/FlatPullback.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/DepthOneQuotient/FlatPullback.lean#L186). The attribute's comment: “flat\_pullback”. References: EGA IV (5.9.4), “Noetherian, coherent F”.

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

## Tag 0DX4, a lemma

[Tag 0DX4](https://stacks.math.columbia.edu/tag/0DX4) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_iso_pullback_pushforward_restrict_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/FlatPullbackDepth.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/FlatPullbackDepth.lean#L172). The attribute's comment: “flat pullback compatibility: the pullback of the canonical map is the canonical map for the inverse image of U”.

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

**`AlgebraicGeometry.isCoherent_pushforward_restrict_pullback_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/FlatPullbackDepth.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/FlatPullbackDepth.lean#L197). The attribute's comment: “flat pullback compatibility: the coherence hypothesis of the source holds again for the inverse image of U, so the lemma applies verbatim downstairs”.

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

**`AlgebraicGeometry.isIso_pullback_map_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/OpenExtension.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/OpenExtension.lean#L130). The attribute's comment: “clause (1) for the canonical map: it restricts to an isomorphism over U”.

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

**`AlgebraicGeometry.two_le_depth_stalk_pushforward_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/OpenExtension.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/OpenExtension.lean#L145). The attribute's comment: “clause (2) for the canonical map: the extension has depth at least two outside U”.

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

**`AlgebraicGeometry.unique_iso_pushforward_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/OpenExtension.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/OpenExtension.lean#L169). The attribute's comment: “uniqueness under the original module”.

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

**`AlgebraicGeometry.flat_pullback_coherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/OpenExtension.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/OpenExtension.lean#L195). The attribute's comment: “flat pullback coherence”.

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

**`AlgebraicGeometry.correctedImprovement_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/CorrectedImprovement.lean, line 462](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/CorrectedImprovement.lean#L462). The attribute's comment: “corrected form (conditions corrected so that existence holds; the source's existence clause is false, Stacks.ImprovementCounterexample.not\_exists\_isImprovement\_cexSheaf): the pullback of the corrected map along a Cohen-Macaulay morphism with Noetherian source satisfies (1), (2) and the corrected surjectivity-and-depth-one condition along f^\{-1}(Z), and the depth-two condition on the inverse image of the points of Z generalizing no point as in (2)”.

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

**`AlgebraicGeometry.existsUnique_isCorrectedImprovement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/CorrectedImprovement.lean, line 557](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/CorrectedImprovement.lean#L557). The attribute's comment: “corrected form (conditions corrected so that existence holds): the source's existence clause is false, refuted by Stacks.ImprovementCounterexample.not\_exists\_isImprovement\_cexSheaf; with condition (3) at the points of Z which generalize a point as in (2) without being one replaced by surjectivity on stalks and depth at least one, a map F -> F'' exists and is unique up to a unique isomorphism under F, at exactly the source's hypotheses”.

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

**`AlgebraicGeometry.exists_isImprovement_iff_two_le_depth_depthOneQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/CorrectedImprovement.lean, line 597](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/CorrectedImprovement.lean#L597). The attribute's comment: “corrected form of the existence clause, which is false as stated (refuted by Stacks.ImprovementCounterexample.not\_exists\_isImprovement\_cexSheaf): at exactly the source's hypotheses, a map F -> F'' satisfying (1), (2) and (3) exists if and only if the depth-one quotient F' of Tag 0DX3 has depth at least two at every point of Z which generalizes a point as in (2) without being one; uniqueness and the Cohen-Macaulay pullback hold as stated”.

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

**`AlgebraicGeometry.isCoherent_pullback_of_isImprovement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/Improvement.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/Improvement.lean#L167). The attribute's comment: “coherence of the target of the pullback, in the assertion about the pullback along a Cohen-Macaulay morphism”.

> The target of the pullback of an improvement along a morphism with locally Noetherian
> source is again coherent.

```lean
public theorem isCoherent_pullback_of_isImprovement {X Y : Scheme.{u}} [IsLocallyNoetherian Y]
    (f : Y ⟶ X) {Z : Set X} {F G : X.Modules} (φ : F ⟶ G) (h : IsImprovement Z φ) :
    ((Scheme.Modules.pullback f).obj G).IsCoherent
```

**`AlgebraicGeometry.isIso_stalk_pullback_map_of_isImprovement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/Improvement.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/Improvement.lean#L177). The attribute's comment: “the isomorphism away from the inverse image of the closed subscheme, in the assertion about the pullback along a Cohen-Macaulay morphism”.

> The pullback of an improvement along any morphism of schemes is an isomorphism on stalks at
> every point outside the inverse image of the closed subset.

```lean
public theorem isIso_stalk_pullback_map_of_isImprovement {X Y : Scheme.{u}} (f : Y ⟶ X)
    {Z : Set X} {F G : X.Modules} (φ : F ⟶ G) (h : IsImprovement Z φ)
    (y : Y) (hy : y ∉ f.base ⁻¹' Z) :
    IsIso ((TopCat.Presheaf.stalkFunctor Ab.{u} y).map
      ((Scheme.Modules.pullback f).map φ).mapPresheaf)
```

**`AlgebraicGeometry.two_le_depth_stalk_pullback_of_notReachedFromOutside`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ImprovementPullback.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ImprovementPullback.lean#L269). The attribute's comment: “condition (3) for the pullback along a Cohen-Macaulay morphism: depth at least two at a point of the inverse image of Z which is not itself reached from outside that inverse image”.

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

**`AlgebraicGeometry.isImprovement_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ImprovementPullback.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ImprovementPullback.lean#L320). The attribute's comment: “the final assertion: the pullback of the map along a Cohen-Macaulay morphism with Noetherian source satisfies conditions (1), (2) and (3) with respect to the inverse image of the closed subscheme”.

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

**`AlgebraicGeometry.epi_stalk_pullback_of_isImprovement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ImprovementPullback.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ImprovementPullback.lean#L338). The attribute's comment: “the surjectivity in condition (2) for the pullback along a Cohen-Macaulay morphism”.

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

**`AlgebraicGeometry.depth_stalk_pullback_eq_one_of_isImprovement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ImprovementPullback.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ImprovementPullback.lean#L353). The attribute's comment: “the depth equality in condition (2) for the pullback along a Cohen-Macaulay morphism: the depth is exactly one, not merely at least one”.

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

**`AlgebraicGeometry.improvement_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ImprovementUniqueness.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ImprovementUniqueness.lean#L171). The attribute's comment: “uniqueness of the map F → F'': two maps satisfying conditions (1), (2) and (3) are isomorphic by a unique isomorphism under F”.

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

**`AlgebraicGeometry.exists_isDepthTwoExtension_of_isCoherent_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ClosedStabilizedExtension.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ClosedStabilizedExtension.lean#L131). The attribute's comment: “existence for a closed subset, conditional only on coherence of the single pushforward of the restriction of the depth-one quotient to the complement; the hypothesis hext of exists\_isDepthTwoExtension\_of\_isStabilizedOpenExtension, namely a coherent stabilized open extension, is discharged here for a closed subset”.

> **Stacks Project, Tag 0EI3, existence for a closed subset.** A coherent module `F` on a
> Noetherian scheme admits a map to a coherent module which is an isomorphism on the stalks away
> from a closed subset `T` and whose stalks on `T` have depth at least two, as soon as the single
> pushforward `j_{V,*}(F'|_V)` is coherent — where `V` is the complement of `T` and `F'` is the
> depth-one quotient of `F` along `T`.
>
> Together with `AlgebraicGeometry.isStabilizedOpenExtension_unit` this replaces the hypothesis
> `hext` of `AlgebraicGeometry.exists_isDepthTwoExtension_of_isStabilizedOpenExtension`, which asks
> for a coherent stabilized open extension, by coherence of one explicit module: for a closed `T`
> no colimit of pushforwards over the opens whose complement lies in `T` is needed, because the
> complement of `T` is itself such an open and is the smallest one.
>
> The remaining hypothesis is not removable; it is where the two hypotheses of [Stacks, Tag 0EI3]
> absent from `AlgebraicGeometry.exists_isDepthTwoExtension` — a dualizing complex and a depth
> bound across the boundary of `T` — must re-enter.  See the implementation notes of this
> module.

```lean
public theorem exists_isDepthTwoExtension_of_isCoherent_pushforward
    (X : Scheme.{u}) [IsNoetherian X] (T : Set X) (hT : IsClosed T) (V : X.Opens)
    (hV : (V : Set X) = Tᶜ) (F : X.Modules) [F.IsCoherent]
    (hcoh : ((Scheme.Modules.pushforward V.ι).obj ((Scheme.Modules.pullback V.ι).obj
      (depthOneQuotient X T hT.stableUnderSpecialization F))).IsCoherent) :
    ∃ (G : X.Modules) (φ : F ⟶ G), IsDepthTwoExtension T φ
```

**`AlgebraicGeometry.exists_isDepthTwoExtension_of_locallyHasDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ClosedSubsetExistence.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ClosedSubsetExistence.lean#L405). The attribute's comment: “existence along a closed subset, with no hypothesis about extensions or colimits, and at the source's hypotheses: the dualizing hypothesis and the depth hypothesis on immediate specializations, nothing else, the coherence of the single pushforward coming from the source's Faltings criterion Tag 0EFD”.

> **Stacks Project, Tag 0EI3, existence along a closed subset.** Let `X` be a Noetherian
> scheme which locally has a dualizing complex, let `V` be an open of `X` with complement `T` —
> so `T` is closed — and let `F` be a coherent `𝒪_X`-module such that `depth(F_x) ≥ 1` whenever
> some point of `T` is an immediate specialization of `x ∉ T`.  Then `F` admits a depth-two
> extension along `T`.
>
> No hypothesis about extensions or colimits is left: the module is the single pushforward
> `j_{V,*}(F'|_V)` of the depth-one quotient, which is a stabilized open extension by
> `AlgebraicGeometry.isStabilizedOpenExtension_unit` and coherent by
> `isCoherent_pushforward_restrict_depthOneQuotient`.  The two
> hypotheses are the source's, and both are necessary.  See the module documentation.

```lean
public theorem exists_isDepthTwoExtension_of_locallyHasDualizingComplex
    (X : Scheme.{u}) [IsNoetherian X] (T : Set X) (V : X.Opens) (hV : (V : Set X) = Tᶜ)
    (F : X.Modules) [F.IsCoherent]
    (hdual : LocallyHasDualizingComplex X)
    (hdepth : ∀ x z : X, x ∉ T → z ∈ T → TopologicalSpace.IsImmediateSpecialization x z →
      (1 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
        (TopCat.Presheaf.stalk (C := Ab.{u}) F.val.presheaf x)) :
    ∃ (G : X.Modules) (φ : F ⟶ G), IsDepthTwoExtension T φ
```

**`AlgebraicGeometry.exists_isDepthTwoExtension_of_stableUnderSpecialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/DepthLocusGlue.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/DepthLocusGlue.lean#L223). The attribute's comment: “existence along a specialization-stable subset, at exactly the source's two hypotheses — the dualizing hypothesis and the depth hypothesis on immediate specializations — with no hypothesis about extensions, colimits, a closed subset of T, or finiteness of an exceptional locus”.

> Let `X` be a Noetherian scheme which locally has a dualizing complex, let `T ⊆ X` be stable
> under specialization and let `F` be a coherent `𝒪_X`-module such that `depth(F_x) ≥ 1` whenever
> some point of `T` is an immediate specialization of `x ∉ T`.  Then `F` admits a depth-two
> extension along `T`.

```lean
public theorem exists_isDepthTwoExtension_of_stableUnderSpecialization
    (X : Scheme.{u}) [IsNoetherian X] (T : Set X) (hT : StableUnderSpecialization T)
    (F : X.Modules) [F.IsCoherent] (hdual : LocallyHasDualizingComplex X)
    (hdepth : ∀ x z : X, x ∉ T → z ∈ T → TopologicalSpace.IsImmediateSpecialization x z →
      (1 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
        (TopCat.Presheaf.stalk (C := Ab.{u}) F.val.presheaf x)) :
    ∃ (G : X.Modules) (φ : F ⟶ G), IsDepthTwoExtension T φ
```

**`AlgebraicGeometry.depthTwoExtension_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/DepthTwoExtension.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/DepthTwoExtension.lean#L464). The attribute's comment: “uniqueness, unconditionally: the subset is arbitrary and no dualizing complex is needed”.

> Two depth-two extensions of a module along a subset are isomorphic by a unique isomorphism
> compatible with the two maps.

```lean
public theorem depthTwoExtension_unique
    (X : Scheme.{u}) [IsNoetherian X]
    (T : Set X)
    (F G H : X.Modules) (φ : F ⟶ G) (ψ : F ⟶ H)
    (hφ : IsDepthTwoExtension T φ) (hψ : IsDepthTwoExtension T ψ) :
    ∃! e : G ≅ H, φ ≫ e.hom = ψ
```

**`AlgebraicGeometry.exists_isDepthTwoExtension_of_hasDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/DepthTwoExtensionConstruction.lean, line 480](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/DepthTwoExtensionConstruction.lean#L480). The attribute's comment: “existence, at the source's hypotheses: X Noetherian with a dualizing complex on an affine open cover, T stable under specialization, F coherent, and depth at least one at the immediate specializations into T from outside T; the witness is the single direct image j\_*(F|\_\{X ∖ Z}) across the closure Z of the low-depth locus, not the source's colimit of pushforwards, and its coherence is proved here from Faltings through Tag 0BJY”.

> **Existence of the depth-two extension.**  Let `X` be a Noetherian scheme which locally has a
> dualizing complex, let `T ⊆ X` be stable under specialization and let `F` be coherent.  Assume
> `depth(F_x) ≥ 1` at every immediate specialization `x ⤳ x'` with `x' ∈ T` and `x ∉ T`.  Then `F`
> admits a map to a coherent module which is an isomorphism on the stalks off `T` and whose stalks
> on `T` have depth at least two.

```lean
public theorem exists_isDepthTwoExtension_of_hasDualizingComplex
    (X : Scheme.{u}) [IsNoetherian X] (hdual : HasDualizingComplexOnAffineCover X)
    (T : Set X) (hT : StableUnderSpecialization T) (F : X.Modules) [F.IsCoherent]
    (himm : ∀ x x' : X, IsImmediateSpecialization x x' → x' ∈ T → x ∉ T →
      (1 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x)) (F.presheaf.stalk x)) :
    ∃ (G : X.Modules) (φ : F ⟶ G), IsDepthTwoExtension T φ
```

**`AlgebraicGeometry.existsUnique_isDepthTwoExtension_of_hasDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/DepthTwoExtensionConstruction.lean, line 499](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/DepthTwoExtensionConstruction.lean#L499). The attribute's comment: “the source's unique map, as existence together with uniqueness up to a unique isomorphism under F, at the source's hypotheses”.

> **Existence and uniqueness of the depth-two extension.**  Under the hypotheses of
> `AlgebraicGeometry.exists_isDepthTwoExtension_of_hasDualizingComplex` there is a map `F ⟶ F''`
> of coherent modules which is an isomorphism on the stalks off `T` and whose stalks on `T` have
> depth at least two, and it is unique: any other such map is carried to it by a unique
> isomorphism under `F`.

```lean
public theorem existsUnique_isDepthTwoExtension_of_hasDualizingComplex
    (X : Scheme.{u}) [IsNoetherian X] (hdual : HasDualizingComplexOnAffineCover X)
    (T : Set X) (hT : StableUnderSpecialization T) (F : X.Modules) [F.IsCoherent]
    (himm : ∀ x x' : X, IsImmediateSpecialization x x' → x' ∈ T → x ∉ T →
      (1 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x)) (F.presheaf.stalk x)) :
    ∃ (G : X.Modules) (φ : F ⟶ G), IsDepthTwoExtension T φ ∧
      ∀ (H : X.Modules) (ψ : F ⟶ H), IsDepthTwoExtension T ψ →
        ∃! e : G ≅ H, φ ≫ e.hom = ψ
```

**`AlgebraicGeometry.exists_isDepthTwoExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/DepthTwoExtensionExistence.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/DepthTwoExtensionExistence.lean#L249). The attribute's comment: “existence, conditional on a coherent stabilized open extension of the depth-one quotient along the subset and on Tag 0EY0 part (3)”.

> **Stacks Project, Tag 0EI3, existence.** A coherent module on a Noetherian scheme admits a
> map to a coherent module which is an isomorphism on the stalks away from a
> specialization-stable subset and whose stalks on that subset have depth at least two.
>
> Two inputs of the source's proof are carried as hypotheses, because this library does not have
> them.
>
> * `hext` asks for the extension of the depth-one quotient of `F` across `T` by sections over the
>   opens whose complement lies in `T` — the colimit of the pushforwards `j_{V,*}(F'|_V)` — as a
>   coherent module.  Its coherence is what the source derives from Faltings' finiteness criterion
>   [Stacks, Tag 0EFD] applied to a dualizing complex, using the hypothesis that `X` locally has
>   one and the hypothesis on the depth of `F` at the immediate specializations into `T`.  Those
>   two hypotheses of [Stacks, Tag 0EI3] therefore do not appear here.
> * `hdepthOutside` is [Stacks, Tag 0EY0] part (3), the converse of
>   `AlgebraicGeometry.isIso_unit_restrict_pushforward_of_depth_ge_two`.
>
> The map itself, the clause away from `T` and the depth clause on `T` are proved.  See the
> implementation notes of this module.

```lean
public theorem exists_isDepthTwoExtension
    (X : Scheme.{u}) [IsNoetherian X] (T : Set X) (hT : StableUnderSpecialization T)
    (F : X.Modules) [F.IsCoherent]
    (hdepthOutside : ∀ (V : X.Opens) (H : X.Modules), H.IsCoherent →
      IsIso ((Scheme.Modules.pullbackPushforwardAdjunction V.ι).unit.app H) →
      ∀ y : X, y ∉ (V : Set X) →
        letI : Module (X.presheaf.stalk y)
            (TopCat.Presheaf.stalk (C := Ab.{u}) H.val.presheaf y) :=
          PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
            (R := X.presheaf) H.val y
        (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk y)
          (IsLocalRing.maximalIdeal (X.presheaf.stalk y))
          (TopCat.Presheaf.stalk (C := Ab.{u}) H.val.presheaf y))
    (hext : ∃ (G : X.Modules) (ψ : depthOneQuotient X T hT F ⟶ G),
      IsStabilizedOpenExtension T ψ) :
    ∃ (G : X.Modules) (φ : F ⟶ G), IsDepthTwoExtension T φ
```

**`AlgebraicGeometry.depthTwoExtension_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/DepthTwoExtensionPullback.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/DepthTwoExtensionPullback.lean#L48). The attribute's comment: “the Cohen-Macaulay pullback clause, unconditionally”.

> The pullback of a depth-two extension along a Cohen–Macaulay morphism of Noetherian schemes
> is a depth-two extension along the inverse image of the subset.
>
> The hypothesis `hfib`, that the fibres of `f` are locally Noetherian, is the one under which
> `AlgebraicGeometry.Scheme.Hom.IsCohenMacaulay` is stated; it follows from `[IsNoetherian Y]` by
> `AlgebraicGeometry.isLocallyNoetherian_fiber`.

```lean
public theorem depthTwoExtension_pullback
    {X Y : Scheme.{u}} [IsNoetherian X] [IsNoetherian Y]
    (T : Set X) (F G : X.Modules) (φ : F ⟶ G)
    (hφ : IsDepthTwoExtension T φ)
    (f : Y ⟶ X) (hfib : ∀ x : X, IsLocallyNoetherian (f.fiber x))
    (hcm : f.IsCohenMacaulay hfib) :
    IsDepthTwoExtension (f ⁻¹' T) ((Scheme.Modules.pullback f).map φ)
```

**`AlgebraicGeometry.exists_isDepthTwoExtension_of_isStabilizedOpenExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ExistenceDepthOutside.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ExistenceDepthOutside.lean#L66). The attribute's comment: “existence, conditional only on a coherent stabilized open extension of the depth-one quotient along the subset; the other hypothesis of exists\_isDepthTwoExtension, namely Tag 0EY0 part (3), is discharged here”.

> A coherent module on a Noetherian scheme admits a map to a coherent module which is an
> isomorphism on the stalks away from a specialization-stable subset and whose stalks on that
> subset have depth at least two, as soon as the depth-one quotient has a stabilized open
> extension across the subset.

```lean
public theorem exists_isDepthTwoExtension_of_isStabilizedOpenExtension
    (X : Scheme.{u}) [IsNoetherian X] (T : Set X) (hT : StableUnderSpecialization T)
    (F : X.Modules) [F.IsCoherent]
    (hext : ∃ (G : X.Modules) (ψ : depthOneQuotient X T hT F ⟶ G),
      IsStabilizedOpenExtension T ψ) :
    ∃ (G : X.Modules) (φ : F ⟶ G), IsDepthTwoExtension T φ
```

**`AlgebraicGeometry.exists_isDepthTwoExtension_of_isClosed_of_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/SpecializationStableExistence.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/SpecializationStableExistence.lean#L211). The attribute's comment: “existence along a specialization-stable subset, with no hypothesis about extensions or colimits, and at the source's hypotheses — the dualizing hypothesis and the depth hypothesis on immediate specializations — together with a closed subset of T outside which the depth-one quotient already has depth two on T”.

> **Stacks Project, Tag 0EI3, existence along a specialization-stable subset.** Let `X` be a
> Noetherian scheme which locally has a dualizing complex, let `T ⊆ X` be stable under
> specialization and let `F` be a coherent `𝒪_X`-module such that `depth(F_x) ≥ 1` whenever some
> point of `T` is an immediate specialization of `x ∉ T`.  Let `Z ⊆ T` be closed and such that the
> depth-one quotient `F'` of `F` along `T` already has `depth(F'_x) ≥ 2` at the points of `T`
> outside `Z`.  Then `F` admits a depth-two extension along `T`.
>
> No hypothesis about extensions or colimits is left, and the depth-two extension is the single
> pushforward `j_{Zᶜ,*}(F'|_{Zᶜ})`: for a closed `T` one may take `Z = T`, recovering
> `AlgebraicGeometry.exists_isDepthTwoExtension_of_locallyHasDualizingComplex`.  See the module
> documentation for the three clauses and for the status of `Z` itself.

```lean
public theorem exists_isDepthTwoExtension_of_isClosed_of_subset
    (X : Scheme.{u}) [IsNoetherian X] (T : Set X) (hT : StableUnderSpecialization T)
    (F : X.Modules) [F.IsCoherent]
    (hdual : LocallyHasDualizingComplex X)
    (hdepth : ∀ x z : X, x ∉ T → z ∈ T → TopologicalSpace.IsImmediateSpecialization x z →
      (1 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
        (TopCat.Presheaf.stalk (C := Ab.{u}) F.val.presheaf x))
    (Z : Set X) (hZclosed : IsClosed Z) (hZT : Z ⊆ T)
    (hZ : ∀ x : X, x ∈ T → x ∉ Z →
      letI : Module (X.presheaf.stalk x)
          (TopCat.Presheaf.stalk (C := Ab.{u}) (depthOneQuotient X T hT F).val.presheaf x) :=
        PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
          (R := X.presheaf) (depthOneQuotient X T hT F).val x
      (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
        (TopCat.Presheaf.stalk (C := Ab.{u})
          (depthOneQuotient X T hT F).val.presheaf x)) :
    ∃ (G : X.Modules) (φ : F ⟶ G), IsDepthTwoExtension T φ
```

**`AlgebraicGeometry.exists_isDepthTwoExtension_of_finite_depthOne_locus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/SpecializationStableExistence.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/SpecializationStableExistence.lean#L285). The attribute's comment: “existence along a specialization-stable subset, with no hypothesis about extensions or colimits, and at the source's hypotheses — the dualizing hypothesis and the depth hypothesis on immediate specializations — together with finiteness of the set of points of T where the depth-one quotient still has depth below two”.

> **Stacks Project, Tag 0EI3, existence along a specialization-stable subset, from finiteness
> of the depth-one locus.** Same as `exists_isDepthTwoExtension_of_isClosed_of_subset`, with the
> closed subset replaced by the hypothesis that the set of points of `T` where the depth-one
> quotient `F'` still has depth below two is **finite**.
>
> A finite set of points has closed closure — the union of the finitely many closures of its
> points — and that closure stays inside `T` because `T` is stable under specialization.  So the
> finite set's closure is a legitimate `Z`, and the remaining gap in the existence half of
> [Stacks, Tag 0EI3] is exactly this finiteness.  It is the shape the finiteness theorems about
> depth take: [Stacks, Tag 0ECN] (`AlgebraicGeometry.finite_setOf_depth_eq_and_lt_supportDim`)
> says that on a Noetherian scheme with a dualizing complex a coherent module satisfying Serre's
> condition `(S₁)` has only finitely many points with `depth(F'_x) = 1` and
> `dim Supp(F'_x) > 1`.

```lean
public theorem exists_isDepthTwoExtension_of_finite_depthOne_locus
    (X : Scheme.{u}) [IsNoetherian X] (T : Set X) (hT : StableUnderSpecialization T)
    (F : X.Modules) [F.IsCoherent]
    (hdual : LocallyHasDualizingComplex X)
    (hdepth : ∀ x z : X, x ∉ T → z ∈ T → TopologicalSpace.IsImmediateSpecialization x z →
      (1 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
        (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
        (TopCat.Presheaf.stalk (C := Ab.{u}) F.val.presheaf x))
    (hfin : {x : X | x ∈ T ∧
      letI : Module (X.presheaf.stalk x)
          (TopCat.Presheaf.stalk (C := Ab.{u}) (depthOneQuotient X T hT F).val.presheaf x) :=
        PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
          (R := X.presheaf) (depthOneQuotient X T hT F).val x
      Module.depth (X.presheaf.stalk x) (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
        (TopCat.Presheaf.stalk (C := Ab.{u})
          (depthOneQuotient X T hT F).val.presheaf x) < (2 : ℕ∞)}.Finite) :
    ∃ (G : X.Modules) (φ : F ⟶ G), IsDepthTwoExtension T φ
```

## Tag 0EI4, a lemma

[Tag 0EI4](https://stacks.math.columbia.edu/tag/0EI4) in the Stacks Project.

**`AlgebraicGeometry.exists_isNestedImprovement_of_isStabilizedOpenExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ExistenceDepthOutside.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/ExistenceDepthOutside.lean#L81). The attribute's comment: “existence, conditional only on a coherent stabilized open extension of the depth-one quotient along T'; the other hypothesis of exists\_isNestedImprovement, namely Tag 0EY0 part (3), is discharged here”.

> A coherent module on a Noetherian scheme admits an improvement along a nested pair `T' ⊆ T`
> of subsets stable under specialization, as soon as the depth-one quotient along `T` has a
> stabilized open extension across `T'`.

```lean
public theorem exists_isNestedImprovement_of_isStabilizedOpenExtension
    (X : Scheme.{u}) [IsNoetherian X] (T T' : Set X) (hTT' : T' ⊆ T)
    (hT : StableUnderSpecialization T) (F : X.Modules) [F.IsCoherent]
    (hext : ∃ (G : X.Modules) (ψ : depthOneQuotient X T hT F ⟶ G),
      IsStabilizedOpenExtension T' ψ) :
    ∃ (G : X.Modules) (φ : F ⟶ G), IsNestedImprovement T T' φ
```

**`AlgebraicGeometry.nestedImprovement_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/NestedImprovement.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/NestedImprovement.lean#L241). The attribute's comment: “uniqueness, unconditionally: no dualizing complex is needed, no condition on immediate specializations is used, and the inclusion T' ⊆ T is not needed either”.

> **Stacks Project, Tag 0EI4, uniqueness.** Two improvements of a coherent module along the
> same pair of subsets are isomorphic by a unique isomorphism compatible with the two maps.
>
> Each one factors through the depth-one quotient of its source along `T` by a depth-two extension
> along `T'`, so the comparison is the one of [Stacks, Tag 0EI3], transported across the
> epimorphism onto the depth-one quotient.

```lean
public theorem nestedImprovement_unique (X : Scheme.{u}) [IsNoetherian X]
    (T T' : Set X) (hT : StableUnderSpecialization T)
    (F G H : X.Modules) [F.IsCoherent] (φ : F ⟶ G) (ψ : F ⟶ H)
    (hφ : IsNestedImprovement T T' φ) (hψ : IsNestedImprovement T T' ψ) :
    ∃! e : G ≅ H, φ ≫ e.hom = ψ
```

**`AlgebraicGeometry.exists_isNestedImprovement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/NestedImprovement.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/NestedImprovement.lean#L275). The attribute's comment: “existence, conditional on a coherent stabilized open extension of the depth-one quotient along T' and on Tag 0EY0 part (3); as for Tag 0EI3 in this library, those two hypotheses replace the dualizing complex and the condition on immediate specializations, which are therefore not assumed”.

> **Stacks Project, Tag 0EI4, existence.** A coherent module on a Noetherian scheme admits an
> improvement along a nested pair `T' ⊆ T` of subsets stable under specialization: a map to a
> coherent module which is an isomorphism on the stalks away from `T`, is surjective on the stalks
> with target of depth at least one at the points of `T` outside `T'`, and has target of depth at
> least two at the points of `T'`.
>
> The map is the depth-one quotient of `F` along `T` followed by a depth-two extension of that
> quotient along `T'`, which is the source's construction.  The hypotheses `hdepthOutside` and
> `hext` are the two inputs of the source's existence proof which this library does not have; they
> subsume what the source extracts from the dualizing complex and from the condition on immediate
> specializations into `T'`, so neither of those two hypotheses of the source appears here.  See
> the implementation notes of this module.

```lean
public theorem exists_isNestedImprovement (X : Scheme.{u}) [IsNoetherian X]
    (T T' : Set X) (hTT' : T' ⊆ T) (hT : StableUnderSpecialization T)
    (F : X.Modules) [F.IsCoherent]
    (hdepthOutside : ∀ (V : X.Opens) (H : X.Modules), H.IsCoherent →
      IsIso ((Scheme.Modules.pullbackPushforwardAdjunction V.ι).unit.app H) →
      ∀ y : X, y ∉ (V : Set X) →
        letI : Module (X.presheaf.stalk y)
            (TopCat.Presheaf.stalk (C := Ab.{u}) H.val.presheaf y) :=
          PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
            (R := X.presheaf) H.val y
        (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk y)
          (IsLocalRing.maximalIdeal (X.presheaf.stalk y))
          (TopCat.Presheaf.stalk (C := Ab.{u}) H.val.presheaf y))
    (hext : ∃ (G : X.Modules) (ψ : depthOneQuotient X T hT F ⟶ G),
      IsStabilizedOpenExtension T' ψ) :
    ∃ (G : X.Modules) (φ : F ⟶ G), IsNestedImprovement T T' φ
```

**`AlgebraicGeometry.isCoherent_pullback_of_isNestedImprovement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/NestedImprovement.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/NestedImprovement.lean#L409). The attribute's comment: “coherence of the target of the pullback, in the assertion about the pullback along a Cohen-Macaulay morphism”.

> **Stacks Project, Tag 0EI4, the pullback clause: coherence of the target.** The target of the
> pullback of an improvement along a morphism with locally Noetherian source is again coherent.
>
> A pullback of a coherent module needs only a locally Noetherian source, so neither flatness nor
> Cohen-Macaulayness of the morphism is used.

```lean
public theorem isCoherent_pullback_of_isNestedImprovement {X Y : Scheme.{u}}
    [IsLocallyNoetherian Y] (f : Y ⟶ X) {T T' : Set X} {F G : X.Modules} (φ : F ⟶ G)
    (hφ : IsNestedImprovement T T' φ) :
    ((Scheme.Modules.pullback f).obj G).IsCoherent
```

**`AlgebraicGeometry.isIso_stalk_pullback_of_isNestedImprovement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/NestedImprovement.lean, line 424](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/NestedImprovement.lean#L424). The attribute's comment: “condition (1) for the pullback: the isomorphism away from the inverse image of T, in the assertion about the pullback along a Cohen-Macaulay morphism”.

> **Stacks Project, Tag 0EI4, the pullback clause, condition (1).** The pullback of an
> improvement along any morphism of schemes is an isomorphism on the stalks at every point outside
> the inverse image of `T`.
>
> The stalk of a pullback is the base change of the stalk, so a bijective stalk map stays
> bijective; no hypothesis on the morphism is used.

```lean
public theorem isIso_stalk_pullback_of_isNestedImprovement {X Y : Scheme.{u}} (f : Y ⟶ X)
    {T T' : Set X} {F G : X.Modules} (φ : F ⟶ G) (hφ : IsNestedImprovement T T' φ)
    (y : Y) (hy : y ∉ f.base ⁻¹' T) :
    IsIso ((TopCat.Presheaf.stalkFunctor Ab.{u} y).map
      ((Scheme.Modules.pullback f).map φ).mapPresheaf)
```

**`AlgebraicGeometry.one_le_depth_stalk_pullback_of_isNestedImprovement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/NestedImprovement.lean, line 441](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/NestedImprovement.lean#L441). The attribute's comment: “the depth bound of condition (2) for the pullback, in the assertion about the pullback along a Cohen-Macaulay morphism”.

> **Stacks Project, Tag 0EI4, the pullback clause, the depth bound of condition (2).** The
> target of the pullback of an improvement along a Cohen-Macaulay morphism of Noetherian schemes
> has stalks of depth at least one at every point of the inverse image of `T` lying outside the
> inverse image of `T'`.
>
> Only the flatness half of the Cohen-Macaulay hypothesis is used: the depth of the base change of
> a stalk along a flat local homomorphism is the depth of the stalk plus the depth of the fibre, so
> the bound downstairs is inherited.

```lean
public theorem one_le_depth_stalk_pullback_of_isNestedImprovement {X Y : Scheme.{u}}
    [IsNoetherian X] [IsNoetherian Y] {T T' : Set X} {F G : X.Modules} (φ : F ⟶ G)
    (hφ : IsNestedImprovement T T' φ) (f : Y ⟶ X)
    (hfib : ∀ x : X, IsLocallyNoetherian (f.fiber x)) (hcm : f.IsCohenMacaulay hfib)
    (y : Y) (hy : y ∈ f.base ⁻¹' T) (hy' : y ∉ f.base ⁻¹' T') :
    letI : Module (Y.presheaf.stalk y)
        (TopCat.Presheaf.stalk (C := Ab.{u})
          ((Scheme.Modules.pullback f).obj G).val.presheaf y) :=
      PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
        (R := Y.presheaf) ((Scheme.Modules.pullback f).obj G).val y
    (1 : ℕ∞) ≤ Module.depth (Y.presheaf.stalk y)
      (IsLocalRing.maximalIdeal (Y.presheaf.stalk y))
      (TopCat.Presheaf.stalk (C := Ab.{u})
        ((Scheme.Modules.pullback f).obj G).val.presheaf y)
```

**`AlgebraicGeometry.two_le_depth_stalk_pullback_of_isNestedImprovement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/NestedImprovement.lean, line 468](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/NestedImprovement.lean#L468). The attribute's comment: “condition (3) for the pullback, in the assertion about the pullback along a Cohen-Macaulay morphism”.

> **Stacks Project, Tag 0EI4, the pullback clause, condition (3).** The target of the pullback
> of an improvement along a Cohen-Macaulay morphism of Noetherian schemes has stalks of depth at
> least two at every point of the inverse image of `T'`.
>
> Only the flatness half of the Cohen-Macaulay hypothesis is used, by the same depth formula along
> a flat local homomorphism.

```lean
public theorem two_le_depth_stalk_pullback_of_isNestedImprovement {X Y : Scheme.{u}}
    [IsNoetherian X] [IsNoetherian Y] {T T' : Set X} {F G : X.Modules} (φ : F ⟶ G)
    (hφ : IsNestedImprovement T T' φ) (f : Y ⟶ X)
    (hfib : ∀ x : X, IsLocallyNoetherian (f.fiber x)) (hcm : f.IsCohenMacaulay hfib)
    (y : Y) (hy' : y ∈ f.base ⁻¹' T') :
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

**`AlgebraicGeometry.isNestedImprovement_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/NestedImprovement.lean, line 569](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/NestedImprovement.lean#L569). The attribute's comment: “the assertion about the pullback along a Cohen-Macaulay morphism: the pullback satisfies conditions (1), (2) and (3) with respect to the inverse images of the two subsets”.

> **Stacks Project, Tag 0EI4, the assertion about the pullback.** The pullback of an improvement
> along a Cohen-Macaulay morphism of Noetherian schemes is an improvement along the inverse images
> of the two subsets.
>
> Coherence of the target and condition (1) need no hypothesis on the morphism at all.  Of the
> Cohen-Macaulay hypothesis only the flatness half is used, for the two depth bounds, by the formula
> for the change in depth along a flat local homomorphism [Stacks, Tag 0338]; the fibre never has to
> be identified.  Surjectivity in condition (2) is epimorphy on a stalk, which is the vanishing of
> the stalk of the cokernel, and the pullback preserves cokernels and kills the zero module.

```lean
public theorem isNestedImprovement_pullback {X Y : Scheme.{u}} [IsNoetherian X] [IsNoetherian Y]
    {T T' : Set X} {F G : X.Modules} (φ : F ⟶ G) (hφ : IsNestedImprovement T T' φ) (f : Y ⟶ X)
    (hfib : ∀ x : X, IsLocallyNoetherian (f.fiber x)) (hcm : f.IsCohenMacaulay hfib) :
    IsNestedImprovement (f.base ⁻¹' T) (f.base ⁻¹' T')
      ((Scheme.Modules.pullback f).map φ)
```

**`AlgebraicGeometry.exists_isNestedImprovement_of_hasDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/NestedImprovementExistence.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/NestedImprovementExistence.lean#L92). The attribute's comment: “existence, at the hypotheses of the source and no others: Noetherian, locally a dualizing complex in the source's sense that every point has an affine neighbourhood carrying one, T' subset T both stable under specialization, immediate specializations into T' starting in T. Tag 0EI3 existence is composed with Tag 0DX3 here”.

> **Stacks Project, Tag 0EI4, existence, at the hypotheses of the source.** Let `X` be a
> Noetherian scheme which locally has a dualizing complex and let `T' ⊆ T ⊆ X` be stable under
> specialization and such that every immediate specialization into `T'` starts in `T`.  Then a
> coherent `𝒪_X`-module `F` admits a map to a coherent module which is an isomorphism on the
> stalks away from `T`, is surjective on the stalks with target of depth at least one at the
> points of `T` outside `T'`, and has target of depth at least two at the points of `T'`.
>
> The map is the depth-one quotient of `F` along `T` followed by a depth-two extension of that
> quotient along `T'`, which is the source's construction: the first step is [Stacks, Tag 0DX3],
> the second is the existence half of [Stacks, Tag 0EI3] in the form
> `AlgebraicGeometry.exists_isDepthTwoExtension_of_hasDualizingComplex`, and the composition is
> `AlgebraicGeometry.isNestedImprovement_depthOneQuotient_comp`.
>
> The dualizing hypothesis is `AlgebraicGeometry.HasDualizingComplexOnAffineCover`, which says
> every point has an affine open neighbourhood whose ring of sections admits a dualizing complex.
> That is the source's phrase "locally has a dualizing complex", and it is **weaker** than
> `AlgebraicGeometry.LocallyHasDualizingComplex`, which asks this of *every* affine open.

```lean
public theorem exists_isNestedImprovement_of_hasDualizingComplex
    (X : Scheme.{u}) [IsNoetherian X] (hdual : HasDualizingComplexOnAffineCover X)
    (T T' : Set X) (hTT' : T' ⊆ T)
    (hT : StableUnderSpecialization T) (hT' : StableUnderSpecialization T')
    (himm : ∀ x x' : X, IsImmediateSpecialization x x' → x' ∈ T' → x ∈ T)
    (F : X.Modules) [F.IsCoherent] :
    ∃ (G : X.Modules) (φ : F ⟶ G), IsNestedImprovement T T' φ
```

**`AlgebraicGeometry.existsUnique_isNestedImprovement_of_hasDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/NestedImprovementExistence.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/ImprovingCoherentModules/NestedImprovementExistence.lean#L119). The attribute's comment: “the source's unique map, as existence together with uniqueness up to a unique isomorphism under F, at the hypotheses of the source and no others”.

> **Stacks Project, Tag 0EI4, the source's unique map.** Under the hypotheses of
> `AlgebraicGeometry.exists_isNestedImprovement_of_hasDualizingComplex` there is a map `F ⟶ F''`
> of coherent modules which is an isomorphism on the stalks away from `T`, is surjective on the
> stalks with target of depth at least one at the points of `T` outside `T'`, and has target of
> depth at least two at the points of `T'`; and it is unique: any other such map is carried to it
> by a unique isomorphism under `F`.
>
> This is the source's sentence "there exists a unique map" in one statement.  Existence is
> `AlgebraicGeometry.exists_isNestedImprovement_of_hasDualizingComplex` and uniqueness is
> `AlgebraicGeometry.nestedImprovement_unique`, which needs neither the dualizing complex, nor the
> condition on immediate specializations, nor `T' ⊆ T`.

```lean
public theorem existsUnique_isNestedImprovement_of_hasDualizingComplex
    (X : Scheme.{u}) [IsNoetherian X] (hdual : HasDualizingComplexOnAffineCover X)
    (T T' : Set X) (hTT' : T' ⊆ T)
    (hT : StableUnderSpecialization T) (hT' : StableUnderSpecialization T')
    (himm : ∀ x x' : X, IsImmediateSpecialization x x' → x' ∈ T' → x ∈ T)
    (F : X.Modules) [F.IsCoherent] :
    ∃ (G : X.Modules) (φ : F ⟶ G), IsNestedImprovement T T' φ ∧
      ∀ (H : X.Modules) (ψ : F ⟶ H), IsNestedImprovement T T' ψ →
        ∃! e : G ≅ H, φ ≫ e.hom = ψ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.15, Tag 0DX2](https://stacks.math.columbia.edu/tag/0DX2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
