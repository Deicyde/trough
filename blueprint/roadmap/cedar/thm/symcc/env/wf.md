---
catalog: module
lean: Cedar.Thm.validEntityUID_implies_validEntityType, Cedar.Thm.wf_εnv_for_policies_cons, Cedar.Thm.wf_εnv_for_policies_implies_wf_for_filter, Cedar.Thm.wf_εnv_all_policies_implies_wf_all, Cedar.Thm.wf_env_all_policies_implies_wf_all, Cedar.Thm.wf_εnv_valid_refs_implies_wf_εnv_for_set, Cedar.Thm.wf_εnv_for_policies_iff_wf_εnv_for_set, Cedar.Thm.wf_env_valid_refs_implies_wf_env_for_set, Cedar.Thm.wf_env_for_policies_iff_wf_env_for_set, Cedar.Thm.wf_εnv_implies_wf_ρeq, Cedar.Thm.wf_εs_implies_wf_attrs, Cedar.Thm.wf_εs_implies_wf_ancs, Cedar.Thm.wf_εs_implies_wf_tags, Cedar.Thm.wf_udf_implies_lit, Cedar.Thm.wf_εnv_for_ite_implies, Cedar.Thm.wf_env_for_ite_implies, Cedar.Thm.wf_εnv_for_and_implies, Cedar.Thm.wf_env_for_and_implies, Cedar.Thm.wf_εnv_for_or_implies, Cedar.Thm.wf_env_for_or_implies, Cedar.Thm.wf_εnv_for_binaryApp_implies, Cedar.Thm.wf_env_for_binaryApp_implies, Cedar.Thm.wf_εnv_for_hasAttr_implies, Cedar.Thm.wf_εnv_for_extHasAttr_implies, Cedar.Thm.wf_env_for_hasAttr_implies, Cedar.Thm.wf_env_for_extHasAttr_implies, Cedar.Thm.wf_εnv_for_getAttr_implies, Cedar.Thm.wf_env_for_getAttr_implies, Cedar.Thm.wf_εnv_for_unaryApp_implies, Cedar.Thm.wf_env_for_unaryApp_implies, Cedar.Thm.wf_εnv_for_set_implies, Cedar.Thm.wf_env_for_set_implies, Cedar.Thm.wf_εnv_for_record_implies, Cedar.Thm.wf_env_for_record_implies, Cedar.Thm.wf_εnv_for_call_implies, Cedar.Thm.wf_env_for_call_implies, Cedar.Thm.SameDomain, Cedar.Thm.same_domain_symmetric, Cedar.Thm.wf_term_type_same_domain, Cedar.Thm.wf_term_var_same_domain, Cedar.Thm.wf_term_prim_same_domain, Cedar.Thm.wf_uuf_same_domain, Cedar.Thm.wt_op_same_domain, Cedar.Thm.wf_term_same_domain, Cedar.Thm.wfl_term_same_domain, Cedar.Thm.wf_udf_same_domain, Cedar.Thm.wfp_term_app_same_domain, Cedar.Thm.wf_interpretation_same_domain, Cedar.Thm.wf_ρeq_same_domain, Cedar.Thm.wf_uf_same_domain, Cedar.Thm.wf_εdata_same_domain, Cedar.Thm.prim_valid_refs_same_domain, Cedar.Thm.expr_valid_refs_same_domain, Cedar.Thm.wf_εnv_implies_attrs_wf
statement: formalized
proof: formalized
---

# Basic properties of well-formed symbolic environments

`Cedar.Thm.SymCC.Env.WF`, in [Cedar/Thm/SymCC/Env/WF.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean).

> This file proves basic lemmas about well-formedness predicate on environments.
> -

`Cedar.Thm.validEntityUID_implies_validEntityType` (theorem, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L34))

```lean
public theorem validEntityUID_implies_validEntityType {εs : SymEntities} {uid : EntityUID} :
  εs.isValidEntityUID uid = true →
  εs.isValidEntityType uid.ty = true
```

`Cedar.Thm.wf_εnv_for_policies_cons` (theorem, [line 46](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L46))

```lean
public theorem wf_εnv_for_policies_cons {εnv : SymEnv} {p : Policy} {ps : Policies} :
  εnv.WellFormedForPolicies (p::ps) →
  εnv.WellFormedFor p.toExpr ∧ εnv.WellFormedForPolicies ps
```

`Cedar.Thm.wf_εnv_for_policies_implies_wf_for_filter` (theorem, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L57))

```lean
public theorem wf_εnv_for_policies_implies_wf_for_filter (f : Policy → Bool) {εnv : SymEnv} {ps : Policies}  :
  εnv.WellFormedForPolicies ps →
  εnv.WellFormedForPolicies (ps.filter f)
```

`Cedar.Thm.wf_εnv_all_policies_implies_wf_all` (theorem, [line 67](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L67))

```lean
public theorem wf_εnv_all_policies_implies_wf_all {εnv : SymEnv} {ps : Policies} :
  εnv.WellFormedForPolicies ps →
  ∀ p ∈ ps, εnv.WellFormedFor p.toExpr
```

`Cedar.Thm.wf_env_all_policies_implies_wf_all` (theorem, [line 74](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L74))

```lean
public theorem wf_env_all_policies_implies_wf_all {env : Env} {ps : Policies} :
  env.WellFormedForPolicies ps →
  ∀ p ∈ ps, env.WellFormedFor p.toExpr
```

`Cedar.Thm.wf_εnv_valid_refs_implies_wf_εnv_for_set` (theorem, [line 81](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L81))

```lean
public theorem wf_εnv_valid_refs_implies_wf_εnv_for_set {xs : List Expr} {εnv : SymEnv}
  (hwε : εnv.WellFormed)
  (hvr : ∀ x ∈ xs, εnv.entities.ValidRefsFor x) :
  εnv.WellFormedFor (Expr.set xs)
```

`Cedar.Thm.wf_εnv_for_policies_iff_wf_εnv_for_set` (theorem, [line 91](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L91))

```lean
public theorem wf_εnv_for_policies_iff_wf_εnv_for_set {ps : Policies} {εnv : SymEnv}  :
  εnv.WellFormedForPolicies ps ↔
  εnv.WellFormedFor (Expr.set (ps.map Policy.toExpr))
```

`Cedar.Thm.wf_env_valid_refs_implies_wf_env_for_set` (theorem, [line 112](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L112))

```lean
public theorem wf_env_valid_refs_implies_wf_env_for_set {xs : List Expr} {env : Env}
  (hwε : env.WellFormed)
  (hvr : ∀ x ∈ xs, env.entities.ValidRefsFor x) :
  env.WellFormedFor (Expr.set xs)
```

`Cedar.Thm.wf_env_for_policies_iff_wf_env_for_set` (theorem, [line 122](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L122))

```lean
public theorem wf_env_for_policies_iff_wf_env_for_set {ps : Policies} {env : Env}  :
  env.WellFormedForPolicies ps ↔
  env.WellFormedFor (Expr.set (ps.map Policy.toExpr))
```

`Cedar.Thm.wf_εnv_implies_wf_ρeq` (theorem, [line 143](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L143))

```lean
public theorem wf_εnv_implies_wf_ρeq {εnv : SymEnv} :
  εnv.WellFormed →
  εnv.request.WellFormed εnv.entities
```

`Cedar.Thm.wf_εs_implies_wf_attrs` (theorem, [line 148](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L148))

```lean
public theorem wf_εs_implies_wf_attrs {ety : EntityType} {fₐ : UnaryFunction} {εs : SymEntities}
  (hwε : SymEntities.WellFormed εs)
  (hf  : SymEntities.attrs εs ety = some fₐ) :
  fₐ.WellFormed εs ∧
  fₐ.argType = .entity ety ∧
  fₐ.outType.isCedarRecordType
```

`Cedar.Thm.wf_εs_implies_wf_ancs` (theorem, [line 164](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L164))

```lean
public theorem wf_εs_implies_wf_ancs {ety₁ ety₂ : EntityType} {fₐ : UnaryFunction} {εs : SymEntities}
  (hwε : SymEntities.WellFormed εs)
  (hf  : SymEntities.ancestorsOfType εs ety₁ ety₂ = some fₐ) :
  fₐ.WellFormed εs ∧
  fₐ.argType = .entity ety₁ ∧
  fₐ.outType = .set (.entity ety₂)
```

`Cedar.Thm.wf_εs_implies_wf_tags` (theorem, [line 178](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L178))

```lean
public theorem wf_εs_implies_wf_tags {ety : EntityType} {τs : SymTags} {εs : SymEntities}
  (hwε : SymEntities.WellFormed εs)
  (hτs : εs.tags ety = some (some τs)) :
  τs.WellFormed εs ety
```

`Cedar.Thm.wf_udf_implies_lit` (theorem, [line 187](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L187))

```lean
public theorem wf_udf_implies_lit {f : UDF} {εs : SymEntities} :
  f.WellFormed εs → f.isLiteral
```

`Cedar.Thm.wf_εnv_for_ite_implies` (theorem, [line 197](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L197))

```lean
public theorem wf_εnv_for_ite_implies {x₁ x₂ x₃ : Expr} {εnv : SymEnv} :
  εnv.WellFormedFor (.ite x₁ x₂ x₃) →
  εnv.WellFormedFor x₁ ∧
  εnv.WellFormedFor x₂ ∧
  εnv.WellFormedFor x₃
```

`Cedar.Thm.wf_env_for_ite_implies` (theorem, [line 210](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L210))

```lean
public theorem wf_env_for_ite_implies {x₁ x₂ x₃ : Expr} {env : Env}
  (h₁ : env.WellFormedFor (.ite x₁ x₂ x₃)) :
  env.WellFormedFor x₁ ∧
  env.WellFormedFor x₂ ∧
  env.WellFormedFor x₃
```

`Cedar.Thm.wf_εnv_for_and_implies` (theorem, [line 231](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L231))

```lean
public theorem wf_εnv_for_and_implies {x₁ x₂ : Expr} {εnv : SymEnv} :
  εnv.WellFormedFor (.and x₁ x₂) →
  εnv.WellFormedFor x₁ ∧
  εnv.WellFormedFor x₂
```

`Cedar.Thm.wf_env_for_and_implies` (theorem, [line 237](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L237))

```lean
public theorem wf_env_for_and_implies {x₁ x₂ : Expr} {env : Env} :
  env.WellFormedFor (.and x₁ x₂) →
  env.WellFormedFor x₁ ∧
  env.WellFormedFor x₂
```

`Cedar.Thm.wf_εnv_for_or_implies` (theorem, [line 243](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L243))

```lean
public theorem wf_εnv_for_or_implies {x₁ x₂ : Expr} {εnv : SymEnv} :
  εnv.WellFormedFor (.or x₁ x₂) →
  εnv.WellFormedFor x₁ ∧
  εnv.WellFormedFor x₂
```

`Cedar.Thm.wf_env_for_or_implies` (theorem, [line 249](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L249))

```lean
public theorem wf_env_for_or_implies {x₁ x₂ : Expr} {env : Env} :
  env.WellFormedFor (.or x₁ x₂) →
  env.WellFormedFor x₁ ∧
  env.WellFormedFor x₂
```

`Cedar.Thm.wf_εnv_for_binaryApp_implies` (theorem, [line 255](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L255))

```lean
public theorem wf_εnv_for_binaryApp_implies {op : BinaryOp} {x₁ x₂ : Expr} {εnv : SymEnv} :
  εnv.WellFormedFor (.binaryApp op x₁ x₂) →
  εnv.WellFormedFor x₁ ∧
  εnv.WellFormedFor x₂
```

`Cedar.Thm.wf_env_for_binaryApp_implies` (theorem, [line 261](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L261))

```lean
public theorem wf_env_for_binaryApp_implies {op : BinaryOp} {x₁ x₂ : Expr} {env : Env} :
  env.WellFormedFor (.binaryApp op x₁ x₂) →
  env.WellFormedFor x₁ ∧
  env.WellFormedFor x₂
```

`Cedar.Thm.wf_εnv_for_hasAttr_implies` (theorem, [line 276](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L276))

```lean
public theorem wf_εnv_for_hasAttr_implies {x₁ : Expr} {a : Attr} {εnv : SymEnv} :
  εnv.WellFormedFor (.hasAttr x₁ a) →
  εnv.WellFormedFor x₁
```

`Cedar.Thm.wf_εnv_for_extHasAttr_implies` (theorem, [line 281](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L281))

```lean
public theorem wf_εnv_for_extHasAttr_implies {x₁ : Expr} {a : Attr} {as : List Attr} {εnv : SymEnv} :
  εnv.WellFormedFor (.extHasAttr x₁ a as) →
  εnv.WellFormedFor x₁
```

`Cedar.Thm.wf_env_for_hasAttr_implies` (theorem, [line 286](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L286))

```lean
public theorem wf_env_for_hasAttr_implies {x₁ : Expr} {a : Attr} {env : Env} :
  env.WellFormedFor (.hasAttr x₁ a) →
  env.WellFormedFor x₁
```

`Cedar.Thm.wf_env_for_extHasAttr_implies` (theorem, [line 291](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L291))

```lean
public theorem wf_env_for_extHasAttr_implies {x₁ : Expr} {a : Attr} {as : List Attr} {env : Env} :
  env.WellFormedFor (.extHasAttr x₁ a as) →
  env.WellFormedFor x₁
```

`Cedar.Thm.wf_εnv_for_getAttr_implies` (theorem, [line 296](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L296))

```lean
public theorem wf_εnv_for_getAttr_implies {x₁ : Expr} {a : Attr} {εnv : SymEnv} :
  εnv.WellFormedFor (.getAttr x₁ a) →
  εnv.WellFormedFor x₁
```

`Cedar.Thm.wf_env_for_getAttr_implies` (theorem, [line 301](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L301))

```lean
public theorem wf_env_for_getAttr_implies {x₁ : Expr} {a : Attr} {env : Env} :
  env.WellFormedFor (.getAttr x₁ a) →
  env.WellFormedFor x₁
```

`Cedar.Thm.wf_εnv_for_unaryApp_implies` (theorem, [line 306](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L306))

```lean
public theorem wf_εnv_for_unaryApp_implies {op : UnaryOp} {x₁ : Expr} {εnv : SymEnv} :
  εnv.WellFormedFor (.unaryApp op x₁) →
  εnv.WellFormedFor x₁
```

`Cedar.Thm.wf_env_for_unaryApp_implies` (theorem, [line 311](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L311))

```lean
public theorem wf_env_for_unaryApp_implies {op : UnaryOp} {x₁ : Expr} {env : Env} :
  env.WellFormedFor (.unaryApp op x₁) →
  env.WellFormedFor x₁
```

`Cedar.Thm.wf_εnv_for_set_implies` (theorem, [line 325](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L325))

```lean
public theorem wf_εnv_for_set_implies {xs : List Expr} {εnv : SymEnv} :
  εnv.WellFormedFor (.set xs) →
  ∀ x, x ∈ xs → εnv.WellFormedFor x
```

`Cedar.Thm.wf_env_for_set_implies` (theorem, [line 330](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L330))

```lean
public theorem wf_env_for_set_implies {xs : List Expr} {env : Env} :
  env.WellFormedFor (.set xs) →
  ∀ x, x ∈ xs → env.WellFormedFor x
```

`Cedar.Thm.wf_εnv_for_record_implies` (theorem, [line 335](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L335))

```lean
public theorem wf_εnv_for_record_implies {axs : List (Attr × Expr)} {εnv : SymEnv} :
  εnv.WellFormedFor (.record axs) →
  ∀ ax, ax ∈ axs → εnv.WellFormedFor ax.snd
```

`Cedar.Thm.wf_env_for_record_implies` (theorem, [line 340](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L340))

```lean
public theorem wf_env_for_record_implies {axs : List (Attr × Expr)} {env : Env} :
  env.WellFormedFor (.record axs) →
  ∀ ax, ax ∈ axs → env.WellFormedFor ax.snd
```

`Cedar.Thm.wf_εnv_for_call_implies` (theorem, [line 345](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L345))

```lean
public theorem wf_εnv_for_call_implies {f : ExtFun} {xs : List Expr} {εnv : SymEnv} :
  εnv.WellFormedFor (.call f xs) →
  ∀ x, x ∈ xs → εnv.WellFormedFor x
```

`Cedar.Thm.wf_env_for_call_implies` (theorem, [line 350](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L350))

```lean
public theorem wf_env_for_call_implies {f : ExtFun} {xs : List Expr} {env : Env} :
  env.WellFormedFor (.call f xs) →
  ∀ x, x ∈ xs → env.WellFormedFor x
```

`Cedar.Thm.SameDomain` (definition, [line 356](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L356))

```lean
public def SameDomain (εs₁ εs₂ : SymEntities) : Prop
```

`Cedar.Thm.same_domain_symmetric` (theorem, [line 360](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L360))

```lean
public theorem same_domain_symmetric {εs₁ εs₂ : SymEntities} :
  SameDomain εs₁ εs₂ → SameDomain εs₂ εs₁
```

`Cedar.Thm.wf_term_type_same_domain` (theorem, [line 369](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L369))

```lean
public theorem wf_term_type_same_domain {εs₁ εs₂ : SymEntities} {ty : TermType} :
  SameDomain εs₁ εs₂ →
  TermType.WellFormed εs₁ ty →
  TermType.WellFormed εs₂ ty
```

`Cedar.Thm.wf_term_var_same_domain` (theorem, [line 396](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L396))

```lean
public theorem wf_term_var_same_domain {εs₁ εs₂ : SymEntities} {v : TermVar} :
  SameDomain εs₁ εs₂ →
  TermVar.WellFormed εs₁ v →
  TermVar.WellFormed εs₂ v
```

`Cedar.Thm.wf_term_prim_same_domain` (theorem, [line 405](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L405))

```lean
public theorem wf_term_prim_same_domain {εs₁ εs₂ : SymEntities} {p : TermPrim} :
  SameDomain εs₁ εs₂ →
  TermPrim.WellFormed εs₁ p →
  TermPrim.WellFormed εs₂ p
```

`Cedar.Thm.wf_uuf_same_domain` (theorem, [line 420](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L420))

```lean
public theorem wf_uuf_same_domain {εs₁ εs₂ : SymEntities} {f : UUF} :
  SameDomain εs₁ εs₂ →
  f.WellFormed εs₁ →
  f.WellFormed εs₂
```

`Cedar.Thm.wt_op_same_domain` (theorem, [line 429](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L429))

```lean
public theorem wt_op_same_domain {εs₁ εs₂ : SymEntities} {op : Op} {ts : List Term} {ty : TermType} :
  SameDomain εs₁ εs₂ →
  Op.WellTyped εs₁ op ts ty →
  Op.WellTyped εs₂ op ts ty
```

`Cedar.Thm.wf_term_same_domain` (theorem, [line 470](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L470))

```lean
public theorem wf_term_same_domain {εs₁ εs₂ : SymEntities} {t : Term} :
  SameDomain εs₁ εs₂ →
  t.WellFormed εs₁ →
  t.WellFormed εs₂
```

`Cedar.Thm.wfl_term_same_domain` (theorem, [line 500](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L500))

```lean
public theorem wfl_term_same_domain {εs₁ εs₂ : SymEntities} {t : Term} :
  SameDomain εs₁ εs₂ →
  t.WellFormedLiteral εs₁ →
  t.WellFormedLiteral εs₂
```

`Cedar.Thm.wf_udf_same_domain` (theorem, [line 510](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L510))

```lean
public theorem wf_udf_same_domain {εs₁ εs₂ : SymEntities} {f : UDF} :
  SameDomain εs₁ εs₂ →
  f.WellFormed εs₁ →
  f.WellFormed εs₂
```

`Cedar.Thm.wfp_term_app_same_domain` (theorem, [line 529](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L529))

```lean
public theorem wfp_term_app_same_domain {εs₁ εs₂ : SymEntities} {t : Term} :
  SameDomain εs₁ εs₂ →
  Term.WellFormedPartialApp εs₁ t →
  Term.WellFormedPartialApp εs₂ t
```

`Cedar.Thm.wf_interpretation_same_domain` (theorem, [line 547](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L547))

```lean
public theorem wf_interpretation_same_domain {εs₁ εs₂ : SymEntities} {I : Interpretation} :
  SameDomain εs₁ εs₂ →
  I.WellFormed εs₁ →
  I.WellFormed εs₂
```

`Cedar.Thm.wf_ρeq_same_domain` (theorem, [line 583](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L583))

```lean
public theorem wf_ρeq_same_domain {εs₁ εs₂ : SymEntities} {ρeq : SymRequest} :
  SameDomain εs₁ εs₂ →
  SymRequest.WellFormed εs₁ ρeq →
  SymRequest.WellFormed εs₂ ρeq
```

`Cedar.Thm.wf_uf_same_domain` (theorem, [line 597](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L597))

```lean
public theorem wf_uf_same_domain {εs₁ εs₂ : SymEntities} {f : UnaryFunction} :
  SameDomain εs₁ εs₂ →
  f.WellFormed εs₁ →
  f.WellFormed εs₂
```

`Cedar.Thm.wf_εdata_same_domain` (theorem, [line 608](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L608))

```lean
public theorem wf_εdata_same_domain {εs₁ εs₂ : SymEntities} {ety : EntityType} {εd : SymEntityData} :
  SameDomain εs₁ εs₂ →
  SymEntityData.WellFormed εs₁ ety εd →
  SymEntityData.WellFormed εs₂ ety εd
```

`Cedar.Thm.prim_valid_refs_same_domain` (theorem, [line 631](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L631))

```lean
public theorem prim_valid_refs_same_domain {εs₁ εs₂ : SymEntities} {p : Prim} :
  SameDomain εs₁ εs₂ →
  p.ValidRef (εs₁.isValidEntityUID · = true) →
  p.ValidRef (εs₂.isValidEntityUID · = true)
```

`Cedar.Thm.expr_valid_refs_same_domain` (theorem, [line 642](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L642))

```lean
public theorem expr_valid_refs_same_domain {εs₁ εs₂ : SymEntities} {x : Expr} :
  SameDomain εs₁ εs₂ →
  x.ValidRefs (εs₁.isValidEntityUID · = true) →
  x.ValidRefs (εs₂.isValidEntityUID · = true)
```

`Cedar.Thm.wf_εnv_implies_attrs_wf` (theorem, [line 680](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean#L680))

> `SymEnv` being well-formed implies that any
> attribute function is well-formed

```lean
public theorem wf_εnv_implies_attrs_wf
  {εnv : SymEnv} {ety : EntityType} {attrs : UnaryFunction}
  (hwf : εnv.WellFormed)
  (hattrs_exists : εnv.entities.attrs ety = .some attrs) :
  UnaryFunction.WellFormed εnv.entities attrs ∧
  attrs.argType = .entity ety ∧
  attrs.outType.isCedarRecordType
```

## Depends on

- [Well-formedness and interpretations](../data/basic.md)

## Sources

- [Cedar/Thm/SymCC/Env/WF.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/WF.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Env.WF.json)
