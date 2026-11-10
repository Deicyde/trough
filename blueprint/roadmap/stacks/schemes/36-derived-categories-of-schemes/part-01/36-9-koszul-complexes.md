---
declaration: section
origin: cited
lean: Koszul.koszulIdealComplexSystem, Koszul.CechSituation, Koszul.alternatingCechComplexIso, Koszul.alternatingCechComplexIso_naturality, Koszul.alternatingCechComplexIso_ι_apply, Koszul.koszulHomColimitIsoAlternatingCechTotal, Koszul.CechSituation.isIso_linearAlternatingCechToDerivedComparison, Koszul.CechSituation.alternatingCechTotalNatIsoDerivedSections
statement: formalized
proof: formalized
---

# 36.9 Koszul complexes

Section 36.9 of the Stacks Project, [Tag 08CX](https://stacks.math.columbia.edu/tag/08CX). 8 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08CY, an equation

[Tag 08CY](https://stacks.math.columbia.edu/tag/08CY) in the Stacks Project.

**`Koszul.koszulIdealComplexSystem`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/Koszul.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/Koszul.lean#L91).

> The canonical inverse system `I^•(f) ← I^•(f²) ← I^•(f³) ← ⋯`.

```lean
noncomputable def koszulIdealComplexSystem {r : ℕ} (f : Fin r → A) :
    KoszulIdealComplexSystem f
```

## Tag 08CZ, a situation

[Tag 08CZ](https://stacks.math.columbia.edu/tag/08CZ) in the Stacks Project.

**`Koszul.CechSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Koszul/Situation.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/Koszul/Situation.lean#L57).

> **Stacks Project, Tag 08CZ.** The standing situation of the section on Koszul complexes:
> a commutative ring `A` and a finite sequence `f₁, …, f_r` of elements of `A`. The affine
> scheme `X = Spec(A)`, the open `U = D(f₁) ∪ ⋯ ∪ D(f_r)` and the covering `𝒰` of `U` by the
> standard opens `D(fᵢ)` are derived from these data.

```lean
structure CechSituation
```

## Tag 08D0, a lemma

[Tag 08D0](https://stacks.math.columbia.edu/tag/08D0) in the Stacks Project.

**`Koszul.alternatingCechComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Koszul/AlternatingCechColimit.lean, line 894](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/Koszul/AlternatingCechColimit.lean#L894). References: EGA III (2.1.2), “special case”.

> **Stacks Project, Tag 08D0.** The canonical identification between the colimit of the
> contragredient Koszul complexes and the alternating Čech complex of `M^~`.

```lean
noncomputable def alternatingCechComplexIso {r : ℕ} (f : Fin r → A) (M : ModuleCat.{v} A) :
    colimit (koszulHomDiagram f M) ≅ moduleAlternatingCechComplex f M
```

**`Koszul.alternatingCechComplexIso_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Koszul/AlternatingCechColimit.lean, line 908](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/Koszul/AlternatingCechColimit.lean#L908).

> **Stacks Project, Tag 08D0.** The identification is natural in the module.

```lean
theorem alternatingCechComplexIso_naturality {r : ℕ} (f : Fin r → A)
    (M N : ModuleCat.{v} A) (g : M ⟶ N) :
    (alternatingCechComplexIso f M).hom ≫ moduleAlternatingCechMap f g =
      koszulHomColimitMap f g ≫ (alternatingCechComplexIso f N).hom
```

**`Koszul.alternatingCechComplexIso_ι_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Koszul/AlternatingCechColimit.lean, line 924](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/Koszul/AlternatingCechColimit.lean#L924).

> **Stacks Project, Tag 08D0.** On the stage-`e` linear form `t` the identification takes the
> value `(-1)^p t([i₀, …, iₚ]) / ∏ⱼ f(iⱼ)^(e+1)` at the tuple `i`.

```lean
theorem alternatingCechComplexIso_ι_apply {r : ℕ} (f : Fin r → A) (M : ModuleCat.{v} A)
    (e p : ℕ) (t : (koszulIdealComplexPower f e).X p →ₗ[A] M) (i : Fin (p + 1) → Fin r) :
    (((colimit.ι (koszulHomDiagram f M) e ≫
        (alternatingCechComplexIso f M).hom).f p) t).1 i =
      koszulCechFraction f M e p t i
```

## Tag 08D1, a lemma

[Tag 08D1](https://stacks.math.columbia.edu/tag/08D1) in the Stacks Project.

**`Koszul.koszulHomColimitIsoAlternatingCechTotal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Koszul/AlternatingCechTotal.lean, line 929](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/Koszul/AlternatingCechTotal.lean#L929).

> **Stacks Project, Tag 08D1.** The filtered colimit of the Hom complexes from the powers
> of the truncated Koszul complex is canonically isomorphic to the total alternating Čech complex
> of the associated sheaf complex, naturally in the coefficient complex.

```lean
noncomputable def koszulHomColimitIsoAlternatingCechTotal
    {A : Type u} [CommRing A] {r : ℕ} (f : Fin r → A) :
    koszulHomColimitFunctor f ⋙
        (forget₂ (ModuleCat.{u} A) AddCommGrpCat.{u}).mapHomologicalComplex (up ℤ) ≅
      alternatingCechTotalFunctor f
```

## Tag 08D2, a lemma

[Tag 08D2](https://stacks.math.columbia.edu/tag/08D2) in the Stacks Project.

**`Koszul.CechSituation.isIso_linearAlternatingCechToDerivedComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Koszul/AlternatingCechComputesCohomology.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/Koszul/AlternatingCechComputesCohomology.lean#L164). The attribute's comment: “the canonical map in D(A) is an isomorphism”.

> **Stacks Project, Tag 08D2.** In the situation of [Stacks, Tag 08CZ], for a complex `F^•`
> of quasi-coherent `𝒪_U`-modules the comparison map `Tot(Č_alt^•(𝒰, F^•)) ⟶ RΓ(U, F^•)` of
> [Stacks, Tag 08C1], taken in `D(A)`, is an isomorphism.

```lean
theorem isIso_linearAlternatingCechToDerivedComparison (F : CochainComplex S.scheme.Modules ℤ)
    (hF : ∀ n, (F.X n).IsQuasicoherent) :
    IsIso ((Stacks.Cech.linearAlternatingCechToDerivedComparison (TopCat.of S.scheme)
      S.scheme.ringCatSheaf S.baseCenter S.coverUlift S.iSup_coverUlift).app F)
```

**`Koszul.CechSituation.alternatingCechTotalNatIsoDerivedSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/Koszul/AlternatingCechComputesCohomology.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/Koszul/AlternatingCechComputesCohomology.lean#L179). The attribute's comment: “the isomorphism in D(A), functorial in F^•”.

> **Stacks Project, Tag 08D2.** In the situation of [Stacks, Tag 08CZ], the canonical
> isomorphism `Tot(Č_alt^•(𝒰, F^•)) ≅ RΓ(U, F^•)` in `D(A)`, natural in the complex `F^•` of
> quasi-coherent `𝒪_U`-modules: its components are the comparison maps of [Stacks, Tag 08C1].

```lean
def alternatingCechTotalNatIsoDerivedSections :
    S.QuasicoherentComplex.ι ⋙
        Stacks.Cech.linearAlternatingCechDerivedFunctor (TopCat.of S.scheme)
          S.scheme.ringCatSheaf S.baseCenter S.coverUlift ≅
      S.QuasicoherentComplex.ι ⋙
        Stacks.Cech.linearUnboundedDerivedGlobalSectionsFunctor (TopCat.of S.scheme)
          S.scheme.ringCatSheaf S.baseCenter
```

**`Koszul.DerivedSystem.isIso_alternatingCechToDerivedComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/KoszulCechComputesSections.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/KoszulCechComputesSections.lean#L160). The attribute's comment: “the comparison map is an isomorphism, in D(Ab)”.

> **Stacks Project, Tag 08D2, in `D(Ab)`.**  In Situation 08CZ, the comparison map
> `Tot(Č_alt(𝒰, ℱ^•)) ⟶ RΓ(U, ℱ^•)` of Tag 08C1 for the covering `𝒰` of `U` by the basic opens
> `D(fᵢ)` is an isomorphism in `D(Ab)` for every complex `ℱ^•` of quasi-coherent
> `𝒪_U`-modules.

```lean
public theorem isIso_alternatingCechToDerivedComparison (f : Fin r → A)
    (K : CochainComplex (SheafOfModules.{u} (unionRingSheaf f)) ℤ)
    (hK : ∀ n : ℤ, (K.X n).IsQuasicoherent) :
    IsIso ((Stacks.Cech.alternatingCechToDerivedComparison (unionSpace f)
      (unionRingSheaf f) (unionSpaceCover f) (iSup_unionSpaceCover f)).app K)
```

## Tag 08DC, an equation

[Tag 08DC](https://stacks.math.columbia.edu/tag/08DC) in the Stacks Project.

**`Koszul.DerivedSystem.cohomologyComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/KoszulCohomologyComparison.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/KoszulCohomologyComparison.lean#L358).

> **The comparison map of Stacks 08DC.** For every object `E` of `D(𝒪_X)` the maps
> `Iₑ → 𝒪_X`, which become isomorphisms after restriction to `U = D(f₁) ∪ ⋯ ∪ D(f_r)`, induce a
> canonical homomorphism
>
> `colimₑ Hom_{D(𝒪_X)}(Iₑ, E) ⟶ H⁰(U, E)`,
>
> sending the class of `α : Iₑ → E` to the restriction of `α` to `U` precomposed with the inverse
> of the restriction of `Iₑ → 𝒪_X`, read as a degree-zero hypercohomology class over `U`.

```lean
public def cohomologyComparison (f : Fin r → A) (E : derivedCat A) :
    ↥(colimit (homGroupSystem f E)) →+ ↥((sectionsOnUnion f).obj E)
```

## Tag 08DD, a proposition

[Tag 08DD](https://stacks.math.columbia.edu/tag/08DD) in the Stacks Project.

**`Koszul.DerivedSystem.cohomologyComparison_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/KoszulCohomologyComparisonBijective.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/KoszulCohomologyComparisonBijective.lean#L360).

> **Stacks 08DD.** In the situation of [Stacks, Tag 08CZ] — `A` a commutative ring, `f` a
> finite sequence in `A`, `X = Spec A` and `U = D(f₁) ∪ ⋯ ∪ D(f_r)` — the comparison map of
> [Stacks, Tag 08DC]
>
> `colimₑ Hom_{D(𝒪_X)}(Iₑ, E) ⟶ H⁰(U, E)`
>
> is an isomorphism for every object `E` of `D_QCoh(𝒪_X)`.

```lean
public theorem cohomologyComparison_bijective (E : derivedCat A)
    (hE : Stacks.DerivedQCoh.IsDQCoh (R := (Spec A).ringCatSheaf) E) :
    Function.Bijective (cohomologyComparison f E)
```

## Tag 08E3, a lemma

[Tag 08E3](https://stacks.math.columbia.edu/tag/08E3) in the Stacks Project.

**`AdicKoszul.exists_koszulPower_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/Coherator/KoszulPowerLift.lean, line 577](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/Coherator/KoszulPowerLift.lean#L577).

> A degree-zero class of a quasi-coherent complex on `Spec A`, supported on the
> closed complement of a union of `r` basic opens in the indicated range, comes
> from a Koszul complex on powers of the defining equations.

```lean
public theorem exists_koszulPower_lift {A : Type u} [CommRing A] {r : ℕ}
    (f : Fin r → A) (E : DerivedCategory (ModuleCat.{u} A))
    (hE : ∀ i : Fin r, ∀ n : ℤ, -(r : ℤ) + 1 ≤ n → n ≤ 0 →
      ∀ x : (DerivedCategory.homologyFunctor (ModuleCat.{u} A) n).obj E,
        ∃ k : ℕ, f i ^ k • x = 0)
    (s : DerivedCategory.Q.obj
      (((CochainComplex.singleFunctors (ModuleCat.{u} A)).functor 0).obj
        (ModuleCat.of A A)) ⟶ E) :
    ∃ e : ℕ, ∃ t : (AdicKoszul.canonicalKoszulPowerSystem f).obj ⟨e⟩ ⟶ E,
      s = DerivedCategory.Q.map (AdicKoszul.koszulPowerUnit f e) ≫ t
```

**`Stacks.Koszul.PowerLift.exists_koszulPower_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/PowerLift/KoszulPowerLift.lean, line 553](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/PowerLift/KoszulPowerLift.lean#L553).

> **[Stacks, Tag 08E3] over a ring**, with the target read as a term of the canonical Koszul
> power system `AdicKoszul.canonicalKoszulPowerSystem`. That system is defined at
> `CategoryTheory.HasDerivedCategory.standard`, so this form of the statement is available only at
> that model; `Stacks.Koszul.PowerLift.exists_koszulPower_lift_koszulCochain` is the same result at
> an arbitrary one.

```lean
public theorem exists_koszulPower_lift {r : ℕ} (f : Fin r → A)
    (E : DerivedCategory (ModuleCat.{u} A))
    (hE : ∀ i : Fin r, ∀ n : ℤ, -(r : ℤ) + 1 ≤ n → n ≤ 0 →
      ∀ x : (DerivedCategory.homologyFunctor (ModuleCat.{u} A) n).obj E,
        ∃ k : ℕ, f i ^ k • x = 0)
    (s : DerivedCategory.Q.obj
      (((CochainComplex.singleFunctors (ModuleCat.{u} A)).functor 0).obj
        (ModuleCat.of A A)) ⟶ E) :
    ∃ e : ℕ, ∃ t : (AdicKoszul.canonicalKoszulPowerSystem f).obj ⟨e⟩ ⟶ E,
      s = DerivedCategory.Q.map (AdicKoszul.koszulPowerUnit f e) ≫ t
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.9, Tag 08CX](https://stacks.math.columbia.edu/tag/08CX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
