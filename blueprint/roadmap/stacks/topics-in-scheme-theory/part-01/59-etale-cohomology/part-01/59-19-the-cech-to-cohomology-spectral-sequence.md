---
declaration: section
origin: cited
lean: CategoryTheory.sheafToPresheaf_preservesInjectiveObjects, Stacks.CechComparison.exists_cechToCohomology_spectralSequence_pageTwo, Stacks.CechComparison.exists_cechToCohomology_spectralSequence_abutsTo_sheafCohomology
statement: formalized
proof: formalized
---

# 59.19 The Čech-to-cohomology spectral sequence

Section 59.19 of the Stacks Project, [Tag 03OU](https://stacks.math.columbia.edu/tag/03OU). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03OV, a lemma

[Tag 03OV](https://stacks.math.columbia.edu/tag/03OV) in the Stacks Project.

**`CategoryTheory.sheafToPresheaf_preservesInjectiveObjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/InjectiveSheafVanishing.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/InjectiveSheafVanishing.lean#L48). The attribute's comment: “the forgetful functor from sheaves to presheaves preserves injectives”. References: SGA 4 V (3.1), “special case”.

> The inclusion of sheaves into presheaves preserves injective objects.

```lean
theorem sheafToPresheaf_preservesInjectiveObjects {C : Type u} [Category.{v} C]
    (J : GrothendieckTopology C) (A : Type u') [Category.{v'} A] [HasSheafify J A] :
    (sheafToPresheaf J A).PreservesInjectiveObjects
```

## Tag 03OW, a theorem

[Tag 03OW](https://stacks.math.columbia.edu/tag/03OW) in the Stacks Project.

**`Stacks.CechComparison.exists_cechToCohomology_spectralSequence_pageTwo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CechComparison/Basic.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CechComparison/Basic.lean#L241). The attribute's comment: “the spectral sequence and its second page”. References: SGA 4 V (7.4.0), “Čech covering case”; SGA 4 V (3.2), “R = sieve of a family”.

> **Stacks Project, Tag 03OW: the Čech-to-cohomology spectral sequence, with its second
> page.**  For a covering family `𝒰 = E` of an object `U` of a site `C` and an abelian sheaf `F`
> there is a cohomological spectral sequence whose second page is
>
> ```
> E₂^{p,q} ≅ Ȟ^p(𝒰, H^q(F)),
> ```
>
> the Čech cohomology of the covering with coefficients in the cohomology presheaves
> `H^q(F) : V ↦ H^q(V, F)`, and which abuts to `R^{p+q}(Ȟ⁰(𝒰, -) ∘ i)(F)`.
>
> The abutment is the cohomology of the right derived functor of the composite
> `Ȟ⁰(𝒰, -) ∘ i`, which is the group [Stacks, Tag 03OW] calls `H^{p+q}(U, F)`; the identification
> of the two is **not** part of this statement, which is why the tag carries a clause.  See the
> implementation notes of this file.

```lean
theorem exists_cechToCohomology_spectralSequence_pageTwo (F : Sheaf J AddCommGrpCat.{u}) :
    ∃ S : CohomologicalSpectralSequence AddCommGrpCat.{u} 0,
      (∀ p q : ℕ, Nonempty ((S.page 2 zero_le_two).X ((p : ℤ), (q : ℤ)) ≅
        Stacks.CechSite.cechCohomology E (F.cohomologyPresheaf q) p)) ∧
      SpectralSequence.AbutsTo S
        (fun n => (((sheafIncl J) ⋙ cechZeroFunctor E).rightDerivedPlus n).obj F)
```

**`Stacks.CechComparison.exists_cechToCohomology_spectralSequence_abutsTo_sheafCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CechComparison/SheafCohomologyAbutment.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CechComparison/SheafCohomologyAbutment.lean#L105). References: SGA 4 V (3.2), “special case”.

> **Stacks Project, Tag 03OW.**  Let `C` be a site, `𝒰 = E = {U_i → U}_{i ∈ I}` a covering of
> `U ∈ Ob(C)` (the family generates a covering sieve of `U`) and `F` an abelian sheaf on `C`.  There
> is a cohomological spectral sequence, zero outside the first quadrant, with second page
>
> ```
> E₂^{p,q} ≅ Ȟ^p(𝒰, H^q(F)),
> ```
>
> the Čech cohomology of the covering with coefficients in the abelian presheaf
> `H^q(F) : V ↦ H^q(V, F)`, and abutting to `H^{p+q}(U, F)`: the graded family abutted to is
> `n ↦ H^n(U, F)` in degrees `n ≥ 0` and is zero in negative degrees, where no term of the
> spectral sequence contributes.
>
> The spectral sequence is the Grothendieck spectral sequence of `Ȟ⁰(𝒰, -) ∘ i` of
> `exists_cechToCohomology_spectralSequence`; its abutment `R^n(Ȟ⁰(𝒰, -) ∘ i)(F)` is identified with
> `H^n(U, F)` by `Stacks.CechSite.rightDerivedPlus_cechZero_obj_iso_cohomologyPresheaf`.

```lean
theorem exists_cechToCohomology_spectralSequence_abutsTo_sheafCohomology
    (hE : E.sieve₀ ∈ J U) (F : Sheaf J AddCommGrpCat.{u}) :
    ∃ S : CohomologicalSpectralSequence AddCommGrpCat.{u} 0,
      (∀ p q : ℕ, Nonempty ((S.page 2 zero_le_two).X ((p : ℤ), (q : ℤ)) ≅
        Stacks.CechSite.cechCohomology E (F.cohomologyPresheaf q) p)) ∧
      (∀ p q : ℤ, p < 0 ∨ q < 0 → IsZero ((S.page 2 zero_le_two).X (p, q))) ∧
      SpectralSequence.AbutsTo S (fun n : ℤ ↦
        if n < 0 then ⊥_ AddCommGrpCat.{u} else (F.cohomologyPresheaf n.toNat).obj (op U))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.19, Tag 03OU](https://stacks.math.columbia.edu/tag/03OU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
