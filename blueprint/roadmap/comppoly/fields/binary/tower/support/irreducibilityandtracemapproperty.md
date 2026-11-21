---
catalog: module
lean: irreducible_quadratic_defining_poly_of_traceMap_eq_1, traceMapProperty_of_quadratic_extension, not_irreducible_of_isRoot_of_degree_gt_one
statement: formalized
proof: formalized
---

# Binary Tower Irreducibility and Trace

`CompPoly.Fields.Binary.Tower.Support.IrreducibilityAndTraceMapProperty`, in [CompPoly/Fields/Binary/Tower/Support/IrreducibilityAndTraceMapProperty.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Support/IrreducibilityAndTraceMapProperty.lean), by Quang Dao, Chung Thai Nguyen.

> Irreducibility and trace-map criteria for binary tower defining polynomials.

`irreducible_quadratic_defining_poly_of_traceMap_eq_1` (theorem, [line 28](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Support/IrreducibilityAndTraceMapProperty.lean#L28))

> Generic irreducibility theorem for binary tower polynomials.
> Proves that X² + s·X + 1 is irreducible when s satisfies the required properties.
> This is the most general form that can be reused across different tower constructions.

```lean
theorem irreducible_quadratic_defining_poly_of_traceMap_eq_1
    {F : Type*} [Field F] [Fintype F] [CharP F 2] (s : F) [NeZero s] (k : ℕ)
    (trace_map_prop : TraceMapProperty F s k)
    (fintypeCard : Fintype.card F = 2 ^ (2 ^ k)) :
    Irreducible (definingPoly s)
```

`traceMapProperty_of_quadratic_extension` (theorem, [line 128](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Support/IrreducibilityAndTraceMapProperty.lean#L128))

> Instance : The trace map property for a quadratic extension defined by a root u of X^2 + t1 * X + 1,
> assuming the trace property for t1 at the previous level.

```lean
theorem traceMapProperty_of_quadratic_extension
    (F_prev : Type*) [Field F_prev] [Fintype F_prev] (k : ℕ)
    (fintypeCardPrev : Fintype.card F_prev = 2 ^ (2 ^ k))
    (t1 : F_prev) [instNeZero_t1 : NeZero t1]
    {F_cur : Type*} [Field F_cur] (u : F_cur) [instNeZero_u : NeZero u]
    [Algebra F_prev F_cur]
    (h_rel : SpecialElementRelation (t1 := t1) (u := u))
    (prev_trace_map : TraceMapProperty F_prev t1 (k))
    (sumZeroIffEq : ∀ (x y : F_cur), x + y = 0 ↔ x = y) :
    TraceMapProperty F_cur u (k + 1)
```

`not_irreducible_of_isRoot_of_degree_gt_one` (theorem, [line 218](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Support/IrreducibilityAndTraceMapProperty.lean#L218))

> A polynomial with a degree greater than 1 is not irreducible if it has a root in `R`.

```lean
theorem not_irreducible_of_isRoot_of_degree_gt_one
    (p : R[X]) (h_root : ∃ r : R, IsRoot p r) (h_deg : p.degree > 1) :
    ¬ Irreducible p
```

## Depends on

- [Binary Tower Defining Polynomials](definingpoly.md)
- [Binary Tower Preliminaries](preliminaries.md)

## Sources

- [CompPoly/Fields/Binary/Tower/Support/IrreducibilityAndTraceMapProperty.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Tower/Support/IrreducibilityAndTraceMapProperty.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.Tower.Support.IrreducibilityAndTraceMapProperty.json)
