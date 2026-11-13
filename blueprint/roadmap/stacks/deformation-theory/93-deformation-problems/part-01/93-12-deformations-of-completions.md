---
declaration: section
origin: cited
lean: Deformation.Examples.DerivedLift.exists_flat_lift_iff_exists_derived_lift, Deformation.HasFlatModuleLift.baseChange, Deformation.exists_flatModuleLift_iff_baseChange_of_sq_zero, Deformation.hasFlatAlgebraLift_iff_hasFlatAlgebraLift_adicCompletion, Deformation.Examples.exists_squareZeroAlgebraExtensionClassesCompletionEquiv, Deformation.Examples.isSmooth_and_bijective_differential_adicCompletionFunctor
statement: formalized
proof: formalized
---

# 93.12 Deformations of completions

Section 93.12 of the Stacks Project, [Tag 0DZ0](https://stacks.math.columbia.edu/tag/0DZ0). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DZ1, a lemma

[Tag 0DZ1](https://stacks.math.columbia.edu/tag/0DZ1) in the Stacks Project.

**`Deformation.Examples.DerivedLift.exists_flat_lift_iff_exists_derived_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/BaseChangeIndependence/DerivedLift.lean, line 481](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/BaseChangeIndependence/DerivedLift.lean#L481).

> Over a nilpotent surjection, an `A`-flat module lifts flatly if and only if
> it admits a bounded-above derived lift.

```lean
public theorem exists_flat_lift_iff_exists_derived_lift
    (A' A P' : Type u) [CommRing A'] [CommRing A] [CommRing P']
    [Algebra A' A] [Algebra A' P']
    (hsurj : Function.Surjective (algebraMap A' A))
    (hnil : IsNilpotent (RingHom.ker (algebraMap A' A)))
    [Module.Flat A' P']
    (M : Type v) [AddCommGroup M] [Module (TensorProduct A' P' A) M]
    [Module A M] [IsScalarTower A (TensorProduct A' P' A) M]
    [Module.Flat A M] :
    (∃ (M' : Type (max u v)) (_ : AddCommGroup M')
      (_ : Module P' M') (_ : Module A' M') (_ : IsScalarTower A' P' M'),
      Module.Flat A' M' ∧
        Nonempty
          ((ModuleCat.extendScalars.{u, u, max u v}
              (algebraMap P' (TensorProduct A' P' A))).obj
                (ModuleCat.of.{max u v, u} P' M') ≅
            ModuleCat.of.{max u v, u} (TensorProduct A' P' A) (ULift.{u} M))) ↔
      ∃ (K : DerivedCategory.Minus (ModuleCat.{max u v} P')),
        Nonempty
          ((CochainComplex.DerivedExtensionScalars.derivedExtensionScalarsGeneral.{u, v, u}
            (algebraMap P' (TensorProduct A' P' A))).functor.obj K.obj ≅
            (DerivedCategory.Q
              (C := ModuleCat.{max u v} (TensorProduct A' P' A))).obj
                ((CochainComplex.singleFunctor
                  (ModuleCat.{max u v} (TensorProduct A' P' A)) 0).obj
                    (ModuleCat.of.{max u v, u} (TensorProduct A' P' A)
                      (ULift.{u} M))))
```

## Tag 0DZ2, a lemma

[Tag 0DZ2](https://stacks.math.columbia.edu/tag/0DZ2) in the Stacks Project.

**`Deformation.HasFlatModuleLift.baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FlatModuleLift.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/FlatModuleLift.lean#L272). The attribute's comment: “the implication (1) => (2) of 0DZ2, at the source's hypotheses with nothing added; it needs neither the Noetherian hypotheses, nor finiteness of `M`, nor `J'`, nor the local liftability hypothesis. The converse (2) => (1) is false as printed (Stacks erratum, see errata.md): `Deformation.Examples.ArtinSchreier.not_flatModuleLiftBaseChangeStatementFaithful` satisfies every hypothesis of the source and (2) holds there while (1) fails. The corrected equivalence, with `ker(A' → A)^2 = ⊥` and `M` finite over `P` added, is `Deformation.exists_flatModuleLift_iff_baseChange_of_sq_zero`”.

> **Stacks 0DZ2, forward implication.** In a commuting square of ring maps `P' → Q'`,
> `P' → P`, `Q' → Q`, `P → Q` whose left vertical map `p` is surjective with nilpotent kernel and
> whose top map `P' → Q'` is flat, a flat module lift of a `P`-module `M` base-changes to a flat
> module lift of `Q ⊗[P] M`.
>
> By Nakayama the lift `N` is generated over `P'` by a family indexed by `M`, so `Q' ⊗[P'] N` is a
> quotient of `M →₀ Q'` and can be presented in the universe of `Q'` and `M`, which is what
> `HasFlatModuleLift` demands of the witness.
>
> This direction of Stacks 0DZ2 carries the source's own hypothesis on the kernel of `P' → P` —
> nilpotent, not square-zero — and uses none of the obstruction calculus, so it is faithful and in
> fact more general than the source: neither the Noetherian hypotheses, nor finiteness of `M`, nor
> the ideal `J'`, nor the local liftability hypothesis is needed. The converse is the
> obstruction-theoretic half, and is
> `exists_flat_lift_iff_exists_flat_lift_baseChange_of_localizationLift_of_isNilpotent_ker` in
> `StacksFrontier.Deformation.FlatModuleLiftLocalization`.

```lean
public theorem HasFlatModuleLift.baseChange
    {A' : Type u₁} {P' : Type u₃} {P : Type u₄} {Q' : Type u₅} {Q : Type u₆}
    [CommRing A'] [CommRing P'] [CommRing P] [CommRing Q'] [CommRing Q]
    [Algebra A' P'] [Algebra P' Q'] [Algebra P Q]
    {p : P' →+* P} {q : Q' →+* Q}
    (hcomm : (algebraMap P Q).comp p = q.comp (algebraMap P' Q'))
    (hflat : Module.Flat P' Q')
    (hp : Function.Surjective p) (hnp : IsNilpotent (RingHom.ker p))
    (M : Type v) [AddCommGroup M] [Module P M]
    (h : HasFlatModuleLift (algebraMap A' P') p M) :
    HasFlatModuleLift ((algebraMap P' Q').comp (algebraMap A' P')) q (Q ⊗[P] M)
```

**`Deformation.exists_flatModuleLift_iff_baseChange_of_sq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FlatModuleLiftBaseChangeAbstract.lean, line 863](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/FlatModuleLiftBaseChangeAbstract.lean#L863). The attribute's comment: “corrected form of 0DZ2 (Stacks erratum, see errata.md): the equivalence (1) <=> (2) with the two hypotheses `hzeroA : ker(A' → A)^2 = ⊥` and `Module.Finite P M` added, every other hypothesis being the source's (Noetherianity is asked of `P` alone, flatness of `A → P` and nilpotence of the kernels follow, and `Module.Flat A' Q'` is the composite of `A' → P' → Q'`). As printed, (2) => (1) is false: `Deformation.Examples.ArtinSchreier.not_flatModuleLiftBaseChangeStatementFaithful` satisfies every hypothesis of the source, with `ker(A' → A) = (t)`, `t^3 = 0`, `t^2 ≠ 0` and `M` cyclic, and (1) fails there. So `I^2 = 0` cannot be weakened to `I^3 = 0`; finiteness of `M` is used by the source's own proof at 0A6A. The implication (1) => (2) holds as printed, with no hypothesis added: `Deformation.HasFlatModuleLift.baseChange`”.

> **Stacks 0DZ2, corrected (Stacks erratum).** Let `A' → P' → Q'` lie over `A → P → Q`, with
> `A' → A`, `P' → P`, `Q' → Q` surjective, `ker(P' → P) = I·P'` and `ker(Q' → Q) = I·Q'` for
> `I = ker(A' → A)` (the two squares are cocartesian), `A' → P'`, `P' → Q'`, `P → Q` flat and `P`
> Noetherian. Let `J' ⊂ P'` be an ideal with `P'/J' = Q'/J'Q'`, let `M` be a `P`-module, finite over
> `P` and flat over `A`, and let `N ≅ Q ⊗_P M`. If `M_g` has an `A'`-flat lift to `(P')_g` for every
> `g ∈ J'` and `I² = 0`, then `M` has an `A'`-flat lift to a `P'`-module if and only if `N` has an
> `A'`-flat lift to a `Q'`-module.
>
> Stacks 0DZ2 as printed asks `I` to be nilpotent and does not ask `M` to be finite, and in that
> form the implication (2) ⇒ (1) is false:
> `Deformation.Examples.ArtinSchreier.not_flatModuleLiftBaseChangeStatementFaithful` is a
> counterexample with `I³ = 0`, `I² ≠ 0` and `M` cyclic, satisfying every hypothesis of the source.
> The two hypotheses added here are the correction recorded in `errata.md`: `I² = 0` is sharp by
> that counterexample, and finiteness of `M` is what the source's own proof uses ("here we use that
> `P` is Noetherian and `M` finite", at Stacks 0A6A). The implication (1) ⇒ (2) holds at the
> source's hypotheses with no addition, as `Deformation.HasFlatModuleLift.baseChange`.
>
> The proof is the source's proof with its induction step removed: it transports to this shape the
> form proved in `StacksFrontier.Deformation.FlatModuleLiftLocalization`, which allows `I` to be
> nilpotent provided the thickening `P' → P` is square-zero.

```lean
theorem exists_flatModuleLift_iff_baseChange_of_sq_zero
    [IsNoetherianRing P] [Module.Flat P' Q'] [Module.Flat P Q]
    (hzeroA : RingHom.ker (algebraMap A' A) ^ 2 = ⊥)
    (J' : Ideal P')
    (hquot : Function.Bijective (Ideal.quotientMap (J'.map (algebraMap P' Q'))
      (algebraMap P' Q') Ideal.le_comap_map))
    (M : Type u) [AddCommGroup M] [Module P M] [Module A M] [IsScalarTower A P M]
      [Module.Finite P M] [Module.Flat A M] (N : Type u) [AddCommGroup N] [Module Q N]
    (hMN : Nonempty ((Q ⊗[P] M) ≃ₗ[Q] N))
    (hloc : ∀ g ∈ J',
      letI : Algebra (Localization.Away g) (Localization.Away (algebraMap P' P g)) :=
        (Localization.awayMap (algebraMap P' P) g).toAlgebra
      ∃ (L : Type u) (_ : AddCommGroup L) (_ : Module (Localization.Away g) L)
        (_ : Module A' L) (_ : IsScalarTower A' (Localization.Away g) L),
        Module.Flat A' L ∧ Nonempty
          ((Localization.Away (algebraMap P' P g) ⊗[Localization.Away g] L)
            ≃ₗ[Localization.Away (algebraMap P' P g)]
              (Localization.Away (algebraMap P' P g) ⊗[P] M))) :
    (∃ (M' : Type u) (_ : AddCommGroup M') (_ : Module P' M') (_ : Module A' M')
        (_ : IsScalarTower A' P' M'), Module.Flat A' M' ∧
        Nonempty ((P ⊗[P'] M') ≃ₗ[P] M)) ↔
      (∃ (N' : Type u) (_ : AddCommGroup N') (_ : Module Q' N') (_ : Module A' N')
        (_ : IsScalarTower A' Q' N'), Module.Flat A' N' ∧
        Nonempty ((Q ⊗[Q'] N') ≃ₗ[Q] N))
```

## Tag 0DZ3, a lemma

[Tag 0DZ3](https://stacks.math.columbia.edu/tag/0DZ3) in the Stacks Project.

**`Deformation.hasFlatAlgebraLift_iff_hasFlatAlgebraLift_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FlatAlgebraLiftCompletionNilpotent.lean, line 348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/FlatAlgebraLiftCompletionNilpotent.lean#L348). The attribute's comment: “`Spec(B) → Spec(A)` being syntomic on the complement of `V(𝔟)` is read pointwise and affinely: for every prime `𝔮` not containing `𝔟` there is `g ∉ 𝔮` with `A → B_g` syntomic, the characterization of Stacks 00SY and 01UE. `B^∧` is `AdicCompletion 𝔟 B`. The published proof rests on Stacks 0DZ2, which is false at a nilpotent kernel; the proof here approximates a flat lift over the completed presentation by relation solutions over the polynomial presentation and corrects them one power of the kernel at a time (Artin-Rees plus Stacks 07M8 at every level). See the module docstring.”.

> **Stacks 0DZ3.** Let `A' → A` be a surjective map of Noetherian rings with nilpotent kernel,
> let `A → B` be a finite type flat ring map and let `𝔟 ⊆ B` be an ideal such that
> `Spec(B) → Spec(A)` is syntomic on the complement of `V(𝔟)`. Then `B` has a flat lift to `A'` if
> and only if the `𝔟`-adic completion `B^∧` has a flat lift to `A'`.
>
> `Spec(B) → Spec(A)` is syntomic at the point `𝔮` exactly when `A → B_g` is syntomic for some
> `g ∉ 𝔮` (Stacks 00SY, 01UE); that is how the hypothesis `hsyn` reads the source's condition at
> every point `𝔮` of the complement of `V(𝔟)`. The proof does not go through Stacks 0DZ2 (which is
> false at a nilpotent kernel); see the module documentation.

```lean
public theorem hasFlatAlgebraLift_iff_hasFlatAlgebraLift_adicCompletion
    (A' A B : Type u) [CommRing A'] [CommRing A] [CommRing B]
    [IsNoetherianRing A'] [IsNoetherianRing A] [Algebra A' A] [Algebra A B]
    (hsurjA : Function.Surjective (algebraMap A' A))
    (hnilA : IsNilpotent (RingHom.ker (algebraMap A' A)))
    [Algebra.FiniteType A B] [Module.Flat A B] (b : Ideal B)
    (hsyn : ∀ q : Ideal B, q.IsPrime → ¬ b ≤ q →
      ∃ g ∉ q, Algebra.Syntomic A (Localization.Away g)) :
    HasFlatAlgebraLift A' A B ↔ HasFlatAlgebraLift A' A (AdicCompletion b B)
```

## Tag 0DZ4, a lemma

[Tag 0DZ4](https://stacks.math.columbia.edu/tag/0DZ4) in the Stacks Project.

**`Deformation.Examples.exists_squareZeroAlgebraExtensionClassesCompletionEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/CompletionFirstOrder.lean, line 1035](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/CompletionFirstOrder.lean#L1035).

> **Stacks 0DZ4.** For a finite type algebra `B` over a field `k` which is smooth over `k`
> outside the zero set of an ideal `J`, and a finite `B`-module `N`, completion along `J` is a
> bijection from the isomorphism classes of square-zero extensions of `B` by `N` to those of `B^`
> by `N^`, matching a class with its image exactly when the two extensions admit a `k`-algebra map
> of middle rings over `B → B^` and over `N → N^`.

```lean
public theorem exists_squareZeroAlgebraExtensionClassesCompletionEquiv
    (k : Type uk) (B : Type uB) [Field k] [CommRing B] [Algebra k B]
    [Algebra.FiniteType k B] (J : Ideal B)
    (hsm : ∀ q : PrimeSpectrum B, ¬ J ≤ q.asIdeal → Algebra.IsSmoothAt k q.asIdeal)
    (N : Type uN) [AddCommGroup N] [Module B N] [Module.Finite B N] :
    ∃ e : SquareZeroExtensionProblem.CompatibleExtension.IsomorphismClasses.{uk, uk, uB, uN,
        max uB uN} (algebraExtensionProblem k B N) ≃
      SquareZeroExtensionProblem.CompatibleExtension.IsomorphismClasses.{uk, uk, uB, uN,
        max uB uN} (algebraExtensionProblem k (AdicCompletion J B) (AdicCompletion J N)),
      ∀ (X : (algebraExtensionProblem k B N).CompatibleExtension.{max uB uN})
        (Y : (algebraExtensionProblem k (AdicCompletion J B)
          (AdicCompletion J N)).CompatibleExtension.{max uB uN}),
        (∃ h : X.B' →ₐ[k] Y.B',
            (∀ z : X.B', Y.toB (h z) = algebraMap B (AdicCompletion J B) (X.toB z)) ∧
              ∀ n : N, h (kernelInclusion X n) =
                kernelInclusion Y (AdicCompletion.of J N n)) ↔
          e ⟦X⟧ = ⟦Y⟧
```

## Tag 0DZ5, a lemma

[Tag 0DZ5](https://stacks.math.columbia.edu/tag/0DZ5) in the Stacks Project.

**`Deformation.Examples.isSmooth_and_bijective_differential_adicCompletionFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/CompletionSmooth.lean, line 540](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/CompletionSmooth.lean#L540). The attribute's comment: “both conclusions, at the completion functor `Deformation.Examples.adicCompletionFunctor` of Stacks 0DYV: it is smooth, and its differential on tangent spaces is bijective. The hypotheses are the source's: `P` of finite type over the field `k`, and `P` smooth over `k` at every prime not containing `J`”.

> **Stacks 0DZ5.** Let `k` be a field, `P` a finite type `k`-algebra, `J ⊆ P` an ideal such
> that `Spec(P) → Spec(k)` is smooth on the complement of `V(J)`, and `P^` the `J`-adic
> completion. Then the completion functor `𝓓_P ⟶ 𝓓_{P^}` of **Stacks 0DYV**
> (`Deformation.Examples.adicCompletionFunctor`) is smooth and induces an isomorphism on tangent
> spaces.
>
> As in the source, this is the criterion of **Stacks 0DYP** applied to the two inputs: the
> isomorphism on tangent spaces, from **Stacks 0DZ4** with `N = B`
> (`Deformation.Examples.bijective_differential_adicCompletionFunctor`), and the correspondence of
> liftability, from **Stacks 0DZ3** at a small extension
> (`Deformation.Examples.lifts_adicCompletionFunctorData_unconditional`), which together give
> smoothness (`Deformation.Examples.isSmooth_adicCompletionFunctor`).

```lean
theorem isSmooth_and_bijective_differential_adicCompletionFunctor [Algebra.FiniteType k P]
    (hsm : ∀ q : PrimeSpectrum P, ¬ J ≤ q.asIdeal → Algebra.IsSmoothAt k q.asIdeal) :
    letI : IsNoetherianRing P := Algebra.FiniteType.isNoetherianRing k P
    IsSmooth (adicCompletionFunctor (Λ := Λ) (k := k) P J).functor ∧
      Function.Bijective (differential (𝓕 := ringDeformationBasedCategory Λ k P)
        (𝓖 := ringDeformationBasedCategory Λ k (AdicCompletion J P))
        isCofiberedInGroupoids_ringDeformationProjection
        isCofiberedInGroupoids_ringDeformationProjection
        (adicCompletionFunctor (Λ := Λ) (k := k) P J).functor)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 93.12, Tag 0DZ0](https://stacks.math.columbia.edu/tag/0DZ0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
