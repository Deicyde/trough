---
catalog: module
lean: Aesop.matchByTactic?, Aesop.RuleBuilder.tacticIMode, Aesop.RuleBuilder.tacticCore, Aesop.RuleBuilder.tactic
statement: formalized
proof: formalized
---

# Builder/Tactic

`Aesop.Builder.Tactic`, in [Aesop/Builder/Tactic.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Tactic.lean), by Jannis Limperg.

`Aesop.matchByTactic?` (definition, [line 18](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Tactic.lean#L18))

```lean
def matchByTactic? : Term → Option (TSyntax ``tacticSeq)
```

`Aesop.RuleBuilder.tacticIMode` (definition, [line 24](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Tactic.lean#L24))

```lean
def tacticIMode (imode? : Option IndexingMode) : IndexingMode
```

`Aesop.RuleBuilder.tacticCore` (definition, [line 27](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Tactic.lean#L27))

```lean
def tacticCore (t : Sum Name (TSyntax ``tacticSeq)) (imode? : Option IndexingMode) (phase : PhaseSpec) :
    MetaM LocalRuleSetMember
```

`Aesop.RuleBuilder.tactic` (definition, [line 50](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Tactic.lean#L50))

```lean
def tactic : RuleBuilder
```

## Depends on

- [Builder/Basic](basic.md)

## Sources

- [Aesop/Builder/Tactic.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Tactic.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Builder.Tactic.json)
