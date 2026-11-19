---
catalog: module
lean: Cedar.Slice.PolicyBound, Cedar.Slice.inSomeOrNone, Cedar.Slice.satisfiedBound, Cedar.Slice.BoundAnalysis, Cedar.Slice.BoundAnalysis.slice, Cedar.Slice.scopeAnalysis
statement: formalized
proof: formalized
---

# Slice/PolicySlice

`Cedar.Slice.PolicySlice`, in [Cedar/Slice/PolicySlice.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Slice/PolicySlice.lean).

> This file defines a simple policy slicing algorithm that is based
> on policy scopes. For proofs of correctness, see Cedar.Thm.PolicySlice.

`Cedar.Slice.PolicyBound` (structure, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Slice/PolicySlice.lean#L35))

> A policy bound consists of optional `principal` and `resource` entities.

```lean
structure PolicyBound where
  principalBound : Option EntityUID
  resourceBound  : Option EntityUID
```

`Cedar.Slice.inSomeOrNone` (definition, [line 39](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Slice/PolicySlice.lean#L39))

```lean
def inSomeOrNone (uid : EntityUID) (opt : Option EntityUID) (entities : Entities) : Bool
```

`Cedar.Slice.satisfiedBound` (definition, [line 49](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Slice/PolicySlice.lean#L49))

> A bound is satisfied by a request and store if the request principal and
> resource fields are descendents of the corresponding bound fields (or if those
> bound fields are `none`).

```lean
def satisfiedBound (bound : PolicyBound) (request : Request) (entities : Entities) : Bool
```

`Cedar.Slice.BoundAnalysis` (abbreviation, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Slice/PolicySlice.lean#L57))

> A bound analysis takes as input a policy and returns a PolicyBound.

```lean
abbrev BoundAnalysis
```

`Cedar.Slice.BoundAnalysis.slice` (definition, [line 64](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Slice/PolicySlice.lean#L64))

> A bound-based slicing algorithm takes as input a bound analysis, request, entities,
> and policies, and filters out the policies whose bound is not satisfied by the
> request and entities.

```lean
def BoundAnalysis.slice (ba : BoundAnalysis) (request : Request) (entities : Entities) (policies : Policies) : Policies
```

`Cedar.Slice.scopeAnalysis` (definition, [line 71](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Slice/PolicySlice.lean#L71))

> Scope-based bound analysis extracts the bound from the policy scope.

```lean
def scopeAnalysis (policy : Policy) : PolicyBound
```

## Depends on

- [Spec/Evaluator](../spec/evaluator.md)
- [Spec/Policy](../spec/policy.md)

## Sources

- [Cedar/Slice/PolicySlice.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Slice/PolicySlice.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Slice.PolicySlice.json)
