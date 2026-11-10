---
declaration: section
origin: cited
lean: Stacks.Algebraization.fullyFaithful_completionFunctor_of_isProper, Stacks.Coherent.exists_isZero_Hgroup_transitionKernel_tensorPowModule_of_isRelativelyAmple, Stacks.Algebraization.isEquivalence_completionFunctor_of_isProjective_of_vanishing
statement: formalized
proof: formalized
---

# 30.24 Grothendieck's existence theorem, I

Section 30.24 of the Stacks Project, [Tag 087V](https://stacks.math.columbia.edu/tag/087V). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0883, a lemma

[Tag 0883](https://stacks.math.columbia.edu/tag/0883) in the Stacks Project.

**`Stacks.Algebraization.fullyFaithful_completionFunctor_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/FullyFaithfulComplete.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/FullyFaithfulComplete.lean#L283).

> **Stacks 0883.** Let `A` be a Noetherian ring complete with respect to an ideal `J`, let
> `f : X ⟶ Spec A` be proper and let `𝓙 = J · 𝒪_X`. Then the completion functor
> `Coh(𝒪_X) ⥤ Coh(X, 𝓙)` of Stacks 0880 is fully faithful.

```lean
public theorem fullyFaithful_completionFunctor_of_isProper :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    Nonempty (completionFunctor X (baseIdealSheaf A J f)).FullyFaithful
```

## Tag 0884, a lemma

[Tag 0884](https://stacks.math.columbia.edu/tag/0884) in the Stacks Project.

**`Stacks.Coherent.exists_isZero_Hgroup_transitionKernel_tensorPowModule_of_isRelativelyAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/TransitionKernelTwistVanishingAmple.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/TransitionKernelTwistVanishingAmple.lean#L73).

> **Stacks 0884.** Let `A` be a Noetherian ring, `I ⊆ A` an ideal, `f : X ⟶ Spec A` a proper
> morphism and `L` an invertible `𝒪_X`-module ample relative to `f`. Let `𝓕` be an object of
> `Coh(X, 𝓘)` for `𝓘 = I · 𝒪_X`. Then there is an integer `d₀` such that
>
>   `H¹(X, Ker(𝓕_{n+1} ⟶ 𝓕_n) ⊗ L ^⊗ d) = 0`
>
> for every `n ≥ 0` and every `d ≥ d₀` — one `d₀` for the whole system.
>
> The hypotheses are exactly the source's. The proof is the degree-one case of
> `Stacks.Coherent.exists_isZero_Hgroup_transitionKernel_tensorPowModule_of_pos` (Stacks 087Z and
> Stacks 0897 part (2)), whose ampleness hypothesis on `V(𝓘)` follows from `f`-ampleness by
> Stacks 01VK over the affine base and Stacks 0892 part (2) along the closed immersion
> `V(𝓘) ⟶ X`.

```lean
public theorem exists_isZero_Hgroup_transitionKernel_tensorPowModule_of_isRelativelyAmple
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) [IsProper f]
    (L : X.Modules) [Stacks.Ample.IsInvertibleModule X L]
    (hL : Stacks.RelativeAmple.IsRelativelyAmple f L)
    (𝓕 : CoherentAdicSystems (baseIdealSheaf A I f)) :
    ∃ d₀ : ℤ, ∀ (n : ℕ) (d : ℤ), d₀ ≤ d →
      IsZero (Hgroup X.ringCatSheaf ⊤ 1
        ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨X.presheaf,
              Presheaf.isSheaf_of_isSheaf_comp _ (X.presheaf) (forget₂ CommRingCat RingCat)
                ((isSheaf_structureRingPresheaf X))⟩).obj (transitionKernel 𝓕 n)).obj
          (Stacks.Ample.tensorPowModule X L d))))
```

## Tag 0885, a lemma

[Tag 0885](https://stacks.math.columbia.edu/tag/0885) in the Stacks Project.

**`Stacks.Algebraization.isEquivalence_completionFunctor_of_isProjective_of_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProjectiveEquivalence.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProjectiveEquivalence.lean#L148).

> **Grothendieck's existence theorem for a projective morphism**, [Stacks, Tag 0885], read at
> clause (1) of Tag 01W8.
>
> Let `A` be a Noetherian ring complete with respect to `I`, let `f : X ⟶ Spec A` be projective —
> a closed immersion over `Spec A` into a projective bundle `𝐏(ℰ)` — and set `𝓘 = I · 𝒪_X`. Then
> the completion functor `Coh(𝒪_X) ⥤ Coh(X, 𝓘)` of Stacks 0880 is an equivalence.
>
> Nothing is assumed beyond the source's hypotheses. In particular `UniversallyClosed f` and
> `LocallyOfFiniteType f` are *derived* from projectivity, through
> `AlgebraicGeometry.IsProjective.isProper`, rather than assumed; so is the local Noetherianity of
> `X` that the completion functor of Stacks 0880 needs, and so is the `f`-ample invertible module
> `L` the proof chooses.
>
> Full faithfulness is Stacks 0883
> (`Stacks.Algebraization.fullyFaithful_completionFunctor_of_isProper`). Essential surjectivity is
> `Stacks.Algebraization.essSurj_of_forall_exists_epi` fed by the generation statement
> `Stacks.Algebraization.exists_epi_completionFunctor_of_vanishing`, whose own input is the uniform
> `H¹`-vanishing of Stacks 0884
> (`Stacks.Coherent.exists_isZero_Hgroup_transitionKernel_tensorPowModule`); and that theorem's
> single hypothesis, part (2) of Stacks 0897 for the associated graded algebra of `𝓘`, is
> `Stacks.Coherent.hasAssociatedGradedTwistVanishing_of_isProper`, which needs only properness and
> the invertibility of `L`.
>
> The name's `_of_vanishing` records the shape the statement had while that hypothesis was still
> carried; it is kept because the statement itself did not change.

```lean
public theorem isEquivalence_completionFunctor_of_isProjective_of_vanishing
    (hf : AlgebraicGeometry.IsProjective f) :
    letI : IsProper f := hf.isProper
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    (completionFunctor X (baseIdealSheaf A I f)).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.24, Tag 087V](https://stacks.math.columbia.edu/tag/087V)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
