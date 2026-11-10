---
declaration: section
origin: cited
lean: Crystalline.DzDecomposition, Crystalline.DzDecomposition.dOne, Crystalline.DzDecomposition.partialZ, Crystalline.DzDecomposition.dOne_add_partialZ_smul, Crystalline.exists_homotopyInverse_baseChangeDeRhamMap_baseLinear, Crystalline.exists_homotopyInverse_baseChangeDeRhamMap, Crystalline.oneVariableTheta_apply, Crystalline.oneVariable_sub_theta_partialZ
statement: formalized
proof: formalized
---

# 60.25 Pulling back along purely inseparable maps

Section 60.25 of the Stacks Project, [Tag 07PZ](https://stacks.math.columbia.edu/tag/07PZ). 7 tags here are carried by 10 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07Q1, an item

[Tag 07Q1](https://stacks.math.columbia.edu/tag/07Q1) in the Stacks Project.

Declarations registered for the tag:

- [`Crystalline.DzDecomposition`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChangeHomotopyInverse/DzDecomposition.lean#L45), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChangeHomotopyInverse/Existence.lean, line 790](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChangeHomotopyInverse/Existence.lean#L790) (StacksFrontier): “the decomposition of one-forms”.
- [`Crystalline.DzDecomposition.dOne`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChangeHomotopyInverse/DzDecomposition.lean#L60), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChangeHomotopyInverse/Existence.lean, line 791](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChangeHomotopyInverse/Existence.lean#L791) (StacksFrontier): “the component d\_1 of the differential”.
- [`Crystalline.DzDecomposition.partialZ`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChangeHomotopyInverse/DzDecomposition.lean#L64), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChangeHomotopyInverse/Existence.lean, line 792](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChangeHomotopyInverse/Existence.lean#L792) (StacksFrontier): “the coefficient of dz in the differential”.
- [`Crystalline.DzDecomposition.dOne_add_partialZ_smul`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChangeHomotopyInverse/DzDecomposition.lean#L70), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChangeHomotopyInverse/Existence.lean, line 794](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChangeHomotopyInverse/Existence.lean#L794) (StacksFrontier): “the equation d(f) = d\_1(f) + the coefficient of dz times dz”.

## Tag 07Q7, a lemma

[Tag 07Q7](https://stacks.math.columbia.edu/tag/07Q7) in the Stacks Project.

**`Crystalline.exists_homotopyInverse_baseChangeDeRhamMap_baseLinear`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChangeHomotopyInverse/Existence.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChangeHomotopyInverse/Existence.lean#L139). The attribute's comment: “with the B-linearity of the reverse map e and of the homotopy h, which the p-adically completed form of Tag 07N1 needs”.

> **Stacks 07Q7 (Lemma 60.25.1).** In the situation of Section 60.25 — a commutative square
> `B → B'` over `A → A'`, quotients `Ω_{B/A} → Ω` and `Ω_{B'/A'} → Ω'` to which the de Rham
> differential descends, a compatible `ψ : Ω → Ω'`, a `B`-module `M` with integrable connection
> `∇`, the canonical map of complexes `c_M^•` of equation 07PY, and data `a ∈ B`, `z ∈ B'`,
> `θ : B' → B'` satisfying assumptions (1)–(7) — there exists a map of complexes
>
> `e_M^• : M ⊗_B (Ω')^• ⟶ M ⊗_B Ω^•`
>
> such that `c_M^• ∘ e_M^•` and `e_M^• ∘ c_M^•` are homotopic to multiplication by `a`.

```lean
public theorem exists_homotopyInverse_baseChangeDeRhamMap_baseLinear
    (S : SourceDeRham A B) (S' : SourceDeRham A' B')
    (pi : Ω[B⁄A] →ₗ[B] Omega) (pi' : Ω[B'⁄A'] →ₗ[B'] Omega')
    (hpi : Function.Surjective pi) (hgen : S.GenerationHypothesis pi)
    (hpi' : Function.Surjective pi') (hgen' : S'.GenerationHypothesis pi')
    (psi : Omega →ₛₗ[algebraMap B B'] Omega')
    (hpsi : ∀ b : B, psi (pi (KaehlerDifferential.D A B b)) =
      pi' (KaehlerDifferential.D A' B' (algebraMap B B' b)))
    (nabla : Connection A B pi M)
    (hintegrable : Connection.IsIntegrable S pi hpi hgen nabla)
    (c : ∀ p : ℕ,
      RestrictScalars A B (M ⊗[B] (⋀[B]^p Omega)) →ₗ[A]
        RestrictScalars A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^p Omega')))
    (hc_wedge : ∀ (p : ℕ) (m : M) (omega : Fin p → Omega),
      c p (m ⊗ₜ[B] exteriorPower.ιMulti B p omega) =
        (1 ⊗ₜ[B] m) ⊗ₜ[B'] exteriorPower.ιMulti B' p (psi ∘ omega))
    (hc_comm : ∀ (p : ℕ) (x : M ⊗[B] (⋀[B]^p Omega)),
      c (p + 1)
          ((extendedConnection S pi hpi hgen nabla).toLinearMap p x) =
        (extendedConnection S' pi' hpi' hgen'
          (Connection.baseChange psi nabla hpsi)).toLinearMap p (c p x))
    (a : B) (z : B') (theta : B' →ₗ[B] B')
    (dec : DzDecomposition pi' psi z)
    (hd_a_eq_zero : SourceDeRham.targetD pi a = 0)
    (hpartialZ_theta : ∀ f : B', dec.partialZ (theta f) = a • f)
    (huniv :
      Stacks.UniversalInjectivity.LocalizationCriteria.UniversallyInjective.{max u w}
        (Algebra.linearMap B B'))
    (hepsilon : ∀ f : B',
      a • f - theta (dec.partialZ f) ∈ Set.range (algebraMap B B'))
    (hepsilonPrime : ∀ f : B',
      TensorProduct.map theta (LinearMap.id (R := B) (M := Omega)) (dec.dOne f) -
          dec.dOne (theta f) ∈
        LinearMap.range (TensorProduct.mk B B' Omega 1)) :
    ∃ e : ∀ p : ℕ,
      RestrictScalars A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^p Omega')) →ₗ[A]
        RestrictScalars A B (M ⊗[B] (⋀[B]^p Omega)),
      (∀ (p : ℕ) (x : RestrictScalars A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^p Omega'))),
          e (p + 1)
              ((extendedConnection S' pi' hpi' hgen'
                (Connection.baseChange psi nabla hpsi)).toLinearMap
                p x) =
            (extendedConnection S pi hpi hgen nabla).toLinearMap
              p (e p x)) ∧
        (∀ (p : ℕ) (b : B) (y : RestrictScalars A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^p Omega'))),
            e p (RestrictScalars.lsmul A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^p Omega'))
                (algebraMap B B' b) y) =
              RestrictScalars.lsmul A B (M ⊗[B] (⋀[B]^p Omega)) b (e p y)) ∧
        (∃ h : ∀ p : ℕ,
            RestrictScalars A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^(p + 1) Omega')) →ₗ[A]
              RestrictScalars A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^p Omega')),
          (∀ x : RestrictScalars A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^0 Omega')),
              h 0 ((extendedConnection S' pi' hpi' hgen'
                (Connection.baseChange psi nabla hpsi)).toLinearMap
                0 x) =
                RestrictScalars.lsmul A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^0 Omega'))
                    (algebraMap B B' a) x -
                  c 0 (e 0 x)) ∧
            (∀ (p : ℕ)
                (x : RestrictScalars A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^(p + 1) Omega'))),
              (show RestrictScalars A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^(p + 1) Omega')) from
                (extendedConnection S' pi' hpi' hgen'
                  (Connection.baseChange psi nabla hpsi)).toLinearMap
                    p (h p x)) +
                  h (p + 1)
                    ((extendedConnection S' pi' hpi' hgen'
                      (Connection.baseChange psi nabla hpsi)).toLinearMap
                      (p + 1) x) =
                RestrictScalars.lsmul A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^(p + 1) Omega'))
                    (algebraMap B B' a) x -
                  c (p + 1) (e (p + 1) x)) ∧
            (∀ (p : ℕ) (b : B)
                (y : RestrictScalars A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^(p + 1) Omega'))),
              h p (RestrictScalars.lsmul A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^(p + 1) Omega'))
                  (algebraMap B B' b) y) =
                RestrictScalars.lsmul A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^p Omega'))
                  (algebraMap B B' b) (h p y))) ∧
        (∃ k : ∀ p : ℕ,
            RestrictScalars A B (M ⊗[B] (⋀[B]^(p + 1) Omega)) →ₗ[A]
              RestrictScalars A B (M ⊗[B] (⋀[B]^p Omega)),
          (∀ x : RestrictScalars A B (M ⊗[B] (⋀[B]^0 Omega)),
              k 0 ((extendedConnection S pi hpi hgen nabla).toLinearMap
                0 x) =
                RestrictScalars.lsmul A B (M ⊗[B] (⋀[B]^0 Omega)) a x - e 0 (c 0 x)) ∧
            (∀ (p : ℕ) (x : RestrictScalars A B (M ⊗[B] (⋀[B]^(p + 1) Omega))),
              (extendedConnection S pi hpi hgen nabla).toLinearMap
                  p (k p x) +
                k (p + 1)
                  ((extendedConnection S pi hpi hgen nabla).toLinearMap
                    (p + 1) x) =
                RestrictScalars.lsmul A B (M ⊗[B] (⋀[B]^(p + 1) Omega)) a x -
                  e (p + 1) (c (p + 1) x)) ∧
            (∀ (p : ℕ) (b : B) (x : RestrictScalars A B (M ⊗[B] (⋀[B]^(p + 1) Omega))),
              k p (RestrictScalars.lsmul A B (M ⊗[B] (⋀[B]^(p + 1) Omega)) b x) =
                RestrictScalars.lsmul A B (M ⊗[B] (⋀[B]^p Omega)) b (k p x)))
```

**`Crystalline.exists_homotopyInverse_baseChangeDeRhamMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChangeHomotopyInverse/Existence.lean, line 368](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChangeHomotopyInverse/Existence.lean#L368).

> Let `c_M^• : M ⊗_B Ω^• ⟶ (M ⊗_B B') ⊗_{B'} (Ω')^•` be the base change map of de Rham
> complexes of a `B`-module `M` with integrable connection `∇`. Given `a ∈ B` with `d(a) = 0`, a
> decomposition `Ω' = (B' ⊗_B Ω) ⊕ B' dz`, and a `B`-linear `θ : B' → B'` with `∂_z ∘ θ = a`,
> `a f - θ(∂_z(f)) ∈ B` and `(θ ⊗ 1)(d₁(f)) - d₁(θ(f)) ∈ Ω` for all `f ∈ B'`, and with `B → B'`
> universally injective, there is a map of complexes
> `e_M^• : (M ⊗_B B') ⊗_{B'} (Ω')^• ⟶ M ⊗_B Ω^•` such that `c_M^• ∘ e_M^•` and `e_M^• ∘ c_M^•`
> are both homotopic to multiplication by `a`.

```lean
public theorem exists_homotopyInverse_baseChangeDeRhamMap
    (S : SourceDeRham A B) (S' : SourceDeRham A' B')
    (pi : Ω[B⁄A] →ₗ[B] Omega) (pi' : Ω[B'⁄A'] →ₗ[B'] Omega')
    (hpi : Function.Surjective pi) (hgen : S.GenerationHypothesis pi)
    (hpi' : Function.Surjective pi') (hgen' : S'.GenerationHypothesis pi')
    (psi : Omega →ₛₗ[algebraMap B B'] Omega')
    (hpsi : ∀ b : B, psi (pi (KaehlerDifferential.D A B b)) =
      pi' (KaehlerDifferential.D A' B' (algebraMap B B' b)))
    (nabla : Connection A B pi M)
    (hintegrable : Connection.IsIntegrable S pi hpi hgen nabla)
    (c : ∀ p : ℕ,
      RestrictScalars A B (M ⊗[B] (⋀[B]^p Omega)) →ₗ[A]
        RestrictScalars A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^p Omega')))
    (hc_wedge : ∀ (p : ℕ) (m : M) (omega : Fin p → Omega),
      c p (m ⊗ₜ[B] exteriorPower.ιMulti B p omega) =
        (1 ⊗ₜ[B] m) ⊗ₜ[B'] exteriorPower.ιMulti B' p (psi ∘ omega))
    (hc_comm : ∀ (p : ℕ) (x : M ⊗[B] (⋀[B]^p Omega)),
      c (p + 1)
          ((extendedConnection S pi hpi hgen nabla).toLinearMap p x) =
        (extendedConnection S' pi' hpi' hgen'
          (Connection.baseChange psi nabla hpsi)).toLinearMap p (c p x))
    (a : B) (z : B') (theta : B' →ₗ[B] B')
    (dec : DzDecomposition pi' psi z)
    (hd_a_eq_zero : SourceDeRham.targetD pi a = 0)
    (hpartialZ_theta : ∀ f : B', dec.partialZ (theta f) = a • f)
    (huniv :
      Stacks.UniversalInjectivity.LocalizationCriteria.UniversallyInjective.{max u w}
        (Algebra.linearMap B B'))
    (hepsilon : ∀ f : B',
      a • f - theta (dec.partialZ f) ∈ Set.range (algebraMap B B'))
    (hepsilonPrime : ∀ f : B',
      TensorProduct.map theta (LinearMap.id (R := B) (M := Omega)) (dec.dOne f) -
          dec.dOne (theta f) ∈
        LinearMap.range (TensorProduct.mk B B' Omega 1)) :
    ∃ e : ∀ p : ℕ,
      RestrictScalars A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^p Omega')) →ₗ[A]
        RestrictScalars A B (M ⊗[B] (⋀[B]^p Omega)),
      (∀ (p : ℕ) (x : RestrictScalars A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^p Omega'))),
          e (p + 1)
              ((extendedConnection S' pi' hpi' hgen'
                (Connection.baseChange psi nabla hpsi)).toLinearMap
                p x) =
            (extendedConnection S pi hpi hgen nabla).toLinearMap
              p (e p x)) ∧
        (∃ h : ∀ p : ℕ,
            RestrictScalars A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^(p + 1) Omega')) →ₗ[A]
              RestrictScalars A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^p Omega')),
          (∀ x : RestrictScalars A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^0 Omega')),
              h 0 ((extendedConnection S' pi' hpi' hgen'
                (Connection.baseChange psi nabla hpsi)).toLinearMap
                0 x) =
                RestrictScalars.lsmul A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^0 Omega'))
                    (algebraMap B B' a) x -
                  c 0 (e 0 x)) ∧
            ∀ (p : ℕ)
                (x : RestrictScalars A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^(p + 1) Omega'))),
              (show RestrictScalars A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^(p + 1) Omega')) from
                (extendedConnection S' pi' hpi' hgen'
                  (Connection.baseChange psi nabla hpsi)).toLinearMap
                    p (h p x)) +
                  h (p + 1)
                    ((extendedConnection S' pi' hpi' hgen'
                      (Connection.baseChange psi nabla hpsi)).toLinearMap
                      (p + 1) x) =
                RestrictScalars.lsmul A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^(p + 1) Omega'))
                    (algebraMap B B' a) x -
                  c (p + 1) (e (p + 1) x)) ∧
        (∃ k : ∀ p : ℕ,
            RestrictScalars A B (M ⊗[B] (⋀[B]^(p + 1) Omega)) →ₗ[A]
              RestrictScalars A B (M ⊗[B] (⋀[B]^p Omega)),
          (∀ x : RestrictScalars A B (M ⊗[B] (⋀[B]^0 Omega)),
              k 0 ((extendedConnection S pi hpi hgen nabla).toLinearMap
                0 x) =
                RestrictScalars.lsmul A B (M ⊗[B] (⋀[B]^0 Omega)) a x - e 0 (c 0 x)) ∧
            ∀ (p : ℕ) (x : RestrictScalars A B (M ⊗[B] (⋀[B]^(p + 1) Omega))),
              (extendedConnection S pi hpi hgen nabla).toLinearMap
                  p (k p x) +
                k (p + 1)
                  ((extendedConnection S pi hpi hgen nabla).toLinearMap
                    (p + 1) x) =
                RestrictScalars.lsmul A B (M ⊗[B] (⋀[B]^(p + 1) Omega)) a x -
                  e (p + 1) (c (p + 1) x))
```

## Tag 07Q8, an example

[Tag 07Q8](https://stacks.math.columbia.edu/tag/07Q8) in the Stacks Project.

**`Crystalline.oneVariableTheta_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/RelativePoincare.lean, line 1030](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/RelativePoincare.lean#L1030). The attribute's comment: “the operator θ”.

> **The operator `θ` of Example 07Q8.**  It raises the divided power degree of the variable by
> one in every term of the divided power monomial expansion: `θ(∑ bₘ z^[m]) = ∑ bₘ z^[m+1]`.

```lean
public theorem oneVariableTheta_apply (f : oneVariableDividedPowerPolynomial B) :
    oneVariableTheta B f =
      ((oneVariableMonomialBasis B).repr f).sum fun m b =>
        b • (oneVariableDividedPowers B).dpow (m + 1) (oneVariableVariable B)
```

**`Crystalline.oneVariable_sub_theta_partialZ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/RelativePoincare.lean, line 1058](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/RelativePoincare.lean#L1058). The attribute's comment: “f - θ(∂\_z f) = f(0)”.

> **Assumption (6) of Section 60.25 at `a = 1`, in sharp form.**  The difference
> `f - θ(∂_z(f))` is the constant term `f(0)` of `f`, the image under `B → B⟨z⟩` of the
> augmentation of `f`.

```lean
public theorem oneVariable_sub_theta_partialZ (f : oneVariableDividedPowerPolynomial B) :
    f - oneVariableTheta B (oneVariablePartialZ A B f) =
      algebraMap (B : Type u) (oneVariableDividedPowerPolynomial B)
        (dividedPowerPolynomialAugmentation (B : Type u) Unit f)
```

**`Crystalline.oneVariableDividedPowerPolynomial_standingAssumptions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/RelativePoincare.lean, line 1087](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/RelativePoincare.lean#L1087). The attribute's comment: “the seven standing assumptions for B⟨z⟩ at a = 1”.

> **Example 07Q8, the verification of the standing assumptions.**  For a divided power ring
> `(B, J, δ)` over `A`, the divided power polynomial ring `B' = B⟨z⟩` with its divided powers on
> `J' = B'₊ + JB'`, the quotients `Ω = Ω¹_{B/A,δ}` and `Ω' = Ω¹_{B'/A,δ'}`, the element `a = 1` and
> the operator `θ` of `Crystalline.oneVariableTheta` satisfy the seven standing assumptions of
> Section 60.25: `d(1) = 0`, the decomposition `Ω' = (B' ⊗_B Ω) ⊕ B' dz`, `B`-linearity of `θ`,
> `∂_z ∘ θ = 1`, universal injectivity of `B → B'`, `f - θ(∂_z(f)) ∈ B`, and
> `(θ ⊗ 1)(d₁(f)) - d₁(θ(f)) ∈ Ω`.

```lean
public theorem oneVariableDividedPowerPolynomial_standingAssumptions :
    ∃ dec : DzDecomposition (oneVariablePolyProjection A B)
      (dividedPowerPolynomialOneFormComparison A B) (oneVariableVariable B),
      SourceDeRham.targetD (oneVariableBaseProjection A B) (1 : (B : Type u)) = 0 ∧
      (∀ f : oneVariableDividedPowerPolynomial B,
        dec.partialZ (oneVariableTheta B f) = (1 : (B : Type u)) • f) ∧
      Stacks.UniversalInjectivity.LocalizationCriteria.UniversallyInjective.{v}
        (Algebra.linearMap (B : Type u) (oneVariableDividedPowerPolynomial B)) ∧
      (∀ f : oneVariableDividedPowerPolynomial B,
        (1 : (B : Type u)) • f - oneVariableTheta B (dec.partialZ f) ∈
          Set.range (algebraMap (B : Type u) (oneVariableDividedPowerPolynomial B))) ∧
      (∀ f : oneVariableDividedPowerPolynomial B,
        TensorProduct.map (oneVariableTheta B)
            (LinearMap.id (R := (B : Type u))
              (M := dividedPowerDifferentials (A := A) B.dividedPowers)) (dec.dOne f) -
            dec.dOne (oneVariableTheta B f) ∈
          LinearMap.range (TensorProduct.mk (B : Type u)
            (oneVariableDividedPowerPolynomial B)
            (dividedPowerDifferentials (A := A) B.dividedPowers) 1))
```

**`Crystalline.exists_homotopyEquiv_oneVariableDeRhamComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/RelativePoincare.lean, line 1131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/RelativePoincare.lean#L1131). The attribute's comment: “Lemma 07Q7 at a = 1 for B⟨z⟩”.

> **Example 07Q8, the conclusion.**  Let `(B, J, δ)` be a divided power ring which is an
> `A`-algebra, let `B⟨z⟩` be the divided power polynomial ring on one divided power variable, and
> let `M` carry an integrable connection `∇ : M → M ⊗_B Ω¹_{B/A,δ}`.  Then the canonical map of de
> Rham complexes `c_M^• : M ⊗_B Ω^*_{B/A,δ} ⟶ M ⊗_B Ω^*_{B⟨z⟩/A,δ'}` is a homotopy equivalence.

```lean
public theorem exists_homotopyEquiv_oneVariableDeRhamComparison
    (nabla : Connection A (B : Type u) (oneVariableBaseProjection A B) M)
    (hint : Connection.IsIntegrable (oneVariableBaseSource A B) (oneVariableBaseProjection A B)
      (Submodule.mkQ_surjective _) (oneVariableBaseGenerationHypothesis A B) nabla)
    (c : ∀ p : ℕ, oneVariableSourceTerm A B M p →ₗ[A] oneVariableTargetTerm A B M p)
    (hc_wedge : ∀ (p : ℕ) (m : M)
        (omega : Fin p → dividedPowerDifferentials (A := A) B.dividedPowers),
      c p (m ⊗ₜ[(B : Type u)] exteriorPower.ιMulti (B : Type u) p omega) =
        ((1 : oneVariableDividedPowerPolynomial B) ⊗ₜ[(B : Type u)] m) ⊗ₜ[
          oneVariableDividedPowerPolynomial B]
          exteriorPower.ιMulti (oneVariableDividedPowerPolynomial B) p
            (dividedPowerPolynomialOneFormComparison A B ∘ omega))
    (hc : ∀ (p : ℕ) (x : oneVariableSourceTerm A B M p),
      c (p + 1) ((extendedConnection (oneVariableBaseSource A B)
            (oneVariableBaseProjection A B) (Submodule.mkQ_surjective _)
            (oneVariableBaseGenerationHypothesis A B) nabla).toLinearMap p x) =
        (extendedConnection (oneVariablePolySource A B) (oneVariablePolyProjection A B)
          (Submodule.mkQ_surjective _) (oneVariablePolyGenerationHypothesis A B)
          (oneVariableBaseChangeConnection A B nabla)).toLinearMap p (c p x)) :
    ∃ E : HomotopyEquiv (oneVariableSourceDeRhamComplex A B nabla hint)
        (oneVariableTargetDeRhamComplex A B nabla hint),
      E.hom = oneVariableDeRhamComparison A B nabla hint c hc
```

## Tag 07N1, a lemma

[Tag 07N1](https://stacks.math.columbia.edu/tag/07N1) in the Stacks Project.

**`Crystalline.PthRootExtension.exists_homotopyInverse_completedPthRootExtension_situation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/PthRootCompletedSituation.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/PthRootCompletedSituation.lean#L74). The attribute's comment: “in Situation 07MD with D the completed divided power envelope of 07J8 and the completed forms of 07J9; for every completed connection integrable in the sense of 07I0”.

> **[Stacks, Lemma 60.25.3, Tag 07N1].**
>
> In Situation 07MD (`s`), let `P = A[x_i] → C` be a surjective polynomial presentation (`f`, `hf`),
> let `D` be the `p`-adic completion of the divided power envelope `D_{P,γ}(ker f)` with its divided
> powers `γ̄` (07J8, [Stacks, Tag 07KG]), and let `Ω^q_D` be the `p`-adic completion of the divided
> power forms of `D` over `A` (07J9, in its second form `Ω_D = lim_e Ω_{D/A,γ̄}/p^e`).  Let `λ ∈ D`,
> let `D'` be the `p`-adic completion of `D[z]⟨ξ⟩/(ξ - (z^p - λ))` with the divided powers of
> [Stacks, Tag 07KD], and let `Ω^q_{D'}` be the `p`-adic completion of the divided power forms of
> `D'` over `A`.  Let `M` be a `D`-module with a connection `∇ : M → M ⊗̂_D Ω_D` (07JC), integrable
> (07JD) in the sense of [Stacks, Remark 60.6.1, Tag 07I0]: the composite `M → M ⊗̂ Ω¹ → M ⊗̂ Ω²`
> vanishes.  Then:
>
> * `M ⊗^∧_D Ω^•_D` and `M ⊗^∧_D Ω^•_{D'}` are complexes;
> * the canonical map `c_M^• : M ⊗^∧_D Ω^•_D → M ⊗^∧_D Ω^•_{D'}` of (07PY) is a map of complexes;
> * there is a map of complexes `e_M^•` in the opposite direction with `e_M^• ∘ c_M^• = p`, so that
>   `e_M^• ∘ c_M^•` is homotopic to `p` (by the zero homotopy), and a homotopy `h` with
>   `h d = p - c_M^• ∘ e_M^•` in degree `0` and `d h + h d = p - c_M^• ∘ e_M^•` in positive degrees,
>   so that `c_M^• ∘ e_M^•` is homotopic to `p`; moreover `h ∘ c_M^• = 0`.
>
> The hypotheses (07JB), completeness of `M`, and (07JE), quasi-nilpotence of `∇`, are not needed
> and are not assumed.

```lean
theorem exists_homotopyInverse_completedPthRootExtension_situation
    (lam : (𝒟 : Type u)) (M : Type u) [AddCommGroup M] [Module (𝒟 : Type u) M]
    (nabla : CompletedConnection s.p (𝒟 : Type u)
      (completedDividedPowerForms s.p (s.A : Type u) (𝒟).dividedPowers 1)
      (completedDividedPowerDifferentialOnRing s.p (s.A : Type u) (𝒟).dividedPowers) M)
    (hint : IsCompletedIntegrable s.p (s.A : Type u) (𝒟 : Type u) (𝒟).dividedPowers M nabla) :
    CompletedDeRham.IsSquareZero s.p (𝒟 : Type u) (completedDividedPowerForms s.p (s.A : Type u)
        (𝒟).dividedPowers)
        (completedDividedPowerWedgeOnRing s.p (s.A : Type u) (𝒟).dividedPowers)
        (completedDividedPowerDeRham s.p (s.A : Type u) (𝒟).dividedPowers) M nabla
        (isGradedLeibniz_completedDividedPowerOnRing s.p (s.A : Type u) (𝒟).dividedPowers) ∧
      CompletedDeRham.IsSquareZero s.p (completedPrimeRingSelf 𝒟 s.p lam)
        (completedDividedPowerForms s.p (s.A : Type u)
          (completedPrimeDividedPowers 𝒟 s.p lam (Fact.out : s.p.Prime).ne_zero
              (completedEnvelopeOfPresentation_prime_nilpotent s f hf)))
        (completedDividedPowerWedgeOnRing s.p (s.A : Type u)
          (completedPrimeDividedPowers 𝒟 s.p lam (Fact.out : s.p.Prime).ne_zero
              (completedEnvelopeOfPresentation_prime_nilpotent s f hf)))
        (completedDividedPowerDeRham s.p (s.A : Type u)
          (completedPrimeDividedPowers 𝒟 s.p lam (Fact.out : s.p.Prime).ne_zero
              (completedEnvelopeOfPresentation_prime_nilpotent s f hf)))
        (genuineCarrier 𝒟 s.p lam M)
        (genuineCompletedConnection (s.A : Type u) 𝒟 s.p lam (Fact.out : s.p.Prime).ne_zero
            (completedEnvelopeOfPresentation_prime_nilpotent s f hf) M nabla)
        (isGradedLeibniz_completedDividedPowerOnRing s.p (s.A : Type u) _) ∧
      (∀ q : ℕ, (genuineCompletedDifferential (s.A : Type u) 𝒟 s.p lam (Fact.out :
          s.p.Prime).ne_zero
          (completedEnvelopeOfPresentation_prime_nilpotent s f hf) M nabla
          q).comp (genuineCompletedComparison (s.A : Type u) 𝒟 s.p lam (Fact.out :
              s.p.Prime).ne_zero
              (completedEnvelopeOfPresentation_prime_nilpotent s f hf) M q) =
        (genuineCompletedComparison (s.A : Type u) 𝒟 s.p lam (Fact.out : s.p.Prime).ne_zero
            (completedEnvelopeOfPresentation_prime_nilpotent s f hf) M (q + 1)).comp
          (baseCompletedDifferential (s.A : Type u) 𝒟 s.p M nabla q)) ∧
      ∃ (e : ∀ q : ℕ, genuineCompletedTerm (s.A : Type u) 𝒟 s.p lam (Fact.out : s.p.Prime).ne_zero
          (completedEnvelopeOfPresentation_prime_nilpotent s f hf) M q →+
          baseCompletedTerm (s.A : Type u) 𝒟 s.p M q)
        (h : ∀ q : ℕ, genuineCompletedTerm (s.A : Type u) 𝒟 s.p lam (Fact.out : s.p.Prime).ne_zero
            (completedEnvelopeOfPresentation_prime_nilpotent s f hf) M (q + 1) →+
          genuineCompletedTerm (s.A : Type u) 𝒟 s.p lam (Fact.out : s.p.Prime).ne_zero
              (completedEnvelopeOfPresentation_prime_nilpotent s f hf) M q),
        (∀ (q : ℕ) (y : genuineCompletedTerm (s.A : Type u) 𝒟 s.p lam (Fact.out : s.p.Prime).ne_zero
            (completedEnvelopeOfPresentation_prime_nilpotent s f hf) M q),
          e (q + 1) (genuineCompletedDifferential (s.A : Type u) 𝒟 s.p lam (Fact.out :
              s.p.Prime).ne_zero
              (completedEnvelopeOfPresentation_prime_nilpotent s f hf) M
            nabla q y) = baseCompletedDifferential (s.A : Type u) 𝒟 s.p M nabla q (e q y)) ∧
        (∀ (q : ℕ) (x : baseCompletedTerm (s.A : Type u) 𝒟 s.p M q),
          e q (genuineCompletedComparison (s.A : Type u) 𝒟 s.p lam (Fact.out : s.p.Prime).ne_zero
              (completedEnvelopeOfPresentation_prime_nilpotent s f hf) M q x) =
            s.p • x) ∧
        (∀ y : genuineCompletedTerm (s.A : Type u) 𝒟 s.p lam (Fact.out : s.p.Prime).ne_zero
            (completedEnvelopeOfPresentation_prime_nilpotent s f hf) M 0,
          h 0 (genuineCompletedDifferential (s.A : Type u) 𝒟 s.p lam (Fact.out : s.p.Prime).ne_zero
              (completedEnvelopeOfPresentation_prime_nilpotent s f hf) M nabla 0
            y) = s.p • y - genuineCompletedComparison (s.A : Type u) 𝒟 s.p lam (Fact.out :
                s.p.Prime).ne_zero
                (completedEnvelopeOfPresentation_prime_nilpotent s f hf) M 0
              (e 0 y)) ∧
        (∀ (q : ℕ) (y : genuineCompletedTerm (s.A : Type u) 𝒟 s.p lam (Fact.out : s.p.Prime).ne_zero
            (completedEnvelopeOfPresentation_prime_nilpotent s f hf) M
            (q + 1)),
          genuineCompletedDifferential (s.A : Type u) 𝒟 s.p lam (Fact.out : s.p.Prime).ne_zero
              (completedEnvelopeOfPresentation_prime_nilpotent s f hf) M nabla q
              (h q y) +
            h (q + 1) (genuineCompletedDifferential (s.A : Type u) 𝒟 s.p lam (Fact.out :
                s.p.Prime).ne_zero
                (completedEnvelopeOfPresentation_prime_nilpotent s f hf) M
              nabla (q + 1) y) =
            s.p • y - genuineCompletedComparison (s.A : Type u) 𝒟 s.p lam (Fact.out :
                s.p.Prime).ne_zero
                (completedEnvelopeOfPresentation_prime_nilpotent s f hf) M
              (q + 1) (e (q + 1) y)) ∧
        (∀ (q : ℕ) (x : baseCompletedTerm (s.A : Type u) 𝒟 s.p M (q + 1)),
          h q (genuineCompletedComparison (s.A : Type u) 𝒟 s.p lam (Fact.out : s.p.Prime).ne_zero
              (completedEnvelopeOfPresentation_prime_nilpotent s f hf) M (q + 1)
            x) = 0)
```

## Tag 07Q9, a lemma

[Tag 07Q9](https://stacks.math.columbia.edu/tag/07Q9) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.annihilation07Q9_of_isIteratedAlphaPCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/AlphaPCover07Q9Main.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/AlphaPCover07Q9Main.lean#L114). The attribute's comment: “for an iterated α\_p-cover f : X' → X over S\_0 of constant degree q and a crystal in quasi-coherent modules F on Cris(X/S), with F' = f\_cris^* F, the cone E of Ru\_\{X/S,*}F → f\_* Ru\_\{X'/S,*}F' has all cohomology sheaves annihilated by q”.

> **Stacks Project, Lemma 60.26.3, Tag 07Q9.**  Let `p = T.p` be the prime of the global
> crystalline situation `T`, whose divided power scheme `(S, 𝓘, γ)` lies over `ℤ_(p)`, and assume
> `p ∈ 𝓘` (`hpI`).  Let `f : X' ⟶ X` be an iterated `α_p`-cover (`hf`) of schemes over
> `S₀ = V(𝓘)` — `X'` lies over `S₀` through `f`, which is the situation `overSituation T f` — of
> constant degree `q` (`hq`).  Let `ℱ` be a crystal in quasi-coherent sheaves on `Cris(X/S)` (`hF`)
> and `ℱ' = f_cris^*ℱ` (`crisModuleInverseImage` of `ℱ`).  Then in every distinguished triangle
>
> `Ru_{X/S, *}ℱ ⟶ f_*Ru_{X'/S, *}ℱ' ⟶ E ⟶ Ru_{X/S, *}ℱ[1]`
>
> on the canonical map `moduleComparison07Q9` (in the derived category of abelian sheaves on `X`;
> `f_*` is the derived direct image of the Zariski topoi, which is `f_*` since `f` is a
> homeomorphism), the object `E` has every cohomology sheaf annihilated by `q` (`Annihilation07Q9`).
>
> The hypothesis `p ∈ 𝓘` of the source is stated; the argument only uses that `p` is nilpotent on
> `X`, which every global crystalline situation carries.

```lean
theorem annihilation07Q9_of_isIteratedAlphaPCover
    (hpI : (T.p : Γ(T.S.scheme, ⊤)) ∈ T.S.ideal.obj (op ⊤)) {q : ℕ}
    (hf : IsIteratedAlphaPCover T.p f) (hq : HasConstantDegree f q)
    (F : SheafOfModules.{u} (structureSheaf T)) (hF : IsQuasiCoherentCrystal T F) :
    Annihilation07Q9 T q
      (moduleComparison07Q9 (overSituation T f) T (𝟙 T.S) f (overSituation_compat T f)
        ((moduleULift T).obj F))
```

## Tag 07QA, a lemma

[Tag 07QA](https://stacks.math.columbia.edu/tag/07QA) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.annihilated_ker_coker_crisModuleCohomologyMap_of_isIteratedAlphaPCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrisCohomologyBound07QAMain.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrisCohomologyBound07QAMain.lean#L84). The attribute's comment: “f^* : H^i(Cris(X/S), F) → H^i(Cris(X'/S), F') has kernel and cokernel annihilated by q^(i+1)”.

> Let `p` be a prime and `(S, I, γ)` a divided power scheme over `ℤ_(p)` with `p ∈ I` (the
> prime, the `ℤ_(p)`-structure of the base and the local nilpotence of `p` on `X` are part of the
> situation `T`; `p ∈ I` is `hpI`), `S₀ = V(I)`.  Let `f : X' ⟶ X` be an iterated `α_p`-cover of
> schemes over `S₀` of constant degree `q`, `ℱ` a crystal in quasi-coherent modules on `Cris(X/S)`
> and `ℱ' = f_cris^*ℱ`.  Then the kernel and the cokernel of
>
> `f^* : H^i(Cris(X/S), ℱ) ⟶ H^i(Cris(X'/S), ℱ')`
>
> are annihilated by `q^{i + 1}`: every class killed by `f^*` is killed by `q^{i + 1}`, and
> `q^{i + 1}` times every class of `H^i(Cris(X'/S), ℱ')` lies in the image of `f^*`.

```lean
theorem annihilated_ker_coker_crisModuleCohomologyMap_of_isIteratedAlphaPCover
    (hpI : (T.p : Γ(T.S.scheme, ⊤)) ∈ T.S.ideal.obj (op ⊤)) (q : ℕ)
    (hf : IsIteratedAlphaPCover T.p f) (hq : HasConstantDegree f q)
    (F : SheafOfModules.{u} (structureSheaf T)) (hF : IsQuasiCoherentCrystal T F)
    [HasDerivedCategory.{w} (Sheaf (smallTopology (overSituation T f)) AddCommGrpCat.{u + 1})]
    [HasDerivedCategory.{w} (Sheaf (smallTopology T) AddCommGrpCat.{u + 1})]
    [HasDerivedCategory.{w'} (Sheaf (opensTopology (overSituation T f)) AddCommGrpCat.{u + 1})]
    [HasDerivedCategory.{w'} (Sheaf (opensTopology T) AddCommGrpCat.{u + 1})]
    [HasDerivedCategory.{w'} AddCommGrpCat.{u + 1}] (i : ℕ) :
    (∀ x, crisModuleCohomologyMap (overSituation T f) T (𝟙 T.S) f (overSituation_compat T f)
        ((moduleULift T).obj F) i x = 0 → ((q : ℤ) ^ (i + 1)) • x = 0) ∧
      ∀ y, ∃ x, ((q : ℤ) ^ (i + 1)) • y =
        crisModuleCohomologyMap (overSituation T f) T (𝟙 T.S) f (overSituation_compat T f)
          ((moduleULift T).obj F) i x
```

## Tag 07QB, a lemma

[Tag 07QB](https://stacks.math.columbia.edu/tag/07QB) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.relativeFrobeniusToTwist_isIteratedAlphaPCover_cohomologyBound`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/AlphaPCoverRelativeFrobenius07QB.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/AlphaPCoverRelativeFrobenius07QB.lean#L204). The attribute's comment: “for the global crystalline situation with p in I and X -> S\_0 smooth of relative dimension d: F\_\{X/S\_0} : X -> X^\{(1)} is an iterated alpha\_p-cover of degree p ^ d, and for every crystal in quasi-coherent modules G on Cris(X^\{(1)}/S) and every i the map F\_\{X/S\_0}^* : H^i(Cris(X^\{(1)}/S), G) -> H^i(Cris(X/S), F\_\{X/S\_0,cris}^* G) has kernel and cokernel annihilated by p^\{d(i+1)}”.

> **[Stacks, Lemma 60.26.5, Tag 07QB].**  In the global crystalline situation `X/S` of
> [Stacks, Tag 07MF] with `p` in the divided power ideal `I`, let `S₀ = V(I)`,
> `X^{(1)} = X ×_{S₀, F_{S₀}} S₀` and `F_{X/S₀} : X ⟶ X^{(1)}` the relative Frobenius, and assume
> that `X ⟶ S₀` is smooth of relative dimension `d`.  Then
>
> * `F_{X/S₀}` is an iterated `α_p`-cover of degree `p ^ d`, and
> * for every crystal in quasi-coherent modules `𝒢` on `Cris(X^{(1)}/S)` and every `i`, the map
>   `F_{X/S₀}^* : H^i(Cris(X^{(1)}/S), 𝒢) ⟶ H^i(Cris(X/S), F_{X/S₀, cris}^*𝒢)` has kernel and
>   cokernel annihilated by `p^{d(i + 1)}`.
>
> The first assertion is
> `Crystalline.GlobalCrystallineSituation.isIteratedAlphaPCoverOfDegree_relativeFrobeniusToTwist`.
> The second is [Stacks, Lemma 60.26.4, Tag 07QA]
> (`...SmallSite.annihilated_ker_coker_crisModuleCohomologyMap_of_isIteratedAlphaPCover`) applied to
> `f = F_{X/S₀}` and `q = p ^ d`, whose two hypotheses on `f` are the first assertion, read on `X/S`
> by `zsmul_id_kernel_cokernel_crisModuleCohomologyMap_relativeFrobeniusToTwist_of`.  The map is
> `...SmallSite.crisModuleCohomologyMap` for the morphism `F_{X/S₀}` of situations over the
> identity of `S`, and `F_{X/S₀, cris}^*` is the pullback `...SmallSite.crisModuleInverseImage` of
> `𝒪`-modules; `𝒢` enters through `...SmallSite.moduleULift`, at the module universe of the
> cohomology of `Cris(X^{(1)}/S)`.

```lean
theorem relativeFrobeniusToTwist_isIteratedAlphaPCover_cohomologyBound (d : ℕ)
    [SmoothOfRelativeDimension d T.toClosedFiber] :
    (IsIteratedAlphaPCover T.p (T.relativeFrobeniusToTwist hp) ∧
        HasConstantDegree (T.relativeFrobeniusToTwist hp) (T.p ^ d)) ∧
      ∀ (G : SheafOfModules.{u} (structureSheaf (T.frobeniusTwistSituation hp))),
        IsQuasiCoherentCrystal (T.frobeniusTwistSituation hp) G → ∀ i : ℕ,
          ((T.p : ℤ) ^ (d * (i + 1))) • 𝟙 (kernel (crisModuleCohomologyMap T
              (T.frobeniusTwistSituation hp) (𝟙 T.S) (T.relativeFrobeniusToTwist hp)
              (T.toClosedFiber_comp_closedFiberMap_id hp)
              ((moduleULift (T.frobeniusTwistSituation hp)).obj G) i)) = 0 ∧
            ((T.p : ℤ) ^ (d * (i + 1))) • 𝟙 (cokernel (crisModuleCohomologyMap T
              (T.frobeniusTwistSituation hp) (𝟙 T.S) (T.relativeFrobeniusToTwist hp)
              (T.toClosedFiber_comp_closedFiberMap_id hp)
              ((moduleULift (T.frobeniusTwistSituation hp)).obj G) i)) = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.25, Tag 07PZ](https://stacks.math.columbia.edu/tag/07PZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
