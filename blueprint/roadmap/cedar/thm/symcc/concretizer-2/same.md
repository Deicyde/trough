---
catalog: module
lean: Cedar.Thm.term_entityUID?_some_iff_eq, Cedar.Thm.term_recordValue?_some_same, Cedar.Thm.term_tag?_some_iff_eq, Cedar.Thm.concretize?_taggedValueFor_some_implies, Cedar.Thm.concretize?_some_same
statement: formalized
proof: formalized
---

# Concretizer/Same

`Cedar.Thm.SymCC.Concretizer.Same`, in [Cedar/Thm/SymCC/Concretizer/Same.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/Same.lean).

> The main lemma in this file, `concretize?_some_same`, proves that succesful
> concretization results in a concrete environment that corresponds to the given
> literal symbolic environment.

`Cedar.Thm.term_entityUID?_some_iff_eq` (theorem, [line 32](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/Same.lean#L32))

```lean
theorem term_entityUID?_some_iff_eq {t : Term} {uid : EntityUID} :
  t.entityUID? = some uid ↔ t = Term.prim (TermPrim.entity uid)
```

`Cedar.Thm.term_recordValue?_some_same` (theorem, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/Same.lean#L47))

```lean
theorem term_recordValue?_some_same {t : Term} {r : Map Attr Value} :
  t.recordValue? = some r → (Value.record r) ∼ t
```

`Cedar.Thm.term_tag?_some_iff_eq` (theorem, [line 107](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/Same.lean#L107))

```lean
theorem term_tag?_some_iff_eq {t : Term} {s : String} :
  t.tag? = some s ↔ t = Term.string s
```

`Cedar.Thm.concretize?_taggedValueFor_some_implies` (theorem, [line 245](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/Same.lean#L245))

```lean
theorem concretize?_taggedValueFor_some_implies {tuid : Term} {tag tag' : Tag} {v : Value} {τs : SymTags} :
  SymEntityData.concretize?.taggedValueFor τs tuid tag = some (tag', v) →
  tag = tag' ∧ (τs.getTag! tuid (.string tag)).value? = some v
```

`Cedar.Thm.concretize?_some_same` (theorem, [line 395](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/Same.lean#L395))

```lean
theorem concretize?_some_same {x : Expr} {env : Env} {εnv : SymEnv} :
  εnv.WellFormedFor x →
  εnv.concretize? x = .some env →
  env ∼ εnv
```

## Depends on

- [Well-formedness and interpretations](../data/basic.md)

## Proof depends on

- [Lemmas about List.mapUnion operator](../../data/mapunion.md)
- [Concretizer/Util](util.md)
- [Properties of the `Same` predicate on Terms](../term/same.md)

## Sources

- [Cedar/Thm/SymCC/Concretizer/Same.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer/Same.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Concretizer.Same.json)
