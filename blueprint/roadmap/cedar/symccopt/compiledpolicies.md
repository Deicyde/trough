---
catalog: module
lean: Cedar.SymCC.CompiledPolicyError, Cedar.SymCC.CompiledPolicy, Cedar.SymCC.CompiledPolicy.compile, Cedar.SymCC.CompiledPolicySet, Cedar.SymCC.CompiledPolicySet.compile, Cedar.SymCC.CompiledPolicySet.allowAll, Cedar.SymCC.CompiledPolicySet.denyAll, Cedar.SymCC.CompiledPolicy.intoCompiledPolicySet, Cedar.SymCC.CompiledPolicies, Cedar.SymCC.CompiledPolicies.allPolicies, Cedar.SymCC.CompiledPolicies.footprint, Cedar.SymCC.CompiledPolicies.εnv
statement: formalized
proof: formalized
---

# SymCCOpt/CompiledPolicies

`Cedar.SymCCOpt.CompiledPolicies`, in [Cedar/SymCCOpt/CompiledPolicies.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/CompiledPolicies.lean).

`Cedar.SymCC.CompiledPolicyError` (inductive type, [line 33](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/CompiledPolicies.lean#L33))

```lean
inductive CompiledPolicyError where
  | validationError (e : Validation.ValidationError)
  | symCCError (e : SymCC.Error)
deriving Repr, BEq
```

`Cedar.SymCC.CompiledPolicy` (structure, [line 48](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/CompiledPolicies.lean#L48))

> Represents a symbolically compiled policy. This can be fed into the various
> functions in SymCCOpt.lean for efficient solver queries (that don't have to
> repeat symbolic compilation).

```lean
structure CompiledPolicy where
  /-- typechecked policy compiled to a `Term` of type .option bool -/
  term : Term
  /-- `SymEnv` representing the environment this policy was compiled for -/
  εnv : SymEnv
  /-- typechecked policy -/
  policy : Policy
  /-- footprint of the policy -/
  footprint : Set Term
  /-- acyclicity constraints for this policy -/
  acyclicity : Set Term
deriving Repr, Inhabited, DecidableEq
```

`Cedar.SymCC.CompiledPolicy.compile` (definition, [line 67](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/CompiledPolicies.lean#L67))

> Compile a policy `p` for the given environment `Γ`.
> This function calls the Cedar typechecker to obtain a policy `p'` that is
> semantically equivalent to `p` and well-typed with respect to `Γ`.
> Then, it runs the symbolic compiler to produce a compiled policy.

```lean
def CompiledPolicy.compile (p : Policy) (s : CompiledSchema) (reqty : Validation.RequestType) : Except CompiledPolicyError CompiledPolicy
```

`Cedar.SymCC.CompiledPolicySet` (structure, [line 80](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/CompiledPolicies.lean#L80))

> Represents a symbolically compiled policyset. This can be fed into the various
> functions in SymCCOpt.lean for efficient solver queries (that don't have to
> repeat symbolic compilation).

```lean
structure CompiledPolicySet where
  /-- typechecked policies compiled to a single `Term` of type .bool representing the authorization decision -/
  term : Term
  /-- `SymEnv` representing the environment these policies were compiled for -/
  εnv : SymEnv
  /-- typechecked policies -/
  policies : Policies
  /-- footprint of the policies -/
  footprint : Set Term
  /-- acyclicity constraints for these policies -/
  acyclicity : Set Term
deriving Repr, Inhabited, DecidableEq
```

`Cedar.SymCC.CompiledPolicySet.compile` (definition, [line 99](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/CompiledPolicies.lean#L99))

> Compile a set of policies `ps` for the given environment `Γ`.
> This function calls the Cedar typechecker on each `p ∈ ps` to obtain a policy `p'`
> that is semantically equivalent to `p` and well-typed with respect to `Γ`.
> Then, it runs the symbolic compiler to produce a compiled policy.

```lean
def CompiledPolicySet.compile (ps : Policies) (s : CompiledSchema) (reqty : Validation.RequestType) : Except CompiledPolicyError CompiledPolicySet
```

`Cedar.SymCC.CompiledPolicySet.allowAll` (definition, [line 111](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/CompiledPolicies.lean#L111))

> A `CompiledPolicySet` that represents the policyset that allows all requests in
> the `εnv`.

```lean
def CompiledPolicySet.allowAll (εnv : SymEnv) : CompiledPolicySet
```

`Cedar.SymCC.CompiledPolicySet.denyAll` (definition, [line 124](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/CompiledPolicies.lean#L124))

> A `CompiledPolicySet` that represents the policyset that denies all requests in
> the `εnv`.

```lean
def CompiledPolicySet.denyAll (εnv : SymEnv) : CompiledPolicySet
```

`Cedar.SymCC.CompiledPolicy.intoCompiledPolicySet` (definition, [line 140](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/CompiledPolicies.lean#L140))

> Convert a `CompiledPolicy` to a `CompiledPolicySet` representing a singleton
> policyset with just that policy.
>
> This function is intended to be much more efficient than re-compiling with
> `CompiledPolicySet.compile`.

```lean
def CompiledPolicy.intoCompiledPolicySet (cp : CompiledPolicy) : CompiledPolicySet
```

`Cedar.SymCC.CompiledPolicies` (inductive type, [line 159](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/CompiledPolicies.lean#L159))

> Represents a `CompiledPolicy` or a `CompiledPolicySet`, for APIs that don't care
> which one they get.

```lean
inductive CompiledPolicies where
  | policy (cp : CompiledPolicy)
  | pset (cpset : CompiledPolicySet)
```

`Cedar.SymCC.CompiledPolicies.allPolicies` (definition, [line 163](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/CompiledPolicies.lean#L163))

```lean
def CompiledPolicies.allPolicies : CompiledPolicies → Policies
```

`Cedar.SymCC.CompiledPolicies.footprint` (definition, [line 167](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/CompiledPolicies.lean#L167))

```lean
def CompiledPolicies.footprint : CompiledPolicies → Set Term
```

`Cedar.SymCC.CompiledPolicies.εnv` (definition, [line 171](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/CompiledPolicies.lean#L171))

```lean
def CompiledPolicies.εnv : CompiledPolicies → SymEnv
```

## Depends on

- [SymCC](../symcc-2.md)
- [SymCCOpt/Authorizer](authorizer.md)
- [CompiledSchema](compiledschema.md)

## Sources

- [Cedar/SymCCOpt/CompiledPolicies.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/CompiledPolicies.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.SymCCOpt.CompiledPolicies.json)
