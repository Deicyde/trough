---
declaration: section
origin: cited
lean: eilenberg_swindle, exists_free_prod_of_projective, exists_finite_free_summand_containing_zero_prod, exists_mem_add_unimodular, exists_finite_isStablyFree_summand_containing, free_of_countablyGenerated_projective_of_localization_not_finite
statement: formalized
proof: formalized
---

# 15.130 Big projective modules are free

Section 15.130 of the Stacks Project, [Tag 0GVE](https://stacks.math.columbia.edu/tag/0GVE). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GVF, a lemma

[Tag 0GVF](https://stacks.math.columbia.edu/tag/0GVF) in the Stacks Project.

**`eilenberg_swindle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/EilenbergSwindle.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/EilenbergSwindle.lean#L81).

> **Eilenberg's lemma / Eilenberg swindle (Stacks Tag 0GVF).**
> Let `R` be a ring and `P`, `Q`, `F` left `R`-modules with `P ⊕ Q ≅ F`, where `F` is a
> free left `R`-module that is not finitely generated. Then `P ⊕ F ≅ F`.

```lean
theorem eilenberg_swindle {R : Type*} [Ring R] (P Q F : Type*) [AddCommGroup P] [Module R P]
    [AddCommGroup Q] [Module R Q] [AddCommGroup F] [Module R F] [Module.Free R F]
    (h : Nonempty ((P × Q) ≃ₗ[R] F)) (hnfg : ¬ Module.Finite R F) :
    Nonempty ((P × F) ≃ₗ[R] F)
```

## Tag 0GVG, a lemma

[Tag 0GVG](https://stacks.math.columbia.edu/tag/0GVG) in the Stacks Project.

**`exists_free_prod_of_projective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/EilenbergSwindle/BigProjective.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/EilenbergSwindle/BigProjective.lean#L107).

> A projective module is a direct summand of a free module with a free complementary
> summand.

```lean
theorem exists_free_prod_of_projective
    {R : Type u} [Ring R] {P : Type v} [AddCommGroup P] [Module R P]
    [Module.Projective R P] :
    ∃ (F : Type (max u v)) (_ : AddCommGroup F) (_ : Module R F)
      (_ : Module.Free R F), Module.Free R (P × F)
```

## Tag 0GVH, a lemma

[Tag 0GVH](https://stacks.math.columbia.edu/tag/0GVH) in the Stacks Project.

**`exists_finite_free_summand_containing_zero_prod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/EilenbergSwindle/BigProjective.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/EilenbergSwindle/BigProjective.lean#L258).

> For an element `s` of a projective module `P`, there is a finite free module `F` and a
> finite free direct summand of `F × P` containing `(0, s)`.

```lean
theorem exists_finite_free_summand_containing_zero_prod
    {R : Type u} [Ring R] {P : Type v} [AddCommGroup P] [Module R P]
    [Module.Projective R P] (s : P) :
    ∃ (F : Type (max u v)) (_ : AddCommGroup F) (_ : Module R F)
      (_ : Module.Finite R F) (_ : Module.Free R F),
      ∃ (K : Submodule R (F × P)) (_ : Module.Finite R K) (_ : Module.Free R K),
        (0, s) ∈ K ∧ ∃ K' : Submodule R (F × P), IsCompl K K'
```

## Tag 0GVI, a lemma

[Tag 0GVI](https://stacks.math.columbia.edu/tag/0GVI) in the Stacks Project.

**`exists_mem_add_unimodular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/EilenbergSwindle/BigProjective.lean, line 637](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/EilenbergSwindle/BigProjective.lean#L637).

> If `P` is projective and has infinite rank after localization at every maximal ideal, then
> an element which generates `P` together with `M` can be modified by an element of `M` to become
> unimodular.

```lean
theorem exists_mem_add_unimodular
    {R : Type u} [CommRing R] {P : Type v} [AddCommGroup P] [Module R P]
    [Module.Projective R P] (M : Submodule R P) (s : P)
    (hR : IsNoetherianRing (R ⧸ Ideal.jacobson (⊥ : Ideal R)))
    (hP : ∀ p : MaximalSpectrum R,
      ¬ Module.Finite (Localization.AtPrime p.asIdeal)
        (LocalizedModule p.asIdeal.primeCompl P))
    (hspan : Submodule.span R {s} ⊔ M = ⊤) :
    ∃ m ∈ M, ∃ φ : P →ₗ[R] R, φ (s + m) = 1
```

## Tag 0GVJ, a lemma

[Tag 0GVJ](https://stacks.math.columbia.edu/tag/0GVJ) in the Stacks Project.

**`exists_finite_isStablyFree_summand_containing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/EilenbergSwindle/BigProjective.lean, line 1142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/EilenbergSwindle/BigProjective.lean#L1142).

> Every element of a projective module of infinite rank at all maximal ideals lies in a finite
> stably free direct summand, provided the quotient by the Jacobson radical is Noetherian.

```lean
theorem exists_finite_isStablyFree_summand_containing
    {R : Type u} [CommRing R] {P : Type v} [AddCommGroup P] [Module R P]
    [Module.Projective R P] (s : P)
    (hR : IsNoetherianRing (R ⧸ Ideal.jacobson (⊥ : Ideal R)))
    (hP : ∀ p : MaximalSpectrum R,
      ¬ Module.Finite (Localization.AtPrime p.asIdeal)
        (LocalizedModule p.asIdeal.primeCompl P)) :
    ∃ M : Submodule R P,
      Module.Finite R M ∧ Module.IsStablyFree R M ∧ s ∈ M ∧
        ∃ M' : Submodule R P, IsCompl M M'
```

## Tag 0GVK, a theorem

[Tag 0GVK](https://stacks.math.columbia.edu/tag/0GVK) in the Stacks Project.

**`free_of_countablyGenerated_projective_of_localization_not_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/EilenbergSwindle/BigProjective.lean, line 1341](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/EilenbergSwindle/BigProjective.lean#L1341).

> A countably generated projective module over a commutative ring is free if the quotient by
> the Jacobson radical is Noetherian and every localization at a maximal ideal has infinite
> rank.

```lean
theorem free_of_countablyGenerated_projective_of_localization_not_finite
    {R : Type u} [CommRing R] {P : Type v} [AddCommGroup P] [Module R P]
    [Module.Projective R P]
    (hR : IsNoetherianRing (R ⧸ Ideal.jacobson (⊥ : Ideal R)))
    (hP : Module.CountablyGenerated R P)
    (hPinf : ∀ p : MaximalSpectrum R,
      ¬ Module.Finite (Localization.AtPrime p.asIdeal)
        (LocalizedModule p.asIdeal.primeCompl P)) :
    Module.Free R P
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.130, Tag 0GVE](https://stacks.math.columbia.edu/tag/0GVE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
