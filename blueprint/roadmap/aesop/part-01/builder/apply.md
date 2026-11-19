---
catalog: module
lean: Aesop.RuleBuilderOptions.applyTransparency, Aesop.RuleBuilderOptions.applyIndexTransparency, Aesop.RuleBuilder.getApplyIndexingMode, Aesop.RuleBuilder.checkNoIff, Aesop.RuleBuilder.applyCore, Aesop.RuleBuilder.apply
statement: formalized
proof: formalized
---

# Builder/Apply

`Aesop.Builder.Apply`, in [Aesop/Builder/Apply.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Apply.lean), by Jannis Limperg.

`Aesop.RuleBuilderOptions.applyTransparency` (definition, [line 20](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Apply.lean#L20))

```lean
def applyTransparency (opts : RuleBuilderOptions) : TransparencyMode
```

`Aesop.RuleBuilderOptions.applyIndexTransparency` (definition, [line 23](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Apply.lean#L23))

```lean
def applyIndexTransparency (opts : RuleBuilderOptions) : TransparencyMode
```

`Aesop.RuleBuilder.getApplyIndexingMode` (definition, [line 30](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Apply.lean#L30))

```lean
def getApplyIndexingMode (indexMd : TransparencyMode) (type : Expr) :
    MetaM IndexingMode
```

`Aesop.RuleBuilder.checkNoIff` (definition, [line 37](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Apply.lean#L37))

```lean
def checkNoIff (type : Expr) : MetaM Unit
```

`Aesop.RuleBuilder.applyCore` (definition, [line 43](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Apply.lean#L43))

```lean
def applyCore (t : ElabRuleTerm) (pat? : Option RulePattern)
    (imode? : Option IndexingMode) (md indexMd : TransparencyMode)
    (phase : PhaseSpec) : MetaM LocalRuleSetMember
```

`Aesop.RuleBuilder.apply` (definition, [line 52](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Apply.lean#L52))

```lean
def apply : RuleBuilder
```

## Depends on

- [Builder/Basic](basic.md)

## Sources

- [Aesop/Builder/Apply.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Apply.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Builder.Apply.json)
