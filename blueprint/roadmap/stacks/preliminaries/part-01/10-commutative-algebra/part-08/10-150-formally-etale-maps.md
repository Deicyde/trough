---
declaration: section
origin: cited
lean: Algebra.FormallyEtale.instTensorProduct, Algebra.existsUnique_lift_iff_finitePresentation_and_subsingleton, Algebra.FormallyEtale.colimit, Algebra.FormallyEtale.of_isLocalization, FormallyEtaleH1D.quotMap_bijective, FormallyEtaleH1D.grMap_bijective, KaehlerDifferential.isBaseChange_quotient_ideal_pow_of_formallyEtale, LinearMap.IsUniversalDifferentialOperatorOfOrderLE.baseChange_of_formallyEtale
statement: formalized
proof: formalized
---

# 10.150 Formally étale maps

Section 10.150 of the Stacks Project, [Tag 00UP](https://stacks.math.columbia.edu/tag/00UP). 7 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H92, a lemma

[Tag 0H92](https://stacks.math.columbia.edu/tag/0H92) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.FormallyEtale.instTensorProduct`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.FormallyEtale.instTensorProduct#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L258) (StacksFrontier). References: SGA 3 VIIB (1.6), “discrete base change”; SGA 3 VIIB (1.6.B), “(a)⇒(c), discrete case”; SGA 3 VIIB (1.6.C), “special case”.

## Tag 00UR, a lemma

[Tag 00UR](https://stacks.math.columbia.edu/tag/00UR) in the Stacks Project.

**`Algebra.existsUnique_lift_iff_finitePresentation_and_subsingleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean#L141). The attribute's comment: “Formally étale (1) is the unique-lifting property of Definition 00UQ, stated for test rings `A` in the universe `max u v` of `R` and `S` (`Ideal.Quotient.mkₐ R I` is `A → A ⧸ I`; an `R`-algebra map `g` makes the lower triangle commute). Étale (2) is Definition 00U1 verbatim: finite presentation, and `NL_{S/R}` quasi-isomorphic to zero, which the source spells out as `H₁(NL_{S/R}) = 0` (`Algebra.H1Cotangent R S`) and `Ω_{S/R} = 0`.”.

> Let `R → S` be a ring map of finite presentation. Then `S` is formally étale over `R` in the
> sense of unique infinitesimal lifting (for every `R`-algebra `A`, every ideal `I ⊆ A` with
> `I ^ 2 = 0` and every `R`-algebra map `f : S → A ⧸ I` there is exactly one `R`-algebra map
> `g : S → A` with `A → A ⧸ I` composed with `g` equal to `f`) if and only if `R → S` is étale: of
> finite presentation with `H₁(NL_{S/R}) = 0` and `Ω_{S/R} = 0`.

```lean
theorem Algebra.existsUnique_lift_iff_finitePresentation_and_subsingleton.{u, v}
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S]
    (hfp : Algebra.FinitePresentation R S) :
    (∀ ⦃A : Type (max u v)⦄ [CommRing A] [Algebra R A] (I : Ideal A), I ^ 2 = ⊥ →
        ∀ f : S →ₐ[R] A ⧸ I, ∃! g : S →ₐ[R] A, (Ideal.Quotient.mkₐ R I).comp g = f) ↔
      Algebra.FinitePresentation R S ∧ Subsingleton (Algebra.H1Cotangent R S) ∧
        Subsingleton Ω[S⁄R]
```

## Tag 031N, a lemma

[Tag 031N](https://stacks.math.columbia.edu/tag/031N) in the Stacks Project.

**`Algebra.FormallyEtale.colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean#L180).

> Let `R` be a commutative ring and let `ι` be a directed set, a nonempty preorder in which
> every pair has an upper bound. Let `F : ι ⥤ CommAlgCat R` be a directed system of `R`-algebras
> over `ι`, the family `S_i = F.obj i` with the transition maps encoded by functoriality. If every
> `S_i` is formally étale over `R`, then the colimit `S = colim_i S_i` is formally étale over
> `R`.

```lean
theorem Algebra.FormallyEtale.colimit
    (R : Type) [CommRing R]
    (ι : Type) [Preorder ι] [Nonempty ι] [IsDirected ι (· ≤ ·)]
    (F : ι ⥤ CommAlgCat.{0} R)
    (h : ∀ i : ι, Algebra.FormallyEtale R (F.obj i)) :
    Algebra.FormallyEtale R (colimit F : CommAlgCat R)
```

## Tag 04EG, a lemma

[Tag 04EG](https://stacks.math.columbia.edu/tag/04EG) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.FormallyEtale.of_isLocalization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.FormallyEtale.of_isLocalization#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/Basic/FirstProperties.lean#L157) (StacksFrontier): “For a multiplicative subset `M ⊆ R` the ring map `R → M⁻¹R` is formally étale, stated for an arbitrary ring `Rₘ` realising the localization rather than for a chosen model.”. References: EGA 0 (19.10.3).

## Tag 0H1D, a lemma

[Tag 0H1D](https://stacks.math.columbia.edu/tag/0H1D) in the Stacks Project.

**`FormallyEtaleH1D.quotMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/AssociatedGraded.lean, line 336](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/AssociatedGraded.lean#L336). The attribute's comment: “(1)”.

> If `φ : R → S` is formally étale and `R → S/J` is surjective, with `I = ker(R → S/J)`, then
> for every `n ≥ 1` the canonical map `φ̄ₙ : R/I^n → S/J^n` is bijective.

```lean
theorem quotMap_bijective
    (hφ : RingHom.FormallyEtale φ)
    (hsurj : Function.Surjective ((Ideal.Quotient.mk J).comp φ))
    (n : ℕ) (hn : 1 ≤ n) :
    Function.Bijective (quotMap φ J n)
```

**`FormallyEtaleH1D.grMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/AssociatedGraded.lean, line 349](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/AssociatedGraded.lean#L349). The attribute's comment: “(2)”.

> If `φ : R → S` is formally étale and `R → S/J` is surjective, with `I = ker(R → S/J)`, then
> the induced map of associated graded rings `gr(φ) : ⊕_n I^n/I^{n+1} → ⊕_n J^n/J^{n+1}` is an
> isomorphism: for every `n` its degree-`n` component `I^n/I^{n+1} → J^n/J^{n+1}` is bijective.

```lean
theorem grMap_bijective
    (hφ : RingHom.FormallyEtale φ)
    (hsurj : Function.Surjective ((Ideal.Quotient.mk J).comp φ))
    (n : ℕ) :
    Function.Bijective (grMap φ J n)
```

## Tag 0H93, a lemma

[Tag 0H93](https://stacks.math.columbia.edu/tag/0H93) in the Stacks Project.

**`KaehlerDifferential.isBaseChange_quotient_ideal_pow_of_formallyEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/Basic/DiagonalIdeal.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/Basic/DiagonalIdeal.lean#L380). The attribute's comment: “Stated for an arbitrary exponent `n` in place of the source's `k + 1`, and in Mathlib's `IsBaseChange` form; the map is the hypothesis `hφ`, which pins it. The source's final assertion, that `S' ⊗_S Ω[S⁄R] → Ω[S'⁄R]` is an isomorphism, is `KaehlerDifferential.isBaseChange_of_formallyEtale`. See the module docstring.”. References: EGA IV (17.2.4), “affine case”.

> Let `R → S → S'` be ring maps and let `J`, resp. `J'`, be the kernel of the
> multiplication map `S ⊗[R] S → S`, resp. `S' ⊗[R] S' → S'`. If `S → S'` is formally étale, then
> the canonical ring map `(S ⊗[R] S) ⧸ J ^ n → (S' ⊗[R] S') ⧸ (J') ^ n`, i.e. the unique one sending
> the class of `a ⊗ₜ b` to the class of `a ⊗ₜ b`, exhibits its target as the base change of its
> source along `S → S'`:
> `S' ⊗_S ((S ⊗[R] S) ⧸ J ^ n) = (S' ⊗[R] S') ⧸ (J') ^ n`.

```lean
theorem isBaseChange_quotient_ideal_pow_of_formallyEtale [Algebra.FormallyEtale S S']
    (n : ℕ)
    (φ : ((S ⊗[R] S) ⧸ KaehlerDifferential.ideal R S ^ n) →ₐ[S]
      ((S' ⊗[R] S') ⧸ KaehlerDifferential.ideal R S' ^ n))
    (hφ : ∀ a b : S, φ (Ideal.Quotient.mk _ (a ⊗ₜ[R] b)) =
      Ideal.Quotient.mk _ (algebraMap S S' a ⊗ₜ[R] algebraMap S S' b)) :
    IsBaseChange S' φ.toLinearMap
```

## Tag 0H94, a lemma

[Tag 0H94](https://stacks.math.columbia.edu/tag/0H94) in the Stacks Project.

**`LinearMap.IsUniversalDifferentialOperatorOfOrderLE.baseChange_of_formallyEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/Basic/PrincipalParts.lean, line 825](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/Basic/PrincipalParts.lean#L825). The attribute's comment: “The identification `S' ⊗_S Pᵏ_{S/R}(M) = Pᵏ_{S'/R}(M')` is stated in Mathlib's `IsBaseChange` form, for an arbitrary base change `f : M → M'` and arbitrary modules of principal parts on both sides (Definition 09CL, constructed in 09CK), via the unique map compatible with the universal differential operators. The extension is unique among differential operators of any finite order and has the order of `E`. The source writes `M' = S' ⊗_R M`, a slip for `S' ⊗_S M`.”.

> Let `R → S → S'` be ring maps with `S → S'` formally étale (for example étale). Let `M` be an
> `S`-module and `M' = S' ⊗[S] M`, given as a base change `f : M → M'`. Let `(P, D)` and `(P', D')`
> be modules of principal parts of order `k` of `M` over `R → S` and of `M'` over `R → S'`. Then
> `S' ⊗[S] Pᵏ_{S/R}(M) = Pᵏ_{S'/R}(M')`: the unique `S`-linear `g : P → P'` with `g ∘ D = D' ∘ f`
> exhibits `P'` as the base change of `P`. Moreover, for any `S`-module `N`, every differential
> operator `E : M → N` of finite order `l` has a unique extension `E' : M' → S' ⊗[S] N` to a
> differential operator, which has order at most `l`.

```lean
theorem baseChange_of_formallyEtale [Algebra.FormallyEtale S S'] (k : ℕ)
    {D : M →ₗ[R] P} (hD : D.IsUniversalDifferentialOperatorOfOrderLE S k)
    {D' : M' →ₗ[R] P'} (hD' : D'.IsUniversalDifferentialOperatorOfOrderLE S' k)
    (f : M →ₗ[S] M') (hf : IsBaseChange S' f) (N : Type*) [AddCommGroup N] [Module R N]
    [Module S N] [IsScalarTower R S N] :
    (∃ g : P →ₗ[S] P', (∀ m : M, g (D m) = D' (f m)) ∧ IsBaseChange S' g ∧
      ∀ g' : P →ₗ[S] P', (∀ m : M, g' (D m) = D' (f m)) → g' = g) ∧
    ∀ (l : ℕ) (E : M →ₗ[R] N), E.IsDifferentialOperatorOfOrderLE S l →
      ∃ E' : M' →ₗ[R] S' ⊗[S] N, E'.IsDifferentialOperatorOfOrderLE S' l ∧
        (∀ m : M, E' (f m) = (1 : S') ⊗ₜ[S] E m) ∧
        ∀ (j : ℕ) (E'' : M' →ₗ[R] S' ⊗[S] N), E''.IsDifferentialOperatorOfOrderLE S' j →
          (∀ m : M, E'' (f m) = (1 : S') ⊗ₜ[S] E m) → E'' = E'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.150, Tag 00UP](https://stacks.math.columbia.edu/tag/00UP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
