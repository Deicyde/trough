---
declaration: section
origin: cited
lean: Stacks.Smoothing.exists_smooth_quotient_factorization, Stacks.Smoothing.exists_smooth_factorization_of_fg_le_map, Stacks.Smoothing.ind_smooth_of_isNilpotent
statement: formalized
proof: formalized
---

# 16.5 The lifting problem

Section 16.5 of the Stacks Project, [Tag 07CJ](https://stacks.math.columbia.edu/tag/07CJ). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07CK, a lemma

[Tag 07CK](https://stacks.math.columbia.edu/tag/07CK) in the Stacks Project.

**`Stacks.Smoothing.exists_smooth_quotient_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/LiftingProblem.lean, line 422](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/LiftingProblem.lean#L422).

> **The lifting problem.** Let `R → Λ` be a ring map and `I ⊂ R` an ideal with `I² = 0` such
> that `Λ/IΛ` is a filtered colimit of smooth `R/I`-algebras. Then every `R`-algebra map
> `φ : A → Λ` with `A` of finite presentation over `R` factors as `A → B/J → Λ` with `B` a smooth
> `R`-algebra and `J ⊂ IB` a finitely generated ideal.

```lean
theorem exists_smooth_quotient_factorization
    {R Λ A : Type u} [CommRing R] [CommRing Λ] [CommRing A]
    [Algebra R Λ] [Algebra R A] [Algebra.FinitePresentation R A]
    (I : Ideal R) (hI : I ^ 2 = ⊥)
    (hΛ : ObjectProperty.ind.{u}
      (fun B : Under (CommRingCat.of (R ⧸ I)) ↦ B.hom.hom.Smooth)
      (Under.mk (CommRingCat.ofHom (algebraMap (R ⧸ I) (Λ ⧸ I.map (algebraMap R Λ))))))
    (φ : A →ₐ[R] Λ) :
    ∃ (B : Type u) (_ : CommRing B) (alg : Algebra R B),
      letI := alg
      Algebra.Smooth R B ∧
        ∃ J : Ideal B, J ≤ I.map (algebraMap R B) ∧ J.FG ∧
          ∃ (α : A →ₐ[R] B ⧸ J) (β : (B ⧸ J) →ₐ[R] Λ), β.comp α = φ
```

## Tag 07CL, a lemma

[Tag 07CL](https://stacks.math.columbia.edu/tag/07CL) in the Stacks Project.

**`Stacks.Smoothing.exists_smooth_factorization_of_fg_le_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/LiftingProblem.lean, line 772](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/LiftingProblem.lean#L772).

> **Stacks Project, Tag 07CL.** Let `I ⊂ R` be an ideal with `I² = 0` such that `Λ/IΛ` is a
> filtered colimit of smooth `R/I`-algebras, and let `Λ` be flat over `R`. Then an `R`-algebra map
> `φ : B → Λ` with `B` smooth over `R` factors as `B → B' → Λ` with `B'` smooth over `R` and with
> `B → B'` killing any prescribed finitely generated ideal `J ⊆ IB` that `φ` annihilates.

```lean
theorem exists_smooth_factorization_of_fg_le_map
    (I : Ideal R) (hI : I ^ 2 = ⊥)
    (hΛ : ObjectProperty.ind.{u}
      (fun C : Under (CommRingCat.of (R ⧸ I)) ↦ C.hom.hom.Smooth)
      (Under.mk (CommRingCat.ofHom (algebraMap (R ⧸ I) (Λ ⧸ I.map (algebraMap R Λ))))))
    [Module.Flat R Λ] {B : Type u} [CommRing B] [Algebra R B] [Algebra.Smooth R B]
    (φ : B →ₐ[R] Λ) (J : Ideal B) (hJI : J ≤ I.map (algebraMap R B)) (hJfg : J.FG)
    (hφJ : ∀ x ∈ J, φ x = 0) :
    ∃ (B' : Type u) (_ : CommRing B') (alg : Algebra R B'),
      letI := alg
      Algebra.Smooth R B' ∧
        ∃ (α : B →ₐ[R] B') (β : B' →ₐ[R] Λ), (∀ x ∈ J, α x = 0) ∧ β.comp α = φ
```

## Tag 07CM, a proposition

[Tag 07CM](https://stacks.math.columbia.edu/tag/07CM) in the Stacks Project.

**`Stacks.Smoothing.ind_smooth_of_isNilpotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/LiftingProblem.lean, line 939](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/LiftingProblem.lean#L939).

> **Stacks Project, Tag 07CM: ind-smoothness of an algebra is stable under infinitesimal
> deformations.** Let `R → Λ` be a ring map and `I ⊂ R` a nilpotent ideal. If `Λ/IΛ` is a filtered
> colimit of smooth `R/I`-algebras and `R → Λ` is flat, then `Λ` is a filtered colimit of smooth
> `R`-algebras.
>
> Here "filtered colimit of smooth algebras" is `CategoryTheory.ObjectProperty.ind` of
> `RingHom.Smooth` on `Under (CommRingCat.of R)`, the spelling of `07C3`, `07CK` and `07CL`;
> nilpotence is `IsNilpotent I`, that is `I ^ n = ⊥` for some `n`; and flatness is
> `Module.Flat R Λ`.

```lean
theorem ind_smooth_of_isNilpotent (I : Ideal R) (hI : IsNilpotent I)
    (hΛ : ObjectProperty.ind.{u}
      (fun C : Under (CommRingCat.of (R ⧸ I)) ↦ C.hom.hom.Smooth)
      (Under.mk (CommRingCat.ofHom (algebraMap (R ⧸ I) (Λ ⧸ I.map (algebraMap R Λ))))))
    [Module.Flat R Λ] :
    ObjectProperty.ind.{u} (fun C : Under (CommRingCat.of R) ↦ C.hom.hom.Smooth)
      (Under.mk (CommRingCat.ofHom (algebraMap R Λ)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 16.5, Tag 07CJ](https://stacks.math.columbia.edu/tag/07CJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
