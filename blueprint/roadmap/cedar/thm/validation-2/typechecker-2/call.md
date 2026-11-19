---
catalog: module
lean: Cedar.Thm.type_of_call_args_inversion, Cedar.Thm.type_of_call_inversion, Cedar.Thm.type_of_call_decimal_inversion, Cedar.Thm.type_of_call_decimal_is_sound, Cedar.Thm.type_of_call_datetime_inversion, Cedar.Thm.type_of_call_datetime_is_sound, Cedar.Thm.type_of_call_duration_inversion, Cedar.Thm.type_of_call_duration_is_sound, Cedar.Thm.type_of_call_ip_inversion, Cedar.Thm.type_of_call_ip_is_sound, Cedar.Thm.typeOf_of_binary_call_inversion, Cedar.Thm.IsDecimalComparator, Cedar.Thm.type_of_call_decimal_comparator_inversion, Cedar.Thm.type_of_call_decimal_comparator_is_sound, Cedar.Thm.typeOfIsInRange_ok_inversion, Cedar.Thm.type_of_call_isInRange_inversion, Cedar.Thm.type_of_call_isInRange_comparator_is_sound, Cedar.Thm.IsIpAddrRecognizer, Cedar.Thm.typeOf_of_unary_call_inversion, Cedar.Thm.type_of_call_toTime_inversion, Cedar.Thm.type_of_call_toTime_is_sound, Cedar.Thm.type_of_call_toDate_inversion, Cedar.Thm.type_of_call_toDate_is_sound, Cedar.Thm.type_of_call_offset_inversion, Cedar.Thm.type_of_call_offset_is_sound, Cedar.Thm.type_of_call_durationSince_inversion, Cedar.Thm.type_of_call_durationSince_is_sound, Cedar.Thm.type_of_call_ipAddr_recognizer_inversion, Cedar.Thm.type_of_call_ipAddr_recognizer_is_sound, Cedar.Thm.IsDurationConverter, Cedar.Thm.type_of_call_duration_converter_inversion, Cedar.Thm.type_of_call_duration_converter_is_sound, Cedar.Thm.type_of_call_is_sound, Cedar.Thm.type_of_preserves_evaluation_results_call
statement: formalized
proof: formalized
---

# Typechecker/Call

`Cedar.Thm.Validation.Typechecker.Call`, in [Cedar/Thm/Validation/Typechecker/Call.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean).

> This file proves that typechecking of `.call` expressions is sound.

`Cedar.Thm.type_of_call_args_inversion` (theorem, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L36))

```lean
theorem type_of_call_args_inversion {xs : List Expr} {txs : List TypedExpr} {c : Capabilities} {env : TypeEnv}
  (htxs : (xs.mapM₁ λ x => justType (typeOf x.val c env)) = Except.ok txs) :
  List.Forall₂ (λ xᵢ txᵢ => ∃ cᵢ, typeOf xᵢ c env = Except.ok (txᵢ, cᵢ)) xs txs
```

`Cedar.Thm.type_of_call_inversion` (theorem, [line 61](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L61))

```lean
theorem type_of_call_inversion {xs : List Expr} {c c' : Capabilities} {env : TypeEnv} {tx : TypedExpr}
  (htx : typeOf (Expr.call xfn xs) c env = Except.ok (tx, c')) :
  ∃ txs,
    (∃ ty, tx = .call xfn txs ty) ∧
    List.Forall₂ (λ xᵢ txᵢ => ∃ cᵢ, typeOf xᵢ c env = .ok (txᵢ, cᵢ)) xs txs
```

`Cedar.Thm.type_of_call_decimal_inversion` (theorem, [line 90](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L90))

```lean
theorem type_of_call_decimal_inversion {xs : List Expr} {c c' : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₁ : typeOf (Expr.call .decimal xs) c env = Except.ok (ty, c')) :
  ty.typeOf = .ext .decimal ∧
  c' = ∅ ∧
  ∃ (s : String),
    xs = [.lit (.string s)] ∧
    (Cedar.Spec.Ext.Decimal.decimal s).isSome
```

`Cedar.Thm.type_of_call_decimal_is_sound` (theorem, [line 110](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L110))

```lean
theorem type_of_call_decimal_is_sound {xs : List Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : typeOf (Expr.call .decimal xs) c₁ env = Except.ok (ty, c₂)) :
  GuardedCapabilitiesInvariant (Expr.call .decimal xs) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.call .decimal xs) request entities v ∧ InstanceOfType env v ty.typeOf
```

`Cedar.Thm.type_of_call_datetime_inversion` (theorem, [line 126](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L126))

```lean
theorem type_of_call_datetime_inversion {xs : List Expr} {c c' : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₁ : typeOf (Expr.call .datetime xs) c env = Except.ok (ty, c')) :
  ty.typeOf = .ext .datetime ∧
  c' = ∅ ∧
  ∃ (s : String),
    xs = [.lit (.string s)] ∧
    (Cedar.Spec.Ext.Datetime.parse s).isSome
```

`Cedar.Thm.type_of_call_datetime_is_sound` (theorem, [line 147](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L147))

```lean
theorem type_of_call_datetime_is_sound {xs : List Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : typeOf (Expr.call .datetime xs) c₁ env = Except.ok (ty, c₂)) :
  GuardedCapabilitiesInvariant (Expr.call .datetime xs) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.call .datetime xs) request entities v ∧ InstanceOfType env v ty.typeOf
```

`Cedar.Thm.type_of_call_duration_inversion` (theorem, [line 163](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L163))

```lean
theorem type_of_call_duration_inversion {xs : List Expr} {c c' : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₁ : typeOf (Expr.call .duration xs) c env = Except.ok (ty, c')) :
  ty.typeOf = .ext .duration ∧
  c' = ∅ ∧
  ∃ (s : String),
    xs = [.lit (.string s)] ∧
    (Cedar.Spec.Ext.Datetime.duration s).isSome
```

`Cedar.Thm.type_of_call_duration_is_sound` (theorem, [line 182](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L182))

```lean
theorem type_of_call_duration_is_sound {xs : List Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : typeOf (Expr.call .duration xs) c₁ env = Except.ok (ty, c₂)) :
  GuardedCapabilitiesInvariant (Expr.call .duration xs) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.call .duration xs) request entities v ∧ InstanceOfType env v ty.typeOf
```

`Cedar.Thm.type_of_call_ip_inversion` (theorem, [line 198](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L198))

```lean
theorem type_of_call_ip_inversion {xs : List Expr} {c c' : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₁ : typeOf (Expr.call .ip xs) c env = Except.ok (ty, c')) :
  ty.typeOf = .ext .ipAddr ∧
  c' = ∅ ∧
  ∃ (s : String),
    xs = [.lit (.string s)] ∧
    (Cedar.Spec.Ext.IPAddr.ip s).isSome
```

`Cedar.Thm.type_of_call_ip_is_sound` (theorem, [line 219](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L219))

```lean
theorem type_of_call_ip_is_sound {xs : List Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : typeOf (Expr.call .ip xs) c₁ env = Except.ok (ty, c₂)) :
  GuardedCapabilitiesInvariant (Expr.call .ip xs) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.call .ip xs) request entities v ∧ InstanceOfType env v ty.typeOf
```

`Cedar.Thm.typeOf_of_binary_call_inversion` (theorem, [line 235](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L235))

```lean
theorem typeOf_of_binary_call_inversion {xs : List Expr} {c : Capabilities} {env : TypeEnv} {ty₁ ty₂ : TypedExpr}
  (h₁ : (xs.mapM₁ fun x => justType (typeOf x.val c env)) = Except.ok [ty₁, ty₂]) :
  ∃ x₁ x₂ c₁ c₂,
    xs = [x₁, x₂] ∧
    (typeOf x₁ c env).typeOf = .ok (ty₁.typeOf, c₁) ∧
    (typeOf x₂ c env).typeOf = .ok (ty₂.typeOf, c₂)
```

`Cedar.Thm.IsDecimalComparator` (definition, [line 273](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L273))

```lean
def IsDecimalComparator : ExtFun → Prop
```

`Cedar.Thm.type_of_call_decimal_comparator_inversion` (theorem, [line 280](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L280))

```lean
theorem type_of_call_decimal_comparator_inversion {xfn : ExtFun} {xs : List Expr} {c c' : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₀ : IsDecimalComparator xfn)
  (h₁ : typeOf (Expr.call xfn xs) c env = Except.ok (ty, c')) :
  ty.typeOf = .bool .anyBool ∧
  c' = ∅ ∧
  ∃ (x₁ x₂ : Expr) (c₁ c₂ : Capabilities),
    xs = [x₁, x₂] ∧
    (typeOf x₁ c env).typeOf = .ok ((CedarType.ext .decimal), c₁) ∧
    (typeOf x₂ c env).typeOf = .ok ((CedarType.ext .decimal), c₂)
```

`Cedar.Thm.type_of_call_decimal_comparator_is_sound` (theorem, [line 317](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L317))

```lean
theorem type_of_call_decimal_comparator_is_sound {xfn : ExtFun} {xs : List Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₀ : IsDecimalComparator xfn)
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.call xfn xs) c₁ env = Except.ok (ty, c₂))
  (ih : ∀ (xᵢ : Expr), xᵢ ∈ xs → TypeOfIsSound xᵢ) :
  GuardedCapabilitiesInvariant (Expr.call xfn xs) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.call xfn xs) request entities v ∧ InstanceOfType env v ty.typeOf
```

`Cedar.Thm.typeOfIsInRange_ok_inversion` (theorem, [line 362](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L362))

> Structural inversion for `typeOfIsInRange`: if it succeeds with `.bool .anyBool`,
> then it typed at least two arguments and every argument's type is `.ext .ipAddr`.

```lean
theorem typeOfIsInRange_ok_inversion {tys : List TypedExpr} {xs : List Expr} {ty : TypedExpr} {c' : Capabilities}
  (h : typeOfIsInRange tys xs = Except.ok (ty, c')) :
  ty.typeOf = .bool .anyBool ∧
  c' = ∅ ∧
  2 ≤ tys.length ∧
  ∀ t ∈ tys, t.typeOf = .ext .ipAddr
```

`Cedar.Thm.type_of_call_isInRange_inversion` (theorem, [line 393](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L393))

```lean
theorem type_of_call_isInRange_inversion {xs : List Expr} {c c' : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₁ : typeOf (Expr.call .isInRange xs) c env = Except.ok (ty, c')) :
  ty.typeOf = .bool .anyBool ∧
  c' = ∅ ∧
  ∃ (x₁ : Expr) (xrest : List Expr) (c₁ : Capabilities),
    xs = x₁ :: xrest ∧
    xrest.length > 0 ∧
    (typeOf x₁ c env).typeOf = .ok ((.ext .ipAddr), c₁) ∧
    ∀ xᵢ ∈ xrest, ∃ cᵢ, (typeOf xᵢ c env).typeOf = .ok ((.ext .ipAddr), cᵢ)
```

`Cedar.Thm.type_of_call_isInRange_comparator_is_sound` (theorem, [line 435](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L435))

```lean
theorem type_of_call_isInRange_comparator_is_sound {xs : List Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.call .isInRange xs) c₁ env = Except.ok (ty, c₂))
  (ih : ∀ (xᵢ : Expr), xᵢ ∈ xs → TypeOfIsSound xᵢ) :
  GuardedCapabilitiesInvariant (Expr.call .isInRange xs) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.call .isInRange xs) request entities v ∧ InstanceOfType env v ty.typeOf
```

`Cedar.Thm.IsIpAddrRecognizer` (definition, [line 503](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L503))

```lean
def IsIpAddrRecognizer : ExtFun → Prop
```

`Cedar.Thm.typeOf_of_unary_call_inversion` (theorem, [line 511](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L511))

```lean
theorem typeOf_of_unary_call_inversion {xs : List Expr} {c : Capabilities} {env : TypeEnv} {ty₁ : TypedExpr}
  (h₁ : (xs.mapM₁ fun x => justType (typeOf x.val c env)) = Except.ok [ty₁]) :
  ∃ x₁ c₁,
    xs = [x₁] ∧
    (typeOf x₁ c env).typeOf = .ok (ty₁.typeOf, c₁)
```

`Cedar.Thm.type_of_call_toTime_inversion` (theorem, [line 542](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L542))

```lean
theorem type_of_call_toTime_inversion {xs : List Expr} {c c' : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₁ : typeOf (Expr.call .toTime xs) c env = Except.ok (ty, c')) :
  ty.typeOf = .ext .duration ∧
  c' = ∅ ∧
  ∃ (x₁ : Expr) (c₁ : Capabilities),
    xs = [x₁] ∧
    (typeOf x₁ c env).typeOf = .ok ((CedarType.ext .datetime), c₁)
```

`Cedar.Thm.type_of_call_toTime_is_sound` (theorem, [line 570](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L570))

```lean
theorem type_of_call_toTime_is_sound {xs : List Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.call .toTime xs) c₁ env = Except.ok (ty, c₂))
  (ih : ∀ (xᵢ : Expr), xᵢ ∈ xs → TypeOfIsSound xᵢ) :
  GuardedCapabilitiesInvariant (Expr.call .toTime xs) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.call .toTime xs) request entities v ∧ InstanceOfType env v ty.typeOf
```

`Cedar.Thm.type_of_call_toDate_inversion` (theorem, [line 600](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L600))

```lean
theorem type_of_call_toDate_inversion {xs : List Expr} {c c' : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₁ : typeOf (Expr.call .toDate xs) c env = Except.ok (ty, c')) :
  ty.typeOf = .ext .datetime ∧
  c' = ∅ ∧
  ∃ (x₁ : Expr) (c₁ : Capabilities),
    xs = [x₁] ∧
    (typeOf x₁ c env).typeOf = .ok ((CedarType.ext .datetime), c₁)
```

`Cedar.Thm.type_of_call_toDate_is_sound` (theorem, [line 628](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L628))

```lean
theorem type_of_call_toDate_is_sound {xs : List Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.call .toDate xs) c₁ env = Except.ok (ty, c₂))
  (ih : ∀ (xᵢ : Expr), xᵢ ∈ xs → TypeOfIsSound xᵢ) :
  GuardedCapabilitiesInvariant (Expr.call .toDate xs) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.call .toDate xs) request entities v ∧ InstanceOfType env v ty.typeOf
```

`Cedar.Thm.type_of_call_offset_inversion` (theorem, [line 663](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L663))

```lean
theorem type_of_call_offset_inversion {xs : List Expr} {c c' : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₁ : typeOf (Expr.call .offset xs) c env = Except.ok (ty, c')) :
  ty.typeOf = .ext .datetime ∧
  c' = ∅ ∧
  ∃ (x₁ x₂ : Expr) (c₁ c₂: Capabilities),
    xs = [x₁, x₂] ∧
    (typeOf x₁ c env).typeOf = .ok ((CedarType.ext .datetime), c₁) ∧
    (typeOf x₂ c env).typeOf = .ok ((CedarType.ext .duration), c₂)
```

`Cedar.Thm.type_of_call_offset_is_sound` (theorem, [line 696](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L696))

```lean
theorem type_of_call_offset_is_sound {xs : List Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.call .offset xs) c₁ env = Except.ok (ty, c₂))
  (ih : ∀ (xᵢ : Expr), xᵢ ∈ xs → TypeOfIsSound xᵢ) :
  GuardedCapabilitiesInvariant (Expr.call .offset xs) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.call .offset xs) request entities v ∧ InstanceOfType env v ty.typeOf
```

`Cedar.Thm.type_of_call_durationSince_inversion` (theorem, [line 742](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L742))

```lean
theorem type_of_call_durationSince_inversion {xs : List Expr} {c c' : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₁ : typeOf (Expr.call .durationSince xs) c env = Except.ok (ty, c')) :
  ty.typeOf = .ext .duration ∧
  c' = ∅ ∧
  ∃ (x₁ x₂ : Expr) (c₁ c₂: Capabilities),
    xs = [x₁, x₂] ∧
    (typeOf x₁ c env).typeOf = .ok ((CedarType.ext .datetime), c₁) ∧
    (typeOf x₂ c env).typeOf = .ok ((CedarType.ext .datetime), c₂)
```

`Cedar.Thm.type_of_call_durationSince_is_sound` (theorem, [line 775](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L775))

```lean
theorem type_of_call_durationSince_is_sound {xs : List Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.call .durationSince xs) c₁ env = Except.ok (ty, c₂))
  (ih : ∀ (xᵢ : Expr), xᵢ ∈ xs → TypeOfIsSound xᵢ) :
  GuardedCapabilitiesInvariant (Expr.call .durationSince xs) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.call .durationSince xs) request entities v ∧ InstanceOfType env v ty.typeOf
```

`Cedar.Thm.type_of_call_ipAddr_recognizer_inversion` (theorem, [line 822](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L822))

```lean
theorem type_of_call_ipAddr_recognizer_inversion {xfn : ExtFun} {xs : List Expr} {c c' : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₀ : IsIpAddrRecognizer xfn)
  (h₁ : typeOf (Expr.call xfn xs) c env = Except.ok (ty, c')) :
  ty.typeOf = .bool .anyBool ∧
  c' = ∅ ∧
  ∃ (x₁ : Expr) (c₁ : Capabilities),
    xs = [x₁] ∧
    (typeOf x₁ c env).typeOf = .ok ((.ext .ipAddr), c₁)
```

`Cedar.Thm.type_of_call_ipAddr_recognizer_is_sound` (theorem, [line 854](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L854))

```lean
theorem type_of_call_ipAddr_recognizer_is_sound {xfn : ExtFun} {xs : List Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₀ : IsIpAddrRecognizer xfn)
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.call xfn xs) c₁ env = Except.ok (ty, c₂))
  (ih : ∀ (xᵢ : Expr), xᵢ ∈ xs → TypeOfIsSound xᵢ) :
  GuardedCapabilitiesInvariant (Expr.call xfn xs) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.call xfn xs) request entities v ∧ InstanceOfType env v ty.typeOf
```

`Cedar.Thm.IsDurationConverter` (definition, [line 887](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L887))

```lean
def IsDurationConverter : ExtFun → Prop
```

`Cedar.Thm.type_of_call_duration_converter_inversion` (theorem, [line 895](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L895))

```lean
theorem type_of_call_duration_converter_inversion {xfn : ExtFun} {xs : List Expr} {c c' : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₀ : IsDurationConverter xfn)
  (h₁ : typeOf (Expr.call xfn xs) c env = Except.ok (ty, c')) :
  ty.typeOf = .int ∧
  c' = ∅ ∧
  ∃ (x₁ : Expr) (c₁ : Capabilities),
    xs = [x₁] ∧
    (typeOf x₁ c env).typeOf = .ok ((.ext .duration), c₁)
```

`Cedar.Thm.type_of_call_duration_converter_is_sound` (theorem, [line 927](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L927))

```lean
theorem type_of_call_duration_converter_is_sound {xfn : ExtFun} {xs : List Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₀ : IsDurationConverter xfn)
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.call xfn xs) c₁ env = Except.ok (ty, c₂))
  (ih : ∀ (xᵢ : Expr), xᵢ ∈ xs → TypeOfIsSound xᵢ) :
  GuardedCapabilitiesInvariant (Expr.call xfn xs) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.call xfn xs) request entities v ∧ InstanceOfType env v ty.typeOf
```

`Cedar.Thm.type_of_call_is_sound` (theorem, [line 960](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L960))

```lean
theorem type_of_call_is_sound {xfn : ExtFun} {xs : List Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.call xfn xs) c₁ env = Except.ok (ty, c₂))
  (ih : ∀ (xᵢ : Expr), xᵢ ∈ xs → TypeOfIsSound xᵢ) :
  GuardedCapabilitiesInvariant (Expr.call xfn xs) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.call xfn xs) request entities v ∧ InstanceOfType env v ty.typeOf
```

`Cedar.Thm.type_of_preserves_evaluation_results_call` (theorem, [line 993](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean#L993))

```lean
theorem type_of_preserves_evaluation_results_call {xfn ty c₂ request entities} {xs : List Expr} {tys : List TypedExpr} :
  typeOfCall xfn tys xs = Except.ok (ty, c₂) →
  List.mapM (fun x => evaluate x request entities) xs = List.mapM (fun y => evaluate y.toExpr request entities) tys →
  evaluate (Expr.call xfn xs) request entities = evaluate ty.toExpr request entities
```

## Depends on

- [Typechecker/Basic](basic.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/Call.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Call.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.Call.json)
