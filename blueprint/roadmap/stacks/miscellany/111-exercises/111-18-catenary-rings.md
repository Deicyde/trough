---
declaration: section
origin: cited
lean: Ideal.ringKrullDim_quotient_localization_eq_height_map, IsLocalization.AtPrime.ringKrullDim_eq_height, Ring.IsCatenary, TopologicalSpace.IsTopologicallyCatenary
statement: formalized
proof: formalized
---

# 111.18 Catenary rings

Section 111.18 of the Stacks Project, [Tag 027N](https://stacks.math.columbia.edu/tag/027N). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 027O, a definition

[Tag 027O](https://stacks.math.columbia.edu/tag/027O) in the Stacks Project.

**`Ideal.ringKrullDim_quotient_localization_eq_height_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Exercises/Catenary.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Exercises/Catenary.lean#L52). The attribute's comment: “relative\_height”. References: EGA 0 (16.1.3), “(16.1.3.2)”; EGA 0 (16.3.1), “more general”.

> For `q ≤ p` with `p` prime, the Krull dimension of `Aₚ/qAₚ` is the height of the prime
> ideal `p/q` of `A/q`.

```lean
theorem ringKrullDim_quotient_localization_eq_height_map
    {A : Type*} [CommRing A] (q p : Ideal A) [p.IsPrime] (hqp : q ≤ p) :
    ringKrullDim
        (Localization.AtPrime p ⧸ q.map (algebraMap A (Localization.AtPrime p))) =
      ((p.map (Ideal.Quotient.mk q)).height : WithBot ℕ∞)
```

Declarations registered for the tag:

- [`IsLocalization.AtPrime.ringKrullDim_eq_height`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization.AtPrime.ringKrullDim_eq_height#doc) registered with `add_to_stacks` in [StacksFrontier/Exercises/Catenary.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Exercises/Catenary.lean#L41) (StacksFrontier): “relative\_height”. References: EGA 0 (16.1.3), “dim(A\_p) = ht(p)”; EGA 0 (16.3.1), “more general”.
- [`Ring.IsCatenary`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Catenary/Basic.lean#L1261), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Exercises/Catenary.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Exercises/Catenary.lean#L44) (StacksFrontier): “ring\_catenary”.
- [`TopologicalSpace.IsTopologicallyCatenary`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Dimension/DimensionFunctionCatenary.lean#L81), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Exercises/Catenary.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Exercises/Catenary.lean#L45) (StacksFrontier): “space\_catenary”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 111.18, Tag 027N](https://stacks.math.columbia.edu/tag/027N)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
