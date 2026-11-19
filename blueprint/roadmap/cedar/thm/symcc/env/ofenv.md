---
catalog: module
lean: Cedar.Thm.ofEnv_preserves_entity, Cedar.Thm.ofEnv_preserves_action_entity, Cedar.Thm.ofActionType_contains_act, Cedar.Thm.ofEnv_entity_exists, Cedar.Thm.ofEnv_action_entity_exists, Cedar.Thm.ofSchema_find?_ets, Cedar.Thm.ofSchema_find?_acts, Cedar.Thm.ofEnv_wf_entity, Cedar.Thm.ofEnv_preserves_tags, Cedar.Thm.ofEnv_preserves_entity_attr, Cedar.Thm.ofRecordType_eq_map, Cedar.Thm.ofType_wf, Cedar.Thm.wf_ofType_right_inverse_cedarType?, Cedar.Thm.ofEnv_request_is_wf, Cedar.Thm.ofEnv_request_is_basic, Cedar.Thm.ofEnv_request_is_swf, Cedar.Thm.ofStandardEntityType_is_wf, Cedar.Thm.ofEnumEntityType_is_wf, Cedar.Thm.ofEntityType_is_wf, Cedar.Thm.ofActionType_ancsUDF_is_wf, Cedar.Thm.ofActionType_is_wf, Cedar.Thm.ofEnv_entities_is_wf, Cedar.Thm.entity_uid_wf_implies_sym_entities_is_valid_entity_uid, Cedar.Thm.env_valid_uid_implies_sym_env_valid_uid, Cedar.Thm.ofEnv_entities_valid_refs_for_wt_expr, Cedar.Thm.ValidRefs_invariant_under_liftBoolTypes, Cedar.Thm.wellTypedPolicy_ok_implies_valid_refs, Cedar.Thm.ofEnv_entities_find?_some, Cedar.Thm.ancsUDF_app, Cedar.Thm.in_ancsUDF_implies_in_ancestors, Cedar.Thm.in_ancestors_implies_in_ancsUDF, Cedar.Thm.ofEnv_entities_is_acyclic, Cedar.Thm.ofEnv_entities_is_transitive, Cedar.Thm.ofEnv_entities_is_partitioned, Cedar.Thm.ofEnv_entities_is_hierarchical, Cedar.Thm.ofEnv_entities_is_swf, Cedar.Thm.ofEnv_is_wf, Cedar.Thm.ofEnv_is_swf, Cedar.Thm.ofEnv_wf_for_expr, Cedar.Thm.ofEnv_swf_for_expr, Cedar.Thm.ofEnv_swf_for_policy, Cedar.Thm.ofEnv_swf_for_policies
statement: formalized
proof: formalized
---

# ofEnv

`Cedar.Thm.SymCC.Env.ofEnv`, in [Cedar/Thm/SymCC/Env/ofEnv.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean).

> This file contains some facts about `SymEnv.ofEnv`.

`Cedar.Thm.ofEnv_preserves_entity` (theorem, [line 30](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L30))

> If some entity exists in `Γ`, then it must
> also exists in `SymEnv.ofEnv Γ` with the corresponding `SymEntityData`

```lean
theorem ofEnv_preserves_entity
  {Γ : TypeEnv} {εnv : SymEnv} {ety : EntityType} {entry : EntitySchemaEntry}
  (hεnv : εnv = SymEnv.ofEnv Γ)
  (hfind : Map.find? Γ.ets ety = some entry) :
  Map.find? εnv.entities ety = some (SymEntityData.ofEntityType ety entry)
```

`Cedar.Thm.ofEnv_preserves_action_entity` (theorem, [line 54](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L54))

> An action entity type is compiled correctly

```lean
theorem ofEnv_preserves_action_entity
  {Γ : TypeEnv} {uid : EntityUID}
  (hwf : Γ.WellFormed)
  (hmem : Map.contains Γ.acts uid) :
  Map.find? (SymEnv.ofEnv Γ).entities uid.ty =
    some (SymEntityData.ofActionType
      uid.ty
      (Γ.acts.toList.map λ (act, _) => act.ty).eraseDups
      Γ.acts)
```

`Cedar.Thm.ofActionType_contains_act` (theorem, [line 124](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L124))

```lean
theorem ofActionType_contains_act
  {Γ : TypeEnv} {uid : EntityUID}
  (hwf : Γ.WellFormed)
  (hmem : Map.contains Γ.acts uid) :
  ∃ m, (SymEntityData.ofActionType
      uid.ty
      (Γ.acts.toList.map λ (act, _) => act.ty).eraseDups
      Γ.acts).members = some m ∧ m.contains uid.eid
```

`Cedar.Thm.ofEnv_entity_exists` (theorem, [line 149](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L149))

> A variant of `ofEnv_preserves_entity`

```lean
theorem ofEnv_entity_exists
  {Γ : TypeEnv} {ety : EntityType}
  (hmem : Map.contains Γ.ets ety) :
  Map.contains (SymEnv.ofEnv Γ).entities ety
```

`Cedar.Thm.ofEnv_action_entity_exists` (theorem, [line 160](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L160))

> Similar to `ofEnv_entity_exists` but for action entities

```lean
theorem ofEnv_action_entity_exists
  {Γ : TypeEnv} {uid : EntityUID}
  (hwf : Γ.WellFormed)
  (hmem : Map.contains Γ.acts uid) :
  Map.contains (SymEnv.ofEnv Γ).entities uid.ty
```

`Cedar.Thm.ofSchema_find?_ets` (theorem, [line 169](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L169))

```lean
theorem ofSchema_find?_ets
  {Γ : TypeEnv} {ety : EntityType} {entry : EntitySchemaEntry}
  (hfind_ety : Γ.ets.find? ety = .some entry) :
  Map.find? (SymEntities.ofSchema Γ.ets Γ.acts) ety
  = .some (SymEntityData.ofEntityType ety entry)
```

`Cedar.Thm.ofSchema_find?_acts` (theorem, [line 198](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L198))

```lean
theorem ofSchema_find?_acts
  {Γ : TypeEnv} {uid : EntityUID} {entry : ActionSchemaEntry}
  (hwf_Γ : Γ.WellFormed)
  (hfind_uid : Γ.acts.find? uid = .some entry) :
  Map.find? (SymEntities.ofSchema Γ.ets Γ.acts) uid.ty
  = .some (SymEntityData.ofActionType
    uid.ty
    (Γ.acts.toList.map λ (act, _) => act.ty).eraseDups
    Γ.acts)
```

`Cedar.Thm.ofEnv_wf_entity` (theorem, [line 260](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L260))

```lean
theorem ofEnv_wf_entity
  {Γ : TypeEnv} {ety : EntityType}
  (hwf : Γ.WellFormed)
  (hwf_ety : EntityType.WellFormed Γ ety) :
  (SymEntities.ofSchema Γ.ets Γ.acts).isValidEntityType ety
```

`Cedar.Thm.ofEnv_preserves_tags` (theorem, [line 281](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L281))

> Lemma that if a concrete `Γ : TypeEnv` has tags for
> a particular entity type, then `SymEnv.ofEnv Γ` must also
> have tags for it

```lean
theorem ofEnv_preserves_tags
  {Γ : TypeEnv} {ety : EntityType} {ty : CedarType}
  (h : Γ.ets.tags? ety = some (some ty)) :
  ∃ τags : SymTags,
    (SymEnv.ofEnv Γ).entities.tags ety = some (some τags) ∧
    τags.vals.outType = TermType.ofType ty
```

`Cedar.Thm.ofEnv_preserves_entity_attr` (theorem, [line 314](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L314))

> Show that `SymEnv.ofEnv Γ` preserves the result of attribute lookup

```lean
theorem ofEnv_preserves_entity_attr
  {Γ : TypeEnv} {εnv : SymEnv}
  {rty : RecordType} {ety : EntityType}
  (hεnv : εnv = SymEnv.ofEnv Γ)
  (hattrs_exists : Γ.ets.attrs? ety = some rty)
  (hwf : εnv.WellFormed) :
  ∃ attrs : UnaryFunction,
    εnv.entities.attrs ety = .some attrs ∧
    UnaryFunction.WellFormed εnv.entities attrs ∧
    attrs.argType = .entity ety ∧
    attrs.outType = .record (Map.mk (TermType.ofRecordType rty.toList))
```

`Cedar.Thm.ofRecordType_eq_map` (theorem, [line 374](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L374))

```lean
theorem ofRecordType_eq_map
  {rty : List (Attr × QualifiedType)} :
  TermType.ofRecordType rty =
    rty.map (fun x => (x.fst, TermType.ofQualifiedType x.snd))
```

`Cedar.Thm.ofType_wf` (theorem, [line 388](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L388))

> `TermType.ofType` of well-formed `CedarType` is well-formed
> (under the compiled `SymEnv`).

```lean
theorem ofType_wf
  {Γ : TypeEnv} {ty : CedarType}
  (hwf : Γ.WellFormed)
  (hwf_ty : CedarType.WellFormed Γ ty) :
  (TermType.ofType ty).WellFormed (SymEnv.ofEnv Γ).entities
```

`Cedar.Thm.wf_ofType_right_inverse_cedarType?` (theorem, [line 445](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L445))

> `TermType.ofType` is a right inverse of `CedarType.cedarType?`
> when applied to a well-formed `CedarType`.

```lean
theorem wf_ofType_right_inverse_cedarType?
  {Γ : TypeEnv} {ty : CedarType}
  (hwf : Γ.WellFormed)
  (hwf_ty : CedarType.WellFormed Γ ty) :
  (TermType.ofType ty).cedarType? = ty.liftBoolTypes
```

`Cedar.Thm.ofEnv_request_is_wf` (theorem, [line 550](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L550))

```lean
theorem ofEnv_request_is_wf
  {Γ : TypeEnv}
  (hwf : Γ.WellFormed) :
  (SymEnv.ofEnv Γ).request.WellFormed
    (SymEnv.ofEnv Γ).entities
```

`Cedar.Thm.ofEnv_request_is_basic` (theorem, [line 595](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L595))

```lean
theorem ofEnv_request_is_basic
  {Γ : TypeEnv} :
  (SymEnv.ofEnv Γ).request.IsBasic
```

`Cedar.Thm.ofEnv_request_is_swf` (theorem, [line 606](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L606))

```lean
theorem ofEnv_request_is_swf
  {Γ : TypeEnv}
  (hwf : Γ.WellFormed) :
  (SymEnv.ofEnv Γ).request.StronglyWellFormed
    (SymEnv.ofEnv Γ).entities
```

`Cedar.Thm.ofStandardEntityType_is_wf` (theorem, [line 617](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L617))

```lean
theorem ofStandardEntityType_is_wf
  {ety : EntityType} {Γ : TypeEnv} {entry : StandardSchemaEntry}
  (hwf : Γ.WellFormed)
  (hfind : Map.find? Γ.ets ety = some (.standard entry)) :
  SymEntityData.WellFormed
    (SymEnv.ofEnv Γ).entities
    ety
    (SymEntityData.ofStandardEntityType ety entry)
```

`Cedar.Thm.ofEnumEntityType_is_wf` (theorem, [line 733](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L733))

```lean
theorem ofEnumEntityType_is_wf
  {ety : EntityType} {Γ : TypeEnv} {eids : Set String}
  (hwf : Γ.WellFormed)
  (hfind : Map.find? Γ.ets ety = some (.enum eids)) :
  SymEntityData.WellFormed
    (SymEnv.ofEnv Γ).entities
    ety
    (SymEntityData.ofEnumEntityType ety eids)
```

`Cedar.Thm.ofEntityType_is_wf` (theorem, [line 763](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L763))

```lean
theorem ofEntityType_is_wf
  {ety : EntityType} {Γ : TypeEnv} {entry : EntitySchemaEntry}
  (hwf : Γ.WellFormed)
  (hfind : Map.find? Γ.ets ety = some entry) :
  SymEntityData.WellFormed
    (SymEnv.ofEnv Γ).entities
    ety
    (SymEntityData.ofEntityType ety entry)
```

`Cedar.Thm.ofActionType_ancsUDF_is_wf` (theorem, [line 780](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L780))

> A technical lemma that `SymEntityData.ofActionType.ancsUDF`
> produces a well-formed UDF.

```lean
theorem ofActionType_ancsUDF_is_wf
  {uid : EntityUID} {Γ : TypeEnv}
  {anc : EntityType}
  {anc_f : UnaryFunction} (hwf : Γ.WellFormed)
  (hanc :
    (SymEntityData.ofActionType
      uid.ty
      (List.map (fun x => x.fst.ty) (Map.toList Γ.acts)).eraseDups
      Γ.acts).ancestors.find? anc = some anc_f) :
  UnaryFunction.WellFormed
    (SymEnv.ofEnv Γ).entities
    (SymEntityData.ofActionType.ancsUDF uid.ty Γ.acts anc) ∧
  (SymEntityData.ofActionType.ancsUDF uid.ty Γ.acts anc).argType = .entity uid.ty ∧
  (SymEntityData.ofActionType.ancsUDF uid.ty Γ.acts anc).outType = .set (.entity anc)
```

`Cedar.Thm.ofActionType_is_wf` (theorem, [line 947](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L947))

```lean
theorem ofActionType_is_wf
  {uid : EntityUID} {Γ : TypeEnv} {entry : ActionSchemaEntry}
  (hwf : Γ.WellFormed)
  (hfind : Map.find? Γ.acts uid = some entry) :
  SymEntityData.WellFormed
    (SymEnv.ofEnv Γ).entities
    uid.ty
    (SymEntityData.ofActionType
      uid.ty
      (List.map (fun x => x.fst.ty) (Map.toList Γ.acts)).eraseDups
      Γ.acts)
```

`Cedar.Thm.ofEnv_entities_is_wf` (theorem, [line 998](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L998))

```lean
theorem ofEnv_entities_is_wf
  {Γ : TypeEnv}
  (hwf : Γ.WellFormed) :
  (SymEnv.ofEnv Γ).entities.WellFormed
```

`Cedar.Thm.entity_uid_wf_implies_sym_entities_is_valid_entity_uid` (theorem, [line 1033](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L1033))

```lean
theorem entity_uid_wf_implies_sym_entities_is_valid_entity_uid
  {Γ : TypeEnv} {uid : EntityUID}
  (hwf : Γ.WellFormed)
  (huid : EntityUID.WellFormed Γ uid) :
  (SymEnv.ofEnv Γ).entities.isValidEntityUID uid
```

`Cedar.Thm.env_valid_uid_implies_sym_env_valid_uid` (theorem, [line 1080](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L1080))

```lean
theorem env_valid_uid_implies_sym_env_valid_uid
  {Γ : TypeEnv} {env : Env} {uid : EntityUID}
  (hinst : InstanceOfWellFormedEnvironment env.request env.entities Γ)
  (hcont_uid : Map.contains env.entities uid = true) :
  (SymEnv.ofEnv Γ).entities.isValidEntityUID uid = true
```

`Cedar.Thm.ofEnv_entities_valid_refs_for_wt_expr` (theorem, [line 1120](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L1120))

> Given a well-formed environment and a well-typed expression in that environment,
> we show that the expression satisfies `ValidRefs`

```lean
theorem ofEnv_entities_valid_refs_for_wt_expr
  {Γ : TypeEnv} {tx : TypedExpr}
  (hwf : Γ.WellFormed)
  (hwt : TypedExpr.WellTyped Γ tx) :
  tx.toExpr.ValidRefs ((SymEnv.ofEnv Γ).entities.isValidEntityUID ·)
```

`Cedar.Thm.ValidRefs_invariant_under_liftBoolTypes` (theorem, [line 1203](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L1203))

> Removing `liftBoolTypes` does not affect `ValidRefs`

```lean
theorem ValidRefs_invariant_under_liftBoolTypes
  {tx : TypedExpr} {f : EntityUID → Prop}
  (hrefs : tx.liftBoolTypes.toExpr.ValidRefs f) :
  tx.toExpr.ValidRefs f
```

`Cedar.Thm.wellTypedPolicy_ok_implies_valid_refs` (theorem, [line 1332](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L1332))

```lean
theorem wellTypedPolicy_ok_implies_valid_refs
  {Γ : TypeEnv} {p p' : Policy}
  (hwf : Γ.WellFormed)
  (hok : wellTypedPolicy p Γ = .ok p') :
  p'.toExpr.ValidRefs ((SymEnv.ofEnv Γ).entities.isValidEntityUID ·)
```

`Cedar.Thm.ofEnv_entities_find?_some` (theorem, [line 1360](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L1360))

```lean
theorem ofEnv_entities_find?_some
  {Γ : TypeEnv} {ety : EntityType} {δ : SymEntityData}
  (hwf : Γ.WellFormed)
  (hfind : Map.find? (SymEnv.ofEnv Γ).entities ety = .some δ) :
  ((∃ entry, Map.find? Γ.ets ety = .some (.standard entry) ∧
    δ = SymEntityData.ofStandardEntityType ety entry) ∨
  (∃ entry, Map.find? Γ.ets ety = .some (.enum entry) ∧
    δ = SymEntityData.ofEnumEntityType ety entry)) ∨
  (∃ uid entry,
    uid.ty = ety ∧
    Map.find? Γ.acts uid = .some entry ∧
    δ = SymEntityData.ofActionType uid.ty
      (List.map (fun x => x.fst.ty) (Map.toList Γ.acts)).eraseDups
      Γ.acts)
```

`Cedar.Thm.ancsUDF_app` (theorem, [line 1409](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L1409))

> Simplifies `SymEntityData.ofActionType.ancsUDF`

```lean
theorem ancsUDF_app
  {Γ : TypeEnv} {uid : EntityUID} {entry : ActionSchemaEntry}
  (ancTy : EntityType)
  (hwf : Γ.WellFormed)
  (hfind : Map.find? Γ.acts uid = some entry) :
  Factory.app
      (SymEntityData.ofActionType.ancsUDF uid.ty Γ.acts ancTy)
      (Term.entity uid)
    = SymEntityData.ofActionType.ancsTerm ancTy entry.ancestors.toList
```

`Cedar.Thm.in_ancsUDF_implies_in_ancestors` (theorem, [line 1439](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L1439))

```lean
theorem in_ancsUDF_implies_in_ancestors
  {Γ : TypeEnv} {uid uid' : EntityUID} {ancTy : EntityType}
  (hwf : Γ.WellFormed)
  (hmem : uid' ∈ (Factory.app (SymEntityData.ofActionType.ancsUDF uid.ty Γ.acts ancTy) (Term.entity uid)).entityUIDs) :
  ∃ entry,
    uid'.ty = ancTy ∧
    Map.find? Γ.acts uid = some entry ∧
    uid' ∈ entry.ancestors
```

`Cedar.Thm.in_ancestors_implies_in_ancsUDF` (theorem, [line 1503](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L1503))

```lean
theorem in_ancestors_implies_in_ancsUDF
  {Γ : TypeEnv} {uid uid' : EntityUID} {entry : ActionSchemaEntry}
  (hwf : Γ.WellFormed)
  (hfind : Map.find? Γ.acts uid = some entry)
  (hmem : uid' ∈ entry.ancestors):
  uid' ∈ (Factory.app (SymEntityData.ofActionType.ancsUDF uid.ty Γ.acts uid'.ty) (Term.entity uid)).entityUIDs
```

`Cedar.Thm.ofEnv_entities_is_acyclic` (theorem, [line 1529](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L1529))

```lean
theorem ofEnv_entities_is_acyclic
  {Γ : TypeEnv}
  (hwf : Γ.WellFormed) :
  (SymEnv.ofEnv Γ).entities.Acyclic
```

`Cedar.Thm.ofEnv_entities_is_transitive` (theorem, [line 1576](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L1576))

```lean
theorem ofEnv_entities_is_transitive
  {Γ : TypeEnv}
  (hwf : Γ.WellFormed) :
  (SymEnv.ofEnv Γ).entities.Transitive
```

`Cedar.Thm.ofEnv_entities_is_partitioned` (theorem, [line 1804](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L1804))

```lean
theorem ofEnv_entities_is_partitioned
  {Γ : TypeEnv}
  (hwf : Γ.WellFormed) :
  (SymEnv.ofEnv Γ).entities.Partitioned
```

`Cedar.Thm.ofEnv_entities_is_hierarchical` (theorem, [line 1854](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L1854))

```lean
theorem ofEnv_entities_is_hierarchical
  {Γ : TypeEnv}
  (hwf : Γ.WellFormed) :
  (SymEnv.ofEnv Γ).entities.Hierarchical
```

`Cedar.Thm.ofEnv_entities_is_swf` (theorem, [line 1865](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L1865))

```lean
theorem ofEnv_entities_is_swf
  {Γ : TypeEnv}
  (hwf : Γ.WellFormed) :
  (SymEnv.ofEnv Γ).entities.StronglyWellFormed
```

`Cedar.Thm.ofEnv_is_wf` (theorem, [line 1879](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L1879))

> Main well-formedness theorem for `SymEnv.ofEnv`,
> which says that if the input environment `Γ` is well-formed,
> then `SymEnv.ofEnv Γ` is well-formed.

```lean
theorem ofEnv_is_wf
  {Γ : TypeEnv}
  (hwf : Γ.WellFormed) :
  (SymEnv.ofEnv Γ).WellFormed
```

`Cedar.Thm.ofEnv_is_swf` (theorem, [line 1893](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L1893))

> A stronger version of `ofEnv_is_wf` that
> shows that `SymEnv.ofEnv Γ` is strongly well-formed.

```lean
theorem ofEnv_is_swf
  {Γ : TypeEnv}
  (hwf : Γ.WellFormed) :
  (SymEnv.ofEnv Γ).StronglyWellFormed
```

`Cedar.Thm.ofEnv_wf_for_expr` (theorem, [line 1907](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L1907))

> If an expression is well-typed in a concrete, well-formed `TypeEnv`,
> then it must also be well-formed in the compiled symbolic environment.

```lean
theorem ofEnv_wf_for_expr
  {Γ : TypeEnv} {tx : TypedExpr}
  (hwf : Γ.WellFormed)
  (hwt : TypedExpr.WellTyped Γ tx) :
  (SymEnv.ofEnv Γ).WellFormedFor tx.toExpr
```

`Cedar.Thm.ofEnv_swf_for_expr` (theorem, [line 1918](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L1918))

> Similar to `ofEnv_wf_for_expr` but for `StronglyWellFormedFor`.

```lean
theorem ofEnv_swf_for_expr
  {Γ : TypeEnv} {tx : TypedExpr}
  (hwf : Γ.WellFormed)
  (hwt : TypedExpr.WellTyped Γ tx) :
  (SymEnv.ofEnv Γ).StronglyWellFormedFor tx.toExpr
```

`Cedar.Thm.ofEnv_swf_for_policy` (theorem, [line 1929](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L1929))

> Similar to `ofEnv_swf_for_expr` but for `StronglyWellFormedForPolicy`.

```lean
theorem ofEnv_swf_for_policy
  {Γ : TypeEnv} {p p' : Policy}
  (hwf : Γ.WellFormed)
  (hwt : wellTypedPolicy p Γ = .ok p') :
  (SymEnv.ofEnv Γ).StronglyWellFormedForPolicy p'
```

`Cedar.Thm.ofEnv_swf_for_policies` (theorem, [line 1940](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean#L1940))

> Similar to `ofEnv_swf_for_expr` but for `StronglyWellFormedForPolicies`.

```lean
theorem ofEnv_swf_for_policies
  {Γ : TypeEnv} {ps ps' : Policies}
  (hwf : Γ.WellFormed)
  (hwt : wellTypedPolicies ps Γ = .ok ps') :
  (SymEnv.ofEnv Γ).StronglyWellFormedForPolicies ps'
```

## Depends on

- [SymCC](../../../symcc-2.md)
- [Strongly well-formed ancestor relations](../data/hierarchy.md)
- [Typechecker/Types](../../validation-2/typechecker-2/types.md)
- [Expr/Definition](../../welltyped/expr-2/definition.md)

## Proof depends on

- [Lemmas about List.mapUnion operator](../../data/mapunion.md)
- [Properties of literal terms](../term/lit.md)
- [UDF](../term/udf.md)
- [Well-formed terms and factory functions](../term/wf.md)
- [Expr/Typechecking](../../welltyped/expr-2/typechecking.md)

## Sources

- [Cedar/Thm/SymCC/Env/ofEnv.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/ofEnv.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Env.ofEnv.json)
