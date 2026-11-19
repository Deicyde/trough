---
catalog: module
lean: Cedar.Thm.asserts_satisfiedBy_true, Cedar.Thm.asserts_satisfiable_def, Cedar.Thm.asserts_unsatisfiable_def, Cedar.Thm.asserts_last_not_true, Cedar.Thm.asserts_all_true
statement: formalized
proof: formalized
---

# Enforcer/Asserts

`Cedar.Thm.SymCC.Enforcer.Asserts`, in [Cedar/Thm/SymCC/Enforcer/Asserts.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Asserts.lean).

> This file proves auxiliary lemmas about `Asserts`, which are lists of
> (well-formed) boolean Terms.
> -

`Cedar.Thm.asserts_satisfiedBy_true` (theorem, [line 28](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Asserts.lean#L28))

```lean
theorem asserts_satisfiedBy_true {I : Interpretation} {asserts : Asserts} :
  asserts.satisfiedBy I ↔
  ∀ t ∈ asserts, t.interpret I = true
```

`Cedar.Thm.asserts_satisfiable_def` (theorem, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Asserts.lean#L34))

```lean
theorem asserts_satisfiable_def {εnv : SymEnv} {asserts : Asserts} :
  (εnv ⊧ asserts) ↔
  ∃ I, I.WellFormed εnv.entities ∧ ∀ t ∈ asserts, t.interpret I = true
```

`Cedar.Thm.asserts_unsatisfiable_def` (theorem, [line 40](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Asserts.lean#L40))

```lean
theorem asserts_unsatisfiable_def {εnv : SymEnv} {asserts : Asserts} :
  (εnv ⊭ asserts) ↔
  ∀ I, I.WellFormed εnv.entities → ∃ t ∈ asserts, t.interpret I ≠ true
```

`Cedar.Thm.asserts_last_not_true` (theorem, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Asserts.lean#L47))

```lean
theorem asserts_last_not_true {I : Interpretation} {ts : Asserts} {t t' : Term} :
  ts.satisfiedBy I →
  t ∈ ts ++ [t'] →
  t.interpret I ≠ Term.prim (TermPrim.bool true) →
  t = t'
```

`Cedar.Thm.asserts_all_true` (theorem, [line 60](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Asserts.lean#L60))

```lean
theorem asserts_all_true {I : Interpretation} {ts : Asserts} {t' : Term} :
  (∀ t ∈ ts ++ [t'], t.interpret I = true) →
  ts.satisfiedBy I ∧ t'.interpret I = true
```

## Depends on

- [Well-formedness and interpretations](../data/basic.md)

## Sources

- [Cedar/Thm/SymCC/Enforcer/Asserts.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Asserts.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Enforcer.Asserts.json)
