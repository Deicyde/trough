---
catalog: module
lean: Cslib.SKI.Church, Cslib.SKI.Church_zero, Cslib.SKI.Church_succ, Cslib.SKI.church_red, Cslib.SKI.IsChurch, Cslib.SKI.isChurch_trans, Cslib.SKI.Zero, Cslib.SKI.zero_correct, Cslib.SKI.One, Cslib.SKI.one_correct, Cslib.SKI.Succ, Cslib.SKI.succ_correct, Cslib.SKI.toChurch, Cslib.SKI.toChurch_zero, Cslib.SKI.toChurch_succ, Cslib.SKI.toChurch_correct, Cslib.SKI.PredAuxPoly, Cslib.SKI.PredAux, Cslib.SKI.predAux_def, Cslib.SKI.IsChurchPair, Cslib.SKI.isChurchPair_trans, Cslib.SKI.predAux_correct, Cslib.SKI.predAux_correct', Cslib.SKI.PredPoly, Cslib.SKI.Pred, Cslib.SKI.pred_def, Cslib.SKI.pred_correct, Cslib.SKI.IsZeroPoly, Cslib.SKI.IsZero, Cslib.SKI.isZero_def, Cslib.SKI.isZero_correct, Cslib.SKI.RecAuxPoly, Cslib.SKI.RecAux, Cslib.SKI.recAux_def, Cslib.SKI.Rec, Cslib.SKI.rec_def, Cslib.SKI.rec_zero, Cslib.SKI.rec_succ, Cslib.SKI.rec_correct', Cslib.SKI.RFindAboveAuxPoly, Cslib.SKI.RFindAboveAux, Cslib.SKI.rfindAboveAux_def, Cslib.SKI.rfindAboveAux_base, Cslib.SKI.rfindAboveAux_step, Cslib.SKI.RFindAbove, Cslib.SKI.RFindAbove_unfold, Cslib.SKI.RFindAbove_correct', Cslib.SKI.RFindAbove_correct, Cslib.SKI.RFind, Cslib.SKI.RFind_correct, Cslib.SKI.AddPoly, Cslib.SKI.Add, Cslib.SKI.add_def, Cslib.SKI.add_correct, Cslib.SKI.MulPoly, Cslib.SKI.Mul, Cslib.SKI.mul_def, Cslib.SKI.mul_correct, Cslib.SKI.SubPoly, Cslib.SKI.Sub, Cslib.SKI.sub_def, Cslib.SKI.sub_correct, Cslib.SKI.LEPoly, Cslib.SKI.LE, Cslib.SKI.le_def, Cslib.SKI.le_correct, Cslib.SKI.SqrtCondPoly, Cslib.SKI.SqrtCond, Cslib.SKI.sqrtCond_def, Cslib.SKI.SqrtPoly, Cslib.SKI.Sqrt, Cslib.SKI.sqrt_def, Cslib.SKI.sqrt_correct, Cslib.SKI.NatPairPoly, Cslib.SKI.NatPair, Cslib.SKI.natPair_def, Cslib.SKI.natPair_correct, Cslib.SKI.NatUnpairLeftPoly, Cslib.SKI.NatUnpairLeft, Cslib.SKI.natUnpairLeft_def, Cslib.SKI.natUnpairLeft_correct, Cslib.SKI.NatUnpairRightPoly, Cslib.SKI.NatUnpairRight, Cslib.SKI.natUnpairRight_def, Cslib.SKI.natUnpairRight_correct
statement: formalized
proof: formalized
---

# General recursion in the SKI calculus

`Cslib.Languages.CombinatoryLogic.Recursion`, in [Cslib/Languages/CombinatoryLogic/Recursion.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean), by Thomas Waring, Jesse Alama.

> In this file we implement general recursion functions (on the natural numbers), inspired by the
> formalisation of `Mathlib.Computability.Partrec`. Since composition (`B`-combinator) and pairs
> (`MkPair`, `Fst`, `Snd`) have been implemented in `Cslib.Computability.CombinatoryLogic.Basic`,
> what remains are the following definitions and proofs of their correctness.
>
> - Church numerals : a predicate `IsChurch n a` expressing that the term `a` is βη-equivalent to
> the standard church numeral `n` — that is, `a ⬝ f ⬝ x ↠ f ⬝ (f ⬝ ... ⬝ (f ⬝ x)))`.
> - SKI numerals : `Zero` and `Succ`, corresponding to `Partrec.zero` and `Partrec.succ`, and
> correctness proofs `zero_correct` and `succ_correct`.
> - Predecessor : a term `Pred` so that (`pred_correct`)
> `IsChurch n a → IsChurch n.pred (Pred ⬝ a)`.
> - Primitive recursion : a term `Rec` so that (`rec_correct_succ`) `IsChurch (n+1) a` implies
> `Rec ⬝ x ⬝ g ⬝ a ↠ g ⬝ a ⬝ (Rec ⬝ x ⬝ g ⬝ (Pred ⬝ a))` and (`rec_correct_zero`) `IsChurch 0 a`
> implies `Rec ⬝ x ⬝ g ⬝ a ↠ x`.
> - Unbounded root finding (μ-recursion) : given a term  `f` representing a function `fℕ: Nat → Nat`,
> which takes on the value 0 a term `RFind` such that (`rFind_correct`) `RFind ⬝ f ↠ a` such that
> `IsChurch n a` for `n` the smallest root of `fℕ`.
> - Integer square root : a term `Sqrt` so that (`sqrt_correct`)
> `IsChurch n a → IsChurch n.sqrt (Sqrt ⬝ a)`.
> - Nat pairing : a term `NatPair` so that (`natPair_correct`)
> `IsChurch a x → IsChurch b y → IsChurch (Nat.pair a b) (NatPair ⬝ x ⬝ y)`.
> - Nat unpairing : terms `NatUnpairLeft` and `NatUnpairRight` so that (`natUnpairLeft_correct`)
> `IsChurch n a → IsChurch n.unpair.1 (NatUnpairLeft ⬝ a)` and (`natUnpairRight_correct`)
> `IsChurch n a → IsChurch n.unpair.2 (NatUnpairRight ⬝ a)`.
>
> ## References
>
> - For church numerals and recursion via the fixed-point combinator, see sections 3.2 and 3.3 of
> Selinger's notes <https://www.mscs.dal.ca/~selinger/papers/papers/lambdanotes.pdf>
>
> …

`Cslib.SKI.Church` (definition, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L69))

> Function form of the church numerals.

```lean
def Church (n : Nat) (f x : SKI) : SKI
```

`Cslib.SKI.Church_zero` (lemma, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L74))

```lean
lemma Church_zero (f x : SKI) : Church 0 f x = x
```

`Cslib.SKI.Church_succ` (lemma, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L75))

```lean
lemma Church_succ (n : Nat) (f x : SKI) : Church (n+1) f x = f ⬝ Church n f x
```

`Cslib.SKI.church_red` (lemma, [line 78](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L78))

> `church` commutes with reduction.

```lean
lemma church_red (n : Nat) (f f' x x' : SKI) (hf : f ↠ f') (hx : x ↠ x') :
    Church n f x ↠ Church n f' x'
```

`Cslib.SKI.IsChurch` (definition, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L85))

> The term `a` is βη-equivalent to a standard church numeral.

```lean
def IsChurch (n : Nat) (a : SKI) : Prop
```

`Cslib.SKI.isChurch_trans` (theorem, [line 89](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L89))

> To show `IsChurch n a` it suffices to show the same for a reduct of `a`.

```lean
theorem isChurch_trans (n : Nat) {a a' : SKI} (h : a ↠ a') :
    IsChurch n a' → IsChurch n a
```

> ### Church numeral basics

`Cslib.SKI.Zero` (definition, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L101))

> Church zero := λ f x. x

```lean
protected def Zero : SKI
```

`Cslib.SKI.zero_correct` (theorem, [line 103](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L103))

```lean
theorem zero_correct : IsChurch 0 SKI.Zero
```

`Cslib.SKI.One` (definition, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L111))

> Church one := λ f x. f x

```lean
protected def One : SKI
```

`Cslib.SKI.one_correct` (theorem, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L113))

```lean
theorem one_correct : IsChurch 1 SKI.One
```

`Cslib.SKI.Succ` (definition, [line 119](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L119))

> Church succ := λ a f x. f (a f x) ~ λ a f. B f (a f) ~ λ a. S B a ~ S B

```lean
protected def Succ : SKI
```

`Cslib.SKI.succ_correct` (theorem, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L121))

```lean
theorem succ_correct (n : Nat) (a : SKI) (h : IsChurch n a) :
    IsChurch (n+1) (SKI.Succ ⬝ a)
```

`Cslib.SKI.toChurch` (definition, [line 130](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L130))

> Build the canonical SKI Church numeral for `n`.

```lean
def toChurch : ℕ → SKI
```

`Cslib.SKI.toChurch_zero` (lemma, [line 135](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L135))

> `toChurch 0 = Zero`.

```lean
lemma toChurch_zero : toChurch 0 = SKI.Zero
```

`Cslib.SKI.toChurch_succ` (lemma, [line 137](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L137))

> `toChurch (n + 1) = Succ ⬝ toChurch n`.

```lean
lemma toChurch_succ (n : ℕ) : toChurch (n + 1) = SKI.Succ ⬝ (toChurch n)
```

`Cslib.SKI.toChurch_correct` (theorem, [line 141](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L141))

> `toChurch n` correctly represents `n`.

```lean
theorem toChurch_correct (n : ℕ) : IsChurch n (toChurch n)
```

`Cslib.SKI.PredAuxPoly` (definition, [line 150](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L150))

> To define the predecessor, iterate the function `PredAux` ⟨i, j⟩ ↦ ⟨j, j+1⟩ on ⟨0,0⟩, then take
> the  first component.

```lean
def PredAuxPoly : SKI.Polynomial 1
```

`Cslib.SKI.PredAux` (definition, [line 152](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L152))

> A term representing PredAux

```lean
def PredAux : SKI
```

`Cslib.SKI.predAux_def` (theorem, [line 153](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L153))

```lean
theorem predAux_def (p : SKI) :  (PredAux ⬝ p) ↠ MkPair ⬝ (Snd ⬝ p) ⬝ (SKI.Succ ⬝ (Snd ⬝ p))
```

`Cslib.SKI.IsChurchPair` (definition, [line 157](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L157))

> Useful auxiliary definition expressing that `p` represents ns ∈ Nat × Nat.

```lean
def IsChurchPair (ns : Nat × Nat) (x : SKI) : Prop
```

`Cslib.SKI.isChurchPair_trans` (theorem, [line 160](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L160))

```lean
theorem isChurchPair_trans (ns : Nat × Nat) (a a' : SKI) (h : a ↠ a') :
    IsChurchPair ns a' → IsChurchPair ns a
```

`Cslib.SKI.predAux_correct` (theorem, [line 172](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L172))

```lean
theorem predAux_correct (p : SKI) (ns : Nat × Nat) (h : IsChurchPair ns p) :
    IsChurchPair ⟨ns.2, ns.2+1⟩ (PredAux ⬝ p)
```

`Cslib.SKI.predAux_correct'` (theorem, [line 181](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L181))

> The stronger induction hypothesis necessary for the proof of `pred_correct`.

```lean
theorem predAux_correct' (n : Nat) :
    IsChurchPair (n.pred, n) <| Church n PredAux  (MkPair ⬝ SKI.Zero ⬝ SKI.Zero)
```

`Cslib.SKI.PredPoly` (definition, [line 195](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L195))

> Predecessor := λ n. Fst ⬝ (n ⬝ PredAux ⬝ (MkPair ⬝ Zero ⬝ Zero))

```lean
def PredPoly : SKI.Polynomial 1
```

`Cslib.SKI.Pred` (definition, [line 197](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L197))

> A term representing Pred

```lean
def Pred : SKI
```

`Cslib.SKI.pred_def` (theorem, [line 198](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L198))

```lean
theorem pred_def (a : SKI) : (Pred ⬝ a) ↠ Fst ⬝ (a ⬝ PredAux ⬝ (MkPair ⬝ SKI.Zero ⬝ SKI.Zero))
```

`Cslib.SKI.pred_correct` (theorem, [line 201](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L201))

```lean
theorem pred_correct (n : Nat) (a : SKI) (h : IsChurch n a) : IsChurch n.pred (Pred ⬝ a)
```

> ### Primitive recursion

`Cslib.SKI.IsZeroPoly` (definition, [line 213](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L213))

> IsZero := λ n. n (K FF) TT

```lean
def IsZeroPoly : SKI.Polynomial 1
```

`Cslib.SKI.IsZero` (definition, [line 215](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L215))

> A term representing IsZero

```lean
def IsZero : SKI
```

`Cslib.SKI.isZero_def` (theorem, [line 216](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L216))

```lean
theorem isZero_def (a : SKI) : (IsZero ⬝ a) ↠ a ⬝ (K ⬝ FF) ⬝ TT
```

`Cslib.SKI.isZero_correct` (theorem, [line 218](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L218))

```lean
theorem isZero_correct (n : Nat) (a : SKI) (h : IsChurch n a) :
    IsBool (n = 0) (IsZero ⬝ a)
```

`Cslib.SKI.RecAuxPoly` (definition, [line 241](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L241))

> To define `Rec x g n := if n==0 then x else (Rec x g (Pred n))`, we obtain a fixed point of
> R ↦ λ x g n. Cond ⬝ (IsZero ⬝ n) ⬝ x ⬝ (g ⬝ a ⬝ (R ⬝ x ⬝ g ⬝ (Pred ⬝ n)))

```lean
def RecAuxPoly : SKI.Polynomial 4
```

`Cslib.SKI.RecAux` (definition, [line 244](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L244))

> A term representing RecAux

```lean
def RecAux : SKI
```

`Cslib.SKI.recAux_def` (theorem, [line 245](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L245))

```lean
theorem recAux_def (R₀ x g a : SKI) :
    (RecAux ⬝ R₀ ⬝ x ⬝ g ⬝ a) ↠
      SKI.Cond ⬝ x ⬝ (g ⬝ a ⬝ (R₀ ⬝ x ⬝ g ⬝ (Pred ⬝ a))) ⬝ (IsZero ⬝ a)
```

`Cslib.SKI.Rec` (definition, [line 254](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L254))

> We define Rec so that
> `Rec ⬝ x ⬝ g ⬝ a ↠ SKI.Cond ⬝ x ⬝ (g ⬝ a ⬝ (Rec ⬝ x ⬝ g ⬝ (Pred ⬝ a))) ⬝ (IsZero ⬝ a)`

```lean
def Rec : SKI
```

`Cslib.SKI.rec_def` (theorem, [line 255](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L255))

```lean
theorem rec_def (x g a : SKI) :
    (Rec ⬝ x ⬝ g ⬝ a) ↠ SKI.Cond ⬝ x ⬝ (g ⬝ a ⬝ (Rec ⬝ x ⬝ g ⬝ (Pred ⬝ a))) ⬝ (IsZero ⬝ a)
```

`Cslib.SKI.rec_zero` (theorem, [line 262](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L262))

```lean
theorem rec_zero (x g a : SKI) (ha : IsChurch 0 a) : (Rec ⬝ x ⬝ g ⬝ a) ↠ x
```

`Cslib.SKI.rec_succ` (theorem, [line 269](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L269))

```lean
theorem rec_succ (n : Nat) (x g a : SKI) (ha : IsChurch (n + 1) a) :
    (Rec ⬝ x ⬝ g ⬝ a) ↠ g ⬝ a ⬝ (Rec ⬝ x ⬝ g ⬝ (Pred ⬝ a))
```

`Cslib.SKI.rec_correct'` (theorem, [line 283](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L283))

> Generalized primitive recursion. Given a sequence `r : ℕ → ℕ`, if `base` computes the base
> value `r 0` and `step` computes the recursion step pointwise — taking the Church numeral of the
> current index `k + 1` and the previous result `r k` to `r (k + 1)` — then `Rec ⬝ base ⬝ step`
> computes `r` on every input. This is the primitive-recursion counterpart of `RFindAbove_correct'`
> for μ-recursion: it isolates the behaviour of `Rec` from any particular client (such as the
> translation of `Nat.Partrec.Code.prec`).

```lean
theorem rec_correct' (base step : SKI) (r : ℕ → ℕ)
    (hbase : IsChurch (r 0) base)
    (hstep : ∀ k : Nat, ∀ cb cp : SKI, IsChurch (k + 1) cb → IsChurch (r k) cp →
      IsChurch (r (k + 1)) (step ⬝ cb ⬝ cp)) :
    ∀ n : Nat, ∀ cn : SKI, IsChurch n cn → IsChurch (r n) (Rec ⬝ base ⬝ step ⬝ cn)
```

> ### Root-finding (μ-recursion)

`Cslib.SKI.RFindAboveAuxPoly` (definition, [line 304](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L304))

> First define an auxiliary function `RFindAbove` that looks for roots above a fixed number n, as a
> fixed point of R ↦ λ n f. if f n = 0 then n else R f (n+1)
>                  ~ λ n f. Cond ⬝ n (R f (Succ n)) (IsZero (f n))

```lean
def RFindAboveAuxPoly : SKI.Polynomial 3
```

`Cslib.SKI.RFindAboveAux` (definition, [line 307](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L307))

> A term representing RFindAboveAux

```lean
def RFindAboveAux : SKI
```

`Cslib.SKI.rfindAboveAux_def` (lemma, [line 308](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L308))

```lean
lemma rfindAboveAux_def (R₀ f a : SKI) :
    (RFindAboveAux ⬝ R₀ ⬝ a ⬝ f) ↠ SKI.Cond ⬝ a ⬝ (R₀ ⬝ (SKI.Succ ⬝ a) ⬝ f) ⬝ (IsZero ⬝ (f ⬝ a))
```

`Cslib.SKI.rfindAboveAux_base` (theorem, [line 312](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L312))

```lean
theorem rfindAboveAux_base (R₀ f a : SKI) (hfa : IsChurch 0 (f ⬝ a)) :
    (RFindAboveAux ⬝ R₀ ⬝ a ⬝ f) ↠ a
```

`Cslib.SKI.rfindAboveAux_step` (theorem, [line 318](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L318))

```lean
theorem rfindAboveAux_step (R₀ f a : SKI) {m : Nat} (hfa : IsChurch (m + 1) (f ⬝ a)) :
    (RFindAboveAux ⬝ R₀ ⬝ a ⬝ f) ↠ R₀ ⬝ (SKI.Succ ⬝ a) ⬝ f
```

`Cslib.SKI.RFindAbove` (definition, [line 326](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L326))

> Find the minimal root of `fNat` above a number n

```lean
def RFindAbove : SKI
```

`Cslib.SKI.RFindAbove_unfold` (theorem, [line 329](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L329))

> One unfolding of `RFindAbove`: apply the fixed-point combinator once.

```lean
theorem RFindAbove_unfold (x g : SKI) :
    (RFindAbove ⬝ x ⬝ g) ↠ RFindAboveAux ⬝ RFindAbove ⬝ x ⬝ g
```

`Cslib.SKI.RFindAbove_correct'` (theorem, [line 335](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L335))

> Generalized root-finding that works with pointwise properties rather than a total
> function. At the root `m + n`, `f` yields Church 0; below, a nonzero Church numeral.

```lean
theorem RFindAbove_correct' (f x : SKI) (n m : Nat) (hx : IsChurch m x)
    (hf_root : ∀ y, IsChurch (m + n) y → IsChurch 0 (f ⬝ y))
    (hf_below : ∀ i < n, ∀ y, IsChurch (m + i) y → ∃ k, IsChurch (k + 1) (f ⬝ y)) :
    IsChurch (m + n) (RFindAbove ⬝ x ⬝ f)
```

`Cslib.SKI.RFindAbove_correct` (theorem, [line 352](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L352))

```lean
theorem RFindAbove_correct (fNat : Nat → Nat) (f x : SKI)
    (hf : ∀ i : Nat, ∀ y : SKI, IsChurch i y → IsChurch (fNat i) (f ⬝ y))
    (n m : Nat) (hx : IsChurch m x) (hroot : fNat (m + n) = 0) (hpos : ∀ i < n, fNat (m + i) ≠ 0) :
    IsChurch (m + n) (RFindAbove ⬝ x ⬝ f)
```

`Cslib.SKI.RFind` (definition, [line 363](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L363))

> Ordinary root finding is root finding above zero

```lean
def RFind
```

`Cslib.SKI.RFind_correct` (theorem, [line 364](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L364))

```lean
theorem RFind_correct (fNat : Nat → Nat) (f : SKI)
    (hf : ∀ (i : Nat) (y : SKI), IsChurch i y → IsChurch (fNat i) (f ⬝ y))
    (n : Nat) (hroot : fNat n = 0) (hpos : ∀ i < n, fNat i ≠ 0) : IsChurch n (RFind ⬝ f)
```

> ### Further numeric operations

`Cslib.SKI.AddPoly` (definition, [line 376](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L376))

> Addition: λ n m. n Succ m

```lean
def AddPoly : SKI.Polynomial 2
```

`Cslib.SKI.Add` (definition, [line 378](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L378))

> A term representing addition on church numerals

```lean
protected def Add : SKI
```

`Cslib.SKI.add_def` (theorem, [line 379](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L379))

```lean
theorem add_def (a b : SKI) : (SKI.Add ⬝ a ⬝ b) ↠ a ⬝ SKI.Succ ⬝ b
```

`Cslib.SKI.add_correct` (theorem, [line 382](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L382))

```lean
theorem add_correct (n m : Nat) (a b : SKI) (ha : IsChurch n a) (hb : IsChurch m b) :
    IsChurch (n + m) (SKI.Add ⬝ a ⬝ b)
```

`Cslib.SKI.MulPoly` (definition, [line 396](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L396))

> Multiplication: λ n m. n (Add m) Zero

```lean
def MulPoly : SKI.Polynomial 2
```

`Cslib.SKI.Mul` (definition, [line 398](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L398))

> A term representing multiplication on church numerals

```lean
protected def Mul : SKI
```

`Cslib.SKI.mul_def` (theorem, [line 399](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L399))

```lean
theorem mul_def (a b : SKI) : (SKI.Mul ⬝ a ⬝ b) ↠ a ⬝ (SKI.Add ⬝ b) ⬝ SKI.Zero
```

`Cslib.SKI.mul_correct` (theorem, [line 402](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L402))

```lean
theorem mul_correct {n m : Nat} {a b : SKI} (ha : IsChurch n a) (hb : IsChurch m b) :
    IsChurch (n * m) (SKI.Mul ⬝ a ⬝ b)
```

`Cslib.SKI.SubPoly` (definition, [line 414](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L414))

> Subtraction: λ n m. n Pred m

```lean
def SubPoly : SKI.Polynomial 2
```

`Cslib.SKI.Sub` (definition, [line 416](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L416))

> A term representing subtraction on church numerals

```lean
protected def Sub : SKI
```

`Cslib.SKI.sub_def` (theorem, [line 417](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L417))

```lean
theorem sub_def (a b : SKI) : (SKI.Sub ⬝ a ⬝ b) ↠ b ⬝ Pred ⬝ a
```

`Cslib.SKI.sub_correct` (theorem, [line 420](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L420))

```lean
theorem sub_correct (n m : Nat) (a b : SKI) (ha : IsChurch n a) (hb : IsChurch m b) :
    IsChurch (n - m) (SKI.Sub ⬝ a ⬝ b)
```

`Cslib.SKI.LEPoly` (definition, [line 434](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L434))

> Comparison: (. ≤ .) := λ n m. IsZero ⬝ (Sub ⬝ n ⬝ m)

```lean
def LEPoly : SKI.Polynomial 2
```

`Cslib.SKI.LE` (definition, [line 436](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L436))

> A term representing comparison on church numerals

```lean
protected def LE : SKI
```

`Cslib.SKI.le_def` (theorem, [line 437](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L437))

```lean
theorem le_def (a b : SKI) : (SKI.LE ⬝ a ⬝ b) ↠ IsZero ⬝ (SKI.Sub ⬝ a ⬝ b)
```

`Cslib.SKI.le_correct` (theorem, [line 440](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L440))

```lean
theorem le_correct (n m : Nat) (a b : SKI) (ha : IsChurch n a) (hb : IsChurch m b) :
    IsBool (n ≤ m) (SKI.LE ⬝ a ⬝ b)
```

> ### Integer square root

`Cslib.SKI.SqrtCondPoly` (definition, [line 451](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L451))

> Inner condition for Sqrt: with &0 = n, &1 = k,
> computes `if n < (k+1)² then 0 else 1`.

```lean
def SqrtCondPoly : SKI.Polynomial 2
```

`Cslib.SKI.SqrtCond` (definition, [line 456](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L456))

> SKI term for the inner condition of Sqrt

```lean
def SqrtCond : SKI
```

`Cslib.SKI.sqrtCond_def` (theorem, [line 460](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L460))

> `SqrtCond ⬝ n ⬝ k` reduces to: return 0 if `(k+1)² > n`, else 1.
> Used by `RFind` to locate the smallest such `k`, which is `√n`.

```lean
theorem sqrtCond_def (cn ck : SKI) :
    (SqrtCond ⬝ cn ⬝ ck) ↠
      SKI.Cond ⬝ SKI.Zero ⬝ SKI.One ⬝
        (SKI.Neg ⬝ (SKI.LE ⬝ (SKI.Mul ⬝ (SKI.Succ ⬝ ck) ⬝ (SKI.Succ ⬝ ck)) ⬝ cn))
```

`Cslib.SKI.SqrtPoly` (definition, [line 468](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L468))

> Sqrt n = smallest k such that (k+1)² > n, i.e., the integer square root.
> Defined as `λ n. RFind (SqrtCond n)`.

```lean
def SqrtPoly : SKI.Polynomial 1
```

`Cslib.SKI.Sqrt` (definition, [line 471](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L471))

> SKI term for integer square root

```lean
def Sqrt : SKI
```

`Cslib.SKI.sqrt_def` (theorem, [line 474](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L474))

> `Sqrt ⬝ n` reduces to an `RFind` search for the smallest `k` with `(k+1)² > n`.

```lean
theorem sqrt_def (cn : SKI) : (Sqrt ⬝ cn) ↠ RFind ⬝ (SqrtCond ⬝ cn)
```

`Cslib.SKI.sqrt_correct` (theorem, [line 478](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L478))

> `Sqrt` correctly computes `Nat.sqrt`.

```lean
theorem sqrt_correct (n : Nat) (cn : SKI) (hcn : IsChurch n cn) :
    IsChurch (Nat.sqrt n) (Sqrt ⬝ cn)
```

> ### Nat pairing (matching Mathlib's `Nat.pair`)

`Cslib.SKI.NatPairPoly` (definition, [line 499](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L499))

> NatPair a b = if a < b then b*b + a else a*a + a + b.
> With &0 = a, &1 = b. The condition `a < b` is `¬(b ≤ a)`.

```lean
def NatPairPoly : SKI.Polynomial 2
```

`Cslib.SKI.NatPair` (definition, [line 505](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L505))

> SKI term for Nat pairing

```lean
def NatPair : SKI
```

`Cslib.SKI.natPair_def` (theorem, [line 508](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L508))

> `NatPair ⬝ a ⬝ b` reduces to: if `a < b` then `b² + a`, else `a² + a + b`.

```lean
theorem natPair_def (ca cb : SKI) :
    (NatPair ⬝ ca ⬝ cb) ↠
      SKI.Cond ⬝ (SKI.Add ⬝ (SKI.Mul ⬝ cb ⬝ cb) ⬝ ca)
               ⬝ (SKI.Add ⬝ (SKI.Add ⬝ (SKI.Mul ⬝ ca ⬝ ca) ⬝ ca) ⬝ cb)
               ⬝ (SKI.Neg ⬝ (SKI.LE ⬝ cb ⬝ ca))
```

`Cslib.SKI.natPair_correct` (theorem, [line 516](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L516))

> `NatPair` correctly computes `Nat.pair`.

```lean
theorem natPair_correct (a b : Nat) (ca cb : SKI)
    (ha : IsChurch a ca) (hb : IsChurch b cb) :
    IsChurch (Nat.pair a b) (NatPair ⬝ ca ⬝ cb)
```

> ### Nat unpairing (matching Mathlib's `Nat.unpair`)

`Cslib.SKI.NatUnpairLeftPoly` (definition, [line 530](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L530))

> `NatUnpairLeft n = if n - s² < s then n - s² else s` where `s = Nat.sqrt n`.

```lean
def NatUnpairLeftPoly : SKI.Polynomial 1
```

`Cslib.SKI.NatUnpairLeft` (definition, [line 538](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L538))

> SKI term for left projection of Nat.unpair

```lean
def NatUnpairLeft : SKI
```

`Cslib.SKI.natUnpairLeft_def` (theorem, [line 542](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L542))

> `NatUnpairLeft ⬝ n` reduces to: let `s = √n` and `d = n - s²`;
> return `d` if `d < s`, else `s`.

```lean
theorem natUnpairLeft_def (cn : SKI) :
    (NatUnpairLeft ⬝ cn) ↠
      SKI.Cond ⬝ (SKI.Sub ⬝ cn ⬝ (SKI.Mul ⬝ (Sqrt ⬝ cn) ⬝ (Sqrt ⬝ cn)))
               ⬝ (Sqrt ⬝ cn)
               ⬝ (SKI.Neg ⬝ (SKI.LE ⬝ (Sqrt ⬝ cn)
                    ⬝ (SKI.Sub ⬝ cn ⬝ (SKI.Mul ⬝ (Sqrt ⬝ cn) ⬝ (Sqrt ⬝ cn)))))
```

`Cslib.SKI.natUnpairLeft_correct` (theorem, [line 559](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L559))

> `NatUnpairLeft` correctly computes the first component of `Nat.unpair`.

```lean
theorem natUnpairLeft_correct (n : Nat) (cn : SKI) (hcn : IsChurch n cn) :
    IsChurch (Nat.unpair n).1 (NatUnpairLeft ⬝ cn)
```

`Cslib.SKI.NatUnpairRightPoly` (definition, [line 568](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L568))

> NatUnpairRight n = let s = sqrt n in if n - s² < s then s else n - s² - s.

```lean
def NatUnpairRightPoly : SKI.Polynomial 1
```

`Cslib.SKI.NatUnpairRight` (definition, [line 576](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L576))

> SKI term for right projection of Nat.unpair

```lean
def NatUnpairRight : SKI
```

`Cslib.SKI.natUnpairRight_def` (theorem, [line 580](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L580))

> `NatUnpairRight ⬝ n` reduces to: let `s = √n` and `d = n - s²`;
> return `s` if `d < s`, else `d - s`.

```lean
theorem natUnpairRight_def (cn : SKI) :
    (NatUnpairRight ⬝ cn) ↠
      SKI.Cond ⬝ (Sqrt ⬝ cn)
               ⬝ (SKI.Sub ⬝ (SKI.Sub ⬝ cn ⬝ (SKI.Mul ⬝ (Sqrt ⬝ cn) ⬝ (Sqrt ⬝ cn)))
                            ⬝ (Sqrt ⬝ cn))
               ⬝ (SKI.Neg ⬝ (SKI.LE ⬝ (Sqrt ⬝ cn)
                    ⬝ (SKI.Sub ⬝ cn ⬝ (SKI.Mul ⬝ (Sqrt ⬝ cn) ⬝ (Sqrt ⬝ cn)))))
```

`Cslib.SKI.natUnpairRight_correct` (theorem, [line 590](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean#L590))

> `NatUnpairRight` correctly computes the second component of `Nat.unpair`.

```lean
theorem natUnpairRight_correct (n : Nat) (cn : SKI) (hcn : IsChurch n cn) :
    IsChurch (Nat.unpair n).2 (NatUnpairRight ⬝ cn)
```

## Depends on

- [Basic results for the SKI calculus](basic.md)

## Sources

- [Cslib/Languages/CombinatoryLogic/Recursion.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/Recursion.lean)
