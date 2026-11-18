---
catalog: module
lean: Cslib.IsApplicativeHom.map_listMapA, Cslib.IsApplicativeHom.map_listForA, Cslib.IsMonadHom.map_listMapM', Cslib.IsMonadHom.map_listMapMLoop, Cslib.IsMonadHom.map_listMapM, Cslib.IsMonadHom.map_listForM, Cslib.IsMonadHom.map_listFoldlM, Cslib.IsMonadHom.map_listFoldrM, Cslib.IsMonadHom.map_listFindSomeM?, Cslib.IsMonadHom.map_listFindM?, Cslib.IsMonadHom.map_listAnyM, Cslib.IsMonadHom.map_listAllM, Cslib.IsMonadHom.map_listFilterAuxM, Cslib.IsMonadHom.map_listFilterM, Cslib.IsAlternativeHom.map_listFirstM, Cslib.IsApplicativeHom.map_listSingleton, Cslib.IsMonadHom.map_listFlatMap, Cslib.IsFunctorHom.map_listNil, List.isMonadHom_reverse, Cslib.isMonadHom_list_iff
statement: formalized
proof: formalized
---

# List operations and monad morphisms

`Cslib.Foundations.Control.Monad.IsMonadHom.List`, in [Cslib/Foundations/Control/Monad/IsMonadHom/List.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean), by Eric Wieser.

> This file proves that monadic operations on lists commute with monad homomorphisms
> (and applicative homomorphisms), and that `List.reverse` is a monad homomorphism on `List`.

> ### Preservation of list operations under applicative homomorphisms

`Cslib.IsApplicativeHom.map_listMapA` (theorem, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean#L35))

```lean
theorem map_listMapA {F : ∀ {α}, m α → n α} (hf : IsApplicativeHom m n F)
    {α : Type v} {β : Type u} (f : α → m β) (l : List α) :
    F (l.mapA f) = l.mapA (F ∘ f)
```

`Cslib.IsApplicativeHom.map_listForA` (theorem, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean#L41))

```lean
theorem map_listForA {F : ∀ {α}, m α → n α} (hf : IsApplicativeHom m n F)
    {α : Type v} (l : List α) (f : α → m PUnit) :
    F (l.forA f) = l.forA (F ∘ f)
```

> ### Preservation of list operations under monad homomorphisms

`Cslib.IsMonadHom.map_listMapM'` (theorem, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean#L54))

```lean
theorem map_listMapM'
    {F : ∀ {α}, m α → n α} (hf : IsMonadHom m n F)
    {α : Type v} {β : Type u} (f : α → m β) (l : List α) :
    F (l.mapM' f) = l.mapM' (F ∘ f)
```

`Cslib.IsMonadHom.map_listMapMLoop` (theorem, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean#L61))

```lean
theorem map_listMapMLoop
    {F : ∀ {α}, m α → n α} (hf : IsMonadHom m n F)
    {α : Type v} {β : Type u} (f : α → m β) (l : List α) (acc : List β) :
    F (List.mapM.loop f l acc) = List.mapM.loop (F ∘ f) l acc
```

`Cslib.IsMonadHom.map_listMapM` (theorem, [line 70](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean#L70))

```lean
theorem map_listMapM
    {F : ∀ {α}, m α → n α} (hf : IsMonadHom m n F)
    {α : Type v} {β : Type u} (f : α → m β) (l : List α) :
    F (l.mapM f) = l.mapM (F ∘ f)
```

`Cslib.IsMonadHom.map_listForM` (theorem, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean#L77))

```lean
theorem map_listForM {F : ∀ {α}, m α → n α} (hf : IsMonadHom m n F)
    {α : Type v} (l : List α) (f : α → m PUnit) :
    F (l.forM f) = l.forM (F ∘ f)
```

`Cslib.IsMonadHom.map_listFoldlM` (theorem, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean#L83))

```lean
theorem map_listFoldlM {F : ∀ {α}, m α → n α} (hf : IsMonadHom m n F)
    {s : Type u} {α : Type v} (f : s → α → m s) (init : s) (l : List α) :
    F (l.foldlM f init) = l.foldlM (fun s a => F (f s a)) init
```

`Cslib.IsMonadHom.map_listFoldrM` (theorem, [line 89](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean#L89))

```lean
theorem map_listFoldrM {F : ∀ {α}, m α → n α} (hf : IsMonadHom m n F)
    {s : Type u} {α : Type v} (f : α → s → m s) (init : s) (l : List α) :
    F (l.foldrM f init) = l.foldrM (fun a s => F (f a s)) init
```

`Cslib.IsMonadHom.map_listFindSomeM?` (theorem, [line 96](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean#L96))

```lean
theorem map_listFindSomeM?
    {F : ∀ {α}, m α → n α} (hf : IsMonadHom m n F)
    {α : Type v} {β : Type u} (f : α → m (Option β)) (l : List α) :
    F (l.findSomeM? f) = l.findSomeM? (F ∘ f)
```

`Cslib.IsMonadHom.map_listFindM?` (theorem, [line 103](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean#L103))

```lean
theorem map_listFindM? {m n : Type → Type v} [Monad m] [Monad n]
    {F : ∀ {α}, m α → n α} (hf : IsMonadHom m n F)
    {α : Type} (p : α → m Bool) (l : List α) :
    F (l.findM? p) = l.findM? (F ∘ p)
```

`Cslib.IsMonadHom.map_listAnyM` (theorem, [line 110](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean#L110))

```lean
theorem map_listAnyM {m n : Type → Type v} [Monad m] [Monad n]
    {F : ∀ {α}, m α → n α} (hf : IsMonadHom m n F)
    {α : Type v} (p : α → m Bool) (l : List α) :
    F (l.anyM p) = l.anyM (F ∘ p)
```

`Cslib.IsMonadHom.map_listAllM` (theorem, [line 117](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean#L117))

```lean
theorem map_listAllM {m n : Type → Type v} [Monad m] [Monad n]
    {F : ∀ {α}, m α → n α} (hf : IsMonadHom m n F)
    {α : Type v} (p : α → m Bool) (l : List α) :
    F (l.allM p) = l.allM (F ∘ p)
```

`Cslib.IsMonadHom.map_listFilterAuxM` (theorem, [line 124](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean#L124))

```lean
theorem map_listFilterAuxM {m n : Type → Type v} [Monad m] [Monad n]
    {F : ∀ {α}, m α → n α} (hf : IsMonadHom m n F)
    {α : Type} (p : α → m Bool) (l acc : List α) :
    F (List.filterAuxM p l acc) = List.filterAuxM (F ∘ p) l acc
```

`Cslib.IsMonadHom.map_listFilterM` (theorem, [line 131](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean#L131))

```lean
theorem map_listFilterM {m n : Type → Type v} [Monad m] [Monad n]
    {F : ∀ {α}, m α → n α} (hf : IsMonadHom m n F)
    {α : Type} (p : α → m Bool) (l : List α) :
    F (l.filterM p) = l.filterM (F ∘ p)
```

> ### Preservation of list operations under alternative homomorphisms

`Cslib.IsAlternativeHom.map_listFirstM` (theorem, [line 145](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean#L145))

```lean
theorem map_listFirstM {F : ∀ {α}, m α → n α} (hf : IsAlternativeHom m n F)
    {α : Type v} {β : Type u} (f : α → m β) (l : List α) :
    F (l.firstM f) = l.firstM (F ∘ f)
```

> ### Monad homomorphisms on the `List` monad

`Cslib.IsApplicativeHom.map_listSingleton` (theorem, [line 155](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean#L155))

```lean
theorem IsApplicativeHom.map_listSingleton
    {F : ∀ {α}, List α → List α} (hf : IsApplicativeHom List List F) {α} (a : α) :
    F ([a] : List α) = [a]
```

`Cslib.IsMonadHom.map_listFlatMap` (theorem, [line 159](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean#L159))

```lean
theorem IsMonadHom.map_listFlatMap
    {F : ∀ {α}, List α → List α} (hf : IsMonadHom List List F) {α β} (l : List α) (g : α → List β) :
    F (l.flatMap g) = (F l).flatMap (F <| g ·)
```

`Cslib.IsFunctorHom.map_listNil` (theorem, [line 164](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean#L164))

```lean
theorem IsFunctorHom.map_listNil {F : ∀ {α}, List α → List α} (hf : IsFunctorHom List List F) {α} :
    F ([] : List α) = []
```

`List.isMonadHom_reverse` (theorem, [line 169](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean#L169))

```lean
protected theorem _root_.List.isMonadHom_reverse : IsMonadHom List List List.reverse
```

`Cslib.isMonadHom_list_iff` (theorem, [line 195](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean#L195))

> The only monad morphisms on lists are the identity and reversal.

```lean
theorem isMonadHom_list_iff (f : ∀ {α : Type u}, List α → List α) :
    IsMonadHom List List @f ↔ @f = (@id <| List ·) ∨ @f = @List.reverse
```

## Depends on

- [(unbundled) morphisms of monads](../ismonadhom.md)

## Sources

- [Cslib/Foundations/Control/Monad/IsMonadHom/List.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/IsMonadHom/List.lean)
