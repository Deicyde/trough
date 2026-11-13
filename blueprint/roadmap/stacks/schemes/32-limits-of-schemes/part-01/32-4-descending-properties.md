---
declaration: section
origin: cited
lean: AlgebraicGeometry.preservesLimit_forget_of_isCofiltered_of_isAffineHom, AlgebraicGeometry.preservesLimit_forgetToTop_of_isCofiltered_of_isAffineHom, AlgebraicGeometry.existsUnique_mem_closure_singleton_of_compatible, AlgebraicGeometry.exists_isLimit_reducedClosures, AlgebraicGeometry.residueField_isColimit, AlgebraicGeometry.SmallDescentSituation, AlgebraicGeometry.nonempty_isLimit_forget_mapCone, AlgebraicGeometry.nonempty_isLimit_forgetToTop_mapCone
statement: formalized
proof: formalized
---

# 32.4 Descending properties

Section 32.4 of the Stacks Project, [Tag 081A](https://stacks.math.columbia.edu/tag/081A). 19 tags here are carried by 29 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CUE, a lemma

[Tag 0CUE](https://stacks.math.columbia.edu/tag/0CUE) in the Stacks Project.

**`AlgebraicGeometry.preservesLimit_forget_of_isCofiltered_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/Descending/UnderlyingSpace.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/Descending/UnderlyingSpace.lean#L142).

> Passing to underlying sets preserves the limit of a cofiltered diagram of schemes with
> affine transition morphisms.

```lean
theorem preservesLimit_forget_of_isCofiltered_of_isAffineHom
    {I : Type u} [Category.{u} I] [IsCofiltered I] (D : I ⥤ Scheme.{u})
    [∀ {i j : I} (f : i ⟶ j), IsAffineHom (D.map f)] :
    PreservesLimit D Scheme.forget
```

## Tag 0CUF, a lemma

[Tag 0CUF](https://stacks.math.columbia.edu/tag/0CUF) in the Stacks Project.

**`AlgebraicGeometry.preservesLimit_forgetToTop_of_isCofiltered_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/Descending/UnderlyingSpace.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/Descending/UnderlyingSpace.lean#L98). References: EGA IV (8.2.9).

> Passing to underlying topological spaces preserves the limit of a cofiltered diagram of
> schemes with affine transition morphisms.

```lean
theorem preservesLimit_forgetToTop_of_isCofiltered_of_isAffineHom
    {I : Type u} [Category.{u} I] [IsCofiltered I]
    (D : I ⥤ Scheme.{u})
    [∀ {i j : I} (f : i ⟶ j), IsAffineHom (D.map f)] :
    PreservesLimit D Scheme.forgetToTop
```

## Tag 0CUG, a lemma

[Tag 0CUG](https://stacks.math.columbia.edu/tag/0CUG) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_mem_closure_singleton_of_compatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/Descending/PointClosure.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/Descending/PointClosure.lean#L59). The attribute's comment: “closures\_sets”.

> **Stacks Project, Tag 0CUG.** The closure of a point in a cofiltered limit of schemes with
> affine transition morphisms is the inverse limit, as a set, of the closures of its images.

```lean
theorem existsUnique_mem_closure_singleton_of_compatible
    {I : Type u} [Category.{u} I] [IsCofiltered I]
    (D : I ⥤ Scheme.{u})
    [∀ {i j : I} (f : i ⟶ j), IsAffineHom (D.map f)]
    (c : Cone D) (hc : IsLimit c) (s : c.pt)
    (x : ∀ i, D.obj i)
    (hx : ∀ ⦃i j : I⦄ (f : i ⟶ j), D.map f (x i) = x j)
    (hx_closure : ∀ i, x i ∈ closure ({c.π.app i s} : Set (D.obj i))) :
    ∃! y : c.pt, y ∈ closure ({s} : Set c.pt) ∧ ∀ i, c.π.app i y = x i
```

**`AlgebraicGeometry.exists_isLimit_reducedClosures`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/Descending/PointClosure.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/Descending/PointClosure.lean#L262). The attribute's comment: “closures\_schemes”.

> **Stacks Project, Tag 0CUG.** The reduced closure of a point of a cofiltered limit of
> schemes is the limit, as a scheme, of the reduced closures of its images.

```lean
theorem exists_isLimit_reducedClosures
    {I : Type u} [Category.{u} I] [IsCofiltered I]
    (D : I ⥤ Scheme.{u})
    [∀ {i j : I} (f : i ⟶ j), IsAffineHom (D.map f)]
    (c : Cone D) (hc : IsLimit c) (s : c.pt) :
    ∃ (E : I ⥤ Scheme.{u}) (ι : E ⟶ D) (c' : Cone E)
      (e : c'.pt ≅ (Scheme.IdealSheafData.vanishingIdeal
        (Closeds.closure ({s} : Set c.pt))).subscheme),
      (∀ i, ∃ eᵢ : E.obj i ≅ (Scheme.IdealSheafData.vanishingIdeal
        (Closeds.closure ({c.π.app i s} : Set (D.obj i)))).subscheme,
        eᵢ.hom ≫ (Scheme.IdealSheafData.vanishingIdeal
          (Closeds.closure ({c.π.app i s} : Set (D.obj i)))).subschemeι = ι.app i) ∧
      (∀ i, c'.π.app i ≫ ι.app i =
        e.hom ≫ (Scheme.IdealSheafData.vanishingIdeal
          (Closeds.closure ({s} : Set c.pt))).subschemeι ≫ c.π.app i) ∧
      Nonempty (IsLimit c')
```

**`AlgebraicGeometry.residueField_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/Descending/ResidueField.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/Descending/ResidueField.lean#L100). The attribute's comment: “residue\_fields”.

> **Stacks Project, Tag 0CUG.** The residue field of a point in a cofiltered limit of schemes
> with affine transition morphisms is the filtered colimit of the residue fields of its images.

```lean
theorem residueField_isColimit
    {I : Type u} [Category.{u} I] [IsCofiltered I]
    (D : I ⥤ Scheme.{u})
    [∀ {i j : I} (f : i ⟶ j), IsAffineHom (D.map f)]
    (c : Cone D) (hc : IsLimit c) (s : c.pt)
    (K : Iᵒᵖ ⥤ CommRingCat.{u})
    (e : ∀ i : I,
      K.obj (Opposite.op i) ≅ (D.obj i).residueField (c.π.app i s))
    (hK : ∀ {i j : I} (f : i ⟶ j),
      K.map f.op =
        (e j).hom ≫
          ((D.obj j).residueFieldCongr (by
            symm
            change (c.π.app i ≫ D.map f) s = _
            rw [c.w f])).hom ≫
          (D.map f).residueFieldMap (c.π.app i s) ≫ (e i).inv) :
    ∀ (T : CommRingCat.{u})
      (φ : ∀ i : I, K.obj (Opposite.op i) ⟶ T),
      (∀ {i j : I} (f : i ⟶ j), K.map f.op ≫ φ i = φ j) →
      ∃! ψ : c.pt.residueField s ⟶ T,
        ∀ i : I, (e i).hom ≫ (c.π.app i).residueFieldMap s ≫ ψ = φ i
```

## Tag 086P, a situation

[Tag 086P](https://stacks.math.columbia.edu/tag/086P) in the Stacks Project.

**`AlgebraicGeometry.SmallDescentSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/Descending/DescentSituation.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/Descending/DescentSituation.lean#L69).

> **Situation 086P.** A directed inverse system `(S_i)_{i ∈ I}` of quasi-compact and
> quasi-separated schemes with affine transition morphisms, indexed by a directed *set* `I`,
> together with its limit `S = lim S_i`, the projections `f_i : S ⟶ S_i`, and a chosen element
> `0 ∈ I`.
>
> The source's directed set is a set, which here means that the index preorder is `u`-small,
> `u` being the universe of the schemes: the field `small`. For such an index the limit of
> Stacks 01YX, glued from the affine-locally computed limits, is the categorical limit in
> `Scheme.{u}`, and the chosen limit cone of the underlying
> `AlgebraicGeometry.DescentSituation` records it with its projections. Without the bound the
> categorical limit in `Scheme.{u}` of a large system need not be that scheme; see
> `StacksFrontier/AlgebraicGeometry/SmallnessNecessary/Basic.lean`. Nonemptiness of `I` is
> witnessed by the chosen element `base`.

```lean
structure SmallDescentSituation (I : Type v) [Preorder I] [IsDirected I (· ≤ ·)]
    extends DescentSituation.{v, u} I
```

## Tag 01YY, a lemma

[Tag 01YY](https://stacks.math.columbia.edu/tag/01YY) in the Stacks Project.

**`AlgebraicGeometry.nonempty_isLimit_forget_mapCone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/Descending/DescentSituation.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/Descending/DescentSituation.lean#L131). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 01YY, part (1).** The underlying-set cone of the chosen limit in the
> descent situation is a limit cone.

```lean
theorem nonempty_isLimit_forget_mapCone
    {I : Type v} [Small.{u} I] [Preorder I] [IsDirected I (· ≤ ·)]
    (D : DescentSituation.{v, u} I) :
    Nonempty (IsLimit (Scheme.forget.mapCone D.limitCone))
```

**`AlgebraicGeometry.nonempty_isLimit_forgetToTop_mapCone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/Descending/DescentSituation.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/Descending/DescentSituation.lean#L141). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 01YY, part (2).** The underlying topological-space cone of the chosen
> limit in the descent situation is a limit cone.

```lean
theorem nonempty_isLimit_forgetToTop_mapCone
    {I : Type v} [Small.{u} I] [Preorder I] [IsDirected I (· ≤ ·)]
    (D : DescentSituation.{v, u} I) :
    Nonempty (IsLimit (Scheme.forgetToTop.mapCone D.limitCone))
```

**`AlgebraicGeometry.exists_not_specializes_map_of_not_specializes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/Descending/DescentSituation.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/Descending/DescentSituation.lean#L152). The attribute's comment: “part (3)”.

> **Stacks Project, Tag 01YY, part (3).** If one point of the limiting scheme does not
> specialize to another, this failure is detected after projection to one of the schemes in the
> inverse system.

```lean
theorem exists_not_specializes_map_of_not_specializes
    {I : Type v} [Small.{u} I] [Preorder I] [IsDirected I (· ≤ ·)]
    (D : DescentSituation.{v, u} I)
    (s s' : D.limitCone.pt) (h : ¬Specializes s s') :
    ∃ i : I, ¬Specializes
      (D.limitCone.π.app (Opposite.op i) s)
      (D.limitCone.π.app (Opposite.op i) s')
```

## Tag 01Z0, a lemma

[Tag 01Z0](https://stacks.math.columbia.edu/tag/01Z0) in the Stacks Project.

**`AlgebraicGeometry.isStagesColimit_stagePullbackSection_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ModuleLimits/SectionsColimitFinitePresentation.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ModuleLimits/SectionsColimitFinitePresentation.lean#L184). The attribute's comment: “for a module of finite presentation on the base stage, with the index set in the universe of the schemes”. References: EGA IV (8.5.2), “(i), special case”; EGA IV (8.5.4), “special case”.

> **[Stacks Project, Tag 01Z0] for a module of finite presentation on the base stage.** Let
> `E` be a directed inverse system of quasi-compact and quasi-separated schemes with affine
> transition morphisms, let `c` be a limit cone on it, let `0` be a chosen index and let `ℱ₀` be a
> module of **finite presentation** on `S₀ = E.obj (op 0)`.  Setting `ℱᵢ = f_{i0}⁺ℱ₀` for `i ≥ 0`
> and `ℱ = f_0⁺ℱ₀`, the group `Γ(S, ℱ)` is the filtered colimit of the `Γ(Sᵢ, ℱᵢ)`, in the
> elementwise form `Stacks.IsStagesColimit`: the maps to `Γ(S, ℱ)` are compatible with the
> transition maps, every global section at the limit comes from a stage, and two global sections at
> one stage with the same image at the limit already agree at a later stage.
>
> The three clauses are, in order,
> `Stacks.AlgebraicGeometry.ModuleLimits.sectionsMap_canHom_modulePullbackSection_comp`,
> `Stacks.AlgebraicGeometry.ModuleLimits.exists_canonical_section_eq_of_isLimit` and
> `...ModuleLimits.exists_canonical_section_eq_of_canonical_section_eq_of_isLimit`
> — the cocone law for the canonical identification of an iterated pullback with the pullback along
> the composite, and the surjectivity and injectivity halves, both of which read a global section
> of a module as a morphism out of the structure sheaf and then apply [Stacks Project, Tag 01ZR],
> (2) and (3) respectively.  That is why the coefficients are restricted to a module of finite
> presentation: Tag 01ZR is a statement about finitely presented modules.
>
> The tag is keyed because this is only part of Stacks 01Z0: the coefficient module is of finite
> presentation and not merely quasi-coherent.  The whole tag is
> `AlgebraicGeometry.isStagesColimit_stagePullbackSection_of_isQuasicoherent` in
> `StacksFrontier/AlgebraicGeometry/ModuleLimits/SectionsColimitQuasiCoherent.lean`, which is this
> statement interchanged with [Stacks Project, Tag 01PJ].  The index set lies in the universe of
> the schemes, which is not a restriction that may be dropped —
> `Stacks.LimitSectionsIdentification.not_card_01Z0` refutes the statement over an index set one
> universe up.

```lean
theorem isStagesColimit_stagePullbackSection_of_isFinitePresentation
    [∀ {i j : αᵒᵖ} (f : i ⟶ j), IsAffineHom (E.map f)]
    [∀ i : αᵒᵖ, CompactSpace (E.obj i)] [∀ i : αᵒᵖ, QuasiSeparatedSpace (E.obj i)]
    (c : Cone E) (hc : IsLimit c) (a₀ : α) (F₀ : (E.obj (op a₀)).Modules)
    (hF₀ : F₀.IsFinitePresentation) :
    Stacks.IsStagesColimit
      (fun (a b : {a : α // a₀ ≤ a}) (h : a ≤ b) =>
        stagePullbackSectionTransition E a.2 b.2 (Subtype.coe_le_coe.mpr h) F₀)
      (fun a : {a : α // a₀ ≤ a} => stagePullbackSectionProjection E a.2 F₀ c)
```

**`AlgebraicGeometry.isStagesColimit_stagePullbackSection_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ModuleLimits/SectionsColimitQuasiCoherent.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ModuleLimits/SectionsColimitQuasiCoherent.lean#L199). References: EGA IV (8.5.4).

> **[Stacks Project, Tag 01Z0].** Let `E` be a directed inverse system of quasi-compact and
> quasi-separated schemes with affine transition morphisms, let `c` be a limit cone on it, let `0`
> be a chosen index and let `ℱ₀` be a **quasi-coherent** module on `S₀ = E.obj (op 0)`.  Setting
> `ℱᵢ = f_{i0}⁺ℱ₀` for `i ≥ 0` and `ℱ = f_0⁺ℱ₀`, the group `Γ(S, ℱ)` is the filtered colimit of the
> `Γ(Sᵢ, ℱᵢ)`, in the elementwise form `Stacks.IsStagesColimit`: the maps to `Γ(S, ℱ)` are
> compatible with the transition maps, every global section at the limit comes from a stage, and
> two global sections at one stage with the same image at the limit already agree at a later stage.
>
> The finite-presentation case is
> `AlgebraicGeometry.isStagesColimit_stagePullbackSection_of_isFinitePresentation`, and this is it
> interchanged with the presentation of a quasi-coherent module as a filtered colimit of finitely
> presented ones, [Stacks Project, Tag 01PJ]; see the file's implementation notes.
>
> The index set lies in the universe of the schemes, which is not a restriction that may be
> dropped — `Stacks.LimitSectionsIdentification.not_card_01Z0` refutes the statement over an index
> set one universe up, so a `u`-small directed index set is exactly the source's "directed set".

```lean
theorem isStagesColimit_stagePullbackSection_of_isQuasicoherent
    [∀ {i j : αᵒᵖ} (f : i ⟶ j), IsAffineHom (E.map f)]
    [∀ i : αᵒᵖ, CompactSpace (E.obj i)] [∀ i : αᵒᵖ, QuasiSeparatedSpace (E.obj i)]
    (c : Cone E) (hc : IsLimit c) (a₀ : α) (F₀ : (E.obj (op a₀)).Modules)
    (hF₀ : F₀.IsQuasicoherent) :
    Stacks.IsStagesColimit
      (fun (a b : {a : α // a₀ ≤ a}) (h : a ≤ b) =>
        stagePullbackSectionTransition E a.2 b.2 (Subtype.coe_le_coe.mpr h) F₀)
      (fun a : {a : α // a₀ ≤ a} => stagePullbackSectionProjection E a.2 F₀ c)
```

**`AlgebraicGeometry.isStagesColimit_appTop_of_isAffine_of_isLimit_of_directed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/SectionsColimitDescent.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/SectionsColimitDescent.lean#L254). The attribute's comment: “for the structure sheaf over a directed inverse system of affine schemes, with the index set in the universe of the schemes”. References: EGA IV (8.5.4), “special case”; SGA 3 VIB (10.0), “(i), special case”.

> **The ring of global sections of a limit of affine schemes is the filtered colimit of the
> rings of global sections of the stages**, in the elementwise form `Stacks.IsStagesColimit`: the
> transition maps are the pullbacks of global sections along the morphisms of the inverse system
> and the maps to the vertex are the pullbacks along the projections of the limiting cone.

```lean
theorem isStagesColimit_appTop_of_isAffine_of_isLimit_of_directed :
    Stacks.IsStagesColimit (G := fun a : α => (Γ(E.obj (op a), ⊤) : Type u))
      (T := (Γ(c.pt, ⊤) : Type u))
      (fun (a b : α) (h : a ≤ b) x => (E.map (homOfLE h).op).appTop.hom x)
      (fun (a : α) x => (c.π.app (op a)).appTop.hom x)
```

**`AlgebraicGeometry.isStagesColimit_appTop_of_isLimit_of_directed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/SectionsColimitDescent.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/SectionsColimitDescent.lean#L284). The attribute's comment: “for the structure sheaf over a directed inverse system of quasi-compact quasi-separated schemes with affine transition morphisms, with the index set in the universe of the schemes”. References: EGA IV (8.5.4), “structure sheaf”.

> **The ring of global sections of a limit of quasi-compact quasi-separated schemes with
> affine transition morphisms is the filtered colimit of the rings of global sections of the
> stages**, in the elementwise form `Stacks.IsStagesColimit`: the transition maps are the
> pullbacks of global sections along the morphisms of the inverse system and the maps to the
> vertex are the pullbacks along the projections of the limiting cone.

```lean
theorem isStagesColimit_appTop_of_isLimit_of_directed :
    Stacks.IsStagesColimit (G := fun a : α => (Γ(E.obj (op a), ⊤) : Type u))
      (T := (Γ(c.pt, ⊤) : Type u))
      (fun (a b : α) (h : a ≤ b) x => (E.map (homOfLE h).op).appTop.hom x)
      (fun (a : α) x => (c.π.app (op a)).appTop.hom x)
```

## Tag 05F3, a lemma

[Tag 05F3](https://stacks.math.columbia.edu/tag/05F3) in the Stacks Project.

**`AlgebraicGeometry.eventually_isEmpty_pullback`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/Descending/ConstructibleImage.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/Descending/ConstructibleImage.lean#L56). References: EGA IV (8.3.6), “Nontrivial direction”.

> **Stacks Project, Tag 05F3.** If the base change of a quasi-compact scheme to the limit of a
> directed inverse system is empty, then its base change to every sufficiently late stage is
> empty.

```lean
lemma eventually_isEmpty_pullback
    {I : Type u} [Preorder I] [IsDirected I (· ≤ ·)]
    (D : DescentSituation.{u, u} I)
    (T : Scheme.{u}) [CompactSpace T]
    (t : T ⟶ D.system.obj (Opposite.op D.base))
    (hT : IsEmpty
      (pullback t (D.limitCone.π.app (Opposite.op D.base)) : Scheme)) :
    ∀ᶠ i in Filter.atTop, ∀ h : D.base ≤ i,
      IsEmpty (pullback t (D.system.map (homOfLE h).op) : Scheme)
```

## Tag 05F4, a lemma

[Tag 05F4](https://stacks.math.columbia.edu/tag/05F4) in the Stacks Project.

**`AlgebraicGeometry.eventually_range_transition_subset_of_isLocallyConstructible`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/Descending/ConstructibleImage.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/Descending/ConstructibleImage.lean#L123).

> **Stacks Project, Tag 05F4.** A locally constructible subset of a stage in a directed inverse
> system contains the images of all sufficiently large stages if it contains the image of the
> limit.

```lean
lemma eventually_range_transition_subset_of_isLocallyConstructible
    {I : Type u} [Preorder I] [IsDirected I (· ≤ ·)]
    (D : DescentSituation.{u, u} I)
    (E : Set (D.system.obj (op D.base)))
    (hE : Topology.IsLocallyConstructible E)
    (hlim : Set.range (D.limitCone.π.app (op D.base)).base ⊆ E) :
    ∀ᶠ i in atTop, ∃ h : D.base ≤ i,
      Set.range (D.system.map (homOfLE h).op).base ⊆ E
```

## Tag 01Z4, a lemma

[Tag 01Z4](https://stacks.math.columbia.edu/tag/01Z4) in the Stacks Project.

**`AlgebraicGeometry.exists_map_preimage_eq_map_preimage_of_preimage_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LimitSituation.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/LimitSituation.lean#L178). The attribute's comment: “(2)”.

> **Stacks 01Z4, part (2).** Let `X = lim X_i` be the limit of a cofiltered inverse system
> of schemes with affine transition morphisms. If quasi-compact opens `U ⊆ X_i` and
> `V ⊆ X_{i'}` have the same inverse image in `X`, then there are transition morphisms
> `X_j ⟶ X_i` and `X_j ⟶ X_{i'}` along which `U` and `V` have the same inverse image in `X_j`.
>
> The source asks the stages to be quasi-compact and quasi-separated as well (Situation 086P);
> that is not used. Both opens are first pulled back to a stage `k` mapping to `i` and `i'`
> (`CategoryTheory.IsCofilteredOrEmpty.cone_objs`), where they are again quasi-compact since affine
> morphisms are quasi-compact, and the single-stage case
> `AlgebraicGeometry.exists_map_preimage_eq_map_preimage'` applies there.

```lean
theorem exists_map_preimage_eq_map_preimage_of_preimage_eq {I : Type u} [Category.{v} I]
    [IsCofiltered I] (D : I ⥤ Scheme.{u}) (c : Cone D) (hc : IsLimit c)
    [∀ {i j : I} (f : i ⟶ j), IsAffineHom (D.map f)] {i i' : I} {U : (D.obj i).Opens}
    {V : (D.obj i').Opens} (hU : IsCompact (U : Set (D.obj i)))
    (hV : IsCompact (V : Set (D.obj i'))) (H : c.π.app i ⁻¹ᵁ U = c.π.app i' ⁻¹ᵁ V) :
    ∃ (j : I) (f : j ⟶ i) (f' : j ⟶ i'), D.map f ⁻¹ᵁ U = D.map f' ⁻¹ᵁ V
```

**`AlgebraicGeometry.exists_iSup_map_preimage_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LimitSituation.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/LimitSituation.lean#L209). The attribute's comment: “(3)”.

> **Stacks 01Z4, part (3).** Let `X = lim X_i` be the limit of a cofiltered inverse system
> of quasi-compact schemes with affine transition morphisms. If a family of opens of a stage
> `X_i` has inverse images in `X` covering `X`, then for some transition morphism
> `X_j ⟶ X_i` the inverse images of the family in `X_j` cover `X_j`.
>
> The source states this for a finite family of quasi-compact opens. Neither hypothesis is
> used: a preimage of opens commutes with arbitrary suprema, so the statement for the single
> open `⨆ k, V k` is the statement for the family. What the proof does use, and what
> Situation 086P provides, is that every stage is quasi-compact.
>
> The single-open case is Mathlib's `AlgebraicGeometry.exists_map_eq_top`, used here through
> `AlgebraicGeometry.exists_map_eq_top'`, its index-morphism-universe-free form, and the step
> from one open to a family is `AlgebraicGeometry.Scheme.Hom.preimage_iSup`. Mathlib records the
> tag for parts (1) and (2) on `AlgebraicGeometry.exists_preimage_eq` and
> `AlgebraicGeometry.exists_map_preimage_eq_map_preimage`; its `exists_map_eq_top` carries no
> tag, so part (3) is recorded here.

```lean
theorem exists_iSup_map_preimage_eq_top {I : Type u} [Category.{v} I] [IsCofiltered I]
    (D : I ⥤ Scheme.{u}) (c : Cone D) (hc : IsLimit c)
    [∀ {i j : I} (f : i ⟶ j), IsAffineHom (D.map f)] [∀ i : I, CompactSpace (D.obj i)]
    {i : I} {ι : Type*} (V : ι → (D.obj i).Opens)
    (hV : (⨆ k, c.π.app i ⁻¹ᵁ V k) = ⊤) :
    ∃ (j : I) (f : j ⟶ i), (⨆ k, D.map f ⁻¹ᵁ V k) = ⊤
```

## Tag 01Z5, a lemma

[Tag 01Z5](https://stacks.math.columbia.edu/tag/01Z5) in the Stacks Project.

**`AlgebraicGeometry.Scheme.exists_forall_isQuasiAffine_of_isLimit`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LimitQuasiAffine/Eventually.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LimitQuasiAffine/Eventually.lean#L42). The attribute's comment: “Stated for a cofiltered index category; `i ⟶ i₀` plays the role of `i ≥ i₀`.”.

> Suppose `{ Xᵢ }` is a cofiltered inverse system of quasi-compact quasi-separated schemes with
> affine transition maps. If `lim Xᵢ` is quasi-affine, then there is an index `i₀` such that `Xᵢ`
> is quasi-affine for every `i ⟶ i₀`.

```lean
lemma Scheme.exists_forall_isQuasiAffine_of_isLimit [IsCofiltered I]
    [∀ {i j} (f : i ⟶ j), IsAffineHom (D.map f)]
    [∀ (i : I), CompactSpace (D.obj i)]
    [∀ (i : I), QuasiSeparatedSpace (D.obj i)]
    [IsQuasiAffine c.pt] :
    ∃ i₀, ∀ i (_ : i ⟶ i₀), IsQuasiAffine (D.obj i)
```

## Tag 01Z6, a lemma

[Tag 01Z6](https://stacks.math.columbia.edu/tag/01Z6) in the Stacks Project.

**`AlgebraicGeometry.eventually_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/Descending/Affine.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/Descending/Affine.lean#L64). The attribute's comment: “for an index preorder essentially small in the scheme universe”. References: SGA 4 VII (5.4), “partial”.

> **Stacks Project, Tag 01Z6.** In a directed inverse system of quasi-compact and
> quasi-separated schemes with affine transition morphisms, if the limit is affine then every
> sufficiently late stage is affine.

```lean
theorem eventually_isAffine
    {I : Type v} [Preorder I] [IsDirected I (· ≤ ·)]
    [EssentiallySmall.{u} I]
    (d : DescentSituation.{v, u} I)
    [IsAffine d.limitCone.pt] :
    ∃ i₀ : I, ∀ i : I, i₀ ≤ i → IsAffine (d.system.obj (op i))
```

## Tag 086Q, a lemma

[Tag 086Q](https://stacks.math.columbia.edu/tag/086Q) in the Stacks Project.

**`AlgebraicGeometry.eventually_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/Descending/Separated.lean, line 579](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/Descending/Separated.lean#L579).

> **Stacks Project, Tag 086Q.** In a directed inverse system of quasi-compact and
> quasi-separated schemes with affine transition morphisms, if the limit is separated then every
> sufficiently late stage is separated.

```lean
theorem eventually_isSeparated
    {I : Type v} [Preorder I] [IsDirected I (· ≤ ·)]
    [EssentiallySmall.{u} I]
    (d : DescentSituation.{v, u} I)
    [d.limitCone.pt.IsSeparated] :
    ∃ i₀ : I, ∀ i : I, i₀ ≤ i → (d.system.obj (Opposite.op i)).IsSeparated
```

## Tag 09MT, a lemma

[Tag 09MT](https://stacks.math.columbia.edu/tag/09MT) in the Stacks Project.

**`Stacks.AlgebraicGeometry.AmpleLimit.exists_isAmple_pullback_map_of_isLimit_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleLimit/Unconditional.lean, line 511](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/AmpleLimit/Unconditional.lean#L511).

> **[Stacks Project, Tag 09MT].**  Let `c` be a limit cone on a cofiltered diagram `D` of
> quasi-compact quasi-separated schemes with affine transition morphisms and let `M` be an
> invertible module on the stage `D.obj j`.  If the pullback of `M` to `c.pt` is ample, then the
> pullback of `M` to some stage over `j` is ample.
>
> This is `exists_isAmple_pullback_map_of_isLimit` with its hypothesis `hdesc` discharged by
> `nonvanishingLocusDescent_of_isLimit`, which derives it from [Stacks Project, Tag 01ZR] (2).

```lean
theorem exists_isAmple_pullback_map_of_isLimit_of_qcqs (hc : IsLimit c) (j : I)
    (M : (D.obj j).Modules)
    [_root_.AlgebraicGeometry.SheafOfModules.IsInvertible (D.obj j).toRingedSpace.presheaf
      (structureSheafRing (D.obj j).toRingedSpace).property M]
    (hample : Scheme.Modules.IsAmple c.pt ((Scheme.Modules.pullback (c.π.app j)).obj M)) :
    ∃ (j' : I) (g : j' ⟶ j),
      Scheme.Modules.IsAmple (D.obj j') ((Scheme.Modules.pullback (D.map g)).obj M)
```

## Tag 081B, a lemma

[Tag 081B](https://stacks.math.columbia.edu/tag/081B) in the Stacks Project.

**`AlgebraicGeometry.EventualLimit.eventually_isClosedImmersion_comp_π_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EventualLimitProperties/ClosedImmersion.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EventualLimitProperties/ClosedImmersion.lean#L309). The attribute's comment: “part (1)”.

> **Stacks 081B (1).**  Let `X = lim Xᵢ` be the limit of a directed inverse system of
> quasi-compact schemes over `S` whose transition morphisms are affine.  If `f : Y ⟶ X` is a closed
> immersion and `Y` is locally of finite type over `S`, then the composite `Y ⟶ Xᵢ` is a closed
> immersion for all sufficiently large `i`.

```lean
theorem eventually_isClosedImmersion_comp_π_app
    (hcomm : c.π ≫ t = (Functor.const Iᵒᵖ).map s)
    [∀ i : I, CompactSpace (D.obj (op i))]
    [∀ ⦃i j : I⦄ (h : i ≤ j), IsAffineHom (D.map (homOfLE h).op)]
    [LocallyOfFiniteType (f ≫ s)] [IsClosedImmersion f] :
    ∀ᶠ i in atTop, IsClosedImmersion (f ≫ c.π.app (op i))
```

**`AlgebraicGeometry.EventualLimit.eventually_isImmersion_comp_π_app_of_quasiSeparatedSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EventualLimitProperties/Immersion.lean, line 465](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EventualLimitProperties/Immersion.lean#L465). The attribute's comment: “part (2)”.

> **Stacks 081B (2).** Let `X = lim Xᵢ` be the limit of a directed inverse system of schemes
> over `S` whose transition morphisms are affine and whose stages are quasi-separated. If
> `f : Y ⟶ X` is an immersion, `Y` is locally of finite type over `S`, and `Y` is quasi-compact,
> then the composite `Y ⟶ Xᵢ` is an immersion for all sufficiently large `i`.
>
> These are exactly the source's hypotheses, and the index type `I` is in a universe unrelated to
> that of the schemes.  `AlgebraicGeometry.EventualLimit.eventually_isImmersion_comp_π_app` drops
> the quasi-separatedness of the stages but ties `I` to the universe of the schemes, which is where
> Mathlib's `AlgebraicGeometry.exists_preimage_eq` applies.

```lean
theorem eventually_isImmersion_comp_π_app_of_quasiSeparatedSpace
    (hcomm : c.π ≫ t = (Functor.const Iᵒᵖ).map s)
    [∀ i : I, QuasiSeparatedSpace (D.obj (op i))]
    [∀ ⦃i j : I⦄ (h : i ≤ j), IsAffineHom (D.map (homOfLE h).op)]
    [LocallyOfFiniteType (f ≫ s)] [IsImmersion f] [CompactSpace Y] :
    ∀ᶠ i in atTop, IsImmersion (f ≫ c.π.app (op i))
```

**`AlgebraicGeometry.EventualLimit.eventually_isIso_comp_π_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EventualLimitProperties/Isomorphism.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EventualLimitProperties/Isomorphism.lean#L258). The attribute's comment: “eventually\_isomorphism”.

> **Stacks 081B (3)**, in the form in which the limit is presented through an isomorphism
> `f : Y ≅ lim Xᵢ`: the composites `Y ⟶ Xᵢ` are isomorphisms for all sufficiently large `i`.

```lean
theorem eventually_isIso_comp_π_app (hp : c.π ≫ t = (Functor.const Iᵒᵖ).map p)
    {Y : Scheme.{u}} (f : Y ⟶ c.pt) [IsIso f]
    [∀ i : I, CompactSpace (D.obj (op i))]
    [∀ i : I, LocallyOfFiniteType (t.app (op i))]
    [∀ ⦃i j : I⦄ (h : i ≤ j), IsClosedImmersion (D.map (homOfLE h).op)]
    [LocallyOfFinitePresentation (f ≫ p)] :
    ∀ᶠ i in atTop, IsIso (f ≫ c.π.app (op i))
```

## Tag 01ZH, a lemma

[Tag 01ZH](https://stacks.math.columbia.edu/tag/01ZH) in the Stacks Project.

**`AlgebraicGeometry.eventually_isSeparated_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/EventuallySeparatedOverBase.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/EventuallySeparatedOverBase.lean#L240).

> **Stacks Project, Tag 01ZH.** Let `S` be a quasi-separated scheme and let `X = lim X_i` be a
> directed inverse limit of quasi-compact and quasi-separated schemes over `S` with affine
> transition morphisms. If `X ⟶ S` is separated, then `X_i ⟶ S` is separated for all sufficiently
> large `i`.

```lean
theorem eventually_isSeparated_app {I : Type v} [Preorder I] [IsDirected I (· ≤ ·)]
    [EssentiallySmall.{u} I] (d : DescentSituation.{v, u} I) {S : Scheme.{u}}
    [QuasiSeparatedSpace S] (t : d.system ⟶ (Functor.const Iᵒᵖ).obj S)
    (hsep : IsSeparated (d.limitCone.π.app (op d.base) ≫ t.app (op d.base))) :
    ∃ i₀ : I, ∀ i : I, i₀ ≤ i → IsSeparated (t.app (op i))
```

## Tag 09ZM, a lemma

[Tag 09ZM](https://stacks.math.columbia.edu/tag/09ZM) in the Stacks Project.

**`AlgebraicGeometry.eventually_isAffineHom_of_isLimit_of_initiallySmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/EventuallyAffine.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/EventuallyAffine.lean#L240).

> `AlgebraicGeometry.eventually_isAffineHom_of_isLimit` with the index universes independent
> of the scheme universe, at the cost of `CategoryTheory.LocallySmall.{u}` and
> `CategoryTheory.InitiallySmall.{u}` on the index category. See the module documentation for why
> some such condition is necessary.

```lean
theorem eventually_isAffineHom_of_isLimit_of_initiallySmall (D : I ⥤ Scheme.{u})
    (t : D ⟶ (Functor.const I).obj S) (c : Cone D) (hc : IsLimit c) (f : c.pt ⟶ S)
    (hf : c.π ≫ t = (Functor.const I).map f)
    [∀ i, CompactSpace (D.obj i)] [∀ i, QuasiSeparatedSpace (D.obj i)]
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (D.map g)] [IsAffineHom f] :
    ∃ i : I, ∀ {j : I} (_ : j ⟶ i), IsAffineHom (t.app j)
```

## Tag 09ZN, a lemma

[Tag 09ZN](https://stacks.math.columbia.edu/tag/09ZN) in the Stacks Project.

**`AlgebraicGeometry.eventually_isFinite_of_isLimit_of_isIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EventualFiniteness/Basic.lean, line 371](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EventualFiniteness/Basic.lean#L371).

> **Stacks 09ZN** for a directed preorder.  In a directed inverse system of qcqs schemes over a
> qcqs scheme, if the transition morphisms are finite, the stages are locally of finite type over the
> base, and the limit is integral over the base, then the stages are eventually finite over the base.
>
> The index type is taken in the same universe as the schemes; see the module docstring.

```lean
theorem eventually_isFinite_of_isLimit_of_isIntegral
    {I : Type u} [Preorder I] [Nonempty I] [IsDirected I (· ≤ ·)]
    {S : Scheme.{u}} [CompactSpace S] [QuasiSeparatedSpace S]
    (F : Iᵒᵖ ⥤ Scheme.{u}) (p : F ⟶ (Functor.const Iᵒᵖ).obj S)
    (c : Cone F) (hc : IsLimit c) (f : c.pt ⟶ S)
    (hf : ∀ i, f = c.π.app (Opposite.op i) ≫ p.app (Opposite.op i))
    [IsIntegralHom f]
    [∀ i, CompactSpace (F.obj (Opposite.op i))]
    [∀ i, QuasiSeparatedSpace (F.obj (Opposite.op i))]
    (haffine : ∀ {i j : I} (h : i ≤ j),
      IsAffineHom (F.map (homOfLE h).op))
    (hfinite : ∀ {i j : I} (h : i ≤ j),
      IsFinite (F.map (homOfLE h).op))
    [∀ i, LocallyOfFiniteType (p.app (Opposite.op i))] :
    ∀ᶠ i in Filter.atTop, IsFinite (p.app (Opposite.op i))
```

## Tag 0A0N, a lemma

[Tag 0A0N](https://stacks.math.columbia.edu/tag/0A0N) in the Stacks Project.

**`AlgebraicGeometry.eventually_isClosedImmersion_app_of_isLimit_of_initiallySmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/EventuallyClosedImmersion.lean, line 427](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/EventuallyClosedImmersion.lean#L427).

> `AlgebraicGeometry.eventually_isClosedImmersion_app_of_isLimit` with the index universes
> independent of the scheme universe, at the cost of `CategoryTheory.LocallySmall.{u}` and
> `CategoryTheory.InitiallySmall.{u}` on the index category.
>
> This is the faithful rendering of Tag 0A0N: the source's limit is indexed by a directed set, so
> the index is small relative to the schemes and the smallness is part of the statement rather than
> an addition to it. See the module documentation, and compare
> `AlgebraicGeometry.eventually_isAffineHom_of_isLimit_of_initiallySmall` (Tag 09ZM), which carries
> the condition for the same reason and whose counterexample shows it cannot be dropped.

```lean
theorem eventually_isClosedImmersion_app_of_isLimit_of_initiallySmall (D : I ⥤ Scheme.{u})
    (t : D ⟶ (Functor.const I).obj S) (c : Cone D) (hc : IsLimit c) (f : c.pt ⟶ S)
    (hf : c.π ≫ t = (Functor.const I).map f)
    [CompactSpace S] [QuasiSeparatedSpace S]
    [∀ i, CompactSpace (D.obj i)] [∀ i, QuasiSeparatedSpace (D.obj i)]
    [∀ {i j : I} (g : i ⟶ j), IsClosedImmersion (D.map g)]
    [∀ i, LocallyOfFiniteType (t.app i : D.obj i ⟶ S)] [IsClosedImmersion f] :
    ∃ i : I, ∀ {j : I} (_ : j ⟶ i), IsClosedImmersion (t.app j : D.obj j ⟶ S)
```

## Tag 0GIH, a lemma

[Tag 0GIH](https://stacks.math.columbia.edu/tag/0GIH) in the Stacks Project.

**`AlgebraicGeometry.eventually_isImmersion`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/RelativeApproximation/ClosedImmersionDescent.lean, line 797](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/RelativeApproximation/ClosedImmersionDescent.lean#L797).

> **Stacks Project, Tag 0GIH.** In a directed inverse system of quasi-compact and
> quasi-separated schemes whose transition morphisms are closed immersions, if all the structure
> morphisms to a quasi-separated base are locally of finite type and the morphism induced on the
> limit is an immersion, then the structure morphisms are immersions for all sufficiently large
> indices.
> `Nonempty I` is not a weakening: it is what makes `Filter.atTop` on the index a PROPER
> filter. Over an empty index `atTop = ⊥` and the conclusion would be vacuously true, so this
> hypothesis is what rules vacuity out. The source assumes it too — a directed limit is indexed
> by a directed set, which is nonempty by convention.

```lean
lemma eventually_isImmersion {I : Type v} [Preorder I]
    [IsDirected I (· ≤ ·)] [Small.{u} I]
    {S : Scheme.{u}} (D : Iᵒᵖ ⥤ Scheme.{u})
    (t : D ⟶ (Functor.const Iᵒᵖ).obj S) (c : Cone D) (hc : IsLimit c)
    (f : c.pt ⟶ S)
    [QuasiSeparatedSpace S]
    [∀ i, CompactSpace (D.obj (op i))]
    [∀ i, QuasiSeparatedSpace (D.obj (op i))]
    [∀ ⦃i j : I⦄ (h : i ≤ j), IsClosedImmersion (D.map (homOfLE h).op)]
    [∀ i, LocallyOfFiniteType (t.app (op i))]
    (hcomm : c.π ≫ t = (Functor.const Iᵒᵖ).map f)
    [IsImmersion f] :
    ∀ᶠ i in atTop, IsImmersion (t.app (op i))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 32.4, Tag 081A](https://stacks.math.columbia.edu/tag/081A)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
