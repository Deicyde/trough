---
catalog: module
lean: Batteries.Tactic.GeneralizeProofs.Config, Batteries.Tactic.GeneralizeProofs.GState, Batteries.Tactic.GeneralizeProofs.MGen, Batteries.Tactic.GeneralizeProofs.MGen.insertFVar, Batteries.Tactic.GeneralizeProofs.AContext, Batteries.Tactic.GeneralizeProofs.AState, Batteries.Tactic.GeneralizeProofs.MAbs, Batteries.Tactic.GeneralizeProofs.MGen.runMAbs, Batteries.Tactic.GeneralizeProofs.MAbs.findProof?, Batteries.Tactic.GeneralizeProofs.MAbs.insertProof, Batteries.Tactic.GeneralizeProofs.MAbs.withLocal, Batteries.Tactic.GeneralizeProofs.MAbs.withRecurse, Batteries.Tactic.GeneralizeProofs.appArgExpectedTypes, Batteries.Tactic.GeneralizeProofs.mkLambdaFVarsUsedOnly, Batteries.Tactic.GeneralizeProofs.abstractProofs, Batteries.Tactic.GeneralizeProofs.initialPropToFVar, Batteries.Tactic.GeneralizeProofs.withGeneralizedProofs, Batteries.Tactic.GeneralizeProofs.generalizeProofsCore, Lean.MVarId.generalizeProofs
statement: formalized
proof: formalized
---

# The `generalize_proofs` tactic

`Batteries.Tactic.GeneralizeProofs`, in [Batteries/Tactic/GeneralizeProofs.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/GeneralizeProofs.lean), by Alex J. Best, Kyle Miller.

> Generalize any proofs occurring in the goal or in chosen hypotheses,
> replacing them by local hypotheses.
> When these hypotheses are named, this makes it easy to refer to these proofs later in a proof,
> commonly useful when dealing with functions like `Classical.choose` that produce data from proofs.
> It is also useful to eliminate proof terms to handle issues with dependent types.
>
> For example:
> ```lean
> def List.nthLe {α} (l : List α) (n : ℕ) (_h : n < l.length) : α := sorry
> example : List.nthLe [1, 2] 1 (by simp) = 2 := by
>   -- ⊢ [1, 2].nthLe 1 ⋯ = 2
>   generalize_proofs h
>   -- h : 1 < [1, 2].length
>   -- ⊢ [1, 2].nthLe 1 h = 2
> ```
>
> The tactic is similar in spirit to `Lean.Meta.AbstractNestedProofs` in core.
> One difference is that it the tactic tries to propagate expected types so that
> we get `1 < [1, 2].length` in the above example rather than `1 < Nat.succ 1`.

`Batteries.Tactic.GeneralizeProofs.Config` (structure, [line 51](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/GeneralizeProofs.lean#L51))

> Configuration for the `generalize_proofs` tactic.

```lean
structure Config where
  /-- The maximum recursion depth when generalizing proofs.
  When `maxDepth > 0`, then proofs are generalized from the types of the generalized proofs too. -/
  maxDepth : Nat := 8
  /-- When `abstract` is `true`, then the tactic will create universally quantified proofs
  to account for bound variables.
  When it is `false` then such proofs are left alone. -/
  abstract : Bool := true
  /-- (Debugging) When `true`, enables consistency checks. -/
  debug : Bool := false
```

`Batteries.Tactic.GeneralizeProofs.GState` (structure, [line 66](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/GeneralizeProofs.lean#L66))

> State for the `MGen` monad.

```lean
structure GState where
  /-- Mapping from propositions to an fvar in the local context with that type. -/
  propToFVar : ExprMap Expr
```

`Batteries.Tactic.GeneralizeProofs.MGen` (abbreviation, [line 72](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/GeneralizeProofs.lean#L72))

> Monad used to generalize proofs.
> Carries `Mathlib.Tactic.GeneralizeProofs.Config` and `Mathlib.Tactic.GeneralizeProofs.State`.

```lean
abbrev MGen
```

`Batteries.Tactic.GeneralizeProofs.MGen.insertFVar` (definition, [line 75](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/GeneralizeProofs.lean#L75))

> Inserts a prop/fvar pair into the `propToFVar` map.

```lean
def MGen.insertFVar (prop fvar : Expr) : MGen Unit
```

`Batteries.Tactic.GeneralizeProofs.AContext` (structure, [line 79](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/GeneralizeProofs.lean#L79))

> Context for the `MAbs` monad.

```lean
structure AContext where
  /-- The local fvars corresponding to bound variables.
  Abstraction needs to be sure that these variables do not appear in abstracted terms. -/
  fvars : Array Expr := #[]
  /-- A copy of `propToFVar` from `GState`. -/
  propToFVar : ExprMap Expr
  /-- The recursion depth, for how many times `visit` is called from within `visitProof. -/
  depth : Nat := 0
  /-- The initial local context, for resetting when recursing. -/
  initLCtx : LocalContext
  /-- The tactic configuration. -/
  config : Config
```

`Batteries.Tactic.GeneralizeProofs.AState` (structure, [line 93](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/GeneralizeProofs.lean#L93))

> State for the `MAbs` monad.

```lean
structure AState where
  /-- The prop/proof triples to add to the local context.
  The proofs must not refer to fvars in `fvars`. -/
  generalizations : Array (Expr × Expr) := #[]
  /-- Map version of `generalizations`. Use `MAbs.findProof?` and `MAbs.insertProof`. -/
  propToProof : ExprMap Expr := {}
```

`Batteries.Tactic.GeneralizeProofs.MAbs` (abbreviation, [line 106](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/GeneralizeProofs.lean#L106))

> Monad used to abstract proofs, to prepare for generalization.
> Has a cache (of expr/type? pairs),
> and it also has a reader context `Mathlib/Tactic/GeneralizeProofs/AContext.lean`
> and a state `Mathlib/Tactic/GeneralizeProofs/AState.lean`.

```lean
abbrev MAbs
```

`Batteries.Tactic.GeneralizeProofs.MGen.runMAbs` (definition, [line 109](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/GeneralizeProofs.lean#L109))

> Runs `MAbs` in `MGen`. Returns the value and the `generalizations`.

```lean
def MGen.runMAbs {α : Type} (mx : MAbs α) : MGen (α × Array (Expr × Expr))
```

`Batteries.Tactic.GeneralizeProofs.MAbs.findProof?` (definition, [line 119](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/GeneralizeProofs.lean#L119))

> Finds a proof of `prop` by looking at `propToFVar` and `propToProof`.

```lean
def MAbs.findProof? (prop : Expr) : MAbs (Option Expr)
```

`Batteries.Tactic.GeneralizeProofs.MAbs.insertProof` (definition, [line 128](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/GeneralizeProofs.lean#L128))

> Generalize `prop`, where `proof` is its proof.

```lean
def MAbs.insertProof (prop pf : Expr) : MAbs Unit
```

`Batteries.Tactic.GeneralizeProofs.MAbs.withLocal` (definition, [line 144](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/GeneralizeProofs.lean#L144))

> Runs `x` with an additional local variable.

```lean
def MAbs.withLocal {α : Type} (fvar : Expr) (x : MAbs α) : MAbs α
```

`Batteries.Tactic.GeneralizeProofs.MAbs.withRecurse` (definition, [line 148](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/GeneralizeProofs.lean#L148))

> Runs `x` with an increased recursion depth and the initial local context, clearing `fvars`.

```lean
def MAbs.withRecurse {α : Type} (x : MAbs α) : MAbs α
```

`Batteries.Tactic.GeneralizeProofs.appArgExpectedTypes` (definition, [line 157](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/GeneralizeProofs.lean#L157))

> Computes expected types for each argument to `f`,
> given that the type of `mkAppN f args` is supposed to be `ty?`
> (where if `ty?` is none, there's no type to propagate inwards).

```lean
def appArgExpectedTypes (f : Expr) (args : Array Expr) (ty? : Option Expr) :
    MetaM (Array (Option Expr))
```

`Batteries.Tactic.GeneralizeProofs.mkLambdaFVarsUsedOnly` (definition, [line 199](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/GeneralizeProofs.lean#L199))

> Does `mkLambdaFVars fvars e` but
> 1. zeta reduces let bindings
> 2. only includes used fvars
> 3. returns the list of fvars that were actually abstracted

```lean
def mkLambdaFVarsUsedOnly (fvars : Array Expr) (e : Expr) : MetaM (Array Expr × Expr)
```

`Batteries.Tactic.GeneralizeProofs.abstractProofs` (definition, [line 230](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/GeneralizeProofs.lean#L230))

> Abstract proofs occurring in the expression.
> A proof is *abstracted* if it is of the form `f a b ...` where `a b ...` are bound variables
> (that is, they are variables that are not present in the initial local context)
> and where `f` contains no bound variables.
> In this form, `f` can be immediately lifted to be a local variable and generalized.
> The abstracted proofs are recorded in the state.
>
> This function is careful to track the type of `e` based on where it's used,
> since the inferred type might be different.
> For example, `(by simp : 1 < [1, 2].length)` has `1 < Nat.succ 1` as the inferred type,
> but from knowing it's an argument to `List.nthLe` we can deduce `1 < [1, 2].length`.

```lean
partial def abstractProofs (e : Expr) (ty? : Option Expr) : MAbs Expr
```

`Batteries.Tactic.GeneralizeProofs.initialPropToFVar` (definition, [line 333](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/GeneralizeProofs.lean#L333))

> Create a mapping of all propositions in the local context to their fvars.

```lean
def initialPropToFVar : MetaM (ExprMap Expr)
```

`Batteries.Tactic.GeneralizeProofs.withGeneralizedProofs` (definition, [line 352](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/GeneralizeProofs.lean#L352))

> Generalizes the proofs in the type `e` and runs `k` in a local context with these propositions.
> This continuation `k` is passed
> 1. an array of fvars for the propositions
> 2. an array of proof terms (extracted from `e`) that prove these propositions
> 3. the generalized `e`, which refers to these fvars
>
> The `propToFVar` map is updated with the new proposition fvars.

```lean
partial def withGeneralizedProofs {α : Type} [Nonempty α] (e : Expr) (ty? : Option Expr)
    (k : Array Expr → Array Expr → Expr → MGen α) :
    MGen α
```

`Batteries.Tactic.GeneralizeProofs.generalizeProofsCore` (definition, [line 385](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/GeneralizeProofs.lean#L385))

> Main loop for `Lean.MVarId.generalizeProofs`.
> The `fvars` array is the array of fvars to generalize proofs for,
> and `rfvars` is the array of fvars that have been reverted.
> The `g` metavariable has all of these fvars reverted.

```lean
partial def generalizeProofsCore
    (g : MVarId) (fvars rfvars : Array FVarId) (target : Bool) :
    MGen (Array Expr × MVarId)
```

`Lean.MVarId.generalizeProofs` (definition, [line 471](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/GeneralizeProofs.lean#L471))

> Generalize proofs in the hypotheses `fvars` and, if `target` is true, the target.
> Returns the fvars for the generalized proofs and the new goal.
>
> If a hypothesis is a proposition and a `let` binding, this will clear the value of the let binding.
>
> If a hypothesis is a proposition that already appears in the local context, it will be eliminated.
>
> Only *nontrivial* proofs are generalized. These are proofs that aren't of the form `f a b ...`
> where `f` is atomic and `a b ...` are bound variables.
> These sorts of proofs cannot be meaningfully generalized, and also these are the sorts of proofs
> that are left in a term after generalization.

```lean
partial def _root_.Lean.MVarId.generalizeProofs
    (g : MVarId) (fvars : Array FVarId) (target : Bool) (config : GeneralizeProofs.Config := {}) :
    MetaM (Array Expr × MVarId)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Proof depends on

- [Additional operations on Expr and related types](../lean/expr.md)

## Sources

- [Batteries/Tactic/GeneralizeProofs.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/GeneralizeProofs.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Tactic.GeneralizeProofs.json)
