---
catalog: module
lean: Aesop.RuleTac.tacticMImpl, Aesop.RuleTac.tacticM, Aesop.RuleTac.ruleTacImpl, Aesop.RuleTac.ruleTac, Aesop.RuleTac.singleRuleTacImpl, Aesop.RuleTac.singleRuleTac, Aesop.RuleTac.tacticStx, Aesop.RuleTac.tacGenImpl, Aesop.RuleTac.tacGen
statement: formalized
proof: formalized
---

# RuleTac/Tactic

`Aesop.RuleTac.Tactic`, in [Aesop/RuleTac/Tactic.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Tactic.lean), by Jannis Limperg, Kaiyu Yang.

`Aesop.RuleTac.tacticMImpl` (definition, [line 18](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Tactic.lean#L18))

```lean
unsafe def tacticMImpl (decl : Name) : RuleTac
```

`Aesop.RuleTac.tacticM` (opaque constant, [line 27](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Tactic.lean#L27))

```lean
opaque tacticM (decl : Name) : RuleTac
```

`Aesop.RuleTac.ruleTacImpl` (definition, [line 30](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Tactic.lean#L30))

```lean
unsafe def ruleTacImpl (decl : Name) : RuleTac
```

`Aesop.RuleTac.ruleTac` (opaque constant, [line 36](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Tactic.lean#L36))

```lean
opaque ruleTac (decl : Name) : RuleTac
```

`Aesop.RuleTac.singleRuleTacImpl` (definition, [line 39](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Tactic.lean#L39))

```lean
unsafe def singleRuleTacImpl (decl : Name) : RuleTac
```

`Aesop.RuleTac.singleRuleTac` (opaque constant, [line 46](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Tactic.lean#L46))

```lean
opaque singleRuleTac (decl : Name) : RuleTac
```

`Aesop.RuleTac.tacticStx` (definition, [line 52](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Tactic.lean#L52))

> Elaborates and runs the given tactic syntax `stx`. The syntax `stx` must be of
> kind `tactic` or `tacticSeq`.

```lean
def tacticStx (stx : Syntax) : RuleTac
```

`Aesop.RuleTac.tacGenImpl` (definition, [line 76](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Tactic.lean#L76))

```lean
unsafe def tacGenImpl (decl : Name) : RuleTac
```

`Aesop.RuleTac.tacGen` (opaque constant, [line 118](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Tactic.lean#L118))

```lean
opaque tacGen (decl : Name) : RuleTac
```

## Depends on

- [Rule Tactic Types](basic.md)

## Sources

- [Aesop/RuleTac/Tactic.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Tactic.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.RuleTac.Tactic.json)
