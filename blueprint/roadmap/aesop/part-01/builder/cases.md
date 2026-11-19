---
catalog: module
lean: Aesop.CasesPattern.check, Aesop.CasesPattern.toIndexingMode, Aesop.RuleBuilderOptions.casesTransparency, Aesop.RuleBuilderOptions.casesIndexTransparency, Aesop.RuleBuilderOptions.casesPatterns, Aesop.RuleBuilder.mkCasesTarget, Aesop.RuleBuilder.getCasesIndexingMode, Aesop.RuleBuilder.casesCore, Aesop.RuleBuilder.cases
statement: formalized
proof: formalized
---

# Builder/Cases

`Aesop.Builder.Cases`, in [Aesop/Builder/Cases.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Cases.lean), by Jannis Limperg.

`Aesop.CasesPattern.check` (definition, [line 21](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Cases.lean#L21))

```lean
def check (decl : Name) (p : CasesPattern) : MetaM Unit
```

`Aesop.CasesPattern.toIndexingMode` (definition, [line 27](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Cases.lean#L27))

```lean
def toIndexingMode (p : CasesPattern) : MetaM IndexingMode
```

`Aesop.RuleBuilderOptions.casesTransparency` (definition, [line 35](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Cases.lean#L35))

```lean
def casesTransparency (opts : RuleBuilderOptions) : TransparencyMode
```

`Aesop.RuleBuilderOptions.casesIndexTransparency` (definition, [line 38](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Cases.lean#L38))

```lean
def casesIndexTransparency (opts : RuleBuilderOptions) : TransparencyMode
```

`Aesop.RuleBuilderOptions.casesPatterns` (definition, [line 41](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Cases.lean#L41))

```lean
def casesPatterns (opts : RuleBuilderOptions) : Array CasesPattern
```

`Aesop.RuleBuilder.mkCasesTarget` (definition, [line 48](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Cases.lean#L48))

```lean
def mkCasesTarget (decl : Name) (casesPatterns : Array CasesPattern) :
    CasesTarget
```

`Aesop.RuleBuilder.getCasesIndexingMode` (definition, [line 55](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Cases.lean#L55))

```lean
def getCasesIndexingMode (decl : Name) (indexMd : TransparencyMode)
    (casesPatterns : Array CasesPattern) : MetaM IndexingMode
```

`Aesop.RuleBuilder.casesCore` (definition, [line 66](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Cases.lean#L66))

> `decl` is either the name of the inductive type described by `info`, or a
> type synonym for it at transparency `default` or `md` (whichever is larger).

```lean
def casesCore (decl : Name) (info : InductiveVal) (pats : Array CasesPattern)
    (imode? : Option IndexingMode) (md indexMd : TransparencyMode)
    (phase : PhaseSpec) : MetaM LocalRuleSetMember
```

`Aesop.RuleBuilder.cases` (definition, [line 76](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Cases.lean#L76))

```lean
def cases : RuleBuilder
```

## Depends on

- [Builder/Basic](basic.md)
- [RuleTac/Cases](../ruletac/cases.md)

## Sources

- [Aesop/Builder/Cases.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Cases.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Builder.Cases.json)
