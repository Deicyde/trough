---
catalog: module
lean: Cedar.Spec.SlotID, Cedar.Spec.EntityUIDOrSlot, Cedar.Spec.ScopeTemplate, Cedar.Spec.PrincipalScopeTemplate, Cedar.Spec.ResourceScopeTemplate, Cedar.Spec.TemplateID, Cedar.Spec.Template, Cedar.Spec.Templates, Cedar.Spec.SlotEnv, Cedar.Spec.SlotEnv.empty, Cedar.Spec.TemplateLinkedPolicy, Cedar.Spec.TemplateLinkedPolicies, Cedar.Spec.Template.link?, Cedar.Spec.link?
statement: formalized
proof: formalized
---

# Template

`Cedar.Spec.Template`, in [Cedar/Spec/Template.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Template.lean).

> This file defines abstract syntax for Cedar policy templates. In general,
> Cedar operations (e.g., authorization, validation) are defined over policies
> rather than templates. We generate policies from templates by using link?.
> During differential testing, templates are only used during parsing

`Cedar.Spec.SlotID` (abbreviation, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Template.lean#L34))

```lean
public abbrev SlotID
```

`Cedar.Spec.EntityUIDOrSlot` (inductive type, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Template.lean#L36))

```lean
public inductive EntityUIDOrSlot where
  | entityUID (entity : EntityUID)
  | slot (id : SlotID)
deriving Repr, DecidableEq
```

`Cedar.Spec.ScopeTemplate` (inductive type, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Template.lean#L41))

```lean
public inductive ScopeTemplate where
  | any
  | eq (entityOrSlot : EntityUIDOrSlot)
  | mem (entityOrSlot : EntityUIDOrSlot)
  | is (ety : EntityType)
  | isMem (ety : EntityType) (entityOrSlot : EntityUIDOrSlot)
deriving Repr, DecidableEq
```

`Cedar.Spec.PrincipalScopeTemplate` (inductive type, [line 49](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Template.lean#L49))

```lean
public inductive PrincipalScopeTemplate where
  | principalScope (scope : ScopeTemplate)
deriving Repr, DecidableEq
```

`Cedar.Spec.ResourceScopeTemplate` (inductive type, [line 53](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Template.lean#L53))

```lean
public inductive ResourceScopeTemplate where
  | resourceScope (scope : ScopeTemplate)
deriving Repr, DecidableEq
```

`Cedar.Spec.TemplateID` (abbreviation, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Template.lean#L57))

```lean
public abbrev TemplateID
```

`Cedar.Spec.Template` (structure, [line 59](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Template.lean#L59))

```lean
public structure Template where
  effect : Effect
  principalScope : PrincipalScopeTemplate
  actionScope : ActionScope
  resourceScope : ResourceScopeTemplate
  condition : Conditions
deriving Repr, DecidableEq
```

`Cedar.Spec.Templates` (abbreviation, [line 67](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Template.lean#L67))

```lean
public abbrev Templates
```

`Cedar.Spec.SlotEnv` (abbreviation, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Template.lean#L69))

```lean
public abbrev SlotEnv
```

`Cedar.Spec.SlotEnv.empty` (definition, [line 71](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Template.lean#L71))

```lean
public def SlotEnv.empty : SlotEnv
```

`Cedar.Spec.TemplateLinkedPolicy` (structure, [line 73](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Template.lean#L73))

```lean
public structure TemplateLinkedPolicy where
  /-- ID of the link, which for static policies will match the `templateId` -/
  id : PolicyID
  /-- ID of the template, which for static policies will match the `id` -/
  templateId : TemplateID
  slotEnv : SlotEnv
deriving Repr
```

`Cedar.Spec.TemplateLinkedPolicies` (abbreviation, [line 81](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Template.lean#L81))

```lean
public abbrev TemplateLinkedPolicies
```

`Cedar.Spec.Template.link?` (definition, [line 110](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Template.lean#L110))

```lean
public def Template.link? (template : Template) (id : PolicyID) (slotEnv : SlotEnv) : Except String Policy
```

`Cedar.Spec.link?` (definition, [line 126](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Template.lean#L126))

```lean
public def link? (templates : Templates) (links : TemplateLinkedPolicies) : Except String Policies
```

## Depends on

- [Spec/Policy](policy.md)

## Sources

- [Cedar/Spec/Template.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Template.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Spec.Template.json)
