---
declaration: section
origin: cited
lean: AdicCompletion.universallyInjective_directSumToPi, AdicCompletion.flat_directSum, tor_pro_zero, flat_limit_and_tensor_limit_of_flat_quotients, AdicCompletion.isNoetherianRing_and_flat_of_flat_quotient
statement: formalized
proof: formalized
---

# 15.28 Completion and flatness

Section 15.28 of the Stacks Project, [Tag 06LD](https://stacks.math.columbia.edu/tag/06LD). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05BC, a lemma

[Tag 05BC](https://stacks.math.columbia.edu/tag/05BC) in the Stacks Project.

**`AdicCompletion.universallyInjective_directSumToPi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/Flat/DirectSumToPi.lean, line 415](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Flat/DirectSumToPi.lean#L415).

> Let `R` be a Noetherian ring that is `I`-adically complete. Then the canonical map
> `(⊕_{α ∈ A} R)^∧ → ∏_{α ∈ A} R` from the `I`-adic completion of a direct sum of copies of `R`
> into the product of copies of `R` is universally injective.

```lean
theorem AdicCompletion.universallyInjective_directSumToPi
    (R : Type u) [CommRing R] (I : Ideal R) (A : Type v)
    [IsNoetherianRing R] [IsAdicComplete I R] :
    UniversallyInjective (AdicCompletion.directSumToPi R I A)
```

## Tag 06LE, a lemma

[Tag 06LE](https://stacks.math.columbia.edu/tag/06LE) in the Stacks Project.

**`AdicCompletion.flat_directSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/Flat/FlatCompletion.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Flat/FlatCompletion.lean#L202). References: EGA 0 (7.3.3), “more general”; SGA 1 IV (3.1), “more general”.

> For a Noetherian ring `R` and an ideal `I`, the `I`-adic completion `(⊕_{α ∈ A} R)^∧` of an
> arbitrary direct sum of copies of `R` is a flat `R`-module.

```lean
theorem AdicCompletion.flat_directSum
    (R : Type u) [CommRing R] (I : Ideal R) (A : Type v) [IsNoetherianRing R] :
    Module.Flat R (AdicCompletion I (DirectSum A (fun _ : A => R)))
```

## Tag 0911, a lemma

[Tag 0911](https://stacks.math.columbia.edu/tag/0911) in the Stacks Project.

**`tor_pro_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/ProZero.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/ProZero.lean#L204).

> Let `A` be a Noetherian ring, `I ⊆ A` an ideal, and `M` a finite `A`-module. Then for every
> `p > 0` there exists `c > 0` such that, for all `n ≥ c`, the map
> `Tor_p^A(M, A/I^n) → Tor_p^A(M, A/I^{n-c})` induced by the canonical surjection
> `A/I^n ↠ A/I^{n-c}` is the zero map.

```lean
theorem tor_pro_zero
    [IsNoetherianRing A]
    (M : ModuleCat A) [Module.Finite A M]
    {p : ℕ} (hp : 0 < p) :
    ∃ c : ℕ, 0 < c ∧ ∀ n : ℕ, c ≤ n →
      ((Tor (ModuleCat A) p).obj M).map
        (torProZeroTransition I (Nat.sub_le n c)) = 0
```

## Tag 0912, a lemma

[Tag 0912](https://stacks.math.columbia.edu/tag/0912) in the Stacks Project.

**`flat_limit_and_tensor_limit_of_flat_quotients`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/Flat/TensorLimit.lean, line 364](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Flat/TensorLimit.lean#L364).

> Let `A` be a Noetherian ring and `I ⊆ A` an ideal. Let `(M_n)` be an inverse system of
> `A`-modules such that each `M_n` is flat over `A ⧸ Iⁿ` (compatibly with its `A`-module structure)
> and each transition map `M_{n+1} → M_n` is surjective. Then `M = lim M_n` is flat over `A`, and
> for every finite `A`-module `Q` the canonical comparison map `Q ⊗_A lim M_n → lim (Q ⊗_A M_n)` is
> an isomorphism.

```lean
theorem flat_limit_and_tensor_limit_of_flat_quotients
    {A : Type u} [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    (M : ℕᵒᵖ ⥤ ModuleCat.{u} A)
    (quotientModule : ∀ n : ℕ, Module (A ⧸ I ^ n) (M.obj (.op n)))
    (hscalar : ∀ n : ℕ, letI := quotientModule n
      IsScalarTower A (A ⧸ I ^ n) (M.obj (.op n)))
    (hflat : ∀ n : ℕ, letI := quotientModule n
      Module.Flat (A ⧸ I ^ n) (M.obj (.op n)))
    (hsurjective : ∀ n : ℕ, Function.Surjective
      (M.map (homOfLE (Nat.le_succ n)).op)) :
    Module.Flat A (limit M : ModuleCat.{u} A) ∧
      ∀ (Q : ModuleCat.{u} A), Module.Finite A Q →
        IsIso (limit.post M
          ((MonoidalCategory.tensoringLeft (ModuleCat.{u} A)).obj Q))
```

## Tag 0AGW, a lemma

[Tag 0AGW](https://stacks.math.columbia.edu/tag/0AGW) in the Stacks Project.

**`AdicCompletion.isNoetherianRing_and_flat_of_flat_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/Flat/FlatCompletion.lean, line 489](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Flat/FlatCompletion.lean#L489). References: EGA 0 (10.2.3), “forward implication”.

> Let `R` be a commutative ring, `I ⊆ R` a finitely generated ideal and `M` an `R`-module. If
> `R/I` is Noetherian, `M/IM` is flat over `R/I` and `Tor₁ᴿ(M, R/I) = 0`, then the `I`-adic
> completion `R^∧` is a Noetherian ring and the `I`-adic completion `M^∧` is flat over `R^∧`.

```lean
theorem AdicCompletion.isNoetherianRing_and_flat_of_flat_quotient
    {R : Type u} {M : Type v} [CommRing R] [AddCommGroup M] [Module R M]
    (I : Ideal R) (hI : I.FG) (hRI : IsNoetherianRing (R ⧸ I))
    (hflat : Module.Flat (R ⧸ I) (M ⧸ (I • (⊤ : Submodule R M))))
    (htor : IsZero
      (((Tor (ModuleCat.{max u v} (ULift.{v} R)) 1).obj
        (ModuleCat.of (ULift.{v} R) (ULift.{u} M))).obj
        (ModuleCat.of (ULift.{v} R) (ULift.{v} (R ⧸ I))))) :
    IsNoetherianRing (AdicCompletion I R) ∧
      Module.Flat (AdicCompletion I R) (AdicCompletion I M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.28, Tag 06LD](https://stacks.math.columbia.edu/tag/06LD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
