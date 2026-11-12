---
catalog: module
lean: Cslib.SKI.Polynomial, Cslib.SKI.CoeTermPolynomial, Cslib.SKI.Polynomial.eval, Cslib.SKI.Polynomial.varFreeToSKI, Cslib.SKI.Polynomial.elimVar, Cslib.SKI.Polynomial.elimVar_correct, Cslib.SKI.Polynomial.toSKI, Cslib.SKI.Polynomial.toSKI_correct, Cslib.SKI.RPoly, Cslib.SKI.R, Cslib.SKI.R_def, Cslib.SKI.BPoly, Cslib.SKI.B, Cslib.SKI.B_def, Cslib.SKI.B_tail_mred, Cslib.SKI.CPoly, Cslib.SKI.C, Cslib.SKI.C_def, Cslib.SKI.C_head_mred, Cslib.SKI.RotRPoly, Cslib.SKI.RotR, Cslib.SKI.rotR_def, Cslib.SKI.RotLPoly, Cslib.SKI.RotL, Cslib.SKI.rotL_def, Cslib.SKI.DelPoly, Cslib.SKI.Del, Cslib.SKI.del_def, Cslib.SKI.HPoly, Cslib.SKI.H, Cslib.SKI.H_def, Cslib.SKI.YPoly, Cslib.SKI.Y, Cslib.SKI.Y_def, Cslib.SKI.Y_correct, Cslib.SKI.fixedPoint, Cslib.SKI.fixedPoint_correct, Cslib.SKI.ThAuxPoly, Cslib.SKI.ThAux, Cslib.SKI.ThAux_def, Cslib.SKI.Th, Cslib.SKI.Th_correct, Cslib.SKI.IsBool, Cslib.SKI.isBool_trans, Cslib.SKI.TT, Cslib.SKI.TT_correct, Cslib.SKI.FF, Cslib.SKI.FF_correct, Cslib.SKI.Cond, Cslib.SKI.cond_correct, Cslib.SKI.Neg, Cslib.SKI.neg_correct, Cslib.SKI.AndPoly, Cslib.SKI.And, Cslib.SKI.and_def, Cslib.SKI.and_correct, Cslib.SKI.OrPoly, Cslib.SKI.Or, Cslib.SKI.or_def, Cslib.SKI.or_correct, Cslib.SKI.MkPair, Cslib.SKI.Fst, Cslib.SKI.Snd, Cslib.SKI.fst_correct, Cslib.SKI.snd_correct, Cslib.SKI.UnpairedPoly, Cslib.SKI.Unpaired, Cslib.SKI.unpaired_def, Cslib.SKI.unpaired_correct, Cslib.SKI.PairPoly, Cslib.SKI.Pair, Cslib.SKI.pair_def
statement: formalized
proof: formalized
---

# Basic results for the SKI calculus

`Cslib.Languages.CombinatoryLogic.Basic`, in [Cslib/Languages/CombinatoryLogic/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean), by Thomas Waring.

> ## Main definition
>
> - `Polynomial`: the type of SKI terms with fixed number of "holes" (read: free variables).
>
> ## Notation
>
> - `⬝'` : application between polynomials,
> - `&i` : the ith free variable of a polynomial.
>
> ## Main results
>
> - Bracket abstraction: an algorithm `Polynomial.toSKI` to convert a polynomial
> $Γ(x_0, ..., x_\{n-1\})$ into a term such that (`Polynomial.toSKI_correct`)
> `Γ.toSKI ⬝ t₁ ⬝ ... ⬝ tₙ` reduces to `Γ(t₁, ..., tₙ)`.
>
> ## References
>
> For a presentation of the bracket abstraction algorithm see:
> <https://web.archive.org/web/19970727171324/http://www.cs.oberlin.edu/classes/cs280/labs/lab4/lab43.html#@l13>

> ### Polynomials and the bracket astraction algorithm

`Cslib.SKI.Polynomial` (inductive type, [line 46](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L46))

> A polynomial is an SKI terms with free variables.

```lean
protected inductive Polynomial (n : Nat) : Type where
  | term : SKI → SKI.Polynomial n
  | var : Fin n → SKI.Polynomial n
  | app : SKI.Polynomial n → SKI.Polynomial n → SKI.Polynomial n
```

`Cslib.SKI.CoeTermPolynomial` (instance, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L57))

```lean
instance CoeTermPolynomial (n : Nat) : Coe SKI (SKI.Polynomial n)
```

`Cslib.SKI.Polynomial.eval` (definition, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L60))

> Substitute terms for the free variables of a polynomial

```lean
def Polynomial.eval {n : Nat} (Γ : SKI.Polynomial n) (l : List SKI) (hl : List.length l = n) :
    SKI
```

`Cslib.SKI.Polynomial.varFreeToSKI` (definition, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L68))

> A polynomial with no free variables is a term

```lean
def Polynomial.varFreeToSKI (Γ : SKI.Polynomial 0) : SKI
```

`Cslib.SKI.Polynomial.elimVar` (definition, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L72))

> Inductively define a polynomial `Γ'` so that (up to the fact that we haven't
> defined reduction on polynomials) `Γ' ⬝ t ↠ Γ[xₙ ← t]`.

```lean
def Polynomial.elimVar {n : Nat} : SKI.Polynomial (n+1) → SKI.Polynomial n
```

`Cslib.SKI.Polynomial.elimVar_correct` (theorem, [line 91](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L91))

> Correctness for the elimVar algorithm, which provides the inductive step of the bracket abstraction
> algorithm. We induct backwards on the list, corresponding to applying the transformation from the
> inside out. Since we haven't defined reduction for polynomials, we substitute arbitrary terms
> for the inner variables.

```lean
theorem Polynomial.elimVar_correct {n : Nat} (Γ : SKI.Polynomial (n + 1)) {ys : List SKI}
    (hys : ys.length = n) (z : SKI) :
    (Γ.elimVar.eval ys hys ⬝ z) ↠ Γ.eval (ys ++ [z])
      (by rw [List.length_append, hys, List.length_singleton])
```

`Cslib.SKI.Polynomial.toSKI` (definition, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L121))

> Bracket abstraction, by induction using `SKI.Polynomial.elimVar`

```lean
def Polynomial.toSKI {n : Nat} (Γ : SKI.Polynomial n) : SKI
```

`Cslib.SKI.Polynomial.toSKI_correct` (theorem, [line 127](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L127))

> Correctness for the toSKI (bracket abstraction) algorithm.

```lean
theorem Polynomial.toSKI_correct {n : Nat} (Γ : SKI.Polynomial n) (xs : List SKI)
    (hxs : xs.length = n) : Γ.toSKI.applyList xs ↠ Γ.eval xs hxs
```

> ### Basic auxiliary combinators.
>
> Each combinator is defined by a polynomial, which is then proved to have the reduction property
> we want. Before each definition we provide its lambda calculus equivalent. If there is accepted
> notation for a given combinator, we use that (given everywhere a capital letter), otherwise we
> choose a descriptive name.

`Cslib.SKI.RPoly` (definition, [line 162](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L162))

> Reversal: R := λ x y. y x

```lean
def RPoly : SKI.Polynomial 2
```

`Cslib.SKI.R` (definition, [line 164](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L164))

> A SKI term representing R

```lean
def R : SKI
```

`Cslib.SKI.R_def` (theorem, [line 165](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L165))

```lean
theorem R_def (x y : SKI) : (R ⬝ x ⬝ y) ↠ y ⬝ x
```

`Cslib.SKI.BPoly` (definition, [line 169](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L169))

> Composition: B := λ f g x. f (g x)

```lean
def BPoly : SKI.Polynomial 3
```

`Cslib.SKI.B` (definition, [line 171](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L171))

> A SKI term representing B

```lean
def B : SKI
```

`Cslib.SKI.B_def` (theorem, [line 172](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L172))

```lean
theorem B_def (f g x : SKI) : (B ⬝ f ⬝ g ⬝ x) ↠ f ⬝ (g ⬝ x)
```

`Cslib.SKI.B_tail_mred` (lemma, [line 176](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L176))

> B followed by tail reduction

```lean
lemma B_tail_mred (f g x y : SKI) (h : (g ⬝ x) ↠ y) : (B ⬝ f ⬝ g ⬝ x) ↠ f ⬝ y
```

`Cslib.SKI.CPoly` (definition, [line 180](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L180))

> C := λ f x y. f y x

```lean
def CPoly : SKI.Polynomial 3
```

`Cslib.SKI.C` (definition, [line 182](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L182))

> A SKI term representing C

```lean
def C : SKI
```

`Cslib.SKI.C_def` (theorem, [line 183](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L183))

```lean
theorem C_def (f x y : SKI) : (C ⬝ f ⬝ x ⬝ y) ↠ f ⬝ y ⬝ x
```

`Cslib.SKI.C_head_mred` (lemma, [line 187](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L187))

> C followed by head reduction

```lean
lemma C_head_mred (f x y z : SKI) (h : (f ⬝ y) ↠ z) : (C ⬝ f ⬝ x ⬝ y) ↠ z ⬝ x
```

`Cslib.SKI.RotRPoly` (definition, [line 191](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L191))

> Rotate right: RotR := λ x y z. z x y

```lean
def RotRPoly : SKI.Polynomial 3
```

`Cslib.SKI.RotR` (definition, [line 193](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L193))

> A SKI term representing RotR

```lean
def RotR : SKI
```

`Cslib.SKI.rotR_def` (theorem, [line 194](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L194))

```lean
theorem rotR_def (x y z : SKI) : (RotR ⬝ x ⬝ y ⬝ z) ↠ z ⬝ x ⬝ y
```

`Cslib.SKI.RotLPoly` (definition, [line 198](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L198))

> Rotate left: RotR := λ x y z. y z x

```lean
def RotLPoly : SKI.Polynomial 3
```

`Cslib.SKI.RotL` (definition, [line 200](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L200))

> A SKI term representing RotL

```lean
def RotL : SKI
```

`Cslib.SKI.rotL_def` (theorem, [line 201](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L201))

```lean
theorem rotL_def (x y z : SKI) : (RotL ⬝ x ⬝ y ⬝ z) ↠ y ⬝ z ⬝ x
```

`Cslib.SKI.DelPoly` (definition, [line 205](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L205))

> Self application: δ := λ x. x x

```lean
def DelPoly : SKI.Polynomial 1
```

`Cslib.SKI.Del` (definition, [line 207](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L207))

> A SKI term representing δ

```lean
def Del : SKI
```

`Cslib.SKI.del_def` (theorem, [line 208](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L208))

```lean
theorem del_def (x : SKI) : (Del ⬝ x) ↠ x ⬝ x
```

`Cslib.SKI.HPoly` (definition, [line 212](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L212))

> H := λ f x. f (x x)

```lean
def HPoly : SKI.Polynomial 2
```

`Cslib.SKI.H` (definition, [line 214](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L214))

> A SKI term representing H

```lean
def H : SKI
```

`Cslib.SKI.H_def` (theorem, [line 215](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L215))

```lean
theorem H_def (f x : SKI) : (H ⬝ f ⬝ x) ↠ f ⬝ (x ⬝ x)
```

`Cslib.SKI.YPoly` (definition, [line 219](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L219))

> Curry's fixed-point combinator: Y := λ f. H f (H f)

```lean
def YPoly : SKI.Polynomial 1
```

`Cslib.SKI.Y` (definition, [line 221](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L221))

> A SKI term representing Y

```lean
def Y : SKI
```

`Cslib.SKI.Y_def` (theorem, [line 222](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L222))

```lean
theorem Y_def (f : SKI) : (Y ⬝ f) ↠ H ⬝ f ⬝ (H ⬝ f)
```

`Cslib.SKI.Y_correct` (theorem, [line 226](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L226))

> The fixed-point property of the Y-combinator

```lean
theorem Y_correct (f : SKI) : Join (ReflTransGen Red) (Y ⬝ f) (f ⬝ (Y ⬝ f))
```

`Cslib.SKI.fixedPoint` (definition, [line 238](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L238))

> It is useful to be able to produce a term such that the fixed point property holds on-the-nose,
> rather than up to a common reduct. An alternative is to use Turing's fixed-point combinator
> (defined below).

```lean
def fixedPoint (f : SKI) : SKI
```

`Cslib.SKI.fixedPoint_correct` (theorem, [line 239](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L239))

```lean
theorem fixedPoint_correct (f : SKI) : f.fixedPoint ↠ f ⬝ f.fixedPoint
```

`Cslib.SKI.ThAuxPoly` (definition, [line 242](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L242))

> Auxiliary definition for Turing's fixed-point combinator: ΘAux := λ x y. y (x x y)

```lean
def ThAuxPoly : SKI.Polynomial 2
```

`Cslib.SKI.ThAux` (definition, [line 244](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L244))

> A term representing ΘAux

```lean
def ThAux : SKI
```

`Cslib.SKI.ThAux_def` (theorem, [line 245](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L245))

```lean
theorem ThAux_def (x y : SKI) : (ThAux ⬝ x ⬝ y) ↠ y ⬝ (x ⬝ x ⬝ y)
```

`Cslib.SKI.Th` (definition, [line 249](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L249))

> Turing's fixed-point combinator: Θ := (λ x y. y (x x y)) (λ x y. y (x x y))

```lean
def Th : SKI
```

`Cslib.SKI.Th_correct` (theorem, [line 251](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L251))

> A SKI term representing Θ

```lean
theorem Th_correct (f : SKI) : (Th ⬝ f) ↠ f ⬝ (Th ⬝ f)
```

> ### Church Booleans

`Cslib.SKI.IsBool` (definition, [line 256](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L256))

> A term a represents the boolean value u if it is βη-equivalent to a standard Church boolean.

```lean
def IsBool (u : Bool) (a : SKI) : Prop
```

`Cslib.SKI.isBool_trans` (theorem, [line 259](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L259))

```lean
theorem isBool_trans (u : Bool) (a a' : SKI) (h : a ↠ a') (ha' : IsBool u a') :
    IsBool u a
```

`Cslib.SKI.TT` (definition, [line 269](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L269))

> Standard true: TT := λ x y. x

```lean
def TT : SKI
```

`Cslib.SKI.TT_correct` (theorem, [line 271](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L271))

```lean
theorem TT_correct : IsBool true TT
```

`Cslib.SKI.FF` (definition, [line 274](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L274))

> Standard false: FF := λ x y. y

```lean
def FF : SKI
```

`Cslib.SKI.FF_correct` (theorem, [line 276](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L276))

```lean
theorem FF_correct : IsBool false FF
```

`Cslib.SKI.Cond` (definition, [line 282](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L282))

> Conditional: Cond x y b := if b then x else y

```lean
protected def Cond : SKI
```

`Cslib.SKI.cond_correct` (theorem, [line 283](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L283))

```lean
theorem cond_correct (a x y : SKI) (u : Bool) (h : IsBool u a) :
    (SKI.Cond ⬝ x ⬝ y ⬝ a) ↠ if u then x else y
```

`Cslib.SKI.Neg` (definition, [line 290](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L290))

> Neg := λ a. Cond FF TT a

```lean
protected def Neg : SKI
```

`Cslib.SKI.neg_correct` (theorem, [line 291](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L291))

```lean
theorem neg_correct (a : SKI) (ua : Bool) (h : IsBool ua a) : IsBool (¬ ua) (SKI.Neg ⬝ a)
```

`Cslib.SKI.AndPoly` (definition, [line 299](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L299))

> And := λ a b. Cond (Cond TT FF b) FF a

```lean
def AndPoly : SKI.Polynomial 2
```

`Cslib.SKI.And` (definition, [line 301](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L301))

> A SKI term representing And

```lean
protected def And : SKI
```

`Cslib.SKI.and_def` (theorem, [line 302](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L302))

```lean
theorem and_def (a b : SKI) : (SKI.And ⬝ a ⬝ b) ↠ SKI.Cond ⬝ (SKI.Cond ⬝ TT ⬝ FF ⬝ b) ⬝ FF ⬝ a
```

`Cslib.SKI.and_correct` (theorem, [line 305](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L305))

```lean
theorem and_correct (a b : SKI) (ua ub : Bool) (ha : IsBool ua a) (hb : IsBool ub b) :
    IsBool (ua && ub) (SKI.And ⬝ a ⬝ b)
```

`Cslib.SKI.OrPoly` (definition, [line 319](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L319))

> Or := λ a b. Cond TT (Cond TT FF b) b

```lean
def OrPoly : SKI.Polynomial 2
```

`Cslib.SKI.Or` (definition, [line 321](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L321))

> A SKI term representing Or

```lean
protected def Or : SKI
```

`Cslib.SKI.or_def` (theorem, [line 322](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L322))

```lean
theorem or_def (a b : SKI) : (SKI.Or ⬝ a ⬝ b) ↠ SKI.Cond ⬝ TT ⬝ (SKI.Cond ⬝ TT ⬝ FF ⬝ b) ⬝ a
```

`Cslib.SKI.or_correct` (theorem, [line 325](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L325))

```lean
theorem or_correct (a b : SKI) (ua ub : Bool) (ha : IsBool ua a) (hb : IsBool ub b) :
  IsBool (ua || ub) (SKI.Or ⬝ a ⬝ b)
```

> ### Pairs

`Cslib.SKI.MkPair` (definition, [line 343](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L343))

> MkPair := λ a b. ⟨a,b⟩

```lean
def MkPair : SKI
```

`Cslib.SKI.Fst` (definition, [line 345](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L345))

> First projection

```lean
def Fst : SKI
```

`Cslib.SKI.Snd` (definition, [line 347](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L347))

> Second projection

```lean
def Snd : SKI
```

`Cslib.SKI.fst_correct` (theorem, [line 350](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L350))

```lean
theorem fst_correct (a b : SKI) : (Fst ⬝ (MkPair ⬝ a ⬝ b)) ↠ a
```

`Cslib.SKI.snd_correct` (theorem, [line 355](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L355))

```lean
theorem snd_correct (a b : SKI) : (Snd ⬝ (MkPair ⬝ a ⬝ b)) ↠ b
```

`Cslib.SKI.UnpairedPoly` (definition, [line 360](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L360))

> Unpaired f ⟨x, y⟩ := f x y, cf `Nat.unparied`.

```lean
def UnpairedPoly : SKI.Polynomial 2
```

`Cslib.SKI.Unpaired` (definition, [line 362](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L362))

> A term representing Unpaired

```lean
protected def Unpaired : SKI
```

`Cslib.SKI.unpaired_def` (theorem, [line 363](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L363))

```lean
theorem unpaired_def (f p : SKI) : (SKI.Unpaired ⬝ f ⬝ p) ↠ f ⬝ (Fst ⬝ p) ⬝ (Snd ⬝ p)
```

`Cslib.SKI.unpaired_correct` (theorem, [line 366](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L366))

```lean
theorem unpaired_correct (f x y : SKI) : (SKI.Unpaired ⬝ f ⬝ (MkPair ⬝ x ⬝ y)) ↠ f ⬝ x ⬝ y
```

`Cslib.SKI.PairPoly` (definition, [line 375](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L375))

> Pair f g x := ⟨f x, g x⟩, cf `Primrec.Pair`.

```lean
def PairPoly : SKI.Polynomial 3
```

`Cslib.SKI.Pair` (definition, [line 377](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L377))

> A SKI term representing Pair

```lean
protected def Pair : SKI
```

`Cslib.SKI.pair_def` (theorem, [line 378](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean#L378))

```lean
theorem pair_def (f g x : SKI) : (SKI.Pair ⬝ f ⬝ g ⬝ x) ↠ MkPair ⬝ (f ⬝ x) ⬝ (g ⬝ x)
```

## Depends on

- [SKI Combinatory Logic](defs.md)

## Sources

- [Cslib/Languages/CombinatoryLogic/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Basic.lean)
