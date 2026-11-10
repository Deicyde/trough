---
declaration: section
origin: cited
lean: Deformation.Examples.DerivedLift.exists_flat_lift_iff_exists_derived_lift, Deformation.HasFlatModuleLift.baseChange, Deformation.exists_flat_lift_iff_exists_flat_lift_baseChange_of_localizationLift_of_isNilpotent_ker, Deformation.exists_flat_lift_iff_exists_flat_lift_baseChange_of_localizationLift, Deformation.hasFlatAlgebraLift_iff_hasFlatAlgebraLift_adicCompletion, Deformation.Examples.exists_squareZeroAlgebraExtensionClassesCompletionEquiv, Deformation.Examples.isSmooth_adicCompletionFunctorData_unconditional, Deformation.Examples.bijective_differential_adicCompletionFunctor
statement: formalized
proof: formalized
---

# 93.12 Deformations of completions

Section 93.12 of the Stacks Project, [Tag 0DZ0](https://stacks.math.columbia.edu/tag/0DZ0). 5 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DZ1, a lemma

[Tag 0DZ1](https://stacks.math.columbia.edu/tag/0DZ1) in the Stacks Project.

**`Deformation.Examples.DerivedLift.exists_flat_lift_iff_exists_derived_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/BaseChangeIndependence/DerivedLift.lean, line 481](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/BaseChangeIndependence/DerivedLift.lean#L481).

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

**`Deformation.HasFlatModuleLift.baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FlatModuleLift.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FlatModuleLift.lean#L280). The attribute's comment: “the implication (1) => (2) of 0DZ2, in full, at the source's hypotheses and with no hypothesis added. This is what the tag asserts in this library: the converse is FALSE at the source's hypotheses, a Stacks ERRATUM. The biconditional is refuted, at every universe, by `Deformation.Examples.ArtinSchreier.not_flatModuleLiftBaseChangeStatement`, and in the form that writes out every one of the source's hypotheses by `Deformation.Examples.ArtinSchreier.not_flatModuleLiftBaseChangeStatementFaithful`. Inside the forward implication nothing is restricted: it carries the source's own nilpotence hypothesis on the kernel of `P' → P` and is more general than the source in needing neither the Noetherian hypotheses, nor finiteness of `M`, nor the ideal `J'`, nor the local liftability hypothesis, and every binder it does carry is used. A restricted converse — a finite `M` under a square-zero thickening `P' → P` — is proved in `StacksFrontier.Deformation.FlatModuleLiftLocalization`, whose clause records why the dévissage to the source's nilpotent thickening is not merely unavailable from 0DZ2's hypotheses but closed: the step it needs is `Deformation.ObstructionIndependentOfLift` and that statement is unsatisfiable, by `Deformation.not_obstructionIndependentOfLift`”.

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

**`Deformation.exists_flat_lift_iff_exists_flat_lift_baseChange_of_localizationLift_of_isNilpotent_ker`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FlatModuleLiftLocalization.lean, line 584](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FlatModuleLiftLocalization.lean#L584). The attribute's comment: “a RESTRICTED form of 0DZ2, restricted by exactly two hypotheses: `hzeroP`, which asks the thickening `P' → P` to be square-zero rather than merely nilpotent, and `Module.Finite P M`, which asks `M` to be finite over `P`. NEITHER IS REMOVABLE, because the UNRESTRICTED statement is FALSE — a Stacks ERRATUM — so what 0DZ2 asserts in this library is the implication (1) => (2), registered on `Deformation.HasFlatModuleLift.baseChange`. It is refuted, at every universe, by `Deformation.Examples.ArtinSchreier.not_flatModuleLiftBaseChangeStatement`, and in the form that writes out every one of the source's hypotheses by `Deformation.Examples.ArtinSchreier.not_flatModuleLiftBaseChangeStatementFaithful`. That witness satisfies both of the hypotheses whose removal is at issue in the other direction: its `ker(A' → A) = (t)` has `t³ = 0` and `t² ≠ 0`, so it is nilpotent and not square-zero, and its `M` IS finite over `P`. What follows is why each restriction is there. Corrected: `M` is assumed finite over `P`. The source's statement omits it, its own proof uses it — `here we use that P is Noetherian and M finite`, when invoking Stacks 0A6A to commute `Ext²` with the flat base change `P → Q` — and that step is FALSE without it, not merely unproved: for `k` countable, `P = k[x, y]`, `Q = k[[x, y]]`, `A' = k[ε]/(ε²)`, `J' = (x, y)` and the non-finite `A`-flat module `M = ⨁ₙ P/(xⁿ, yⁿ)`, the comparison `Ext²_P(M, M ⊗_P IP) ⊗_P Q → Ext²_Q(M ⊗_P Q, (M ⊗_P Q) ⊗_Q IQ)` is the multiplication map `T ⊗_P Q → T` of a copy of `Q` sitting inside the infinite product `T` that `Ext` out of an infinite direct sum produces, and `Q ⊗_P Q → Q` has a nonzero kernel. Nothing weaker will do either: over the Noetherian `P` that 0DZ2 assumes, the `(-3)`-pseudo-coherence that Stacks 087Q needs in degree `2` is equivalent to finiteness. The computation, and the Mayer–Vietoris identification of what a finiteness-free proof would still owe, are in the implementation notes of this file; the equivalence itself is not refuted for a non-finite `M`, only the source's proof of it. Also: the thickening `P' → P` is assumed square-zero rather than merely nilpotent, which is what the obstruction calculus of Stacks 0DYR needs in order to have an obstruction class at all. Those are the only two deviations: the kernel of `A' → A` itself is assumed only nilpotent, as in the source, and squareness of the second thickening `Q' → Q` is derived rather than assumed, by `Deformation.sq_ker_algebraMap_tensorProduct_eq_bot_of_tower`; so this statement is strictly stronger than the one registered on `Deformation.exists_flat_lift_iff_exists_flat_lift_baseChange_of_localizationLift`. The dévissage from the square-zero thickening to the source's nilpotent one is NOT available from 0DZ2's own hypotheses. The source's reduction is `details omitted`; with `A'' = A'/I^{n-1}` every hypothesis of the lemma transports to the stage `A'' → A`, including local liftability, which reduces along the already-proved forward direction, so the induction produces an `A''`-flat `P''`-lift `M''` of `M` — and then needs the obstruction class of the square-zero step `A' → A''` to be independent of which `A''`-flat `P''`-lift of `M` it is evaluated on. Grant that and the induction closes; it is false already for `I³ = 0`. All of this is now a Lean object rather than a paragraph: the tower of quotients is `Deformation.squareZero_devissage`, a lift across one step of it is a lift across the composite by `Deformation.hasFlatModuleLift_comp`, the generic step of the induction with its missing input named is `Deformation.hasFlatModuleLift_of_obstructionIndependentOfLift`, that input is `Deformation.ObstructionIndependentOfLift`, and it is UNSATISFIABLE — `Deformation.not_obstructionIndependentOfLift`, at every universe, by the elementary witness `A' = ℤ/8`, `Q' = A'[ε]/(ε²)`, where the two lifts `Q''/(ε)` and `Q''/(ε − 2)` over `Q'' = Q'/4Q'` have the same reduction and only the first lifts. So the source's route to the nilpotent case is closed, not untried. In the shape the source's own `k` would take it: over `A' = k[t]/(t³)`, `P' = k[t, x]/(t³, x²)`, the module `M = k` has the `A'`-flat `P'`-lift `P'/(x)`, while its `A''`-flat `P''`-lift `P''/(x - t)` has none, the two obstructions differing by the Yoneda square of the separating class in `Ext¹_{k[x]/(x²)}(k, k)`; and that is a legitimate instance of 0DZ2, with `Q' = P'` and `J' = P'`. Selecting `M''` instead by `Q'' ⊗ M'' ≅ N''` would need base change to be surjective on isomorphism classes of lifts, i.e. `Ext¹_P(M, M ⊗_P ĪP)` to be `J'`-power torsion by Stacks 0A6A and 05EC, which fails already for a hypersurface `M = P/(f)`. Full diagnosis in the implementation notes of this file”.

> **Stacks 0DZ2 with the source's local liftability hypothesis, at the source's nilpotence
> hypothesis.** Let `A' → A` be a surjection of commutative rings with nilpotent kernel whose
> thickening `P' → P` is square-zero, let `P'` and `Q'` be flat `A'`-algebras with
> `P' → Q'` flat, let `P = P' ⊗_{A'} A` and `Q = Q' ⊗_{A'} A` with `P` Noetherian and
> `P/J'P ≅ Q/J'Q` for an ideal `J'` of `P'`, and let `N` be the base change to `Q` of a `P`-module
> `M` finite over `P` and flat over `A`. If for every `g ∈ J'` the base change of `M` to the
> localization of `P` at the image of `g` has an `A'`-flat module lift over `(P')_g`, then `M` has
> an `A'`-flat lift to a `P'`-module if and only if `N` has an `A'`-flat lift to a `Q'`-module.
>
> This is `exists_flat_lift_iff_exists_flat_lift_baseChange_of_localizationLift` with the
> hypothesis `ker(A' → A)² = ⊥` dropped, so that the kernel of `A' → A` carries only the
> nilpotence the source assumes; what remains square-zero is the single thickening `P' → P`,
> squareness of `Q' → Q` being derived from it by
> `Deformation.sq_ker_algebraMap_tensorProduct_eq_bot_of_tower`.
>
> Flatness of `N` over `A` is not assumed, in either form: `N` is isomorphic to `Q ⊗_P M` and `M`
> is `A`-flat, so `flat_base_of_baseChangeEquiv` supplies it. The source does not assume it either.
>
> The localization of `P` at the image of `g` is realized as `(P')_g ⊗_{A'} A`, which
> `IsLocalization.Away.tensorBaseChange` identifies with it.

```lean
theorem exists_flat_lift_iff_exists_flat_lift_baseChange_of_localizationLift_of_isNilpotent_ker
    (A' A P' Q' : Type u) [CommRing A'] [CommRing A] [CommRing P'] [CommRing Q']
    [Algebra A' A] [Algebra A' P'] [Algebra A' Q'] [Algebra P' Q'] [IsScalarTower A' P' Q']
    [Module.Flat A' P'] [Module.Flat P' Q']
    (hsurjA : Function.Surjective (algebraMap A' A))
    (hnilA : IsNilpotent (RingHom.ker (algebraMap A' A)))
    (hzeroP : (RingHom.ker (algebraMap P' (TensorProduct A' P' A))) ^ 2 = ⊥)
    [Algebra (TensorProduct A' P' A) (TensorProduct A' Q' A)]
    [IsNoetherianRing (TensorProduct A' P' A)]
    (hcomm : (algebraMap (TensorProduct A' P' A) (TensorProduct A' Q' A)).comp
        (algebraMap P' (TensorProduct A' P' A)) =
      (algebraMap Q' (TensorProduct A' Q' A)).comp (algebraMap P' Q'))
    (hflatPQ : Module.Flat (TensorProduct A' P' A) (TensorProduct A' Q' A))
    (J' : Ideal P')
    (hquot : Function.Bijective (Ideal.quotientMap
      ((J'.map (algebraMap P' (TensorProduct A' P' A))).map
        (algebraMap (TensorProduct A' P' A) (TensorProduct A' Q' A)))
      (algebraMap (TensorProduct A' P' A) (TensorProduct A' Q' A)) Ideal.le_comap_map))
    (M : Type u) [AddCommGroup M] [Module (TensorProduct A' P' A) M] [Module A M]
    [IsScalarTower A (TensorProduct A' P' A) M] [Module.Flat A M]
    [Module.Finite (TensorProduct A' P' A) M]
    (N : Type u) [AddCommGroup N] [Module (TensorProduct A' Q' A) N] [Module A N]
    [IsScalarTower A (TensorProduct A' Q' A) N]
    (hN : Nonempty ((ModuleCat.extendScalars.{u, u, u}
        (algebraMap (TensorProduct A' P' A) (TensorProduct A' Q' A))).obj
          (ModuleCat.of (TensorProduct A' P' A) (ULift.{u} M)) ≅
      ModuleCat.of (TensorProduct A' Q' A) (ULift.{u} N)))
    (K : DerivedCategory (ModuleCat.{u} (TensorProduct A' P' A)))
    (hK : (DerivedCategory.TStructure.t
      (C := ModuleCat.{u} (TensorProduct A' P' A))).minus K)
    (eK : K ≅ DerivedCategory.Q.obj ((CochainComplex.singleFunctor
      (ModuleCat.{u} (TensorProduct A' P' A)) 0).obj
        (ModuleCat.of (TensorProduct A' P' A) (ULift.{u} M))))
    (hlocal : ∀ g ∈ J',
      letI : Algebra (TensorProduct A' P' A) (TensorProduct A' (Localization.Away g) A) :=
        (Algebra.TensorProduct.map (IsScalarTower.toAlgHom A' P' (Localization.Away g))
          (AlgHom.id A' A)).toRingHom.toAlgebra
      ∃ (L : Type u) (_ : AddCommGroup L) (_ : Module (Localization.Away g) L)
        (_ : Module A' L) (_ : IsScalarTower A' (Localization.Away g) L),
        Module.Flat A' L ∧ Nonempty
          ((ModuleCat.extendScalars.{u, u, u} (algebraMap (Localization.Away g)
              (TensorProduct A' (Localization.Away g) A))).obj
                (ModuleCat.of (Localization.Away g) L) ≅
            ModuleCat.of (TensorProduct A' (Localization.Away g) A)
              (ULift.{u} (TensorProduct (TensorProduct A' P' A)
                (TensorProduct A' (Localization.Away g) A) (ULift.{u} M))))) :
    (∃ (M' : Type u) (_ : AddCommGroup M') (_ : Module P' M') (_ : Module A' M')
        (_ : IsScalarTower A' P' M'), Module.Flat A' M' ∧
        Nonempty ((ModuleCat.extendScalars.{u, u, u}
            (algebraMap P' (TensorProduct A' P' A))).obj (ModuleCat.of P' M') ≅
          ModuleCat.of (TensorProduct A' P' A) (ULift.{u} M))) ↔
      (∃ (N' : Type u) (_ : AddCommGroup N') (_ : Module Q' N') (_ : Module A' N')
        (_ : IsScalarTower A' Q' N'), Module.Flat A' N' ∧
        Nonempty ((ModuleCat.extendScalars.{u, u, u}
            (algebraMap Q' (TensorProduct A' Q' A))).obj (ModuleCat.of Q' N') ≅
          ModuleCat.of (TensorProduct A' Q' A) (ULift.{u} N)))
```

**`Deformation.exists_flat_lift_iff_exists_flat_lift_baseChange_of_localizationLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FlatModuleLiftLocalization.lean, line 716](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FlatModuleLiftLocalization.lean#L716). The attribute's comment: “a RESTRICTED form of 0DZ2, restricted by `hzeroA` — the kernel of `A' → A` is assumed square-zero rather than merely nilpotent — and by `Module.Finite P M`. NEITHER IS REMOVABLE: the UNRESTRICTED statement is FALSE — a Stacks ERRATUM — so what 0DZ2 asserts in this library is the implication (1) => (2), registered on `Deformation.HasFlatModuleLift.baseChange`. It is refuted at every universe by `Deformation.Examples.ArtinSchreier.not_flatModuleLiftBaseChangeStatement` and, with every source hypothesis written out, by `Deformation.Examples.ArtinSchreier.not_flatModuleLiftBaseChangeStatementFaithful`, whose witness has a nilpotent non-square-zero `ker(A' → A)` and a finite `M`. Why each restriction is there: `M` is assumed finite over `P` — the source's statement omits it, its own proof uses it when invoking Stacks 0A6A to commute `Ext²` with the flat base change `P → Q`, and that step is false without it, by the counterexample written out in the implementation notes of this file; and the kernel of `A' → A` is assumed square-zero rather than merely nilpotent, which is what makes both the nilpotence of that kernel and squareness of the thickening `P' → P` theorems here rather than hypotheses. This is the weaker of the two registrations: `exists_flat_lift_iff_exists_flat_lift_baseChange_of_localizationLift_of_isNilpotent_ker` carries the source's nilpotence on that kernel and asks squareness only of the thickening `P' → P`, and the clause there records why the dévissage to the source's nilpotent thickening is not available from 0DZ2's own hypotheses”.

> **Stacks 0DZ2 with the source's local liftability hypothesis.** Let `A' → A` be a surjection
> of commutative rings with square-zero kernel, let `P'` and `Q'` be flat `A'`-algebras with
> `P' → Q'` flat, let `P = P' ⊗_{A'} A` and `Q = Q' ⊗_{A'} A` with `P` Noetherian and
> `P/J'P ≅ Q/J'Q` for an ideal `J'` of `P'`, and let `N` be the base change to `Q` of a `P`-module
> `M` finite over `P` and flat over `A`. If for every `g ∈ J'` the base change of `M` to the
> localization of `P` at the image of `g` has an `A'`-flat module lift over `(P')_g`, then `M` has
> an `A'`-flat lift to a `P'`-module if and only if `N` has an `A'`-flat lift to a `Q'`-module.
>
> Flatness of `N` over `A` is not assumed here either; see
> `exists_flat_lift_iff_exists_flat_lift_baseChange_of_localizationLift_of_isNilpotent_ker`.
>
> The localization of `P` at the image of `g` is realized as `(P')_g ⊗_{A'} A`, which
> `IsLocalization.Away.tensorBaseChange` identifies with it.

```lean
theorem exists_flat_lift_iff_exists_flat_lift_baseChange_of_localizationLift
    (A' A P' Q' : Type u) [CommRing A'] [CommRing A] [CommRing P'] [CommRing Q']
    [Algebra A' A] [Algebra A' P'] [Algebra A' Q'] [Algebra P' Q'] [IsScalarTower A' P' Q']
    [Module.Flat A' P'] [Module.Flat P' Q']
    (hsurjA : Function.Surjective (algebraMap A' A))
    (hzeroA : (RingHom.ker (algebraMap A' A)) ^ 2 = ⊥)
    [Algebra (TensorProduct A' P' A) (TensorProduct A' Q' A)]
    [IsNoetherianRing (TensorProduct A' P' A)]
    (hcomm : (algebraMap (TensorProduct A' P' A) (TensorProduct A' Q' A)).comp
        (algebraMap P' (TensorProduct A' P' A)) =
      (algebraMap Q' (TensorProduct A' Q' A)).comp (algebraMap P' Q'))
    (hflatPQ : Module.Flat (TensorProduct A' P' A) (TensorProduct A' Q' A))
    (J' : Ideal P')
    (hquot : Function.Bijective (Ideal.quotientMap
      ((J'.map (algebraMap P' (TensorProduct A' P' A))).map
        (algebraMap (TensorProduct A' P' A) (TensorProduct A' Q' A)))
      (algebraMap (TensorProduct A' P' A) (TensorProduct A' Q' A)) Ideal.le_comap_map))
    (M : Type u) [AddCommGroup M] [Module (TensorProduct A' P' A) M] [Module A M]
    [IsScalarTower A (TensorProduct A' P' A) M] [Module.Flat A M]
    [Module.Finite (TensorProduct A' P' A) M]
    (N : Type u) [AddCommGroup N] [Module (TensorProduct A' Q' A) N] [Module A N]
    [IsScalarTower A (TensorProduct A' Q' A) N]
    (hN : Nonempty ((ModuleCat.extendScalars.{u, u, u}
        (algebraMap (TensorProduct A' P' A) (TensorProduct A' Q' A))).obj
          (ModuleCat.of (TensorProduct A' P' A) (ULift.{u} M)) ≅
      ModuleCat.of (TensorProduct A' Q' A) (ULift.{u} N)))
    (K : DerivedCategory (ModuleCat.{u} (TensorProduct A' P' A)))
    (hK : (DerivedCategory.TStructure.t
      (C := ModuleCat.{u} (TensorProduct A' P' A))).minus K)
    (eK : K ≅ DerivedCategory.Q.obj ((CochainComplex.singleFunctor
      (ModuleCat.{u} (TensorProduct A' P' A)) 0).obj
        (ModuleCat.of (TensorProduct A' P' A) (ULift.{u} M))))
    (hlocal : ∀ g ∈ J',
      letI : Algebra (TensorProduct A' P' A) (TensorProduct A' (Localization.Away g) A) :=
        (Algebra.TensorProduct.map (IsScalarTower.toAlgHom A' P' (Localization.Away g))
          (AlgHom.id A' A)).toRingHom.toAlgebra
      ∃ (L : Type u) (_ : AddCommGroup L) (_ : Module (Localization.Away g) L)
        (_ : Module A' L) (_ : IsScalarTower A' (Localization.Away g) L),
        Module.Flat A' L ∧ Nonempty
          ((ModuleCat.extendScalars.{u, u, u} (algebraMap (Localization.Away g)
              (TensorProduct A' (Localization.Away g) A))).obj
                (ModuleCat.of (Localization.Away g) L) ≅
            ModuleCat.of (TensorProduct A' (Localization.Away g) A)
              (ULift.{u} (TensorProduct (TensorProduct A' P' A)
                (TensorProduct A' (Localization.Away g) A) (ULift.{u} M))))) :
    (∃ (M' : Type u) (_ : AddCommGroup M') (_ : Module P' M') (_ : Module A' M')
        (_ : IsScalarTower A' P' M'), Module.Flat A' M' ∧
        Nonempty ((ModuleCat.extendScalars.{u, u, u}
            (algebraMap P' (TensorProduct A' P' A))).obj (ModuleCat.of P' M') ≅
          ModuleCat.of (TensorProduct A' P' A) (ULift.{u} M))) ↔
      (∃ (N' : Type u) (_ : AddCommGroup N') (_ : Module Q' N') (_ : Module A' N')
        (_ : IsScalarTower A' Q' N'), Module.Flat A' N' ∧
        Nonempty ((ModuleCat.extendScalars.{u, u, u}
            (algebraMap Q' (TensorProduct A' Q' A))).obj (ModuleCat.of Q' N') ≅
          ModuleCat.of (TensorProduct A' Q' A) (ULift.{u} N)))
```

## Tag 0DZ3, a lemma

[Tag 0DZ3](https://stacks.math.columbia.edu/tag/0DZ3) in the Stacks Project.

**`Deformation.hasFlatAlgebraLift_iff_hasFlatAlgebraLift_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FlatAlgebraLiftCompletionNilpotent.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FlatAlgebraLiftCompletionNilpotent.lean#L348). The attribute's comment: “`Spec(B) → Spec(A)` being syntomic on the complement of `V(𝔟)` is read pointwise and affinely: for every prime `𝔮` not containing `𝔟` there is `g ∉ 𝔮` with `A → B_g` syntomic, the characterization of Stacks 00SY and 01UE. `B^∧` is `AdicCompletion 𝔟 B`. The published proof rests on Stacks 0DZ2, which is false at a nilpotent kernel; the proof here approximates a flat lift over the completed presentation by relation solutions over the polynomial presentation and corrects them one power of the kernel at a time (Artin-Rees plus Stacks 07M8 at every level). See the module docstring.”.

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

**`Deformation.Examples.exists_squareZeroAlgebraExtensionClassesCompletionEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/CompletionFirstOrder.lean, line 1035](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/CompletionFirstOrder.lean#L1035).

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

**`Deformation.Examples.isSmooth_adicCompletionFunctorData_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/CompletionSmooth.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/CompletionSmooth.lean#L457). The attribute's comment: “the first conclusion, smoothness, over an arbitrary base-compatible completion functor datum, and unconditionally: no hypothesis stands for Stacks 0DZ2, because only the square-zero case of Stacks 0DZ3 is consumed and that case is proved in `StacksFrontier.Deformation.FlatModuleLiftBaseChangeAbstract`. The second conclusion, the isomorphism on tangent spaces, is `Deformation.Examples.bijective_differential_adicCompletionFunctorData` over the same data. RESTRICTED in the same way as that declaration, to a datum satisfying `Deformation.Examples.AdicCompletionFunctorData.IsBaseCompatible`; at the canonical choice the conclusion is `Deformation.Examples.isSmooth_adicCompletionFunctor`”. References: SGA 7 VI (4.13), “(a), special case”.

> **Stacks 0DZ5, the smoothness conclusion.** Let `k` be a field, `P` a finite type
> `k`-algebra, `J ⊆ P` an ideal such that `Spec(P) → Spec(k)` is smooth outside `V(J)`, and `P^`
> the `J`-adic completion. The completion functor `𝓓_P ⟶ 𝓓_{P^}` of **Stacks 0DYV** is smooth.
>
> The criterion of **Stacks 0DYP** reduces this to surjectivity of the differential, which is
> `Deformation.Examples.bijective_differential_adicCompletionFunctorData`, and to the
> correspondence of liftability, which is
> `Deformation.Examples.lifts_adicCompletionFunctorData_unconditional`.

```lean
theorem isSmooth_adicCompletionFunctorData_unconditional [Algebra.FiniteType k P]
    (F : AdicCompletionFunctorData (Λ := Λ) (k := k) P J) (hF : F.IsBaseCompatible)
    (hsm : ∀ q : PrimeSpectrum P, ¬ J ≤ q.asIdeal → Algebra.IsSmoothAt k q.asIdeal) :
    IsSmooth F.functor
```

**`Deformation.Examples.bijective_differential_adicCompletionFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/CompletionSmooth.lean, line 512](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/CompletionSmooth.lean#L512). The attribute's comment: “the second conclusion only: the functor induces an isomorphism on tangent spaces. The first conclusion, smoothness, is `Deformation.Examples.isSmooth_adicCompletionFunctor`”.

> **Stacks 0DZ5, the tangent-space conclusion.** This is
> `Deformation.Examples.bijective_differential_adicCompletionFunctorData` specialized to the
> completion functor `Deformation.Examples.adicCompletionFunctor` of **Stacks 0DYV**, whose
> base-compatibility is `Deformation.Examples.isBaseCompatible_adicCompletionFunctor`; so no
> hypothesis on the functor remains.

```lean
theorem bijective_differential_adicCompletionFunctor [Algebra.FiniteType k P]
    (hsm : ∀ q : PrimeSpectrum P, ¬ J ≤ q.asIdeal → Algebra.IsSmoothAt k q.asIdeal) :
    letI : IsNoetherianRing P := Algebra.FiniteType.isNoetherianRing k P
    Function.Bijective (differential (𝓕 := ringDeformationBasedCategory Λ k P)
      (𝓖 := ringDeformationBasedCategory Λ k (AdicCompletion J P))
      isCofiberedInGroupoids_ringDeformationProjection
      isCofiberedInGroupoids_ringDeformationProjection
      (adicCompletionFunctor (Λ := Λ) (k := k) P J).functor)
```

**`Deformation.Examples.isSmooth_adicCompletionFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/CompletionSmooth.lean, line 532](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/CompletionSmooth.lean#L532). The attribute's comment: “the first conclusion, smoothness. The second conclusion, the isomorphism on tangent spaces, is `Deformation.Examples.bijective_differential_adicCompletionFunctor`”.

> **Stacks 0DZ5, the smoothness conclusion.** This is
> `Deformation.Examples.isSmooth_adicCompletionFunctorData_unconditional` specialized to the
> completion functor `Deformation.Examples.adicCompletionFunctor` of **Stacks 0DYV**, whose
> base-compatibility is `Deformation.Examples.isBaseCompatible_adicCompletionFunctor`; so no
> hypothesis on the functor remains.

```lean
theorem isSmooth_adicCompletionFunctor [Algebra.FiniteType k P]
    (hsm : ∀ q : PrimeSpectrum P, ¬ J ≤ q.asIdeal → Algebra.IsSmoothAt k q.asIdeal) :
    letI : IsNoetherianRing P := Algebra.FiniteType.isNoetherianRing k P
    IsSmooth (adicCompletionFunctor (Λ := Λ) (k := k) P J).functor
```

**`Deformation.Examples.bijective_differential_baseCompatibleAdicCompletionFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/CompletionSmooth.lean, line 568](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/CompletionSmooth.lean#L568). The attribute's comment: “the second conclusion only: the functor induces an isomorphism on tangent spaces. Stated at the canonical base-compatible completion functor datum `Deformation.Examples.baseCompatibleAdicCompletionFunctor` rather than over an arbitrary datum, so there is no hypothesis on the functor; it is still RESTRICTED to a base-compatible datum. The first conclusion, smoothness, is proved over an arbitrary base-compatible datum by `Deformation.Examples.isSmooth_adicCompletionFunctorData_unconditional`, and at `Deformation.Examples.adicCompletionFunctor` by `Deformation.Examples.isSmooth_adicCompletionFunctor`”.

> **Stacks 0DZ5, the tangent-space conclusion, at the canonical base-compatible completion
> functor.** This is `Deformation.Examples.bijective_differential_adicCompletionFunctorData`
> specialized to `Deformation.Examples.baseCompatibleAdicCompletionFunctor`, whose
> base-compatibility is its own second component; so no hypothesis on the functor remains.

```lean
theorem bijective_differential_baseCompatibleAdicCompletionFunctor
    [Algebra.FiniteType k P] [IsNoetherianRing P]
    (hsm : ∀ q : PrimeSpectrum P, ¬ J ≤ q.asIdeal → Algebra.IsSmoothAt k q.asIdeal) :
    Function.Bijective (differential (𝓕 := ringDeformationBasedCategory Λ k P)
      (𝓖 := ringDeformationBasedCategory Λ k (AdicCompletion J P))
      isCofiberedInGroupoids_ringDeformationProjection
      isCofiberedInGroupoids_ringDeformationProjection
      (baseCompatibleAdicCompletionFunctor (Λ := Λ) (k := k) P J).1.functor)
```

**`Deformation.Examples.bijective_differential_adicCompletionFunctorData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/CompletionTangentSpace.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/CompletionTangentSpace.lean#L360). The attribute's comment: “the second conclusion only: the functor induces an isomorphism on tangent spaces. The first conclusion, smoothness, is not proved here; granted the correspondence of liftability it is `Deformation.Examples.isSmooth_adicCompletionFunctorData_of_lifts`. RESTRICTED: the statement is for any completion functor datum of Stacks 0DYV which in addition satisfies `Deformation.Examples.AdicCompletionFunctorData.IsBaseCompatible`, and such data exist by `Deformation.Examples.nonempty_isBaseCompatible_adicCompletionFunctorData`; it is not for the arbitrary choice `Deformation.Examples.adicCompletionFunctor`, which satisfies only the clauses recorded in Stacks 0DYV. See the implementation notes”.

> **Stacks 0DZ5, the tangent-space conclusion.** Let `k` be a field, `P` a finite type
> `k`-algebra, `J ⊆ P` an ideal such that `Spec(P) → Spec(k)` is smooth outside `V(J)`, and `P^`
> the `J`-adic completion. The completion functor `𝓓_P ⟶ 𝓓_{P^}` of **Stacks 0DYV** induces a
> bijection on tangent spaces.
>
> The proof is the source's: the family of extension classes of **Stacks 0DY3** is a bijection of
> each tangent space with a first Ext group of the naive cotangent complex, by
> `Deformation.Examples.bijective_tangentExtClass`; the functor is compatible with those classes
> through the two comparison maps of **Stacks 0GPV**, by
> `Deformation.Examples.squareZeroFiberExtClass_completion`; and both comparison maps are
> bijective by **Stacks 0DZ4**.

```lean
public theorem bijective_differential_adicCompletionFunctorData
    [Algebra.FiniteType k P]
    (F : AdicCompletionFunctorData (Λ := Λ) (k := k) P J) (hF : F.IsBaseCompatible)
    (hsm : ∀ q : PrimeSpectrum P, ¬ J ≤ q.asIdeal → Algebra.IsSmoothAt k q.asIdeal) :
    Function.Bijective (differential (𝓕 := ringDeformationBasedCategory Λ k P)
      (𝓖 := ringDeformationBasedCategory Λ k (AdicCompletion J P))
      isCofiberedInGroupoids_ringDeformationProjection
      isCofiberedInGroupoids_ringDeformationProjection F.functor)
```

**`Deformation.Examples.isSmooth_adicCompletionFunctorData_of_lifts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/CompletionTangentSpace.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/CompletionTangentSpace.lean#L435). The attribute's comment: “the first conclusion, smoothness, GRANTED the hypothesis `hlifts`: that a deformation lifts along a small extension of its Artinian base whenever its completion does. That correspondence of liftability is the deformation-category reading of Stacks 0DZ3 and is NOT proved here, so this declaration is not the conclusion of the tag. The tag's other input, surjectivity of the differential, is supplied in full from `Deformation.Examples.bijective_differential_adicCompletionFunctorData`, and the reduction to the two inputs is Stacks 0DYP. RESTRICTED in the same way as that declaration, to a base-compatible completion functor datum. See the implementation notes”.

> **Stacks 0DZ5, the smoothness conclusion, granted the correspondence of liftability.**
> Under the hypotheses of Stacks 0DZ5, the completion functor `𝓓_P ⟶ 𝓓_{P^}` is smooth as soon as
> liftability of a deformation along a small extension of the Artinian base is implied by
> liftability of its completion.
>
> That implication is the deformation-category reading of **Stacks 0DZ3** and is the only input
> missing: the other half of the criterion of **Stacks 0DYP**, surjectivity of the differential,
> is `Deformation.Examples.bijective_differential_adicCompletionFunctorData`.

```lean
public theorem isSmooth_adicCompletionFunctorData_of_lifts
    [Algebra.FiniteType k P]
    (F : AdicCompletionFunctorData (Λ := Λ) (k := k) P J) (hF : F.IsBaseCompatible)
    (hsm : ∀ q : PrimeSpectrum P, ¬ J ≤ q.asIdeal → Algebra.IsSmoothAt k q.asIdeal)
    (hlifts : ∀ ⦃B A : ArtinianLocalAlgCat.{u, w, w} Λ k⦄ (f : B ⟶ A),
      InfinitesimalLifting.IsSmallExtension (CommRingCat.ofHom f.hom.toRingHom) →
        ∀ x : (ringDeformationBasedCategory Λ k P).p.Fiber A,
          (∃ (y' : (ringDeformationBasedCategory Λ k (AdicCompletion J P)).obj)
              (g : y' ⟶ F.functor.obj x.1),
            (ringDeformationBasedCategory Λ k (AdicCompletion J P)).p.IsHomLift f g) →
            ∃ (x' : (ringDeformationBasedCategory Λ k P).obj) (h : x' ⟶ x.1),
              (ringDeformationBasedCategory Λ k P).p.IsHomLift f h) :
    IsSmooth F.functor
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 93.12, Tag 0DZ0](https://stacks.math.columbia.edu/tag/0DZ0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
