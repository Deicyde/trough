---
declaration: section
origin: cited
lean: IsIPowerTorsion, IsElementPowerTorsion, exists_directSum_quotient_resolution, torsionBySet_eq_bot_iff_powers_eq_bot_iff_bigLambda_injective, torsionBySet_quotient_primaryComponent_eq_bot_and_isIPowerTorsion_of_exact, isSerreClass_isIPowerTorsion, isIPowerTorsion_iff_support_subset, StacksDraft.PowerTorsionVanishing.positive_homology_derivedTensorProduct_isZero_of_mod_ideal
statement: formalized
proof: formalized
---

# 15.90 Torsion modules

Section 15.90 of the Stacks Project, [Tag 0ALX](https://stacks.math.columbia.edu/tag/0ALX). 9 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05E6, a definition

[Tag 05E6](https://stacks.math.columbia.edu/tag/05E6) in the Stacks Project.

**`IsIPowerTorsion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/IPowerTorsion.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/IPowerTorsion.lean#L58).

> An `R`-module `M` is *`I`-power torsion* if for every `m ∈ M` there exists an
> integer `n > 0` such that `Iⁿ m = 0`, i.e. `a • m = 0` for every `a ∈ Iⁿ`.

```lean
def IsIPowerTorsion (R : Type*) [CommSemiring R] (M : Type*) [AddCommMonoid M]
    [Module R M] (I : Ideal R) : Prop
```

**`IsElementPowerTorsion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/IPowerTorsion.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/IPowerTorsion.lean#L65).

> An `R`-module `M` is *`f`-power torsion* if every element is annihilated by some strictly
> positive power of `f`.

```lean
def IsElementPowerTorsion (R : Type*) [CommSemiring R] (M : Type*) [AddCommMonoid M]
    [Module R M] (f : R) : Prop
```

## Tag 05E8, a lemma

[Tag 05E8](https://stacks.math.columbia.edu/tag/05E8) in the Stacks Project.

**`exists_directSum_quotient_resolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/IPowerTorsion/Resolution.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/IPowerTorsion/Resolution.lean#L151).

> **Stacks 05E8.** An `I`-power torsion module admits an exact resolution whose terms are
> direct sums of quotients of the ring by positive powers of `I`.

```lean
public theorem exists_directSum_quotient_resolution
    (R : Type u) [CommRing R] (I : Ideal R)
    (M : Type v) [AddCommGroup M] [Module R M]
    (hM : IsIPowerTorsion R M I) :
    ∃ (α : ℕ → Type (max u v)) (n : ∀ i, α i → ℕ),
      (∀ i a, 0 < n i a) ∧
        ∃ (d : ∀ i,
            DirectSum (α (i + 1)) (fun a ↦ R ⧸ I ^ n (i + 1) a) →ₗ[R]
              DirectSum (α i) (fun a ↦ R ⧸ I ^ n i a))
          (ε : DirectSum (α 0) (fun a ↦ R ⧸ I ^ n 0 a) →ₗ[R] M),
          Function.Surjective ε ∧ Function.Exact (d 0) ε ∧
            ∀ i, Function.Exact (d (i + 1)) (d i)
```

## Tag 05EA, a lemma

[Tag 05EA](https://stacks.math.columbia.edu/tag/05EA) in the Stacks Project.

**`torsionBySet_eq_bot_iff_powers_eq_bot_iff_bigLambda_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/IPowerTorsion.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/IPowerTorsion.lean#L170).

> For a finitely generated ideal `I`, the following are equivalent: no
> nonzero element of `M` is annihilated by `I`; the same holds for every positive power of `I`;
> and, for every finite generating family of `I`, the canonical map from `M` to the direct sum of
> the localizations at those generators is injective.

```lean
theorem torsionBySet_eq_bot_iff_powers_eq_bot_iff_bigLambda_injective
    {R : Type u} [CommRing R] (I : Ideal R)
    {M : Type v} [AddCommGroup M] [Module R M] (hI : I.FG) :
    (Submodule.torsionBySet R M (I : Set R) = ⊥ ↔
      ∀ n : ℕ, 1 ≤ n → Submodule.torsionBySet R M ((I ^ n : Ideal R) : Set R) = ⊥) ∧
    ((∀ n : ℕ, 1 ≤ n → Submodule.torsionBySet R M ((I ^ n : Ideal R) : Set R) = ⊥) ↔
      ∀ (t : ℕ) (f : Fin t → R), I = Ideal.span (Set.range f) →
        Function.Injective (bigLambda (M := M) t f))
```

## Tag 05EB, a lemma

[Tag 05EB](https://stacks.math.columbia.edu/tag/05EB) in the Stacks Project.

**`torsionBySet_quotient_primaryComponent_eq_bot_and_isIPowerTorsion_of_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/IPowerTorsion.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/IPowerTorsion.lean#L232).

> For a finitely generated ideal `I`, the quotient of any module by its
> `I`-primary component has no nonzero elements annihilated by `I`. Moreover, in a short exact
> sequence, if the first and third modules are `I`-power torsion, then so is the middle module.

```lean
theorem torsionBySet_quotient_primaryComponent_eq_bot_and_isIPowerTorsion_of_exact
    {R : Type u} [CommRing R] (I : Ideal R) (hI : I.FG) :
    (∀ (M : Type v) [AddCommGroup M] [Module R M],
      Submodule.torsionBySet R (M ⧸ (Ideal.primaryComponent M I)) (I : Set R) = ⊥) ∧
    ∀ (M₁ : Type v₁) (M₂ : Type v₂) (M₃ : Type v₃)
      [AddCommGroup M₁] [Module R M₁] [AddCommGroup M₂] [Module R M₂]
      [AddCommGroup M₃] [Module R M₃]
      (f : M₁ →ₗ[R] M₂) (g : M₂ →ₗ[R] M₃),
      Function.Injective f → Function.Exact f g → Function.Surjective g →
        IsIPowerTorsion R M₁ I →
        IsIPowerTorsion R M₃ I →
        IsIPowerTorsion R M₂ I
```

## Tag 0A6K, a lemma

[Tag 0A6K](https://stacks.math.columbia.edu/tag/0A6K) in the Stacks Project.

**`isSerreClass_isIPowerTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/IPowerTorsion/SerreClass.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/IPowerTorsion/SerreClass.lean#L43).

> **Stacks 0A6K.** The modules annihilated elementwise by positive powers of a finitely
> generated ideal form a Serre subcategory of the category of modules.

```lean
public theorem isSerreClass_isIPowerTorsion
    {R : Type u} [CommRing R] (I : Ideal R) (hI : I.FG) :
    CategoryTheory.ObjectProperty.IsSerreClass
      ((fun M : ModuleCat.{v} R => IsIPowerTorsion R M I) :
        CategoryTheory.ObjectProperty (ModuleCat.{v} R))
```

## Tag 0953, a lemma

[Tag 0953](https://stacks.math.columbia.edu/tag/0953) in the Stacks Project.

**`isIPowerTorsion_iff_support_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/IPowerTorsion.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/IPowerTorsion.lean#L108).

> Let `R` be a commutative ring and let `I ⊆ R` be a finitely generated ideal. Then for every
> `R`-module `M`, `M` is `I`-power torsion if and only if `Supp(M) ⊆ V(I)`.

```lean
theorem isIPowerTorsion_iff_support_subset
    (R : Type*) [CommRing R] (M : Type*) [AddCommGroup M] [Module R M]
    (I : Ideal R) (hI : I.FG) :
    IsIPowerTorsion R M I ↔
      Module.support R M ⊆ PrimeSpectrum.zeroLocus (I : Set R)
```

## Tag 0H82, a lemma

[Tag 0H82](https://stacks.math.columbia.edu/tag/0H82) in the Stacks Project.

**`StacksDraft.PowerTorsionVanishing.positive_homology_derivedTensorProduct_isZero_of_mod_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/TorsionAmplitude.lean, line 672](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/DerivedComplete/TorsionAmplitude.lean#L672).

> **Stacks 0H82.** If `K ⊗ᴸ[R] R / I` has no positive cohomology, then positive cohomology
> also vanishes after derived tensoring `K` with every positive-power quotient of `R`, with
> every `I`-power-torsion module, and with every bounded, nonpositively concentrated object of
> `D(R)` whose cohomology is `I`-power torsion.

```lean
public theorem positive_homology_derivedTensorProduct_isZero_of_mod_ideal
    {R : Type u} [CommRing R] (I : Ideal R)
    (K : DerivedCategory (ModuleCat.{u} R))
    (hK : ∀ i : ℤ, 0 < i →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) i).obj
        (((CochainComplex.DerivedTensor.canonicalDerivedTensorProductFunctor R).obj K).obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj
            (ModuleCat.of R (R ⧸ I)))))) :
    (∀ (n : ℕ), 0 < n → ∀ i : ℤ, 0 < i →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) i).obj
        (((CochainComplex.DerivedTensor.canonicalDerivedTensorProductFunctor R).obj K).obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj
            (ModuleCat.of R (R ⧸ I ^ n)))))) ∧
    (∀ (N : ModuleCat.{u} R), IsIPowerTorsion R N I → ∀ i : ℤ, 0 < i →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) i).obj
        (((CochainComplex.DerivedTensor.canonicalDerivedTensorProductFunctor R).obj K).obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj N)))) ∧
    (∀ (M : DerivedCategory.Bounded (ModuleCat.{u} R)),
      (∀ i : ℤ, IsIPowerTorsion R
        ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) i).obj M.obj) I) →
      (∀ i : ℤ, 0 < i →
        IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) i).obj M.obj)) →
      ∀ i : ℤ, 0 < i →
        IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) i).obj
          (((CochainComplex.DerivedTensor.canonicalDerivedTensorProductFunctor R).obj K).obj
            M.obj)))
```

## Tag 0G1T, a lemma

[Tag 0G1T](https://stacks.math.columbia.edu/tag/0G1T) in the Stacks Project.

**`IPowerTorsionDerivedTensor.derivedTensorProduct_isZero_of_mod_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/IPowerTorsion/TorAmplitude.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/IPowerTorsion/TorAmplitude.lean#L138).

> **Stacks 0G1T.** If `K ⊗ᴸ[R] R / I` vanishes, then so does the derived tensor product of `K`
> with every positive-power quotient of `R`, every `I`-power-torsion module, and every bounded
> derived object with `I`-power-torsion cohomology.

```lean
public theorem derivedTensorProduct_isZero_of_mod_ideal
    {R : Type u} [CommRing R] (I : Ideal R)
    (K : DerivedCategory (ModuleCat.{u} R))
    (hK : IsZero
      (((CochainComplex.DerivedTensor.canonicalDerivedTensorProductFunctor R).obj K).obj
        ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj
          (ModuleCat.of R (R ⧸ I))))) :
    (∀ (n : ℕ), 0 < n →
      IsZero
        (((CochainComplex.DerivedTensor.canonicalDerivedTensorProductFunctor R).obj K).obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj
            (ModuleCat.of R (R ⧸ I ^ n))))) ∧
    (∀ (N : ModuleCat.{u} R), IsIPowerTorsion R N I →
      IsZero
        (((CochainComplex.DerivedTensor.canonicalDerivedTensorProductFunctor R).obj K).obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj N))) ∧
    (∀ (M : DerivedCategory.Bounded (ModuleCat.{u} R)),
      (∀ i : ℤ, IsIPowerTorsion R
        ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) i).obj M.obj) I) →
      IsZero
        (((CochainComplex.DerivedTensor.canonicalDerivedTensorProductFunctor R).obj K).obj
          M.obj))
```

## Tag 0BNK, a lemma

[Tag 0BNK](https://stacks.math.columbia.edu/tag/0BNK) in the Stacks Project.

**`tensorProduct_mk_bijective_of_ideal_power_torsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/IPowerTorsion/ScalarExtension.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/IPowerTorsion/ScalarExtension.lean#L281). References: SGA 2 IV (4.5), “more general”; SGA 2 IV (4.6), “more general”.

> The canonical map from an ideal-power torsion module to its scalar extension is an
> isomorphism when the scalar extension is unchanged modulo every positive power of the ideal. In
> particular this holds for the adic completion of a finitely generated ideal; this is a slight
> generalization of Beauville--Laszlo, Lemme 1.

```lean
public theorem tensorProduct_mk_bijective_of_ideal_power_torsion
    (R : Type u) [CommRing R] (I : Ideal R)
    (M : Type w) [AddCommGroup M] [Module R M]
    (hM : ∀ m : M, ∃ n : ℕ, ∀ r ∈ I ^ n, r • m = 0) :
    (∀ (S : Type v) [CommRing S] [Algebra R S],
      (∀ n : ℕ, 0 < n →
        Function.Bijective
          (Ideal.quotientMap (Ideal.map (algebraMap R S) (I ^ n))
            (algebraMap R S) Ideal.le_comap_map)) →
      Function.Bijective (fun m : M => TensorProduct.mk R M S m (1 : S))) ∧
    (I.FG →
      Function.Bijective
        (fun m : M => TensorProduct.mk R M (AdicCompletion I R) m 1))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.90, Tag 0ALX](https://stacks.math.columbia.edu/tag/0ALX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
