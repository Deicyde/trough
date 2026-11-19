---
catalog: module
lean: Cedar.Spec.Residual.isTrue, Cedar.Spec.Residual.isFalse, Cedar.TPE.ResidualPolicy, Cedar.TPE.ResidualPolicy.satisfied, Cedar.TPE.ResidualPolicy.hasError, Cedar.TPE.ResidualPolicy.isFalse, Cedar.TPE.ResidualPolicy.isResidual, Cedar.TPE.ResidualPolicy.erroredWithEffect, Cedar.TPE.ResidualPolicy.falseWithEffect, Cedar.TPE.ResidualPolicy.residualWithEffect, Cedar.TPE.ResidualPolicy.satisfiedWithEffect, Cedar.TPE.Response, Cedar.TPE.isAuthorizedFromResiduals, Cedar.TPE.isAuthorized, Cedar.TPE.Response.reauthorize
statement: formalized
proof: formalized
---

# Cedar/TPE/Authorizer

`Cedar.TPE.Authorizer`, in [Cedar/TPE/Authorizer.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Authorizer.lean).

`Cedar.Spec.Residual.isTrue` (definition, [line 27](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Authorizer.lean#L27))

```lean
def Residual.isTrue : Residual → Bool
```

`Cedar.Spec.Residual.isFalse` (definition, [line 31](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Authorizer.lean#L31))

```lean
def Residual.isFalse : Residual → Bool
```

`Cedar.TPE.ResidualPolicy` (structure, [line 43](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Authorizer.lean#L43))

```lean
structure ResidualPolicy where
  id : PolicyID
  effect : Effect
  residual : Residual
```

`Cedar.TPE.ResidualPolicy.satisfied` (definition, [line 48](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Authorizer.lean#L48))

```lean
def ResidualPolicy.satisfied (policy : ResidualPolicy) : Bool
```

`Cedar.TPE.ResidualPolicy.hasError` (definition, [line 51](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Authorizer.lean#L51))

```lean
def ResidualPolicy.hasError (policy : ResidualPolicy) : Bool
```

`Cedar.TPE.ResidualPolicy.isFalse` (definition, [line 54](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Authorizer.lean#L54))

```lean
def ResidualPolicy.isFalse (policy : ResidualPolicy) : Bool
```

`Cedar.TPE.ResidualPolicy.isResidual` (definition, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Authorizer.lean#L57))

```lean
def ResidualPolicy.isResidual (policy : ResidualPolicy) : Bool
```

`Cedar.TPE.ResidualPolicy.erroredWithEffect` (definition, [line 60](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Authorizer.lean#L60))

```lean
def ResidualPolicy.erroredWithEffect (effect : Effect) (policy : ResidualPolicy) : Option PolicyID
```

`Cedar.TPE.ResidualPolicy.falseWithEffect` (definition, [line 65](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Authorizer.lean#L65))

```lean
def ResidualPolicy.falseWithEffect (effect : Effect) (policy : ResidualPolicy) : Option PolicyID
```

`Cedar.TPE.ResidualPolicy.residualWithEffect` (definition, [line 70](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Authorizer.lean#L70))

```lean
def ResidualPolicy.residualWithEffect (effect : Effect) (policy : ResidualPolicy) : Option PolicyID
```

`Cedar.TPE.ResidualPolicy.satisfiedWithEffect` (definition, [line 75](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Authorizer.lean#L75))

```lean
def ResidualPolicy.satisfiedWithEffect (effect : Effect) (policy : ResidualPolicy) : Option PolicyID
```

`Cedar.TPE.Response` (structure, [line 80](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Authorizer.lean#L80))

```lean
structure Response where
  decision : Option Decision

  satisfiedPermits : Set PolicyID
  falsePermits : Set PolicyID
  errorPermits : Set PolicyID
  residualPermits : Set PolicyID

  satisfiedForbids : Set PolicyID
  falseForbids : Set PolicyID
  errorForbids : Set PolicyID
  residualForbids : Set PolicyID

  residuals : List ResidualPolicy
```

`Cedar.TPE.isAuthorizedFromResiduals` (definition, [line 97](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Authorizer.lean#L97))

> Compute an authorization decision (if possible) from a list of partially
> evaluated policies. Also used for batched evaluation.

```lean
def isAuthorizedFromResiduals (residuals : List ResidualPolicy) : Response
```

`Cedar.TPE.isAuthorized` (definition, [line 141](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Authorizer.lean#L141))

```lean
def isAuthorized (schema : Schema) (policies : List Policy) (req : PartialRequest) (es : PartialEntities) : Except Error Response
```

`Cedar.TPE.Response.reauthorize` (definition, [line 156](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Authorizer.lean#L156))

> Take a partial authorization Response and fully evaluate it using a concrete
> requests and entities. This implementation of this function is fully analogous
> to the concrete `isAuthorized` function, only working with residuals instead of
> policies.

```lean
def Response.reauthorize (response : Response) (req : Request) (es : Entities) : Spec.Response
```

## Depends on

- [Response](../spec/response.md)
- [TPE/Evaluator](evaluator.md)

## Sources

- [Cedar/TPE/Authorizer.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Authorizer.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.TPE.Authorizer.json)
