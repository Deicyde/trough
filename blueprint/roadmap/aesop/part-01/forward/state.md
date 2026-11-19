---
catalog: module
lean: Aesop.RawHyp, Aesop.Hyp, Aesop.Hyp.containsHyp, Aesop.Hyp.isPatSubst, Aesop.InstMap, Aesop.InstMap.find?, Aesop.InstMap.findD, Aesop.InstMap.modify, Aesop.InstMap.insertHyp, Aesop.InstMap.insertMatchCore, Aesop.InstMap.insertMatch, Aesop.InstMap.modifyMapsForSlotsFrom, Aesop.InstMap.eraseHyp, Aesop.InstMap.erasePatSubst, Aesop.InstMap.stats, Aesop.VariableMap, Aesop.VariableMap.find?, Aesop.VariableMap.find, Aesop.VariableMap.modifyM, Aesop.VariableMap.modify, Aesop.VariableMap.addHyp, Aesop.VariableMap.addMatch, Aesop.VariableMap.eraseHyp, Aesop.VariableMap.erasePatSubst, Aesop.VariableMap.findMatches, Aesop.VariableMap.findHyps, Aesop.VariableMap.stats, Aesop.ClusterState, Aesop.ClusterState.slot!, Aesop.ClusterState.findSlot?, Aesop.ClusterState.matchPremise?, Aesop.ClusterState.AddM.Context, Aesop.ClusterState.AddM, Aesop.ClusterState.AddM.run, Aesop.ClusterState.addMatch, Aesop.ClusterState.addHyp, Aesop.ClusterState.addRawHyp, Aesop.ClusterState.addQueuedRawHyps, Aesop.ClusterState.enqueueRawHyp, Aesop.ClusterState.eraseEnqueuedRawHyp, Aesop.ClusterState.eraseHyp, Aesop.ClusterState.erasePatSubst, Aesop.ClusterState.update, Aesop.ClusterState.stats, Aesop.PatSubstSource, Aesop.RuleState, Aesop.ForwardRule.initialRuleState, Aesop.RuleState.enqueueRawHyp, Aesop.RuleState.erasePatSubst, Aesop.RuleState.eraseHyp, Aesop.RuleState.update, Aesop.RuleState.stats, Aesop.ForwardState, Aesop.ForwardState.enqueueHyp, Aesop.ForwardState.enqueuePatSubst, Aesop.ForwardState.enqueuePatSubsts, Aesop.ForwardState.enqueueHypWithPatSubsts, Aesop.ForwardState.erasePatSubsts, Aesop.ForwardState.eraseHyp, Aesop.ForwardState.eraseTargetPatSubsts, Aesop.ForwardState.enqueueTargetPatSubsts, Aesop.ForwardState.update, Aesop.ForwardState.stats
statement: formalized
proof: formalized
---

# Forward/State

`Aesop.Forward.State`, in [Aesop/Forward/State.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean), by Xavier Généreux, Jannis Limperg.

`Aesop.RawHyp` (inductive type, [line 38](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L38))

> A hypothesis that has not yet been matched against a premise, or a rule
> pattern substitution.

```lean
inductive RawHyp where
  /-- The hypothesis. -/
  | fvarId (fvarId : FVarId)
  /-- The rule pattern substitution. -/
  | patSubst (subst : Substitution)
  deriving Inhabited, BEq, Hashable
```

`Aesop.Hyp` (structure, [line 52](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L52))

> A hypothesis that was matched against a premise, or a rule pattern
> substitution.

```lean
structure Hyp where
  /-- The hypothesis, or `none` if this is a rule pattern substitution. -/
  fvarId? : Option FVarId
  /-- The substitution that results from matching the hypothesis against a
  premise or that was derived from the pattern. -/
  subst : Substitution
  deriving Inhabited
```

`Aesop.Hyp.containsHyp` (definition, [line 77](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L77))

> Returns `true` if `h` is the hyp `fvarId` or is a pattern substitution
> containing `fvarId`.

```lean
def containsHyp (fvarId : FVarId) (h : Hyp) : Bool
```

`Aesop.Hyp.isPatSubst` (definition, [line 81](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L81))

> Does this `Hyp` represent a pattern substitution?

```lean
def isPatSubst (h : Hyp) : Bool
```

`Aesop.InstMap` (structure, [line 90](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L90))

> Partial matches associated with a particular slot instantiation. An entry
> `s ↦ e ↦ (ms, hs)` indicates that for the instantiation `e` of slot `s`, we have
> partial matches `ms` and hypotheses `hs`.

```lean
structure InstMap where
  map : PHashMap SlotIndex (EMap (PHashSet Match × PHashSet Hyp))
  deriving Inhabited
```

`Aesop.InstMap.find?` (definition, [line 114](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L114))

> Returns the set of matches and hypotheses associated with a slot `slot`
> with instantiation `inst`.

```lean
def find? (imap : InstMap) (slot : SlotIndex) (inst : Expr) :
    MetaM (Option (PHashSet Match × PHashSet Hyp))
```

`Aesop.InstMap.findD` (definition, [line 122](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L122))

> Returns the set of matches and hypotheses associated with a slot `slot`
> with instantiation `inst`, or `(∅, ∅)` if `slot` and `inst` do not have any
> associated matches.

```lean
def findD (imap : InstMap) (slot : SlotIndex) (inst : Expr) :
    MetaM (PHashSet Match × PHashSet Hyp)
```

`Aesop.InstMap.modify` (definition, [line 129](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L129))

> Applies a transformation to the data associated with `slot` and `inst`.
> If there is no such data, the transformation is applied to `(∅, ∅)`. Returns the
> new instantiation map and the result of `f`.

```lean
def modify (imap : InstMap) (slot : SlotIndex) (inst : Expr)
    (f : PHashSet Match → PHashSet Hyp → PHashSet Match × PHashSet Hyp × α) :
    MetaM (InstMap × α)
```

`Aesop.InstMap.insertHyp` (definition, [line 157](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L157))

> Inserts a hyp associated with slot `slot` and instantiation `inst`.
> The hyp must be a valid assignment for the slot's premise. Returns `true` if
> the hyp was not previously associated with `slot` and `inst`.

```lean
def insertHyp (imap : InstMap) (slot : SlotIndex) (inst : Expr) (hyp : Hyp) :
    MetaM (InstMap × Bool)
```

`Aesop.InstMap.insertMatchCore` (definition, [line 168](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L168))

> Inserts a match associated with slot `slot` and instantiation `inst`.
> The match's level must be `slot`. Returns `true` if the match was not previously
> associated with `slot` and `inst`.

```lean
def insertMatchCore (imap : InstMap) (slot : SlotIndex) (inst : Expr)
    (m : Match) : MetaM (InstMap × Bool)
```

`Aesop.InstMap.insertMatch` (definition, [line 180](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L180))

> Inserts a match. The match `m` is associated with the slot given by its
> level (i.e., the maximal slot for which `m` contains a hypothesis) and the
> instantiation of `var` given by the map's substitution. Returns `true` if the
> match was not previously associated with this slot and instantiation.

```lean
def insertMatch (imap : InstMap) (var : PremiseIndex) (m : Match) :
    BaseM (InstMap × Bool)
```

`Aesop.InstMap.modifyMapsForSlotsFrom` (definition, [line 187](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L187))

> Modify the maps for slot `slot` and all later slots.

```lean
def modifyMapsForSlotsFrom (imap : InstMap) (slot : SlotIndex)
    (f : PHashSet Match → PHashSet Hyp → (PHashSet Match × PHashSet Hyp)) :
    InstMap
```

`Aesop.InstMap.eraseHyp` (definition, [line 203](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L203))

> Remove `hyp` from `slot` and all later slots. For each mapping
> `s ↦ e ↦ (ms, hs)` in `imap`, if `s ≥ slot`, then `hyp` is removed from `hs` and
> any matches containing `hyp` are removed from `ms`.

```lean
def eraseHyp (imap : InstMap) (hyp : FVarId) (slot : SlotIndex) :
    InstMap
```

`Aesop.InstMap.erasePatSubst` (definition, [line 213](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L213))

> Remove the pattern substitution `subst` from `slot` and all later slots.
> For each mapping `s ↦ e ↦ (ms, hs)` in `imap`, if `s ≥ slot`, then `subst` is
> removed from `hs` and any matches containing `subst` are removed from `ms`.

```lean
def erasePatSubst (imap : InstMap) (subst : Substitution) (slot : SlotIndex) :
    InstMap
```

`Aesop.InstMap.stats` (definition, [line 224](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L224))

> Extract stats from an `InstMap`.

```lean
def stats (imap : InstMap) : Array ForwardInstantiationStats
```

`Aesop.VariableMap` (structure, [line 236](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L236))

> Map from variables to the matches and hypotheses of slots whose types
> contain the variables.

```lean
structure VariableMap where
  map : PHashMap PremiseIndex InstMap
  deriving Inhabited
```

`Aesop.VariableMap.find?` (definition, [line 249](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L249))

> Get the `InstMap` associated with a variable.

```lean
def find? (vmap : VariableMap) (var : PremiseIndex) : Option InstMap
```

`Aesop.VariableMap.find` (definition, [line 253](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L253))

> Get the `InstMap` associated with a variable, or an empty `InstMap`.

```lean
def find (vmap : VariableMap) (var : PremiseIndex) : InstMap
```

`Aesop.VariableMap.modifyM` (definition, [line 259](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L259))

> Modify the `InstMap` associated to variable `var`. If no such `InstMap`
> exists, the function `f` is applied to the empty `InstMap` and the result is
> associated with `var`. Returns the new variable map and the result of `f`.

```lean
def modifyM [Monad m] (vmap : VariableMap) (var : PremiseIndex)
    (f : InstMap → m (InstMap × α)) : m (VariableMap × α)
```

`Aesop.VariableMap.modify` (definition, [line 270](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L270))

```lean
def modify (vmap : VariableMap) (var : PremiseIndex) (f : InstMap → InstMap × α) :
    VariableMap × α
```

`Aesop.VariableMap.addHyp` (definition, [line 278](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L278))

> Add a hypothesis `hyp`. Precondition: `hyp` matches the premise of slot
> `slot` with substitution `hyp.subst` (and hence `hyp.subst` contains a mapping
> for each variable in `slot.common`). Returns `true` if the variable map
> changed.

```lean
def addHyp (vmap : VariableMap) (slot : Slot) (hyp : Hyp) : BaseM (VariableMap × Bool)
```

`Aesop.VariableMap.addMatch` (definition, [line 289](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L289))

> Add a match `m`. Precondition: `nextSlot` is the slot with index
> `m.level + 1`. Returns `true` if the variable map changed.

```lean
def addMatch (vmap : VariableMap) (nextSlot : Slot) (m : Match) :
    BaseM (VariableMap × Bool)
```

`Aesop.VariableMap.eraseHyp` (definition, [line 297](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L297))

> Remove a hyp from `slot` and all later slots.

```lean
def eraseHyp (vmap : VariableMap) (hyp : FVarId) (slot : SlotIndex) :
    VariableMap
```

`Aesop.VariableMap.erasePatSubst` (definition, [line 302](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L302))

> Remove the pattern substitution `subst` from `slot` and all later slots.

```lean
def erasePatSubst (vmap : VariableMap) (subst : Substitution) (slot : SlotIndex) :
    VariableMap
```

`Aesop.VariableMap.findMatches` (definition, [line 309](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L309))

> Find matches in slot `slot - 1` whose substitutions are compatible with
> `subst`. Preconditions: `slot.index` is nonzero, `slot.common` is nonempty and
> each variable contained in `slot.common` is also contained in `subst`.

```lean
def findMatches (vmap : VariableMap) (slot : Slot) (subst : Substitution) :
    BaseM (Std.HashSet Match)
```

`Aesop.VariableMap.findHyps` (definition, [line 336](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L336))

> Find hyps in `slot` whose substitutions are compatible with `subst`.
> Precondition: `slot.common` is nonempty and each variable contained in it is
> also contained in `subst`.

```lean
def findHyps (vmap : VariableMap) (slot : Slot) (subst : Substitution) :
    BaseM (Std.HashSet Hyp)
```

`Aesop.VariableMap.stats` (definition, [line 358](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L358))

> Extract stats from a `VariableMap`.

```lean
def stats (vmap : VariableMap) : Array ForwardInstantiationStats
```

`Aesop.ClusterState` (structure, [line 367](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L367))

> Structure representing the state of a slot cluster. …

```lean
structure ClusterState where
  /-- The cluster's slots. -/
  slots : Array Slot
  /-- The premises that appear in the rule's conclusion. These are the same for
  all cluster states of a rule, but are stored here for convenience. -/
  conclusionDeps : Array PremiseIndex
  /-- The variable map for this cluster. -/
  variableMap : VariableMap
  /-- Complete matches for this cluster. -/
  completeMatches : PHashSet Match
  /-- This flag is `true` if all `slotQueues` are potentially nonempty. Before
  that point, we do not add any hyps to the variable maps since the rule cannot
  possibly produce a complete match. -/
  haveHypForEachSlot : Bool
  /-- Hypotheses or pattern substitutions that have been added to the cluster
  state, but have not yet been added to the `variableMap`. -/
  slotQueues : Array (Array RawHyp)
  /-- There is exactly one queue for each slot. -/
  slotQueues_size : slotQueues.size = slots.size
```

`Aesop.ClusterState.slot!` (definition, [line 405](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L405))

> Get the slot with the given index. Panic if the index is invalid.

```lean
def slot! (cs : ClusterState) (slot : SlotIndex) : Slot
```

`Aesop.ClusterState.findSlot?` (definition, [line 409](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L409))

> Get the slot with the given premise index.

```lean
def findSlot? (cs : ClusterState) (i : PremiseIndex) : Option Slot
```

`Aesop.ClusterState.matchPremise?` (definition, [line 414](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L414))

> Match hypothesis `hyp` against the slot with index `slot` in `cs` (which
> must be a valid index).

```lean
def matchPremise? (premises : Array MVarId) (lmvarIds : Array LMVarId)
    (cs : ClusterState) (slot : SlotIndex) (hyp : FVarId) :
    BaseM (Option Substitution)
```

`Aesop.ClusterState.AddM.Context` (structure, [line 457](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L457))

> Context for the `AddM` monad.

```lean
structure AddM.Context where
  /-- Metavariables for the premises of the rule for which a hyp or match is
  being added. When adding hyps, they are unified with these metavariables. -/
  premiseMVars : Array MVarId
  /-- Metavariables for level parameters appearing in the rule's premises. -/
  premiseLMVars : Array LMVarId
```

`Aesop.ClusterState.AddM` (abbreviation, [line 467](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L467))

> A monad for operations that add hyps or matches to a cluster state. The
> monad's state is an array of complete matches discovered while adding
> hyps/matches.

```lean
abbrev AddM
```

`Aesop.ClusterState.AddM.run` (definition, [line 470](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L470))

> Run an `AddM` action.

```lean
def AddM.run (premiseMVars : Array MVarId) (premiseLMVars : Array LMVarId)
    (x : AddM α) : BaseM (α × Array Match)
```

`Aesop.ClusterState.addMatch` (definition, [line 476](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L476))

> Add a match to the cluster state.

```lean
partial def addMatch (cs : ClusterState) (m : Match) : AddM ClusterState
```

`Aesop.ClusterState.addHyp` (definition, [line 503](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L503))

> Add a hypothesis to the cluster state. `hyp.subst` must be the substitution
> that results from applying `h` to `slot`.

```lean
partial def addHyp (cs : ClusterState) (slot : Slot) (h : Hyp) :
    AddM ClusterState
```

`Aesop.ClusterState.addRawHyp` (definition, [line 523](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L523))

> Add a hypothesis or pattern substitution to the cluster state.

```lean
partial def addRawHyp (h : RawHyp) (slot : Slot) (cs : ClusterState) :
    AddM ClusterState
```

`Aesop.ClusterState.addQueuedRawHyps` (definition, [line 538](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L538))

> Insert the raw hyps from `slot`'s queue into the variable map.

```lean
partial def addQueuedRawHyps (slot : Slot) (cs : ClusterState) :
    AddM ClusterState
```

`Aesop.ClusterState.enqueueRawHyp` (definition, [line 551](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L551))

> Add a hypothesis or pattern substitution to the queue for its slot.

```lean
def enqueueRawHyp (h : RawHyp) (pi : PremiseIndex) (cs : ClusterState) :
    ClusterState
```

`Aesop.ClusterState.eraseEnqueuedRawHyp` (definition, [line 565](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L565))

> Erase a `RawHyp` from the slot queue of the given slot.

```lean
def eraseEnqueuedRawHyp (h : RawHyp) (slot : Slot) (cs : ClusterState) :
    ClusterState
```

`Aesop.ClusterState.eraseHyp` (definition, [line 579](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L579))

> Erase a hypothesis from the cluster state's variable map.

```lean
def eraseHyp (h : FVarId) (pi : PremiseIndex) (cs : ClusterState) :
    ClusterState
```

`Aesop.ClusterState.erasePatSubst` (definition, [line 594](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L594))

> Erase a pattern substitution from the cluster state.

```lean
def erasePatSubst (subst : Substitution) (pi : PremiseIndex) (cs : ClusterState) :
    ClusterState
```

`Aesop.ClusterState.update` (definition, [line 609](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L609))

> Update a cluster change, adding any enqueued hypotheses. This may result in
> new complete matches.

```lean
def update (cs : ClusterState) : AddM ClusterState
```

`Aesop.ClusterState.stats` (definition, [line 615](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L615))

> Extract stats from a `ClusterState`.

```lean
def stats (cs : ClusterState) : ForwardClusterStateStats
```

`Aesop.PatSubstSource` (inductive type, [line 623](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L623))

> The source of a pattern substitution. The same substitution can have
> multiple sources.

```lean
inductive PatSubstSource
  /-- The pattern substitution came from the given hypothesis. -/
  | hyp (fvarId : FVarId)
  /-- The pattern substitution came from the goal's target. -/
  | target
  deriving Inhabited, Hashable, BEq
```

`Aesop.RuleState` (structure, [line 634](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L634))

> Forward state for one rule. Updates are lazy: when adding a hyp or pattern
> subst to the rule, it is initially only enqueued in the cluster states. The
> `update` method must be called to actually make the corresponding changes,
> which result in new complete matches for the rule.

```lean
structure RuleState where
  /-- The rule to which this state belongs. -/
  rule : ForwardRule
  /-- States for each of the rule's slot clusters. -/
  clusterStates : Array ClusterState
  /-- The sources of all pattern substitutions present in the
  `clusterStates`. Invariant: each pattern substitution in the cluster states
  is associated with a nonempty set. -/
  patSubstSources : PHashMap Substitution (PHashSet PatSubstSource)
  deriving Inhabited
```

`Aesop.ForwardRule.initialRuleState` (definition, [line 652](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L652))

> The initial (empty) rule state for a given forward rule.

```lean
def ForwardRule.initialRuleState (r : ForwardRule) : RuleState
```

`Aesop.RuleState.enqueueRawHyp` (definition, [line 669](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L669))

> Add a hypothesis or pattern substitution to the rule state. The
> hypothesis's type does not necessarily need to match the given premise. If it
> does not, this is detected by `update` and the hyp is not added.

```lean
def enqueueRawHyp (hyp : RawHyp) (pi : PremiseIndex) (rs : RuleState) : RuleState
```

`Aesop.RuleState.erasePatSubst` (definition, [line 673](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L673))

> Erase a pattern substitution that was obtained from the given source.

```lean
def erasePatSubst (subst : Substitution) (source : PatSubstSource)
    (rs : RuleState) : RuleState
```

`Aesop.RuleState.eraseHyp` (definition, [line 694](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L694))

> Erase a hypothesis from the rule state.

```lean
def eraseHyp (h : FVarId) (pi : PremiseIndex) (rs : RuleState) : RuleState
```

`Aesop.RuleState.update` (definition, [line 700](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L700))

> Add any enqueued hyps to the rule state, potentially generating new
> complete matches in the process.

```lean
def update (goal : MVarId) (rs : RuleState) : BaseM (RuleState × Array ForwardRuleMatch)
```

`Aesop.RuleState.stats` (definition, [line 758](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L758))

> Extract stats from a `RuleState`.

```lean
def stats (rs : RuleState) : ForwardRuleStateStats
```

`Aesop.ForwardState` (structure, [line 766](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L766))

> State representing the non-complete matches of a given set of forward rules
> in a given local context.

```lean
structure ForwardState where
  /-- Map from each rule's name to its `RuleState`-/
  ruleStates : PHashMap RuleName RuleState
  /-- A map from hypotheses to the rules and premises that they matched against
  when they were initially added to the rule state. Invariant: the rule states
  in which a hypothesis `h` appear are exactly those identified by the rule
  names in `hyps[h]`. Furthermore, `h` only appears in slots with premise
  indices greater than or equal to those in `hyps[h]`. -/
  hyps : PHashMap FVarId (PArray (RuleName × PremiseIndex))
  /-- The pattern substitutions present in the rule states. Invariant:
  `patSubsts` maps the source `s` to a rule name `r` and pattern substitution `i`
  iff the rule state of `r` contains `i` with source `s`. -/
  patSubsts : PHashMap PatSubstSource (PArray (RuleName × Substitution))
 deriving Inhabited
```

`Aesop.ForwardState.enqueueHyp` (definition, [line 806](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L806))

> Add a hypothesis to the forward state. If `fs` represents a local context
> `lctx`, then `fs.addHyp h ms` represents `lctx` with `h` added. `ms` must
> overapproximate the rules for which `h` may unify with a maximal premise.

```lean
def enqueueHyp (h : FVarId) (ms : Array (ForwardRule × PremiseIndex))
    (fs : ForwardState) : ForwardState
```

`Aesop.ForwardState.enqueuePatSubst` (definition, [line 817](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L817))

> Add a pattern substitution to the forward state.

```lean
def enqueuePatSubst (r : ForwardRule) (patSubst : Substitution)
    (source : PatSubstSource) (fs : ForwardState) : ForwardState
```

`Aesop.ForwardState.enqueuePatSubsts` (definition, [line 836](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L836))

> Add multiple pattern substitutions to the forward state.

```lean
def enqueuePatSubsts (source : PatSubstSource)
    (patSubsts : Array (ForwardRule × Substitution))
    (fs : ForwardState) : ForwardState
```

`Aesop.ForwardState.enqueueHypWithPatSubsts` (definition, [line 844](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L844))

> Add a hypothesis and to the forward state, along with any rule pattern
> substitutions obtained from it.

```lean
def enqueueHypWithPatSubsts (h : FVarId)
    (ms : Array (ForwardRule × PremiseIndex))
    (patSubsts : Array (ForwardRule × Substitution)) (fs : ForwardState) :
    ForwardState
```

`Aesop.ForwardState.erasePatSubsts` (definition, [line 852](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L852))

> Erase pattern substitutions with the given source.

```lean
def erasePatSubsts (source : PatSubstSource) (fs : ForwardState) :
    ForwardState
```

`Aesop.ForwardState.eraseHyp` (definition, [line 864](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L864))

> Remove a hypothesis from the forward state. If `fs` represents a local
> context `lctx`, then `fs.eraseHyp h` represents `lctx` with `h` removed.

```lean
def eraseHyp (h : FVarId) (fs : ForwardState) : ForwardState
```

`Aesop.ForwardState.eraseTargetPatSubsts` (definition, [line 875](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L875))

> Erase all pattern substitutions whose source is the target.

```lean
def eraseTargetPatSubsts (fs : ForwardState) : ForwardState
```

`Aesop.ForwardState.enqueueTargetPatSubsts` (definition, [line 881](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L881))

> Update the pattern substitutions after the goal's target changed.
> `goal` is the new goal. `newPatSubsts` are the new target's pattern
> substitutions.

```lean
def enqueueTargetPatSubsts (newPatSubsts : Array (ForwardRule × Substitution))
    (fs : ForwardState) : ForwardState
```

`Aesop.ForwardState.update` (definition, [line 891](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L891))

> Update the forward state. This applies any previously enqueued changes to
> all rule states, potentially generating new complete matches in the process.
> If a phase is given, only rules from that phase are updated.

```lean
def update (goal : MVarId) (fs : ForwardState) (phase? : Option PhaseName) :
    BaseM (ForwardState × Array ForwardRuleMatch)
```

`Aesop.ForwardState.stats` (definition, [line 916](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean#L916))

> Extract stats from a `ForwardState`.

```lean
def stats (fs : ForwardState) : ForwardStateStats
```

## Depends on

- [EMap](../emap.md)
- [Match](match.md)

## Sources

- [Aesop/Forward/State.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/State.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Forward.State.json)
