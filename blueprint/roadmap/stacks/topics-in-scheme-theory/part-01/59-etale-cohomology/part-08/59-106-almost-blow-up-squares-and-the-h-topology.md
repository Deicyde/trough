---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsAlmostBlowUpSquare, AlgebraicGeometry.isCSquareIso_of_essImage_almostBlowUpSquare_bigH, AlgebraicGeometry.isCSquareIso_of_essImage_affineAlmostBlowUp_bigH, AlgebraicGeometry.essImage_iff_forall_isCSquareIso_affineAlmostBlowUp_bigH, AlgebraicGeometry.essImage_iff_forall_isCSquareIso_affineAlmostBlowUp_fppf_bigH, AlgebraicGeometry.essImage_iff_forall_isCSquareIso_generatorAlmostBlowUp_fppf_bigH, AlgebraicGeometry.isCSquareIso_of_essImage_principalCenterModelPair_bigH
statement: formalized
proof: formalized
---

# 59.106 Almost blow up squares and the h topology

Section 59.106 of the Stacks Project, [Tag 0EWL](https://stacks.math.columbia.edu/tag/0EWL). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EWM, an equation

[Tag 0EWM](https://stacks.math.columbia.edu/tag/0EWM) in the Stacks Project.

**`AlgebraicGeometry.IsAlmostBlowUpSquare`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AlmostBlowUp/Basic.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AlmostBlowUp/Basic.lean#L44).

> An almost blowup square with centre `I.subscheme` and modification `b`. The exceptional
> closed subscheme is `(I.comap b).subscheme`.

```lean
public structure IsAlmostBlowUpSquare {X X' : Scheme.{u}}
    (I : X.IdealSheafData) (b : X' ⟶ X) : Prop
```

## Tag 0EWN, a lemma

[Tag 0EWN](https://stacks.math.columbia.edu/tag/0EWN) in the Stacks Project.

**`AlgebraicGeometry.isCSquareIso_of_essImage_almostBlowUpSquare_bigH`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AlmostBlowUp/DerivedHDescent.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AlmostBlowUp/DerivedHDescent.lean#L149).

> **Stacks 0EWN.** Let `J' ≤ J` be a topology coarser than the h topology on the big h
> category over `S` — the fppf topology in the source — and let `𝒪` be a sheaf of rings for the h
> topology, so that the identity functor is a comparison of ringed sites
> `ε : (C_J, 𝒪_J) ⟶ (C_{J'}, 𝒪_{J'})`. Then for every almost blowup square in the big h category
> over `S` and every object `K` of `D(𝒪_{J'})` in the essential image of the derived direct image
> `Rε_*`, the canonical Mayer–Vietoris comparison `c^K_{X,Z,X',E}` of Stacks 0F16 for the coarser
> topology is an isomorphism, i.e. a quasi-isomorphism of complexes of abelian groups.
>
> The h sheafified representables of the square form a pushout square by Stacks 0EVD, and
> `h_E^# ⟶ h_{X'}^#` is a monomorphism because `E ⟶ X'` is one, so Stacks 0F19 applies.

```lean
theorem isCSquareIso_of_essImage_almostBlowUpSquare_bigH
    (B : BigHSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (O : Sheaf (BigHOver.topology B S hS) CommRingCat.{r})
    {J' : GrothendieckTopology (BigHOver B S hS)} (hJ : J' ≤ BigHOver.topology B S hS)
    [HasSheafify (BigHOver.topology B S hS) AddCommGrpCat.{v}]
    [(BigHOver.topology B S hS).WEqualsLocallyBijective AddCommGrpCat.{v}]
    [HasSheafify J' AddCommGrpCat.{v}] [J'.WEqualsLocallyBijective AddCommGrpCat.{v}]
    [UnivLE.{u + 1, v}] [UnivLE.{u, v}] [UnivLE.{r, v}]
    (Rε : DerivedCategory (SheafOfModules.{v}
        (Stacks.SheafOfModules.Tensor.ringSheaf (bigHRingedSite B S hS O).O)) ⥤
      DerivedCategory (SheafOfModules.{v}
        (Stacks.SheafOfModules.Tensor.ringSheaf ((bigHRingedSite B S hS O).ofLe hJ).O)))
    (η : (Stacks.Sites.CoarserTopology.modulePushforward.{u + 1, v, u, r} hJ
          (Stacks.SheafOfModules.Tensor.ringSheaf (bigHRingedSite B S hS O).O)).mapHomotopyCategory
            (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rε)
    [Rε.IsRightDerivedFunctor η (HomotopyCategory.quasiIso
      (SheafOfModules.{v} (Stacks.SheafOfModules.Tensor.ringSheaf (bigHRingedSite B S hS O).O))
        (ComplexShape.up ℤ))]
    (K : DerivedCategory (SheafOfModules.{v}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((bigHRingedSite B S hS O).ofLe hJ).O)))
    (hK : Rε.essImage K)
    (sq : Square (BigHOver B S hS))
    (I : ((BigHOver.toScheme B S hS).obj sq.X₄).IdealSheafData)
    (hb : IsAlmostBlowUpSquare I ((BigHOver.toScheme B S hS).map sq.f₂₄))
    (hZ : Nonempty (Over.mk ((BigHOver.toScheme B S hS).map sq.f₃₄) ≅ Over.mk I.subschemeι))
    (hSquare : (sq.map (BigHOver.toScheme B S hS)).IsPullback) :
    (Stacks.MayerVietoris.CanonicalMapOfComplexes.derivedCSquareData.{u + 1, v}
      (R := (Stacks.SheafOfModules.Tensor.ringSheaf ((bigHRingedSite B S hS O).ofLe hJ).O))
        sq).IsCSquareIso K
```

## Tag 0EWQ, a proposition

[Tag 0EWQ](https://stacks.math.columbia.edu/tag/0EWQ) in the Stacks Project.

**`AlgebraicGeometry.isCSquareIso_of_essImage_affineAlmostBlowUp_bigH`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AlmostBlowUp/AffineAlmostBlowUpCriterion.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AlmostBlowUp/AffineAlmostBlowUpCriterion.lean#L171). The attribute's comment: “only if”.

> **Stacks 0EWQ, the direction "only if".** Let `J' ≤ J` be a topology coarser than the h
> topology on the big h category over `S` and let `𝒪` be a sheaf of rings for the h topology, so
> that the identity functor is a comparison of ringed sites
> `ε : (C_J, 𝒪_J) ⟶ (C_{J'}, 𝒪_{J'})`. Then for every object `K` of `D(𝒪_{J'})` in the essential
> image of the derived direct image `Rε_*` and every almost blowup square of the site with affine
> base, the canonical Mayer–Vietoris comparison `c^K_{X,X',Z,E}` of Stacks 0F16 is an isomorphism.
>
> This is Stacks 0EWN; affineness of the base is not used, and `K` need not be bounded below.

```lean
theorem isCSquareIso_of_essImage_affineAlmostBlowUp_bigH
    (Rε : DerivedCategory (SheafOfModules.{v}
        (Stacks.SheafOfModules.Tensor.ringSheaf (bigHRingedSite B S hS O).O)) ⥤
      DerivedCategory (SheafOfModules.{v}
        (Stacks.SheafOfModules.Tensor.ringSheaf ((bigHRingedSite B S hS O).ofLe hJ).O)))
    (η : (modulePushforward.{u + 1, v, u, r} hJ
          (Stacks.SheafOfModules.Tensor.ringSheaf (bigHRingedSite B S hS O).O)).mapHomotopyCategory
            (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rε)
    [Rε.IsRightDerivedFunctor η (HomotopyCategory.quasiIso
      (SheafOfModules.{v} (Stacks.SheafOfModules.Tensor.ringSheaf (bigHRingedSite B S hS O).O))
        (ComplexShape.up ℤ))]
    (K : DerivedCategory (SheafOfModules.{v}
        (Stacks.SheafOfModules.Tensor.ringSheaf ((bigHRingedSite B S hS O).ofLe hJ).O)))
    (hK : Rε.essImage K) (sq : AffineAlmostBlowUpSquare B S hS) :
    (Stacks.MayerVietoris.CanonicalMapOfComplexes.derivedCSquareData.{u + 1, v}
      (R := (Stacks.SheafOfModules.Tensor.ringSheaf ((bigHRingedSite B S hS O).ofLe hJ).O))
        sq.square).IsCSquareIso K
```

**`AlgebraicGeometry.essImage_iff_forall_isCSquareIso_affineAlmostBlowUp_bigH`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AlmostBlowUp/AffineAlmostBlowUpCriterion.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AlmostBlowUp/AffineAlmostBlowUpCriterion.lean#L280). The attribute's comment: “the iff, given the detection hypothesis”.

> **Stacks 0EWQ.** Let `J' ≤ J` be a topology coarser than the h topology on the big h category
> over `S` and let `𝒪` be a sheaf of rings for the h topology, so that the identity functor is a
> comparison of ringed sites `ε : (C_J, 𝒪_J) ⟶ (C_{J'}, 𝒪_{J'})`, and assume that affine almost
> blowup squares detect h sheaves among `J'`-sheaves of sets. Then an object `K` of `D⁺(𝒪_{J'})`
> lies in the essential image of the derived direct image `Rε_*` if and only if the canonical
> Mayer–Vietoris comparison `c^K_{X,X',Z,E}` of Stacks 0F16 is an isomorphism for every almost
> blowup square of the site whose base is affine.
>
> This is the derived functor, its unit and the object spelled out as binders, which is
> `AlgebraicGeometry.essImageIffAffineAlmostBlowUpBigH_of_isAffineAlmostBlowUpDetecting` with its
> conclusion unfolded; the bundled form is the one a downstream file can state, because there the
> binders no longer elaborate. The tag is registered here with the detection hypothesis named, and
> again unconditionally on
> `AlgebraicGeometry.essImage_iff_forall_isCSquareIso_affineAlmostBlowUp_fppf_bigH`, the assertion
> at the fppf topology, where detection holds.

```lean
theorem essImage_iff_forall_isCSquareIso_affineAlmostBlowUp_bigH
    (hdetect : BigHOver.IsAffineAlmostBlowUpDetecting B S hS J')
    (Rε : DerivedCategory (SheafOfModules.{v}
        (Stacks.SheafOfModules.Tensor.ringSheaf (bigHRingedSite B S hS O).O)) ⥤
      DerivedCategory (SheafOfModules.{v}
        (Stacks.SheafOfModules.Tensor.ringSheaf ((bigHRingedSite B S hS O).ofLe hJ).O)))
    (η : (modulePushforward.{u + 1, v, u, r} hJ
          (Stacks.SheafOfModules.Tensor.ringSheaf (bigHRingedSite B S hS O).O)).mapHomotopyCategory
            (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rε)
    [hRD : Rε.IsRightDerivedFunctor η (HomotopyCategory.quasiIso
      (SheafOfModules.{v} (Stacks.SheafOfModules.Tensor.ringSheaf (bigHRingedSite B S hS O).O))
        (ComplexShape.up ℤ))]
    (K : DerivedCategory (SheafOfModules.{v}
        (Stacks.SheafOfModules.Tensor.ringSheaf ((bigHRingedSite B S hS O).ofLe hJ).O)))
    (hK : (DerivedCategory.TStructure.t (C := SheafOfModules.{v}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((bigHRingedSite B S hS O).ofLe hJ).O))).plus K) :
    Rε.essImage K ↔ ∀ sq : AffineAlmostBlowUpSquare B S hS,
      (Stacks.MayerVietoris.CanonicalMapOfComplexes.derivedCSquareData.{u + 1, v}
      (R := (Stacks.SheafOfModules.Tensor.ringSheaf ((bigHRingedSite B S hS O).ofLe hJ).O))
        sq.square).IsCSquareIso K
```

**`AlgebraicGeometry.essImage_iff_forall_isCSquareIso_affineAlmostBlowUp_fppf_bigH`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AlmostBlowUp/AffineAlmostBlowUpFppfCriterion.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AlmostBlowUp/AffineAlmostBlowUpFppfCriterion.lean#L234).

> **Stacks 0EWQ.** Let `𝒪` be a sheaf of rings for the h topology on the big h category over
> `S`, and let `ε : (C_h, 𝒪_h) ⟶ (C_{fppf}, 𝒪_{fppf})` be the comparison of ringed sites given by
> the identity functor, the fppf topology on that category being coarser than the h topology.  Then
> an object `K` of `D⁺(𝒪_{fppf})` lies in the essential image of the derived direct image `Rε_*` if
> and only if the canonical Mayer–Vietoris comparison `c^K_{X,X',Z,E}` of Stacks 0F16 is an
> isomorphism for every almost blowup square of the site whose base is affine.
>
> This is
> `AlgebraicGeometry.essImageIffAffineAlmostBlowUpBigH_of_isAffineAlmostBlowUpDetecting` at the fppf
> topology, where the detection of h sheaves by affine almost blowup squares is
> `AlgebraicGeometry.BigHOver.isAffineAlmostBlowUpDetecting_fppfTopology`, the sufficiency direction
> of Stacks 0EVF.

```lean
theorem essImage_iff_forall_isCSquareIso_affineAlmostBlowUp_fppf_bigH :
    EssImageIffAffineAlmostBlowUpBigH.{u, v, r} B S hS O
      (BigHOver.fppfTopology_le_topology B S hS)
```

## Tag 0EWR, a lemma

[Tag 0EWR](https://stacks.math.columbia.edu/tag/0EWR) in the Stacks Project.

**`AlgebraicGeometry.essImage_iff_forall_isCSquareIso_generatorAlmostBlowUp_fppf_bigH`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AlmostBlowUp/GeneratorAlmostBlowUpFppfCriterion.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AlmostBlowUp/GeneratorAlmostBlowUpFppfCriterion.lean#L250).

> **Stacks 0EWR.** Let `𝒪` be a sheaf of rings for the h topology on the big h category over
> `S`, and let `ε : (C_h, 𝒪_h) ⟶ (C_{fppf}, 𝒪_{fppf})` be the comparison of ringed sites given by
> the identity functor, the fppf topology on that category being coarser than the h topology. Then
> an object `K` of `D⁺(𝒪_{fppf})` lies in the essential image of the derived direct image `Rε_*` if
> and only if the canonical Mayer–Vietoris comparison `c^K_{X,X',Z,E}` of Stacks 0F16 is an
> isomorphism for every almost blow up square of the site as in More on Flatness, Examples 0EVG
> and 0EVH.
>
> This is `AlgebraicGeometry.essImageIffAffineAlmostBlowUpFamilyBigH_of_isDetecting` at the fppf
> topology for the family of squares of the two shapes, whose detection of h sheaves among fppf
> sheaves of sets is the sufficiency direction of More on Flatness, Lemma 0EVI,
> `AlgebraicGeometry.BigHOver.isAffineAlmostBlowUpFamilyDetecting_generator_fppfTopology`.

```lean
theorem essImage_iff_forall_isCSquareIso_generatorAlmostBlowUp_fppf_bigH :
    EssImageIffAffineAlmostBlowUpFamilyBigH.{u + 1, u, v, r} B S hS O
      (BigHOver.fppfTopology_le_topology B S hS)
      (GeneratorAlmostBlowUpSquare.toAffineAlmostBlowUpSquare (B := B) (S := S) (hS := hS))
```

**`AlgebraicGeometry.isCSquareIso_of_essImage_principalCenterModelPair_bigH`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AlmostBlowUp/PrincipalCenterHDescent.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AlmostBlowUp/PrincipalCenterHDescent.lean#L233). The attribute's comment: “only if, for the almost blow up squares of More on Flatness, Example 0EVG”.

> **Stacks 0EWR, the "only if" direction for the almost blow up squares of More on Flatness,
> Example 0EVG.** Let `J' ≤ J` be a topology coarser than the h topology on the big h category
> over `S` — the fppf topology in the source — and let `𝒪` be a sheaf of rings for the h topology,
> so that the identity functor is a comparison of ringed sites
> `ε : (C_J, 𝒪_J) ⟶ (C_{J'}, 𝒪_{J'})`. Let `K` be an object of `D(𝒪_{J'})` in the essential image
> of the derived direct image `Rε_*`. Then for every almost blow up square of the shape of More on
> Flatness, Example 0EVG in the big h category over `S` the canonical Mayer–Vietoris comparison
> `c^K_{X,X',Z,E}` of Stacks 0F16 for the coarser topology is a quasi-isomorphism.
>
> The squares named by the source are almost blow up squares, by Stacks 0EVG transported along the
> isomorphism recognizing the shape, so this is Stacks 0EWN.

```lean
theorem isCSquareIso_of_essImage_principalCenterModelPair_bigH
    (B : BigHSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (O : Sheaf (BigHOver.topology B S hS) CommRingCat.{r})
    {J' : GrothendieckTopology (BigHOver B S hS)} (hJ : J' ≤ BigHOver.topology B S hS)
    [HasSheafify (BigHOver.topology B S hS) AddCommGrpCat.{v}]
    [(BigHOver.topology B S hS).WEqualsLocallyBijective AddCommGrpCat.{v}]
    [HasSheafify J' AddCommGrpCat.{v}] [J'.WEqualsLocallyBijective AddCommGrpCat.{v}]
    [UnivLE.{u + 1, v}] [UnivLE.{u, v}] [UnivLE.{r, v}]
    (Rε : DerivedCategory (SheafOfModules.{v}
        (Stacks.SheafOfModules.Tensor.ringSheaf (bigHRingedSite B S hS O).O)) ⥤
      DerivedCategory (SheafOfModules.{v}
        (Stacks.SheafOfModules.Tensor.ringSheaf ((bigHRingedSite B S hS O).ofLe hJ).O)))
    (η : (Stacks.Sites.CoarserTopology.modulePushforward.{u + 1, v, u, r} hJ
          (Stacks.SheafOfModules.Tensor.ringSheaf (bigHRingedSite B S hS O).O)).mapHomotopyCategory
            (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rε)
    [Rε.IsRightDerivedFunctor η (HomotopyCategory.quasiIso
      (SheafOfModules.{v} (Stacks.SheafOfModules.Tensor.ringSheaf (bigHRingedSite B S hS O).O))
      (ComplexShape.up ℤ))]
    (K : DerivedCategory (SheafOfModules.{v}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((bigHRingedSite B S hS O).ofLe hJ).O)))
    (hK : Rε.essImage K)
    (sq : Square (BigHOver B S hS))
    (hmodel : IsPrincipalCenterModelPair ((BigHOver.toScheme B S hS).map sq.f₂₄)
      ((BigHOver.toScheme B S hS).map sq.f₃₄))
    (hSquare : (sq.map (BigHOver.toScheme B S hS)).IsPullback) :
    (Stacks.MayerVietoris.CanonicalMapOfComplexes.derivedCSquareData.{u + 1, v}
      (R := (Stacks.SheafOfModules.Tensor.ringSheaf ((bigHRingedSite B S hS O).ofLe hJ).O))
      sq).IsCSquareIso K
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.106, Tag 0EWL](https://stacks.math.columbia.edu/tag/0EWL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
