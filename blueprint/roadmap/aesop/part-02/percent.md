---
catalog: module
lean: Aesop.Percent, Aesop.Percent.ofFloat, Aesop.Percent.δ, Aesop.Percent.hundred, Aesop.Percent.fifty, Aesop.Percent.toHumanString, Aesop.Percent.ofNat
statement: formalized
proof: formalized
---

# Percent

`Aesop.Percent`, in [Aesop/Percent.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Percent.lean), by Jannis Limperg, Asta Halkjær From.

`Aesop.Percent` (structure, [line 18](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Percent.lean#L18))

```lean
structure Percent where
  toFloat : Float
  deriving Inhabited
```

`Aesop.Percent.ofFloat` (definition, [line 24](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Percent.lean#L24))

```lean
protected def ofFloat (f : Float) : Option Percent
```

`Aesop.Percent.δ` (definition, [line 31](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Percent.lean#L31))

```lean
def δ : Percent
```

`Aesop.Percent.hundred` (definition, [line 60](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Percent.lean#L60))

```lean
def hundred : Percent
```

`Aesop.Percent.fifty` (definition, [line 63](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Percent.lean#L63))

```lean
def fifty : Percent
```

`Aesop.Percent.toHumanString` (definition, [line 66](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Percent.lean#L66))

```lean
def toHumanString (p : Percent) : String
```

`Aesop.Percent.ofNat` (definition, [line 74](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Percent.lean#L74))

```lean
protected def ofNat (n : Nat) : Option Percent
```

## Depends on

Its statements use no other Aesop module's declarations.

## Sources

- [Aesop/Percent.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Percent.lean)
- [Declaration ledger](../../../sources/aesop/Aesop.Percent.json)
