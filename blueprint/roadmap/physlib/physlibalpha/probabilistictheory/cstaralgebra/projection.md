---
declaration: module
origin: cited
lean: ProbabilisticTheory.Projection, ProbabilisticTheory.Projection.ext, ProbabilisticTheory.Projection.isSharp, ProbabilisticTheory.Projection.complement, ProbabilisticTheory.Projection.complement_complement, ProbabilisticTheory.Projection.spectrum_subset_zero_one
statement: formalized
proof: formalized
---

# Projections

The module `PhyslibAlpha.ProbabilisticTheory.CStarAlgebra.Projection`, [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Projection.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Projection.lean): 7 declarations (1 instance with no name), 6 with a docstring.

> Projections of a C⋆-algebra: sharp idempotent effects with complements and spectrum in \{0, 1}.

## i. Overview

> A projection is an effect `p` with `p * p = p`. Projections are sharp effects, closed under
> complement, and their spectrum lies in `{0, 1}`.

## ii. Key results

> - `Projection` : projections of a C⋆-algebra.
> - `Projection.isSharp` : projections are sharp.
> - `Projection.complement` : the complementary projection `1 - p`.
> - `Projection.spectrum_subset_zero_one` : the spectrum of a projection lies in `{0, 1}`.

## iv. References

> * None.

## A. Projections

**`ProbabilisticTheory.Projection`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Projection.lean#L53).

> A projection: an idempotent effect in the self-adjoint part of a C⋆-algebra.

```lean
def Projection (A : Type*) [CStarAlgebra A] [PartialOrder A]
```

**An instance with no name**, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Projection.lean#L59).

> A projection, viewed as an effect, forgetting idempotence.

```lean
instance : CoeOut (Projection A) (Effect (selfAdjoint A))
```

**`ProbabilisticTheory.Projection.ext`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Projection.lean#L63).

```lean
lemma ext {p q : Projection A} (h : (p : Effect (selfAdjoint A)) = (q : Effect (selfAdjoint A))) :
    p = q
```

## B. Sharpness, complements and spectrum

**`ProbabilisticTheory.Projection.isSharp`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Projection.lean#L74).

> Every projection is a sharp effect.

```lean
lemma isSharp (p : Projection A) : Effect.IsSharp (p : Effect (selfAdjoint A))
```

**`ProbabilisticTheory.Projection.complement`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Projection.lean#L78).

> The complementary projection `1 - p`.

```lean
noncomputable def complement (p : Projection A) : Projection A
```

**`ProbabilisticTheory.Projection.complement_complement`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Projection.lean#L83).

> Taking the complement twice returns the original projection.

```lean
lemma complement_complement (p : Projection A) : complement (complement p) = p
```

**`ProbabilisticTheory.Projection.spectrum_subset_zero_one`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Projection.lean#L88).

> The real spectrum of a projection is contained in `{0, 1}`.

```lean
lemma spectrum_subset_zero_one (p : Projection A) :
    spectrum ℝ (((p : Effect (selfAdjoint A)) : selfAdjoint A) : A) ⊆ {0, 1}
```

## Depends on

- [The observables of a C⋆-algebra](../../../physlib/probabilistictheory/cstaralgebra/orderunit.md)
- [Sharp effects](../../../physlib/probabilistictheory/effect/sharp.md)

## Proof depends on

- [Projections are sharp](sharpeffect.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Projection.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Projection.lean)
