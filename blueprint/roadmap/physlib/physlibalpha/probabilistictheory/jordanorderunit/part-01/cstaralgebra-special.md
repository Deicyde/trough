---
declaration: module
origin: cited
lean: ProbabilisticTheory.JBAlgebra.IsSpecialWitness, ProbabilisticTheory.JBAlgebra.IsSpecial, ProbabilisticTheory.JBAlgebra.IsSpecialWitness.map_nonneg, ProbabilisticTheory.JBAlgebra.IsSpecialWitness.monotone, ProbabilisticTheory.JB.isSpecialWitnessRefl, ProbabilisticTheory.JB.isSpecial_selfAdjoint
statement: formalized
proof: formalized
---

# Special JB-algebras

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.CStarAlgebra.Special`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Special.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Special.lean): 6 declarations, 6 with a docstring.

> Special JB-algebras: those embedding as closed Jordan subalgebras of a C⋆-algebra.

## i. Overview

> A JB-algebra is special when it embeds as a closed Jordan subalgebra of the self-adjoint part of a
> C⋆-algebra, by a linear, isometric, unital map preserving the Jordan product. The self-adjoint part
> of a C⋆-algebra is special.

## ii. Key results

> - `JBAlgebra.IsSpecialWitness` : an embedding into the self-adjoint part of a C⋆-algebra.
> - `JBAlgebra.IsSpecial` : a special JB-algebra.
> - `JB.isSpecial_selfAdjoint` : the self-adjoint part of a C⋆-algebra is special.
> - `JBAlgebra.IsSpecialWitness.map_nonneg`, `JBAlgebra.IsSpecialWitness.monotone` : such an
>   embedding preserves positivity and order.

## iv. References

> * None.

## A. Special JB-algebras

**`ProbabilisticTheory.JBAlgebra.IsSpecialWitness`**, a structure, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Special.lean#L57).

> A witness that `E` is special: an isometric unital Jordan embedding into the self-adjoint part
> of a Cstar algebra whose range is norm closed.

```lean
structure JBAlgebra.IsSpecialWitness (E : Type*) [NormedJordanAlgebra E]
    [JBAlgebra E] (A : Type*) [CStarAlgebra A] [PartialOrder A] [StarOrderedRing A] where
  /-- The underlying injective isometric real-linear map. -/
  toLinearIsometry : E →ₗᵢ[ℝ] selfAdjoint A
  /-- The order unit is preserved. -/
  map_one : toLinearIsometry 1 = 1
  /-- The Jordan product is preserved. -/
  map_mul : ∀ x y : E, toLinearIsometry (x * y) = toLinearIsometry x * toLinearIsometry y
  /-- The represented Jordan subalgebra is norm closed. -/
  isClosed_range : IsClosed (Set.range toLinearIsometry)
```

**`ProbabilisticTheory.JBAlgebra.IsSpecial`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Special.lean#L70).

> `E` is special when it embeds as a closed Jordan subalgebra of the self-adjoint part of a
> Cstar algebra in the same universe.

```lean
def JBAlgebra.IsSpecial (E : Type u) [NormedJordanAlgebra E]
    [JBAlgebra E] : Prop
```

## B. Order properties of special embeddings

**`ProbabilisticTheory.JBAlgebra.IsSpecialWitness.map_nonneg`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Special.lean#L89).

> A special-JB embedding preserves positivity. Exact-cone reconstruction supplies a square
> witness in the source; multiplicativity carries that witness to a square in the represented
> self-adjoint algebra.

```lean
lemma map_nonneg (j : JBAlgebra.IsSpecialWitness E A) {x : E} (hx : 0 ≤ x) :
    0 ≤ (j.toLinearIsometry x : selfAdjoint A)
```

**`ProbabilisticTheory.JBAlgebra.IsSpecialWitness.monotone`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Special.lean#L97).

> A special-JB embedding is order preserving. This is derived from exact cone reconstruction,
> not assumed in the definition of specialness.

```lean
lemma monotone (j : JBAlgebra.IsSpecialWitness E A) : Monotone j.toLinearIsometry
```

## C. The self-adjoint part of a C⋆-algebra

**`ProbabilisticTheory.JB.isSpecialWitnessRefl`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Special.lean#L116).

> The identity equivalence witnesses that `selfAdjoint A` is special in `A` itself.

```lean
noncomputable def isSpecialWitnessRefl : JBAlgebra.IsSpecialWitness (selfAdjoint A) A
```

**`ProbabilisticTheory.JB.isSpecial_selfAdjoint`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Special.lean#L123).

> `selfAdjoint A` is special, for any unital C⋆-algebra `A`.

```lean
lemma isSpecial_selfAdjoint : JBAlgebra.IsSpecial (selfAdjoint A)
```

## Depends on

- [The self-adjoint part of a C⋆-algebra is a JB-algebra](cstaralgebra-basic.md)

## Proof depends on

- [The positive cone of a JB-algebra](../part-02/jb-order.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Special.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Special.lean)
