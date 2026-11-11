---
declaration: section
origin: cited
lean: RingHom.IsEtaleLocalHom, Algebra.isEtaleAt_iff_isEtaleLocalHom, RingHom.isEtaleLocalHom_iff_isEtaleLocalHom_adicCompletion, RingHom.isEtaleLocalHom_adicCompletion_iff_etale_adicCompletion, RingHom.exists_linearEquiv_fin_adicCompletion_of_isEtaleLocalHom, AlgebraicGeometry.IsEtaleAt, AlgebraicGeometry.etale_iff_forall_isEtaleAt, AlgebraicGeometry.Etale
statement: formalized
proof: formalized
---

# 41.11 Étale morphisms

Section 41.11 of the Stacks Project, [Tag 0257](https://stacks.math.columbia.edu/tag/0257). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0258, a definition

[Tag 0258](https://stacks.math.columbia.edu/tag/0258) in the Stacks Project.

**`RingHom.IsEtaleLocalHom`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/EtaleLocalHom.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/EtaleLocalHom.lean#L57). References: SGA 1 I (4.1), “special case”; SGA 1 III (1.2), “partial”.

> A local homomorphism between Noetherian local rings is étale if it is flat, formally
> unramified, and essentially of finite type.

```lean
abbrev IsEtaleLocalHom {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B] [IsLocalRing A] [IsLocalRing B]
    (f : A →+* B) [IsLocalHom f] : Prop
```

## Tag 039L, a lemma

[Tag 039L](https://stacks.math.columbia.edu/tag/039L) in the Stacks Project.

**`Algebra.isEtaleAt_iff_isEtaleLocalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/EtaleLocalHom.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/EtaleLocalHom.lean#L104).

> A finite type algebra over a Noetherian ring is étale at a prime if and only if the induced
> map between the local rings at the corresponding primes is an étale local homomorphism.

```lean
theorem isEtaleAt_iff_isEtaleLocalHom
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [Algebra A B] [Algebra.FiniteType A B] [IsNoetherianRing A]
    (p : Ideal A) [p.IsPrime] (q : Ideal B) [q.IsPrime] [q.LiesOver p] :
    Algebra.IsEtaleAt A q ↔
      letI : IsNoetherianRing B := Algebra.FiniteType.isNoetherianRing A B
      letI : IsNoetherianRing (Localization.AtPrime p) :=
        IsLocalization.isNoetherianRing p.primeCompl _ inferInstance
      letI : IsNoetherianRing (Localization.AtPrime q) :=
        IsLocalization.isNoetherianRing q.primeCompl _ inferInstance
      RingHom.IsEtaleLocalHom
        (Localization.localRingHom p q (algebraMap A B) Ideal.LiesOver.over)
```

## Tag 039M, a lemma

[Tag 039M](https://stacks.math.columbia.edu/tag/039M) in the Stacks Project.

**`RingHom.isEtaleLocalHom_iff_isEtaleLocalHom_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/CompletionCriteria.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/CompletionCriteria.lean#L318). The attribute's comment: “parts (1) and (2)”. References: EGA IV (17.6.3), “a) <=> e)”; SGA 1 I (4.2), “special case”.

> **Stacks Project, Tag 039M**, parts (1) and (2). An essentially finite type local
> homomorphism of Noetherian local rings is étale if and only if the induced homomorphism of
> completions is étale.

```lean
theorem isEtaleLocalHom_iff_isEtaleLocalHom_adicCompletion
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B] (f : A →+* B) [IsLocalHom f] (hft : f.EssFiniteType) :
    letI := AdicCompletion.isLocalHom_adicCompletionMap f
    IsEtaleLocalHom f ↔
      IsEtaleLocalHom
        (adicCompletionMap f (maximalIdeal A) (maximalIdeal B) (map_maximalIdeal_le f))
```

**`RingHom.isEtaleLocalHom_adicCompletion_iff_etale_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/CompletionCriteria.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/CompletionCriteria.lean#L349). The attribute's comment: “parts (2) and (3)”.

> **Stacks Project, Tag 039M**, parts (2) and (3). For the completion of an essentially finite
> type local homomorphism of Noetherian local rings, étaleness as a homomorphism of local rings
> agrees with étaleness as an algebra.

```lean
theorem isEtaleLocalHom_adicCompletion_iff_etale_adicCompletion
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B] (f : A →+* B) [IsLocalHom f] (hft : f.EssFiniteType) :
    letI := AdicCompletion.isLocalHom_adicCompletionMap f
    IsEtaleLocalHom
        (adicCompletionMap f (maximalIdeal A) (maximalIdeal B) (map_maximalIdeal_le f)) ↔
      (letI := (adicCompletionMap f (maximalIdeal A) (maximalIdeal B)
        (map_maximalIdeal_le f)).toAlgebra
       Algebra.Etale
         (AdicCompletion (maximalIdeal A) A) (AdicCompletion (maximalIdeal B) B))
```

**`RingHom.exists_linearEquiv_fin_adicCompletion_of_isEtaleLocalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/CompletionCriteria.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleBasics/CompletionCriteria.lean#L391). The attribute's comment: “finite free conclusion”. References: EGA IV (17.6.3), “e') freeness”.

> **Stacks Project, Tag 039M.** The completion of the target of an étale local homomorphism of
> Noetherian local rings is a finite free module of positive rank over the completion of the
> source.

```lean
theorem exists_linearEquiv_fin_adicCompletion_of_isEtaleLocalHom
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B] (f : A →+* B) [IsLocalHom f] (hf : IsEtaleLocalHom f) :
    letI := (adicCompletionMap f (maximalIdeal A) (maximalIdeal B)
      (map_maximalIdeal_le f)).toAlgebra
    ∃ n : ℕ, 0 < n ∧ Nonempty
      (AdicCompletion (maximalIdeal B) B ≃ₗ[AdicCompletion (maximalIdeal A) A]
        (Fin n → AdicCompletion (maximalIdeal A) A))
```

## Tag 0259, a definition

[Tag 0259](https://stacks.math.columbia.edu/tag/0259) in the Stacks Project.

**`AlgebraicGeometry.IsEtaleAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/EtaleAt.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/EtaleAt.lean#L57). The attribute's comment: “étale at a point”. References: SGA 1 I (4.1), “loc. Noetherian base”.

> A locally finite type morphism over a locally Noetherian scheme is étale at
> `x` when the induced local homomorphism on stalks is étale.

```lean
abbrev IsEtaleAt {X Y : Scheme.{u}} (f : X ⟶ Y) (x : X)
    [LocallyOfFiniteType f] [IsLocallyNoetherian Y] : Prop
```

**`AlgebraicGeometry.etale_iff_forall_isEtaleAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/EtaleAt.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/EtaleAt.lean#L72). The attribute's comment: “global étaleness is étaleness at every point”. References: SGA 1 I (4.1), “loc. Noetherian base”.

> Over a locally Noetherian scheme, a locally finite type morphism is étale
> if and only if it is étale at each point in the local-ring sense.

```lean
theorem etale_iff_forall_isEtaleAt {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] [IsLocallyNoetherian Y] :
    AlgebraicGeometry.Etale f ↔ ∀ x : X, IsEtaleAt f x
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Etale`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Etale#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/EtaleAt.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/EtaleAt.lean#L62) (StacksFrontier): “étale morphism”. References: EGA IV (17.3.1); SGA 1 I (4.1); SGA 3 XI (1.1); SGA 3 XI (1.6); SGA 4 VII (1.1).

## Tag 039N, a lemma

[Tag 039N](https://stacks.math.columbia.edu/tag/039N) in the Stacks Project.

**`AlgebraicGeometry.isEtaleAt_iff_etaleAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/EtaleAt.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/EtaleAt.lean#L129).

> **Stacks Project, Tag 039N.** For a morphism locally of finite type over a locally
> Noetherian scheme, étaleness of the induced map of local rings at `x` is equivalent to
> étaleness on suitable affine neighbourhoods of `x` and its image.

```lean
theorem isEtaleAt_iff_etaleAt {X Y : Scheme.{u}} (f : X ⟶ Y) (x : X)
    [LocallyOfFiniteType f] [IsLocallyNoetherian Y] :
    IsEtaleAt f x ↔ EtaleAt f x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 41.11, Tag 0257](https://stacks.math.columbia.edu/tag/0257)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
