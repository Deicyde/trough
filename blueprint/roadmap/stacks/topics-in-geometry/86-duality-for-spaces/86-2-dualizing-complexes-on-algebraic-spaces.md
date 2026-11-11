---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.forall_isDualizingOnChart_iff_exists_surjective, AlgebraicGeometry.Space.IsDualizingComplex, AlgebraicGeometry.Space.IsDualizingComplexOnSpace, AlgebraicGeometry.AffineEtaleDuality.isIso_comparison_app, AlgebraicGeometry.Space.dualizingComplex_duality, AlgebraicGeometry.Space.exists_isInvertible_tensor_iso_of_isDualizingComplexOnSpace, AlgebraicGeometry.Space.exists_dimensionFunction_of_isDualizingComplex_chart, AlgebraicGeometry.Space.exists_dimensionFunction_isNormalizedDualizingComplex_geometricDerivedStalk
statement: formalized
proof: formalized
---

# 86.2 Dualizing complexes on algebraic spaces

Section 86.2 of the Stacks Project, [Tag 0E4X](https://stacks.math.columbia.edu/tag/0E4X). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E4Y, a lemma

[Tag 0E4Y](https://stacks.math.columbia.edu/tag/0E4Y) in the Stacks Project.

**`AlgebraicGeometry.Space.forall_isDualizingOnChart_iff_exists_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualizingComplexEtaleCharts.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualizingComplexEtaleCharts.lean#L295).

> **Stacks Project, Tag 0E4Y.** Let `X` be a locally Noetherian algebraic space over `S` and
> let `K` be an object of `D_QCoh(𝒪_X)`. Then the restriction `K|_U` is a dualizing complex on `U`,
> in the sense of Stacks 0E4X, for every étale morphism `h_U ⟶ X` with `U` a scheme if and only if
> it is one for some surjective such morphism.
>
> The ascent from `U` to `U ×_X V` and the descent from there to `V` are Stacks 0E4N, applied to the
> dualizing complex `ω_U` with `K|_U = ε^*ω_U` and to the complex `ω_V` with `K|_V = ε^*ω_V` that
> Stacks 071Q provides; the two pullbacks to `U ×_X V` agree because `ε^*` commutes with étale
> pullback and is fully faithful on `D_QCoh`.

```lean
theorem forall_isDualizingOnChart_iff_exists_surjective
    (hX : IsAlgebraicSpace B S hS X)
    (hN : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (K : QuasicoherentDerivedCategory.{u, u} B S hS X hX) :
    (∀ (U : BigFppfOver B S hS) (φ : yoneda.obj U ⟶ X)
        (hφ : (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) φ),
        IsDualizingRestriction B S hS X hX hN K.obj U φ hφ) ↔
      ∃ (U : BigFppfOver B S hS) (φ : yoneda.obj U ⟶ X)
        (hφ : (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) φ),
        (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) φ ∧
          IsDualizingRestriction B S hS X hX hN K.obj U φ hφ
```

## Tag 0E4Z, a definition

[Tag 0E4Z](https://stacks.math.columbia.edu/tag/0E4Z) in the Stacks Project.

**`AlgebraicGeometry.Space.IsDualizingComplex`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualizingComplexEtaleCharts.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualizingComplexEtaleCharts.lean#L331). The attribute's comment: “the every-chart condition of 0E4Y; the restrictions of K to the etale scheme charts of X are the family L”.

> **Stacks Project, Tag 0E4Z.** An object of `D_QCoh(𝒪_X)` on a locally Noetherian algebraic
> space `X` over `S` is a *dualizing complex* when its restriction to every étale scheme chart of
> `X` is a dualizing complex on that chart, in the sense of Stacks 0A87.
>
> This is the chart-family formulation, written before the restriction of an object of `D(𝒪_X)` to
> a chart was available: the object is presented by a family `L` of complexes on the Zariski sites
> of the charts, `quasicoherent` and `pullback_compat` are what membership in `D_QCoh(𝒪_X)` says
> about the family of its restrictions, and `isDualizingOnChart` is the every-chart condition of
> Stacks 0E4Y. The notion phrased on an object of `D_QCoh(𝒪_X)` itself is
> `AlgebraicGeometry.Space.IsDualizingComplexOnSpace`.

```lean
structure IsDualizingComplex (hX : IsAlgebraicSpace B S hS X)
    (hN : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (L : ∀ (U : BigFppfOver B S hS) (φ : yoneda.obj U ⟶ X),
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) φ →
      DerivedCategory ((BigFppfOver.toScheme B S hS).obj U).Modules) : Prop
```

**`AlgebraicGeometry.Space.IsDualizingComplexOnSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualizingComplexEtaleCharts.lean, line 461](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualizingComplexEtaleCharts.lean#L461).

> **Stacks Project, Tag 0E4Z.** An object `K` of `D_QCoh(𝒪_X)` on a locally Noetherian algebraic
> space `X` over `S` is a *dualizing complex* when it satisfies the equivalent conditions of Stacks
> 0E4Y: its restriction `K|_U` to every étale morphism `h_U ⟶ X` with `U` a scheme is a dualizing
> complex on `U` in the sense of Stacks 0E4X, that is `K|_U = ε^*ω_U` for a dualizing complex `ω_U`
> on `U` (`AlgebraicGeometry.Space.IsDualizingRestriction`). By
> `AlgebraicGeometry.Space.forall_isDualizingOnChart_iff_exists_surjective` it is enough to ask this
> for one surjective such morphism.

```lean
def IsDualizingComplexOnSpace (hX : IsAlgebraicSpace B S hS X)
    (hN : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (K : QuasicoherentDerivedCategory.{u, u} B S hS X hX) : Prop
```

## Tag 0E50, a lemma

[Tag 0E50](https://stacks.math.columbia.edu/tag/0E50) in the Stacks Project.

**`AlgebraicGeometry.AffineEtaleDuality.isIso_comparison_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleDuality/Derived.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleDuality/Derived.lean#L366).

> **Stacks 0E50.** Let `A` be a Noetherian ring and `X = Spec A`, let `𝒪_étale` be the
> structure sheaf of the small étale site of `X`, and let `ε : (X_étale, 𝒪_étale) ⟶ (X, 𝒪_X)` be
> the comparison morphism. For `K, L ∈ D(A)` with `K ∈ D_Coh(A)` and `L` of finite injective
> dimension, the canonical map
> `ε^* (R Hom_A(K, L))~ ⟶ R SheafHom_{𝒪_étale}(ε^* K̃, ε^* L̃)` is an isomorphism in `D(𝒪_étale)`.
>
> The source is lifted to the module universe of the derived internal Hom, which on the small étale
> site lands one universe up (`AlgebraicGeometry.SmallEtale.derivedSheafHomBifunctor`).

```lean
theorem isIso_comparison_app [IsNoetherianRing A] (K L : DerivedCategory (ModuleCat.{u} A))
    (hK : ∀ n : ℤ, Module.Finite A ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) n).obj K))
    (hL : StacksDraft.InjectiveDimension.HasFiniteInjectiveDimension L) :
    IsIso ((comparison A B hX).app (op K, L))
```

## Tag 0E51, a lemma

[Tag 0E51](https://stacks.math.columbia.edu/tag/0E51) in the Stacks Project.

**`AlgebraicGeometry.Space.dualizingComplex_duality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DerivedDuality/SpaceDuality.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DerivedDuality/SpaceDuality.lean#L240).

> **Stacks 0E51.** Let `X` be a locally Noetherian algebraic space and `K` a dualizing complex
> on `X` (Stacks 0E4Z). Then
>
> * `K` is an object of `D_Coh(𝒪_X)`;
> * `D = R𝓗om_{𝒪_X}(-, K)` carries `D_Coh(𝒪_X)` to itself and induces an anti-equivalence
>   `D : D_Coh(𝒪_X)ᵒᵖ ≌ D_Coh(𝒪_X)`, which comes equipped with the canonical isomorphism
>   `id → D ∘ D` whose components are the biduality morphisms `L ⟶ R𝓗om(R𝓗om(L, K), K)`;
> * if `X` is quasi-compact, `D` carries `D^+_Coh(𝒪_X)` to `D^-_Coh(𝒪_X)` and `D^-_Coh(𝒪_X)` to
>   `D^+_Coh(𝒪_X)` (and induces an anti-equivalence between them), and induces an
>   anti-equivalence `D^b_Coh(𝒪_X)ᵒᵖ ≌ D^b_Coh(𝒪_X)`.

```lean
theorem dualizingComplex_duality (K : QuasicoherentDerivedCategory.{u, u} B S hS F hF)
    (hK : IsDualizingComplexOnSpace B S hS F hF hN K) :
    coherentDerived B S hS F hF K.obj ∧
    ∃ hD : ∀ L, coherentDerived B S hS F hF L →
        coherentDerived B S hS F hF ((dualFunctor B S hS F hF K.obj).obj (op L)),
      (∃ e : (coherentDerived B S hS F hF).FullSubcategoryᵒᵖ ≌
          (coherentDerived B S hS F hF).FullSubcategory,
        e.functor = (coherentDerived B S hS F hF).lift
          ((coherentDerived B S hS F hF).ι.op ⋙ dualFunctor B S hS F hF K.obj)
          (fun L => hD _ L.unop.2)) ∧
      (∃ η : 𝟭 (coherentDerived B S hS F hF).FullSubcategory ≅
          ((coherentDerived B S hS F hF).lift
            ((coherentDerived B S hS F hF).ι.op ⋙ dualFunctor B S hS F hF K.obj)
            (fun L => hD _ L.unop.2)).rightOp ⋙
          (coherentDerived B S hS F hF).lift
            ((coherentDerived B S hS F hF).ι.op ⋙ dualFunctor B S hS F hF K.obj)
            (fun L => hD _ L.unop.2),
        ∀ L, (coherentDerived B S hS F hF).ι.map (η.hom.app L) =
          (derivedBiduality B S hS F hF K.obj).app L.1) ∧
      (IsQuasiCompactSpace B S hS F →
        (∀ L, coherentDerivedPlus B S hS F hF L →
          coherentDerivedMinus B S hS F hF ((dualFunctor B S hS F hF K.obj).obj (op L))) ∧
        (∀ L, coherentDerivedMinus B S hS F hF L →
          coherentDerivedPlus B S hS F hF ((dualFunctor B S hS F hF K.obj).obj (op L))) ∧
        (∃ (hpm : ∀ L, coherentDerivedPlus B S hS F hF L →
            coherentDerivedMinus B S hS F hF ((dualFunctor B S hS F hF K.obj).obj (op L)))
          (e : (coherentDerivedPlus B S hS F hF).FullSubcategoryᵒᵖ ≌
            (coherentDerivedMinus B S hS F hF).FullSubcategory),
          e.functor = (coherentDerivedMinus B S hS F hF).lift
            ((coherentDerivedPlus B S hS F hF).ι.op ⋙ dualFunctor B S hS F hF K.obj)
            (fun L => hpm _ L.unop.2)) ∧
        (∃ (hb : ∀ L, coherentDerivedBounded B S hS F hF L →
            coherentDerivedBounded B S hS F hF ((dualFunctor B S hS F hF K.obj).obj (op L)))
          (e : (coherentDerivedBounded B S hS F hF).FullSubcategoryᵒᵖ ≌
            (coherentDerivedBounded B S hS F hF).FullSubcategory),
          e.functor = (coherentDerivedBounded B S hS F hF).lift
            ((coherentDerivedBounded B S hS F hF).ι.op ⋙ dualFunctor B S hS F hF K.obj)
            (fun L => hb _ L.unop.2)))
```

## Tag 0E52, a lemma

[Tag 0E52](https://stacks.math.columbia.edu/tag/0E52) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isInvertible_tensor_iso_of_isDualizingComplexOnSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualizingUniqueness/Uniqueness.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualizingUniqueness/Uniqueness.lean#L195).

> **Stacks 0E52.** Let `S` be a scheme and `X` a locally Noetherian algebraic space over `S`. If
> `K` and `K'` are dualizing complexes on `X` (Stacks 0E4Z), then `K'` is isomorphic to
> `K ⊗^L_{𝒪_X} L` for some invertible object `L` of `D(𝒪_X)`.
>
> `D(𝒪_X)` is the derived category of the `𝒪_X`-modules on the small étale site of `X`, and
> `⊗^L_{𝒪_X}` with its unit `𝒪_X` is `AlgebraicGeometry.Space.derivedMonoidalOfModel`, the derived
> tensor product of Stacks 0FPT read on the equi-universe model of the small étale ringed site.
> The proof is the source's: `R𝓗om(K', K)` is invertible because affine locally `K'` is a shift
> of `K` (Stacks 0A7F, 0ATP) and `R𝓗om(K, K) = 𝒪_X`, and `K' ≅ R𝓗om(R𝓗om(K', K), K)` by
> biduality (Stacks 0E51).

```lean
theorem exists_isInvertible_tensor_iso_of_isDualizingComplexOnSpace
    (hN : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (K K' : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2)
    (hK : IsDualizingComplexOnSpace B S hS X.1 X.2 hN K)
    (hK' : IsDualizingComplexOnSpace B S hS X.1 X.2 hN K') :
    letI := derivedMonoidalOfModel B S hS X.1 X.2
    ∃ L, IsInvertible L ∧ Nonempty (K'.obj ≅ K.obj ⊗ L)
```

## Tag 0E53, a lemma

[Tag 0E53](https://stacks.math.columbia.edu/tag/0E53) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_dimensionFunction_of_isDualizingComplex_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualizingDimensionFunction.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualizingDimensionFunction.lean#L108).

> Let `X` be a locally Noetherian quasi-separated algebraic space over a scheme `S` and let
> `ω_X^•` be a dualizing complex on `X` (Stacks 0E4Z). Then the function `δ : |X| → ℤ` for which
> `ω^•_{X, x̄}[-δ x]` is a normalized dualizing complex over `𝒪_{X, x̄}` at every geometric point
> `x̄` of `X` over `x` is a dimension function on `|X|`.

```lean
theorem exists_dimensionFunction_of_isDualizingComplex_chart
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X)
    (hN : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (ω : QuasicoherentDerivedCategory.{u, u} B S hS X hX)
    (hω : IsDualizingComplexOnSpace B S hS X hX hN ω)
    (δ : points B S hS X → ℤ)
    (hδ : IsNormalizingShiftAtGeometricPoints B S hS ⟨X, hX⟩ hN ω.obj δ) :
    ∃ d : DimensionFunction (points B S hS X), ∀ x : points B S hS X, d x = δ x
```

**`AlgebraicGeometry.Space.exists_dimensionFunction_isNormalizedDualizingComplex_geometricDerivedStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualizingDimensionFunction.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DualizingDimensionFunction.lean#L371).

> Let `X` be a locally Noetherian quasi-separated algebraic space over a scheme `S` and let
> `ω_X^•` be a dualizing complex on `X` (Stacks 0E4Z). Then there is a dimension function `δ` on
> `|X|` such that at every geometric point `x̄` of `X`, lying over `x ∈ |X|`, the stalk `ω_{X, x̄}^•`
> is a dualizing complex over the étale local ring `𝒪_{X, x̄}` and `δ x` is the unique integer `n`
> for which `ω_{X, x̄}^•[-n]` is a normalized dualizing complex. In particular the normalizing shift
> exists at every geometric point and depends only on the point of `|X|` under it.

```lean
theorem exists_dimensionFunction_isNormalizedDualizingComplex_geometricDerivedStalk
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X)
    (hN : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (ω : QuasicoherentDerivedCategory.{u, u} B S hS X hX)
    (hω : IsDualizingComplexOnSpace B S hS X hX hN ω) :
    ∃ δ : DimensionFunction (points B S hS X),
      ∀ x : GeometricPoint B S hS X,
        letI := isNoetherianRing_geometricStalkRing B S hS ⟨X, hX⟩ hN x
        letI := isLocalRing_geometricStalkRing B S hS ⟨X, hX⟩ x
        Dualizing.IsDualizingComplex ((geometricDerivedStalk B S hS (X := ⟨X, hX⟩) x).obj ω.obj) ∧
          ∀ n : ℤ, Dualizing.IsNormalizedDualizingComplex.{u, u}
              ((geometricDerivedStalk B S hS (X := ⟨X, hX⟩) x).obj ω.obj⟦-n⟧) ↔ n = δ x.image
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 86.2, Tag 0E4X](https://stacks.math.columbia.edu/tag/0E4X)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
