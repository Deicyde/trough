---
catalog: module
lean: Cedar.Thm.IsSoundPolicySlice, Cedar.Thm.sound_slice_transitive, Cedar.Thm.IsSoundPolicySliceFalseDef, Cedar.Thm.is_sound_policy_slice_def_equiv, Cedar.Thm.IsSoundPolicyBound, Cedar.Thm.IsSoundBoundAnalysis, Cedar.Thm.sound_policy_slice_is_equisatisfied, Cedar.Thm.satisfiedPolicies_eq_for_sound_policy_slice, Cedar.Thm.sound_policy_slice_is_equierror, Cedar.Thm.errorPolicies_eq_for_sound_policy_slice
statement: formalized
proof: formalized
---

# Authorization/PolicySlice

`Cedar.Thm.Authorization.PolicySlice`, in [Cedar/Thm/Authorization/PolicySlice.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/PolicySlice.lean).

> This file contains definitions relevant to slicing.

`Cedar.Thm.IsSoundPolicySlice` (definition, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/PolicySlice.lean#L37))

> A policy slice is a subset of a collection of policies.  This slice is sound for
> a given request and entities if every policy in the collection that is not in
> the slice is also not satisfied with respect to the request and entities, and
> doesn't produce an error when evaluated.

```lean
def IsSoundPolicySlice (req : Request) (entities : Entities) (slice policies : Policies) : Prop
```

`Cedar.Thm.sound_slice_transitive` (theorem, [line 43](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/PolicySlice.lean#L43))

```lean
theorem sound_slice_transitive :
  IsSoundPolicySlice r es slice₁ ps →
  IsSoundPolicySlice r es slice₂ slice₁ →
  IsSoundPolicySlice r es slice₂ ps
```

`Cedar.Thm.IsSoundPolicySliceFalseDef` (definition, [line 63](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/PolicySlice.lean#L63))

> Alternate definition of soundness for policy slicing. Rather than showing
> that a policy doesn't evaluate to `true` or error, we can show that it
> does evaluate to `false`.

```lean
def IsSoundPolicySliceFalseDef (req : Request) (entities : Entities) (slice policies : Policies) : Prop
```

`Cedar.Thm.is_sound_policy_slice_def_equiv` (theorem, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/PolicySlice.lean#L69))

```lean
theorem is_sound_policy_slice_def_equiv {req : Request} {entities : Entities} {slice policies : Policies} :
  IsSoundPolicySlice req entities slice policies ↔ IsSoundPolicySliceFalseDef req entities slice policies
```

`Cedar.Thm.IsSoundPolicyBound` (definition, [line 93](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/PolicySlice.lean#L93))

> A bound is sound for a given policy if the bound is satisfied for every request
> and entities for which the policy is satisfied or for which the policy produces
> an error.

```lean
def IsSoundPolicyBound (bound : PolicyBound) (policy : Policy) : Prop
```

`Cedar.Thm.IsSoundBoundAnalysis` (definition, [line 103](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/PolicySlice.lean#L103))

> A bound analysis is sound if it produces sound bounds for all policies.

```lean
def IsSoundBoundAnalysis (ba : BoundAnalysis) : Prop
```

`Cedar.Thm.sound_policy_slice_is_equisatisfied` (theorem, [line 106](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/PolicySlice.lean#L106))

```lean
theorem sound_policy_slice_is_equisatisfied (effect : Effect) {request : Request} {entities : Entities} {slice policies : Policies} :
  IsSoundPolicySlice request entities slice policies →
  slice.filterMap (satisfiedWithEffect effect · request entities) ≡
  policies.filterMap (satisfiedWithEffect effect · request entities)
```

`Cedar.Thm.satisfiedPolicies_eq_for_sound_policy_slice` (theorem, [line 129](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/PolicySlice.lean#L129))

```lean
theorem satisfiedPolicies_eq_for_sound_policy_slice (effect : Effect) {request : Request} {entities : Entities} {slice policies : Policies} :
  IsSoundPolicySlice request entities slice policies →
  satisfiedPolicies effect slice request entities = satisfiedPolicies effect policies request entities
```

`Cedar.Thm.sound_policy_slice_is_equierror` (theorem, [line 138](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/PolicySlice.lean#L138))

```lean
theorem sound_policy_slice_is_equierror {request : Request} {entities : Entities} {slice policies : Policies} :
  IsSoundPolicySlice request entities slice policies →
  slice.filter (hasError · request entities) ≡ policies.filter (hasError · request entities)
```

`Cedar.Thm.errorPolicies_eq_for_sound_policy_slice` (theorem, [line 157](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/PolicySlice.lean#L157))

```lean
theorem errorPolicies_eq_for_sound_policy_slice {request : Request} {entities : Entities} {slice policies : Policies} :
  IsSoundPolicySlice request entities slice policies →
  errorPolicies slice request entities = errorPolicies policies request entities
```

## Depends on

- [Slice/PolicySlice](../../slice/policyslice.md)
- [Spec/Authorizer](../../spec/authorizer.md)
- [List properties](../data/list/basic.md)

## Proof depends on

- [Authorization/Authorizer](authorizer.md)

## Sources

- [Cedar/Thm/Authorization/PolicySlice.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/PolicySlice.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Authorization.PolicySlice.json)
