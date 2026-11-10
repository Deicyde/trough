---
declaration: section
origin: cited
lean: Rig.isRigSmooth_iff_forall_idealOfDefinition, RingHom.IsRigSmooth, Rig.rigSmooth_isLocalNoetherian, Rig.rigSmooth_isLocalNoetherian', TopologicalRing.rigSmooth_completedTensorProduct_of_isAdic, Rig.rigSmooth_comp, Rig.isRigFlat_and_exists_isRegular_of_isRigSmooth, Rig.CompletedPolynomialPresentation.exists_pow_adicIdeal_le_annihilator_ker_onH₁_chainMapInl
statement: formalized
proof: formalized
---

# 88.17 Rig-smooth homomorphisms

Section 88.17 of the Stacks Project, [Tag 0GCH](https://stacks.math.columbia.edu/tag/0GCH). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GCI, a lemma

[Tag 0GCI](https://stacks.math.columbia.edu/tag/0GCI) in the Stacks Project.

**`Rig.isRigSmooth_iff_forall_idealOfDefinition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigSmooth.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/RigSmooth.lean#L186).

> **Stacks Project, Tag 0GCI.** Rig-smoothness of a finite-type morphism of Noetherian
> weakly admissible rings does not depend on the ideal of definition of its source.

```lean
public theorem isRigSmooth_iff_forall_idealOfDefinition
    {A : Type u} {B : Type v}
    [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    (hA : TopologicalRing.IsWeaklyAdmissible A) (_hB : TopologicalRing.IsWeaklyAdmissible B)
    (φ : A →+* B) (_hφ : Continuous φ) (hft : FiniteTypeAdicAlgebraForEveryIdeal φ) :
    (∃ (I : Ideal A) (hI : TopologicalRing.IsIdealOfDefinition I),
      IsRigSmooth (adicFiniteTypeAlgebra φ hft I hI)) ↔
      (∀ (I : Ideal A) (hI : TopologicalRing.IsIdealOfDefinition I),
        IsRigSmooth (adicFiniteTypeAlgebra φ hft I hI))
```

## Tag 0GCJ, a definition

[Tag 0GCJ](https://stacks.math.columbia.edu/tag/0GCJ) in the Stacks Project.

**`RingHom.IsRigSmooth`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigSmooth.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/RigSmooth.lean#L251).

> **Stacks Project, Tag 0GCJ.** A continuous homomorphism of Noetherian adic topological
> rings is *rig-smooth* when it is adic of topologically finite type — condition (6) of Tag 0GBW
> — and makes its target rig-smooth over some ideal of definition of its source.  By Tag 0GCI the
> choice of that ideal is immaterial.

```lean
public abbrev IsRigSmooth {A : Type u} {B : Type v}
    [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [IsNoetherianRing A]
    [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [IsNoetherianRing B]
    (φ : A →+* B) : Prop
```

## Tag 0GCK, a lemma

[Tag 0GCK](https://stacks.math.columbia.edu/tag/0GCK) in the Stacks Project.

**`Rig.rigSmooth_isLocalNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigSmoothLocality.lean, line 451](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/RigSmoothLocality.lean#L451).

> **Stacks 0GCK.** Rig-smoothness is a local property of arrows of `WAdm^Noeth`: it ascends
> along a completed étale localization diagram, descends along one whose target-side horizontal
> map is faithfully flat, and is preserved by finite products of targets.

```lean
public theorem rigSmooth_isLocalNoetherian :
    TopologicalRing.PropertyIsLocalNoetherian.{u}
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦
        RingHom.IsRigSmoothArrow φ)
```

**`Rig.rigSmooth_isLocalNoetherian'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigSmoothLocalityRefined.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/RigSmoothLocalityRefined.lean#L124).

> **Stacks 0GCK.** Rig-smoothness is a local property of arrows of `WAdm^Noeth`: it is
> independent of the presentations of its source and target, ascends along a completed étale
> localization diagram, descends along one whose target-side horizontal map is faithfully flat,
> and is preserved by finite products of targets.

```lean
public theorem rigSmooth_isLocalNoetherian' :
    TopologicalRing.PropertyIsLocalNoetherian'.{u}
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦
        RingHom.IsRigSmoothArrow φ)
```

## Tag 0GCL, a lemma

[Tag 0GCL](https://stacks.math.columbia.edu/tag/0GCL) in the Stacks Project.

**`TopologicalRing.rigSmooth_completedTensorProduct_of_isAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigSmoothStability.lean, line 771](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/RigSmoothStability.lean#L771).

> Rig-smoothness (Tag 0GCJ) is stable under base change by adic morphisms (Tag 0GBR) in the
> sense of Remark 0GBG: if `B → A` is rig-smooth and `B → C` is adic, both arrows of
> `WAdm^{Noeth}`, then the completed tensor product `A ⊗̂_B C` is again Noetherian adic and
> rig-smooth over `C`.

```lean
public theorem rigSmooth_completedTensorProduct_of_isAdic
    {B A C : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B] [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing C] [TopologicalSpace C] [IsTopologicalRing C]
    [IsLinearTopology C C] [Algebra B A] [Algebra B C] [IsNoetherianRing B]
    [IsNoetherianRing A] [IsNoetherianRing C]
    (hB : TopologicalRing.IsAdic B) (hA : TopologicalRing.IsAdic A)
    (hC : TopologicalRing.IsAdic C)
    (hBA : Continuous (algebraMap B A)) (hBC : Continuous (algebraMap B C))
    (hP : RingHom.IsRigSmoothArrow (algebraMap B A))
    (hQ : RingHom.IsAdic (algebraMap B C)) :
    TopologicalRing.IsAdic (TopologicalRing.CompletedTensorProduct (R := B) (M := A) (N := C)) ∧
      IsNoetherianRing (TopologicalRing.CompletedTensorProduct (R := B) (M := A) (N := C)) ∧
      RingHom.IsRigSmoothArrow
        (algebraMap C (TopologicalRing.CompletedTensorProduct (R := B) (M := A) (N := C)))
```

## Tag 0GCM, a lemma

[Tag 0GCM](https://stacks.math.columbia.edu/tag/0GCM) in the Stacks Project.

**`Rig.rigSmooth_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigSmoothStableUnderComposition.lean, line 401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/RigSmoothStableUnderComposition.lean#L401).

> **Stacks Project, Tag 0GCM.**  Rig-smoothness of arrows of `WAdm^Noeth` is stable under
> composition: if `f : B →+* A` and `g : C →+* B` are continuous rig-smooth homomorphisms of
> Noetherian adic topological rings, then so is `f ∘ g`.
>
> Condition (6) of Stacks 0GBW for the composite is
> `Rig.finiteTypeAdicAlgebraForEveryIdeal_comp`.  For rig-smoothness over an ideal of definition
> `I ⊆ C`, Stacks 0GCI moves both hypotheses onto `I` and onto `I B`, Stacks 0ALM presents `A`
> over `(C, I)` by combining the two presentations, and
> `Rig.hasCotangentFactorization_combinedPresentation` multiplies the two factorizations of
> condition (3) of Stacks 0GAJ.

```lean
public theorem rigSmooth_comp
    {A B C : Type u} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B] [CommRing C] [TopologicalSpace C] [IsTopologicalRing C]
    [IsLinearTopology C C]
    (hA : TopologicalRing.IsAdic A ∧ IsNoetherianRing A)
    (hB : TopologicalRing.IsAdic B ∧ IsNoetherianRing B)
    (hC : TopologicalRing.IsAdic C ∧ IsNoetherianRing C)
    (f : B →+* A) (g : C →+* B) (hf : Continuous f) (hg : Continuous g)
    (hPf : RingHom.IsRigSmoothArrow f) (hPg : RingHom.IsRigSmoothArrow g) :
    RingHom.IsRigSmoothArrow (f.comp g)
```

## Tag 0GH1, a lemma

[Tag 0GH1](https://stacks.math.columbia.edu/tag/0GH1) in the Stacks Project.

**`Rig.isRigFlat_and_exists_isRegular_of_isRigSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigSmoothRigFlat.lean, line 640](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/RigSmoothRigFlat.lean#L640).

> **Stacks Project, Tag 0GH1.**  Let `φ : A → B` be an arrow of `WAdm^{Noeth}` — a continuous
> homomorphism of Noetherian adic topological rings — which is rig-smooth.  Then `φ` is rig-flat,
> and for every presentation `B = A⟨x₁, …, x_n⟩ / J` (over an ideal of definition `I` of `A`) and
> every prime `J ⊆ 𝔮 ⊆ A⟨x⟩` not containing an ideal of definition, the ideal `J_𝔮` of `A⟨x⟩_𝔮` is
> generated by a regular sequence.
>
> Rig-flatness asks naive rig-flatness of every map `A_{\{f\}} → B_{\{f\}}`, which is
> `Rig.isNaivelyRigFlat_completedAwayMap_of_isRigSmooth`; the regular sequences are
> `Rig.exists_isRegular_ofList_eq_map_presentationIdeal`.  Both rest on the reduction of the
> source's proof to a rig-closed prime lying over a rig-closed prime, through the completed
> principal localization of Stacks 0GGG, where the Jacobian criterion on the regular fibre
> (Stacks 0GGJ, 0GEE, 00MG) concludes.

```lean
public theorem isRigFlat_and_exists_isRegular_of_isRigSmooth
    {A : Type u} {B : Type v}
    [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [IsNoetherianRing A]
    [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [IsNoetherianRing B]
    (hA : TopologicalRing.IsAdic A) (hB : TopologicalRing.IsAdic B)
    (φ : A →+* B) (hφ : Continuous φ) (hsm : _root_.RingHom.IsRigSmooth φ) :
    RingHom.IsRigFlat φ ∧
      ∀ (hft : FiniteTypeAdicAlgebraForEveryIdeal φ) (I : Ideal A)
        (hI : TopologicalRing.IsIdealOfDefinition I)
        (P : CompletedPolynomialPresentation I (adicFiniteTypeAlgebra φ hft I hI))
        (q : Ideal P.completedPolynomialRing) [q.IsPrime],
        ¬ I.map (algebraMap A P.completedPolynomialRing) ≤ q → P.ideal ≤ q →
        ∃ fs : List (Localization.AtPrime q),
          RingTheory.Sequence.IsRegular (Localization.AtPrime q) fs ∧
            Ideal.ofList fs =
              P.ideal.map (algebraMap P.completedPolynomialRing (Localization.AtPrime q))
```

## Tag 0GH2, a lemma

[Tag 0GH2](https://stacks.math.columbia.edu/tag/0GH2) in the Stacks Project.

**`Rig.CompletedPolynomialPresentation.exists_pow_adicIdeal_le_annihilator_ker_onH₁_chainMapInl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/NaiveCotangent/CombinedRigSmooth.lean, line 566](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/NaiveCotangent/CombinedRigSmooth.lean#L566).

> **Stacks Project, Tag 0GH2.**  Let `A → B → C` be morphisms of (0AL4), so that `B` and `C`
> are adic and topologically of finite type over `A`, and suppose `B → C` is rig-smooth, i.e. `C`
> is rig-smooth over `(B, I B)` (Stacks 0GAI, 0GCJ).  Then the kernel of the first map
> `H⁻¹(NL^∧_{B/A} ⊗_B C) → H⁻¹(NL^∧_{C/A})` of the six-term sequence of Stacks 0ALM is annihilated
> by a power of the ideal of definition `I C`.
>
> The presentations are the given ones: `P` of `B` over `A`, the presentation `ψ` of `C` over
> `B`, and the combined presentation of `C` over `A` they define.

```lean
public theorem exists_pow_adicIdeal_le_annihilator_ker_onH₁_chainMapInl
    (KB : CompletedNaiveCotangentComplex P)
    (KC : CompletedNaiveCotangentComplex
      (P.combinedPresentation s (ψ.restrictScalars A) hψ))
    (hBC : IsRigSmooth (AdicFiniteTypeAlgebra.overBase (B := B) (C := C))) :
    ∃ n : ℕ, C.adicIdeal ^ n ≤ Module.annihilator C.carrier
      (LinearMap.ker (NaiveCotangent.chainMapInl _
        (P.combinedDifferential_comp_innerCotangentMap s ψ hψ KB KC)).onH₁)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.17, Tag 0GCH](https://stacks.math.columbia.edu/tag/0GCH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
