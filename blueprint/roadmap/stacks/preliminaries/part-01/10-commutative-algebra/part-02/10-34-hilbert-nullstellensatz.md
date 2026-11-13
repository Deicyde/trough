---
declaration: section
origin: cited
lean: Stacks.HilbertNullstellensatz.module_finite_quotient_of_finiteType, Stacks.HilbertNullstellensatz.eq_sInf_isMaximal_of_finiteType, Stacks.HilbertNullstellensatz.module_finite_quotient_mvPolynomial, Stacks.HilbertNullstellensatz.eq_sInf_isMaximal_mvPolynomial, Stacks.HilbertNullstellensatz.coe_eq_iInter_isMaximal_mvPolynomial, finite_of_finite_type_of_isJacobsonRing, MvPolynomial.isJacobsonRing, exists_isField_localizationAway_and_finite_of_finiteType
statement: formalized
proof: formalized
---

# 10.34 Hilbert Nullstellensatz

Section 10.34 of the Stacks Project, [Tag 00FS](https://stacks.math.columbia.edu/tag/00FS). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00FV, a theorem

[Tag 00FV](https://stacks.math.columbia.edu/tag/00FV) in the Stacks Project.

**`Stacks.HilbertNullstellensatz.module_finite_quotient_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/HilbertNullstellensatz.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/HilbertNullstellensatz.lean#L54). The attribute's comment: “part (1), for an arbitrary finite type algebra over the field”. References: EGA IV (10.4.5), “a⇒b′ over a field”.

> **Hilbert Nullstellensatz**, part (1), for a finite type algebra: if `A` is a `k`-algebra of
> finite type over a field `k` and `𝔪 ⊆ A` is a maximal ideal, then the residue field
> `κ(𝔪) = A ⧸ 𝔪` is a finite extension of `k`.
>
> The quotient `A ⧸ 𝔪` is a field by `Ideal.Quotient.field`, and it is of finite type over `k`
> because `A` is, so Zariski's lemma over the Jacobson ring `k` applies.

```lean
public theorem module_finite_quotient_of_finiteType (k A : Type*) [Field k] [CommRing A]
    [Algebra k A] [Algebra.FiniteType k A] (𝔪 : Ideal A) [𝔪.IsMaximal] :
    Module.Finite k (A ⧸ 𝔪)
```

**`Stacks.HilbertNullstellensatz.eq_sInf_isMaximal_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/HilbertNullstellensatz.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/HilbertNullstellensatz.lean#L68). The attribute's comment: “part (2), for an arbitrary finite type algebra over the field”. References: EGA IV (10.4.6), “partial”.

> **Hilbert Nullstellensatz**, part (2), for a finite type algebra: a radical ideal `I` of a
> `k`-algebra `A` of finite type over a field `k` is the infimum of the maximal ideals of `A`
> containing `I`.
>
> A finite type algebra over a field is a Jacobson ring, and in a Jacobson ring a radical ideal
> equals its Jacobson radical, which is by definition that infimum.

```lean
public theorem eq_sInf_isMaximal_of_finiteType (k A : Type*) [Field k] [CommRing A] [Algebra k A]
    [Algebra.FiniteType k A] (I : Ideal A) (hI : I.IsRadical) :
    I = sInf {J : Ideal A | I ≤ J ∧ J.IsMaximal}
```

**`Stacks.HilbertNullstellensatz.module_finite_quotient_mvPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/HilbertNullstellensatz.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/HilbertNullstellensatz.lean#L88). The attribute's comment: “part (1)”.

> **Hilbert Nullstellensatz**, part (1): for a field `k`, finitely many variables `ι` and a
> maximal ideal `𝔪` of the polynomial ring `k[x_i : i ∈ ι]`, the residue field
> `κ(𝔪) = k[x_i : i ∈ ι] ⧸ 𝔪` is a finite extension of `k`.

```lean
public theorem module_finite_quotient_mvPolynomial (k : Type*) [Field k] (ι : Type*) [Finite ι]
    (𝔪 : Ideal (MvPolynomial ι k)) [𝔪.IsMaximal] :
    Module.Finite k (MvPolynomial ι k ⧸ 𝔪)
```

**`Stacks.HilbertNullstellensatz.eq_sInf_isMaximal_mvPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/HilbertNullstellensatz.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/HilbertNullstellensatz.lean#L97). The attribute's comment: “part (2)”.

> **Hilbert Nullstellensatz**, part (2): for a field `k` and finitely many variables `ι`, a
> radical ideal `I` of the polynomial ring `k[x_i : i ∈ ι]` is the infimum of the maximal ideals
> containing `I`.

```lean
public theorem eq_sInf_isMaximal_mvPolynomial (k : Type*) [Field k] (ι : Type*) [Finite ι]
    (I : Ideal (MvPolynomial ι k)) (hI : I.IsRadical) :
    I = sInf {J : Ideal (MvPolynomial ι k) | I ≤ J ∧ J.IsMaximal}
```

**`Stacks.HilbertNullstellensatz.coe_eq_iInter_isMaximal_mvPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/HilbertNullstellensatz.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/HilbertNullstellensatz.lean#L106). The attribute's comment: “part (2), as an intersection of the underlying sets”.

> **Hilbert Nullstellensatz**, part (2), as an equality of sets: a radical ideal `I` of the
> polynomial ring `k[x_i : i ∈ ι]` over a field `k` in finitely many variables is, as a subset of
> the polynomial ring, the intersection of the maximal ideals containing `I`.

```lean
public theorem coe_eq_iInter_isMaximal_mvPolynomial (k : Type*) [Field k] (ι : Type*) [Finite ι]
    (I : Ideal (MvPolynomial ι k)) (hI : I.IsRadical) :
    (I : Set (MvPolynomial ι k)) =
      ⋂ J ∈ {J : Ideal (MvPolynomial ι k) | I ≤ J ∧ J.IsMaximal},
        (J : Set (MvPolynomial ι k))
```

Declarations registered for the tag:

- [`finite_of_finite_type_of_isJacobsonRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=finite_of_finite_type_of_isJacobsonRing#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Jacobson/HilbertNullstellensatz.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/HilbertNullstellensatz.lean#L118) (StacksFrontier): “part (1) is this applied to the field `A ⧸ 𝔪`, which is of finite type over `k`; see `Stacks.HilbertNullstellensatz.module_finite_quotient_of_finiteType`”. References: EGA IV (10.4.5), “a⇒b′”.
- [`MvPolynomial.isJacobsonRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=MvPolynomial.isJacobsonRing#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Jacobson/HilbertNullstellensatz.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/HilbertNullstellensatz.lean#L124) (StacksFrontier): “part (2): a radical ideal of a Jacobson ring equals its Jacobson radical, which is the infimum of the maximal ideals containing it; see `Stacks.HilbertNullstellensatz.eq_sInf_isMaximal_mvPolynomial`”.

## Tag 00FY, a lemma

[Tag 00FY](https://stacks.math.columbia.edu/tag/00FY) in the Stacks Project.

**`exists_isField_localizationAway_and_finite_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean#L108).

> Let `R ⊂ K` with `K` a field and `K` of finite type over `R` as an `R`-algebra. Then there
> exists `f ∈ R` such that the localization `R_f` is a field, and `K` is a finite extension of
> `R_f`.

```lean
theorem exists_isField_localizationAway_and_finite_of_finiteType (R K : Type*)
    [CommRing R] [Field K]
    [Algebra R K] (hRK : Function.Injective (algebraMap R K))
    [Algebra.FiniteType R K] :
    ∃ f : R, IsField (Localization.Away f) ∧
      ∃ (_ : Algebra (Localization.Away f) K)
        (_ : IsScalarTower R (Localization.Away f) K),
        Module.Finite (Localization.Away f) K
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.34, Tag 00FS](https://stacks.math.columbia.edu/tag/00FS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
