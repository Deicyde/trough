---
declaration: section
origin: cited
lean: AlgebraicGeometry.isIso_restrict_compl_support, AlgebraicGeometry.IsAlmostBlowUpSquare, AlgebraicGeometry.supportedSectionsIdeal_ideal, AlgebraicGeometry.isAlmostBlowUpSquare_baseChange, AlgebraicGeometry.isIso_restrict_iff_le_supportedSectionsIdeal, AlgebraicGeometry.le_supportedSectionsIdeal_iff_isAlmostBlowUpSquare, AlgebraicGeometry.isFiltered_and_exists_isLimit_blowUpCone, AlgebraicGeometry.exists_isAlmostBlowUpSquare
statement: formalized
proof: formalized
---

# 38.37 Almost blow up squares and the h topology

Section 38.37 of the Stacks Project, [Tag 0EV4](https://stacks.math.columbia.edu/tag/0EV4). 14 tags here are carried by 33 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EV6, an equation

[Tag 0EV6](https://stacks.math.columbia.edu/tag/0EV6) in the Stacks Project.

**`AlgebraicGeometry.isIso_restrict_compl_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/AlmostBlowUp/IsomorphismAwayFromCenter.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/AlmostBlowUp/IsomorphismAwayFromCenter.lean#L117). The attribute's comment: “isomorphism\_away\_from\_center”.

> **Stacks Project, Tag 0EV6.** The modification of an almost blowup square is an isomorphism
> over the complement of the centre of the square.

```lean
public theorem isIso_restrict_compl_support {X X' : Scheme.{u}}
    (I : X.IdealSheafData) (b : X' ⟶ X) (hb : IsAlmostBlowUpSquare I b) :
    IsIso (b ∣_ (⟨I.supportᶜ, I.support.isClosed.isOpen_compl⟩ : X.Opens))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.IsAlmostBlowUpSquare`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AlmostBlowUp/Basic.lean#L44), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AlmostBlowUp/Basic.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AlmostBlowUp/Basic.lean#L60) (StacksFrontier): “almost\_blow\_up\_square”.
- [`AlgebraicGeometry.supportedSectionsIdeal_ideal`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/AlmostBlowUp/SupportedSections.lean#L95), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/AlmostBlowUp/SupportedSections.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/AlmostBlowUp/SupportedSections.lean#L120) (StacksFrontier): “almost\_blow\_up\_square”.

## Tag 0EV7, a lemma

[Tag 0EV7](https://stacks.math.columbia.edu/tag/0EV7) in the Stacks Project.

**`AlgebraicGeometry.isAlmostBlowUpSquare_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/BaseChange.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/BaseChange.lean#L89).

> An almost blowup square stays an almost blowup square after an arbitrary base change: the new
> centre is the inverse image of the old one and the new modification is the base change of the
> old one.

```lean
public theorem isAlmostBlowUpSquare_baseChange {X X' Y : Scheme.{u}} (I : X.IdealSheafData)
    (b : X' ⟶ X) (f : Y ⟶ X) (h : IsAlmostBlowUpSquare I b) :
    IsAlmostBlowUpSquare (I.comap f) (pullback.fst f b)
```

## Tag 0EV8, a lemma

[Tag 0EV8](https://stacks.math.columbia.edu/tag/0EV8) in the Stacks Project.

**`AlgebraicGeometry.isIso_restrict_iff_le_supportedSectionsIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/AlmostBlowUp/IsomorphismAwayFromCenter.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/AlmostBlowUp/IsomorphismAwayFromCenter.lean#L106). The attribute's comment: “(1) iff (2)”.

> **Stacks Project, Tag 0EV8.** The closed subscheme cut out by an ideal sheaf is an
> isomorphism over the complement of a closed set exactly when the ideal sheaf is contained in the
> ideal of sections supported on that set.

```lean
public theorem isIso_restrict_iff_le_supportedSectionsIdeal {X : Scheme.{u}} (Z : Set X)
    (hZ : IsClosed Z) (J : X.IdealSheafData) :
    IsIso (J.subschemeι ∣_ (⟨Zᶜ, hZ.isOpen_compl⟩ : X.Opens)) ↔
      J ≤ supportedSectionsIdeal Z
```

**`AlgebraicGeometry.le_supportedSectionsIdeal_iff_isAlmostBlowUpSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/Shrinking.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/Shrinking.lean#L117). The attribute's comment: “(2) iff (3)”.

> **Stacks Project, Tag 0EV8.** For a finitely presented closed subscheme of the modification
> of an almost blowup square, containing the blowup of the centre is equivalent to the induced
> square, with the scheme-theoretic inverse image of the centre, being again an almost blowup
> square.

```lean
public theorem le_supportedSectionsIdeal_iff_isAlmostBlowUpSquare {X X' : Scheme.{u}}
    (I : X.IdealSheafData) (b : X' ⟶ X) (h : IsAlmostBlowUpSquare I b)
    (J : X'.IdealSheafData) (hJ : FinitePresentation J.subschemeι) :
    J ≤ supportedSectionsIdeal (I.comap b).support ↔
      IsAlmostBlowUpSquare I (J.subschemeι ≫ b)
```

## Tag 0EV9, a lemma

[Tag 0EV9](https://stacks.math.columbia.edu/tag/0EV9) in the Stacks Project.

**`AlgebraicGeometry.isFiltered_and_exists_isLimit_blowUpCone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/AlmostBlowUp/BlowUpAsLimit.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/AlmostBlowUp/BlowUpAsLimit.lean#L138).

> Consider an almost blowup square with centre `I.subscheme` and modification `b : X' ⟶ X`,
> with `X` quasi-compact and quasi-separated. The closed subschemes `X'ᵢ ⊆ X'` of finite
> presentation satisfying the equivalent conditions of Tag 0EV8 — their ideal sheaves `J` are
> finitely presented with `J ≤ almostBlowUpIdeal I b`, that is, the blowup `X''` is scheme
> theoretically contained in `X'ᵢ` (condition (2)), equivalently `X'ᵢ` contains `X' ∖ E` scheme
> theoretically (condition (1), `AlgebraicGeometry.le_almostBlowUpIdeal_iff`) — form a directed
> system, and the blowup `X''` of `X` in the centre, identified by `i` over `X` with the closed
> subscheme of `X'` cut out by `almostBlowUpIdeal I b`, is its limit `X'' = lim X'ᵢ`, both as
> schemes over `X'` and as schemes.

```lean
public theorem isFiltered_and_exists_isLimit_blowUpCone [CompactSpace X] [QuasiSeparatedSpace X]
    (h : IsAlmostBlowUpSquare I b) :
    IsFiltered (FinitePresentationSubscheme (almostBlowUpIdeal I b)) ∧
      ∃ i : blowUp I ⟶ (almostBlowUpIdeal I b).subscheme, IsIso i ∧
        i ≫ (almostBlowUpIdeal I b).subschemeι ≫ b = blowUpToBase I ∧
        Nonempty (IsLimit (blowUpCone I b i)) ∧
        Nonempty (IsLimit ((Over.forget X').mapCone (blowUpCone I b i)))
```

## Tag 0EVA, a lemma

[Tag 0EVA](https://stacks.math.columbia.edu/tag/0EVA) in the Stacks Project.

**`AlgebraicGeometry.exists_isAlmostBlowUpSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/Existence.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/Existence.lean#L66).

> **Stacks Project, Tag 0EVA.** Let `X` be a quasi-compact and quasi-separated scheme and let
> `I` be a quasi-coherent ideal sheaf of finite type on `X`, cutting out a closed subscheme `Z`.
> Then there is an almost blowup square with centre `Z`, that is, a modification `b : X' ⟶ X`
> making `(I.comap b, X', Z, X)` an almost blowup square.

```lean
public theorem exists_isAlmostBlowUpSquare (X : Scheme.{u})
    [CompactSpace X] [QuasiSeparatedSpace X] (I : X.IdealSheafData)
    (hI : Scheme.IdealSheafData.IsFiniteType I) :
    ∃ (X' : Scheme.{u}) (b : X' ⟶ X), IsAlmostBlowUpSquare I b
```

## Tag 0EVB, a lemma

[Tag 0EVB](https://stacks.math.columbia.edu/tag/0EVB) in the Stacks Project.

**`AlgebraicGeometry.exists_isAlmostBlowUpSquare_closedImmersion_to_both`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/CommonRefinement.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/CommonRefinement.lean#L46).

> Let `X` be a quasi-compact and quasi-separated scheme, let `I` be a quasi-coherent ideal sheaf
> of finite type on `X`, and let `b₁ : X₁ ⟶ X` and `b₂ : X₂ ⟶ X` be the modifications of two almost
> blowup squares with centre `I`. Then there is an almost blowup square with centre `I` and
> modification `b : X' ⟶ X` together with closed immersions `i₁ : X' ⟶ X₁` and `i₂ : X' ⟶ X₂` over
> `X` for which the exceptional subscheme of `b` is the inverse image of the exceptional subscheme
> of `b₁` and of `b₂`.

```lean
public theorem exists_isAlmostBlowUpSquare_closedImmersion_to_both
    {X X₁ X₂ : Scheme.{u}} [CompactSpace X] [QuasiSeparatedSpace X]
    (I : X.IdealSheafData) (hI : Scheme.IdealSheafData.IsFiniteType I)
    (b₁ : X₁ ⟶ X) (b₂ : X₂ ⟶ X)
    (h₁ : IsAlmostBlowUpSquare I b₁) (h₂ : IsAlmostBlowUpSquare I b₂) :
    ∃ (X' : Scheme.{u}) (b : X' ⟶ X) (i₁ : X' ⟶ X₁) (i₂ : X' ⟶ X₂),
      IsAlmostBlowUpSquare I b ∧
        IsClosedImmersion i₁ ∧ IsClosedImmersion i₂ ∧
        i₁ ≫ b₁ = b ∧ i₂ ≫ b₂ = b ∧
        I.comap b = (I.comap b₁).comap i₁ ∧
        I.comap b = (I.comap b₂).comap i₂
```

## Tag 0EVC, a lemma

[Tag 0EVC](https://stacks.math.columbia.edu/tag/0EVC) in the Stacks Project.

**`AlgebraicGeometry.hasFlatAlmostBlowUpSquarePair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/Flattening.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/Flattening.lean#L203). The attribute's comment: “locally Noetherian base; the affine case of the flatness half of [Stacks, Tag 0815] carried as the hypothesis `AlgebraicGeometry.AffineChartFlatteningCentre`, inherited from the library's form of [Stacks, Tag 081R]”.

> **Stacks Project, Tag 0EVC.** Let `Y` be a quasi-compact and quasi-separated scheme, let `X`
> be a scheme of finite presentation over `Y`, and let `V ⊆ Y` be a quasi-compact open. Then there
> is a diagram as in the tag: two almost blowup squares, over `Y` with a centre disjoint from `V`
> and over `X` with the inverse-image centre, whose lower and top squares are cartesian
> (`AlgebraicGeometry.lowerSquareIso`, `AlgebraicGeometry.topSquareIso`) and whose relative
> morphism `X' ⟶ Y'` is flat and of finite presentation.
>
> The flattening centre comes from
> `AlgebraicGeometry.exists_isAdmissibleBlowup_flat_strictTransform`, the library's form of Stacks tag
> 081R, and two things are carried beyond the tag's own hypotheses. The base is assumed locally
> Noetherian: this is the case the Stacks proof calls immediate, the general case being reduced to
> it by absolute Noetherian approximation, which is not done here. And the affine case of the
> flatness half of Stacks tag 0815 is carried as
> `AlgebraicGeometry.AffineChartFlatteningCentre f X.unitModule V`, exactly as that form of
> tag 081R carries it. The tag's remaining hypothesis that `X_V ⟶ V` be flat is not assumed
> separately, because in the source it enters only through that affine case; so the statement below
> is a generalization in that respect.

```lean
public theorem hasFlatAlmostBlowUpSquarePair [IsLocallyNoetherian Y] [CompactSpace Y]
    [QuasiSeparatedSpace Y] (f : X ⟶ Y) (hf : FinitePresentation f) (V : Y.Opens)
    (hV : IsCompact (V : Set Y)) (H : AffineChartFlatteningCentre f X.unitModule V) :
    HasFlatAlmostBlowUpSquarePair f V
```

**`AlgebraicGeometry.hasFlatAlmostBlowUpSquarePair_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/FlatteningApproximation.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/FlatteningApproximation.lean#L288).

> **[Stacks, Tag 0EVC].** Let `Y` be a quasi-compact and quasi-separated scheme, let `X` be a
> scheme of finite presentation over `Y`, and let `V ⊆ Y` be a quasi-compact open such that
> `X_V ⟶ V` is flat. Then there is a diagram as in the tag: two almost blowup squares, over `Y`
> with a centre disjoint from `V` and over `X` with the inverse-image centre, whose lower and top
> squares are cartesian (`AlgebraicGeometry.lowerSquareIso`,
> `AlgebraicGeometry.topSquareIso`) and whose relative morphism `X' ⟶ Y'` is flat and of finite
> presentation.
>
> The general case is reduced to the locally Noetherian case
> `AlgebraicGeometry.hasFlatAlmostBlowUpSquarePair` by absolute Noetherian approximation; see the
> module docstring.

```lean
public theorem hasFlatAlmostBlowUpSquarePair_of_flat {X Y : Scheme.{u}}
    [CompactSpace Y] [QuasiSeparatedSpace Y] (f : X ⟶ Y) (hf : FinitePresentation f)
    (V : Y.Opens) (hV : IsCompact (V : Set Y)) (hflat : Flat (pullback.snd f V.ι)) :
    HasFlatAlmostBlowUpSquarePair f V
```

**`AlgebraicGeometry.hasFlatAlmostBlowUpSquarePair_of_affineCase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/FlatteningFlatModel.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/FlatteningFlatModel.lean#L289). The attribute's comment: “the conclusion in full, under exactly the source's hypotheses and with no Noetherian hypothesis on the base: the affine case of the flatness assertion of [Stacks, Tag 0815] that the proof consumes is `AlgebraicGeometry.AffineChartFlatteningCentreUnderSourceHypotheses.of_compactSpace`, itself proved from [Stacks, Tag 0811]”.

> **Stacks Project, Tag 0EVC.** Let `Y` be a quasi-compact and quasi-separated scheme, let
> `f : X ⟶ Y` be of finite presentation and let `V ⊆ Y` be a quasi-compact open such that
> `X_V ⟶ V` is flat. Then there is a diagram as in the tag: two almost blowup squares, over `Y`
> with a centre disjoint from `V` and over `X` with the inverse-image centre, whose lower and top
> squares are cartesian (`AlgebraicGeometry.lowerSquareIso`, `AlgebraicGeometry.topSquareIso`) and
> whose relative morphism `X' ⟶ Y'` is flat and of finite presentation.
>
> Every hypothesis of the source is present, with no Noetherian hypothesis on `Y`: the Noetherian
> case is `AlgebraicGeometry.hasFlatAlmostBlowUpSquarePair_of_flat`, run at the Noetherian model
> supplied by `AlgebraicGeometry.exists_isNoetherian_model_of_finitePresentation_of_flat` and
> pulled back along `Y ⟶ Y₀`. The affine case of the flatness assertion of
> [Stacks, Tag 0815] it consumes is
> `AlgebraicGeometry.AffineChartFlatteningCentreUnderSourceHypotheses.of_compactSpace`, itself proved
> from [Stacks, Tag 0811], which
> `AlgebraicGeometry.NoetherianAffineChartFlatteningCentre.of_affineCase` turns into the form the
> Noetherian case consumes.
>
> The tag's hypothesis that `X_V ⟶ V` be flat is essential and is present here, where
> `AlgebraicGeometry.hasFlatAlmostBlowUpSquarePair` omits it: without it the affine case cannot be
> applied at the model at all, its own hypothesis (5) being exactly that flatness.

```lean
theorem hasFlatAlmostBlowUpSquarePair_of_affineCase {X Y : Scheme.{u}} [CompactSpace Y]
    [QuasiSeparatedSpace Y] (f : X ⟶ Y) (hf : FinitePresentation f) (V : Y.Opens)
    (hV : IsCompact (V : Set Y)) (hflat : Flat (f ∣_ V)) :
    HasFlatAlmostBlowUpSquarePair f V
```

## Tag 0EVD, a lemma

[Tag 0EVD](https://stacks.math.columbia.edu/tag/0EVD) in the Stacks Project.

**`AlgebraicGeometry.isPullback_of_almostBlowUpSquare_bigH`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AlmostBlowUpDescent.lean, line 905](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AlmostBlowUpDescent.lean#L905). The attribute's comment: “big h site”.

> **Stacks 0EVD.** A sheaf on the big h site over a scheme sends an almost blowup square to
> a cartesian square of sets.

```lean
public theorem isPullback_of_almostBlowUpSquare_bigH
    (B : BigHSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigHOver B S hS)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (BigHOver.topology B S hS) F)
    {X X' Z E : BigHOver B S hS}
    (b : X' ⟶ X) (z : Z ⟶ X) (p : E ⟶ X') (e : E ⟶ Z)
    (I : ((BigHOver.toScheme B S hS).obj X).IdealSheafData)
    (hb : IsAlmostBlowUpSquare I ((BigHOver.toScheme B S hS).map b))
    (hZ : Nonempty
      (Over.mk ((BigHOver.toScheme B S hS).map z) ≅
        Over.mk I.subschemeι))
    (hSquare : IsPullback
      ((BigHOver.toScheme B S hS).map e)
      ((BigHOver.toScheme B S hS).map p)
      ((BigHOver.toScheme B S hS).map z)
      ((BigHOver.toScheme B S hS).map b)) :
    IsPullback (F.map z.op) (F.map b.op) (F.map e.op) (F.map p.op)
```

**`AlgebraicGeometry.isPullback_of_almostBlowUpSquare_bigAffineH`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AlmostBlowUpDescent.lean, line 950](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AlmostBlowUpDescent.lean#L950). The attribute's comment: “big affine h site”.

> **Stacks 0EVD.** A sheaf on the big affine h site over a scheme sends an almost blowup
> square to a cartesian square of sets.

```lean
public theorem isPullback_of_almostBlowUpSquare_bigAffineH
    (B : BigHSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigAffineH B S hS)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (BigAffineH.topology B S hS) F)
    {X X' Z E : BigAffineH B S hS}
    (b : X' ⟶ X) (z : Z ⟶ X) (p : E ⟶ X') (e : E ⟶ Z)
    (I : ((BigAffineH.toScheme B S hS).obj X).IdealSheafData)
    (hb : IsAlmostBlowUpSquare I ((BigAffineH.toScheme B S hS).map b))
    (hZ : Nonempty
      (Over.mk ((BigAffineH.toScheme B S hS).map z) ≅
        Over.mk I.subschemeι))
    (hSquare : IsPullback
      ((BigAffineH.toScheme B S hS).map e)
      ((BigAffineH.toScheme B S hS).map p)
      ((BigAffineH.toScheme B S hS).map z)
      ((BigAffineH.toScheme B S hS).map b)) :
    IsPullback (F.map z.op) (F.map b.op) (F.map e.op) (F.map p.op)
```

## Tag 0EVE, a lemma

[Tag 0EVE](https://stacks.math.columbia.edu/tag/0EVE) in the Stacks Project.

**`AlgebraicGeometry.bijective_map_of_isThickening_bigH`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AlmostBlowUpDescent.lean, line 1016](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AlmostBlowUpDescent.lean#L1016). The attribute's comment: “big h site”.

> **Stacks 0EVE.** A sheaf on the big h site over a scheme restricts bijectively along a
> morphism of the site which is a thickening and of finite presentation.

```lean
public theorem bijective_map_of_isThickening_bigH
    (B : BigHSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigHOver B S hS)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (BigHOver.topology B S hS) F)
    {X X' : BigHOver B S hS} (i : X ⟶ X')
    (hi : IsThickening ((BigHOver.toScheme B S hS).map i))
    (hfp : FinitePresentation ((BigHOver.toScheme B S hS).map i)) :
    Function.Bijective (F.map i.op)
```

**`AlgebraicGeometry.bijective_map_of_isThickening_bigAffineH`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AlmostBlowUpDescent.lean, line 1036](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AlmostBlowUpDescent.lean#L1036). The attribute's comment: “big affine h site”.

> **Stacks 0EVE.** A sheaf on the big affine h site over a scheme restricts bijectively
> along a morphism of the site which is a thickening and of finite presentation.

```lean
public theorem bijective_map_of_isThickening_bigAffineH
    (B : BigHSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigAffineH B S hS)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (BigAffineH.topology B S hS) F)
    {X X' : BigAffineH B S hS} (i : X ⟶ X')
    (hi : IsThickening ((BigAffineH.toScheme B S hS).map i))
    (hfp : FinitePresentation ((BigAffineH.toScheme B S hS).map i)) :
    Function.Bijective (F.map i.op)
```

## Tag 0EVF, a proposition

[Tag 0EVF](https://stacks.math.columbia.edu/tag/0EVF) in the Stacks Project.

**`AlgebraicGeometry.BigHOver.isAffineFlatProperFinitePresentationSheaf_of_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AlmostBlowUpSheafCriterion.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AlmostBlowUpSheafCriterion.lean#L210). The attribute's comment: “only if, condition (2)”.

> **Stacks 0EVF, a sheaf satisfies condition (2).** A sheaf on the big h site over `S` satisfies
> the sheaf condition for the one-element family attached to a morphism of the site with affine
> target which is flat, proper, surjective and of finite presentation.
>
> Flatness is not used: such a morphism is an h covering all by itself, and so is every proper
> surjective morphism of finite presentation, which is the content of condition (2) of Stacks
> 0EU5.

```lean
public theorem isAffineFlatProperFinitePresentationSheaf_of_isSheaf
    (hF : Presheaf.IsSheaf (BigHOver.topology B S hS) F) :
    BigHOver.IsAffineFlatProperFinitePresentationSheaf B S hS F
```

**`AlgebraicGeometry.BigHOver.IsAffineFlatProperFinitePresentationSheaf.bijective_mapToEqualizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AlmostBlowUpSheafCriterion.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AlmostBlowUpSheafCriterion.lean#L225). The attribute's comment: “condition (2) in equalizer form”.

> **Condition (2) of Stacks 0EVF in the source's equalizer form.** Let `f : V ⟶ U` be a
> morphism of the big h category over `S` whose target has affine underlying scheme and whose
> underlying morphism of schemes is flat, proper, surjective and of finite presentation, and let
> `p₁, p₂ : W ⟶ V` complete `f` to a cartesian square, so that `W = V ×_U V`.  Then condition (2)
> says exactly that `F(U)` maps bijectively onto the equalizer of the two maps `F(V) ⟶ F(W)`.
>
> This is the form in which the source states the condition; the two are identified by
> `AlgebraicGeometry.isSheafFor_singleton_iff_bijective_mapToEqualizer`.

```lean
public theorem IsAffineFlatProperFinitePresentationSheaf.bijective_mapToEqualizer
    (hF : BigHOver.IsAffineFlatProperFinitePresentationSheaf B S hS F)
    {V U W : BigHOver B S hS} (f : V ⟶ U) (p₁ p₂ : W ⟶ V) (hW : IsPullback p₁ p₂ f f)
    (haffine : IsAffine ((BigHOver.toScheme B S hS).obj U))
    (hflat : Flat ((BigHOver.toScheme B S hS).map f))
    (hproper : IsProper ((BigHOver.toScheme B S hS).map f))
    (hsurj : Surjective ((BigHOver.toScheme B S hS).map f))
    (hfp : FinitePresentation ((BigHOver.toScheme B S hS).map f)) :
    Function.Bijective (regularTopology.mapToEqualizer F f p₁ p₂ hW.w)
```

**`AlgebraicGeometry.BigHOver.isAffineAlmostBlowUpSheaf_of_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AlmostBlowUpSheafCriterion.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AlmostBlowUpSheafCriterion.lean#L243). The attribute's comment: “only if, condition (3)”.

> **Stacks 0EVF, a sheaf satisfies condition (3).** A sheaf on the big h site over `S` sends an
> almost blowup square of the site with affine base to a cartesian square of sets.
>
> Affineness of the base is not used: this is Stacks 0EVD for an arbitrary almost blowup square of
> the site.

```lean
public theorem isAffineAlmostBlowUpSheaf_of_isSheaf
    (hF : Presheaf.IsSheaf (BigHOver.topology B S hS) F) :
    BigHOver.IsAffineAlmostBlowUpSheaf B S hS F
```

**`AlgebraicGeometry.BigHOver.zariski_and_affineFlatProperFP_and_affineAlmostBlowUp_of_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AlmostBlowUpSheafCriterion.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AlmostBlowUpSheafCriterion.lean#L261). The attribute's comment: “only if, all three conditions”.

> **Stacks 0EVF, the three conditions are necessary.** A sheaf on the big h site over `S`
> satisfies condition (1), the sheaf condition for Zariski coverings, condition (2), the sheaf
> condition for every morphism of the site with affine target which is flat, proper, surjective and
> of finite presentation, and condition (3), the cartesianness of the image of every almost blowup
> square of the site with affine base.
>
> The converse is
> `AlgebraicGeometry.BigHOver.isSheaf_of_zariski_and_affineFlatProperFP_and_affineAlmostBlowUp`, and
> the two together are
> `AlgebraicGeometry.BigHOver.isSheaf_iff_zariski_and_affineFlatProperFP_and_affineAlmostBlowUp`,
> both in `StacksFrontier.AlgebraicGeometry.Topologies.HTopology.AlmostBlowUpSheafInduction`.

```lean
public theorem zariski_and_affineFlatProperFP_and_affineAlmostBlowUp_of_isSheaf
    (hF : Presheaf.IsSheaf (BigHOver.topology B S hS) F) :
    BigHOver.IsZariskiSheaf B S hS F ∧
      BigHOver.IsAffineFlatProperFinitePresentationSheaf B S hS F ∧
      BigHOver.IsAffineAlmostBlowUpSheaf B S hS F
```

**`AlgebraicGeometry.BigHOver.isSheaf_of_zariski_and_affineFlatProperFP_and_affineAlmostBlowUp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AlmostBlowUpSheafInduction.lean, line 541](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AlmostBlowUpSheafInduction.lean#L541).

> **Stacks 0EVF, the three conditions are sufficient.** A presheaf of sets on the big h
> category over `S` which satisfies condition (1), the sheaf condition for Zariski coverings,
> condition (2), the sheaf condition for every morphism of the site with affine target which is
> flat, proper, surjective and of finite presentation, and condition (3), the cartesianness of the
> image of every almost blowup square of the site with affine base, is a sheaf for the h topology.

```lean
public theorem isSheaf_of_zariski_and_affineFlatProperFP_and_affineAlmostBlowUp
    (hZ : BigHOver.IsZariskiSheaf B S hS F)
    (h2 : BigHOver.IsAffineFlatProperFinitePresentationSheaf B S hS F)
    (h3 : BigHOver.IsAffineAlmostBlowUpSheaf B S hS F) :
    Presheaf.IsSheaf (BigHOver.topology B S hS) F
```

**`AlgebraicGeometry.BigHOver.isSheaf_iff_zariski_and_affineFlatProperFP_and_affineAlmostBlowUp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AlmostBlowUpSheafInduction.lean, line 557](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/AlmostBlowUpSheafInduction.lean#L557).

> **Stacks 0EVF.** A presheaf of sets on the big h category over `S` is a sheaf for the h
> topology if and only if it satisfies condition (1), the sheaf condition for Zariski coverings,
> condition (2), the sheaf condition for every morphism of the site with affine target which is
> flat, proper, surjective and of finite presentation, and condition (3), the cartesianness of the
> image of every almost blowup square of the site with affine base.

```lean
public theorem isSheaf_iff_zariski_and_affineFlatProperFP_and_affineAlmostBlowUp :
    Presheaf.IsSheaf (BigHOver.topology B S hS) F ↔
      (BigHOver.IsZariskiSheaf B S hS F ∧
        BigHOver.IsAffineFlatProperFinitePresentationSheaf B S hS F ∧
        BigHOver.IsAffineAlmostBlowUpSheaf B S hS F)
```

## Tag 0EVG, an example

[Tag 0EVG](https://stacks.math.columbia.edu/tag/0EVG) in the Stacks Project.

**`AlgebraicGeometry.isAlmostBlowUpSquare_quotient_of_pow_mul_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/PrincipalCenter.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BlowUpSquares/PrincipalCenter.lean#L321).

> **Stacks Project, Tag 0EVG.** For a finitely generated ideal `J` of `A` annihilated by a power
> of `f`, the closed immersion `Spec (A ⧸ J) ⟶ Spec A` is the modification of an almost blowup
> square whose centre is the closed subscheme cut out by `f`.

```lean
public theorem isAlmostBlowUpSquare_quotient_of_pow_mul_eq_zero (A : Type u) [CommRing A]
    (f : A) (J : Ideal A) (hJ : J.FG) (h : ∃ n : ℕ, ∀ x ∈ J, f ^ n * x = 0) :
    IsAlmostBlowUpSquare
      (Scheme.IdealSheafData.ofIdealTop
        (Ideal.map (Scheme.ΓSpecIso (.of A)).inv.hom (Ideal.span {f})))
      (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk J)))
```

## Tag 0EVH, an example

[Tag 0EVH](https://stacks.math.columbia.edu/tag/0EVH) in the Stacks Project.

**`Stacks.AlmostBlowUp.isAlmostBlowUpSquare_twoGeneratorSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/TwoGeneratorSupportedSections.lean, line 612](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/TwoGeneratorSupportedSections.lean#L612).

> **Stacks Project, Tag 0EVH.** Let `A` be a ring and `f₁, f₂ ∈ A`. The square
> ```
> E = Proj ((A/(f₁,f₂))[T₀,T₁]) ⟶ Proj (A[T₀,T₁]/(f₂T₀-f₁T₁)) = X'
>             ↓                                ↓
>      Z = Spec (A/(f₁,f₂))      ⟶       Spec A = X
> ```
> is an almost blowup square: it is cartesian, so that `E = b⁻¹(Z)`; its lower arrow is, over
> `Spec A`, the closed subscheme cut out by `(f₁,f₂)`; and the right-hand arrow `b` with that centre
> satisfies the conditions of an almost blowup square.

```lean
theorem isAlmostBlowUpSquare_twoGeneratorSquare :
    letI := (twoGeneratorSquare A f₁ f₂).modificationGraded
    IsPullback (exceptionalToModification A f₁ f₂) (exceptionalToCenter A f₁ f₂)
        (modificationToBase A f₁ f₂) (centerToBase A f₁ f₂) ∧
      Nonempty (Over.mk (centerToBase A f₁ f₂) ≅
        Over.mk (centerIdealSheaf A f₁ f₂).subschemeι) ∧
      AlgebraicGeometry.IsAlmostBlowUpSquare (centerIdealSheaf A f₁ f₂)
        (modificationToBase A f₁ f₂)
```

## Tag 0EVI, a lemma

[Tag 0EVI](https://stacks.math.columbia.edu/tag/0EVI) in the Stacks Project.

**`AlgebraicGeometry.BigHOver.isSheaf_iff_zariski_and_flatProper_and_generatorSquares`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpReduction.lean, line 786](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpReduction.lean#L786).

> **Stacks 0EVI.** A presheaf of sets on the big h category over `S` is a sheaf for the h
> topology if and only if it satisfies condition (1), the sheaf condition for Zariski coverings,
> condition (2), the sheaf condition for every morphism of the site with affine target which is
> flat, proper, surjective and of finite presentation, condition (3), cartesianness of the image
> of every almost blowup square of the site with affine base and the shape of Example 0EVG, and
> condition (4), the same for the shape of Example 0EVH.
>
> The sufficiency direction is the sufficiency direction of Stacks 0EVF,
> `AlgebraicGeometry.affineAlmostBlowUpHSheafCriterion`, applied after the reduction of its
> condition (3) to the two shapes, `AlgebraicGeometry.generatorAlmostBlowUpSquaresSuffice`.
> Condition (2) in the source's equalizer form is
> `AlgebraicGeometry.BigHOver.IsAffineFlatProperFinitePresentationSheaf.bijective_mapToEqualizer`.

```lean
theorem isSheaf_iff_zariski_and_flatProper_and_generatorSquares
    (B : BigHSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigHOver B S hS)ᵒᵖ ⥤ Type v) :
    Presheaf.IsSheaf (BigHOver.topology B S hS) F ↔
      (BigHOver.IsZariskiSheaf B S hS F ∧
        BigHOver.IsAffineFlatProperFinitePresentationSheaf B S hS F ∧
        BigHOver.IsOneGeneratorAlmostBlowUpSheaf B S hS F ∧
        BigHOver.IsTwoGeneratorAlmostBlowUpSheaf B S hS F)
```

**`AlgebraicGeometry.BigHOver.isSheaf_iff_generatorAlmostBlowUpConditions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpSheafCharacterization.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpSheafCharacterization.lean#L52).

> **Stacks 0EVI.** A presheaf of sets on the big h category over `S` is a sheaf for the h
> topology if and only if it is a Zariski sheaf, satisfies the sheaf condition for every flat proper
> surjection of finite presentation of the site onto an affine object, and sends the almost blowup
> squares of the site of the shapes of Examples 0EVG and 0EVH to cartesian squares of sets.

```lean
public theorem isSheaf_iff_generatorAlmostBlowUpConditions :
    Presheaf.IsSheaf (BigHOver.topology B S hS) F ↔
      (IsZariskiSheaf B S hS F ∧ IsAffineFlatProperFinitePresentationSheaf B S hS F ∧
        IsOneGeneratorAlmostBlowUpSheaf B S hS F ∧ IsTwoGeneratorAlmostBlowUpSheaf B S hS F)
```

**`AlgebraicGeometry.BigHOver.isOneGeneratorAlmostBlowUpSheaf_of_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpSheafCriterion.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpSheafCriterion.lean#L245). The attribute's comment: “only if, condition (3)”.

> **Stacks 0EVI, a sheaf satisfies condition (3).** A sheaf on the big h site over `S` sends an
> almost blowup square of the site of the shape of Example 0EVG to a cartesian square of sets.
>
> Neither the shape nor affineness of the base is used: this is Stacks 0EVD for an arbitrary
> almost blowup square of the site.

```lean
public theorem isOneGeneratorAlmostBlowUpSheaf_of_isSheaf
    (hF : Presheaf.IsSheaf (BigHOver.topology B S hS) F) :
    BigHOver.IsOneGeneratorAlmostBlowUpSheaf B S hS F
```

**`AlgebraicGeometry.BigHOver.isTwoGeneratorAlmostBlowUpSheaf_of_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpSheafCriterion.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpSheafCriterion.lean#L257). The attribute's comment: “only if, condition (4)”.

> **Stacks 0EVI, a sheaf satisfies condition (4).** A sheaf on the big h site over `S` sends an
> almost blowup square of the site of the shape of Example 0EVH to a cartesian square of sets.
>
> Neither the shape nor affineness of the base is used: this is Stacks 0EVD for an arbitrary
> almost blowup square of the site.

```lean
public theorem isTwoGeneratorAlmostBlowUpSheaf_of_isSheaf
    (hF : Presheaf.IsSheaf (BigHOver.topology B S hS) F) :
    BigHOver.IsTwoGeneratorAlmostBlowUpSheaf B S hS F
```

**`AlgebraicGeometry.BigHOver.zariski_and_affineFlatProperFP_and_generatorSquares_of_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpSheafCriterion.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpSheafCriterion.lean#L269). The attribute's comment: “only if, all four conditions”.

> **Stacks 0EVI, the necessity of all four conditions.** A sheaf on the big h site over `S` is a
> sheaf for the Zariski topology, satisfies the equalizer condition for every morphism of the site
> with affine target which is flat, proper, surjective and of finite presentation, and sends an
> almost blowup square of the shape of Example 0EVG, respectively of Example 0EVH, to a cartesian
> square of sets.

```lean
public theorem zariski_and_affineFlatProperFP_and_generatorSquares_of_isSheaf
    (hF : Presheaf.IsSheaf (BigHOver.topology B S hS) F) :
    BigHOver.IsZariskiSheaf B S hS F ∧
      BigHOver.IsAffineFlatProperFinitePresentationSheaf B S hS F ∧
      BigHOver.IsOneGeneratorAlmostBlowUpSheaf B S hS F ∧
      BigHOver.IsTwoGeneratorAlmostBlowUpSheaf B S hS F
```

## Tag 0EX9, a lemma

[Tag 0EX9](https://stacks.math.columbia.edu/tag/0EX9) in the Stacks Project.

**`AlgebraicGeometry.BigHOver.isStackInGroupoids_iff_generatorSquares`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpStackCharacterization.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpStackCharacterization.lean#L69). The attribute's comment: “with condition (2) in its descent form: the source's literal condition (2) is false for h stacks, see `AlgebraicGeometry.BigHOver.IsAffineFlatProperFinitePresentationDescent`”.

> **Stacks 0EX9.** A category fibred over the big h category over `S` is a stack in groupoids
> for the h topology if and only if it is a stack in groupoids for the Zariski topology, has
> effective descent along every surjective flat proper morphism of finite presentation onto an
> affine object of the site, and has `𝒮_X ⟶ 𝒮_Z ×_{𝒮_E} 𝒮_{X'}` an equivalence for every almost
> blowup square of the site with affine base of the shape of Example 0EVG or of Example 0EVH.
>
> Condition (2) is in its descent form: the source's literal condition (2), equivalence onto the
> two-fibre product, is false for h stacks, as recorded in the module documentation.  Conditions (1)
> and (3) are the source's.

```lean
public theorem isStackInGroupoids_iff_generatorSquares :
    p.IsStackInGroupoids.{u + 1} (BigHOver.topology B S hS) ↔
      IsZariskiStackInGroupoids B S hS p ∧ IsAffineFlatProperFinitePresentationDescent B S hS p ∧
        IsOneGeneratorAlmostBlowUpStack B S hS p ∧ IsTwoGeneratorAlmostBlowUpStack B S hS p
```

**`AlgebraicGeometry.BigHOver.isZariskiStackInGroupoids_of_isStackInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpStackCriterion.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpStackCriterion.lean#L342). The attribute's comment: “only if, condition (1)”.

> **Stacks 0EX9, necessity of condition (1).** A category fibred in groupoids over the big h
> category over `S` which is a stack in groupoids for the h topology is a stack in groupoids for the
> Zariski topology.
>
> The Zariski topology on `(Sch/S)_h` is coarser than the h topology,
> `AlgebraicGeometry.BigHOver.zariskiTopology_le_topology`, and the conditions of Stacks 02ZI are
> indexed by the covering families of the topology.

```lean
public theorem isZariskiStackInGroupoids_of_isStackInGroupoids
    (hp : p.IsStackInGroupoids.{u + 1} (BigHOver.topology B S hS)) :
    BigHOver.IsZariskiStackInGroupoids B S hS p
```

**`AlgebraicGeometry.BigHOver.isAffineFlatProperFinitePresentationDescent_of_isStackInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpStackCriterion.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpStackCriterion.lean#L393). The attribute's comment: “only if, condition (2) in its descent form”.

> **Stacks 0EX9, necessity of condition (2) in its descent form.** A category fibred in
> groupoids over the big h category over `S` which is a stack in groupoids for the h topology has
> effective descent, with descent of morphisms, along every surjective flat proper morphism of finite
> presentation onto an affine object of the site.
>
> Flatness and affineness of the target are not used:
> `AlgebraicGeometry.BigHOver.isEquivalence_toDescentData_singleton_of_isStackInGroupoids` holds for
> every proper surjection of finite presentation, such a morphism being an h covering by itself.

```lean
public theorem isAffineFlatProperFinitePresentationDescent_of_isStackInGroupoids [p.IsFibered]
    (hp : p.IsStackInGroupoids.{u + 1} (BigHOver.topology B S hS)) :
    IsAffineFlatProperFinitePresentationDescent B S hS p
```

**`AlgebraicGeometry.BigHOver.isOneGeneratorAlmostBlowUpStack_of_isStackInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpStackNecessity.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpStackNecessity.lean#L152). The attribute's comment: “only if, condition (3) for the shape of Example 0EVG”.

> **Stacks 0EX9, necessity of condition (3) for the shape of Example 0EVG.**  A stack in
> groupoids for the h topology satisfies condition (3) for the squares of Example 0EVG; this is
> `AlgebraicGeometry.BigHOver.isEquivalence_twoFibreProductComparison_of_isStackInGroupoids`, which
> needs neither the affineness of the base nor the shape.

```lean
public theorem isOneGeneratorAlmostBlowUpStack_of_isStackInGroupoids [p.IsFibered]
    (hp : p.IsStackInGroupoids.{u + 1} (BigHOver.topology B S hS)) :
    IsOneGeneratorAlmostBlowUpStack B S hS p
```

**`AlgebraicGeometry.BigHOver.isTwoGeneratorAlmostBlowUpStack_of_isStackInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpStackNecessity.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpStackNecessity.lean#L163). The attribute's comment: “only if, condition (3) for the shape of Example 0EVH”.

> **Stacks 0EX9, necessity of condition (3) for the shape of Example 0EVH.**  A stack in
> groupoids for the h topology satisfies condition (3) for the squares of Example 0EVH; this is
> `AlgebraicGeometry.BigHOver.isEquivalence_twoFibreProductComparison_of_isStackInGroupoids`, which
> needs neither the affineness of the base nor the shape.

```lean
public theorem isTwoGeneratorAlmostBlowUpStack_of_isStackInGroupoids [p.IsFibered]
    (hp : p.IsStackInGroupoids.{u + 1} (BigHOver.topology B S hS)) :
    IsTwoGeneratorAlmostBlowUpStack B S hS p
```

**`AlgebraicGeometry.BigHOver.isStackInGroupoids_of_generatorSquares`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpStackSufficiency.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/GeneratorAlmostBlowUpStackSufficiency.lean#L171). The attribute's comment: “if, with condition (2) in its descent form”.

> **Stacks 0EX9, the sufficiency direction.**  A category fibred in groupoids over the big h
> category over `S` which
>
> 1. is a stack in groupoids for the Zariski topology,
> 2. has effective descent, with descent of morphisms, along every surjective flat proper morphism
>    of finite presentation `X ⟶ Y` of the site with `Y` affine: the functor from `𝒮_Y` to the
>    descent data relative to `{X ⟶ Y}` is an equivalence, and
> 3. has `𝒮_X ⟶ 𝒮_Z ×_{𝒮_E} 𝒮_{X'}` an equivalence for every almost blow up square of the site of
>    the shape of Example 0EVG or of Example 0EVH
>
> is a stack in groupoids for the h topology.
>
> Conditions (1) and (3) are those of the source.  Condition (2) is the source's condition (2) with
> the two-fibre product `𝒮_X ×_{𝒮_{X ×_Y X}} 𝒮_X` replaced by the category of descent data, which
> adds the cocycle condition over `X ×_Y X ×_Y X`: the literal condition fails for every h stack with
> a nontrivial automorphism over an affine object, by the fold-map computation in the module
> documentation of
> `StacksFrontier.AlgebraicGeometry.Topologies.HTopology.GeneratorAlmostBlowUpStackCriterion`, and the
> descent form is what the source's proof uses.  The three hypotheses are those of the sheaf-level
> criterion of Stacks 0EVI that the proof of the source applies, read for a category fibred in
> groupoids: the Zariski one is the topology condition (1) of 0EVI quantifies over, and the descent
> along `{X ⟶ Y}` and the two equivalences range over the morphisms and squares conditions (2), (3)
> and (4) of 0EVI range over.
>
> The proof runs Stacks 0EVI on the two auxiliary presheaves of sets on the slice `(Sch/S)_h / U`
> that the source builds out of `𝒮`: the presheaf of morphisms between two objects of the fibre over
> `U`, whose sheaf property is
> `AlgebraicGeometry.BigHOver.isMorSheaf_of_generatorSquares`, and the presheaf of solutions of a
> descent problem, whose sheaf property is
> `AlgebraicGeometry.BigHOver.nonempty_descentSolution_id`.  Both are run through
> `AlgebraicGeometry.BigHOver.of_localOnGenerators`.

```lean
public theorem isStackInGroupoids_of_generatorSquares
    (h1 : IsZariskiStackInGroupoids B S hS p)
    (h2 : IsAffineFlatProperFinitePresentationDescent B S hS p)
    (h3 : IsOneGeneratorAlmostBlowUpStack B S hS p)
    (h4 : IsTwoGeneratorAlmostBlowUpStack B S hS p) :
    p.IsStackInGroupoids.{u + 1} (BigHOver.topology B S hS)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.37, Tag 0EV4](https://stacks.math.columbia.edu/tag/0EV4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
