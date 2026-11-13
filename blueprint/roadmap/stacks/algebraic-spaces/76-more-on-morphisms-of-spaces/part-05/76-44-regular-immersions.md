---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.property_on_all_etale_charts_iff_exists_atlas, AlgebraicGeometry.Space.property_on_all_etale_charts_iff_of_schemes, AlgebraicGeometry.Space.IsKoszulRegularImmersion, AlgebraicGeometry.Space.IsH1RegularImmersion, AlgebraicGeometry.Space.IsQuasiRegularImmersion, AlgebraicGeometry.Space.isH1RegularImmersion_of_isKoszulRegularImmersion, AlgebraicGeometry.Space.isQuasiRegularImmersion_of_isH1RegularImmersion, AlgebraicGeometry.Space.isKoszulRegularImmersion_tfae
statement: formalized
proof: formalized
---

# 76.44 Regular immersions

Section 76.44 of the Stacks Project, [Tag 06BL](https://stacks.math.columbia.edu/tag/06BL). 10 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06BM, a lemma

[Tag 06BM](https://stacks.math.columbia.edu/tag/06BM) in the Stacks Project.

**`AlgebraicGeometry.Space.property_on_all_etale_charts_iff_exists_atlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RegularImmersion.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RegularImmersion.lean#L134). The attribute's comment: “equivalence of all charts and one surjective chart”.

> **Stacks 06BM, the equivalence of conditions (1) and (2).** For a property `P` of
> scheme morphisms which is étale local on the target and a representable morphism `f` of
> algebraic spaces over `S`, the projection of the represented fibre product has `P` over
> every étale scheme chart of the target if and only if it has `P` over some surjective étale
> chart.

```lean
theorem property_on_all_etale_charts_iff_exists_atlas (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (P : MorphismProperty Scheme.{u})
    [P.IsLocalAtTarget Scheme.etalePrecoverage]
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (_hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f) :
    (∀ (V : BigFppfOver B S hS) (q : yoneda.obj V ⟶ Y),
      (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf q →
      P ((BigFppfOver.toScheme B S hS).map (hf.snd q))) ↔
    (∃ (V : BigFppfOver B S hS) (q : yoneda.obj V ⟶ Y),
      (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf q ∧
      (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf q ∧
      P ((BigFppfOver.toScheme B S hS).map (hf.snd q)))
```

**`AlgebraicGeometry.Space.property_on_all_etale_charts_iff_of_schemes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RegularImmersion.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RegularImmersion.lean#L222). The attribute's comment: “comparison when both spaces are schemes”.

> **Stacks 06BM, the comparison with the scheme-theoretic property.** When the source and
> target of a representable morphism of algebraic spaces over `S` are representable, the
> condition of Stacks 06BM on all étale charts holds exactly when the morphism of schemes
> they represent has the property.

```lean
theorem property_on_all_etale_charts_iff_of_schemes (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (P : MorphismProperty Scheme.{u})
    [P.IsLocalAtTarget Scheme.etalePrecoverage]
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} [X.IsRepresentable] [Y.IsRepresentable]
    (f : X ⟶ Y) (hf : yoneda.relativelyRepresentable f) :
    (∀ (W : BigFppfOver B S hS) (q : yoneda.obj W ⟶ Y),
      (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf q →
      P ((BigFppfOver.toScheme B S hS).map (hf.snd q))) ↔
    P ((BigFppfOver.toScheme B S hS).map
      (yoneda.preimage (X.reprW.hom ≫ f ≫ Y.reprW.inv)))
```

## Tag 06BN, a definition

[Tag 06BN](https://stacks.math.columbia.edu/tag/06BN) in the Stacks Project.

**`AlgebraicGeometry.Space.IsKoszulRegularImmersion`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RegularImmersion.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RegularImmersion.lean#L268). The attribute's comment: “part (1): Koszul-regular immersion”.

> **Stacks 06BN, part (1).** A representable morphism of algebraic spaces over `S` is a
> *Koszul-regular immersion* when its base change to every étale scheme chart of the target
> is a Koszul-regular immersion of schemes.

```lean
abbrev IsKoszulRegularImmersion (i : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.IsH1RegularImmersion`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RegularImmersion.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RegularImmersion.lean#L282). The attribute's comment: “part (2): H₁-regular immersion”.

> **Stacks 06BN, part (2).** A representable morphism of algebraic spaces over `S` is an
> *`H₁`-regular immersion* when its base change to every étale scheme chart of the target is
> an `H₁`-regular immersion of schemes.

```lean
abbrev IsH1RegularImmersion (i : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.IsQuasiRegularImmersion`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RegularImmersion.lean, line 296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RegularImmersion.lean#L296). The attribute's comment: “part (3): quasi-regular immersion”.

> **Stacks 06BN, part (3).** A representable morphism of algebraic spaces over `S` is a
> *quasi-regular immersion* when its base change to every étale scheme chart of the target is
> a quasi-regular immersion of schemes.

```lean
abbrev IsQuasiRegularImmersion (i : X ⟶ Y) : Prop
```

## Tag 06BP, a lemma

[Tag 06BP](https://stacks.math.columbia.edu/tag/06BP) in the Stacks Project.

**`AlgebraicGeometry.Space.isH1RegularImmersion_of_isKoszulRegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionImplications.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionImplications.lean#L71). The attribute's comment: “Koszul-regular implies H₁-regular”.

> **Stacks tag 06BP, the first implication.**  A Koszul-regular immersion of algebraic spaces
> over `S` is an `H₁`-regular immersion:  degree `1` is a positive degree, so the condition on each
> étale chart becomes weaker.

```lean
theorem isH1RegularImmersion_of_isKoszulRegularImmersion (i : Z ⟶ X)
    (h : IsKoszulRegularImmersion B S hS i) : IsH1RegularImmersion B S hS i
```

**`AlgebraicGeometry.Space.isQuasiRegularImmersion_of_isH1RegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionImplications.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionImplications.lean#L81). The attribute's comment: “H₁-regular implies quasi-regular”.

> **Stacks tag 06BP, the second implication.**  An `H₁`-regular immersion of algebraic spaces
> over `S` is a quasi-regular immersion.

```lean
theorem isQuasiRegularImmersion_of_isH1RegularImmersion (i : Z ⟶ X)
    (h : IsH1RegularImmersion B S hS i) : IsQuasiRegularImmersion B S hS i
```

## Tag 09RW, a lemma

[Tag 09RW](https://stacks.math.columbia.edu/tag/09RW) in the Stacks Project.

**`AlgebraicGeometry.Space.isKoszulRegularImmersion_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionImplications.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionImplications.lean#L109).

> **Stacks tag 09RW.**  For an immersion of algebraic spaces over `S` into a locally Noetherian
> algebraic space, Koszul-regularity, `H₁`-regularity and quasi-regularity agree.

```lean
theorem isKoszulRegularImmersion_tfae (_hZ : IsAlgebraicSpace B S hS Z)
    (hX : IsAlgebraicSpace B S hS X) (i : Z ⟶ X) (_hi : IsImmersion B S hS i)
    (hnoeth : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsLocallyNoetherian T)) :
    List.TFAE
      [IsKoszulRegularImmersion B S hS i,
        IsH1RegularImmersion B S hS i,
        IsQuasiRegularImmersion B S hS i]
```

## Tag 09RX, a lemma

[Tag 09RX](https://stacks.math.columbia.edu/tag/09RX) in the Stacks Project.

**`AlgebraicGeometry.Space.isKoszulRegularImmersion_pullback_snd_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RegularImmersionFlatBaseChange.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RegularImmersionFlatBaseChange.lean#L232). The attribute's comment: “koszul”.

> **Stacks 09RX, the Koszul-regular clause.** The base change `Z ×_X X' ⟶ X'` of a
> Koszul-regular immersion `i : Z ⟶ X` of algebraic spaces over `S` along a flat morphism
> `g : X' ⟶ X` is a Koszul-regular immersion.

```lean
theorem isKoszulRegularImmersion_pullback_snd_of_isFlat (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {Z X X' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (i : Z ⟶ X) (g : X' ⟶ X) (hg : IsFlat B S hS g)
    (hi : IsKoszulRegularImmersion B S hS i) :
    IsKoszulRegularImmersion B S hS (pullback.snd i g)
```

**`AlgebraicGeometry.Space.isH1RegularImmersion_pullback_snd_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RegularImmersionFlatBaseChange.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RegularImmersionFlatBaseChange.lean#L272). The attribute's comment: “h1”.

> **Stacks 09RX, the `H₁`-regular clause.** The base change `Z ×_X X' ⟶ X'` of an
> `H₁`-regular immersion `i : Z ⟶ X` of algebraic spaces over `S` along a flat morphism
> `g : X' ⟶ X` is an `H₁`-regular immersion.

```lean
theorem isH1RegularImmersion_pullback_snd_of_isFlat (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {Z X X' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (i : Z ⟶ X) (g : X' ⟶ X) (hg : IsFlat B S hS g)
    (hi : IsH1RegularImmersion B S hS i) :
    IsH1RegularImmersion B S hS (pullback.snd i g)
```

**`AlgebraicGeometry.Space.isQuasiRegularImmersion_pullback_snd_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RegularImmersionFlatBaseChange.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RegularImmersionFlatBaseChange.lean#L313). The attribute's comment: “quasi”.

> **Stacks 09RX, the quasi-regular clause.** The base change `Z ×_X X' ⟶ X'` of a
> quasi-regular immersion `i : Z ⟶ X` of algebraic spaces over `S` along a flat morphism
> `g : X' ⟶ X` is a quasi-regular immersion.

```lean
theorem isQuasiRegularImmersion_pullback_snd_of_isFlat (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {Z X X' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (i : Z ⟶ X) (g : X' ⟶ X) (hg : IsFlat B S hS g)
    (hi : IsQuasiRegularImmersion B S hS i) :
    IsQuasiRegularImmersion B S hS (pullback.snd i g)
```

## Tag 09RY, a lemma

[Tag 09RY](https://stacks.math.columbia.edu/tag/09RY) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiRegularImmersion_iff_conormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/QuasiRegularConormalCriterion.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/QuasiRegularConormalCriterion.lean#L81). The attribute's comment: “the whole statement: an immersion of algebraic spaces is quasi-regular iff it is locally of finite presentation, its conormal sheaf is finite locally free, and the map of 09RQ from the symmetric algebra on the conormal sheaf is an isomorphism in every degree, for every symmetric algebra”.

> **Stacks Project, Tag 09RY.**  An immersion `i : Z ⟶ X` of algebraic spaces is a
> quasi-regular immersion if and only if (1) it is locally of finite presentation, (2) its conormal
> sheaf `𝒞_{Z/X}` is finite locally free, and (3) the canonical map
> `Sym^*(𝒞_{Z/X}) ⟶ 𝒞_{Z/X,*}` of Stacks 09RQ is an isomorphism in every degree, for every
> symmetric algebra `Sym^*(𝒞_{Z/X})` on the conormal sheaf.
>
> The proof reduces to the closed factorisation `Z ⟶ X ∖ ∂Z` of Stacks 04CE and its base changes to
> the étale charts of `X ∖ ∂Z`, where the case of schemes, Stacks 063M, is run on the sections of
> the conormal algebra over affine charts; see the module documentation.

```lean
theorem isQuasiRegularImmersion_iff_conormal (hX : IsAlgebraicSpace B S hS X₀)
    (hZ : IsAlgebraicSpace B S hS Z₀) (i : Z₀ ⟶ X₀) (hi : IsImmersion B S hS i) :
    IsQuasiRegularImmersion B S hS i ↔
      IsLocallyOfFinitePresentation B S hS i ∧
        SheafOfModules.IsFiniteLocallyFreeOnSite (conormalModuleOfImmersion B S hS hX hZ i hi) ∧
        ∀ (A : SheafOfModules.GradedAlgebra.{u, u}
            (structureRingSheaf B S hS (⟨Z₀, hZ⟩ : AlgebraicSpaces B S hS)))
          (ι : (conormalAlgebraOfImmersion B S hS hX hZ i hi).piece 1 ⟶ A.piece 1)
          (hA : SheafOfModules.GradedAlgebra.IsSymmetricAlgebra A ι) (n : ℤ),
          IsIso ((symmetricAlgebraToConormalAlgebraOfImmersion B S hS hX hZ i hi A ι hA).app
            n)
```

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_isQuasiRegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RegularImmersion.lean, line 359](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RegularImmersion.lean#L359). The attribute's comment: “the direction out of quasi-regularity, condition (1) only: a quasi-regular immersion of algebraic spaces is locally of finite presentation. Conditions (2) and (3) and the converse are not transported, because the case of schemes, Tag 063M, is itself carried only as conditions (1) and (2) out of quasi-regularity”.

> **Stacks 09RY, condition (1) in the direction out of quasi-regularity.** A quasi-regular
> immersion of algebraic spaces over `S` is locally of finite presentation.
>
> Each represented base change of `i` to an étale scheme chart of the target is a quasi-regular
> immersion of schemes, hence locally of finite presentation by the case of schemes
> [Stacks, Tag 063M]; local finite presentation is étale local on the source and target
> [Stacks, Tag 04R3], so those chart conditions are the local finite presentation of `i`.

```lean
theorem isLocallyOfFinitePresentation_of_isQuasiRegularImmersion
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {Z X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hZ : IsAlgebraicSpace B S hS Z)
    (hX : IsAlgebraicSpace B S hS X) (i : Z ⟶ X)
    (_hIm : IsImmersion B S hS i) (h : IsQuasiRegularImmersion B S hS i) :
    IsLocallyOfFinitePresentation B S hS i
```

## Tag 09RZ, a lemma

[Tag 09RZ](https://stacks.math.columbia.edu/tag/09RZ) in the Stacks Project.

**`AlgebraicGeometry.Space.isSplitExactConormalSequenceOnEtaleCharts_of_isH1RegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionConormalSequence.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionConormalSequence.lean#L108). The attribute's comment: “both conclusions — exactness and local splitness — of the conormal sequence of Tag 06BD for an H₁-regular immersion, read on the étale scheme charts of X as `IsSplitExactConormalSequenceOnEtaleCharts`, which is how this development states every condition on algebraic spaces whose scheme analogue it localizes. The sequence has no left-hand map as a sequence of modules on Z in this development, so nothing is asserted about it on Z itself; the splitting is étale-local, Zariski-local on each chart of an étale cover, and is neither global nor claimed on a single chart”. References: SGA 6 VIII (2.2), “partial”.

> **[Stacks Project, Tag 09RZ].**  Let `i : Z ⟶ Y` and `j : Y ⟶ X` be morphisms of algebraic
> spaces over `S` with `j` an immersion and `i` an `H₁`-regular immersion.  Then the conormal
> sequence `0 ⟶ i^* 𝒞_{Y/X} ⟶ 𝒞_{Z/X} ⟶ 𝒞_{Z/Y} ⟶ 0` of [Stacks Project, Tag 06BD] is exact and
> locally split, read on the étale scheme charts of `X`:  over every such chart the base changes of
> `j` and of `i` are immersions of schemes whose conormal sequence is short exact and splits on a
> neighbourhood of every point.
>
> Over a chart `c` of `X` the pair of scheme immersions is the base change of `j` to `c` together
> with the base change of `i` to the chart of `Y` that `j` pulls back from `c`.  That chart of `Y`
> is étale, because étaleness of a morphism of presheaves is stable under base change, so
> `H₁`-regularity of `i` gives it for the base change of `i`; the case of schemes,
> [Stacks Project, Tag 063N] in the bundled form
> `Stacks.AlgebraicGeometry.isSplitExactConormalSequence_of_isH1RegularImmersion`, then applies.
>
> This is the hypothesis of the three clauses of [Stacks Project, Tag 09S1]; see
> `AlgebraicGeometry.Space.isH1RegularImmersion_of_comp_of_isSplitExactConormalSequence` and its
> siblings.

```lean
theorem isSplitExactConormalSequenceOnEtaleCharts_of_isH1RegularImmersion (i : Z ⟶ Y) (j : Y ⟶ X)
    (hj : IsImmersion B S hS j) (hi : IsH1RegularImmersion B S hS i) :
    IsSplitExactConormalSequenceOnEtaleCharts B S hS i j
```

## Tag 09S0, a lemma

[Tag 09S0](https://stacks.math.columbia.edu/tag/09S0) in the Stacks Project.

**`AlgebraicGeometry.Space.isKoszulRegularImmersion_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionComposition.lean, line 415](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionComposition.lean#L415). The attribute's comment: “composition of Koszul-regular immersions”.

> **Stacks 09S0, the Koszul-regular case.**  The composite of two Koszul-regular immersions of
> algebraic spaces over `S` is a Koszul-regular immersion.

```lean
theorem isKoszulRegularImmersion_comp (i : Z ⟶ Y) (j : Y ⟶ X)
    (hi : IsKoszulRegularImmersion B S hS i) (hj : IsKoszulRegularImmersion B S hS j) :
    IsKoszulRegularImmersion B S hS (i ≫ j)
```

**`AlgebraicGeometry.Space.isH1RegularImmersion_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionComposition.lean, line 424](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionComposition.lean#L424). The attribute's comment: “composition of H₁-regular immersions”.

> **Stacks 09S0, the `H₁`-regular case.**  The composite of two `H₁`-regular immersions of
> algebraic spaces over `S` is an `H₁`-regular immersion.

```lean
theorem isH1RegularImmersion_comp (i : Z ⟶ Y) (j : Y ⟶ X)
    (hi : IsH1RegularImmersion B S hS i) (hj : IsH1RegularImmersion B S hS j) :
    IsH1RegularImmersion B S hS (i ≫ j)
```

**`AlgebraicGeometry.Space.isQuasiRegularImmersion_comp_of_isH1RegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionComposition.lean, line 434](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionComposition.lean#L434). The attribute's comment: “composition of an H₁-regular and a quasi-regular immersion”.

> **Stacks 09S0, the mixed case.**  The composite of an `H₁`-regular immersion of algebraic
> spaces over `S` and a quasi-regular immersion of algebraic spaces over `S` is a quasi-regular
> immersion.

```lean
theorem isQuasiRegularImmersion_comp_of_isH1RegularImmersion (i : Z ⟶ Y) (j : Y ⟶ X)
    (hi : IsH1RegularImmersion B S hS i) (hj : IsQuasiRegularImmersion B S hS j) :
    IsQuasiRegularImmersion B S hS (i ≫ j)
```

## Tag 09S1, a lemma

[Tag 09S1](https://stacks.math.columbia.edu/tag/09S1) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiRegularImmersion_of_comp_of_isSplitExactConormalSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionSplitConormal.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionSplitConormal.lean#L223). The attribute's comment: “(1) quasi-regularity descends to the first immersion, with the conormal hypothesis read on the étale charts of X”.

> **Stacks tag 09S1, clause (1).**  Let `i : Z ⟶ Y` and `j : Y ⟶ X` be representable morphisms
> of algebraic spaces over `S` with `j` locally of finite presentation and with the conormal
> sequence of Stacks tag 06BD exact and locally split on the étale charts of `X`.  If `i ≫ j` is a
> quasi-regular immersion, so is `i`.
>
> The sibling clauses are
> `AlgebraicGeometry.Space.isH1RegularImmersion_of_comp_of_isSplitExactConormalSequence`, clause
> (2) for `H₁`-regularity, and
> `AlgebraicGeometry.Space.isKoszulRegularImmersion_of_comp_of_isSplitExactConormalSequence`,
> clause (3) for Koszul-regularity.

```lean
theorem isQuasiRegularImmersion_of_comp_of_isSplitExactConormalSequence
    (hZ : IsAlgebraicSpace B S hS Z) (hY : IsAlgebraicSpace B S hS Y)
    (hX : IsAlgebraicSpace B S hS X) (i : Z ⟶ Y) (j : Y ⟶ X)
    (hjfp : IsLocallyOfFinitePresentation B S hS j)
    (hcon : IsSplitExactConormalSequenceOnEtaleCharts B S hS i j)
    (hij : IsQuasiRegularImmersion B S hS (i ≫ j)) :
    IsQuasiRegularImmersion B S hS i
```

**`AlgebraicGeometry.Space.isH1RegularImmersion_of_comp_of_isSplitExactConormalSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionSplitConormal.lean, line 265](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionSplitConormal.lean#L265). The attribute's comment: “(2) H₁-regularity descends to the first immersion, with the conormal hypothesis read on the étale charts of X”.

> **Stacks tag 09S1, clause (2).**  Let `i : Z ⟶ Y` and `j : Y ⟶ X` be representable morphisms
> of algebraic spaces over `S` with `j` locally of finite presentation and with the conormal
> sequence of Stacks tag 06BD exact and locally split on the étale charts of `X`.  If `i ≫ j` is an
> `H₁`-regular immersion, so is `i`.
>
> The sibling clauses are
> `AlgebraicGeometry.Space.isQuasiRegularImmersion_of_comp_of_isSplitExactConormalSequence`, clause
> (1) for quasi-regularity, and
> `AlgebraicGeometry.Space.isKoszulRegularImmersion_of_comp_of_isSplitExactConormalSequence`,
> clause (3) for Koszul-regularity.

```lean
theorem isH1RegularImmersion_of_comp_of_isSplitExactConormalSequence
    (hZ : IsAlgebraicSpace B S hS Z) (hY : IsAlgebraicSpace B S hS Y)
    (hX : IsAlgebraicSpace B S hS X) (i : Z ⟶ Y) (j : Y ⟶ X)
    (hjfp : IsLocallyOfFinitePresentation B S hS j)
    (hcon : IsSplitExactConormalSequenceOnEtaleCharts B S hS i j)
    (hij : IsH1RegularImmersion B S hS (i ≫ j)) :
    IsH1RegularImmersion B S hS i
```

**`AlgebraicGeometry.Space.isKoszulRegularImmersion_of_comp_of_isSplitExactConormalSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionSplitConormal.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionSplitConormal.lean#L307). The attribute's comment: “(3) Koszul-regularity of the first immersion, with the conormal hypothesis read on the étale charts of X”.

> **Stacks tag 09S1, clause (3).**  Let `i : Z ⟶ Y` and `j : Y ⟶ X` be representable morphisms
> of algebraic spaces over `S` with `j` locally of finite presentation and with the conormal
> sequence of Stacks tag 06BD exact and locally split on the étale charts of `X`.  If both `j` and
> `i ≫ j` are Koszul-regular immersions, so is `i`.
>
> The sibling clauses are
> `AlgebraicGeometry.Space.isQuasiRegularImmersion_of_comp_of_isSplitExactConormalSequence`, clause
> (1) for quasi-regularity, and
> `AlgebraicGeometry.Space.isH1RegularImmersion_of_comp_of_isSplitExactConormalSequence`, clause
> (2) for `H₁`-regularity.

```lean
theorem isKoszulRegularImmersion_of_comp_of_isSplitExactConormalSequence
    (hZ : IsAlgebraicSpace B S hS Z) (hY : IsAlgebraicSpace B S hS Y)
    (hX : IsAlgebraicSpace B S hS X) (i : Z ⟶ Y) (j : Y ⟶ X)
    (hjfp : IsLocallyOfFinitePresentation B S hS j)
    (hcon : IsSplitExactConormalSequenceOnEtaleCharts B S hS i j)
    (hj : IsKoszulRegularImmersion B S hS j)
    (hij : IsKoszulRegularImmersion B S hS (i ≫ j)) :
    IsKoszulRegularImmersion B S hS i
```

## Tag 09S2, a lemma

[Tag 09S2](https://stacks.math.columbia.edu/tag/09S2) in the Stacks Project.

**`AlgebraicGeometry.Space.isKoszulRegularImmersion_tfae_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionNoetherianSplitConormal.lean, line 318](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RegularImmersionNoetherianSplitConormal.lean#L318). The attribute's comment: “all three conditions, with the second clause of condition (1) — Koszul-regularity of j — localized to a neighbourhood of the image of i and read on the étale charts of X. The source states that clause on all of Y, which is false: for Z empty, conditions (2) and (3) hold for every j, while j need not be Koszul-regular. The localized clause is what the cited scheme-level Tag 0690 proves, that tag being stated at a point of Z”.

> **Stacks tag 09S2.**  Let `i : Z ⟶ Y` and `j : Y ⟶ X` be immersions of algebraic spaces over
> a scheme `S` with `X` locally Noetherian.  Then the following are equivalent:
>
> 1. `i` is a Koszul-regular immersion and `j` is a Koszul-regular immersion near the image of `i`,
> 2. `i` and `i ≫ j` are Koszul-regular immersions,
> 3. `i ≫ j` is a Koszul-regular immersion and the conormal sequence
>    `0 ⟶ i^* 𝒞_{Y/X} ⟶ 𝒞_{Z/X} ⟶ 𝒞_{Z/Y} ⟶ 0` of Stacks tag 06BD is exact and locally split.
>
> Conditions (1) and (3) are read on the étale scheme charts of `X`, as every condition on
> algebraic spaces whose scheme analogue this development localizes.  The second clause of
> condition (1) is Koszul-regularity of `j` on a neighbourhood of the image of `i`, not on all of
> `Y`:  the source states it on all of `Y`, which is false, and the module documentation gives the
> counterexample and the reason the cited scheme-level Stacks tag 0690 is itself pointwise.

```lean
theorem isKoszulRegularImmersion_tfae_of_isLocallyNoetherian (hZ : IsAlgebraicSpace B S hS Z)
    (hY : IsAlgebraicSpace B S hS Y) (hX : IsAlgebraicSpace B S hS X) (i : Z ⟶ Y) (j : Y ⟶ X)
    (_hi : IsImmersion B S hS i) (hj : IsImmersion B S hS j)
    (hnoeth : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsLocallyNoetherian T)) :
    List.TFAE
      [IsKoszulRegularImmersion B S hS i ∧
          IsKoszulRegularImmersionNearImageOnEtaleCharts B S hS i j,
        IsKoszulRegularImmersion B S hS i ∧ IsKoszulRegularImmersion B S hS (i ≫ j),
        IsKoszulRegularImmersion B S hS (i ≫ j) ∧
          IsSplitExactConormalSequenceOnEtaleCharts B S hS i j]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.44, Tag 06BL](https://stacks.math.columbia.edu/tag/06BL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
