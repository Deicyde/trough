---
declaration: module
origin: cited
lean: ProbabilisticTheory.Effect.Orthogonal, ProbabilisticTheory.Effect.addOfOrthogonal, ProbabilisticTheory.Effect.coe_addOfOrthogonal
statement: formalized
proof: formalized
---

# Orthogonal effects

The module `PhyslibAlpha.ProbabilisticTheory.Effect.Basic`, [PhyslibAlpha/ProbabilisticTheory/Effect/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Effect/Basic.lean): 3 declarations, 3 with a docstring.

> Effects: the order interval `[0, 1]` of an ordered space, modelling yes/no measurement outcomes.

## i. Overview

> Two effects are orthogonal when their sum is still an effect, that is, still bounded by the order
> unit. Their partial sum is then again an effect.

## ii. Key results

> - `Effect.Orthogonal` : two effects whose sum is bounded by the order unit.
> - `Effect.addOfOrthogonal` : the partial sum of two orthogonal effects.

## iv. References

> - G. Ludwig, *Foundations of Quantum Mechanics I*, Springer, 1983.
>   <https://link.springer.com/book/10.1007/978-3-642-86751-4>

## A. Orthogonal effects

**`ProbabilisticTheory.Effect.Orthogonal`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Effect/Basic.lean#L51).

> Two effects are orthogonal when their sum is still bounded by the order unit.

```lean
def Orthogonal (e f : Effect E) : Prop
```

**`ProbabilisticTheory.Effect.addOfOrthogonal`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Effect/Basic.lean#L54).

> The partial sum of two orthogonal effects.

```lean
def addOfOrthogonal (e f : Effect E) (h : Orthogonal e f) : Effect E
```

**`ProbabilisticTheory.Effect.coe_addOfOrthogonal`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Effect/Basic.lean#L59).

> The underlying observable of an orthogonal effect sum is the ordinary sum.

```lean
lemma coe_addOfOrthogonal (e f : Effect E) (h : Orthogonal e f) :
    (addOfOrthogonal e f h : E) = (e : E) + (f : E)
```

## Depends on

- [Effects](../../../physlib/probabilistictheory/effect/basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Effect/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Effect/Basic.lean)
