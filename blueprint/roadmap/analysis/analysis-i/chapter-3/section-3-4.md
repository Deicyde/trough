---
declaration: abbrev
origin: cited
lean: Chapter3.SetTheory.Set.image, Chapter3.SetTheory.Set.mem_image, Chapter3.f_3_4_2, Chapter3.SetTheory.Set.preimage, Chapter3.SetTheory.Set.preimage_f_3_4_2, Chapter3.SetTheory.Set.powerset_axiom, Chapter3.f_3_4_9_a, Chapter3.SetTheory.Set.powerset, Chapter3.SetTheory.Set.mem_powerset, Chapter3.SetTheory.Set.exists_powerset, Chapter3.SetTheory.Set.powerset_of_triple, Chapter3.SetTheory.Set.union_axiom, Chapter3.SetTheory.Set.example_3_4_12, Chapter3.SetTheory.Set.preimage_eq_image_of_inv, Chapter3.SetTheory.Set.image_of_inter, Chapter3.SetTheory.Set.preimage_of_inter, Chapter3.SetTheory.Set.image_preimage_of_surj, Chapter3.SetTheory.Set.preimage_image_of_inj, Chapter3.SetTheory.Set.partial_functions, Chapter3.SetTheory.Set.union_pair_exists, Chapter3.SetTheory.Set.iInter'_insensitive, Chapter3.SetTheory.Set.union_iUnion, Chapter3.SetTheory.Set.union_of_nonempty, Chapter3.SetTheory.Set.inter_iInter, Chapter3.SetTheory.Set.compl_iUnion, Chapter3.SetTheory.Set.compl_iInter
statement: formalized
---

# Section 3.4: Images and inverse images

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Images and inverse images of (Mathlib) functions, within the framework of Section 3.1 set
>   theory. (The Section 3.3 functions are now deprecated and will not be used further.)
> - Connection with Mathlib's image `f '' S` and preimage `f ⁻¹' S` notions.
>
> ## Tips from past users
>
> Users of the companion who have completed the exercises in this section are welcome to send their tips for future users in this section as PRs.
>
> - (Add tip here)

*Quoted from [Analysis/Section_3_4.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 22 labelled items, carried by 28 declarations: 8 proved here, 15 stated without proof (14 of them exercises) and 5 definitions (1 with a value left as `sorry`). It also has 38 declarations and 1 example with no label, counted here but not shown.

## Definition 3.4.1

`Chapter3.SetTheory.Set.image` (abbrev, [line 34](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L34)). A definition.

> Definition 3.4.1.  Interestingly, the definition does not require `S` to be a subset of `X`.

```lean
abbrev SetTheory.Set.image {X Y:Set} (f:X → Y) (S: Set) : Set
```

`Chapter3.SetTheory.Set.mem_image` (theorem, [line 38](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L38)). Proved here.

> Definition 3.4.1

```lean
theorem SetTheory.Set.mem_image {X Y:Set} (f:X → Y) (S: Set) (y:Object) :
    y ∈ image f S ↔ ∃ x:X, x.val ∈ S ∧ f x = y
```

## Example 3.4.2

`Chapter3.f_3_4_2` (abbrev, [line 58](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L58)). A definition.

> Example 3.4.2

```lean
abbrev f_3_4_2 : nat → nat
```

## Example 3.4.3

An `example` ([line 68](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L68)). Proved here.

> Example 3.4.3 is written using Mathlib's notion of image.

```lean
example : (fun n:ℤ ↦ n^2) '' {-1,0,1,2} = {0,1,4}
```

## Definition 3.4.4

`Chapter3.SetTheory.Set.preimage` (abbrev, [line 80](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L80)). A definition.

> Definition 3.4.4 (inverse images).
> Again, it is not required that `U` be a subset of `Y`.

```lean
abbrev SetTheory.Set.preimage {X Y:Set} (f:X → Y) (U: Set) : Set
```

## Example 3.4.6

`Chapter3.SetTheory.Set.preimage_f_3_4_2` (theorem, [line 106](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L106)). Proved here.

> Example 3.4.6

```lean
theorem SetTheory.Set.preimage_f_3_4_2 : preimage f_3_4_2 {2,4,6} = {1,2,3}
```

## Example 3.4.7

An `example` ([line 116](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L116)). Proved here.

> Example 3.4.7 (using the Mathlib notion of preimage)

```lean
example : (fun n:ℤ ↦ n^2) ⁻¹' {0,1,4} = {-2,-1,0,1,2}
```

## Axiom 3.11

`Chapter3.SetTheory.Set.powerset_axiom` (theorem, [line 141](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L141)). Proved here.

> Axiom 3.11 (Power set axiom)

```lean
theorem SetTheory.Set.powerset_axiom {X Y:Set} (F:Object) :
    F ∈ (X ^ Y) ↔ ∃ f: Y → X, f = F
```

## Example 3.4.9

`Chapter3.f_3_4_9_a` (abbrev, [line 145](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L145)). A definition.

> Example 3.4.9

```lean
abbrev f_3_4_9_a : ({4,7}:Set) → ({0,1}:Set)
```

## Exercise 3.4.6 (i)

`Chapter3.SetTheory.Set.powerset` (def, [line 171](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L171)). A definition whose value is left as `sorry`.

> Exercise 3.4.6 (i). One needs to provide a suitable definition of the power set here.

```lean
def SetTheory.Set.powerset (X:Set) : Set
```

`Chapter3.SetTheory.Set.mem_powerset` (theorem, [line 177](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L177)). An exercise, stated without proof.

> Exercise 3.4.6 (i)

```lean
theorem SetTheory.Set.mem_powerset {X:Set} (x:Object) :
    x ∈ powerset X ↔ ∃ Y:Set, x = Y ∧ Y ⊆ X
```

## Lemma 3.4.10

`Chapter3.SetTheory.Set.exists_powerset` (theorem, [line 181](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L181)). Proved here.

> Lemma 3.4.10

```lean
theorem SetTheory.Set.exists_powerset (X:Set) :
   ∃ (Z: Set), ∀ x, x ∈ Z ↔ ∃ Y:Set, x = Y ∧ Y ⊆ X
```

## Remark 3.4.11

`Chapter3.SetTheory.Set.powerset_of_triple` (theorem, [line 188](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L188)). Proved here.

> Remark 3.4.11

```lean
theorem SetTheory.Set.powerset_of_triple (a b c x:Object) :
    x ∈ powerset {a,b,c}
    ↔ x = (∅:Set)
    ∨ x = ({a}:Set)
    ∨ x = ({b}:Set)
    ∨ x = ({c}:Set)
    ∨ x = ({a,b}:Set)
    ∨ x = ({a,c}:Set)
    ∨ x = ({b,c}:Set)
    ∨ x = ({a,b,c}:Set)
```

## Axiom 3.12

`Chapter3.SetTheory.Set.union_axiom` (theorem, [line 212](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L212)). Proved here.

> Axiom 3.12 (Union)

```lean
theorem SetTheory.Set.union_axiom (A: Set) (x:Object) :
    x ∈ union A ↔ ∃ (S:Set), x ∈ S ∧ (S:Object) ∈ A
```

## Example 3.4.12

`Chapter3.SetTheory.Set.example_3_4_12` (theorem, [line 216](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L216)). Stated without proof.

> Example 3.4.12

```lean
theorem SetTheory.Set.example_3_4_12 :
    union { (({2,3}:Set):Object), (({3,4}:Set):Object), (({4,5}:Set):Object) } = {2,3,4,5}
```

## Exercise 3.4.1

`Chapter3.SetTheory.Set.preimage_eq_image_of_inv` (theorem, [line 267](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L267)). An exercise, stated without proof.

> Exercise 3.4.1

```lean
theorem SetTheory.Set.preimage_eq_image_of_inv {X Y V:Set} (f:X → Y) (f_inv: Y → X)
  (hf: Function.LeftInverse f_inv f ∧ Function.RightInverse f_inv f) (hV: V ⊆ Y) :
    image f_inv V = preimage f V
```

## Exercise 3.4.3

`Chapter3.SetTheory.Set.image_of_inter` (theorem, [line 285](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L285)). An exercise, stated without proof.

> Exercise 3.4.3.

```lean
theorem SetTheory.Set.image_of_inter {X Y:Set} (f:X → Y) (A B: Set) :
    image f (A ∩ B) ⊆ (image f A) ∩ (image f B)
```

## Exercise 3.4.4

`Chapter3.SetTheory.Set.preimage_of_inter` (theorem, [line 303](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L303)). An exercise, stated without proof.

> Exercise 3.4.4

```lean
theorem SetTheory.Set.preimage_of_inter {X Y:Set} (f:X → Y) (A B: Set) :
    preimage f (A ∩ B) = (preimage f A) ∩ (preimage f B)
```

## Exercise 3.4.5

`Chapter3.SetTheory.Set.image_preimage_of_surj` (theorem, [line 313](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L313)). An exercise, stated without proof.

> Exercise 3.4.5 (image of a preimage)

```lean
theorem SetTheory.Set.image_preimage_of_surj {X Y:Set} (f:X → Y) :
    (∀ S, S ⊆ Y → image f (preimage f S) = S) ↔ Function.Surjective f
```

`Chapter3.SetTheory.Set.preimage_image_of_inj` (theorem, [line 317](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L317)). An exercise, stated without proof.

> Exercise 3.4.5 (preimage of an image)

```lean
theorem SetTheory.Set.preimage_image_of_inj {X Y:Set} (f:X → Y) :
    (∀ S, S ⊆ X → preimage f (image f S) = S) ↔ Function.Injective f
```

## Exercise 3.4.7

`Chapter3.SetTheory.Set.partial_functions` (theorem, [line 332](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L332)). An exercise, stated without proof.

> Exercise 3.4.7

```lean
theorem SetTheory.Set.partial_functions {X Y:Set} :
    ∃ Z:Set, ∀ F:Object, F ∈ Z ↔ ∃ X' Y':Set, X' ⊆ X ∧ Y' ⊆ Y ∧ ∃ f: X' → Y', F = f
```

## Exercise 3.4.8

`Chapter3.SetTheory.Set.union_pair_exists` (theorem, [line 340](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L340)). An exercise, stated without proof.

> Exercise 3.4.8.  The point of this exercise is to prove it without using the
> pairwise union operation `∪`.

```lean
theorem SetTheory.Set.union_pair_exists (X Y:Set) : ∃ Z:Set, ∀ x, x ∈ Z ↔ (x ∈ X ∨ x ∈ Y)
```

## Exercise 3.4.9

`Chapter3.SetTheory.Set.iInter'_insensitive` (theorem, [line 344](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L344)). An exercise, stated without proof.

> Exercise 3.4.9

```lean
theorem SetTheory.Set.iInter'_insensitive {I:Set} (β β':I) (A: I → Set) :
    iInter' I β A = iInter' I β' A
```

## Exercise 3.4.10

`Chapter3.SetTheory.Set.union_iUnion` (theorem, [line 348](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L348)). An exercise, stated without proof.

> Exercise 3.4.10 (union over a union of index sets)

```lean
theorem SetTheory.Set.union_iUnion {I J:Set} (A: (I ∪ J:Set) → Set) :
    iUnion I (fun α ↦ A ⟨ α.val, by simp [α.property]⟩)
    ∪ iUnion J (fun α ↦ A ⟨ α.val, by simp [α.property]⟩)
    = iUnion (I ∪ J) A
```

`Chapter3.SetTheory.Set.union_of_nonempty` (theorem, [line 354](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L354)). An exercise, stated without proof.

> Exercise 3.4.10 (a union of nonempty index sets is nonempty)

```lean
theorem SetTheory.Set.union_of_nonempty {I J:Set} (hI: I ≠ ∅) (hJ: J ≠ ∅) : I ∪ J ≠ ∅
```

`Chapter3.SetTheory.Set.inter_iInter` (theorem, [line 357](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L357)). An exercise, stated without proof.

> Exercise 3.4.10 (intersection over a union of index sets)

```lean
theorem SetTheory.Set.inter_iInter {I J:Set} (hI: I ≠ ∅) (hJ: J ≠ ∅) (A: (I ∪ J:Set) → Set) :
    iInter I hI (fun α ↦ A ⟨ α.val, by simp [α.property]⟩)
    ∩ iInter J hJ (fun α ↦ A ⟨ α.val, by simp [α.property]⟩)
    = iInter (I ∪ J) (union_of_nonempty hI hJ) A
```

## Exercise 3.4.11

`Chapter3.SetTheory.Set.compl_iUnion` (theorem, [line 363](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L363)). An exercise, stated without proof.

> Exercise 3.4.11 (complement of a union)

```lean
theorem SetTheory.Set.compl_iUnion {X I: Set} (hI: I ≠ ∅) (A: I → Set) :
    X \ iUnion I A = iInter I hI (fun α ↦ X \ A α)
```

`Chapter3.SetTheory.Set.compl_iInter` (theorem, [line 367](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean#L367)). An exercise, stated without proof.

> Exercise 3.4.11 (complement of an intersection)

```lean
theorem SetTheory.Set.compl_iInter {X I: Set} (hI: I ≠ ∅) (A: I → Set) :
    X \ iInter I hI A = iUnion I (fun α ↦ X \ A α)
```

## Depends on

- [Section 3.1: Fundamentals (of set theory)](section-3-1.md)

## Sources

- [Analysis/Section_3_4.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_4.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_3_4/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_3_4.html)
