---
declaration: section
origin: cited
lean: Module.IsReflexive, isTorsionFree_of_isReflexive_and_dualEval_isTorsion_and_injective_iff, surjective_dualEval_of_finite, reflexive_tfae, isReflexive_of_exact_of_isReflexive_of_isTorsionFree, isReflexive_iff_exists_finFree_shortExact, isReflexive_baseChange_of_flat, isReflexive_linearMap
statement: formalized
proof: formalized
---

# 15.24 Reflexive modules

Section 15.24 of the Stacks Project, [Tag 0AUY](https://stacks.math.columbia.edu/tag/0AUY). 20 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AUZ, a definition

[Tag 0AUZ](https://stacks.math.columbia.edu/tag/0AUZ) in the Stacks Project.

Declarations registered for the tag:

- [`Module.IsReflexive`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.IsReflexive#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/Reflexive.lean, line 2851](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Reflexive.lean#L2851) (StacksFrontier).

## Tag 0AV0, a lemma

[Tag 0AV0](https://stacks.math.columbia.edu/tag/0AV0) in the Stacks Project.

**`isTorsionFree_of_isReflexive_and_dualEval_isTorsion_and_injective_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Reflexive.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Reflexive.lean#L425).

> **Stacks Tag 0AV0.** A reflexive module over a domain is torsion-free. For a finite module,
> the kernel and cokernel of the canonical evaluation map into the double dual are torsion,
> and that map is injective if and only if the module is torsion-free.

```lean
theorem isTorsionFree_of_isReflexive_and_dualEval_isTorsion_and_injective_iff
    {R : Type u} [CommRing R] [IsDomain R]
    {M : Type v} [AddCommGroup M] [Module R M] :
    (Module.IsReflexive R M → Module.IsTorsionFree R M) ∧
      (Module.Finite R M →
        Module.IsTorsion R (LinearMap.ker (Module.Dual.eval R M)) ∧
          Module.IsTorsion R
            (Module.Dual R (Module.Dual R M) ⧸ LinearMap.range (Module.Dual.eval R M))) ∧
      (Module.Finite R M →
        (Function.Injective (Module.Dual.eval R M) ↔ Module.IsTorsionFree R M))
```

## Tag 0B36, a lemma

[Tag 0B36](https://stacks.math.columbia.edu/tag/0B36) in the Stacks Project.

**`surjective_dualEval_of_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Reflexive.lean, line 679](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Reflexive.lean#L679).

> **Stacks Tag 0B36.** The canonical evaluation map from a finite module over a Dedekind domain
> to its double dual is surjective.

```lean
theorem surjective_dualEval_of_finite
    (R : Type u) [CommRing R] [IsDedekindDomain R]
    (M : Type v) [AddCommGroup M] [Module R M] [Module.Finite R M] :
    Function.Surjective (Module.Dual.eval R M)
```

## Tag 0AV1, a lemma

[Tag 0AV1](https://stacks.math.columbia.edu/tag/0AV1) in the Stacks Project.

**`reflexive_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Reflexive/Localization.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Reflexive/Localization.lean#L186).

> **Stacks 0AV1**.
> Let `R` be a Noetherian ring and `M` a finite `R`-module. The following are equivalent: `M` is
> reflexive; `M_p` is a reflexive `R_p`-module for every prime `p`; `M_m` is a reflexive
> `R_m`-module for every maximal ideal `m`.

```lean
theorem reflexive_tfae
    (R : Type*) [CommRing R] [IsNoetherianRing R]
    (M : Type*) [AddCommGroup M] [Module R M] [Module.Finite R M] :
    [ Module.IsReflexive R M,
      ∀ (p : Ideal R) [p.IsPrime],
        Module.IsReflexive (Localization.AtPrime p) (LocalizedModule p.primeCompl M),
      ∀ (m : Ideal R) [m.IsMaximal],
        Module.IsReflexive (Localization.AtPrime m) (LocalizedModule m.primeCompl M)
    ].TFAE
```

## Tag 0EB8, a lemma

[Tag 0EB8](https://stacks.math.columbia.edu/tag/0EB8) in the Stacks Project.

**`isReflexive_of_exact_of_isReflexive_of_isTorsionFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Reflexive.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Reflexive.lean#L446).

> **Stacks Tag 0EB8.** Let `R` be a Noetherian domain and let `0 → M → M' → M''` be an exact
> sequence of finite `R`-modules. If `M'` is reflexive and `M''` is torsion-free, then `M` is
> reflexive.

```lean
theorem isReflexive_of_exact_of_isReflexive_of_isTorsionFree
    {R : Type u} [CommRing R] [IsDomain R] [IsNoetherianRing R]
    {M : Type v} {M' : Type w} {M'' : Type x}
    [AddCommGroup M] [Module R M] [Module.Finite R M]
    [AddCommGroup M'] [Module R M'] [Module.Finite R M']
    [AddCommGroup M''] [Module R M''] [Module.Finite R M'']
    (f : M →ₗ[R] M') (g : M' →ₗ[R] M'')
    (hf : Function.Injective f) (hfg : Function.Exact f g)
    (hM' : Module.IsReflexive R M') (hM'' : Module.IsTorsionFree R M'') :
    Module.IsReflexive R M
```

## Tag 0AV2, a lemma

[Tag 0AV2](https://stacks.math.columbia.edu/tag/0AV2) in the Stacks Project.

**`isReflexive_iff_exists_finFree_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Reflexive.lean, line 526](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Reflexive.lean#L526).

> **Stacks Tag 0AV2.** A finite module over a Noetherian domain is reflexive if and only if it
> fits into a short exact sequence `0 → M → F → N → 0` with `F` finite free and `N`
> torsion-free.

```lean
theorem isReflexive_iff_exists_finFree_shortExact
    {R : Type u} [CommRing R] [IsDomain R] [IsNoetherianRing R]
    {M : Type v} [AddCommGroup M] [Module R M] [Module.Finite R M] :
    Module.IsReflexive R M ↔
      ∃ (n : ℕ) (N : Type u) (_ : AddCommGroup N) (_ : Module R N),
        Module.IsTorsionFree R N ∧
          ∃ (f : M →ₗ[R] (Fin n → R)) (g : (Fin n → R) →ₗ[R] N),
            Function.Injective f ∧ Function.Exact f g ∧ Function.Surjective g
```

## Tag 0EB9, a lemma

[Tag 0EB9](https://stacks.math.columbia.edu/tag/0EB9) in the Stacks Project.

**`isReflexive_baseChange_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Reflexive.lean, line 636](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Reflexive.lean#L636).

> **Stacks Tag 0EB9.** A finite reflexive module over a Noetherian domain remains reflexive
> after flat base change to a Noetherian domain. The base-changed module is automatically
> finite.

```lean
theorem isReflexive_baseChange_of_flat
    {R : Type u} {R' : Type v} [CommRing R] [CommRing R'] [Algebra R R']
    [IsDomain R] [IsDomain R'] [IsNoetherianRing R] [IsNoetherianRing R']
    [Module.Flat R R'] {M : Type w} [AddCommGroup M] [Module R M]
    [Module.Finite R M] [Module.IsReflexive R M] :
    Module.IsReflexive R' (TensorProduct R R' M)
```

## Tag 0AV3, a lemma

[Tag 0AV3](https://stacks.math.columbia.edu/tag/0AV3) in the Stacks Project.

**`isReflexive_linearMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Reflexive.lean, line 612](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Reflexive.lean#L612).

> **Stacks Tag 0AV3.** Over a Noetherian domain, the module of linear maps from a finite module
> into a finite reflexive module is reflexive.

```lean
theorem isReflexive_linearMap
    {R : Type u} [CommRing R] [IsDomain R] [IsNoetherianRing R]
    {M : Type v} [AddCommGroup M] [Module R M] [Module.Finite R M]
    {N : Type w} [AddCommGroup N] [Module R N] [Module.Finite R N]
    (hN : Module.IsReflexive R N) :
    Module.IsReflexive R (M →ₗ[R] N)
```

## Tag 0AV4, a definition

[Tag 0AV4](https://stacks.math.columbia.edu/tag/0AV4) in the Stacks Project.

**`Module.reflexiveHull`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Reflexive.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Reflexive.lean#L116).

> **Stacks Tag 0AV4.** The reflexive hull of an `R`-module `M` is its double dual
> `Hom_R(Hom_R(M, R), R)`.

```lean
abbrev Module.reflexiveHull (R : Type u) [CommSemiring R]
    (M : Type v) [AddCommMonoid M] [Module R M]
```

## Tag 0AV5, a lemma

[Tag 0AV5](https://stacks.math.columbia.edu/tag/0AV5) in the Stacks Project.

**`one_le_depth_and_two_le_depth_linearMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Reflexive.lean, line 730](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Reflexive.lean#L730).

> **Stacks Tag 0AV5.** If `M` and `N` are finite modules over a Noetherian local ring, then
> `Hom(M, N)` has depth at least one (respectively, at least two) whenever `N` does.

```lean
theorem one_le_depth_and_two_le_depth_linearMap
    {R : Type u} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    {M : Type v} [AddCommGroup M] [Module R M] [Module.Finite R M]
    {N : Type w} [AddCommGroup N] [Module R N] [Module.Finite R N] :
    ((1 : ℕ∞) ≤ Module.depth R (IsLocalRing.maximalIdeal R) N →
      (1 : ℕ∞) ≤ Module.depth R (IsLocalRing.maximalIdeal R) (M →ₗ[R] N)) ∧
    ((2 : ℕ∞) ≤ Module.depth R (IsLocalRing.maximalIdeal R) N →
      (2 : ℕ∞) ≤ Module.depth R (IsLocalRing.maximalIdeal R) (M →ₗ[R] N))
```

## Tag 0AV6, a lemma

[Tag 0AV6](https://stacks.math.columbia.edu/tag/0AV6) in the Stacks Project.

**`propertySk_linearMap_one_two_and_isTorsionFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Reflexive.lean, line 843](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Reflexive.lean#L843).

> **Stacks Tag 0AV6.** For finite modules `M` and `N` over a Noetherian ring, the module
> `Hom_R(M, N)` inherits `(S₁)` and `(S₂)` from `N`; if the ring is a domain, it also
> inherits the conjunction of torsion-freeness and `(S₂)`.

```lean
theorem propertySk_linearMap_one_two_and_isTorsionFree
    {R : Type u} [CommRing R] [IsNoetherianRing R]
    {M : Type v} [AddCommGroup M] [Module R M] [Module.Finite R M]
    {N : Type w} [AddCommGroup N] [Module R N] [Module.Finite R N] :
    (PropertySkModule R N 1 → PropertySkModule R (M →ₗ[R] N) 1) ∧
      (PropertySkModule R N 2 → PropertySkModule R (M →ₗ[R] N) 2) ∧
      (IsDomain R → Module.IsTorsionFree R N → PropertySkModule R N 2 →
        Module.IsTorsionFree R (M →ₗ[R] N) ∧ PropertySkModule R (M →ₗ[R] N) 2)
```

## Tag 0AV7, a lemma

[Tag 0AV7](https://stacks.math.columbia.edu/tag/0AV7) in the Stacks Project.

**`injective_of_injective_localized_at_associatedPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AssociatedPrime/Injective.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AssociatedPrime/Injective.lean#L42).

> Stacks Tag 0AV7. If for every prime ideal `p` of the Noetherian ring `R` either
> the localized map `φ_p : M_p → N_p` is injective or `p` is not an associated prime
> of `M`, then `φ : M → N` is injective.

```lean
theorem injective_of_injective_localized_at_associatedPrimes (φ : M →ₗ[R] N)
    (h : ∀ p : Ideal R, [p.IsPrime] →
      Function.Injective (LocalizedModule.map p.primeCompl φ) ∨ p ∉ associatedPrimes R M) :
    Function.Injective φ
```

## Tag 0AV8, a lemma

[Tag 0AV8](https://stacks.math.columbia.edu/tag/0AV8) in the Stacks Project.

**`bijective_of_bijective_localized_or_depth_two_and_notMem_associatedPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Reflexive.lean, line 1009](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Reflexive.lean#L1009).

> **Stacks Tag 0AV8.** A map from a finite module over a Noetherian ring is bijective if, at
> every prime, it is bijective after localization or the localized source has depth at least two
> and the prime is not associated to the target.

```lean
theorem bijective_of_bijective_localized_or_depth_two_and_notMem_associatedPrimes
    {R M N : Type*} [CommRing R] [IsNoetherianRing R]
    [AddCommGroup M] [Module R M] [Module.Finite R M]
    [AddCommGroup N] [Module R N] (φ : M →ₗ[R] N)
    (h : ∀ (p : Ideal R) (_ : p.IsPrime),
      Function.Bijective (LocalizedModule.map p.primeCompl φ) ∨
        2 ≤ Module.depth (Localization.AtPrime p)
          (IsLocalRing.maximalIdeal (Localization.AtPrime p))
          (LocalizedModule p.primeCompl M) ∧ p ∉ associatedPrimes R N) :
    Function.Bijective φ
```

## Tag 0AV9, a lemma

[Tag 0AV9](https://stacks.math.columbia.edu/tag/0AV9) in the Stacks Project.

**`bijective_of_bijective_localized_or_depth_two_of_isTorsionFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Reflexive.lean, line 1120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Reflexive.lean#L1120).

> **Stacks Tag 0AV9.** A map from a finite nonzero module to a torsion-free module over a
> Noetherian domain is bijective if, at every prime, either its localization is bijective or the
> localized source has depth at least two.

```lean
theorem bijective_of_bijective_localized_or_depth_two_of_isTorsionFree
    {R M N : Type*} [CommRing R] [IsDomain R] [IsNoetherianRing R]
    [AddCommGroup M] [Module R M] [Module.Finite R M] [Nontrivial M]
    [AddCommGroup N] [Module R N] [Module.IsTorsionFree R N]
    (φ : M →ₗ[R] N)
    (h : ∀ (p : Ideal R) (_ : p.IsPrime),
      Function.Bijective (LocalizedModule.map p.primeCompl φ) ∨
        2 ≤ Module.depth (Localization.AtPrime p)
          (IsLocalRing.maximalIdeal (Localization.AtPrime p))
          (LocalizedModule p.primeCompl M)) :
    Function.Bijective φ
```

## Tag 0AVA, a lemma

[Tag 0AVA](https://stacks.math.columbia.edu/tag/0AVA) in the Stacks Project.

**`isReflexive_iff_localized_isReflexive_or_depth_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Reflexive.lean, line 1177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Reflexive.lean#L1177).

> **Stacks Tag 0AVA.** A finite module over a Noetherian domain is reflexive if and only if, at
> every prime, its localization is reflexive or has depth at least two.

```lean
theorem isReflexive_iff_localized_isReflexive_or_depth_two
    {R : Type u} [CommRing R] [IsDomain R] [IsNoetherianRing R]
    {M : Type v} [AddCommGroup M] [Module R M] [Module.Finite R M] :
    Module.IsReflexive R M ↔
      ∀ (p : Ideal R) [p.IsPrime],
        Module.IsReflexive (Localization.AtPrime p) (LocalizedModule p.primeCompl M) ∨
          2 ≤ Module.depth (Localization.AtPrime p)
            (IsLocalRing.maximalIdeal (Localization.AtPrime p))
            (LocalizedModule p.primeCompl M)
```

## Tag 0EBA, a lemma

[Tag 0EBA](https://stacks.math.columbia.edu/tag/0EBA) in the Stacks Project.

**`depth_localized_ge_two_and_propertyS2_of_isReflexive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Reflexive.lean, line 868](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Reflexive.lean#L868).

> **Stacks Tag 0EBA.** A finite reflexive module over a Noetherian commutative ring has depth at
> least two at a prime whenever the localized ring does, and inherits Serre's condition `(S₂)`
> from the ring.

```lean
theorem depth_localized_ge_two_and_propertyS2_of_isReflexive
    {R : Type u} [CommRing R] [IsNoetherianRing R]
    {M : Type v} [AddCommGroup M] [Module R M] [Module.Finite R M]
    [Module.IsReflexive R M] (p : Ideal R) [p.IsPrime] :
    ((2 : ℕ∞) ≤
        Module.depth (Localization.AtPrime p)
          (IsLocalRing.maximalIdeal (Localization.AtPrime p)) (Localization.AtPrime p) →
      (2 : ℕ∞) ≤
        Module.depth (Localization.AtPrime p)
          (IsLocalRing.maximalIdeal (Localization.AtPrime p)) (LocalizedModule.AtPrime p M)) ∧
      (PropertySkRing R 2 → PropertySkModule R M 2)
```

## Tag 0EBB, an example

[Tag 0EBB](https://stacks.math.columbia.edu/tag/0EBB) in the Stacks Project.

**`mvPolynomial_adjoin_reflexive_propertyS2_module_not_propertyS2`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Reflexive.lean, line 2811](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Reflexive.lean#L2811).

> **Stacks Tag 0EBB.** The subalgebra `R = k[1, y, x², xy, x³]` of `k[x, y]` is a
> Noetherian domain which is not `(S₂)`.  Both `R` and `k[x, y]` are reflexive as
> `R`-modules, while `k[x, y]` is `(S₂)`.  Moreover, if
> `m = (y, x², xy, x³)`, then the two successive `R`-duals of `k[x, y]` are `m`
> and `k[x, y]`, respectively.

```lean
theorem mvPolynomial_adjoin_reflexive_propertyS2_module_not_propertyS2
    (k : Type u) [Field k] :
    let P := MvPolynomial (Fin 2) k
    let x : P := MvPolynomial.X 0
    let y : P := MvPolynomial.X 1
    let R : Subalgebra k P := Algebra.adjoin k {1, y, x ^ 2, x * y, x ^ 3}
    let m : Ideal R := Ideal.span {r | (r : P) ∈ ({y, x ^ 2, x * y, x ^ 3} : Set P)}
    ∃ (_ : IsNoetherianRing R) (_ : IsDomain R) (_ : Module.Finite R P),
      ∃ (dualPToM : Module.Dual R P ≃ₗ[R] m) (dualMToP : Module.Dual R m ≃ₗ[R] P),
        ¬ PropertySkRing R 2 ∧
          Module.IsReflexive R R ∧
          ¬ PropertySkModule R R 2 ∧
          (∀ (f : Module.Dual R P) (q : P),
            (↑(↑(dualPToM f) : R) : P) * q = (↑(f q) : P)) ∧
          (∀ (g : Module.Dual R m) (a : m),
            (↑(g a) : P) = dualMToP g * (↑(↑a : R) : P)) ∧
          Module.IsReflexive R P ∧
          PropertySkModule R P 2
```

## Tag 0AVB, a lemma

[Tag 0AVB](https://stacks.math.columbia.edu/tag/0AVB) in the Stacks Project.

**`isReflexive_isTorsionFree_propertyS2_intersection_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Reflexive.lean, line 1418](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Reflexive.lean#L1418). References: EGA 0 (23.2.9), “special case”; EGA IV (7.8.3), “(viii), special case”.

> **Stacks Tag 0AVB.** Let `R` be a Noetherian normal domain and `M` a finite `R`-module. The
> following are equivalent: `M` is reflexive; `M` is torsion-free and satisfies `(S₂)`; and `M` is
> torsion-free and equals the intersection of its localizations at the height-one primes inside
> its generic fibre.

```lean
theorem isReflexive_isTorsionFree_propertyS2_intersection_tfae
    {R : Type u} [CommRing R] [IsDomain R] [IsNoetherianRing R] [IsIntegrallyClosed R]
    {M : Type v} [AddCommGroup M] [Module R M] [Module.Finite R M] :
    List.TFAE [
      Module.IsReflexive R M,
      Module.IsTorsionFree R M ∧ PropertySkModule R M 2,
      Module.IsTorsionFree R M ∧
        ∀ x : LocalizedModule (nonZeroDivisors R) M,
          x ∈ LinearMap.range (LocalizedModule.mkLinearMap (nonZeroDivisors R) M) ↔
            ∀ (p : Ideal R) (_ : p.IsPrime), p.height = 1 →
              ∃ (m : M) (s : R), s ∉ p ∧
                s • x = LocalizedModule.mkLinearMap (nonZeroDivisors R) M m]
```

## Tag 0AVC, a lemma

[Tag 0AVC](https://stacks.math.columbia.edu/tag/0AVC) in the Stacks Project.

**`reflexiveHull_eq_iInf_localization_mod_torsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Reflexive.lean, line 1597](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Reflexive.lean#L1597). References: EGA 0 (23.2.9), “special case”.

> **Stacks Tag 0AVC.** Let `R` be a Noetherian normal domain and `M` a finite `R`-module. Inside
> the generic fibre, the reflexive hull `M⁎⁎` is the intersection over height-one primes `p` of
> `M_p / (M_p)_tors`, and this is also the intersection of `(M / M_tors)_p`.
>
> Membership in the three submodules is written elementwise, with the first condition using the
> canonical localization of the evaluation map `M → M⁎⁎`.

```lean
theorem reflexiveHull_eq_iInf_localization_mod_torsion
    {R : Type u} [CommRing R] [IsDomain R] [IsNoetherianRing R] [IsIntegrallyClosed R]
    {M : Type v} [AddCommGroup M] [Module R M] [Module.Finite R M] :
    ∀ x : LocalizedModule (nonZeroDivisors R) M,
      (((IsLocalizedModule.map (nonZeroDivisors R)
          (LocalizedModule.mkLinearMap (nonZeroDivisors R) M)
          (LocalizedModule.mkLinearMap (nonZeroDivisors R)
            (Module.Dual R (Module.Dual R M)))
          (Module.Dual.eval R M)) x ∈
            LinearMap.range (LocalizedModule.mkLinearMap (nonZeroDivisors R)
              (Module.Dual R (Module.Dual R M)))) ↔
        ∀ (p : Ideal R) (_ : p.IsPrime), p.height = 1 →
          ∃ (m : M) (s : R), s ∉ p ∧
            s • x = LocalizedModule.mkLinearMap (nonZeroDivisors R) M m) ∧
      ((∀ (p : Ideal R) (_ : p.IsPrime), p.height = 1 →
          ∃ (m : M) (s : R), s ∉ p ∧
            s • x = LocalizedModule.mkLinearMap (nonZeroDivisors R) M m) ↔
        ∀ (p : Ideal R) (_ : p.IsPrime), p.height = 1 →
          ∃ (q : M ⧸ Submodule.torsion R M) (s : R), s ∉ p ∧
            s • x = Module.torsionQuotientToGenericFiber R M q)
```

## Tag 0BM4, a lemma

[Tag 0BM4](https://stacks.math.columbia.edu/tag/0BM4) in the Stacks Project.

**`integralClosure_isReflexive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Reflexive.lean, line 1657](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Reflexive.lean#L1657).

> **Stacks Tag 0BM4.** If `A` is a Noetherian normal domain, `K` is its fraction field, and `L`
> is a finite extension of `K`, then a module-finite integral closure of `A` in `L` is reflexive as
> an `A`-module.

```lean
theorem integralClosure_isReflexive
    (A : Type u) [CommRing A] [IsDomain A] [IsNoetherianRing A] [IsIntegrallyClosed A]
    (K : Type v) [Field K] [Algebra A K] [IsFractionRing A K]
    (L : Type w) [Field L] [Algebra A L] [Algebra K L] [IsScalarTower A K L]
    [FiniteDimensional K L] (hB : Module.Finite A (integralClosure A L)) :
    Module.IsReflexive A (integralClosure A L)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.24, Tag 0AUY](https://stacks.math.columbia.edu/tag/0AUY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
