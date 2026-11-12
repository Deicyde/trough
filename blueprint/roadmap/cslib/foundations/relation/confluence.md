---
catalog: module
lean: Relation.Commute.to_confluent, Relation.Commute.toConfluent, Relation.StronglyCommute.to_stronglyConfluent, Relation.StronglyCommute.toStronglyConfluent, Relation.DiamondCommute.to_diamond, Relation.DiamondCommute.toDiamond, Relation.SemiCommute.to_semiConfluent, Relation.LocallyCommute.to_locallyConfluent, Relation.DiamondCommute.diamond_commute_reflTransGen_right, Relation.DiamondCommute.diamond_commute_reflTransGen_left, Relation.DiamondCommute.to_semiCommute, Relation.Diamond.to_semiConfluent, Relation.Diamond.extend, Relation.Commute.isTrans_join₂_reflTransGen, Relation.Confluent.isTrans_join_reflTransGen, Relation.SemiCommute.to_commute, Relation.SemiConfluent.to_confluent, Relation.SemiConfluent.toConfluent, Relation.commute_equivalents, Relation.semiCommute_iff_commute, Relation.DiamondCommute.to_commute, Relation.churchRosser_iff_eqvGen_le_join_reflTransGen, Relation.confluent_equivalents, Relation.semiConfluent_iff_churchRosser, Relation.SemiConfluent_iff_ChurchRosser, Relation.confluent_iff_churchRosser, Relation.Confluent_iff_ChurchRosser, Relation.confluent_iff_semiConfluent, Relation.Confluent_iff_SemiConfluent, Relation.Diamond.to_confluent, Relation.Diamond.toConfluent, Relation.confluent_of_unique_end, Relation.Confluent_of_unique_end, Relation.ChurchRosser.normal_eqvGen_reflTransGen, Relation.ChurchRosser.normal_eq, Relation.Confluent.equivalence_join_reflTransGen, Relation.Normalizing.confluent_iff_forall_unique_normal, Relation.Terminating.confluent_iff_forall_unique_normal, Relation.Terminating.isConfluent_iff_all_unique_Normal, Relation.Convergent.to_terminating, Relation.Convergent.isTerminating, Relation.Convergent.to_confluent, Relation.Convergent.isConfluent, Relation.Convergent.to_normalizing, Relation.Convergent.isNormalizing, Relation.Convergent.unique_normal, Relation.Convergent.unique_Normal, Relation.Confluent.to_locallyConfluent, Relation.Confluent.toLocallyConfluent, Relation.LocallyCommute.commute_of_terminating_sup, Relation.LocallyConfluent.terminating_toConfluent, Relation.LocallyConfluent.Terminating_toConfluent, Relation.StronglyCommute.extend, Relation.StronglyCommute.to_commute, Relation.StronglyCommute.toCommute, Relation.StronglyConfluent.to_confluent, Relation.StronglyConfluent.toConfluent, Relation.DiamondCommute.join_left, Relation.Commute.join_left, Relation.Commute.join_confluent, Relation.RightUnique.to_confluent, Relation.RightUnique.toConfluent, Relation.Reducible.sup_iff, Relation.Normal.sup_iff
statement: formalized
proof: formalized
---

# Relations: Confluence

`Cslib.Foundations.Relation.Confluence`, in [Cslib/Foundations/Relation/Confluence.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean), by Fabrizio Montesi, Thomas Waring, Chris Henson.

> This module proves some properties regarding confluence that are used for both lambda calculi and
> combinatory logic. Some notable theorems:
>
> * `Diamond.to_confluent`: the diamond property implies confluence
> * `LocallyConfluent.terminating_toConfluent`: Newman's lemma
>
> We prove most results first for two relations, where `Confluent r` becomes `Commute r₁ r₂`, then
> specialize to the classical case where `r₁ = r₂`.
>
> ## References
>
> * [*Term Rewriting and All That*][Baader1998]

`Relation.Commute.to_confluent` (theorem, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L37))

```lean
theorem Commute.to_confluent : Commute r r = Confluent r
```

`Relation.Commute.toConfluent` (alias, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L39))

```lean
alias Commute.toConfluent
```

`Relation.StronglyCommute.to_stronglyConfluent` (theorem, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L41))

```lean
theorem StronglyCommute.to_stronglyConfluent :
StronglyCommute r r = StronglyConfluent r
```

`Relation.StronglyCommute.toStronglyConfluent` (alias, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L44))

```lean
alias StronglyCommute.toStronglyConfluent
```

`Relation.DiamondCommute.to_diamond` (theorem, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L47))

```lean
theorem DiamondCommute.to_diamond : DiamondCommute r r = Diamond r
```

`Relation.DiamondCommute.toDiamond` (alias, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L49))

```lean
alias DiamondCommute.toDiamond
```

`Relation.SemiCommute.to_semiConfluent` (theorem, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L51))

```lean
theorem SemiCommute.to_semiConfluent : SemiCommute r r = SemiConfluent r
```

`Relation.LocallyCommute.to_locallyConfluent` (theorem, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L53))

```lean
theorem LocallyCommute.to_locallyConfluent : LocallyCommute r r = LocallyConfluent r
```

`Relation.DiamondCommute.diamond_commute_reflTransGen_right` (lemma, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L61))

```lean
lemma DiamondCommute.diamond_commute_reflTransGen_right (h : DiamondCommute r₁ r₂) :
    DiamondCommute r₁ (ReflTransGen r₂)
```

`Relation.DiamondCommute.diamond_commute_reflTransGen_left` (lemma, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L71))

```lean
lemma DiamondCommute.diamond_commute_reflTransGen_left (h : DiamondCommute r₁ r₂) :
    DiamondCommute (ReflTransGen r₁) r₂
```

`Relation.DiamondCommute.to_semiCommute` (lemma, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L76))

```lean
lemma DiamondCommute.to_semiCommute (h : DiamondCommute r₁ r₂) : SemiCommute r₁ r₂
```

`Relation.Diamond.to_semiConfluent` (lemma, [line 81](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L81))

> Extending a multistep reduction by a single step preserves multi-joinability.

```lean
lemma Diamond.to_semiConfluent (h : Diamond r) : SemiConfluent r
```

`Relation.Diamond.extend` (alias, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L83))

```lean
alias Diamond.extend
```

`Relation.Commute.isTrans_join₂_reflTransGen` (theorem, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L85))

```lean
theorem Commute.isTrans_join₂_reflTransGen (h : Commute r₁ r₂) :
    IsTrans α (Join₂ (ReflTransGen r₁) (ReflTransGen r₂))
```

`Relation.Confluent.isTrans_join_reflTransGen` (theorem, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L92))

```lean
theorem Confluent.isTrans_join_reflTransGen (h : Confluent r) : IsTrans α (Join (ReflTransGen r))
```

`Relation.SemiCommute.to_commute` (theorem, [line 95](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L95))

```lean
theorem SemiCommute.to_commute (h : SemiCommute r₁ r₂) : Commute r₁ r₂
```

`Relation.SemiConfluent.to_confluent` (theorem, [line 104](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L104))

```lean
theorem SemiConfluent.to_confluent (h : SemiConfluent r) : Confluent r
```

`Relation.SemiConfluent.toConfluent` (alias, [line 106](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L106))

```lean
alias SemiConfluent.toConfluent
```

`Relation.commute_equivalents` (theorem, [line 108](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L108))

```lean
theorem commute_equivalents :
    [SemiCommute r₁ r₂, Commute r₁ r₂, IsTrans α (Join₂ (ReflTransGen r₁) (ReflTransGen r₂)),
      ReflTransGen (r₁ ⊔ swap r₂) ≤ Join₂ (ReflTransGen r₁) (ReflTransGen r₂),
      ReflTransGen (r₁ ⊔ swap r₂) = Join₂ (ReflTransGen r₁) (ReflTransGen r₂)].TFAE
```

`Relation.semiCommute_iff_commute` (theorem, [line 124](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L124))

```lean
theorem semiCommute_iff_commute : SemiCommute r₁ r₂ ↔ Commute r₁ r₂
```

`Relation.DiamondCommute.to_commute` (theorem, [line 126](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L126))

```lean
theorem DiamondCommute.to_commute (h : DiamondCommute r₁ r₂) : Commute r₁ r₂
```

`Relation.churchRosser_iff_eqvGen_le_join_reflTransGen` (theorem, [line 134](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L134))

```lean
theorem churchRosser_iff_eqvGen_le_join_reflTransGen :
    ChurchRosser r ↔ EqvGen r ≤ Join (ReflTransGen r)
```

`Relation.confluent_equivalents` (theorem, [line 138](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L138))

```lean
theorem confluent_equivalents :
    [ChurchRosser r, SemiConfluent r, Confluent r, IsTrans α (Join (ReflTransGen r)),
      EqvGen r ≤ Join (ReflTransGen r), EqvGen r = Join (ReflTransGen r)].TFAE
```

`Relation.semiConfluent_iff_churchRosser` (theorem, [line 145](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L145))

```lean
theorem semiConfluent_iff_churchRosser : SemiConfluent r ↔ ChurchRosser r
```

`Relation.SemiConfluent_iff_ChurchRosser` (alias, [line 148](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L148))

```lean
alias SemiConfluent_iff_ChurchRosser
```

`Relation.confluent_iff_churchRosser` (theorem, [line 151](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L151))

```lean
theorem confluent_iff_churchRosser : Confluent r ↔ ChurchRosser r
```

`Relation.Confluent_iff_ChurchRosser` (alias, [line 156](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L156))

```lean
alias Confluent_iff_ChurchRosser
```

`Relation.confluent_iff_semiConfluent` (theorem, [line 160](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L160))

```lean
theorem confluent_iff_semiConfluent : Confluent r ↔ SemiConfluent r
```

`Relation.Confluent_iff_SemiConfluent` (alias, [line 163](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L163))

```lean
alias Confluent_iff_SemiConfluent
```

`Relation.Diamond.to_confluent` (theorem, [line 166](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L166))

```lean
theorem Diamond.to_confluent (h : Diamond r) : Confluent r
```

`Relation.Diamond.toConfluent` (alias, [line 168](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L168))

```lean
alias Diamond.toConfluent
```

`Relation.confluent_of_unique_end` (theorem, [line 170](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L170))

```lean
theorem confluent_of_unique_end {x : α} (h : ∀ y : α, ReflTransGen r y x) : Confluent r
```

`Relation.Confluent_of_unique_end` (alias, [line 174](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L174))

```lean
alias Confluent_of_unique_end
```

`Relation.ChurchRosser.normal_eqvGen_reflTransGen` (theorem, [line 177](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L177))

> For a Church-Rosser relation, elements in an equivalence class must be multi-step related.

```lean
theorem ChurchRosser.normal_eqvGen_reflTransGen (cr : ChurchRosser r) (norm : Normal r x)
    (xy : EqvGen r y x) : ReflTransGen r y x
```

`Relation.ChurchRosser.normal_eq` (theorem, [line 183](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L183))

> For a Church-Rosser relation there is one normal form in each equivalence class.

```lean
theorem ChurchRosser.normal_eq (cr : ChurchRosser r) (nx : Normal r x) (ny : Normal r y)
    (xy : EqvGen r x y) : x = y
```

`Relation.Confluent.equivalence_join_reflTransGen` (theorem, [line 189](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L189))

> Confluence implies that multi-step joinability is an equivalence.

```lean
theorem Confluent.equivalence_join_reflTransGen (h : Confluent r) :
    Equivalence (Join (ReflTransGen r))
```

`Relation.Normalizing.confluent_iff_forall_unique_normal` (theorem, [line 194](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L194))

```lean
theorem Normalizing.confluent_iff_forall_unique_normal (hn : Normalizing r) :
    Confluent r ↔ ∀ a : α, ∃! n : α, ReflTransGen r a n ∧ Normal r n
```

`Relation.Terminating.confluent_iff_forall_unique_normal` (theorem, [line 212](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L212))

```lean
theorem Terminating.confluent_iff_forall_unique_normal (ht : Terminating r) :
    Confluent r ↔ ∀ a : α, ∃! n : α, ReflTransGen r a n ∧ Normal r n
```

`Relation.Terminating.isConfluent_iff_all_unique_Normal` (alias, [line 216](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L216))

```lean
alias Terminating.isConfluent_iff_all_unique_Normal
```

`Relation.Convergent.to_terminating` (theorem, [line 219](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L219))

```lean
theorem Convergent.to_terminating (h : Convergent r) : Terminating r
```

`Relation.Convergent.isTerminating` (alias, [line 221](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L221))

```lean
alias Convergent.isTerminating
```

`Relation.Convergent.to_confluent` (theorem, [line 223](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L223))

```lean
theorem Convergent.to_confluent (h : Convergent r) : Confluent r
```

`Relation.Convergent.isConfluent` (alias, [line 225](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L225))

```lean
alias Convergent.isConfluent
```

`Relation.Convergent.to_normalizing` (theorem, [line 227](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L227))

```lean
theorem Convergent.to_normalizing (h : Convergent r) : Normalizing r
```

`Relation.Convergent.isNormalizing` (alias, [line 230](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L230))

```lean
alias Convergent.isNormalizing
```

`Relation.Convergent.unique_normal` (theorem, [line 232](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L232))

```lean
theorem Convergent.unique_normal (h : Convergent r) :
    ∀ a : α, ∃! n : α, ReflTransGen r a n ∧ Normal r n
```

`Relation.Convergent.unique_Normal` (alias, [line 236](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L236))

```lean
alias Convergent.unique_Normal
```

`Relation.Confluent.to_locallyConfluent` (theorem, [line 238](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L238))

```lean
theorem Confluent.to_locallyConfluent (h : Confluent r) : LocallyConfluent r
```

`Relation.Confluent.toLocallyConfluent` (alias, [line 242](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L242))

```lean
alias Confluent.toLocallyConfluent
```

`Relation.LocallyCommute.commute_of_terminating_sup` (theorem, [line 245](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L245))

```lean
theorem LocallyCommute.commute_of_terminating_sup (hlc : LocallyCommute r₁ r₂)
    (ht : Terminating (r₁ ⊔ r₂)) : Commute r₁ r₂
```

`Relation.LocallyConfluent.terminating_toConfluent` (theorem, [line 261](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L261))

> Newman's lemma: a terminating, locally confluent relation is confluent.

```lean
theorem LocallyConfluent.terminating_toConfluent (hlc : LocallyConfluent r) (ht : Terminating r) :
    Confluent r
```

`Relation.LocallyConfluent.Terminating_toConfluent` (alias, [line 264](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L264))

```lean
alias LocallyConfluent.Terminating_toConfluent
```

`Relation.StronglyCommute.extend` (theorem, [line 267](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L267))

```lean
theorem StronglyCommute.extend (h : StronglyCommute r₁ r₂) (xy : ReflTransGen r₁ x y)
    (xz : r₂ x z) : ∃ w, ReflGen r₂ y w ∧ ReflTransGen r₁ z w
```

`Relation.StronglyCommute.to_commute` (theorem, [line 277](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L277))

```lean
theorem StronglyCommute.to_commute (h : StronglyCommute r₁ r₂) : Commute r₁ r₂
```

`Relation.StronglyCommute.toCommute` (alias, [line 284](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L284))

```lean
alias StronglyCommute.toCommute
```

`Relation.StronglyConfluent.to_confluent` (theorem, [line 286](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L286))

```lean
theorem StronglyConfluent.to_confluent (h : StronglyConfluent r) : Confluent r
```

`Relation.StronglyConfluent.toConfluent` (alias, [line 289](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L289))

```lean
alias StronglyConfluent.toConfluent
```

`Relation.DiamondCommute.join_left` (lemma, [line 293](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L293))

> Diamond commutation is preserved by taking the union of the left relations.

```lean
lemma DiamondCommute.join_left (c₁ : DiamondCommute r₁ r₃) (c₂ : DiamondCommute r₂ r₃) :
    DiamondCommute (r₁ ⊔ r₂) r₃
```

`Relation.Commute.join_left` (lemma, [line 299](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L299))

```lean
lemma Commute.join_left (c₁ : Commute r₁ r₃) (c₂ : Commute r₂ r₃) : Commute (r₁ ⊔ r₂) r₃
```

`Relation.Commute.join_confluent` (theorem, [line 305](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L305))

```lean
theorem Commute.join_confluent (c₁ : Confluent r₁) (c₂ : Confluent r₂) (comm : Commute r₁ r₂) :
    Confluent (r₁ ⊔ r₂)
```

`Relation.RightUnique.to_confluent` (theorem, [line 313](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L313))

> `Relator.RightUnique` corresponds to deterministic reductions, which are confluent, as all
> multi-reductions with a common origin start the same (this fact is
> `Relation.ReflTransGen.total_of_right_unique`.)

```lean
theorem RightUnique.to_confluent (hr : Relator.RightUnique r) : Confluent r
```

`Relation.RightUnique.toConfluent` (alias, [line 319](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L319))

```lean
alias RightUnique.toConfluent
```

`Relation.Reducible.sup_iff` (theorem, [line 321](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L321))

```lean
theorem Reducible.sup_iff (x : α) : Reducible (r₁ ⊔ r₂) x ↔ Reducible r₁ x ∨ Reducible r₂ x
```

`Relation.Normal.sup_iff` (theorem, [line 324](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean#L324))

```lean
theorem Normal.sup_iff (x : α) : Normal (r₁ ⊔ r₂) x ↔ Normal r₁ x ∧ Normal r₂ x
```

## Depends on

- [Relations: Definitions](defs.md)

## Proof depends on

- [Basic properties of relations](basic.md)
- [Termination (well-foundedness) properties of relations](termination.md)

## Sources

- [Cslib/Foundations/Relation/Confluence.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/Confluence.lean)
