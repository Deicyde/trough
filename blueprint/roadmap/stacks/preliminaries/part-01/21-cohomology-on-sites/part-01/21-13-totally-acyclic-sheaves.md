---
declaration: section
origin: cited
lean: Stacks.Cohomology.PresheafCoefficients.modulePresheafCohomologyFunctorIso, Stacks.Cohomology.exists_abutsTo_cechNerveSpectralSequence, Stacks.Cohomology.exists_abutsTo_cechNerveSpectralSequence_of_epi_sheafify, Stacks.Cohomology.SheafOfSets.cohomologyOnSheafIso, Stacks.Sites.LocalizationShriek.preservesInjectiveObjects_sheafLocalizationInverseImage, Stacks.Cohomology.IsTotallyAcyclic, Stacks.Cohomology.isTotallyAcyclic_iff
statement: formalized
proof: formalized
---

# 21.13 Totally acyclic sheaves

Section 21.13 of the Stacks Project, [Tag 079X](https://stacks.math.columbia.edu/tag/079X). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 079Y, a lemma

[Tag 079Y](https://stacks.math.columbia.edu/tag/079Y) in the Stacks Project.

**`Stacks.Cohomology.PresheafCoefficients.modulePresheafCohomologyFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/PresheafCoefficients/Basic.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/PresheafCoefficients/Basic.lean#L376). References: SGA 4 V (3.5), “H^q isomorphisms”; SGA 4 V (2.3.6), “e)”; SGA 4 V (4.4).

> **Stacks Project, Tag 079Y.** Cohomology of a sheaf of modules over a presheaf of sets is
> canonically and naturally isomorphic to the cohomology of its underlying sheaf of abelian
> groups.

```lean
public def modulePresheafCohomologyFunctorIso
    [HasExt.{u} (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))]
    [HasExt.{u} (Sheaf X.J AddCommGrpCat.{u})] :
    modulePresheafCohomologyFunctor X K p ≅ abelianPresheafCohomologyFunctor X K p
```

## Tag 079Z, a lemma

[Tag 079Z](https://stacks.math.columbia.edu/tag/079Z) in the Stacks Project.

**`Stacks.Cohomology.exists_abutsTo_cechNerveSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/CechNerveSpectralSequence.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/CechNerveSpectralSequence.lean#L226).

> **Stacks Project, Tag 079Z.** Let `𝒞` be a site and `K' → K` a map of presheaves of sets
> whose sheafification is surjective. For every abelian sheaf `𝓕` there is a cohomological spectral
> sequence, starting on page one, with
>
> ```
> E₁^{p,q} = H^q(K'_p, 𝓕),
> ```
>
> the cohomology of `𝓕` over the fibre power `K'_p = K' ×_K … ×_K K'` with `p + 1` factors,
> abutting to `H^{p+q}(K, 𝓕)`.
>
> Cohomology over a presheaf of sets is `Ext` out of the free abelian sheaf it generates, as in
> [Stacks, Tag 072Y]; see `Stacks.Cohomology.cohomologyOverSheafEquivZExt`. Abutment is
> `CategoryTheory.SpectralSequence.AbutsTo`: the spectral sequence has an infinity page everywhere
> and its terms are the graded pieces of a finite decreasing filtration of each `H^n(K, 𝓕)`.

```lean
theorem exists_abutsTo_cechNerveSpectralSequence (hf : Presheaf.IsLocallySurjective J f)
    (F : Sheaf J AddCommGrpCat.{u}) :
    ∃ E : CohomologicalSpectralSequence AddCommGrpCat.{u + 1} 1,
      (∀ (p : ℕ) (q : ℤ), Nonempty ((E.page 1).X ((p : ℤ), q) ≅
        AddCommGrpCat.of (Abelian.zExt
          ((Presheaf.freeAbelianSheaf J).obj (cechFibrePower f p)) F q))) ∧
      SpectralSequence.AbutsTo E (fun n ↦ AddCommGrpCat.of
        (Abelian.zExt ((Presheaf.freeAbelianSheaf J).obj K) F n))
```

**`Stacks.Cohomology.exists_abutsTo_cechNerveSpectralSequence_of_epi_sheafify`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/CechNerveSpectralSequence.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/CechNerveSpectralSequence.lean#L266).

> **Stacks Project, Tag 079Z**, with the hypothesis in the source's own words: the
> sheafification of `K' → K` is surjective, i.e. an epimorphism of sheaves of sets.
>
> This is `Stacks.Cohomology.exists_abutsTo_cechNerveSpectralSequence` read through
> `Stacks.Cohomology.isLocallySurjective_iff_epi_presheafToSheaf_map`. It needs sheafification of
> type-valued presheaves, which the statement with the locally surjective hypothesis does not.

```lean
theorem exists_abutsTo_cechNerveSpectralSequence_of_epi_sheafify [HasSheafify J (Type u)]
    (hf : Epi ((presheafToSheaf J (Type u)).map f)) (F : Sheaf J AddCommGrpCat.{u}) :
    ∃ E : CohomologicalSpectralSequence AddCommGrpCat.{u + 1} 1,
      (∀ (p : ℕ) (q : ℤ), Nonempty ((E.page 1).X ((p : ℤ), q) ≅
        AddCommGrpCat.of (Abelian.zExt
          ((Presheaf.freeAbelianSheaf J).obj (cechFibrePower f p)) F q))) ∧
      SpectralSequence.AbutsTo E (fun n ↦ AddCommGrpCat.of
        (Abelian.zExt ((Presheaf.freeAbelianSheaf J).obj K) F n))
```

## Tag 07A0, a lemma

[Tag 07A0](https://stacks.math.columbia.edu/tag/07A0) in the Stacks Project.

**`Stacks.Cohomology.SheafOfSets.cohomologyOnSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/CohomologyOverASheafOfSets.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/CohomologyOverASheafOfSets.lean#L268). The attribute's comment: “the cohomology comparison”.

> **Stacks 07A0, the cohomology comparison.** For a sheaf of sets `K` on a small site `(C, J)`,
> cohomology over `K` — that is, `Ext` out of the free abelian sheaf on `K` — is the cohomology of
> the site of elements of `K` with coefficients in the inverse image:
>
>   `Ext^p_{Sh(C, J)}(ℤ_K, -) ≅ j⁻¹ ⋙ H^p(C/K, -)`,
>
> naturally in the abelian sheaf of coefficients.

```lean
def cohomologyOnSheafIso (p : ℕ) :
    extFunctorObj (freeAbelianSheafOn J K) p ≅
      inverseImage J K ⋙ Sheaf.functorH (localizedTopology J K) p
```

**`Stacks.Sites.LocalizationShriek.preservesInjectiveObjects_sheafLocalizationInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/LocalizationShriekExact.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topos/LocalizationShriekExact.lean#L345). The attribute's comment: “the inverse image preserves injectives”.

> **Stacks 07A0, first assertion.** For a *sheaf* of sets `K`, the projection `j` from the site
> of elements of `K` is continuous for the restricted topology (Stacks 0791), so that restriction of
> abelian sheaves along it is the inverse image of the localization morphism of topoi
> `j : Sh(C/K) ⟶ Sh(C)`; that inverse image preserves injective abelian sheaves.
>
> The continuity instance is the one Stacks 0791 provides, so the functor here is literally the
> inverse image of the localization morphism and not merely isomorphic to it.

```lean
theorem preservesInjectiveObjects_sheafLocalizationInverseImage
    (J : GrothendieckTopology C) [HasSheafify J AddCommGrpCat.{v}] (K : Sheaf J (Type v)) :
    letI : (CostructuredArrow.proj yoneda K.obj).IsContinuous
        ((CostructuredArrow.proj yoneda K.obj).restrictedTopology J) J :=
      (K.property.exists_sheafEquivalence_costructuredArrow_yoneda).2.2.choose
    ((CostructuredArrow.proj yoneda K.obj).sheafPushforwardContinuous AddCommGrpCat.{v}
        ((CostructuredArrow.proj yoneda K.obj).restrictedTopology J)
        J).PreservesInjectiveObjects
```

## Tag 072Y, a definition

[Tag 072Y](https://stacks.math.columbia.edu/tag/072Y) in the Stacks Project.

**`Stacks.Cohomology.IsTotallyAcyclic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/TotallyAcyclicSheaves.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/TotallyAcyclicSheaves.lean#L63). References: SGA 4 V (4.1), “flasque case”.

> An abelian sheaf is **totally acyclic** if its cohomology over every sheaf of sets
> vanishes in every positive degree.

```lean
def IsTotallyAcyclic (F : Sheaf J AddCommGrpCat.{w}) : Prop
```

## Tag 07A1, a lemma

[Tag 07A1](https://stacks.math.columbia.edu/tag/07A1) in the Stacks Project.

**`Stacks.Cohomology.isTotallyAcyclic_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/TotallyAcyclicCriterion.lean, line 436](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/TotallyAcyclicCriterion.lean#L436).

> Let `𝒞` be a site and `𝓕` an abelian sheaf on it. Then `𝓕` is
> totally acyclic ([Stacks, Tag 072Y]) if and only if
>
> 1. `H^p(U, 𝓕) = 0` for `p > 0` and every object `U` of `𝒞` — `VanishesOnObjects`; and
> 2. for every surjection `K' ⟶ K` of sheaves of sets the extended Čech complex
>    `0 → H^0(K, 𝓕) → H^0(K', 𝓕) → H^0(K' ×_K K', 𝓕) → …` is exact — `CechComplexExact`.

```lean
theorem isTotallyAcyclic_iff (F : Sheaf J AddCommGrpCat.{u}) :
    IsTotallyAcyclic.{w} J F ↔ (VanishesOnObjects.{w} J F ∧ CechComplexExact J F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.13, Tag 079X](https://stacks.math.columbia.edu/tag/079X)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
