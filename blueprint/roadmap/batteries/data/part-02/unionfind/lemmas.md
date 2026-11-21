---
catalog: module
lean: Batteries.UnionFind.arr_empty, Batteries.UnionFind.parent_empty, Batteries.UnionFind.rank_empty, Batteries.UnionFind.rootD_empty, Batteries.UnionFind.arr_push, Batteries.UnionFind.parentD_push, Batteries.UnionFind.parent_push, Batteries.UnionFind.rankD_push, Batteries.UnionFind.rank_push, Batteries.UnionFind.rankMax_push, Batteries.UnionFind.root_push, Batteries.UnionFind.arr_link, Batteries.UnionFind.parentD_linkAux, Batteries.UnionFind.parent_link, Batteries.UnionFind.root_link, Batteries.UnionFind.Equiv.rfl, Batteries.UnionFind.Equiv.symm, Batteries.UnionFind.Equiv.trans, Batteries.UnionFind.equiv_empty, Batteries.UnionFind.equiv_push, Batteries.UnionFind.equiv_rootD, Batteries.UnionFind.equiv_rootD_l, Batteries.UnionFind.equiv_rootD_r, Batteries.UnionFind.equiv_find, Batteries.UnionFind.equiv_link, Batteries.UnionFind.equiv_union
statement: formalized
proof: formalized
---

# UnionFind/Lemmas

`Batteries.Data.UnionFind.Lemmas`, in [Batteries/Data/UnionFind/Lemmas.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean), by Mario Carneiro.

`Batteries.UnionFind.arr_empty` (theorem, [line 15](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L15))

```lean
theorem arr_empty : empty.arr = #[]
```

`Batteries.UnionFind.parent_empty` (theorem, [line 16](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L16))

```lean
theorem parent_empty : empty.parent a = a
```

`Batteries.UnionFind.rank_empty` (theorem, [line 17](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L17))

```lean
theorem rank_empty : empty.rank a = 0
```

`Batteries.UnionFind.rootD_empty` (theorem, [line 18](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L18))

```lean
theorem rootD_empty : empty.rootD a = a
```

`Batteries.UnionFind.arr_push` (theorem, [line 20](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L20))

```lean
theorem arr_push {m : UnionFind} : m.push.arr = m.arr.push ⟨m.arr.size, 0⟩
```

`Batteries.UnionFind.parentD_push` (theorem, [line 22](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L22))

```lean
theorem parentD_push {arr : Array UFNode} :
    parentD (arr.push ⟨arr.size, 0⟩) a = parentD arr a
```

`Batteries.UnionFind.parent_push` (theorem, [line 30](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L30))

```lean
theorem parent_push {m : UnionFind} : m.push.parent a = m.parent a
```

`Batteries.UnionFind.rankD_push` (theorem, [line 32](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L32))

```lean
theorem rankD_push {arr : Array UFNode} :
    rankD (arr.push ⟨arr.size, 0⟩) a = rankD arr a
```

`Batteries.UnionFind.rank_push` (theorem, [line 37](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L37))

```lean
theorem rank_push {m : UnionFind} : m.push.rank a = m.rank a
```

`Batteries.UnionFind.rankMax_push` (theorem, [line 39](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L39))

```lean
theorem rankMax_push {m : UnionFind} : m.push.rankMax = m.rankMax
```

`Batteries.UnionFind.root_push` (theorem, [line 41](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L41))

```lean
theorem root_push {self : UnionFind} : self.push.rootD x = self.rootD x
```

`Batteries.UnionFind.arr_link` (theorem, [line 44](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L44))

```lean
theorem arr_link : (link self x y yroot).arr = linkAux self.arr x y
```

`Batteries.UnionFind.parentD_linkAux` (theorem, [line 46](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L46))

```lean
theorem parentD_linkAux {self} {x y : Fin self.size} :
    parentD (linkAux self x y) i =
    if x.1 = y then
      parentD self i
    else
      if self[y.1].rank < self[x.1].rank then
        if y = i then x else parentD self i
      else
        if x = i then y else parentD self i
```

`Batteries.UnionFind.parent_link` (theorem, [line 58](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L58))

```lean
theorem parent_link {self} {x y : Fin self.size} (yroot) {i} :
    (link self x y yroot).parent i =
    if x.1 = y then
      self.parent i
    else
      if self.rank y < self.rank x then
        if y = i then x else self.parent i
      else
        if x = i then y else self.parent i
```

`Batteries.UnionFind.root_link` (theorem, [line 69](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L69))

```lean
theorem root_link {self : UnionFind} {x y : Fin self.size}
    (xroot : self.parent x = x) (yroot : self.parent y = y) :
    ∃ r, (r = x ∨ r = y) ∧ ∀ i,
      (link self x y yroot).rootD i =
      if self.rootD i = x ∨ self.rootD i = y then r.1 else self.rootD i
```

`Batteries.UnionFind.Equiv.rfl` (theorem, [line 104](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L104))

```lean
nonrec theorem Equiv.rfl : Equiv self a a
```

`Batteries.UnionFind.Equiv.symm` (theorem, [line 105](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L105))

```lean
nonrec theorem Equiv.symm : Equiv self a b → Equiv self b a
```

`Batteries.UnionFind.Equiv.trans` (theorem, [line 106](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L106))

```lean
nonrec theorem Equiv.trans : Equiv self a b → Equiv self b c → Equiv self a c
```

`Batteries.UnionFind.equiv_empty` (theorem, [line 108](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L108))

```lean
theorem equiv_empty : Equiv empty a b ↔ a = b
```

`Batteries.UnionFind.equiv_push` (theorem, [line 110](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L110))

```lean
theorem equiv_push : Equiv self.push a b ↔ Equiv self a b
```

`Batteries.UnionFind.equiv_rootD` (theorem, [line 112](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L112))

```lean
theorem equiv_rootD : Equiv self (self.rootD a) a
```

`Batteries.UnionFind.equiv_rootD_l` (theorem, [line 113](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L113))

```lean
theorem equiv_rootD_l : Equiv self (self.rootD a) b ↔ Equiv self a b
```

`Batteries.UnionFind.equiv_rootD_r` (theorem, [line 115](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L115))

```lean
theorem equiv_rootD_r : Equiv self a (self.rootD b) ↔ Equiv self a b
```

`Batteries.UnionFind.equiv_find` (theorem, [line 118](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L118))

```lean
theorem equiv_find : Equiv (self.find x).1 a b ↔ Equiv self a b
```

`Batteries.UnionFind.equiv_link` (theorem, [line 120](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L120))

```lean
theorem equiv_link {self : UnionFind} {x y : Fin self.size}
    (xroot : self.parent x = x) (yroot : self.parent y = y) :
    Equiv (link self x y yroot) a b ↔
    Equiv self a b ∨ Equiv self a x ∧ Equiv self y b ∨ Equiv self a y ∧ Equiv self x b
```

`Batteries.UnionFind.equiv_union` (theorem, [line 141](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean#L141))

```lean
theorem equiv_union {self : UnionFind} {x y : Fin self.size} :
    Equiv (union self x y) a b ↔
    Equiv self a b ∨ Equiv self a x ∧ Equiv self y b ∨ Equiv self a y ∧ Equiv self x b
```

## Depends on

- [UnionFind/Basic](basic.md)

## Sources

- [Batteries/Data/UnionFind/Lemmas.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/UnionFind/Lemmas.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.UnionFind.Lemmas.json)
