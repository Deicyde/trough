---
catalog: module
lean: Language.toSet, Cslib.ωLanguage, Cslib.ωLanguage.ofSet_toSet, Cslib.ωLanguage.toSet_ofSet, Cslib.ωLanguage.equiv, Cslib.ωLanguage.eq_bot_ofIsEmpty, Cslib.ωLanguage.le_def, Cslib.ωLanguage.top_def, Cslib.ωLanguage.bot_def, Cslib.ωLanguage.sup_def, Cslib.ωLanguage.inf_def, Cslib.ωLanguage.compl_def, Cslib.ωLanguage.sSup_def, Cslib.ωLanguage.sInf_def, Cslib.ωLanguage.iSup_def, Cslib.ωLanguage.iInf_def, Cslib.ωLanguage.closure, Cslib.ωLanguage.hmul_def, Cslib.ωLanguage.omegaPow, Cslib.ωLanguage.OmegaPow, Cslib.ωLanguage.omegaPow_def, Cslib.ωLanguage.omegaLim, Cslib.ωLanguage.OmegaLim, Cslib.ωLanguage.instOmegaLim, Cslib.ωLanguage.omegaLim_def, Cslib.ωLanguage.map, Cslib.ωLanguage.map_def, Cslib.ωLanguage.mem_def, Cslib.ωLanguage.mem_ext, Cslib.ωLanguage.mem_top, Cslib.ωLanguage.notMem_bot, Cslib.ωLanguage.mem_sup, Cslib.ωLanguage.mem_inf, Cslib.ωLanguage.mem_compl, Cslib.ωLanguage.mem_sSup, Cslib.ωLanguage.mem_sInf, Cslib.ωLanguage.mem_iSup, Cslib.ωLanguage.mem_iInf, Cslib.ωLanguage.mem_hmul, Cslib.ωLanguage.append_mem_hmul, Cslib.ωLanguage.mem_omegaPow, Cslib.ωLanguage.flatten_mem_omegaPow, Cslib.ωLanguage.mem_omegaLim, Cslib.ωLanguage.mul_hmul, Cslib.ωLanguage.zero_hmul, Cslib.ωLanguage.hmul_bot, Cslib.ωLanguage.one_hmul, Cslib.ωLanguage.hmul_sup, Cslib.ωLanguage.add_hmul, Cslib.ωLanguage.iSup_hmul, Cslib.ωLanguage.hmul_iSup, Cslib.ωLanguage.le_hmul_congr, Cslib.ωLanguage.le_omegaPow_congr, Cslib.ωLanguage.omegaPow_of_sub_one, Cslib.ωLanguage.zero_omegaPow, Cslib.ωLanguage.one_omegaPow, Cslib.ωLanguage.omegaPow_of_le_one, Cslib.ωLanguage.omegaPow_eq_empty, Cslib.ωLanguage.hmul_seq_prop, Cslib.ωLanguage.omegaPow_seq_prop, Cslib.ωLanguage.omegaPow_coind', Cslib.ωLanguage.omegaPow_coind, Cslib.ωLanguage.omegaPow_le_hmul_omegaPow', Cslib.ωLanguage.omegaPow_le_hmul_omegaPow, Cslib.ωLanguage.hmul_omegaPow_le_omegaPow, Cslib.ωLanguage.hmul_omegaPow_eq_omegaPow, Cslib.ωLanguage.omegaPow_le_kstar_omegaPow, Cslib.ωLanguage.kstar_omegaPow_le_omegaPow, Cslib.ωLanguage.kstar_omegaPow_eq_omegaPow, Cslib.ωLanguage.kstar_hmul_omegaPow_eq_omegaPow, Cslib.ωLanguage.omegaLim_zero, Cslib.ωLanguage.map_id, Cslib.ωLanguage.map_map
statement: formalized
proof: formalized
---

# ωLanguage

`Cslib.Computability.Languages.OmegaLanguage`, in [Cslib/Computability/Languages/OmegaLanguage.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean), by Ching-Tsun Chou.

> This file contains the definition and operations on formal ω-languages, which
> are sets of infinite sequences over an alphabet `α` (namely, objects of type
> `ωSequence α`).
>
> ## Main definitions and notations
>
> In general we will use `p` and `q` to denote ω-languages and `l` and `m` to
> denote languages (namely, sets of finite sequences of type `List α`).
>
> * Set operations (union, intersection, complementation), constants (empty and
>   universe sets), and the subset relation are denoted using lattice-theoretic
>   notations (`p ∪ q`, `p ∩ q`, `pᶜ`, `⊥`, `⊤`, and `≤`) and terminologies in
>   definition and theorem names ("inf", "sup", "compl", "bot", "top", "le").
> * `p.closure`: the topological closure of `p`, where `ωLanguage α` inherits the
>   product topology of `TopologicalSpace (ωSequence α)`
> * `l * p`: ω-language of `x ++ω y` where `x ∈ l` and `y ∈ p`; referred to as
>   "hmul" in definition and theorem names.
> * `l^ω`: ω-language of infinite sequences each of which is the concatenation of
>   infinitely many (nonemoty) members of `l`; referred to as "omegaPow" in
>   definition and theorem names.
>   + Note: Since `l^ω` is defined using `ωSequence.flatten`, any theorem about it
>     needs the additional assumption `[Inhabited α]`.
> * `l↗ω`: ω-language of infinite sequences each of which has infinitely many
>   distinct prefixes in `l`; referred to as "omegaLim" in definition and theorem names.
> * `p.map f`: transform an ω-language `p` over `α` into an ω-language over `β`
>   by mapping through `f : α → β`; referred to as "map" in definition and theorem names.
>
> ## Main theorems
>
> * Many algebraic properties of the above operations.
> * `omegaPow_seq_prop`: an alternative characterization of `l^ω`.
> * `omegaPow_coind`: a "coinductive" rule for proving `p` is a subset of `l^ω`.
> * `hmul_omegaPow_eq_omegaPow`: `l * l^ω = l^ω`.
> * `kstar_omegaPow_eq_omegaPow`: `(l∗)^ω = l^ω`.
> * `kstar_hmul_omegaPow_eq_omegaPow`: `l∗ * l^ω = l^ω`.
>
> …

`Language.toSet` (definition, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L68))

> The set of lists in a language.

```lean
def Language.toSet (l : Language α) : Set (List α)
```

`Cslib.ωLanguage` (structure, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L79))

> An ω-language is a set of ω-sequences over an alphabet.

```lean
structure ωLanguage (α : Type u) where
  /-- Construct an ω-language from a set of ω-sequences. -/
  ofSet ::
  /-- The set of ω-sequences in an ω-language. -/
  toSet : Set (ωSequence α)
deriving Inhabited
```

`Cslib.ωLanguage.ofSet_toSet` (lemma, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L92))

```lean
lemma ofSet_toSet (l : ωLanguage α) : ofSet l.toSet = l
```

`Cslib.ωLanguage.toSet_ofSet` (lemma, [line 94](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L94))

```lean
lemma toSet_ofSet (s : Set (ωSequence α)) : (ofSet s).toSet = s
```

`Cslib.ωLanguage.equiv` (definition, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L97))

> The equivalence between `ωLanguage α` and `Set (ωSequence α)`.

```lean
def equiv : ωLanguage α ≃ Set (ωSequence α)
```

`Cslib.ωLanguage.eq_bot_ofIsEmpty` (theorem, [line 105](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L105))

> `⊥` is the only possible ω-language over an empty type.

```lean
theorem eq_bot_ofIsEmpty [IsEmpty α] (p : ωLanguage α) : p = ⊥
```

`Cslib.ωLanguage.le_def` (lemma, [line 119](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L119))

```lean
lemma le_def (p q : ωLanguage α) : p ≤ q ↔ p.toSet ⊆ q.toSet
```

`Cslib.ωLanguage.top_def` (lemma, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L121))

```lean
lemma top_def : (⊤ : ωLanguage α) = ⟨univ⟩
```

`Cslib.ωLanguage.bot_def` (lemma, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L123))

```lean
lemma bot_def : (⊥ : ωLanguage α) = ⟨∅⟩
```

`Cslib.ωLanguage.sup_def` (lemma, [line 125](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L125))

```lean
lemma sup_def (p q : ωLanguage α) : p ⊔ q = ⟨p.toSet ∪ q.toSet⟩
```

`Cslib.ωLanguage.inf_def` (lemma, [line 127](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L127))

```lean
lemma inf_def (p q : ωLanguage α) : p ⊓ q = ⟨p.toSet ∩ q.toSet⟩
```

`Cslib.ωLanguage.compl_def` (lemma, [line 129](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L129))

```lean
lemma compl_def (p : ωLanguage α) : pᶜ = ⟨p.toSetᶜ⟩
```

`Cslib.ωLanguage.sSup_def` (lemma, [line 131](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L131))

```lean
lemma sSup_def (s : Set (ωLanguage α)) : sSup s = ⟨⋃ p ∈ s, p.toSet⟩
```

`Cslib.ωLanguage.sInf_def` (lemma, [line 133](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L133))

```lean
lemma sInf_def (s : Set (ωLanguage α)) : sInf s = ⟨⋂ p ∈ s, p.toSet⟩
```

`Cslib.ωLanguage.iSup_def` (lemma, [line 135](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L135))

```lean
lemma iSup_def {ι : Sort v} {p : ι → ωLanguage α} : ⨆ i, p i = ⟨⋃ i, (p i).toSet⟩
```

`Cslib.ωLanguage.iInf_def` (lemma, [line 139](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L139))

```lean
lemma iInf_def {ι : Sort v} {p : ι → ωLanguage α} : ⨅ i, p i = ⟨⋂ i, (p i).toSet⟩
```

`Cslib.ωLanguage.closure` (definition, [line 144](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L144))

> The topological closure of an ω-language.

```lean
def closure (p : ωLanguage α) : ωLanguage α
```

`Cslib.ωLanguage.hmul_def` (theorem, [line 152](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L152))

```lean
theorem hmul_def (l : Language α) (p : ωLanguage α) : l * p = image2 (· ++ω ·) l.toSet p.toSet
```

`Cslib.ωLanguage.omegaPow` (definition, [line 158](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L158))

> Concatenation of infinitely many copies of a languages, resulting in an ω-language.
> A.k.a. ω-power.

```lean
def omegaPow [Inhabited α] (l : Language α) : ωLanguage α
```

`Cslib.ωLanguage.OmegaPow` (class, [line 163](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L163))

> Notation class for `omegaPow`.

```lean
class OmegaPow (α : Type*) (β : outParam (Type*)) where
  /-- The `omegaPow` operation. -/
  omegaPow : α → β
```

`Cslib.ωLanguage.omegaPow_def` (theorem, [line 173](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L173))

```lean
theorem omegaPow_def [Inhabited α] (l : Language α) :
    l^ω = { s | ∃ xs : ωSequence (List α), xs.flatten = s ∧ ∀ k, xs k ∈ l - 1 }
```

`Cslib.ωLanguage.omegaLim` (definition, [line 179](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L179))

> The ω-limit of a language `l` is the ω-language of infinite sequences each of which
> contains infinitely many distinct prefixes in `l`.

```lean
def omegaLim (l : Language α) : ωLanguage α
```

`Cslib.ωLanguage.OmegaLim` (class, [line 184](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L184))

> Notation class for `omegaLim`.

```lean
class OmegaLim (α : Type*) (β : outParam (Type*)) where
  /-- The `omegaLim` operation. -/
  omegaLim : α → β
```

`Cslib.ωLanguage.instOmegaLim` (instance, [line 191](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L191))

```lean
instance instOmegaLim : OmegaLim (Language α) (ωLanguage α)
```

`Cslib.ωLanguage.omegaLim_def` (theorem, [line 194](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L194))

```lean
theorem omegaLim_def (l : Language α) :
    l↗ω = { s : ωSequence α | ∃ᶠ m in atTop, s.extract 0 m ∈ l }
```

`Cslib.ωLanguage.map` (definition, [line 200](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L200))

> transform an ω-language `p` over `α` into an ω-language over `β`
> by mapping through `f : α → β`.

```lean
def map (f : α → β) : ωLanguage α → ωLanguage β
```

`Cslib.ωLanguage.map_def` (theorem, [line 203](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L203))

```lean
theorem map_def (f : α → β) (p : ωLanguage α) :
    p.map f = image (ωSequence.map f) p.toSet
```

`Cslib.ωLanguage.mem_def` (theorem, [line 208](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L208))

```lean
theorem mem_def (p : ωLanguage α) (s : ωSequence α) : s ∈ p ↔ s ∈ p.toSet
```

`Cslib.ωLanguage.mem_ext` (theorem, [line 211](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L211))

```lean
theorem mem_ext (h : ∀ (s : ωSequence α), s ∈ p ↔ s ∈ q) : p = q
```

`Cslib.ωLanguage.mem_top` (theorem, [line 216](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L216))

```lean
theorem mem_top (s : ωSequence α) : s ∈ (⊤ : ωLanguage α)
```

`Cslib.ωLanguage.notMem_bot` (theorem, [line 220](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L220))

```lean
theorem notMem_bot (s : ωSequence α) : s ∉ (⊥ : ωLanguage α)
```

`Cslib.ωLanguage.mem_sup` (theorem, [line 224](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L224))

```lean
theorem mem_sup (p q : ωLanguage α) (s : ωSequence α) : s ∈ p ⊔ q ↔ s ∈ p ∨ s ∈ q
```

`Cslib.ωLanguage.mem_inf` (theorem, [line 228](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L228))

```lean
theorem mem_inf (p q : ωLanguage α) (s : ωSequence α) : s ∈ p ⊓ q ↔ s ∈ p ∧ s ∈ q
```

`Cslib.ωLanguage.mem_compl` (theorem, [line 232](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L232))

```lean
theorem mem_compl (p : ωLanguage α) (s : ωSequence α) : s ∈ pᶜ ↔ ¬ s ∈ p
```

`Cslib.ωLanguage.mem_sSup` (theorem, [line 236](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L236))

```lean
theorem mem_sSup (ps : Set (ωLanguage α)) {s : ωSequence α} :
    s ∈ sSup ps ↔ ∃ p ∈ ps, s ∈ p
```

`Cslib.ωLanguage.mem_sInf` (theorem, [line 241](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L241))

```lean
theorem mem_sInf (ps : Set (ωLanguage α)) {s : ωSequence α} :
    s ∈ sInf ps ↔ ∀ p ∈ ps, s ∈ p
```

`Cslib.ωLanguage.mem_iSup` (theorem, [line 246](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L246))

```lean
theorem mem_iSup {ι : Sort v} {p : ι → ωLanguage α} {s : ωSequence α} :
    (s ∈ ⨆ i, p i) ↔ ∃ i, s ∈ p i
```

`Cslib.ωLanguage.mem_iInf` (theorem, [line 252](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L252))

```lean
theorem mem_iInf {ι : Sort v} {p : ι → ωLanguage α} {s : ωSequence α} :
    (s ∈ ⨅ i, p i) ↔ ∀ i, s ∈ p i
```

`Cslib.ωLanguage.mem_hmul` (theorem, [line 258](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L258))

```lean
theorem mem_hmul : s ∈ l * p ↔ ∃ x ∈ l, ∃ t ∈ p, x ++ω t = s
```

`Cslib.ωLanguage.append_mem_hmul` (theorem, [line 261](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L261))

```lean
theorem append_mem_hmul : x ∈ l → s ∈ p → x ++ω s ∈ l * p
```

`Cslib.ωLanguage.mem_omegaPow` (theorem, [line 265](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L265))

```lean
theorem mem_omegaPow [Inhabited α] :
    s ∈ l^ω ↔ ∃ xs : ωSequence (List α), xs.flatten = s ∧ ∀ k, xs k ∈ l - 1
```

`Cslib.ωLanguage.flatten_mem_omegaPow` (theorem, [line 269](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L269))

```lean
theorem flatten_mem_omegaPow [Inhabited α] {xs : ωSequence (List α)}
    (h_xs : ∀ k, xs k ∈ l - 1) : xs.flatten ∈ l^ω
```

`Cslib.ωLanguage.mem_omegaLim` (theorem, [line 274](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L274))

```lean
theorem mem_omegaLim :
    s ∈ l↗ω ↔ ∃ᶠ m in atTop, s.extract 0 m ∈ l
```

`Cslib.ωLanguage.mul_hmul` (theorem, [line 278](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L278))

```lean
theorem mul_hmul : (l * m) * p = l * (m * p)
```

`Cslib.ωLanguage.zero_hmul` (theorem, [line 283](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L283))

```lean
theorem zero_hmul : (0 : Language α) * p = ⊥
```

`Cslib.ωLanguage.hmul_bot` (theorem, [line 288](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L288))

```lean
theorem hmul_bot : l * (⊥ : ωLanguage α) = ⊥
```

`Cslib.ωLanguage.one_hmul` (theorem, [line 293](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L293))

```lean
theorem one_hmul : (1 : Language α) * p = p
```

`Cslib.ωLanguage.hmul_sup` (theorem, [line 297](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L297))

```lean
theorem hmul_sup : l * (p ⊔ q) = l * p ⊔ l * q
```

`Cslib.ωLanguage.add_hmul` (theorem, [line 301](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L301))

```lean
theorem add_hmul : (l + m) * p = l * p ⊔ m * p
```

`Cslib.ωLanguage.iSup_hmul` (theorem, [line 305](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L305))

```lean
theorem iSup_hmul {ι : Sort v} (l : ι → Language α) (p : ωLanguage α) :
    (⨆ i, l i) * p = ⨆ i, l i * p
```

`Cslib.ωLanguage.hmul_iSup` (theorem, [line 311](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L311))

```lean
theorem hmul_iSup {ι : Sort v} (p : ι → ωLanguage α) (l : Language α) :
    (l * ⨆ i, p i) = ⨆ i, l * p i
```

`Cslib.ωLanguage.le_hmul_congr` (theorem, [line 317](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L317))

```lean
theorem le_hmul_congr {l1 l2 : Language α} {p1 p2 : ωLanguage α} (hl : l1 ≤ l2) (hp : p1 ≤ p2) :
    l1 * p1 ≤ l2 * p2
```

`Cslib.ωLanguage.le_omegaPow_congr` (theorem, [line 324](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L324))

```lean
theorem le_omegaPow_congr [Inhabited α] {l1 l2 : Language α} (h : l1 ≤ l2) : l1^ω ≤ l2^ω
```

`Cslib.ωLanguage.omegaPow_of_sub_one` (theorem, [line 332](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L332))

```lean
theorem omegaPow_of_sub_one [Inhabited α] : (l - 1)^ω = l^ω
```

`Cslib.ωLanguage.zero_omegaPow` (theorem, [line 337](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L337))

```lean
theorem zero_omegaPow [Inhabited α] : (0 : Language α)^ω = ⊥
```

`Cslib.ωLanguage.one_omegaPow` (theorem, [line 342](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L342))

```lean
theorem one_omegaPow [Inhabited α] : (1 : Language α)^ω = ⊥
```

`Cslib.ωLanguage.omegaPow_of_le_one` (theorem, [line 346](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L346))

```lean
theorem omegaPow_of_le_one [Inhabited α] (h : l ≤ 1) : l^ω = ⊥
```

`Cslib.ωLanguage.omegaPow_eq_empty` (theorem, [line 351](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L351))

> A grind regression found moving to nightly-2026-03-31 (from lean#13166? seems different)

```lean
theorem omegaPow_eq_empty [Inhabited α] (h : l^ω = ⊥) : l ≤ 1
```

`Cslib.ωLanguage.hmul_seq_prop` (theorem, [line 360](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L360))

> An alternative characterization of `l * p`.

```lean
theorem hmul_seq_prop : l * p = { s : ωSequence α | ∃ k, s.take k ∈ l ∧ s.drop k ∈ p }
```

`Cslib.ωLanguage.omegaPow_seq_prop` (theorem, [line 370](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L370))

> An alternative characterization of `l^ω`.

```lean
theorem omegaPow_seq_prop [Inhabited α] :
    l^ω = { s : ωSequence α |
      ∃ f : ℕ → ℕ, StrictMono f ∧ f 0 = 0 ∧ ∀ m, s.extract (f m) (f (m + 1)) ∈ l }
```

`Cslib.ωLanguage.omegaPow_coind'` (theorem, [line 393](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L393))

```lean
theorem omegaPow_coind' [Inhabited α] (h_nn : [] ∉ l) (h_le : p ≤ l * p) : p ≤ l^ω
```

`Cslib.ωLanguage.omegaPow_coind` (theorem, [line 410](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L410))

> A "coinductive" rule for proving `p` is a subset of `l^ω`.

```lean
theorem omegaPow_coind [Inhabited α] (h_le : p ≤ (l - 1) * p) : p ≤ l^ω
```

`Cslib.ωLanguage.omegaPow_le_hmul_omegaPow'` (theorem, [line 417](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L417))

> A grind regression found moving to nightly-2026-03-31 (changes from lean#13166)

```lean
theorem omegaPow_le_hmul_omegaPow' [Inhabited α] (l : Language α) :
    l^ω ≤ (l - 1) * l^ω
```

`Cslib.ωLanguage.omegaPow_le_hmul_omegaPow` (theorem, [line 427](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L427))

```lean
theorem omegaPow_le_hmul_omegaPow [Inhabited α] (l : Language α) : l^ω ≤ l * l^ω
```

`Cslib.ωLanguage.hmul_omegaPow_le_omegaPow` (theorem, [line 434](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L434))

```lean
theorem hmul_omegaPow_le_omegaPow [Inhabited α] (l : Language α) : l * l^ω ≤ l^ω
```

`Cslib.ωLanguage.hmul_omegaPow_eq_omegaPow` (theorem, [line 442](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L442))

```lean
theorem hmul_omegaPow_eq_omegaPow [Inhabited α] (l : Language α) : l * l^ω = l^ω
```

`Cslib.ωLanguage.omegaPow_le_kstar_omegaPow` (theorem, [line 447](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L447))

```lean
theorem omegaPow_le_kstar_omegaPow [Inhabited α] (l : Language α) : l^ω ≤ (l∗)^ω
```

`Cslib.ωLanguage.kstar_omegaPow_le_omegaPow` (theorem, [line 450](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L450))

```lean
theorem kstar_omegaPow_le_omegaPow [Inhabited α] (l : Language α) : (l∗)^ω ≤ l^ω
```

`Cslib.ωLanguage.kstar_omegaPow_eq_omegaPow` (theorem, [line 459](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L459))

```lean
theorem kstar_omegaPow_eq_omegaPow [Inhabited α] (l : Language α) : (l∗)^ω = l^ω
```

`Cslib.ωLanguage.kstar_hmul_omegaPow_eq_omegaPow` (theorem, [line 465](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L465))

```lean
theorem kstar_hmul_omegaPow_eq_omegaPow [Inhabited α] (l : Language α) : l∗ * l^ω = l^ω
```

`Cslib.ωLanguage.omegaLim_zero` (theorem, [line 472](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L472))

```lean
theorem omegaLim_zero : (0 : Language α)↗ω = ⊥
```

`Cslib.ωLanguage.map_id` (theorem, [line 477](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L477))

```lean
theorem map_id (p : ωLanguage α) : map id p = p
```

`Cslib.ωLanguage.map_map` (theorem, [line 483](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean#L483))

```lean
theorem map_map (g : β → γ) (f : α → β) (p : ωLanguage α) : map g (map f p) = map (g ∘ f) p
```

## Depends on

- [Flattening an infinite sequence of lists](../../foundations/data/omegasequence/flatten.md)
- [Topology on ω-sequences](../../foundations/data/omegasequence/topology.md)

## Proof depends on

- [Language (additional definitions and theorems)](language.md)

## Sources

- [Cslib/Computability/Languages/OmegaLanguage.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaLanguage.lean)
