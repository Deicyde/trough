---
declaration: section
origin: cited
lean: IsDiscreteValuationRing.IntegralClosureBaseChange.IsWeakSolution, IsDiscreteValuationRing.IntegralClosureBaseChange.IsSolution, IsDiscreteValuationRing.IntegralClosureBaseChange.IsSeparableSolution, IsDiscreteValuationRing.weakSolution_isInseparable_and_inseparable_isSolution, IsDiscreteValuationRing.isField_tensorProduct_and_isDVR_baseChange_of_totallyRamified, IsDiscreteValuationRing.weakSolutions_and_solutions_go_down_and_compose, IsDiscreteValuationRing.normal_extension_acts_transitively_on_maximalSpectrum_integralClosure, Stacks.EisensteinExtension.exists_totallyRamifiedExtension_with_uniformizer_eq
statement: formalized
proof: formalized
---

# 15.117 Eliminating ramification

Section 15.117 of the Stacks Project, [Tag 09EL](https://stacks.math.columbia.edu/tag/09EL). 19 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09EN, a definition

[Tag 09EN](https://stacks.math.columbia.edu/tag/09EN) in the Stacks Project.

**`IsDiscreteValuationRing.IntegralClosureBaseChange.IsWeakSolution`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Solution.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Solution.lean#L144). The attribute's comment: “(1), weak solution”.

> Every localization arising from the base change has ramification index one.

```lean
def IsWeakSolution
    {A : Type uA} {B : Type uB} {K : Type uK} {L : Type uL}
    {K₁ : Type uK₁}
    [CommRing A] [CommRing B] [Field K] [Field L] [Field K₁]
    [IsDomain A] [IsDomain B] [IsDiscreteValuationRing A] [IsDiscreteValuationRing B]
    [Algebra A B] [Algebra A K] [Algebra A L] [Algebra B L]
    [Algebra K L] [Algebra K K₁] [Algebra A K₁]
    [IsExtension A B] [IsFractionRing A K] [IsFractionRing B L]
    [IsScalarTower A B L] [IsScalarTower A K L] [IsScalarTower A K K₁]
    [Module.Finite K K₁]
    (D : IntegralClosureBaseChange A B K L K₁) : Prop
```

**`IsDiscreteValuationRing.IntegralClosureBaseChange.IsSolution`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Solution.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Solution.lean#L163). The attribute's comment: “(2), solution”.

> Every localization arising from the base change is formally smooth for the adic topology
> defined by the maximal ideal of the target localization.

```lean
def IsSolution.{v}
    {A : Type uA} {B : Type uB} {K : Type uK} {L : Type uL}
    {K₁ : Type uK₁}
    [CommRing A] [CommRing B] [Field K] [Field L] [Field K₁]
    [IsDomain A] [IsDomain B] [IsDiscreteValuationRing A] [IsDiscreteValuationRing B]
    [Algebra A B] [Algebra A K] [Algebra A L] [Algebra B L]
    [Algebra K L] [Algebra K K₁] [Algebra A K₁]
    [IsExtension A B] [IsFractionRing A K] [IsFractionRing B L]
    [IsScalarTower A B L] [IsScalarTower A K L] [IsScalarTower A K K₁]
    [Module.Finite K K₁]
    (D : IntegralClosureBaseChange.{uA, uB, uK, uL, uK₁, uL₁, uA₁, uB₁}
      A B K L K₁) : Prop
```

**`IsDiscreteValuationRing.IntegralClosureBaseChange.IsSeparableSolution`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Solution.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Solution.lean#L188). The attribute's comment: “separable solution”.

> A solution whose finite extension `K₁/K` is separable.

```lean
def IsSeparableSolution.{v}
    {A : Type uA} {B : Type uB} {K : Type uK} {L : Type uL}
    {K₁ : Type uK₁}
    [CommRing A] [CommRing B] [Field K] [Field L] [Field K₁]
    [IsDomain A] [IsDomain B] [IsDiscreteValuationRing A] [IsDiscreteValuationRing B]
    [Algebra A B] [Algebra A K] [Algebra A L] [Algebra B L]
    [Algebra K L] [Algebra K K₁] [Algebra A K₁]
    [IsExtension A B] [IsFractionRing A K] [IsFractionRing B L]
    [IsScalarTower A B L] [IsScalarTower A K L] [IsScalarTower A K K₁]
    [Module.Finite K K₁]
    (D : IntegralClosureBaseChange.{uA, uB, uK, uL, uK₁, uL₁, uA₁, uB₁}
      A B K L K₁) : Prop
```

## Tag 09EP, an example

[Tag 09EP](https://stacks.math.columbia.edu/tag/09EP) in the Stacks Project.

**`IsDiscreteValuationRing.weakSolution_isInseparable_and_inseparable_isSolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/WeakSolution/Inseparability.lean, line 924](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/WeakSolution/Inseparability.lean#L924).

> For `k[[x]] → k[[x^(1/p)]]` in positive characteristic `p`, every weak solution is
> inseparable, while every finite inseparable extension of `k((x))` is a solution.

```lean
theorem weakSolution_isInseparable_and_inseparable_isSolution
    (p : ℕ) [Fact p.Prime]
    (k : Type uk) (A : Type uA) (B : Type uB) (K : Type uK) (L : Type uL)
    [Field k] [PerfectField k] [CharP k p]
    [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    [CommRing B] [IsDomain B] [IsDiscreteValuationRing B]
    [Field K] [Field L]
    [Algebra k A] [Algebra k B] [Algebra k K] [Algebra k L]
    [Algebra A B] [Algebra A K] [Algebra A L] [Algebra B L] [Algebra K L]
    [IsScalarTower k A B] [IsScalarTower k A K] [IsScalarTower k B L]
    [IsScalarTower k K L] [IsScalarTower A B L] [IsScalarTower A K L]
    [IsExtension A B] [IsFractionRing A K] [IsFractionRing B L]
    (eA : A ≃ₐ[k] PowerSeries k) (eB : B ≃ₐ[k] PowerSeries k)
    (eK : K ≃ₐ[k] LaurentSeries k) (eL : L ≃ₐ[k] LaurentSeries k)
    (hAB : ∀ a : A, eB (algebraMap A B a) =
      PowerSeries.subst (PowerSeries.X ^ p) (eA a))
    (_hAK : ∀ a : A, eK (algebraMap A K a) = (eA a : LaurentSeries k))
    (_hBL : ∀ b : B, eL (algebraMap B L b) = (eB b : LaurentSeries k)) :
    (∀ (K₁ : Type uK₁) [Field K₁] [Algebra K K₁] [Algebra A K₁]
        [IsScalarTower A K K₁] [Module.Finite K K₁]
        (D : IntegralClosureBaseChange.{uA, uB, uK, uL, uK₁, uL₁, uA₁, uB₁}
          A B K L K₁),
        D.IsWeakSolution → ¬ Algebra.IsSeparable K K₁) ∧
      ∀ (K₁ : Type uK₁) [Field K₁] [Algebra K K₁] [Algebra A K₁]
        [IsScalarTower A K K₁] [Module.Finite K K₁],
        ¬ Algebra.IsSeparable K K₁ →
          ∃ D : IntegralClosureBaseChange.{uA, uB, uK, uL, uK₁,
              max uL uK₁, uK₁, max uL uK₁} A B K L K₁,
            D.IsSolution.{uA, uB, uK, uL, uK₁, max uL uK₁, uK₁, max uL uK₁, v}
```

## Tag 09ER, a lemma

[Tag 09ER](https://stacks.math.columbia.edu/tag/09ER) in the Stacks Project.

**`IsDiscreteValuationRing.isField_tensorProduct_and_isDVR_baseChange_of_totallyRamified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/WeakSolution/TotallyRamified.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/WeakSolution/TotallyRamified.lean#L272).

> A finite separable extension totally ramified with respect to the lower discrete valuation
> ring preserves a weakly unramified extension after tensor-product base change. The tensor
> product is canonically the integral closure in the base-changed fraction field.

```lean
theorem isField_tensorProduct_and_isDVR_baseChange_of_totallyRamified
    (A : Type uA) (B : Type uB) (K : Type uK) (L : Type uL) (K₁ : Type uK₁)
    [CommRing A] [CommRing B] [Field K] [Field L] [Field K₁]
    [IsDomain A] [IsDomain B] [IsDiscreteValuationRing A] [IsDiscreteValuationRing B]
    [Algebra A B] [FaithfulSMul A B] [IsLocalHom (algebraMap A B)]
    [Algebra A K] [Algebra B L] [Algebra A L] [Algebra K L]
    [IsScalarTower A B L] [IsScalarTower A K L]
    [IsFractionRing A K] [IsFractionRing B L]
    [Algebra K K₁] [Algebra A K₁] [IsScalarTower A K K₁]
    [FiniteDimensional K K₁] [Algebra.IsSeparable K K₁]
    (hweak : Ideal.map (algebraMap A B) (IsLocalRing.maximalIdeal A) =
      IsLocalRing.maximalIdeal B)
    (htot : IsTotallyRamifiedWithRespectTo A K K₁) :
    let A₁ := integralClosure A K₁
    let B₁ := B ⊗[A] A₁
    let L₁ := L ⊗[K] K₁
    let C₁ := integralClosure B L₁
    ∃ hL₁ : IsField L₁,
      letI := hL₁.toField
      ∃ hA₁ : IsDiscreteValuationRing A₁,
        letI := hA₁
        ∃ hBdom : IsDomain B₁,
          letI := hBdom
          ∃ hB₁ : IsDiscreteValuationRing B₁,
            letI := hB₁
            let f : A₁ →+* B₁ := Algebra.TensorProduct.includeRight.toRingHom
            Function.Injective f ∧
              Ideal.map f (IsLocalRing.maximalIdeal A₁) = IsLocalRing.maximalIdeal B₁ ∧
              ∃ hCdom : IsDomain C₁,
                letI := hCdom
                ∃ hC₁ : IsDiscreteValuationRing C₁,
                  letI := hC₁
                  ∃ _ : IsFractionRing C₁ L₁,
                    ∃ e : B₁ ≃ₐ[B] C₁,
                      (∀ a : A₁,
                        ((e ((Algebra.TensorProduct.includeRight : A₁ →ₐ[A] B₁) a) : C₁)
                            : L₁) =
                          (Algebra.TensorProduct.includeRight : K₁ →ₐ[K] L₁) (a : K₁)) ∧
                        let f' : A₁ →+* C₁ :=
                          e.toRingHom.comp Algebra.TensorProduct.includeRight.toRingHom
                        Function.Injective f' ∧
                          Ideal.map f' (IsLocalRing.maximalIdeal A₁) =
                            IsLocalRing.maximalIdeal C₁
```

## Tag 09ES, a lemma

[Tag 09ES](https://stacks.math.columbia.edu/tag/09ES) in the Stacks Project.

**`IsDiscreteValuationRing.weakSolutions_and_solutions_go_down_and_compose`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/EppSolution.lean, line 1210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/EppSolution.lean#L1210).

> Weak solutions and solutions descend along a tower of extensions of discrete valuation
> rings. Conversely, they compose provided every field factor of the intermediate reduced tensor
> product is respectively a weak solution or a solution for the upper extension.

```lean
theorem weakSolutions_and_solutions_go_down_and_compose
    (A : Type uA) (B : Type uB) (C : Type uC)
    (K : Type uK) (L : Type uL) (M : Type uM) (K₁ : Type uK₁)
    [CommRing A] [CommRing B] [CommRing C]
    [IsDomain A] [IsDomain B] [IsDomain C]
    [IsDiscreteValuationRing A] [IsDiscreteValuationRing B]
    [IsDiscreteValuationRing C]
    [Field K] [Field L] [Field M] [Field K₁]
    [Algebra A B] [Algebra B C] [Algebra A C]
    [Algebra A K] [Algebra A L] [Algebra A M]
    [Algebra B L] [Algebra B M] [Algebra C M]
    [Algebra K L] [Algebra K M] [Algebra L M]
    [Algebra K K₁] [Algebra A K₁]
    [IsExtension A B] [IsExtension B C]
    [IsExtension A C]
    [IsFractionRing A K] [IsFractionRing B L] [IsFractionRing C M]
    [IsScalarTower A B C] [IsScalarTower A B L] [IsScalarTower A B M]
    [IsScalarTower B C M] [IsScalarTower A C M]
    [IsScalarTower A K L] [IsScalarTower A K M] [IsScalarTower K L M]
    [IsScalarTower B L M] [IsScalarTower A K K₁] [Module.Finite K K₁]
    (DAB : IntegralClosureBaseChange.{uA, uB, uK, uL, uK₁, uL₁, uA₁, uB₁}
      A B K L K₁)
    (DAC : IntegralClosureBaseChange.{uA, uC, uK, uM, uK₁, uM₁, uA₂, uC₁}
      A C K M K₁) :
    letI := DAB.commRingL₁
    letI := DAB.algebraLL₁
    ((DAC.IsWeakSolution → DAB.IsWeakSolution) ∧
      (DAC.IsSolution.{uA, uC, uK, uM, uK₁, uM₁, uA₂, uC₁, max uA₂ uC₁} →
        DAB.IsSolution.{uA, uB, uK, uL, uK₁, uL₁, uA₁, uB₁, max uA₁ uB₁})) ∧
      ∀ (n : ℕ) (E : Fin n → Type uE)
        [∀ i, Field (E i)] [∀ i, Algebra L (E i)] [∀ i, Algebra B (E i)]
        [∀ i, IsScalarTower B L (E i)] [∀ i, Module.Finite L (E i)],
        0 < n → Nonempty (DAB.L₁ ≃ₐ[L] ∀ i, E i) →
          ∀ DBC : ∀ i, IntegralClosureBaseChange.{uB, uC, uL, uM, uE, uN₁, uB₂, uC₂}
              B C L M (E i),
            ((DAB.IsWeakSolution ∧ ∀ i, (DBC i).IsWeakSolution) →
              DAC.IsWeakSolution) ∧
            ((DAB.IsSolution.{uA, uB, uK, uL, uK₁, uL₁, uA₁, uB₁, max uA₁ uB₁} ∧
                ∀ i, (DBC i).IsSolution.{uB, uC, uL, uM, uE, uN₁, uB₂, uC₂, max uB₂ uC₂}) →
              DAC.IsSolution.{uA, uC, uK, uM, uK₁, uM₁, uA₂, uC₁, max uA₂ uC₁})
```

## Tag 09EU, a lemma

[Tag 09EU](https://stacks.math.columbia.edu/tag/09EU) in the Stacks Project.

**`IsDiscreteValuationRing.normal_extension_acts_transitively_on_maximalSpectrum_integralClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/WeakSolution/GaloisAction.lean, line 394](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/WeakSolution/GaloisAction.lean#L394).

> After a finite normal extension `K₁/K`, the automorphisms of `K₁` over `K` act
> compatibly on the reduced base change `L₁`, on the integral closure `A₁` of `A` in `K₁`,
> and on the integral closure `B₁` of `B` in `L₁`.  The resulting action on the maximal
> ideals of `B₁` is transitive.

```lean
theorem normal_extension_acts_transitively_on_maximalSpectrum_integralClosure
    (A B K L K₁ L₁ A₁ B₁ : Type u)
    [CommRing A] [CommRing B] [Field K] [Field L] [Field K₁]
    [CommRing L₁] [CommRing A₁] [CommRing B₁]
    [IsDomain A] [IsDomain B] [IsDiscreteValuationRing A] [IsDiscreteValuationRing B]
    [Algebra A B] [FaithfulSMul A B] [IsLocalHom (algebraMap A B)]
    [Algebra A K] [Algebra A L] [Algebra B L] [Algebra K L] [Algebra K K₁]
    [Algebra A K₁] [Algebra K L₁] [Algebra B L₁] [Algebra L L₁] [Algebra K₁ L₁]
    [Algebra A A₁] [Algebra B B₁] [Algebra A B₁] [Algebra A₁ B₁] [Algebra B₁ L₁]
    [IsScalarTower A B L] [IsScalarTower A K L] [IsScalarTower A K K₁]
    [IsScalarTower K L L₁] [IsScalarTower K K₁ L₁] [IsScalarTower B L L₁]
    [IsScalarTower A B B₁] [IsScalarTower A A₁ B₁] [IsScalarTower B B₁ L₁]
    [IsFractionRing A K] [IsFractionRing B L] [Module.Finite K K₁] [Normal K K₁]
    (eL₁ : L₁ ≃ₐ[K] ((L ⊗[K] K₁) ⧸ nilradical (L ⊗[K] K₁)))
    (eA₁ : A₁ ≃ₐ[A] integralClosure A K₁)
    (eB₁ : B₁ ≃ₐ[B] integralClosure B L₁)
    (eL₁_left : ∀ x : L,
      eL₁ (algebraMap L L₁ x) = Ideal.Quotient.mk _
        ((Algebra.TensorProduct.includeLeft : L →ₐ[K] L ⊗[K] K₁) x))
    (eL₁_right : ∀ x : K₁,
      eL₁ (algebraMap K₁ L₁ x) = Ideal.Quotient.mk _
        ((Algebra.TensorProduct.includeRight : K₁ →ₐ[K] L ⊗[K] K₁) x))
    (eB₁_coe : ∀ x : B₁, ((eB₁ x : integralClosure B L₁) : L₁) = algebraMap B₁ L₁ x)
    (_hfieldSquare : ∀ x : K, algebraMap L L₁ (algebraMap K L x) =
      algebraMap K₁ L₁ (algebraMap K K₁ x))
    (hringSquare : ∀ x : A₁, algebraMap B₁ L₁ (algebraMap A₁ B₁ x) =
      algebraMap K₁ L₁ ((eA₁ x : integralClosure A K₁) : K₁)) :
    ∃ (ρL₁ : (K₁ ≃ₐ[K] K₁) →* (L₁ ≃ₐ[L] L₁))
        (ρA₁ : (K₁ ≃ₐ[K] K₁) →* (A₁ ≃ₐ[A] A₁))
        (ρB₁ : (K₁ ≃ₐ[K] K₁) →* (B₁ ≃ₐ[B] B₁)),
      (∀ (g : K₁ ≃ₐ[K] K₁) (x : K₁),
        ρL₁ g (algebraMap K₁ L₁ x) = algebraMap K₁ L₁ (g x)) ∧
      (∀ (g : K₁ ≃ₐ[K] K₁) (x : A₁),
        (((eA₁ (ρA₁ g x) : integralClosure A K₁) : K₁)) =
          g ((eA₁ x : integralClosure A K₁) : K₁)) ∧
      (∀ (g : K₁ ≃ₐ[K] K₁) (x : B₁),
        algebraMap B₁ L₁ (ρB₁ g x) = ρL₁ g (algebraMap B₁ L₁ x)) ∧
      (∀ (g : K₁ ≃ₐ[K] K₁) (x : A₁),
        ρB₁ g (algebraMap A₁ B₁ x) = algebraMap A₁ B₁ (ρA₁ g x)) ∧
      ∀ q q' : MaximalSpectrum B₁, ∃ g : K₁ ≃ₐ[K] K₁,
        q'.asIdeal = q.asIdeal.comap (ρB₁ g).symm.toRingHom
```

## Tag 09EW, a lemma

[Tag 09EW](https://stacks.math.columbia.edu/tag/09EW) in the Stacks Project.

**`Stacks.EisensteinExtension.exists_totallyRamifiedExtension_with_uniformizer_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Kummer/Eisenstein.lean, line 636](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Kummer/Eisenstein.lean#L636).

> Let `A` be a discrete valuation ring with fraction field `K` and residue characteristic
> `p > 0`, with uniformizer `π`, and let `n > 1`. For every power `q` of `p` there is a separable
> extension `L / K` of degree `q`, totally ramified with respect to `A` with ramification index
> `q`, whose integral closure `B` of `A` is a discrete valuation ring with a uniformizer `π_B`
> satisfying `π_B^q = π + π^n b` and `π_B^q = π + π_B^{nq} b'` for some `b, b'` in `B`.

```lean
theorem exists_totallyRamifiedExtension_with_uniformizer_eq
    (A : Type u) (K : Type v) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    [Field K] [Algebra A K] [IsFractionRing A K]
    (π : A) (hπ : Irreducible π) (p n q : ℕ)
    (hp : 0 < p)
    (_hres : ringChar (A ⧸ IsLocalRing.maximalIdeal A) = p)
    (hn : 1 < n) (hq : ∃ r : ℕ, q = p ^ r) :
    ∃ (L : Type v) (_ : Field L) (_ : Algebra K L) (_ : Algebra A L)
      (_ : IsScalarTower A K L) (_ : Module.Finite K L)
      (_ : Algebra.IsSeparable K L)
      (_ : IsDiscreteValuationRing (integralClosure A L)),
      Module.finrank K L = q ∧
        Stacks.KummerExtension.IsTotallyRamified A K L ∧
        Ideal.ramificationIdx' (IsLocalRing.maximalIdeal A)
            (IsLocalRing.maximalIdeal (integralClosure A L)) = q ∧
        ∃ πB b b' : integralClosure A L,
          Irreducible πB ∧
            πB ^ q = algebraMap A (integralClosure A L) π +
              (algebraMap A (integralClosure A L) π) ^ n * b ∧
            πB ^ q = algebraMap A (integralClosure A L) π + πB ^ (n * q) * b'
```

## Tag 09EX, a lemma

[Tag 09EX](https://stacks.math.columbia.edu/tag/09EX) in the Stacks Project.

**`Stacks.DiscreteValuationRing.AdjoinPthRoot.statement1_not_pth_power`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/AdjoinPthRoot.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/AdjoinPthRoot.lean#L184). The attribute's comment: “(1)”.

> If the residue class `abar` of `a` is not a `p`-th power in the residue field `kappa_A`,
> then `a` is not a `p`-th power in `K`.

```lean
theorem statement1_not_pth_power
    (ha : ¬ ∃ b : IsLocalRing.ResidueField A, IsLocalRing.residue A a = b ^ p) :
    ¬ ∃ b : K, algebraMap A K a = b ^ p
```

**`Stacks.DiscreteValuationRing.AdjoinPthRoot.statement2_integralClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/AdjoinPthRoot.lean, line 451](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/AdjoinPthRoot.lean#L451). The attribute's comment: “(2)”.

> The integral closure of `A` in `K[a^{1/p}]` equals
> `A[a^{1/p}] = A[alpha]`.

```lean
theorem statement2_integralClosure
    (ha : ¬ ∃ b : IsLocalRing.ResidueField A, IsLocalRing.residue A a = b ^ p) :
    integralClosure A (FieldExt (A := A) (K := K) p a)
      = ringExt (A := A) (K := K) p a
```

**`Stacks.DiscreteValuationRing.AdjoinPthRoot.statement3_dvr_weaklyUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/AdjoinPthRoot.lean, line 480](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/AdjoinPthRoot.lean#L480). The attribute's comment: “(3)”.

> The ring `A[a^{1/p}] = A[alpha]` is a discrete valuation ring, and the extension
> `A ⊆ A[a^{1/p}]` is weakly unramified: every uniformizer (irreducible element) of `A` maps to a
> uniformizer (irreducible element) of `A[a^{1/p}]`.

```lean
theorem statement3_dvr_weaklyUnramified
    (ha : ¬ ∃ b : IsLocalRing.ResidueField A, IsLocalRing.residue A a = b ^ p) :
    haveI : Fact (Irreducible (polyK (A := A) (K := K) p a)) :=
      ⟨statement1_irreducible p a ha⟩
    letI B := ringExt (A := A) (K := K) p a
    haveI : IsDomain B := inferInstance
    IsDiscreteValuationRing B
      ∧ (∀ ϖ : A, Irreducible ϖ → Irreducible (algebraMap A B ϖ))
```

## Tag 09EY, a lemma

[Tag 09EY](https://stacks.math.columbia.edu/tag/09EY) in the Stacks Project.

**`IsDiscreteValuationRing.weaklyUnramified_or_adjoin_root_or_after_totallyRamified_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/PurelyInseparable.lean, line 899](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/PurelyInseparable.lean#L899).

> For a weakly unramified extension `A → B` of discrete valuation rings with `B`
> Nagata, followed by a purely inseparable extension of fraction fields of prime degree `p`,
> either the composite extension is weakly unramified, the upper DVR is generated by a
> `p`-th root of a uniformizer of `A`, or a separable totally ramified degree-`p` base change
> makes both maps between the resulting integral closures weakly unramified.

```lean
theorem weaklyUnramified_or_adjoin_root_or_after_totallyRamified_baseChange
    (A B C K L M : Type u)
    [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    [CommRing B] [IsDomain B] [IsDiscreteValuationRing B]
    [CommRing C] [IsDomain C] [IsDiscreteValuationRing C]
    [Field K] [Field L] [Field M]
    [Algebra A B] [Algebra B C] [Algebra A C]
    [FaithfulSMul A B] [FaithfulSMul B C]
    [IsScalarTower A B C]
    [IsLocalHom (algebraMap A B)] [IsLocalHom (algebraMap B C)]
    [Algebra A K] [Algebra B L] [Algebra C M]
    [Algebra A L] [Algebra A M] [Algebra B M]
    [Algebra K L] [Algebra K M] [Algebra L M]
    [IsScalarTower A B L] [IsScalarTower B C M]
    [IsScalarTower A C M] [IsScalarTower B L M]
    [IsScalarTower A K L] [IsScalarTower K L M]
    [IsScalarTower A B M] [IsScalarTower A K M]
    [IsFractionRing A K] [IsFractionRing B L] [IsFractionRing C M]
    (p : ℕ) [Fact p.Prime] [FiniteDimensional L M] [IsPurelyInseparable L M]
    (hdegree : Module.finrank L M = p)
    (π : A) (hπ : Irreducible π)
    (hNagata : IsNagataRing B)
    (hweak : Ideal.map (algebraMap A B) (IsLocalRing.maximalIdeal A) =
      IsLocalRing.maximalIdeal B) :
    Ideal.map (algebraMap A C) (IsLocalRing.maximalIdeal A) =
        IsLocalRing.maximalIdeal C ∨
      (∃ x : C, x ^ p = algebraMap A C π ∧ Algebra.adjoin B {x} = ⊤) ∨
      ∃ (K₁ : Type u) (_ : Field K₁) (_ : Algebra K K₁) (_ : Algebra A K₁)
        (_ : IsScalarTower A K K₁) (_ : FiniteDimensional K K₁)
        (_ : Algebra.IsSeparable K K₁),
        Module.finrank K K₁ = p ∧
          IsDiscreteValuationRing.IsTotallyRamifiedWithRespectTo A K K₁ ∧
          let L₁ := L ⊗[K] K₁
          let M₁ := M ⊗[K] K₁
          let A₁ := integralClosure A K₁
          let B₁ := integralClosure B L₁
          let C₁ := integralClosure C M₁
          IsField L₁ ∧ IsField M₁ ∧
            ∃ hA₁ : IsDiscreteValuationRing A₁,
              letI := hA₁
              ∃ hB₁dom : IsDomain B₁,
                letI := hB₁dom
                ∃ hB₁ : IsDiscreteValuationRing B₁,
                  letI := hB₁
                  ∃ hC₁dom : IsDomain C₁,
                    letI := hC₁dom
                    ∃ hC₁ : IsDiscreteValuationRing C₁,
                      letI := hC₁
                      ∃ (g : L₁ →+* M₁) (f : A₁ →+* B₁) (f' : B₁ →+* C₁),
                        Function.Injective f ∧ Function.Injective f' ∧
                          (∀ l : L, g
                            ((Algebra.TensorProduct.includeLeft : L →ₐ[K] L₁) l) =
                            (Algebra.TensorProduct.includeLeft : M →ₐ[K] M₁)
                              (algebraMap L M l)) ∧
                          (∀ k : K₁, g
                            ((Algebra.TensorProduct.includeRight : K₁ →ₐ[K] L₁) k) =
                            (Algebra.TensorProduct.includeRight : K₁ →ₐ[K] M₁) k) ∧
                          (∀ a : A₁, ((f a : B₁) : L₁) =
                            (Algebra.TensorProduct.includeRight : K₁ →ₐ[K] L₁) (a : K₁)) ∧
                          (∀ b : B₁, ((f' b : C₁) : M₁) = g (b : L₁)) ∧
                          Ideal.map f (IsLocalRing.maximalIdeal A₁) =
                            IsLocalRing.maximalIdeal B₁ ∧
                          Ideal.map f' (IsLocalRing.maximalIdeal B₁) =
                            IsLocalRing.maximalIdeal C₁
```

## Tag 09EZ, a lemma

[Tag 09EZ](https://stacks.math.columbia.edu/tag/09EZ) in the Stacks Project.

**`IsLocalRing.exists_residueField_section_compatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalRing/ResidueSection.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalRing/ResidueSection.lean#L51).

> A local ring of prime characteristic with nilpotent maximal ideal has a coefficient field,
> and it can be extended compatibly across a local homomorphism whose target also has nilpotent
> maximal ideal and whose residue field extension is separable.

```lean
theorem exists_residueField_section_compatible
    {p : ℕ} [Fact p.Prime]
    (A : Type u) [CommRing A] [IsLocalRing A] [CharP A p]
    (hA : IsNilpotent (IsLocalRing.maximalIdeal A)) :
    ∃ σ : IsLocalRing.ResidueField A →+* A,
      (IsLocalRing.residue A).comp σ = RingHom.id _ ∧
      ∀ (A' : Type v) [CommRing A'] [IsLocalRing A'] [Algebra A A']
        [IsLocalHom (algebraMap A A')],
        IsNilpotent (IsLocalRing.maximalIdeal A') →
        Algebra.IsSeparableExtension (IsLocalRing.ResidueField A)
          (IsLocalRing.ResidueField A') →
        ∃ σ' : IsLocalRing.ResidueField A' →+* A',
          (IsLocalRing.residue A').comp σ' = RingHom.id _ ∧
          (algebraMap A A').comp σ =
            σ'.comp (algebraMap (IsLocalRing.ResidueField A)
              (IsLocalRing.ResidueField A'))
```

## Tag 09F0, a lemma

[Tag 09F0](https://stacks.math.columbia.edu/tag/09F0) in the Stacks Project.

**`IsDiscreteValuationRing.isGalois_and_ramification_cases_of_adjoin_root_artinSchreier`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/ArtinSchreier/RamificationCases.lean, line 689](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/ArtinSchreier/RamificationCases.lean#L689).

> Let `A` be a discrete valuation ring with fraction field `K` of characteristic
> `p > 0`. If `L = K[z]` and `z ^ p - z = ξ`, then `L / K` is Galois and is either
> trivial, unramified of degree `p`, totally ramified of ramification index `p`, or
> weakly unramified with purely inseparable residue extension of degree `p`.
>
> Moreover, for a uniformizer `π` of `A`, an integral `ξ` gives one of the first two
> cases; a pole of order prime to `p` gives the totally ramified case; and a pole whose
> positive order is divisible by `p` and whose leading coefficient is not a `p`-th
> power in the residue field gives the weakly unramified, residually inseparable case.

```lean
theorem isGalois_and_ramification_cases_of_adjoin_root_artinSchreier
    (A : Type uA) (K : Type uK) (L : Type uL)
    [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    [Field K] [Algebra A K] [IsFractionRing A K]
    [Field L] [Algebra K L] [Algebra A L] [IsScalarTower A K L]
    (p : ℕ) (hp : p.Prime) [CharP K p]
    (ξ : K) (z : L)
    (hz : z ^ p - z = algebraMap K L ξ)
    (hgen : Algebra.adjoin K {z} = ⊤)
    (π : A) (hπ : Irreducible π) :
    ∃ hfin : Module.Finite K L,
      letI := hfin
      let B := integralClosure A L
      let mA := IsLocalRing.maximalIdeal A
      let trivial : Prop := Function.Surjective (algebraMap K L)
      let unramified : Prop :=
        Module.finrank K L = p ∧
          ∀ m : Ideal B, m.IsMaximal → ∃ _ : m.LiesOver mA,
            Ideal.ramificationIdx' mA m = 1 ∧
              @Algebra.IsSeparable (A ⧸ mA) (B ⧸ m) _ _
                (Ideal.Quotient.algebraOfLiesOver m mA)
      let totallyRamified : Prop :=
        Stacks.KummerExtension.IsTotallyRamified A K L ∧
          ∀ m : Ideal B, m.IsMaximal → m.LiesOver mA →
            Ideal.ramificationIdx' mA m = p
      let residuallyInseparable : Prop :=
        ∃ hDVR : IsDiscreteValuationRing B,
          letI := hDVR
          let mB := IsLocalRing.maximalIdeal B
          ∃ _ : mB.LiesOver mA,
            Ideal.ramificationIdx' mA mB = 1 ∧
              letI := Ideal.Quotient.algebraOfLiesOver mB mA
              IsPurelyInseparable (A ⧸ mA) (B ⧸ mB) ∧
                Module.finrank (A ⧸ mA) (B ⧸ mB) = p
      IsGalois K L ∧
        (trivial ∨ unramified ∨ totallyRamified ∨ residuallyInseparable) ∧
        ((∃ a : A, ξ = algebraMap A K a) → trivial ∨ unramified) ∧
        (∀ (n : ℕ) (a : A), 0 < n → ¬p ∣ n → IsUnit a →
          ξ = (algebraMap A K π)⁻¹ ^ n * algebraMap A K a → totallyRamified) ∧
        (∀ (n : ℕ) (a : A), 0 < n → p ∣ n →
          (¬∃ b : IsLocalRing.ResidueField A, IsLocalRing.residue A a = b ^ p) →
          ξ = (algebraMap A K π)⁻¹ ^ n * algebraMap A K a →
            residuallyInseparable)
```

## Tag 09F1, a lemma

[Tag 09F1](https://stacks.math.columbia.edu/tag/09F1) in the Stacks Project.

**`IsDiscreteValuationRing.exists_isGalois_totallyRamified_isWeakSolution_of_charP`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/ArtinSchreier/CharPSolution.lean, line 690](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/ArtinSchreier/CharPSolution.lean#L690).

> In equal characteristic `p`, a weakly unramified extension `A ⊆ B` followed
> by a degree-`p` Galois extension of fraction fields admits a finite Galois base
> extension which is totally ramified over `A` and is a weak solution for `A → C`,
> provided the image of the residue field of `A` in that of `B` is the intersection
> of all sets of `p ^ n`-th powers for `n ≥ 1`.
>
> This is Tag 09F1 as stated.  The two consequences of `hresidue` that the proof consumes are
> isolated in `exists_isGalois_totallyRamified_isWeakSolution_of_charP_of_perfectCore_le`, which is
> strictly more general: it drops the inclusion `image ⊆ perfectCore` entirely, keeping only
> perfectness of `κ_A` and `perfectCore κ_B p ⊆ image`.

```lean
theorem exists_isGalois_totallyRamified_isWeakSolution_of_charP
    (A : Type uA) (B : Type uB) (C : Type uC)
    (K : Type uK) (L : Type uL) (M : Type uM)
    [CommRing A] [CommRing B] [CommRing C]
    [IsDomain A] [IsDomain B] [IsDomain C]
    [IsDiscreteValuationRing A] [IsDiscreteValuationRing B]
    [IsDiscreteValuationRing C]
    [Field K] [Field L] [Field M]
    [Algebra A B] [Algebra B C] [Algebra A C]
    [Algebra A K] [Algebra B L] [Algebra C M]
    [Algebra K L] [Algebra L M] [Algebra K M]
    [Algebra A L] [Algebra B M] [Algebra A M]
    [IsScalarTower A B C] [IsScalarTower A B L] [IsScalarTower A K L]
    [IsScalarTower B C M] [IsScalarTower B L M]
    [IsScalarTower A C M] [IsScalarTower A K M] [IsScalarTower K L M]
    [IsExtension A B] [IsExtension B C]
    [IsExtension A C]
    [IsFractionRing A K] [IsFractionRing B L] [IsFractionRing C M]
    (p : ℕ) (hp : p.Prime) [CharP K p]
    [FiniteDimensional L M] [IsGalois L M]
    (hdegree : Module.finrank L M = p)
    (hweak : IsWeaklyUnramified A B)
    (hresidue : ∀ x : IsLocalRing.ResidueField B,
      (∃ a : IsLocalRing.ResidueField A,
          algebraMap (IsLocalRing.ResidueField A) (IsLocalRing.ResidueField B) a = x) ↔
        ∀ n : ℕ, 1 ≤ n → ∃ y : IsLocalRing.ResidueField B, y ^ (p ^ n) = x) :
    ∃ (K₁ : Type uK) (_ : Field K₁) (_ : Algebra K K₁) (_ : Algebra A K₁)
      (_ : IsScalarTower A K K₁) (_ : Module.Finite K K₁) (_ : IsGalois K K₁),
      IsTotallyRamifiedWithRespectTo A K K₁ ∧
        ∃ D : IntegralClosureBaseChange.{uA, uC, uK, uM, uK,
            max uM uK, uK, max uM uK} A C K M K₁,
          D.IsWeakSolution
```

## Tag 09F2, a lemma

[Tag 09F2](https://stacks.math.columbia.edu/tag/09F2) in the Stacks Project.

**`main_statement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/Cyclotomic/OneAddPow/QuotientPolynomial.lean, line 768](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/NumberTheory/Cyclotomic/OneAddPow/QuotientPolynomial.lean#L768).

> **Lemma 15.117.13 (Stacks tag 09F2).**
> Let `p` be prime, `A` a commutative ring containing a primitive `p`-th root of unity `ζ`
> (encoded by `f : ℤ[ζ_p] → A`), and `w = 1 - ζ`. Then there is ONE common polynomial
> `P ∈ A[z]` such that:
>
> * (Statement 1, integrality) `P` *is* the quotient `((1 + w z)^p - 1)/w^p` over `A`:
>   `w^p · P = (1 + wz)^p - 1` in `A[z]`, `P = ∑_{0 < i ≤ p} c_i z^i`, and
>   `w^{p-i} · c_i = (p choose i)` for `0 < i ≤ p` (predicate `intProp`). In particular `P` is
>   monic of degree `p`. The corresponding statement in `(A[w⁻¹])[z]` (predicate `quotChar`) is
>   recorded too, but it is weaker — vacuous when `w` is nilpotent, see
>   `quotChar_of_isNilpotent` — so it is `intProp` that carries the assertion "`P ∈ A[z]`";
> * (Statement 1, shape) `P(z) = z^p - z + ∑_{0 < i < p} a_i z^i` with `a_i ∈ (w)`
>   (predicate `shapeProp`);
> * (Statement 2, functional equation)
>   `P(z_1 + z_2 + w z_1 z_2) = P(z_1) + P(z_2) + w^p P(z_1) P(z_2)` in `A[z_1, z_2]`
>   (predicate `funcEq`).
>
> Bundling all of them into a single existential guarantees they hold for the same `P`.

```lean
theorem main_statement :
    ∃ P : A[X], intProp f P ∧ quotChar f P ∧ shapeProp f P ∧ funcEq f P
```

## Tag 09F3, a lemma

[Tag 09F3](https://stacks.math.columbia.edu/tag/09F3) in the Stacks Project.

**`isGalois_and_ramification_cases_of_adjoin_root_cyclotomic_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/Cyclotomic/OneAddPow/RamificationCases.lean, line 511](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/NumberTheory/Cyclotomic/OneAddPow/RamificationCases.lean#L511).

> Let `A` be a mixed-characteristic discrete valuation ring containing a primitive
> `p`-th root of unity, and let `P` be the cyclotomic quotient polynomial of Tag 09F2.
> If `L = K[z]` with `P(z) = ξ`, then `L / K` is Galois and is either trivial,
> unramified of degree `p`, totally ramified with ramification index `p`, or weakly
> unramified with purely inseparable residue extension of degree `p`.
>
> Moreover, for a uniformizer `π` of `A`, an integral `ξ` gives one of the first two
> cases; a pole of positive order not divisible by `p` gives the totally ramified case;
> and a pole whose order is divisible by `p` and whose leading coefficient is not a
> `p`-th power in the residue field gives the weakly unramified, residually inseparable
> case.

```lean
theorem isGalois_and_ramification_cases_of_adjoin_root_cyclotomic_quotient
    (A : Type uA) (K : Type uK) (L : Type uL)
    [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    [Field K] [Algebra A K] [IsFractionRing A K] [CharZero K]
    [Field L] [Algebra K L] [Algebra A L] [IsScalarTower A K L]
    (p : ℕ) [Fact p.Prime] [CharP (IsLocalRing.ResidueField A) p]
    (f : CyclotomicRing p ℤ ℚ →+* A) (P : Polynomial A)
    (hP : intProp f P ∧ quotChar f P ∧ shapeProp f P ∧ funcEq f P)
    (ξ : K) (z : L)
    (hz : Polynomial.aeval z P = algebraMap K L ξ)
    (hgen : Algebra.adjoin K {z} = ⊤)
    (π : A) (hπ : Irreducible π) :
    ∃ hfin : Module.Finite K L,
      letI := hfin
      let B := integralClosure A L
      let mA := IsLocalRing.maximalIdeal A
      let trivial : Prop := Function.Surjective (algebraMap K L)
      let unramified : Prop :=
        Module.finrank K L = p ∧
          ∀ m : Ideal B, m.IsMaximal → ∃ _ : m.LiesOver mA,
            Ideal.ramificationIdx' mA m = 1 ∧
              @Algebra.IsSeparable (A ⧸ mA) (B ⧸ m) _ _
                (Ideal.Quotient.algebraOfLiesOver m mA)
      let totallyRamified : Prop :=
        Stacks.KummerExtension.IsTotallyRamified A K L ∧
          ∀ m : Ideal B, m.IsMaximal → m.LiesOver mA →
            Ideal.ramificationIdx' mA m = p
      let residuallyInseparable : Prop :=
        ∃ hDVR : IsDiscreteValuationRing B,
          letI := hDVR
          let mB := IsLocalRing.maximalIdeal B
          ∃ _ : mB.LiesOver mA,
            Ideal.ramificationIdx' mA mB = 1 ∧
              letI := Ideal.Quotient.algebraOfLiesOver mB mA
              IsPurelyInseparable (A ⧸ mA) (B ⧸ mB) ∧
                Module.finrank (A ⧸ mA) (B ⧸ mB) = p
      IsGalois K L ∧
        (trivial ∨ unramified ∨ totallyRamified ∨ residuallyInseparable) ∧
        ((∃ a : A, ξ = algebraMap A K a) → trivial ∨ unramified) ∧
        (∀ (n : ℕ) (a : A), 0 < n → ¬p ∣ n → IsUnit a →
          ξ = (algebraMap A K π)⁻¹ ^ n * algebraMap A K a → totallyRamified) ∧
        (∀ (n : ℕ) (a : A), 0 < n → p ∣ n →
          (¬∃ b : IsLocalRing.ResidueField A, IsLocalRing.residue A a = b ^ p) →
          ξ = (algebraMap A K π)⁻¹ ^ n * algebraMap A K a →
            residuallyInseparable)
```

## Tag 09F4, a lemma

[Tag 09F4](https://stacks.math.columbia.edu/tag/09F4) in the Stacks Project.

**`Stacks.DegreePExtensionLevel.exists_totallyRamified_isGalois_isWeakSolution_or_finiteLevel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/ExtensionLevel/FiniteLevel.lean, line 1205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/ExtensionLevel/FiniteLevel.lean#L1205).

> **Stacks 09F4.** Let `A ⊆ B ⊆ C` be extensions of discrete valuation rings with fraction
> fields `K ⊆ L ⊆ M`, where `A` has mixed characteristic `(0, p)`, `A ⊆ B` is weakly unramified,
> `B` contains a primitive `p`-th root of unity (the ring map `f : ℤ[ζ_p] → B`) and `M / L` is
> Galois of degree `p`. Then there is a finite Galois extension `K₁ / K`, totally ramified with
> respect to `A`, which is either a weak solution for `A → C` or is such that
> `M₁ / L₁ = M ⊗_K K₁ / L ⊗_K K₁` is a degree-`p` extension of finite level.
>
> When the Kummer parameter of `M / L` has valuation prime to `p`, the proof of Stacks uses a
> degree-`p` totally ramified extension (Lemma 15.117.7, Tag 09EW), which in characteristic zero is
> `K(π ^ (1 / p))`; this is Galois over `K` only when `K` contains the `p`-th roots of unity. Here
> the base extension is instead the degree-`p` Galois, totally ramified extension of
> `Stacks.DegreePExtensionLevel.GaloisTotallyRamified.exists_isGalois_totallyRamified`, which
> contains an element `t` with `t ^ p = π V` for a unit `V`, and the rest of the argument of
> Stacks goes through with `t` in place of `π ^ (1 / p)`.

```lean
theorem exists_totallyRamified_isGalois_isWeakSolution_or_finiteLevel
    (A B C K L M : Type u)
    [CommRing A] [CommRing B] [CommRing C]
    [IsDomain A] [IsDomain B] [IsDomain C]
    [IsDiscreteValuationRing A] [IsDiscreteValuationRing B]
    [IsDiscreteValuationRing C]
    [Field K] [Field L] [Field M]
    [Algebra A B] [Algebra B C] [Algebra A C]
    [Algebra A K] [Algebra B L] [Algebra C M]
    [Algebra K L] [Algebra L M] [Algebra K M]
    [Algebra A L] [Algebra A M] [Algebra B M]
    [IsScalarTower A B C] [IsScalarTower A B L]
    [IsScalarTower B C M] [IsScalarTower B L M]
    [IsScalarTower A C M] [IsScalarTower A K L]
    [IsScalarTower A K M] [IsScalarTower K L M]
    [IsDiscreteValuationRing.IsExtension A B] [IsDiscreteValuationRing.IsExtension B C]
    [IsDiscreteValuationRing.IsExtension A C]
    [IsFractionRing A K] [IsFractionRing B L] [IsFractionRing C M]
    (p : ℕ) [Fact p.Prime] [CharZero K]
    [CharP (IsLocalRing.ResidueField A) p]
    (hweak : IsDiscreteValuationRing.IsWeaklyUnramified A B)
    (f : CyclotomicRing p ℤ ℚ →+* B)
    [FiniteDimensional L M] [IsGalois L M]
    (hdegree : Module.finrank L M = p) :
    ∃ (K₁ : Type u) (_ : Field K₁) (_ : Algebra K K₁) (_ : Algebra A K₁)
      (_ : IsScalarTower A K K₁) (_ : Module.Finite K K₁),
      IsGalois K K₁ ∧ IsDiscreteValuationRing.IsTotallyRamifiedWithRespectTo A K K₁ ∧
        ((∃ D : IsDiscreteValuationRing.IntegralClosureBaseChange.{u, u, u, u, u, u, u, u} A C K M
          K₁,
            D.IsWeakSolution) ∨
          let L₁ := L ⊗[K] K₁
          let M₁ := M ⊗[K] K₁
          ∃ (hL₁ : IsField L₁) (hM₁ : IsField M₁),
            letI := hL₁.toField
            letI := hM₁.toField
            let ι : L₁ →ₐ[K] M₁ :=
              Algebra.TensorProduct.map (IsScalarTower.toAlgHom K L M) (AlgHom.id K K₁)
            letI : Algebra L₁ M₁ := ι.toRingHom.toAlgebra
            let B₁ := integralClosure B L₁
            ∃ (hB₁ : IsDiscreteValuationRing B₁) (hfrac : IsFractionRing B₁ L₁)
              (hfin : Module.Finite L₁ M₁),
              letI := hB₁
              letI := hfrac
              letI := hfin
              ∃ P : Polynomial B,
                intProp f P ∧ quotChar f P ∧ shapeProp f P ∧ funcEq f P ∧
                  IsDegreePExtensionOfFiniteLevel B₁ L₁ M₁ p
                    ((algebraMap B B₁).comp f) (P.map (algebraMap B B₁)))
```

## Tag 09F5, a lemma

[Tag 09F5](https://stacks.math.columbia.edu/tag/09F5) in the Stacks Project.

**`Stacks.DiscreteValuationRing.EppLevelInduction.exists_totallyRamified_isWeakSolution_or_extensionLevel_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/ExtensionLevel/LevelLowering.lean, line 850](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/ExtensionLevel/LevelLowering.lean#L850).

> The traditional Tag 09F5 interface.  The global residue-field hypothesis identifies the
> perfect core with the image of the base residue field, so the finite-support alternative in
> `exists_totallyRamified_isWeakSolution_or_extensionLevel_le_or_finiteSupport_of_uniformizer` is
> impossible.

```lean
theorem exists_totallyRamified_isWeakSolution_or_extensionLevel_le
    (A B C K L M : Type u)
    [CommRing A] [CommRing B] [CommRing C]
    [IsDomain A] [IsDomain B] [IsDomain C]
    [IsDiscreteValuationRing A] [IsDiscreteValuationRing B]
    [IsDiscreteValuationRing C]
    [Field K] [Field L] [Field M]
    [Algebra A B] [Algebra B C] [Algebra A C]
    [Algebra A K] [Algebra B L] [Algebra C M]
    [Algebra K L] [Algebra L M] [Algebra K M]
    [Algebra A L] [Algebra A M] [Algebra B M]
    [IsScalarTower A B C] [IsScalarTower A B L]
    [IsScalarTower B C M] [IsScalarTower B L M]
    [IsScalarTower A C M] [IsScalarTower A K L]
    [IsScalarTower A K M] [IsScalarTower K L M]
    [IsDiscreteValuationRing.IsExtension A B] [IsDiscreteValuationRing.IsExtension B C]
    [IsDiscreteValuationRing.IsExtension A C]
    [IsFractionRing A K] [IsFractionRing B L] [IsFractionRing C M]
    (p : ℕ) [Fact p.Prime] [CharZero K]
    [CharP (IsLocalRing.ResidueField A) p]
    (hweak : IsDiscreteValuationRing.IsWeaklyUnramified A B)
    (f : CyclotomicRing p ℤ ℚ →+* B) (P : Polynomial B)
    (hP : intProp f P ∧ quotChar f P ∧ shapeProp f P ∧ funcEq f P)
    [Module.Finite L M]
    (hfinite : Stacks.DegreePExtensionLevel.IsDegreePExtensionOfFiniteLevel B L M p f P)
    (l : ℚ)
    (hlevel : ∃ (π : B) (e₁ : ℕ) (he₁ : 0 < e₁)
        (hne : (Stacks.DegreePExtensionLevel.extensionLevelNumerators B L M P π).Nonempty),
        Irreducible π ∧ Associated (wElt f) (π ^ e₁) ∧
          l = Stacks.DegreePExtensionLevel.extensionLevel B L M P π e₁ he₁ hne)
    (hl : 0 < l)
    (hresidue : ∀ x : IsLocalRing.ResidueField B,
      (∃ a : IsLocalRing.ResidueField A,
          algebraMap (IsLocalRing.ResidueField A) (IsLocalRing.ResidueField B) a = x) ↔
        ∀ n : ℕ, 1 ≤ n → ∃ y : IsLocalRing.ResidueField B, y ^ (p ^ n) = x) :
    ∃ (K₁ : Type u) (_ : Field K₁) (_ : Algebra K K₁) (_ : Algebra A K₁)
      (_ : IsScalarTower A K K₁) (_ : Module.Finite K K₁)
      (_ : Algebra.IsSeparable K K₁),
      IsDiscreteValuationRing.IsTotallyRamifiedWithRespectTo A K K₁ ∧
        ((∃ D : IsDiscreteValuationRing.IntegralClosureBaseChange.{u, u, u, u, u, u, u, u}
            A C K M K₁, D.IsWeakSolution) ∨
          let L₁ := L ⊗[K] K₁
          let M₁ := M ⊗[K] K₁
          ∃ (hL₁ : IsField L₁) (hM₁ : IsField M₁),
            letI := hL₁.toField
            letI := hM₁.toField
            let ι : L₁ →ₐ[K] M₁ :=
              Algebra.TensorProduct.map (IsScalarTower.toAlgHom K L M) (AlgHom.id K K₁)
            letI : Algebra L₁ M₁ := ι.toRingHom.toAlgebra
            let B₁ := integralClosure B L₁
            ∃ (hB₁ : IsDiscreteValuationRing B₁) (hfrac : IsFractionRing B₁ L₁)
              (hfin : Module.Finite L₁ M₁),
              letI := hB₁
              letI := hfrac
              letI := hfin
              let f₁ := (algebraMap B B₁).comp f
              let P₁ := P.map (algebraMap B B₁)
              Stacks.DegreePExtensionLevel.IsDegreePExtensionOfFiniteLevel B₁ L₁ M₁ p f₁ P₁ ∧
                ∃ (π₁ : B₁) (e₁ : ℕ) (he₁ : 0 < e₁)
                  (hne : (Stacks.DegreePExtensionLevel.extensionLevelNumerators B₁ L₁ M₁ P₁
                    π₁).Nonempty),
                  Irreducible π₁ ∧ Associated (wElt f₁) (π₁ ^ e₁) ∧
                    Stacks.DegreePExtensionLevel.extensionLevel B₁ L₁ M₁ P₁ π₁ e₁ he₁ hne ≤
                      max 0 (max (l - 1) (2 * l - (p : ℚ))))
```

## Tag 09F6, an equation

[Tag 09F6](https://stacks.math.columbia.edu/tag/09F6) in the Stacks Project.

**`IsDiscreteValuationRing.eval_sub_pow_sub_mem_uniformizer_zpow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/EliminateRamification.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/EliminateRamification.lean#L163).

> For the Kummer polynomial `P` associated to a primitive `p`-th root of unity,
> if `w = 1 - ζ` has order `e₁` and `π ^ n P(z)` is integral, then
> `P(z) ≡ z ^ p - z` modulo `π ^ (e₁ - n) B`.

```lean
theorem eval_sub_pow_sub_mem_uniformizer_zpow
    (B : Type uB) (K : Type uK)
    [CommRing B] [IsDomain B] [IsDiscreteValuationRing B]
    [Field K] [Algebra B K] [IsFractionRing B K]
    (p : ℕ) [Fact p.Prime]
    (f : CyclotomicRing p ℤ ℚ →+* B) (P : Polynomial B)
    (hP : shapeProp f P)
    (π : B) (hπ : Irreducible π) (e₁ n : ℕ)
    (hw : Associated (wElt f) (π ^ e₁)) (z : K)
    (hz : ∃ b : B,
      (algebraMap B K π) ^ n * P.eval₂ (algebraMap B K) z = algebraMap B K b) :
    ∃ b : B,
      P.eval₂ (algebraMap B K) z - (z ^ p - z) =
        (algebraMap B K π) ^ ((e₁ : ℤ) - n) * algebraMap B K b
```

## Tag 09F7, an equation

[Tag 09F7](https://stacks.math.columbia.edu/tag/09F7) in the Stacks Project.

**`IsDiscreteValuationRing.add_mul_correction_sModEq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/EliminateRamification.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/EliminateRamification.lean#L219).

> **Stacks 09F7.** The correction term in the finite-level group law vanishes modulo
> `π ^ (-2n + p e₁) B`.

```lean
theorem add_mul_correction_sModEq
    {B K : Type*} [CommRing B] [IsDomain B] [Field K]
    [Algebra B K] [IsFractionRing B K]
    {p n e₁ : ℕ} {π w : B} {ξ₁ ξ₂ : K}
    (hw : Associated w (π ^ e₁))
    (hξ₁ : ξ₁ ∈ FractionalIdeal.spanSingleton B⁰
      ((algebraMap B K π) ^ (-(n : ℤ))))
    (hξ₂ : ξ₂ ∈ FractionalIdeal.spanSingleton B⁰
      ((algebraMap B K π) ^ (-(n : ℤ)))) :
    SModEq (FractionalIdeal.spanSingleton B⁰
        ((algebraMap B K π) ^ (-(2 : ℤ) * n + p * e₁ : ℤ)) : Submodule B K)
      (ξ₁ + ξ₂ + (algebraMap B K w) ^ p * ξ₁ * ξ₂) (ξ₁ + ξ₂)
```

## Tag 09F8, a lemma

[Tag 09F8](https://stacks.math.columbia.edu/tag/09F8) in the Stacks Project.

**`IsDiscreteValuationRing.exists_finite_extension_isWeakSolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/EppAlgClosedResidue/IntermediateFieldInduction.lean, line 681](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/EppAlgClosedResidue/IntermediateFieldInduction.lean#L681).

> Epp's theorem in the complete case: under the residue-field intersection
> hypothesis, every finite extension at the top of a weakly unramified tower admits
> a finite base extension which is a weak solution for the full tower.

```lean
theorem exists_finite_extension_isWeakSolution
    (A : Type uA) (B : Type uB) (C : Type uC)
    (K : Type uK) (L : Type uL) (M : Type uM)
    [CommRing A] [CommRing B] [CommRing C]
    [IsDomain A] [IsDomain B] [IsDomain C]
    [IsDiscreteValuationRing A] [IsDiscreteValuationRing B]
    [IsDiscreteValuationRing C]
    [Field K] [Field L] [Field M]
    [Algebra A B] [Algebra B C] [Algebra A C]
    [Algebra A K] [Algebra B L] [Algebra C M]
    [Algebra K L] [Algebra L M] [Algebra K M]
    [Algebra A L] [Algebra B M] [Algebra A M]
    [IsScalarTower A B C] [IsScalarTower A B L] [IsScalarTower A K L]
    [IsScalarTower B C M] [IsScalarTower B L M]
    [IsScalarTower A C M] [IsScalarTower A K M] [IsScalarTower K L M]
    [IsDiscreteValuationRing.IsExtension A B] [IsDiscreteValuationRing.IsExtension B C]
    [IsDiscreteValuationRing.IsExtension A C]
    [IsFractionRing A K] [IsFractionRing B L] [IsFractionRing C M]
    (p : ℕ) [Fact p.Prime] [CharP (IsLocalRing.ResidueField A) p]
    [IsAlgClosed (IsLocalRing.ResidueField A)]
    [IsAdicComplete (IsLocalRing.maximalIdeal A) A]
    [IsAdicComplete (IsLocalRing.maximalIdeal B) B]
    (hweak : IsDiscreteValuationRing.IsWeaklyUnramified A B)
    [Module.Finite L M]
    (hresidue : ∀ x : IsLocalRing.ResidueField B,
      (∃ a : IsLocalRing.ResidueField A,
          algebraMap (IsLocalRing.ResidueField A) (IsLocalRing.ResidueField B) a = x) ↔
        ∀ n : ℕ, 1 ≤ n → ∃ y : IsLocalRing.ResidueField B, y ^ (p ^ n) = x) :
    ∃ (K₁ : Type uK) (_ : Field K₁) (_ : Algebra K K₁) (_ : Algebra A K₁)
      (_ : IsScalarTower A K K₁) (_ : Module.Finite K K₁),
      ∃ D : IsDiscreteValuationRing.IntegralClosureBaseChange.{uA, uC, uK, uM, uK,
          max uM uK, uK, max uM uK} A C K M K₁,
        D.IsWeakSolution
```

## Tag 09F9, a theorem

[Tag 09F9](https://stacks.math.columbia.edu/tag/09F9) in the Stacks Project.

**`Stacks.EppTheorem.exists_finite_extension_isWeakSolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/EppTheorem.lean, line 26](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/EppTheorem.lean#L26).

> Epp's theorem when all input types lie in one universe.

```lean
theorem exists_finite_extension_isWeakSolution
    (A B K L : Type u)
    [CommRing A] [CommRing B] [IsDomain A] [IsDomain B]
    [IsDiscreteValuationRing A] [IsDiscreteValuationRing B]
    [Field K] [Field L]
    [Algebra A B] [Algebra A K] [Algebra A L] [Algebra B L] [Algebra K L]
    [IsScalarTower A B L] [IsScalarTower A K L]
    [IsExtension A B] [IsFractionRing A K] [IsFractionRing B L]
    (hEpp : ∀ p : ℕ, p.Prime → CharP (ResidueField A) p →
      ∀ [ExpChar (ResidueField B) p], EppCondition A B p) :
    ∃ (K₁ : Type u) (_ : Field K₁) (_ : Algebra K K₁) (_ : Algebra A K₁)
      (_ : IsScalarTower A K K₁) (_ : Module.Finite K K₁),
      ∃ D : IntegralClosureBaseChange.{u, u, u, u, u, u, u, u} A B K L K₁,
        D.IsWeakSolution
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.117, Tag 09EL](https://stacks.math.columbia.edu/tag/09EL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
