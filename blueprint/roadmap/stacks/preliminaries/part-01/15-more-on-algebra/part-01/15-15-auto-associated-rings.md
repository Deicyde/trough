---
declaration: section
origin: cited
lean: IsAutoAssociated, annihilator_ne_bot_of_isAutoAssociated, universallyInjective_iff_injective_of_projective, annihilator_projective_splitting_tfae, exists_universallyInjective_nonSplit_freeModule_endomorphism, Stacks.DeterminantalRank.injective_iff_rank_eq_and_annihilator_eq_bot, Stacks.DeterminantalRank.injective_iff_rank_eq_and_contains_nonZeroDivisor, subsingleton_dual_quotient_range_of_injective
statement: formalized
proof: formalized
---

# 15.15 Auto-associated rings

Section 15.15 of the Stacks Project, [Tag 05GL](https://stacks.math.columbia.edu/tag/05GL). 7 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05GM, a definition

[Tag 05GM](https://stacks.math.columbia.edu/tag/05GM) in the Stacks Project.

**`IsAutoAssociated`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AutoAssociated.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AutoAssociated.lean#L52).

> **Stacks 05GM.** A commutative ring is *auto-associated* if it is local and its maximal
> ideal is weakly associated to the ring as a module over itself.

```lean
def IsAutoAssociated (R : Type u) [CommRing R] : Prop
```

## Tag 05GN, a lemma

[Tag 05GN](https://stacks.math.columbia.edu/tag/05GN) in the Stacks Project.

**`annihilator_ne_bot_of_isAutoAssociated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AutoAssociated.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AutoAssociated.lean#L59).

> **Stacks 05GN.** Every proper finitely generated ideal in an auto-associated ring has a
> nonzero annihilator.

```lean
theorem annihilator_ne_bot_of_isAutoAssociated {R : Type u} [CommRing R]
    (hR : IsAutoAssociated R) (I : Ideal R) (hI : I.FG) (hI_ne : I ≠ ⊤) :
    I.annihilator ≠ ⊥
```

## Tag 05GP, a lemma

[Tag 05GP](https://stacks.math.columbia.edu/tag/05GP) in the Stacks Project.

**`universallyInjective_iff_injective_of_projective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AutoAssociated.lean, line 316](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AutoAssociated.lean#L316).

> **Stacks 05GP.** Over a ring in which every proper finitely generated ideal has a nonzero
> annihilator, a homomorphism between projective modules is universally injective if and only if it
> is injective.

```lean
theorem universallyInjective_iff_injective_of_projective
    {R : Type u} [CommRing R]
    (hR : ∀ I : Ideal R, I.FG → I ≠ ⊤ → I.annihilator ≠ ⊥)
    {N M : Type v} [AddCommGroup N] [Module R N] [Module.Projective R N]
    [AddCommGroup M] [Module R M] [Module.Projective R M] (f : N →ₗ[R] M) :
    UniversallyInjective f ↔ Function.Injective f
```

## Tag 05GQ, a lemma

[Tag 05GQ](https://stacks.math.columbia.edu/tag/05GQ) in the Stacks Project.

**`annihilator_projective_splitting_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AutoAssociated.lean, line 409](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AutoAssociated.lean#L409).

> **Stacks 05GQ.** For a commutative ring `R`, the following are equivalent: every proper
> finitely generated ideal has a nonzero annihilator; every injection between projective modules is
> universally injective; the cokernel of every injection between finite projective modules is finite
> projective; every finite projective submodule of a finite projective module is a direct summand;
> and every injection from `R` to a finite-rank free module splits. The quantified module universe
> contains the ring universe, so the finite free modules in the last condition can be lifted into
> the preceding conditions.

```lean
theorem annihilator_projective_splitting_tfae {R : Type u} [CommRing R] :
    [ (∀ I : Ideal R, I.FG → I ≠ ⊤ → I.annihilator ≠ ⊥),
      (∀ (N M : Type (max u v)) [AddCommGroup N] [Module R N] [Module.Projective R N]
        [AddCommGroup M] [Module R M] [Module.Projective R M] (f : N →ₗ[R] M),
        Function.Injective f → UniversallyInjective f),
      (∀ (N M : Type (max u v)) [AddCommGroup N] [Module R N] [Module.Finite R N]
        [Module.Projective R N] [AddCommGroup M] [Module R M] [Module.Finite R M]
        [Module.Projective R M] (f : N →ₗ[R] M), Function.Injective f →
        Module.Finite R (M ⧸ LinearMap.range f) ∧ Module.Projective R (M ⧸ LinearMap.range f)),
      (∀ (M : Type (max u v)) [AddCommGroup M] [Module R M] [Module.Finite R M]
        [Module.Projective R M] (N : Submodule R M) [Module.Finite R N]
        [Module.Projective R N], ∃ p : M →ₗ[R] N, p.comp N.subtype = LinearMap.id),
      (∀ (n : ℕ) (f : R →ₗ[R] (Fin n → R)), Function.Injective f →
        ∃ p : (Fin n → R) →ₗ[R] R, p.comp f = LinearMap.id) ].TFAE
```

## Tag 05GR, an example

[Tag 05GR](https://stacks.math.columbia.edu/tag/05GR) in the Stacks Project.

**`exists_universallyInjective_nonSplit_freeModule_endomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AutoAssociated.lean, line 833](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AutoAssociated.lean#L833).

> **Stacks 05GR.** Let `R = k[x₁, x₂, …]/(xᵢ²)`. The endomorphism of the countable free
> `R`-module given on basis vectors by `eᵢ ↦ eᵢ - xᵢ eᵢ₊₁` is injective and universally
> injective, but is neither surjective nor split. After specializing every variable to zero it
> becomes an isomorphism. Its cokernel is countably generated and flat, but is not projective and
> not Mittag--Leffler. The ring `R` is auto-associated and satisfies the annihilator condition of
> Stacks 05GQ.

```lean
theorem exists_universallyInjective_nonSplit_freeModule_endomorphism
    (k : Type u) [Field k] :
    let P := MvPolynomial ℕ k
    let I : Ideal P := Ideal.span (Set.range (fun i : ℕ ↦ MvPolynomial.X i ^ 2))
    let R := P ⧸ I
    let x : ℕ → R := fun i ↦ Ideal.Quotient.mk I (MvPolynomial.X i)
    ∃ ν : (ℕ →₀ R) →ₗ[R] (ℕ →₀ R),
      (∀ i, ν (Finsupp.single i 1) =
        Finsupp.single i 1 - x i • Finsupp.single (i + 1) 1) ∧
      (∀ n : ℕ, LinearIndependent R (fun i : Fin n ↦ ν (Finsupp.single i 1))) ∧
      IsAutoAssociated R ∧
      (∀ J : Ideal R, J.FG → J ≠ ⊤ → J.annihilator ≠ ⊥) ∧
      Function.Injective ν ∧
      UniversallyInjective ν ∧
      (∃ ε : R →ₐ[k] k, (∀ i, ε (x i) = 0) ∧
        letI := ε.toRingHom.toAlgebra
        Function.Bijective (ν.rTensor k)) ∧
      ¬ Function.Surjective ν ∧
      ¬ (∃ p : (ℕ →₀ R) →ₗ[R] (ℕ →₀ R), p.comp ν = LinearMap.id) ∧
      Module.Flat R ((ℕ →₀ R) ⧸ LinearMap.range ν) ∧
      Module.CountablyGenerated R ((ℕ →₀ R) ⧸ LinearMap.range ν) ∧
      ¬ Module.Projective R ((ℕ →₀ R) ⧸ LinearMap.range ν) ∧
      ¬ IsMittagLeffler.{u, u, u, u, u} R ((ℕ →₀ R) ⧸ LinearMap.range ν)
```

## Tag 00MX, a lemma

[Tag 00MX](https://stacks.math.columbia.edu/tag/00MX) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.DeterminantalRank.injective_iff_rank_eq_and_annihilator_eq_bot`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/Matrix/DeterminantalRank/ExteriorRank.lean#L561), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/AutoAssociated.lean, line 953](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AutoAssociated.lean#L953) (StacksFrontier): “(1) iff (2)”.
- [`Stacks.DeterminantalRank.injective_iff_rank_eq_and_contains_nonZeroDivisor`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/Matrix/DeterminantalRank/ExteriorRank.lean#L622), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/AutoAssociated.lean, line 955](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AutoAssociated.lean#L955) (StacksFrontier): “(1) iff (3)”.

## Tag 0EWY, a lemma

[Tag 0EWY](https://stacks.math.columbia.edu/tag/0EWY) in the Stacks Project.

**`subsingleton_dual_quotient_range_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AutoAssociated.lean, line 936](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AutoAssociated.lean#L936).

> **Stacks 0EWY.** The dual of the cokernel of an injective endomorphism of a finite free
> module is zero.

```lean
theorem subsingleton_dual_quotient_range_of_injective
    {R : Type u} [CommRing R]
    {M : Type v} [AddCommGroup M] [Module R M] [Module.Free R M] [Module.Finite R M]
    (φ : M →ₗ[R] M) (hφ : Function.Injective φ) :
    Subsingleton (Module.Dual R (M ⧸ LinearMap.range φ))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.15, Tag 05GL](https://stacks.math.columbia.edu/tag/05GL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
