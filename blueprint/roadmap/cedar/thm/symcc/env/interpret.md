---
catalog: module
lean: Cedar.Thm.interpret_entities_find?_some, Cedar.Thm.interpret_entities_find?_none, Cedar.Thm.interpret_entities_isValidEntityUID, Cedar.Thm.interpret_entities_isValidEntityType, Cedar.Thm.interpret_entities_ancestors_none, Cedar.Thm.interpret_entities_ancestors_some, Cedar.Thm.interpret_entities_ancestorsOfType_none, Cedar.Thm.interpret_entities_ancestorsOfType_some, Cedar.Thm.interpret_entities_tags_none, Cedar.Thm.interpret_entities_tags_some, Cedar.Thm.interpret_entities_same_domain, Cedar.Thm.interpret_uf_wf, Cedar.Thm.interpret_εdata_wf, Cedar.Thm.interpret_εntities_wf, Cedar.Thm.interpret_ρeq_wf, Cedar.Thm.interpret_εnv_wf, Cedar.Thm.interpret_εnv_wf_for_expr, Cedar.Thm.interpret_εnv_wf_for_policies, Cedar.Thm.interpret_uf_lit, Cedar.Thm.interpret_εnv_lit
statement: formalized
proof: formalized
---

# Properties of interpretations on symbolic environments

`Cedar.Thm.SymCC.Env.Interpret`, in [Cedar/Thm/SymCC/Env/Interpret.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean).

> This file proves basic lemmas about the `interpret` function
> on symbolic environments.
> -

`Cedar.Thm.interpret_entities_find?_some` (theorem, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean#L41))

```lean
public theorem interpret_entities_find?_some {εs : SymEntities} {I : Interpretation} {ety : EntityType} {d : SymEntityData}
  (h₁ : εs.find? ety = .some d) :
  (εs.interpret I).find? ety = .some (d.interpret I)
```

`Cedar.Thm.interpret_entities_find?_none` (theorem, [line 49](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean#L49))

```lean
public theorem interpret_entities_find?_none {εs : SymEntities} {I : Interpretation} {ety : EntityType}
  (h₁ : εs.find? ety = .none) :
  (εs.interpret I).find? ety = .none
```

`Cedar.Thm.interpret_entities_isValidEntityUID` (theorem, [line 54](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean#L54))

```lean
public theorem interpret_entities_isValidEntityUID (εs : SymEntities) (I : Interpretation) (uid : EntityUID) :
  εs.isValidEntityUID uid = (εs.interpret I).isValidEntityUID uid
```

`Cedar.Thm.interpret_entities_isValidEntityType` (theorem, [line 64](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean#L64))

```lean
public theorem interpret_entities_isValidEntityType (εs : SymEntities) (I : Interpretation) (ety : EntityType) :
  εs.isValidEntityType ety = (εs.interpret I).isValidEntityType ety
```

`Cedar.Thm.interpret_entities_ancestors_none` (theorem, [line 70](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean#L70))

```lean
public theorem interpret_entities_ancestors_none  {εs : SymEntities} {ety : EntityType} (I : Interpretation) :
  εs.ancestors ety = .none →
  (εs.interpret I).ancestors ety = .none
```

`Cedar.Thm.interpret_entities_ancestors_some` (theorem, [line 83](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean#L83))

```lean
public theorem interpret_entities_ancestors_some  {εs : SymEntities} {ety : EntityType} {ancs : Map EntityType UnaryFunction} (I : Interpretation) :
  εs.ancestors ety = .some ancs →
  (εs.interpret I).ancestors ety = .some (ancs.mapOnValues (UnaryFunction.interpret I))
```

`Cedar.Thm.interpret_entities_ancestorsOfType_none` (theorem, [line 93](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean#L93))

```lean
public theorem interpret_entities_ancestorsOfType_none {εs : SymEntities} {ety ancTy : EntityType} {I : Interpretation} :
  εs.ancestorsOfType ety ancTy = .none →
  (εs.interpret I).ancestorsOfType ety ancTy = .none
```

`Cedar.Thm.interpret_entities_ancestorsOfType_some` (theorem, [line 110](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean#L110))

```lean
public theorem interpret_entities_ancestorsOfType_some {εs : SymEntities} {ety ancTy : EntityType} {I : Interpretation} {f : UnaryFunction} :
  εs.ancestorsOfType ety ancTy = .some f →
  (εs.interpret I).ancestorsOfType ety ancTy = .some (f.interpret I)
```

`Cedar.Thm.interpret_entities_tags_none` (theorem, [line 120](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean#L120))

```lean
public theorem interpret_entities_tags_none {εs : SymEntities} {I : Interpretation} {ety : EntityType} :
  εs.tags ety = some none →
  (εs.interpret I).tags ety = some none
```

`Cedar.Thm.interpret_entities_tags_some` (theorem, [line 130](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean#L130))

```lean
public theorem interpret_entities_tags_some {εs : SymEntities} {I : Interpretation} {ety : EntityType} {τs : SymTags} :
  εs.tags ety = some τs →
  (εs.interpret I).tags ety = some (τs.interpret I)
```

`Cedar.Thm.interpret_entities_same_domain` (theorem, [line 141](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean#L141))

```lean
public theorem interpret_entities_same_domain (εs : SymEntities) (I : Interpretation) :
  SameDomain εs (εs.interpret I)
```

`Cedar.Thm.interpret_uf_wf` (theorem, [line 145](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean#L145))

```lean
public theorem interpret_uf_wf {εs : SymEntities} {I : Interpretation} {f : UnaryFunction} :
  I.WellFormed εs →
  f.WellFormed εs →
  (f.interpret I).WellFormed εs ∧
  (f.interpret I).argType = f.argType ∧
  (f.interpret I).outType = f.outType
```

`Cedar.Thm.interpret_εdata_wf` (theorem, [line 163](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean#L163))

```lean
public theorem interpret_εdata_wf {εs : SymEntities} {I : Interpretation} {ety : EntityType} {εd : SymEntityData} :
  I.WellFormed εs →
  εd.WellFormed εs ety →
  (εd.interpret I).WellFormed εs ety
```

`Cedar.Thm.interpret_εntities_wf` (theorem, [line 196](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean#L196))

```lean
public theorem interpret_εntities_wf {εs : SymEntities} {I : Interpretation} :
  εs.WellFormed →
  I.WellFormed εs →
  (εs.interpret I).WellFormed
```

`Cedar.Thm.interpret_ρeq_wf` (theorem, [line 228](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean#L228))

```lean
public theorem interpret_ρeq_wf {εs : SymEntities} {ρeq : SymRequest} {I : Interpretation} :
  I.WellFormed εs →
  ρeq.WellFormed εs →
  (ρeq.interpret I).WellFormed εs
```

`Cedar.Thm.interpret_εnv_wf` (theorem, [line 241](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean#L241))

```lean
public theorem interpret_εnv_wf {εnv : SymEnv} {I : Interpretation} :
  εnv.WellFormed →
  I.WellFormed εnv.entities →
  (εnv.interpret I).WellFormed
```

`Cedar.Thm.interpret_εnv_wf_for_expr` (theorem, [line 253](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean#L253))

```lean
public theorem interpret_εnv_wf_for_expr {x : Expr} {εnv : SymEnv} {I : Interpretation} :
  εnv.WellFormedFor x →
  I.WellFormed εnv.entities →
  (εnv.interpret I).WellFormedFor x
```

`Cedar.Thm.interpret_εnv_wf_for_policies` (theorem, [line 264](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean#L264))

```lean
public theorem interpret_εnv_wf_for_policies {ps : Policies} {εnv : SymEnv} {I : Interpretation} :
  εnv.WellFormedForPolicies ps →
  I.WellFormed εnv.entities →
  (εnv.interpret I).WellFormedForPolicies ps
```

`Cedar.Thm.interpret_uf_lit` (theorem, [line 274](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean#L274))

```lean
public theorem interpret_uf_lit {εs : SymEntities} {I : Interpretation} {f : UnaryFunction} :
  I.WellFormed εs →
  f.WellFormed εs →
  (f.interpret I).isLiteral
```

`Cedar.Thm.interpret_εnv_lit` (theorem, [line 287](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean#L287))

```lean
public theorem interpret_εnv_lit {εnv : SymEnv} {I : Interpretation} :
  εnv.WellFormed →
  I.WellFormed εnv.entities →
  (εnv.interpret I).isLiteral
```

## Depends on

- [Basic properties of well-formed symbolic environments](wf.md)

## Proof depends on

- [Interpretation preserves well-formedness of Terms (Lit)](../term/interpret/lit.md)

## Sources

- [Cedar/Thm/SymCC/Env/Interpret.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Interpret.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Env.Interpret.json)
