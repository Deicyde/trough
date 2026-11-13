---
declaration: section
origin: cited
lean: isKInjective_restrictScalars_of_flat, isKInjective_of_restrictScalars_of_isEpi, coextend_isKInjective
statement: formalized
proof: formalized
---

# 15.57 Derived categories of modules

Section 15.57 of the Stacks Project, [Tag 0914](https://stacks.math.columbia.edu/tag/0914). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0915, a lemma

[Tag 0915](https://stacks.math.columbia.edu/tag/0915) in the Stacks Project.

**`isKInjective_restrictScalars_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/KInjective/ChangeOfRings.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/KInjective/ChangeOfRings.lean#L99). References: SGA 4 V (4.9), “special case”.

> **Stacks Tag 0915.** Let `f : R → S` be a flat ring map of commutative rings. If `I` is a
> K-injective complex of `S`-modules, then its restriction of scalars `res_f I` is a K-injective
> complex of `R`-modules.
>
> This is the adjoint criterion `CochainComplex.isKInjective_mapHomologicalComplex` (Stacks
> 13.31.9) applied to the extension–restriction adjunction `(- ⊗_R S) ⊣ res_f` (Stacks 05DQ,
> `ModuleCat.extendRestrictScalarsAdj`): the left adjoint `- ⊗_R S` preserves acyclicity by
> `acyclic_extendScalarsComplex_of_flat`, which is where flatness enters.

```lean
theorem isKInjective_restrictScalars_of_flat
    {R S : Type u₁} [CommRing R] [CommRing S] (f : R →+* S) (hf : f.Flat)
    (I : CochainComplex (ModuleCat.{max v u₁} S) ℤ) (hI : I.IsKInjective) :
    ((CochainComplex.restrictScalars f).obj I).IsKInjective
```

## Tag 0916, a lemma

[Tag 0916](https://stacks.math.columbia.edu/tag/0916) in the Stacks Project.

**`isKInjective_of_restrictScalars_of_isEpi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/KInjective/ChangeOfRings.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/KInjective/ChangeOfRings.lean#L162).

> **Stacks 0916.** Let `R → S` be an epimorphism of commutative rings. If a complex of
> `S`-modules is K-injective when regarded as a complex of `R`-modules, then it is K-injective as
> a complex of `S`-modules.
>
> Given an acyclic complex `K` of `S`-modules and a chain map `f : K → I`, restriction of scalars
> keeps `K` acyclic, so the hypothesis supplies a null-homotopy of `res f`. Restriction of scalars
> is full and faithful here, so that homotopy is the image of a null-homotopy of `f` itself.

```lean
theorem isKInjective_of_restrictScalars_of_isEpi [Algebra.IsEpi R S]
    (I : CochainComplex (ModuleCat.{max w u₁ u₂} S) ℤ)
    (hI : CochainComplex.IsKInjective
      (((ModuleCat.restrictScalars (algebraMap R S)).mapHomologicalComplex
        (ComplexShape.up ℤ)).obj I :
          CochainComplex (ModuleCat.{max w u₁ u₂} R) ℤ)) :
    CochainComplex.IsKInjective I
```

## Tag 0917, a lemma

[Tag 0917](https://stacks.math.columbia.edu/tag/0917) in the Stacks Project.

**`coextend_isKInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/KInjective/ChangeOfRings.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/KInjective/ChangeOfRings.lean#L230).

> **Stacks Tag 0917.** If `I` is a K-injective complex of `R`-modules, then its degreewise
> coextension of scalars `Hom_R(S, I)` is a K-injective complex of `S`-modules.
>
> This is the adjoint criterion `CochainComplex.isKInjective_mapHomologicalComplex` for the
> adjunction `ModuleCat.restrictCoextendScalarsAdj f`, whose left adjoint `(-)_R` preserves
> acyclicity by `restrictScalars_acyclic`.

```lean
theorem coextend_isKInjective {R : Type u₁} {S : Type u₂} [Ring R] [Ring S] (f : R →+* S)
    (I : CochainComplex (ModuleCat.{max v u₂} R) ℤ) (hI : I.IsKInjective) :
    ((coextendComplex.{u₁, u₂, v} f).obj I).IsKInjective
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.57, Tag 0914](https://stacks.math.columbia.edu/tag/0914)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
