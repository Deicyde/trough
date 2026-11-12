---
catalog: module
lean: Cslib.SKI.RedexFree, Cslib.SKI.evalStep, Cslib.SKI.evalStep_right_correct, Cslib.SKI.redexFree_of_normal_red, Cslib.SKI.RedexFree.normal_red, Cslib.SKI.redexFree_iff, Cslib.SKI.redexFree_iff_evalStep, Cslib.SKI.redexFree_iff_mred_eq, Cslib.SKI.join_mRed_redexFree, Cslib.SKI.mJoin_red_redexFree, Cslib.SKI.confluent_redexFree, Cslib.SKI.unique_normal_form, Cslib.SKI.eq_of_join_mRed_redexFree, Cslib.SKI.eq_of_mJoin_red_redexFree, Cslib.SKI.sk_nequiv, Cslib.SKI.isBool_injective, Cslib.SKI.TF_nequiv, Cslib.SKI.churchK, Cslib.SKI.churchK_church, Cslib.SKI.churchK_redexFree, Cslib.SKI.churchK_size, Cslib.SKI.churchK_injective, Cslib.SKI.isChurch_injective, Cslib.SKI.rice, Cslib.SKI.rice'
statement: formalized
proof: formalized
---

# Evaluation results

`Cslib.Languages.CombinatoryLogic.Evaluation`, in [Cslib/Languages/CombinatoryLogic/Evaluation.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean), by Thomas Waring.

> This file formalises evaluation and normal forms of SKI terms.
>
> ## Main definitions
>
> - `RedexFree` : a predicate expressing that a term has no redexes
> - `evalStep` : SKI-reduction as a function
>
> ## Main results
>
> - `evalStep_right_correct` : correctness for `evalStep`
> - `redexFree_iff` and `redexFree_iff_mred_eq` : a term is redex free if and only if it has
> (respectively) no one-step reductions, or if its only many step reduction is itself.
> - `unique_normal_form` : if `x` reduces to both `y` and `z`, and both `y` and `z` are in normal
> form, then they are equal.
> - **Rice's theorem**: no SKI term is a non-trivial predicate.
>
> ## References
>
> This file draws heavily from <https://gist.github.com/b-mehta/e412c837818223b8f16ca0b4aa19b166>.

`Cslib.SKI.RedexFree` (definition, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L45))

> The predicate that a term has no reducible sub-terms.

```lean
def RedexFree : SKI → Prop
```

`Cslib.SKI.evalStep` (definition, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L64))

> One-step evaluation as a function: either it returns a term that has been reduced by one step,
> or a proof that the term is redex free. Uses normal-order reduction.

```lean
def evalStep : (x : SKI) → PLift (x.RedexFree) ⊕ SKI
```

`Cslib.SKI.evalStep_right_correct` (theorem, [line 90](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L90))

> The normal-order reduction implemented by `evalStep` indeed computes a one-step reduction.

```lean
theorem evalStep_right_correct : (x y : SKI) → (x.evalStep = Sum.inr y) → x ⭢ y
```

`Cslib.SKI.redexFree_of_normal_red` (theorem, [line 134](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L134))

```lean
theorem redexFree_of_normal_red {x : SKI} (h : Normal Red x) : x.RedexFree
```

`Cslib.SKI.RedexFree.normal_red` (theorem, [line 139](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L139))

```lean
theorem RedexFree.normal_red {x : SKI} (hx : x.RedexFree) : Normal Red x
```

`Cslib.SKI.redexFree_iff` (theorem, [line 151](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L151))

> A term is redex free iff it has no one-step reductions.

```lean
theorem redexFree_iff {x : SKI} : x.RedexFree ↔ Normal Red x
```

`Cslib.SKI.redexFree_iff_evalStep` (theorem, [line 154](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L154))

```lean
theorem redexFree_iff_evalStep {x : SKI} : x.RedexFree ↔ (x.evalStep).isLeft = true
```

`Cslib.SKI.redexFree_iff_mred_eq` (theorem, [line 170](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L170))

> A term is redex free iff its only many-step reduction is itself.

```lean
theorem redexFree_iff_mred_eq {x : SKI} : x.RedexFree ↔ ∀ y, (x ↠ y) ↔ x = y
```

`Cslib.SKI.join_mRed_redexFree` (theorem, [line 181](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L181))

> If a term has a common reduct with a normal term, it in fact reduces to that term.

```lean
theorem join_mRed_redexFree {x y : SKI} (hy : y.RedexFree) (h : Join (ReflTransGen Red) x y) :
    x ↠ y
```

`Cslib.SKI.mJoin_red_redexFree` (alias, [line 186](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L186))

```lean
alias mJoin_red_redexFree
```

`Cslib.SKI.confluent_redexFree` (lemma, [line 189](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L189))

> If `x` reduces to both `y` and `z`, and `z` is not reducible, then `y` reduces to `z`.

```lean
lemma confluent_redexFree {x y z : SKI} (hxy : x ↠ y) (hxz : x ↠ z) (hz : RedexFree z) : y ↠ z
```

`Cslib.SKI.unique_normal_form` (lemma, [line 196](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L196))

> If `x` reduces to both `y` and `z`, and both `y` and `z` are in normal form, then they are equal.

```lean
lemma unique_normal_form {x y z : SKI}
    (hxy : x ↠ y) (hxz : x ↠ z) (hy : y.RedexFree) (hz : RedexFree z) : y = z
```

`Cslib.SKI.eq_of_join_mRed_redexFree` (lemma, [line 201](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L201))

> If `x` and `y` are normal and have a common reduct, then they are equal.

```lean
lemma eq_of_join_mRed_redexFree {x y : SKI} (h : Join (ReflTransGen Red) x y)
    (hx : x.RedexFree) (hy : y.RedexFree) : x = y
```

`Cslib.SKI.eq_of_mJoin_red_redexFree` (alias, [line 205](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L205))

```lean
alias eq_of_mJoin_red_redexFree
```

> ### Injectivity for datatypes

`Cslib.SKI.sk_nequiv` (lemma, [line 210](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L210))

```lean
lemma sk_nequiv : ¬ Join (ReflTransGen Red) S K
```

`Cslib.SKI.isBool_injective` (theorem, [line 218](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L218))

> Injectivity for booleans.

```lean
theorem isBool_injective (x y : SKI) (u v : Bool) (hx : IsBool u x) (hy : IsBool v y)
    (hxy : Join (ReflTransGen Red) x y) : u = v
```

`Cslib.SKI.TF_nequiv` (lemma, [line 231](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L231))

```lean
lemma TF_nequiv : ¬ Join (ReflTransGen Red) TT FF
```

`Cslib.SKI.churchK` (definition, [line 235](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L235))

> A specialisation of `Church : Nat → SKI`.

```lean
def churchK : Nat → SKI
```

`Cslib.SKI.churchK_church` (lemma, [line 239](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L239))

```lean
lemma churchK_church : (n : Nat) → churchK n = Church n K K
```

`Cslib.SKI.churchK_redexFree` (lemma, [line 243](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L243))

```lean
lemma churchK_redexFree : (n : Nat) → RedexFree (churchK n)
```

`Cslib.SKI.churchK_size` (lemma, [line 248](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L248))

```lean
lemma churchK_size : (n : Nat) → (churchK n).size = n+1
```

`Cslib.SKI.churchK_injective` (lemma, [line 252](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L252))

```lean
lemma churchK_injective : Function.Injective churchK
```

`Cslib.SKI.isChurch_injective` (theorem, [line 256](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L256))

> Injectivity for Church numerals

```lean
theorem isChurch_injective (x y : SKI) (n m : Nat) (hx : IsChurch n x) (hy : IsChurch m y)
    (hxy : Join (ReflTransGen Red) x y) : n = m
```

`Cslib.SKI.rice` (theorem, [line 278](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L278))

> **Rice's theorem**: no SKI term is a non-trivial predicate.
>
> More specifically, say a term `P` is a *predicate* if, for every term `x`, `P · x` reduces to either
> `TT` or `FF`. A predicate `P` is *trivial* if either it always reduces to true, or always to false.
> This version of Rice's theorem derives a contradiction from the existence of a predicate `P` and the
> existence of terms `x` for which `P · x` is true (`P · x ↠ TT`) and for which `P · x` is false
> (`P · x ↠ FF`).

```lean
theorem rice {P : SKI} (hP : ∀ x : SKI, ((P ⬝ x) ↠ TT) ∨ (P ⬝ x) ↠ FF)
    (hxt : ∃ x : SKI, (P ⬝ x) ↠ TT) (hxf : ∃ x : SKI, (P ⬝ x) ↠ FF) : False
```

`Cslib.SKI.rice'` (theorem, [line 309](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean#L309))

> **Rice's theorem**: any SKI predicate is trivial.
>
> This version of Rice's theorem proves (classically) that any SKI predicate `P` either is constantly
> true (ie `P · x ↠ TT` for every `x`) or is constantly false (`P · x ↠ FF` for every `x`).

```lean
theorem rice' {P : SKI} (hP : ∀ x : SKI, ((P ⬝ x) ↠ TT) ∨ (P ⬝ x) ↠ FF) :
    (∀ x : SKI, (P ⬝ x) ↠ TT) ∨ (∀ x : SKI, (P ⬝ x) ↠ FF)
```

## Depends on

- [Relations: Definitions](../../foundations/relation/defs.md)
- [General recursion in the SKI calculus](recursion.md)

## Proof depends on

- [SKI reduction is confluent](confluence.md)

## Sources

- [Cslib/Languages/CombinatoryLogic/Evaluation.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Evaluation.lean)
