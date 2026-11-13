---
declaration: section
origin: cited
lean: Stacks.PureModules.associatedPrime_add_map_maximalIdeal_ne_top, Stacks.PureModules.associatedPrime_add_map_ne_top_of_isAdicComplete, Stacks.PureModules.associatedPrime_add_map_maximalIdeal_ne_top_of_directSum_finite, Stacks.PureModules.associatedPrime_add_map_maximalIdeal_ne_top_of_countable_mittagLeffler
statement: formalized
proof: formalized
---

# 38.14 Examples of relatively pure modules

Section 38.14 of the Stacks Project, [Tag 05IS](https://stacks.math.columbia.edu/tag/05IS). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05FV, a lemma

[Tag 05FV](https://stacks.math.columbia.edu/tag/05FV) in the Stacks Project.

**`Stacks.PureModules.associatedPrime_add_map_maximalIdeal_ne_top`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/ClosedFibreAssociatedPrimes.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/ClosedFibreAssociatedPrimes.lean#L77).

> **Stacks Project, Tag 05FV.** Under the finite Noetherian closed-fibre hypotheses, an
> associated prime of any fibre of a projective module meets the closed fibre of a local base.

```lean
lemma associatedPrime_add_map_maximalIdeal_ne_top
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S] [IsLocalRing R]
    (N : Type w) [AddCommGroup N] [Module S N] [Module R N] [IsScalarTower R S N]
    [Module.Projective R N]
    [IsNoetherianRing (S ⧸ (IsLocalRing.maximalIdeal R).map (algebraMap R S))]
    [Module.Finite (S ⧸ (IsLocalRing.maximalIdeal R).map (algebraMap R S))
      (N ⧸ ((IsLocalRing.maximalIdeal R).map (algebraMap R S) • (⊤ : Submodule S N)))]
    (q : PrimeSpectrum S)
    (hq : IsAssociatedPrimeStacks S
      (N ⊗[R] (PrimeSpectrum.comap (algebraMap R S) q).asIdeal.ResidueField) q.asIdeal) :
    q.asIdeal + (IsLocalRing.maximalIdeal R).map (algebraMap R S) ≠ ⊤
```

## Tag 05IT, a lemma

[Tag 05IT](https://stacks.math.columbia.edu/tag/05IT) in the Stacks Project.

**`Stacks.PureModules.associatedPrime_add_map_ne_top_of_isAdicComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/AdicComplete.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/AdicComplete.lean#L49).

> **Stacks Project, Tag 05IT.** An associated prime of the tensor product of an adically
> complete module with any base module is not comaximal with the ideal of completion.

```lean
theorem associatedPrime_add_map_ne_top_of_isAdicComplete
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
    (I : Ideal R) (N : Type w) [AddCommGroup N] [Module R N] [Module S N]
    [IsScalarTower R S N] [IsAdicComplete I N]
    (M : Type x) [AddCommGroup M] [Module R M]
    (q : Ideal S) (hq : IsAssociatedPrimeStacks S (N ⊗[R] M) q) :
    q + I.map (algebraMap R S) ≠ ⊤
```

## Tag 05IU, a lemma

[Tag 05IU](https://stacks.math.columbia.edu/tag/05IU) in the Stacks Project.

**`Stacks.PureModules.associatedPrime_add_map_maximalIdeal_ne_top_of_directSum_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/MittagLeffler.lean, line 325](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/MittagLeffler.lean#L325).

> **Stacks Project, Tag 05IU.** An associated prime of a tensor product of a direct sum of
> finite modules cannot be comaximal with the closed fibre of a local base ring.

```lean
theorem associatedPrime_add_map_maximalIdeal_ne_top_of_directSum_finite
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [IsLocalRing R] [Algebra R S]
    (N : Type w) [AddCommGroup N] [Module R N] [Module S N] [IsScalarTower R S N]
    (ι : Type x) (F : ι → Type y)
    [∀ i, AddCommGroup (F i)] [∀ i, Module R (F i)]
    (hF : ∀ i, Module.Finite R (F i))
    (e : N ≃ₗ[R] ⨁ i, F i)
    (M : Type z) [AddCommGroup M] [Module R M]
    (q : Ideal S) (hq : IsAssociatedPrimeStacks S (N ⊗[R] M) q) :
    q + (IsLocalRing.maximalIdeal R).map (algebraMap R S) ≠ ⊤
```

## Tag 05IV, a lemma

[Tag 05IV](https://stacks.math.columbia.edu/tag/05IV) in the Stacks Project.

**`Stacks.PureModules.associatedPrime_add_map_maximalIdeal_ne_top_of_countable_mittagLeffler`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/MittagLeffler.lean, line 388](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/MittagLeffler.lean#L388).

> **Stacks Project, Tag 05IV.** An associated prime of a tensor product of a countably
> generated Mittag-Leffler module over a henselian local ring cannot be comaximal with the
> closed fibre.

```lean
theorem associatedPrime_add_map_maximalIdeal_ne_top_of_countable_mittagLeffler
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [HenselianLocalRing R]
    [Algebra R S]
    (N : Type w) [AddCommGroup N] [Module R N] [Module S N] [IsScalarTower R S N]
    [Small.{w} R]
    (hcg : ∃ t : Set N, t.Countable ∧ Submodule.span R t = ⊤)
    (hML : IsMittagLeffler.{u, w, w, w, w} R N)
    (M : Type x) [AddCommGroup M] [Module R M]
    (q : Ideal S) (hq : IsAssociatedPrimeStacks S (N ⊗[R] M) q) :
    q + (IsLocalRing.maximalIdeal R).map (algebraMap R S) ≠ ⊤
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.14, Tag 05IS](https://stacks.math.columbia.edu/tag/05IS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
