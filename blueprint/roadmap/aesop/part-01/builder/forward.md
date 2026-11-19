---
catalog: module
lean: Aesop.RuleBuilderOptions.forwardTransparency, Aesop.RuleBuilderOptions.forwardIndexTransparency, Aesop.RuleBuilder.getForwardIndexingMode, Aesop.RuleBuilder.getImmediatePremises, Aesop.RuleBuilder.forwardCore₂, Aesop.RuleBuilder.forwardCore, Aesop.RuleBuilder.forward
statement: formalized
proof: formalized
---

# Builder/Forward

`Aesop.Builder.Forward`, in [Aesop/Builder/Forward.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Forward.lean), by Jannis Limperg.

`Aesop.RuleBuilderOptions.forwardTransparency` (definition, [line 19](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Forward.lean#L19))

```lean
def forwardTransparency (opts : RuleBuilderOptions) : TransparencyMode
```

`Aesop.RuleBuilderOptions.forwardIndexTransparency` (definition, [line 22](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Forward.lean#L22))

```lean
def forwardIndexTransparency (opts : RuleBuilderOptions) : TransparencyMode
```

`Aesop.RuleBuilder.getForwardIndexingMode` (definition, [line 29](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Forward.lean#L29))

```lean
def getForwardIndexingMode (type : Expr)
    (immediate : UnorderedArraySet PremiseIndex) : MetaM IndexingMode
```

`Aesop.RuleBuilder.getImmediatePremises` (definition, [line 45](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Forward.lean#L45))

```lean
def getImmediatePremises  (type : Expr) (pat? : Option RulePattern) :
    Option (Array Name) → MetaM (UnorderedArraySet PremiseIndex)
  | none =>
    -- If no immediate names are given, every argument becomes immediate,
    -- except instance args, dependent args and args determined by a rule
    -- pattern.
    withReducible $ forallTelescopeReducing type λ args _ => do
      let mut result := #[]
      for h : i in [:args.size] do
        if isPatternInstantiated i then
          continue
        let fvarId := args[i].fvarId!
        let ldecl ← fvarId.getDecl
        let isNondep : MetaM Bool :=
          notM <| args.anyM (start := i + 1) λ arg => do
            let type ← instantiateMVars (← inferType arg)
            -- We do not count instance dependencies here. E.g. for the rule
            -- type `∀ {S} [Cls S], T`, we consider `S` nondependent since only
            -- instances depend on it.
            if (← arg.fvarId!.getBinderInfo) matches .instImplicit then
              return false
            return type.containsFVar fvarId
        if ← pure ! ldecl.binderInfo.isInstImplicit <&&> isNondep then
          result := result.push ⟨i⟩
      return UnorderedArraySet.ofDeduplicatedArray result
  | some immediate =>
    -- If immediate names are given, we check that corresponding arguments
    -- exist and record these arguments' positions.
    withReducible $ forallTelescopeReducing type λ args _ => do
      let mut unseen := immediate.sortDedup (ord := ⟨Name.quickCmp⟩)
      let mut result := #[]
      for h : i in [:args.size] do
        let argName := (← args[i].fvarId!.getDecl).userName
        if immediate.contains argName then
          if isPatternInstantiated i then
            throwError "{errPrefix}argument '{argName}' cannot be immediate since it is already determined by a pattern"
          else
            result := result.push ⟨i⟩
            unseen
```

`Aesop.RuleBuilder.forwardCore₂` (definition, [line 95](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Forward.lean#L95))

```lean
def forwardCore₂ (t : ElabRuleTerm) (immediate? : Option (Array Name))
    (pat? : Option RulePattern) (phase : PhaseSpec) (isDestruct : Bool) :
    MetaM ForwardRule
```

`Aesop.RuleBuilder.forwardCore` (definition, [line 124](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Forward.lean#L124))

```lean
def forwardCore (t : ElabRuleTerm) (immediate? : Option (Array Name))
    (pat? : Option RulePattern) (phase : PhaseSpec) (isDestruct : Bool) :
    MetaM LocalRuleSetMember
```

`Aesop.RuleBuilder.forward` (definition, [line 148](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Forward.lean#L148))

```lean
def forward (isDestruct : Bool) : RuleBuilder
```

## Depends on

- [Builder/Basic](basic.md)

## Sources

- [Aesop/Builder/Forward.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Forward.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Builder.Forward.json)
