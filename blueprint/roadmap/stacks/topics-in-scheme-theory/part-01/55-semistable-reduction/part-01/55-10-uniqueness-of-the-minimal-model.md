---
declaration: section
origin: cited
lean: Stacks.Models.exists_isMinimalModel_and_existsUnique_iso, Stacks.Models.existsUnique_exceptionalContractionSequence_of_isMinimalModel, Stacks.Models.GenusZero.minimalModel_not_unique
statement: formalized
proof: formalized
---

# 55.10 Uniqueness of the minimal model

Section 55.10 of the Stacks Project, [Tag 0C9Y](https://stacks.math.columbia.edu/tag/0C9Y). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C6B, a lemma

[Tag 0C6B](https://stacks.math.columbia.edu/tag/0C6B) in the Stacks Project.

**`Stacks.Models.exists_isMinimalModel_and_existsUnique_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/MinimalModelUniqueness.lean, line 686](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/MinimalModelUniqueness.lean#L686).

> **Stacks Project, Tag 0C6B.** Let `C` be a smooth projective curve over `K` with
> `H⁰(C, 𝒪_C) = K` and genus `> 0`. There is a unique minimal model for `C`: a minimal model exists,
> and any two minimal models are isomorphic by a unique isomorphism of models, that is, over `R`
> and compatible with the identifications of their generic fibres with `C`.

```lean
theorem exists_isMinimalModel_and_existsUnique_iso {C : Scheme.{u}} (c : C ⟶ Spec (.of K))
    [IsCurve K c] [Smooth c] (hproj : Stacks.HProjective.IsHProjective c)
    (hH0 : IsIso ((Scheme.ΓSpecIso (.of K)).inv ≫ c.appTop)) (hg : 0 < genus c) :
    (∃ (X : Scheme.{u}) (p : X ⟶ Spec (.of R))
      (e : C ≅ pullback p (Spec.map (CommRingCat.ofHom (algebraMap R K)))),
      IsMinimalModel c p e) ∧
    ∀ {X Y : Scheme.{u}} (p : X ⟶ Spec (.of R)) (q : Y ⟶ Spec (.of R))
      (eX : C ≅ pullback p (Spec.map (CommRingCat.ofHom (algebraMap R K))))
      (eY : C ≅ pullback q (Spec.map (CommRingCat.ofHom (algebraMap R K)))),
      IsMinimalModel c p eX → IsMinimalModel c q eY →
        ∃! φ : X ≅ Y, φ.hom ≫ q = p ∧
          eX.hom ≫ pullback.fst p (Spec.map (CommRingCat.ofHom (algebraMap R K))) ≫ φ.hom =
            eY.hom ≫ pullback.fst q (Spec.map (CommRingCat.ofHom (algebraMap R K)))
```

## Tag 0C9Z, a lemma

[Tag 0C9Z](https://stacks.math.columbia.edu/tag/0C9Z) in the Stacks Project.

**`Stacks.Models.existsUnique_exceptionalContractionSequence_of_isMinimalModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/MinimalModelMappingProperty.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/MinimalModelMappingProperty.lean#L157).

> **Stacks Project, Tag 0C9Z.** Let `C` be a smooth projective curve over `K` with
> `H⁰(C, 𝒪_C) = K` and genus `> 0`, let `X` be the minimal model of `C` and let `Y` be a regular
> proper model of `C`. Then there is a unique morphism of models `Y ⟶ X` which is a sequence of
> contractions of exceptional curves of the first kind.
>
> A morphism of models is a morphism over `R` compatible with the identifications of the generic
> fibres with `C`; "a sequence of contractions" is a sequence `Y = Xₘ → ⋯ → X₀` of contractions of
> exceptional curves of the first kind between regular proper models of `C`
> (`Stacks.Models.ExceptionalContractionSequence`), followed by an isomorphism of `X₀` with `X`
> over `R`. The morphism is unique among all morphisms of models, and is a sequence of contractions
> by [Stacks, Tag 0CD9] and [Stacks, Tag 0C6B].

```lean
theorem existsUnique_exceptionalContractionSequence_of_isMinimalModel {C X Y : Scheme.{u}}
    (c : C ⟶ Spec (.of K)) [IsCurve K c] [Smooth c] (hg : 0 < genus c)
    (p : X ⟶ Spec (.of R)) (eX : C ≅ pullback p (Spec.map (CommRingCat.ofHom (algebraMap R K))))
    (hX : IsMinimalModel c p eX) (q : Y ⟶ Spec (.of R))
    (eY : C ≅ pullback q (Spec.map (CommRingCat.ofHom (algebraMap R K))))
    (hmod : IsModel c q eY) [IsProper q] (hreg : IsRegular Y) :
    ∃! f : Y ⟶ X, (f ≫ p = q ∧
      eY.hom ≫ pullback.fst q (Spec.map (CommRingCat.ofHom (algebraMap R K))) ≫ f =
        eX.hom ≫ pullback.fst p (Spec.map (CommRingCat.ofHom (algebraMap R K)))) ∧
      ∃ (X₀ : Scheme.{u}) (p₀ : X₀ ⟶ Spec (.of R)) (g : Y ⟶ X₀) (ψ : X₀ ≅ X),
        ExceptionalContractionSequence c q p₀ g ∧ ψ.hom ≫ p = p₀ ∧ g ≫ ψ.hom = f
```

## Tag 0CA0, an example

[Tag 0CA0](https://stacks.math.columbia.edu/tag/0CA0) in the Stacks Project.

**`Stacks.Models.GenusZero.minimalModel_not_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/GenusZeroExample.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/GenusZeroExample.lean#L70).

> **Stacks Project, Tag 0CA0: in genus zero, minimal models are not unique.** Let `R` be a
> discrete valuation ring with fraction field `K`, residue field `k` and uniformizer `π`, and let
> `X = Proj R[T₀, T₁, T₂]/(T₁T₂ - πT₀²)`.
>
> 1. `X` is a closed subscheme of `ℙ²_R`, regular and proper over `R`, and a model of `ℙ¹_K`, its
>    generic fibre being identified with `ℙ¹_K` by `[u : v] ↦ [uv : v² : πu²]`.
> 2. The special fibre of `X` is the union, and as a divisor the sum, of the lines
>    `C₁ = V(π, T₁)` and `C₂ = V(π, T₂)`; each is a copy of `ℙ¹_k` and an exceptional curve of the
>    first kind on `X`. In particular `X` is not a minimal model.
> 3. The projection `[T₂ : T₀]` from `(0 : 1 : 0)` is a morphism of models from `X` to `ℙ¹_R` with
>    the identification `e₂` of its generic fibre twisted by `[u : v] ↦ [πu : v]`; it contracts
>    `C₂` to a `k`-point and maps `C₁` isomorphically onto the special fibre of `ℙ¹_R`. The
>    projection `[T₀ : T₁]` from `(0 : 0 : 1)` is a morphism of models from `X` to `ℙ¹_R` with the
>    canonical identification `e₁`; it contracts `C₁` and maps `C₂` isomorphically onto the special
>    fibre of `ℙ¹_R`.
> 4. `(ℙ¹_R, e₁)` and `(ℙ¹_R, e₂)` are minimal models of `ℙ¹_K`, and no isomorphism of models
>    relates them.

```lean
theorem minimalModel_not_unique (hπ : Irreducible π) :
    -- (1) `X ⊆ ℙ²_R` is a regular proper model of `ℙ¹_K`
    IsClosedImmersion (PlaneCurveModel.embedding (conicEquation π)
      (isHomogeneous_conicEquation π)) ∧
    IsRegular (conicScheme π) ∧ IsProper (conicToSpec π) ∧
    IsModel (projectiveSpaceOverRing 1 (.of K) ↘ Spec (.of K)) (conicToSpec π)
      (conicGenericFibreIso (K := K) hπ) ∧
    -- (2) the special fibre is `C₁ + C₂`, two exceptional curves of the first kind
    Set.range (pullback.fst (conicToSpec π) (residueSpecMap R)) =
      Set.range (firstLine (mem_maximalIdeal_of_irreducible hπ)) ∪
        Set.range (secondLine (mem_maximalIdeal_of_irreducible hπ)) ∧
    (pullback.fst (conicToSpec π) (residueSpecMap R)).ker =
      (firstLine (mem_maximalIdeal_of_irreducible hπ)).ker *
        (secondLine (mem_maximalIdeal_of_irreducible hπ)).ker ∧
    (firstLine (mem_maximalIdeal_of_irreducible hπ)).ker.IsExceptionalCurveOfFirstKind κ
      (firstLineIso hπ) ∧
    (secondLine (mem_maximalIdeal_of_irreducible hπ)).ker.IsExceptionalCurveOfFirstKind κ
      (secondLineIso hπ) ∧
    (conicScheme π).HasExceptionalCurveOfFirstKind ∧
    -- (3) the projection from `(0 : 1 : 0)` contracts `C₂` and maps `C₁` onto the special fibre
    IsModelHom (conicToSpec π) (projectiveSpaceOverRing 1 (.of R) ↘ Spec (.of R))
      (conicGenericFibreIso (K := K) hπ) (twistedGenericFibreIso (K := K) hπ) (secondProjection π) ∧
    (∃ q : Spec (.of κ) ⟶ projectiveSpaceOverRing 1 (.of R),
      secondLine (mem_maximalIdeal_of_irreducible hπ) ≫ secondProjection π =
        projToSpecCoeff κ 1 ≫ q) ∧
    (∃ e : AlgebraicGeometry.Proj (lineGrading κ) ≅
        pullback (projectiveSpaceOverRing 1 (.of R) ↘ Spec (.of R)) (residueSpecMap R),
      firstLine (mem_maximalIdeal_of_irreducible hπ) ≫ secondProjection π =
        e.hom ≫ pullback.fst _ _) ∧
    -- the projection from `(0 : 0 : 1)` contracts `C₁` and maps `C₂` onto the special fibre
    IsModelHom (conicToSpec π) (projectiveSpaceOverRing 1 (.of R) ↘ Spec (.of R))
      (conicGenericFibreIso (K := K) hπ) (projectiveLineGenericFibreIso (K := K))
      (firstProjection π) ∧
    (∃ q : Spec (.of κ) ⟶ projectiveSpaceOverRing 1 (.of R),
      firstLine (mem_maximalIdeal_of_irreducible hπ) ≫ firstProjection π =
        projToSpecCoeff κ 1 ≫ q) ∧
    (∃ e : AlgebraicGeometry.Proj (lineGrading κ) ≅
        pullback (projectiveSpaceOverRing 1 (.of R) ↘ Spec (.of R)) (residueSpecMap R),
      secondLine (mem_maximalIdeal_of_irreducible hπ) ≫ firstProjection π =
        e.hom ≫ pullback.fst _ _) ∧
    -- (4) two minimal models of `ℙ¹_K`, not isomorphic as models
    IsMinimalModel (projectiveSpaceOverRing 1 (.of K) ↘ Spec (.of K))
      (projectiveSpaceOverRing 1 (.of R) ↘ Spec (.of R)) (projectiveLineGenericFibreIso (K := K)) ∧
    IsMinimalModel (projectiveSpaceOverRing 1 (.of K) ↘ Spec (.of K))
      (projectiveSpaceOverRing 1 (.of R) ↘ Spec (.of R)) (twistedGenericFibreIso (K := K) hπ) ∧
    ¬ ∃ g : projectiveSpaceOverRing 1 (.of R) ⟶ projectiveSpaceOverRing 1 (.of R), IsIso g ∧
      IsModelHom (projectiveSpaceOverRing 1 (.of R) ↘ Spec (.of R))
        (projectiveSpaceOverRing 1 (.of R) ↘ Spec (.of R))
        (projectiveLineGenericFibreIso (K := K)) (twistedGenericFibreIso hπ) g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 55.10, Tag 0C9Y](https://stacks.math.columbia.edu/tag/0C9Y)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
