---
catalog: module
lean: Cedar.SymCC.SymEntities.SameOn, Cedar.SymCC.SymEnv.SameOn, Cedar.Thm.mem_footprints_iff, Cedar.Thm.mem_footprint_option_entity, Cedar.Thm.mem_footprint_exists_wf, Cedar.Thm.mem_footprint_compile_exists_swf, Cedar.Thm.mem_footprint_wf, Cedar.Thm.mem_footprints_wf, Cedar.Thm.footprints_empty, Cedar.Thm.footprints_singleton, Cedar.Thm.footprints_append, Cedar.Thm.footprint_subset_footprints
statement: formalized
proof: formalized
---

# Footprint

`Cedar.Thm.SymCC.Enforcer.Footprint`, in [Cedar/Thm/SymCC/Enforcer/Footprint.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Footprint.lean).

> This file proves properties of the `footprints` function in `Cedar/SymCC/Enforcer.lean`.
> -

`Cedar.SymCC.SymEntities.SameOn` (definition, [line 32](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Footprint.lean#L32))

```lean
def SymEntities.SameOn (εs : SymEntities) (ft : Set Term) (I₁ I₂ : Interpretation) : Prop
```

`Cedar.SymCC.SymEnv.SameOn` (definition, [line 45](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Footprint.lean#L45))

```lean
def SymEnv.SameOn (εnv : SymEnv) (ft : Set Term) (I₁ I₂ : Interpretation) : Prop
```

`Cedar.Thm.mem_footprints_iff` (theorem, [line 55](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Footprint.lean#L55))

```lean
theorem mem_footprints_iff {xs : List Expr} {εnv : SymEnv} {t : Term} :
  t ∈ footprints xs εnv ↔ ∃ x ∈ xs, t ∈ footprint x εnv
```

`Cedar.Thm.mem_footprint_option_entity` (theorem, [line 103](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Footprint.lean#L103))

```lean
theorem mem_footprint_option_entity {x : Expr} {εnv : SymEnv} {t : Term} :
  t ∈ footprint x εnv → ∃ ety, t.typeOf = .option (.entity ety)
```

`Cedar.Thm.mem_footprint_exists_wf` (theorem, [line 225](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Footprint.lean#L225))

```lean
theorem mem_footprint_exists_wf {x : Expr} {tₑ : Term} {env : Env} {εnv : SymEnv} :
  εnv.WellFormedFor x →
  env.WellFormedFor x →
  tₑ ∈ footprint x εnv →
  ∃ xₑ,
    εnv.WellFormedFor xₑ ∧
    env.WellFormedFor xₑ ∧
    compile xₑ εnv = .ok tₑ
```

`Cedar.Thm.mem_footprint_compile_exists_swf` (theorem, [line 243](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Footprint.lean#L243))

```lean
theorem mem_footprint_compile_exists_swf {x : Expr} {tₑ : Term} {env : Env} {εnv : SymEnv} :
  εnv.StronglyWellFormedFor x →
  env.StronglyWellFormedFor x →
  tₑ ∈ footprint x εnv →
  ∃ xₑ,
    εnv.StronglyWellFormedFor xₑ ∧
    env.StronglyWellFormedFor xₑ ∧
    compile xₑ εnv = .ok tₑ
```

`Cedar.Thm.mem_footprint_wf` (theorem, [line 260](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Footprint.lean#L260))

```lean
theorem mem_footprint_wf {x : Expr} {tₑ : Term} {εnv : SymEnv} :
  εnv.WellFormedFor x →
  tₑ ∈ footprint x εnv →
  tₑ.WellFormed εnv.entities
```

`Cedar.Thm.mem_footprints_wf` (theorem, [line 271](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Footprint.lean#L271))

```lean
theorem mem_footprints_wf {xs : List Expr} {t : Term} {εnv : SymEnv}
  (hwε : εnv.WellFormed)
  (hvr : ∀ x ∈ xs, εnv.entities.ValidRefsFor x)
  (hin : t ∈ footprints xs εnv) :
  t.WellFormed εnv.entities
```

`Cedar.Thm.footprints_empty` (theorem, [line 281](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Footprint.lean#L281))

```lean
theorem footprints_empty {εnv : SymEnv} :
  footprints [] εnv = ∅
```

`Cedar.Thm.footprints_singleton` (theorem, [line 286](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Footprint.lean#L286))

```lean
theorem footprints_singleton {x : Expr} {εnv : SymEnv} :
  footprints [x] εnv = footprint x εnv
```

`Cedar.Thm.footprints_append` (theorem, [line 291](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Footprint.lean#L291))

```lean
theorem footprints_append {xs₁ xs₂ : List Expr} {εnv : SymEnv} :
  footprints (xs₁ ++ xs₂) εnv = footprints xs₁ εnv ++ footprints xs₂ εnv
```

`Cedar.Thm.footprint_subset_footprints` (theorem, [line 297](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Footprint.lean#L297))

```lean
theorem footprint_subset_footprints {x : Expr} {xs : List Expr} {εnv : SymEnv} :
  x ∈ xs → footprint x εnv ⊆ footprints xs εnv
```

## Depends on

- [Strongly well-formed ancestor relations](../data/hierarchy.md)

## Proof depends on

- [Lemmas about List.mapUnion operator](../../data/mapunion.md)
- [Compiler/WF](../compiler-2/wf.md)
- [Basic properties of strongly well-formed symbolic environments](../env/swf.md)

## Sources

- [Cedar/Thm/SymCC/Enforcer/Footprint.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Footprint.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Enforcer.Footprint.json)
