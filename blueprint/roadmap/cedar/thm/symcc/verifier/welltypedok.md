---
catalog: module
lean: Cedar.Thm.verifyEvaluate_is_ok, Cedar.Thm.verifyEvaluatePair_is_ok, Cedar.Thm.compileWithEffect_is_ok, Cedar.Thm.satisfiedPolicies_is_ok, Cedar.Thm.isAuthorized_is_ok, Cedar.Thm.verifyIsAuthorized_is_ok, Cedar.Thm.verifyNeverErrors_is_ok, Cedar.Thm.verifyAlwaysMatches_is_ok, Cedar.Thm.verifyNeverMatches_is_ok, Cedar.Thm.verifyMatchesEquivalent_is_ok, Cedar.Thm.verifyMatchesImplies_is_ok, Cedar.Thm.verifyMatchesDisjoint_is_ok, Cedar.Thm.verifyImplies_is_ok, Cedar.Thm.isAuthorized_allowAll_is_ok, Cedar.Thm.verifyAlwaysAllows_is_ok, Cedar.Thm.verifyAlwaysDenies_is_ok, Cedar.Thm.verifyEquivalent_is_ok, Cedar.Thm.verifyDisjoint_is_ok
statement: formalized
proof: formalized
---

# WellTypedOk

`Cedar.Thm.SymCC.Verifier.WellTypedOk`, in [Cedar/Thm/SymCC/Verifier/WellTypedOk.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/WellTypedOk.lean).

> `verify*` functions always succeed on well-formed inputs. -

`Cedar.Thm.verifyEvaluate_is_ok` (theorem, [line 27](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/WellTypedOk.lean#L27))

> `verifyEvaluate` succeeds on sufficiently well-formed inputs.

```lean
theorem verifyEvaluate_is_ok {φ : Term → Term} {p p' : Policy} {Γ : TypeEnv}
  (hwf : Γ.WellFormed)
  (hwt : wellTypedPolicy p Γ = .ok p') :
  ∃ asserts, verifyEvaluate φ p' (SymEnv.ofEnv Γ) = .ok asserts
```

`Cedar.Thm.verifyEvaluatePair_is_ok` (theorem, [line 39](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/WellTypedOk.lean#L39))

> `verifyEvaluatePair` succeeds on sufficiently well-formed inputs.

```lean
theorem verifyEvaluatePair_is_ok {φ : Term → Term → Term} {p₁ p₁' p₂ p₂' : Policy} {Γ : TypeEnv}
  (hwf : Γ.WellFormed)
  (hwt₁ : wellTypedPolicy p₁ Γ = .ok p₁')
  (hwt₂ : wellTypedPolicy p₂ Γ = .ok p₂') :
  ∃ asserts, verifyEvaluatePair φ p₁' p₂' (SymEnv.ofEnv Γ) = .ok asserts
```

`Cedar.Thm.compileWithEffect_is_ok` (theorem, [line 54](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/WellTypedOk.lean#L54))

> `compileWithEffect` succeeds on sufficiently well-formed inputs.

```lean
theorem compileWithEffect_is_ok (effect : Effect) {p p' : Policy} {Γ : TypeEnv}
  (hwf : Γ.WellFormed)
  (hwt : wellTypedPolicy p Γ = .ok p') :
  ∃ asserts, compileWithEffect effect p' (SymEnv.ofEnv Γ) = .ok asserts
```

`Cedar.Thm.satisfiedPolicies_is_ok` (theorem, [line 67](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/WellTypedOk.lean#L67))

> `satisfiedPolicies` succeeds on sufficiently well-formed inputs.

```lean
theorem satisfiedPolicies_is_ok (effect : Effect) {ps ps' : Policies} {Γ : TypeEnv}
  (hwf : Γ.WellFormed)
  (hwt : wellTypedPolicies ps Γ = .ok ps') :
  ∃ asserts, satisfiedPolicies effect ps' (SymEnv.ofEnv Γ) = .ok asserts
```

`Cedar.Thm.isAuthorized_is_ok` (theorem, [line 103](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/WellTypedOk.lean#L103))

> `isAuthorized` succeeds on sufficiently well-formed inputs.

```lean
theorem isAuthorized_is_ok {ps ps' : Policies} {Γ : TypeEnv}
  (hwf : Γ.WellFormed)
  (hwt : wellTypedPolicies ps Γ = .ok ps') :
  ∃ asserts, isAuthorized ps' (SymEnv.ofEnv Γ) = .ok asserts
```

`Cedar.Thm.verifyIsAuthorized_is_ok` (theorem, [line 114](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/WellTypedOk.lean#L114))

> `verifyIsAuthorized` succeeds on sufficiently well-formed inputs.

```lean
theorem verifyIsAuthorized_is_ok (φ : Term → Term → Term) {ps₁ ps₁' ps₂ ps₂' : Policies} {Γ : TypeEnv}
  (hwf : Γ.WellFormed)
  (hwt₁ : wellTypedPolicies ps₁ Γ = .ok ps₁')
  (hwt₂ : wellTypedPolicies ps₂ Γ = .ok ps₂') :
  ∃ asserts, verifyIsAuthorized φ ps₁' ps₂' (SymEnv.ofEnv Γ) = .ok asserts
```

`Cedar.Thm.verifyNeverErrors_is_ok` (theorem, [line 126](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/WellTypedOk.lean#L126))

> `verifyNeverErrors` succeeds on sufficiently well-formed inputs.

```lean
theorem verifyNeverErrors_is_ok {p p' : Policy} {Γ : TypeEnv}
  (hwf : Γ.WellFormed)
  (hwt : wellTypedPolicy p Γ = .ok p') :
  ∃ asserts, verifyNeverErrors p' (SymEnv.ofEnv Γ) = .ok asserts
```

`Cedar.Thm.verifyAlwaysMatches_is_ok` (theorem, [line 134](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/WellTypedOk.lean#L134))

> `verifyAlwaysMatches` succeeds on sufficiently well-formed inputs.

```lean
theorem verifyAlwaysMatches_is_ok {p p' : Policy} {Γ : TypeEnv}
  (hwf : Γ.WellFormed)
  (hwt : wellTypedPolicy p Γ = .ok p') :
  ∃ asserts, verifyAlwaysMatches p' (SymEnv.ofEnv Γ) = .ok asserts
```

`Cedar.Thm.verifyNeverMatches_is_ok` (theorem, [line 142](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/WellTypedOk.lean#L142))

> `verifyNeverMatches` succeeds on sufficiently well-formed inputs.

```lean
theorem verifyNeverMatches_is_ok {p p' : Policy} {Γ : TypeEnv}
  (hwf : Γ.WellFormed)
  (hwt : wellTypedPolicy p Γ = .ok p') :
  ∃ asserts, verifyNeverMatches p' (SymEnv.ofEnv Γ) = .ok asserts
```

`Cedar.Thm.verifyMatchesEquivalent_is_ok` (theorem, [line 150](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/WellTypedOk.lean#L150))

> `verifyMatchesEquivalent` succeeds on sufficiently well-formed inputs.

```lean
theorem verifyMatchesEquivalent_is_ok {p₁ p₁' p₂ p₂' : Policy} {Γ : TypeEnv}
  (hwf : Γ.WellFormed)
  (hwt₁ : wellTypedPolicy p₁ Γ = .ok p₁')
  (hwt₂ : wellTypedPolicy p₂ Γ = .ok p₂') :
  ∃ asserts, verifyMatchesEquivalent p₁' p₂' (SymEnv.ofEnv Γ) = .ok asserts
```

`Cedar.Thm.verifyMatchesImplies_is_ok` (theorem, [line 159](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/WellTypedOk.lean#L159))

> `verifyMatchesImplies` succeeds on sufficiently well-formed inputs.

```lean
theorem verifyMatchesImplies_is_ok {p₁ p₁' p₂ p₂' : Policy} {Γ : TypeEnv}
  (hwf : Γ.WellFormed)
  (hwt₁ : wellTypedPolicy p₁ Γ = .ok p₁')
  (hwt₂ : wellTypedPolicy p₂ Γ = .ok p₂') :
  ∃ asserts, verifyMatchesImplies p₁' p₂' (SymEnv.ofEnv Γ) = .ok asserts
```

`Cedar.Thm.verifyMatchesDisjoint_is_ok` (theorem, [line 168](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/WellTypedOk.lean#L168))

> `verifyMatchesDisjoint` succeeds on sufficiently well-formed inputs.

```lean
theorem verifyMatchesDisjoint_is_ok {p₁ p₁' p₂ p₂' : Policy} {Γ : TypeEnv}
  (hwf : Γ.WellFormed)
  (hwt₁ : wellTypedPolicy p₁ Γ = .ok p₁')
  (hwt₂ : wellTypedPolicy p₂ Γ = .ok p₂') :
  ∃ asserts, verifyMatchesDisjoint p₁' p₂' (SymEnv.ofEnv Γ) = .ok asserts
```

`Cedar.Thm.verifyImplies_is_ok` (theorem, [line 177](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/WellTypedOk.lean#L177))

> `verifyImplies` succeeds on sufficiently well-formed inputs.

```lean
theorem verifyImplies_is_ok {ps₁ ps₁' ps₂ ps₂' : Policies} {Γ : TypeEnv}
  (hwf : Γ.WellFormed)
  (hwt₁ : wellTypedPolicies ps₁ Γ = .ok ps₁')
  (hwt₂ : wellTypedPolicies ps₂ Γ = .ok ps₂') :
  ∃ asserts, verifyImplies ps₁' ps₂' (SymEnv.ofEnv Γ) = .ok asserts
```

`Cedar.Thm.isAuthorized_allowAll_is_ok` (theorem, [line 185](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/WellTypedOk.lean#L185))

```lean
theorem isAuthorized_allowAll_is_ok (Γ : TypeEnv) :
  isAuthorized [verifyAlwaysAllows.allowAll] (SymEnv.ofEnv Γ) = .ok (.prim (.bool .true))
```

`Cedar.Thm.verifyAlwaysAllows_is_ok` (theorem, [line 197](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/WellTypedOk.lean#L197))

> `verifyAlwaysAllows` succeeds on sufficiently well-formed inputs.

```lean
theorem verifyAlwaysAllows_is_ok {ps ps' : Policies} {Γ : TypeEnv}
  (hwf : Γ.WellFormed)
  (hwt : wellTypedPolicies ps Γ = .ok ps') :
  ∃ asserts, verifyAlwaysAllows ps' (SymEnv.ofEnv Γ) = .ok asserts
```

`Cedar.Thm.verifyAlwaysDenies_is_ok` (theorem, [line 212](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/WellTypedOk.lean#L212))

> `verifyAlwaysDenies` succeeds on sufficiently well-formed inputs.

```lean
theorem verifyAlwaysDenies_is_ok {ps ps' : Policies} {Γ : TypeEnv}
  (hwf : Γ.WellFormed)
  (hwt : wellTypedPolicies ps Γ = .ok ps') :
  ∃ asserts, verifyAlwaysDenies ps' (SymEnv.ofEnv Γ) = .ok asserts
```

`Cedar.Thm.verifyEquivalent_is_ok` (theorem, [line 226](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/WellTypedOk.lean#L226))

> `verifyEquivalent` succeeds on sufficiently well-formed inputs.

```lean
theorem verifyEquivalent_is_ok {ps₁ ps₁' ps₂ ps₂' : Policies} {Γ : TypeEnv}
  (hwf : Γ.WellFormed)
  (hwt₁ : wellTypedPolicies ps₁ Γ = .ok ps₁')
  (hwt₂ : wellTypedPolicies ps₂ Γ = .ok ps₂') :
  ∃ asserts, verifyEquivalent ps₁' ps₂' (SymEnv.ofEnv Γ) = .ok asserts
```

`Cedar.Thm.verifyDisjoint_is_ok` (theorem, [line 235](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/WellTypedOk.lean#L235))

> `verifyDisjoint` succeeds on sufficiently well-formed inputs.

```lean
theorem verifyDisjoint_is_ok {ps₁ ps₁' ps₂ ps₂' : Policies} {Γ : TypeEnv}
  (hwf : Γ.WellFormed)
  (hwt₁ : wellTypedPolicies ps₁ Γ = .ok ps₁')
  (hwt₂ : wellTypedPolicies ps₂ Γ = .ok ps₂') :
  ∃ asserts, verifyDisjoint ps₁' ps₂' (SymEnv.ofEnv Γ) = .ok asserts
```

## Depends on

- [SymCC](../../../symcc-2.md)
- [Typechecker/WF](../../validation-2/typechecker-2/wf.md)

## Proof depends on

- [SymCC/WellTyped](../welltyped.md)
- [SymbolicCompilation](../../symboliccompilation.md)

## Sources

- [Cedar/Thm/SymCC/Verifier/WellTypedOk.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/WellTypedOk.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Verifier.WellTypedOk.json)
