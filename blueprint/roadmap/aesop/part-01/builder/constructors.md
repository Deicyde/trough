---
catalog: module
lean: Aesop.RuleBuilderOptions.constructorsTransparency, Aesop.RuleBuilderOptions.constructorsIndexTransparency, Aesop.RuleBuilder.getConstructorsIndexingMode, Aesop.RuleBuilder.constructorsCore, Aesop.RuleBuilder.constructors
statement: formalized
proof: formalized
---

# Constructors

`Aesop.Builder.Constructors`, in [Aesop/Builder/Constructors.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Constructors.lean), by Jannis Limperg.

`Aesop.RuleBuilderOptions.constructorsTransparency` (definition, [line 17](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Constructors.lean#L17))

```lean
def constructorsTransparency (opts : RuleBuilderOptions) : TransparencyMode
```

`Aesop.RuleBuilderOptions.constructorsIndexTransparency` (definition, [line 20](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Constructors.lean#L20))

```lean
def constructorsIndexTransparency (opts : RuleBuilderOptions) : TransparencyMode
```

`Aesop.RuleBuilder.getConstructorsIndexingMode` (definition, [line 27](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Constructors.lean#L27))

```lean
def getConstructorsIndexingMode (indexMd : TransparencyMode)
    (info : InductiveVal) : MetaM IndexingMode
```

`Aesop.RuleBuilder.constructorsCore` (definition, [line 39](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Constructors.lean#L39))

```lean
def constructorsCore (info : InductiveVal) (imode? : Option IndexingMode)
    (md indexMd : TransparencyMode) (phase : PhaseSpec) :
    MetaM LocalRuleSetMember
```

`Aesop.RuleBuilder.constructors` (definition, [line 47](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Constructors.lean#L47))

```lean
def constructors : RuleBuilder
```

## Depends on

- [Builder/Basic](basic.md)

## Sources

- [Aesop/Builder/Constructors.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Constructors.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Builder.Constructors.json)
