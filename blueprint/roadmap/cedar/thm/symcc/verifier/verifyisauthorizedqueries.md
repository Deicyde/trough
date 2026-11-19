---
catalog: module
lean: Cedar.Thm.bothAllowOrBothDeny, Cedar.Thm.verifyEquivalent_wbaq, Cedar.Thm.atLeastOneDenies, Cedar.Thm.verifyDisjoint_wbaq, Cedar.Thm.ifFirstAllowsSoDoesSecond, Cedar.Thm.verifyImplies_wbaq, Cedar.Thm.denies, Cedar.Thm.isAuthorized_empty_denies, Cedar.Thm.denies_eq_implies_false, Cedar.Thm.swf_εnv_for_empty_policies, Cedar.Thm.swf_env_for_empty_policies, Cedar.Thm.allows, Cedar.Thm.isAuthorized_allowAll_allows, Cedar.Thm.allows_eq_allowAll_implies, Cedar.Thm.swf_εnv_for_allowAll_policies, Cedar.Thm.swf_env_for_allowAll_policies
statement: formalized
proof: formalized
---

# VerifyIsAuthorizedQueries

`Cedar.Thm.SymCC.Verifier.VerifyIsAuthorizedQueries`, in [Cedar/Thm/SymCC/Verifier/VerifyIsAuthorizedQueries.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorizedQueries.lean).

> This file proves that `verifyIsAuthorized` queries are well-behaved.
> -

`Cedar.Thm.bothAllowOrBothDeny` (definition, [line 27](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorizedQueries.lean#L27))

```lean
def bothAllowOrBothDeny (r₁ r₂ : Response) : Bool
```

`Cedar.Thm.verifyEquivalent_wbaq` (theorem, [line 30](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorizedQueries.lean#L30))

```lean
theorem verifyEquivalent_wbaq :
  WellBehavedIsAuthorizedQuery eq bothAllowOrBothDeny
```

`Cedar.Thm.atLeastOneDenies` (definition, [line 51](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorizedQueries.lean#L51))

```lean
def atLeastOneDenies (r₁ r₂ : Response) : Bool
```

`Cedar.Thm.verifyDisjoint_wbaq` (theorem, [line 54](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorizedQueries.lean#L54))

```lean
theorem verifyDisjoint_wbaq :
  WellBehavedIsAuthorizedQuery verifyDisjoint.disjoint atLeastOneDenies
```

`Cedar.Thm.ifFirstAllowsSoDoesSecond` (definition, [line 77](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorizedQueries.lean#L77))

```lean
def ifFirstAllowsSoDoesSecond (r₁ r₂ : Response) : Bool
```

`Cedar.Thm.verifyImplies_wbaq` (theorem, [line 80](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorizedQueries.lean#L80))

```lean
theorem verifyImplies_wbaq :
  WellBehavedIsAuthorizedQuery implies ifFirstAllowsSoDoesSecond
```

`Cedar.Thm.denies` (definition, [line 105](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorizedQueries.lean#L105))

```lean
def denies (r₁ : Response) : Bool
```

`Cedar.Thm.isAuthorized_empty_denies` (theorem, [line 108](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorizedQueries.lean#L108))

```lean
theorem isAuthorized_empty_denies (env : Env) :
  (Spec.isAuthorized env.request env.entities []).decision = .deny
```

`Cedar.Thm.denies_eq_implies_false` (theorem, [line 113](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorizedQueries.lean#L113))

```lean
theorem denies_eq_implies_false (r₁ : Response) (env : Env) :
  denies r₁ = ifFirstAllowsSoDoesSecond r₁ (Spec.isAuthorized env.request env.entities [])
```

`Cedar.Thm.swf_εnv_for_empty_policies` (theorem, [line 119](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorizedQueries.lean#L119))

```lean
theorem swf_εnv_for_empty_policies {εnv : SymEnv} :
  εnv.StronglyWellFormed → εnv.StronglyWellFormedForPolicies []
```

`Cedar.Thm.swf_env_for_empty_policies` (theorem, [line 124](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorizedQueries.lean#L124))

```lean
theorem swf_env_for_empty_policies {env : Env} :
  env.StronglyWellFormed → env.StronglyWellFormedForPolicies []
```

`Cedar.Thm.allows` (definition, [line 129](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorizedQueries.lean#L129))

```lean
def allows (r₁ : Response) : Bool
```

`Cedar.Thm.isAuthorized_allowAll_allows` (theorem, [line 162](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorizedQueries.lean#L162))

```lean
theorem isAuthorized_allowAll_allows (env : Env) :
  (Spec.isAuthorized env.request env.entities [verifyAlwaysAllows.allowAll]).decision = .allow
```

`Cedar.Thm.allows_eq_allowAll_implies` (theorem, [line 169](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorizedQueries.lean#L169))

```lean
theorem allows_eq_allowAll_implies (r₁ : Response) (env : Env) :
  allows r₁ = ifFirstAllowsSoDoesSecond (Spec.isAuthorized env.request env.entities [verifyAlwaysAllows.allowAll]) r₁
```

`Cedar.Thm.swf_εnv_for_allowAll_policies` (theorem, [line 195](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorizedQueries.lean#L195))

```lean
theorem swf_εnv_for_allowAll_policies {εnv : SymEnv} :
  εnv.StronglyWellFormed → εnv.StronglyWellFormedForPolicies [verifyAlwaysAllows.allowAll]
```

`Cedar.Thm.swf_env_for_allowAll_policies` (theorem, [line 203](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorizedQueries.lean#L203))

```lean
theorem swf_env_for_allowAll_policies {env : Env} :
  env.StronglyWellFormed → env.StronglyWellFormedForPolicies [verifyAlwaysAllows.allowAll]
```

## Depends on

- [VerifyIsAuthorized](verifyisauthorized.md)

## Sources

- [Cedar/Thm/SymCC/Verifier/VerifyIsAuthorizedQueries.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorizedQueries.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Verifier.VerifyIsAuthorizedQueries.json)
