---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.exists_smooth_atlas_iff_forall_smooth_chart, AlgebraicGeometry.Stack.forall_smooth_chart_iff_forall_space, AlgebraicGeometry.Stack.forall_smooth_chart_iff_finite_irreducibleComponents, AlgebraicGeometry.Stack.AlgebraicStacks.isIntegralHom_normalization_and_isTwoFibreProduct_normSpace, AlgebraicGeometry.Stack.AlgebraicStacks.exists_isIntegralHom_and_isTwoFibreProduct_normSpace, AlgebraicGeometry.Stack.AlgebraicStacks.normalization, AlgebraicGeometry.Stack.normalization
statement: formalized
proof: formalized
---

# 101.46 Normalization

Section 101.46 of the Stacks Project, [Tag 0GMH](https://stacks.math.columbia.edu/tag/0GMH). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GMI, a lemma

[Tag 0GMI](https://stacks.math.columbia.edu/tag/0GMI) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_smooth_atlas_iff_forall_smooth_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Normalization.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Normalization.lean#L120). The attribute's comment: “conditions (1) and (2)”.

> **Stacks 0GMI, conditions (1) and (2).** One smooth surjective scheme chart whose
> quasi-compact opens have finitely many irreducible components suffices: then every smooth scheme
> chart of the algebraic stack has that property.

```lean
theorem exists_smooth_atlas_iff_forall_smooth_chart (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    HasPropertyOnSomeSchemeAtlas B S hS
        (fun X : Scheme.{u} =>
          ∀ V : X.Opens, IsCompact (V : Set X) → (irreducibleComponents V).Finite) 𝒳 ↔
      HasPropertyOnEverySchemeChart B S hS
        (fun X : Scheme.{u} =>
          ∀ V : X.Opens, IsCompact (V : Set X) → (irreducibleComponents V).Finite) 𝒳
```

**`AlgebraicGeometry.Stack.forall_smooth_chart_iff_forall_space`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Normalization.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Normalization.lean#L133). The attribute's comment: “conditions (2) and (3)”.

> **Stacks 0GMI, conditions (2) and (3).** Every smooth scheme chart of the algebraic stack has
> finitely many irreducible components over each of its quasi-compact opens exactly when every
> algebraic space smooth over it satisfies the equivalent conditions of Tag 0BB1.

```lean
theorem forall_smooth_chart_iff_forall_space (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    HasPropertyOnEverySchemeChart B S hS
        (fun X : Scheme.{u} =>
          ∀ V : X.Opens, IsCompact (V : Set X) → (irreducibleComponents V).Finite) 𝒳 ↔
      ∀ (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
        (f : algebraicSpaceStack.{u, w} B S hS F hF ⟶ 𝒳),
        AlgebraicStacks.IsSmooth B S hS f →
          Space.HasLocallyFiniteIrreducibleComponents B S hS F
```

**`AlgebraicGeometry.Stack.forall_smooth_chart_iff_finite_irreducibleComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Normalization.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Normalization.lean#L153). The attribute's comment: “conditions (2) and (4)”.

> **Stacks 0GMI, conditions (2) and (4).** Every smooth scheme chart of the algebraic stack has
> finitely many irreducible components over each of its quasi-compact opens exactly when the space
> of points of Tag 04XL of every quasi-compact algebraic stack smooth over it has finitely many
> irreducible components.

```lean
theorem forall_smooth_chart_iff_finite_irreducibleComponents
    (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    HasPropertyOnEverySchemeChart B S hS
        (fun X : Scheme.{u} =>
          ∀ V : X.Opens, IsCompact (V : Set X) → (irreducibleComponents V).Finite) 𝒳 ↔
      ∀ (𝒴 : AlgebraicStacks.{u, w} B S hS) (f : 𝒴 ⟶ 𝒳),
        IsQuasiCompactStack.{u, w} B S hS 𝒴.val 𝒴.property →
          AlgebraicStacks.IsSmooth B S hS f →
            (@irreducibleComponents (AlgebraicStacks.points B S hS 𝒴)
              (pointTopology B S hS 𝒴.val)).Finite
```

## Tag 0GMJ, a lemma

[Tag 0GMJ](https://stacks.math.columbia.edu/tag/0GMJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isIntegralHom_normalization_and_isTwoFibreProduct_normSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/NormalizationBaseChange.lean, line 351](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/NormalizationBaseChange.lean#L351).

> **Stacks 0GMJ.** Let `𝒳` be an algebraic stack over `S` satisfying the equivalent conditions
> of Stacks 0GMI, and let `ν : 𝒳^ν ⟶ 𝒳` be its normalization (Stacks 0GMK). Then `ν` is integral
> (Stacks 0CHU), and for every scheme `U` over `S` and every smooth 1-morphism `f : U ⟶ 𝒳`, every
> 2-fibre product `U ×_𝒳 𝒳^ν` is the normalization of `U`: it is represented by an algebraic space
> isomorphic, over `U`, to the normalization `U^ν ⟶ U` of the scheme `U`
> (`AlgebraicGeometry.Space.normSpace`, `AlgebraicGeometry.Space.normSpaceProj`; Stacks 035N).
>
> The finiteness of irreducible components of the quasi-compact opens of `U` that the
> normalization of `U` needs is condition (2) of Stacks 0GMI for the smooth chart `f`.
>
> Nothing beyond the hypothesis of Stacks 0GMI is assumed: the normalized groupoid, the 2-fibre
> product along the presenting chart and its descent to an arbitrary smooth chart are all
> constructed. This is the complete registration of Stacks 0GMJ; the integrality step of
> `StacksFrontier.AlgebraicGeometry.Stacks.NormalizationMorphism` and the presenting-chart step of
> `StacksFrontier.AlgebraicGeometry.Stacks.NormalizationChartFibreProduct`, which take the normalized
> groupoid as data, are not tagged.

```lean
theorem isIntegralHom_normalization_and_isTwoFibreProduct_normSpace :
    AlgebraicStacks.IsIntegralHom B S hS (normalization 𝒳 h𝒳) ∧
      ∀ (U : BigFppfOver B S hS) (f : schemeStack.{u, w} B S hS U ⟶ 𝒳)
        (hf : AlgebraicStacks.IsSmooth B S hS f)
        (P : Bicategory.TwoCommSq f (normalization 𝒳 h𝒳)) (_ : Bicategory.IsTwoFibreProduct P),
        ∃ (V : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_ : IsAlgebraicSpace B S hS V)
          (eV : StacksRepresentableCFG.EquivalenceOver P.pt.val.val.p
            (presheafOfCategories (V ⋙ typeToCat)).p)
          (e : V ≅ yoneda.obj (Space.normSpace B S hS U
            ((exists_smooth_atlas_iff_forall_smooth_chart B S hS 𝒳).1 h𝒳 U f hf))),
          e.hom ≫ yoneda.map (Space.normSpaceProj B S hS U
              ((exists_smooth_atlas_iff_forall_smooth_chart B S hS 𝒳).1 h𝒳 U f hf)) =
            representingMap B S hS P.pt.val (schemeStack.{u, w} B S hS U).val V (yoneda.obj U) eV
              (PresheafOfCategories.sliceElementsEquivalenceOver U) P.fst.hom
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_isIntegralHom_and_isTwoFibreProduct_normSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/NormalizationBaseChange.lean, line 394](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/NormalizationBaseChange.lean#L394). The attribute's comment: “the existential form”.

> **Stacks 0GMJ, in the existential form the source states.** An algebraic stack `𝒳` over `S`
> satisfying the equivalent conditions of Stacks 0GMI admits an integral 1-morphism of algebraic
> stacks `𝒳^ν ⟶ 𝒳` such that for every scheme `U` and smooth `U ⟶ 𝒳` every 2-fibre product
> `U ×_𝒳 𝒳^ν` is the normalization of `U`. The witness is the normalization of Stacks 0GMK.

```lean
theorem exists_isIntegralHom_and_isTwoFibreProduct_normSpace :
    ∃ (𝒳ν : AlgebraicStacks.{u, w} B S hS) (ν : 𝒳ν ⟶ 𝒳),
      AlgebraicStacks.IsIntegralHom B S hS ν ∧
      ∀ (U : BigFppfOver B S hS) (f : schemeStack.{u, w} B S hS U ⟶ 𝒳)
        (hf : AlgebraicStacks.IsSmooth B S hS f)
        (P : Bicategory.TwoCommSq f ν) (_ : Bicategory.IsTwoFibreProduct P),
        ∃ (V : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_ : IsAlgebraicSpace B S hS V)
          (eV : StacksRepresentableCFG.EquivalenceOver P.pt.val.val.p
            (presheafOfCategories (V ⋙ typeToCat)).p)
          (e : V ≅ yoneda.obj (Space.normSpace B S hS U
            ((exists_smooth_atlas_iff_forall_smooth_chart B S hS 𝒳).1 h𝒳 U f hf))),
          e.hom ≫ yoneda.map (Space.normSpaceProj B S hS U
              ((exists_smooth_atlas_iff_forall_smooth_chart B S hS 𝒳).1 h𝒳 U f hf)) =
            representingMap B S hS P.pt.val (schemeStack.{u, w} B S hS U).val V (yoneda.obj U) eV
              (PresheafOfCategories.sliceElementsEquivalenceOver U) P.fst.hom
```

## Tag 0GMK, a definition

[Tag 0GMK](https://stacks.math.columbia.edu/tag/0GMK) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.normalization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/NormalizationAlgebraicStack.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/NormalizationAlgebraicStack.lean#L130).

> **Stacks 0GMK, the normalization of an algebraic stack.** Let `𝒳` be an algebraic stack
> satisfying the equivalent conditions of Stacks 0GMI. Its *normalization* is the morphism
> `ν : 𝒳^ν ⟶ 𝒳` constructed in the proof of Stacks 0GMJ: for a presentation `𝒳 ≃ [U/R]`
> (Stacks 04T3), `𝒳^ν = [U^ν/R^ν]` is the quotient stack of the normalized groupoid, and `ν` is the
> 1-morphism `[U^ν/R^ν] ⟶ [U/R]` of Stacks 046Q induced by the morphism of groupoids
> `(U^ν, R^ν) ⟶ (U, R)`, followed by the presentation.
>
> Every ingredient is constructed from `𝒳` and the hypothesis of Stacks 0GMI: the normalization
> `U^ν` (Stacks 07U4), the cartesian square `R^ν = U^ν ×_{U, s} R`, the groupoid structure and its
> smoothness are those of `AlgebraicGeometry.Stack.normalizationGroupoid`.

```lean
noncomputable def normalization (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS
      (fun X : Scheme.{u} =>
        ∀ V : X.Opens, IsCompact (V : Set X) → (irreducibleComponents V).Finite) 𝒳) :
    normalizationStack 𝒳 h𝒳 ⟶ 𝒳
```

**`AlgebraicGeometry.Stack.normalization`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/NormalizationMorphism.lean, line 344](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/NormalizationMorphism.lean#L344). The attribute's comment: “the normalization ν : 𝒳^ν ⟶ 𝒳 at a presenting smooth groupoid, with the normalized groupoid as data”.

> **Stacks 0GMK, the normalization of an algebraic stack.** For a groupoid in algebraic spaces
> `(U, R, s, t, c)` presenting `ð³ = [U/R]`, and a normalized groupoid `N` for it, the
> *normalization* of `𝒳` is the 1-morphism `ν : 𝒳^ν ⟶ 𝒳` of Stacks 046Q induced by the
> morphism
> of groupoids `(U^Î½, R^Î½) â¶ (U, R)`, with `ð³^Î½ = [U^Î½/R^Î½]` the quotient stack
> `AlgebraicGeometry.Stack.normalizationStack` of the normalized groupoid.
>
> This is the morphism constructed in Stacks 0GMJ, named: the body is the construction
> `AlgebraicGeometry.Stack.quotientStackMapHom` of the source's proof, so nothing is chosen out of
> the existential of
> `AlgebraicGeometry.Stack.exists_isIntegralHom_quotientStackMapHom_normalization`. Its
> integrality is `AlgebraicGeometry.Stack.isIntegralHom_quotientStackMapHom_normalization`, which
> applies to it unchanged.
>
> The hypothesis of Stacks 0GMI on `ð³` is not a separate assumption, for the reason given in the
> coverage notes of this module's documentation: it is carried inside `N`, whose
> normalization data of the object space contains condition (1) of Stacks 0GMI for the presenting
> chart through
> `AlgebraicGeometry.Space.NormalizationData.finite_irreducibleComponents_of_chart`. The
> equivalences of Stacks 0GMI are stated for `AlgebraicGeometry.Stack.AlgebraicStacks`, and
> exhibiting a quotient stack there is Stacks 04TK, which this library does not have, so no 0GMI
> condition can be stated at this presentation.

```lean
noncomputable abbrev normalization {G : GroupoidInAlgebraicSpaces C S hS B}
    (N : NormalizationGroupoid C S hS G) :
    normalizationStack C S hS N ⟶ quotientStackCFG C S hS G
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.46, Tag 0GMH](https://stacks.math.columbia.edu/tag/0GMH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
