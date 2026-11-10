---
declaration: section
origin: cited
lean: AlgebraicGeometry.CurveFamily.exists_isOpen_forall_isStructureContraction_baseChange, AlgebraicGeometry.Space.exists_iso_near_point_of_iso_fibre, AlgebraicGeometry.CurveFamily.exists_elementaryEtaleNeighborhood_contraction, AlgebraicGeometry.CurveFamily.exists_stabilization_and_existsUnique_iso, AlgebraicGeometry.stabilizationMorphism, AlgebraicGeometry.stabilizationMorphism_obj
statement: formalized
proof: formalized
---

# 109.23 Contraction morphisms

Section 109.23 of the Stacks Project, [Tag 0E7B](https://stacks.math.columbia.edu/tag/0E7B). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E88, a lemma

[Tag 0E88](https://stacks.math.columbia.edu/tag/0E88) in the Stacks Project.

**`AlgebraicGeometry.CurveFamily.exists_isOpen_forall_isStructureContraction_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurveFamilyContractionOpen.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurveFamilyContractionOpen.lean#L56).

> Let `S` be a scheme, `s ∈ S`, and `c : X ⟶ Y` a morphism over `S` of families of curves. If
> `c_{s,*}𝒪_{X_s} = 𝒪_{Y_s}` and `R¹c_{s,*}𝒪_{X_s} = 0`, there is an open neighbourhood `W` of `s`
> such that for every scheme `T ⟶ S` landing in `W` and every base change `c' : X_T ⟶ Y_T` of `c`,
> `𝒪_{Y_T} = c'_*𝒪_{X_T}` and `R¹c'_*𝒪_{X_T} = 0`. Taking `T = W` gives the statement over `W`,
> and the quantification over `T` is the persistence under base change.

```lean
theorem exists_isOpen_forall_isStructureContraction_baseChange
    (X Y : CurveFamily B hZ) (hb : Y.base = X.base) (c : X.total ⟶ Y.total)
    (hc : c ≫ Y.toBase ≫ eqToHom (congrArg schemeSpace hb) = X.toBase) (s : X.base.left.1)
    (hs : Space.IsStructureContraction B integerBase hZ
      (Space.structureContractionBaseChange B integerBase hZ c hc
        (schemeSpaceMap (Space.residueFieldMap B integerBase hZ X.base s
          (B.residueField_spec_contains X.base.left.property s))))) :
    ∃ W : X.base.left.1.Opens, s ∈ W ∧
      ∀ (T : BigFppfOver B integerBase hZ) (h : T ⟶ X.base),
        (∀ t, ((𝒯).map h).base t ∈ W) →
        ∀ (X' Y' : AlgebraicSpaces B integerBase hZ) (pX' : X' ⟶ X.total)
          (fX' : X' ⟶ schemeSpace T) (pY' : Y' ⟶ Y.total) (fY' : Y' ⟶ schemeSpace T)
          (c' : X' ⟶ Y'),
          IsPullback pX' fX' X.toBase (schemeSpaceMap h) →
          IsPullback pY' fY' (Y.toBase ≫ eqToHom (congrArg schemeSpace hb)) (schemeSpaceMap h) →
          c' ≫ pY' = pX' ≫ c → c' ≫ fY' = fX' →
          Space.IsStructureContraction B integerBase hZ c'
```

## Tag 0E89, a lemma

[Tag 0E89](https://stacks.math.columbia.edu/tag/0E89) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_iso_near_point_of_iso_fibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ContractionUniquenessNearPoint.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/ContractionUniquenessNearPoint.lean#L415). The attribute's comment: “Families of curves are read as in `AlgebraicGeometry.CurveFamily` (Stacks 0D4Z): algebraic spaces `X`, `Y₁`, `Y₂` with morphisms to `S` which are flat, proper, of finite presentation and of relative dimension at most one. The fibres over `s` are the fibre products along `Spec κ(s) ⟶ S`; the hypotheses on `c₁,ₛ` are read on the morphism of schemes presenting it (the fibres being schemes by Stacks 0ADD).”.

> Let `S` be a scheme and `s ∈ S` a point. Let `f : X ⟶ S` and `gᵢ : Yᵢ ⟶ S`, `i = 1, 2`, be
> families of curves (algebraic spaces, flat, proper, of finite presentation and of relative
> dimension at most one over `S`) and `cᵢ : X ⟶ Yᵢ` morphisms over `S`. Let `φ : Y₁,ₛ ≅ Y₂,ₛ` be an
> isomorphism of the fibres over `Spec κ(s) ⟶ S` compatible with `c₁,ₛ` and `c₂,ₛ`. Suppose
> `c₁,ₛ,* 𝒪_{Xₛ} = 𝒪_{Y₁,ₛ}` and `R¹c₁,ₛ,* 𝒪_{Xₛ} = 0`; these are read on the morphism of schemes
> `a₁ : F_X ⟶ F₁` which `c₁,ₛ` is through presentations `e_X`, `e₁` of the fibres `Xₛ` and `Y₁,ₛ`
> by schemes (the fibres of a family of curves over a field are schemes, [Stacks, Tag 0ADD],
> `AlgebraicGeometry.Space.exists_presentation_of_curveFamilyConditions_of_field`). Then there are
> an open neighbourhood `j : U ⟶ S` of `s` and an isomorphism `ψ : Y₁ ×_S U ≅ Y₂ ×_S U` over `U`,
> compatible with `c₁` and `c₂` and with `φ` (through the factorisation `k` of `Spec κ(s) ⟶ S`
> through `U`).

```lean
theorem exists_iso_near_point_of_iso_fibre (S : BigFppfOver B integerBase hZ) (s : (𝒯).obj S)
    {X Y₁ Y₂ : (BigFppfOver B integerBase hZ)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B integerBase hZ X) (hY₁ : IsAlgebraicSpace B integerBase hZ Y₁)
    (hY₂ : IsAlgebraicSpace B integerBase hZ Y₂)
    (f : X ⟶ yoneda.obj S) (g₁ : Y₁ ⟶ yoneda.obj S) (g₂ : Y₂ ⟶ yoneda.obj S)
    (hfl : IsFlat B integerBase hZ f) (hpr : IsProper B integerBase hZ f)
    (hfp : IsFinitePresentation B integerBase hZ f)
    (hd : HasRelativeDimensionLE 1 B integerBase hZ f)
    (hfl₁ : IsFlat B integerBase hZ g₁) (hpr₁ : IsProper B integerBase hZ g₁)
    (hfp₁ : IsFinitePresentation B integerBase hZ g₁)
    (hd₁ : HasRelativeDimensionLE 1 B integerBase hZ g₁)
    (hfl₂ : IsFlat B integerBase hZ g₂) (hpr₂ : IsProper B integerBase hZ g₂)
    (hfp₂ : IsFinitePresentation B integerBase hZ g₂)
    (hd₂ : HasRelativeDimensionLE 1 B integerBase hZ g₂)
    (c₁ : X ⟶ Y₁) (c₂ : X ⟶ Y₂) (hc₁ : c₁ ≫ g₁ = f) (hc₂ : c₂ ≫ g₂ = f)
    {FX F₁ : BigFppfOver B integerBase hZ}
    (eX : yoneda.obj FX ≅ pullback f (yoneda.map (pointFieldMap S s)))
    (e₁ : yoneda.obj F₁ ≅ pullback g₁ (yoneda.map (pointFieldMap S s)))
    (tX : FX ⟶ pointFieldObject S s) (t₁ : F₁ ⟶ pointFieldObject S s)
    (heX : eX.hom ≫ pullback.snd f (yoneda.map (pointFieldMap S s)) = yoneda.map tX)
    (he₁ : e₁.hom ≫ pullback.snd g₁ (yoneda.map (pointFieldMap S s)) = yoneda.map t₁)
    (a₁ : FX ⟶ F₁)
    (ha₁ : yoneda.map a₁ ≫ e₁.hom =
      eX.hom ≫ pullback.map f (yoneda.map (pointFieldMap S s)) g₁
        (yoneda.map (pointFieldMap S s)) c₁ (𝟙 _) (𝟙 _) (by simp [hc₁]) (by simp))
    (h0 : IsIso (Scheme.Modules.unitToPushforwardUnit ((𝒯).map a₁)))
    (hR : IsZero (firstDirectImageStructureSheaf ((𝒯).map a₁)))
    (φ : pullback g₁ (yoneda.map (pointFieldMap S s)) ≅
      pullback g₂ (yoneda.map (pointFieldMap S s)))
    (hφ : φ.hom ≫ pullback.snd g₂ (yoneda.map (pointFieldMap S s)) =
      pullback.snd g₁ (yoneda.map (pointFieldMap S s)))
    (hφc : pullback.map f (yoneda.map (pointFieldMap S s)) g₁
        (yoneda.map (pointFieldMap S s)) c₁ (𝟙 _) (𝟙 _) (by simp [hc₁]) (by simp) ≫ φ.hom =
      pullback.map f (yoneda.map (pointFieldMap S s)) g₂
        (yoneda.map (pointFieldMap S s)) c₂ (𝟙 _) (𝟙 _) (by simp [hc₂]) (by simp)) :
    ∃ (U : BigFppfOver B integerBase hZ) (j : U ⟶ S),
      _root_.AlgebraicGeometry.IsOpenImmersion ((𝒯).map j) ∧
      s ∈ Set.range ((𝒯).map j) ∧
      ∃ (ψ : pullback g₁ (yoneda.map j) ≅ pullback g₂ (yoneda.map j))
        (k : pointFieldObject S s ⟶ U),
        ψ.hom ≫ pullback.snd g₂ (yoneda.map j) = pullback.snd g₁ (yoneda.map j) ∧
        pullback.map f (yoneda.map j) g₁ (yoneda.map j) c₁ (𝟙 _) (𝟙 _) (by simp [hc₁])
            (by simp) ≫ ψ.hom =
          pullback.map f (yoneda.map j) g₂ (yoneda.map j) c₂ (𝟙 _) (𝟙 _) (by simp [hc₂])
            (by simp) ∧
        ∃ (hk : k ≫ j = pointFieldMap S s),
          pullback.map g₁ (yoneda.map (pointFieldMap S s)) g₁ (yoneda.map j) (𝟙 _) (yoneda.map k)
              (𝟙 _) (by simp) (by rw [Category.comp_id, ← Functor.map_comp, hk]) ≫ ψ.hom =
            φ.hom ≫ pullback.map g₂ (yoneda.map (pointFieldMap S s)) g₂ (yoneda.map j) (𝟙 _)
              (yoneda.map k) (𝟙 _) (by simp)
              (by rw [Category.comp_id, ← Functor.map_comp, hk])
```

## Tag 0E7C, a lemma

[Tag 0E7C](https://stacks.math.columbia.edu/tag/0E7C) in the Stacks Project.

**`AlgebraicGeometry.CurveFamily.exists_elementaryEtaleNeighborhood_contraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ContractionExistenceScheme.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/ContractionExistenceScheme.lean#L225).

> Let `F` be a family of curves (Stacks 0D4Z) over a scheme `S` of the site, `s ∈ S`, `X₀` the
> fibre of `F` over `s` (the cartesian square `ι` over `Spec κ(s) ⟶ S`; the fibre of a family of
> curves over a field is a scheme, Stacks 0ADD), and `h₀ : X₀ ⟶ Y₀` a morphism over `κ(s)` to a
> proper scheme `Y₀` over `κ(s)` with `𝒪_{Y₀} = h₀,*𝒪_{X₀}` and `R¹h₀,*𝒪_{X₀} = 0`. Then there are an
> elementary étale neighbourhood `(U, u)` of `(S, s)`, with the lift `t : Spec κ(s) ⟶ U` of `s` onto
> `u` which identifies `κ(u)` with `κ(s)`, a family of curves `G` over `U` and a morphism `h` over
> `U` from the total space of the base change `F_U` to that of `G` whose fibre in `u` is isomorphic
> to `h₀`: `X₀` and `Y₀` are the fibres of `F_U` and `G` over `t` (the cartesian squares `ιU` and
> `j`, with `ιU` lying over `ι`), and `h` restricts to `h₀`.

```lean
theorem exists_elementaryEtaleNeighborhood_contraction {S : Scheme.{u}} (hS : B.Contains S)
    (F : CurveFamily B hZ) (hF : F.base = integerSiteObject B hZ hS) (s : S)
    {X₀ : Scheme.{u}} (hX₀ : B.Contains X₀) (pX₀ : X₀ ⟶ Spec (.of (S.residueField s)))
    (ι : yoneda.obj (integerSiteObject B hZ hX₀) ⟶ F.total.obj)
    (hι : IsPullback ι (yoneda.map (integerSiteMap B hZ hX₀
        (BigFppfSite.residueField_spec_contains B hS s) pX₀)) (F.toBaseYonedaOfEq hF)
      (yoneda.map (integerSiteMap B hZ (BigFppfSite.residueField_spec_contains B hS s) hS
        (S.fromSpecResidueField s))))
    {Y₀ : Scheme.{u}} (pY₀ : Y₀ ⟶ Spec (.of (S.residueField s))) [IsProper pY₀]
    (h₀ : X₀ ⟶ Y₀) (hh₀ : h₀ ≫ pY₀ = pX₀)
    (h0 : IsIso (C := Y₀.Modules) (Scheme.Modules.unitToPushforwardUnit h₀))
    (hR1 : IsZero (((Scheme.Modules.pushforward h₀).rightDerived 1).obj
      (SheafOfModules.unit X₀.ringCatSheaf))) :
    ∃ U : EtaleNeighborhood S s, U.IsElementary ∧
      ∃ (hU : B.Contains U.scheme) (t : Spec (.of (S.residueField s)) ⟶ U.scheme),
        t ≫ U.toBase = S.fromSpecResidueField s ∧ (∀ x, t x = U.point) ∧
        ∃ (G : CurveFamily B hZ) (hG : G.base = integerSiteObject B hZ hU)
          (h : ((F.ofBaseEq hF).pullback (integerSiteMap B hZ hU hS U.toBase)).total.obj ⟶
            G.total.obj),
          h ≫ G.toBaseYonedaOfEq hG =
            ((F.ofBaseEq hF).pullback (integerSiteMap B hZ hU hS U.toBase)).toBaseYoneda ∧
          ∃ ιU : yoneda.obj (integerSiteObject B hZ hX₀) ⟶
              ((F.ofBaseEq hF).pullback (integerSiteMap B hZ hU hS U.toBase)).total.obj,
            ιU ≫ ((F.ofBaseEq hF).pullbackHom
              (integerSiteMap B hZ hU hS U.toBase)).totalMap.hom = ι ∧
            IsPullback ιU (yoneda.map (integerSiteMap B hZ hX₀
                (BigFppfSite.residueField_spec_contains B hS s) pX₀))
              ((F.ofBaseEq hF).pullback (integerSiteMap B hZ hU hS U.toBase)).toBaseYoneda
              (yoneda.map (integerSiteMap B hZ (BigFppfSite.residueField_spec_contains B hS s)
                hU t)) ∧
            ∃ j : yoneda.obj (integerSiteObject B hZ
                (Scheme.size_lt_of_locallyOfFiniteType_of_quasiCompact pY₀
                  (BigFppfSite.residueField_spec_contains B hS s))) ⟶ G.total.obj,
              IsPullback j (yoneda.map (integerSiteMap B hZ
                  (Scheme.size_lt_of_locallyOfFiniteType_of_quasiCompact pY₀
                    (BigFppfSite.residueField_spec_contains B hS s))
                  (BigFppfSite.residueField_spec_contains B hS s) pY₀))
                (G.toBaseYonedaOfEq hG)
                (yoneda.map (integerSiteMap B hZ (BigFppfSite.residueField_spec_contains B hS s)
                  hU t)) ∧
              ιU ≫ h = yoneda.map (integerSiteMap B hZ hX₀
                (Scheme.size_lt_of_locallyOfFiniteType_of_quasiCompact pY₀
                  (BigFppfSite.residueField_spec_contains B hS s)) h₀) ≫ j
```

## Tag 0E8A, a lemma

[Tag 0E8A](https://stacks.math.columbia.edu/tag/0E8A) in the Stacks Project.

**`AlgebraicGeometry.CurveFamily.exists_stabilization_and_existsUnique_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PrestableStabilizationTheorem.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PrestableStabilizationTheorem.lean#L68). The attribute's comment: “Existence and uniqueness in one statement. `X ⟶ S` is a prestable family of curves whose fibres over all field-valued points have genus `g ≥ 2` (`HasFibresOfGenus`, the genus of a prestable family, Stacks 0E6V). The factorization `X ⟶ Y ⟶ S` is a family of curves `Y` over `S` (same base, `hb`) with `c ≫ g = f`. Condition (1) is `IsUniversalStructureContraction`: for every scheme `S' ⟶ S` of the site and the base change `c' : X' ⟶ Y'`, `𝒪_{Y'} ⟶ c'_*𝒪_{X'}` is an isomorphism and `R¹c'_*𝒪_{X'} = 0` (S' = S gives the condition for c). Condition (2) is `HasStableContractionFibres`, asserted at every field-valued point of `S` (so at every `s ∈ S` through `Spec κ(s)`): the fibre `c_s` satisfies the three conditions of Stacks 0E7Q, which characterize the contraction of rational tails and bridges of Section 0E7N up to unique isomorphism (`exists_isStableContraction_comp_tails_bridges`). Uniqueness up to unique isomorphism: for any two such `cᵢ : X ⟶ Yᵢ` (the targets need not be assumed stable) there is exactly one isomorphism `e : Y₁ ≅ Y₂` over `S` with `c₁ ≫ e = c₂`.”.

> Let `X ⟶ S` be a prestable family of curves of genus `g ≥ 2`. Then there are a stable family
> of curves `Y ⟶ S` and a morphism `c : X ⟶ Y` over `S` such that
>
> 1. `𝒪_Y = c_*𝒪_X` and `R¹c_*𝒪_X = 0`, and this remains true after base change by any morphism
>    `S' ⟶ S`, and
> 2. for every field-valued point `s` of `S` the morphism `c_s : X_s ⟶ Y_s` is the contraction of
>    rational tails and bridges (it satisfies the conditions of Stacks 0E7Q characterizing it).
>
> Moreover `c` is unique up to unique isomorphism: for any two morphisms `cᵢ : X ⟶ Yᵢ` over `S` to
> families of curves satisfying (1) and (2) there is exactly one isomorphism `e : Y₁ ≅ Y₂` over `S`
> with `c₁ ≫ e = c₂`.

```lean
theorem exists_stabilization_and_existsUnique_iso
    {X : CurveFamily B hZ} (hX : IsPrestableCurveFamily B hZ X) {g : ℕ} (hg : 2 ≤ g)
    (hgen : X.HasFibresOfGenus g) :
    (∃ (Y : CurveFamily B hZ) (hb : Y.base = X.base) (c : X.total ⟶ Y.total),
      IsStableCurveFamily B hZ Y ∧ c ≫ Y.toBase ≫ eqToHom (congrArg schemeSpace hb) = X.toBase ∧
      X.IsUniversalStructureContraction B hZ Y hb c ∧ X.HasStableContractionFibres B hZ Y hb c) ∧
    ∀ (Y₁ Y₂ : CurveFamily B hZ) (hb₁ : Y₁.base = X.base) (hb₂ : Y₂.base = X.base)
      (c₁ : X.total ⟶ Y₁.total) (c₂ : X.total ⟶ Y₂.total),
      c₁ ≫ Y₁.toBase ≫ eqToHom (congrArg schemeSpace hb₁) = X.toBase →
      c₂ ≫ Y₂.toBase ≫ eqToHom (congrArg schemeSpace hb₂) = X.toBase →
      X.IsUniversalStructureContraction B hZ Y₁ hb₁ c₁ →
      X.IsUniversalStructureContraction B hZ Y₂ hb₂ c₂ →
      X.HasStableContractionFibres B hZ Y₁ hb₁ c₁ → X.HasStableContractionFibres B hZ Y₂ hb₂ c₂ →
      ∃! e : Y₁.total ≅ Y₂.total, c₁ ≫ e.hom = c₂ ∧
        e.hom ≫ Y₂.toBase ≫ eqToHom (congrArg schemeSpace hb₂) =
          Y₁.toBase ≫ eqToHom (congrArg schemeSpace hb₁)
```

## Tag 0E8B, a lemma

[Tag 0E8B](https://stacks.math.columbia.edu/tag/0E8B) in the Stacks Project.

**`AlgebraicGeometry.stabilizationMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ModuliStabilization.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/ModuliStabilization.lean#L103). The attribute's comment: “the stabilization morphism Curves^\{prestable}\_g → Mbar\_g”.

> For `g ≥ 2`, the stabilization morphism `Curves^{prestable}_g ⟶ 𝓜̄_g` of stacks over `ℤ`, a
> 1-morphism of categories fibred in groupoids over the big fppf site of `Spec(ℤ)`. It sends a
> prestable family of curves `X → S` of genus `g` to the stable family `Y → S` of Stacks 0E8A
> (`AlgebraicGeometry.stabilizationMorphism_obj`).

```lean
def stabilizationMorphism (g : ℕ) (hg : 2 ≤ g) :
    curvesPrestableOfGenus B hZ g ⟶ moduliStableCurvesOfGenus B hZ g
```

**`AlgebraicGeometry.stabilizationMorphism_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ModuliStabilization.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/ModuliStabilization.lean#L115). The attribute's comment: “it sends a prestable family X → S of genus g to its stable model Y → S of 0E8A”.

> The stabilization morphism sends a prestable family of curves `X → S` of genus `g ≥ 2` to a
> stable family `Y → S` over the same base together with a morphism `c : X → Y` over `S` which is the
> stable model of Stacks 0E8A: `Y` is stable with fibres of genus `g`, `𝒪_Y = c_*𝒪_X` and
> `R¹c_*𝒪_X = 0` after every base change, and on every fibre `c` is the contraction of rational tails
> and bridges.

```lean
theorem stabilizationMorphism_obj (g : ℕ) (hg : 2 ≤ g)
    (X : (curvesPrestableOfGenus B hZ g).val.obj) :
    ∃ (h : ((stabilizationMorphism B hZ g hg).hom.obj X).obj.base = X.obj.base)
      (c : X.obj.total ⟶ ((stabilizationMorphism B hZ g hg).hom.obj X).obj.total),
      IsStableModel B hZ g (eqToHom h.symm) c
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.23, Tag 0E7B](https://stacks.math.columbia.edu/tag/0E7B)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
