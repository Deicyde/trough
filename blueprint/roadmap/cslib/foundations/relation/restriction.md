---
catalog: module
lean: Set.refl_iff_reflOn, Set.symm_iff_symmOn, Set.ReflOn.of_dom, Set.ReflOn.of_cod, Set.SymmOn.of_dom, Set.SymmOn.of_cod
statement: formalized
proof: formalized
---

# Relations: Properties on set restrictions

`Cslib.Foundations.Relation.Restriction`, in [Cslib/Foundations/Relation/Restriction.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Restriction.lean), by Chris Henson.

> ## References
>
> * [*Simple Laws about Nonprominent Properties of Binary Relations*][Burghardt2018]

`Set.refl_iff_reflOn` (theorem, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Restriction.lean#L28))

```lean
theorem refl_iff_reflOn : Std.Refl (α := s) r ↔ s.ReflOn r
```

`Set.symm_iff_symmOn` (theorem, [line 34](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Restriction.lean#L34))

```lean
theorem symm_iff_symmOn : Std.Symm (α := s) r ↔ s.SymmOn r
```

`Set.ReflOn.of_dom` (theorem, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Restriction.lean#L41))

```lean
theorem ReflOn.of_dom {r} : (dom r).ReflOn r → r a b → r a a
```

`Set.ReflOn.of_cod` (theorem, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Restriction.lean#L44))

```lean
theorem ReflOn.of_cod {r} : (cod r).ReflOn r → r a b → r b b
```

`Set.SymmOn.of_dom` (theorem, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Restriction.lean#L47))

```lean
theorem SymmOn.of_dom {r} : (dom r).SymmOn r → r a b → r b c → r b a
```

`Set.SymmOn.of_cod` (theorem, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Restriction.lean#L50))

```lean
theorem SymmOn.of_cod {r} : (cod r).SymmOn r → r a b → r c a → r b a
```

## Depends on

- [Relations: Definitions](defs.md)

## Proof depends on

- [Relations: Domain and Codomain](domain.md)

## Sources

- [Cslib/Foundations/Relation/Restriction.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Restriction.lean)
