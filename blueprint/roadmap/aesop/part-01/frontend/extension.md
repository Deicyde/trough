---
catalog: module
lean: Aesop.Frontend.extensionDescr, Aesop.Frontend.declareRuleSetUnchecked, Aesop.Frontend.isRuleSetDeclared, Aesop.Frontend.checkRuleSetNotDeclared, Aesop.Frontend.declareRuleSet, Aesop.Frontend.getGlobalRuleSetData, Aesop.Frontend.getGlobalRuleSetFromData, Aesop.Frontend.getGlobalRuleSet, Aesop.Frontend.getGlobalRuleSets, Aesop.Frontend.getDefaultGlobalRuleSets, Aesop.Frontend.getDeclaredGlobalRuleSets, Aesop.Frontend.modifyGetGlobalRuleSet, Aesop.Frontend.modifyGlobalRuleSet, Aesop.Frontend.addGlobalRule, Aesop.Frontend.eraseGlobalRules
statement: formalized
proof: formalized
---

# Frontend/Extension

`Aesop.Frontend.Extension`, in [Aesop/Frontend/Extension.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension.lean), by Jannis Limperg.

`Aesop.Frontend.extensionDescr` (definition, [line 18](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension.lean#L18))

```lean
def extensionDescr (rsName : RuleSetName) :
    SimpleScopedEnvExtension.Descr BaseRuleSetMember BaseRuleSet
```

`Aesop.Frontend.declareRuleSetUnchecked` (definition, [line 24](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension.lean#L24))

```lean
def declareRuleSetUnchecked (rsName : RuleSetName) (isDefault : Bool) :
    IO Unit
```

`Aesop.Frontend.isRuleSetDeclared` (definition, [line 42](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension.lean#L42))

```lean
def isRuleSetDeclared (rsName : RuleSetName) : IO Bool
```

`Aesop.Frontend.checkRuleSetNotDeclared` (definition, [line 48](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension.lean#L48))

```lean
def checkRuleSetNotDeclared (rsName : RuleSetName) : m Unit
```

`Aesop.Frontend.declareRuleSet` (definition, [line 52](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension.lean#L52))

```lean
def declareRuleSet (rsName : RuleSetName) (isDefault : Bool) : m Unit
```

`Aesop.Frontend.getGlobalRuleSetData` (definition, [line 59](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension.lean#L59))

```lean
def getGlobalRuleSetData (rsName : RuleSetName) :
    m (RuleSetExtension × Name × SimpExtension × Name × Simp.SimprocExtension)
```

`Aesop.Frontend.getGlobalRuleSetFromData` (definition, [line 70](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension.lean#L70))

```lean
def getGlobalRuleSetFromData (ext : RuleSetExtension) (simpExt : SimpExtension)
    (simprocExt : Simp.SimprocExtension) : m GlobalRuleSet
```

`Aesop.Frontend.getGlobalRuleSet` (definition, [line 78](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension.lean#L78))

```lean
def getGlobalRuleSet (rsName : RuleSetName) :
    CoreM (GlobalRuleSet × Name × Name)
```

`Aesop.Frontend.getGlobalRuleSets` (definition, [line 85](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension.lean#L85))

```lean
def getGlobalRuleSets (rsNames : Array RuleSetName) :
    CoreM (Array (GlobalRuleSet × Name × Name))
```

`Aesop.Frontend.getDefaultGlobalRuleSets` (definition, [line 89](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension.lean#L89))

```lean
def getDefaultGlobalRuleSets : CoreM (Array (GlobalRuleSet × Name × Name))
```

`Aesop.Frontend.getDeclaredGlobalRuleSets` (definition, [line 92](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension.lean#L92))

```lean
def getDeclaredGlobalRuleSets :
    CoreM (Array (RuleSetName × GlobalRuleSet × Name × Name))
```

`Aesop.Frontend.modifyGetGlobalRuleSet` (definition, [line 97](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension.lean#L97))

```lean
def modifyGetGlobalRuleSet (rsName : RuleSetName)
    (f : GlobalRuleSet → α × GlobalRuleSet) : m α
```

`Aesop.Frontend.modifyGlobalRuleSet` (definition, [line 114](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension.lean#L114))

```lean
def modifyGlobalRuleSet (rsName : RuleSetName)
    (f : GlobalRuleSet → GlobalRuleSet) : CoreM Unit
```

`Aesop.Frontend.addGlobalRule` (definition, [line 118](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension.lean#L118))

```lean
def addGlobalRule (rsName : RuleSetName) (r : GlobalRuleSetMember)
    (kind : AttributeKind) (checkNotExists : Bool) : m Unit
```

`Aesop.Frontend.eraseGlobalRules` (definition, [line 135](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension.lean#L135))

```lean
def eraseGlobalRules (rsf : RuleSetNameFilter) (rf : RuleFilter)
    (checkExists : Bool) : m Unit
```

## Depends on

- [Init](extension-2/init.md)

## Sources

- [Aesop/Frontend/Extension.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Extension.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Frontend.Extension.json)
