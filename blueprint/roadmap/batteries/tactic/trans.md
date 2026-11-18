---
catalog: module
lean: Trans.simple, Batteries.Tactic.getExplicitFuncArg?, Batteries.Tactic.getExplicitRelArg?, Batteries.Tactic.getExplicitRelArgCore, Batteries.Tactic.TransRelation, Batteries.Tactic.getRel
statement: formalized
proof: formalized
---

# `trans` tactic

`Batteries.Tactic.Trans`, in [Batteries/Tactic/Trans.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Trans.lean), by Siddhartha Gadgil, Mario Carneiro.

> This implements the `trans` tactic, which can apply transitivity theorems with an optional middle
> variable argument.

`Trans.simple` (definition, [line 22](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Trans.lean#L22))

> Compose using transitivity, homogeneous case.

```lean
def Trans.simple {r : α → α → Sort _} [Trans r r r] : r a b → r b c → r a c
```

`Batteries.Tactic.getExplicitFuncArg?` (definition, [line 58](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Trans.lean#L58))

> solving `e ← mkAppM' f #[x]`

```lean
def getExplicitFuncArg? (e : Expr) : MetaM (Option <| Expr × Expr)
```

`Batteries.Tactic.getExplicitRelArg?` (definition, [line 68](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Trans.lean#L68))

> solving `tgt ← mkAppM' rel #[x, z]` given `tgt = f z`

```lean
def getExplicitRelArg? (tgt f z : Expr) : MetaM (Option <| Expr × Expr)
```

`Batteries.Tactic.getExplicitRelArgCore` (definition, [line 84](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Trans.lean#L84))

> refining `tgt ← mkAppM' rel #[x, z]` dropping more arguments if possible

```lean
def getExplicitRelArgCore (tgt rel x z : Expr) : MetaM (Expr × Expr)
```

`Batteries.Tactic.TransRelation` (inductive type, [line 101](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Trans.lean#L101))

> Internal definition for `trans` tactic. Either a binary relation or a non-dependent
> arrow.

```lean
inductive TransRelation
  /-- Expression for transitive relation. -/
  | app (rel : Expr)
  /-- Constant name for transitive relation. -/
  | implies (name : Name) (bi : BinderInfo)
```

`Batteries.Tactic.getRel` (definition, [line 108](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Trans.lean#L108))

> Finds an explicit binary relation in the argument, if possible.

```lean
def getRel (tgt : Expr) : MetaM (Option (TransRelation × Expr × Expr))
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Tactic/Trans.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Trans.lean)
