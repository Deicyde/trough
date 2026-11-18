---
catalog: module
lean: Cslib.Query.ArithQuery, Cslib.Query.ArithQuery.doAdd, Cslib.Query.ArithQuery.doSub, Cslib.Query.ArithQuery.doMul, Cslib.Query.ArithQuery.honest, Cslib.Query.ArithQuery.weight, Cslib.Query.complexMulNaive, Cslib.Query.complexMulGauss
statement: formalized
proof: formalized
---

# Arithmetic Queries and Complex Multiplication

`Cslib.Algorithms.Lean.Query.Arith.Defs`, in [Cslib/Algorithms/Lean/Query/Arith/Defs.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Arith/Defs.lean), by Kim Morrison, Shreyas Srinivas.

> A simple example showing how to use `FreeM.cost` with variable/parametrized query costs.
>
> `ArithQuery α` supports addition, subtraction, and multiplication, each with
> independently parametrized costs. Complex number multiplication provides a toy example
> where two algorithms (naive and Gauss's trick) trade multiplications for additions,
> and the optimal choice depends on the cost ratio.

`Cslib.Query.ArithQuery` (inductive type, [line 25](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Arith/Defs.lean#L25))

> Arithmetic queries: addition, subtraction, and multiplication.

```lean
inductive ArithQuery (α : Type) : Type → Type where
  | add (a b : α) : ArithQuery α α
  | sub (a b : α) : ArithQuery α α
  | mul (a b : α) : ArithQuery α α
```

`Cslib.Query.ArithQuery.doAdd` (abbreviation, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Arith/Defs.lean#L33))

> Lift `ArithQuery.add a b` into a `FreeM` that returns the sum.

```lean
abbrev doAdd (a b : α) : FreeM (ArithQuery α) α
```

`Cslib.Query.ArithQuery.doSub` (abbreviation, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Arith/Defs.lean#L35))

> Lift `ArithQuery.sub a b` into a `FreeM` that returns the difference.

```lean
abbrev doSub (a b : α) : FreeM (ArithQuery α) α
```

`Cslib.Query.ArithQuery.doMul` (abbreviation, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Arith/Defs.lean#L37))

> Lift `ArithQuery.mul a b` into a `FreeM` that returns the product.

```lean
abbrev doMul (a b : α) : FreeM (ArithQuery α) α
```

`Cslib.Query.ArithQuery.honest` (definition, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Arith/Defs.lean#L40))

> An honest oracle interprets arithmetic queries using the actual ring operations.

```lean
def honest [Add α] [Sub α] [Mul α] {ι : Type} : ArithQuery α ι → ι
```

`Cslib.Query.ArithQuery.weight` (definition, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Arith/Defs.lean#L47))

> Weighted cost model for arithmetic queries. Subtraction costs the same as addition
> (both are linear-time on bignums).

```lean
def weight (c_add c_mul : Nat) {ι : Type} : ArithQuery α ι → Nat
```

`Cslib.Query.complexMulNaive` (definition, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Arith/Defs.lean#L56))

> Naive complex multiplication: `(a + bi)(c + di) = (ac - bd) + (ad + bc)i`.
> Uses 4 multiplications, 1 subtraction, 1 addition.

```lean
def complexMulNaive (a b c d : α) : FreeM (ArithQuery α) (α × α)
```

`Cslib.Query.complexMulGauss` (definition, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Arith/Defs.lean#L68))

> Gauss's trick for complex multiplication: computes `(a+b)(c+d)` to save one
> multiplication, at the cost of extra additions and subtractions.
> Uses 3 multiplications, 2 subtractions, 3 additions.

```lean
def complexMulGauss (a b c d : α) : FreeM (ArithQuery α) (α × α)
```

## Depends on

- [Free Monad (Free)](../../../../foundations/control/monad/free.md)

## Sources

- [Cslib/Algorithms/Lean/Query/Arith/Defs.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Arith/Defs.lean)
