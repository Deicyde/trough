---
declaration: section
origin: cited
lean: Algebra.FormallyUnramified, Algebra.FormallyUnramified.iff_comp_injective, Algebra.FormallyUnramified.base_change, Algebra.forall_comp_injective_iff_subsingleton_kaehlerDifferential, formally_unramified_local, Algebra.FormallyUnramified.localization_map, Algebra.FormallyUnramified.of_isLocalization, Algebra.FormallyUnramified.directLimit
statement: formalized
proof: formalized
---

# 10.148 Formally unramified maps

Section 10.148 of the Stacks Project, [Tag 00UM](https://stacks.math.columbia.edu/tag/00UM). 6 tags here are carried by 3 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00UN, a definition

[Tag 00UN](https://stacks.math.columbia.edu/tag/00UN) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.FormallyUnramified`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.FormallyUnramified#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Unramified/Basic.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Basic.lean#L44) (StacksFrontier): “formally unramified ring maps”. References: EGA IV (17.1.1); EGA 0 (19.10.2), “discrete, unramified”; SGA 3 XI (1.1); SGA 3 XI (1.6), “affine case, unramified”.
- [`Algebra.FormallyUnramified.iff_comp_injective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.FormallyUnramified.iff_comp_injective#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Unramified/Basic.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Basic.lean#L49) (StacksFrontier): “at most one dotted arrow, as injectivity of post-composition”. References: EGA 0 (19.10.4), “partial, special case”; EGA IV (17.1.1), “special case”; EGA 0 (19.10.2), “discrete, unramified”; SGA 3 XI (1.1), “partial”; SGA 3 XI (1.6), “affine case, unramified”.

## Tag 0H91, a lemma

[Tag 0H91](https://stacks.math.columbia.edu/tag/0H91) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.FormallyUnramified.base_change`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.FormallyUnramified.base_change#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Unramified/Basic.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Basic.lean#L73) (StacksFrontier): “formal unramifiedness is stable under base change”. References: EGA IV (17.1.3), “(iii), special case”; EGA IV (17.7.3), “(i), (ii)”; SGA 3 XI (1.6), “partial”.

## Tag 00UO, a lemma

[Tag 00UO](https://stacks.math.columbia.edu/tag/00UO) in the Stacks Project.

**`Algebra.forall_comp_injective_iff_subsingleton_kaehlerDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Basic.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Basic.lean#L207). The attribute's comment: “(1) is the lifting property of Definition 00UN, stated as injectivity of `Hom_R(S, A) → Hom_R(S, A/I)` for every `R`-algebra `A` in the universe of `S` and every ideal `I` with `I ^ 2 = ⊥`; (2) is `Subsingleton Ω[S⁄R]`. Proved from Mathlib's `Algebra.FormallyUnramified.iff_comp_injective`.”.

> **Stacks 00UO.** Let `R → S` be a ring map. Then `R → S` is formally unramified in the sense
> of Definition 00UN — for every `R`-algebra `A` and every ideal `I` of `A` with `I² = 0`, the map
> `Hom_R(S, A) → Hom_R(S, A/I)` given by composition with the quotient map is injective — if and
> only if the module of differentials `Ω_{S/R}` is zero.

```lean
theorem Algebra.forall_comp_injective_iff_subsingleton_kaehlerDifferential
    (R : Type*) (S : Type u) [CommRing R] [CommRing S] [Algebra R S] :
    (∀ ⦃A : Type u⦄ [CommRing A] [Algebra R A] (I : Ideal A), I ^ 2 = ⊥ →
      Function.Injective ((Ideal.Quotient.mkₐ R I).comp : (S →ₐ[R] A) → S →ₐ[R] A ⧸ I)) ↔
      Subsingleton Ω[S⁄R]
```

## Tag 04E8, a lemma

[Tag 04E8](https://stacks.math.columbia.edu/tag/04E8) in the Stacks Project.

**`formally_unramified_local`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Basic.lean, line 312](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Basic.lean#L312). References: EGA IV (17.4.2), “Affine case of a ⇔ e”.

> Formally unramified is a local property: for a ring map `R → S`, being formally
> unramified is equivalent to all the localized maps `R → S_𝔮` being formally
> unramified, which in turn is equivalent to all the maps `R_𝔭 → S_𝔮` (with
> `𝔭 = R ∩ 𝔮`) being formally unramified.

```lean
theorem formally_unramified_local
    (R S : Type*) [CommRing R] [CommRing S] [Algebra R S] :
    List.TFAE
      [ Algebra.FormallyUnramified R S,
        ∀ (𝔮 : Ideal S) [𝔮.IsPrime],
          Algebra.FormallyUnramified R (Localization.AtPrime 𝔮),
        ∀ (𝔮 : Ideal S) [𝔮.IsPrime],
          haveI : (𝔮.comap (algebraMap R S)).IsPrime := Ideal.IsPrime.comap _
          haveI : 𝔮.LiesOver (𝔮.comap (algebraMap R S)) := ⟨rfl⟩
          haveI : Algebra (Localization.AtPrime (𝔮.comap (algebraMap R S)))
              (Localization.AtPrime 𝔮) := Localization.AtPrime.algebraOfLiesOver _ 𝔮
          Algebra.FormallyUnramified
            (Localization.AtPrime (𝔮.comap (algebraMap R S)))
            (Localization.AtPrime 𝔮) ]
```

## Tag 04E9, a lemma

[Tag 04E9](https://stacks.math.columbia.edu/tag/04E9) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.FormallyUnramified.localization_map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.FormallyUnramified.localization_map#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Unramified/Basic.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Basic.lean#L67) (StacksFrontier): “(1)”.
- [`Algebra.FormallyUnramified.of_isLocalization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.FormallyUnramified.of_isLocalization#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Unramified/Basic.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Basic.lean#L68) (StacksFrontier): “(2), together with `Algebra.FormallyUnramified.comp`”. References: EGA 0 (19.10.3), “partial”.

## Tag 07QE, a lemma

[Tag 07QE](https://stacks.math.columbia.edu/tag/07QE) in the Stacks Project.

**`Algebra.FormallyUnramified.directLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Basic.lean, line 458](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Unramified/Basic.lean#L458).

> **Concrete `Ring.DirectLimit` form.** Equip the direct limit
> `Ring.DirectLimit S φ` of a directed system of `R`-algebras with its canonical
> `R`-algebra structure `directLimitAlgebra φ`. If every `S i` is formally unramified
> over `R`, then so is the direct limit. (No extra compatibility hypothesis is needed:
> the canonical maps `Ring.DirectLimit.of … i` are automatically `R`-algebra
> homomorphisms, cf. `Ring.DirectLimit.of_commutes`.)

```lean
theorem Algebra.FormallyUnramified.directLimit
    [DirectedSystem S (fun i j h => (φ i j h : S i → S j))]
    (hunram : ∀ i, Algebra.FormallyUnramified R (S i)) :
    letI := directLimitAlgebra φ
    Algebra.FormallyUnramified R (Ring.DirectLimit S (fun i j h => (φ i j h : S i → S j)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.148, Tag 00UM](https://stacks.math.columbia.edu/tag/00UM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
