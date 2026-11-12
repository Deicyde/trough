---
catalog: module
lean: Cslib.Query.complexMulNaive_eval_honest, Cslib.Query.complexMulGauss_eval_honest, Cslib.Query.complexMulNaive_cost, Cslib.Query.complexMulGauss_cost, Cslib.Query.gauss_le_naive, Cslib.Query.gauss_le_naive_iff
statement: formalized
proof: formalized
---

# Complex Multiplication: Correctness and Cost Analysis

`Cslib.Algorithms.Lean.Query.Arith.Lemmas`, in [Cslib/Algorithms/Lean/Query/Arith/Lemmas.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Arith/Lemmas.lean), by Kim Morrison.

> A simple example showing how to use `FreeM.cost` with variable/parametrized query costs.
>
> We prove that both `complexMulNaive` and `complexMulGauss` correctly compute
> complex multiplication when given an honest oracle, and compute their exact
> costs under a parametric weight function. The cost theorems hold for *any* oracle
> (not just honest ones), because both algorithms are straight-line (no branching
> on query results).

> ## Correctness

`Cslib.Query.complexMulNaive_eval_honest` (theorem, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Arith/Lemmas.lean#L33))

```lean
theorem complexMulNaive_eval_honest [Add α] [Sub α] [Mul α] (a b c d : α) :
    (complexMulNaive a b c d).eval ArithQuery.honest = (a * c - b * d, a * d + b * c)
```

`Cslib.Query.complexMulGauss_eval_honest` (theorem, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Arith/Lemmas.lean#L37))

```lean
theorem complexMulGauss_eval_honest [CommRing α] (a b c d : α) :
    (complexMulGauss a b c d).eval ArithQuery.honest = (a * c - b * d, a * d + b * c)
```

> ## Exact cost counts

`Cslib.Query.complexMulNaive_cost` (theorem, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Arith/Lemmas.lean#L44))

```lean
theorem complexMulNaive_cost (oracle : {ι : Type} → ArithQuery α ι → ι)
    (c_add c_mul : Nat) (a b c d : α) :
    (complexMulNaive a b c d).cost oracle (ArithQuery.weight c_add c_mul) =
      4 * c_mul + 2 * c_add
```

`Cslib.Query.complexMulGauss_cost` (theorem, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Arith/Lemmas.lean#L51))

```lean
theorem complexMulGauss_cost (oracle : {ι : Type} → ArithQuery α ι → ι)
    (c_add c_mul : Nat) (a b c d : α) :
    (complexMulGauss a b c d).cost oracle (ArithQuery.weight c_add c_mul) =
      3 * c_mul + 5 * c_add
```

> ## Crossover: Gauss beats naive when multiplication costs at least 3× addition

`Cslib.Query.gauss_le_naive` (theorem, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Arith/Lemmas.lean#L60))

```lean
theorem gauss_le_naive (oracle : {ι : Type} → ArithQuery α ι → ι)
    (c_add c_mul : Nat) (a b c d : α) (h : 3 * c_add ≤ c_mul) :
    (complexMulGauss a b c d).cost oracle (ArithQuery.weight c_add c_mul) ≤
      (complexMulNaive a b c d).cost oracle (ArithQuery.weight c_add c_mul)
```

`Cslib.Query.gauss_le_naive_iff` (theorem, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Arith/Lemmas.lean#L67))

```lean
theorem gauss_le_naive_iff (oracle : {ι : Type} → ArithQuery α ι → ι)
    (c_add c_mul : Nat) (a b c d : α) :
    (complexMulGauss a b c d).cost oracle (ArithQuery.weight c_add c_mul) ≤
      (complexMulNaive a b c d).cost oracle (ArithQuery.weight c_add c_mul) ↔
        3 * c_add ≤ c_mul
```

## Depends on

- [Arithmetic Queries and Complex Multiplication](defs.md)
- [FreeM: query/cost interpreters and lower-bound lemma](../freem.md)

## Sources

- [Cslib/Algorithms/Lean/Query/Arith/Lemmas.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Arith/Lemmas.lean)
