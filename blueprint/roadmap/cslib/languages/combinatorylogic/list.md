---
catalog: module
lean: Cslib.SKI.IsChurchList, Cslib.SKI.isChurchList_trans, Cslib.SKI.IsChurchListPair, Cslib.SKI.isChurchListPair_trans, Cslib.SKI.List.NilPoly, Cslib.SKI.List.Nil, Cslib.SKI.List.nil_def, Cslib.SKI.List.nil_correct, Cslib.SKI.List.ConsPoly, Cslib.SKI.List.Cons, Cslib.SKI.List.cons_def, Cslib.SKI.List.cons_correct, Cslib.SKI.List.singleton_correct, Cslib.SKI.List.toChurch, Cslib.SKI.List.toChurch_nil, Cslib.SKI.List.toChurch_cons, Cslib.SKI.List.toChurch_correct, Cslib.SKI.List.HeadDPoly, Cslib.SKI.List.HeadD, Cslib.SKI.List.headD_def, Cslib.SKI.List.headD_correct, Cslib.SKI.List.Head, Cslib.SKI.List.head_def, Cslib.SKI.List.head_correct, Cslib.SKI.List.TailStepPoly, Cslib.SKI.List.TailStep, Cslib.SKI.List.tailStep_def, Cslib.SKI.List.TailPoly, Cslib.SKI.List.Tail, Cslib.SKI.List.tail_def, Cslib.SKI.List.tail_init, Cslib.SKI.List.tailStep_correct, Cslib.SKI.List.tailFold_correct, Cslib.SKI.List.tail_correct, Cslib.SKI.List.PrependZeroPoly, Cslib.SKI.List.PrependZero, Cslib.SKI.List.prependZero_def, Cslib.SKI.List.prependZero_correct, Cslib.SKI.List.SuccHead, Cslib.SKI.List.succHead_correct
statement: formalized
proof: formalized
---

# Church-Encoded Lists in SKI Combinatory Logic

`Cslib.Languages.CombinatoryLogic.List`, in [Cslib/Languages/CombinatoryLogic/List.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean), by Jesse Alama.

> Church-encoded lists for proving SKI ≃ TM equivalence. A list is encoded as
> `λ c n. c a₀ (c a₁ (... (c aₖ n)...))` where each `aᵢ` is a Church numeral.

> ### Church List Representation

`Cslib.SKI.IsChurchList` (definition, [line 29](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L29))

> A term correctly Church-encodes a list of natural numbers.

```lean
def IsChurchList : List ℕ → SKI → Prop
```

`Cslib.SKI.isChurchList_trans` (theorem, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L36))

> `IsChurchList` is preserved under multi-step reduction of the term.

```lean
theorem isChurchList_trans {ns : List ℕ} {cns cns' : SKI} (h : cns ↠ cns')
    (hcns' : IsChurchList ns cns') : IsChurchList ns cns
```

`Cslib.SKI.IsChurchListPair` (structure, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L48))

> Both components of a pair are Church lists.

```lean
structure IsChurchListPair (prev curr : List ℕ) (p : SKI) : Prop where
  fst : IsChurchList prev (Fst ⬝ p)
  snd : IsChurchList curr (Snd ⬝ p)
```

`Cslib.SKI.isChurchListPair_trans` (theorem, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L54))

> IsChurchListPair is preserved under reduction.

```lean
theorem isChurchListPair_trans {prev curr : List ℕ} {p p' : SKI} (hp : p ↠ p')
    (hp' : IsChurchListPair prev curr p') : IsChurchListPair prev curr p
```

> ### Nil: The empty list

`Cslib.SKI.List.NilPoly` (definition, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L67))

> nil = λ c n. n

```lean
def NilPoly : SKI.Polynomial 2
```

`Cslib.SKI.List.Nil` (definition, [line 70](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L70))

> The SKI term for the empty list.

```lean
def Nil : SKI
```

`Cslib.SKI.List.nil_def` (theorem, [line 73](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L73))

> Reduction: `Nil ⬝ c ⬝ n ↠ n`.

```lean
theorem nil_def (c n : SKI) : (Nil ⬝ c ⬝ n) ↠ n
```

`Cslib.SKI.List.nil_correct` (theorem, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L77))

> The empty list term correctly represents `[]`.

```lean
theorem nil_correct : IsChurchList [] Nil
```

> ### Cons: Consing an element onto a list

`Cslib.SKI.List.ConsPoly` (definition, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L82))

> cons = λ x xs c n. c x (xs c n)

```lean
def ConsPoly : SKI.Polynomial 4
```

`Cslib.SKI.List.Cons` (definition, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L85))

> The SKI term for list cons.

```lean
def Cons : SKI
```

`Cslib.SKI.List.cons_def` (theorem, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L88))

> Reduction: `Cons ⬝ x ⬝ xs ⬝ c ⬝ n ↠ c ⬝ x ⬝ (xs ⬝ c ⬝ n)`.

```lean
theorem cons_def (x xs c n : SKI) :
    (Cons ⬝ x ⬝ xs ⬝ c ⬝ n) ↠ c ⬝ x ⬝ (xs ⬝ c ⬝ n)
```

`Cslib.SKI.List.cons_correct` (theorem, [line 93](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L93))

> Cons preserves Church list representation.

```lean
theorem cons_correct {x : ℕ} {xs : List ℕ} {cx cxs : SKI}
    (hcx : IsChurch x cx) (hcxs : IsChurchList xs cxs) :
    IsChurchList (x :: xs) (Cons ⬝ cx ⬝ cxs)
```

`Cslib.SKI.List.singleton_correct` (theorem, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L101))

> Singleton list correctness.

```lean
theorem singleton_correct {x : ℕ} {cx : SKI} (hcx : IsChurch x cx) :
    IsChurchList [x] (Cons ⬝ cx ⬝ Nil)
```

`Cslib.SKI.List.toChurch` (definition, [line 106](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L106))

> The canonical SKI term for a Church-encoded list.

```lean
def toChurch : List ℕ → SKI
```

`Cslib.SKI.List.toChurch_nil` (lemma, [line 112](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L112))

> `toChurch [] = Nil`.

```lean
lemma toChurch_nil : toChurch [] = Nil
```

`Cslib.SKI.List.toChurch_cons` (lemma, [line 116](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L116))

> `toChurch (x :: xs) = Cons ⬝ SKI.toChurch x ⬝ toChurch xs`.

```lean
lemma toChurch_cons (x : ℕ) (xs : List ℕ) :
    toChurch (x :: xs) = Cons ⬝ (SKI.toChurch x) ⬝ (toChurch xs)
```

`Cslib.SKI.List.toChurch_correct` (theorem, [line 120](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L120))

> `toChurch ns` correctly represents `ns`.

```lean
theorem toChurch_correct (ns : List ℕ) : IsChurchList ns (toChurch ns)
```

> ### Head: Extract the head of a list

`Cslib.SKI.List.HeadDPoly` (definition, [line 128](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L128))

> headD d xs = xs K d (returns d for empty list)

```lean
def HeadDPoly : SKI.Polynomial 2
```

`Cslib.SKI.List.HeadD` (definition, [line 131](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L131))

> The SKI term for list head with default.

```lean
def HeadD : SKI
```

`Cslib.SKI.List.headD_def` (theorem, [line 134](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L134))

> Reduction: `HeadD ⬝ d ⬝ xs ↠ xs ⬝ K ⬝ d`.

```lean
theorem headD_def (d xs : SKI) : (HeadD ⬝ d ⬝ xs) ↠ xs ⬝ K ⬝ d
```

`Cslib.SKI.List.headD_correct` (theorem, [line 138](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L138))

> General head-with-default correctness.

```lean
theorem headD_correct {d : ℕ} {cd : SKI} (hcd : IsChurch d cd)
    {ns : List ℕ} {cns : SKI} (hcns : IsChurchList ns cns) :
    IsChurch (ns.headD d) (HeadD ⬝ cd ⬝ cns)
```

`Cslib.SKI.List.Head` (definition, [line 154](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L154))

> The SKI term for list head (default 0).

```lean
def Head : SKI
```

`Cslib.SKI.List.head_def` (theorem, [line 157](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L157))

> Reduction: `Head ⬝ xs ↠ xs ⬝ K ⬝ Zero`.

```lean
theorem head_def (xs : SKI) : (Head ⬝ xs) ↠ xs ⬝ K ⬝ SKI.Zero
```

`Cslib.SKI.List.head_correct` (theorem, [line 161](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L161))

> Head correctness (default 0).

```lean
theorem head_correct (ns : List ℕ) (cns : SKI) (hcns : IsChurchList ns cns) :
    IsChurch (ns.headD 0) (Head ⬝ cns)
```

> ### Tail: Extract the tail of a list

`Cslib.SKI.List.TailStepPoly` (definition, [line 168](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L168))

> Step function for tail: (prev, curr) → (curr, cons h curr)

```lean
def TailStepPoly : SKI.Polynomial 2
```

`Cslib.SKI.List.TailStep` (definition, [line 172](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L172))

> The step function for computing list tail.

```lean
def TailStep : SKI
```

`Cslib.SKI.List.tailStep_def` (theorem, [line 175](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L175))

> Reduction of the tail step function.

```lean
theorem tailStep_def (h p : SKI) :
    (TailStep ⬝ h ⬝ p) ↠ MkPair ⬝ (Snd ⬝ p) ⬝ (Cons ⬝ h ⬝ (Snd ⬝ p))
```

`Cslib.SKI.List.TailPoly` (definition, [line 180](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L180))

> tail xs = Fst (xs TailStep (MkPair Nil Nil))

```lean
def TailPoly : SKI.Polynomial 1
```

`Cslib.SKI.List.Tail` (definition, [line 184](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L184))

> The tail of a Church-encoded list.

```lean
def Tail : SKI
```

`Cslib.SKI.List.tail_def` (theorem, [line 187](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L187))

> Reduction: `Tail ⬝ xs ↠ Fst ⬝ (xs ⬝ TailStep ⬝ (MkPair ⬝ Nil ⬝ Nil))`.

```lean
theorem tail_def (xs : SKI) :
    (Tail ⬝ xs) ↠ Fst ⬝ (xs ⬝ TailStep ⬝ (MkPair ⬝ Nil ⬝ Nil))
```

`Cslib.SKI.List.tail_init` (theorem, [line 193](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L193))

> The initial pair (nil, nil) satisfies the invariant.

```lean
theorem tail_init : IsChurchListPair [] [] (MkPair ⬝ Nil ⬝ Nil)
```

`Cslib.SKI.List.tailStep_correct` (theorem, [line 199](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L199))

> The step function preserves the tail-computing invariant.

```lean
theorem tailStep_correct {x : ℕ} {xs : List ℕ} {cx p : SKI}
    (hcx : IsChurch x cx) (hp : IsChurchListPair xs.tail xs p) :
    IsChurchListPair xs (x :: xs) (TailStep ⬝ cx ⬝ p)
```

`Cslib.SKI.List.tailFold_correct` (theorem, [line 206](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L206))

```lean
theorem tailFold_correct (ns : List ℕ) (cns : SKI) (hcns : IsChurchList ns cns) :
    ∃ p, (cns ⬝ TailStep ⬝ (MkPair ⬝ Nil ⬝ Nil)) ↠ p ∧
         IsChurchListPair ns.tail ns p
```

`Cslib.SKI.List.tail_correct` (theorem, [line 233](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L233))

> Tail correctness.

```lean
theorem tail_correct (ns : List ℕ) (cns : SKI) (hcns : IsChurchList ns cns) :
    IsChurchList ns.tail (Tail ⬝ cns)
```

> ### Prepending zero to a list (for Code.zero')

`Cslib.SKI.List.PrependZeroPoly` (definition, [line 247](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L247))

> PrependZero xs = cons 0 xs = Cons ⬝ Zero ⬝ xs

```lean
def PrependZeroPoly : SKI.Polynomial 1
```

`Cslib.SKI.List.PrependZero` (definition, [line 250](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L250))

> Prepend zero to a Church-encoded list.

```lean
def PrependZero : SKI
```

`Cslib.SKI.List.prependZero_def` (theorem, [line 253](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L253))

> Reduction: `PrependZero ⬝ xs ↠ Cons ⬝ Zero ⬝ xs`.

```lean
theorem prependZero_def (xs : SKI) : (PrependZero ⬝ xs) ↠ Cons ⬝ SKI.Zero ⬝ xs
```

`Cslib.SKI.List.prependZero_correct` (theorem, [line 257](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L257))

> Prepending zero preserves Church list representation.

```lean
theorem prependZero_correct {ns : List ℕ} {cns : SKI} (hcns : IsChurchList ns cns) :
    IsChurchList (0 :: ns) (PrependZero ⬝ cns)
```

> ### Successor on list head (for Code.succ)

`Cslib.SKI.List.SuccHead` (definition, [line 265](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L265))

> SuccHead xs = cons (succ (head xs)) nil

```lean
def SuccHead : SKI
```

`Cslib.SKI.List.succHead_correct` (theorem, [line 268](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean#L268))

> `SuccHead` correctly computes a singleton containing `succ(head ns)`.

```lean
theorem succHead_correct (ns : List ℕ) (cns : SKI) (hcns : IsChurchList ns cns) :
    IsChurchList [ns.headD 0 + 1] (SuccHead ⬝ cns)
```

## Depends on

- [General recursion in the SKI calculus](recursion.md)

## Sources

- [Cslib/Languages/CombinatoryLogic/List.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/List.lean)
