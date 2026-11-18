---
catalog: module
lean: Cslib.URM.Computes, Cslib.URM.Computable
statement: formalized
proof: formalized
---

# URM-Computable Functions

`Cslib.Computability.URM.Computable`, in [Cslib/Computability/URM/Computable.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Computable.lean), by Jesse Alama.

> This file defines the notion of URM-computability for partial functions on natural numbers.
>
> ## Main definitions
>
> - `URM.Computes`: A program computes a given partial function.
> - `URM.Computable`: A partial function is URM-computable if there exists a URM program that
>   computes it.
>
> ## Implementation notes
>
> Inputs are provided in registers 0, 1, ..., n-1 and output is read from register 0.

`Cslib.URM.Computes` (definition, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Computable.lean#L35))

> A program `p` computes a partial function `f : (Fin n → ℕ) → Part ℕ` if for any input,
> `eval p inputs = f inputs` as partial values. This captures both:
> - The program halts iff the function is defined on that input
> - When both are defined, the program's output equals the function's value
>
> Note: Inputs are provided in registers 0, 1, ..., n-1 and output is read from register 0.

```lean
def Computes (n : ℕ) (p : Program) (f : (Fin n → ℕ) → Part ℕ) : Prop
```

`Cslib.URM.Computable` (definition, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Computable.lean#L40))

> A partial function `f : (Fin n → ℕ) → Part ℕ` is URM-computable if there exists a URM program
> that computes it.

```lean
def Computable (n : ℕ) (f : (Fin n → ℕ) → Part ℕ) : Prop
```

## Depends on

- [URM Execution Semantics](execution.md)

## Sources

- [Cslib/Computability/URM/Computable.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/URM/Computable.lean)
