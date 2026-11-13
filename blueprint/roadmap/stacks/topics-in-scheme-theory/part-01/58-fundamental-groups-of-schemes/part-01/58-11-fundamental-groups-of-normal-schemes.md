---
declaration: section
origin: cited
lean: AlgebraicGeometry.unramified_normalization_iff_etale, AlgebraicGeometry.etale_normalization_iff_finite_etale, AlgebraicGeometry.isNormal_of_etale, AlgebraicGeometry.isIntegral_of_finite_etale_connected, AlgebraicGeometry.normalizationDesc_isIso_of_finite_etale_connected, AlgebraicGeometry.isQuotientMap_absoluteGaloisToFundamentalGroup, AlgebraicGeometry.surjective_galoisToFundamentalGroup, AlgebraicGeometry.isExactSequence_etaleFundamentalGroupMap_fractionField_of_isHenselization
statement: formalized
proof: formalized
---

# 58.11 Fundamental groups of normal schemes

Section 58.11 of the Stacks Project, [Tag 0BQJ](https://stacks.math.columbia.edu/tag/0BQJ). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BQK, a lemma

[Tag 0BQK](https://stacks.math.columbia.edu/tag/0BQK) in the Stacks Project.

**`AlgebraicGeometry.unramified_normalization_iff_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/EtaleNormalization.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/EtaleNormalization.lean#L58). The attribute's comment: “unramified iff étale”. References: SGA 1 I (9.11), “special case”.

> The morphism from the relative normalization of a normal integral scheme in a dominant
> morphism of integral schemes is unramified exactly when it is étale: the normalization is
> irreducible and dominates the normal, hence geometrically unibranch, target.

```lean
theorem unramified_normalization_iff_etale
    {Y X : Scheme.{u}} (f : Y ⟶ X) [IsIntegral Y] [IsIntegral X] [IsNormal X]
    [QuasiCompact f] [QuasiSeparated f] [IsDominant f] :
    Unramified f.fromNormalization ↔ Etale f.fromNormalization
```

**`AlgebraicGeometry.etale_normalization_iff_finite_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/EtaleNormalization.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/EtaleNormalization.lean#L81). The attribute's comment: “étale iff finite étale”.

> The morphism from a relative normalization is étale exactly when it is finite étale: it is
> always integral, and an étale morphism is locally of finite type.

```lean
theorem etale_normalization_iff_finite_etale
    {Y X : Scheme.{u}} (f : Y ⟶ X) [QuasiCompact f] [QuasiSeparated f] :
    Etale f.fromNormalization ↔ (IsFinite f.fromNormalization ∧ Etale f.fromNormalization)
```

## Tag 0BQL, a lemma

[Tag 0BQL](https://stacks.math.columbia.edu/tag/0BQL) in the Stacks Project.

**`AlgebraicGeometry.isNormal_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Normal.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Normal.lean#L187). The attribute's comment: “normality”.

> The source of an étale morphism with normal target is normal, an étale morphism being
> smooth.

```lean
theorem isNormal_of_etale {X Y : Scheme.{u}} (f : X ⟶ Y) [Etale f] [IsNormal Y] :
    IsNormal X
```

**`AlgebraicGeometry.isIntegral_of_finite_etale_connected`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/FiniteEtaleCover.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/FiniteEtaleCover.lean#L116). The attribute's comment: “integrality”. References: SGA 1 I (10.1), “integrality, finite case”.

> A connected finite étale cover of a normal integral scheme is integral.

```lean
theorem isIntegral_of_finite_etale_connected {X Y : Scheme.{u}} (f : Y ⟶ X)
    [IsIntegral X] [IsNormal X] [IsFinite f] [Etale f]
    [ConnectedSpace Y] : IsIntegral Y
```

**`AlgebraicGeometry.normalizationDesc_isIso_of_finite_etale_connected`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/FiniteEtaleCover.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/FiniteEtaleCover.lean#L254). The attribute's comment: “normalization in the function field”. References: SGA 1 I (10.1), “finite étale case”; SGA 1 I (10.2), “finite => normalization”.

> A connected finite étale cover of a normal integral scheme is canonically the
> normalization of the base in the function field of the cover.

```lean
theorem normalizationDesc_isIso_of_finite_etale_connected
    {X Y : Scheme.{u}} (f : Y ⟶ X)
    [IsIntegral X] [IsNormal X] [IsFinite f] [Etale f]
    [ConnectedSpace Y] :
    let : IsIntegral Y := isIntegral_of_finite_etale_connected f
    IsIso ((Y.fromSpecStalk (genericPoint Y) ≫ f).normalizationDesc
      (Y.fromSpecStalk (genericPoint Y)) f rfl)
```

## Tag 0BQM, a proposition

[Tag 0BQM](https://stacks.math.columbia.edu/tag/0BQM) in the Stacks Project.

**`AlgebraicGeometry.isQuotientMap_absoluteGaloisToFundamentalGroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalFunctionField/QuotientMap.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalFunctionField/QuotientMap.lean#L295). The attribute's comment: “π₁(X, η̄) = Gal(M/K), with the canonical generic-point homomorphism identified with the quotient map onto Gal(M/K)”. References: SGA 1 V (8.2), “special case”; SGA 7 XIX (1.4), “π1(ℓ−S”.

> **Stacks Project, Tag 0BQM.** Let `X` be a normal integral scheme with function field
> `K = κ(η)` and let `η̄` be an algebraic geometric point over the generic point, with
> algebraically closed residue field `Ω = κ(η̄)`. Let `M ⊆ Ω` be the union of the finite
> subextensions of `K` in which `X` is unramified, that is `AlgebraicGeometry.maximalEtaleExtension`.
> Then `M` has that defining property and is the largest subextension with it, `M/K` is Galois —
> in particular `M` is separable over `K`, so it lies in a separable closure `K^sep` of `K` inside
> `Ω` — and the canonical homomorphism `Gal(Ω/K) → π₁(X, η̄)` is identified with the quotient map
> `Gal(Ω/K) → Gal(M/K)`: there is an isomorphism of topological groups
> `π₁(X, η̄) ≃ Gal(M/K)` carrying the canonical homomorphism to restriction of automorphisms
> to `M`.
>
> No Noetherian hypothesis is needed; this is the difference between the present tag and Stacks
> Tag 03VG, which the library also proves without the Noetherian hypothesis, for an algebraic
> geometric point over the generic point as that tag requires
> (`AlgebraicGeometry.fundamentalGroupIsoGalMaximalEtaleExtension`).

```lean
public theorem isQuotientMap_absoluteGaloisToFundamentalGroup
    [IsIntegral X] [IsNormal X]
    (hs : GeometricPoint.IsAlgebraic sbar)
    (hgeneric : sbar.hom default = genericPoint X) :
    letI : Normal (X.residueField (sbar.hom default)) (maximalEtaleExtension X sbar) :=
      normal_maximalEtaleExtension X sbar hs
    (∀ L : IntermediateField (X.residueField (sbar.hom default)) sbar.residueField,
        FiniteDimensional (X.residueField (sbar.hom default)) L →
          L ≤ maximalEtaleExtension X sbar → FiniteEtaleNormalization X sbar L) ∧
      (∀ N : IntermediateField (X.residueField (sbar.hom default)) sbar.residueField,
        (∀ L : IntermediateField (X.residueField (sbar.hom default)) sbar.residueField,
            L ≤ N → FiniteDimensional (X.residueField (sbar.hom default)) L →
              FiniteEtaleNormalization X sbar L) →
          N ≤ maximalEtaleExtension X sbar) ∧
      Normal (X.residueField (sbar.hom default)) (maximalEtaleExtension X sbar) ∧
      Algebra.IsSeparable (X.residueField (sbar.hom default)) (maximalEtaleExtension X sbar) ∧
      ∃ e : AlgebraicGeometry.EtaleFundamentalGroup X sbar ≃ₜ*
          Gal(maximalEtaleExtension X sbar / X.residueField (sbar.hom default)),
        ∀ σ : Gal(sbar.residueField / X.residueField (sbar.hom default)),
          e (absoluteGaloisToFundamentalGroup X sbar σ) =
            AlgEquiv.restrictNormalHom (maximalEtaleExtension X sbar) σ
```

**`AlgebraicGeometry.surjective_galoisToFundamentalGroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalGenericPointSurjective.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalGenericPointSurjective.lean#L209). The attribute's comment: “surjectivity of the generic-point map”. References: SGA 1 V (8.2), “surjectivity”.

> **Stacks 0BQM, surjectivity.** For a normal integral scheme `X` with function field
> `K = κ(η)` at its generic point `η`, a separable closure `L` of `K` and an algebraically closed
> algebraic extension `Ω` of `K` containing `L`, the canonical continuous homomorphism
>
> ```
> Gal(L / K) → π₁(X, η̄)
> ```
>
> is surjective. Equivalently, every connected finite étale cover of `X` stays connected over the
> function field.

```lean
theorem surjective_galoisToFundamentalGroup
    (X : Scheme.{u}) [IsIntegral X] [IsNormal X]
    (L Ω : Type u) [Field L] [Field Ω]
    [Algebra (X.residueField (genericPoint X)) L]
    [IsSepClosure (X.residueField (genericPoint X)) L]
    [Algebra L Ω] [Algebra (X.residueField (genericPoint X)) Ω]
    [IsScalarTower (X.residueField (genericPoint X)) L Ω]
    [IsAlgClosed Ω] [Algebra.IsAlgebraic (X.residueField (genericPoint X)) Ω] :
    Function.Surjective (galoisToFundamentalGroup X L Ω)
```

## Tag 0BSM, a lemma

[Tag 0BSM](https://stacks.math.columbia.edu/tag/0BSM) in the Stacks Project.

**`AlgebraicGeometry.isExactSequence_etaleFundamentalGroupMap_fractionField_of_isHenselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalLocalExactSequence.lean, line 730](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/NormalLocalExactSequence.lean#L730).

> **The local exact sequence for a normal local ring.** Let
> `A` be a normal local domain with fraction field `K`, let `A^sh` be a strict henselization of `A`
> and `K^sh` its fraction field, and let `x` be a geometric point of `Spec K^sh`. Then
>
> ```
> π₁(Spec K^sh, x) → π₁(Spec K, x) → π₁(Spec A, x) → 1
> ```
>
> is exact.
>
> The criterion of Stacks 0BS9 reduces this to two statements. Base change to the generic point is
> fully faithful because a connected finite étale cover of `Spec A` with a section over `K` has a
> section over `A`. A cover of `Spec K` comes from `Spec A` exactly when it becomes a finite
> coproduct of copies of the base over `Spec K^sh`: one direction is that a cover pulled back from
> `Spec A` is already split over the strictly henselian `Spec A^sh`, and the other is that the
> integral closure of `A` in such a cover is finite étale over `A` — which it is because it is so
> after the faithfully flat base change to `A^sh` — and has the cover as its generic fibre.
>
> The four spectra are spectra of local rings, hence connected, so the Galois-category property
> of Stacks Tag 0BNB applies at each of their geometric points.

```lean
theorem isExactSequence_etaleFundamentalGroupMap_fractionField_of_isHenselization
    [IsIntegrallyClosed A] [IsSepClosure (ResidueField A) κsep] [IsHenselization A κsep Ash]
    (x : GeometricPoint (Spec (.of Ksh))) :
    IsExactSequence
      (etaleFundamentalGroupMap (Spec.map (CommRingCat.ofHom (algebraMap K Ksh))) x)
      (etaleFundamentalGroupMap (Spec.map (CommRingCat.ofHom (algebraMap A K)))
        (x.map (Spec.map (CommRingCat.ofHom (algebraMap K Ksh)))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.11, Tag 0BQJ](https://stacks.math.columbia.edu/tag/0BQJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
