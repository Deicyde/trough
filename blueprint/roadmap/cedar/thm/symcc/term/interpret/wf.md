---
catalog: module
lean: Cedar.Thm.InterpretTermWF, Cedar.Thm.interpret_term_prim_wf, Cedar.Thm.interpret_term_var_wf, Cedar.Thm.interpret_term_none_wf, Cedar.Thm.interpret_term_some_wf, Cedar.Thm.interpret_term_set_wf, Cedar.Thm.interpret_term_record_wf, Cedar.Thm.interpret_term_app_wf, Cedar.Thm.interpret_term_wf, Cedar.Thm.interpret_term_isEntityType, Cedar.Thm.interpret_term_isRecordType
statement: formalized
proof: formalized
---

# Interpretation preserves well-formedness of Terms (WF)

`Cedar.Thm.SymCC.Term.Interpret.WF`, in [Cedar/Thm/SymCC/Term/Interpret/WF.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/WF.lean).

> This file proves that interpretation preserves well-formedness: interpreting a
> well-formed term of a given type produces a well-formed term of the same type.
> -

`Cedar.Thm.InterpretTermWF` (definition, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/WF.lean#L41))

```lean
public def InterpretTermWF (εs : SymEntities) (I : Interpretation) (t : Term) : Prop
```

`Cedar.Thm.interpret_term_prim_wf` (theorem, [line 45](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/WF.lean#L45))

```lean
public theorem interpret_term_prim_wf {εs : SymEntities} {I : Interpretation} {p : TermPrim}
  (h : Term.WellFormed εs (Term.prim p)) :
  InterpretTermWF εs I (Term.prim p)
```

`Cedar.Thm.interpret_term_var_wf` (theorem, [line 51](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/WF.lean#L51))

```lean
public theorem interpret_term_var_wf {εs : SymEntities} {I : Interpretation} {v : TermVar}
  (h₁ : I.WellFormed εs)
  (h₂ : Term.WellFormed εs (Term.var v)) :
  InterpretTermWF εs I (Term.var v)
```

`Cedar.Thm.interpret_term_none_wf` (theorem, [line 62](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/WF.lean#L62))

```lean
public theorem interpret_term_none_wf {εs : SymEntities} {I : Interpretation} {ty : TermType}
  (h : Term.WellFormed εs (Term.none ty)) :
  InterpretTermWF εs I (Term.none ty)
```

`Cedar.Thm.interpret_term_some_wf` (theorem, [line 68](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/WF.lean#L68))

```lean
public theorem interpret_term_some_wf {εs : SymEntities} {I : Interpretation} {t : Term}
  (ih : InterpretTermWF εs I t) :
  InterpretTermWF εs I (Term.some t)
```

`Cedar.Thm.interpret_term_set_wf` (theorem, [line 75](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/WF.lean#L75))

```lean
public theorem interpret_term_set_wf {εs : SymEntities} {I : Interpretation} {s : Set Term} {ty : TermType}
  (h₁ : Term.WellFormed εs (Term.set s ty))
  (ih : ∀ (t : Term), t ∈ s → InterpretTermWF εs I t) :
  InterpretTermWF εs I (Term.set s ty)
```

`Cedar.Thm.interpret_term_record_wf` (theorem, [line 97](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/WF.lean#L97))

```lean
public theorem interpret_term_record_wf {εs : SymEntities} {I : Interpretation} {r : Map Attr Term}
  (h₁ : Term.WellFormed εs (Term.record r))
  (ih :  ∀ (a : Attr) (t : Term), (a, t) ∈ r.toList → InterpretTermWF εs I t) :
  InterpretTermWF εs I (Term.record r)
```

`Cedar.Thm.interpret_term_app_wf` (theorem, [line 479](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/WF.lean#L479))

```lean
public theorem interpret_term_app_wf {εs : SymEntities} {I : Interpretation} {op : Op} {ts : List Term} {ty : TermType}
  (h₀ : I.WellFormed εs)
  (h₁ : Term.WellFormed εs (Term.app op ts ty))
  (ih : ∀ (t : Term), t ∈ ts → InterpretTermWF εs I t) :
  InterpretTermWF εs I (Term.app op ts ty)
```

`Cedar.Thm.interpret_term_wf` (theorem, [line 531](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/WF.lean#L531))

```lean
public theorem interpret_term_wf {εs : SymEntities} {I : Interpretation} {t : Term}
  (h₁ : I.WellFormed εs)
  (h₂ : t.WellFormed εs) :
  (t.interpret I).WellFormed εs ∧
  (t.interpret I).typeOf = t.typeOf
```

`Cedar.Thm.interpret_term_isEntityType` (theorem, [line 568](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/WF.lean#L568))

```lean
public theorem interpret_term_isEntityType {εs : SymEntities} {I : Interpretation} {t : Term}
  (h₁ : I.WellFormed εs)
  (h₂ : t.WellFormed εs) :
  t.typeOf.isEntityType = (t.interpret I).typeOf.isEntityType
```

`Cedar.Thm.interpret_term_isRecordType` (theorem, [line 574](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/WF.lean#L574))

```lean
public theorem interpret_term_isRecordType {εs : SymEntities} {I : Interpretation} {t : Term}
  (h₁ : I.WellFormed εs)
  (h₂ : t.WellFormed εs) :
  t.typeOf.isRecordType = (t.interpret I).typeOf.isRecordType
```

## Depends on

- [Well-formedness and interpretations](../../data/basic.md)

## Proof depends on

- [Interpretation of Terms and Factory functions](basic.md)
- [Well-formed terms and factory functions](../wf.md)

## Sources

- [Cedar/Thm/SymCC/Term/Interpret/WF.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/WF.lean)
- [Declaration ledger](../../../../../../sources/cedar/Cedar.Thm.SymCC.Term.Interpret.WF.json)
