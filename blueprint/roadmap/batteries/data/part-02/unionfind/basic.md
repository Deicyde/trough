---
catalog: module
lean: Batteries.UFNode, Batteries.UnionFind.parentD, Batteries.UnionFind.rankD, Batteries.UnionFind.parentD_eq, Batteries.UnionFind.rankD_eq, Batteries.UnionFind.parentD_of_not_lt, Batteries.UnionFind.lt_of_parentD, Batteries.UnionFind.parentD_set, Batteries.UnionFind.rankD_set, Batteries.UnionFind, Batteries.UnionFind.size, Batteries.UnionFind.mkEmpty, Batteries.UnionFind.empty, Batteries.UnionFind.parent, Batteries.UnionFind.parent'_lt, Batteries.UnionFind.parent_lt, Batteries.UnionFind.rank, Batteries.UnionFind.rank_lt, Batteries.UnionFind.rank'_lt, Batteries.UnionFind.rankMax, Batteries.UnionFind.rank'_lt_rankMax, Batteries.UnionFind.rankD_lt_rankMax, Batteries.UnionFind.lt_rankMax, Batteries.UnionFind.push_rankD, Batteries.UnionFind.push_parentD, Batteries.UnionFind.push, Batteries.UnionFind.root, Batteries.UnionFind.rootN, Batteries.UnionFind.root!, Batteries.UnionFind.rootD, Batteries.UnionFind.parent_root, Batteries.UnionFind.parent_rootD, Batteries.UnionFind.rootD_parent, Batteries.UnionFind.rootD_lt, Batteries.UnionFind.rootD_eq_self, Batteries.UnionFind.rootD_rootD, Batteries.UnionFind.rootD_ext, Batteries.UnionFind.le_rank_root, Batteries.UnionFind.lt_rank_root, Batteries.UnionFind.FindAux, Batteries.UnionFind.findAux, Batteries.UnionFind.findAux_root, Batteries.UnionFind.findAux_s, Batteries.UnionFind.rankD_findAux, Batteries.UnionFind.parentD_findAux, Batteries.UnionFind.parentD_findAux_rootD, Batteries.UnionFind.parentD_findAux_lt, Batteries.UnionFind.parentD_findAux_or, Batteries.UnionFind.lt_rankD_findAux, Batteries.UnionFind.find, Batteries.UnionFind.findN, Batteries.UnionFind.find!, Batteries.UnionFind.findD, Batteries.UnionFind.find_size, Batteries.UnionFind.find_root_2, Batteries.UnionFind.find_parent_1, Batteries.UnionFind.find_parent_or, Batteries.UnionFind.find_root_1, Batteries.UnionFind.linkAux, Batteries.UnionFind.setParentBump_rankD_lt, Batteries.UnionFind.setParent_rankD_lt, Batteries.UnionFind.linkAux_size, Batteries.UnionFind.link, Batteries.UnionFind.linkN, Batteries.UnionFind.link!, Batteries.UnionFind.union, Batteries.UnionFind.unionN, Batteries.UnionFind.union!, Batteries.UnionFind.checkEquiv, Batteries.UnionFind.checkEquivN, Batteries.UnionFind.checkEquiv!, Batteries.UnionFind.checkEquivD, Batteries.UnionFind.Equiv
statement: formalized
proof: formalized
---

# UnionFind/Basic

`Batteries.Data.UnionFind.Basic`, in [Batteries/Data/UnionFind/Basic.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean), by Mario Carneiro.

`Batteries.UFNode` (structure, [line 17](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L17))

> Union-find node type

```lean
structure UFNode where
  /-- Parent of node -/
  parent : Nat
  /-- Rank of node -/
  rank : Nat
```

`Batteries.UnionFind.parentD` (definition, [line 26](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L26))

> Parent of a union-find node, defaults to self when the node is a root

```lean
def parentD (arr : Array UFNode) (i : Nat) : Nat
```

`Batteries.UnionFind.rankD` (definition, [line 30](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L30))

> Rank of a union-find node, defaults to 0 when the node is a root

```lean
def rankD (arr : Array UFNode) (i : Nat) : Nat
```

`Batteries.UnionFind.parentD_eq` (theorem, [line 33](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L33))

```lean
theorem parentD_eq {arr : Array UFNode} {i} (h) :
    parentD arr i = arr[i].parent
```

`Batteries.UnionFind.rankD_eq` (theorem, [line 36](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L36))

```lean
theorem rankD_eq {arr : Array UFNode} {i} (h) : rankD arr i = arr[i].rank
```

`Batteries.UnionFind.parentD_of_not_lt` (theorem, [line 38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L38))

```lean
theorem parentD_of_not_lt : ¬i < arr.size → parentD arr i = i
```

`Batteries.UnionFind.lt_of_parentD` (theorem, [line 40](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L40))

```lean
theorem lt_of_parentD : parentD arr i ≠ i → i < arr.size
```

`Batteries.UnionFind.parentD_set` (theorem, [line 43](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L43))

```lean
theorem parentD_set {arr : Array UFNode} {x v i h} :
    parentD (arr.set x v h) i = if x = i then v.parent else parentD arr i
```

`Batteries.UnionFind.rankD_set` (theorem, [line 50](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L50))

```lean
theorem rankD_set {arr : Array UFNode} {x v i h} :
    rankD (arr.set x v h) i = if x = i then v.rank else rankD arr i
```

`Batteries.UnionFind` (structure, [line 97](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L97))

> ### Union-find data structure
>
> The `UnionFind` structure is an implementation of disjoint-set data structure
> that uses path compression to make the primary operations run in amortized
> nearly linear time. The nodes of a `UnionFind` structure `s` are natural
> numbers smaller than `s.size`. The structure associates with a canonical
> representative from its equivalence class. The structure can be extended
> using the `push` operation and equivalence classes can be updated using the
> `union` operation.
>
> The main operations for `UnionFind` are:
>
> * `empty`/`mkEmpty` are used to create a new empty structure.
> * `size` returns the size of the data structure.
> * `push` adds a new node to a structure, unlinked to any other node.
> * `union` links two nodes of the data structure, joining their equivalence
>   classes, and performs path compression.
> * `find` returns the canonical representative of a node and updates the data
>   structure using path compression.
> * `root` returns the canonical representative of a node without altering the
>   data structure.
> * `checkEquiv` checks whether two nodes have the same canonical representative
>   and updates the structure using path compression.
>
> Most use cases should prefer `find` over `root` to benefit from the speedup from path-compression.
>
> The main operations use `Fin s.size` to represent nodes of the union-find structure.
> Some alternatives are provided:
>
> * `unionN`, `findN`, `rootN`, `checkEquivN` use `Fin n` with a proof that `n = s.size`.
> * `union!`, `find!`, `root!`, `checkEquiv!` use `Nat` and panic when the indices are out of bounds.
> * `findD`, `rootD`, `checkEquivD` use `Nat` and treat out of bound indices as isolated nodes.
>
> The noncomputable relation `UnionFind.Equiv` is provided to use the equivalence relation from a
> `UnionFind` structure in the context of proofs.

```lean
structure UnionFind where
  /-- Array of union-find nodes -/
  arr : Array UFNode
  /-- Validity for parent nodes -/
  parentD_lt : ∀ {i}, i < arr.size → parentD arr i < arr.size
  /-- Validity for rank -/
  rankD_lt : ∀ {i}, parentD arr i ≠ i → rankD arr i < rankD arr (parentD arr i)
```

`Batteries.UnionFind.size` (abbreviation, [line 108](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L108))

> Size of union-find structure.

```lean
abbrev size (self : UnionFind)
```

`Batteries.UnionFind.mkEmpty` (definition, [line 111](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L111))

> Create an empty union-find structure with specific capacity

```lean
def mkEmpty (c : Nat) : UnionFind
```

`Batteries.UnionFind.empty` (definition, [line 117](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L117))

> Empty union-find structure

```lean
def empty
```

`Batteries.UnionFind.parent` (abbreviation, [line 122](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L122))

> Parent of union-find node

```lean
abbrev parent (self : UnionFind) (i : Nat) : Nat
```

`Batteries.UnionFind.parent'_lt` (theorem, [line 124](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L124))

```lean
theorem parent'_lt (self : UnionFind) (i : Nat) (h) : self.arr[i].parent < self.size
```

`Batteries.UnionFind.parent_lt` (theorem, [line 127](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L127))

```lean
theorem parent_lt (self : UnionFind) (i : Nat) : self.parent i < self.size ↔ i < self.size
```

`Batteries.UnionFind.rank` (abbreviation, [line 131](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L131))

> Rank of union-find node

```lean
abbrev rank (self : UnionFind) (i : Nat) : Nat
```

`Batteries.UnionFind.rank_lt` (theorem, [line 133](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L133))

```lean
theorem rank_lt {self : UnionFind} {i : Nat} : self.parent i ≠ i →
    self.rank i < self.rank (self.parent i)
```

`Batteries.UnionFind.rank'_lt` (theorem, [line 136](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L136))

```lean
theorem rank'_lt (self : UnionFind) (i h) : self.arr[i].parent ≠ i →
    self.rank i < self.rank (self.arr[i]).parent
```

`Batteries.UnionFind.rankMax` (definition, [line 141](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L141))

> Maximum rank of nodes in a union-find structure

```lean
noncomputable def rankMax (self : UnionFind)
```

`Batteries.UnionFind.rank'_lt_rankMax` (theorem, [line 143](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L143))

```lean
theorem rank'_lt_rankMax (self : UnionFind) (i : Nat) (h) : (self.arr[i]).rank < self.rankMax
```

`Batteries.UnionFind.rankD_lt_rankMax` (theorem, [line 150](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L150))

```lean
theorem rankD_lt_rankMax (self : UnionFind) (i : Nat) :
    rankD self.arr i < self.rankMax
```

`Batteries.UnionFind.lt_rankMax` (theorem, [line 154](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L154))

```lean
theorem lt_rankMax (self : UnionFind) (i : Nat) : self.rank i < self.rankMax
```

`Batteries.UnionFind.push_rankD` (theorem, [line 156](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L156))

```lean
theorem push_rankD (arr : Array UFNode) : rankD (arr.push ⟨arr.size, 0⟩) i = rankD arr i
```

`Batteries.UnionFind.push_parentD` (theorem, [line 160](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L160))

```lean
theorem push_parentD (arr : Array UFNode) : parentD (arr.push ⟨arr.size, 0⟩) i = parentD arr i
```

`Batteries.UnionFind.push` (definition, [line 167](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L167))

> Add a new node to a union-find structure, unlinked with any other nodes

```lean
def push (self : UnionFind) : UnionFind
```

`Batteries.UnionFind.root` (definition, [line 175](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L175))

> Root of a union-find node.

```lean
def root (self : UnionFind) (x : Fin self.size) : Fin self.size
```

`Batteries.UnionFind.rootN` (definition, [line 185](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L185))

```lean
def rootN (self : UnionFind) (x : Fin n) (h : n = self.size) : Fin n
```

`Batteries.UnionFind.root!` (definition, [line 189](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L189))

> Root of a union-find node. Panics if index is out of bounds.

```lean
def root! (self : UnionFind) (x : Nat) : Nat
```

`Batteries.UnionFind.rootD` (definition, [line 193](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L193))

> Root of a union-find node. Returns input if index is out of bounds.

```lean
def rootD (self : UnionFind) (x : Nat) : Nat
```

`Batteries.UnionFind.parent_root` (theorem, [line 198](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L198))

```lean
theorem parent_root (self : UnionFind) (x : Fin self.size) :
    (self.arr[(self.root x).1]).parent = self.root x
```

`Batteries.UnionFind.parent_rootD` (theorem, [line 205](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L205))

```lean
theorem parent_rootD (self : UnionFind) (x : Nat) :
    self.parent (self.rootD x) = self.rootD x
```

`Batteries.UnionFind.rootD_parent` (theorem, [line 213](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L213))

```lean
theorem rootD_parent (self : UnionFind) (x : Nat) : self.rootD (self.parent x) = self.rootD x
```

`Batteries.UnionFind.rootD_lt` (theorem, [line 222](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L222))

```lean
theorem rootD_lt {self : UnionFind} {x : Nat} : self.rootD x < self.size ↔ x < self.size
```

`Batteries.UnionFind.rootD_eq_self` (theorem, [line 226](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L226))

```lean
theorem rootD_eq_self {self : UnionFind} {x : Nat} : self.rootD x = x ↔ self.parent x = x
```

`Batteries.UnionFind.rootD_rootD` (theorem, [line 230](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L230))

```lean
theorem rootD_rootD {self : UnionFind} {x : Nat} : self.rootD (self.rootD x) = self.rootD x
```

`Batteries.UnionFind.rootD_ext` (theorem, [line 233](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L233))

```lean
theorem rootD_ext {m1 m2 : UnionFind}
    (H : ∀ x, m1.parent x = m2.parent x) {x} : m1.rootD x = m2.rootD x
```

`Batteries.UnionFind.le_rank_root` (theorem, [line 242](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L242))

```lean
theorem le_rank_root {self : UnionFind} {x : Nat} : self.rank x ≤ self.rank (self.rootD x)
```

`Batteries.UnionFind.lt_rank_root` (theorem, [line 251](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L251))

```lean
theorem lt_rank_root {self : UnionFind} {x : Nat} :
    self.rank x < self.rank (self.rootD x) ↔ self.parent x ≠ x
```

`Batteries.UnionFind.FindAux` (structure, [line 258](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L258))

> Auxiliary data structure for find operation

```lean
structure FindAux (n : Nat) where
  /-- Array of nodes -/
  s : Array UFNode
  /-- Index of root node -/
  root : Fin n
  /-- Size requirement -/
  size_eq : s.size = n
```

`Batteries.UnionFind.findAux` (definition, [line 267](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L267))

> Auxiliary function for find operation

```lean
def findAux (self : UnionFind) (x : Fin self.size) : FindAux self.size
```

`Batteries.UnionFind.findAux_root` (theorem, [line 278](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L278))

```lean
theorem findAux_root {self : UnionFind} {x : Fin self.size} :
    (findAux self x).root = self.root x
```

`Batteries.UnionFind.findAux_s` (theorem, [line 288](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L288))

```lean
theorem findAux_s {self : UnionFind} {x : Fin self.size} :
    (findAux self x).s = if self.arr[x.1].parent = x then self.arr else
      (self.findAux ⟨_, self.parent'_lt x x.2⟩).s.modify x fun s =>
        { s with parent := self.rootD x }
```

`Batteries.UnionFind.rankD_findAux` (theorem, [line 298](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L298))

```lean
theorem rankD_findAux {self : UnionFind} {x : Fin self.size} :
    rankD (findAux self x).s i = self.rank i
```

`Batteries.UnionFind.parentD_findAux` (theorem, [line 312](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L312))

```lean
theorem parentD_findAux {self : UnionFind} {x : Fin self.size} :
    parentD (findAux self x).s i =
    if i = x then self.rootD x else parentD (self.findAux ⟨_, self.parent'_lt _ x.2⟩).s i
```

`Batteries.UnionFind.parentD_findAux_rootD` (theorem, [line 326](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L326))

```lean
theorem parentD_findAux_rootD {self : UnionFind} {x : Fin self.size} :
    parentD (findAux self x).s (self.rootD x) = self.rootD x
```

`Batteries.UnionFind.parentD_findAux_lt` (theorem, [line 335](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L335))

```lean
theorem parentD_findAux_lt {self : UnionFind} {x : Fin self.size} (h : i < self.size) :
    parentD (findAux self x).s i < self.size
```

`Batteries.UnionFind.parentD_findAux_or` (theorem, [line 347](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L347))

```lean
theorem parentD_findAux_or (self : UnionFind) (x : Fin self.size) (i) :
    parentD (findAux self x).s i = self.rootD i ∧ self.rootD i = self.rootD x ∨
    parentD (findAux self x).s i = self.parent i
```

`Batteries.UnionFind.lt_rankD_findAux` (theorem, [line 362](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L362))

```lean
theorem lt_rankD_findAux {self : UnionFind} {x : Fin self.size} :
    parentD (findAux self x).s i ≠ i →
    self.rank i < self.rank (parentD (findAux self x).s i)
```

`Batteries.UnionFind.find` (definition, [line 375](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L375))

> Find root of a union-find node, updating the structure using path compression.

```lean
def find (self : UnionFind) (x : Fin self.size) :
    (s : UnionFind) × {_root : Fin s.size // s.size = self.size}
```

`Batteries.UnionFind.findN` (definition, [line 388](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L388))

```lean
def findN (self : UnionFind) (x : Fin n) (h : n = self.size) : UnionFind × Fin n
```

`Batteries.UnionFind.find!` (definition, [line 393](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L393))

> Find root of a union-find node, updating the structure using path compression.
> Panics if index is out of bounds.

```lean
def find! (self : UnionFind) (x : Nat) : UnionFind × Nat
```

`Batteries.UnionFind.findD` (definition, [line 401](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L401))

> Find root of a union-find node, updating the structure using path compression.
> Returns inputs unchanged when index is out of bounds.

```lean
def findD (self : UnionFind) (x : Nat) : UnionFind × Nat
```

`Batteries.UnionFind.find_size` (theorem, [line 407](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L407))

```lean
theorem find_size (self : UnionFind) (x : Fin self.size) :
    (self.find x).1.size = self.size
```

`Batteries.UnionFind.find_root_2` (theorem, [line 410](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L410))

```lean
theorem find_root_2 (self : UnionFind) (x : Fin self.size) :
    (self.find x).2.1.1 = self.rootD x
```

`Batteries.UnionFind.find_parent_1` (theorem, [line 413](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L413))

```lean
theorem find_parent_1 (self : UnionFind) (x : Fin self.size) :
    (self.find x).1.parent x = self.rootD x
```

`Batteries.UnionFind.find_parent_or` (theorem, [line 418](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L418))

```lean
theorem find_parent_or (self : UnionFind) (x : Fin self.size) (i) :
    (self.find x).1.parent i = self.rootD i ∧ self.rootD i = self.rootD x ∨
    (self.find x).1.parent i = self.parent i
```

`Batteries.UnionFind.find_root_1` (theorem, [line 422](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L422))

```lean
theorem find_root_1 (self : UnionFind) (x : Fin self.size) (i : Nat) :
    (self.find x).1.rootD i = self.rootD i
```

`Batteries.UnionFind.linkAux` (definition, [line 439](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L439))

> Link two union-find nodes

```lean
def linkAux (self : Array UFNode) (x y : Fin self.size) : Array UFNode
```

`Batteries.UnionFind.setParentBump_rankD_lt` (theorem, [line 454](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L454))

```lean
theorem setParentBump_rankD_lt {arr : Array UFNode} {x y : Fin arr.size}
    (hroot : arr[x.1].rank < arr[y.1].rank ∨ arr[y.1].parent = y)
    (H : arr[x.1].rank ≤ arr[y.1].rank) {i : Nat}
    (rankD_lt : parentD arr i ≠ i → rankD arr i < rankD arr (parentD arr i))
    (hP : parentD arr' i = if x.1 = i then y.1 else parentD arr i)
    (hR : ∀ {i}, rankD arr' i =
      if y.1 = i ∧ arr[x.1].rank = arr[y.1].rank then
        arr[y.1].rank + 1
      else rankD arr i) :
    ¬parentD arr' i = i → rankD arr' i < rankD arr' (parentD arr' i)
```

`Batteries.UnionFind.setParent_rankD_lt` (theorem, [line 479](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L479))

```lean
theorem setParent_rankD_lt {arr : Array UFNode} {x y : Fin arr.size}
    (h : arr[x.1].rank < arr[y.1].rank) {i : Nat}
    (rankD_lt : parentD arr i ≠ i → rankD arr i < rankD arr (parentD arr i)) :
    let arr' := arr.set x ⟨y, arr[x].rank⟩
    parentD arr' i ≠ i → rankD arr' i < rankD arr' (parentD arr' i)
```

`Batteries.UnionFind.linkAux_size` (theorem, [line 487](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L487))

```lean
theorem linkAux_size : (linkAux self x y).size = self.size
```

`Batteries.UnionFind.link` (definition, [line 493](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L493))

> Link a union-find node to a root node.

```lean
def link (self : UnionFind) (x y : Fin self.size) (yroot : self.parent y = y) : UnionFind
```

`Batteries.UnionFind.linkN` (definition, [line 525](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L525))

```lean
def linkN (self : UnionFind) (x y : Fin n) (yroot : self.parent y = y) (h : n = self.size) :
    UnionFind
```

`Batteries.UnionFind.link!` (definition, [line 529](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L529))

> Link a union-find node to a root node. Panics if either index is out of bounds.

```lean
def link! (self : UnionFind) (x y : Nat) (yroot : self.parent y = y) : UnionFind
```

`Batteries.UnionFind.union` (definition, [line 536](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L536))

> Link two union-find nodes, uniting their respective classes.

```lean
def union (self : UnionFind) (x y : Fin self.size) : UnionFind
```

`Batteries.UnionFind.unionN` (definition, [line 547](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L547))

```lean
def unionN (self : UnionFind) (x y : Fin n) (h : n = self.size) : UnionFind
```

`Batteries.UnionFind.union!` (definition, [line 552](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L552))

> Link two union-find nodes, uniting their respective classes.
> Panics if either index is out of bounds.

```lean
def union! (self : UnionFind) (x y : Nat) : UnionFind
```

`Batteries.UnionFind.checkEquiv` (definition, [line 559](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L559))

> Check whether two union-find nodes are equivalent, updating structure using path compression.

```lean
def checkEquiv (self : UnionFind) (x y : Fin self.size) : UnionFind × Bool
```

`Batteries.UnionFind.checkEquivN` (definition, [line 565](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L565))

```lean
def checkEquivN (self : UnionFind) (x y : Fin n) (h : n = self.size) : UnionFind × Bool
```

`Batteries.UnionFind.checkEquiv!` (definition, [line 570](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L570))

> Check whether two union-find nodes are equivalent, updating structure using path compression.
> Panics if either index is out of bounds.

```lean
def checkEquiv! (self : UnionFind) (x y : Nat) : UnionFind × Bool
```

`Batteries.UnionFind.checkEquivD` (definition, [line 578](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L578))

> Check whether two union-find nodes are equivalent with path compression,
> returns `x == y` if either index is out of bounds

```lean
def checkEquivD (self : UnionFind) (x y : Nat) : UnionFind × Bool
```

`Batteries.UnionFind.Equiv` (definition, [line 584](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean#L584))

> Equivalence relation from a `UnionFind` structure

```lean
def Equiv (self : UnionFind) (a b : Nat) : Prop
```

## Depends on

- [Panic](../../../util/panic.md)

## Sources

- [Batteries/Data/UnionFind/Basic.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UnionFind/Basic.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.UnionFind.Basic.json)
