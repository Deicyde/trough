---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.hasFiniteTypeQuasicoherentIdealZeroLocus_of_isQuasiCompactSpace, AlgebraicGeometry.Space.isQuasiCompactSpace_of_hasFiniteTypeQuasicoherentIdealZeroLocus, AlgebraicGeometry.Space.tfae_isQuasiCompact_openSubspace, AlgebraicGeometry.Space.isQuasiCompact_iff_isQuasiCompactSpace_openSubspace, AlgebraicGeometry.Space.mem_annihilatorSubmodule_obj_of_isAffine, AlgebraicGeometry.Space.exists_germ_annihilatorSubmodule_iff, AlgebraicGeometry.Space.isQuasicoherentOnSite_annihilatorSubmodule, AlgebraicGeometry.Space.annihilatorSubmodule
statement: formalized
proof: formalized
---

# 70.14 Sections with support in a closed subset

Section 70.14 of the Stacks Project, [Tag 0854](https://stacks.math.columbia.edu/tag/0854). 7 tags here are carried by 17 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0855, a lemma

[Tag 0855](https://stacks.math.columbia.edu/tag/0855) in the Stacks Project.

**`AlgebraicGeometry.Space.hasFiniteTypeQuasicoherentIdealZeroLocus_of_isQuasiCompactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeIdealOfQuasiCompactOpen.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeIdealOfQuasiCompactOpen.lean#L256). The attribute's comment: “part (2) implies part (3)”.

> Let `X` be a quasi-compact and quasi-separated algebraic space over `S` and let `U ⊆ X` be an
> open subspace. If `U` is quasi-compact, then there is a finite type quasi-coherent sheaf of ideals
> `ℐ ⊆ 𝒪_X` with `|X| ∖ |U| = |V(ℐ)|`.
>
> This is
> `AlgebraicGeometry.Space.exists_isFiniteTypeQuasicoherentIdeal_idealZeroLocus_eq_compl_range`,
> which follows the source: the reduced sheaf of ideals of `|X| ∖ |U|` is cut down by Stacks 0853,
> `AlgebraicGeometry.Space.exists_etaleSubmodule_extension`, to a quasi-coherent sheaf of ideals of
> finite type with the same restriction to `U`.

```lean
theorem hasFiniteTypeQuasicoherentIdealZeroLocus_of_isQuasiCompactSpace
    (hZ : B.Contains (⊤_ Scheme.{u})) (X : AlgebraicSpaces B S hS)
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    {U : Subfunctor X.1} (hU : IsOpenSubspace B S hS U)
    (hUqc : IsQuasiCompactSpace B S hS U.toFunctor) :
    HasFiniteTypeQuasicoherentIdealZeroLocus B S hS X U
```

**`AlgebraicGeometry.Space.isQuasiCompactSpace_of_hasFiniteTypeQuasicoherentIdealZeroLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactOpenOfFiniteTypeIdeal.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactOpenOfFiniteTypeIdeal.lean#L129). The attribute's comment: “part (3) implies part (2)”.

> **Stacks 0855, part (3) implies part (2).** Let `X` be a quasi-compact algebraic space over
> `S` and let `U ⊆ X` be an open subspace.  If there is a finite type quasi-coherent sheaf of
> ideals `ℐ ⊆ 𝒪_X` with `|X| ∖ |U| = |V(ℐ)|`, then `U` is quasi-compact.
>
> An affine étale chart of `X` surjective on points exists by Tag 03H6.  The Zariski sheaf of
> ideals which `ℐ` induces on the chart's scheme is of finite type, so the complement of its
> support is a quasi-compact open of that affine — and hence quasi-compact — scheme, by part
> (4) ⟹ (2) of [Stacks, Tag 01PH].  That complement maps onto `|U| = |X| ∖ |V(ℐ)|`, continuously,
> so `|U|` is a quasi-compact subset of `|X|`, and Tag 03E4 turns that into quasi-compactness of
> the open subspace `U`.

```lean
theorem isQuasiCompactSpace_of_hasFiniteTypeQuasicoherentIdealZeroLocus
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    {U : Subfunctor X.1} (hU : IsOpenSubspace B S hS U)
    (h : HasFiniteTypeQuasicoherentIdealZeroLocus B S hS X U) :
    IsQuasiCompactSpace B S hS U.toFunctor
```

**`AlgebraicGeometry.Space.tfae_isQuasiCompact_openSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactOpenTfae.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactOpenTfae.lean#L56).

> **Stacks 0855.** Let `X` be a quasi-compact and quasi-separated algebraic space over `S` and
> let `U ⊆ X` be an open subspace.  The following are equivalent:
>
> 1. the inclusion `U → X` is quasi-compact,
> 2. `U` is quasi-compact, and
> 3. there exists a finite type quasi-coherent sheaf of ideals `ℐ ⊆ 𝒪_X` such that
>    `|X| ∖ |U| = |V(ℐ)|`.

```lean
theorem tfae_isQuasiCompact_openSubspace (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS) (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    (U : Subfunctor X.1) (hU : IsOpenSubspace B S hS U) :
    List.TFAE [IsQuasiCompact B S hS U.ι, IsQuasiCompactSpace B S hS U.toFunctor,
      HasFiniteTypeQuasicoherentIdealZeroLocus B S hS X U]
```

**`AlgebraicGeometry.Space.isQuasiCompact_iff_isQuasiCompactSpace_openSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactSupport.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactSupport.lean#L205). The attribute's comment: “parts (1) and (2)”.

> For an open subspace of a quasi-compact and
> quasi-separated algebraic space, quasi-compactness of the inclusion is equivalent to
> quasi-compactness of its source.

```lean
theorem isQuasiCompact_iff_isQuasiCompactSpace_openSubspace
    (X : AlgebraicSpaces B S hS)
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    (U : {U : Subfunctor X.1 // IsOpenSubspace B S hS U}) :
    IsQuasiCompact B S hS U.1.ι ↔ IsQuasiCompactSpace B S hS U.1.toFunctor
```

## Tag 0856, a lemma

[Tag 0856](https://stacks.math.columbia.edu/tag/0856) in the Stacks Project.

**`AlgebraicGeometry.Space.mem_annihilatorSubmodule_obj_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IdealAnnihilatorAffineSections.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IdealAnnihilatorAffineSections.lean#L117). The attribute's comment: “part (2)”.

> **[Stacks, Tag 0856], part (2): the sections of the annihilator subsheaf over an affine
> chart.**  Over an affine étale chart `W` of an algebraic space, a section of `G` lies in the
> subsheaf annihilated by a quasi-coherent sheaf of ideals `I` exactly when the sections of `I`
> over `W` itself kill it — no restriction to a smaller chart has to be tested.

```lean
theorem mem_annihilatorSubmodule_obj_of_isAffine
    (hI : I.toSheafOfModules.IsQuasicoherentOnSite) (W : (SmallEtale B S hS F)ᵒᵖ)
    (hW : IsAffine ((SmallEtale.toOver B S hS F ⋙ BigFppfOver.toScheme B S hS).obj W.unop))
    (s : G.val.obj W) :
    s ∈ (annihilatorSubmodule B S hS F hF I G).toSubmodule.obj W ↔
      ∀ a : (Stacks.SheafOfModules.Tensor.ringSheaf
          (smallEtaleRingedSite B S hS F hF).O).obj.obj W,
        a ∈ I.obj W → a • s = 0
```

**`AlgebraicGeometry.Space.exists_germ_annihilatorSubmodule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IdealAnnihilatorGeometricStalk.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IdealAnnihilatorGeometricStalk.lean#L91). The attribute's comment: “part (3)”.

> **[Stacks, Tag 0856], part (3): the geometric stalk of the annihilator subsheaf.**  Let `F`
> be an algebraic space, `I ⊆ 𝒪_F` a quasi-coherent sheaf of ideals of finite type and `G` a
> quasi-coherent `𝒪_F`-module.  An element of the stalk of `G` at a geometric point `x̄` is the
> germ of a section of the subsheaf annihilated by `I` exactly when every germ at `x̄` of a
> section of `I` kills it; that is, `G'_x̄ = {s ∈ G_x̄ | I_x̄ s = 0}` inside `G_x̄`.

```lean
theorem exists_germ_annihilatorSubmodule_iff
    (hI : I.toSheafOfModules.IsQuasicoherentOnSite)
    (hIft : SheafOfModules.IsFiniteTypeOnSite I.toSheafOfModules)
    (x : GeometricPoint B S hS F)
    (s : geometricModuleStalk B S hS ⟨F, hF⟩ x G) :
    (∃ (N : SmallEtaleNeighborhood x)
        (t : (annihilatorSubmodule B S hS F hF I G).toSheafOfModules.val.obj (op N.chart)),
        geometricModuleStalkGerm B S hS ⟨F, hF⟩ x G N
          ((annihilatorSubmodule B S hS F hF I G).ι.val.app (op N.chart) t) = s) ↔
      ∀ (N : SmallEtaleNeighborhood x) (a : chartRing B S hS F hF N.chart),
        a ∈ I.obj (op N.chart) →
          etaleLocalRingGerm B S hS F x (op N) a • s = 0
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_annihilatorSubmodule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IdealAnnihilatorQuasicoherentSpace.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IdealAnnihilatorQuasicoherentSpace.lean#L179). The attribute's comment: “part (1)”.

> **The annihilator subsheaf is quasi-coherent.**  Let `F` be an algebraic space, `I ⊆ 𝒪_F` a
> quasi-coherent sheaf of ideals of finite type and `G` a quasi-coherent `𝒪_F`-module.  The subsheaf
> of sections of `G` annihilated by `I` is quasi-coherent.

```lean
theorem isQuasicoherentOnSite_annihilatorSubmodule
    (hI : I.toSheafOfModules.IsQuasicoherentOnSite)
    (hIft : SheafOfModules.IsFiniteTypeOnSite I.toSheafOfModules)
    (hG : G.IsQuasicoherentOnSite) :
    (annihilatorSubmodule B S hS F hF I G).toSheafOfModules.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.annihilatorSubmodule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IdealAnnihilatorSubsheaf.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IdealAnnihilatorSubsheaf.lean#L79). The attribute's comment: “the subsheaf”.

> **The subsheaf of sections annihilated by an ideal sheaf on an algebraic space**, the
> object of [Stacks, Tag 0856].  Its sections over an étale chart `W` are the sections of `G`
> over `W` all of whose restrictions are annihilated by the sections of `I` there, and that rule
> defines a submodule sheaf of `G`.

```lean
noncomputable def annihilatorSubmodule
    (I : (SheafOfModules.unit
      ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS F hF).O))).Submodule)
    (G : Modules.{u, u} B S hS F hF) : G.Submodule
```

**`AlgebraicGeometry.Space.mem_annihilatorSubmodule_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IdealAnnihilatorSubsheaf.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IdealAnnihilatorSubsheaf.lean#L100). The attribute's comment: “the sections”.

> **The sections of the annihilator subsheaf of [Stacks, Tag 0856].**  A section `s` of `G`
> over an étale chart is annihilated by `I` exactly when, over every chart `W'` over it, every
> section of `I` kills the restriction of `s` to `W'`.

```lean
theorem mem_annihilatorSubmodule_obj (W : (SmallEtale B S hS F)ᵒᵖ) (s : G.val.obj W) :
    s ∈ (annihilatorSubmodule B S hS F hF I G).toSubmodule.obj W ↔
      ∀ (W' : (SmallEtale B S hS F)ᵒᵖ) (g : W ⟶ W')
        (a : ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS F hF).O)).obj.obj W'),
        a ∈ I.obj W' → a • G.val.restrictₛₗ g s = 0
```

## Tag 0857, a definition

[Tag 0857](https://stacks.math.columbia.edu/tag/0857) in the Stacks Project.

Declarations registered for the tag:

- [`annihilatorSubmodule`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=annihilatorSubmodule#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/IdealAnnihilatorSubsheaf.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IdealAnnihilatorSubsheaf.lean#L89) (StacksFrontier): “the subsheaf of sections annihilated by `I`”.

## Tag 0858, a lemma

[Tag 0858](https://stacks.math.columbia.edu/tag/0858) in the Stacks Project.

**`AlgebraicGeometry.Space.pushforwardSubmodule_annihilatorSubmodule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AnnihilatorSubsheafPushforward.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AnnihilatorSubsheafPushforward.lean#L386).

> **[Stacks, Tag 0858].**  Let `f : X ⟶ Y` be a morphism of algebraic spaces, `I ⊆ 𝒪_Y` a
> sheaf of ideals and `M` an `𝒪_X`-module on the spaces-étale site.  The direct image along `f`
> of the subsheaf of sections of `M` annihilated by `f^{-1}I · 𝒪_X` is the subsheaf of sections
> of `f_*M` annihilated by `I`.
>
> The source assumes `f` quasi-compact and quasi-separated, `I` quasi-coherent of finite type and
> `M` quasi-coherent; all three are discharged as unnecessary, being needed in the source only so
> that the subsheaf of [Stacks, Tag 0857] is available for `I` and `f_*M`.

```lean
theorem pushforwardSubmodule_annihilatorSubmodule (f : X ⟶ Y)
    (I : (SheafOfModules.unit
      ((Stacks.SheafOfModules.Tensor.ringSheaf (spacesEtaleRingedSite B S hS Y).O))).Submodule)
    (M : SheafOfModules.{u + 1}
      ((Stacks.SheafOfModules.Tensor.ringSheaf (spacesEtaleRingedSite B S hS X).O))) :
    Stacks.SheafOfModules.pushforwardSubmodule (spacesEtaleSharpRing B S hS f) M
        (CoverPreserving.of_isContinuous _ _ _)
        (Stacks.SheafOfModules.annihilatorSubmodule M
          (RingedSite.mul_comm_ringSheaf (spacesEtaleRingedSite B S hS X))
          (Stacks.SheafOfModules.inverseImageIdeal (spacesEtaleSharpRing B S hS f) I)) =
      Stacks.SheafOfModules.annihilatorSubmodule
        ((_root_.SheafOfModules.pushforward.{u + 1}
          (spacesEtaleSharpRing B S hS f)).obj M)
        (RingedSite.mul_comm_ringSheaf (spacesEtaleRingedSite B S hS Y)) I
```

## Tag 0859, a lemma

[Tag 0859](https://stacks.math.columbia.edu/tag/0859) in the Stacks Project.

**`AlgebraicGeometry.Space.sectionSupportedIn_iff_exists_pow_le_annihilator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChartBasicOpenLocalization.lean, line 389](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ChartBasicOpenLocalization.lean#L389). The attribute's comment: “part (2): the supported sections over an affine chart are the ideal-power torsion”.

> Let `T` be a subset of the points of an algebraic space `F`, let
> `U` be an affine étale chart of `F` and let `I` be a finitely generated ideal of the regular
> functions on the chart whose zero locus is the preimage of `T`. A section of a quasi-coherent
> `𝒪_F`-module over `U` is supported on `T` exactly when some power of `I` annihilates it.
>
> Part (1), `AlgebraicGeometry.Space.exists_fg_ideal_zeroLocus_eq_preimage_chartPointsMap`,
> supplies such an `I` whenever `T` is closed and its complement is the point set of an open
> subspace with quasi-compact inclusion; `AlgebraicGeometry.Space.chartRing` of a chart is the
> ring of global functions on its scheme, so the two are ideals of the same ring.
>
> Quasi-coherence enters only through
> `AlgebraicGeometry.Space.IsCartesianOnAffineCharts`, which it implies by Stacks 03DX; it is
> derived here rather than assumed, since Stacks 0859 already assumes the module
> quasi-coherent.

```lean
theorem sectionSupportedIn_iff_exists_pow_le_annihilator
    (G : Modules.{u, u} B S hS F hF) (hG : G.IsQuasicoherentOnSite)
    (T : Set (points B S hS F)) (U : SmallEtale B S hS F) (hU : IsAffine (chartScheme U))
    {I : Ideal (chartRing B S hS F hF U)} (hIfg : I.FG)
    (hI : chartPointsMap U ⁻¹' T =
      (chartScheme U).zeroLocus (U := ⊤) (I : Set (chartRing B S hS F hF U)))
    (s : G.val.obj (op U)) :
    SectionSupportedIn B S hS F hF T G U s ↔ ∃ n : ℕ, ∀ a ∈ I ^ n, a • s = 0
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_supportedSectionsSubmodule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChartBasicOpenLocalization.lean, line 649](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ChartBasicOpenLocalization.lean#L649). The attribute's comment: “part (3): the subsheaf of sections supported on T is quasi-coherent”.

> Let `T ⊆ |F|` be a closed subset of the points of an algebraic
> space `F` whose complement is the point set of an open subspace `O ⊆ F` with quasi-compact
> inclusion, and let `G` be a quasi-coherent `𝒪_F`-module.  Then the subsheaf of `G` of sections
> supported on `T` is again quasi-coherent.
>
> The hypotheses are `T` closed, `T ⨿ |O| = |F|`, and `O → F` quasi-compact.  Quasi-coherence
> of the subsheaf is `SheafOfModules.IsQuasicoherentOnSite` (Stacks 03DL (6)), the condition that
> cuts out `AlgebraicGeometry.Space.QuasicoherentSheaves` (Stacks 03G9); it follows from
> `AlgebraicGeometry.Space.bijective_sectionsBaseChange_supportedSectionsSubmodule` by
> Descent, Proposition 03DX (2),
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_iff_isCartesianOnAffineCharts`.

```lean
theorem isQuasicoherentOnSite_supportedSectionsSubmodule
    (G : Modules.{u, u} B S hS F hF) (hG : G.IsQuasicoherentOnSite)
    {T : Set (points B S hS F)} (hT : IsClosed T) {O : Subfunctor F}
    (hO : IsOpenSubspace B S hS O)
    (hOT : Set.range (pointsMap B S hS O.toFunctor O.ι) = Tᶜ)
    (hOqc : IsQuasiCompact B S hS O.ι) :
    (supportedSectionsSubmodule B S hS F hF T G).toSheafOfModules.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.supportedSectionsSubmoduleData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SupportedSectionsSubsheaf.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SupportedSectionsSubsheaf.lean#L197). The attribute's comment: “supported-section subsheaf”.

> The subsheaf of sections supported in `T`, together with its defining local membership
> criterion.

```lean
noncomputable def supportedSectionsSubmoduleData (T : Set (points B S hS F))
    (G : Modules.{u, m} B S hS F hF) :
    {N : G.Submodule // ∀ (W : SmallEtale B S hS F)
      (s : G.val.obj (op W)),
      s ∈ N.toSubmodule.obj (op W) ↔
        SectionSupportedIn B S hS F hF T G W s}
```

**`AlgebraicGeometry.Space.exists_fg_ideal_zeroLocus_eq_preimage_chartPointsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SupportedSectionsSubsheaf.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SupportedSectionsSubsheaf.lean#L294). The attribute's comment: “part (1): a finite type ideal cutting out the closed subset on an affine chart”.

> Let `T ⊆ |F|` be a closed subset of the points of an algebraic space `F`, and let `U ⊆ F` be
> the open subspace whose points are the complement of `T`. If the inclusion `U → F` is
> quasi-compact then on every affine étale chart `φ : W → F` the preimage `|φ|⁻¹(T)` is the zero
> locus of a finitely generated ideal of `𝒪_F(W)`.

```lean
theorem exists_fg_ideal_zeroLocus_eq_preimage_chartPointsMap (hF : IsAlgebraicSpace B S hS F)
    {T : Set (points B S hS F)} (hT : IsClosed T) {U : Subfunctor F}
    (hU : IsOpenSubspace B S hS U)
    (hUT : Set.range (pointsMap B S hS U.toFunctor U.ι) = Tᶜ)
    (hUqc : IsQuasiCompact B S hS U.ι) (W : SmallEtale B S hS F)
    (hW : IsAffine (chartScheme W)) :
    ∃ I : Ideal Γ(chartScheme W, ⊤), I.FG ∧
      chartPointsMap W ⁻¹' T =
        (chartScheme W).zeroLocus (U := ⊤) (I : Set Γ(chartScheme W, ⊤))
```

## Tag 085A, a definition

[Tag 085A](https://stacks.math.columbia.edu/tag/085A) in the Stacks Project.

**`AlgebraicGeometry.Space.supportedSectionsSubmoduleData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SupportedSectionsSubsheaf.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SupportedSectionsSubsheaf.lean#L197). The attribute's comment: “the subsheaf of sections supported on T”.

> The subsheaf of sections supported in `T`, together with its defining local membership
> criterion.

```lean
noncomputable def supportedSectionsSubmoduleData (T : Set (points B S hS F))
    (G : Modules.{u, m} B S hS F hF) :
    {N : G.Submodule // ∀ (W : SmallEtale B S hS F)
      (s : G.val.obj (op W)),
      s ∈ N.toSubmodule.obj (op W) ↔
        SectionSupportedIn B S hS F hF T G W s}
```

## Tag 085B, a lemma

[Tag 085B](https://stacks.math.columbia.edu/tag/085B) in the Stacks Project.

**`AlgebraicGeometry.Space.modulePushforward_supportedSectionsSubmodule_range_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SupportedSectionsModulePushforward.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SupportedSectionsModulePushforward.lean#L95). The attribute's comment: “the identification of the two subsheaves of the direct image, with the direct image spelled as the one of Stacks 03LU”.

> **Stacks 085B with the direct image spelled as the one of Stacks 03LU.**  For a morphism
> `f : X ⟶ Y` of algebraic spaces over `S`, a closed subset `T` of the points of `Y` and an
> `𝒪_X`-module `F`, the direct image `f_*` of Stacks 03LU of the subsheaf of sections supported
> over `|f|⁻¹T` is the subsheaf of `f_*F` of sections supported on `T`: the two canonical
> inclusions into `f_*F` have the same image over every étale chart of `Y`.
>
> This is the same identification as
> `AlgebraicGeometry.Space.pushforward_supportedSectionsSubmodule_range_eq`, which states it for
> the direct image attached to the morphism of ringed topoi of Stacks 03G8.  Both spellings are
> registered, because consumers of the tag are written against one or the other and the passage
> between them is not available downstream: it is cheap only at the two small equations above,
> which is why it is made here.

```lean
theorem modulePushforward_supportedSectionsSubmodule_range_eq
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (T : Set (points B S hS Y.1))
    (hT : @IsClosed _ (pointTopology B S hS Y.1) T)
    (F : Modules.{u, u} B S hS X.1 X.2)
    (W : SmallEtale B S hS Y.1) :
    Set.range (((modulePushforward B S hS f).map
        (supportedSectionsSubmodule B S hS X.1 X.2
          (pointsMap B S hS X.1 f.hom ⁻¹' T) F).ι).val.app (op W)) =
      Set.range ((supportedSectionsSubmodule B S hS Y.1 Y.2 T
        ((modulePushforward B S hS f).obj F)).ι.val.app (op W))
```

**`AlgebraicGeometry.Space.pushforward_supportedSectionsSubmodule_range_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SupportedSectionsPushforward.lean, line 1037](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SupportedSectionsPushforward.lean#L1037). The attribute's comment: “the identification of the two subsheaves of the direct image”.

> For a morphism `f : X ⟶ Y` of algebraic spaces over `S`, a closed subset
> `T` of the points of `Y` and an `𝒪_X`-module `F`, the direct image of the subsheaf of sections
> supported over `|f|⁻¹T` is the subsheaf of `f_*F` of sections supported on `T`: the two
> canonical inclusions into `f_*F` have the same image over every étale chart of `Y`.

```lean
theorem pushforward_supportedSectionsSubmodule_range_eq
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (T : Set (points B S hS Y.1))
    (hT : @IsClosed _ (pointTopology B S hS Y.1) T)
    (F : Modules.{u, u} B S hS X.1 X.2)
    (W : SmallEtale B S hS Y.1) :
    Set.range ((((smallEtaleRingedToposHom B S hS f).pushforwardModules).map
      (supportedSectionsSubmodule B S hS X.1 X.2
        (pointsMap B S hS X.1 f.hom ⁻¹' T) F).ι).val.app (op W)) =
    Set.range (((supportedSectionsSubmodule B S hS Y.1 Y.2 T
      (((smallEtaleRingedToposHom B S hS f).pushforwardModules).obj F)).ι).val.app (op W))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 70.14, Tag 0854](https://stacks.math.columbia.edu/tag/0854)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
