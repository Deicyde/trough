---
declaration: section
origin: cited
lean: Rig.IsRigSmooth, Rig.isRigSmooth_iff_cotangentCohomologyCondition, Rig.isRigSmooth_iff_cotangentFactorization, Rig.isRigSmooth_iff_hasJacobianCover, Rig.isElementPowerTorsion_hneg_of_jacobianChart, Rig.free_localized_hzero_of_jacobianChart, Rig.isRigSmooth_adicCompletionObj_of_smoothAwayFrom, Rig.exists_sub_one_mem_and_smoothAwayFrom_of_isRigSmooth
statement: formalized
proof: formalized
---

# 88.4 Rig-smooth algebras

Section 88.4 of the Stacks Project, [Tag 0GAH](https://stacks.math.columbia.edu/tag/0GAH). 5 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GAI, a definition

[Tag 0GAI](https://stacks.math.columbia.edu/tag/0GAI) in the Stacks Project.

**`Rig.IsRigSmooth`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigSmoothDefs.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/RigSmoothDefs.lean#L60).

> **Stacks Project, Tag 0GAI.** Rig-smoothness of an adically finite type `A`-algebra over
> `(A, I)`: some uniform power of `I` annihilates `Ext¹` from its completed naive cotangent
> complex to every `B`-module.

```lean
public def IsRigSmooth (B : AdicFiniteTypeAlgebra.{u, v} A I) : Prop
```

## Tag 0GAJ, a lemma

[Tag 0GAJ](https://stacks.math.columbia.edu/tag/0GAJ) in the Stacks Project.

**`Rig.isRigSmooth_iff_cotangentCohomologyCondition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Restricted/RigSmoothCriteria/Equivalences.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Restricted/RigSmoothCriteria/Equivalences.lean#L377). The attribute's comment: “conditions (1) and (2)”.

> Rig-smoothness is equivalent to the cohomological criterion for the completed naive
> cotangent complex.

```lean
public theorem isRigSmooth_iff_cotangentCohomologyCondition
    {A : Type u} [CommRing A] [IsNoetherianRing A] {I : Ideal A}
    (B : AdicFiniteTypeAlgebra.{u, v} A I) (P : CompletedPolynomialPresentation I B) :
    Rig.IsRigSmooth B ↔ HasCotangentCohomologyCondition B P
```

**`Rig.isRigSmooth_iff_cotangentFactorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Restricted/RigSmoothCriteria/Equivalences.lean, line 403](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Restricted/RigSmoothCriteria/Equivalences.lean#L403). The attribute's comment: “conditions (1) and (3)”.

> Rig-smoothness is equivalent to uniform factorization of powers of the ideal of
> definition through the differential of a chosen completed naive cotangent complex.

```lean
public theorem isRigSmooth_iff_cotangentFactorization
    {A : Type u} [CommRing A] [IsNoetherianRing A] {I : Ideal A}
    (B : AdicFiniteTypeAlgebra.{u, v} A I) (P : CompletedPolynomialPresentation I B) :
    Rig.IsRigSmooth B ↔ HasCotangentFactorization B P
```

**`Rig.isRigSmooth_iff_hasJacobianCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Restricted/RigSmoothCriteria/Equivalences.lean, line 459](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Restricted/RigSmoothCriteria/Equivalences.lean#L459). The attribute's comment: “conditions (1) and (4)”.

> Rig-smoothness is equivalent to a finite Jacobian cover away from the ideal of
> definition.

```lean
public theorem isRigSmooth_iff_hasJacobianCover
    {A : Type u} [CommRing A] [IsNoetherianRing A] {I : Ideal A}
    (B : AdicFiniteTypeAlgebra.{u, v} A I) (P : CompletedPolynomialPresentation I B) :
    Rig.IsRigSmooth B ↔ HasJacobianCover B P
```

**`Rig.isElementPowerTorsion_hneg_of_jacobianChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Restricted/RigSmoothCriteria/Equivalences.lean, line 527](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Restricted/RigSmoothCriteria/Equivalences.lean#L527). The attribute's comment: “the proof of (4) ⟹ (2): H⁻¹(NL^∧) is b_l-power torsion”.

> **Stacks 0GAJ, inside the proof of (4) ⟹ (2).**  Let `b` carry a Jacobian chart: a
> subset `T` of `m` of the variables and `m` elements `f₁, …, fₘ` of the presentation ideal `J`
> whose Jacobian minor along `T` divides `b`, with `b J ⊆ (f₁, …, fₘ) + J²`.  Then
> `H⁻¹(NL^∧_{B/A})` is `b`-power torsion; in fact `b²` already annihilates it.

```lean
public theorem isElementPowerTorsion_hneg_of_jacobianChart
    {A : Type u} [CommRing A] [IsNoetherianRing A] {I : Ideal A}
    (B : AdicFiniteTypeAlgebra.{u, v} A I)
    (P : CompletedPolynomialPresentation I B) (b : P.completedPolynomialRing)
    {m : ℕ} (T : Fin m ↪ Fin P.variableCount) (f : Fin m → P.ker)
    (hdet : P.toAlgHom
      (Matrix.det fun i j : Fin m ↦
        (completedNaiveCotangentComplex B P).partialDeriv (T i) (f j : P.completedPolynomialRing)) ∣
        P.toAlgHom b)
    (hrelations : ∀ x : P.completedPolynomialRing, x ∈ P.ker →
      b * x ∈ Ideal.span (Set.range fun j : Fin m ↦ (f j : P.completedPolynomialRing)) +
        P.ker ^ 2) :
    IsElementPowerTorsion B.carrier (completedNaiveCotangentComplex B P).Hneg
      (P.toAlgHom b)
```

**`Rig.free_localized_hzero_of_jacobianChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Restricted/RigSmoothCriteria/JacobianChartPointwise.lean, line 411](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Restricted/RigSmoothCriteria/JacobianChartPointwise.lean#L411). The attribute's comment: “the proof of (4) ⟹ (2): H⁰(NL^∧) is finite free after inverting b_l”.

> **Stacks 0GAJ, inside the proof of (4) ⟹ (2).**  Let `b` carry a Jacobian chart: a subset
> `T` of `m` of the variables and `m` elements `f₁, …, fₘ` of the presentation ideal `J` whose
> Jacobian minor along `T` divides `b`, with `b J ⊆ (f₁, …, fₘ) + J²`.  Then `H⁰(NL^∧_{B/A})`
> becomes finite free after inverting `b`.

```lean
public theorem free_localized_hzero_of_jacobianChart
    {A : Type u} [CommRing A] [IsNoetherianRing A] {I : Ideal A}
    (B : AdicFiniteTypeAlgebra.{u, v} A I)
    (P : CompletedPolynomialPresentation I B) (b : P.completedPolynomialRing)
    {m : ℕ} (T : Fin m ↪ Fin P.variableCount) (f : Fin m → P.ker)
    (hdet : P.toAlgHom
      (Matrix.det fun i j : Fin m ↦
        (completedNaiveCotangentComplex B P).partialDeriv (T i) (f j : P.completedPolynomialRing)) ∣
        P.toAlgHom b)
    (hrelations : ∀ x : P.completedPolynomialRing, x ∈ P.ker →
      b * x ∈ Ideal.span (Set.range fun j : Fin m ↦ (f j : P.completedPolynomialRing)) +
        P.ker ^ 2) :
    Module.Free (Localization.Away (P.toAlgHom b))
        (LocalizedModule (Submonoid.powers (P.toAlgHom b))
          (completedNaiveCotangentComplex B P).Hzero) ∧
      Module.Finite (Localization.Away (P.toAlgHom b))
        (LocalizedModule (Submonoid.powers (P.toAlgHom b))
          (completedNaiveCotangentComplex B P).Hzero)
```

## Tag 0GAK, a lemma

[Tag 0GAK](https://stacks.math.columbia.edu/tag/0GAK) in the Stacks Project.

**`Rig.isRigSmooth_adicCompletionObj_of_smoothAwayFrom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Restricted/RigSmoothSmoothLocus.lean, line 705](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Restricted/RigSmoothSmoothLocus.lean#L705). The attribute's comment: “part (1)”.

> **Stacks 0GAK (1).** If `Spec(B) → Spec(A)` is smooth over `Spec(A) ∖ V(I)`, then the
> `I`-adic completion `B^` is rig-smooth over `(A, I)`.

```lean
public theorem isRigSmooth_adicCompletionObj_of_smoothAwayFrom (h : SmoothAwayFrom A I B) :
    IsRigSmooth (adicCompletionObj I (B := B))
```

**`Rig.exists_sub_one_mem_and_smoothAwayFrom_of_isRigSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Restricted/RigSmoothSmoothLocus.lean, line 747](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Restricted/RigSmoothSmoothLocus.lean#L747). The attribute's comment: “part (2)”.

> **Stacks 0GAK (2).** If the `I`-adic completion `B^` is rig-smooth over `(A, I)`, then there
> is `g ∈ 1 + IB` such that `Spec(B_g) → Spec(A)` is smooth over `Spec(A) ∖ V(I)`.

```lean
public theorem exists_sub_one_mem_and_smoothAwayFrom_of_isRigSmooth
    (h : IsRigSmooth (adicCompletionObj I (B := B))) :
    ∃ g : B, g - 1 ∈ I.map (algebraMap A B) ∧ SmoothAwayFrom A I (Localization.Away g)
```

## Tag 0GAL, a lemma

[Tag 0GAL](https://stacks.math.columbia.edu/tag/0GAL) in the Stacks Project.

**`Rig.smul_ext_one_completedBaseChangeOfIsNoetherianRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/NaiveCotangent/BaseChangeExt.lean, line 556](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/NaiveCotangent/BaseChangeExt.lean#L556).

> **Stacks Project, Tag 0GAL.**  Let `(A₁, I₁) → (A₂, I₂)` be as in Stacks Remark 0AL5 — a
> ring map `A₁ → A₂` of Noetherian rings with ideals `I₁ ⊆ A₁`, `I₂ ⊆ A₂` such that `I₁ ^ c`
> maps into `I₂` for some `c ≥ 1` — let `B₁` be adically of finite type over `(A₁, I₁)` (Stacks
> 0AL4), let `B₂ = (B₁ ⊗_{A₁} A₂)^∧` be its base change, the value at `B₁` of the completed
> base-change functor `Rig.completedBaseChangeOfIsNoetherianRing` of Remark 0AL5, and let
> `f₂ ∈ B₂` be the image of `f₁ ∈ B₁`, that is of `f₁ ⊗ 1` (`Rig.CompletedBaseChange.scalar`).
> If `f₁` annihilates `Ext¹_{B₁}(NL^∧_{B₁/A₁}, N₁)` for
> every `B₁`-module `N₁`, then `f₂` annihilates `Ext¹_{B₂}(NL^∧_{B₂/A₂}, N₂)` for every
> `B₂`-module `N₂`.
>
> The completed cotangent complexes are computed from arbitrary completed polynomial
> presentations `P₁` and `P₂`, on which they do not depend (Stacks 0GAE).

```lean
public theorem smul_ext_one_completedBaseChangeOfIsNoetherianRing
    (hpow : ∃ c : ℕ, 0 < c ∧ (I₁ ^ c).map (algebraMap A₁ A₂) ≤ I₂)
    (B₁ : AdicFiniteTypeAlgebra.{u₁, v} A₁ I₁)
    (P₁ : CompletedPolynomialPresentation I₁ B₁)
    (P₂ : CompletedPolynomialPresentation I₂
      ((completedBaseChangeOfIsNoetherianRing hpow).functor.obj B₁))
    (f₁ : B₁.carrier)
    (h : ∀ (N : ModuleCat.{max u₁ v} B₁.carrier)
      (ξ : DerivedCategory.Ext (derivedCompletedNaiveCotangentComplex B₁ P₁)
        ((DerivedCategory.singleFunctor (ModuleCat.{max u₁ v} B₁.carrier) 0).obj N) 1),
      f₁ • ξ = 0) :
    ∀ (N : ModuleCat.{max u₂ v}
        ((completedBaseChangeOfIsNoetherianRing hpow).functor.obj B₁).carrier)
      (ξ : DerivedCategory.Ext
        (derivedCompletedNaiveCotangentComplex
          ((completedBaseChangeOfIsNoetherianRing hpow).functor.obj B₁) P₂)
        ((DerivedCategory.singleFunctor (ModuleCat.{max u₂ v}
          ((completedBaseChangeOfIsNoetherianRing hpow).functor.obj B₁).carrier) 0).obj N) 1),
      (completedBaseChangeOfIsNoetherianRing hpow).scalar B₁ f₁ • ξ = 0
```

## Tag 0GAM, a lemma

[Tag 0GAM](https://stacks.math.columbia.edu/tag/0GAM) in the Stacks Project.

**`Rig.isRigSmooth_completedBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigSmoothBaseChange.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/RigSmoothBaseChange.lean#L135).

> **Stacks Project, Tag 0GAM.** Rig-smoothness is preserved by completed base change along a
> map of Noetherian rings whose source and target ideals define the same closed subset of the
> target spectrum.

```lean
public theorem isRigSmooth_completedBaseChange
    (hV : (I₁.map (algebraMap A₁ A₂)).radical = I₂.radical)
    (C : CompletedBaseChange (A₁ := A₁) (A₂ := A₂) (I₁ := I₁) (I₂ := I₂))
    (B₁ : AdicFiniteTypeAlgebra.{u₁, v} A₁ I₁) (hB₁ : IsRigSmooth B₁) :
    IsRigSmooth (C.functor.obj B₁)
```

**`Rig.isRigSmooth_completedBaseChangedAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigSmoothCompletedBaseChange.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/RigSmoothCompletedBaseChange.lean#L86).

> **Stacks Project, Tag 0GAM.** Let `A₁ → A₂` be a map of Noetherian rings and let
> `I₁ ⊆ A₁`, `I₂ ⊆ A₂` be ideals with `V(I₁ A₂) = V(I₂)`.  If `B₁` is rig-smooth over
> `(A₁, I₁)`, then its base change `B₂ = (B₁ ⊗_{A₁} A₂)^`, the `I₂`-adic completion of Remark
> 0AL5, is rig-smooth over `(A₂, I₂)`.

```lean
public theorem isRigSmooth_completedBaseChangedAlgebra
    (hV : (I₁.map (algebraMap A₁ A₂)).radical = I₂.radical)
    (B₁ : AdicFiniteTypeAlgebra.{u₁, v} A₁ I₁) (hB₁ : IsRigSmooth B₁) :
    IsRigSmooth (I := I₂)
      (⟨CommAlgCat.of A₂ (completedBaseChangedAlgebra (I₂ := I₂) B₁),
        isAdicComplete_and_finiteType_completedBaseChangedAlgebra hV B₁⟩ :
        AdicFiniteTypeAlgebra.{u₂, max v u₂} A₂ I₂)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.4, Tag 0GAH](https://stacks.math.columbia.edu/tag/0GAH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
