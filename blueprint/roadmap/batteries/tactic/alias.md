---
catalog: module
lean: Batteries.Tactic.Alias.AliasInfo, Batteries.Tactic.Alias.AliasInfo.name, Batteries.Tactic.Alias.AliasInfo.toString, Batteries.Tactic.Alias.addAliasDocstring, Batteries.Tactic.Alias.getAliasInfo?, Batteries.Tactic.Alias.getOldAliasInfo?, Batteries.Tactic.Alias.getAliasInfo, Batteries.Tactic.Alias.getAliasPath, Batteries.Tactic.Alias.setAliasInfo, Batteries.Tactic.Alias.setDeprecatedTarget, Batteries.Tactic.Alias.isReducibilityAttr, Batteries.Tactic.Alias.declNamespace?, Batteries.Tactic.Alias.realizeAliasTarget, Batteries.Tactic.Alias.mkIffMpApp
statement: formalized
proof: formalized
---

# The `alias` command

`Batteries.Tactic.Alias`, in [Batteries/Tactic/Alias.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Alias.lean), by Mario Carneiro, David Renshaw, François G. Dorais.

> The `alias` command is used to create synonyms. The plain command can create a synonym of any
> declaration. There is also a version to create synonyms for the forward and reverse implications of
> an iff theorem.

`Batteries.Tactic.Alias.AliasInfo` (inductive type, [line 27](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Alias.lean#L27))

> An alias can be in one of three forms

```lean
inductive AliasInfo where
  /-- Plain alias -/
  | plain (n : Name)
  /-- Forward direction of an iff alias -/
  | forward (n : Name)
  /-- Reverse direction of an iff alias -/
  | reverse (n : Name)
deriving Inhabited
```

`Batteries.Tactic.Alias.AliasInfo.name` (definition, [line 37](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Alias.lean#L37))

> The name underlying an alias target

```lean
def AliasInfo.name : AliasInfo → Name
```

`Batteries.Tactic.Alias.AliasInfo.toString` (definition, [line 43](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Alias.lean#L43))

> The docstring for an alias.

```lean
def AliasInfo.toString : AliasInfo → String
```

`Batteries.Tactic.Alias.addAliasDocstring` (definition, [line 53](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Alias.lean#L53))

> Add a docstring to the alias `declName` if it doesn't already have one.
> This needs to run after elaboration of attributes, because e.g. `inherit_doc` could a add docstring.
> This is also used in `to_additive`/`to_dual`.

```lean
def addAliasDocstring (declName : Name) (info : AliasInfo) : CoreM Unit
```

`Batteries.Tactic.Alias.getAliasInfo?` (definition, [line 64](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Alias.lean#L64))

> Get the alias information for a name

```lean
def getAliasInfo?  [Monad m] [MonadEnv m] (name : Name) : m (Option AliasInfo)
```

`Batteries.Tactic.Alias.getOldAliasInfo?` (definition, [line 68](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Alias.lean#L68))

> Get the old alias information for a name.

```lean
partial def getOldAliasInfo? [Monad m] [MonadEnv m] (name : Name) : m (Option AliasInfo)
```

`Batteries.Tactic.Alias.getAliasInfo` (definition, [line 86](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Alias.lean#L86))

> Get the alias information for a name

```lean
def getAliasInfo [Monad m] [MonadEnv m] (name : Name) : m (Option AliasInfo)
```

`Batteries.Tactic.Alias.getAliasPath` (definition, [line 95](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Alias.lean#L95))

> Returns the path of aliases starting at a given name.
>
> The return value is a pair `(mps, name)` where `name` is the final non-aliased name in the
> alias chain and `mps` is a list of `Bool` indicating the sequence of forward (`true`) and
> reverse (`false`) aliases along the chain.

```lean
partial def getAliasPath [Monad m] [MonadEnv m] (name : Name) : m (List Bool × Name)
```

`Batteries.Tactic.Alias.setAliasInfo` (definition, [line 107](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Alias.lean#L107))

> Set the alias info for a new declaration

```lean
def setAliasInfo [MonadEnv m] (info : AliasInfo) (declName : Name) : m Unit
```

`Batteries.Tactic.Alias.setDeprecatedTarget` (definition, [line 111](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Alias.lean#L111))

> Updates the `deprecated` declaration to point to `target` if no target is provided.

```lean
def setDeprecatedTarget (target : Name) (arr : Array Attribute) : Array Attribute × Bool
```

`Batteries.Tactic.Alias.isReducibilityAttr` (definition, [line 126](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Alias.lean#L126))

> Whether `attr` is one of the attributes that set the reducibility status of a definition.

```lean
def isReducibilityAttr (attr : Name) : Bool
```

`Batteries.Tactic.Alias.declNamespace?` (definition, [line 134](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Alias.lean#L134))

> The namespace that `def` opens while elaborating a declaration named `declName`:
> `Foo.Bar` for `Foo.Bar.baz`, and none for atomic names and names starting with `_root_`.

```lean
def declNamespace? (declName : Name) : Option Name
```

`Batteries.Tactic.Alias.realizeAliasTarget` (definition, [line 146](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Alias.lean#L146))

> Resolves the target of an alias named `aliasName`. If `target` cannot be resolved in the ambient
> scope, it is resolved again with the namespace of `aliasName` open, as `def` would do. The ambient
> scope is tried first so that existing aliases keep resolving to the same constants.

```lean
def realizeAliasTarget (aliasName : Name) (target : Ident) : TermElabM Name
```

`Batteries.Tactic.Alias.mkIffMpApp` (definition, [line 233](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Alias.lean#L233))

> Given a possibly forall-quantified iff expression `prf`, produce a value for one
> of the implication directions (determined by `mp`).

```lean
def mkIffMpApp (mp : Bool) (ty prf : Expr) : MetaM Expr
```

## Depends on

Its statements use no other Batteries module's declarations.

## Proof depends on

- [Code action for @\\[deprecated\\] replacements](../codeaction/deprecated.md)

## Sources

- [Batteries/Tactic/Alias.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Alias.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Tactic.Alias.json)
