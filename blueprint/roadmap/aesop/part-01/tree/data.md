---
catalog: module
lean: Aesop.GoalId, Aesop.GoalId.zero, Aesop.GoalId.one, Aesop.GoalId.succ, Aesop.GoalId.dummy, Aesop.RappId, Aesop.RappId.zero, Aesop.RappId.succ, Aesop.RappId.one, Aesop.RappId.dummy, Aesop.Iteration, Aesop.Iteration.one, Aesop.Iteration.succ, Aesop.Iteration.none, Aesop.NodeState, Aesop.NodeState.isUnknown, Aesop.NodeState.isProven, Aesop.NodeState.isUnprovable, Aesop.NodeState.isIrrelevant, Aesop.NodeState.toEmoji, Aesop.GoalState, Aesop.GoalState.isProvenByRuleApplication, Aesop.GoalState.isProvenByNormalization, Aesop.GoalState.isProven, Aesop.GoalState.isUnprovable, Aesop.GoalState.isUnknown, Aesop.GoalState.toNodeState, Aesop.GoalState.isIrrelevant, Aesop.GoalState.toEmoji, Aesop.NormalizationState, Aesop.NormalizationState.isNormal, Aesop.NormalizationState.isProvenByNormalization, Aesop.NormalizationState.normalizedGoal?, Aesop.GoalOrigin, Aesop.GoalOrigin.originalGoalId?, Aesop.GoalOrigin.toString, Aesop.GoalData, Aesop.MVarClusterData, Aesop.RappData, Aesop.GoalUnsafe, Aesop.MVarClusterUnsafe, Aesop.RappUnsafe, Aesop.TreeSpec, Aesop.treeImpl, Aesop.tree, Aesop.Goal, Aesop.Rapp, Aesop.MVarCluster, Aesop.GoalRef, Aesop.RappRef, Aesop.MVarClusterRef, Aesop.MVarCluster.mk, Aesop.MVarCluster.elim, Aesop.MVarCluster.modify, Aesop.MVarCluster.parent?, Aesop.MVarCluster.setParent, Aesop.MVarCluster.goals, Aesop.MVarCluster.setGoals, Aesop.MVarCluster.isIrrelevant, Aesop.MVarCluster.setIsIrrelevant, Aesop.MVarCluster.state, Aesop.MVarCluster.setState, Aesop.Goal.mk, Aesop.Goal.elim, Aesop.Goal.modify, Aesop.Goal.id, Aesop.Goal.parent, Aesop.Goal.children, Aesop.Goal.origin, Aesop.Goal.depth, Aesop.Goal.state, Aesop.Goal.isIrrelevant, Aesop.Goal.isForcedUnprovable, Aesop.Goal.preNormGoal, Aesop.Goal.normalizationState, Aesop.Goal.mvars, Aesop.Goal.forwardState, Aesop.Goal.forwardRuleMatches, Aesop.Goal.successProbability, Aesop.Goal.addedInIteration, Aesop.Goal.lastExpandedInIteration, Aesop.Goal.failedRapps, Aesop.Goal.unsafeRulesSelected, Aesop.Goal.unsafeQueue, Aesop.Goal.unsafeQueue?, Aesop.Goal.setId, Aesop.Goal.setParent, Aesop.Goal.setChildren, Aesop.Goal.setOrigin, Aesop.Goal.setDepth, Aesop.Goal.setIsIrrelevant, Aesop.Goal.setIsForcedUnprovable, Aesop.Goal.setPreNormGoal, Aesop.Goal.setNormalizationState, Aesop.Goal.setMVars, Aesop.Goal.setForwardState, Aesop.Goal.setForwardRuleMatches, Aesop.Goal.setSuccessProbability, Aesop.Goal.setAddedInIteration, Aesop.Goal.setLastExpandedInIteration, Aesop.Goal.setUnsafeRulesSelected, Aesop.Goal.setUnsafeQueue, Aesop.Goal.setState, Aesop.Goal.setFailedRapps, Aesop.Rapp.mk, Aesop.Rapp.elim, Aesop.Rapp.modify, Aesop.Rapp.id, Aesop.Rapp.parent, Aesop.Rapp.children, Aesop.Rapp.state, Aesop.Rapp.isIrrelevant, Aesop.Rapp.appliedRule, Aesop.Rapp.scriptSteps?, Aesop.Rapp.originalSubgoals, Aesop.Rapp.successProbability, Aesop.Rapp.metaState, Aesop.Rapp.introducedMVars, Aesop.Rapp.assignedMVars, Aesop.Rapp.setId, Aesop.Rapp.setParent, Aesop.Rapp.setChildren, Aesop.Rapp.setState, Aesop.Rapp.setIsIrrelevant, Aesop.Rapp.setAppliedRule, Aesop.Rapp.setScriptSteps?, Aesop.Rapp.setOriginalSubgoals, Aesop.Rapp.setSuccessProbability, Aesop.Rapp.setMetaState, Aesop.Rapp.setIntroducedMVars, Aesop.Rapp.setAssignedMVars, Aesop.Rapp.isSafe, Aesop.Goal.postNormGoalAndMetaState?, Aesop.Goal.postNormGoal?, Aesop.Goal.currentGoal, Aesop.Goal.parentRapp?, Aesop.Goal.parentMetaState, Aesop.Goal.currentGoalAndMetaState, Aesop.Goal.safeRapps, Aesop.Goal.hasSafeRapp, Aesop.Goal.isUnsafeExhausted, Aesop.Goal.isExhausted, Aesop.Goal.isActive, Aesop.Goal.hasProvableRapp, Aesop.Goal.firstProvenRapp?, Aesop.Goal.hasMVar, Aesop.Goal.priority, Aesop.Goal.isNormal, Aesop.Goal.originalGoalId, Aesop.Goal.isRoot, Aesop.Rapp.introducesMVar, Aesop.Rapp.parentPostNormMetaState, Aesop.Rapp.foldSubgoalsM, Aesop.Rapp.forSubgoalsM, Aesop.Rapp.subgoals, Aesop.Rapp.depth, Aesop.MVarCluster.provenGoal?, Aesop.RappRef.getChildAuxDeclNameGenerator
statement: formalized
proof: formalized
---

# Data

`Aesop.Tree.Data`, in [Aesop/Tree/Data.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean), by Jannis Limperg, Asta Halkjær From.

> ## Node IDs

`Aesop.GoalId` (structure, [line 29](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L29))

```lean
structure GoalId where
  toNat : Nat
  deriving Inhabited, DecidableEq
```

`Aesop.GoalId.zero` (definition, [line 35](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L35))

```lean
protected def zero : GoalId
```

`Aesop.GoalId.one` (definition, [line 38](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L38))

```lean
protected def one : GoalId
```

`Aesop.GoalId.succ` (definition, [line 41](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L41))

```lean
protected def succ : GoalId → GoalId
```

`Aesop.GoalId.dummy` (definition, [line 44](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L44))

```lean
def dummy : GoalId
```

> ## Rule Application IDs

`Aesop.RappId` (structure, [line 64](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L64))

```lean
structure RappId where
  toNat : Nat
  deriving Inhabited, DecidableEq
```

`Aesop.RappId.zero` (definition, [line 70](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L70))

```lean
protected def zero : RappId
```

`Aesop.RappId.succ` (definition, [line 73](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L73))

```lean
protected def succ : RappId → RappId
```

`Aesop.RappId.one` (definition, [line 76](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L76))

```lean
protected def one : RappId
```

`Aesop.RappId.dummy` (definition, [line 79](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L79))

```lean
def dummy : RappId
```

> ## Iterations

`Aesop.Iteration` (definition, [line 99](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L99))

```lean
def Iteration
```

`Aesop.Iteration.one` (definition, [line 113](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L113))

```lean
protected def one : Iteration
```

`Aesop.Iteration.succ` (definition, [line 117](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L117))

```lean
protected def succ (i : Iteration) : Iteration
```

`Aesop.Iteration.none` (definition, [line 120](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L120))

```lean
protected def none : Iteration
```

> ## The Tree

`Aesop.NodeState` (inductive type, [line 158](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L158))

> At each point during the search, every node of the tree (goal, rapp or mvar
> cluster) is in one of these states:
>
> - `proven`: the node is proven.
> - `unprovable`: the node is unprovable, i.e. it will never be proven regardless
>   of any future expansions that might be performed.
> - `unknown`: neither of the above.
>
> Every node starts in the `unknown` state and may later become either `proven` or
> `unprovable`. After this, the state does not change any more.

```lean
inductive NodeState
  | unknown
  | proven
  | unprovable
  deriving Inhabited, BEq
```

`Aesop.NodeState.isUnknown` (definition, [line 172](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L172))

```lean
def isUnknown : NodeState → Bool
```

`Aesop.NodeState.isProven` (definition, [line 176](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L176))

```lean
def isProven : NodeState → Bool
```

`Aesop.NodeState.isUnprovable` (definition, [line 180](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L180))

```lean
def isUnprovable : NodeState → Bool
```

`Aesop.NodeState.isIrrelevant` (definition, [line 184](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L184))

```lean
def isIrrelevant : NodeState → Bool
```

`Aesop.NodeState.toEmoji` (definition, [line 189](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L189))

```lean
def toEmoji : NodeState → String
```

`Aesop.GoalState` (inductive type, [line 201](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L201))

> A refinement of the `NodeState`, distinguishing between goals proven during
> normalisation and goals proven by a child rule application.

```lean
inductive GoalState
  | unknown
  | provenByRuleApplication
  | provenByNormalization
  | unprovable
  deriving Inhabited, BEq
```

`Aesop.GoalState.isProvenByRuleApplication` (definition, [line 217](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L217))

```lean
def isProvenByRuleApplication : GoalState → Bool
```

`Aesop.GoalState.isProvenByNormalization` (definition, [line 221](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L221))

```lean
def isProvenByNormalization : GoalState → Bool
```

`Aesop.GoalState.isProven` (definition, [line 225](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L225))

```lean
def isProven : GoalState → Bool
```

`Aesop.GoalState.isUnprovable` (definition, [line 230](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L230))

```lean
def isUnprovable : GoalState → Bool
```

`Aesop.GoalState.isUnknown` (definition, [line 234](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L234))

```lean
def isUnknown : GoalState → Bool
```

`Aesop.GoalState.toNodeState` (definition, [line 238](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L238))

```lean
def toNodeState : GoalState → NodeState
```

`Aesop.GoalState.isIrrelevant` (definition, [line 244](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L244))

```lean
def isIrrelevant (s : GoalState) : Bool
```

`Aesop.GoalState.toEmoji` (definition, [line 247](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L247))

```lean
def toEmoji : GoalState → String
```

`Aesop.NormalizationState` (inductive type, [line 255](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L255))

```lean
inductive NormalizationState
  | notNormal
  | normal (postGoal : MVarId) (postState : Meta.SavedState)
      (script : Array (DisplayRuleName × Option (Array Script.LazyStep)))
  | provenByNormalization (postState : Meta.SavedState)
      (script : Array (DisplayRuleName × Option (Array Script.LazyStep)))
  deriving Inhabited
```

`Aesop.NormalizationState.isNormal` (definition, [line 265](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L265))

```lean
def isNormal : NormalizationState → Bool
```

`Aesop.NormalizationState.isProvenByNormalization` (definition, [line 270](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L270))

```lean
def isProvenByNormalization : NormalizationState → Bool
```

`Aesop.NormalizationState.normalizedGoal?` (definition, [line 275](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L275))

```lean
def normalizedGoal? : NormalizationState → Option MVarId
```

`Aesop.GoalOrigin` (inductive type, [line 294](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L294))

> A goal `G` can be added to the tree for three reasons:
>
> 1. `G` was produced by its parent rule as a subgoal. This is the most common
>    reason.
> 2. `G` was copied because it contains some metavariables which were assigned by
>    its parent rule. In this case, we record goal of which `G` is a copy. We also
>    record the representative of the equivalence class of goals which are copies
>    of each other. E.g. if goal `1` is copied to goal `2` and goal `2` is copied
>    to goal `3`, they are all part of the equivalence class with representative
>    `1`.

```lean
inductive GoalOrigin
  | subgoal
  | copied («from» : GoalId) (rep : GoalId)
  | droppedMVar
  deriving Inhabited
```

`Aesop.GoalOrigin.originalGoalId?` (definition, [line 302](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L302))

```lean
def originalGoalId? : GoalOrigin → Option GoalId
```

`Aesop.GoalOrigin.toString` (definition, [line 306](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L306))

```lean
protected def toString : GoalOrigin → String
```

`Aesop.GoalData` (structure, [line 315](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L315))

```lean
structure GoalData (Rapp MVarCluster : Type) : Type where
  id : GoalId
  parent : IO.Ref MVarCluster
  children : Array (IO.Ref Rapp)
  origin : GoalOrigin
  depth : Nat
  state : GoalState
  isIrrelevant : Bool
  isForcedUnprovable : Bool
    -- True if the goal was designated unprovable 'by force'. This happens when
    -- we reach the search depth limit. Any goal beyond this limit becomes
    -- irrelevant and therefore unprovable.
  preNormGoal : MVarId
    -- The goal before normalisation. The goal after normalisation (if any) is
    -- contained in the `normalizationState`.
  normalizationState : NormalizationState
  mvars : UnorderedArraySet MVarId
    -- Unassigned expression metavariables that appear in the goal, i.e. that
    -- appear in the target or hypotheses of `goal` when interpreted in the
    -- metavar context of `parent?` (or in the global metavar context if
    -- `parent? = none`).
  /-- The forward state reflects the local context of the current goal. Before
  normalisation, this is the local context of `preNormGoal`; after normalisation,
  it is the local context of the post-normalisation goal (unless normalisation
  solved the goal, in which case the forward state is undetermined). -/
  forwardState : ForwardState
  /-- Complete matches of forward rules for the current goal (in the same sense
  as above). -/
  forwardRuleMatches : ForwardRuleMatches
  successProbability : Percent
  addedInIteration : Iteration
  lastExpandedInIteration : Iteration
    -- Iteration 0 means the node has never been expanded.
  unsafeRulesSelected : Bool
  unsafeQueue : UnsafeQueue
  failedRapps : Array RegularRule
  deriving Nonempty
```

`Aesop.MVarClusterData` (structure, [line 353](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L353))

```lean
structure MVarClusterData (Goal Rapp : Type) : Type where
  parent? : Option (IO.Ref Rapp)
  goals : Array (IO.Ref Goal)
  isIrrelevant : Bool
  state : NodeState
  deriving Inhabited
```

`Aesop.RappData` (structure, [line 361](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L361))

```lean
structure RappData (Goal MVarCluster : Type) : Type where
  id : RappId
  parent : IO.Ref Goal
  children : Array (IO.Ref MVarCluster)
  state : NodeState
  isIrrelevant : Bool
  appliedRule : RegularRule
  scriptSteps? : Option (Array Script.LazyStep)
  originalSubgoals : Array MVarId
  successProbability : Percent
  metaState : Meta.SavedState
    -- This is the state *after* the rule was successfully applied, so the goal
    -- mvar is assigned in this state.
  introducedMVars : UnorderedArraySet MVarId
    -- Unassigned expression mvars introduced by this rapp. These are exactly
    -- the unassigned expr mvars that are declared in `metaState`, but not in
    -- the meta state of the parent rapp of `parent`.
  assignedMVars : UnorderedArraySet MVarId
    -- Expression mvars that were previously unassigned but were assigned by
    -- this rapp. These are exactly the expr mvars that (a) are declared and
    -- unassigned in the meta state of the parent rapp of `parent` and (b) are
    -- assigned in `metaState`.
  deriving Nonempty
```

`Aesop.GoalUnsafe` (inductive type, [line 386](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L386))

```lean
unsafe inductive GoalUnsafe
  | mk (d : GoalData RappUnsafe MVarClusterUnsafe)
```

`Aesop.MVarClusterUnsafe` (inductive type, [line 389](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L389))

```lean
unsafe inductive MVarClusterUnsafe
  | mk (d : MVarClusterData GoalUnsafe RappUnsafe)
```

`Aesop.RappUnsafe` (inductive type, [line 392](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L392))

```lean
unsafe inductive RappUnsafe
  | mk (d : RappData GoalUnsafe MVarClusterUnsafe)
```

`Aesop.TreeSpec` (structure, [line 396](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L396))

```lean
structure TreeSpec where
  Goal : Type
  Rapp : Type
  MVarCluster : Type
  introGoal : GoalData Rapp MVarCluster → Goal
  elimGoal : Goal → GoalData Rapp MVarCluster
  introRapp : RappData Goal MVarCluster → Rapp
  elimRapp : Rapp → RappData Goal MVarCluster
  introMVarCluster : MVarClusterData Goal Rapp → MVarCluster
  elimMVarCluster : MVarCluster → MVarClusterData Goal Rapp
```

`Aesop.treeImpl` (definition, [line 411](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L411))

```lean
unsafe def treeImpl : TreeSpec
```

`Aesop.tree` (opaque constant, [line 423](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L423))

```lean
opaque tree : TreeSpec
```

`Aesop.Goal` (definition, [line 425](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L425))

```lean
def Goal
```

`Aesop.Rapp` (definition, [line 426](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L426))

```lean
def Rapp
```

`Aesop.MVarCluster` (definition, [line 427](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L427))

```lean
def MVarCluster
```

`Aesop.GoalRef` (abbreviation, [line 429](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L429))

```lean
abbrev GoalRef
```

`Aesop.RappRef` (abbreviation, [line 430](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L430))

```lean
abbrev RappRef
```

`Aesop.MVarClusterRef` (abbreviation, [line 431](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L431))

```lean
abbrev MVarClusterRef
```

`Aesop.MVarCluster.mk` (definition, [line 437](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L437))

```lean
protected def mk : MVarClusterData Goal Rapp → MVarCluster
```

`Aesop.MVarCluster.elim` (definition, [line 444](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L444))

```lean
protected def elim : MVarCluster → MVarClusterData Goal Rapp
```

`Aesop.MVarCluster.modify` (definition, [line 448](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L448))

```lean
protected def modify (f : MVarClusterData Goal Rapp → MVarClusterData Goal Rapp)
    (c : MVarCluster) : MVarCluster
```

`Aesop.MVarCluster.parent?` (definition, [line 453](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L453))

```lean
def parent? (c : MVarCluster) : Option RappRef
```

`Aesop.MVarCluster.setParent` (definition, [line 457](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L457))

```lean
def setParent (parent? : Option RappRef) (c : MVarCluster) : MVarCluster
```

`Aesop.MVarCluster.goals` (definition, [line 461](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L461))

```lean
def goals (c : MVarCluster) : Array GoalRef
```

`Aesop.MVarCluster.setGoals` (definition, [line 465](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L465))

```lean
def setGoals (goals : Array GoalRef) (c : MVarCluster) : MVarCluster
```

`Aesop.MVarCluster.isIrrelevant` (definition, [line 469](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L469))

```lean
def isIrrelevant (c : MVarCluster) : Bool
```

`Aesop.MVarCluster.setIsIrrelevant` (definition, [line 473](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L473))

```lean
def setIsIrrelevant (isIrrelevant : Bool) (c : MVarCluster) : MVarCluster
```

`Aesop.MVarCluster.state` (definition, [line 477](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L477))

```lean
def state (c : MVarCluster) : NodeState
```

`Aesop.MVarCluster.setState` (definition, [line 481](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L481))

```lean
def setState (state : NodeState) (c : MVarCluster) : MVarCluster
```

`Aesop.Goal.mk` (definition, [line 490](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L490))

```lean
protected def mk : GoalData Rapp MVarCluster → Goal
```

`Aesop.Goal.elim` (definition, [line 494](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L494))

```lean
protected def elim : Goal → GoalData Rapp MVarCluster
```

`Aesop.Goal.modify` (definition, [line 498](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L498))

```lean
protected def modify (f : GoalData Rapp MVarCluster → GoalData Rapp MVarCluster)
    (g : Goal) : Goal
```

`Aesop.Goal.id` (definition, [line 503](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L503))

```lean
def id (g : Goal) : GoalId
```

`Aesop.Goal.parent` (definition, [line 507](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L507))

```lean
def parent (g : Goal) : MVarClusterRef
```

`Aesop.Goal.children` (definition, [line 511](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L511))

```lean
def children (g : Goal) : Array RappRef
```

`Aesop.Goal.origin` (definition, [line 515](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L515))

```lean
def origin (g : Goal) : GoalOrigin
```

`Aesop.Goal.depth` (definition, [line 519](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L519))

```lean
def depth (g : Goal) : Nat
```

`Aesop.Goal.state` (definition, [line 523](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L523))

```lean
def state (g : Goal) : GoalState
```

`Aesop.Goal.isIrrelevant` (definition, [line 527](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L527))

```lean
def isIrrelevant (g : Goal) : Bool
```

`Aesop.Goal.isForcedUnprovable` (definition, [line 531](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L531))

```lean
def isForcedUnprovable (g : Goal) : Bool
```

`Aesop.Goal.preNormGoal` (definition, [line 535](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L535))

```lean
def preNormGoal (g : Goal) : MVarId
```

`Aesop.Goal.normalizationState` (definition, [line 539](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L539))

```lean
def normalizationState (g : Goal) : NormalizationState
```

`Aesop.Goal.mvars` (definition, [line 543](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L543))

```lean
def mvars (g : Goal) : UnorderedArraySet MVarId
```

`Aesop.Goal.forwardState` (definition, [line 547](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L547))

```lean
def forwardState (g : Goal) : ForwardState
```

`Aesop.Goal.forwardRuleMatches` (definition, [line 551](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L551))

```lean
def forwardRuleMatches (g : Goal) : ForwardRuleMatches
```

`Aesop.Goal.successProbability` (definition, [line 555](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L555))

```lean
def successProbability (g : Goal) : Percent
```

`Aesop.Goal.addedInIteration` (definition, [line 559](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L559))

```lean
def addedInIteration (g : Goal) : Iteration
```

`Aesop.Goal.lastExpandedInIteration` (definition, [line 563](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L563))

```lean
def lastExpandedInIteration (g : Goal) : Iteration
```

`Aesop.Goal.failedRapps` (definition, [line 567](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L567))

```lean
def failedRapps (g : Goal) : Array RegularRule
```

`Aesop.Goal.unsafeRulesSelected` (definition, [line 571](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L571))

```lean
def unsafeRulesSelected (g : Goal) : Bool
```

`Aesop.Goal.unsafeQueue` (definition, [line 575](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L575))

```lean
def unsafeQueue (g : Goal) : UnsafeQueue
```

`Aesop.Goal.unsafeQueue?` (definition, [line 579](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L579))

```lean
def unsafeQueue? (g : Goal) : Option UnsafeQueue
```

`Aesop.Goal.setId` (definition, [line 583](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L583))

```lean
def setId (id : GoalId) (g : Goal) : Goal
```

`Aesop.Goal.setParent` (definition, [line 587](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L587))

```lean
def setParent (parent : MVarClusterRef) (g : Goal) : Goal
```

`Aesop.Goal.setChildren` (definition, [line 591](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L591))

```lean
def setChildren (children : Array RappRef) (g : Goal) : Goal
```

`Aesop.Goal.setOrigin` (definition, [line 595](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L595))

```lean
def setOrigin (origin : GoalOrigin) (g : Goal) : Goal
```

`Aesop.Goal.setDepth` (definition, [line 599](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L599))

```lean
def setDepth (depth : Nat) (g : Goal) : Goal
```

`Aesop.Goal.setIsIrrelevant` (definition, [line 603](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L603))

```lean
def setIsIrrelevant (isIrrelevant : Bool) (g : Goal) : Goal
```

`Aesop.Goal.setIsForcedUnprovable` (definition, [line 607](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L607))

```lean
def setIsForcedUnprovable (isForcedUnprovable : Bool) (g : Goal) : Goal
```

`Aesop.Goal.setPreNormGoal` (definition, [line 611](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L611))

```lean
def setPreNormGoal (preNormGoal : MVarId) (g : Goal) : Goal
```

`Aesop.Goal.setNormalizationState` (definition, [line 615](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L615))

```lean
def setNormalizationState (normalizationState : NormalizationState) (g : Goal) :
    Goal
```

`Aesop.Goal.setMVars` (definition, [line 620](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L620))

```lean
def setMVars (mvars : UnorderedArraySet MVarId) (g : Goal) : Goal
```

`Aesop.Goal.setForwardState` (definition, [line 624](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L624))

```lean
def setForwardState (forwardState : ForwardState) (g : Goal) : Goal
```

`Aesop.Goal.setForwardRuleMatches` (definition, [line 628](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L628))

```lean
def setForwardRuleMatches (forwardRuleMatches : ForwardRuleMatches) (g : Goal) :
    Goal
```

`Aesop.Goal.setSuccessProbability` (definition, [line 633](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L633))

```lean
def setSuccessProbability (successProbability : Percent) (g : Goal) : Goal
```

`Aesop.Goal.setAddedInIteration` (definition, [line 637](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L637))

```lean
def setAddedInIteration (addedInIteration : Iteration) (g : Goal) : Goal
```

`Aesop.Goal.setLastExpandedInIteration` (definition, [line 641](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L641))

```lean
def setLastExpandedInIteration (lastExpandedInIteration : Iteration) (g : Goal) :
    Goal
```

`Aesop.Goal.setUnsafeRulesSelected` (definition, [line 646](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L646))

```lean
def setUnsafeRulesSelected (unsafeRulesSelected : Bool) (g : Goal) : Goal
```

`Aesop.Goal.setUnsafeQueue` (definition, [line 650](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L650))

```lean
def setUnsafeQueue (unsafeQueue : UnsafeQueue) (g : Goal) : Goal
```

`Aesop.Goal.setState` (definition, [line 654](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L654))

```lean
def setState (state : GoalState) (g : Goal) : Goal
```

`Aesop.Goal.setFailedRapps` (definition, [line 658](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L658))

```lean
def setFailedRapps (failedRapps : Array RegularRule) (g : Goal) : Goal
```

`Aesop.Rapp.mk` (definition, [line 676](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L676))

```lean
protected def mk : RappData Goal MVarCluster → Rapp
```

`Aesop.Rapp.elim` (definition, [line 680](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L680))

```lean
protected def elim : Rapp → RappData Goal MVarCluster
```

`Aesop.Rapp.modify` (definition, [line 684](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L684))

```lean
protected def modify (f : RappData Goal MVarCluster → RappData Goal MVarCluster)
    (r : Rapp) : Rapp
```

`Aesop.Rapp.id` (definition, [line 689](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L689))

```lean
def id (r : Rapp) : RappId
```

`Aesop.Rapp.parent` (definition, [line 693](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L693))

```lean
def parent (r : Rapp) : GoalRef
```

`Aesop.Rapp.children` (definition, [line 697](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L697))

```lean
def children (r : Rapp) : Array MVarClusterRef
```

`Aesop.Rapp.state` (definition, [line 701](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L701))

```lean
def state (r : Rapp) : NodeState
```

`Aesop.Rapp.isIrrelevant` (definition, [line 705](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L705))

```lean
def isIrrelevant (r : Rapp) : Bool
```

`Aesop.Rapp.appliedRule` (definition, [line 709](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L709))

```lean
def appliedRule (r : Rapp) : RegularRule
```

`Aesop.Rapp.scriptSteps?` (definition, [line 713](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L713))

```lean
def scriptSteps? (r : Rapp) : Option (Array Script.LazyStep)
```

`Aesop.Rapp.originalSubgoals` (definition, [line 717](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L717))

```lean
def originalSubgoals (r : Rapp) : Array MVarId
```

`Aesop.Rapp.successProbability` (definition, [line 721](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L721))

```lean
def successProbability (r : Rapp) : Percent
```

`Aesop.Rapp.metaState` (definition, [line 725](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L725))

```lean
def metaState (r : Rapp) : Meta.SavedState
```

`Aesop.Rapp.introducedMVars` (definition, [line 729](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L729))

```lean
def introducedMVars (r : Rapp) : UnorderedArraySet MVarId
```

`Aesop.Rapp.assignedMVars` (definition, [line 733](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L733))

```lean
def assignedMVars (r : Rapp) : UnorderedArraySet MVarId
```

`Aesop.Rapp.setId` (definition, [line 737](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L737))

```lean
def setId (id : RappId) (r : Rapp) : Rapp
```

`Aesop.Rapp.setParent` (definition, [line 741](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L741))

```lean
def setParent (parent : GoalRef) (r : Rapp) : Rapp
```

`Aesop.Rapp.setChildren` (definition, [line 745](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L745))

```lean
def setChildren (children : Array MVarClusterRef) (r : Rapp) : Rapp
```

`Aesop.Rapp.setState` (definition, [line 749](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L749))

```lean
def setState (state : NodeState) (r : Rapp) : Rapp
```

`Aesop.Rapp.setIsIrrelevant` (definition, [line 753](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L753))

```lean
def setIsIrrelevant (isIrrelevant : Bool) (r : Rapp) : Rapp
```

`Aesop.Rapp.setAppliedRule` (definition, [line 757](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L757))

```lean
def setAppliedRule (appliedRule : RegularRule) (r : Rapp) : Rapp
```

`Aesop.Rapp.setScriptSteps?` (definition, [line 761](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L761))

```lean
def setScriptSteps? (scriptSteps? : Option (Array Script.LazyStep)) (r : Rapp) :
    Rapp
```

`Aesop.Rapp.setOriginalSubgoals` (definition, [line 766](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L766))

```lean
def setOriginalSubgoals (originalSubgoals : Array MVarId)
    (r : Rapp) : Rapp
```

`Aesop.Rapp.setSuccessProbability` (definition, [line 771](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L771))

```lean
def setSuccessProbability (successProbability : Percent) (r : Rapp) : Rapp
```

`Aesop.Rapp.setMetaState` (definition, [line 775](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L775))

```lean
def setMetaState (metaState : Meta.SavedState) (r : Rapp) : Rapp
```

`Aesop.Rapp.setIntroducedMVars` (definition, [line 779](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L779))

```lean
def setIntroducedMVars (introducedMVars : UnorderedArraySet MVarId)
    (r : Rapp) : Rapp
```

`Aesop.Rapp.setAssignedMVars` (definition, [line 784](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L784))

```lean
def setAssignedMVars (assignedMVars : UnorderedArraySet MVarId) (r : Rapp) :
    Rapp
```

> ## Miscellaneous Queries

`Aesop.Rapp.isSafe` (definition, [line 802](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L802))

```lean
def Rapp.isSafe (r : Rapp) : Bool
```

`Aesop.Goal.postNormGoalAndMetaState?` (definition, [line 811](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L811))

```lean
def postNormGoalAndMetaState? (g : Goal) : Option (MVarId × Meta.SavedState)
```

`Aesop.Goal.postNormGoal?` (definition, [line 816](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L816))

```lean
def postNormGoal? (g : Goal) : Option MVarId
```

`Aesop.Goal.currentGoal` (definition, [line 819](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L819))

```lean
def currentGoal (g : Goal) : MVarId
```

`Aesop.Goal.parentRapp?` (definition, [line 822](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L822))

```lean
def parentRapp? (g : Goal) : BaseIO (Option RappRef)
```

`Aesop.Goal.parentMetaState` (definition, [line 825](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L825))

```lean
def parentMetaState (g : Goal) (rootMetaState : Meta.SavedState) :
    BaseIO Meta.SavedState
```

`Aesop.Goal.currentGoalAndMetaState` (definition, [line 831](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L831))

```lean
def currentGoalAndMetaState (g : Goal) (rootMetaState : Meta.SavedState) :
    MetaM (MVarId × Meta.SavedState)
```

`Aesop.Goal.safeRapps` (definition, [line 837](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L837))

```lean
def safeRapps (g : Goal) : BaseIO (Array RappRef)
```

`Aesop.Goal.hasSafeRapp` (definition, [line 840](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L840))

```lean
def hasSafeRapp (g : Goal) : BaseIO Bool
```

`Aesop.Goal.isUnsafeExhausted` (definition, [line 843](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L843))

```lean
def isUnsafeExhausted (g : Goal) : Bool
```

`Aesop.Goal.isExhausted` (definition, [line 846](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L846))

```lean
def isExhausted (g : Goal) : BaseIO Bool
```

`Aesop.Goal.isActive` (definition, [line 849](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L849))

```lean
def isActive (g : Goal) : BaseIO Bool
```

`Aesop.Goal.hasProvableRapp` (definition, [line 852](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L852))

```lean
def hasProvableRapp (g : Goal) : BaseIO Bool
```

`Aesop.Goal.firstProvenRapp?` (definition, [line 855](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L855))

```lean
def firstProvenRapp? (g : Goal) : BaseIO (Option RappRef)
```

`Aesop.Goal.hasMVar` (definition, [line 859](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L859))

```lean
def hasMVar (g : Goal) : Bool
```

`Aesop.Goal.priority` (definition, [line 862](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L862))

```lean
def priority (g : Goal) : Percent
```

`Aesop.Goal.isNormal` (definition, [line 865](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L865))

```lean
def isNormal (g : Goal) : Bool
```

`Aesop.Goal.originalGoalId` (definition, [line 868](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L868))

```lean
def originalGoalId (g : Goal) : GoalId
```

`Aesop.Goal.isRoot` (definition, [line 871](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L871))

```lean
def isRoot (g : Goal) : BaseIO Bool
```

`Aesop.Rapp.introducesMVar` (definition, [line 879](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L879))

```lean
def introducesMVar (r : Rapp) : Bool
```

`Aesop.Rapp.parentPostNormMetaState` (definition, [line 882](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L882))

```lean
def parentPostNormMetaState (r : Rapp) (rootMetaState : Meta.SavedState) :
    BaseIO Meta.SavedState
```

`Aesop.Rapp.foldSubgoalsM` (definition, [line 886](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L886))

```lean
def foldSubgoalsM [Monad m] [MonadLiftT (ST IO.RealWorld) m] (init : σ)
    (f : σ → GoalRef → m σ) (r : Rapp) : m σ
```

`Aesop.Rapp.forSubgoalsM` (definition, [line 891](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L891))

```lean
def forSubgoalsM [Monad m] [MonadLiftT (ST IO.RealWorld) m]
    (f : GoalRef → m Unit) (r : Rapp) : m Unit
```

`Aesop.Rapp.subgoals` (definition, [line 895](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L895))

```lean
def subgoals [Monad m] [MonadLiftT (ST IO.RealWorld) m] (r : Rapp) :
    m (Array GoalRef)
```

`Aesop.Rapp.depth` (definition, [line 899](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L899))

```lean
def depth (r : Rapp) : BaseIO Nat
```

`Aesop.MVarCluster.provenGoal?` (definition, [line 907](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L907))

```lean
def provenGoal? (c : MVarCluster) : BaseIO (Option GoalRef)
```

`Aesop.RappRef.getChildAuxDeclNameGenerator` (definition, [line 918](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean#L918))

> Get a `DeclNameGenerator` for auxiliary declarations that can be used by
> children of this rapp. Successive calls to this function return
> `DeclNameGenerators` that are guaranteed to generate distinct names.

```lean
def getChildAuxDeclNameGenerator (r : RappRef) : BaseIO DeclNameGenerator
```

## Depends on

- [Forward/State](../forward/state.md)
- [ForwardRuleMatches](data-2/forwardrulematches.md)
- [UnsafeQueue](unsafequeue.md)

## Sources

- [Aesop/Tree/Data.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Tree.Data.json)
