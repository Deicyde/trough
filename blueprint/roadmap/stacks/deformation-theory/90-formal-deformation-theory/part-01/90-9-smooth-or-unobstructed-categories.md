---
declaration: section
origin: cited
lean: Deformation.IsSmooth, Deformation.smooth_formallySmooth_flat_specialFibre_tfae, Deformation.smooth_formallySmooth_flat_specialFibre_powerSeries_tfae, Deformation.isSmooth_baseProjection_iff_formallySmoothNAdic, Deformation.isSmooth_baseProjection_iff_powerSeries, Deformation.smoothModel, Deformation.smoothModel_formallySmooth, Deformation.smoothModel_h1Cotangent_bijective
statement: formalized
proof: formalized
---

# 90.9 Smooth or unobstructed categories

Section 90.9 of the Stacks Project, [Tag 0DYK](https://stacks.math.columbia.edu/tag/0DYK). 4 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06HP, a definition

[Tag 06HP](https://stacks.math.columbia.edu/tag/06HP) in the Stacks Project.

**`Deformation.IsSmooth`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/Basic.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Smooth/Basic.lean#L102). The attribute's comment: “smoothness of the structure morphism, i.e. an unobstructed cofibered category”. References: SGA 7 VI (2.1), “smooth”.

> A morphism of categories over `\mathcal C_\Lambda` is smooth if every
> lifting problem over a surjective map `B \to A` has a compatible solution over
> `B`.

```lean
public abbrev IsSmooth {𝓕 : BasedCategory.{v₁, u₁} (ArtinianLocalAlgCat.{u, v, w} Λ
  k)} {𝓖 : BasedCategory.{v₂, u₂} (ArtinianLocalAlgCat.{u, v, w} Λ k)} (φ : BasedFunctor 𝓕 𝓖) : Prop
```

## Tag 0DYL, a lemma

[Tag 0DYL](https://stacks.math.columbia.edu/tag/0DYL) in the Stacks Project.

**`Deformation.smooth_formallySmooth_flat_specialFibre_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/CompleteLocalAlgebra/LiftingCriterion.lean, line 662](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Smooth/CompleteLocalAlgebra/LiftingCriterion.lean#L662). The attribute's comment: “conditions (1)--(4)”. References: EGA 0 (19.7.1), “complete local case”; EGA 0 (19.6.5), “complete, K=k: (2)⇔(3)”; SGA 7 VI (1.14), “Prorepresentable case”.

> **Stacks 0DYL.** Smoothness of the restricted representable category of `R`, formal
> smoothness of `Λ → R` in the `m_R`-adic topology, and the two conditions combining flatness
> with regularity of the special fibre over `k' = Λ / ker(Λ → k)`, are equivalent.

```lean
public theorem smooth_formallySmooth_flat_specialFibre_tfae
    (R : CompleteLocalAlgCat.{u, v, w} Λ k) :
    let k' := Λ ⧸ RingHom.ker (algebraMap Λ k)
    letI : (RingHom.ker (algebraMap Λ k)).IsMaximal :=
      Algebra.ker_algebraMap_isMaximal_of_isIntegral Λ k
    letI : Field k' := Ideal.Quotient.field _
    let Bbar := R ⊗[Λ] k'
    letI : Algebra k' Bbar := Algebra.TensorProduct.rightAlgebra
    List.TFAE [
      IsSmooth (restrictedCoyonedaProjection R),
      RingHom.FormallySmoothNAdic.{max u v} (algebraMap Λ R) (maximalIdeal R),
      Module.Flat Λ R ∧ Algebra.IsGeometricallyRegular k' Bbar,
      Module.Flat Λ R ∧
        RingHom.FormallySmoothNAdic.{max u v} (algebraMap k' Bbar)
          ((maximalIdeal R).map Algebra.TensorProduct.includeLeftRingHom)]
```

**`Deformation.smooth_formallySmooth_flat_specialFibre_powerSeries_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/CompleteLocalAlgebra/PowerSeriesCase.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Smooth/CompleteLocalAlgebra/PowerSeriesCase.lean#L182). The attribute's comment: “condition (5), classical case”. References: EGA 0 (19.7.1), “classical case”; EGA 0 (19.6.5), “complete, K=k: (2)⇔(5)”.

> **Stacks 0DYL.** If the base is classical, the four smoothness conditions are also
> equivalent to `R` being a formal power series algebra in finitely many variables over `Λ`.

```lean
public theorem smooth_formallySmooth_flat_specialFibre_powerSeries_tfae
    (R : CompleteLocalAlgCat.{u, v, w} Λ k) (hΛ : IsClassical Λ k) :
    let k' := Λ ⧸ RingHom.ker (algebraMap Λ k)
    letI : (RingHom.ker (algebraMap Λ k)).IsMaximal :=
      Algebra.ker_algebraMap_isMaximal_of_isIntegral Λ k
    letI : Field k' := Ideal.Quotient.field _
    let Bbar := R ⊗[Λ] k'
    letI : Algebra k' Bbar := Algebra.TensorProduct.rightAlgebra
    List.TFAE [
      IsSmooth (restrictedCoyonedaProjection R),
      RingHom.FormallySmoothNAdic.{max u v} (algebraMap Λ R) (maximalIdeal R),
      Module.Flat Λ R ∧ Algebra.IsGeometricallyRegular k' Bbar,
      Module.Flat Λ R ∧
        RingHom.FormallySmoothNAdic.{max u v} (algebraMap k' Bbar)
          ((maximalIdeal R).map Algebra.TensorProduct.includeLeftRingHom),
      ∃ n : ℕ, Nonempty (R ≃ₐ[Λ] MvPowerSeries (Fin n) Λ)]
```

## Tag 0DZK, a lemma

[Tag 0DZK](https://stacks.math.columbia.edu/tag/0DZK) in the Stacks Project.

**`Deformation.isSmooth_baseProjection_iff_formallySmoothNAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/Unobstructed.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Smooth/Unobstructed.lean#L196). The attribute's comment: “conditions (1) and (2)”. References: SGA 7 VI (2.4), “P smooth <=> R f.smooth”.

> **Stacks 0DZK.** A predeformation category with a versal formal object over `R` is
> unobstructed if and only if `Λ → R` is formally smooth in the `m_R`-adic topology.

```lean
public theorem isSmooth_baseProjection_iff_formallySmoothNAdic
    [IsNoetherianRing Λ] [Module.Finite Λ k]
    (hp : IsPredeformationCategory p)
    (ξ : FormalObject p) (hξ : IsVersal hp.cofibered ξ) :
    IsSmooth (baseProjection p) ↔
      RingHom.FormallySmoothNAdic.{max u (max v w)}
        (algebraMap Λ ξ.base) (maximalIdeal ξ.base)
```

**`Deformation.isSmooth_baseProjection_iff_powerSeries`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/Unobstructed.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Smooth/Unobstructed.lean#L221). The attribute's comment: “condition (3), classical case”. References: SGA 7 VI (2.4), “P smooth <=> R=Λ[[x]]”; SGA 7 VI (1.14), “more general”.

> **Stacks 0DZK.** In the classical case, a predeformation category with a versal formal
> object over `R` is unobstructed if and only if `R` is a formal power series algebra in
> finitely many variables over `Λ`.

```lean
public theorem isSmooth_baseProjection_iff_powerSeries
    [IsNoetherianRing Λ] [Module.Finite Λ k]
    (hp : IsPredeformationCategory p)
    (ξ : FormalObject p) (hξ : IsVersal hp.cofibered ξ)
    (hΛ : IsClassical Λ k) :
    IsSmooth (baseProjection p) ↔
      ∃ n : ℕ, Nonempty (ξ.base ≃ₐ[Λ] MvPowerSeries (Fin n) Λ)
```

## Tag 06SM, a lemma

[Tag 06SM](https://stacks.math.columbia.edu/tag/06SM) in the Stacks Project.

**`Deformation.smoothModel`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Completed/SmoothModel.lean, line 943](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Completed/SmoothModel.lean#L943). The attribute's comment: “the object”.

> A complete local algebra realizing the smooth deformation base.

```lean
public noncomputable def smoothModel : CompleteLocalAlgCat.{u, max u w, w} Λ k
```

**`Deformation.smoothModel_formallySmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Completed/SmoothModel.lean, line 956](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Completed/SmoothModel.lean#L956). The attribute's comment: “smoothness”.

> The chosen complete local algebra is formally smooth over `Λ` for the maximal-ideal-adic
> topology.

```lean
public theorem smoothModel_formallySmooth :
    RingHom.FormallySmoothNAdic.{max u w}
      (algebraMap Λ (smoothModel (Λ := Λ) (k := k)))
      (maximalIdeal (smoothModel (Λ := Λ) (k := k)))
```

**`Deformation.smoothModel_h1Cotangent_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Completed/SmoothModel.lean, line 967](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Completed/SmoothModel.lean#L967). The attribute's comment: “first cotangent homology”.

> For the chosen complete local algebra `R`, the canonical map
> `H₁(L_{k/Λ}) → H₁(L_{k/R})` is bijective. Since `R → k` is surjective the target is
> canonically the conormal module `𝔪_R/𝔪_R²`, so this is the conormal description of
> `H₁(L_{k/Λ})`.

```lean
public theorem smoothModel_h1Cotangent_bijective :
    let R := smoothModel (Λ := Λ) (k := k)
    letI : Algebra R k := (smoothModelResidue (Λ := Λ) (k := k)).toRingHom.toAlgebra
    letI : IsScalarTower Λ R k :=
      IsScalarTower.of_algebraMap_eq'
        (smoothModelResidue (Λ := Λ) (k := k)).comp_algebraMap.symm
    Function.Bijective (Algebra.H1Cotangent.map Λ R k k)
```

**`Deformation.smoothModel_mapBaseChange_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Completed/SmoothModel.lean, line 980](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Completed/SmoothModel.lean#L980). The attribute's comment: “differentials”.

> For the chosen complete local algebra `R`, the canonical base-change map
> `k ⊗_R Ω[R⁄Λ] → Ω[k⁄Λ]` is bijective.

```lean
public theorem smoothModel_mapBaseChange_bijective :
    let R := smoothModel (Λ := Λ) (k := k)
    letI : Algebra R k := (smoothModelResidue (Λ := Λ) (k := k)).toRingHom.toAlgebra
    letI : IsScalarTower Λ R k :=
      IsScalarTower.of_algebraMap_eq'
        (smoothModelResidue (Λ := Λ) (k := k)).comp_algebraMap.symm
    Function.Bijective (KaehlerDifferential.mapBaseChange Λ R k)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.9, Tag 0DYK](https://stacks.math.columbia.edu/tag/0DYK)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
