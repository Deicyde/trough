---
catalog: module
lean: Aesop.TraceOption, Aesop.registerTraceOption, Aesop.TraceOption.isEnabled, Aesop.TraceOption.withEnabled, Aesop.resolveTraceOption, Aesop.ruleSuccessEmoji, Aesop.ruleFailureEmoji, Aesop.ruleProvedEmoji, Aesop.ruleErrorEmoji, Aesop.rulePostponedEmoji, Aesop.ruleSkippedEmoji, Aesop.nodeUnknownEmoji, Aesop.nodeProvedEmoji, Aesop.nodeUnprovableEmoji, Aesop.newNodeEmoji, Aesop.exceptRuleResultToEmoji, Aesop.withAesopTraceNode, Aesop.withAesopTraceNodeBefore, Aesop.withConstAesopTraceNode, Aesop.traceSimpTheoremTreeContents, Aesop.traceSimpTheorems
statement: formalized
proof: formalized
---

# Aesop/Tracing

`Aesop.Tracing`, in [Aesop/Tracing.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean), by Jannis Limperg.

`Aesop.TraceOption` (structure, [line 16](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean#L16))

```lean
structure TraceOption where
  traceClass : Name
  option : Lean.Option Bool
  deriving Inhabited
```

`Aesop.registerTraceOption` (definition, [line 21](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean#L21))

```lean
def registerTraceOption (traceName : Name) (descr : String) :
    IO TraceOption
```

`Aesop.TraceOption.isEnabled` (definition, [line 31](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean#L31))

```lean
def isEnabled [Monad m] [MonadOptions m] (opt : TraceOption) : m Bool
```

`Aesop.TraceOption.withEnabled` (definition, [line 34](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean#L34))

```lean
def withEnabled [MonadWithOptions m] (opt : TraceOption) (k : m α) : m α
```

`Aesop.resolveTraceOption` (definition, [line 90](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean#L90))

```lean
meta def resolveTraceOption (stx : Ident) : MacroM Name
```

`Aesop.ruleSuccessEmoji` (definition, [line 125](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean#L125))

```lean
def ruleSuccessEmoji
```

`Aesop.ruleFailureEmoji` (definition, [line 126](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean#L126))

```lean
def ruleFailureEmoji
```

`Aesop.ruleProvedEmoji` (definition, [line 127](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean#L127))

```lean
def ruleProvedEmoji
```

`Aesop.ruleErrorEmoji` (definition, [line 128](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean#L128))

```lean
def ruleErrorEmoji
```

`Aesop.rulePostponedEmoji` (definition, [line 129](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean#L129))

```lean
def rulePostponedEmoji
```

`Aesop.ruleSkippedEmoji` (definition, [line 130](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean#L130))

```lean
def ruleSkippedEmoji
```

`Aesop.nodeUnknownEmoji` (definition, [line 131](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean#L131))

```lean
def nodeUnknownEmoji
```

`Aesop.nodeProvedEmoji` (definition, [line 132](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean#L132))

```lean
def nodeProvedEmoji
```

`Aesop.nodeUnprovableEmoji` (definition, [line 133](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean#L133))

```lean
def nodeUnprovableEmoji
```

`Aesop.newNodeEmoji` (definition, [line 134](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean#L134))

```lean
def newNodeEmoji
```

`Aesop.exceptRuleResultToEmoji` (definition, [line 136](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean#L136))

```lean
def exceptRuleResultToEmoji (toEmoji : α → String) : Except ε α → String
```

`Aesop.withAesopTraceNode` (definition, [line 146](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean#L146))

```lean
def withAesopTraceNode [ExceptToTraceResult ε α] (opt : TraceOption)
    (msg : Except ε α → m MessageData) (k : m α) (collapsed := true) : m α
```

`Aesop.withAesopTraceNodeBefore` (definition, [line 151](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean#L151))

```lean
def withAesopTraceNodeBefore [ExceptToTraceResult ε α] (opt : TraceOption)
    (msg : m MessageData) (k : m α) (collapsed := true) : m α
```

`Aesop.withConstAesopTraceNode` (definition, [line 156](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean#L156))

```lean
def withConstAesopTraceNode [ExceptToTraceResult ε α] (opt : TraceOption)
    (msg : m MessageData) (k : m α) (collapsed := true) : m α
```

`Aesop.traceSimpTheoremTreeContents` (definition, [line 162](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean#L162))

```lean
def traceSimpTheoremTreeContents (t : SimpTheoremTree) (opt : TraceOption) :
    CoreM Unit
```

`Aesop.traceSimpTheorems` (definition, [line 169](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean#L169))

```lean
def traceSimpTheorems (s : SimpTheorems) (opt : TraceOption) : CoreM Unit
```

## Depends on

- [Util/Basic](../part-01/util/basic.md)

## Sources

- [Aesop/Tracing.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tracing.lean)
- [Declaration ledger](../../../sources/aesop/Aesop.Tracing.json)
