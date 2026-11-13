---
declaration: section
origin: cited
lean: Stacks.Models.IsModelHom, Stacks.Models.IsProperModel, Stacks.Models.IsRegularModel, Stacks.Models.IsModel.baseChange, Stacks.Models.IsModelHom.baseChange, Stacks.Models.Model.baseChange, Stacks.Models.IsModel, Stacks.Models.schemeTheoreticImage_isModel
statement: formalized
proof: formalized
---

# 55.8 Models

Section 55.8 of the Stacks Project, [Tag 0C2R](https://stacks.math.columbia.edu/tag/0C2R). 7 tags here are carried by 16 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0C2R, the section

[Tag 0C2R](https://stacks.math.columbia.edu/tag/0C2R) in the Stacks Project.

**`Stacks.Models.IsModelHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Models/BaseChange.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Models/BaseChange.lean#L91). The attribute's comment: “a morphism of models X ⟶ X' for V: a morphism of schemes over R which induces the identity on V”.

> **A morphism of models** `X ⟶ X'` for `V` (Section 0C2R): a morphism of schemes over `R`
> which induces the identity on `V`, i.e. carries the identification `V ≅ X_K` to `V ≅ X'_K`.

```lean
def IsModelHom {V X X' : Scheme.{u}} (p : X ⟶ Spec (CommRingCat.of R))
    (p' : X' ⟶ Spec (CommRingCat.of R))
    (e : V ≅ pullback p (genericPointInclusion R K))
    (e' : V ≅ pullback p' (genericPointInclusion R K)) (φ : X ⟶ X') : Prop
```

**`Stacks.Models.IsProperModel`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Models/BaseChange.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Models/BaseChange.lean#L124). The attribute's comment: “a proper model: a model whose structure morphism X ⟶ Spec R is proper”.

> **A proper model** of `V` (Section 0C2R): a model whose structure morphism is proper.

```lean
def IsProperModel [IsDomain R] [IsDiscreteValuationRing R] [IsFractionRing R K]
    {V X : Scheme.{u}} (v : V ⟶ Spec (CommRingCat.of K)) (p : X ⟶ Spec (CommRingCat.of R))
    (e : V ≅ pullback p (genericPointInclusion R K)) : Prop
```

**`Stacks.Models.IsRegularModel`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Models/BaseChange.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Models/BaseChange.lean#L131). The attribute's comment: “a regular model: a model which is a regular scheme”.

> **A regular model** of `V` (Section 0C2R): a model whose total space is a regular scheme.

```lean
def IsRegularModel [IsDomain R] [IsDiscreteValuationRing R] [IsFractionRing R K]
    {V X : Scheme.{u}} (v : V ⟶ Spec (CommRingCat.of K)) (p : X ⟶ Spec (CommRingCat.of R))
    (e : V ≅ pullback p (genericPointInclusion R K)) : Prop
```

**`Stacks.Models.IsModel.baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Models/BaseChange.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Models/BaseChange.lean#L288). The attribute's comment: “base change X ↦ X ×\_\{Spec R} Spec R' along an extension of discrete valuation rings sends models of V over R to models of V' = V ×\_\{Spec K} Spec K' over R'”.

> **Base change of a model** (Section 0C2R). Let `R ⊆ R'` be an extension of discrete
> valuation rings with induced extension `K'/K` of fraction fields. If `X` is a model of the
> `K`-scheme `V` over `R`, then `X ×_{Spec R} Spec R'` is a model of `V' = V ×_{Spec K} Spec K'`
> over `R'`.

```lean
theorem IsModel.baseChange {V X : Scheme.{u}} {v : V ⟶ Spec (CommRingCat.of K)}
    {p : X ⟶ Spec (CommRingCat.of R)} {e : V ≅ pullback p (genericPointInclusion R K)}
    (h : IsModel v p e) :
    IsModel (pullback.snd v (Spec.map (CommRingCat.ofHom (algebraMap K K'))))
      (pullback.snd p (Spec.map (CommRingCat.ofHom (algebraMap R R'))))
      (baseChangeGenericFiberIso (R' := R') (K' := K') p e h.2.2.2)
```

**`Stacks.Models.IsModelHom.baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Models/BaseChange.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Models/BaseChange.lean#L317). The attribute's comment: “base change sends morphisms of models of V over R to morphisms of models of V' over R'”.

> **Base change of a morphism of models** (Section 0C2R): the base change of a morphism of
> models of `V` over `R` is a morphism of models of `V'` over `R'`.

```lean
theorem IsModelHom.baseChange {V X X' : Scheme.{u}} {v : V ⟶ Spec (CommRingCat.of K)}
    {p : X ⟶ Spec (CommRingCat.of R)} {p' : X' ⟶ Spec (CommRingCat.of R)}
    {e : V ≅ pullback p (genericPointInclusion R K)}
    {e' : V ≅ pullback p' (genericPointInclusion R K)}
    (hv : e.hom ≫ pullback.snd p (genericPointInclusion R K) = v)
    (hv' : e'.hom ≫ pullback.snd p' (genericPointInclusion R K) = v) {φ : X ⟶ X'}
    (hφ : IsModelHom p p' e e' φ) :
    IsModelHom (pullback.snd p (Spec.map (CommRingCat.ofHom (algebraMap R R'))))
      (pullback.snd p' (Spec.map (CommRingCat.ofHom (algebraMap R R'))))
      (baseChangeGenericFiberIso (R' := R') (K' := K') p e hv)
      (baseChangeGenericFiberIso (R' := R') (K' := K') p' e' hv')
      (baseChangeMap (R' := R') p p' φ hφ.1)
```

**`Stacks.Models.Model.baseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Models/BaseChange.lean, line 348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Models/BaseChange.lean#L348). The attribute's comment: “the functor from models for V over R to models for V' over R' sending X to X ×\_\{Spec R} Spec R'”.

> **The base change functor** (Section 0C2R): for an extension of discrete valuation rings
> `R ⊆ R'` with induced extension `K'/K` of fraction fields, `X ↦ X ×_{Spec R} Spec R'` is a
> functor from models of `V` over `R` to models of `V' = V ×_{Spec K} Spec K'` over `R'`.

```lean
def Model.baseChange (V : Scheme.{u}) (v : V ⟶ Spec (CommRingCat.of K)) :
    Model R v ⥤ Model R' (pullback.snd v (Spec.map (CommRingCat.ofHom (algebraMap K K'))))
```

Declarations registered for the tag:

- [`Stacks.Models.IsModel`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Models/Basic.lean#L61), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Models/BaseChange.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Models/BaseChange.lean#L68) (StacksFrontier): “a model for V: a flat finite type morphism X ⟶ Spec R endowed with an isomorphism V ⟶ X\_K”.

## Tag 0C2S, a lemma

[Tag 0C2S](https://stacks.math.columbia.edu/tag/0C2S) in the Stacks Project.

**`Stacks.Models.schemeTheoreticImage_isModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Models/Basic.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Models/Basic.lean#L229).

> **Stacks Project, Tag 0C2S.** The scheme-theoretic image of a closed immersion of
> algebraic `K`-schemes in an `R`-model of its target is an `R`-model of its source.

```lean
theorem schemeTheoreticImage_isModel {V₁ V₂ X₂ : Scheme.{u}}
    (v₁ : V₁ ⟶ Spec (CommRingCat.of K)) (v₂ : V₂ ⟶ Spec (CommRingCat.of K))
    [LocallyOfFiniteType v₁] [QuasiCompact v₁]
    [LocallyOfFiniteType v₂] [QuasiCompact v₂]
    (f : V₁ ⟶ V₂) [IsClosedImmersion f] (hf : f ≫ v₂ = v₁)
    (p₂ : X₂ ⟶ Spec (CommRingCat.of R))
    (e₂ : V₂ ≅ pullback p₂ (Spec.map (CommRingCat.ofHom (algebraMap R K))))
    (hX₂ : IsModel v₂ p₂ e₂) :
    let i := Spec.map (CommRingCat.ofHom (algebraMap R K))
    let g := f ≫ e₂.hom ≫ pullback.fst p₂ i
    ∃ e₁ : V₁ ≅ pullback (g.imageι ≫ p₂) i, IsModel v₁ (g.imageι ≫ p₂) e₁
```

## Tag 0C2T, a lemma

[Tag 0C2T](https://stacks.math.columbia.edu/tag/0C2T) in the Stacks Project.

**`Stacks.Models.isFinite_normalization_of_isModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Models/Normalization.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Models/Normalization.lean#L237). The attribute's comment: “finiteness of the normalization”.

> **Stacks Project, Tag 0C2T (finiteness of the normalization).** The normalization of a model,
> over a discrete valuation ring, of a geometrically normal scheme over its fraction field is a
> finite morphism.

```lean
theorem isFinite_normalization_of_isModel {V X : Scheme.{u}}
    (v : V ⟶ Spec (CommRingCat.of K)) (hV : IsGeometricallyNormal v)
    (p : X ⟶ Spec (CommRingCat.of R))
    (e : V ≅ pullback p (Spec.map (CommRingCat.ofHom (algebraMap R K))))
    (hX : IsModel v p e)
    (hfinX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    IsFinite (Scheme.normalization X hfinX)
```

**`Stacks.Models.exists_iso_baseChange_normalization_adicCompletion_of_isModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Models/Normalization.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Models/Normalization.lean#L253). The attribute's comment: “normalization commutes with completion”.

> **Stacks Project, Tag 0C2T (normalization commutes with completion).** For a model, over a
> discrete valuation ring `R`, of a geometrically normal scheme over the fraction field of `R`, the
> base change of the normalization to the completion `R^∧` is the normalization of the base change
> of the model, compatibly with the two normalization morphisms.

```lean
theorem exists_iso_baseChange_normalization_adicCompletion_of_isModel {V X : Scheme.{u}}
    (v : V ⟶ Spec (CommRingCat.of K)) (hV : IsGeometricallyNormal v)
    (p : X ⟶ Spec (CommRingCat.of R))
    (e : V ≅ pullback p (Spec.map (CommRingCat.ofHom (algebraMap R K))))
    (hX : IsModel v p e)
    (hfinX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    let ν := Scheme.normalization X hfinX
    let Rhat := AdicCompletion (IsLocalRing.maximalIdeal R) R
    let i : Spec (CommRingCat.of Rhat) ⟶ Spec (CommRingCat.of R) :=
      Spec.map (CommRingCat.ofHom (algebraMap R Rhat))
    let Y : Scheme.{u} := pullback p i
    let νhat : pullback (ν ≫ p) i ⟶ Y :=
      pullback.map (ν ≫ p) i p i ν (𝟙 _) (𝟙 _) (by simp) (by simp)
    ∀ hfinY : ∀ U : Y.Opens, IsCompact (U : Set Y) → (irreducibleComponents U).Finite,
      ∃ α : pullback (ν ≫ p) i ≅ Scheme.normalizationScheme Y hfinY,
        α.hom ≫ Scheme.normalization Y hfinY = νhat
```

**`Stacks.Models.isNormalRing_adicCompletion_stalk_normalization_of_isModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Models/Normalization.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Models/Normalization.lean#L283). The attribute's comment: “completions of the local rings are normal”.

> **Stacks Project, Tag 0C2T (completions of the local rings are normal).** At every point of
> the normalization of a model, over a discrete valuation ring, of a geometrically normal scheme
> over the fraction field, the completion of the local ring is a normal ring.

```lean
theorem isNormalRing_adicCompletion_stalk_normalization_of_isModel {V X : Scheme.{u}}
    (v : V ⟶ Spec (CommRingCat.of K)) (hV : IsGeometricallyNormal v)
    (p : X ⟶ Spec (CommRingCat.of R))
    (e : V ≅ pullback p (Spec.map (CommRingCat.ofHom (algebraMap R K))))
    (hX : IsModel v p e)
    (hfinX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (x : Scheme.normalizationScheme X hfinX) :
    IsNormalRing (AdicCompletion
      (IsLocalRing.maximalIdeal ((Scheme.normalizationScheme X hfinX).presheaf.stalk x))
      ((Scheme.normalizationScheme X hfinX).presheaf.stalk x))
```

## Tag 0C2U, a lemma

[Tag 0C2U](https://stacks.math.columbia.edu/tag/0C2U) in the Stacks Project.

**`Stacks.Models.exists_isResolution_of_isModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Models/RegularProperModelExists.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Models/RegularProperModelExists.lean#L378). The attribute's comment: “existence of a resolution”.

> **Stacks Project, Tag 0C2U (existence of a resolution).** Let `X` be a model over a discrete
> valuation ring `R` of a smooth curve `C` over the fraction field `K`. Then `X` is integral and
> Noetherian, and there exists a resolution of singularities of `X`.
>
> If the special fibre of `X` is empty, `X` is its generic fibre, which is the smooth curve `C`, and
> the identity is a resolution. Otherwise `X` is two-dimensional and Lipman's theorem applies, see
> `exists_isResolution_of_isModel_of_topologicalKrullDim_eq_two`.

```lean
theorem exists_isResolution_of_isModel {C X : Scheme.{u}} (c : C ⟶ Spec (.of K)) [Smooth c]
    [IsCurve K c] (p : X ⟶ Spec (.of R))
    (e : C ≅ pullback p (Spec.map (CommRingCat.ofHom (algebraMap R K))))
    (hX : IsModel c p e) :
    ∃ (_ : IsIntegral X) (_ : IsNoetherian X) (Y : Scheme.{u}) (f : Y ⟶ X), IsResolution f
```

**`AlgebraicGeometry.isModel_comp_of_isResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Resolution/Models.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Resolution/Models.lean#L272). The attribute's comment: “resolution\_is\_model”.

> **Stacks Project, Tag 0C2U.** A resolution of singularities of a model of a smooth curve is
> again a model of that curve.

```lean
theorem isModel_comp_of_isResolution {C X Y : Scheme.{u}} (c : C ⟶ Spec (.of K)) [Smooth c]
    [IsCurve K c] (p : X ⟶ Spec (.of R)) [IsIntegral X] [IsNoetherian X]
    (eX : C ≅ pullback p (Spec.map (CommRingCat.ofHom (algebraMap R K))))
    (hX : Stacks.Models.IsModel c p eX) (f : Y ⟶ X) (hf : IsResolution f) :
    ∃ eY : C ≅ pullback (f ≫ p) (Spec.map (CommRingCat.ofHom (algebraMap R K))),
      Stacks.Models.IsModel c (f ≫ p) eY
```

**`AlgebraicGeometry.exists_isResolution_and_isModel_comp_of_isModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Resolution/ModelsResolutionExistence.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Resolution/ModelsResolutionExistence.lean#L186).

> **Stacks Project, Tag 0C2U.** Let `X` be a model of a smooth curve `C` over `K`. Then `X` is
> a Noetherian integral scheme, there exists a resolution of singularities of `X`, and any
> resolution of singularities of `X` is a model of `C`.

```lean
theorem exists_isResolution_and_isModel_comp_of_isModel {C X : Scheme.{u}}
    (c : C ⟶ Spec (.of K)) [Smooth c] [IsCurve K c] (p : X ⟶ Spec (.of R))
    (eX : C ≅ pullback p (Spec.map (CommRingCat.ofHom (algebraMap R K))))
    (hX : Stacks.Models.IsModel c p eX) :
    ∃ (_ : IsIntegral X) (_ : IsNoetherian X),
      (∃ (Y : Scheme.{u}) (f : Y ⟶ X), IsResolution f) ∧
      ∀ (Y : Scheme.{u}) (f : Y ⟶ X), IsResolution f →
        ∃ eY : C ≅ pullback (f ≫ p) (Spec.map (CommRingCat.ofHom (algebraMap R K))),
          Stacks.Models.IsModel c (f ≫ p) eY
```

## Tag 0C2V, a definition

[Tag 0C2V](https://stacks.math.columbia.edu/tag/0C2V) in the Stacks Project.

**`Stacks.Models.IsMinimalModel`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/MinimalModel.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/MinimalModel.lean#L79). The attribute's comment: “a minimal model of a smooth projective curve”.

> **Stacks Project, Tag 0C2V.** A *minimal model* of a smooth projective curve `C` over `K`
> with `H⁰(C, 𝒪_C) = K` is a regular, proper model `X ⟶ Spec(R)` of `C` such that `X` contains no
> exceptional curve of the first kind.

```lean
public structure IsMinimalModel {C X : Scheme.{u}} (c : C ⟶ Spec (.of K)) [IsCurve K c]
    [Smooth c] (p : X ⟶ Spec (.of R))
    (e : C ≅ pullback p (Spec.map (CommRingCat.ofHom (algebraMap R K)))) : Prop
```

## Tag 0CD9, a lemma

[Tag 0CD9](https://stacks.math.columbia.edu/tag/0CD9) in the Stacks Project.

**`Stacks.Models.exists_exceptionalContractionSequence_isMinimalModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/MinimalModelExistence.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/MinimalModelExistence.lean#L139).

> **Stacks Project, Tag 0CD9.** Let `C` be a smooth projective curve over `K` with
> `H⁰(C, 𝒪_C) = K`. If `X` is a regular proper model for `C`, then there is a sequence of morphisms
> `X = Xₘ → Xₘ₋₁ → ⋯ → X₁ → X₀` of regular proper models of `C`, each the contraction of an
> exceptional curve of the first kind, such that `X₀` is a minimal model.
>
> The proof is the source's: `X` is projective over `R` ([Stacks, Tag 0C5P]), so an exceptional
> curve of the first kind on it can be contracted onto a regular projective model
> ([Stacks, Tag 0C2N]), and the number of points of the special fibre with one-dimensional local
> ring — the generic points of the irreducible components of the special fibre — drops by one.

```lean
theorem exists_exceptionalContractionSequence_isMinimalModel {C X : Scheme.{u}}
    (c : C ⟶ Spec (.of K)) [IsCurve K c] [Smooth c] (hproj : Stacks.HProjective.IsHProjective c)
    (hH0 : IsIso ((Scheme.ΓSpecIso (.of K)).inv ≫ c.appTop)) (p : X ⟶ Spec (.of R))
    (e : C ≅ pullback p (Spec.map (CommRingCat.ofHom (algebraMap R K))))
    (hmod : IsModel c p e) [IsProper p] (hreg : IsRegular X) :
    ∃ (X₀ : Scheme.{u}) (p₀ : X₀ ⟶ Spec (.of R))
      (e₀ : C ≅ pullback p₀ (Spec.map (CommRingCat.ofHom (algebraMap R K)))) (g : X ⟶ X₀),
      ExceptionalContractionSequence c p p₀ g ∧ IsMinimalModel c p₀ e₀
```

## Tag 0C2W, a proposition

[Tag 0C2W](https://stacks.math.columbia.edu/tag/0C2W) in the Stacks Project.

**`Stacks.Models.exists_isMinimalModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/MinimalModelExistence.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/MinimalModelExistence.lean#L165). References: SGA 7 I (3.5), “partial”.

> **Stacks Project, Tag 0C2W.** Let `C` be a smooth projective curve over `K` with
> `H⁰(C, 𝒪_C) = K`. A minimal model of `C` exists.
>
> The proof is the source's: the scheme-theoretic image of `C` in a projective space over `R` is a
> projective model, a resolution of its singularities is a regular proper model
> (`Stacks.Models.exists_isModel_isProper_isRegular`, through [Stacks, Tag 0C2S] and
> [Stacks, Tag 0C2U]), and [Stacks, Tag 0CD9] contracts it to a minimal model.

```lean
theorem exists_isMinimalModel {C : Scheme.{u}} (c : C ⟶ Spec (.of K)) [IsCurve K c] [Smooth c]
    (hproj : Stacks.HProjective.IsHProjective c)
    (hH0 : IsIso ((Scheme.ΓSpecIso (.of K)).inv ≫ c.appTop)) :
    ∃ (X : Scheme.{u}) (p : X ⟶ Spec (.of R))
      (e : C ≅ pullback p (Spec.map (CommRingCat.ofHom (algebraMap R K)))),
      IsMinimalModel c p e
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 55.8, Tag 0C2R](https://stacks.math.columbia.edu/tag/0C2R)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
