---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_adicCompletion_ringEquiv_henselianLocalRing_completionSpace, AlgebraicGeometry.Space.isRegularLocalRing_henselianLocalRing_of_completion, AlgebraicGeometry.Space.isRegularLocalRing_henselianLocalRing_completion_iff, AlgebraicGeometry.Space.hasEtaleLocalProperty_isRegular_completionSpace_iff_of_isProper, AlgebraicGeometry.Space.isFinite_normalization_of_isAnalyticallyUnramified
statement: formalized
proof: formalized
---

# 89.6 Base change to the completion

Section 89.6 of the Stacks Project, [Tag 0BHN](https://stacks.math.columbia.edu/tag/0BHN). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BHP, a lemma

[Tag 0BHP](https://stacks.math.columbia.edu/tag/0BHP) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_adicCompletion_ringEquiv_henselianLocalRing_completionSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/HenselianCompletionBaseChange.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/HenselianCompletionBaseChange.lean#L210).

> Let `(A, 𝔪)` be a local ring with finitely generated maximal ideal, let `X` be a decent
> algebraic space over `Spec A` and let `Y = X ×_{Spec A} Spec A^` be its base change to the
> `𝔪`-adic completion of `A`. For a point `q` of `Y` whose image `p` in `X` lies over the closed
> point of `Spec A`, the canonical local homomorphism `𝒪^h_{X,p} ⟶ 𝒪^h_{Y,q}` — the one compatible
> with the local rings of a pair of corresponding elementary étale neighborhoods — induces an
> isomorphism on `𝔪`-adic completions.

```lean
theorem exists_adicCompletion_ringEquiv_henselianLocalRing_completionSpace
    (hfg : (IsLocalRing.maximalIdeal A).FG)
    (hX : IsAlgebraicSpace B (Spec (.of A)) hA X)
    (hXdec : IsDecentSpace B (Spec (.of A)) hA X)
    (q : points B (Spec (.of A)) hA (completionSpace A B hA hAc f))
    (p : points B (Spec (.of A)) hA X)
    (hp : pointsMap B (Spec (.of A)) hA (completionSpace A B hA hAc f)
      (completionProjection A B hA hAc f) q = p)
    (hclosed : pointsToScheme B (Spec (.of A)) hA (Over.mk (𝟙 (B.obj hA)))
        (pointsMap B (Spec (.of A)) hA X f p) =
      (⟨IsLocalRing.maximalIdeal A, inferInstance⟩ : PrimeSpectrum A)) :
    letI hY := isAlgebraicSpace_completionSpace A B hA hAc f hX
    letI hYdec := isDecentSpace_completionSpace A B hA hAc f hX hXdec
    letI := isLocalRing_henselianLocalRing B (Spec (.of A)) hA hX hXdec p
    letI := isLocalRing_henselianLocalRing B (Spec (.of A)) hA hY hYdec q
    ∃ φ : (henselianLocalRing B (Spec (.of A)) hA X hX p hXdec : Type (u + 1)) →+*
        (henselianLocalRing B (Spec (.of A)) hA (completionSpace A B hA hAc f) hY q hYdec :
          Type (u + 1)),
      IsLocalHom φ ∧
      (∃ (E : ElementaryEtaleNeighborhood B (Spec (.of A)) hA X hX p)
          (N : ElementaryEtaleNeighborhood B (Spec (.of A)) hA
            (completionSpace A B hA hAc f) hY q)
          (j : N.scheme ⟶ E.scheme) (hj : j.left.1 N.point = E.point),
        yoneda.map j ≫ E.toSpace = N.toSpace ≫ completionProjection A B hA hAc f ∧
          φ.comp (stalkToHenselianLocalRing B (Spec (.of A)) hA X hX p hXdec E) =
            (stalkToHenselianLocalRing B (Spec (.of A)) hA (completionSpace A B hA hAc f) hY q
                hYdec N).comp
              ((E.scheme.left.1.presheaf.stalkCongr (Inseparable.of_eq hj.symm)).hom ≫
                j.left.1.stalkMap N.point).hom) ∧
      ∃ e : AdicCompletion (IsLocalRing.maximalIdeal
            (henselianLocalRing B (Spec (.of A)) hA X hX p hXdec : Type (u + 1)))
            (henselianLocalRing B (Spec (.of A)) hA X hX p hXdec : Type (u + 1)) ≃+*
          AdicCompletion (IsLocalRing.maximalIdeal
            (henselianLocalRing B (Spec (.of A)) hA (completionSpace A B hA hAc f) hY q hYdec :
              Type (u + 1)))
            (henselianLocalRing B (Spec (.of A)) hA (completionSpace A B hA hAc f) hY q hYdec :
              Type (u + 1)),
        e.toRingHom.comp (algebraMap _ _) = (algebraMap _ _).comp φ
```

## Tag 0BHQ, a lemma

[Tag 0BHQ](https://stacks.math.columbia.edu/tag/0BHQ) in the Stacks Project.

**`AlgebraicGeometry.Space.isRegularLocalRing_henselianLocalRing_of_completion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularCompletionBaseChange.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RegularCompletionBaseChange.lean#L97). The attribute's comment: “part (1)”.

> **Stacks 0BHQ, part (1).** Let `(A, 𝔪)` be a Noetherian local ring, let `X` be a decent
> algebraic space locally of finite type over `Spec A` and let `Y = X ×_{Spec A} Spec A^` be its
> base change to the `𝔪`-adic completion. If the henselian local ring of `Y` at a point `y` is
> regular, then so is the henselian local ring of `X` at the image of `y`.

```lean
theorem isRegularLocalRing_henselianLocalRing_of_completion
    (hX : IsAlgebraicSpace B (Spec (.of A)) hA X)
    (hXdec : IsDecentSpace B (Spec (.of A)) hA X)
    (hf : IsLocallyOfFiniteType B (Spec (.of A)) hA f)
    (y : points B (Spec (.of A)) hA (completionSpace A B hA hAc f))
    (hy : IsRegularLocalRing
      (henselianLocalRing B (Spec (.of A)) hA (completionSpace A B hA hAc f)
        (isAlgebraicSpace_completionSpace A B hA hAc f hX) y
        (isDecentSpace_completionSpace A B hA hAc f hX hXdec) : Type (u + 1))) :
    IsRegularLocalRing
      (henselianLocalRing B (Spec (.of A)) hA X hX
        (pointsMap B (Spec (.of A)) hA (completionSpace A B hA hAc f)
          (completionProjection A B hA hAc f) y) hXdec : Type (u + 1))
```

**`AlgebraicGeometry.Space.isRegularLocalRing_henselianLocalRing_completion_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularCompletionClosedFibre.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RegularCompletionClosedFibre.lean#L151). The attribute's comment: “part (2)”.

> Let `(A, 𝔪)` be a Noetherian local ring, let `X` be a decent algebraic space locally of finite
> type over `Spec A` and let `Y = X ×_{Spec A} Spec A^` be its base change to the `𝔪`-adic
> completion. At a point `y` of `Y` lying over the closed point of `Spec A^`, the henselian local
> ring of `Y` at `y` is regular if and only if the henselian local ring of `X` at the image of `y`
> is regular.

```lean
theorem isRegularLocalRing_henselianLocalRing_completion_iff
    (hX : IsAlgebraicSpace B (Spec (.of A)) hA X)
    (hXdec : IsDecentSpace B (Spec (.of A)) hA X)
    (hf : IsLocallyOfFiniteType B (Spec (.of A)) hA f)
    (y : points B (Spec (.of A)) hA (completionSpace A B hA hAc f))
    (hy : pointsToScheme B (Spec (.of A)) hA (completionBase A B hA hAc)
        (pointsMap B (Spec (.of A)) hA (completionSpace A B hA hAc f)
          (pullback.snd f (completionBaseMap A B hA hAc)) y) =
      (⟨IsLocalRing.maximalIdeal (AdicCompletion (IsLocalRing.maximalIdeal A) A),
        inferInstance⟩ :
        PrimeSpectrum (AdicCompletion (IsLocalRing.maximalIdeal A) A))) :
    IsRegularLocalRing
        (henselianLocalRing B (Spec (.of A)) hA (completionSpace A B hA hAc f)
          (isAlgebraicSpace_completionSpace A B hA hAc f hX) y
          (isDecentSpace_completionSpace A B hA hAc f hX hXdec) : Type (u + 1)) ↔
      IsRegularLocalRing
        (henselianLocalRing B (Spec (.of A)) hA X hX
          (pointsMap B (Spec (.of A)) hA (completionSpace A B hA hAc f)
            (completionProjection A B hA hAc f) y) hXdec : Type (u + 1))
```

**`AlgebraicGeometry.Space.hasEtaleLocalProperty_isRegular_completionSpace_iff_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularCompletionProper.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RegularCompletionProper.lean#L220). The attribute's comment: “part (3)”.

> **Stacks 0BHQ, part (3).** Let `(A, 𝔪)` be a Noetherian local ring and let `X` be a decent
> algebraic space proper over `Spec A`. Then `X` is regular if and only if its base change
> `Y = X ×_{Spec A} Spec A^` to the `𝔪`-adic completion of `A` is regular.

```lean
theorem hasEtaleLocalProperty_isRegular_completionSpace_iff_of_isProper
    (hX : IsAlgebraicSpace B (Spec (.of A)) hA X)
    (hXdec : IsDecentSpace B (Spec (.of A)) hA X)
    (hproper : IsProper B (Spec (.of A)) hA f) :
    HasEtaleLocalProperty B (Spec (.of A)) hA X (fun T : Scheme.{u} ↦ IsRegular T) ↔
      HasEtaleLocalProperty B (Spec (.of A)) hA (completionSpace A B hA hAc f)
        (fun T : Scheme.{u} ↦ IsRegular T)
```

## Tag 0BHR, a lemma

[Tag 0BHR](https://stacks.math.columbia.edu/tag/0BHR) in the Stacks Project.

**`AlgebraicGeometry.Space.isFinite_normalization_of_isAnalyticallyUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationSpaceConstruction.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationSpaceConstruction.lean#L322). References: SGA 3 XXV (4.2), “more general”.

> **Stacks 0BHR.** Let `(A, 𝔪)` be an analytically unramified Noetherian local ring and let
> `F` be an algebraic space over `S` whose structure morphism goes to an object of the site with
> underlying scheme `Spec A`. If `F` is locally of finite type over `A` and its structure
> morphism is étale at every point of codimension zero, then **the** normalization morphism
> `F^ν ⟶ F` of `F` is a finite morphism of algebraic spaces.
>
> The normalization is the constructed one, neither assumed nor existentially quantified: `F` is
> locally of finite type over a Noetherian ring, so its étale scheme charts are locally
> Noetherian and satisfy the finiteness condition of Tag 0BB1, and
> `AlgebraicGeometry.Space.normalizationData` is then the normalization of `F`, unique up to a
> unique isomorphism over `F` by
> `AlgebraicGeometry.Space.NormalizationData.existsUnique_iso_hom`. Finiteness of its
> normalization morphism is
> `AlgebraicGeometry.Space.NormalizationData.isFinite_hom_of_isAnalyticallyUnramified`, which is
> Stacks 0BG8 on a surjective étale chart followed by the étale-local characterisation of
> finiteness, condition (3) of Stacks 03ZQ.
>
> The base is a representable presheaf with an isomorphism of its underlying scheme onto
> `Spec A`, which is the source's hypothesis with no identification of schemes imposed and with
> the base scheme `S` of the site left arbitrary.

```lean
theorem isFinite_normalization_of_isAnalyticallyUnramified {A : Type u} [CommRing A]
    [IsNoetherianRing A] [IsLocalRing A] (hA : IsAnalyticallyUnramified A)
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F)
    {Z : BigFppfOver B S hS} (f : F ⟶ yoneda.obj Z)
    (a : (BigFppfOver.toScheme B S hS).obj Z ⟶ Spec (.of A)) [IsIso a]
    (hft : IsLocallyOfFiniteType B S hS f)
    (het : ∀ x : points B S hS F, localRingDimension B S hS x = 0 → IsEtaleAt B S hS f x) :
    IsFinite B S hS (normalizationData B S hS hF
      (hasLocallyFiniteIrreducibleComponents_of_isLocallyOfFiniteType B S hS f a hft)).hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 89.6, Tag 0BHN](https://stacks.math.columbia.edu/tag/0BHN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
