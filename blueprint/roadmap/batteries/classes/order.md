---
catalog: module
lean: lexOrd_def, Ordering.byKey, Std.OrientedOrd.isGE_of_isLT, Ord.compare_opposite, Batteries.TotalBLE, Batteries.compareOfLessAndEq_eq_lt, Std.OrientedCmp.le_iff_ge, Std.TransCmp.le_trans, Std.TransCmp.lt_of_lt_of_le, Std.TransCmp.lt_of_le_of_lt, Std.TransCmp.ge_trans, Std.TransCmp.gt_of_gt_of_ge, Std.TransCmp.gt_of_ge_of_gt, Std.LawfulLTCmp, Std.LawfulLTCmp.eq_gt_iff_gt, Std.LawfulLECmp, Std.LawfulLECmp.isGE_iff_ge, Std.LawfulLECmp.ne_gt_iff_le, Std.LawfulLECmp.ne_lt_iff_ge, Std.LawfulBCmp, Std.LawfulCmp, Std.LawfulLTOrd, Std.LawfulLEOrd, Std.LawfulBOrd, Std.LawfulOrd, Std.OrientedOrd.instOn, Std.TransOrd.instOn, Std.OrientedOrd.instOrdLex', Std.TransOrd.instOrdLex', Std.LawfulLTCmp.eq_compareOfLessAndEq, Std.ReflCmp.compareOfLessAndEq_of_lt_irrefl, Std.LawfulBEqCmp.compareOfLessAndEq_of_lt_irrefl, Std.TransCmp.compareOfLessAndEq_of_irrefl_of_trans_of_antisymm, Std.TransCmp.compareOfLessAndEq_of_irrefl_of_trans_of_not_lt_of_antisymm, Std.LawfulLTCmp.compareOfLessAndEq_of_irrefl_of_trans_of_antisymm, Std.LawfulLTCmp.compareOfLessAndEq_of_irrefl_of_trans_of_not_lt_of_antisymm, Std.LawfulLECmp.compareOfLessAndEq_of_irrefl_of_trans_of_not_lt_of_antisymm, Std.LawfulCmp.compareOfLessAndEq_of_irrefl_of_trans_of_not_lt_of_antisymm
statement: formalized
proof: formalized
---

# Order

`Batteries.Classes.Order`, in [Batteries/Classes/Order.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean), by Mario Carneiro.

`lexOrd_def` (theorem, [line 13](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L13))

```lean
theorem lexOrd_def [Ord α] [Ord β] :
    (lexOrd : Ord (α × β)).compare = compareLex (compareOn (·.1)) (compareOn (·.2))
```

`Ordering.byKey` (definition, [line 17](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L17))

> Pull back a comparator by a function `f`, by applying the comparator to both arguments.

```lean
def Ordering.byKey (f : α → β) (cmp : β → β → Ordering) (a b : α) : Ordering
```

`Std.OrientedOrd.isGE_of_isLT` (theorem, [line 20](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L20))

```lean
theorem Std.OrientedOrd.isGE_of_isLT [Ord α] [Std.OrientedOrd α] {a b : α}
    (h : (compare b a).isLT) : (compare a b).isGE
```

`Ord.compare_opposite` (theorem, [line 25](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L25))

```lean
theorem Ord.compare_opposite [ord : Ord α] {x y : α} :
    ord.opposite.compare x y = ord.compare y x
```

`Batteries.TotalBLE` (class, [line 31](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L31))

> `TotalBLE le` asserts that `le` has a total order, that is, `le a b ∨ le b a`.

```lean
class TotalBLE (le : α → α → Bool) : Prop where
  /-- `le` is total: either `le a b` or `le b a`. -/
  total : le a b ∨ le b a
```

`Batteries.compareOfLessAndEq_eq_lt` (theorem, [line 35](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L35))

```lean
theorem compareOfLessAndEq_eq_lt {x y : α} [LT α] [Decidable (x < y)] [DecidableEq α] :
    compareOfLessAndEq x y = .lt ↔ x < y
```

> Batteries features not in core Std

`Std.OrientedCmp.le_iff_ge` (theorem, [line 50](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L50))

```lean
theorem le_iff_ge : cmp x y ≠ .gt ↔ cmp y x ≠ .lt
```

`Std.TransCmp.le_trans` (theorem, [line 58](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L58))

```lean
theorem le_trans : cmp x y ≠ .gt → cmp y z ≠ .gt → cmp x z ≠ .gt
```

`Std.TransCmp.lt_of_lt_of_le` (theorem, [line 61](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L61))

```lean
theorem lt_of_lt_of_le : cmp x y = .lt → cmp y z ≠ .gt → cmp x z = .lt
```

`Std.TransCmp.lt_of_le_of_lt` (theorem, [line 64](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L64))

```lean
theorem lt_of_le_of_lt : cmp x y ≠ .gt → cmp y z = .lt → cmp x z = .lt
```

`Std.TransCmp.ge_trans` (theorem, [line 67](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L67))

```lean
theorem ge_trans : cmp x y ≠ .lt → cmp y z ≠ .lt → cmp x z ≠ .lt
```

`Std.TransCmp.gt_of_gt_of_ge` (theorem, [line 70](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L70))

```lean
theorem gt_of_gt_of_ge : cmp x y = .gt → cmp y z ≠ .lt → cmp x z = .gt
```

`Std.TransCmp.gt_of_ge_of_gt` (theorem, [line 73](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L73))

```lean
theorem gt_of_ge_of_gt : cmp x y ≠ .lt → cmp y z = .gt → cmp x z = .gt
```

`Std.LawfulLTCmp` (class, [line 79](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L79))

> `LawfulLTCmp cmp` asserts that `cmp x y = .lt` and `x < y` coincide.

```lean
class LawfulLTCmp [LT α] (cmp : α → α → Ordering) : Prop extends OrientedCmp cmp where
  /-- `cmp x y = .lt` holds iff `x < y` is true. -/
  eq_lt_iff_lt : cmp x y = .lt ↔ x < y
```

`Std.LawfulLTCmp.eq_gt_iff_gt` (theorem, [line 83](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L83))

```lean
theorem LawfulLTCmp.eq_gt_iff_gt [LT α] [LawfulLTCmp (α := α) cmp] :
    cmp x y = .gt ↔ y < x
```

`Std.LawfulLECmp` (class, [line 87](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L87))

> `LawfulLECmp cmp` asserts that `(cmp x y).isLE` and `x ≤ y` coincide.

```lean
class LawfulLECmp [LE α] (cmp : α → α → Ordering) : Prop extends OrientedCmp cmp where
  /-- `cmp x y ≠ .gt` holds iff `x ≤ y` is true. -/
  isLE_iff_le : (cmp x y).isLE ↔ x ≤ y
```

`Std.LawfulLECmp.isGE_iff_ge` (theorem, [line 91](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L91))

```lean
theorem LawfulLECmp.isGE_iff_ge [LE α] [LawfulLECmp (α := α) cmp] :
    (cmp x y).isGE ↔ y ≤ x
```

`Std.LawfulLECmp.ne_gt_iff_le` (theorem, [line 94](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L94))

```lean
theorem LawfulLECmp.ne_gt_iff_le [LE α] [LawfulLECmp (α := α) cmp] :
    cmp x y ≠ .gt ↔ x ≤ y
```

`Std.LawfulLECmp.ne_lt_iff_ge` (theorem, [line 97](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L97))

```lean
theorem LawfulLECmp.ne_lt_iff_ge [LE α] [LawfulLECmp (α := α) cmp] :
    cmp x y ≠ .lt ↔ y ≤ x
```

`Std.LawfulBCmp` (class, [line 102](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L102))

> `LawfulBCmp cmp` asserts that the `LE`, `LT`, `BEq` are all coherent with each other
> and with `cmp`, describing a strict weak order (a linear order except for antisymmetry).

```lean
class LawfulBCmp [LE α] [LT α] [BEq α] (cmp : α → α → Ordering) : Prop extends
  TransCmp cmp, LawfulBEqCmp cmp, LawfulLTCmp cmp, LawfulLECmp cmp
```

`Std.LawfulCmp` (class, [line 107](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L107))

> `LawfulBCmp cmp` asserts that the `LE`, `LT`, `Eq` are all coherent with each other
> and with `cmp`, describing a linear order.

```lean
class LawfulCmp [LE α] [LT α] (cmp : α → α → Ordering) : Prop extends
  TransCmp cmp, LawfulEqCmp cmp, LawfulLTCmp cmp, LawfulLECmp cmp
```

`Std.LawfulLTOrd` (abbreviation, [line 111](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L111))

> Class for types where the ordering function is compatible with the `LT`.

```lean
abbrev LawfulLTOrd (α) [LT α] [Ord α]
```

`Std.LawfulLEOrd` (abbreviation, [line 114](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L114))

> Class for types where the ordering function is compatible with the `LE`.

```lean
abbrev LawfulLEOrd (α) [LE α] [Ord α]
```

`Std.LawfulBOrd` (abbreviation, [line 117](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L117))

> Class for types where the ordering function is compatible with the `LE`, `LT` and `BEq`.

```lean
abbrev LawfulBOrd (α) [LE α] [LT α] [BEq α] [Ord α]
```

`Std.LawfulOrd` (abbreviation, [line 120](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L120))

> Class for types where the ordering function is compatible with the `LE`, `LT` and `Eq`.

```lean
abbrev LawfulOrd (α) [LE α] [LT α] [Ord α]
```

`Std.OrientedOrd.instOn` (theorem, [line 150](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L150))

```lean
theorem OrientedOrd.instOn [ord : Ord β] [OrientedOrd β] (f : α → β) : @OrientedOrd _ (ord.on f)
```

`Std.TransOrd.instOn` (theorem, [line 153](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L153))

```lean
theorem TransOrd.instOn [ord : Ord β] [TransOrd β] (f : α → β) : @TransOrd _ (ord.on f)
```

`Std.OrientedOrd.instOrdLex'` (theorem, [line 156](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L156))

```lean
theorem OrientedOrd.instOrdLex' (ord₁ ord₂ : Ord α) [@OrientedOrd _ ord₁] [@OrientedOrd _ ord₂] :
    @OrientedOrd _ (ord₁.lex' ord₂)
```

`Std.TransOrd.instOrdLex'` (theorem, [line 160](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L160))

```lean
theorem TransOrd.instOrdLex' (ord₁ ord₂ : Ord α) [@TransOrd _ ord₁] [@TransOrd _ ord₂] :
    @TransOrd _ (ord₁.lex' ord₂)
```

`Std.LawfulLTCmp.eq_compareOfLessAndEq` (theorem, [line 164](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L164))

```lean
theorem LawfulLTCmp.eq_compareOfLessAndEq
    [LT α] [DecidableEq α] [LawfulEqCmp cmp] [LawfulLTCmp cmp]
    (x y : α) [Decidable (x < y)] : cmp x y = compareOfLessAndEq x y
```

`Std.ReflCmp.compareOfLessAndEq_of_lt_irrefl` (theorem, [line 176](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L176))

```lean
theorem ReflCmp.compareOfLessAndEq_of_lt_irrefl [LT α] [DecidableLT α] [DecidableEq α]
    (lt_irrefl : ∀ x : α, ¬ x < x) :
    ReflCmp (α := α) (compareOfLessAndEq · ·)
```

`Std.LawfulBEqCmp.compareOfLessAndEq_of_lt_irrefl` (theorem, [line 181](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L181))

```lean
theorem LawfulBEqCmp.compareOfLessAndEq_of_lt_irrefl
    [LT α] [DecidableLT α] [DecidableEq α] [BEq α] [LawfulBEq α]
    (lt_irrefl : ∀ x : α, ¬x < x) :
    LawfulBEqCmp (α := α) (compareOfLessAndEq · ·)
```

`Std.TransCmp.compareOfLessAndEq_of_irrefl_of_trans_of_antisymm` (theorem, [line 191](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L191))

```lean
theorem TransCmp.compareOfLessAndEq_of_irrefl_of_trans_of_antisymm
    [LT α] [DecidableLT α] [DecidableEq α]
    (lt_irrefl : ∀ x : α, ¬x < x)
    (lt_trans : ∀ {x y z : α}, x < y → y < z → x < z)
    (lt_antisymm : ∀ {x y : α}, ¬x < y → ¬y < x → x = y) :
    TransCmp (α := α) (compareOfLessAndEq · ·)
```

`Std.TransCmp.compareOfLessAndEq_of_irrefl_of_trans_of_not_lt_of_antisymm` (theorem, [line 212](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L212))

```lean
theorem TransCmp.compareOfLessAndEq_of_irrefl_of_trans_of_not_lt_of_antisymm
    [LT α] [LE α] [DecidableLT α] [DecidableEq α]
    (lt_irrefl : ∀ x : α, ¬x < x)
    (lt_trans : ∀ {x y z : α}, x < y → y < z → x < z)
    (not_lt : ∀ {x y : α}, ¬x < y → y ≤ x)
    (le_antisymm : ∀ {x y : α}, x ≤ y → y ≤ x → x = y) :
    TransCmp (α := α) (compareOfLessAndEq · ·)
```

`Std.LawfulLTCmp.compareOfLessAndEq_of_irrefl_of_trans_of_antisymm` (theorem, [line 223](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L223))

```lean
theorem LawfulLTCmp.compareOfLessAndEq_of_irrefl_of_trans_of_antisymm
    [LT α] [DecidableLT α] [DecidableEq α]
    (lt_irrefl : ∀ x : α, ¬x < x)
    (lt_trans : ∀ {x y z : α}, x < y → y < z → x < z)
    (lt_antisymm : ∀ {x y : α}, ¬x < y → ¬y < x → x = y) :
    LawfulLTCmp (α := α) (compareOfLessAndEq · ·)
```

`Std.LawfulLTCmp.compareOfLessAndEq_of_irrefl_of_trans_of_not_lt_of_antisymm` (theorem, [line 234](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L234))

```lean
theorem LawfulLTCmp.compareOfLessAndEq_of_irrefl_of_trans_of_not_lt_of_antisymm
    [LT α] [DecidableLT α] [DecidableEq α] [LE α]
    (lt_irrefl : ∀ x : α, ¬x < x)
    (lt_trans : ∀ {x y z : α}, x < y → y < z → x < z)
    (not_lt : ∀ {x y : α}, ¬x < y → y ≤ x)
    (le_antisymm : ∀ {x y : α}, x ≤ y → y ≤ x → x = y) :
    LawfulLTCmp (α := α) (compareOfLessAndEq · ·)
```

`Std.LawfulLECmp.compareOfLessAndEq_of_irrefl_of_trans_of_not_lt_of_antisymm` (theorem, [line 246](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L246))

```lean
theorem LawfulLECmp.compareOfLessAndEq_of_irrefl_of_trans_of_not_lt_of_antisymm
    [LT α] [DecidableLT α] [DecidableEq α] [LE α]
    (lt_irrefl : ∀ x : α, ¬x < x)
    (lt_trans : ∀ {x y z : α}, x < y → y < z → x < z)
    (not_lt : ∀ {x y : α}, ¬x < y ↔ y ≤ x)
    (le_antisymm : ∀ {x y : α}, x ≤ y → y ≤ x → x = y) :
    LawfulLECmp (α := α) (compareOfLessAndEq · ·)
```

`Std.LawfulCmp.compareOfLessAndEq_of_irrefl_of_trans_of_not_lt_of_antisymm` (theorem, [line 262](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean#L262))

```lean
theorem LawfulCmp.compareOfLessAndEq_of_irrefl_of_trans_of_not_lt_of_antisymm
    [LT α] [LE α] [DecidableLT α] [DecidableEq α]
    (lt_irrefl : ∀ x : α, ¬x < x)
    (lt_trans : ∀ {x y z : α}, x < y → y < z → x < z)
    (not_lt : ∀ {x y : α}, ¬x < y ↔ y ≤ x)
    (le_antisymm : ∀ {x y : α}, x ≤ y → y ≤ x → x = y) :
    LawfulCmp (α := α) (compareOfLessAndEq · ·)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Classes/Order.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Classes/Order.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Classes.Order.json)
