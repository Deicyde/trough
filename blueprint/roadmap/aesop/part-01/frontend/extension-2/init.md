---
catalog: module
lean: Aesop.RuleSetExtension, Aesop.DeclaredRuleSets, Aesop.getDeclaredRuleSets, Aesop.getDefaultRuleSetNames
statement: formalized
proof: formalized
---

# Init

`Aesop.Frontend.Extension.Init`, in [Aesop/Frontend/Extension/Init.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension/Init.lean), by Jannis Limperg.

`Aesop.RuleSetExtension` (abbreviation, [line 20](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension/Init.lean#L20))

> An environment extension containing an Aesop rule set. Each rule set has its
> own extension.

```lean
abbrev RuleSetExtension
```

`Aesop.DeclaredRuleSets` (structure, [line 26](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension/Init.lean#L26))

> Structure containing information about all declared Aesop rule sets.

```lean
structure DeclaredRuleSets where
  /--
  The collection of declared rule sets. Each rule set has an extension, the
  name of the associated `SimpExtension` and the name of the associated
  `SimprocExtension`. The two simp extensions are expected to be declared.
  -/
  ruleSets : Std.HashMap RuleSetName (RuleSetExtension × Name × Name)
  /--
  The set of Aesop rule sets that are enabled by default.
  -/
  defaultRuleSets : Std.HashSet RuleSetName
  deriving Inhabited
```

`Aesop.getDeclaredRuleSets` (definition, [line 45](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension/Init.lean#L45))

```lean
def getDeclaredRuleSets : IO (Std.HashMap RuleSetName (RuleSetExtension × Name × Name))
```

`Aesop.getDefaultRuleSetNames` (definition, [line 48](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension/Init.lean#L48))

```lean
def getDefaultRuleSetNames : IO (Std.HashSet Name)
```

## Depends on

- [RuleSet](../../../part-02/ruleset.md)

## Sources

- [Aesop/Frontend/Extension/Init.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension/Init.lean)
- [Declaration ledger](../../../../../sources/aesop/Aesop.Frontend.Extension.Init.json)
