---
catalog: module
lean: Cslib.LTS.IsSimulation, Cslib.LTS.IsHomSimulation, Cslib.LTS.Similarity, Cslib.LTS.HomSimilarity, Cslib.LTS.HomSimilarity.refl, Cslib.LTS.IsSimulation.comp, Cslib.LTS.Similarity.trans, Cslib.LTS.IsSimulation.sup, Cslib.LTS.IsSimulation.sim_trace, Cslib.LTS.IsSimulationMap, Cslib.LTS.IsSimulationMap.isSimulation, Cslib.LTS.IsSimulationMap.sim_trace, Cslib.LTS.SimulationEquiv, Cslib.LTS.HomSimulationEquiv, Cslib.LTS.HomSimulationEquiv.refl, Cslib.LTS.SimulationEquiv.symm, Cslib.LTS.SimulationEquiv.trans, Cslib.LTS.HomSimulationEquiv.eqv, Cslib.LTS.IsSimulation.follow, Cslib.LTS.IsSimulation.follow_internal, Cslib.LTS.IsSimulation.isSimulation_saturate_left, Cslib.LTS.IsSimulation.mono, Cslib.LTS.IsSimulation.match_deterministic, Cslib.LTS.IsSimulation.follow_deterministic
statement: formalized
proof: formalized
---

# IsSimulation and Similarity

`Cslib.Foundations.Semantics.LTS.Simulation`, in [Cslib/Foundations/Semantics/LTS/Simulation.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean), by Fabrizio Montesi.

> A simulation is a binary relation on the states of two `LTS`s: if two states `s₁` and `s2` are
> related by a simulation, then `s2` can mimic all transitions of `s₁` in their respective LTSs.
> Furthermore, the derivatives reaches through these transitions remain related by the simulation.
>
> Similarity is the largest simulation: given an `LTS`, it relates any two states that are related
> by a simulation for that LTS.
>
> The module provides abbreviations for the homogeneous case of comparing states in the same LTS.
>
> For an introduction to theory of simulation, we refer to [Sangiorgi2011].
>
> ## Main definitions
>
> - `IsSimulation lts₁ lts₂ r`: the relation `r` on the states of `lts₁` and `lts₂` is a simulation.
> - `IsSimulationMap lts₁ lts₂ f`: the map `f` from the states of `lts₁` to those of `lts₂` sends
> transitions to transitions.
> - `Similarity lts₁ lts₂` is the binary relation that relates any two states related by some
> simulation on `lts₁` and `lts₂`.
> - `SimulationEquiv lts₁ lts₂` is the binary relation on the states of `lts₁` and `lts₂` that relates
> any two states similar to each other.
>
> ## Notations
>
> - `s₁ ≤[lts₁, lts₂] s₂`: the states `s₁` and `s2` are similar under `lts₁` and `lts₂`.
> - `s₁ ≤≥[lts₁, lts₂] s2`: the states `s₁` and `s2` are simulation equivalent under `lts₁` and
> `lts₂`.
>
> ## Main statements
>
> - `HomSimulationEquiv.eqv`: homogeneous simulation equivalence is an equivalence relation.

`Cslib.LTS.IsSimulation` (definition, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L57))

> A relation is a simulation if, whenever it relates two states in an lts,
> any transition originating from the first state is mimicked by a transition from the second state
> and the reached derivatives are themselves related.

```lean
def IsSimulation (lts₁ : LTS State₁ Label) (lts₂ : LTS State₂ Label) (r : State₁ → State₂ → Prop) :
    Prop
```

`Cslib.LTS.IsHomSimulation` (abbreviation, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L62))

> A homogeneous simulation is a simulation where the underlying LTSs are the same.

```lean
abbrev IsHomSimulation (lts : LTS State Label)
```

`Cslib.LTS.Similarity` (definition, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L65))

> Two states are similar if they are related by some simulation.

```lean
def Similarity (lts₁ : LTS State₁ Label) (lts₂ : LTS State₂ Label) : State₁ → State₂ → Prop
```

`Cslib.LTS.HomSimilarity` (abbreviation, [line 78](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L78))

> Homogeneous similarity is similarity where the underlying LTSs are the same.

```lean
abbrev HomSimilarity (lts : LTS State Label)
```

`Cslib.LTS.HomSimilarity.refl` (theorem, [line 84](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L84))

> Homogeneous similarity is reflexive.

```lean
theorem HomSimilarity.refl (s : State) : s ≤[lts] s
```

`Cslib.LTS.IsSimulation.comp` (theorem, [line 89](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L89))

> The composition of two simulations is a simulation.

```lean
theorem IsSimulation.comp
    (r1 : State₁ → State₂ → Prop)
    (r2 : State₂ → State₃ → Prop)
    (h1 : IsSimulation lts₁ lts₂ r1) (h2 : IsSimulation lts₂ lts₃ r2) :
    IsSimulation lts₁ lts₃ (Relation.Comp r1 r2)
```

`Cslib.LTS.Similarity.trans` (theorem, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L101))

> Similarity is transitive.

```lean
theorem Similarity.trans (h1 : s₁ ≤[lts₁,lts₂] s2) (h2 : s2 ≤[lts₂,lts₃] s₃) :
    s₁ ≤[lts₁,lts₃] s₃
```

`Cslib.LTS.IsSimulation.sup` (theorem, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L107))

```lean
theorem IsSimulation.sup (hr : IsSimulation lts₁ lts₂ r)
    (hs : IsSimulation lts₁ lts₂ s) : IsSimulation lts₁ lts₂ (r ⊔ s)
```

`Cslib.LTS.IsSimulation.sim_trace` (theorem, [line 115](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L115))

```lean
theorem IsSimulation.sim_trace (hr : IsSimulation lts₁ lts₂ r) (hrel : r s₁ s₂) :
    ∀ μs s₁', lts₁.MTr s₁ μs s₁' → ∃ s₂', lts₂.MTr s₂ μs s₂' ∧ r s₁' s₂'
```

`Cslib.LTS.IsSimulationMap` (definition, [line 131](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L131))

> A map of states is a simulation map if it sends every transition of `lts₁` to a transition of
> `lts₂` with the same label.

```lean
def IsSimulationMap (lts₁ : LTS State₁ Label) (lts₂ : LTS State₂ Label) (f : State₁ → State₂) :
    Prop
```

`Cslib.LTS.IsSimulationMap.isSimulation` (theorem, [line 136](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L136))

> The graph of a simulation map is a simulation.

```lean
theorem IsSimulationMap.isSimulation {lts₁ : LTS State₁ Label} {lts₂ : LTS State₂ Label}
    {f : State₁ → State₂} (hf : IsSimulationMap lts₁ lts₂ f) :
    IsSimulation lts₁ lts₂ fun s t => t = f s
```

`Cslib.LTS.IsSimulationMap.sim_trace` (theorem, [line 143](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L143))

> A simulation map sends multistep transitions to multistep transitions.

```lean
theorem IsSimulationMap.sim_trace {lts₁ : LTS State₁ Label} {lts₂ : LTS State₂ Label}
    {f : State₁ → State₂} (hf : IsSimulationMap lts₁ lts₂ f) {s s' : State₁} {μs : List Label}
    (h : lts₁.MTr s μs s') : lts₂.MTr (f s) μs (f s')
```

`Cslib.LTS.SimulationEquiv` (definition, [line 151](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L151))

> Simulation equivalence relates all states `s₁` and `s2` such that `s₁ ≤[lts₁ lts₂] s2` and
> `s2 ≤[lts₂ lts₁] s₁`.

```lean
def SimulationEquiv (lts₁ : LTS State₁ Label) (lts₂ : LTS State₂ Label) :
    State₁ → State₂ → Prop
```

`Cslib.LTS.HomSimulationEquiv` (abbreviation, [line 162](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L162))

> Homogeneous simulation equivalence.

```lean
abbrev HomSimulationEquiv (lts : LTS State Label)
```

`Cslib.LTS.HomSimulationEquiv.refl` (theorem, [line 168](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L168))

> Homogeneous simulation equivalence is reflexive.

```lean
theorem HomSimulationEquiv.refl (s : State) : s ≤≥[lts] s
```

`Cslib.LTS.SimulationEquiv.symm` (theorem, [line 172](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L172))

> Simulation equivalence is symmetric.

```lean
theorem SimulationEquiv.symm {State₁ State₂ Label : Type*}
    {lts₁ : LTS State₁ Label} {lts₂ : LTS State₂ Label} {s₁ : State₁} {s2 : State₂}
    (h : s₁ ≤≥[lts₁,lts₂] s2) : s2 ≤≥[lts₂,lts₁] s₁
```

`Cslib.LTS.SimulationEquiv.trans` (theorem, [line 178](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L178))

> Simulation equivalence is transitive.

```lean
theorem SimulationEquiv.trans (h1 : s₁ ≤≥[lts₁,lts₂] s2) (h2 : s2 ≤≥[lts₂,lts₃] s₃) :
    s₁ ≤≥[lts₁,lts₃] s₃
```

`Cslib.LTS.HomSimulationEquiv.eqv` (theorem, [line 183](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L183))

> Homogeneous simulation equivalence is an equivalence relation.

```lean
theorem HomSimulationEquiv.eqv : Equivalence (· ≤≥[lts] ·)
```

`Cslib.LTS.IsSimulation.follow` (theorem, [line 197](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L197))

> Helper for following a transition by the first state in a pair of a simulation.

```lean
theorem IsSimulation.follow
    (hb : IsSimulation lts₁ lts₂ r) (hr : r s₁ s₂) (htr : lts₁.Tr s₁ μ s₁') :
    ∃ s₂', lts₂.Tr s₂ μ s₂' ∧ r s₁' s₂'
```

`Cslib.LTS.IsSimulation.follow_internal` (lemma, [line 202](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L202))

> Utility theorem for following internal transitions along a saturated lts.

```lean
lemma IsSimulation.follow_internal [HasTau Label] {lts₁ : LTS State₁ Label}
    {lts₂ : LTS State₂ Label} (h : IsSimulation lts₁ lts₂.saturate r) (hr : r s₁ s₂)
    (hstr : lts₁.τSTr s₁ s₁') : ∃ s₂', lts₂.τSTr s₂ s₂' ∧ r s₁' s₂'
```

`Cslib.LTS.IsSimulation.isSimulation_saturate_left` (theorem, [line 214](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L214))

> If the right-hand lts is saturated, a simulation lifts along saturating the left-hand lts.

```lean
theorem IsSimulation.isSimulation_saturate_left [HasTau Label] {lts₁ : LTS State₁ Label}
    {lts₂ : LTS State₂ Label} (h : IsSimulation lts₁ lts₂.saturate r) :
    IsSimulation lts₁.saturate lts₂.saturate r
```

`Cslib.LTS.IsSimulation.mono` (theorem, [line 230](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L230))

> Simulation is preserved by removing transitions on the left, and adding transitions on the
> right.

```lean
theorem IsSimulation.mono (h₁ : lts₁'.Tr ≤ lts₁.Tr) (h₂ : lts₂.Tr ≤ lts₂'.Tr)
    (h : IsSimulation lts₁ lts₂ r) : IsSimulation lts₁' lts₂' r
```

`Cslib.LTS.IsSimulation.match_deterministic` (theorem, [line 238](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L238))

> When a deterministic state matches a transition in a simulation, then the derivatives are still
> in the simulation.

```lean
theorem IsSimulation.match_deterministic (hb : IsSimulation lts₁ lts₂ r) (hr : r s₁ s₂)
    (hdet : lts₂.DeterministicStateLabel s₂ μ) (htr₁ : lts₁.Tr s₁ μ s₁') (htr₂ : lts₂.Tr s₂ μ s₂') :
    r s₁' s₂'
```

`Cslib.LTS.IsSimulation.follow_deterministic` (theorem, [line 245](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean#L245))

> If a state is deterministic for `μ`, then any transition made by a related state in a
> simulation is matched by a unique transition.

```lean
theorem IsSimulation.follow_deterministic (hb : IsSimulation lts₁ lts₂ r) (hr : r s₁ s₂)
    (hdet : lts₂.DeterministicStateLabel s₂ μ) (htr : lts₁.Tr s₁ μ s₁') :
    ∃! s₂', lts₂.Tr s₂ μ s₂' ∧ r s₁' s₂'
```

## Depends on

- [LTS with a special "internal" transition `τ`](hastau.md)

## Sources

- [Cslib/Foundations/Semantics/LTS/Simulation.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Simulation.lean)
