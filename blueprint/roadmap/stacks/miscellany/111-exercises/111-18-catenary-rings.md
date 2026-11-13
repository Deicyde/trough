---
declaration: section
origin: cited
lean: Ideal.ringKrullDim_quotient_localization_eq_height_map, Ring.IsHeightCatenary, IsLocalization.AtPrime.ringKrullDim_eq_height, TopologicalSpace.IsTopologicallyCatenary, Ring.isHeightCatenary_iff_isCatenary
statement: formalized
proof: formalized
---

# 111.18 Catenary rings

Section 111.18 of the Stacks Project, [Tag 027N](https://stacks.math.columbia.edu/tag/027N). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 027O, a definition

[Tag 027O](https://stacks.math.columbia.edu/tag/027O) in the Stacks Project.

**`Ideal.ringKrullDim_quotient_localization_eq_height_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Exercises/Catenary.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Exercises/Catenary.lean#L57). The attribute's comment: “relative\_height”. References: EGA 0 (16.1.3), “(16.1.3.2)”; EGA 0 (16.3.1), “more general”.

> For `q ≤ p` with `p` prime, the Krull dimension of `Aₚ/qAₚ` is the height of the prime
> ideal `p/q` of `A/q`.

```lean
theorem ringKrullDim_quotient_localization_eq_height_map
    {A : Type*} [CommRing A] (q p : Ideal A) [p.IsPrime] (hqp : q ≤ p) :
    ringKrullDim
        (Localization.AtPrime p ⧸ q.map (algebraMap A (Localization.AtPrime p))) =
      ((p.map (Ideal.Quotient.mk q)).height : WithBot ℕ∞)
```

**`Ring.IsHeightCatenary`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Exercises/Catenary.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Exercises/Catenary.lean#L245). The attribute's comment: “ring\_catenary”.

> A ring `A` is **catenary** in the sense of relative heights if for all primes
> `p₁ ⊆ p₂ ⊆ p₃` the height of `p₃/p₁` in `A/p₁` is the sum of the height of `p₃/p₂` in `A/p₂`
> and the height of `p₂/p₁` in `A/p₁`. The source defines this for Noetherian rings; the condition
> is stated here for any commutative ring, and for Noetherian rings it agrees with the chain
> condition `Ring.IsCatenary` (`Ring.isHeightCatenary_iff_isCatenary`).

```lean
def IsHeightCatenary (A : Type*) [CommRing A] : Prop
```

Declarations registered for the tag:

- [`IsLocalization.AtPrime.ringKrullDim_eq_height`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization.AtPrime.ringKrullDim_eq_height#doc) registered with `add_to_stacks` in [StacksFrontier/Exercises/Catenary.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Exercises/Catenary.lean#L47) (StacksFrontier): “relative\_height”. References: EGA 0 (16.1.3), “dim(A\_p) = ht(p)”; EGA 0 (16.3.1), “more general”.
- [`TopologicalSpace.IsTopologicallyCatenary`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/DimensionFunctionCatenary.lean#L81), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Exercises/Catenary.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Exercises/Catenary.lean#L50) (StacksFrontier): “space\_catenary”.

## Tag 0CT5, an exercise

[Tag 0CT5](https://stacks.math.columbia.edu/tag/0CT5) in the Stacks Project.

**`Ring.isHeightCatenary_iff_isCatenary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Exercises/Catenary.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Exercises/Catenary.lean#L255).

> For a Noetherian ring, catenarity by additivity of relative heights agrees with catenarity
> by chains of primes: chains between two primes are bounded and all saturated ones have the same
> length.

```lean
theorem isHeightCatenary_iff_isCatenary (A : Type*) [CommRing A] [IsNoetherianRing A] :
    IsHeightCatenary A ↔ IsCatenary A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 111.18, Tag 027N](https://stacks.math.columbia.edu/tag/027N)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
