---
catalog: module
lean: Cedar.Thm.concretize?_some_wf
statement: formalized
proof: formalized
---

# Concretizer/WF

`Cedar.Thm.SymCC.Concretizer.WF`, in [Cedar/Thm/SymCC/Concretizer/WF.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/WF.lean).

> The main lemma in this file, `concretize?_some_wf`, proves that
> `εnv.concretize? x` produces an environment that is well-formed for `x`.

`Cedar.Thm.concretize?_some_wf` (theorem, [line 502](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/WF.lean#L502))

```lean
theorem concretize?_some_wf {x : Expr} {env : Env} {εnv : SymEnv} :
  εnv.WellFormedFor x →
  εnv.concretize? x = .some env →
  env.WellFormedFor x
```

## Depends on

- [Well-formedness and interpretations](../data/basic.md)

## Proof depends on

- [Concretizer/Same](same.md)
- [WFValue](wfvalue.md)

## Sources

- [Cedar/Thm/SymCC/Concretizer/WF.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/WF.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Concretizer.WF.json)
