---
catalog: module
lean: Aesop.RuleTac.ForwardM.Context, Aesop.RuleTac.ForwardM.State, Aesop.RuleTac.ForwardM, Aesop.RuleTac.makeForwardHypProofs, Aesop.RuleTac.makeForwardHypProofs', Aesop.RuleTac.assertForwardHyp, Aesop.RuleTac.applyForwardRule, Aesop.RuleTac.forwardExpr, Aesop.RuleTac.forwardConst, Aesop.RuleTac.forwardTerm, Aesop.RuleTac.forward, Aesop.RuleTac.forwardMatches, Aesop.RuleTac.forwardMatch
statement: formalized
proof: formalized
---

# RuleTac/Forward

`Aesop.RuleTac.Forward`, in [Aesop/RuleTac/Forward.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Forward.lean), by Jannis Limperg.

`Aesop.RuleTac.ForwardM.Context` (structure, [line 22](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Forward.lean#L22))

```lean
structure ForwardM.Context where
  maxDepth? : Option Nat
  forwardHypData : ForwardHypData
  deriving Inhabited
```

`Aesop.RuleTac.ForwardM.State` (structure, [line 27](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Forward.lean#L27))

```lean
structure ForwardM.State where
  toAssert : Array (Expr × Expr × Nat) := #[]
  usedHyps : Std.HashSet FVarId := ∅
  deriving Inhabited
```

`Aesop.RuleTac.ForwardM` (abbreviation, [line 32](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Forward.lean#L32))

```lean
abbrev ForwardM
```

`Aesop.RuleTac.makeForwardHypProofs` (definition, [line 34](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Forward.lean#L34))

```lean
partial def makeForwardHypProofs (e : Expr) (patSubst? : Option Substitution)
    (immediate : UnorderedArraySet PremiseIndex) : ForwardM Unit
```

`Aesop.RuleTac.makeForwardHypProofs'` (definition, [line 116](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Forward.lean#L116))

```lean
def makeForwardHypProofs' (e : Expr)
    (patSubsts? : Option (Array Substitution))
    (immediate : UnorderedArraySet PremiseIndex) : ForwardM Unit
```

`Aesop.RuleTac.assertForwardHyp` (definition, [line 125](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Forward.lean#L125))

```lean
def assertForwardHyp (goal : MVarId) (hyp : Hypothesis) (depth : Nat) :
    ScriptM (FVarId × MVarId)
```

`Aesop.RuleTac.applyForwardRule` (definition, [line 146](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Forward.lean#L146))

```lean
def applyForwardRule (goal : MVarId) (e : Expr)
    (patSubsts? : Option (Array Substitution))
    (immediate : UnorderedArraySet PremiseIndex) (clear : Bool)
    (maxDepth? : Option Nat) :
    ScriptM Subgoal
```

`Aesop.RuleTac.forwardExpr` (definition, [line 183](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Forward.lean#L183))

```lean
def forwardExpr (e : Expr) (immediate : UnorderedArraySet PremiseIndex)
    (clear : Bool) : RuleTac
```

`Aesop.RuleTac.forwardConst` (definition, [line 192](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Forward.lean#L192))

```lean
def forwardConst (decl : Name) (immediate : UnorderedArraySet PremiseIndex)
    (clear : Bool) : RuleTac
```

`Aesop.RuleTac.forwardTerm` (definition, [line 197](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Forward.lean#L197))

```lean
def forwardTerm (stx : Term) (immediate : UnorderedArraySet PremiseIndex)
    (clear : Bool) : RuleTac
```

`Aesop.RuleTac.forward` (definition, [line 203](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Forward.lean#L203))

```lean
def forward (t : RuleTerm) (immediate : UnorderedArraySet PremiseIndex)
    (clear : Bool) : RuleTac
```

`Aesop.RuleTac.forwardMatches` (definition, [line 209](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Forward.lean#L209))

```lean
def forwardMatches (ms : Array ForwardRuleMatch) : RuleTac
```

`Aesop.RuleTac.forwardMatch` (definition, [line 235](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Forward.lean#L235))

```lean
def forwardMatch (m : ForwardRuleMatch) : RuleTac
```

## Depends on

- [Match](../forward/match.md)

## Sources

- [Aesop/RuleTac/Forward.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Forward.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.RuleTac.Forward.json)
