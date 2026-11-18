---
catalog: module
lean: Cslib.LTS.withIdle, Cslib.LTSCat, Cslib.LTS.Morphism, Cslib.LTS.Morphism.id, Cslib.LTS.Morphism.comp
statement: formalized
proof: formalized
---

# Category of Labelled Transition Systems

`Cslib.Foundations.Semantics.LTS.LTSCat.Basic`, in [Cslib/Foundations/Semantics/LTS/LTSCat/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/LTSCat/Basic.lean), by Ayberk Tosun.

> This file contains the definition of the category of labelled transition systems
> as defined in Winskel and Nielsen's handbook chapter [WinskelNielsen1995].
>
> ## References
>
> * [N. Winskel and M. Nielsen, *Models for concurrency*][WinskelNielsen1995]

`Cslib.LTS.withIdle` (definition, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/LTSCat/Basic.lean#L33))

> We first define what is denoted `Tran*` in [WinskelNielsen1995]: the extension of
> a transition relation with idle transitions.

```lean
def LTS.withIdle (lts : LTS State Label) : LTS State (Option Label)
```

> ## LTSs and LTS morphisms form a category

`Cslib.LTSCat` (structure, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/LTSCat/Basic.lean#L43))

> The definition of labelled transition system (with the type of states and the
> type of labels as part of the structure).

```lean
structure LTSCat : Type (max u v + 1) where
  /-- Type of states of an LTS -/
  State : Type u
  /-- Type of labels of an LTS -/
  Label : Type v
  /-- Transition relation of an LTS -/
  lts : LTS State Label
```

`Cslib.LTS.Morphism` (structure, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/LTSCat/Basic.lean#L56))

> A morphism between two labelled transition systems consists of (1) a function on
> states, (2) a partial function on labels, and a proof that (1) preserves each
> transition along (2).

```lean
structure LTS.Morphism (lts₁ lts₂ : LTSCat.{u, v}) : Type (max u v) where
  /-- Mapping of states of `lts₁` to states of `lts₂` -/
  stateMap : lts₁.State → lts₂.State
  /-- Mapping of labels of `lts₁` to labels of `lts₂` -/
  labelMap : lts₁.Label → Option lts₂.Label
  /-- Stipulation that `stateMap` preserve transitions -/
  labelMap_tr (s s' : lts₁.State) (l : lts₁.Label) :
    lts₁.lts.Tr s l s' → (withIdle lts₂.lts).Tr (stateMap s) (labelMap l) (stateMap s')
```

`Cslib.LTS.Morphism.id` (definition, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/LTSCat/Basic.lean#L66))

> The identity LTS morphism.

```lean
def LTS.Morphism.id (lts : LTSCat) : LTS.Morphism lts lts
```

`Cslib.LTS.Morphism.comp` (definition, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/LTSCat/Basic.lean#L75))

> Composition of LTS morphisms.
>
> We use Kleisli composition to define this.

```lean
def LTS.Morphism.comp {lts₁ lts₂ lts₃} (f : LTS.Morphism lts₁ lts₂) (g : LTS.Morphism lts₂ lts₃) :
    LTS.Morphism lts₁ lts₃
```

## Depends on

- [Labelled Transition System (LTS)](../basic.md)

## Sources

- [Cslib/Foundations/Semantics/LTS/LTSCat/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/LTSCat/Basic.lean)
