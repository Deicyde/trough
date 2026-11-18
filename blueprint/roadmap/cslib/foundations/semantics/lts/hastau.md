---
catalog: module
lean: Cslib.HasTau, Cslib.DecidableEqTau, Cslib.LTS.τSTr, Cslib.LTS.τSTr.refl, Cslib.LTS.STr, Cslib.LTS.saturate, Cslib.LTS.saturate_tr_sTr, Cslib.LTS.STr.single, Cslib.LTS.tr_le_tr_saturate, Cslib.LTS.sTr_τSTr_iff, Cslib.LTS.saturate_τsTr_τSTr_iff, Cslib.LTS.STr.trans_τ, Cslib.LTS.STr.comp, Cslib.LTS.saturate_tr_saturate_sTr, Cslib.LTS.mem_saturate_image_τ, Cslib.LTS.subset_saturate_setImage_τ, Cslib.LTS.empty_saturate_setImage_τ, Cslib.LTS.τClosure, Cslib.LTS.τClosure_subset, Cslib.LTS.mem_τClosure_iff, Cslib.LTS.τClosure_empty, Cslib.LTS.τClosure_union, Cslib.LTS.τClosure_mono, Cslib.LTS.τClosure_τClosure, Cslib.LTS.saturate_setImage_of_ne_τ, Cslib.LTS.SMTr, Cslib.LTS.SMTr.refl, Cslib.LTS.SMTr.comp, Cslib.LTS.SMTr.fromMTr, Cslib.LTS.sMTr_τSTr_iff, Cslib.LTS.saturate_mTr_sMTr_not_nil_iff, Cslib.LTS.τSTr_iff_exists_mTr_replicate, Cslib.LTS.sMTr_iff_exists_mTr_filter
statement: formalized
proof: formalized
---

# LTS with a special "internal" transition `τ`

`Cslib.Foundations.Semantics.LTS.HasTau`, in [Cslib/Foundations/Semantics/LTS/HasTau.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean), by Fabrizio Montesi.

`Cslib.HasTau` (class, [line 23](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L23))

> A type of transition labels that includes a special 'internal' transition `τ`.

```lean
class HasTau (Label : Type v) where
  /-- The internal transition label, also known as τ. -/
  τ : Label
```

`Cslib.DecidableEqTau` (abbreviation, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L28))

> Checking whether an element is `τ` is decidable.

```lean
abbrev DecidableEqTau (α : Type*) [HasTau α]
```

`Cslib.LTS.τSTr` (definition, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L33))

> Saturated τ-transition relation.

```lean
def τSTr [HasTau Label] (lts : LTS State Label) : State → State → Prop
```

`Cslib.LTS.τSTr.refl` (theorem, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L37))

```lean
theorem τSTr.refl [HasTau Label] {lts : LTS State Label} : lts.τSTr s s
```

`Cslib.LTS.STr` (inductive type, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L42))

> Saturated transition relation.

```lean
inductive STr [HasTau Label] (lts : LTS State Label) : State → Label → State → Prop where
  | refl : lts.STr s HasTau.τ s
  | tr : lts.τSTr s1 s2 → lts.Tr s2 μ s3 → lts.τSTr s3 s4 → lts.STr s1 μ s4
```

`Cslib.LTS.saturate` (definition, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L48))

> The `LTS` obtained by saturating the transition relation in `lts`.

```lean
def saturate [HasTau Label] (lts : LTS State Label) : LTS State Label
```

`Cslib.LTS.saturate_tr_sTr` (theorem, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L52))

```lean
theorem saturate_tr_sTr [HasTau Label] {lts : LTS State Label} :
  lts.saturate.Tr = lts.STr
```

`Cslib.LTS.STr.single` (theorem, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L56))

> Any transition is also a saturated transition.

```lean
theorem STr.single [HasTau Label] {lts : LTS State Label} :
    lts.Tr s μ s' → lts.STr s μ s'
```

`Cslib.LTS.tr_le_tr_saturate` (lemma, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L61))

```lean
lemma tr_le_tr_saturate [HasTau Label] (lts : LTS State Label) : lts.Tr ≤ lts.saturate.Tr
```

`Cslib.LTS.sTr_τSTr_iff` (theorem, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L65))

> STr transitions labeled by HasTau.τ are exactly the τSTr transitions.

```lean
theorem sTr_τSTr_iff [HasTau Label] (lts : LTS State Label) :
    lts.STr s HasTau.τ s' ↔ lts.τSTr s s'
```

`Cslib.LTS.saturate_τsTr_τSTr_iff` (theorem, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L79))

> Saturating an LTS does not change its saturated τ-transition relation.

```lean
theorem saturate_τsTr_τSTr_iff [hHasTau : HasTau Label] (lts : LTS State Label) :
    lts.saturate.τSTr = lts.τSTr
```

`Cslib.LTS.STr.trans_τ` (theorem, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L87))

> Saturated transitions labelled by τ can be composed.

```lean
theorem STr.trans_τ
    [HasTau Label] {lts : LTS State Label}
    (h1 : lts.STr s1 HasTau.τ s2) (h2 : lts.STr s2 HasTau.τ s3) :
    lts.STr s1 HasTau.τ s3
```

`Cslib.LTS.STr.comp` (theorem, [line 96](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L96))

> Saturated transitions can be composed.

```lean
theorem STr.comp
    [HasTau Label] {lts : LTS State Label}
    (h1 : lts.STr s1 HasTau.τ s2)
    (h2 : lts.STr s2 μ s3)
    (h3 : lts.STr s3 HasTau.τ s4) :
  lts.STr s1 μ s4
```

`Cslib.LTS.saturate_tr_saturate_sTr` (theorem, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L111))

> In a saturated LTS, transitions and saturated transitions agree for every label.

```lean
theorem saturate_tr_saturate_sTr [hHasTau : HasTau Label] (lts : LTS State Label) :
    lts.saturate.Tr s μ = lts.saturate.STr s μ
```

`Cslib.LTS.mem_saturate_image_τ` (lemma, [line 125](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L125))

> In a saturated LTS, every state is in its τ-image.

```lean
lemma mem_saturate_image_τ [HasTau Label] (lts : LTS State Label) :
  s ∈ lts.saturate.image s HasTau.τ
```

`Cslib.LTS.subset_saturate_setImage_τ` (lemma, [line 130](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L130))

> Monotonicity of `setImage` on `HasTau.τ`.

```lean
lemma subset_saturate_setImage_τ [HasTau Label] (lts : LTS State Label) :
    S ⊆ lts.saturate.setImage S HasTau.τ
```

`Cslib.LTS.empty_saturate_setImage_τ` (lemma, [line 136](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L136))

> `setImage` preserves (non-)emptyness.

```lean
lemma empty_saturate_setImage_τ [HasTau Label] (lts : LTS State Label) :
    lts.saturate.setImage S HasTau.τ = ∅ ↔ S = ∅
```

`Cslib.LTS.τClosure` (definition, [line 141](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L141))

> The `τ`-closure of a set of states `S` is the set of states reachable by any state in `S`
> by performing only `τ`-transitions.

```lean
def τClosure [HasTau Label] (lts : LTS State Label) (S : Set State) : Set State
```

`Cslib.LTS.τClosure_subset` (lemma, [line 146](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L146))

> Monotonicity of `setImage` on `HasTau.τ`.

```lean
lemma τClosure_subset [HasTau Label] (lts : LTS State Label) :
    S ⊆ lts.τClosure S
```

`Cslib.LTS.mem_τClosure_iff` (theorem, [line 151](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L151))

> The `τ`-closure of `S` consists of the states reachable from `S` by `τ`-transitions.

```lean
theorem mem_τClosure_iff [HasTau Label] {lts : LTS State Label} {S : Set State} {s' : State} :
    s' ∈ lts.τClosure S ↔ ∃ s ∈ S, lts.τSTr s s'
```

`Cslib.LTS.τClosure_empty` (theorem, [line 157](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L157))

> The `τ`-closure of the empty set is empty.

```lean
theorem τClosure_empty [HasTau Label] (lts : LTS State Label) : lts.τClosure ∅ = ∅
```

`Cslib.LTS.τClosure_union` (theorem, [line 162](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L162))

> The `τ`-closure distributes over binary unions.

```lean
theorem τClosure_union [HasTau Label] (lts : LTS State Label) (S T : Set State) :
    lts.τClosure (S ∪ T) = lts.τClosure S ∪ lts.τClosure T
```

`Cslib.LTS.τClosure_mono` (theorem, [line 168](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L168))

> Taking the `τ`-closure is monotone.

```lean
theorem τClosure_mono [HasTau Label] (lts : LTS State Label) {S T : Set State} (h : S ⊆ T) :
    lts.τClosure S ⊆ lts.τClosure T
```

`Cslib.LTS.τClosure_τClosure` (theorem, [line 174](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L174))

> The `τ`-closure is idempotent.

```lean
theorem τClosure_τClosure [HasTau Label] (lts : LTS State Label) (S : Set State) :
    lts.τClosure (lts.τClosure S) = lts.τClosure S
```

`Cslib.LTS.saturate_setImage_of_ne_τ` (theorem, [line 183](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L183))

> For a label other than `τ`, the saturated image of `S` is the `τ`-closure of the image of the
> `τ`-closure of `S`.

```lean
theorem saturate_setImage_of_ne_τ [HasTau Label] (lts : LTS State Label) {S : Set State}
    {μ : Label} (hμ : μ ≠ HasTau.τ) :
    lts.saturate.setImage S μ = lts.τClosure (lts.setImage (lts.τClosure S) μ)
```

`Cslib.LTS.SMTr` (inductive type, [line 191](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L191))

> Saturated multistep transition relation.

```lean
inductive SMTr [HasTau Label] (lts : LTS State Label) : State → List Label → State → Prop where
  | τ : lts.STr s HasTau.τ s' → lts.SMTr s [] s'
  | stepL : lts.STr s1 μ s2 → lts.SMTr s2 μs s3 → lts.SMTr s1 (μ :: μs) s3
```

`Cslib.LTS.SMTr.refl` (theorem, [line 197](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L197))

> The saturated multistep transition relation is reflexive.

```lean
theorem SMTr.refl [HasTau Label] (lts : LTS State Label) (s : State) :
    lts.SMTr s [] s
```

`Cslib.LTS.SMTr.comp` (theorem, [line 204](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L204))

> The saturated multistep transition relation is transitive.

```lean
theorem SMTr.comp [HasTau Label] {lts : LTS State Label}
    (h₁ : lts.SMTr s₁ μs₁ s₂) (h₂ : lts.SMTr s₂ μs₂ s₃) : lts.SMTr s₁ (μs₁ ++ μs₂) s₃
```

`Cslib.LTS.SMTr.fromMTr` (theorem, [line 216](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L216))

> A multistep transition implies a saturated multistep transition.

```lean
theorem SMTr.fromMTr [HasTau Label] {lts : LTS State Label}
    (h : lts.MTr s μs s') : lts.SMTr s μs s'
```

`Cslib.LTS.sMTr_τSTr_iff` (theorem, [line 225](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L225))

```lean
theorem sMTr_τSTr_iff [HasTau Label] {lts : LTS State Label} :
    lts.τSTr s s' ↔ lts.SMTr s [] s'
```

`Cslib.LTS.saturate_mTr_sMTr_not_nil_iff` (theorem, [line 230](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L230))

> A saturated multistep transition with a nonempty label list implies a multistep transition.

```lean
theorem saturate_mTr_sMTr_not_nil_iff [HasTau Label] {lts : LTS State Label}
    (hμs : μs ≠ []) : lts.saturate.MTr s μs s' ↔ lts.SMTr s μs s'
```

`Cslib.LTS.τSTr_iff_exists_mTr_replicate` (theorem, [line 259](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L259))

> A saturated `τ`-transition is a run along a list of `τ`s.

```lean
theorem τSTr_iff_exists_mTr_replicate [HasTau Label] {lts : LTS State Label} {s t : State} :
    lts.τSTr s t ↔ ∃ n, lts.MTr s (List.replicate n HasTau.τ) t
```

`Cslib.LTS.sMTr_iff_exists_mTr_filter` (theorem, [line 281](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean#L281))

> A saturated run along a list of visible labels is a run whose labels, once the `τ`s are
> dropped, are that list.

```lean
theorem sMTr_iff_exists_mTr_filter [HasTau Label] [DecidableEqTau Label]
    {lts : LTS State Label} {s t : State} {μs : List Label} (hμs : ∀ μ ∈ μs, μ ≠ HasTau.τ) :
    lts.SMTr s μs t ↔ ∃ νs : List Label, νs.filter (· ≠ HasTau.τ) = μs ∧ lts.MTr s νs t
```

## Depends on

- [Conversions between `LTS` and `Relation`](relation.md)
- [Images of sets of states](setimage.md)

## Sources

- [Cslib/Foundations/Semantics/LTS/HasTau.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/HasTau.lean)
