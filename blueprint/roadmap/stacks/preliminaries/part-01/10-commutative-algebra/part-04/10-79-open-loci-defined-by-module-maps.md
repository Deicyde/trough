---
declaration: section
origin: cited
lean: LinearMap.setOf_localizedMap_atPrime_surjective_eq_setOf_baseChange_surjective, LinearMap.isOpen_setOf_localizedMap_atPrime_bijective, Module.FinitePresentation.exists_free_localizedModule_powers, Stacks.FiniteProjective.MapLocus.isOpen_injLocus_and_localized, Stacks.FiniteProjective.MapLocus.isOpen_surjLocus_and_localized, Stacks.FiniteProjective.MapLocus.isOpen_isoLocus_and_localized
statement: formalized
proof: formalized
---

# 10.79 Open loci defined by module maps

Section 10.79 of the Stacks Project, [Tag 05GD](https://stacks.math.columbia.edu/tag/05GD). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05GE, a lemma

[Tag 05GE](https://stacks.math.columbia.edu/tag/05GE) in the Stacks Project.

**`LinearMap.setOf_localizedMap_atPrime_surjective_eq_setOf_baseChange_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/SurjectivityLocus.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/SurjectivityLocus.lean#L122). The attribute's comment: “the equality of the two loci in the displayed formula”.

> Let `R` be a ring and let `φ : M →ₗ[R] N` be a map of `R`-modules whose cokernel `N ⧸ φ.range`
> is a finite `R`-module. Then the set of primes `p` of `R` such that the localized map
> `φ_p : M_p → N_p` is surjective is the set of primes `p` such that the fibre map
> `φ ⊗ κ(p) : M ⊗_R κ(p) → N ⊗_R κ(p)` is surjective.

```lean
public theorem LinearMap.setOf_localizedMap_atPrime_surjective_eq_setOf_baseChange_surjective
    {R M N : Type*} [CommRing R] [AddCommGroup M] [Module R M] [AddCommGroup N] [Module R N]
    (φ : M →ₗ[R] N) [Module.Finite R (N ⧸ φ.range)] :
    {p : PrimeSpectrum R | Function.Surjective (LocalizedModule.map p.asIdeal.primeCompl φ)} =
      {p | Function.Surjective (φ.baseChange p.asIdeal.ResidueField)}
```

## Tag 05GF, a lemma

[Tag 05GF](https://stacks.math.columbia.edu/tag/05GF) in the Stacks Project.

**`LinearMap.isOpen_setOf_localizedMap_atPrime_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/FinitePresentation/Locus.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/FinitePresentation/Locus.lean#L102).

> Let `R` be a ring and let `φ : M →ₗ[R] N` be a map of `R`-modules with `M` a finite
> `R`-module and `N` a finitely presented `R`-module. Then the set of primes `p` of `R` such that
> the localized map `φ_p : M_p → N_p` is an isomorphism is an open subset of `Spec(R)`.

```lean
public theorem LinearMap.isOpen_setOf_localizedMap_atPrime_bijective
    {R M N : Type*} [CommRing R] [AddCommGroup M] [Module R M] [AddCommGroup N] [Module R N]
    (φ : M →ₗ[R] N) [Module.Finite R M] [Module.FinitePresentation R N] :
    IsOpen {p : PrimeSpectrum R |
      Function.Bijective (LocalizedModule.map p.asIdeal.primeCompl φ)}
```

## Tag 0GWM, a lemma

[Tag 0GWM](https://stacks.math.columbia.edu/tag/0GWM) in the Stacks Project.

Declarations registered for the tag:

- [`Module.FinitePresentation.exists_free_localizedModule_powers`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.FinitePresentation.exists_free_localizedModule_powers#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L255) (StacksFrontier). References: EGA IV (8.5.5), “special case”.

## Tag 00O0, a lemma

[Tag 00O0](https://stacks.math.columbia.edu/tag/00O0) in the Stacks Project.

**`Stacks.FiniteProjective.MapLocus.isOpen_injLocus_and_localized`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/Locus.lean, line 882](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/Projective/Locus.lean#L882). The attribute's comment: “(1)”. References: EGA 0 (19.1.12), “P₁,P₂ finite projective”; EGA IV (11.3.7), “affine case, b)=>a)”.

> **(Injectivity locus.)** The injectivity locus `U` is open, and for every
> `f` with `D(f) ⊆ U`:
> (a) the localized map `φ_f` is injective; and
> (b) `Coker(φ)_f` is finite projective over `R_f`.

```lean
theorem isOpen_injLocus_and_localized
    (φ : P₁ →ₗ[R] P₂) [Module.Finite R P₁] [Module.Projective R P₁]
    [Module.Finite R P₂] [Module.Projective R P₂] :
    IsOpen (injLocus φ) ∧
    ∀ f : R, (PrimeSpectrum.basicOpen f : Set (PrimeSpectrum R)) ⊆ injLocus φ →
      Function.Injective (localizedMap φ f) ∧
      Module.Finite (Localization.Away f)
        (Localization.Away f ⊗[R] (P₂ ⧸ LinearMap.range φ)) ∧
      Module.Projective (Localization.Away f)
        (Localization.Away f ⊗[R] (P₂ ⧸ LinearMap.range φ))
```

**`Stacks.FiniteProjective.MapLocus.isOpen_surjLocus_and_localized`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/Locus.lean, line 901](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/Projective/Locus.lean#L901). The attribute's comment: “(2)”.

> **(Surjectivity locus.)** The surjectivity locus `W` is open, and for every
> `f` with `D(f) ⊆ W`:
> (a) the localized map `φ_f` is surjective; and
> (b) `Ker(φ)_f` is finite projective over `R_f`.

```lean
theorem isOpen_surjLocus_and_localized
    (φ : P₁ →ₗ[R] P₂) [Module.Finite R P₁] [Module.Projective R P₁]
    [Module.Finite R P₂] [Module.Projective R P₂] :
    IsOpen (surjLocus φ) ∧
    ∀ f : R, (PrimeSpectrum.basicOpen f : Set (PrimeSpectrum R)) ⊆ surjLocus φ →
      Function.Surjective (localizedMap φ f) ∧
      Module.Finite (Localization.Away f)
        (Localization.Away f ⊗[R] (LinearMap.ker φ)) ∧
      Module.Projective (Localization.Away f)
        (Localization.Away f ⊗[R] (LinearMap.ker φ))
```

**`Stacks.FiniteProjective.MapLocus.isOpen_isoLocus_and_localized`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/Locus.lean, line 924](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/Projective/Locus.lean#L924). The attribute's comment: “(3)”.

> **(Isomorphism locus.)** The isomorphism locus `V` is open, and for every
> `f` with `D(f) ⊆ V`, the localized map `φ_f` is bijective.
>
> Formal consequence of Theorems 1 and 2: `isoLocus φ = injLocus φ ∩ surjLocus φ`
> (`isoLocus_eq`), so it is open as an intersection of two opens; and on
> `D(f) ⊆ isoLocus φ ⊆ injLocus φ` (resp. `⊆ surjLocus φ`) the localized map is both
> injective (`injective_localizedMap_of_subset`) and surjective
> (`surjective_localizedMap_of_subset`), hence bijective.

```lean
theorem isOpen_isoLocus_and_localized
    (φ : P₁ →ₗ[R] P₂) [Module.Finite R P₁] [Module.Projective R P₁]
    [Module.Finite R P₂] [Module.Projective R P₂] :
    IsOpen (isoLocus φ) ∧
    ∀ f : R, (PrimeSpectrum.basicOpen f : Set (PrimeSpectrum R)) ⊆ isoLocus φ →
      Function.Bijective (localizedMap φ f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.79, Tag 05GD](https://stacks.math.columbia.edu/tag/05GD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
