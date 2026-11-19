---
catalog: module
lean: Cedar.Thm.value_set_entityUIDs_def, Cedar.Thm.value_record_entityUIDs_def, Cedar.Thm.termPrim_entityUIDs_wf, Cedar.Thm.term_entityUIDs_wf, Cedar.Thm.value_ws_closed_implies_wf, Cedar.Thm.term_prim_value?_some_implies_ws, Cedar.Thm.term_set_value?_some_implies, Cedar.Thm.term_set_value?_some_implies_ws, Cedar.Thm.term_value?_some_implies_ws, Cedar.Thm.term_value?_some_implies_eq_entityUIDs
statement: formalized
proof: formalized
---

# WFValue

`Cedar.Thm.SymCC.Concretizer.WFValue`, in [Cedar/Thm/SymCC/Concretizer/WFValue.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/WFValue.lean).

> The lemmas in this file prove key properties of well-structured and
> well-formed values.

`Cedar.Thm.value_set_entityUIDs_def` (theorem, [line 29](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/WFValue.lean#L29))

```lean
theorem value_set_entityUIDs_def {vs : Set Value} :
  (Value.set vs).entityUIDs = vs.elts.mapUnion Value.entityUIDs
```

`Cedar.Thm.value_record_entityUIDs_def` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/WFValue.lean#L35))

```lean
theorem value_record_entityUIDs_def {avs : Map Attr Value} :
  (Value.record avs).entityUIDs = avs.toList.mapUnion λ (_, v) => v.entityUIDs
```

`Cedar.Thm.termPrim_entityUIDs_wf` (theorem, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/WFValue.lean#L41))

```lean
theorem termPrim_entityUIDs_wf (p : TermPrim) :
  p.entityUIDs.WellFormed
```

`Cedar.Thm.term_entityUIDs_wf` (theorem, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/WFValue.lean#L47))

```lean
theorem term_entityUIDs_wf (t : Term) :
  t.entityUIDs.WellFormed
```

`Cedar.Thm.value_ws_closed_implies_wf` (theorem, [line 82](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/WFValue.lean#L82))

```lean
theorem value_ws_closed_implies_wf {v : Value} {es : Entities} :
  v.WellStructured →
  es.ClosedFor v.entityUIDs →
  v.WellFormed es
```

`Cedar.Thm.term_prim_value?_some_implies_ws` (theorem, [line 118](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/WFValue.lean#L118))

```lean
theorem term_prim_value?_some_implies_ws {t : TermPrim} {v : Value} :
  t.value? = .some v → v.WellStructured
```

`Cedar.Thm.term_set_value?_some_implies` (theorem, [line 132](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/WFValue.lean#L132))

```lean
theorem term_set_value?_some_implies {ts : List Term} {ty : TermType} {v : Value} :
  (Term.set (Set.mk ts) ty).value? = some v →
  ∃ vs,
    List.mapM Term.value? ts = some vs ∧ Value.set (Set.make vs) = v
```

`Cedar.Thm.term_set_value?_some_implies_ws` (theorem, [line 140](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/WFValue.lean#L140))

```lean
theorem term_set_value?_some_implies_ws {ts : List Term} {ty : TermType} {v : Value} {εs : SymEntities}
  (hw : Term.WellFormed εs (Term.set (Set.mk ts) ty))
  (hv : (Term.set (Set.mk ts) ty).value? = some v)
  (ih : ∀ (tᵢ : Term), tᵢ ∈ ts → ∀ {vᵢ : Value}, Term.WellFormed εs tᵢ → tᵢ.value? = some vᵢ → vᵢ.WellStructured) :
  v.WellStructured
```

`Cedar.Thm.term_value?_some_implies_ws` (theorem, [line 235](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/WFValue.lean#L235))

```lean
theorem term_value?_some_implies_ws {t : Term} {v : Value} {εs : SymEntities} :
  t.WellFormed εs → t.value? = .some v → v.WellStructured
```

`Cedar.Thm.term_value?_some_implies_eq_entityUIDs` (theorem, [line 337](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/WFValue.lean#L337))

```lean
theorem term_value?_some_implies_eq_entityUIDs {t : Term} {v : Value} :
  t.value? = .some v → t.entityUIDs = v.entityUIDs
```

## Depends on

- [Well-formedness and interpretations](../data/basic.md)

## Proof depends on

- [Lemmas about List.mapUnion operator](../../data/mapunion.md)
- [Properties of the `Same` predicate on Terms](../term/same.md)

## Sources

- [Cedar/Thm/SymCC/Concretizer/WFValue.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/WFValue.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Concretizer.WFValue.json)
