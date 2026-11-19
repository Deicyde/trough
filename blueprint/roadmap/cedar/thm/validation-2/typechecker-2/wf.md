---
catalog: module
lean: Cedar.Validation.ActionSchema.IsActionEntityType, Cedar.Validation.EntityType.WellFormed, Cedar.Validation.QualifiedType.WellFormed, Cedar.Validation.CedarType.WellFormed, Cedar.Validation.QualifiedType.IsLifted, Cedar.Validation.CedarType.IsLifted, Cedar.Validation.StandardSchemaEntry.WellFormed, Cedar.Validation.EntitySchemaEntry.WellFormed, Cedar.Validation.EntitySchema.WellFormed, Cedar.Validation.EntityUID.WellFormed, Cedar.Validation.EntitySchema.attrs?_eq_map_find?, Cedar.Validation.EntitySchemaEntry.tags?_eq, Cedar.Validation.EntitySchema.tags?_eq_map_find?, Cedar.Validation.EntitySchema.isValidEntityUID_implies_contains, Cedar.Validation.ActionSchemaEntry.WellFormed, Cedar.Validation.ActionSchema.AcyclicActionHierarchy, Cedar.Validation.ActionSchema.TransitiveActionHierarchy, Cedar.Validation.ActionSchema.WellFormed, Cedar.Validation.RequestType.WellFormed, Cedar.Validation.TypeEnv.WellFormed, Cedar.Validation.qty_wf_implies_type_of_wf, Cedar.Validation.wf_record_type_cons, Cedar.Validation.wf_record_implies_wf_attr, Cedar.Validation.CedarType.WellFormed.mono, Cedar.Validation.emptyRecord_wf, Cedar.Validation.emptyRecord_lifted, Cedar.Validation.standardEntry_wf, Cedar.Validation.wf_env_implies_wf_entity_schema_entry, Cedar.Validation.wf_env_implies_wf_tag_type, Cedar.Validation.wf_env_implies_tag_type_lifted, Cedar.Validation.wf_env_implies_wf_attrs, Cedar.Validation.wf_env_implies_attrs_lifted, Cedar.Validation.wf_env_implies_action_wf, Cedar.Validation.wf_env_disjoint_ets_acts, Cedar.Validation.wf_env_implies_wf_request, Cedar.Validation.wf_env_implies_ctx_lifted, Cedar.Validation.wf_env_implies_wf_acts_map, Cedar.Validation.wf_env_implies_wf_ets_map, Cedar.Validation.wf_env_implies_wf_entity_entry, Cedar.Validation.wf_env_implies_wf_action_entity_entry, Cedar.Validation.wf_env_implies_wf_action_entity_ancestor, Cedar.Validation.wf_env_implies_wf_ancestor, Cedar.Validation.wf_env_implies_wf_ancestor_set, Cedar.Validation.wf_env_implies_wf_action_ancestor_set, Cedar.Validation.wf_env_implies_acyclic_action_hierarchy, Cedar.Validation.wf_env_implies_transitive_action_hierarchy, Cedar.Validation.wf_env_implies_ancestors_of_standard_ety_exist, Cedar.Validation.wf_env_implies_ancestors_of_action_is_action, Cedar.Validation.TypeEnv.maps_wf_of_eq
statement: formalized
proof: formalized
---

# Typechecker/WF

`Cedar.Thm.Validation.Typechecker.WF`, in [Cedar/Thm/Validation/Typechecker/WF.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean).

> This file contains the definition of well-formedness of `TypeEnv`
> and related definitions.
> -

`Cedar.Validation.ActionSchema.IsActionEntityType` (definition, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L41))

```lean
def ActionSchema.IsActionEntityType (acts : ActionSchema) (ety : EntityType) : Prop
```

`Cedar.Validation.EntityType.WellFormed` (definition, [line 48](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L48))

> Either a non-action entity type in `env.ets`,
> or an action entity type in `env.acts`.

```lean
def EntityType.WellFormed (env : TypeEnv) (ety : EntityType) : Prop
```

`Cedar.Validation.QualifiedType.WellFormed` (inductive type, [line 52](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L52))

```lean
inductive QualifiedType.WellFormed (env : TypeEnv) : Qualified CedarType → Prop where
  | optional_wf {ty : CedarType}
    (h : CedarType.WellFormed env ty) :
    QualifiedType.WellFormed env (.optional ty)
  | required_wf {ty : CedarType}
    (h : CedarType.WellFormed env ty) :
    QualifiedType.WellFormed env (.required ty)
```

`Cedar.Validation.CedarType.WellFormed` (inductive type, [line 63](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L63))

> Defines when a `CedarType` is well-formed in an `TypeEnv`.

```lean
inductive CedarType.WellFormed (env : TypeEnv) : CedarType → Prop where
  | bool_wf {bty : BoolType} : CedarType.WellFormed env (.bool bty)
  | int_wf : CedarType.WellFormed env .int
  | string_wf : CedarType.WellFormed env .string
  | entity_wf {ety : EntityType}
    (h : EntityType.WellFormed env ety) :
    CedarType.WellFormed env (.entity ety)
  | set_wf {ty : CedarType}
    (h : CedarType.WellFormed env ty) :
    CedarType.WellFormed env (.set ty)
  | record_wf {rty : RecordType}
    -- Well-formed as a `Map`
    (h₁ : rty.WellFormed)
    -- Each attribute type is well-formed
    (h₂ : ∀ attr qty, rty.find? attr = some qty → QualifiedType.WellFormed env qty) :
    CedarType.WellFormed env (.record rty)
  | ext_wf {xty : ExtType} : CedarType.WellFormed env (.ext xty)
```

`Cedar.Validation.QualifiedType.IsLifted` (inductive type, [line 83](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L83))

```lean
inductive QualifiedType.IsLifted : Qualified CedarType → Prop where
  | optional_lifted {ty : CedarType}
    (h : CedarType.IsLifted ty) :
    QualifiedType.IsLifted (.optional ty)
  | required_lifted {ty : CedarType}
    (h : CedarType.IsLifted ty) :
    QualifiedType.IsLifted (.required ty)
```

`Cedar.Validation.CedarType.IsLifted` (inductive type, [line 94](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L94))

> Defines when a `CedarType` does not have any singleton Bool types.

```lean
inductive CedarType.IsLifted : CedarType → Prop where
  | bool_lifted : CedarType.IsLifted (.bool .anyBool)
  | int_lifted : CedarType.IsLifted .int
  | string_lifted : CedarType.IsLifted .string
  | entity_lifted {ety : EntityType} : CedarType.IsLifted (.entity ety)
  | set_lifted {ty : CedarType}
    (h : CedarType.IsLifted ty) :
    CedarType.IsLifted (.set ty)
  | record_lifted {rty : RecordType}
    (h₂ : ∀ attr qty, (attr, qty) ∈ rty.toList → QualifiedType.IsLifted qty) :
    CedarType.IsLifted (.record rty)
  | ext_lifted {xty : ExtType} : CedarType.IsLifted (.ext xty)
```

`Cedar.Validation.StandardSchemaEntry.WellFormed` (definition, [line 108](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L108))

```lean
def StandardSchemaEntry.WellFormed (env : TypeEnv) (entry : StandardSchemaEntry) : Prop
```

`Cedar.Validation.EntitySchemaEntry.WellFormed` (definition, [line 121](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L121))

```lean
def EntitySchemaEntry.WellFormed (env : TypeEnv) (entry : EntitySchemaEntry) : Prop
```

`Cedar.Validation.EntitySchema.WellFormed` (definition, [line 126](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L126))

```lean
def EntitySchema.WellFormed (env : TypeEnv) (ets : EntitySchema) : Prop
```

`Cedar.Validation.EntityUID.WellFormed` (definition, [line 130](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L130))

```lean
def EntityUID.WellFormed (env : TypeEnv) (uid : EntityUID) : Prop
```

`Cedar.Validation.EntitySchema.attrs?_eq_map_find?` (theorem, [line 133](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L133))

```lean
theorem EntitySchema.attrs?_eq_map_find? {ets : EntitySchema} {ety : EntityType} :
  ets.attrs? ety = (ets.find? ety).map EntitySchemaEntry.attrs
```

`Cedar.Validation.EntitySchemaEntry.tags?_eq` (theorem, [line 137](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L137))

```lean
theorem EntitySchemaEntry.tags?_eq {entry : EntitySchemaEntry} :
  entry.tags? = match entry with | .standard ty => ty.tags | .enum _ => none
```

`Cedar.Validation.EntitySchema.tags?_eq_map_find?` (theorem, [line 141](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L141))

```lean
theorem EntitySchema.tags?_eq_map_find? {ets : EntitySchema} {ety : EntityType} :
  ets.tags? ety = (ets.find? ety).map EntitySchemaEntry.tags?
```

`Cedar.Validation.EntitySchema.isValidEntityUID_implies_contains` (theorem, [line 145](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L145))

```lean
theorem EntitySchema.isValidEntityUID_implies_contains {ets : EntitySchema} {uid : EntityUID} :
  ets.isValidEntityUID uid → ets.contains uid.ty
```

`Cedar.Validation.ActionSchemaEntry.WellFormed` (definition, [line 153](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L153))

```lean
def ActionSchemaEntry.WellFormed (env : TypeEnv) (entry : ActionSchemaEntry) : Prop
```

`Cedar.Validation.ActionSchema.AcyclicActionHierarchy` (definition, [line 167](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L167))

```lean
def ActionSchema.AcyclicActionHierarchy (acts : ActionSchema) : Prop
```

`Cedar.Validation.ActionSchema.TransitiveActionHierarchy` (definition, [line 170](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L170))

```lean
def ActionSchema.TransitiveActionHierarchy (acts : ActionSchema) : Prop
```

`Cedar.Validation.ActionSchema.WellFormed` (definition, [line 177](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L177))

```lean
def ActionSchema.WellFormed (env : TypeEnv) (acts : ActionSchema) : Prop
```

`Cedar.Validation.RequestType.WellFormed` (definition, [line 184](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L184))

```lean
def RequestType.WellFormed (env : TypeEnv) (reqty : RequestType) : Prop
```

`Cedar.Validation.TypeEnv.WellFormed` (definition, [line 193](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L193))

```lean
def TypeEnv.WellFormed (env : TypeEnv) : Prop
```

`Cedar.Validation.qty_wf_implies_type_of_wf` (theorem, [line 200](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L200))

```lean
theorem qty_wf_implies_type_of_wf {env : TypeEnv} {qty : Qualified CedarType}
  (h : QualifiedType.WellFormed env qty) :
  CedarType.WellFormed env qty.getType
```

`Cedar.Validation.wf_record_type_cons` (theorem, [line 208](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L208))

```lean
theorem wf_record_type_cons {env : TypeEnv}
  {hd : (Attr × Qualified CedarType)}
  {tl : List (Attr × Qualified CedarType)}
  (hwf : CedarType.WellFormed env (.record (Map.mk (hd :: tl)))) :
  CedarType.WellFormed env hd.snd.getType ∧
  CedarType.WellFormed env (.record (Map.mk tl))
```

`Cedar.Validation.wf_record_implies_wf_attr` (theorem, [line 237](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L237))

```lean
theorem wf_record_implies_wf_attr {env : TypeEnv} {rty : RecordType} {attr : Attr} {qty : QualifiedType}
  (hwf : CedarType.WellFormed env (.record rty))
  (hqty : rty.find? attr = some qty) :
  QualifiedType.WellFormed env qty
```

`Cedar.Validation.CedarType.WellFormed.mono` (theorem, [line 247](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L247))

> A type stays well-formed in an environment that has every entity type of the original.

```lean
theorem CedarType.WellFormed.mono {env₁ env₂ : TypeEnv}
  (hety : ∀ ety, EntityType.WellFormed env₁ ety → EntityType.WellFormed env₂ ety)
  {ty : CedarType} (h : CedarType.WellFormed env₁ ty) :
  CedarType.WellFormed env₂ ty
```

`Cedar.Validation.emptyRecord_wf` (theorem, [line 287](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L287))

> The empty record type is well-formed.

```lean
theorem emptyRecord_wf {env : TypeEnv} :
  (CedarType.record Map.empty).WellFormed env
```

`Cedar.Validation.emptyRecord_lifted` (theorem, [line 293](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L293))

> The empty record type is lifted.

```lean
theorem emptyRecord_lifted : (CedarType.record Map.empty).IsLifted
```

`Cedar.Validation.standardEntry_wf` (theorem, [line 298](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L298))

> A standard entity type without tags is well-formed when its ancestors and attributes are.

```lean
theorem standardEntry_wf {env : TypeEnv} {ancestors : Set EntityType}
  {attrs : RecordType} (hwf : ancestors.WellFormed)
  (hdeclared : ∀ a ∈ ancestors, ∃ entry, env.ets.find? a = some entry)
  (hattrs : (CedarType.record attrs).WellFormed env)
  (hlifted : (CedarType.record attrs).IsLifted) :
  EntitySchemaEntry.WellFormed env (.standard { ancestors, attrs, tags := none })
```

`Cedar.Validation.wf_env_implies_wf_entity_schema_entry` (theorem, [line 307](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L307))

```lean
theorem wf_env_implies_wf_entity_schema_entry {env : TypeEnv} {ety : EntityType} {entry : EntitySchemaEntry}
  (hwf : env.WellFormed)
  (hets : env.ets.find? ety = some entry) :
  entry.WellFormed env
```

`Cedar.Validation.wf_env_implies_wf_tag_type` (theorem, [line 315](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L315))

```lean
theorem wf_env_implies_wf_tag_type {env : TypeEnv} {ety : EntityType} {ty : CedarType}
  (hwf : env.WellFormed)
  (hety : env.ets.tags? ety = .some (.some ty)) :
  CedarType.WellFormed env ty
```

`Cedar.Validation.wf_env_implies_tag_type_lifted` (theorem, [line 331](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L331))

```lean
theorem wf_env_implies_tag_type_lifted {env : TypeEnv} {ety : EntityType} {ty : CedarType}
  (hwf : env.WellFormed)
  (hety : env.ets.tags? ety = .some (.some ty)) :
  ty.IsLifted
```

`Cedar.Validation.wf_env_implies_wf_attrs` (theorem, [line 347](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L347))

```lean
theorem wf_env_implies_wf_attrs {env : TypeEnv} {ety : EntityType} {attrs : RecordType}
  (hwf : env.WellFormed)
  (hattrs : env.ets.attrs? ety = .some attrs) :
  CedarType.WellFormed env (.record attrs)
```

`Cedar.Validation.wf_env_implies_attrs_lifted` (theorem, [line 365](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L365))

```lean
theorem wf_env_implies_attrs_lifted {env : TypeEnv} {ety : EntityType} {attrs : RecordType}
  (hwf : env.WellFormed)
  (hattrs : env.ets.attrs? ety = .some attrs) :
  (CedarType.record attrs).IsLifted
```

`Cedar.Validation.wf_env_implies_action_wf` (theorem, [line 383](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L383))

```lean
theorem wf_env_implies_action_wf {env : TypeEnv}
  (hwf : env.WellFormed) :
  EntityUID.WellFormed env env.reqty.action
```

`Cedar.Validation.wf_env_disjoint_ets_acts` (theorem, [line 392](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L392))

```lean
theorem wf_env_disjoint_ets_acts
  {env : TypeEnv} {uid : EntityUID}
  {ets_entry : EntitySchemaEntry}
  {acts_entry : ActionSchemaEntry}
  (hwf : env.WellFormed)
  (hets : env.ets.find? uid.ty = some ets_entry)
  (hacts : env.acts.find? uid = some acts_entry) :
  False
```

`Cedar.Validation.wf_env_implies_wf_request` (theorem, [line 410](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L410))

> More well-formedness properties of `env.reqty`.

```lean
theorem wf_env_implies_wf_request
  {env : TypeEnv}
  (hwf : env.WellFormed) :
  EntityType.WellFormed env env.reqty.principal ∧
  env.acts.contains env.reqty.action ∧
  EntityType.WellFormed env env.reqty.resource ∧
  (CedarType.record env.reqty.context).WellFormed env
```

`Cedar.Validation.wf_env_implies_ctx_lifted` (theorem, [line 433](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L433))

> More well-formedness properties of `env.reqty`.

```lean
theorem wf_env_implies_ctx_lifted
  {env : TypeEnv}
  (hwf : env.WellFormed) :
  (CedarType.record env.reqty.context).IsLifted
```

`Cedar.Validation.wf_env_implies_wf_acts_map` (theorem, [line 444](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L444))

```lean
theorem wf_env_implies_wf_acts_map
  {env : TypeEnv}
  (hwf : env.WellFormed) :
  Map.WellFormed env.acts
```

`Cedar.Validation.wf_env_implies_wf_ets_map` (theorem, [line 452](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L452))

```lean
theorem wf_env_implies_wf_ets_map
  {env : TypeEnv}
  (hwf : env.WellFormed) :
  Map.WellFormed env.ets
```

`Cedar.Validation.wf_env_implies_wf_entity_entry` (theorem, [line 460](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L460))

```lean
theorem wf_env_implies_wf_entity_entry
  {env : TypeEnv} {ety : EntityType} {entry : EntitySchemaEntry}
  (hwf : env.WellFormed)
  (hfind : env.ets.find? ety = some entry) :
  entry.WellFormed env
```

`Cedar.Validation.wf_env_implies_wf_action_entity_entry` (theorem, [line 469](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L469))

```lean
theorem wf_env_implies_wf_action_entity_entry
  {env : TypeEnv} {uid : EntityUID} {entry : ActionSchemaEntry}
  (hwf : env.WellFormed)
  (hfind : env.acts.find? uid = some entry) :
  entry.WellFormed env
```

`Cedar.Validation.wf_env_implies_wf_action_entity_ancestor` (theorem, [line 479](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L479))

> Ancestor of an action entity should also be an action entity

```lean
theorem wf_env_implies_wf_action_entity_ancestor
  {env : TypeEnv} {uid : EntityUID} {anc : EntityUID}
  {entry : ActionSchemaEntry}
  (hwf : env.WellFormed)
  (hfind : env.acts.find? uid = some entry)
  (hanc : anc ∈ entry.ancestors) :
  ∃ anc_entry,
    env.acts.find? anc = some anc_entry ∧
    anc_entry.WellFormed env
```

`Cedar.Validation.wf_env_implies_wf_ancestor` (theorem, [line 498](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L498))

```lean
theorem wf_env_implies_wf_ancestor
  {env : TypeEnv} {entry : EntitySchemaEntry}
  {ety : EntityType} {anc : EntityType}
  (hwf : env.WellFormed)
  (hfind : env.ets.find? ety = some entry)
  (hanc : anc ∈ entry.ancestors) :
  EntityType.WellFormed env anc
```

`Cedar.Validation.wf_env_implies_wf_ancestor_set` (theorem, [line 519](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L519))

```lean
theorem wf_env_implies_wf_ancestor_set
  {env : TypeEnv} {entry : EntitySchemaEntry}
  {ety : EntityType}
  (hwf : env.WellFormed)
  (hfind : env.ets.find? ety = some entry) :
  Set.WellFormed entry.ancestors
```

`Cedar.Validation.wf_env_implies_wf_action_ancestor_set` (theorem, [line 537](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L537))

```lean
theorem wf_env_implies_wf_action_ancestor_set
  {env : TypeEnv} {entry : ActionSchemaEntry}
  {uid : EntityUID}
  (hwf : env.WellFormed)
  (hfind : env.acts.find? uid = some entry) :
  Set.WellFormed entry.ancestors
```

`Cedar.Validation.wf_env_implies_acyclic_action_hierarchy` (theorem, [line 549](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L549))

```lean
theorem wf_env_implies_acyclic_action_hierarchy
  {env : TypeEnv}
  (hwf : env.WellFormed) :
  env.acts.AcyclicActionHierarchy
```

`Cedar.Validation.wf_env_implies_transitive_action_hierarchy` (theorem, [line 558](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L558))

```lean
theorem wf_env_implies_transitive_action_hierarchy
  {env : TypeEnv}
  (hwf : env.WellFormed) :
  env.acts.TransitiveActionHierarchy
```

`Cedar.Validation.wf_env_implies_ancestors_of_standard_ety_exist` (theorem, [line 567](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L567))

```lean
theorem wf_env_implies_ancestors_of_standard_ety_exist
  {env : TypeEnv} {ety : EntityType} {entry : StandardSchemaEntry}
  (hwf : env.WellFormed)
  (hfind : env.ets.find? ety = some (.standard entry)) :
  ∀ anc ∈ entry.ancestors,
    ∃ entry, env.ets.find? anc = some entry
```

`Cedar.Validation.wf_env_implies_ancestors_of_action_is_action` (theorem, [line 580](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L580))

```lean
theorem wf_env_implies_ancestors_of_action_is_action
  {env : TypeEnv} {uid : EntityUID} {entry : ActionSchemaEntry}
  (hwf : env.WellFormed)
  (hfind : env.acts.find? uid = some entry) :
  ∀ uid ∈ entry.ancestors, env.acts.contains uid
```

`Cedar.Validation.TypeEnv.maps_wf_of_eq` (theorem, [line 593](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean#L593))

> Whether an environment's maps are well-formed does not depend on its request type.

```lean
theorem TypeEnv.maps_wf_of_eq {env₁ env₂ : TypeEnv}
  (hets : env₁.ets = env₂.ets) (hacts : env₁.acts = env₂.acts)
  (h : env₁.ets.WellFormed env₁ ∧ env₁.acts.WellFormed env₁) :
  env₂.ets.WellFormed env₂ ∧ env₂.acts.WellFormed env₂
```

## Depends on

- [Map properties](../../data/map.md)
- [Validation/Types](../../../validation/types.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/WF.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/WF.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.WF.json)
