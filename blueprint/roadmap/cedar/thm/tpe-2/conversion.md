---
catalog: module
lean: Cedar.Thm.conversion_preserves_evaluation_forall2, Cedar.Thm.conversion_preserves_evaluation_forall2_map, Cedar.Thm.conversion_preserves_evaluation, Cedar.Thm.conversion_preserves_typeof, Cedar.Thm.conversion_preserves_typedness
statement: formalized
proof: formalized
---

# Conversion

`Cedar.Thm.TPE.Conversion`, in [Cedar/Thm/TPE/Conversion.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Conversion.lean).

> This file defines the main theorem of TPE soundness and its associated lemmas.

`Cedar.Thm.conversion_preserves_evaluation_forall2` (theorem, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Conversion.lean#L36))

```lean
theorem conversion_preserves_evaluation_forall2 :
  List.Forall₂ (fun x y => Spec.evaluate x.toExpr req es = (TypedExpr.toResidual y).evaluate req es) ls ls
```

`Cedar.Thm.conversion_preserves_evaluation_forall2_map` (theorem, [line 49](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Conversion.lean#L49))

```lean
theorem conversion_preserves_evaluation_forall2_map {map : List (Attr × TypedExpr)} :
  List.Forall₂
  (fun x y =>
    Prod.mk x.fst <$> Spec.evaluate x.snd.toExpr req es =
      Prod.mk y.fst <$> (TypedExpr.toResidual y.snd).evaluate req es)
  map map
```

`Cedar.Thm.conversion_preserves_evaluation` (theorem, [line 73](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Conversion.lean#L73))

> Theorem stating that converting a TypedExpr to a Residual preserves evaluation semantics.
> That is, evaluating the original TypedExpr (converted to Expr) gives the same result
> as evaluating the converted Residual.

```lean
theorem conversion_preserves_evaluation (te : TypedExpr) (req : Request) (es : Entities) :
  Spec.evaluate te.toExpr req es = (TypedExpr.toResidual te).evaluate req es
```

`Cedar.Thm.conversion_preserves_typeof` (theorem, [line 166](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Conversion.lean#L166))

```lean
theorem conversion_preserves_typeof (e: TypedExpr) :
  TypedExpr.typeOf e = Residual.typeOf (TypedExpr.toResidual e)
```

`Cedar.Thm.conversion_preserves_typedness` (theorem, [line 173](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Conversion.lean#L173))

```lean
theorem conversion_preserves_typedness:
  TypedExpr.WellTyped env expr →
    Residual.WellTyped env (TypedExpr.toResidual expr)
```

## Depends on

- [Residual/Definition](../welltyped/residual-2/definition.md)

## Proof depends on

- [Authorization/Evaluator](../authorization-2/evaluator.md)

## Sources

- [Cedar/Thm/TPE/Conversion.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Conversion.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.TPE.Conversion.json)
