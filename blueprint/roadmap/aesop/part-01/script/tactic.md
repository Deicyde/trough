---
catalog: module
lean: Aesop.Script.UTactic, Aesop.Script.STactic, Aesop.Script.Tactic, Aesop.Script.Tactic.unstructured, Aesop.Script.Tactic.structured, Aesop.Script.TacticBuilder
statement: formalized
proof: formalized
---

# Script/Tactic

`Aesop.Script.Tactic`, in [Aesop/Script/Tactic.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Tactic.lean), by Jannis Limperg.

`Aesop.Script.UTactic` (abbreviation, [line 16](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Tactic.lean#L16))

```lean
abbrev UTactic
```

`Aesop.Script.STactic` (structure, [line 18](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Tactic.lean#L18))

```lean
structure STactic where
  numSubgoals : Nat
  run : Array (Array Syntax.Tactic) → Syntax.Tactic
```

`Aesop.Script.Tactic` (structure, [line 22](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Tactic.lean#L22))

```lean
structure Tactic where
  uTactic : UTactic
  sTactic? : Option STactic
```

`Aesop.Script.Tactic.unstructured` (definition, [line 31](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Tactic.lean#L31))

```lean
def unstructured (uTactic : UTactic) : Tactic
```

`Aesop.Script.Tactic.structured` (definition, [line 35](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Tactic.lean#L35))

```lean
def structured (uTactic : UTactic) (sTactic : STactic) : Tactic
```

`Aesop.Script.TacticBuilder` (abbreviation, [line 41](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Tactic.lean#L41))

```lean
abbrev TacticBuilder
```

## Depends on

Its statements use no other Aesop module's declarations.

## Sources

- [Aesop/Script/Tactic.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Tactic.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Script.Tactic.json)
