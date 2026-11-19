---
catalog: module
lean: ForInStep.bind_done, ForInStep.bind_yield, ForInStep.run_done, ForInStep.run_yield, ForInStep.bindList_nil, ForInStep.bindList_cons, ForInStep.done_bindList, ForInStep.bind_yield_bindList, ForInStep.bind_bindList_assoc, ForInStep.bindList_cons', ForInStep.bindList_append
statement: formalized
proof: formalized
---

# Additional theorems on `ForInStep`

`Batteries.Control.ForInStep.Lemmas`, in [Batteries/Control/ForInStep/Lemmas.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/ForInStep/Lemmas.lean), by Mario Carneiro.

`ForInStep.bind_done` (theorem, [line 14](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/ForInStep/Lemmas.lean#L14))

```lean
theorem ForInStep.bind_done [Monad m] (a : α) (f : α → m (ForInStep α)) :
    (ForInStep.done a).bind (m := m) f = pure (.done a)
```

`ForInStep.bind_yield` (theorem, [line 16](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/ForInStep/Lemmas.lean#L16))

```lean
theorem ForInStep.bind_yield [Monad m] (a : α) (f : α → m (ForInStep α)) :
    (ForInStep.yield a).bind (m := m) f = f a
```

`ForInStep.run_done` (theorem, [line 21](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/ForInStep/Lemmas.lean#L21))

```lean
theorem ForInStep.run_done : (ForInStep.done a).run = a
```

`ForInStep.run_yield` (theorem, [line 22](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/ForInStep/Lemmas.lean#L22))

```lean
theorem ForInStep.run_yield : (ForInStep.yield a).run = a
```

`ForInStep.bindList_nil` (theorem, [line 24](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/ForInStep/Lemmas.lean#L24))

```lean
theorem ForInStep.bindList_nil [Monad m] (f : α → β → m (ForInStep β))
    (s : ForInStep β) : s.bindList f [] = pure s
```

`ForInStep.bindList_cons` (theorem, [line 27](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/ForInStep/Lemmas.lean#L27))

```lean
theorem ForInStep.bindList_cons [Monad m]
    (f : α → β → m (ForInStep β)) (s : ForInStep β) (a l) :
    s.bindList f (a::l) = s.bind fun b => f a b >>= (·.bindList f l)
```

`ForInStep.done_bindList` (theorem, [line 31](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/ForInStep/Lemmas.lean#L31))

```lean
theorem ForInStep.done_bindList [Monad m]
    (f : α → β → m (ForInStep β)) (a l) :
    (ForInStep.done a).bindList f l = pure (.done a)
```

`ForInStep.bind_yield_bindList` (theorem, [line 35](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/ForInStep/Lemmas.lean#L35))

```lean
theorem ForInStep.bind_yield_bindList [Monad m]
    (f : α → β → m (ForInStep β)) (s : ForInStep β) (l) :
    (s.bind fun a => (yield a).bindList f l) = s.bindList f l
```

`ForInStep.bind_bindList_assoc` (theorem, [line 39](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/ForInStep/Lemmas.lean#L39))

```lean
theorem ForInStep.bind_bindList_assoc [Monad m] [LawfulMonad m]
    (f : β → m (ForInStep β)) (g : α → β → m (ForInStep β)) (s : ForInStep β) (l) :
    s.bind f >>= (·.bindList g l) = s.bind fun b => f b >>= (·.bindList g l)
```

`ForInStep.bindList_cons'` (theorem, [line 44](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/ForInStep/Lemmas.lean#L44))

```lean
theorem ForInStep.bindList_cons' [Monad m] [LawfulMonad m]
    (f : α → β → m (ForInStep β)) (s : ForInStep β) (a l) :
    s.bindList f (a::l) = s.bind (f a) >>= (·.bindList f l)
```

`ForInStep.bindList_append` (theorem, [line 48](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/ForInStep/Lemmas.lean#L48))

```lean
theorem ForInStep.bindList_append [Monad m] [LawfulMonad m]
    (f : α → β → m (ForInStep β)) (s : ForInStep β) (l₁ l₂) :
    s.bindList f (l₁ ++ l₂) = s.bindList f l₁ >>= (·.bindList f l₂)
```

## Depends on

- [Additional definitions on `ForInStep`](basic.md)

## Sources

- [Batteries/Control/ForInStep/Lemmas.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Control/ForInStep/Lemmas.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Control.ForInStep.Lemmas.json)
