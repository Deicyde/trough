---
declaration: section
origin: cited
lean: Stacks.Smoothing.exists_finitePresentation_factorization_singularIdeal, Stacks.Smoothing.exists_finitePresentation_factorization_singularIdeal_le, Stacks.Smoothing.exists_finitePresentation_factorization_smoothAway_singularIdeal_le
statement: formalized
proof: formalized
---

# 16.7 The desingularization lemma

Section 16.7 of the Stacks Project, [Tag 07CQ](https://stacks.math.columbia.edu/tag/07CQ). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07CR, a lemma

[Tag 07CR](https://stacks.math.columbia.edu/tag/07CR) in the Stacks Project.

**`Stacks.Smoothing.exists_finitePresentation_factorization_singularIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/DesingularizationLemma.lean, line 956](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/DesingularizationLemma.lean#L956).

> **The desingularization lemma.** Let `R` be Noetherian, let `Λ` be an `R`-algebra in which
> the annihilators of `π` and of `π²` agree, and let `A` be an `R`-algebra of finite presentation
> with an `R`-algebra map `f : A → Λ`. If the image of `π` in `A` is strictly standard over `R`,
> and if there is a retraction `ρ : A/π⁴A → R/π⁴R` compatible with the maps to `Λ/π⁴Λ`, then `f`
> factors through an `R`-algebra `B` of finite presentation with `𝔞 B ⊆ H_{B/R}`, where
> `𝔞 = Ann_R (Ann_R (π²) / Ann_R (π))`.

```lean
theorem exists_finitePresentation_factorization_singularIdeal
    (R : Type u) (A : Type v) (Λ : Type w) [CommRing R] [CommRing A] [CommRing Λ]
    [Algebra R A] [Algebra R Λ] [IsNoetherianRing R] [Algebra.FinitePresentation R A]
    (π : R) (f : A →ₐ[R] Λ)
    (hAnn : (Submodule.span Λ {algebraMap R Λ π}).annihilator =
      (Submodule.span Λ {(algebraMap R Λ π) ^ 2}).annihilator)
    (hstandard : IsStrictlyStandard (R := R) (algebraMap R A π))
    (ρ : (A ⧸ Ideal.span {(algebraMap R A π) ^ 4}) →ₐ[R] (R ⧸ Ideal.span {π ^ 4}))
    (hρ : ∀ (x : A) (r : R),
      ρ (Ideal.Quotient.mk (Ideal.span {(algebraMap R A π) ^ 4}) x) =
          Ideal.Quotient.mk (Ideal.span {π ^ 4}) r →
        Ideal.Quotient.mk (Ideal.span {(algebraMap R Λ π) ^ 4}) (f x) =
          Ideal.Quotient.mk (Ideal.span {(algebraMap R Λ π) ^ 4}) (algebraMap R Λ r)) :
    ∃ (B : Type u) (_ : CommRing B) (_ : Algebra R B) (_ : Algebra.FinitePresentation R B)
      (g : A →ₐ[R] B) (h : B →ₐ[R] Λ),
      h.comp g = f ∧
        Ideal.map (algebraMap R B) (annihilatorDefectIdeal R π) ≤ singularIdeal R B
```

## Tag 07CT, a lemma

[Tag 07CT](https://stacks.math.columbia.edu/tag/07CT) in the Stacks Project.

**`Stacks.Smoothing.exists_finitePresentation_factorization_singularIdeal_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/CommonDesingularization.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/CommonDesingularization.lean#L200).

> **Stacks 07CT.** A strictly standard element and a factorization modulo its fourth power
> yield a common finitely presented factorization `A → B ← D` over `Λ` with
> `H_{D/R} B ⊆ H_{B/D}` and `H_{D/R} B ⊆ H_{B/R}`.

```lean
theorem exists_finitePresentation_factorization_singularIdeal_le
    (R : Type u) (A : Type v) (D : Type w) (Λ : Type x)
    [CommRing R] [CommRing A] [CommRing D] [CommRing Λ] [IsNoetherianRing R]
    [Algebra R A] [Algebra R D] [Algebra R Λ]
    [Algebra.FinitePresentation R A] [Algebra.FinitePresentation R D] (π : R)
    (hR : (Submodule.span R {π}).annihilator = (Submodule.span R {π ^ 2}).annihilator)
    (hΛ : (Submodule.span Λ {algebraMap R Λ π}).annihilator =
      (Submodule.span Λ {(algebraMap R Λ π) ^ 2}).annihilator)
    (fA : A →ₐ[R] Λ) (fD : D →ₐ[R] Λ)
    (hπ : IsStrictlyStandard (R := R) (A := A) (algebraMap R A π))
    (bar : (A ⧸ Ideal.span {(algebraMap R A π) ^ 4}) →ₐ[R]
      D ⧸ Ideal.span {(algebraMap R D π) ^ 4})
    (hbar : ∀ (a : A) (y : D),
      bar (Ideal.Quotient.mk (Ideal.span {(algebraMap R A π) ^ 4}) a) =
          Ideal.Quotient.mk (Ideal.span {(algebraMap R D π) ^ 4}) y →
        Ideal.Quotient.mk (Ideal.span {(algebraMap R Λ π) ^ 4}) (fA a) =
          Ideal.Quotient.mk (Ideal.span {(algebraMap R Λ π) ^ 4}) (fD y)) :
    ∃ (B : Type w) (_ : CommRing B) (_ : Algebra D B) (_ : Algebra R B)
      (_ : IsScalarTower R D B) (_ : Algebra.FinitePresentation R B)
      (a : A →ₐ[R] B) (g : B →ₐ[R] Λ),
      g.comp a = fA ∧ g.comp (IsScalarTower.toAlgHom R D B) = fD ∧
        (singularIdeal R D).map (algebraMap D B) ≤ singularIdeal D B ∧
        (singularIdeal R D).map (algebraMap D B) ≤ singularIdeal R B
```

## Tag 07F0, a lemma

[Tag 07F0](https://stacks.math.columbia.edu/tag/07F0) in the Stacks Project.

**`Stacks.Smoothing.exists_finitePresentation_factorization_smoothAway_singularIdeal_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/DesingularizationLifting.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/DesingularizationLifting.lean#L146).

> **Stacks 07F0.** Let `R` be Noetherian, let `Λ` be an `R`-algebra and let `π ∈ R` be an
> element with `Ann_R(π) = Ann_R(π²)` and `Ann_Λ(π) = Ann_Λ(π²)`. Let `A → Λ` be an `R`-algebra
> map with `A` of finite presentation and with the image of `π` strictly standard in `A` over `R`,
> and let `A/π⁸A → C̄ → Λ/π⁸Λ` be a factorization of the induced map with `C̄` of finite
> presentation over `R/π⁸R`. Then `A → Λ` factors as `A → B → Λ` with `B` of finite presentation
> such that `R_π → B_π` is smooth and
> `H_{C̄/(R/π⁸R)} · Λ/π⁸Λ ⊆ √(H_{B/R}Λ) mod π⁸Λ`.

```lean
theorem exists_finitePresentation_factorization_smoothAway_singularIdeal_le
    (R : Type u) (Λ : Type v) (A : Type w) (C : Type x)
    [CommRing R] [CommRing Λ] [CommRing A] [CommRing C] [IsNoetherianRing R]
    [Algebra R Λ] [Algebra R A] [Algebra.FinitePresentation R A] (π : R)
    (hR : (Submodule.span R {π}).annihilator = (Submodule.span R {π ^ 2}).annihilator)
    (hΛ : (Submodule.span Λ {algebraMap R Λ π}).annihilator =
      (Submodule.span Λ {(algebraMap R Λ π) ^ 2}).annihilator)
    (fA : A →ₐ[R] Λ) (hπ : IsStrictlyStandard (R := R) (A := A) (algebraMap R A π))
    [Algebra (R ⧸ Ideal.span {π ^ 8}) C]
    [Algebra.FinitePresentation (R ⧸ Ideal.span {π ^ 8}) C]
    [Algebra (R ⧸ Ideal.span {π ^ 8}) (Λ ⧸ Ideal.span {(algebraMap R Λ π) ^ 8})]
    (hquot : ∀ r : R, algebraMap (R ⧸ Ideal.span {π ^ 8})
        (Λ ⧸ Ideal.span {(algebraMap R Λ π) ^ 8}) (Ideal.Quotient.mk _ r) =
      Ideal.Quotient.mk _ (algebraMap R Λ r))
    (toC : (A ⧸ Ideal.span {(algebraMap R A π) ^ 8}) →+* C)
    (htoC : ∀ r : R, toC (Ideal.Quotient.mk _ (algebraMap R A r)) =
      algebraMap (R ⧸ Ideal.span {π ^ 8}) C (Ideal.Quotient.mk _ r))
    (fC : C →ₐ[R ⧸ Ideal.span {π ^ 8}] Λ ⧸ Ideal.span {(algebraMap R Λ π) ^ 8})
    (hfC : ∀ a : A, fC (toC (Ideal.Quotient.mk _ a)) = Ideal.Quotient.mk _ (fA a)) :
    ∃ (B : Type (max u v x)) (_ : CommRing B) (_ : Algebra R B)
      (_ : Algebra.FinitePresentation R B) (a : A →ₐ[R] B) (g : B →ₐ[R] Λ),
      g.comp a = fA ∧
      (letI : Algebra (Localization.Away π) (Localization.Away (algebraMap R B π)) :=
        (Localization.awayMap (algebraMap R B) π).toAlgebra
       Algebra.Smooth (Localization.Away π) (Localization.Away (algebraMap R B π))) ∧
      Ideal.map fC.toRingHom (singularIdeal (R ⧸ Ideal.span {π ^ 8}) C) ≤
        Ideal.map (Ideal.Quotient.mk (Ideal.span {(algebraMap R Λ π) ^ 8}))
          (Ideal.map g.toRingHom (singularIdeal R B)).radical
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 16.7, Tag 07CQ](https://stacks.math.columbia.edu/tag/07CQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
