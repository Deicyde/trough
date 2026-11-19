---
catalog: module
lean: Cedar.Spec.Effect, Cedar.Spec.Scope, Cedar.Spec.PrincipalScope, Cedar.Spec.ResourceScope, Cedar.Spec.ActionScope, Cedar.Spec.PolicyID, Cedar.Spec.ConditionKind, Cedar.Spec.Condition, Cedar.Spec.Conditions, Cedar.Spec.Policy, Cedar.Spec.Policies, Cedar.Spec.PrincipalScope.scope, Cedar.Spec.ResourceScope.scope, Cedar.Spec.Var.eqEntityUID, Cedar.Spec.Var.inEntityUID, Cedar.Spec.Var.isEntityType, Cedar.Spec.Scope.toExpr, Cedar.Spec.PrincipalScope.toExpr, Cedar.Spec.ResourceScope.toExpr, Cedar.Spec.ActionScope.toExpr, Cedar.Spec.Condition.toExpr, Cedar.Spec.Conditions.toExpr, Cedar.Spec.Policy.toExpr, Cedar.Spec.Scope.bound, Cedar.Spec.Policy.allowAll
statement: formalized
proof: formalized
---

# Spec/Policy

`Cedar.Spec.Policy`, in [Cedar/Spec/Policy.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean).

> This file defines abstract syntax for Cedar policies.

`Cedar.Spec.Effect` (inductive type, [line 27](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L27))

```lean
public inductive Effect where
  | permit
  | forbid
```

`Cedar.Spec.Scope` (inductive type, [line 31](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L31))

```lean
public inductive Scope where
  | any
  | eq (entity : EntityUID)
  | mem (entity : EntityUID)
  | is (ety : EntityType)
  | isMem (ety : EntityType) (entity : EntityUID)
```

`Cedar.Spec.PrincipalScope` (inductive type, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L38))

```lean
public inductive PrincipalScope where
  | principalScope (scope : Scope)
```

`Cedar.Spec.ResourceScope` (inductive type, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L41))

```lean
public inductive ResourceScope where
  | resourceScope (scope : Scope)
```

`Cedar.Spec.ActionScope` (inductive type, [line 53](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L53))

> This definition of the ActionScope is more liberal than what is allowed by
> Cedar's concrete grammar. In particular, the concrete grammar doesn't allow `is`
> constraints in action scopes (e.g., `action is ety`), while our abstract grammar
> does. Restricting action scopes in this way is not necessary for proving any
> properties of Cedar; it is done in the concrete grammar for usability (since
> `is` constraints on actions can be expressed using groups instead). We're
> choosing the more liberal modeling here for uniformity and simplicity.

```lean
public inductive ActionScope where
  | actionScope (scope : Scope)
  | actionInAny (ls : List EntityUID)
```

`Cedar.Spec.PolicyID` (abbreviation, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L57))

```lean
public abbrev PolicyID
```

`Cedar.Spec.ConditionKind` (inductive type, [line 59](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L59))

```lean
public inductive ConditionKind where
  | when
  | unless
```

`Cedar.Spec.Condition` (structure, [line 63](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L63))

```lean
public structure Condition where
  kind : ConditionKind
  body : Expr
```

`Cedar.Spec.Conditions` (abbreviation, [line 67](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L67))

```lean
public abbrev Conditions
```

`Cedar.Spec.Policy` (structure, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L69))

```lean
public structure Policy where
  id : PolicyID
  effect : Effect
  principalScope : PrincipalScope
  actionScope : ActionScope
  resourceScope : ResourceScope
  condition : Conditions
```

`Cedar.Spec.Policies` (abbreviation, [line 77](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L77))

```lean
public abbrev Policies
```

`Cedar.Spec.PrincipalScope.scope` (definition, [line 79](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L79))

```lean
public def PrincipalScope.scope : PrincipalScope → Scope
```

`Cedar.Spec.ResourceScope.scope` (definition, [line 82](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L82))

```lean
public def ResourceScope.scope : ResourceScope → Scope
```

`Cedar.Spec.Var.eqEntityUID` (definition, [line 85](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L85))

```lean
public def Var.eqEntityUID (v : Var) (uid : EntityUID) : Expr
```

`Cedar.Spec.Var.inEntityUID` (definition, [line 88](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L88))

```lean
public def Var.inEntityUID (v : Var) (uid : EntityUID) : Expr
```

`Cedar.Spec.Var.isEntityType` (definition, [line 91](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L91))

```lean
public def Var.isEntityType (v : Var) (ety : EntityType) : Expr
```

`Cedar.Spec.Scope.toExpr` (definition, [line 94](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L94))

```lean
public def Scope.toExpr (s : Scope) (v : Var) : Expr
```

`Cedar.Spec.PrincipalScope.toExpr` (definition, [line 102](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L102))

```lean
public def PrincipalScope.toExpr : PrincipalScope → Expr
```

`Cedar.Spec.ResourceScope.toExpr` (definition, [line 105](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L105))

```lean
public def ResourceScope.toExpr : ResourceScope → Expr
```

`Cedar.Spec.ActionScope.toExpr` (definition, [line 108](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L108))

```lean
public def ActionScope.toExpr : ActionScope → Expr
```

`Cedar.Spec.Condition.toExpr` (definition, [line 114](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L114))

```lean
public def Condition.toExpr (c : Condition) : Expr
```

`Cedar.Spec.Conditions.toExpr` (definition, [line 120](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L120))

```lean
public def Conditions.toExpr (cs : Conditions) : Expr
```

`Cedar.Spec.Policy.toExpr` (definition, [line 126](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L126))

```lean
public def Policy.toExpr (p : Policy) : Expr
```

`Cedar.Spec.Scope.bound` (definition, [line 135](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L135))

```lean
public def Scope.bound : Scope → Option EntityUID
```

`Cedar.Spec.Policy.allowAll` (definition, [line 142](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean#L142))

> The trivial allow-all policy

```lean
public def Policy.allowAll : Policy
```

## Depends on

- [Spec/Expr](expr.md)

## Sources

- [Cedar/Spec/Policy.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Policy.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Spec.Policy.json)
