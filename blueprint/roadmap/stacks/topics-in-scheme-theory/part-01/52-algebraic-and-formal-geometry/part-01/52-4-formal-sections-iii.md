---
declaration: section
origin: cited
lean: Stacks.LocalCohomology.exists_pow_linearMaps_sum_eq_self, Stacks.ReesAlgebra.extendLinearMaps, Stacks.ReesAlgebra.extendLinearMaps_degreeOne, Stacks.ReesAlgebra.extendLinearMaps_homogeneous, Stacks.ReesAlgebra.extendLinearMaps_unique, Stacks.ReesAlgebra.aeval_extendLinearMaps_eq, Stacks.ReesAlgebra.exists_unique_extendLinearMaps_module, Stacks.Coherent.existsUnique_gradedSplitting
statement: formalized
proof: formalized
---

# 52.4 Formal sections, III

Section 52.4 of the Stacks Project, [Tag 0EI9](https://stacks.math.columbia.edu/tag/0EI9). 6 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EIA, a lemma

[Tag 0EIA](https://stacks.math.columbia.edu/tag/0EIA) in the Stacks Project.

**`Stacks.LocalCohomology.exists_pow_linearMaps_sum_eq_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/IdealPowerSplitting.lean, line 561](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/IdealPowerSplitting.lean#L561).

> **Stacks Project, Tag 0EIA.** Let `I = (f_1, …, f_r)` be an ideal of a Noetherian ring `A`
> with `cd(A, I) = 1`. Then there are `c ≥ 1` and `A`-linear maps `φ_j : I^c → A` such that
> `∑ f_j φ_j : I^c → I` is the inclusion map.

```lean
theorem exists_pow_linearMaps_sum_eq_self
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (I : Ideal A) {r : ℕ} (f : Fin r → A)
    (hf : I = Ideal.span (Set.range f))
    (hcd : cohomologicalDimension A I (IsNoetherian.noetherian I) = 1) :
    ∃ c : ℕ, 1 ≤ c ∧
      ∃ φ : Fin r → (I ^ c : Ideal A) →ₗ[A] A,
        ∀ x : (I ^ c : Ideal A), (∑ j, f j * φ j x) = (x : A)
```

## Tag 0EIB, a lemma

[Tag 0EIB](https://stacks.math.columbia.edu/tag/0EIB) in the Stacks Project.

**`Stacks.ReesAlgebra.extendLinearMaps`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ReesAlgebra/ExtendLinearMaps.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ReesAlgebra/ExtendLinearMaps.lean#L297). The attribute's comment: “the extended graded algebra map”.

> The graded `A`-algebra map `reesAlgebra J →ₐ[A] A[Xᵢ]` extending a finite family `φ` of
> `A`-linear maps `J →ₗ[A] A`.

```lean
public noncomputable def extendLinearMaps (J : Ideal A) (φ : Fin r → J →ₗ[A] A) :
    reesAlgebra J →ₐ[A] MvPolynomial (Fin r) A
```

**`Stacks.ReesAlgebra.extendLinearMaps_degreeOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ReesAlgebra/ExtendLinearMaps.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ReesAlgebra/ExtendLinearMaps.lean#L303). The attribute's comment: “the degree-one formula”.

> The extension sends an element of `J` in degree one to the linear form `∑ⱼ φ j x · Xⱼ`.

```lean
public theorem extendLinearMaps_degreeOne (J : Ideal A) (φ : Fin r → J →ₗ[A] A) (x : J) :
    extendLinearMaps J φ (degreeOne J x) =
      ∑ j, MvPolynomial.C (φ j x) * MvPolynomial.X j
```

**`Stacks.ReesAlgebra.extendLinearMaps_homogeneous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ReesAlgebra/ExtendLinearMaps.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ReesAlgebra/ExtendLinearMaps.lean#L320). The attribute's comment: “preservation of grading”.

> The extension sends an element of the Rees algebra supported in degree `n` to a homogeneous
> polynomial of total degree `n`.

```lean
public theorem extendLinearMaps_homogeneous (J : Ideal A) (φ : Fin r → J →ₗ[A] A) (n : ℕ)
    (p : reesAlgebra J) (hp : ∀ k : ℕ, k ≠ n → (p : Polynomial A).coeff k = 0) :
    (extendLinearMaps J φ p).IsHomogeneous n
```

**`Stacks.ReesAlgebra.extendLinearMaps_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ReesAlgebra/ExtendLinearMaps.lean, line 351](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ReesAlgebra/ExtendLinearMaps.lean#L351). The attribute's comment: “uniqueness”.

> An algebra map out of the Rees algebra with the prescribed degree-one component is the
> extension.

```lean
public theorem extendLinearMaps_unique (J : Ideal A) (φ : Fin r → J →ₗ[A] A)
    (Ψ : reesAlgebra J →ₐ[A] MvPolynomial (Fin r) A)
    (hΨ : ∀ x : J, Ψ (degreeOne J x) = ∑ j, MvPolynomial.C (φ j x) * MvPolynomial.X j) :
    Ψ = extendLinearMaps J φ
```

**`Stacks.ReesAlgebra.aeval_extendLinearMaps_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ReesAlgebra/ExtendLinearMaps.lean, line 365](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ReesAlgebra/ExtendLinearMaps.lean#L365). The attribute's comment: “the composite is the inclusion”.

> If the maps `φ` split the inclusion of `I ^ c` into `A` against the generators `f` of `I`,
> then evaluating the extension at the `f j` in degree one is the inclusion
> `reesAlgebra (I ^ c) ⊆ A[X]`.
>
> Both sides are algebra maps out of `reesAlgebra (I ^ c)`, so by `reesAlgebra_hom_ext` it is
> enough to compare them in degree one, where the comparison is exactly the splitting identity.

```lean
public theorem aeval_extendLinearMaps_eq (I : Ideal A) (c : ℕ) (f : Fin r → A)
    (hf : ∀ j, f j ∈ I) (φ : Fin r → (I ^ c : Ideal A) →ₗ[A] A)
    (hφ : ∀ x : (I ^ c : Ideal A), (∑ j, f j * φ j x) = (x : A))
    (p : reesAlgebra (I ^ c)) :
    ((MvPolynomial.aeval (fun j ↦ degreeOne I ⟨f j, hf j⟩)
        (extendLinearMaps (I ^ c) φ p) : reesAlgebra I) : Polynomial A) =
      (p : Polynomial A)
```

## Tag 0EIC, a lemma

[Tag 0EIC](https://stacks.math.columbia.edu/tag/0EIC) in the Stacks Project.

**`Stacks.ReesAlgebra.exists_unique_extendLinearMaps_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ReesAlgebra/ExtendToModule.lean, line 826](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ReesAlgebra/ExtendToModule.lean#L826).

> The degreewise graded map extending the maps on a power of `I`.

```lean
public theorem exists_unique_extendLinearMaps_module
    (A : Type u) (B : Type v) (N : Type w)
    [CommRing A]
    [CommRing B] [Algebra A B] [IsNoetherianRing B]
    [AddCommGroup N] [Module B N] [Module.Finite B N]
    (I : Ideal A) {r : ℕ} (f : Fin r → A)
    (hf : I = Ideal.span (Set.range f))
    (c : ℕ) (_hc : 1 ≤ c)
    (φ : Fin r → (I ^ c : Ideal A) →ₗ[A] A)
    (hφ : ∀ g : (I ^ c : Ideal A), (∑ j, f j * φ j g) = (g : A)) :
    ∃ c' : ℕ, ∃ hc' : c ≤ c',
      ∃ φ' : Fin r → (I ^ c' : Ideal A) →ₗ[A] A,
        (∀ j (g : A) (hg : g ∈ I ^ c'),
          φ' j ⟨g, hg⟩ = φ j ⟨g, Ideal.pow_le_pow_right hc' hg⟩) ∧
        (∀ g : (I ^ c' : Ideal A), (∑ j, f j * φ' j g) = (g : A)) ∧
        ∃! Ψ : ∀ n : ℕ, reesModulePiece (B := B) (N := N) I c' n →ₗ[B] moduleMvPolynomial r N,
          (∀ n (y : reesModulePiece (B := B) (N := N) I c' n) (m : Fin r →₀ ℕ),
            (m.sum fun _ e => e) ≠ n → (Ψ n y) m = 0) ∧
          (∀ n (p : reesAlgebra (I ^ c'))
              (_hp : ∀ k : ℕ, k ≠ n → (p : Polynomial A).coeff k = 0)
              (x : N)
              (hx : (algebraMap A B ((p : Polynomial A).coeff n)) • x ∈
                reesModulePiece (B := B) (N := N) I c' n)
              (m : Fin r →₀ ℕ),
            (Ψ n ⟨(algebraMap A B ((p : Polynomial A).coeff n)) • x, hx⟩) m =
              (algebraMap A B
                ((Stacks.ReesAlgebra.extendLinearMaps (I ^ c') φ' p).coeff m)) • x) ∧
          (∀ n (y : reesModulePiece (B := B) (N := N) I c' n),
            ∑ m ∈ (Ψ n y).support,
              (∏ j, (algebraMap A B (f j)) ^ m j) • (Ψ n y) m = (y : N))
```

## Tag 0EH6, a lemma

[Tag 0EH6](https://stacks.math.columbia.edu/tag/0EH6) in the Stacks Project.

**`Stacks.Coherent.existsUnique_gradedSplitting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/GradedSplittingCharts.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/GradedSplittingCharts.lean#L264).

> **Stacks Project, Tag 0EH6.** Let `I = (f₁, …, f_r)` be an ideal of a Noetherian ring `A`
> with `cd(A, I) = 1`, let `φ_j : I ^ c ⟶ A` split the inclusion against the generators, let `X`
> be a Noetherian scheme over `Spec A` and let `(F_n)` be a coherent adic system along `I · 𝒪_X`
> with inverse limit `F`. Then `c` may be enlarged to a `d`, with a splitting `ψ_j : I ^ d ⟶ A`
> restricting `φ` and still splitting the inclusion, so that there is a *unique* graded
> `𝒪_X`-module map
>
> `Φ_F : ⨁_{n ≥ 0} I ^ (n d) F ⟶ F[T₁, …, T_r]`
>
> with `Φ_F (g s) = Φ(g) s` for `g ∈ I ^ (n d)` and `s` a local section of `F`, and the composite
> of `Φ_F` with the substitution `T_j ↦ f_j` is the inclusion `I ^ (n d) F ⟶ F` in every
> degree.

```lean
public theorem existsUnique_gradedSplitting (A : Type u) [CommRing A] [IsNoetherianRing A]
    (J : Ideal A) {r : ℕ} (f : Fin r → A) (hf : J = Ideal.span (Set.range f))
    (hcd : Stacks.LocalCohomology.cohomologicalDimension A J (IsNoetherian.noetherian J) = 1)
    {c : ℕ} (hc : 1 ≤ c) (φ : Fin r → (J ^ c : Ideal A) →ₗ[A] A)
    (hφ : ∀ x : (J ^ c : Ideal A), (∑ j, f j * φ j x) = (x : A))
    (fX : X ⟶ Spec (.of A)) [AlgebraicGeometry.IsNoetherian X]
    (S : ℕᵒᵖ ⥤ X.Modules) (hS : IsCoherentAdicSystem (baseIdealSheaf A J fX) S) :
    ∃ d : ℕ, ∃ hcd' : c ≤ d, ∃ ψ : Fin r → (J ^ d : Ideal A) →ₗ[A] A,
      RestrictsSplitting J hcd' φ ψ ∧
      (∀ x : (J ^ d : Ideal A), (∑ j, f j * ψ j x) = (x : A)) ∧
      ∃! Ψ : GradedSplittingComponents A J fX (limit S) r d,
        IsGradedSplitting A J fX (limit S) d ψ Ψ ∧
          ∀ n : ℕ, gradedSplittingEvalHom Ψ f n =
            ιModules (idealPowerMultiple (baseIdealSheaf A J fX) (n * d) (limit S))
```

## Tag 0EH7, a lemma

[Tag 0EH7](https://stacks.math.columbia.edu/tag/0EH7) in the Stacks Project.

**`Stacks.Algebraization.AdicInverseSystem.limitIntCohomologyTopology_eq_adicModuleTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicInverseSystem/LimitTopologyIsAdic.lean, line 640](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicInverseSystem/LimitTopologyIsAdic.lean#L640).

> **Stacks Project, Tag 0EH7.** Let `I` be an ideal of a Noetherian ring `A`, let `X` be a
> Noetherian scheme over `Spec A` and let `… ⟶ F_3 ⟶ F_2 ⟶ F_1` be an inverse system of coherent
> `𝒪_X`-modules with `F_n = F_{n+1} / I ^ n F_{n+1}`. If `cd(A, I) = 1` then for every `p ∈ ℤ` the
> limit topology on `lim_n H^p(X, F_n)` — the infimum of the topologies induced from the discrete
> modules `H^p(X, F_n)` — is the `I`-adic topology.
>
> Cohomology is `moduleCohomologyFunctorInt X p`, the `p`-th right derived functor of global
> sections taken in `Γ(X, 𝒪_X)`-modules, so that `lim_n H^p(X, F_n)` carries the module structure
> the `I`-adic topology needs, and `I` acts through the ideal of `Γ(X, 𝒪_X)` generated by its
> image. The system is zero-indexed, so its object at `n` is the source's `F_{n+1}` and the
> source's exponent `n` appears as `n + 1`; quasi-coherence of the terms is a field of
> `Stacks.Algebraization.AdicInverseSystem` rather than a hypothesis here, and it follows from the
> coherence `hcoh` the source assumes.

```lean
public theorem limitIntCohomologyTopology_eq_adicModuleTopology [IsNoetherianRing A] (I : Ideal A)
    (S : AdicInverseSystem.{u}) [AlgebraicGeometry.IsNoetherian S.X]
    (fX : S.X ⟶ Spec (.of A))
    (hSI : S.I = baseIdealSheaf A I fX)
    (hcoh : ∀ n : ℕ, _root_.SheafOfModules.IsCoherent.{u} (S.system.obj (op n)))
    (hcd : Stacks.LocalCohomology.cohomologicalDimension A I (IsNoetherian.noetherian I) = 1)
    (p : ℤ) :
    (⨅ n : ℕ, TopologicalSpace.induced
        (fun x : AdicInverseSystem.cohomologyLimit S (moduleCohomologyFunctorInt S.X p) =>
          (limit.π (AdicInverseSystem.cohomologySystem S
            (moduleCohomologyFunctorInt S.X p)) (op n)).hom x) ⊥) =
      (I.map (fX.appTop.hom.comp (Scheme.ΓSpecIso (.of A)).inv.hom)).adicModuleTopology
        (AdicInverseSystem.cohomologyLimit S (moduleCohomologyFunctorInt S.X p))
```

## Tag 0EH8, an example

[Tag 0EH8](https://stacks.math.columbia.edu/tag/0EH8) in the Stacks Project.

**`Stacks.Examples.NonAdicLimit.truncationEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/NonAdicLimitChart.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/NonAdicLimitChart.lean#L158). The attribute's comment: “A/I^n is the polynomial chart k[x,y][s,t]/((xs - yt) + (s,t)^n): the truncation that makes the chart isomorphism true, where its untruncated form A[1/x] = k[x^\{±1},y][[t]] is false”.

> **The truncation of `A`, Stacks 0EH8.** `A ⧸ Iⁿ` is the *polynomial* chart
> `k[x,y][s,t] ⧸ ((xs − yt) + (s,t)ⁿ)`: modulo `Iⁿ = (s,t)ⁿ` only the coefficients in total degree
> below `n` survive, so no power series does.
>
> This is the step whose untruncated form is false. `A[1/x]` is a *proper* subring of
> `k[x^{±1}, y][[t]]`, because the pole order in `x` of the image of `a/xᵐ` grows with the degree
> in `t` while `m` does not — see the docstring of
> `Stacks.Examples.NonAdicLimit.not_isUnit_mul_add_mul`. Modulo `Iⁿ` the degrees in `t` are
> bounded, and what remains is a polynomial ring, which does commute with localization.

```lean
def truncationEquiv (n : ℕ) :
    (ambientPoly k ⧸
        chartIdeal (MvPolynomial.X 0 : MvPolynomial (Fin 2) k) (MvPolynomial.X 1) n) ≃+*
      (exampleRing k ⧸ adicIdeal k ^ n)
```

**`Stacks.Examples.NonAdicLimit.chartTruncationEquivX`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/NonAdicLimitChart.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/NonAdicLimitChart.lean#L300). The attribute's comment: “the truncated chart isomorphism A[1/x]/I^n = k[x^\{±1},y][t]/(t^n), sending s to (y/x)t; the chart the omitted computation of H^0(X, F\_n) needs, and whose untruncated form is false”.

> **The truncated chart isomorphism of Stacks 0EH8, on `D(x)`.**
>
> `A[1/x] ⧸ Iⁿ ≃+* k[x^{±1}, y][t] ⧸ (tⁿ)`, the `D(x)`-chart of `𝒪_X/Iⁿ𝒪_X` that the source's
> "computation omitted" rests on. It sends `s ↦ (y/x)t`, hence `I = (s,t) ↦ (t)` and
> `g = t/x ↦ x⁻¹t`.
>
> Its *untruncated* form `A[1/x] ≅ k[x^{±1}, y][[t]]` is **false** — see the docstring of
> `Stacks.Examples.NonAdicLimit.not_isUnit_mul_add_mul`. The truncation is what makes it true, and
> the proof shows why: `A ⧸ Iⁿ` is a *polynomial* ring
> (`Stacks.Examples.NonAdicLimit.truncationEquiv`), a polynomial ring does commute with
> localization (`MvPolynomial.isLocalization`), and then `x` being a unit the change of variables
> `s ↦ (y/x)t` eliminates `s` (`Stacks.TruncatedChart.chartEquiv`). The middle step is the one that
> has no untruncated analogue.
>
> The `D(y)` twin is `Stacks.Examples.NonAdicLimit.chartTruncationEquivY`.

```lean
def chartTruncationEquivX (n : ℕ) :
    (Localization.Away (coordX k) ⧸
        (adicIdeal k ^ n).map
          (algebraMap (exampleRing k) (Localization.Away (coordX k)))) ≃+*
      truncPoly (coeffAwayX k) n
```

**`Stacks.Examples.NonAdicLimit.chartTruncationEquivY`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/NonAdicLimitChart.lean, line 351](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/NonAdicLimitChart.lean#L351). The attribute's comment: “the truncated chart isomorphism A[1/y]/I^n = k[x,y^\{±1}][s]/(s^n), sending t to (x/y)s; the D(y) twin of the chart the omitted computation of H^0(X, F\_n) needs, and whose untruncated form is likewise false”.

> **The truncated chart isomorphism of Stacks 0EH8, on `D(y)`.**
>
> `A[1/y] ⧸ Iⁿ ≃+* k[x, y^{±1}][s] ⧸ (sⁿ)`, the twin of
> `Stacks.Examples.NonAdicLimit.chartTruncationEquivX` and the second of the two charts the
> source's "computation omitted" rests on. It sends `t ↦ (x/y)s`, hence `I = (s,t) ↦ (s)` and
> `g = t/x ↦ y⁻¹s`.
>
> The proof is the `D(x)` proof with the two variables interchanged, and only the last of its three
> steps is asymmetric. Steps 1 and 2 — `A ⧸ Iⁿ` is the polynomial chart
> `k[x,y][s,t] ⧸ ((xs − yt) + (s,t)ⁿ)` (`Stacks.Examples.NonAdicLimit.truncationEquiv`), and a
> polynomial chart commutes with localization (`MvPolynomial.isLocalization`,
> `Stacks.Examples.NonAdicLimit.map_chartIdeal`) — do not mention which variable is inverted. Step
> 3 does: `Stacks.TruncatedChart.chartEquiv` eliminates the *first* variable and wants the
> coefficient of `s` to be a unit, so here it is used through
> `Stacks.TruncatedChart.chartEquivSwap`, which runs it after `MvPolynomial.rename (Equiv.swap 0 1)`
> and eliminates `t` instead.
>
> As for `D(x)`, the untruncated form `A[1/y] ≅ k[x, y^{±1}][[s]]` is **false**: the pole-order
> argument in the docstring of `Stacks.Examples.NonAdicLimit.not_isUnit_mul_add_mul` is symmetric
> in the two variables.

```lean
def chartTruncationEquivY (n : ℕ) :
    (Localization.Away (coordY k) ⧸
        (adicIdeal k ^ n).map
          (algebraMap (exampleRing k) (Localization.Away (coordY k)))) ≃+*
      truncPoly (coeffAwayY k) n
```

**`Stacks.Examples.NonAdicLimit.notMemAdicIdealSmulFormalLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/NonAdicLimitNotAdic.lean, line 580](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/NonAdicLimitNotAdic.lean#L580). The attribute's comment: “g^e is never in I*M, so the limit topology on M differs from the I-adic one and the cd = 1 hypothesis of Stacks 0EH7 is sharp”.

> **`gᵉ ∉ I·M`, the last clause of Stacks 0EH8.** Each power of the rational function
> `g = t/x = s/y` is a formal section tending to zero in the limit topology on
> `M = lim H⁰(X, 𝒪_X/Iⁿ𝒪_X)`, and none of them lies in `I·M`. The limit topology is therefore
> not the `I`-adic topology, which is what makes the example sharp against Stacks 0EH7.
>
> The whole situation is specialized along `ρ : A ⟶ R[x,y]`, `x ↦ x`, `y ↦ y`, `s ↦ y·z`,
> `t ↦ x·z` with `R = k[T]/(Tᵉ⁺¹)` and `z` the image of `T`. Since `ρ(𝔞) ⊆ (x,y)`, the punctured
> plane `W = D(x) ∪ D(y) ⊆ Spec R[x,y]` maps to `X`; since `ρ(I)ᵉ⁺¹ = 0`, that map factors
> through `ℱₑ₊₁`; and since `Γ(W, 𝒪) = R[x,y]` — the punctured plane acquires no new function,
> which is where the codimension two of the removed locus enters — every formal section acquires
> a value in `R[x,y]` (`exists_specializationFunctional`). On `gᵉ` the value is `zᵉ`, whereas a
> decomposition `gᵉ = s·p + t·q` makes it `y z·(…) + x z·(…)`, which vanishes at `x = y = 0`
> while `zᵉ ≠ 0`.

```lean
theorem notMemAdicIdealSmulFormalLimit (e : ℕ) : NotMemAdicIdealSmulFormalLimit k e
```

**`Stacks.Examples.NonAdicLimit.notMem_or_notMem_of_adicIdeal_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/NonAdicLimitTopology.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/NonAdicLimitTopology.lean#L237). The attribute's comment: “the open neighbourhood V of V(I·O\_X) in X on which t/x = s/y is regular is D(x) ∪ D(y)”.

> **The neighbourhood `V` of Stacks 0EH8.** At every point of `X = Spec(A) ∖ V(𝔞)` at which
> `I` vanishes, one of `x`, `y` is invertible: `V(I𝒪_X) ⊆ D(x) ∪ D(y)`. So `D(x) ∪ D(y)` is the
> open neighbourhood of `V(I𝒪_X)` inside `X` on which the rational function `g = t/x = s/y`
> below is regular.

```lean
theorem notMem_or_notMem_of_adicIdeal_le (p : PrimeSpectrum (exampleRing k))
    (hp : ¬ puncturingIdeal k ≤ p.asIdeal) (hI : adicIdeal k ≤ p.asIdeal) :
    coordX k ∉ p.asIdeal ∨ coordY k ∉ p.asIdeal
```

**`Stacks.Examples.NonAdicLimit.coordX_mul_rationalFunctionAwayX`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/NonAdicLimitTopology.lean, line 266](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/NonAdicLimitTopology.lean#L266). The attribute's comment: “the chart t/x of the rational function g, regular on D(x)”.

> **`g = t/x` on `D(x)`.**

```lean
theorem coordX_mul_rationalFunctionAwayX :
    algebraMap (exampleRing k) (Localization.Away (coordX k)) (coordX k) *
        rationalFunctionAwayX k =
      algebraMap (exampleRing k) (Localization.Away (coordX k)) (coordT k)
```

**`Stacks.Examples.NonAdicLimit.coordY_mul_rationalFunctionAwayY`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/NonAdicLimitTopology.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/NonAdicLimitTopology.lean#L274). The attribute's comment: “the chart s/y of the rational function g, regular on D(y)”.

> **`g = s/y` on `D(y)`.**

```lean
theorem coordY_mul_rationalFunctionAwayY :
    algebraMap (exampleRing k) (Localization.Away (coordY k)) (coordY k) *
        rationalFunctionAwayY k =
      algebraMap (exampleRing k) (Localization.Away (coordY k)) (coordS k)
```

**`Stacks.Examples.NonAdicLimit.rationalFunctionAway_eq_of_isUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/NonAdicLimitTopology.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/NonAdicLimitTopology.lean#L284). The attribute's comment: “t/x = s/y: the two charts agree wherever x and y are both invertible”.

> **The two charts are the same rational function.** In any `A`-algebra in which `x` and `y`
> are both invertible, an element solving `x·gx = t` and an element solving `y·gy = s` are
> equal: `t/x = s/y`.

```lean
theorem rationalFunctionAway_eq_of_isUnit {R : Type*} [CommRing R] [Algebra (exampleRing k) R]
    (hx : IsUnit (algebraMap (exampleRing k) R (coordX k)))
    (hy : IsUnit (algebraMap (exampleRing k) R (coordY k)))
    (gx gy : R)
    (hgx : algebraMap (exampleRing k) R (coordX k) * gx =
      algebraMap (exampleRing k) R (coordT k))
    (hgy : algebraMap (exampleRing k) R (coordY k) * gy =
      algebraMap (exampleRing k) R (coordS k)) :
    gx = gy
```

**`Stacks.Examples.NonAdicLimit.pow_rationalFunctionAwayX_mem_map_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/NonAdicLimitTopology.lean, line 316](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/NonAdicLimitTopology.lean#L316). The attribute's comment: “g^e dies modulo I^n for n ≤ e, on the chart D(x)”.

> **`gᵉ → 0`, on the chart `D(x)`.** The `e`-th power of `t/x` lies in `Iⁿ·A[1/x]` for every
> `n ≤ e`, because `tᵉ ∈ Iⁿ`.

```lean
theorem pow_rationalFunctionAwayX_mem_map_pow (e n : ℕ) (hne : n ≤ e) :
    rationalFunctionAwayX k ^ e ∈
      (adicIdeal k ^ n).map (algebraMap (exampleRing k) (Localization.Away (coordX k)))
```

**`Stacks.Examples.NonAdicLimit.pow_rationalFunctionAwayY_mem_map_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/NonAdicLimitTopology.lean, line 324](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/NonAdicLimitTopology.lean#L324). The attribute's comment: “g^e dies modulo I^n for n ≤ e, on the chart D(y)”.

> **`gᵉ → 0`, on the chart `D(y)`.** The `e`-th power of `s/y` lies in `Iⁿ·A[1/y]` for every
> `n ≤ e`, because `sᵉ ∈ Iⁿ`.

```lean
theorem pow_rationalFunctionAwayY_mem_map_pow (e n : ℕ) (hne : n ≤ e) :
    rationalFunctionAwayY k ^ e ∈
      (adicIdeal k ^ n).map (algebraMap (exampleRing k) (Localization.Away (coordY k)))
```

**`Stacks.Examples.NonAdicLimit.cohomologicalDimension_adicIdeal_eq_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/NonAdicLimitTopology.lean, line 456](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/NonAdicLimitTopology.lean#L456). The attribute's comment: “cd(A, I) = 2, so the cd = 1 hypothesis of Stacks 0EH7 is sharp”.

> **`cd(A, I) = 2`.** The ideal `I = (s,t)` of `A = k[x,y][[s,t]]/(xs - yt)` has
> cohomological dimension two: at most two because `I` has two generators (Stacks 0DX9), and at
> least two because specializing `x, y ↦ 0` carries `I` onto the maximal ideal of `k[[s]][[t]]`,
> whose cohomological dimension is its Krull dimension (Stacks 0DXE), and that is at least two.
>
> This is why Stacks 0EH7 — which concludes that the limit topology on `lim Hᵖ(X, ℱₙ)` is
> `I`-adic — does not apply: that result needs `cd(A, I) = 1`.

```lean
theorem cohomologicalDimension_adicIdeal_eq_two :
    cohomologicalDimension (exampleRing k) (adicIdeal k) (adicIdeal_fg k) = 2
```

**`Stacks.Examples.NonAdicLimit.sectionG`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/NonAdicLimitTopology.lean, line 726](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/NonAdicLimitTopology.lean#L726). The attribute's comment: “the section g”.

> **`g` as a genuine section of `𝒪_X` over `V = D(x) ∪ D(y)`.** The rational function
> `g = t/x = s/y` of Stacks 0EH8 is regular on the neighbourhood `V` of `V(I𝒪_X)`: it is glued
> from `sectionX` and `sectionY`, which agree on the overlap by `res_sectionX_eq_res_sectionY`,
> via the sheaf condition for two opens.

```lean
noncomputable def sectionG :
    (puncturedSpectrum k).presheaf.obj (Opposite.op (nearVanishingOpen k).openSet)
```

**`Stacks.Examples.NonAdicLimit.formalSectionG`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/NonAdicLimitTopology.lean, line 931](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/NonAdicLimitTopology.lean#L931). The attribute's comment: “each power g^e gives an element of M = lim H⁰(X, ℱₙ)”.

> **`gᵉ` as a formal section, Stacks 0EH8's element of `M = lim H⁰(X, 𝒪_X/IⁿM)`.** The
> image of `sectionGFormal k e` under the canonical comparison `comparisonAt` at the
> neighbourhood `nearVanishingOpen k`.

```lean
noncomputable def formalSectionG (e : ℕ) :
    ToType (limit (formalSections (exampleRing k) (adicIdeal k) (puncturingIdeal k)
      (formalModule k)))
```

**`Stacks.Examples.NonAdicLimit.tendsto_formalSectionG_atTop_nhds_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/NonAdicLimitTopology.lean, line 993](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/NonAdicLimitTopology.lean#L993). The attribute's comment: “g^e → 0 as e → ∞ in the limit topology on M”.

> **`gᵉ → 0` in the limit topology, Stacks 0EH8.** For each `n`, `gᵉ` already dies in the
> tower's `n`-th term as soon as `e ≥ n`, by `sectionG_pow_mem_idealPowerMultiple`.

```lean
theorem tendsto_formalSectionG_atTop_nhds_zero :
    Filter.Tendsto (fun e => formalSectionG k e) Filter.atTop
      (@nhds _ (limitTopologyFormalLimitModule k) 0)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.4, Tag 0EI9](https://stacks.math.columbia.edu/tag/0EI9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
