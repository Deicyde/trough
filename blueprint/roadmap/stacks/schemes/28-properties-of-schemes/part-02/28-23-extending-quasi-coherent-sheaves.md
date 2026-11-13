---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_quasicoherent_restrict_iso, AlgebraicGeometry.exists_quasicoherent_extension, AlgebraicGeometry.exists_quasicoherentSubobject_restrict, Stacks.AlgebraicGeometry.Tag01PFAffineExtend.exists_isFiniteType_submodule_restrictTo_eq_of_qcqs, AlgebraicGeometry.exists_finiteTypeQuasicoherentSubobject_extension, Stacks.AlgebraicGeometry.Tag01PGColimitClose.isColimit_finiteTypeQuasicoherentSubobjectCocone, AlgebraicGeometry.isColimit_finiteTypeQuasicoherentSubobjectCocone, AlgebraicGeometry.finiteTypeQuasicoherentSubobject_isFiltered
statement: formalized
proof: formalized
---

# 28.23 Extending quasi-coherent sheaves

Section 28.23 of the Stacks Project, [Tag 01PD](https://stacks.math.columbia.edu/tag/01PD). 13 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01PE, a lemma

[Tag 01PE](https://stacks.math.columbia.edu/tag/01PE) in the Stacks Project.

**`AlgebraicGeometry.exists_quasicoherent_restrict_iso`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/OpenExtension.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/OpenExtension.lean#L59). The attribute's comment: “extend\_quasicoherent”. References: EGA I (1.4.2).

> **Stacks Project, Tag 01PE.** A quasi-coherent module on a quasi-compact open subscheme
> extends to a quasi-coherent module on the ambient scheme: the pushforward along the open immersion
> is quasi-coherent, and its restriction is isomorphic to the given module.

```lean
public lemma exists_quasicoherent_restrict_iso {U X : Scheme.{u}} (j : U ⟶ X)
    [IsOpenImmersion j] [QuasiCompact j] (G : U.Modules) [G.IsQuasicoherent] :
    ∃ (F : X.Modules) (_ : F.IsQuasicoherent), Nonempty (F.restrict j ≅ G)
```

**`AlgebraicGeometry.exists_quasicoherent_extension`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/QuasiCoherentExtension.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/QuasiCoherentExtension.lean#L111). The attribute's comment: “extend\_quasicoherent\_morphism”.

> **Stacks Project, Tag 01PE.** A morphism from a quasi-coherent module on a quasi-compact
> open subscheme to the restriction of a quasi-coherent module extends to a morphism of
> quasi-coherent modules on the whole scheme.

```lean
lemma exists_quasicoherent_extension
    {U X : Scheme.{u}} (j : U ⟶ X) [IsOpenImmersion j] [QuasiCompact j]
    (F : X.Modules) [F.IsQuasicoherent]
    (G : U.Modules) [G.IsQuasicoherent] (φ : G ⟶ F.restrict j) :
    ∃ (H : X.Modules) (_ : H.IsQuasicoherent)
      (ψ : H ⟶ F) (e : H.restrict j ≅ G),
      e.hom ≫ φ = (Scheme.Modules.restrictFunctor j).map ψ
```

**`AlgebraicGeometry.exists_quasicoherentSubobject_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/QuasiCoherentExtension.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/QuasiCoherentExtension.lean#L142). The attribute's comment: “extend\_quasicoherent\_subsheaf”.

> **Stacks Project, Tag 01PE.** A quasi-coherent submodule of the restriction of a
> quasi-coherent module to a quasi-compact open subscheme extends to a quasi-coherent submodule
> of the ambient module.

```lean
theorem exists_quasicoherentSubobject_restrict {U X : Scheme.{u}}
    (j : U ⟶ X) [IsOpenImmersion j] [QuasiCompact j]
    (F : X.Modules) [F.IsQuasicoherent]
    (G : Subobject (F.restrict j)) (hG : (G : U.Modules).IsQuasicoherent) :
    ∃ H : Subobject F, (H : X.Modules).IsQuasicoherent ∧
      ∃ e : (H : X.Modules).restrict j ≅ (G : U.Modules),
        e.hom ≫ G.arrow = (restrictFunctor j).map H.arrow
```

## Tag 01PF, a lemma

[Tag 01PF](https://stacks.math.columbia.edu/tag/01PF) in the Stacks Project.

**`Stacks.AlgebraicGeometry.Tag01PFAffineExtend.exists_isFiniteType_submodule_restrictTo_eq_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineExtend/Induction.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/AffineExtend/Induction.lean#L209). References: EGA I (9.4.6), “qcqs case”; EGA I (9.4.3), “qcqs scheme”; EGA I (9.4.7), “(b)”.

> **Stacks Project, Tag 01PF.** Let `X` be a quasi-compact and quasi-separated scheme, let
> `U ⊆ X` be a quasi-compact open, let `F` be a quasi-coherent `𝒪_X`-module and let `G ⊆ F|_U` be a
> quasi-coherent `𝒪_U`-submodule which is of finite type. Then there exists a quasi-coherent
> submodule `G' ⊆ F` which is of finite type such that `G'|_U = G`.

```lean
theorem exists_isFiniteType_submodule_restrictTo_eq_of_qcqs
    [CompactSpace X] [QuasiSeparatedSpace X] [F.IsQuasicoherent]
    {U : X.Opens} (hU : IsCompact (U : Set X)) (G : (F.restrict U.ι).Submodule)
    (hqc : (G.toSheafOfModules : U.toScheme.Modules).IsQuasicoherent)
    (hft : (G.toSheafOfModules : U.toScheme.Modules).IsFiniteType) :
    ∃ N : F.Submodule, (N.toSheafOfModules : X.Modules).IsQuasicoherent ∧
      (N.toSheafOfModules : X.Modules).IsFiniteType ∧ restrictTo U.ι N = G
```

**`AlgebraicGeometry.exists_finiteTypeQuasicoherentSubobject_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/FiniteTypeSubobjectExtension.lean, line 442](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/FiniteTypeSubobjectExtension.lean#L442). References: EGA I (9.4.6), “qcqs case”; EGA I (9.4.3), “qcqs scheme”; EGA I (9.4.7), “(b)”.

> Let `X` be a quasi-compact quasi-separated scheme, `F` a quasi-coherent `𝒪_X`-module, `U` a
> quasi-compact open and `G` a quasi-coherent subobject of `F|_U` of finite type. Then `G` extends to
> a quasi-coherent subobject of `F` of finite type: there is a quasi-coherent subobject `G'` of `F`
> of finite type and an isomorphism of `G'|_U` with `G` compatible with the inclusions into `F|_U`.

```lean
theorem exists_finiteTypeQuasicoherentSubobject_extension
    {X : Scheme.{u}} [CompactSpace X] [QuasiSeparatedSpace X]
    (F : X.Modules) [F.IsQuasicoherent]
    (U : X.Opens) (hU : IsCompact U.1)
    (G : CategoryTheory.Subobject (F.restrict U.ι))
    [(G : U.toScheme.Modules).IsQuasicoherent]
    [(G : U.toScheme.Modules).IsFiniteType] :
    ∃ (G' : CategoryTheory.Subobject F), (G' : X.Modules).IsQuasicoherent ∧
      (G' : X.Modules).IsFiniteType ∧
      ∃ e : (G' : X.Modules).restrict U.ι ≅ (G : U.toScheme.Modules),
        (Scheme.Modules.restrictFunctor U.ι).map G'.arrow = e.hom ≫ G.arrow
```

## Tag 01PG, a lemma

[Tag 01PG](https://stacks.math.columbia.edu/tag/01PG) in the Stacks Project.

**`Stacks.AlgebraicGeometry.Tag01PGColimitClose.isColimit_finiteTypeQuasicoherentSubobjectCocone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ColimitClose/Basic.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ColimitClose/Basic.lean#L204). The attribute's comment: “colimit”.

> **Stacks Project, Tag 01PG (colimit).** On a quasi-compact and quasi-separated scheme, a
> quasi-coherent module is the colimit of the canonical diagram of all its quasi-coherent finite
> type submodules.

```lean
def isColimit_finiteTypeQuasicoherentSubobjectCocone {X : Scheme.{u}} (F : X.Modules)
    [CompactSpace X] [QuasiSeparatedSpace X] [F.IsQuasicoherent] :
    Limits.IsColimit (finiteTypeQuasicoherentSubobjectCocone F)
```

**`AlgebraicGeometry.isColimit_finiteTypeQuasicoherentSubobjectCocone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/FiniteTypeSubobjectColimit.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/FiniteTypeSubobjectColimit.lean#L223). References: EGA I (9.4.9), “quasi-compact scheme”.

> **Stacks Project, Tag 01PG.** On a quasi-compact and quasi-separated scheme, a quasi-coherent
> module is the colimit of the canonical diagram of all its quasi-coherent finite type submodules.
>
> This is the colimit half of the tag; the other half, that the diagram is filtered — so that the
> colimit is a *directed* one — is
> `AlgebraicGeometry.finiteTypeQuasicoherentSubobject_isFiltered`. Together the two are the tag's
> assertion, so the tag is attached to both.

```lean
noncomputable def isColimit_finiteTypeQuasicoherentSubobjectCocone
    {X : Scheme.{u}} (F : X.Modules)
    [CompactSpace X] [QuasiSeparatedSpace X] [F.IsQuasicoherent] :
    IsColimit (finiteTypeQuasicoherentSubobjectCocone F)
```

**`AlgebraicGeometry.finiteTypeQuasicoherentSubobject_isFiltered`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/FiniteTypeSubobjects.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/FiniteTypeSubobjects.lean#L159).

> **Stacks Project, Tag 01PG.** The category of quasi-coherent finite type submodules of a
> quasi-coherent module is filtered.
>
> This is the directedness half of the tag; the other half, that the canonical cocone over this
> diagram is a colimit cocone, is
> `AlgebraicGeometry.isColimit_finiteTypeQuasicoherentSubobjectCocone`. Together the two are the
> tag's assertion that a quasi-coherent module is the directed colimit of its quasi-coherent
> submodules of finite type, so the tag is attached to both.

```lean
instance finiteTypeQuasicoherentSubobject_isFiltered {X : Scheme.{u}} (F : X.Modules)
    [F.IsQuasicoherent] :
    IsFiltered (FiniteTypeQuasicoherentSubobject F)
```

## Tag 01PI, a lemma

[Tag 01PI](https://stacks.math.columbia.edu/tag/01PI) in the Stacks Project.

**`AlgebraicGeometry.exists_finitePresentation_extension_of_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/FinitePresentationExtension.lean, line 560](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/FinitePresentationExtension.lean#L560). References: EGA I (9.4.8), “special case”.

> **Stacks Project, Tag 01PI.**  Extension of a finitely presented module from a
> quasi-compact open.  Let `X` be a quasi-compact, quasi-separated scheme, `U` a quasi-compact
> open, `F` a quasi-coherent `𝒪_X`-module and `φ : G ⟶ F|_U` a morphism from a finitely presented
> `𝒪_U`-module.  Then `φ` is the restriction of a morphism `G' ⟶ F` from a finitely presented
> `𝒪_X`-module `G'` restricting to `G`.

```lean
theorem exists_finitePresentation_extension_of_hom [CompactSpace X] [QuasiSeparatedSpace X]
    (F : X.Modules) [F.IsQuasicoherent] (U : X.Opens) (hU : IsCompact U.1)
    (G : U.toScheme.Modules) [G.IsFinitePresentation] (φ : G ⟶ F.restrict U.ι) :
    ∃ (G' : X.Modules) (_ : G'.IsFinitePresentation)
      (φ' : G' ⟶ F) (e : G'.restrict U.ι ≅ G),
      e.hom ≫ φ = (restrictFunctor U.ι).map φ'
```

## Tag 0G41, a lemma

[Tag 0G41](https://stacks.math.columbia.edu/tag/0G41) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteTypeQuasicoherent_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/Basic.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/Basic.lean#L47). The attribute's comment: “(1)”. References: EGA I (9.4.8); EGA I (9.4.5).

> **Stacks Project, Tag 0G41 (1).** Let `X` be a quasi-compact and quasi-separated scheme and
> let `U ⊆ X` be a quasi-compact open. A quasi-coherent `𝒪_U`-module of finite type extends to a
> quasi-coherent `𝒪_X`-module of finite type.

```lean
theorem exists_finiteTypeQuasicoherent_extension
    {X : Scheme.{u}} [CompactSpace X] [QuasiSeparatedSpace X]
    (U : X.Opens) (hU : IsCompact U.1)
    (G : U.toScheme.Modules) [G.IsQuasicoherent] [G.IsFiniteType] :
    ∃ (G' : X.Modules) (_ : G'.IsQuasicoherent) (_ : G'.IsFiniteType),
      Nonempty (G'.restrict U.ι ≅ G)
```

**`AlgebraicGeometry.exists_extension_of_isQuasicoherent_isFiniteType`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Extend/Finiteness.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Extend/Finiteness.lean#L48). The attribute's comment: “part (1)”. References: EGA I (9.4.8); EGA I (9.4.5).

> A quasi-coherent module of finite type on a quasi-compact open of a quasi-compact and
> quasi-separated scheme extends to a quasi-coherent module of finite type on the whole scheme.

```lean
lemma exists_extension_of_isQuasicoherent_isFiniteType {X : Scheme.{u}} [CompactSpace X]
    [QuasiSeparatedSpace X] (U : X.Opens) (hU : IsCompact U.1)
    (G : U.toScheme.Modules) [G.IsQuasicoherent] [G.IsFiniteType] :
    ∃ (G' : X.Modules) (_ : G'.IsQuasicoherent) (_ : G'.IsFiniteType),
      Nonempty (G'.restrict U.ι ≅ G)
```

**`AlgebraicGeometry.exists_extension_of_isFinitePresentation`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Extend/Finiteness.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Extend/Finiteness.lean#L70). The attribute's comment: “part (2)”. References: EGA I (9.4.8), “special case”.

> A finitely presented module on a quasi-compact open of a quasi-compact and quasi-separated
> scheme extends to a finitely presented module on the whole scheme.

```lean
lemma exists_extension_of_isFinitePresentation {X : Scheme.{u}} [CompactSpace X]
    [QuasiSeparatedSpace X] (U : X.Opens) (hU : IsCompact U.1)
    (G : U.toScheme.Modules) [G.IsFinitePresentation] :
    ∃ (G' : X.Modules) (_ : G'.IsFinitePresentation), Nonempty (G'.restrict U.ι ≅ G)
```

## Tag 01PJ, a lemma

[Tag 01PJ](https://stacks.math.columbia.edu/tag/01PJ) in the Stacks Project.

**`AlgebraicGeometry.exists_filtered_diagram_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/FinitePresentationColimit.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/FinitePresentationColimit.lean#L337).

> A quasi-coherent module on a quasi-compact, quasi-separated scheme is a filtered colimit of
> finitely presented modules.

```lean
theorem exists_filtered_diagram_of_isFinitePresentation (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X] (F : X.Modules) [F.IsQuasicoherent] :
    ∃ (I : Type u) (inst : SmallCategory I),
      let _ := inst
      ∃ (_ : IsFiltered I) (D : CategoryTheory.Functor I X.Modules)
        (φ : NatTrans D ((Functor.const I).obj F)),
        (∀ i, (D.obj i).IsFinitePresentation) ∧
          Nonempty (IsColimit (Cocone.mk F φ))
```

## Tag 01PK, a lemma

[Tag 01PK](https://stacks.math.columbia.edu/tag/01PK) in the Stacks Project.

**`AlgebraicGeometry.exists_directed_system_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/FinitePresentationColimit.lean, line 376](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/FinitePresentationColimit.lean#L376).

> A quasi-coherent module on a quasi-compact, quasi-separated scheme is a directed colimit of
> finitely presented modules.

```lean
theorem exists_directed_system_of_isFinitePresentation (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X] (F : X.Modules) [F.IsQuasicoherent] :
    ∃ (I : Type u) (_ : PartialOrder I) (_ : Nonempty I)
      (_ : IsDirected I (· ≤ ·)) (D : I ⥤ X.Modules)
      (φ : D ⟶ (Functor.const I).obj F),
      (∀ i, (D.obj i).IsFinitePresentation) ∧
        Nonempty (IsColimit (Cocone.mk F φ))
```

## Tag 086M, a lemma

[Tag 086M](https://stacks.math.columbia.edu/tag/086M) in the Stacks Project.

**`AlgebraicGeometry.exists_directed_colimit_finitePresentation_with_epi_maps`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Coherent/FiniteTypeSubobjectLimits/EpiTransitionMaps.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Coherent/FiniteTypeSubobjectLimits/EpiTransitionMaps.lean#L135). References: EGA IV (1.7.9), “I.9.6.5 clause”.

> **Stacks Project, Tag 086M.** A finite type quasi-coherent module on a quasi-compact and
> quasi-separated scheme is a directed colimit of finitely presented modules with surjective
> transition maps.

```lean
theorem exists_directed_colimit_finitePresentation_with_epi_maps
    (X : Scheme.{u}) [CompactSpace X] [QuasiSeparatedSpace X]
    (M : X.Modules) [M.IsQuasicoherent] [M.IsFiniteType] :
    ∃ (ι : Type u) (_ : PartialOrder ι) (_ : Nonempty ι) (_ : IsDirected ι (· ≤ ·))
      (F : ι ⥤ X.Modules) (_e : colimit F ≅ M),
      (∀ i, (F.obj i).IsFinitePresentation) ∧
        ∀ ⦃i j : ι⦄ (h : i ≤ j), Epi (F.map (homOfLE h))
```

## Tag 080V, a lemma

[Tag 080V](https://stacks.math.columbia.edu/tag/080V) in the Stacks Project.

**`AlgebraicGeometry.exists_finitePresentation_epi_isIso_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/FinitePresentationColimit.lean, line 422](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/FinitePresentationColimit.lean#L422).

> Let `F` be a quasi-coherent module of finite type on a quasi-compact, quasi-separated scheme
> `X` whose restriction to a quasi-compact open `U` is of finite presentation.  Then there is a
> morphism `φ : G ⟶ F` with `G` of finite presentation, `φ` surjective, and `φ|_U` an
> isomorphism.

```lean
theorem exists_finitePresentation_epi_isIso_restrict [CompactSpace X] [QuasiSeparatedSpace X]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType] (U : X.Opens) (hU : IsCompact U.1)
    [(F.restrict U.ι).IsFinitePresentation] :
    ∃ (G : X.Modules) (_ : G.IsFinitePresentation) (φ : G ⟶ F),
      Epi φ ∧ IsIso ((Scheme.Modules.restrictFunctor U.ι).map φ)
```

## Tag 05JS, a lemma

[Tag 05JS](https://stacks.math.columbia.edu/tag/05JS) in the Stacks Project.

**`Stacks.QcohAlgebraFPColimit.exists_directedSystem_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QcohAlgebraFPColimit/Main.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QcohAlgebraFPColimit/Main.lean#L57).

> Let `X` be a quasi-compact and quasi-separated scheme and let `𝒜` be a quasi-coherent sheaf of
> commutative `𝒪_X`-algebras. Then there are a directed set `I`, a system `(𝒜ᵢ, φᵢᵢ')` over `I` of
> `𝒪_X`-algebras and morphisms `φᵢ : 𝒜ᵢ ⟶ 𝒜` with each `𝒜ᵢ` quasi-coherent of finite
> presentation, such that the `φᵢ` induce an isomorphism `colim 𝒜ᵢ ≅ 𝒜`.

```lean
theorem exists_directedSystem_of_isFinitePresentation (X : Scheme.{u}) [CompactSpace ↥X]
    [QuasiSeparatedSpace ↥X] (A : X.QuasicoherentAlgebra)
    (hA : Scheme.QuasicoherentAlgebra.IsQuasicoherent A) :
    ∃ (I : Type (u + 1)) (_ : PartialOrder I) (_ : Nonempty I) (_ : IsDirected I (· ≤ ·))
      (F : Functor I X.QuasicoherentAlgebra) (φ : F ⟶ (Functor.const I).obj A),
      (∀ i, Scheme.QuasicoherentAlgebra.IsQuasicoherent (F.obj i) ∧
        Scheme.QuasicoherentAlgebra.IsOfFinitePresentation (F.obj i)) ∧
        Nonempty (IsColimit (Cocone.mk A φ))
```

## Tag 05JT, a lemma

[Tag 05JT](https://stacks.math.columbia.edu/tag/05JT) in the Stacks Project.

**`Stacks.AlgebraicGeometry.FiniteTypeSubalgebraFiltered.isFiltered_finiteTypeSubalgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteTypeSubalgebraFiltered/Basic.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FiniteTypeSubalgebraFiltered/Basic.lean#L56). The attribute's comment: “directedness”.

> The finite type quasi-coherent subalgebras of a quasi-coherent sheaf of commutative
> `𝒪_X`-algebras form a filtered category. No hypothesis on `X` is needed.
>
> An upper bound of two subalgebras is the image of the morphism to `A` out of the pushed-forward
> structure sheaf of the fibre product of their relative spectra, and the category is nonempty
> because it contains the image of the initial algebra sheaf `𝒪_X`.

```lean
theorem isFiltered_finiteTypeSubalgebra {X : Scheme.{u}} (A : AlgebraSheaf X)
    (hA : AlgebraSheaf.IsQuasicoherent A) :
    IsFiltered (FiniteTypeSubalgebras.FiniteTypeSubalgebra A)
```

**`Stacks.AlgebraicGeometry.FiniteTypeSubalgebraFiltered.nonempty_isColimit_finiteTypeSubalgebraCocone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteTypeSubalgebraFiltered/Basic.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FiniteTypeSubalgebraFiltered/Basic.lean#L84). The attribute's comment: “the colimit”. References: EGA I (9.6.6), “partial”.

> On a quasi-compact and quasi-separated scheme, a quasi-coherent sheaf of commutative
> `𝒪_X`-algebras is the colimit of the canonical diagram of its finite type quasi-coherent
> subalgebras, with the inclusions of the subobjects as the structure morphisms.
>
> The affine sections hypothesis of `nonempty_isColimit_of_affineSections` is
> `Stacks.AlgebraicGeometry.SubalgebraGeneratedByModule.exists_finiteTypeSubalgebra_section`: a
> section over an affine open lies in the subalgebra generated by a finite type quasi-coherent
> submodule.

```lean
theorem nonempty_isColimit_finiteTypeSubalgebraCocone {X : Scheme.{u}} [CompactSpace X]
    [QuasiSeparatedSpace X] (A : AlgebraSheaf X) (hA : AlgebraSheaf.IsQuasicoherent A) :
    Nonempty (IsColimit (FiniteTypeSubalgebras.finiteTypeSubalgebraCocone A))
```

## Tag 086N, a lemma

[Tag 086N](https://stacks.math.columbia.edu/tag/086N) in the Stacks Project.

**`Stacks.FiniteAlgebraLimitPresentation.exists_isColimit_finite_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteAlgebraLimitPresentation/Basic.lean, line 629](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FiniteAlgebraLimitPresentation/Basic.lean#L629).

> **Stacks Project, Tag 086N.** On a quasi-compact and quasi-separated scheme, a finite
> quasi-coherent algebra is a directed colimit of finite and finitely presented quasi-coherent
> algebras whose transition maps are surjective.

```lean
theorem exists_isColimit_finite_finitePresentation (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X] (A : AlgebraSheaf X) (hAqc : A.IsQuasicoherent)
    (hAfin : A.IsFinite) :
    ∃ (I : Type (u + 1)) (_ : Preorder I) (_ : Nonempty I) (_ : IsDirected I (· ≤ ·))
      (F : I ⥤ AlgebraSheaf X) (t : F ⟶ (Functor.const I).obj A)
      (_ : IsColimit (Cocone.mk A t)),
      (∀ i, (F.obj i).IsQuasicoherent ∧ (F.obj i).IsFinite ∧
        (F.obj i).IsFinitePresentation) ∧
        ∀ i j (h : i ≤ j), AlgebraSheaf.Hom.IsSurjective (F.map (homOfLE h))
```

## Tag 0817, a lemma

[Tag 0817](https://stacks.math.columbia.edu/tag/0817) in the Stacks Project.

**`Stacks.AlgebraicGeometry.FiniteSubalgebras.isFiltered_finiteSubalgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteSubalgebra/Basic.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FiniteSubalgebra/Basic.lean#L195). The attribute's comment: “part (1), the directedness assertion: the finite quasi-coherent subalgebras of an integral quasi-coherent algebra sheaf form a filtered category; no hypothesis on X”.

> **[Stacks, Tag 0817], the directedness assertion.**  The finite quasi-coherent subalgebras of
> an integral quasi-coherent sheaf of commutative `𝒪_X`-algebras form a filtered category.
>
> No hypothesis on `X` is used: not quasi-compactness, not quasi-separatedness, not Noetherian and
> not affineness.  This is
> `Stacks.AlgebraicGeometry.FiniteTypeSubalgebraFiltered.isFiltered_finiteTypeSubalgebra`,
> which is unconditional, transported along `equivFiniteTypeSubalgebra`.
>
> This is one of the two declarations covering part (1) of the tag; the other is
> `nonempty_isColimit_finiteSubalgebraCocone`.

```lean
theorem isFiltered_finiteSubalgebra (A : AlgebraSheaf X) (hAqc : AlgebraSheaf.IsQuasicoherent A)
    (hAint : A.IsIntegral) : IsFiltered (FiniteSubalgebra A)
```

**`Stacks.AlgebraicGeometry.FiniteSubalgebras.nonempty_isColimit_finiteSubalgebraCocone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteSubalgebra/Basic.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FiniteSubalgebra/Basic.lean#L262). The attribute's comment: “part (1), the colimit assertion: an integral quasi-coherent algebra sheaf is the colimit of its finite quasi-coherent subalgebras, for X quasi-compact and quasi-separated”.

> **Stacks Project, Tag 0817, the colimit assertion of part (1).**  On a quasi-compact and
> quasi-separated scheme an integral quasi-coherent sheaf of commutative `𝒪_X`-algebras is the
> colimit of the canonical diagram of all its finite quasi-coherent subalgebras, with the
> inclusions of the subobjects as the structure morphisms.
>
> For an integral algebra sheaf a finite type quasi-coherent subalgebra is finite
> ([Stacks, Tag 02JJ] on affine sections), so this is the tag 05JT form of the same statement,
> `Stacks.AlgebraicGeometry.FiniteTypeSubalgebraFiltered`'s
> `nonempty_isColimit_finiteTypeSubalgebraCocone`, transported along
> `equivFiniteTypeSubalgebra`.

```lean
theorem nonempty_isColimit_finiteSubalgebraCocone [CompactSpace X] [QuasiSeparatedSpace X]
    (A : AlgebraSheaf X) (hAqc : AlgebraSheaf.IsQuasicoherent A) (hAint : A.IsIntegral) :
    Nonempty (IsColimit (finiteSubalgebraCocone A))
```

**`Stacks.AlgebraicGeometry.Tag0817PartTwo.exists_small_index_finite_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PartTwoResidue/Complete.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PartTwoResidue/Complete.lean#L109). The attribute's comment: “part (2): A is a directed colimit of finite and finitely presented quasi-coherent algebras, for X quasi-compact and quasi-separated and A quasi-coherent and integral”.

> **Stacks Project, Tag 0817, part (2).**  On a quasi-compact and quasi-separated scheme an
> integral quasi-coherent sheaf of commutative `𝒪_X`-algebras is a directed colimit, over a nonempty
> directed preorder in the universe of the scheme, of quasi-coherent `𝒪_X`-algebras that are both
> finite and of finite presentation.
>
> Part (1) of the tag writes `A` as the colimit of its finite quasi-coherent subalgebras,
> [Stacks, Tag 086N] writes each of those as a colimit of finite finitely presented ones, and the
> two colimits are spliced by
> `Stacks.FinitelyPresentableComposition.exists_directed_index_algebraSheaf`; its presentability
> hypothesis holds along these cocones by
> `Stacks.AlgebraicGeometry.Tag0817Presentable.presentableAlong_of_isFinitePresentation`.

```lean
theorem exists_small_index_finite_finitePresentation (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X] (A : AlgebraSheaf X) (hAqc : AlgebraSheaf.IsQuasicoherent A)
    (hAint : AlgebraSheaf.IsIntegral A) :
    ∃ (I : Type u) (_ : Preorder I) (_ : Nonempty I) (_ : IsDirected I (· ≤ ·))
      (F : I ⥤ AlgebraSheaf X) (t : F ⟶ (Functor.const I).obj A)
      (_ : IsColimit (Cocone.mk A t)),
      ∀ i, AlgebraSheaf.IsQuasicoherent (F.obj i) ∧ AlgebraSheaf.IsFinite (F.obj i) ∧
        AlgebraSheaf.IsFinitePresentation (F.obj i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.23, Tag 01PD](https://stacks.math.columbia.edu/tag/01PD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
