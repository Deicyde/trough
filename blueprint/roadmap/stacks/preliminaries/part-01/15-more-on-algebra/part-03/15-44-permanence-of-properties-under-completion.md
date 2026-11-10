---
declaration: section
origin: cited
lean: AdicCompletion.noetherian_completeLocal_faithfullyFlat, ringKrullDim_adicCompletion_maximalIdeal, depth_adicCompletion_maximalIdeal, isMaximalCohenMacaulay_iff_adicCompletion_maximalIdeal, isRegularLocalRing_iff_adicCompletion_maximalIdeal, isDiscreteValuationRing_iff_adicCompletion_maximalIdeal, reducedness_and_adicCompletion, isNormalRing_of_isNormalRing_adicCompletion
statement: formalized
proof: formalized
---

# 15.44 Permanence of properties under completion

Section 15.44 of the Stacks Project, [Tag 07NU](https://stacks.math.columbia.edu/tag/07NU). 10 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07NU, the section

[Tag 07NU](https://stacks.math.columbia.edu/tag/07NU) in the Stacks Project.

**`AdicCompletion.noetherian_completeLocal_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/PermanenceUnderCompletion.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AdicCompletion/PermanenceUnderCompletion.lean#L34). The attribute's comment: “the completion of a Noetherian local ring”.

> The completion of a Noetherian local ring `(A, 𝔪)` is a Noetherian local ring with maximal
> ideal `𝔪 A^∧`, complete with respect to it, and faithfully flat over `A`.

```lean
theorem noetherian_completeLocal_faithfullyFlat (A : Type*) [CommRing A] [IsNoetherianRing A]
    [IsLocalRing A] :
    IsNoetherianRing (AdicCompletion (maximalIdeal A) A) ∧
      IsLocalRing (AdicCompletion (maximalIdeal A) A) ∧
      maximalIdeal (AdicCompletion (maximalIdeal A) A) =
        (maximalIdeal A).map (algebraMap A (AdicCompletion (maximalIdeal A) A)) ∧
      IsAdicComplete (maximalIdeal (AdicCompletion (maximalIdeal A) A))
        (AdicCompletion (maximalIdeal A) A) ∧
      Module.FaithfullyFlat A (AdicCompletion (maximalIdeal A) A)
```

## Tag 07NV, a lemma

[Tag 07NV](https://stacks.math.columbia.edu/tag/07NV) in the Stacks Project.

**`ringKrullDim_adicCompletion_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/PermanenceOfProperties.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AdicCompletion/PermanenceOfProperties.lean#L306). References: EGA IV (7.3.19), “partial”.

> **Stacks 07NV.** A Noetherian local ring and its completion at the maximal ideal have the
> same Krull dimension.

```lean
public theorem ringKrullDim_adicCompletion_maximalIdeal {A : Type*} [CommRing A]
    [IsNoetherianRing A] [IsLocalRing A] :
    ringKrullDim A = ringKrullDim (AdicCompletion (maximalIdeal A) A)
```

## Tag 07NW, a lemma

[Tag 07NW](https://stacks.math.columbia.edu/tag/07NW) in the Stacks Project.

**`depth_adicCompletion_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/PermanenceOfProperties.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AdicCompletion/PermanenceOfProperties.lean#L372).

> **Stacks 07NW.** A Noetherian local ring and its completion at the maximal ideal have the
> same depth.

```lean
public theorem depth_adicCompletion_maximalIdeal {A : Type*} [CommRing A]
    [IsNoetherianRing A] [IsLocalRing A] :
    Module.depth A (maximalIdeal A) A =
      Module.depth (AdicCompletion (maximalIdeal A) A)
        (maximalIdeal (AdicCompletion (maximalIdeal A) A))
        (AdicCompletion (maximalIdeal A) A)
```

## Tag 07NX, a lemma

[Tag 07NX](https://stacks.math.columbia.edu/tag/07NX) in the Stacks Project.

**`isMaximalCohenMacaulay_iff_adicCompletion_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/PermanenceOfProperties.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AdicCompletion/PermanenceOfProperties.lean#L397).

> **Stacks 07NX.** A Noetherian local ring is Cohen–Macaulay if and only if its completion at
> the maximal ideal is Cohen–Macaulay.

```lean
public theorem isMaximalCohenMacaulay_iff_adicCompletion_maximalIdeal {A : Type*} [CommRing A]
    [IsNoetherianRing A] [IsLocalRing A] :
    Module.IsMaximalCohenMacaulay A A ↔
      Module.IsMaximalCohenMacaulay (AdicCompletion (IsLocalRing.maximalIdeal A) A)
        (AdicCompletion (IsLocalRing.maximalIdeal A) A)
```

## Tag 07NY, a lemma

[Tag 07NY](https://stacks.math.columbia.edu/tag/07NY) in the Stacks Project.

**`isRegularLocalRing_iff_adicCompletion_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/PermanenceOfProperties.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AdicCompletion/PermanenceOfProperties.lean#L419). References: EGA 0 (17.1.5); EGA 0 (17.3.8.1), “local, J = maximal ideal”.

> **Stacks 07NY.** A Noetherian local ring is regular if and only if its completion at the
> maximal ideal is regular.

```lean
public theorem isRegularLocalRing_iff_adicCompletion_maximalIdeal {A : Type*} [CommRing A]
    [IsNoetherianRing A] [IsLocalRing A] :
    IsRegularLocalRing A ↔
      IsRegularLocalRing (AdicCompletion (IsLocalRing.maximalIdeal A) A)
```

## Tag 0AP1, a lemma

[Tag 0AP1](https://stacks.math.columbia.edu/tag/0AP1) in the Stacks Project.

**`isDiscreteValuationRing_iff_adicCompletion_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/PermanenceOfProperties.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AdicCompletion/PermanenceOfProperties.lean#L440).

> **Stacks 0AP1.** A Noetherian local ring is a discrete valuation ring if and only if its
> completion at the maximal ideal is a discrete valuation ring.

```lean
public theorem isDiscreteValuationRing_iff_adicCompletion_maximalIdeal {A : Type*} [CommRing A]
    [IsNoetherianRing A] [IsLocalRing A] :
    (∃ _ : IsDomain A, IsDiscreteValuationRing A) ↔
      ∃ _ : IsDomain (AdicCompletion (IsLocalRing.maximalIdeal A) A),
        IsDiscreteValuationRing (AdicCompletion (IsLocalRing.maximalIdeal A) A)
```

## Tag 07NZ, a lemma

[Tag 07NZ](https://stacks.math.columbia.edu/tag/07NZ) in the Stacks Project.

**`reducedness_and_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/PermanenceOfProperties.lean, line 515](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AdicCompletion/PermanenceOfProperties.lean#L515). References: EGA IV (7.6.1), “more general”.

> **Stacks 07NZ.** For a Noetherian local ring `A`, a reduced completion forces `A` to be
> reduced. The converse fails, even for a Noetherian local domain. If `A` is Nagata, then `A` is
> reduced if and only if its completion is reduced.

```lean
public theorem reducedness_and_adicCompletion (A : Type u) [CommRing A] [IsLocalRing A]
    [IsNoetherianRing A] :
    (IsAnalyticallyUnramified A → IsReduced A) ∧
      (∃ (B : Type v) (_ : CommRing B) (_ : IsLocalRing B) (_ : IsNoetherianRing B)
        (_ : IsDomain B), ¬ IsAnalyticallyUnramified B) ∧
      (IsNagataRing A → (IsReduced A ↔ IsAnalyticallyUnramified A))
```

## Tag 0FIZ, a lemma

[Tag 0FIZ](https://stacks.math.columbia.edu/tag/0FIZ) in the Stacks Project.

**`isNormalRing_of_isNormalRing_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/PermanenceOfProperties.lean, line 547](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AdicCompletion/PermanenceOfProperties.lean#L547).

> A Noetherian local ring is normal if its completion at the maximal ideal is normal.

```lean
public theorem isNormalRing_of_isNormalRing_adicCompletion
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hA : IsNormalRing (AdicCompletion (IsLocalRing.maximalIdeal A) A)) :
    IsNormalRing A
```

## Tag 0C4G, a lemma

[Tag 0C4G](https://stacks.math.columbia.edu/tag/0C4G) in the Stacks Project.

**`adicCompletionMap_flat_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/PermanenceOfProperties.lean, line 684](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AdicCompletion/PermanenceOfProperties.lean#L684). References: SGA 3 VIIB (1.3.4), “partial”.

> **Stacks 0C4G.** A local homomorphism of Noetherian local rings is flat if and only if the
> induced homomorphism between their completions at the maximal ideals is flat.

```lean
public theorem adicCompletionMap_flat_iff {A : Type u} {B : Type v}
    [CommRing A] [CommRing B] [IsLocalRing A] [IsLocalRing B]
    [IsNoetherianRing A] [IsNoetherianRing B] (f : A →+* B) [IsLocalHom f] :
    (adicCompletionMap f (IsLocalRing.maximalIdeal A) (IsLocalRing.maximalIdeal B)
      (IsLocalRing.map_maximalIdeal_le f)).Flat ↔ f.Flat
```

## Tag 0AGX, a lemma

[Tag 0AGX](https://stacks.math.columbia.edu/tag/0AGX) in the Stacks Project.

**`exists_adicCompletion_ringEquiv_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/PermanenceOfProperties.lean, line 784](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AdicCompletion/PermanenceOfProperties.lean#L784).

> **Stacks 0AGX.** A flat local homomorphism which identifies the maximal ideals and induces an
> isomorphism of residue fields induces an isomorphism of adic completions.

```lean
public theorem exists_adicCompletion_ringEquiv_of_flat
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [IsLocalRing A] [IsLocalRing B]
    [Algebra A B] [IsLocalHom (algebraMap A B)] [Module.Flat A B]
    (hfg : (maximalIdeal A).FG)
    (hmax : (maximalIdeal A).map (algebraMap A B) = maximalIdeal B)
    (hres : Function.Bijective (ResidueField.map (algebraMap A B))) :
    ∃ e : AdicCompletion (maximalIdeal A) A ≃+* AdicCompletion (maximalIdeal B) B,
      ∀ a : A,
        e (algebraMap A (AdicCompletion (maximalIdeal A) A) a) =
          algebraMap B (AdicCompletion (maximalIdeal B) B) (algebraMap A B a)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.44, Tag 07NU](https://stacks.math.columbia.edu/tag/07NU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
