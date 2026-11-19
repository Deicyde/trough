---
catalog: module
lean: Aesop.BuiltinRules.not_intro, Aesop.BuiltinRules.empty_false, Aesop.BuiltinRules.pEmpty_false, Aesop.BuiltinRules.heq_iff_eq
statement: formalized
proof: formalized
---

# BuiltinRules

`Aesop.BuiltinRules`, in [Aesop/BuiltinRules.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules.lean), by Jannis Limperg.

`Aesop.BuiltinRules.not_intro` (theorem, [line 48](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules.lean#L48))

```lean
theorem not_intro (h : P → False) : ¬ P
```

`Aesop.BuiltinRules.empty_false` (theorem, [line 51](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules.lean#L51))

```lean
theorem empty_false (h : Empty) : False
```

`Aesop.BuiltinRules.pEmpty_false` (theorem, [line 54](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules.lean#L54))

```lean
theorem pEmpty_false (h : PEmpty) : False
```

`Aesop.BuiltinRules.heq_iff_eq` (theorem, [line 61](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules.lean#L61))

```lean
theorem heq_iff_eq (x y : α) : x ≍ y ↔ x = y
```

## Depends on

Its statements use no other Aesop module's declarations.

## Sources

- [Aesop/BuiltinRules.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules.lean)
- [Declaration ledger](../../../sources/aesop/Aesop.BuiltinRules.json)
