---
catalog: module
lean: Cedar.SymCC.enforceCompiledPolicy, Cedar.SymCC.enforceCompiledPolicySet, Cedar.SymCC.enforcePairCompiledPolicy, Cedar.SymCC.enforcePairCompiledPolicySet
statement: formalized
proof: formalized
---

# SymCCOpt/Enforcer

`Cedar.SymCCOpt.Enforcer`, in [Cedar/SymCCOpt/Enforcer.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Enforcer.lean).

`Cedar.SymCC.enforceCompiledPolicy` (definition, [line 29](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Enforcer.lean#L29))

> Returns the ground acyclicity and transitivity assumptions for a single `CompiledPolicy`.

```lean
public def enforceCompiledPolicy (cp : CompiledPolicy) : Set Term
```

`Cedar.SymCC.enforceCompiledPolicySet` (definition, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Enforcer.lean#L36))

> Returns the ground acyclicity and transitivity assumptions for a single `CompiledPolicySet`.

```lean
public def enforceCompiledPolicySet (cpset : CompiledPolicySet) : Set Term
```

`Cedar.SymCC.enforcePairCompiledPolicy` (definition, [line 44](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Enforcer.lean#L44))

> Returns the ground acyclicity and transitivity assumptions for a pair of `CompiledPolicy`.
> Caller guarantees that `cp₁` and `cp₂` were compiled for the same `εnv`.

```lean
public def enforcePairCompiledPolicy (cp₁ : CompiledPolicy) (cp₂ : CompiledPolicy) : Set Term
```

`Cedar.SymCC.enforcePairCompiledPolicySet` (definition, [line 54](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Enforcer.lean#L54))

> Returns the ground acyclicity and transitivity assumptions for a pair of `CompiledPolicySet`.
> Caller guarantees that `cpset₁` and `cpset₂` were compiled for the same `εnv`.

```lean
public def enforcePairCompiledPolicySet (cpset₁ : CompiledPolicySet) (cpset₂ : CompiledPolicySet) : Set Term
```

## Depends on

- [SymCCOpt/CompiledPolicies](compiledpolicies.md)

## Sources

- [Cedar/SymCCOpt/Enforcer.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Enforcer.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.SymCCOpt.Enforcer.json)
