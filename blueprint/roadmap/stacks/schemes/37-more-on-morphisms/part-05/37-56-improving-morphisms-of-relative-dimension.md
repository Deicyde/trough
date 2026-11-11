---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_curveDiagram_near_genericPoint
statement: formalized
proof: formalized
---

# 37.56 Improving morphisms of relative dimension one

Section 37.56 of the Stacks Project, [Tag 0GK6](https://stacks.math.columbia.edu/tag/0GK6). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GK7, a lemma

[Tag 0GK7](https://stacks.math.columbia.edu/tag/0GK7) in the Stacks Project.

**`AlgebraicGeometry.exists_curveDiagram_near_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeDimensionOne/CurveDiagram.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeDimensionOne/CurveDiagram.lean#L483).

> **Stacks Project, Tag 0GK7.** Let `f : X ⟶ S` be separated and of finite presentation, and
> let `η` be a generic point of an irreducible component of `S` such that `dim(X_η) ≤ 1`. Then
> there are
>
> 1. an open neighbourhood `U` of `η`,
> 2. a finite, surjective, universally injective morphism `V ⟶ U`,
> 3. the base change `X_V = V ×_S X`, a pullback square over `V ⟶ U ⟶ S`,
> 4. a finite surjective morphism `ν : ∐ Yᵢ ⟶ X_V` and an open `W ⊆ X_V` such that `W` is dense
>    in all fibres of `X_V ⟶ V`, `ν⁻¹(W) ∩ Yᵢ` is dense in all fibres of `Yᵢ ⟶ Tᵢ`, and
>    `ν⁻¹(W) ⟶ W` is a thickening,
> 5. open immersions `jᵢ : Yᵢ ⟶ Ȳᵢ`,
> 6. finite étale morphisms `Tᵢ ⟶ V`,
> 7. surjective smooth morphisms `Yᵢ ⟶ Tᵢ`, and
> 8. smooth proper morphisms `Ȳᵢ ⟶ Tᵢ` with geometrically connected fibres of dimension at most
>    one,
>
> such that the diagram commutes: `jᵢ ≫ (Ȳᵢ ⟶ Tᵢ) = (Yᵢ ⟶ Tᵢ)` and the map `Yᵢ ⟶ X_V ⟶ V` is
> `Yᵢ ⟶ Tᵢ ⟶ V`.

```lean
theorem exists_curveDiagram_near_genericPoint {X S : Scheme.{u}} (f : X ⟶ S) [IsSeparated f]
    (hf : FinitePresentation f) (η : S) (hη : η ∈ genericPoints S)
    (hdim : topologicalKrullDim (f.fiber η) ≤ 1) :
    ∃ (U : S.Opens) (_ : η ∈ U) (V : Scheme.{u}) (v : V ⟶ U.toScheme),
      IsFinite v ∧ Surjective v ∧ UniversallyInjective v ∧
      ∃ (XV : Scheme.{u}) (a : XV ⟶ X) (pV : XV ⟶ V), IsPullback a pV f (v ≫ U.ι) ∧
      ∃ (n : ℕ) (T Y Ybar : Fin n → Scheme.{u}) (t : ∀ i, T i ⟶ V) (q : ∀ i, Y i ⟶ T i)
        (qbar : ∀ i, Ybar i ⟶ T i) (j : ∀ i, Y i ⟶ Ybar i) (ν : (∐ Y) ⟶ XV) (W : XV.Opens),
        (∀ i, j i ≫ qbar i = q i) ∧ (∀ i, Sigma.ι Y i ≫ ν ≫ pV = q i ≫ t i) ∧
        IsFinite ν ∧ Surjective ν ∧
        (∀ s : V, Dense ((pV.fiberι s) ⁻¹' (W : Set XV))) ∧
        (∀ i (s : T i), Dense (((q i).fiberι s) ⁻¹' ((Sigma.ι Y i ≫ ν) ⁻¹' (W : Set XV)))) ∧
        Stacks.Thickenings.IsThickening (ν ∣_ W) ∧
        (∀ i, IsOpenImmersion (j i)) ∧ (∀ i, IsFinite (t i) ∧ Etale (t i)) ∧
        (∀ i, Surjective (q i) ∧ Smooth (q i)) ∧
        (∀ i, IsProper (qbar i) ∧ Smooth (qbar i) ∧
          (∀ s : T i, GeometricallyConnected ((qbar i).fiberToSpecResidueField s)) ∧
          ∀ s : T i, topologicalKrullDim ((qbar i).fiber s) ≤ 1)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.56, Tag 0GK6](https://stacks.math.columbia.edu/tag/0GK6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
