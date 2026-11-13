---
declaration: section
origin: cited
lean: Rig.naivelyRigFlat_tfae, Rig.RingHom.IsNaivelyRigFlat, Rig.exists_isNaivelyRigFlat_not_isNaivelyRigFlat_completedAwayMap, Rig.RingHom.IsRigFlat, Rig.RingHom.isRigFlat_of_isNaivelyRigFlat_of_isJacobsonRing_quotient, AlgebraicGeometry.FormalSpace.isRigFlat_completedTensorProduct_baseChange, Rig.flat_atPrime_completedTensorProduct_restrictedPowerSeries, Rig.isRigFlat_of_flat_etale_square
statement: formalized
proof: formalized
---

# 88.15 Rig-flat homomorphisms

Section 88.15 of the Stacks Project, [Tag 0GGK](https://stacks.math.columbia.edu/tag/0GGK). 10 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GGL, a lemma

[Tag 0GGL](https://stacks.math.columbia.edu/tag/0GGL) in the Stacks Project.

**`Rig.naivelyRigFlat_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Flat.lean, line 333](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Flat.lean#L333).

> For an adic morphism of weakly admissible adic topological rings with
> finitely generated ideals of definition, flatness after localization may be
> tested on topologically nilpotent elements of either ring, on all primes away
> from an ideal of definition, or on rig-closed primes.

```lean
public theorem naivelyRigFlat_tfae
    {A B : Type*} [CommRing A] [CommRing B]
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    (phi : A →+* B) (_hphi_continuous : Continuous phi)
    (_hA_weaklyAdmissible : TopologicalRing.IsWeaklyAdmissible A)
    (_hB_weaklyAdmissible : TopologicalRing.IsWeaklyAdmissible B)
    (_hA_adicStar : ∃ I : Ideal A, IsAdic I ∧ I.FG)
    (_hB_adicStar : ∃ J : Ideal B, IsAdic J ∧ J.FG)
    (_hphi_adic : _root_.RingHom.IsAdic phi) :
    List.TFAE
      [ ∀ f : A, IsTopologicallyNilpotent f →
          _root_.RingHom.Flat
            ((algebraMap B (Localization.Away (phi f))).comp phi),
        ∀ g : B, IsTopologicallyNilpotent g →
          _root_.RingHom.Flat
            ((algebraMap B (Localization.Away g)).comp phi),
        ∀ (q : Ideal B) [q.IsPrime],
          (∃ J : Ideal B, TopologicalRing.IsIdealOfDefinition J ∧ ¬ J ≤ q) →
            _root_.RingHom.Flat
              ((algebraMap B (Localization.AtPrime q)).comp phi),
        ∀ (q : Ideal B) [q.IsPrime],
          (∃ J : Ideal B, TopologicalRing.IsIdealOfDefinition J ∧
            Rig.Ideal.IsMaximalAmongPrimesAvoiding J q) →
              _root_.RingHom.Flat
                ((algebraMap B (Localization.AtPrime q)).comp phi) ]
```

## Tag 0GGM, a definition

[Tag 0GGM](https://stacks.math.columbia.edu/tag/0GGM) in the Stacks Project.

**`Rig.RingHom.IsNaivelyRigFlat`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Flat.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Flat.lean#L116).

> A ring homomorphism `φ : A →+* B` is naively rig-flat if it is adic, topologically of finite
> type, and `B[1 / φ(f)]` is flat over `A` for every topologically nilpotent `f : A`.

```lean
public abbrev IsNaivelyRigFlat {A B : Type*} [CommRing A] [CommRing B]
    [TopologicalSpace A] [TopologicalSpace B] (φ : A →+* B) : Prop
```

## Tag 0GGN, an example

[Tag 0GGN](https://stacks.math.columbia.edu/tag/0GGN) in the Stacks Project.

**`Rig.exists_isNaivelyRigFlat_not_isNaivelyRigFlat_completedAwayMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/FlatRecompletionExample.lean, line 594](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/FlatRecompletionExample.lean#L594).

> **Stacks 0GGN.** Naive rig-flatness is not preserved by passing to completed principal
> localizations: there is a two-dimensional Noetherian local domain `A`, complete for a principal
> ideal `(a)`, and `f ∈ 𝔪 ∖ (a)`, such that the reduction `B` of the completed localization
> `C = (A_f)^∧` receives a naively rig-flat adic map `φ : A → B` of topological finite type —
> presented by the restricted power series ring `A{x}` with `x ↦ 1/f` — while the induced map `ψ`
> of completed principal localizations of `φ` at `f` is not naively rig-flat.

```lean
public theorem exists_isNaivelyRigFlat_not_isNaivelyRigFlat_completedAwayMap :
    ∃ (A : Type u) (_ : CommRing A) (_ : IsDomain A) (_ : IsLocalRing A)
      (_ : IsNoetherianRing A) (a f : A),
      ringKrullDim A = 2 ∧
        IsAdicComplete (Ideal.span {a}) A ∧
        f ∈ IsLocalRing.maximalIdeal A ∧
        f ∉ Ideal.span {a} ∧
        (let I : Ideal A := Ideal.span {a}
         let Af := Localization.Away f
         let If : Ideal Af := I.map (algebraMap A Af)
         let C := AdicCompletion If Af
         let B := C ⧸ nilradical C
         let φ : A →+* B := (Ideal.Quotient.mk (nilradical C)).comp (algebraMap A C)
         letI : TopologicalSpace A := I.adicTopology
         letI : TopologicalSpace B := (I.map φ).adicTopology
         (¬ IsReduced (Localization.Away (algebraMap A C a))) ∧
           (∃ θ : RestrictedPowerSeries I (Fin 1) →+* B,
             Function.Surjective θ ∧
               (∀ x : A,
                 θ (RestrictedPowerSeries.polynomialRingHom I (Fin 1) (MvPolynomial.C x)) =
                   φ x) ∧
               θ (RestrictedPowerSeries.polynomialRingHom I (Fin 1) (MvPolynomial.X 0)) =
                 Ideal.Quotient.mk (nilradical C)
                   (algebraMap Af C (IsLocalization.Away.invSelf (S := Af) f))) ∧
           (∀ q : Ideal B, q.IsPrime → φ a ∉ q → q.comap φ = ⊥) ∧
           RingHom.IsNaivelyRigFlat φ ∧
             (let B_f := Localization.Away (φ f)
              let J_f := (I.map φ).map (algebraMap B B_f)
              let I_hat := If.map (algebraMap Af C)
              let J_hat := J_f.map (algebraMap B_f (AdicCompletion J_f B_f))
              letI : TopologicalSpace C := I_hat.adicTopology
              letI : TopologicalSpace (AdicCompletion J_f B_f) := J_hat.adicTopology
              let ψ := RingHom.completedAwayMap φ I f
              (∃ e : AdicCompletion J_f B_f ≃+* B,
                (∀ b : B, e ((algebraMap B_f (AdicCompletion J_f B_f))
                  (algebraMap B B_f b)) = b) ∧
                (∀ c : C, e (ψ c) = Ideal.Quotient.mk (nilradical C) c)) ∧
              let a_hat : C := algebraMap Af C (algebraMap A Af a)
              (¬ _root_.RingHom.Flat (IsLocalization.Away.map (Localization.Away a_hat)
                (Localization.Away (ψ a_hat)) ψ a_hat)) ∧
                (¬ RingHom.IsNaivelyRigFlat ψ)))
```

## Tag 0GGP, a definition

[Tag 0GGP](https://stacks.math.columbia.edu/tag/0GGP) in the Stacks Project.

**`Rig.RingHom.IsRigFlat`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Flat.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Flat.lean#L182).

> A ring homomorphism is rig-flat if it is adic and topologically of finite
> type, and all the induced maps between completed principal localizations are
> naively rig-flat.

```lean
public abbrev IsRigFlat {A B : Type*} [CommRing A] [CommRing B]
    [TopologicalSpace A] [TopologicalSpace B] (φ : A →+* B) : Prop
```

## Tag 0GGQ, a lemma

[Tag 0GGQ](https://stacks.math.columbia.edu/tag/0GGQ) in the Stacks Project.

**`Rig.RingHom.isRigFlat_of_isNaivelyRigFlat_of_isJacobsonRing_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/FlatJacobson.lean, line 490](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/FlatJacobson.lean#L490).

> **Stacks 0GGQ.** A naively rig-flat arrow of `WAdm^Noeth` whose source has a Jacobson
> reduction modulo an ideal of definition is rig-flat.

```lean
public theorem isRigFlat_of_isNaivelyRigFlat_of_isJacobsonRing_quotient
    {A B : Type*} [CommRing A] [CommRing B]
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    (hA : TopologicalRing.IsWeaklyAdmissible A) (_hB : TopologicalRing.IsWeaklyAdmissible B)
    (φ : A →+* B) (hφ : Continuous φ)
    (hJacobson : ∃ I : Ideal A,
      TopologicalRing.IsIdealOfDefinition I ∧ IsJacobsonRing (A ⧸ I))
    (hflat : IsNaivelyRigFlat φ) :
    IsRigFlat φ
```

## Tag 0GGR, a lemma

[Tag 0GGR](https://stacks.math.columbia.edu/tag/0GGR) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigFlat_completedTensorProduct_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigFlatBaseChangeAdicFiniteType.lean, line 450](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigFlatBaseChangeAdicFiniteType.lean#L450).

> **Stacks 0GGR.**  Let `A → B` and `A → C` be arrows of `WAdm^Noeth`.  If `A → B` is rig-flat
> and `A → C` is adic and topologically of finite type, then `C → B ⊗̂_A C` is rig-flat.
>
> The naive form is `AlgebraicGeometry.FormalSpace.naiveRigFlatBaseChangeByAdicFiniteType`, the
> second to fifth paragraphs of the proof; the first paragraph upgrades it to rig-flatness through
> `AlgebraicGeometry.FormalSpace.rigFlat_completedTensorProduct_of_naive`.

```lean
public theorem isRigFlat_completedTensorProduct_baseChange
    {A B C : Type u} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B] [CommRing C] [TopologicalSpace C] [IsTopologicalRing C]
    [IsLinearTopology C C] [Algebra A B] [Algebra A C] [IsNoetherianRing A]
    [IsNoetherianRing B] [IsNoetherianRing C]
    (h₀ : TopologicalRing.IsAdic A) (h₁ : TopologicalRing.IsAdic B)
    (h₂ : TopologicalRing.IsAdic C) (hc₁ : Continuous (algebraMap A B))
    (hc₂ : Continuous (algebraMap A C)) (hP : Rig.RingHom.IsRigFlat (algebraMap A B))
    (hQ : _root_.RingHom.IsAdic (algebraMap A C) ∧
      TopologicalRing.IsTopologicallyOfFiniteType (algebraMap A C)) :
    Rig.RingHom.IsRigFlat (algebraMap C
      (CompletedTensorProduct (R := A) (M := B) (N := C)))
```

**`Rig.flat_atPrime_completedTensorProduct_restrictedPowerSeries`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ClosedPoint/CompletedTensorProductFlat.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/CompletedTensorProductFlat.lean#L269). The attribute's comment: “the last step only: for `C` the restricted power series ring `A{σ}` on a finite set of variables rather than an arbitrary adic `A → C` of topologically finite type, and flatness of `C → B ⊗̂_A C` localized at one rig-closed prime whose contraction to `A` is also rig-closed, rather than rig-flatness of `C → B ⊗̂_A C`”.

> **Flatness of `A{σ} → B ⊗̂[A] A{σ}` at a rig-closed point.**  Let `A → B` be a continuous
> adic and naively rig-flat homomorphism of Noetherian adic topological rings, complete along an
> ideal of definition `I` of `A` and its extension to `B`, and let `C = A{σ}` be the restricted
> power series ring on a finite set of variables.  If `q` is a rig-closed prime of the
> identification `B{σ}` of `B ⊗̂[A] C` whose contraction to `A` is rig-closed, then
> `C → B ⊗̂[A] C` is flat after localizing at the prime `q` cuts out.

```lean
public theorem flat_atPrime_completedTensorProduct_restrictedPowerSeries
    {A B : Type u} [CommRing A] [CommRing B] [Algebra A B]
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A] [IsNoetherianRing A]
    [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B] [IsNoetherianRing B]
    (I : Ideal A) (hI : _root_.IsAdic I) [IsAdicComplete I A]
    (hJ : _root_.IsAdic (I.map (algebraMap A B)))
    [IsAdicComplete (I.map (algebraMap A B)) B]
    (σ : Type u) [Finite σ]
    (hcont : Continuous (algebraMap A B))
    (hflat : RingHom.IsNaivelyRigFlat (algebraMap A B))
    (q : Ideal (RestrictedPowerSeries (I.map (algebraMap A B)) σ)) [q.IsPrime]
    (hq : Ideal.IsClosedPointAwayFrom
      ((I.map (algebraMap A B)).map (coefficientRingHom (I.map (algebraMap A B)) σ)) q)
    (hpA : Ideal.IsClosedPointAwayFrom I
      ((q.comap (TopologicalRing.restrictedPowerSeriesMap (B := B) I σ)).comap
        (coefficientRingHom I σ))) :
    letI : IsLinearTopology (RestrictedPowerSeries I σ) (RestrictedPowerSeries I σ) :=
      RestrictedPowerSeries.isLinearTopology_restrictedPowerSeries I
        (Ideal.fg_of_isNoetherianRing I) σ
    letI : TopologicalSpace (B ⊗[A] RestrictedPowerSeries I σ) :=
      tensorProductTopology (R := A) (M := B) (N := RestrictedPowerSeries I σ)
    letI : UniformSpace (B ⊗[A] RestrictedPowerSeries I σ) :=
      tensorProductUniformSpace (R := A) (M := B) (N := RestrictedPowerSeries I σ)
    letI : IsTopologicalRing (B ⊗[A] RestrictedPowerSeries I σ) :=
      tensorProduct_isTopologicalRing (R := A) (A := B) (B := RestrictedPowerSeries I σ)
    letI : IsUniformAddGroup (B ⊗[A] RestrictedPowerSeries I σ) :=
      tensorProduct_isUniformAddGroup (R := A) (M := B) (N := RestrictedPowerSeries I σ)
    let e := completedTensorProductRestrictedEquiv I (Ideal.fg_of_isNoetherianRing I) σ hJ
    let ι : RestrictedPowerSeries I σ →+*
        CompletedTensorProduct (R := A) (M := B) (N := RestrictedPowerSeries I σ) :=
      (UniformSpace.Completion.coeRingHom).comp
        (Algebra.TensorProduct.includeRight (R := A) (A := B)
          (B := RestrictedPowerSeries I σ)).toRingHom
    letI : (q.comap e.toRingHom).IsPrime := Ideal.comap_isPrime _ _
    _root_.RingHom.Flat
      ((algebraMap (CompletedTensorProduct (R := A) (M := B) (N := RestrictedPowerSeries I σ))
        (Localization.AtPrime (q.comap e.toRingHom))).comp ι)
```

## Tag 0GGS, a lemma

[Tag 0GGS](https://stacks.math.columbia.edu/tag/0GGS) in the Stacks Project.

**`Rig.isRigFlat_of_flat_etale_square`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/FlatEtaleLocalization.lean, line 1241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/FlatEtaleLocalization.lean#L1241).

> **Stacks 0GGS.** Rig-flatness ascends across the flat horizontal maps of a commutative
> square of adic homomorphisms of topological finite type between Noetherian weakly admissible
> rings whose lower map is étale modulo an ideal of definition: if `φ` is rig-flat, so is `φ'`.

```lean
public theorem isRigFlat_of_flat_etale_square
    {A A' B B' : Type u}
    [CommRing A] [CommRing A'] [CommRing B] [CommRing B']
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [TopologicalSpace A'] [IsTopologicalRing A'] [IsLinearTopology A' A']
    [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [TopologicalSpace B'] [IsTopologicalRing B'] [IsLinearTopology B' B']
    [IsNoetherianRing A] [IsNoetherianRing A']
    [IsNoetherianRing B] [IsNoetherianRing B']
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (_hA' : TopologicalRing.IsWeaklyAdmissible A')
    (_hB : TopologicalRing.IsWeaklyAdmissible B)
    (_hB' : TopologicalRing.IsWeaklyAdmissible B')
    (φ : A →+* B) (φ' : A' →+* B')
    (α : A →+* A') (β : B →+* B')
    (hsquare : φ'.comp α = β.comp φ)
    (hφ_cont : Continuous φ) (_hφ'_cont : Continuous φ')
    (hα_cont : Continuous α) (_hβ_cont : Continuous β)
    (hφ_adic : _root_.RingHom.IsAdic φ)
    (hφ'_adic : _root_.RingHom.IsAdic φ')
    (hα_adic : _root_.RingHom.IsAdic α)
    (_hβ_adic : _root_.RingHom.IsAdic β)
    (hφ_ft : TopologicalRing.IsTopologicallyOfFiniteType φ)
    (hφ'_ft : TopologicalRing.IsTopologicallyOfFiniteType φ')
    (hα_ft : TopologicalRing.IsTopologicallyOfFiniteType α)
    (hβ_ft : TopologicalRing.IsTopologicallyOfFiniteType β)
    (hα_flat : α.Flat) (hβ_flat : β.Flat)
    (I : Ideal A) (hI : TopologicalRing.IsIdealOfDefinition I)
    (hφ_rigFlat : RingHom.IsRigFlat φ)
    (hα_etale : (Ideal.quotientMap (I.map α) α Ideal.le_comap_map).Etale) :
    RingHom.IsRigFlat φ'
```

## Tag 0GGT, a lemma

[Tag 0GGT](https://stacks.math.columbia.edu/tag/0GGT) in the Stacks Project.

**`Rig.RingHom.isRigFlat_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/FlatDescent.lean, line 742](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/FlatDescent.lean#L742).

> **Stacks 0GGT.** Rig-flatness descends in a commutative square of adic homomorphisms of
> topological finite type between Noetherian weakly admissible rings whose lower horizontal map is
> flat and whose upper horizontal map is faithfully flat: if `φ'` is rig-flat, so is `φ`.

```lean
public theorem isRigFlat_of_faithfullyFlat
    {A A' B B' : Type*} [CommRing A] [CommRing A'] [CommRing B] [CommRing B']
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [TopologicalSpace A'] [IsTopologicalRing A'] [IsLinearTopology A' A']
    [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [TopologicalSpace B'] [IsTopologicalRing B'] [IsLinearTopology B' B']
    [IsNoetherianRing A] [IsNoetherianRing A'] [IsNoetherianRing B] [IsNoetherianRing B']
    (_hA : TopologicalRing.IsWeaklyAdmissible A) (_hA' : TopologicalRing.IsWeaklyAdmissible A')
    (_hB : TopologicalRing.IsWeaklyAdmissible B) (_hB' : TopologicalRing.IsWeaklyAdmissible B')
    (φ : A →+* B) (α : A →+* A') (β : B →+* B') (φ' : A' →+* B')
    (hcomm : β.comp φ = φ'.comp α)
    (_hφ_cont : Continuous φ) (_hα_cont : Continuous α)
    (_hβ_cont : Continuous β) (_hφ'_cont : Continuous φ')
    (hφ_adic : _root_.RingHom.IsAdic φ) (hα_adic : _root_.RingHom.IsAdic α)
    (_hβ_adic : _root_.RingHom.IsAdic β) (hφ'_adic : _root_.RingHom.IsAdic φ')
    (hφ_ft : TopologicalRing.IsTopologicallyOfFiniteType φ)
    (_hα_ft : TopologicalRing.IsTopologicallyOfFiniteType α)
    (_hβ_ft : TopologicalRing.IsTopologicallyOfFiniteType β)
    (_hφ'_ft : TopologicalRing.IsTopologicallyOfFiniteType φ')
    (hα_flat : α.Flat) (hβ_ff : β.FaithfullyFlat)
    (hφ'_rigFlat : Rig.RingHom.IsRigFlat φ') :
    Rig.RingHom.IsRigFlat φ
```

## Tag 0GGU, a lemma

[Tag 0GGU](https://stacks.math.columbia.edu/tag/0GGU) in the Stacks Project.

**`Rig.rigFlat_isLocalNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/FlatIsLocal.lean, line 749](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/FlatIsLocal.lean#L749).

> **Rig-flatness is a local property of arrows of `WAdm^Noeth`** (Stacks 0GGU): it ascends
> along completed étale localization diagrams, descends along faithfully flat ones, and is
> preserved by finite products of targets.

```lean
theorem rigFlat_isLocalNoetherian :
    TopologicalRing.PropertyIsLocalNoetherian
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦
        RingHom.IsRigFlat φ)
```

**`Rig.rigFlat_isLocalNoetherian'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/FlatIsLocalRefined.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/FlatIsLocalRefined.lean#L161).

> **Rig-flatness is a local property of arrows of `WAdm^Noeth`**: it is
> independent of the presentations of its source and target, ascends along completed étale
> localization diagrams, descends along faithfully flat ones, and is preserved by finite products
> of targets.

```lean
theorem rigFlat_isLocalNoetherian' :
    TopologicalRing.PropertyIsLocalNoetherian'
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦
        RingHom.IsRigFlat φ)
```

## Tag 0GGV, a lemma

[Tag 0GGV](https://stacks.math.columbia.edu/tag/0GGV) in the Stacks Project.

**`Rig.rigFlat_isStableUnderCompositionNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/FlatStableUnderComposition.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/FlatStableUnderComposition.lean#L214).

> **Rig-flatness is stable under composition on `WAdm^Noeth`** (Stacks 0GGV). Adicness and
> topological finite type of the composite are Stacks 0GBZ; naive rig-flatness of the induced map
> of completed principal localizations is `Rig.RingHom.isNaivelyRigFlat_comp` applied to the two
> factors, transported along the functoriality `Rig.completedAwayMap_comp`.

```lean
theorem rigFlat_isStableUnderCompositionNoetherian :
    TopologicalRing.PropertyIsStableUnderCompositionNoetherian
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦
        RingHom.IsRigFlat φ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.15, Tag 0GGK](https://stacks.math.columbia.edu/tag/0GGK)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
