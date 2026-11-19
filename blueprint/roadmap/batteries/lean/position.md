---
catalog: module
lean: Lean.findLineStart, Lean.findIndentAndIsStart, Lean.Position.getDeclsAfter, String.Pos.Raw.getDeclsAfter, Lean.DeclarationRange.toSyntaxRange, Lean.findDeclarationSyntaxRange?, Lean.withDeclRef?
statement: formalized
proof: formalized
---

# Position

`Batteries.Lean.Position`, in [Batteries/Lean/Position.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Position.lean), by Mario Carneiro, Thomas R. Murrills.

`Lean.findLineStart` (definition, [line 15](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Position.lean#L15))

> Return the beginning of the line contatining character `pos`.

```lean
def findLineStart (s : String) (pos : String.Pos.Raw) : String.Pos.Raw
```

`Lean.findIndentAndIsStart` (definition, [line 22](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Position.lean#L22))

> Return the indentation (number of leading spaces) of the line containing `pos`,
> and whether `pos` is the first non-whitespace character in the line.

```lean
def findIndentAndIsStart (s : String) (pos : String.Pos.Raw) : Nat × Bool
```

`Lean.Position.getDeclsAfter` (definition, [line 38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Position.lean#L38))

> If `pos` is a `Lean.Position`, then `pos.getDeclsAfter` returns the array of names of declarations
> whose selection range begins in position at least `pos`. By using the `selectionRange`, which is
> usually smaller than the `range`, we err on the side of including declarations when possible.
>
> By default, this only inspects the local branch of the environment. This is compatible with being
> used to find declarations from the current command in a linter, where we have already waited for
> async tasks/parallel branches to complete. Further, since the environment exposed to linters does
> not include constants added after the elaboration of the current command, it is safe to use this on
> the command's start position without picking up later declarations.

```lean
protected def Position.getDeclsAfter (env : Environment) (pos : Position)
    (asyncMode := EnvExtension.AsyncMode.local) : Array Name
```

`String.Pos.Raw.getDeclsAfter` (definition, [line 52](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Position.lean#L52))

> If `pos` is a `String.Pos.Raw`, then `pos.getDeclsAfter` returns the array of names of declarations
> whose selection range begins in position at least `pos`. By using the `selectionRange`, which is
> usually smaller than the `range`, we err on the side of including declarations when possible.
>
> By default, this is intended for use in linters, where only the current environment branch needs to
> be checked. See the docstring for `Lean.Position.getDeclsAfter` for details.

```lean
protected def _root_.String.Pos.Raw.getDeclsAfter (env : Environment) (map : FileMap)
    (pos : String.Pos.Raw) (asyncMode := EnvExtension.AsyncMode.local) : Array Name
```

`Lean.DeclarationRange.toSyntaxRange` (definition, [line 58](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Position.lean#L58))

> Converts a `DeclarationRange` to a `Syntax.Range`. This assumes that the
> `DeclarationRange` is sourced in the given `FileMap`.

```lean
def DeclarationRange.toSyntaxRange (map : FileMap) (range : DeclarationRange) : Syntax.Range
```

`Lean.findDeclarationSyntaxRange?` (definition, [line 67](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Position.lean#L67))

> Yields the `Syntax.Range` for the declaration `decl` in the current file. If `decl` is not in
> the current file, yields `none`.
>
> By default, this provides the "selection range", which is usually the declaration's identifier or
> e.g. the `instance` token for an unnamed instance. If `fullRange` is instead set to `true`, this
> returns the full declaration range (which includes modifiers, such as the docstring).

```lean
def findDeclarationSyntaxRange? {m : Type → Type} [Monad m] [MonadEnv m] [MonadLiftT BaseIO m]
    [MonadFileMap m] (decl : Name) (fullRange := false) : m (Option Syntax.Range)
```

`Lean.withDeclRef?` (definition, [line 86](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Position.lean#L86))

> Runs `x` with a synthetic ref that has position info locating the given `decl` if it is defined
> in the current file, or else runs `x` without modifying the ref. This is useful for logging on a
> declaration's name from within linters.
>
> By default, this uses the "selection range" of the declaration, which is usually the declaration's
> identifier or e.g. the `instance` token for an unnamed instance. (This is also the place that
> receives hovers for the declaration.)
>
> If `fullRange` is instead set to `true`, this uses the full declaration range, which includes the
> modifiers (such as the docstring, if there is one) and the body of the declaration.
>
> `canonical` applies to the synthetic syntax generated for the ref; see `Syntax.ofRange`.

```lean
def withDeclRef? {α} {m : Type → Type} [Monad m] [MonadEnv m] [MonadLiftT BaseIO m]
    [MonadFileMap m] [MonadRef m] (decl : Name) (x : m α)
    (fullRange := false) (canonical := true) : m α
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Lean/Position.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Position.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Lean.Position.json)
