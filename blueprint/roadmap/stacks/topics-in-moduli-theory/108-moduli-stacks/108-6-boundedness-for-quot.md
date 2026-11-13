---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProjectiveQuot.isProperAlgebraicSpaceOver_hilbertSubfunctor_quotSituation, AlgebraicGeometry.ProjectiveQuotOverSpace.isProperAlgebraicSpaceOver_hilbertPolynomialQuot_productSpace, AlgebraicGeometry.Space.QuotSituation.isProperAlgebraicSpaceOver_hilbertPolynomialQuot_of_isRelativelyAmple, AlgebraicGeometry.Space.QuotSituation.exists_model_isSeparated_isFinitePresentation_hilbertPolynomialQuot
statement: formalized
proof: formalized
---

# 108.6 Boundedness for Quot

Section 108.6 of the Stacks Project, [Tag 0DP9](https://stacks.math.columbia.edu/tag/0DP9). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DPA, a lemma

[Tag 0DPA](https://stacks.math.columbia.edu/tag/0DPA) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveQuot.isProperAlgebraicSpaceOver_hilbertSubfunctor_quotSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ProjectiveQuot/SiteQuotProper.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ProjectiveQuot/SiteQuotProper.lean#L140).

> Let `n ≥ 0`, `r ≥ 1` and `P ∈ ℚ[t]`.  The algebraic space `Quot^P_{𝒪^{⊕ r}_{ℙⁿ_ℤ}/ℙⁿ_ℤ/ℤ}`
> parametrizing quotients of `𝒪^{⊕ r}_{ℙⁿ_ℤ}` with Hilbert polynomial `P` is proper over `Spec ℤ`:
> the subfunctor of the Quot presheaf (Stacks 09TR) of `𝒪^{⊕ r}/ℙⁿ_ℤ/ℤ` of the quotients which,
> read on `ℙⁿ_T`, have Hilbert polynomial `P` on every fibre is an algebraic space proper over
> `Spec ℤ`.

```lean
theorem isProperAlgebraicSpaceOver_hilbertSubfunctor_quotSituation (hr : 1 ≤ r)
    (P : Polynomial ℚ) :
    (quotSituation B n r).IsProperAlgebraicSpaceOver
      (hilbertSubfunctor (quotSituationFrame B n r) P)
```

## Tag 0DPB, a lemma

[Tag 0DPB](https://stacks.math.columbia.edu/tag/0DPB) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveQuotOverSpace.isProperAlgebraicSpaceOver_hilbertPolynomialQuot_productSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ProjectiveQuotOverSpace/QuotProper.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ProjectiveQuotOverSpace/QuotProper.lean#L45).

> Let `Y` be an algebraic space, `X = Y × ℙⁿ_ℤ`, `𝓛` the pullback of `𝒪_{ℙⁿ}(1)` to `X` and `F`
> an `𝒪_X`-module of finite presentation.  For a numerical polynomial `P : ℤ → ℤ` (the function of a
> rational polynomial `p`), the algebraic space `Quot^P_{F/X/Y}` parametrizing quotients of `F`
> having Hilbert polynomial `P` with respect to `𝓛` is proper over `Y`.

```lean
theorem isProperAlgebraicSpaceOver_hilbertPolynomialQuot_productSpace
    (Y : AlgebraicSpaces B integerBase B.contains_integerBase)
    (F : Space.Modules.{u, u} B integerBase B.contains_integerBase (productSpace n Y).1
      (productSpace n Y).2) (hF : SheafOfModules.IsFinitePresentationOnSite F)
    {P : ℤ → ℤ} {p : Polynomial ℚ} (hP : ∀ m : ℤ, p.eval (m : ℚ) = (P m : ℚ)) :
    (situation n Y F (@SheafOfModules.isQuasicoherentOnSite_of_isFinitePresentationOnSite
        _ _ _ _ F hF)).IsProperAlgebraicSpaceOver
      ((situation n Y F (@SheafOfModules.isQuasicoherentOnSite_of_isFinitePresentationOnSite
          _ _ _ _ F hF)).hilbertPolynomialQuot
        (twistingModule (situationFrame n Y F
          (@SheafOfModules.isQuasicoherentOnSite_of_isFinitePresentationOnSite _ _ _ _ F hF)))
        (hL := isInvertible_twistingModule (situationFrame n Y F
          (@SheafOfModules.isQuasicoherentOnSite_of_isFinitePresentationOnSite _ _ _ _ F hF))) P)
```

## Tag 0DPC, a lemma

[Tag 0DPC](https://stacks.math.columbia.edu/tag/0DPC) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotSituation.isProperAlgebraicSpaceOver_hilbertPolynomialQuot_of_isRelativelyAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotHilbertPolynomialRelativelyAmpleProper.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotHilbertPolynomialRelativelyAmpleProper.lean#L59).

> **Stacks 0DPC.**  Let `f : X ⟶ B` be a proper morphism of finite presentation of algebraic
> spaces (over `Spec ℤ`), `F` a finitely presented `𝒪_X`-module, `L` an invertible `𝒪_X`-module
> ample on `X/B` (Stacks 0D31) and `P` a numerical polynomial.  Then the algebraic space
> `Quot^P_{F/X/B}` parametrizing quotients of `F` having Hilbert polynomial `P` with respect to `L`
> is proper over `B`.

```lean
theorem isProperAlgebraicSpaceOver_hilbertPolynomialQuot_of_isRelativelyAmple
    (D : QuotSituation B integerBase B.contains_integerBase)
    (hf : IsProper B integerBase B.contains_integerBase D.f.hom)
    (hF : SheafOfModules.IsFinitePresentationOnSite D.F)
    (L : Modules.{u, u} B integerBase B.contains_integerBase D.X.1 D.X.2)
    [hL : Stacks.SheafOfModules.IsInvertible (structurePresheaf B integerBase
      B.contains_integerBase D.X.1)
      ((Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B integerBase B.contains_integerBase D.X.1 D.X.2).O)).property L]
    (hamp : IsRelativelyAmple B integerBase B.contains_integerBase D.f L)
    {P : ℤ → ℤ} {p : Polynomial ℚ} (hP : ∀ m : ℤ, p.eval (m : ℚ) = (P m : ℚ)) :
    D.IsProperAlgebraicSpaceOver (D.hilbertPolynomialQuot L P)
```

## Tag 0DPD, a lemma

[Tag 0DPD](https://stacks.math.columbia.edu/tag/0DPD) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotSituation.exists_model_isSeparated_isFinitePresentation_hilbertPolynomialQuot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotHilbertPolynomialSeparatedFinitePresentation.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/QuotHilbertPolynomialSeparatedFinitePresentation.lean#L51).

> Let `F/X/B` be a Quot situation over `Spec ℤ` (Stacks 09TR): `f : X ⟶ B` a morphism of finite
> presentation of algebraic spaces and `F` a quasi-coherent `𝒪_X`-module.  If `f` is separated, `F`
> is of finite presentation, `L` is an invertible `𝒪_X`-module ample on `X/B` (Stacks 0D31) and `P`
> is a numerical polynomial, then `Quot^P_{F/X/B}` (the quotients of `F` having Hilbert polynomial
> `P` with respect to `L`) has a model `M` in the universe of the site, identified with it over `B`,
> which is an algebraic space whose morphism to `B` is separated and of finite presentation.

```lean
theorem exists_model_isSeparated_isFinitePresentation_hilbertPolynomialQuot
    (D : QuotSituation B integerBase B.contains_integerBase)
    (hsep : IsSeparated B integerBase B.contains_integerBase D.f.hom)
    (hF : SheafOfModules.IsFinitePresentationOnSite D.F)
    (L : Modules.{u, u} B integerBase B.contains_integerBase D.X.1 D.X.2)
    [hL : Stacks.SheafOfModules.IsInvertible
      (structurePresheaf B integerBase B.contains_integerBase D.X.1)
      ((Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B integerBase B.contains_integerBase D.X.1 D.X.2).O)).property L]
    (hamp : IsRelativelyAmple B integerBase B.contains_integerBase D.f L)
    {P : ℤ → ℤ} {p : Polynomial ℚ} (hP : ∀ m : ℤ, p.eval (m : ℚ) = (P m : ℚ)) :
    ∃ M : D.SubfunctorModel (D.hilbertPolynomialQuot L P),
      IsAlgebraicSpace B integerBase B.contains_integerBase M.presheaf ∧
        IsSeparated B integerBase B.contains_integerBase M.toBase ∧
        IsFinitePresentation B integerBase B.contains_integerBase M.toBase
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 108.6, Tag 0DP9](https://stacks.math.columbia.edu/tag/0DP9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
