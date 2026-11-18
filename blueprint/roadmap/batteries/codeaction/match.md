---
catalog: module
lean: Batteries.CodeAction.isMatchTerm, Batteries.CodeAction.getMatchHeaderRange?, Batteries.CodeAction.findAllInfos, Batteries.CodeAction.hasImplicitNonparArg, Batteries.CodeAction.patternFromConstructor, Batteries.CodeAction.matchExpand
statement: formalized
proof: formalized
---

# Match

`Batteries.CodeAction.Match`, in [Batteries/CodeAction/Match.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Match.lean), by Moritz Roos.

`Batteries.CodeAction.isMatchTerm` (definition, [line 22](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Match.lean#L22))

> Filter for the info-nodes to find the match-nodes.

```lean
def isMatchTerm : Info → Bool
```

`Batteries.CodeAction.getMatchHeaderRange?` (definition, [line 27](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Match.lean#L27))

> Returns the String.range that encompasses `match e (with)`.

```lean
def getMatchHeaderRange? (matchStx : Syntax) : Option Lean.Syntax.Range
```

`Batteries.CodeAction.findAllInfos` (definition, [line 48](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Match.lean#L48))

> Flattens an Infotree into an array of Info-nodes that fulfill p.

```lean
partial def findAllInfos (p : Info → Bool) (t : InfoTree) : Array Info
```

`Batteries.CodeAction.hasImplicitNonparArg` (definition, [line 62](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Match.lean#L62))

> Computes for a constructor, if it makes sense to use `@constr` in a match, by determining
> if it has any non-parameter implicit arguments.

```lean
def hasImplicitNonparArg (ctor : Name) (env : Environment) : Bool
```

`Batteries.CodeAction.patternFromConstructor` (definition, [line 73](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Match.lean#L73))

> From a constructor-name e.g. `Option.some` construct the corresponding match pattern, e.g.
> `.some val`. We implement special cases for `Nat` and `List`, `Option` and `Bool` to e.g.
> produce `n + 1` instead of `Nat.succ n`.

```lean
def patternFromConstructor (ctor : Name) (env : Environment) (suffix : String)
    (explicitArgsOnly : Bool) (ctor_hasImplicitNonparArg : Bool): Option String
```

`Batteries.CodeAction.matchExpand` (definition, [line 186](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Match.lean#L186))

> Invoking tactic code action `Generate a list of alternatives for this match.` in the
> following:
> ```lean
> def myfun2 (n : Nat) : Nat :=
>   match n
> ```
> produces:
> ```lean
> def myfun2 (n : Nat) : Nat :=
>   match n with
>   | 0 => _
>   | n + 1 => _
> ```
> Also has support for multiple discriminants, e.g.
> ```
> def myfun3 (o : Option Bool) (m : Nat) : Nat :=
>   match o, m with
> ```
> can be expanded into
> ```
> def myfun3 (o : Option Bool) (m : Nat) : Nat :=
>   match o, m with
>   | none, 0 => _
>   | none, n_2 + 1 => _
>   | some val_1, 0 => _
>   | some val_1, n_2 + 1 => _
> ```
> If it makes sense to use at least one of the constructors with `@` (i.e. iff it has an
> implicit non-parameter argument) then we also show a codeaction that expands every such constructor
> with implicit arguments filled in with the syntax `implicitArg := implicitArg`.
> E.g. invoking `Generate a list of equations with implicit arguments for this match.` in
> the following
> ```lean
> inductive TermWithImplicit (F : Nat → Type u) (α : Type w)
>   | var (x : α) : TermWithImplicit F α
>   | func {l : Nat} (f : F l) (ts : Fin l → TermWithImplicit F α) : TermWithImplicit F α
>
> def myfun4 (t : TermWithImplicit F α) : Nat := by
>   match t with
> ```
> produces
> ```lean
> def myfun4 (t : TermWithImplicit F α) : Nat := by
>   match t with
>   | .var x => _
>   | .func (l := l) f ts => _
> ```
> where the implicit argument `{l : Nat}` is now usable.
> Note that the arguments `F` and `α` are not filled since they are `parameters`
> (a parameter is an argument to an inductive type that is fixed over constructors), i.e.
> they are already determined by the match discriminant `t`. This means they don't provide any
> new information for you.

```lean
def matchExpand : CommandCodeAction
```

## Depends on

- [Miscellaneous code actions](misc.md)
- [List/Basic](../data/part-01/list/part-01/basic.md)

## Sources

- [Batteries/CodeAction/Match.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Match.lean)
