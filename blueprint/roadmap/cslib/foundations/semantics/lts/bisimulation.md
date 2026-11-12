---
catalog: module
lean: Cslib.LTS.IsBisimulation, Cslib.LTS.IsBisimulation.isSimulation, Cslib.LTS.IsBisimulation.flip_isSimulation, Cslib.LTS.IsBisimulation.isSimulation_iff, Cslib.LTS.IsBisimulation.follow_fst, Cslib.LTS.IsBisimulation.follow_snd, Cslib.LTS.IsBisimulation.match_deterministic, Cslib.LTS.IsBisimulation.match_deterministic₂, Cslib.LTS.IsBisimulation.follow_fst_deterministic, Cslib.LTS.IsBisimulation.follow_snd_deterministic, Cslib.LTS.IsHomBisimulation, Cslib.LTS.Bisimilarity, Cslib.LTS.HomBisimilarity, Cslib.LTS.Bisimilarity.follow_fst, Cslib.LTS.Bisimilarity.follow_snd, Cslib.LTS.HomBisimilarity.refl, Cslib.LTS.HomBisimilarity.of_image_eq, Cslib.LTS.IsBisimulation.inv, Cslib.LTS.Bisimilarity.symm, Cslib.LTS.IsBisimulation.comp, Cslib.LTS.Bisimilarity.trans, Cslib.LTS.HomBisimilarity.eqv, Cslib.LTS.IsBisimulation.simulationEquiv, Cslib.LTS.IsBisimulation.sup, Cslib.LTS.Bisimilarity.isBisimulation, Cslib.LTS.IsBisimulation.le_bisimilarity, Cslib.LTS.Bisimilarity.gfp, Cslib.LTS.coe_sup, Cslib.LTS.IsBisimulation.bot, Cslib.LTS.UpToHomBisimilarity, Cslib.LTS.IsBisimulationUpTo, Cslib.LTS.IsBisimulationUpTo.isBisimulation, Cslib.LTS.IsBisimulationUpTo.le_bisimilarity, Cslib.LTS.IsBisimulation.bisim_trace, Cslib.LTS.IsBisimulation.traceEq, Cslib.LTS.Bisimilarity.le_traceEq, Cslib.LTS.IsBisimulation.traceEq_not_bisim, Cslib.LTS.Bisimilarity.bisimilarity_neq_traceEq, Cslib.LTS.IsBisimulation.deterministic_traceEq_isBisimulation, Cslib.LTS.Bisimilarity.deterministic_traceEq_bisim, Cslib.LTS.Deterministic.bisim_tfae, Cslib.LTS.Bisimilarity.deterministic_bisim_eq_traceEq, Cslib.LTS.HomBisimilarity.symm_simulation, Cslib.LTS.IsWeakBisimulation, Cslib.LTS.IsHomWeakBisimulation, Cslib.LTS.WeakBisimilarity, Cslib.LTS.HomWeakBisimilarity, Cslib.LTS.IsSWBisimulation, Cslib.LTS.IsSWBisimulation.isSimulation, Cslib.LTS.IsSWBisimulation.isSimulation_flip, Cslib.LTS.IsSWBisimulation.iff_isSimulation, Cslib.LTS.isWeakBisimulation_iff_isSWBisimulation, Cslib.LTS.IsWeakBisimulation.isSwBisimulation, Cslib.LTS.IsSWBisimulation.isWeakBisimulation, Cslib.LTS.WeakBisimilarity.weakBisim_eq_swBisim, Cslib.LTS.HomWeakBisimilarity.refl, Cslib.LTS.IsWeakBisimulation.inv, Cslib.LTS.WeakBisimilarity.symm, Cslib.LTS.IsWeakBisimulation.comp, Cslib.LTS.IsSWBisimulation.comp, Cslib.LTS.WeakBisimilarity.trans, Cslib.LTS.HomWeakBisimilarity.eqv, Cslib.LTS.reindex, Cslib.LTS.reindex.tr, Cslib.LTS.reindex.isBisimulation, Cslib.LTS.reindex.bisim_trace, Cslib.LTS.reindex.bisim_trace_iff
statement: formalized
proof: formalized
---

# Bisimulation and Bisimilarity

`Cslib.Foundations.Semantics.LTS.Bisimulation`, in [Cslib/Foundations/Semantics/LTS/Bisimulation.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean), by Fabrizio Montesi, Thomas Waring.

> A bisimulation is a binary relation on the states of two `LTS`s, which establishes a tight semantic
> correspondence. More specifically, if two states `s₁` and `s₂` are related by a bisimulation, then
> `s₁` can mimic all transitions of `s₂` and vice versa. Furthermore, the derivatives reached through
> these transitions remain related by the bisimulation.
>
> Bisimilarity is the largest bisimulation between two LTSs: it relates any two states that are
> related by some bisimulation between those LTSs.
>
> Weak bisimulation (resp. bisimilarity) is the relaxed version of bisimulation (resp. bisimilarity)
> whereby internal actions performed by processes can be ignored.
>
> For an introduction to theory of bisimulation, we refer to [Sangiorgi2011].
>
> ## Main definitions
>
> - `IsBisimulation lts₁ lts₂ r`: the relation `r` is a bisimulation between `lts₁` and `lts₂`.
> - `Bisimilarity lts₁ lts₂`: states related by some bisimulation between `lts₁` and `lts₂`.
> - `UpToHomBisimilarity lts₁ lts₂ r`: the closure of `r` under bisimilarity in each LTS.
> - `IsBisimulationUpTo lts₁ lts₂ r`: transitions from states related by `r` can be matched with
>   derivatives in `UpToHomBisimilarity lts₁ lts₂ r`.
> - `IsWeakBisimulation lts₁ lts₂ r`: the relation `r` is a weak bisimulation.
> - `WeakBisimilarity lts₁ lts₂`: states related by some weak bisimulation.
> - `IsSWBisimulation lts₁ lts₂ r`: a characterization of weak bisimulation using single-transition
>   challenges, which we prove to be sound and complete.
>
> The `Hom` variants specialize these definitions to comparing states in the same LTS.
>
> ## Notations
>
> - `s₁ ~[lts₁,lts₂] s₂`: the states `s₁` and `s₂` are bisimilar under `lts₁` and `lts₂`.
> - `s₁ ≈[lts₁,lts₂] s₂`: the states `s₁` and `s₂` are weakly bisimilar under `lts₁` and `lts₂`.
> - `s₁ ~[lts] s₂` and `s₁ ≈[lts] s₂`: the corresponding homogeneous relations.
>
> ## Main statements
>
> - `LTS.IsBisimulation.inv`: the inverse of a bisimulation is a bisimulation.
> - `HomBisimilarity.eqv`: homogeneous bisimilarity is an equivalence relation (see `Equivalence`).
> - `Bisimilarity.isBisimulation`: bisimilarity is itself a bisimulation.
> - `IsBisimulation.le_bisimilarity`: bisimilarity is the largest bisimulation.
> - `Bisimilarity.gfp`: the union of bisimilarity and any bisimulation is equal to bisimilarity.
> - `LTS.IsBisimulationUpTo.isBisimulation`: if `r` is a bisimulation up to bisimilarity,
>   `UpToHomBisimilarity lts₁ lts₂ r` is a bisimulation.
> - `LTS.IsBisimulationUpTo.le_bisimilarity`: a bisimulation up to bisimilarity relates only
>   bisimilar states.
> - `LTS.IsBisimulation.traceEq`: any bisimulation that relates two states implies that they are
> trace equivalent (see `TraceEq`).
> - `Bisimilarity.deterministic_bisim_eq_traceEq`: in a deterministic LTS, bisimilarity and trace
> equivalence coincide.
> - `HomBisimilarity.symm_simulation`: homogeneous bisimilarity can be characterized through
>   symmetric simulations.
> - `WeakBisimilarity.weakBisim_eq_swBisim`: weak bisimulation and sw-bisimulation coincide.
> - `HomWeakBisimilarity.eqv`: homogeneous weak bisimilarity is an equivalence relation.

`Cslib.LTS.IsBisimulation` (definition, [line 81](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L81))

> A relation is a bisimulation if, whenever it relates two states,
> the transitions originating from these states mimic each other and the reached
> derivatives are themselves related.

```lean
def IsBisimulation (lts₁ : LTS State₁ Label) (lts₂ : LTS State₂ Label)
    (r : State₁ → State₂ → Prop) : Prop
```

> ## Relation to simulation

`Cslib.LTS.IsBisimulation.isSimulation` (theorem, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L92))

> Any bisimulation is also a simulation.

```lean
theorem IsBisimulation.isSimulation : IsBisimulation lts₁ lts₂ r → IsSimulation lts₁ lts₂ r
```

`Cslib.LTS.IsBisimulation.flip_isSimulation` (theorem, [line 96](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L96))

> The inverse of a bisimulation is a simulation.

```lean
theorem IsBisimulation.flip_isSimulation :
    IsBisimulation lts₁ lts₂ r → IsSimulation lts₂ lts₁ (flip r)
```

`Cslib.LTS.IsBisimulation.isSimulation_iff` (theorem, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L101))

> A relation is a bisimulation iff both it and its inverse are simulations.

```lean
theorem IsBisimulation.isSimulation_iff :
    IsBisimulation lts₁ lts₂ r ↔ (IsSimulation lts₁ lts₂ r ∧ IsSimulation lts₂ lts₁ (flip r))
```

`Cslib.LTS.IsBisimulation.follow_fst` (theorem, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L107))

> Helper for following a transition by the first state in a pair of a `Bisimulation`.

```lean
theorem IsBisimulation.follow_fst
    (hb : IsBisimulation lts₁ lts₂ r) (hr : r s₁ s₂) (htr : lts₁.Tr s₁ μ s₁') :
    ∃ s₂', lts₂.Tr s₂ μ s₂' ∧ r s₁' s₂'
```

`Cslib.LTS.IsBisimulation.follow_snd` (theorem, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L113))

> Helper for following a transition by the second state in a pair of a `Bisimulation`.

```lean
theorem IsBisimulation.follow_snd
    (hb : IsBisimulation lts₁ lts₂ r) (hr : r s₁ s₂) (htr : lts₂.Tr s₂ μ s₂') :
    ∃ s₁', lts₁.Tr s₁ μ s₁' ∧ r s₁' s₂'
```

`Cslib.LTS.IsBisimulation.match_deterministic` (theorem, [line 120](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L120))

> If the unique transition of a state is matched by a related state in a bisimulation,
> then the derivatives are still in the bisimulation.

```lean
theorem IsBisimulation.match_deterministic
    (hb : IsBisimulation lts₁ lts₂ r)
    (hr : r s₁ s₂)
    (hdet : lts₁.DeterministicStateLabel s₁ μ)
    (htr₁ : lts₁.Tr s₁ μ s₁')
    (htr₂ : lts₂.Tr s₂ μ s₂') : r s₁' s₂'
```

`Cslib.LTS.IsBisimulation.match_deterministic₂` (theorem, [line 131](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L131))

> If the unique transition of a state is matched by a related state in the inverse of a
> bisimulation, then the derivatives are still in the bisimulation.

```lean
theorem IsBisimulation.match_deterministic₂
    (hb : IsBisimulation lts₁ lts₂ r)
    (hr : r s₁ s₂)
    (hdet : lts₂.DeterministicStateLabel s₂ μ)
    (htr₁ : lts₁.Tr s₁ μ s₁')
    (htr₂ : lts₂.Tr s₂ μ s₂') : r s₁' s₂'
```

`Cslib.LTS.IsBisimulation.follow_fst_deterministic` (theorem, [line 141](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L141))

> If a state is deterministic for `μ`, then any transition made by a related state in a
> bisimulation is matched by a unique transition (left variant).

```lean
theorem IsBisimulation.follow_fst_deterministic (hb : IsBisimulation lts₁ lts₂ r) (hr : r s₁ s₂)
    (hdet : lts₂.DeterministicStateLabel s₂ μ) (htr : lts₁.Tr s₁ μ s₁') :
    ∃! s₂', lts₂.Tr s₂ μ s₂' ∧ r s₁' s₂'
```

`Cslib.LTS.IsBisimulation.follow_snd_deterministic` (theorem, [line 148](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L148))

> If a state is deterministic for `μ`, then any transition made by a related state in a
> bisimulation is matched by a unique transition (right variant).

```lean
theorem IsBisimulation.follow_snd_deterministic
    (hb : IsBisimulation lts₁ lts₂ r)
    (hr : r s₁ s₂)
    (hdet : lts₁.DeterministicStateLabel s₁ μ)
    (htr : lts₂.Tr s₂ μ s₂') : ∃! s₁', lts₁.Tr s₁ μ s₁' ∧ r s₁' s₂'
```

`Cslib.LTS.IsHomBisimulation` (abbreviation, [line 156](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L156))

> A homogeneous bisimulation is a bisimulation where the underlying LTSs are the same.

```lean
abbrev IsHomBisimulation (lts : LTS State Label)
```

`Cslib.LTS.Bisimilarity` (definition, [line 160](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L160))

> Two states are bisimilar if they are related by some bisimulation.

```lean
def Bisimilarity (lts₁ : LTS State₁ Label) (lts₂ : LTS State₂ Label) : State₁ → State₂ → Prop
```

`Cslib.LTS.HomBisimilarity` (abbreviation, [line 172](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L172))

> Homogeneous bisimilarity is bisimilarity where the underlying LTSs are the same.

```lean
abbrev HomBisimilarity (lts : LTS State Label)
```

`Cslib.LTS.Bisimilarity.follow_fst` (theorem, [line 178](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L178))

> Helper for following a transition by the first state in a pair of a `Bisimilarity`.

```lean
theorem Bisimilarity.follow_fst (hr : s₁ ~[lts₁,lts₂] s₂) (htr : lts₁.Tr s₁ μ s₁') :
    ∃ s₂', lts₂.Tr s₂ μ s₂' ∧ s₁' ~[lts₁,lts₂ ] s₂'
```

`Cslib.LTS.Bisimilarity.follow_snd` (theorem, [line 182](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L182))

> Helper for following a transition by the first state in a pair of a `Bisimilarity`.

```lean
theorem Bisimilarity.follow_snd (hr : s₁ ~[lts₁,lts₂] s₂) (htr : lts₂.Tr s₂ μ s₂') :
    ∃ s₁', lts₁.Tr s₁ μ s₁' ∧ s₁' ~[lts₁,lts₂] s₂'
```

`Cslib.LTS.HomBisimilarity.refl` (theorem, [line 187](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L187))

> Homogeneous bisimilarity is reflexive.

```lean
theorem HomBisimilarity.refl (s : State) : s ~[lts] s
```

`Cslib.LTS.HomBisimilarity.of_image_eq` (theorem, [line 192](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L192))

> States with the same image function are bisimilar.

```lean
theorem HomBisimilarity.of_image_eq {lts : LTS State Label} {s₁ s₂ : State}
    (h : lts.image s₁ = lts.image s₂) : s₁ ~[lts] s₂
```

`Cslib.LTS.IsBisimulation.inv` (theorem, [line 203](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L203))

> The inverse of a bisimulation is a bisimulation.

```lean
theorem IsBisimulation.inv (h : IsBisimulation lts₁ lts₂ r) :
  IsBisimulation lts₂ lts₁ (flip r)
```

`Cslib.LTS.Bisimilarity.symm` (theorem, [line 209](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L209))

> Bisimilarity is symmetric.

```lean
theorem Bisimilarity.symm {State₁ State₂ : Type*}
    {lts₁ : LTS State₁ Label} {lts₂ : LTS State₂ Label} {s₁ : State₁} {s₂ : State₂}
    (h : s₁ ~[lts₁,lts₂] s₂) : s₂ ~[lts₂,lts₁] s₁
```

`Cslib.LTS.IsBisimulation.comp` (theorem, [line 216](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L216))

> The composition of two bisimulations is a bisimulation.

```lean
theorem IsBisimulation.comp
    (h1 : IsBisimulation lts₁ lts₂ r1) (h2 : IsBisimulation lts₂ lts₃ r2) :
  IsBisimulation lts₁ lts₃ (Relation.Comp r1 r2)
```

`Cslib.LTS.Bisimilarity.trans` (theorem, [line 222](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L222))

> Bisimilarity is transitive.

```lean
theorem Bisimilarity.trans
    (h1 : s₁ ~[lts₁,lts₂] s₂) (h2 : s₂ ~[lts₂,lts₃] s₃) :
  s₁ ~[lts₁,lts₃] s₃
```

`Cslib.LTS.HomBisimilarity.eqv` (theorem, [line 231](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L231))

> Homogeneous bisimilarity is an equivalence relation.

```lean
theorem HomBisimilarity.eqv :
  Equivalence (HomBisimilarity lts)
```

`Cslib.LTS.IsBisimulation.simulationEquiv` (theorem, [line 244](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L244))

> Bisimulation implies simulation equivalence.

```lean
theorem IsBisimulation.simulationEquiv (h : IsBisimulation lts₁ lts₂ r) (hrel : r s₁ s₂) :
    s₁ ≤≥[lts₁,lts₂] s₂
```

`Cslib.LTS.IsBisimulation.sup` (theorem, [line 249](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L249))

> The union of two bisimulations is a bisimulation.

```lean
theorem IsBisimulation.sup (hrb : IsBisimulation lts₁ lts₂ r) (hsb : IsBisimulation lts₁ lts₂ s) :
    IsBisimulation lts₁ lts₂ (r ⊔ s)
```

`Cslib.LTS.Bisimilarity.isBisimulation` (theorem, [line 257](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L257))

> Bisimilarity is a bisimulation.

```lean
theorem Bisimilarity.isBisimulation (lts₁ : LTS State₁ Label) (lts₂ : LTS State₂ Label) :
  IsBisimulation lts₁ lts₂ (Bisimilarity lts₁ lts₂)
```

`Cslib.LTS.IsBisimulation.le_bisimilarity` (theorem, [line 262](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L262))

> Bisimilarity is the largest bisimulation.

```lean
theorem IsBisimulation.le_bisimilarity (h : IsBisimulation lts₁ lts₂ r) :
    r ≤ (Bisimilarity lts₁ lts₂)
```

`Cslib.LTS.Bisimilarity.gfp` (theorem, [line 269](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L269))

> The union of bisimilarity with any bisimulation is bisimilarity.

```lean
theorem Bisimilarity.gfp (r : State₁ → State₂ → Prop) (h : IsBisimulation lts₁ lts₂ r) :
    (Bisimilarity lts₁ lts₂) ⊔ r = Bisimilarity lts₁ lts₂
```

> ## Order properties

`Cslib.LTS.coe_sup` (lemma, [line 283](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L283))

```lean
lemma coe_sup (r s : {r // IsBisimulation lts₁ lts₂ r}) :
(↑(r ⊔ s) : State₁ → State₂ → Prop) = (r : State₁ → State₂ → Prop) ⊔ s
```

`Cslib.LTS.IsBisimulation.bot` (theorem, [line 295](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L295))

> The empty (heterogeneous) relation is a bisimulation.

```lean
theorem IsBisimulation.bot : IsBisimulation lts₁ lts₂ Relation.emptyHRelation
```

> ## Bisimulation up-to

`Cslib.LTS.UpToHomBisimilarity` (definition, [line 322](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L322))

> The closure of `r` under bisimilarity in each LTS: `s₁` and `s₂` are related if there are
> `t₁` and `t₂` with `s₁ ~[lts₁] t₁`, `r t₁ t₂`, and `t₂ ~[lts₂] s₂`.

```lean
def UpToHomBisimilarity (lts₁ : LTS State₁ Label) (lts₂ : LTS State₂ Label)
    (r : State₁ → State₂ → Prop) : State₁ → State₂ → Prop
```

`Cslib.LTS.IsBisimulationUpTo` (definition, [line 329](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L329))

> A relation `r` is a bisimulation up to homogeneous bisimilarity if, whenever it relates two
> states, their transitions can be matched with derivatives related by
> `UpToHomBisimilarity lts₁ lts₂ r`.

```lean
def IsBisimulationUpTo (lts₁ : LTS State₁ Label) (lts₂ : LTS State₂ Label)
    (r : State₁ → State₂ → Prop) : Prop
```

`Cslib.LTS.IsBisimulationUpTo.isBisimulation` (theorem, [line 342](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L342))

> If `r` is a bisimulation up to bisimilarity, its closure
> `UpToHomBisimilarity lts₁ lts₂ r` is a bisimulation.

```lean
theorem IsBisimulationUpTo.isBisimulation (h : IsBisimulationUpTo lts₁ lts₂ r) :
    IsBisimulation lts₁ lts₂ (UpToHomBisimilarity lts₁ lts₂ r)
```

`Cslib.LTS.IsBisimulationUpTo.le_bisimilarity` (theorem, [line 367](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L367))

> A bisimulation up to bisimilarity relates only bisimilar states.

```lean
theorem IsBisimulationUpTo.le_bisimilarity (h : IsBisimulationUpTo lts₁ lts₂ r) :
    r ≤ Bisimilarity lts₁ lts₂
```

`Cslib.LTS.IsBisimulation.bisim_trace` (theorem, [line 375](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L375))

> If two states are related by a bisimulation, they can mimic each other's multi-step
> transitions.

```lean
theorem IsBisimulation.bisim_trace (hb : IsBisimulation lts₁ lts₂ r) (hr : r s₁ s₂) :
    ∀ μs s₁', lts₁.MTr s₁ μs s₁' → ∃ s₂', lts₂.MTr s₂ μs s₂' ∧ r s₁' s₂'
```

> ## Relation to trace equivalence

`Cslib.LTS.IsBisimulation.traceEq` (theorem, [line 383](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L383))

> Any bisimulation implies trace equivalence.

```lean
theorem IsBisimulation.traceEq (hb : IsBisimulation lts₁ lts₂ r) (hr : r s₁ s₂) :
    s₁ ~tr[lts₁,lts₂] s₂
```

`Cslib.LTS.Bisimilarity.le_traceEq` (theorem, [line 388](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L388))

> Bisimilarity is included in trace equivalence.

```lean
theorem Bisimilarity.le_traceEq : Bisimilarity lts₁ lts₂ ≤ TraceEq lts₁ lts₂
```

`Cslib.LTS.IsBisimulation.traceEq_not_bisim` (theorem, [line 408](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L408))

> In general, trace equivalence is not a bisimulation (extra conditions are needed, see for
> example `Bisimulation.deterministic_trace_eq_is_bisim`).

```lean
theorem IsBisimulation.traceEq_not_bisim :
    ∃ (State : Type) (Label : Type) (lts : LTS State Label),
      ¬(IsHomBisimulation lts (HomTraceEq lts))
```

`Cslib.LTS.Bisimilarity.bisimilarity_neq_traceEq` (theorem, [line 458](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L458))

> In general, bisimilarity and trace equivalence are distinct.

```lean
theorem Bisimilarity.bisimilarity_neq_traceEq :
    ∃ (State : Type) (Label : Type) (lts : LTS State Label),
      HomBisimilarity lts ≠ HomTraceEq lts
```

`Cslib.LTS.IsBisimulation.deterministic_traceEq_isBisimulation` (theorem, [line 465](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L465))

> In any deterministic LTS, trace equivalence is a bisimulation.

```lean
theorem IsBisimulation.deterministic_traceEq_isBisimulation
    {lts₁ : LTS State₁ Label} {lts₂ : LTS State₂ Label}
    [lts₁.Deterministic] [lts₂.Deterministic] :
    (IsBisimulation lts₁ lts₂ (TraceEq lts₁ lts₂))
```

`Cslib.LTS.Bisimilarity.deterministic_traceEq_bisim` (theorem, [line 473](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L473))

> In deterministic LTSs, trace equivalence implies bisimilarity.

```lean
theorem Bisimilarity.deterministic_traceEq_bisim {lts₁ : LTS State₁ Label} {lts₂ : LTS State₂ Label}
    [lts₁.Deterministic] [lts₂.Deterministic] (h : s₁ ~tr[lts₁,lts₂] s₂) :
    (s₁ ~[lts₁,lts₂] s₂)
```

`Cslib.LTS.Deterministic.bisim_tfae` (theorem, [line 480](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L480))

> In a deterministic lts, bisimilarity, trace equivalence, and simulation equivalence are
> equivalent to one-another.

```lean
theorem Deterministic.bisim_tfae {lts₁ : LTS State₁ Label} {lts₂ : LTS State₂ Label}
    [lts₁.Deterministic] [lts₂.Deterministic] (s₁ : State₁) (s₂ : State₂) :
    [s₁ ~[lts₁,lts₂] s₂, s₁ ~tr[lts₁,lts₂] s₂, s₁ ≤≥[lts₁,lts₂] s₂].TFAE
```

`Cslib.LTS.Bisimilarity.deterministic_bisim_eq_traceEq` (theorem, [line 489](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L489))

> In deterministic LTSs, bisimilarity and trace equivalence coincide.

```lean
theorem Bisimilarity.deterministic_bisim_eq_traceEq
    {lts₁ : LTS State₁ Label} {lts₂ : LTS State₂ Label}
    [lts₁.Deterministic] [lts₂.Deterministic] : Bisimilarity lts₁ lts₂ = TraceEq lts₁ lts₂
```

`Cslib.LTS.HomBisimilarity.symm_simulation` (theorem, [line 496](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L496))

> Homogeneous bisimilarity can also be characterized through symmetric simulations.

```lean
theorem HomBisimilarity.symm_simulation :
  HomBisimilarity lts =
    fun s₁ s₂ => ∃ r, r s₁ s₂ ∧ Std.Symm r ∧ IsHomSimulation lts r
```

> ## Weak bisimulation and weak bisimilarity

`Cslib.LTS.IsWeakBisimulation` (definition, [line 517](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L517))

> A weak bisimulation is similar to a `Bisimulation`, but allows for the related processes to do
> internal work. Technically, this is defined as a `Bisimulation` on the saturation of the LTSs.

```lean
def IsWeakBisimulation [HasTau Label] (lts₁ : LTS State₁ Label) (lts₂ : LTS State₂ Label)
    (r : State₁ → State₂ → Prop)
```

`Cslib.LTS.IsHomWeakBisimulation` (abbreviation, [line 522](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L522))

> A homogeneous bisimulation is a bisimulation where the underlying LTSs are the same.

```lean
abbrev IsHomWeakBisimulation [HasTau Label] (lts : LTS State Label)
```

`Cslib.LTS.WeakBisimilarity` (definition, [line 525](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L525))

> Two states are weakly bisimilar if they are related by some weak bisimulation.

```lean
def WeakBisimilarity [HasTau Label] (lts₁ : LTS State₁ Label) (lts₂ : LTS State₂ Label) :
    State₁ → State₂ → Prop
```

`Cslib.LTS.HomWeakBisimilarity` (abbreviation, [line 534](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L534))

> Homogeneous bisimilarity is bisimilarity where the underlying LTSs are the same.

```lean
abbrev HomWeakBisimilarity [HasTau Label] (lts : LTS State Label)
```

`Cslib.LTS.IsSWBisimulation` (definition, [line 542](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L542))

> An `SWBisimulation` is a more convenient definition of weak bisimulation, because the challenge
> is a single transition. We prove later that this technique is sound, following a strategy inspired
> by [Sangiorgi2011].

```lean
def IsSWBisimulation [HasTau Label] (lts₁ : LTS State₁ Label) (lts₂ : LTS State₂ Label)
    (r : State₁ → State₂ → Prop) : Prop
```

`Cslib.LTS.IsSWBisimulation.isSimulation` (lemma, [line 550](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L550))

```lean
lemma IsSWBisimulation.isSimulation [HasTau Label] (h : IsSWBisimulation lts₁ lts₂ r) :
    IsSimulation lts₁ lts₂.saturate r
```

`Cslib.LTS.IsSWBisimulation.isSimulation_flip` (lemma, [line 555](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L555))

```lean
lemma IsSWBisimulation.isSimulation_flip [HasTau Label] (h : IsSWBisimulation lts₁ lts₂ r) :
    IsSimulation lts₂ lts₁.saturate (flip r)
```

`Cslib.LTS.IsSWBisimulation.iff_isSimulation` (theorem, [line 560](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L560))

```lean
theorem IsSWBisimulation.iff_isSimulation [HasTau Label] :
    IsSWBisimulation lts₁ lts₂ r ↔
      IsSimulation lts₁ lts₂.saturate r ∧ IsSimulation lts₂ lts₁.saturate (flip r)
```

`Cslib.LTS.isWeakBisimulation_iff_isSWBisimulation` (theorem, [line 569](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L569))

> We can now prove that any relation is a `WeakBisimulation` iff it is an `SWBisimulation`.
> This formalises lemma 4.2.10 in [Sangiorgi2011].

```lean
theorem isWeakBisimulation_iff_isSWBisimulation
    [HasTau Label] {lts₁ : LTS State₁ Label} {lts₂ : LTS State₂ Label} :
    IsWeakBisimulation lts₁ lts₂ r ↔ IsSWBisimulation lts₁ lts₂ r
```

`Cslib.LTS.IsWeakBisimulation.isSwBisimulation` (theorem, [line 584](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L584))

```lean
theorem IsWeakBisimulation.isSwBisimulation
    [HasTau Label] {lts₁ : LTS State₁ Label} {lts₂ : LTS State₂ Label} {r : State₁ → State₂ → Prop}
    (h : IsWeakBisimulation lts₁ lts₂ r) :
  IsSWBisimulation lts₁ lts₂ r
```

`Cslib.LTS.IsSWBisimulation.isWeakBisimulation` (theorem, [line 589](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L589))

```lean
theorem IsSWBisimulation.isWeakBisimulation
    [HasTau Label] {lts₁ : LTS State₁ Label} {lts₂ : LTS State₂ Label} {r : State₁ → State₂ → Prop}
    (h : IsSWBisimulation lts₁ lts₂ r) :
  IsWeakBisimulation lts₁ lts₂ r
```

`Cslib.LTS.WeakBisimilarity.weakBisim_eq_swBisim` (theorem, [line 596](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L596))

> Weak bisimilarity can also be characterized through sw-bisimulations.

```lean
theorem WeakBisimilarity.weakBisim_eq_swBisim [HasTau Label]
    (lts₁ : LTS State₁ Label) (lts₂ : LTS State₂ Label) :
    WeakBisimilarity lts₁ lts₂ =
      fun s₁ s₂ => ∃ r : State₁ → State₂ → Prop, r s₁ s₂ ∧ IsSWBisimulation lts₁ lts₂ r
```

`Cslib.LTS.HomWeakBisimilarity.refl` (theorem, [line 606](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L606))

> Homogeneous weak bisimilarity is reflexive.

```lean
theorem HomWeakBisimilarity.refl [HasTau Label] {lts : LTS State Label} (s : State) :
    s ≈[lts] s
```

`Cslib.LTS.IsWeakBisimulation.inv` (theorem, [line 610](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L610))

> The inverse of a weak bisimulation is a weak bisimulation.

```lean
theorem IsWeakBisimulation.inv [HasTau Label]
    {lts₁ : LTS State₁ Label} {lts₂ : LTS State₂ Label}
    (r : State₁ → State₂ → Prop) (h : IsWeakBisimulation lts₁ lts₂ r) :
    IsWeakBisimulation lts₂ lts₁ (flip r)
```

`Cslib.LTS.WeakBisimilarity.symm` (theorem, [line 616](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L616))

> Weak bisimilarity is symmetric.

```lean
theorem WeakBisimilarity.symm [HasTau Label] {lts₁ : LTS State₁ Label} {lts₂ : LTS State₂ Label}
    (h : s₁ ≈[lts₁,lts₂] s₂) : s₂ ≈[lts₂,lts₁] s₁
```

`Cslib.LTS.IsWeakBisimulation.comp` (theorem, [line 620](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L620))

> The composition of two weak bisimulations is a weak bisimulation.

```lean
theorem IsWeakBisimulation.comp
    [HasTau Label] {lts₁ : LTS State₁ Label} {lts₂ : LTS State₂ Label} {lts₃ : LTS State₃ Label}
    (h1 : IsWeakBisimulation lts₁ lts₂ r1) (h2 : IsWeakBisimulation lts₂ lts₃ r2) :
    IsWeakBisimulation lts₁ lts₃ (Relation.Comp r1 r2)
```

`Cslib.LTS.IsSWBisimulation.comp` (theorem, [line 626](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L626))

> The composition of two sw-bisimulations is an sw-bisimulation.

```lean
theorem IsSWBisimulation.comp
    [HasTau Label] {lts₁ : LTS State₁ Label} {lts₂ : LTS State₂ Label} {lts₃ : LTS State₃ Label}
    (h1 : IsSWBisimulation lts₁ lts₂ r1) (h2 : IsSWBisimulation lts₂ lts₃ r2) :
    IsSWBisimulation lts₁ lts₃ (Relation.Comp r1 r2)
```

`Cslib.LTS.WeakBisimilarity.trans` (theorem, [line 634](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L634))

> Weak bisimilarity is transitive.

```lean
theorem WeakBisimilarity.trans [HasTau Label]
    {lts₁ : LTS State₁ Label} {lts₂ : LTS State₂ Label} {lts₃ : LTS State₃ Label}
    (h1 : s₁ ≈[lts₁,lts₂] s₂) (h2 : s₂ ≈[lts₂,lts₃] s₃) : s₁ ≈[lts₁,lts₃] s₃
```

`Cslib.LTS.HomWeakBisimilarity.eqv` (theorem, [line 640](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L640))

> Homogeneous weak bisimilarity is an equivalence relation.

```lean
theorem HomWeakBisimilarity.eqv [HasTau Label] {lts : LTS State Label} :
    Equivalence (HomWeakBisimilarity lts)
```

> ## Reindex an LTS by an equivalence between two state types

`Cslib.LTS.reindex` (definition, [line 653](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L653))

> Reindex an LTS by an equivalence between two state types.

```lean
def reindex (lts₁ : LTS State₁ Label) (e : State₁ ≃ State₂) : LTS State₂ Label
```

`Cslib.LTS.reindex.tr` (theorem, [line 656](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L656))

```lean
theorem reindex.tr (lts₁ : LTS State₁ Label) (e : State₁ ≃ State₂) (s₁ t₁ : State₁) (μ : Label) :
    (lts₁.reindex e).Tr (e s₁) μ (e t₁) ↔ lts₁.Tr s₁ μ t₁
```

`Cslib.LTS.reindex.isBisimulation` (theorem, [line 660](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L660))

```lean
theorem reindex.isBisimulation (lts₁ : LTS State₁ Label) (e : State₁ ≃ State₂) :
    IsBisimulation lts₁ (lts₁.reindex e) (fun s s' ↦ s' = e s)
```

`Cslib.LTS.reindex.bisim_trace` (theorem, [line 671](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L671))

```lean
theorem reindex.bisim_trace (lts₁ : LTS State₁ Label) (e : State₁ ≃ State₂)
    (s₁ t₁ : State₁) (μs : List Label) :
    lts₁.MTr s₁ μs t₁ → (lts₁.reindex e).MTr (e s₁) μs (e t₁)
```

`Cslib.LTS.reindex.bisim_trace_iff` (theorem, [line 678](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean#L678))

```lean
theorem reindex.bisim_trace_iff (lts₁ : LTS State₁ Label) (e : State₁ ≃ State₂)
    (s₁ t₁ : State₁) (μs : List Label) :
    lts₁.MTr s₁ μs t₁ ↔ (lts₁.reindex e).MTr (e s₁) μs (e t₁)
```

## Depends on

- [Trace Equivalence](traceeq.md)

## Proof depends on

- [Relations: Domain and Codomain](../../relation/domain.md)

## Sources

- [Cslib/Foundations/Semantics/LTS/Bisimulation.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Bisimulation.lean)
