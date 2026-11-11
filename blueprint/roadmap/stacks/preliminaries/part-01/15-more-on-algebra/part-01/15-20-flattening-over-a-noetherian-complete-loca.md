---
declaration: section
origin: cited
lean: Module.FlatAfterQuotientAlong, Module.exists_least_flattening_ideal, Module.flatAlongZeroLocus_baseChange_iff_map_eq_bot, Module.flatAlongZeroLocus_baseChange_iff_map_eq_bot_of_finiteType
statement: formalized
proof: formalized
---

# 15.20 Flattening over a Noetherian complete local ring

Section 15.20 of the Stacks Project, [Tag 05LV](https://stacks.math.columbia.edu/tag/05LV). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0526, a lemma

[Tag 0526](https://stacks.math.columbia.edu/tag/0526) in the Stacks Project.

**`Module.FlatAfterQuotientAlong`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/CompleteLocal.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/CompleteLocal.lean#L50). The attribute's comment: “the property (15.20.1) quantified over in the statement”.

> Flatness along the inverse image of `V(m)` after quotienting `R`, `S` and `M` by the ideal
> `I` of `R`. Here `(S / IS) ⊗[S] M` is the canonical model of `M / IM`.

```lean
abbrev Module.FlatAfterQuotientAlong
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
    (M : Type w) [AddCommGroup M] [Module S M] (m I : Ideal R) : Prop
```

**`Module.exists_least_flattening_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/CompleteLocal.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/CompleteLocal.lean#L352).

> Over a complete Noetherian local ring, there is a least ideal contained in the maximal ideal
> such that the quotient module is flat at every prime lying over the maximal ideal.

```lean
theorem Module.exists_least_flattening_ideal
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
    [IsLocalRing R] [IsNoetherianRing R]
    [IsAdicComplete (IsLocalRing.maximalIdeal R) R]
    (M : Type w) [AddCommGroup M] [Module S M] [Module.Finite S M]
    [IsNoetherianRing S] :
    ∃ I : Ideal R,
      I ≤ IsLocalRing.maximalIdeal R ∧
        Module.FlatAfterQuotientAlong R S M (IsLocalRing.maximalIdeal R) I ∧
          ∀ J : Ideal R,
            Module.FlatAfterQuotientAlong R S M (IsLocalRing.maximalIdeal R) J → I ≤ J
```

## Tag 0527, a lemma

[Tag 0527](https://stacks.math.columbia.edu/tag/0527) in the Stacks Project.

**`Module.flatAlongZeroLocus_baseChange_iff_map_eq_bot`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/CompleteLocal.lean, line 473](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/CompleteLocal.lean#L473).

> For the least ideal making the indicated quotient of `M` flat along the closed point, a local
> map from `R` to a Noetherian local ring `R'` annihilates that ideal exactly when the base change
> of `M` is flat along the closed point of `R'`.

```lean
lemma Module.flatAlongZeroLocus_baseChange_iff_map_eq_bot
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
    [IsLocalRing R] [IsNoetherianRing R]
    (M : Type w) [AddCommGroup M] [Module S M]
    (I : Ideal R)
    (hI_flat : Module.FlatAfterQuotientAlong
      R S M (IsLocalRing.maximalIdeal R) I)
    (hI_min : ∀ J : Ideal R,
      Module.FlatAfterQuotientAlong R S M (IsLocalRing.maximalIdeal R) J → I ≤ J)
    (R' : Type x) [CommRing R'] [IsLocalRing R'] [IsNoetherianRing R']
    [Algebra R R'] [IsLocalHom (algebraMap R R')] :
    Module.FlatAlongZeroLocus R' (S ⊗[R] R')
        (IsLocalRing.maximalIdeal R') ((S ⊗[R] R') ⊗[S] M) ↔
      I.map (algebraMap R R') = ⊥
```

## Tag 0528, a lemma

[Tag 0528](https://stacks.math.columbia.edu/tag/0528) in the Stacks Project.

**`Module.flatAlongZeroLocus_baseChange_iff_map_eq_bot_of_finiteType`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/CompleteLocal.lean, line 1084](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/CompleteLocal.lean#L1084).

> For the least ideal making the indicated quotient of `M` flat along the closed point, a local
> map from `R` to an arbitrary local ring `R'` annihilates that ideal exactly when the base change
> of `M` is flat along the closed point, provided `S` is of finite type over the Noetherian local
> ring `R` and `M` is finite over `S`. No Noetherian hypothesis is imposed on `R'`.

```lean
lemma Module.flatAlongZeroLocus_baseChange_iff_map_eq_bot_of_finiteType
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
    [IsLocalRing R] [IsNoetherianRing R] [Algebra.FiniteType R S]
    (M : Type w) [AddCommGroup M] [Module S M] [Module.Finite S M]
    (I : Ideal R)
    (hI_flat : Module.FlatAfterQuotientAlong
      R S M (IsLocalRing.maximalIdeal R) I)
    (hI_min : ∀ J : Ideal R,
      Module.FlatAfterQuotientAlong R S M (IsLocalRing.maximalIdeal R) J → I ≤ J)
    (R' : Type x) [CommRing R'] [IsLocalRing R']
    [Algebra R R'] [IsLocalHom (algebraMap R R')] :
    Module.FlatAlongZeroLocus R' (S ⊗[R] R')
        (IsLocalRing.maximalIdeal R') ((S ⊗[R] R') ⊗[S] M) ↔
      I.map (algebraMap R R') = ⊥
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.20, Tag 05LV](https://stacks.math.columbia.edu/tag/05LV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
