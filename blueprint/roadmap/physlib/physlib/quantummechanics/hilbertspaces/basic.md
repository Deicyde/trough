---
declaration: module
origin: cited
lean: QuantumMechanics.QuantumHilbertSpace
statement: formalized
proof: formalized
---

# The Hilbert space of a quantum system

The module `Physlib.QuantumMechanics.HilbertSpaces.Basic`, [Physlib/QuantumMechanics/HilbertSpaces/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HilbertSpaces/Basic.lean): 1 declaration, 1 with a docstring.

## i. Overview

> A quantum system is specified first of all by its Hilbert space of states: a complex Hilbert
> space, that is a normed additive commutative group with a complex inner product, complete for
> the induced norm.
>
> `QuantumHilbertSpace HS` is a `variable_alias` for this collection of instances on a type `HS`.
> It carries no data and is not a class. Its purpose is to state the assumptions of a quantum
> system in one place: one only types
>
> ```
> variable? (HS : Type*) [QuantumHilbertSpace HS]
> ```
>
> and Lean inserts the instances `NormedAddCommGroup HS`, `InnerProductSpace ℂ HS` and
> `CompleteSpace HS` itself, offering a `Try this` suggestion that appends them after `=>`.
> Accepting it records the expanded form, which Lean then checks if the instances change.
> A concrete system is given by its type, for example `Qubit`, on which these instances are found
> directly.

## ii. Key results

> - `QuantumHilbertSpace` : the instances making a type a complex Hilbert space, the space of
>   states of a quantum system.

## iv. References

> * None.

## A. The variable alias `QuantumHilbertSpace`

**`QuantumMechanics.QuantumHilbertSpace`**, a structure, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HilbertSpaces/Basic.lean#L63).

> The Hilbert space of a quantum system: the instances making `HS` a complex Hilbert space.
> This is a `variable_alias`, to be used with `variable?`.

```lean
structure QuantumHilbertSpace (HS : Type*) [NormedAddCommGroup HS] [InnerProductSpace ℂ HS]
    [CompleteSpace HS]
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/QuantumMechanics/HilbertSpaces/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HilbertSpaces/Basic.lean)
