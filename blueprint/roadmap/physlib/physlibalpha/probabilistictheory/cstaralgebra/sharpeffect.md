---
declaration: module
origin: cited
lean: ProbabilisticTheory.nonneg_add_eq_zero, ProbabilisticTheory.sandwich_eq_zero, ProbabilisticTheory.eq_of_mem_openSegment_of_isIdempotentElem, IsIdempotentElem.isSharp
statement: formalized
proof: formalized
---

# Projections are sharp

The module `PhyslibAlpha.ProbabilisticTheory.CStarAlgebra.SharpEffect`, [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SharpEffect.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SharpEffect.lean): 4 declarations, 4 with a docstring.

> An idempotent effect of a C⋆-algebra is not a proper mixture of two different effects.

## i. Overview

> A projection `p` is a sharp effect: it is not a proper mixture of two different effects. If `p = t
> y₁ + s y₂`, conjugating by `1 - p` kills both `y₁` and `y₂`, so by the C⋆-identity both commute with
> `p` and lie below it, which forces `y₁ = y₂ = p`.

## ii. Key results

> - `IsIdempotentElem.isSharp` : idempotent effects are sharp.
> - `ProbabilisticTheory.eq_of_mem_openSegment_of_isIdempotentElem` : the algebraic heart of the
>   proof, stated on bare elements.

## iv. References

> * None.

## A. Consequences of the C⋆-identity

**`ProbabilisticTheory.nonneg_add_eq_zero`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SharpEffect.lean#L53).

> In a partially ordered additive group, two nonnegative terms summing to zero vanish.

```lean
lemma nonneg_add_eq_zero {x y : A} (hx : 0 ≤ x) (hy : 0 ≤ y) (hxy : x + y = 0) :
    x = 0
```

**`ProbabilisticTheory.sandwich_eq_zero`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SharpEffect.lean#L62).

> If `b * x * b = 0` for `b` self-adjoint and `x ≥ 0`, then `√x * b = 0`: the C⋆-identity
> `‖z⋆z‖ = ‖z‖²`, applied to `z := √x * b`, since `z⋆z = b * √x * √x * b = b * x * b`.

```lean
lemma sandwich_eq_zero {b x : A} (hb : IsSelfAdjoint b) (hx : 0 ≤ x)
    (h : b * x * b = 0) : CFC.sqrt x * b = 0
```

**`ProbabilisticTheory.eq_of_mem_openSegment_of_isIdempotentElem`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SharpEffect.lean#L75).

> The algebraic heart of `IsIdempotentElem.isSharp`, stated on bare elements of `A`: an
> idempotent `a` between `0` and `1` cannot be written as a nontrivial mixture of two different
> effects.

```lean
lemma eq_of_mem_openSegment_of_isIdempotentElem {a y₁ y₂ : A} (ha0 : 0 ≤ a) (_ha1 : a ≤ 1)
    (hidem : a * a = a) (hy₁0 : 0 ≤ y₁) (hy₁1 : y₁ ≤ 1) (hy₂0 : 0 ≤ y₂) (hy₂1 : y₂ ≤ 1)
    {t s : ℝ} (ht : 0 < t) (hs : 0 < s) (hts : t + s = 1) (heq : t • y₁ + s • y₂ = a) :
    y₁ = a
```

## B. Projections are sharp

**`IsIdempotentElem.isSharp`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SharpEffect.lean#L158).

> **Projections are sharp**: an idempotent effect is not a proper mixture of two different
> effects.

```lean
lemma _root_.IsIdempotentElem.isSharp {e : Effect (selfAdjoint A)}
    (h : IsIdempotentElem ((e : selfAdjoint A) : A)) : Effect.IsSharp e
```

## Depends on

- [The observables of a C⋆-algebra](../../../physlib/probabilistictheory/cstaralgebra/orderunit.md)
- [Sharp effects](../../../physlib/probabilistictheory/effect/sharp.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SharpEffect.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/SharpEffect.lean)
