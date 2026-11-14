---
declaration: module
origin: cited
lean: QuantumMechanics.RectangularBarrier, QuantumMechanics.RectangularBarrier.m_pos, QuantumMechanics.RectangularBarrier.m_nonneg, QuantumMechanics.RectangularBarrier.m_ne_zero, QuantumMechanics.RectangularBarrier.potentialFunction, QuantumMechanics.RectangularBarrier.potentialFunction_eq, QuantumMechanics.RectangularBarrier.potentialFunction_aestronglyMeasurable, QuantumMechanics.RectangularBarrier.HS
statement: formalized
proof: formalized
---

# The rectangular potential barrier

The module `Physlib.QuantumMechanics.RectangularBarrier.Basic`, [Physlib/QuantumMechanics/RectangularBarrier/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/RectangularBarrier/Basic.lean): 11 declarations, 7 with a docstring.

## i. Overview

> The rectangular potential barrier in one dimension provides the simplest example of quantum
> tunnelling. A particle of mass `m` is subject to a piece-wise constant potential which is `V₀`
> on a closed interval and zero elsewhere.

## ii. Key results

## iv. References

> * None.

**`QuantumMechanics.RectangularBarrier`**, a structure, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/RectangularBarrier/Basic.lean#L49).

> A quantum particle with mass `m > 0` on `Space 1` subject to a rectangular potential barrier.
>
> The potential is `V₀` on the interval `Icc lower upper` and zero elsewhere.

```lean
structure RectangularBarrier where
  /-- The mass (positive). -/
  m : ℝ
  hm : 0 < m
  /-- The lower bound of the barrier. -/
  lower : ℝ
  /-- The upper bound of the barrier. -/
  upper : ℝ
  h_bounds : lower < upper
  /-- The height of the potential barrier. -/
  V₀ : ℝ
```

## A. Basic properties

**`QuantumMechanics.RectangularBarrier.m_pos`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/RectangularBarrier/Basic.lean#L70).

```lean
lemma m_pos : 0 < Q.m
```

**`QuantumMechanics.RectangularBarrier.m_nonneg`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/RectangularBarrier/Basic.lean#L73).

```lean
lemma m_nonneg : 0 ≤ Q.m
```

**`QuantumMechanics.RectangularBarrier.m_ne_zero`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/RectangularBarrier/Basic.lean#L76).

```lean
lemma m_ne_zero : Q.m ≠ 0
```

## B. Potential function

**`QuantumMechanics.RectangularBarrier.potentialFunction`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/RectangularBarrier/Basic.lean#L84).

> The piece-wise constant potential, equal to `Q.V₀` for `x.val 0 ∈ Icc Q.lower Q.upper`
> and zero otherwise.

```lean
def potentialFunction : Space 1 → ℝ
```

**`QuantumMechanics.RectangularBarrier.potentialFunction_eq`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/RectangularBarrier/Basic.lean#L86).

```lean
lemma potentialFunction_eq :
    Q.potentialFunction = fun x ↦ (Icc Q.lower Q.upper).indicator (fun _ ↦ Q.V₀) (x 0)
```

**`QuantumMechanics.RectangularBarrier.potentialFunction_aestronglyMeasurable`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/RectangularBarrier/Basic.lean#L91).

> The piecewise-constant potential of the rectangular barrier is a.e. strongly measurable.

```lean
lemma potentialFunction_aestronglyMeasurable: AEStronglyMeasurable Q.potentialFunction volume
```

## C. Hilbert space

**`QuantumMechanics.RectangularBarrier.HS`**, an abbrev, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/RectangularBarrier/Basic.lean#L102).

> The Hilbert space for the 1d rectangular barrier.

```lean
abbrev HS (_ : RectangularBarrier) : Type _
```

## D. Operators

### D.1. Kinetic

**`QuantumMechanics.RectangularBarrier.kineticOperator`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/RectangularBarrier/Basic.lean#L113).

> The kinetic energy operator, `p²/2m`.

```lean
def kineticOperator : Q.HS →ₗ.[ℂ] Q.HS
```

### D.2. Potential

**`QuantumMechanics.RectangularBarrier.potentialOperator`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/RectangularBarrier/Basic.lean#L120).

> The potential energy operator, defined by multiplication by `Q.potentialFunction`.

```lean
def potentialOperator : Q.HS →ₗ.[ℂ] Q.HS
```

**`QuantumMechanics.RectangularBarrier.potentialOperator_isSelfAdjoint`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/RectangularBarrier/Basic.lean#L123).

> The potential operator for the rectangular barrier is self-adjoint.

```lean
lemma potentialOperator_isSelfAdjoint (Q : RectangularBarrier) :
    IsSelfAdjoint Q.potentialOperator
```

### D.3. Hamiltonian

## E. As a quantum system

## Depends on

- [Physlib.Meta.Informal.Basic](../../meta/informal/basic.md)
- [Momentum operators](../operators/momentum.md)
- [Multiplication operators on `SpaceDHilbertSpace`](../operators/multiplication.md)

## Sources

- [Physlib/QuantumMechanics/RectangularBarrier/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/RectangularBarrier/Basic.lean)
