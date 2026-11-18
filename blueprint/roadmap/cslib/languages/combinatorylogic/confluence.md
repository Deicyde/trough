---
catalog: module
lean: Cslib.SKI.ParallelReduction, Cslib.SKI.ParallelReduction.le_reflTransGen_red, Cslib.SKI.Red.le_parallelReduction, Cslib.SKI.reflTransGen_parallelReduction_mRed, Cslib.SKI.I_irreducible, Cslib.SKI.K_irreducible, Cslib.SKI.Ka_irreducible, Cslib.SKI.S_irreducible, Cslib.SKI.Sa_irreducible, Cslib.SKI.Sab_irreducible, Cslib.SKI.parallelReduction_diamond, Cslib.SKI.join_parallelReduction_equivalence, Cslib.SKI.join_mRed_equivalence, Cslib.SKI.MRed.diamond
statement: formalized
proof: formalized
---

# SKI reduction is confluent

`Cslib.Languages.CombinatoryLogic.Confluence`, in [Cslib/Languages/CombinatoryLogic/Confluence.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Confluence.lean), by Thomas Waring.

> This file proves the **Church-Rosser** theorem for the SKI calculus, that is, if `a ↠ b` and
> `a ↠ c`, `b ↠ d` and `c ↠ d` for some term `d`. More strongly (though equivalently), we show
> that the relation of having a common reduct is transitive — in the above situation, `a` and `b`,
> and `a` and `c` have common reducts, so the result implies the same of `b` and `c`. Note that
> `Join (ReflTransGen Red)` is symmetric (trivially) and reflexive (since `↠` is), so we in fact show
> that `Join (ReflTransGen Red)` is an equivalence.
>
> Our proof
> follows the method of Tait and Martin-Löf for the lambda calculus, as presented for instance in
> Chapter 4 of Peter Selinger's notes:
> <https://www.mscs.dal.ca/~selinger/papers/papers/lambdanotes.pdf>.
>
> ## Main definitions
>
> - `ParallelReduction` : a relation `⭢ₚ` on terms such that `⭢ ⊆ ⭢ₚ ⊆ ↠`, allowing simultaneous
> reduction on the head and tail of a term.
>
> ## Main results
>
> - `parallelReduction_diamond` : parallel reduction satisfies the diamond property, that is, it is
> confluent in a single step.
> - `join_mRed_equivalence` : by a general result, the diamond property for `⭢ₚ` implies the same
> for its reflexive-transitive closure. This closure is exactly `↠`, which implies the
> **Church-Rosser** theorem as sketched above.

`Cslib.SKI.ParallelReduction` (inductive type, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Confluence.lean#L51))

> A reduction step allowing simultaneous reduction of disjoint redexes

```lean
inductive ParallelReduction : SKI → SKI → Prop
  /-- Parallel reduction is reflexive, -/
  | refl (a : SKI) : ParallelReduction a a
  /-- Contains `Red`, -/
  | red_I (a : SKI) : ParallelReduction (I ⬝ a) a
  | red_K (a b : SKI) : ParallelReduction (K ⬝ a ⬝ b) a
  | red_S (a b c : SKI) : ParallelReduction (S ⬝ a ⬝ b ⬝ c) (a ⬝ c ⬝ (b ⬝ c))
  /-- and allows simultaneous reduction of disjoint redexes. -/
  | par ⦃a a' b b' : SKI⦄ :
      ParallelReduction a a' → ParallelReduction b b' → ParallelReduction (a ⬝ b) (a' ⬝ b')
```

`Cslib.SKI.ParallelReduction.le_reflTransGen_red` (theorem, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Confluence.lean#L63))

> The inclusion `(· ⭢ₚ ·) ≤ (· ↠ ·)`.

```lean
theorem ParallelReduction.le_reflTransGen_red :
    (· ⭢ₚ ·) ≤ (· ↠ ·)
```

`Cslib.SKI.Red.le_parallelReduction` (theorem, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Confluence.lean#L77))

> The inclusion `(· ⭢ ·) ≤ (· ⭢ₚ ·)`.

```lean
theorem Red.le_parallelReduction :
    (· ⭢ ·) ≤ (· ⭢ₚ ·)
```

`Cslib.SKI.reflTransGen_parallelReduction_mRed` (theorem, [line 94](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Confluence.lean#L94))

> The relations `⭢` and `⭢ₚ` have the same reflexive-transitive closure.

```lean
theorem reflTransGen_parallelReduction_mRed :
    ReflTransGen ParallelReduction = ReflTransGen Red
```

> Irreducibility for the (partially applied) primitive combinators.
>
> …

`Cslib.SKI.I_irreducible` (lemma, [line 106](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Confluence.lean#L106))

```lean
lemma I_irreducible (a : SKI) (h : I ⭢ₚ a) : a = I
```

`Cslib.SKI.K_irreducible` (lemma, [line 110](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Confluence.lean#L110))

```lean
lemma K_irreducible (a : SKI) (h : K ⭢ₚ a) : a = K
```

`Cslib.SKI.Ka_irreducible` (lemma, [line 114](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Confluence.lean#L114))

```lean
lemma Ka_irreducible (a c : SKI) (h : (K ⬝ a) ⭢ₚ c) : ∃ a', a ⭢ₚ a' ∧ c = K ⬝ a'
```

`Cslib.SKI.S_irreducible` (lemma, [line 119](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Confluence.lean#L119))

```lean
lemma S_irreducible (a : SKI) (h : S ⭢ₚ a) : a = S
```

`Cslib.SKI.Sa_irreducible` (lemma, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Confluence.lean#L123))

```lean
lemma Sa_irreducible (a c : SKI) (h : (S ⬝ a) ⭢ₚ c) : ∃ a', a ⭢ₚ a' ∧ c = S ⬝ a'
```

`Cslib.SKI.Sab_irreducible` (lemma, [line 129](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Confluence.lean#L129))

```lean
lemma Sab_irreducible (a b c : SKI) (h : (S ⬝ a ⬝ b) ⭢ₚ c) :
    ∃ a' b', a ⭢ₚ a' ∧ b ⭢ₚ b' ∧ c = S ⬝ a' ⬝ b'
```

`Cslib.SKI.parallelReduction_diamond` (theorem, [line 142](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Confluence.lean#L142))

> The key result: the Church-Rosser property holds for `⭢ₚ`. The proof is a lengthy case analysis
> on the reductions `a ⭢ₚ a₁` and `a ⭢ₚ a₂`, but is entirely mechanical.

```lean
theorem parallelReduction_diamond : Diamond ParallelReduction
```

`Cslib.SKI.join_parallelReduction_equivalence` (theorem, [line 207](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Confluence.lean#L207))

```lean
theorem join_parallelReduction_equivalence :
    Equivalence (Join (ReflTransGen ParallelReduction))
```

`Cslib.SKI.join_mRed_equivalence` (theorem, [line 212](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Confluence.lean#L212))

> The **Church-Rosser** theorem in its general form.

```lean
theorem join_mRed_equivalence : Equivalence (Join (ReflTransGen Red))
```

`Cslib.SKI.MRed.diamond` (theorem, [line 217](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Confluence.lean#L217))

> The **Church-Rosser** theorem in the form it is usually stated.

```lean
theorem MRed.diamond : Confluent Red
```

## Depends on

- [Relations: Definitions](../../foundations/relation/defs.md)
- [SKI Combinatory Logic](defs.md)

## Proof depends on

- [Relations: Confluence](../../foundations/relation/confluence.md)

## Sources

- [Cslib/Languages/CombinatoryLogic/Confluence.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Confluence.lean)
