---
declaration: section
origin: cited
lean: Algebra.FormallyUnramified.exists_extension_ker_sq_eq_bot_and_existsUnique_lift, Algebra.FormallyUnramified.universalFirstOrderThickening, Algebra.FormallyUnramified.conormal, UniversalThickening.universal_property, UniversalThickening.conormal_module, Algebra.Extension.IsUniversalFirstOrderThickening.localization, Algebra.Extension.IsUniversalFirstOrderThickening.formallyUnramified_ring_and_bijective_map
statement: formalized
proof: formalized
---

# 10.149 Conormal modules and universal thickenings

Section 10.149 of the Stacks Project, [Tag 04EA](https://stacks.math.columbia.edu/tag/04EA). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04EB, a lemma

[Tag 04EB](https://stacks.math.columbia.edu/tag/04EB) in the Stacks Project.

**`Algebra.FormallyUnramified.exists_extension_ker_sq_eq_bot_and_existsUnique_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Thickening.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Unramified/Thickening.lean#L289). The attribute's comment: “The surjection of `R`-algebras `S' → S` is an `Algebra.Extension R S` (the structure whose data is exactly a surjection onto `S` of `R`-algebras). The source's square is encoded by `A` being an `R`-algebra — its `b : R → A` is `algebraMap R A` — and `a` being an `R`-algebra map, so that commutativity of the square is `a`'s `R`-linearity. The test algebra lives in a universe of its own; see the module docstring.”.

> **Stacks 04EB.** Let `R → S` be a formally unramified ring map. There is a surjection of
> `R`-algebras `S' → S` whose kernel is an ideal of square zero and which is universal: for every
> `R`-algebra `A`, every ideal `I ⊆ A` with `I ^ 2 = 0` and every `R`-algebra map `a : S → A/I`,
> there is a unique `R`-algebra map `a' : S' → A` such that `S' → A → A/I` equals `S' → S → A/I`.
> The surjection `S' → S` is `algebraMap P.Ring S` for the produced `Algebra.Extension P`.

```lean
theorem Algebra.FormallyUnramified.exists_extension_ker_sq_eq_bot_and_existsUnique_lift
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.FormallyUnramified R S] :
    ∃ P : Algebra.Extension.{max u v} R S, P.ker ^ 2 = ⊥ ∧
      ∀ ⦃A : Type w⦄ [CommRing A] [Algebra R A] (I : Ideal A), I ^ 2 = ⊥ →
        ∀ a : S →ₐ[R] A ⧸ I, ∃! a' : P.Ring →ₐ[R] A,
          (Ideal.Quotient.mkₐ R I).comp a' = a.comp (IsScalarTower.toAlgHom R P.Ring S)
```

## Tag 04EC, a definition

[Tag 04EC](https://stacks.math.columbia.edu/tag/04EC) in the Stacks Project.

**`Algebra.FormallyUnramified.universalFirstOrderThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Thickening.lean, line 368](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Unramified/Thickening.lean#L368). The attribute's comment: “Part (1). The surjection `S' → S` is an `Algebra.Extension R S`, the structure whose data is exactly a surjection of `R`-algebras onto `S`; the surjection is `algebraMap S'.Ring S`. Only determined up to unique isomorphism, so defined by choosing one of the thickenings produced by Tag 04EB and used only through `Algebra.FormallyUnramified.isUniversalFirstOrderThickening`. See the module docstring.”.

> The **universal first order thickening** `S' → S` of `S` over a formally unramified base
> `R`: the surjection of `R`-algebras onto `S` with square-zero kernel through which every
> square-zero situation over `S` lifts uniquely, provided by Tag 04EB. It is determined up to
> unique isomorphism by `Algebra.FormallyUnramified.isUniversalFirstOrderThickening`, which is all
> that is ever used about it.

```lean
noncomputable def universalFirstOrderThickening : Extension.{max u v} R S
```

**`Algebra.FormallyUnramified.conormal`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Thickening.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Unramified/Thickening.lean#L385). The attribute's comment: “Part (2). The kernel of `algebraMap S'.Ring S` seen as an `S`-module is `Algebra.Extension.Cotangent`, the quotient of the kernel by its square — equal to the kernel because the square is zero, and the object on which `S` acts. See the module docstring.”.

> The **conormal module** `C_{S/R}` of a formally unramified ring map `R → S`: the kernel of
> the universal first order thickening `S' → S`, as a module over `S`. Being an ideal of square
> zero in `S'`, that kernel equals its own image in `S' / (ker) ^ 2`, which is where the `S`-action
> lives.

```lean
abbrev conormal : Type (max u v)
```

## Tag 04ED, a lemma

[Tag 04ED](https://stacks.math.columbia.edu/tag/04ED) in the Stacks Project.

**`UniversalThickening.universal_property`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Thickening.lean, line 1174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Unramified/Thickening.lean#L1174).

> For any commutative ring `A` with a
> square-zero ideal `J ⊆ A`, and ring homomorphisms `b : R → A`,
> `a : R/I → A/J` such that the square
> `a ∘ (R → R/I) = (A → A/J) ∘ b` commutes (where `R → A/J` is `b` followed
> by `A → A/J`), there exists a **unique** `R`-algebra homomorphism
> `a' : R/I² → A`, encoded as a unique ring homomorphism with
> `a' ∘ (R → R/I²) = b` (the `R`-algebra condition), such that
> `(A → A/J) ∘ a' = a ∘ π`.

```lean
theorem universal_property
    {A : Type*} [CommRing A] (J : Ideal A) (hJ : IsSquareZero J)
    (b : R →+* A) (a : (R ⧸ I) →+* (A ⧸ J))
    (hcomm : a.comp (Ideal.Quotient.mk I) = (Ideal.Quotient.mk J).comp b) :
    ∃! a' : (R ⧸ I ^ 2) →+* A,
      a'.comp (Ideal.Quotient.mk (I ^ 2)) = b ∧
      (Ideal.Quotient.mk J).comp a' = a.comp (pi I : (R ⧸ I ^ 2) →+* (R ⧸ I))
```

**`UniversalThickening.conormal_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Thickening.lean, line 1222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Unramified/Thickening.lean#L1222). References: EGA 0 (20.5.12), “kernel of E → C is R/R²”.

> Consequently the
> universal first order thickening of `R/I` over `R` is the surjection
> `π : R/I² → R/I`, whose kernel — the conormal module `C_{(R/I)/R}` — is
> `I/I²`. Concretely, the kernel of `π` is `Ideal.cotangentIdeal I`
> (Statement 1b), and the conormal module `Ideal.Cotangent I` (the `R`-module
> `I/I²`) is `R`-linearly isomorphic to this kernel via
> `Ideal.cotangentEquivIdeal`. We record both facts:
> the kernel description and the existence of such an `R`-linear equivalence.

```lean
theorem conormal_module :
    RingHom.ker (pi I : (R ⧸ I ^ 2) →+* (R ⧸ I)) = I.cotangentIdeal ∧
    Nonempty (I.Cotangent ≃ₗ[R] (RingHom.ker (pi I : (R ⧸ I ^ 2) →+* (R ⧸ I))))
```

## Tag 04EE, a lemma

[Tag 04EE](https://stacks.math.columbia.edu/tag/04EE) in the Stacks Project.

**`Algebra.Extension.IsUniversalFirstOrderThickening.localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Thickening.lean, line 473](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Unramified/Thickening.lean#L473). The attribute's comment: “Both parts at once: part (1) is `N = Algebra.algebraMapSubmonoid B M`, part (2) is `M = ⊥`, whose instance `IsLocalization (⊥ : Submonoid A) A` is not found by synthesis and is supplied as `IsLocalization.of_le_isUnit bot_le`. The localized thickening is an arbitrary `Q : Algebra.Extension Aₘ Bₙ` pinned by the `IsLocalization` and `IsScalarTower` hypotheses and by `algebraMap_comp`, because Mathlib's `Algebra.Extension.localization` does not localize the base. The `In particular` on conormal modules is the ideal equation, `Algebra.idealMap_isLocalizedModule` supplying the rest. That `φ⁻¹(N)` is multiplicative is `Submonoid.comap`. See the module docstring.”.

> **Stacks 04EE.** Let `A → B` be a ring map, let `φ : P.Ring → B` be a universal first order
> thickening of `B` over `A`, let `M ⊆ A` and `N ⊆ B` be multiplicative subsets, and let `Aₘ` and
> `Bₙ` be localizations of `A` at `M` and of `B` at `N`, compatibly. Then the localization
> `φ⁻¹(N)⁻¹P.Ring → N⁻¹B` of `φ` is a universal first order thickening of `N⁻¹B` over `Aₘ`, and its
> kernel is the extension of `ker φ`, so that the conormal module localizes:
> `N⁻¹C_{B/A} = C_{N⁻¹B/Aₘ}`. Taking `N` to be the image of `M` gives the source's part (1), and
> taking `M = ⊥`, so that `Aₘ = A`, gives its part (2).

```lean
theorem Algebra.Extension.IsUniversalFirstOrderThickening.localization {A : Type u} {B : Type v}
    [CommRing A] [CommRing B] [Algebra A B]
    {P : Extension.{w} A B} (hP : P.IsUniversalFirstOrderThickening)
    (M : Submonoid A) (N : Submonoid B)
    {Aₘ : Type*} [CommRing Aₘ] [Algebra A Aₘ] [IsLocalization M Aₘ]
    {Bₙ : Type*} [CommRing Bₙ] [Algebra B Bₙ] [IsLocalization N Bₙ]
    [Algebra A Bₙ] [IsScalarTower A B Bₙ] [Algebra Aₘ Bₙ] [IsScalarTower A Aₘ Bₙ]
    (Q : Extension.{w} Aₘ Bₙ) [Algebra P.Ring Q.Ring] [IsScalarTower A P.Ring Q.Ring]
    [IsLocalization (N.comap (algebraMap P.Ring B)) Q.Ring]
    (algebraMap_comp : (algebraMap Q.Ring Bₙ).comp (algebraMap P.Ring Q.Ring)
      = (algebraMap B Bₙ).comp (algebraMap P.Ring B)) :
    Q.IsUniversalFirstOrderThickening ∧ Q.ker = P.ker.map (algebraMap P.Ring Q.Ring)
```

## Tag 04EF, a lemma

[Tag 04EF](https://stacks.math.columbia.edu/tag/04EF) in the Stacks Project.

**`Algebra.Extension.IsUniversalFirstOrderThickening.formallyUnramified_ring_and_bijective_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Thickening.lean, line 1052](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Unramified/Thickening.lean#L1052). The attribute's comment: “The thickening `B' → B` is an `Algebra.Extension A B` satisfying `Algebra.Extension.IsUniversalFirstOrderThickening` (04EC); existence is 04EB. Tensor products carry the scalars on the left, as in `KaehlerDifferential.mapBaseChange`, and the source's canonical map is spelled as the `B`-linear extension of `ω ↦ 1 ⊗ₜ KaehlerDifferential.map ω`. Formal unramifiedness of `A → B` is not assumed: it follows from `hP`. See the module docstring.”.

> **Stacks 04EF.** Let `R → A → B` be ring maps and let `B' → B` be the universal first order
> thickening of `B` over `A`. Then `B'` is formally unramified over `A`, and the canonical map
> `Ω_{A/R} ⊗_A B → Ω_{B'/R} ⊗_{B'} B`, which sends `b ⊗ D a` to `b ⊗ D (algebraMap A B' a)`, is
> an isomorphism.

```lean
public theorem formallyUnramified_ring_and_bijective_map (R : Type u) {A : Type v} {B : Type*}
    [CommRing R] [CommRing A] [CommRing B] [Algebra R A] [Algebra A B] [Algebra R B]
    [IsScalarTower R A B] {P : Extension.{w} A B} (hP : P.IsUniversalFirstOrderThickening) :
    FormallyUnramified A P.Ring ∧
      Function.Bijective
        ((((TensorProduct.mk P.Ring B Ω[P.Ring⁄R] 1).restrictScalars A).comp
          (KaehlerDifferential.map R R A P.Ring)).liftBaseChange B)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.149, Tag 04EA](https://stacks.math.columbia.edu/tag/04EA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
