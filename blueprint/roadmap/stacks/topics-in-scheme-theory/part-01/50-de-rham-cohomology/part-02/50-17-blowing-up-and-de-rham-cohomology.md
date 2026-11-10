---
declaration: section
origin: cited
lean: Stacks.DeRham.isIso_formsDirectImageComparison_blowUpToBase, Stacks.DeRham.isIso_formsDirectImageComparison_exceptionalDivisorToCentre, Stacks.DeRham.isIso_blowupFormsDirectImage_of_smooth, Stacks.DeRham.isIso_exceptionalFormsDirectImage_of_smooth, Stacks.DeRham.isIso_formsDirectImage_of_isEffectiveCartierDivisor, Stacks.DeRham.isIso_homology_blowupFormsDerivedComparison, Stacks.DeRham.isIso_homology_blowupFormsRestrictionDerivedComparison_of_smooth, Stacks.DeRham.BlowupTriangle.exists_distTriang
statement: formalized
proof: formalized
---

# 50.17 Blowing up and de Rham cohomology

Section 50.17 of the Stacks Project, [Tag 0FUC](https://stacks.math.columbia.edu/tag/0FUC). 5 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FUU, a lemma

[Tag 0FUU](https://stacks.math.columbia.edu/tag/0FUU) in the Stacks Project.

**`Stacks.DeRham.isIso_formsDirectImageComparison_blowUpToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BlowupSmoothCentreForms.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/BlowupSmoothCentreForms.lean#L310). The attribute's comment: “corrected form, clause (1): Ω^a\_\{X/S} ⟶ b\_*Ω^a\_\{X'/S} is an isomorphism for every a ≥ 0, for f smooth and i a closed immersion of a scheme smooth over S whose image has EMPTY INTERIOR in X. The interior hypothesis is a correction: as stated (any closed immersion of S-smooth schemes) the clause is false when Z contains a nonempty open of X — for S = X = Z = Spec k the blowup is empty and 𝒪\_X ⟶ 0 is not an isomorphism (counterexample Stacks.DeRham.exists\_smooth\_not\_isIso\_formsDirectImage, untagged). The blowup is AlgebraicGeometry.blowUpToBase i.ker”.

> **[Stacks, Tag 0FUU], clause (1), in corrected form.**  Let `f : X ⟶ S` be smooth, let
> `i : Z ⟶ X` be a closed immersion with `Z` smooth over `S` and with image of empty interior in
> `X`, and let `b : X' ⟶ X` be the blowing up of `X` along `Z`.  Then for every `a ≥ 0` the
> canonical map `Ω^a_{X/S} ⟶ b_*Ω^a_{X'/S}` is an isomorphism.
>
> The hypothesis on the interior is a correction of the source.  The source states the clause for
> every closed immersion of schemes smooth over `S`, and it is false when `Z` contains a non-empty
> open subset of `X`: for `S = X = Z = Spec k` the blowup is empty, and `𝒪_X ⟶ 0` is not an
> isomorphism (`Stacks.DeRham.exists_smooth_not_isIso_formsDirectImage`).  The proof is the
> source's: the étale-local reduction to the coordinate model ([Stacks, Tag 0FUE]), with clause (1)
> of [Stacks, Tag 0FUR] there.  Empty interior is exactly what makes the codimension `n ≥ 1` on
> every chart.

```lean
theorem isIso_formsDirectImageComparison_blowUpToBase [IsClosedImmersion i] [Smooth f]
    [Smooth (i ≫ f)] (hint : interior (Set.range i.base) = ∅) (a : ℕ) :
    IsIso (formsDirectImageComparison (blowUpToBase i.ker) f (a : ℤ))
```

**`Stacks.DeRham.isIso_formsDirectImageComparison_exceptionalDivisorToCentre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BlowupSmoothCentreForms.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/BlowupSmoothCentreForms.lean#L334). The attribute's comment: “corrected form, clause (2): Ω^a\_\{Z/S} ⟶ p\_*Ω^a\_\{E/S} is an isomorphism for every a ≥ 0, for f smooth and i a closed immersion of a scheme smooth over S whose image has EMPTY INTERIOR in X; E is the exceptional divisor of AlgebraicGeometry.blowUpToBase i.ker and p is AlgebraicGeometry.exceptionalDivisorToCentre i. The interior hypothesis is a correction: as stated the clause is false when Z contains a nonempty open of X — for S = X = Z = Spec k, E is empty and 𝒪\_Z ⟶ 0 is not an isomorphism (counterexample Stacks.DeRham.exists\_smooth\_not\_isIso\_formsDirectImageComparison\_blowUpToBase, untagged)”.

> **[Stacks, Tag 0FUU], clause (2), in corrected form.**  Let `f : X ⟶ S` be smooth, let
> `i : Z ⟶ X` be a closed immersion with `Z` smooth over `S` and with image of empty interior in
> `X`, let `E` be the exceptional divisor of the blowing up of `X` along `Z`, and let `p : E ⟶ Z`
> be its structure morphism.  Then for every `a ≥ 0` the canonical map
> `Ω^a_{Z/S} ⟶ p_*Ω^a_{E/S}` is an isomorphism.
>
> As in clause (1), the hypothesis on the interior corrects the source: for `S = X = Z = Spec k`
> the exceptional divisor is empty and `𝒪_Z ⟶ 0` is not an isomorphism
> (`Stacks.DeRham.exists_smooth_not_isIso_formsDirectImageComparison_blowUpToBase`).  The proof is
> the étale-local reduction of the source to clause (2) of [Stacks, Tag 0FUR], on the exceptional
> divisor of the coordinate model.

```lean
theorem isIso_formsDirectImageComparison_exceptionalDivisorToCentre [IsClosedImmersion i]
    [Smooth f] [Smooth (i ≫ f)] (hint : interior (Set.range i.base) = ∅) (a : ℕ) :
    IsIso (formsDirectImageComparison (exceptionalDivisorToCentre i) (i ≫ f) (a : ℤ))
```

**`Stacks.DeRham.isIso_blowupFormsDirectImage_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BlowupSmoothCentreFormsAffine.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/BlowupSmoothCentreFormsAffine.lean#L248). The attribute's comment: “clause (1), corrected: false as written when Z contains a nonempty open of X (counterexample Z = X = S = Spec k: the blowup is empty and O\_X → b\_*O = 0), so stated for Z containing no nonempty open of X (positive codimension everywhere)”.

> **[Stacks, Tag 0FUU], clause (1).** Let `f : X ⟶ S` be smooth and let `i : Z ⟶ X` be a closed
> immersion with `Z` smooth over `S`, of positive codimension at every point, i.e. containing no
> nonempty open subset of `X`. Let `b : X' ⟶ X` be the blowing up of `X` along `Z`. Then for every
> `a ≥ 0` the canonical map `Ω^a_{X/S} ⟶ b_*Ω^a_{X'/S}` is an isomorphism.
>
> The positivity of the codimension is not stated in the source, and it is needed: where `Z`
> contains an open subset `W` of `X` the ideal of the centre vanishes on `W`, the blowup is empty
> over `W` (`AlgebraicGeometry.isEmpty_blowUp_bot`), and `𝒪_W = Ω^0_{W/S} ⟶ b_*Ω^0 = 0` is not an
> isomorphism — for instance for `Z = X = S = Spec k`. The source's proof reduces to the
> coordinate situation `𝐀^m_S ⊆ 𝐀^{m+n}_S` of Section 50.16, where `n ≥ 1`, and that is exactly
> what the hypothesis provides in the charts of [Stacks, Tag 0FUE].

```lean
theorem isIso_blowupFormsDirectImage_of_smooth (hint : interior (Set.range i.base) = ∅) (a : ℕ) :
    IsIso (blowupFormsDirectImage i f (a : ℤ))
```

**`Stacks.DeRham.isIso_exceptionalFormsDirectImage_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BlowupSmoothCentreFormsAffine.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/BlowupSmoothCentreFormsAffine.lean#L276). The attribute's comment: “clause (2), corrected: false as written when Z contains a nonempty open of X (counterexample Z = X = S = Spec k: E is empty and O\_Z → p\_*O\_E = 0), so stated for Z containing no nonempty open of X (positive codimension everywhere)”.

> **[Stacks, Tag 0FUU], clause (2).** Let `f : X ⟶ S` be smooth and let `i : Z ⟶ X` be a closed
> immersion with `Z` smooth over `S`, of positive codimension at every point, i.e. containing no
> nonempty open subset of `X`. Let `p : E ⟶ Z` be the projection onto the centre of the
> exceptional divisor of the blowing up of `X` along `Z`. Then for every `a ≥ 0` the canonical
> map `Ω^a_{Z/S} ⟶ p_*Ω^a_{E/S}` is an isomorphism.
>
> As for clause (1), the positivity of the codimension is not stated in the source and is needed:
> for `Z = X` the exceptional divisor is empty and `𝒪_Z ⟶ p_*𝒪_E = 0` is not an isomorphism.

```lean
theorem isIso_exceptionalFormsDirectImage_of_smooth (hint : interior (Set.range i.base) = ∅)
    (a : ℕ) : IsIso (exceptionalFormsDirectImage i f (a : ℤ))
```

**`Stacks.DeRham.isIso_formsDirectImage_of_isEffectiveCartierDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BlowupSmoothCentreFormsDirectImage.lean, line 566](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/BlowupSmoothCentreFormsDirectImage.lean#L566). The attribute's comment: “clauses (1) and (2) in every integer degree, for a centre whose ideal sheaf is an effective Cartier divisor — a divisorial centre, which for a closed immersion of schemes smooth over S means codimension one at every point of the centre (the empty centre qualifying vacuously). This is the degenerate case of the tag, proved for a nearly trivial reason: blowing up an effective Cartier divisor leaves the scheme unchanged (Stacks 0807), so b : X' ⟶ X is an isomorphism, and the exceptional divisor is the fibre product of the blowup with the centre, so p : E ⟶ Z is the base change of b along i and is an isomorphism too; each comparison is then the unit of the inverse image–direct image adjunction along an isomorphism followed by the direct image of a map which is an isomorphism by Stacks 0FLV. A centre of codimension two or more is NOT proved, in any degree: none of the content of the source's proof — the étale-local reduction of Stacks 0FUE to the coordinate situation 𝐀^m\_S ⊆ 𝐀^\{m+n}\_S, and the computation of Stacks 0FUR there — is used. In the other direction this is more general than the source: the smoothness of f and of i ≫ f is not needed for a divisorial centre and is not assumed, and every integer degree is covered, not only a ≥ 0. Clause (3) is not included: the derived comparison of Rb\_* ∘ j\_* against i\_* ∘ Rp\_* has no carrier in this library, so clause (3) has no canonical map to be a statement about”.

> **[Stacks, Tag 0FUU], clauses (1) and (2), for a centre which is an effective Cartier
> divisor.**  Let `i : Z ⟶ X` be a closed immersion whose ideal sheaf is an effective Cartier
> divisor, let `f : X ⟶ S` be any morphism, let `b : X' ⟶ X` be the blowing up of `X` along `Z`,
> let `E` be its exceptional divisor and let `p : E ⟶ Z` be the structure morphism of `E` over the
> centre.  Then in every degree the comparison maps
>
> * `Ω^a_{X/S} ⟶ b_*Ω^a_{X'/S}` and
> * `Ω^a_{Z/S} ⟶ p_*Ω^a_{E/S}`
>
> are isomorphisms.
>
> This is the degenerate case of the tag, and it is proved for a nearly trivial reason.  Blowing up
> an effective Cartier divisor leaves the scheme unchanged ([Stacks, Tag 0807]), so `b` is an
> isomorphism; the exceptional divisor is the fibre product of the blowup with the centre, so `p`
> is the base change of `b` along `i` and is an isomorphism too.  Each comparison is then the unit
> of the inverse image–direct image adjunction along an isomorphism, followed by the direct image
> of a map which is an isomorphism by [Stacks, Tag 0FLV].
>
> For a closed immersion of schemes smooth over `S` the ideal of the centre is locally generated by
> a regular sequence, by [Stacks, Tag 0FUE], so the hypothesis here holds precisely when that
> sequence has length one at every point of the centre — the centre is a divisor, of codimension
> one wherever it is non-empty.  The empty centre satisfies it vacuously, its ideal being the unit
> ideal.  The source states the tag for a centre of arbitrary codimension, and nothing of its
> proof — the étale-local reduction of [Stacks, Tag 0FUE] to the coordinate situation
> `𝐀^m_S ⊆ 𝐀^{m+n}_S` and the computation of [Stacks, Tag 0FUR] there — is used.  Smoothness of
> `f` and of `i ≫ f` is not needed for this case and is not assumed.

```lean
theorem isIso_formsDirectImage_of_isEffectiveCartierDivisor {S X Z : Scheme.{u}} (f : X ⟶ S)
    (i : Z ⟶ X) [IsClosedImmersion i]
    (hi : Stacks.Divisors.IsEffectiveCartierDivisor i.ker) (a : ℤ) :
    IsIso (blowupFormsDirectImage i f a) ∧ IsIso (exceptionalFormsDirectImage i f a)
```

**`Stacks.DeRham.isIso_homology_blowupFormsDerivedComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BlowupSmoothCentreFormsHigherDirectImage.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/BlowupSmoothCentreFormsHigherDirectImage.lean#L56). The attribute's comment: “clause (3): for f smooth and i a closed immersion of an S-smooth scheme, Rb\_*Ω^a\_\{X'/S} ⟶ i\_*Rp\_*Ω^a\_\{E/S} is an isomorphism on cohomology sheaves in every degree q ≥ 1. No interior hypothesis is needed for this clause”.

> **[Stacks, Tag 0FUU], clause (3).** Let `f : X ⟶ S` be smooth and `i : Z ⟶ X` a closed
> immersion with `Z` smooth over `S`, let `b : X' ⟶ X` be the blowing up along `Z`, `E` its
> exceptional divisor and `p : E ⟶ Z` the structure morphism. For every `a ≥ 0` and every `q ≥ 1`
> the comparison `Rb_*Ω^a_{X'/S} ⟶ i_*Rp_*Ω^a_{E/S}`
> (`Stacks.DeRham.blowupFormsDerivedComparison`) is an isomorphism on `H^q`.

```lean
theorem isIso_homology_blowupFormsDerivedComparison [IsClosedImmersion i] [Smooth f]
    [Smooth (i ≫ f)] (a : ℕ) {q : ℤ} (hq : 1 ≤ q) :
    IsIso ((DerivedCategory.homologyFunctor X.Modules q).map
      (blowupFormsDerivedComparison f i (a : ℤ)))
```

**`Stacks.DeRham.isIso_homology_blowupFormsRestrictionDerivedComparison_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BlowupSmoothCentreFormsKernelVanishing.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/BlowupSmoothCentreFormsKernelVanishing.lean#L381). The attribute's comment: “clause (3): Rb\_*Ω^a\_\{X'/S} ⟶ i\_*Rp\_*Ω^a\_\{E/S} is an isomorphism on cohomology sheaves in every degree q ≥ 1, every a ≥ 0, for a closed immersion of schemes smooth over S of any codimension”.

> **[Stacks, Tag 0FUU], clause (3).** Let `f : X ⟶ S` be smooth and let `i : Z ⟶ X` be a closed
> immersion with `Z` smooth over `S`. Let `b : X' ⟶ X` be the blowing up of `X` along `Z`, with
> exceptional divisor `E` and projection `p : E ⟶ Z`. Then for every `a ≥ 0` the canonical map
> `Rb_*Ω^a_{X'/S} ⟶ i_*Rp_*Ω^a_{E/S}` is an isomorphism on cohomology sheaves in every degree
> `q ≥ 1`, at any models of the derived categories.
>
> No hypothesis on the codimension is needed: where `Z` contains an open of `X`, the blowup and the
> exceptional divisor are empty there. The proof reduces, étale locally by [Stacks, Tag 0FUE], to
> the coordinate situation of Section 50.16, where it is clause (3) of [Stacks, Tag 0FUR].

```lean
theorem isIso_homology_blowupFormsRestrictionDerivedComparison_of_smooth (a : ℕ) (q : ℤ)
    (hq : 0 < q) :
    IsIso ((DerivedCategory.homologyFunctor _ q).map
      (blowupFormsRestrictionDerivedComparison f i (a : ℤ)))
```

## Tag 0FUV, a lemma

[Tag 0FUV](https://stacks.math.columbia.edu/tag/0FUV) in the Stacks Project.

**`Stacks.DeRham.BlowupTriangle.exists_distTriang`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BlowupDeRhamTriangleSmooth.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/BlowupDeRhamTriangleSmooth.lean#L76). The attribute's comment: “the distinguished triangle Ω^•\_\{X/S} → Rb\_*Ω^•\_\{X'/S} ⊕ i\_*Ω^•\_\{Z/S} → i\_*Rp\_*Ω^•\_\{E/S} → Ω^•\_\{X/S}[1] in D(X, f^\{-1}O\_S) whose four maps are the canonical ones, the sign of i\_*Ω^•\_\{Z/S} → i\_*Rp\_*Ω^•\_\{E/S} reversed; Z ⊂ X closed, X and Z smooth over S, any codimension”.

> **The blowup triangle of de Rham complexes.** Let `f : X ⟶ S` be smooth and let `i : Z ⟶ X`
> be a closed immersion with `Z` smooth over `S`, of any codimension. Let `b : X' ⟶ X` be the
> blowing up of `X` along `Z`, with exceptional divisor `j : E ⟶ X'` and projection `p : E ⟶ Z`.
> Then there is a distinguished triangle
>
> `Ω^•_{X/S} ⟶ Rb_*Ω^•_{X'/S} ⊕ i_*Ω^•_{Z/S} ⟶ i_*Rp_*Ω^•_{E/S} ⟶ Ω^•_{X/S}[1]`
>
> in `D(X, f^{-1}𝒪_S)` whose first map has components the canonical maps
> `Ω^•_{X/S} ⟶ Rb_*Ω^•_{X'/S}` and `Ω^•_{X/S} ⟶ i_*Ω^•_{Z/S}`, and whose second map has components
> the canonical map `Rb_*Ω^•_{X'/S} ⟶ i_*Rp_*Ω^•_{E/S}` and the negative of the canonical map
> `i_*Ω^•_{Z/S} ⟶ i_*Rp_*Ω^•_{E/S}`, for any models of the derived categories.

```lean
theorem exists_distTriang :
    ∃ δ : exceptionalDeRham f i ⟶ (deRham f)⟦(1 : ℤ)⟧,
      Triangle.mk (biprod.lift (toBlowUp f i) (toCentre f i))
        (biprod.desc (blowUpToExceptional f i) (-centreToExceptional f i)) δ ∈
          distTriang (DerivedCategory (ModuleSheaves (inverseImageBase f)))
```

## Tag 0FUW, a proposition

[Tag 0FUW](https://stacks.math.columbia.edu/tag/0FUW) in the Stacks Project.

**`Stacks.DeRham.BlowupTriangle.exists_retraction_toBlowUp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BlowupDeRhamSplitting.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/BlowupDeRhamSplitting.lean#L50). The attribute's comment: “f : X -> S smooth, i : Z -> X a closed immersion with Z smooth over S, b : X' -> X the blowing up along Z; if Z has positive codimension in X at every point (used in the weaker form that Z contains no nonempty open subset of X), then Omega\_\{X/S} -> Rb\_*Omega\_\{X'/S} has a splitting in D(X, (X -> S)^\{-1}O\_S), for any models”.

> **[Stacks, Tag 0FUW]: the de Rham complex splits off along a blowing up with smooth centre.**
> Let `f : X ⟶ S` be smooth, `i : Z ⟶ X` a closed immersion with `Z` smooth over `S`, and
> `b : X' ⟶ X` the blowing up of `X` along `Z`. If `Z` contains no nonempty open subset of `X` (in
> particular, if `Z` has positive codimension in `X` at every point), the canonical map
> `Ω^•_{X/S} ⟶ Rb_*Ω^•_{X'/S}` has a retraction in `D(X, (X ⟶ S)⁻¹𝒪_S)`, for any models of the
> derived categories.

```lean
theorem exists_retraction_toBlowUp [Smooth f] [Smooth (i ≫ f)]
    [HasDerivedCategory.{w} (ModuleSheaves (inverseImageBase f))]
    [HasDerivedCategory.{w} (ModuleSheaves (inverseImageBase (blowupMap i ≫ f)))]
    (hint : interior (Set.range i.base) = ∅) :
    ∃ r : blowUpDeRham f i ⟶ deRham f, toBlowUp f i ≫ r = 𝟙 _
```

## Tag 0G5I, a lemma

[Tag 0G5I](https://stacks.math.columbia.edu/tag/0G5I) in the Stacks Project.

**`Stacks.RegularSequence.subsingleton_ext_pushforward_of_isRegularClosedImmersionOfCodim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RegularSequence/ExtVanishingImmersion.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RegularSequence/ExtVanishingImmersion.lean#L261). References: SGA 4½ Cycle (2.2.1), “more general”.

> Let `i : Z ⟶ X` be a closed immersion of schemes which is regular of codimension `c`, let
> `F` be an arbitrary `𝒪_Z`-module and let `E` be a locally free `𝒪_X`-module. Then
> `Ext^q_{𝒪_X}(i_*F, E) = 0` for every `q < c`.

```lean
theorem subsingleton_ext_pushforward_of_isRegularClosedImmersionOfCodim {Z X : Scheme.{u}}
    (i : Z ⟶ X) [IsClosedImmersion i] (c : ℕ) (hi : IsRegularClosedImmersionOfCodim i c)
    (F : Z.Modules) (E : X.Modules) (hE : Scheme.Modules.IsLocallyFree E)
    (q : ℕ) (hq : q < c) :
    Subsingleton (Abelian.Ext ((Scheme.Modules.pushforward i).obj F) E q)
```

## Tag 0G5J, a lemma

[Tag 0G5J](https://stacks.math.columbia.edu/tag/0G5J) in the Stacks Project.

**`Stacks.DeRham.existsUnique_blowUpFormsRetraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BlowupFormsDerivedRetraction.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/BlowupFormsDerivedRetraction.lean#L259). The attribute's comment: “both clauses reduced to the two inputs the source uses, for the canonical map Ω^a\_\{X/S} ⟶ Rb\_*Ω^a\_\{X'/S} in D(𝒪\_X) constructed here. NOT proved: either input. `hcone` is the source's Tag 0FUU (3) + 0E7D + 0G5I vanishing, and Tag 0FUU is not proved here; `hv` is its twist isomorphism of Tags 0G5G and 0G5H, proved only for the coordinate model”.

> **Stacks Project, Tag 0G5J**, granted its two inputs.  Let `f : X ⟶ S` be smooth, let
> `I` cut out a closed subscheme of `X` smooth over `S`, and let `b : X' ⟶ X` be the blowing up of
> `X` along it.  For `a ≥ 0` there is exactly one arrow `Rb_*Ω^a_{X'/S} ⟶ Ω^a_{X/S}` in `D(𝒪_X)`
> whose composition with the canonical `Ω^a_{X/S} ⟶ Rb_*Ω^a_{X'/S}` is the identity, provided:
>
> * `hcone`:  the third term `Z` of a distinguished triangle on the canonical map admits no
>   nonzero morphism to `Ω^a_{X/S}`.  This is the hypothesis discharged in the source by
>   [Stacks, Tag 0FUU] part (3), [Stacks, Tag 0E7D] and [Stacks, Tag 0G5I].
> * `hv`:  an invertible factorization of the canonical map.  This is the hypothesis discharged in
>   the source by the twist isomorphism of [Stacks, Tags 0G5G and 0G5H].
>
> The two smoothness hypotheses are those of the setting of [Stacks, Tag 0FUT] and are not used by
> the proof.

```lean
theorem existsUnique_blowUpFormsRetraction [Smooth f] [Smooth (I.subschemeι ≫ f)] (a : ℕ)
    {Z : DerivedCategory X.Modules}
    {p : blowUpFormsObj f I (a : ℤ) ⟶ Z} {q : Z ⟶ (formsSingle f (a : ℤ))⟦(1 : ℤ)⟧}
    (hT : Triangle.mk (blowUpFormsDerivedDirectImage f I (a : ℤ)) p q ∈
      distTriang (DerivedCategory X.Modules))
    (hcone : ∀ g : Z ⟶ formsSingle f (a : ℤ), g = 0)
    {D : DerivedCategory X.Modules} (v : blowUpFormsObj f I (a : ℤ) ⟶ D)
    (hv : IsIso (blowUpFormsDerivedDirectImage f I (a : ℤ) ≫ v)) :
    ∃! r : blowUpFormsObj f I (a : ℤ) ⟶ formsSingle f (a : ℤ),
      blowUpFormsDerivedDirectImage f I (a : ℤ) ≫ r = 𝟙 (formsSingle f (a : ℤ))
```

**`Stacks.DeRham.existsUnique_blowUpFormsRetraction_blowUpToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BlowupFormsRetractionCorrected.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/BlowupFormsRetractionCorrected.lean#L73). The attribute's comment: “corrected form: for f smooth and i : Z ⟶ X a closed immersion of a scheme smooth over S whose image has EMPTY INTERIOR in X, and b = blowUpToBase i.ker, for every a ≥ 0 there is a unique arrow Rb\_*Ω^a\_\{X'/S} ⟶ Ω^a\_\{X/S} in D(𝒪\_X) whose composite with the canonical Ω^a\_\{X/S} ⟶ Rb\_*Ω^a\_\{X'/S} is the identity. The interior hypothesis is a correction: as stated the lemma is false when Z contains a nonempty open of X — for S = X = Z = Spec k the blowup is empty (Stacks.DeRham.isEmpty\_blowUp\_bot) and 𝒪\_X ⟶ 0 has no retraction (counterexample of 0FUU: Stacks.DeRham.exists\_smooth\_not\_isIso\_formsDirectImageComparison\_blowUpToBase)”.

> **[Stacks, Tag 0G5J], in corrected form.**  Let `f : X ⟶ S` be smooth, let `i : Z ⟶ X` be a
> closed immersion with `Z` smooth over `S` and with image of empty interior in `X`, and let
> `b : X' ⟶ X` be the blowing up of `X` along `Z`.  For every `a ≥ 0` there is exactly one arrow
> `Rb_*Ω^a_{X'/S} ⟶ Ω^a_{X/S}` in `D(𝒪_X)` whose composite with the canonical map
> `Ω^a_{X/S} ⟶ Rb_*Ω^a_{X'/S}` is the identity.
>
> The hypothesis on the interior corrects the source: for `S = X = Z = Spec k` the blowup is empty
> and `𝒪_X ⟶ 0` has no retraction
> (`Stacks.DeRham.exists_smooth_not_isIso_formsDirectImageComparison_blowUpToBase`,
> `Stacks.DeRham.isEmpty_blowUp_bot`).  The proof is the source's.  Existence: the canonical map
> followed by `Rb_*` of the second map of [Stacks, Tag 0G5G] is the twist map of
> [Stacks, Tag 0G5H] for `𝒟 = Σ_c (c - 1)E_c`, an isomorphism.  Uniqueness: by
> [Stacks, Tag 0FUU] (3) the higher direct images are pushed forward from the centre, and
> [Stacks, Tags 0E7D and 0G5I] kill every map from the cone to `Ω^a_{X/S}`.

```lean
theorem existsUnique_blowUpFormsRetraction_blowUpToBase [IsClosedImmersion i] [Smooth f]
    [Smooth (i ≫ f)] (hint : interior (Set.range i.base) = ∅) (a : ℕ) :
    ∃! r : blowUpFormsObj f i.ker (a : ℤ) ⟶ formsSingle f (a : ℤ),
      blowUpFormsDerivedDirectImage f i.ker (a : ℤ) ≫ r = 𝟙 (formsSingle f (a : ℤ))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.17, Tag 0FUC](https://stacks.math.columbia.edu/tag/0FUC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
