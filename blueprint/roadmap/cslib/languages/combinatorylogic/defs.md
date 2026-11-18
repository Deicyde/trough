---
catalog: module
lean: Cslib.SKI, Cslib.SKI.applyList, Cslib.SKI.applyList_concat, Cslib.SKI.size, Cslib.SKI.Red, Cslib.SKI.Red.ne, Cslib.SKI.MRed.S, Cslib.SKI.MRed.K, Cslib.SKI.MRed.I, Cslib.SKI.MRed.head, Cslib.SKI.MRed.tail, Cslib.SKI.parallel_mRed, Cslib.SKI.parallel_red, Cslib.SKI.join_mRed_head, Cslib.SKI.mJoin_red_head, Cslib.SKI.join_mRed_tail, Cslib.SKI.mJoin_red_tail
statement: formalized
proof: formalized
---

# SKI Combinatory Logic

`Cslib.Languages.CombinatoryLogic.Defs`, in [Cslib/Languages/CombinatoryLogic/Defs.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Defs.lean), by Thomas Waring.

> This file defines the syntax and operational semantics (reduction rules) of combinatory logic,
> using the SKI basis.
>
> ## Main definitions
>
> - `SKI`: the type of expressions in the SKI calculus,
> - `Red`: single-step reduction of SKI expressions,
> - `MRed`: multi-step reduction of SKI expressions.
>
> ## Notation
>
> - `⬝` : application between SKI terms,
> - `⭢` : single-step reduction,
> - `↠` : multi-step reduction,
>
> ## References
>
> The setup of SKI combinatory logic is standard, see for example:
> - <https://en.m.wikipedia.org/wiki/SKI_combinator_calculus>
> - <https://en.m.wikipedia.org/wiki/Combinatory_logic>

`Cslib.SKI` (inductive type, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Defs.lean#L43))

> An SKI expression is built from the primitive combinators `S`, `K` and `I`, and application.

```lean
inductive SKI where
  /-- `S`-combinator, with semantics $λxyz.xz(yz)$ -/
  | S
  /-- `K`-combinator, with semantics $λxy.x$ -/
  | K
  /-- `I`-combinator, with semantics $λx.x$ -/
  | I
  /-- Application $x y ↦ xy$ -/
  | app : SKI → SKI → SKI
deriving Repr, DecidableEq
```

`Cslib.SKI.applyList` (definition, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Defs.lean#L60))

> Apply a term to a list of terms

```lean
def applyList (f : SKI) (xs : List SKI) : SKI
```

`Cslib.SKI.applyList_concat` (lemma, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Defs.lean#L62))

```lean
lemma applyList_concat (f : SKI) (ys : List SKI) (z : SKI) :
    f.applyList (ys ++ [z]) = f.applyList ys ⬝ z
```

`Cslib.SKI.size` (definition, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Defs.lean#L67))

> The size of an SKI term is its number of combinators.

```lean
def size : SKI → Nat
```

> ### Reduction relations between SKI terms

`Cslib.SKI.Red` (inductive type, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Defs.lean#L77))

> Single-step reduction of SKI terms

```lean
inductive Red : SKI → SKI → Prop where
  /-- The operational semantics of the `S`, -/
  | red_S (x y z : SKI) : Red (S ⬝ x ⬝ y ⬝ z) (x ⬝ z ⬝ (y ⬝ z))
  /-- `K`, -/
  | red_K (x y : SKI) : Red (K ⬝ x ⬝ y) x
  /-- and `I` combinators. -/
  | red_I (x : SKI) : Red (I ⬝ x) x
  /-- Reduction on the head -/
  | red_head (x x' y : SKI) (_ : Red x x') : Red (x ⬝ y) (x' ⬝ y)
  /-- and tail of an SKI term. -/
  | red_tail (x y y' : SKI) (_ : Red y y') : Red (x ⬝ y) (x ⬝ y')
```

`Cslib.SKI.Red.ne` (lemma, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Defs.lean#L92))

```lean
lemma Red.ne {x y : SKI} : (x ⭢ y) → x ≠ y
```

`Cslib.SKI.MRed.S` (theorem, [line 99](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Defs.lean#L99))

```lean
theorem MRed.S (x y z : SKI) : (S ⬝ x ⬝ y ⬝ z) ↠ (x ⬝ z ⬝ (y ⬝ z))
```

`Cslib.SKI.MRed.K` (theorem, [line 100](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Defs.lean#L100))

```lean
theorem MRed.K (x y : SKI) : (K ⬝ x ⬝ y) ↠ x
```

`Cslib.SKI.MRed.I` (theorem, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Defs.lean#L101))

```lean
theorem MRed.I (x : SKI) : (I ⬝ x) ↠ x
```

`Cslib.SKI.MRed.head` (theorem, [line 103](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Defs.lean#L103))

```lean
theorem MRed.head {a a' : SKI} (b : SKI) (h : a ↠ a') : (a ⬝ b) ↠ (a' ⬝ b)
```

`Cslib.SKI.MRed.tail` (theorem, [line 106](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Defs.lean#L106))

```lean
theorem MRed.tail (a : SKI) {b b' : SKI} (h : b ↠ b') : (a ⬝ b) ↠ (a ⬝ b')
```

`Cslib.SKI.parallel_mRed` (lemma, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Defs.lean#L109))

```lean
lemma parallel_mRed {a a' b b' : SKI} (ha : a ↠ a') (hb : b ↠ b') :
    (a ⬝ b) ↠ (a' ⬝ b')
```

`Cslib.SKI.parallel_red` (lemma, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Defs.lean#L113))

```lean
lemma parallel_red {a a' b b' : SKI} (ha : a ⭢ a') (hb : b ⭢ b') : (a ⬝ b) ↠ (a' ⬝ b')
```

`Cslib.SKI.join_mRed_head` (theorem, [line 116](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Defs.lean#L116))

```lean
theorem join_mRed_head {x x' : SKI} (y : SKI) :
    Join (ReflTransGen Red) x x' → Join (ReflTransGen Red) (x ⬝ y) (x' ⬝ y)
```

`Cslib.SKI.mJoin_red_head` (alias, [line 120](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Defs.lean#L120))

```lean
alias mJoin_red_head
```

`Cslib.SKI.join_mRed_tail` (theorem, [line 122](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Defs.lean#L122))

```lean
theorem join_mRed_tail (x : SKI) {y y' : SKI} :
    Join (ReflTransGen Red) y y' → Join (ReflTransGen Red) (x ⬝ y) (x ⬝ y')
```

`Cslib.SKI.mJoin_red_tail` (alias, [line 126](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Defs.lean#L126))

```lean
alias mJoin_red_tail
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Languages/CombinatoryLogic/Defs.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Defs.lean)
