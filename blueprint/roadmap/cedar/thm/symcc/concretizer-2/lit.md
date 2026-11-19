---
catalog: module
lean: Cedar.Thm.wf_term_implies_valid_uids, Cedar.Thm.concretize?_wfl_implies_some
statement: formalized
proof: formalized
---

# Lit

`Cedar.Thm.SymCC.Concretizer.Lit`, in [Cedar/Thm/SymCC/Concretizer/Lit.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/Lit.lean).

> The main lemma in this file, `concretize?_wfl_some`, proves that
> `εnv.concretize? x` succeeds when `εnv` is a literal symbolic environment that
> is well-formed with respect to `x`.

`Cedar.Thm.wf_term_implies_valid_uids` (theorem, [line 153](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/Lit.lean#L153))

```lean
public theorem wf_term_implies_valid_uids {t : Term} {εs : SymEntities} :
  t.WellFormed εs →
  ∀ uid ∈ t.entityUIDs, εs.isValidEntityUID uid
```

`Cedar.Thm.concretize?_wfl_implies_some` (theorem, [line 509](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/Lit.lean#L509))

```lean
public theorem concretize?_wfl_implies_some {x : Expr} {εnv : SymEnv} :
  εnv.WellFormedLiteralFor x →
  ∃ (env : Env), εnv.concretize? x = .some env
```

## Depends on

- [Well-formedness and interpretations](../data/basic.md)

## Proof depends on

- [Lemmas about List.mapUnion operator](../../data/mapunion.md)
- [Concretizer/Util](util.md)
- [Properties of the `Same` predicate on Terms](../term/same.md)

## Sources

- [Cedar/Thm/SymCC/Concretizer/Lit.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/Lit.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Concretizer.Lit.json)
