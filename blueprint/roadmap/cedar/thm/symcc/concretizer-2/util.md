---
catalog: module
lean: Cedar.Thm.concretize?_ρ_some_eq, Cedar.Thm.concretize?_εs_some_eq, Cedar.Thm.concretize?_entityData?_some_eq, Cedar.Thm.concretize?_δ_isValidEntityUID_implies_wfl, Cedar.Thm.wf_δ_implies_wf_app_attrs, Cedar.Thm.wf_δ_implies_wf_app_ancs, Cedar.Thm.wf_δ_implies_wf_app_tags_keys, Cedar.Thm.lit_tagOf
statement: formalized
proof: formalized
---

# Concretizer/Util

`Cedar.Thm.SymCC.Concretizer.Util`, in [Cedar/Thm/SymCC/Concretizer/Util.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/Util.lean).

> This file contains helper lemmas that are shared by concretization proofs.

`Cedar.Thm.concretize?_ρ_some_eq` (theorem, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/Util.lean#L34))

```lean
public theorem concretize?_ρ_some_eq {ρ : SymRequest} {r : Request} :
  ρ.concretize? = .some r →
  ∃ uidₚ uidₐ uidᵣ ctx,
    ρ.principal.entityUID? = .some uidₚ ∧
    ρ.action.entityUID? = .some uidₐ ∧
    ρ.resource.entityUID? = .some uidᵣ ∧
    ρ.context.recordValue? = .some ctx ∧
    r = {principal := uidₚ, action := uidₐ, resource := uidᵣ, context := ctx}
```

`Cedar.Thm.concretize?_εs_some_eq` (theorem, [line 48](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/Util.lean#L48))

```lean
public theorem concretize?_εs_some_eq {uids : Set EntityUID} {εs : SymEntities} {es : Entities} :
  εs.concretize? uids = .some es →
   ∃ eds,
    (uids ∪ εs.entityUIDs).elts.mapM (SymEntities.concretize?.entityData? εs) = some eds ∧
    Map.make eds = es
```

`Cedar.Thm.concretize?_entityData?_some_eq` (theorem, [line 59](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/Util.lean#L59))

```lean
public theorem concretize?_entityData?_some_eq {uid : EntityUID} {ed : EntityUID × EntityData} {εs : SymEntities} :
  SymEntities.concretize?.entityData? εs uid = some ed →
  ∃ δ d,
    Map.find? εs uid.ty = some δ ∧
    SymEntityData.concretize? uid δ = some d ∧
    (uid, d) = ed
```

`Cedar.Thm.concretize?_δ_isValidEntityUID_implies_wfl` (theorem, [line 71](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/Util.lean#L71))

```lean
public theorem concretize?_δ_isValidEntityUID_implies_wfl {uid : EntityUID} {δ : SymEntityData} {εs : SymEntities} :
  Map.find? εs uid.ty = some δ →
  SymEntityData.concretize?.isValidEntityUID uid δ = true →
  Term.WellFormedLiteral εs (Term.entity uid)
```

`Cedar.Thm.wf_δ_implies_wf_app_attrs` (theorem, [line 84](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/Util.lean#L84))

```lean
public theorem wf_δ_implies_wf_app_attrs {uid : EntityUID} {δ : SymEntityData} {εs : SymEntities} :
  δ.WellFormed εs uid.ty →
  (Term.entity uid).WellFormed εs →
  (app δ.attrs (Term.entity uid)).WellFormed εs ∧
  (app δ.attrs (Term.entity uid)).typeOf = δ.attrs.outType
```

`Cedar.Thm.wf_δ_implies_wf_app_ancs` (theorem, [line 94](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/Util.lean#L94))

```lean
public theorem wf_δ_implies_wf_app_ancs {uid : EntityUID} {δ : SymEntityData} {εs : SymEntities} {ancTy : EntityType} {ancUF : UnaryFunction} :
  δ.WellFormed εs uid.ty →
  (Term.entity uid).WellFormed εs →
  δ.ancestors.find? ancTy = ancUF →
  (app ancUF (Term.entity uid)).WellFormed εs ∧
  (app ancUF (Term.entity uid)).typeOf = .set (.entity ancTy)
```

`Cedar.Thm.wf_δ_implies_wf_app_tags_keys` (theorem, [line 107](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/Util.lean#L107))

```lean
public theorem wf_δ_implies_wf_app_tags_keys {uid : EntityUID} {δ : SymEntityData} {τs : SymTags} :
  δ.WellFormed εs uid.ty →
  (Term.entity uid).WellFormed εs →
  δ.tags = .some τs →
  (app τs.keys (Term.entity uid)).WellFormed εs ∧
  (app τs.keys (Term.entity uid)).typeOf = .set .string
```

`Cedar.Thm.lit_tagOf` (theorem, [line 121](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/Util.lean#L121))

> …

```lean
public theorem lit_tagOf (uid : EntityUID) (tag : Tag) :
  (tagOf (Term.entity uid) (Term.string tag)).isLiteral
```

## Depends on

- [Well-formedness and interpretations](../data/basic.md)

## Proof depends on

- [Well-formed terms and factory functions](../term/wf.md)

## Sources

- [Cedar/Thm/SymCC/Concretizer/Util.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/Util.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Concretizer.Util.json)
