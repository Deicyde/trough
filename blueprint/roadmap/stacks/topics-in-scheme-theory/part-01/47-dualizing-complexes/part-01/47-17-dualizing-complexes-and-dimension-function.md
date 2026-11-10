---
declaration: section
origin: cited
lean: Dualizing.dualizingDimension, Dualizing.dualizingDimension_eq_iff, Dualizing.existsUnique_nontrivial_localized_homology, Dualizing.dualizingDimension_derivedHom_of_surjective, Dualizing.dualizingDimension_eq_succ_of_isImmediateSpecialization, Dualizing.dualizingDimension_lt_of_specializes, Dualizing.dualizingDimensionFunction, Dualizing.ringKrullDim_lt_top_of_isDualizingComplex
statement: formalized
proof: formalized
---

# 47.17 Dualizing complexes and dimension functions

Section 47.17 of the Stacks Project, [Tag 0A7W](https://stacks.math.columbia.edu/tag/0A7W). 6 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A7W, the section

[Tag 0A7W](https://stacks.math.columbia.edu/tag/0A7W) in the Stacks Project.

**`Dualizing.dualizingDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DimensionFunction.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DimensionFunction.lean#L119). The attribute's comment: “the function δ attached to a dualizing complex over a Noetherian ring”.

> The **dimension function** of a dualizing complex `K` over a Noetherian ring `A`: the value
> at a prime `p` is the unique integer `n` for which the localization `K_p`, shifted by `-n`, is a
> normalized dualizing complex over `A_p`. The infimum is a device for naming that integer; it is
> attained and unique by `Dualizing.dualizingDimension_eq_iff`.

```lean
noncomputable def dualizingDimension {A : Type u} [CommRing A] [IsNoetherianRing A]
    (K : DerivedCategory (ModuleCat.{max v u} A)) (p : PrimeSpectrum A) : ℤ
```

**`Dualizing.dualizingDimension_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DimensionFunction.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DimensionFunction.lean#L151). The attribute's comment: “δ(p) is the unique integer n with K_p⟦-n⟧ normalized over A_p”.

> **The defining property of the dimension function.** A shift of the localization of a
> dualizing complex at a prime is normalized exactly when the shift is the value of the dimension
> function there.

```lean
theorem dualizingDimension_eq_iff {A : Type u} [CommRing A] [IsNoetherianRing A]
    (K : DerivedCategory (ModuleCat.{max v u} A)) (hK : IsDualizingComplex K)
    (p : PrimeSpectrum A) (n : ℤ) :
    IsNormalizedDualizingComplex.{u, v}
        (((StacksDraft.PseudoCoherence.derivedExtensionScalars
          (algebraMap A (Localization.AtPrime p.asIdeal))).obj K)⟦-n⟧) ↔
      n = dualizingDimension.{u, v} K p
```

## Tag 0A7X, a lemma

[Tag 0A7X](https://stacks.math.columbia.edu/tag/0A7X) in the Stacks Project.

**`Dualizing.existsUnique_nontrivial_localized_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/MinimalPrimeNonvanishing.lean, line 533](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/MinimalPrimeNonvanishing.lean#L533).

> **Stacks Project, Tag 0A7X.** Let `A` be a Noetherian ring with a dualizing complex `K` and
> let `p` be a minimal prime of `A`. Then the localization at `p` of the cohomology module `H^i(K)`
> is nonzero for exactly one `i`.

```lean
theorem existsUnique_nontrivial_localized_homology
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (K : DerivedCategory (ModuleCat.{v} A)) (hK : IsDualizingComplex K)
    (p : Ideal A) [p.IsPrime] (hp : p ∈ minimalPrimes A) :
    ∃! i : ℤ, Nontrivial
      (LocalizedModule p.primeCompl
        ((DerivedCategory.homologyFunctor (ModuleCat.{v} A) i).obj K))
```

## Tag 0A7Y, a lemma

[Tag 0A7Y](https://stacks.math.columbia.edu/tag/0A7Y) in the Stacks Project.

**`Dualizing.dualizingDimension_derivedHom_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DimensionFunctionSurjective.lean, line 756](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DimensionFunctionSurjective.lean#L756).

> **Stacks 0A7Y.** For a surjection `f : A → B` of Noetherian rings and a dualizing complex
> `K` over `A`, the dimension function of the dualizing complex `RHom_A(B, K)` over `B` is the
> restriction of the dimension function of `K` along the induced closed immersion
> `Spec B → Spec A`.
>
> The hypothesis of
> `Dualizing.dualizingDimension_derivedHom_of_surjective_of_localizationComparison` is discharged
> here: the localization at `q` of `RHom_A(B, K)` is `RHom_{A_p}(B_q, K_p)`, where `g : A_p → B_q`
> is the surjection of local rings induced by `f`. Both sides are computed by one and the same
> complex of `B_q`-modules, namely the degreewise localization of the degreewise coextension of
> scalars of a bounded complex of injectives representing `K`; the identification of the two
> complexes is `Dualizing.coextendExtendScalarsIso`.

```lean
theorem dualizingDimension_derivedHom_of_surjective
    (f : A →+* B) (hf : Function.Surjective f)
    (K : DerivedCategory (ModuleCat.{max v u} A)) (hK : IsDualizingComplex K)
    (q : PrimeSpectrum B) :
    dualizingDimension.{u, v} ((derivedHom.{u, v} f).obj K) q
      = dualizingDimension.{u, v} K (PrimeSpectrum.comap f q)
```

## Tag 0A7Z, a lemma

[Tag 0A7Z](https://stacks.math.columbia.edu/tag/0A7Z) in the Stacks Project.

**`Dualizing.dualizingDimension_eq_succ_of_isImmediateSpecialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DimensionFunctionSpecialization.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DimensionFunctionSpecialization.lean#L301). The attribute's comment: “δ(p) = δ(q) + 1 for an immediate specialization p ⤳ q”.

> The dimension function of a dualizing complex drops by exactly one along an immediate
> specialization.

```lean
theorem dualizingDimension_eq_succ_of_isImmediateSpecialization
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (K : DerivedCategory (ModuleCat.{max v u} A)) (hK : IsDualizingComplex K)
    {p q : PrimeSpectrum A} (himm : IsImmediateSpecialization p q) :
    dualizingDimension.{u, v} K p = dualizingDimension.{u, v} K q + 1
```

**`Dualizing.dualizingDimension_lt_of_specializes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DimensionFunctionSpecialization.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DimensionFunctionSpecialization.lean#L392). The attribute's comment: “δ(q) < δ(p) for a non-trivial specialization p ⤳ q”.

> The dimension function of a dualizing complex drops strictly along a non-trivial
> specialization.

```lean
theorem dualizingDimension_lt_of_specializes
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (K : DerivedCategory (ModuleCat.{max v u} A)) (hK : IsDualizingComplex K)
    {p q : PrimeSpectrum A} (hpq : p ⤳ q) (hne : p ≠ q) :
    dualizingDimension.{u, v} K q < dualizingDimension.{u, v} K p
```

**`Dualizing.dualizingDimensionFunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DimensionFunctionSpecialization.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DimensionFunctionSpecialization.lean#L404). The attribute's comment: “the function δ of a dualizing complex is a dimension function on Spec A”.

> The dimension function `δ_K` of a dualizing complex `K` over a Noetherian ring `A`, as a
> dimension function on `Spec A`.

```lean
def dualizingDimensionFunction {A : Type u} [CommRing A] [IsNoetherianRing A]
    (K : DerivedCategory (ModuleCat.{max v u} A)) (hK : IsDualizingComplex K) :
    TopologicalSpace.DimensionFunction (PrimeSpectrum A)
```

## Tag 0A80, a lemma

[Tag 0A80](https://stacks.math.columbia.edu/tag/0A80) in the Stacks Project.

**`Dualizing.ringKrullDim_lt_top_of_isDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/FiniteDimension.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/FiniteDimension.lean#L360). The attribute's comment: “of finite dimension”.

> **Stacks Project, Tag 0A80.** A Noetherian ring admitting a dualizing complex has finite
> Krull dimension.

```lean
theorem ringKrullDim_lt_top_of_isDualizingComplex {A : Type u} [CommRing A] [IsNoetherianRing A]
    {K : DerivedCategory (ModuleCat.{u} A)} (hK : IsDualizingComplex K) :
    ringKrullDim A < ⊤
```

**`Dualizing.isUniversallyCatenary_of_isDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UniversallyCatenary.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UniversallyCatenary.lean#L110). The attribute's comment: “universally catenary”.

> **Stacks Project, Tag 0A80.** A Noetherian ring admitting a dualizing complex is universally
> catenary: every algebra of finite type over it is catenary.

```lean
theorem isUniversallyCatenary_of_isDualizingComplex {A : Type u} [CommRing A] [IsNoetherianRing A]
    {K : DerivedCategory (ModuleCat.{u} A)} (hK : IsDualizingComplex K) :
    Ring.IsUniversallyCatenary A
```

## Tag 0AWE, a lemma

[Tag 0AWE](https://stacks.math.columbia.edu/tag/0AWE) in the Stacks Project.

**`Dualizing.support_canonicalModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/CanonicalModule.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/CanonicalModule.lean#L293). The attribute's comment: “(1): the support of ω_A is the union of the d-dimensional irreducible components”.

> Let `A` be a Noetherian local ring with a normalized
> dualizing complex `K`, let `d = dim(A)` and let `ω_A = H^{-d}(K)`. The support of `ω_A` is the
> union of the irreducible components of `Spec(A)` of dimension `d`.

```lean
theorem support_canonicalModule
    {A : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (K : DerivedCategory (ModuleCat.{u} A)) (hK : IsNormalizedDualizingComplex.{u, u} K)
    (d : ℕ) (hd : ringKrullDim A = (d : WithBot ℕ∞)) :
    Module.support A ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) (-(d : ℤ))).obj K) =
      ⋃₀ {C ∈ irreducibleComponents (PrimeSpectrum A) |
        topologicalKrullDim C = (d : WithBot ℕ∞)}
```

**`Dualizing.propertySkModule_canonicalModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/CanonicalModuleDepth.lean, line 603](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/CanonicalModuleDepth.lean#L603). The attribute's comment: “(2): the canonical module ω_A satisfies Serre's condition (S₂)”.

> Let `A` be a Noetherian local ring with a normalized dualizing complex `K`, let `d = dim(A)`
> and let `ω_A = H^{-d}(K)`. Then `ω_A` satisfies Serre's condition `(S₂)`.

```lean
theorem propertySkModule_canonicalModule {A : Type u} [CommRing A] [IsNoetherianRing A]
    [IsLocalRing A] (K : DerivedCategory (ModuleCat.{u} A))
    (hK : IsNormalizedDualizingComplex.{u, u} K) :
    let d := (ringKrullDim A).unbotD 0 |>.toNat
    let ω := (DerivedCategory.homologyFunctor (ModuleCat.{u} A) (-(d : ℤ))).obj K
    letI : Module.Finite A ω := hK.1.finiteCohomology (-(d : ℤ))
    PropertySkModule A ω 2
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.17, Tag 0A7W](https://stacks.math.columbia.edu/tag/0A7W)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
