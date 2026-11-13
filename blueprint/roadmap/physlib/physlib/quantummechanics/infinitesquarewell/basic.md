---
declaration: module
origin: cited
lean: QuantumMechanics.InfiniteSquareWell, QuantumMechanics.InfiniteSquareWell.m_pos, QuantumMechanics.InfiniteSquareWell.m_nonneg, QuantumMechanics.InfiniteSquareWell.m_ne_zero, QuantumMechanics.InfiniteSquareWell.well, QuantumMechanics.InfiniteSquareWell.measure, QuantumMechanics.InfiniteSquareWell.HS
statement: formalized
proof: formalized
---

# The infinite square well

The module `Physlib.QuantumMechanics.InfiniteSquareWell.Basic`, [Physlib/QuantumMechanics/InfiniteSquareWell/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/InfiniteSquareWell/Basic.lean): 7 declarations, 4 with a docstring.

## i. Overview

> The particle in an infinite square well is one of the simplest quantum systems.
> The domain is an axis-aligned cuboid (the well) and energy eigenstates are (products of)
> trigonometric functions satisfying appropriate boundary conditions.

## ii. Key results

## iv. References

> * None.

**`QuantumMechanics.InfiniteSquareWell`**, a structure, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/InfiniteSquareWell/Basic.lean#L46).

> A spinless quantum particle with mass `m > 0` confined to a cuboid in `Space d`.
>
> The bounds of the well are specified by two functions `lower upper : Fin d → ℝ`
> satisfying `∀ i, lower i < upper i`.

```lean
structure InfiniteSquareWell (d : ℕ) where
  /-- The mass (positive). -/
  m : ℝ
  hm : 0 < m
  /-- The lower bounds of the well. -/
  lower : Fin d → ℝ
  /-- The upper bounds of the well. -/
  upper : Fin d → ℝ
  /-- The well is a non-empty set. -/
  h_bounds : ∀ i, lower i < upper i
```

## A. Basic properties

**`QuantumMechanics.InfiniteSquareWell.m_pos`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/InfiniteSquareWell/Basic.lean#L66).

```lean
lemma m_pos : 0 < Q.m
```

**`QuantumMechanics.InfiniteSquareWell.m_nonneg`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/InfiniteSquareWell/Basic.lean#L69).

```lean
lemma m_nonneg : 0 ≤ Q.m
```

**`QuantumMechanics.InfiniteSquareWell.m_ne_zero`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/InfiniteSquareWell/Basic.lean#L72).

```lean
lemma m_ne_zero : Q.m ≠ 0
```

## B. Domain

**`QuantumMechanics.InfiniteSquareWell.well`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/InfiniteSquareWell/Basic.lean#L79).

> The domain of the infinite square well as a Cartesian product of closed intervals.

```lean
def well : Set (Space d)
```

## C. Hilbert space

**`QuantumMechanics.InfiniteSquareWell.measure`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/InfiniteSquareWell/Basic.lean#L86).

> The measure associated with the domain of the infinite square well.

```lean
def measure : Measure (Space d)
```

**`QuantumMechanics.InfiniteSquareWell.HS`**, an abbrev, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/InfiniteSquareWell/Basic.lean#L89).

> The Hilbert space for the infinite square well.

```lean
abbrev HS : Type _
```

## D. Hamiltonian

## E. As a quantum system

## Depends on

- [Physlib.Meta.Informal.Basic](../../meta/informal/basic.md)
- [Hilbert spaces for quantum mechanics on `Space d`](../hilbertspaces/spaced/basic.md)

## Sources

- [Physlib/QuantumMechanics/InfiniteSquareWell/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/InfiniteSquareWell/Basic.lean)
