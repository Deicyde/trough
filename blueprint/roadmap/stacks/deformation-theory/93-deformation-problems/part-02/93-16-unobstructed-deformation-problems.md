---
declaration: section
origin: cited
lean: Deformation.Examples.ringDeformationCategory_isSmooth_of_isLocalCompleteIntersection, Deformation.Examples.GluingSituation.isSmooth_toChartProductOfCover, Deformation.Examples.GluingSituation.isSmooth_toChartProductOfCover_comp_snd, Deformation.Examples.isSmooth_localRingFunctors_and_chain, Deformation.Examples.isSmooth_baseProjection_schemeDeformationCategoryProjection, Deformation.Examples.isSmooth_baseProjection_schemeDeformationCategoryProjection_of_lci
statement: formalized
proof: formalized
---

# 93.16 Unobstructed deformation problems

Section 93.16 of the Stacks Project, [Tag 0DZG](https://stacks.math.columbia.edu/tag/0DZG). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DZH, a lemma

[Tag 0DZH](https://stacks.math.columbia.edu/tag/0DZH) in the Stacks Project.

**`Deformation.Examples.ringDeformationCategory_isSmooth_of_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/RingsUnobstructed.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/RingsUnobstructed.lean#L282).

> **Stacks 0DZH.** In the setting of Stacks 0DY1, the deformation category of a local
> complete intersection `P` over a field `k` is unobstructed: the structure functor of
> `Deformation.Examples.ringDeformationCategory P` to the category of Artinian local `Λ`-algebras
> with residue field `k` is smooth.

```lean
public theorem ringDeformationCategory_isSmooth_of_isLocalCompleteIntersection
    {Λ : Type u} {k P : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    [CommRing P] [Algebra k P]
    (hP : IsLocalCompleteIntersection k P) :
    IsSmooth
      (baseProjection
        (Over.forget (residueFieldAlgebra (Λ := Λ) (k := k) P) ⋙
          FlatAlgebraCategory.projection (Λ := Λ) (k := k)))
```

## Tag 0DZN, a lemma

[Tag 0DZN](https://stacks.math.columbia.edu/tag/0DZN) in the Stacks Project.

**`Deformation.Examples.GluingSituation.isSmooth_toChartProductOfCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCoverSmooth.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCoverSmooth.lean#L384). The attribute's comment: “clause 1: Def\_X ⟶ Def\_\{P\_1} × Def\_\{P\_2} is smooth when U\_12 is smooth over k; unconditional, the hypothesis on P\_12 being the source's own”.

> **Stacks Project, Tag 0DZN**, first clause. In Situation 0DYY, if `U₁₂ → Spec(k)` is smooth
> then `Def_X ⟶ Def_{U₁} × Def_{U₂} = Def_{P₁} × Def_{P₂}` is smooth.

```lean
theorem isSmooth_toChartProductOfCover (hU₁₂ : Algebra.Smooth k S.P₁₂) :
    IsSmooth (toChartProductOfCover S)
```

**`Deformation.Examples.GluingSituation.isSmooth_toChartProductOfCover_comp_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCoverSmooth.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCoverSmooth.lean#L407). The attribute's comment: “clause 2: Def\_X ⟶ Def\_\{P\_2} is smooth when U\_12 is smooth over k and U\_1 is a local complete intersection over k; unconditional, the hypotheses on P\_12 and P\_1 being the source's own”.

> **Stacks Project, Tag 0DZN**, second clause. In Situation 0DYY, if `U₁₂ → Spec(k)` is smooth
> and `U₁` is in addition a local complete intersection over `k`, then
> `Def_X ⟶ Def_{U₂} = Def_{P₂}` is smooth.

```lean
theorem isSmooth_toChartProductOfCover_comp_snd (hU₁₂ : Algebra.Smooth k S.P₁₂)
    (hU₁ : IsLocalCompleteIntersection k S.P₁) :
    IsSmooth (BasedFunctor.comp (toChartProductOfCover S)
      (cofiberedProductSnd (ringDeformationCategoryOver Λ k S.P₁)
        (ringDeformationCategoryOver Λ k S.P₂)))
```

## Tag 0DZP, a lemma

[Tag 0DZP](https://stacks.math.columbia.edu/tag/0DZP) in the Stacks Project.

**`Deformation.Examples.isSmooth_localRingFunctors_and_chain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/CurveIsolatedSingularities.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/CurveIsolatedSingularities.lean#L131).

> Let `X` be a separated scheme of finite type over `k` with `dim X ≤ 1`, and let `p_i` be
> finitely many distinct closed points of `X` outside of which `X → Spec k` is smooth. In the chain
> of deformation categories
> `Def_X ⟶ ∏ Def_{𝒪_{X, p_i}} ⟶ ∏ Def_{𝒪^h_{X, p_i}} ⟶ ∏ Def_{𝒪^∧_{X, p_i}}`
> the first map is smooth, and the second and third maps are smooth and induce isomorphisms
> (bijections of `k`-vector spaces, by Stacks 06IJ) on tangent spaces.

```lean
theorem isSmooth_localRingFunctors_and_chain [IsSeparated X.hom] [LocallyOfFiniteType X.hom]
    [QuasiCompact X.hom] (hdim : topologicalKrullDim (X.left : Type u) ≤ 1) [Finite ι]
    (hinj : Function.Injective p) (hclosed : ∀ i, IsClosed ({p i} : Set X.left))
    (hsm : ∀ x : X.left, x ∉ Set.range p → x ∈ X.hom.smoothLocus) :
    letI : ∀ i, Algebra k (X.left.presheaf.stalk (p i)) := fun i => stalkAlgebraOver X (p i)
    haveI : IsLocallyNoetherian X.left := LocallyOfFiniteType.isLocallyNoetherian X.hom
    IsSmooth (localRingFunctors (Λ := Λ) X p) ∧
      IsSmooth (stalkHenselizationFunctors (Λ := Λ) X p) ∧
      Function.Bijective (differential
        (isCofiberedInGroupoids_pi_ringDeformation (Λ := Λ) (k := k)
          fun i => X.left.presheaf.stalk (p i))
        (isCofiberedInGroupoids_pi_ringDeformation (Λ := Λ) (k := k)
          fun i => (henselization (X.left.presheaf.stalk (p i))
            (IsLocalRing.maximalIdeal (X.left.presheaf.stalk (p i))) : Type u))
        (stalkHenselizationFunctors (Λ := Λ) X p)) ∧
      IsSmooth (stalkCompletionFunctors (Λ := Λ) X p) ∧
      Function.Bijective (differential
        (isCofiberedInGroupoids_pi_ringDeformation (Λ := Λ) (k := k)
          fun i => (henselization (X.left.presheaf.stalk (p i))
            (IsLocalRing.maximalIdeal (X.left.presheaf.stalk (p i))) : Type u))
        (isCofiberedInGroupoids_pi_ringDeformation (Λ := Λ) (k := k)
          fun i => AdicCompletion (IsLocalRing.maximalIdeal (X.left.presheaf.stalk (p i)))
            (X.left.presheaf.stalk (p i)))
        (stalkCompletionFunctors (Λ := Λ) X p))
```

## Tag 0DZQ, a lemma

[Tag 0DZQ](https://stacks.math.columbia.edu/tag/0DZQ) in the Stacks Project.

**`Deformation.Examples.isSmooth_baseProjection_schemeDeformationCategoryProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesUnobstructed.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesUnobstructed.lean#L412). The attribute's comment: “carrying four hypotheses this repository cannot discharge, and no others: h09NZ, the existence of an ample invertible sheaf on a Noetherian separated scheme of dimension at most one (Tag 09NZ), which is what Tag 0A25 carries; hΛ, the Rim–Schlessinger condition for 𝒞\_Λ over itself, which is what Tag 0DZN carries; h0DYZ, Tag 0DYZ in the form Tag 0DZN consumes it, namely the existence of restriction morphisms Def\_\{P\_i} ⟶ Def\_\{P\_12} and of a smooth comparison morphism Def\_X ⟶ Def\_\{P\_1} ×\_\{Def\_\{P\_12}} Def\_\{P\_2} for every gluing situation — this absorbs the identification Def\_\{U\_i} = Def\_\{P\_i} of Tag 0DYX, as Tag 0DZN does; and hsmooth, the affine-local reading of smoothness over a field, which translates smoothness of U\_12 ⟶ Spec k into Algebra.Smooth k Γ(X, U\_12) as Tag 0DZN asks. The three hypotheses (1), (2), (3) of the source are present in full, scheme-level form; the affine-local reading of (2) is proved here from Tag 01UD and is not carried”.

> **[Stacks, Tag 0DZQ].** Let `X` be a scheme over a field `k` which is separated and of finite
> type over `k`, of dimension at most one, a local complete intersection over `k`, and smooth over
> `k` outside a finite set of points. Then the deformation category `Def_X` of Example 0DY7 is
> unobstructed: its structure morphism over `𝒞_Λ` is smooth.
>
> The proof is the source's. The two-chart cover is
> `Deformation.Examples.exists_affineOpen_cover_avoiding_of_topologicalKrullDim_le_one`, applied to
> the complement of the smooth locus; it produces affine opens `U₁`, `U₂` covering `X` with `U₁`
> inside the smooth locus, hence with `U₁` and `U₁₂` smooth over `k`. Tag 0DZN, clause 2, then
> makes `Def_X ⟶ Def_{P₂}` smooth, and Tag 0DZH makes `Def_{P₂} ⟶ 𝒞_Λ` smooth, `P₂ = Γ(X, U₂)`
> being a local complete intersection over `k` by hypothesis (2); the composite is the structure
> morphism of `Def_X` by `Deformation.comp_baseProjection`.
>
> See the module documentation for a full account of the four carried hypotheses.

```lean
theorem isSmooth_baseProjection_schemeDeformationCategoryProjection {Λ k : Type u} [CommRing Λ]
    [Field k] [Algebra Λ k]
    (h09NZ : Stacks.HQuasiProjectiveDimensionOne.AmpleOfNoetherianSeparatedDimLEOne.{u})
    (hΛ : IsDeformationCategory.{u, u, u} (𝟭 (ArtinianLocalAlgCat.{u, u, u} Λ k)))
    (h0DYZ : GluingComparisonSmooth Λ k) (hsmooth : SmoothSectionsOfSmoothAffineOpen.{u} k)
    (X : Over (Spec (CommRingCat.of k))) [IsSeparated X.hom] [LocallyOfFiniteType X.hom]
    [QuasiCompact X.hom] (hdim : topologicalKrullDim (X.left : Type u) ≤ 1)
    (hlci : IsLocalCompleteIntersectionOverField X.hom)
    (hfinite : ((X.hom.smoothLocus : Set X.left)ᶜ).Finite) :
    IsSmooth (baseProjection (schemeDeformationCategoryProjection (Λ := Λ) (k := k) X))
```

**`Deformation.Examples.isSmooth_baseProjection_schemeDeformationCategoryProjection_of_lci`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesUnobstructedUnconditional.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesUnobstructedUnconditional.lean#L92). References: SGA 7 VI (4.10), “(a)”; SGA 7 VI (4.13), “(b), special case”.

> **[Stacks, Tag 0DZQ].** Let `X` be a scheme over a field `k` which is separated and of finite
> type over `k`, of dimension at most one, a local complete intersection over `k`, and smooth over
> `k` outside a finite set of points. Then the deformation category `Def_X` of Example 0DY7 is
> unobstructed: its structure morphism over `𝒞_Λ` is smooth.

```lean
theorem isSmooth_baseProjection_schemeDeformationCategoryProjection_of_lci {Λ k : Type u}
    [CommRing Λ] [Field k] [Algebra Λ k]
    (X : Over (Spec (CommRingCat.of k))) [IsSeparated X.hom] [LocallyOfFiniteType X.hom]
    [QuasiCompact X.hom] (hdim : topologicalKrullDim (X.left : Type u) ≤ 1)
    (hlci : IsLocalCompleteIntersectionOverField X.hom)
    (hfinite : ((X.hom.smoothLocus : Set X.left)ᶜ).Finite) :
    IsSmooth (baseProjection (schemeDeformationCategoryProjection (Λ := Λ) (k := k) X))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 93.16, Tag 0DZG](https://stacks.math.columbia.edu/tag/0DZG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
