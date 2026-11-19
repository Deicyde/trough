---
catalog: module
lean: Cedar.Thm.same_bool_def, Cedar.Thm.same_bool_not_true_implies_false, Cedar.Thm.same_bool_not_not_true_implies_true
statement: formalized
proof: formalized
---

# Verifier/Same

`Cedar.Thm.SymCC.Verifier.Same`, in [Cedar/Thm/SymCC/Verifier/Same.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/Same.lean).

> This file contains useful definitions and theorems for comparing
> booleans to terms.
> -

`Cedar.Thm.same_bool_def` (theorem, [line 32](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/Same.lean#L32))

```lean
theorem same_bool_def {b : Bool} {t : Term} :
  b ∼ t ↔ t = Term.bool b
```

`Cedar.Thm.same_bool_not_true_implies_false` (theorem, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/Same.lean#L36))

```lean
theorem same_bool_not_true_implies_false {b : Bool} {t : Term} :
  b ∼ t →
  not t = .bool true →
  b = false
```

`Cedar.Thm.same_bool_not_not_true_implies_true` (theorem, [line 48](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/Same.lean#L48))

```lean
theorem same_bool_not_not_true_implies_true {b : Bool} {t : Term} :
  b ∼ t →
  ¬ not t = .bool true →
  b = true
```

## Depends on

- [Well-formedness and interpretations](../data/basic.md)

## Proof depends on

- [Basic properties of partial evaluation of terms](../term/pe.md)

## Sources

- [Cedar/Thm/SymCC/Verifier/Same.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/Same.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Verifier.Same.json)
