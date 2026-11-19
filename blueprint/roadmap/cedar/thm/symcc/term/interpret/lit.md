---
catalog: module
lean: Cedar.Thm.interpret_term_lit_id, Cedar.Thm.interpret_term_lit, Cedar.Thm.interpret_term_wfl
statement: formalized
proof: formalized
---

# Interpretation preserves well-formedness of Terms (Lit)

`Cedar.Thm.SymCC.Term.Interpret.Lit`, in [Cedar/Thm/SymCC/Term/Interpret/Lit.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Lit.lean).

> This file proves that interpretation produces literals that preserve
> well-formedness: interpreting a well-formed term of a given type produces a
> well-formed literal term of the same type. It also proves that interpreting
> a well-formed literal produces that same literal.
> -

`Cedar.Thm.interpret_term_lit_id` (theorem, [line 72](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Lit.lean#L72))

```lean
public theorem interpret_term_lit_id {εs : SymEntities} (I : Interpretation) {t : Term}
  (h₁ : t.WellFormedLiteral εs) :
  t.interpret I = t
```

`Cedar.Thm.interpret_term_lit` (theorem, [line 286](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Lit.lean#L286))

```lean
public theorem interpret_term_lit {εs : SymEntities} {I : Interpretation} {t : Term}
  (h₀ : I.WellFormed εs)
  (h₁ : t.WellFormed εs) :
  (t.interpret I).isLiteral
```

`Cedar.Thm.interpret_term_wfl` (theorem, [line 307](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Lit.lean#L307))

```lean
public theorem interpret_term_wfl {εs : SymEntities} {I : Interpretation} {t : Term}
  (h₁ : I.WellFormed εs)
  (h₂ : t.WellFormed εs) :
  (t.interpret I).WellFormedLiteral εs ∧
  (t.interpret I).typeOf = t.typeOf
```

## Depends on

- [Well-formedness and interpretations](../../data/basic.md)

## Proof depends on

- [Interpretation preserves well-formedness of Terms (WF)](wf.md)
- [Basic properties of partial evaluation of terms](../pe.md)

## Sources

- [Cedar/Thm/SymCC/Term/Interpret/Lit.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/Interpret/Lit.lean)
- [Declaration ledger](../../../../../../sources/cedar/Cedar.Thm.SymCC.Term.Interpret.Lit.json)
