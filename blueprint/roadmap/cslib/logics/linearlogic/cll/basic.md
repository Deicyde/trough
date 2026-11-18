---
catalog: module
lean: Cslib.Logic.CLL.Proposition, Cslib.Logic.CLL.Proposition.Context, Cslib.Logic.CLL.Proposition.Context.fill, Cslib.Logic.CLL.Proposition.context_fill_def, Cslib.Logic.CLL.Proposition.positive, Cslib.Logic.CLL.Proposition.negative, Cslib.Logic.CLL.Proposition.positiveDecidable, Cslib.Logic.CLL.Proposition.negativeDecidable, Cslib.Logic.CLL.Proposition.dual, Cslib.Logic.CLL.Proposition.top_eq_zero_dual, Cslib.Logic.CLL.Proposition.dual_sizeOf, Cslib.Logic.CLL.Proposition.dual_neq, Cslib.Logic.CLL.Proposition.dual_involution, Cslib.Logic.CLL.Proposition.dual_inj, Cslib.Logic.CLL.Proposition.linImpl, Cslib.Logic.CLL.Sequent, Cslib.Logic.CLL.Sequent.allQuest, Cslib.Logic.CLL.Sequent.Context, Cslib.Logic.CLL.Sequent.Context.fill, Cslib.Logic.CLL.Proof, Cslib.Logic.CLL.Proof.rwConclusion, Cslib.Logic.CLL.Proof.ax', Cslib.Logic.CLL.Proof.cut', Cslib.Logic.CLL.Proof.parrInversion, Cslib.Logic.CLL.Proof.botInversion, Cslib.Logic.CLL.Proof.withInversion₁, Cslib.Logic.CLL.Proof.withInversion₂, Cslib.Logic.CLL.Proposition.equiv, Cslib.Logic.CLL.Proposition.Equiv, Cslib.Logic.CLL.Proposition.prop_equiv_def, Cslib.Logic.CLL.Proposition.equiv.toProp, Cslib.Logic.CLL.chooseEquiv, Cslib.Logic.CLL.Proposition.equiv.refl, Cslib.Logic.CLL.Proposition.equiv.symm, Cslib.Logic.CLL.Proposition.equiv.trans, Cslib.Logic.CLL.Proposition.Equiv.refl, Cslib.Logic.CLL.Proposition.Equiv.symm, Cslib.Logic.CLL.Proposition.Equiv.trans, Cslib.Logic.CLL.Proposition.Equiv.dual, Cslib.Logic.CLL.Proposition.propositionSetoid, Cslib.Logic.CLL.Proposition.bangTopEqvOne, Cslib.Logic.CLL.Proposition.questZeroEqvBot, Cslib.Logic.CLL.Proposition.tensorZeroEqvZero, Cslib.Logic.CLL.Proposition.parrTopEqvTop, Cslib.Logic.CLL.Proposition.tensorDistribOplus, Cslib.Logic.CLL.Proposition.substEqvHead, Cslib.Logic.CLL.Proposition.add_middle_eq_cons, Cslib.Logic.CLL.Proposition.substEqv, Cslib.Logic.CLL.Proposition.tensorSymm, Cslib.Logic.CLL.Proposition.tensorAssoc, Cslib.Logic.CLL.Proposition.oplusIdem, Cslib.Logic.CLL.Proposition.withIdem, Cslib.Logic.CLL.Proof.cutFree
statement: formalized
proof: formalized
---

# Classical Linear Logic

`Cslib.Logics.LinearLogic.CLL.Basic`, in [Cslib/Logics/LinearLogic/CLL/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean), by Fabrizio Montesi.

> …
> ## References
>
> * [J.-Y. Girard, *Linear Logic: its syntax and semantics*][Girard1995]

`Cslib.Logic.CLL.Proposition` (inductive type, [line 32](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L32))

> Propositions.

```lean
inductive Proposition (Atom : Type u) : Type u where
  | atom (x : Atom)
  | atomDual (x : Atom)
  | one
  | zero
  | top
  | bot
  /-- The multiplicative conjunction connective. -/
  | tensor (a b : Proposition Atom)
  /-- The multiplicative disjunction connective. -/
  | parr (a b : Proposition Atom)
  /-- The additive disjunction connective. -/
  | oplus (a b : Proposition Atom)
  /-- The additive conjunction connective. -/
  | with (a b : Proposition Atom)
  /-- The "of course" exponential. -/
  | bang (a : Proposition Atom)
  /-- The "why not" exponential.
  This is written as ʔ, or \_?, to distinguish itself from the lean syntatical hole ? syntax -/
  | quest (a : Proposition Atom)
deriving DecidableEq, BEq
```

`Cslib.Logic.CLL.Proposition.Context` (inductive type, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L69))

> Propositional contexts (single-hole contexts for propositions).

```lean
inductive Proposition.Context (Atom : Type u) : Type u where
  | hole
  | tensorL (c : Context Atom) (b : Proposition Atom)
  | tensorR (a : Proposition Atom) (c : Context Atom)
  | parrL (c : Context Atom) (b : Proposition Atom)
  | parrR (a : Proposition Atom) (c : Context Atom)
  | oplusL (c : Context Atom) (b : Proposition Atom)
  | oplusR (a : Proposition Atom) (c : Context Atom)
  | withL (c : Context Atom) (b : Proposition Atom)
  | withR (a : Proposition Atom) (c : Context Atom)
  | bang (c : Context Atom)
  | quest (c : Context Atom)
deriving DecidableEq, BEq
```

`Cslib.Logic.CLL.Proposition.Context.fill` (definition, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L85))

> Replaces the hole in a propositional context with a propositions.

```lean
def Proposition.Context.fill (c : Context Atom) (a : Proposition Atom) : Proposition Atom
```

`Cslib.Logic.CLL.Proposition.context_fill_def` (theorem, [line 103](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L103))

> Definition of context filling.

```lean
theorem Proposition.context_fill_def (c : Context Atom) (a : Proposition Atom) :
  c<[a] = c.fill a
```

`Cslib.Logic.CLL.Proposition.positive` (definition, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L107))

> Positive propositions.

```lean
def Proposition.positive : Proposition Atom → Bool
```

`Cslib.Logic.CLL.Proposition.negative` (definition, [line 112](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L112))

> Negative propositions.

```lean
def Proposition.negative : Proposition Atom → Bool
```

`Cslib.Logic.CLL.Proposition.positiveDecidable` (instance, [line 117](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L117))

> Whether a `Proposition` is positive is decidable.

```lean
instance Proposition.positiveDecidable (a : Proposition Atom) : Decidable a.positive
```

`Cslib.Logic.CLL.Proposition.negativeDecidable` (instance, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L121))

> Whether a `Proposition` is negative is decidable.

```lean
instance Proposition.negativeDecidable (a : Proposition Atom) : Decidable a.negative
```

`Cslib.Logic.CLL.Proposition.dual` (definition, [line 126](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L126))

> Propositional duality.

```lean
def Proposition.dual : Proposition Atom → Proposition Atom
```

`Cslib.Logic.CLL.Proposition.top_eq_zero_dual` (theorem, [line 143](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L143))

```lean
theorem Proposition.top_eq_zero_dual : ⊤ = (0⫠ : Proposition Atom)
```

`Cslib.Logic.CLL.Proposition.dual_sizeOf` (theorem, [line 147](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L147))

> Duality preserves size.

```lean
theorem Proposition.dual_sizeOf (a : Proposition Atom) : sizeOf a⫠ = sizeOf a
```

`Cslib.Logic.CLL.Proposition.dual_neq` (theorem, [line 152](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L152))

> No proposition is equal to its dual.

```lean
theorem Proposition.dual_neq (a : Proposition Atom) : a ≠ a⫠
```

`Cslib.Logic.CLL.Proposition.dual_involution` (theorem, [line 157](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L157))

> Duality is an involution.

```lean
theorem Proposition.dual_involution (a : Proposition Atom) : a⫠⫠ = a
```

`Cslib.Logic.CLL.Proposition.dual_inj` (theorem, [line 162](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L162))

> Two propositions are equal iff their respective duals are equal.

```lean
theorem Proposition.dual_inj (a b : Proposition Atom) : a⫠ = b⫠ ↔ a = b
```

`Cslib.Logic.CLL.Proposition.linImpl` (definition, [line 167](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L167))

> Linear implication.

```lean
def Proposition.linImpl (a b : Proposition Atom) : Proposition Atom
```

`Cslib.Logic.CLL.Sequent` (abbreviation, [line 172](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L172))

> A sequent in CLL is a multiset of propositions.

```lean
abbrev Sequent Atom
```

`Cslib.Logic.CLL.Sequent.allQuest` (definition, [line 175](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L175))

> Checks that all propositions in a sequent `Γ` are question marks.

```lean
def Sequent.allQuest (Γ : Sequent Atom)
```

`Cslib.Logic.CLL.Sequent.Context` (definition, [line 180](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L180))

> Judgemental contexts for CLL.

```lean
def Sequent.Context Atom
```

`Cslib.Logic.CLL.Sequent.Context.fill` (definition, [line 183](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L183))

> Filling a judgemental context returns a sequent.

```lean
def Sequent.Context.fill (Γc : Sequent.Context Atom) (a : Proposition Atom)
```

`Cslib.Logic.CLL.Proof` (inductive type, [line 189](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L189))

> A proof in the sequent calculus for classical linear logic.

```lean
inductive Proof : Sequent Atom → Type u where
  | ax : Proof {a, a⫠}
  | cut : Proof (a ::ₘ Γ) → Proof (a⫠ ::ₘ Δ) → Proof (Γ + Δ)
  | one : Proof {1}
  | bot : Proof Γ → Proof (⊥ ::ₘ Γ)
  | parr : Proof (a ::ₘ b ::ₘ Γ) → Proof ((a ⅋ b) ::ₘ Γ)
  | tensor : Proof (a ::ₘ Γ) → Proof (b ::ₘ Δ) → Proof ((a ⊗ b) ::ₘ (Γ + Δ))
  | oplus₁ : Proof (a ::ₘ Γ) → Proof ((a ⊕ b) ::ₘ Γ)
  | oplus₂ : Proof (b ::ₘ Γ) → Proof ((a ⊕ b) ::ₘ Γ)
  | with : Proof (a ::ₘ Γ) → Proof (b ::ₘ Γ) → Proof ((a & b) ::ₘ Γ)
  | top : Proof (⊤ ::ₘ Γ)
  | quest : Proof (a ::ₘ Γ) → Proof (ʔa ::ₘ Γ)
  | weaken : Proof Γ → Proof (ʔa ::ₘ Γ)
  | contract : Proof (ʔa ::ₘ ʔa ::ₘ Γ) → Proof (ʔa ::ₘ Γ)
  | bang {Γ : Sequent Atom} {a} : Γ.allQuest → Proof (a ::ₘ Γ) → Proof ((!a) ::ₘ Γ)
```

`Cslib.Logic.CLL.Proof.rwConclusion` (definition, [line 212](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L212))

> Convenience definition for rewriting conclusions in proofs.

```lean
def Proof.rwConclusion {Γ Δ : Sequent Atom} (h : Γ = Δ) (p : ⇓Γ)
```

`Cslib.Logic.CLL.Proof.ax'` (definition, [line 216](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L216))

> The axiom, but where the order of propositions is reversed.

```lean
def Proof.ax' {a : Proposition Atom} : ⇓({a⫠, a} : Sequent Atom)
```

`Cslib.Logic.CLL.Proof.cut'` (definition, [line 221](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L221))

> Cut, but where the premises are reversed.

```lean
def Proof.cut' (p : ⇓(a⫠ ::ₘ Γ)) (q : ⇓(a ::ₘ Δ)) : ⇓(Γ + Δ)
```

`Cslib.Logic.CLL.Proof.parrInversion` (definition, [line 226](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L226))

> Inversion of the ⅋ rule.

```lean
def Proof.parrInversion {Γ : Sequent Atom} (h : ⇓((a ⅋ b) ::ₘ Γ)) : ⇓(a ::ₘ b ::ₘ Γ)
```

`Cslib.Logic.CLL.Proof.botInversion` (definition, [line 231](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L231))

> Inversion of the ⊥ rule.

```lean
def Proof.botInversion {Γ : Sequent Atom} (h : ⇓(⊥ ::ₘ Γ)) : ⇓Γ
```

`Cslib.Logic.CLL.Proof.withInversion₁` (definition, [line 236](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L236))

> Inversion of the & rule, first component.

```lean
def Proof.withInversion₁ {Γ : Sequent Atom} (h : ⇓((a & b) ::ₘ Γ)) : ⇓(a ::ₘ Γ)
```

`Cslib.Logic.CLL.Proof.withInversion₂` (definition, [line 240](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L240))

> Inversion of the & rule, second component.

```lean
def Proof.withInversion₂ {Γ : Sequent Atom} (h : ⇓((a & b) ::ₘ Γ)) : ⇓(b ::ₘ Γ)
```

> ## Logical equivalences

`Cslib.Logic.CLL.Proposition.equiv` (definition, [line 249](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L249))

> Two propositions are equivalent if one implies the other and vice versa.
> Proof-relevant version.

```lean
def Proposition.equiv (a b : Proposition Atom)
```

`Cslib.Logic.CLL.Proposition.Equiv` (definition, [line 257](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L257))

> Propositional equivalence, proof-irrelevant version (`Prop`).

```lean
def Proposition.Equiv (a b : Proposition Atom)
```

`Cslib.Logic.CLL.Proposition.prop_equiv_def` (theorem, [line 263](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L263))

```lean
theorem Proposition.prop_equiv_def {a b : Proposition Atom} : Proposition.Equiv a b ↔ a ≡ b
```

`Cslib.Logic.CLL.Proposition.equiv.toProp` (theorem, [line 268](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L268))

> Conversion from proof-relevant to proof-irrelevant versions of propositional
> equivalence.

```lean
theorem Proposition.equiv.toProp (h : a ≡⇓ b) : a ≡ b
```

`Cslib.Logic.CLL.chooseEquiv` (definition, [line 274](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L274))

> Transforms a proof-irrelevant equivalence into a proof-relevant one (this is not computable).

```lean
noncomputable def chooseEquiv (h : a ≡ b) : a ≡⇓ b
```

`Cslib.Logic.CLL.Proposition.equiv.refl` (definition, [line 282](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L282))

> Proof-relevant equivalence is reflexive.

```lean
def equiv.refl (a : Proposition Atom) : a ≡⇓ a
```

`Cslib.Logic.CLL.Proposition.equiv.symm` (definition, [line 286](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L286))

> Proof-relevant equivalence is symmetric.

```lean
def equiv.symm (a : Proposition Atom) (h : a ≡⇓ b) : b ≡⇓ a
```

`Cslib.Logic.CLL.Proposition.equiv.trans` (definition, [line 289](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L289))

> Proof-relevant equivalence is transitive.

```lean
def equiv.trans {a b c : Proposition Atom} (hab : a ≡⇓ b) (hbc : b ≡⇓ c) : a ≡⇓ c
```

`Cslib.Logic.CLL.Proposition.Equiv.refl` (theorem, [line 295](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L295))

> Proof-irrelevant equivalence is reflexive.

```lean
theorem Equiv.refl (a : Proposition Atom) : a ≡ a
```

`Cslib.Logic.CLL.Proposition.Equiv.symm` (theorem, [line 299](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L299))

> Proof-irrelevant equivalence is symmetric.

```lean
theorem Equiv.symm {a b : Proposition Atom} (h : a ≡ b) : b ≡ a
```

`Cslib.Logic.CLL.Proposition.Equiv.trans` (theorem, [line 302](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L302))

> Proof-irrelevant equivalence is transitive.

```lean
theorem Equiv.trans {a b c : Proposition Atom} (hab : a ≡ b) (hbc : b ≡ c) : a ≡ c
```

`Cslib.Logic.CLL.Proposition.Equiv.dual` (theorem, [line 308](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L308))

> Logical equivalence is preserved by duality.

```lean
theorem Equiv.dual {a b : Proposition Atom} (h : a ≡ b) : a⫠ ≡ b⫠
```

`Cslib.Logic.CLL.Proposition.propositionSetoid` (definition, [line 314](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L314))

> The canonical equivalence relation for propositions.

```lean
def propositionSetoid : Setoid (Proposition Atom)
```

`Cslib.Logic.CLL.Proposition.bangTopEqvOne` (definition, [line 324](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L324))

> !⊤ ≡⇓ 1

```lean
def bangTopEqvOne : (!⊤ : Proposition Atom) ≡⇓ 1
```

`Cslib.Logic.CLL.Proposition.questZeroEqvBot` (definition, [line 329](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L329))

> ʔ0 ≡⇓ ⊥

```lean
def questZeroEqvBot : (ʔ0 : Proposition Atom) ≡⇓ ⊥
```

`Cslib.Logic.CLL.Proposition.tensorZeroEqvZero` (definition, [line 335](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L335))

> a ⊗ 0 ≡⇓ 0

```lean
def tensorZeroEqvZero (a : Proposition Atom) : a ⊗ 0 ≡⇓ 0
```

`Cslib.Logic.CLL.Proposition.parrTopEqvTop` (definition, [line 340](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L340))

> a ⅋ ⊤ ≡⇓ ⊤

```lean
def parrTopEqvTop (a : Proposition Atom) : a ⅋ ⊤ ≡⇓ ⊤
```

`Cslib.Logic.CLL.Proposition.tensorDistribOplus` (definition, [line 353](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L353))

> ⊗ distributes over ⊕.

```lean
def tensorDistribOplus (a b c : Proposition Atom) : a ⊗ (b ⊕ c) ≡⇓ (a ⊗ b) ⊕ (a ⊗ c)
```

`Cslib.Logic.CLL.Proposition.substEqvHead` (definition, [line 372](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L372))

> The proposition at the head of a proof can be substituted by an equivalent
> proposition.

```lean
def substEqvHead {Γ : Sequent Atom} (heqv : a ≡⇓ b) (p : ⇓(a ::ₘ Γ)) : ⇓(b ::ₘ Γ)
```

`Cslib.Logic.CLL.Proposition.add_middle_eq_cons` (theorem, [line 375](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L375))

```lean
theorem add_middle_eq_cons {a : Proposition Atom} : Γ + {a} + Δ = a ::ₘ (Γ + Δ)
```

`Cslib.Logic.CLL.Proposition.substEqv` (definition, [line 382](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L382))

> Any proposition in a proof (regardless of its position) can be substituted by
> an equivalent proposition.

```lean
def substEqv {Γ Δ : Sequent Atom} (heqv : a ≡⇓ b) (p : ⇓(Γ + {a} + Δ)) : ⇓(Γ + {b} + Δ)
```

`Cslib.Logic.CLL.Proposition.tensorSymm` (definition, [line 559](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L559))

> Tensor is commutative.

```lean
def tensorSymm {a b : Proposition Atom} : a ⊗ b ≡⇓ b ⊗ a
```

`Cslib.Logic.CLL.Proposition.tensorAssoc` (definition, [line 567](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L567))

> ⊗ is associative.

```lean
def tensorAssoc {a b c : Proposition Atom} : a ⊗ (b ⊗ c) ≡⇓ (a ⊗ b) ⊗ c
```

`Cslib.Logic.CLL.Proposition.oplusIdem` (definition, [line 583](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L583))

> ⊕ is idempotent.

```lean
def oplusIdem {a : Proposition Atom} : a ⊕ a ≡⇓ a
```

`Cslib.Logic.CLL.Proposition.withIdem` (definition, [line 589](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L589))

> & is idempotent.

```lean
def withIdem {a : Proposition Atom} : a & a ≡⇓ a
```

`Cslib.Logic.CLL.Proof.cutFree` (definition, [line 598](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean#L598))

> A proof is cut-free if it does not contain any applications of rule cut.

```lean
def Proof.cutFree {Γ : Sequent Atom} : ⇓Γ → Bool
```

## Depends on

- [LogicalEquivalence](../../../foundations/logic/logicalequivalence.md)

## Sources

- [Cslib/Logics/LinearLogic/CLL/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/LinearLogic/CLL/Basic.lean)
