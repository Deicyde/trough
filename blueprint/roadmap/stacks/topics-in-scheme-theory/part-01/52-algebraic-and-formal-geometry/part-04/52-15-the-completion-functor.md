---
declaration: section
origin: cited
lean: Stacks.Algebraization.quasiAffine_sectionsComplete_implies_amplePower_sectionsComplete, Stacks.Algebraization.sectionsComplete_chain, Stacks.Algebraization.NeighbourhoodCompletion.implications_among_conditions, Stacks.Algebraization.quasiAffine_neighbourhoodSectionsComplete_implies_amplePower, Stacks.Coherent.coherentAdicToPro_fullyFaithful, Stacks.Algebraization.completionFullyFaithful_of_associatedPrimes_of_depth, Stacks.Algebraization.completionFullyFaithfulOnFiniteLocallyFree_iff, Stacks.Algebraization.completionFullyFaithful_of_annihilated
statement: formalized
proof: formalized
---

# 52.15 The completion functor

Section 52.15 of the Stacks Project, [Tag 0EKN](https://stacks.math.columbia.edu/tag/0EKN). 9 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EKP, a lemma

[Tag 0EKP](https://stacks.math.columbia.edu/tag/0EKP) in the Stacks Project.

**`Stacks.Algebraization.quasiAffine_sectionsComplete_implies_amplePower_sectionsComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/Basic.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/Basic.lean#L358). The attribute's comment: “(1) implies (2)”.

> **Stacks 0EKP, (1) implies (2).** On a quasi-affine scheme the structure sheaf is itself an
> ample invertible module, and every tensor power of it is again the structure sheaf, so section
> completeness on the infinitesimal neighbourhoods transports to all powers.

```lean
public theorem quasiAffine_sectionsComplete_implies_amplePower_sectionsComplete
    {X Y : Scheme.{u}} (i : Y ⟶ X) [IsClosedImmersion i] [IsNoetherian X]
    (hX : Scheme.IsQuasiAffine X)
    (h : IsInfinitesimalSectionsComplete i (SheafOfModules.unit X.ringCatSheaf)) :
    ∃ (L : X.Modules)
      (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.toRingedSpace.presheaf
        (structureSheafRing X.toRingedSpace).property L),
      letI := hL
      AlgebraicGeometry.Scheme.Modules.IsAmple X L ∧
        ∃ N : ℕ, ∀ m : ℕ, N ≤ m →
          IsInfinitesimalSectionsComplete i
            (Stacks.SheafOfModules.Invertible.tensorPower X.toRingedSpace.presheaf
              (structureSheafRing X.toRingedSpace).property L (m : ℤ))
```

**`Stacks.Algebraization.sectionsComplete_chain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/Chain.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/Chain.lean#L148).

> Let `X` be a Noetherian scheme, let `Y ⊆ X` be a closed subscheme and let `Y_n ⊆ X` be the
> `n`-th infinitesimal neighbourhood of `Y` in `X`. Consider the conditions
>
> 1. `X` is quasi-affine and `Γ(X, 𝒪_X) → lim Γ(Y_n, 𝒪_{Y_n})` is an isomorphism;
> 2. `X` has an ample invertible module `L` and `Γ(X, L^{⊗ m}) → lim Γ(Y_n, L^{⊗ m}|_{Y_n})` is an
>    isomorphism for all `m ≫ 0`;
> 3. for every finite locally free `𝒪_X`-module `ℰ` the map `Γ(X, ℰ) → lim Γ(Y_n, ℰ|_{Y_n})` is an
>    isomorphism;
> 4. the completion functor `Coh(𝒪_X) → Coh(X, I)` is fully faithful on the full subcategory of
>    finite locally free objects.
>
> Then `(1) ⇒ (2) ⇒ (3) ⇒ (4)` and `(4) ⇒ (3)`.

```lean
public theorem sectionsComplete_chain {X Y : Scheme.{u}} (i : Y ⟶ X) [IsClosedImmersion i]
    [IsNoetherian X] :
    (SectionsCompleteQuasiAffine i → SectionsCompleteAmplePowers i) ∧
      (SectionsCompleteAmplePowers i → SectionsCompleteFiniteLocallyFree i) ∧
      (SectionsCompleteFiniteLocallyFree i →
        CompletionFullyFaithfulOnFiniteLocallyFree X i.ker) ∧
      (CompletionFullyFaithfulOnFiniteLocallyFree X i.ker →
        SectionsCompleteFiniteLocallyFree i)
```

## Tag 0EK2, a lemma

[Tag 0EK2](https://stacks.math.columbia.edu/tag/0EK2) in the Stacks Project.

**`Stacks.Algebraization.NeighbourhoodCompletion.implications_among_conditions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/NeighbourhoodCompletion.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/NeighbourhoodCompletion.lean#L269).

> **[Stacks, Tag 0EK2].** Let `X` be a Noetherian scheme and let `Y ⊂ X` be a closed subscheme
> with ideal sheaf `ℐ ⊂ 𝒪_X`. Let `Y_n ⊂ X` be the `n`-th infinitesimal neighbourhood of `Y` in `X`,
> and let `𝒱` be the set of open subschemes `V ⊂ X` containing `Y`, ordered by reverse inclusion.
> Consider the conditions
>
> 1. `X` is quasi-affine and `colim_𝒱 Γ(V, 𝒪_V) ⟶ lim Γ(Y_n, 𝒪_{Y_n})` is an isomorphism;
> 2. `X` has an ample invertible module `ℒ` and
>    `colim_𝒱 Γ(V, ℒ^{⊗ m}) ⟶ lim Γ(Y_n, ℒ^{⊗ m}|_{Y_n})` is an isomorphism for all `m ≫ 0`;
> 3. for every `V ∈ 𝒱` and every finite locally free `𝒪_V`-module `ℰ` the map
>    `colim_{V' ≥ V} Γ(V', ℰ|_{V'}) ⟶ lim Γ(Y_n, ℰ|_{Y_n})` is an isomorphism;
> 4. the completion functor `colim_𝒱 Coh(𝒪_V) ⟶ Coh(X, ℐ)`, `ℱ ↦ ℱ^∧`, is fully faithful on the
>    full subcategory of finite locally free objects.
>
> Then `(1) ⇒ (2) ⇒ (3) ⇒ (4)` and `(4) ⇒ (3)`.
>
> The source proves `(1) ⇒ (2)` from the ampleness of `𝒪_X` on a quasi-affine scheme, `(2) ⇒ (3)`
> from a universally exact sequence `0 → ℰ → (ℒ^{⊗ p})^{⊕ r}|_V → (ℒ^{⊗ q})^{⊕ s}|_V`, and
> `(3) ⇒ (4)` by applying `(3)` to the internal hom; it omits the proof of `(4) ⇒ (3)`, which is
> `(4)` applied to the pair `(𝒪_V, ℰ)`, read through the identification of a section of `ℰ` with a
> morphism `𝒪 ⟶ ℰ`.

```lean
public theorem implications_among_conditions [IsNoetherian X] :
    (IsQuasiAffineComplete i → HasAmpleComplete i) ∧
      (HasAmpleComplete i → FiniteLocallyFreeComplete i) ∧
      (FiniteLocallyFreeComplete i → CompletionFullyFaithfulComplete i) ∧
      (CompletionFullyFaithfulComplete i → FiniteLocallyFreeComplete i)
```

**`Stacks.Algebraization.quasiAffine_neighbourhoodSectionsComplete_implies_amplePower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/Neighbourhoods.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/Neighbourhoods.lean#L248). The attribute's comment: “(1) implies (2)”.

> **Condition (1) implies condition (2).** Let `i : Y ⟶ X` be a closed immersion into a
> Noetherian quasi-affine scheme such that the colimit of the sections of `𝒪_X` over the open
> neighbourhoods of `Y` is the limit of its sections on the infinitesimal neighbourhoods. Then `X`
> carries an ample invertible module `L` for which the same holds for every tensor power `L^{⊗ m}`
> with `m` large enough.

```lean
public theorem quasiAffine_neighbourhoodSectionsComplete_implies_amplePower
    {X Y : Scheme.{u}} (i : Y ⟶ X) [IsClosedImmersion i] [IsNoetherian X]
    (hX : Scheme.IsQuasiAffine X)
    (h : IsNeighbourhoodSectionsComplete i (SheafOfModules.unit X.ringCatSheaf)) :
    ∃ (L : X.Modules)
      (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.toRingedSpace.presheaf
        (structureSheafRing X.toRingedSpace).property L),
      letI := hL
      AlgebraicGeometry.Scheme.Modules.IsAmple X L ∧
        ∃ N : ℕ, ∀ m : ℕ, N ≤ m →
          IsNeighbourhoodSectionsComplete i
            (Stacks.SheafOfModules.Invertible.tensorPower X.toRingedSpace.presheaf
              (structureSheafRing X.toRingedSpace).property L (m : ℤ))
```

## Tag 0EIQ, a lemma

[Tag 0EIQ](https://stacks.math.columbia.edu/tag/0EIQ) in the Stacks Project.

**`Stacks.Coherent.coherentAdicToPro_fullyFaithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicPro.lean, line 1144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicPro.lean#L1144).

> A coherent adic system has exactly the morphisms of its associated
> pro-quasi-coherent object.

```lean
public theorem coherentAdicToPro_fullyFaithful
    (X : Scheme.{u}) (I : X.IdealSheafData) :
    Nonempty (coherentAdicToPro X I).FullyFaithful
```

## Tag 0EKQ, a lemma

[Tag 0EKQ](https://stacks.math.columbia.edu/tag/0EKQ) in the Stacks Project.

**`Stacks.Algebraization.completionFullyFaithful_of_associatedPrimes_of_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/DimensionDepthCriterion.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/DimensionDepthCriterion.lean#L256).

> **Stacks 0EKQ.** Let `I ⊆ 𝔞` be ideals of a Noetherian ring `A` and let
> `U = Spec(A) ∖ V(𝔞)`. Assume
>
> 1. `A` is `I`-adically complete and has a dualizing complex,
> 2. for every associated prime `𝔭` of `A` with `𝔭 ∉ V(I)` and `V(𝔭) ∩ V(I) ⊄ V(𝔞)`, and every
>    `𝔮 ∈ V(𝔭) ∩ V(𝔞)`, one has `dim((A/𝔭)_𝔮) > cd(A, I) + 1`,
> 3. for every prime `𝔭` with `𝔭 ∉ V(I)` and `V(𝔭) ∩ V(I) ⊆ V(𝔞)`, one has `depth(A_𝔭) ≥ 2`.
>
> Then the completion functor `Coh(𝒪_U) ⟶ Coh(U, I𝒪_U)`, `ℱ ↦ ℱ^∧`, is fully faithful on the full
> subcategory of finite locally free objects.
>
> The dimension `dim((A/𝔭)_𝔮)` is written as the Krull dimension of `A_𝔮 / 𝔭 A_𝔮`, which is the
> same ring.

```lean
theorem completionFullyFaithful_of_associatedPrimes_of_depth
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I a : Ideal A) (hIa : I ≤ a)
    (hcomplete : IsAdicComplete I A)
    (hdualizing : ∃ K : DerivedCategory (ModuleCat.{u} A), Dualizing.IsDualizingComplex K)
    (hdim : ∀ p : PrimeSpectrum A, p.asIdeal ∈ associatedPrimes A A → ¬ I ≤ p.asIdeal →
      ¬ (PrimeSpectrum.zeroLocus (p.asIdeal : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) ⊆
        PrimeSpectrum.zeroLocus (a : Set A)) →
      ∀ q ∈ PrimeSpectrum.zeroLocus (p.asIdeal : Set A) ∩ PrimeSpectrum.zeroLocus (a : Set A),
        ((cohomologicalDimension A I I.fg_of_isNoetherianRing + 1 : ℤ) : EInt) <
          krullDimToEInt (ringKrullDim ((Localization.AtPrime q.asIdeal) ⧸
            p.asIdeal.map (algebraMap A (Localization.AtPrime q.asIdeal)))))
    (hdepth : ∀ p : PrimeSpectrum A, ¬ I ≤ p.asIdeal →
      PrimeSpectrum.zeroLocus (p.asIdeal : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) ⊆
        PrimeSpectrum.zeroLocus (a : Set A) →
      (2 : ℕ∞) ≤ Module.depth (Localization.AtPrime p.asIdeal)
        (maximalIdeal (Localization.AtPrime p.asIdeal)) (Localization.AtPrime p.asIdeal)) :
    CompletionFullyFaithfulOnFiniteLocallyFree (complementZeroLocus A a : Scheme)
      (idealSheafNearVanishing A I a)
```

**`Stacks.Algebraization.completionFullyFaithfulOnFiniteLocallyFree_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/InternalHomCriterion.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/InternalHomCriterion.lean#L170). The attribute's comment: “REDUCED, not proved: full faithfulness on the finite locally free objects holds exactly when the formal-functions comparison is an isomorphism for the internal homs. That half is Stacks 0EIG, which the library has at Stacks 0EG2's hypotheses and for another spelling of the comparison; it is neither proved nor assumed here, being one side of this equivalence. Conditions (1)-(3) of the tag are not consumed”.

> **Stacks 0EKQ, reduced to the theorem on formal functions in degree zero.** For ideals
> `I ⊆ 𝔞` of a Noetherian ring `A` and `U = Spec(A) ∖ V(𝔞)`, completion along `I𝒪_U` is fully
> faithful on the finite locally free coherent sheaves on `U` exactly when
> `Γ(U, ℋ) ⟶ lim_n Γ(U, ℋ / Iⁿ ℋ)` is an isomorphism for every `ℋ = SheafHom(ℱ, 𝒢)`.

```lean
public theorem completionFullyFaithfulOnFiniteLocallyFree_iff
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I a : Ideal A) :
    CompletionFullyFaithfulOnFiniteLocallyFree (complementZeroLocus A a : Scheme)
        (idealSheafNearVanishing A I a) ↔
      ∀ P Q : AlgebraicGeometry.SheafOfModules.CoherentModules
          (complementZeroLocus A a : Scheme).ringCatSheaf,
        AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} P.obj →
        AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} Q.obj →
        IsIso (globalSectionsToLimit (idealSheafNearVanishing A I a)
          (internalHomCoherent (complementZeroLocus A a : Scheme) P Q))
```

## Tag 0EKS, a lemma

[Tag 0EKS](https://stacks.math.columbia.edu/tag/0EKS) in the Stacks Project.

**`Stacks.Algebraization.completionFullyFaithful_of_annihilated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/AnnihilatedCriterion.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/AnnihilatedCriterion.lean#L91).

> Let `A` be a Noetherian ring, let `f ∈ 𝔞 ⊆ A` and let `U = Spec(A) ∖ V(𝔞)`. If `A` is
> `f`-adically complete and `H¹_𝔞(A)` and `H²_𝔞(A)` are annihilated by powers of `f`, then the
> completion functor `Coh(𝒪_U) ⟶ Coh(U, (f)𝒪_U)`, `ℱ ↦ ℱ^∧`, is fully faithful on the full
> subcategory of finite locally free objects.

```lean
public theorem completionFullyFaithful_of_annihilated (hf : f ∈ a)
    (hcomplete : IsAdicComplete (Ideal.span {f}) A)
    (h1 : ∃ n, ∀ x : localCohomologyModule A a (Ideal.fg_of_isNoetherianRing a)
      (ModuleCat.of A A) 1, f ^ n • x = 0)
    (h2 : ∃ n, ∀ x : localCohomologyModule A a (Ideal.fg_of_isNoetherianRing a)
      (ModuleCat.of A A) 2, f ^ n • x = 0) :
    CompletionFullyFaithfulOnFiniteLocallyFree (complementZeroLocus A a : Scheme)
      (complementPrincipalIdealSheaf A a f)
```

**`Stacks.Algebraization.completionFullyFaithfulOnFiniteLocallyFree_of_isAdicComplete_of_annihilated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/CompleteCriteria.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/CompleteCriteria.lean#L78).

> **[Stacks, Tag 0EKS].** Let `A` be a Noetherian ring, let `f ∈ 𝔞 ⊆ A` and let
> `U = Spec(A) ∖ V(𝔞)`. If `A` is `f`-adically complete and `H¹_𝔞(A)` and `H²_𝔞(A)` are
> annihilated by a power of `f`, then the completion functor `Coh(𝒪_U) ⟶ Coh(U, (f)𝒪_U)` is fully
> faithful on the finite locally free objects.
>
> The ideal sheaf `(f)𝒪_U` is `complementPrincipalIdealSheaf A 𝔞 f`, and full faithfulness on the
> finite locally free objects is `CompletionFullyFaithfulOnFiniteLocallyFree`. The proof is
> `completionFullyFaithful_of_isAdicComplete_of_annihilated`, Stacks 0EII followed by the chain
> (1) ⇒ (4) of Stacks 0EKP, with that chain supplied by
> `completionFullyFaithfulOnFiniteLocallyFree_of_bijective_sectionsToLimit`.

```lean
public theorem completionFullyFaithfulOnFiniteLocallyFree_of_isAdicComplete_of_annihilated
    (A : Type u) [CommRing A] [IsNoetherianRing A] (a : Ideal A) (f : A) (hf : f ∈ a)
    (hcomplete : IsAdicComplete (Ideal.span {f}) A)
    (h1 : ∃ n, ∀ x : localCohomologyModule A a (Ideal.fg_of_isNoetherianRing a)
      (ModuleCat.of A A) 1, f ^ n • x = 0)
    (h2 : ∃ n, ∀ x : localCohomologyModule A a (Ideal.fg_of_isNoetherianRing a)
      (ModuleCat.of A A) 2, f ^ n • x = 0) :
    CompletionFullyFaithfulOnFiniteLocallyFree (complementZeroLocus A a : Scheme)
      (complementPrincipalIdealSheaf A a f)
```

## Tag 0EKT, a lemma

[Tag 0EKT](https://stacks.math.columbia.edu/tag/0EKT) in the Stacks Project.

**`Stacks.Algebraization.completionFullyFaithfulOnFiniteLocallyFree_of_isAdicComplete_of_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/CompleteCriteria.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/CompleteCriteria.lean#L108).

> **[Stacks, Tag 0EKT].** Let `A` be a Noetherian ring, let `f ∈ 𝔞 ⊆ A` and let
> `U = Spec(A) ∖ V(𝔞)`. Assume
>
> 1. `A` has a dualizing complex and is complete with respect to `f`, and
> 2. `depth(A_𝔭) + dim((A/𝔭)_𝔮) > 2` for every prime `𝔭 ⊆ A` with `f ∉ 𝔭` and every
>    `𝔮 ∈ V(𝔭) ∩ V(𝔞)`.
>
> Then the completion functor `Coh(𝒪_U) ⟶ Coh(U, (f)𝒪_U)` is fully faithful on the finite locally
> free objects.
>
> Hypothesis (1) is `hdual` together with `hcomplete`. In hypothesis (2), `𝔮 ∈ V(𝔭) ∩ V(𝔞)` is
> `𝔞 ≤ 𝔮` and `𝔭 ≤ 𝔮`, `(A/𝔭)_𝔮` is `A_𝔮 / 𝔭A_𝔮`, and the inequality is read in the extended
> integers through `enatToEInt` and `krullDimToEInt`, as in
> `completionFullyFaithful_of_isAdicComplete_of_depth`. The proof is that theorem — Faltings'
> annihilator theorem, Stacks 0EFC, followed by Stacks 0EKS — with the chain (1) ⇒ (4) of
> Stacks 0EKP supplied by `completionFullyFaithfulOnFiniteLocallyFree_of_bijective_sectionsToLimit`.

```lean
public theorem completionFullyFaithfulOnFiniteLocallyFree_of_isAdicComplete_of_depth
    (A : Type u) [CommRing A] [IsNoetherianRing A] (a : Ideal A) (f : A) (hf : f ∈ a)
    (hdual : ∃ omega : DerivedCategory (ModuleCat.{u} A), Dualizing.IsDualizingComplex omega)
    (hcomplete : IsAdicComplete (Ideal.span {f}) A)
    (hdepth : ∀ p q : PrimeSpectrum A, f ∉ p.asIdeal → a ≤ q.asIdeal →
      p.asIdeal ≤ q.asIdeal →
      enatToEInt
          (Module.depth (Localization.AtPrime p.asIdeal)
            (maximalIdeal (Localization.AtPrime p.asIdeal))
            (LocalizedModule p.asIdeal.primeCompl A)) +
        krullDimToEInt
          (ringKrullDim ((Localization.AtPrime q.asIdeal) ⧸
            p.asIdeal.map (algebraMap A (Localization.AtPrime q.asIdeal)))) > ((2 : ℤ) : EInt)) :
    CompletionFullyFaithfulOnFiniteLocallyFree (complementZeroLocus A a : Scheme)
      (complementPrincipalIdealSheaf A a f)
```

**`Stacks.Algebraization.completionFullyFaithful_of_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/DepthCriterion.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/DepthCriterion.lean#L206).

> **Stacks 0EKT.** Let `A` be a Noetherian ring, let `f ∈ 𝔞 ⊆ A` and let
> `U = Spec(A) ∖ V(𝔞)`. If `A` has a dualizing complex and is `f`-adically complete, and if
> `depth(A_𝔭) + dim((A/𝔭)_𝔮) > 2` for every prime `𝔭` with `f ∉ 𝔭` and every
> `𝔮 ∈ V(𝔭) ∩ V(𝔞)`, then the completion functor `Coh(𝒪_U) ⟶ Coh(U, (f)𝒪_U)` is fully faithful
> on the full subcategory of finite locally free objects.

```lean
public theorem completionFullyFaithful_of_depth (A : Type u) [CommRing A] [IsNoetherianRing A]
    (a : Ideal A) (f : A) (hf : f ∈ a)
    (omega : DerivedCategory (ModuleCat.{u} A))
    (homega : Dualizing.IsDualizingComplex (A := A) (K := omega))
    (hcomplete : IsAdicComplete (Ideal.span {f}) A)
    (hdepth : ∀ p q : PrimeSpectrum A, f ∉ p.asIdeal → a ≤ q.asIdeal →
      p.asIdeal ≤ q.asIdeal →
      enatToEInt
          (Module.depth (Localization.AtPrime p.asIdeal)
            (maximalIdeal (Localization.AtPrime p.asIdeal))
            (LocalizedModule p.asIdeal.primeCompl A)) +
        krullDimToEInt
          (ringKrullDim ((Localization.AtPrime q.asIdeal) ⧸
            p.asIdeal.map (algebraMap A (Localization.AtPrime q.asIdeal)))) > ((2 : ℤ) : EInt)) :
    CompletionFullyFaithfulOnFiniteLocallyFree (complementZeroLocus A a : Scheme)
      (complementPrincipalIdealSheaf A a f)
```

## Tag 0EKU, a lemma

[Tag 0EKU](https://stacks.math.columbia.edu/tag/0EKU) in the Stacks Project.

**`Stacks.Algebraization.completionFullyFaithful_finiteLocallyFree_on`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/NeighbourhoodHomsOnBijective.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/NeighbourhoodHomsOnBijective.lean#L120).

> **Stacks 0EKU.** Let `I ⊆ 𝔞 ⊆ A` be ideals of a Noetherian ring `A`, put
> `U = Spec(A) ∖ V(𝔞)` and let `𝒱` be the set of open subschemes of `U` containing `U ∩ V(I)`,
> ordered by reverse inclusion. Assume
>
> 1. `A` is `I`-adically complete and has a dualizing complex, and
> 2. for every associated prime `𝔭` of `A` with `I ⊄ 𝔭` and `V(𝔭) ∩ V(I) ⊄ V(𝔞)`, and every
>    `𝔮 ∈ V(𝔭) ∩ V(𝔞)`, we have `dim((A/𝔭)_𝔮) > cd(A, I) + 1`.
>
> Then the completion functor `colim_𝒱 Coh(𝒪_V) ⟶ Coh(U, I𝒪_U)` is fully faithful on the full
> subcategory of finite locally free objects: for every `V ∈ 𝒱` and all finite locally free coherent
> `𝒪_V`-modules `G`, `F`, the map
> `colim_{V' ≥ V} Hom_{V'}(G|_{V'}, F|_{V'}) ⟶ Hom_{Coh(V, I𝒪_V)}(G^∧, F^∧)` is bijective.
>
> Two objects of the colimit category given on members `V₁`, `V₂` of `𝒱` are compared on
> `V₁ ∩ V₂ ∈ 𝒱`, so "for every `V`" is full faithfulness. The target `Coh(V, I𝒪_V)` is
> `Coh(U, I𝒪_U)` on morphisms by `Stacks.Algebraization.bijective_restrictCompletionHom`.
> The source's condition (2) on the associated primes of `A` gives condition (2) of Stacks 0EIV for
> a finite locally free `F`, whose associated points are associated points of `V`
> (`Stacks.Algebraization.associatedPointsClosureDimensionBoundOn_of_isFiniteLocallyFree`); the
> finite local freeness of `G` is not needed.

```lean
theorem completionFullyFaithful_finiteLocallyFree_on (hIa : I ≤ a)
    (hcomplete : IsAdicComplete I A)
    (hdualizing : ∃ K : DerivedCategory (ModuleCat.{u} A), Dualizing.IsDualizingComplex K)
    (hdim : ∀ p : PrimeSpectrum A, IsAssociatedPrimeStacks A A p.asIdeal →
      ¬ I ≤ p.asIdeal →
      (∃ y : PrimeSpectrum A, p.asIdeal ≤ y.asIdeal ∧ I ≤ y.asIdeal ∧ ¬ a ≤ y.asIdeal) →
      ∀ z : PrimeSpectrum A, p.asIdeal ≤ z.asIdeal → a ≤ z.asIdeal →
        ((cohomologicalDimension A I I.fg_of_isNoetherianRing + 1 : ℤ) : EInt) <
          krullDimToEInt (closureLocalDimension A p z))
    (V : OpensNearVanishing A I a)
    (G F : AlgebraicGeometry.SheafOfModules.CoherentModules V.openSet.toScheme.ringCatSheaf)
    (_hG : Scheme.Modules.IsFiniteLocallyFree G.obj)
    (hF : Scheme.Modules.IsFiniteLocallyFree F.obj) :
    Function.Bijective (nbhdHomComparisonOn V G F)
```

## Tag 0EKV, a lemma

[Tag 0EKV](https://stacks.math.columbia.edu/tag/0EKV) in the Stacks Project.

**`Stacks.Algebraization.completionFullyFaithfulComplete_principal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/PrincipalFullyFaithful.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFullyFaithful/PrincipalFullyFaithful.lean#L189).

> **[Stacks, Tag 0EKV].** Let `A` be a Noetherian ring, let `f ∈ 𝔞 ⊆ A`, put
> `U = Spec(A) ∖ V(𝔞)` and let `𝒱` be the open subschemes of `U` containing `U ∩ V(f)`, ordered by
> reverse inclusion. Assume
>
> 1. `A` is complete with respect to the `f`-adic topology,
> 2. `f` is a nonzerodivisor, and
> 3. `H¹_𝔞(A/fA)` is a finite `A`-module.
>
> Then the completion functor `colim_𝒱 Coh(𝒪_V) ⟶ Coh(U, f𝒪_U)`, `ℱ ↦ ℱ^∧`, is fully faithful on
> the full subcategory of finite locally free objects.
>
> An object of `colim_𝒱 Coh(𝒪_V)` is a coherent module on *some* `V ∈ 𝒱`, and a morphism between
> two of them is an element of `colim_{W ⊆ V} Hom_{𝒪_W}(𝒢|_W, ℱ|_W)`; so the conclusion is
> `Stacks.Algebraization.NeighbourhoodCompletion.CompletionFullyFaithfulComplete`, which quantifies
> over every `V ∈ 𝒱` and all finite locally free `𝒪_V`-modules `𝒢`, `ℱ`, and asserts that
> `colim_{W ⊆ V} Hom_{𝒪_W}(𝒢|_W, ℱ|_W) ⟶ lim_n Hom_{𝒪_{Y_n}}(𝒢|_{Y_n}, ℱ|_{Y_n})` is bijective.
> The quantifier here is the tag's own — an arbitrary member `V` of `𝒱`, not the single member
> `V = U` — which matters because a finite locally free module on a small `V` need not extend to
> `U`. That is full faithfulness: an object of `Coh(U, f𝒪_U)` is an inverse system of coherent
> modules,
> `𝒢^∧` is the system `(𝒢|_{Y_n})` of restrictions to the infinitesimal neighbourhoods of
> `U ∩ V(f)`, and a morphism `𝒢^∧ ⟶ ℱ^∧` is a compatible family of morphisms of the restrictions.
>
> The source's proof is two citations: by [Stacks, Tag 0EK2] it suffices that
> `colim_𝒱 Γ(V, 𝒪_V) = lim_n Γ(U, 𝒪_U / fⁿ 𝒪_U)`, which is [Stacks, Tag 0EIH] at the module `A`.
> Both are available: the equality is `Stacks.Algebraization.isQuasiAffineComplete_principal`,
> condition (1) of [Stacks, Tag 0EK2], and the chain (1) ⇒ (2) ⇒ (3) ⇒ (4) is
> `Stacks.Algebraization.NeighbourhoodCompletion.implications_among_conditions`. No step of the
> argument needs the pair `𝒢`, `ℱ` to extend from `V` to `U`: the implication (2) ⇒ (3) embeds a
> finite locally free module on `V` into a finite direct sum of restrictions to `V` of high twists
> of the ample module `𝒪_U`, which is what carries the comparison from `U` down to `V`.

```lean
public theorem completionFullyFaithfulComplete_principal (hf : f ∈ a)
    [IsAdicComplete (Ideal.span {f}) A] (hnzd : f ∈ nonZeroDivisors A)
    (hH1 : Module.Finite A
      (localCohomologyModule A a (Ideal.fg_of_isNoetherianRing a)
        (Quot f (ModuleCat.of A A) 1) 1)) :
    NeighbourhoodCompletion.CompletionFullyFaithfulComplete (principalFormalLocusι A a f)
```

## Tag 0EIV, a lemma

[Tag 0EIV](https://stacks.math.columbia.edu/tag/0EIV) in the Stacks Project.

**`Stacks.Algebraization.NeighbourhoodHoms.sectionsNearVanishing_internalHomNear`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/NeighbourhoodHoms.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/NeighbourhoodHoms.lean#L402). The attribute's comment: “at the member V = U: the source is the colimit over the whole family”.

> **The source of the comparison of Stacks 0EIV is the colimit of the morphisms of the
> restrictions.** A section of the internal hom `SheafHom(𝒢, ℱ)` over an open neighbourhood `V`
> of the formal locus is, on the nose, a morphism `𝒢|_V ⟶ ℱ|_V` of modules on the site of opens
> below `V`. So the source of `nbhdHomComparison` is `colim_{V ∈ 𝒱} Hom_V(𝒢|_V, ℱ|_V)`.

```lean
public theorem sectionsNearVanishing_internalHomNear
    (V : OpensNearVanishing A I a) :
    ToType ((sectionsNearVanishing A I a (internalHomNear A a G F).obj).obj V) =
      ((_root_.restrFun (complementZeroLocus A a : Scheme).sheaf.obj V.openSet).obj
          G.obj.val ⟶
        (_root_.restrFun (complementZeroLocus A a : Scheme).sheaf.obj V.openSet).obj
          F.obj.val)
```

**`Stacks.Algebraization.NeighbourhoodHoms.nbhdHomComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/NeighbourhoodHoms.lean, line 422](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/NeighbourhoodHoms.lean#L422). The attribute's comment: “at V = U: the canonical map from germs of morphisms to the completions”.

> **The map of Stacks 0EIV.** The canonical map from the morphisms `𝒢|_{V'} ⟶ ℱ|_{V'}`
> defined on arbitrarily small open neighbourhoods `V'` of the formal locus `U ∩ V(I)` to the
> morphisms of the completions `𝒢^∧ ⟶ ℱ^∧` in `Coh(U, I𝒪_U)`.
>
> It is the composite of three canonical maps: the comparison of Stacks 0EG2 for the internal
> hom `H = SheafHom(𝒢, ℱ)`, which lands in the compatible families of sections of `H / Iⁿ H` on
> `U`; the identification of that limit with the limit of the global sections of the completion
> of `H`, which is `adicCompletionLimitIso` on the tower and `sectionsAbLimitIso` on sections;
> and the identification of Stacks 0882 of the latter with the morphisms of the completions.

```lean
public def nbhdHomComparison :
    ToType (colimit (C := Ab.{u})
        (sectionsNearVanishing A I a (internalHomNear A a G F).obj)) →
      ((completionFunctor (complementZeroLocus A a : Scheme)
          (idealSheafNearVanishing A I a)).obj G ⟶
        (completionFunctor (complementZeroLocus A a : Scheme)
          (idealSheafNearVanishing A I a)).obj F)
```

**`Stacks.Algebraization.nbhdHomComparisonOn_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/NeighbourhoodHomsOnBijective.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/NeighbourhoodHomsOnBijective.lean#L89).

> **Stacks 0EIV.** Let `I ⊆ 𝔞` be ideals of a Noetherian ring `A`, put `U = Spec(A) ∖ V(𝔞)` and
> let `𝒱` be the set of open subschemes of `U` containing `U ∩ V(I)`, ordered by reverse inclusion.
> Let `G`, `F` be coherent `𝒪_V`-modules for some `V ∈ 𝒱`. The map
> `colim_{V' ≥ V} Hom_{V'}(G|_{V'}, F|_{V'}) ⟶ Hom_{Coh(V, I𝒪_V)}(G^∧, F^∧)` is bijective if
>
> 1. `A` is `I`-adically complete and has a dualizing complex, and
> 2. whenever `x` is an associated point of `F` outside `V(I)` whose closure meets `V(I)` outside
>    `V(𝔞)`, every `z ∈ closure {x} ∩ V(𝔞)` has `dim(𝒪_{closure {x}, z}) > cd(A, I) + 1`.
>
> The target is the category of coherent adic systems on `V` along `I 𝒪_V`; restriction from `U`
> to `V` identifies the morphisms of completions there with those in `Coh(U, I𝒪_U)`
> (`Stacks.Algebraization.bijective_restrictCompletionHom`), the terms being supported in
> `U ∩ V(I) ⊆ V`.

```lean
theorem nbhdHomComparisonOn_bijective (hIa : I ≤ a) (hcomplete : IsAdicComplete I A)
    (hdualizing : ∃ K : DerivedCategory (ModuleCat.{u} A), Dualizing.IsDualizingComplex K)
    (V : OpensNearVanishing A I a)
    (G F : AlgebraicGeometry.SheafOfModules.CoherentModules V.openSet.toScheme.ringCatSheaf)
    (hdim : AssociatedPointsClosureDimensionBoundOn V F.obj) :
    Function.Bijective (nbhdHomComparisonOn V G F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.15, Tag 0EKN](https://stacks.math.columbia.edu/tag/0EKN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
