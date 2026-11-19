---
catalog: module
lean: Aesop.optimizeFocusRenameI, Aesop.optimizeInitialRenameI, Aesop.optimizeSyntax
statement: formalized
proof: formalized
---

# OptimizeSyntax

`Aesop.Script.OptimizeSyntax`, in [Aesop/Script/OptimizeSyntax.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/OptimizeSyntax.lean), by Jannis Limperg.

`Aesop.optimizeFocusRenameI` (definition, [line 19](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/OptimizeSyntax.lean#L19))

```lean
partial def optimizeFocusRenameI : Syntax → m Syntax
```

`Aesop.optimizeInitialRenameI` (definition, [line 41](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/OptimizeSyntax.lean#L41))

```lean
def optimizeInitialRenameI : Syntax → m Syntax
  | stx@`(tacticSeq| $tacs:tactic*) => do
    let tacs := tacs.getElems
    let some (tac : TSyntax `tactic) := tacs[0]?
      | return stx
    match tac with
    | `(tactic| rename_i $[$ns:ident]*) =>
      let usedNames := tacs[1:].foldl (init := ∅) λ usedNames stx =>
        addIdents usedNames stx.raw
      let mut dropUntil := 0
      for n in ns do
        if usedNames.contains n.getId then
          break
        else
          dropUntil
```

`Aesop.optimizeSyntax` (definition, [line 75](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/OptimizeSyntax.lean#L75))

```lean
def optimizeSyntax (stx : TSyntax kind) : m (TSyntax kind)
```

## Depends on

Its statements use no other Aesop module's declarations.

## Sources

- [Aesop/Script/OptimizeSyntax.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/OptimizeSyntax.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Script.OptimizeSyntax.json)
