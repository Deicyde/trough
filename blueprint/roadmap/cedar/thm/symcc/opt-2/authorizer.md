---
catalog: module
lean: Cedar.Thm.Opt.compileWithEffect.correctness, Cedar.Thm.Opt.satisfiedPolicies.correctness, Cedar.Thm.Opt.isAuthorized.correctness
statement: formalized
proof: formalized
---

# Opt/Authorizer

`Cedar.Thm.SymCC.Opt.Authorizer`, in [Cedar/Thm/SymCC/Opt/Authorizer.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Authorizer.lean).

`Cedar.Thm.Opt.compileWithEffect.correctness` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Authorizer.lean#L35))

> Correctness theorem for `Opt.compileWithEffect`:
>
> `Opt.compileWithEffect` produces the same `term` as `SymCC.compileWithEffect`, and
> `Opt.compileWithEffect` produces the same `footprint` as `footprint`

```lean
theorem Opt.compileWithEffect.correctness (effect : Effect) (p : Policy) (εnv : SymEnv) :
  Opt.compileWithEffect effect p εnv = (do
    let term ← SymCC.compileWithEffect effect p εnv
    let footprint := footprint p.toExpr εnv
    .ok $ term.map λ term => { term, footprint }
  )
```

`Cedar.Thm.Opt.satisfiedPolicies.correctness` (theorem, [line 112](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Authorizer.lean#L112))

> Correctness theorem for `Opt.satisfiedPolicies`:
>
> `Opt.satisfiedPolicies` produces the same `term` as `SymCC.satisfiedPolicies`, and
> `Opt.satisfiedPolicies` produces the same `footprint` as `footprints` applied to
> just the policies with the appropriate `effect`

```lean
theorem Opt.satisfiedPolicies.correctness (effect : Effect) (ps : Policies) (εnv : SymEnv) :
  Opt.satisfiedPolicies effect ps εnv = (do
    let term ← SymCC.satisfiedPolicies effect ps εnv
    let footprint := footprints (ps.filterMap λ p => if p.effect = effect then p.toExpr else none) εnv
    .ok { term, footprint }
  )
```

`Cedar.Thm.Opt.isAuthorized.correctness` (theorem, [line 146](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Authorizer.lean#L146))

> Correctness theorem for `Opt.isAuthorized`:
>
> `Opt.isAuthorized` produces the same `term` as `SymCC.isAuthorized`, and
> `Opt.isAuthorized` produces the same `footprint` as `footprints`

```lean
theorem Opt.isAuthorized.correctness (ps : Policies) (εnv : SymEnv) :
  Opt.isAuthorized ps εnv = (do
    let term ← SymCC.isAuthorized ps εnv
    let footprint := footprints (ps.map Policy.toExpr) εnv
    .ok { term, footprint }
  )
```

## Depends on

- [Cedar/SymCC/Authorizer](../../../symcc/part-01/authorizer.md)
- [Cedar/SymCC/Enforcer](../../../symcc/part-01/enforcer.md)
- [SymCCOpt/Authorizer](../../../symccopt/authorizer.md)

## Proof depends on

- [Opt/Compiler](compiler.md)

## Sources

- [Cedar/Thm/SymCC/Opt/Authorizer.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Authorizer.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Opt.Authorizer.json)
