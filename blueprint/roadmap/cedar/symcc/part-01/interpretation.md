---
catalog: module
lean: Cedar.SymCC.Interpretation, Cedar.SymCC.UnaryFunction.interpret, Cedar.SymCC.Factory.option.get', Cedar.SymCC.Factory.ext.ipaddr.addrV4', Cedar.SymCC.Factory.ext.ipaddr.prefixV4', Cedar.SymCC.Factory.ext.ipaddr.addrV6', Cedar.SymCC.Factory.ext.ipaddr.prefixV6', Cedar.SymCC.Term.interpret, Cedar.SymCC.SymRequest.interpret, Cedar.SymCC.SymTags.interpret, Cedar.SymCC.SymEntityData.interpret, Cedar.SymCC.SymEntities.interpret, Cedar.SymCC.SymEnv.interpret
statement: formalized
proof: formalized
---

# Interpretations

`Cedar.SymCC.Interpretation`, in [Cedar/SymCC/Interpretation.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Interpretation.lean).

> An `Interpretation` is a structure that binds term variables to literal terms
> and uninterpreted functions (`UUF`) to interpreted ones (`UDF`). In practice,
> Interpretations are obtained from low-level models returned by SMT solvers.
>
> When a symbolic structure (such as a term, request, function, or entities) is
> interpreted with respect to an Interpretation, the result is a literal symbolic
> structure.

`Cedar.SymCC.Interpretation` (structure, [line 55](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Interpretation.lean#L55))

> An Interpretation consists of three maps:
> - `vars` maps variables to literal terms of the same type;
> - `funs` maps uninterpreted functions to intepreted functions; and
> - `partials` maps partial application terms to literals of the right type.
>
> A partial application term represents the application of an operator to a
> correctly typed literal outside of the operator's domain---for example, the
> application of `option.get` to a `.none` term. The SMTLib language treats all
> such operators as total, and it picks an arbitrary value of the right type as
> the result of the application.

```lean
public structure Interpretation where
  vars : TermVar → Term
  funs : UUF → UDF
  partials : Term → Term
```

`Cedar.SymCC.UnaryFunction.interpret` (definition, [line 61](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Interpretation.lean#L61))

```lean
public def UnaryFunction.interpret (I : Interpretation) : UnaryFunction → UnaryFunction
```

`Cedar.SymCC.Factory.option.get'` (definition, [line 65](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Interpretation.lean#L65))

```lean
public def Factory.option.get' (I : Interpretation) (t : Term) : Term
```

`Cedar.SymCC.Factory.ext.ipaddr.addrV4'` (definition, [line 71](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Interpretation.lean#L71))

```lean
public def Factory.ext.ipaddr.addrV4' (I : Interpretation) (t : Term) : Term
```

`Cedar.SymCC.Factory.ext.ipaddr.prefixV4'` (definition, [line 77](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Interpretation.lean#L77))

```lean
public def Factory.ext.ipaddr.prefixV4' (I : Interpretation) (t : Term) : Term
```

`Cedar.SymCC.Factory.ext.ipaddr.addrV6'` (definition, [line 83](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Interpretation.lean#L83))

```lean
public def Factory.ext.ipaddr.addrV6' (I : Interpretation) (t : Term) : Term
```

`Cedar.SymCC.Factory.ext.ipaddr.prefixV6'` (definition, [line 89](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Interpretation.lean#L89))

```lean
public def Factory.ext.ipaddr.prefixV6' (I : Interpretation) (t : Term) : Term
```

`Cedar.SymCC.Term.interpret` (definition, [line 144](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Interpretation.lean#L144))

```lean
public def Term.interpret (I : Interpretation) : Term → Term
```

`Cedar.SymCC.SymRequest.interpret` (definition, [line 168](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Interpretation.lean#L168))

```lean
public def SymRequest.interpret (I : Interpretation) (req : SymRequest)  : SymRequest
```

`Cedar.SymCC.SymTags.interpret` (definition, [line 176](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Interpretation.lean#L176))

```lean
public def SymTags.interpret (I : Interpretation) (τags : SymTags) : SymTags
```

`Cedar.SymCC.SymEntityData.interpret` (definition, [line 182](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Interpretation.lean#L182))

```lean
public def SymEntityData.interpret (I : Interpretation) (d : SymEntityData) : SymEntityData
```

`Cedar.SymCC.SymEntities.interpret` (definition, [line 190](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Interpretation.lean#L190))

```lean
public def SymEntities.interpret (I : Interpretation) (es : SymEntities)  : SymEntities
```

`Cedar.SymCC.SymEnv.interpret` (definition, [line 194](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Interpretation.lean#L194))

```lean
public def SymEnv.interpret (I : Interpretation) (env : SymEnv) : SymEnv
```

## Depends on

- [Env](env.md)

## Sources

- [Cedar/SymCC/Interpretation.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Interpretation.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.SymCC.Interpretation.json)
