---
catalog: module
lean: Cedar.Spec.Prim.entityUIDs, Cedar.Spec.Value.entityUIDs, Cedar.Spec.Value.entityUID?, Cedar.Spec.Value.record?, Cedar.Spec.Request.entityUIDs, Cedar.Spec.EntityData.entityUIDs, Cedar.Spec.Entities.entityUIDs, Cedar.Spec.Env, Cedar.Spec.Env.entityUIDs, Cedar.Spec.Expr.entityUIDs, Cedar.SymCC.BitVec.int64?, Cedar.SymCC.TermPrim.value?, Cedar.SymCC.Term.value?, Cedar.SymCC.Term.recordValue?, Cedar.SymCC.TermPrim.entityUIDs, Cedar.SymCC.Term.entityUIDs, Cedar.SymCC.Term.entityUID?, Cedar.SymCC.Term.setOfEntityUIDs?, Cedar.SymCC.Term.tag?, Cedar.SymCC.Term.setOfTags?, Cedar.SymCC.SymRequest.entityUIDs, Cedar.SymCC.UDF.entityUIDs, Cedar.SymCC.UnaryFunction.entityUIDs, Cedar.SymCC.SymEntityData.entityUIDs, Cedar.SymCC.SymEntities.entityUIDs, Cedar.SymCC.SymEnv.entityUIDs, Cedar.SymCC.SymRequest.concretize?, Cedar.SymCC.SymEntityData.concretize?, Cedar.SymCC.SymEntities.concretize?, Cedar.SymCC.SymEnv.concretize?
statement: formalized
proof: formalized
---

# Concretizing symbolic environments

`Cedar.SymCC.Concretizer`, in [Cedar/SymCC/Concretizer.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean).

> This file defines functions for concretizing a literal symbolic environment
> (`SymEnv`) into a corresponding concrete environment (`Env`). This functionality
> is needed for extracting counterexamples from models returned by the solver and
> also for proving that Cedar's reduction to SMT (`Cedar.SymCC.compile`) is
> complete.
>
> See Cedar.Thm.SymbolicCompilation for a statement of the completeness theorem.

`Cedar.Spec.Prim.entityUIDs` (definition, [line 43](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L43))

```lean
def Prim.entityUIDs : Prim → Set EntityUID
```

`Cedar.Spec.Value.entityUIDs` (definition, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L47))

```lean
def Value.entityUIDs : Value → Set EntityUID
```

`Cedar.Spec.Value.entityUID?` (definition, [line 63](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L63))

```lean
def Value.entityUID? : Value → Option EntityUID
```

`Cedar.Spec.Value.record?` (definition, [line 67](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L67))

```lean
def Value.record? : Value → Option (Map Attr Value)
```

`Cedar.Spec.Request.entityUIDs` (definition, [line 71](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L71))

```lean
def Request.entityUIDs (r : Request) : Set EntityUID
```

`Cedar.Spec.EntityData.entityUIDs` (definition, [line 77](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L77))

```lean
def EntityData.entityUIDs (d : EntityData) : Set EntityUID
```

`Cedar.Spec.Entities.entityUIDs` (definition, [line 80](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L80))

```lean
def Entities.entityUIDs (es : Entities) : Set EntityUID
```

`Cedar.Spec.Env` (structure, [line 83](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L83))

```lean
structure Env where
  request : Request
  entities : Entities
deriving Repr, DecidableEq
```

`Cedar.Spec.Env.entityUIDs` (definition, [line 88](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L88))

```lean
def Env.entityUIDs (env : Env) : Set EntityUID
```

`Cedar.Spec.Expr.entityUIDs` (definition, [line 91](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L91))

```lean
def Expr.entityUIDs : Expr → Set EntityUID
```

`Cedar.SymCC.BitVec.int64?` (definition, [line 112](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L112))

```lean
def BitVec.int64? {n} (bv : BitVec n) : Option Int64
```

`Cedar.SymCC.TermPrim.value?` (definition, [line 117](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L117))

```lean
def TermPrim.value? : TermPrim → Option Value
```

`Cedar.SymCC.Term.value?` (definition, [line 124](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L124))

```lean
def Term.value? : Term → Option Value
  | .prim p => p.value?
  | .set s _ => do
    let vs ← s.elts.mapM₁ λ ⟨tᵢ, _⟩ => tᵢ.value?
    .some (.set (Set.make vs))
  | .record ats => do
    let avs? ← ats.toList.mapM₂ λ ⟨(aᵢ, tᵢ), _⟩ => attrValue? aᵢ tᵢ
    let avs := avs?.filterMap λ (aᵢ, vᵢ?) => vᵢ?.map (Prod.mk aᵢ)
    .some (.record (Map.mk avs))
  | _ => .none
termination_by t => sizeOf t
decreasing_by
  all_goals simp_wf ; rename_i h
  · have := List.sizeOf_lt_of_mem h
    have := Set.sizeOf_lt_of_elts s
    omega
  · have := Map.sizeOf_lt_of_toList ats
    simp only at *
    omega
```

`Cedar.SymCC.Term.recordValue?` (definition, [line 153](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L153))

```lean
def Term.recordValue? (t : Term) : Option (Map Attr Value)
```

`Cedar.SymCC.TermPrim.entityUIDs` (definition, [line 156](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L156))

```lean
def TermPrim.entityUIDs : TermPrim → Set EntityUID
```

`Cedar.SymCC.Term.entityUIDs` (definition, [line 160](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L160))

```lean
def Term.entityUIDs : Term → Set EntityUID
```

`Cedar.SymCC.Term.entityUID?` (definition, [line 181](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L181))

```lean
def Term.entityUID? : Term → Option EntityUID
```

`Cedar.SymCC.Term.setOfEntityUIDs?` (definition, [line 185](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L185))

```lean
def Term.setOfEntityUIDs? : Term → Option (Set EntityUID)
```

`Cedar.SymCC.Term.tag?` (definition, [line 189](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L189))

```lean
def Term.tag? : Term → Option Tag
```

`Cedar.SymCC.Term.setOfTags?` (definition, [line 193](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L193))

```lean
def Term.setOfTags? : Term → Option (Set Tag)
```

`Cedar.SymCC.SymRequest.entityUIDs` (definition, [line 197](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L197))

```lean
def SymRequest.entityUIDs (ρ : SymRequest) : Set EntityUID
```

`Cedar.SymCC.UDF.entityUIDs` (definition, [line 203](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L203))

```lean
def UDF.entityUIDs (f : UDF) : Set EntityUID
```

`Cedar.SymCC.UnaryFunction.entityUIDs` (definition, [line 207](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L207))

```lean
def UnaryFunction.entityUIDs : UnaryFunction → Set EntityUID
```

`Cedar.SymCC.SymEntityData.entityUIDs` (definition, [line 211](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L211))

```lean
def SymEntityData.entityUIDs (ety : EntityType) (δ : SymEntityData) : Set EntityUID
```

`Cedar.SymCC.SymEntities.entityUIDs` (definition, [line 223](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L223))

```lean
def SymEntities.entityUIDs (εs : SymEntities) : Set EntityUID
```

`Cedar.SymCC.SymEnv.entityUIDs` (definition, [line 226](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L226))

```lean
def SymEnv.entityUIDs (εnv : SymEnv) : Set EntityUID
```

`Cedar.SymCC.SymRequest.concretize?` (definition, [line 229](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L229))

```lean
def SymRequest.concretize? (ρ : SymRequest) : Option Request
```

`Cedar.SymCC.SymEntityData.concretize?` (definition, [line 237](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L237))

```lean
def SymEntityData.concretize? (uid : EntityUID) (δ : SymEntityData) : Option EntityData
```

`Cedar.SymCC.SymEntities.concretize?` (definition, [line 256](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L256))

```lean
def SymEntities.concretize? (uids : Set EntityUID) (εs : SymEntities) : Option Entities
```

`Cedar.SymCC.SymEnv.concretize?` (definition, [line 263](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean#L263))

```lean
def SymEnv.concretize? (x : Expr) (εnv : SymEnv) : Option Env
```

## Depends on

- [Entities](../../spec/entities.md)
- [Spec/Expr](../../spec/expr.md)
- [Request](../../spec/request.md)
- [Env](env.md)

## Sources

- [Cedar/SymCC/Concretizer.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Concretizer.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.SymCC.Concretizer.json)
