---
catalog: module
lean: Cslib.Logic.Kleene.Value, Cslib.Logic.Kleene.Value.le_def, Cslib.Logic.Kleene.Value.top_eq_true, Cslib.Logic.Kleene.Value.bot_eq_false, Cslib.Logic.Kleene.Value.false_lt_unknown, Cslib.Logic.Kleene.Value.unknown_lt_true, Cslib.Logic.Kleene.Value.false_inf, Cslib.Logic.Kleene.Value.inf_false, Cslib.Logic.Kleene.Value.true_inf, Cslib.Logic.Kleene.Value.inf_true, Cslib.Logic.Kleene.Value.true_sup, Cslib.Logic.Kleene.Value.sup_true, Cslib.Logic.Kleene.Value.false_sup, Cslib.Logic.Kleene.Value.sup_false, Cslib.Logic.Kleene.Value.inf_eq_true_iff, Cslib.Logic.Kleene.Value.sup_eq_true_iff, Cslib.Logic.Kleene.Value.sup_eq_false_iff, Cslib.Logic.Kleene.Value.compl_true, Cslib.Logic.Kleene.Value.compl_false, Cslib.Logic.Kleene.Value.compl_unknown, Cslib.Logic.Kleene.Value.compl_compl, Cslib.Logic.Kleene.Value.compl_eq_true_iff, Cslib.Logic.Kleene.Value.compl_eq_false_iff, Cslib.Logic.Kleene.Value.compl_antitone, Cslib.Logic.Kleene.Value.compl_inf, Cslib.Logic.Kleene.Value.compl_sup, Cslib.Logic.Kleene.Value.ofBool, Cslib.Logic.Kleene.Value.ofBool_true, Cslib.Logic.Kleene.Value.ofBool_false, Cslib.Logic.Kleene.Value.ofBool_injective, Cslib.Logic.Kleene.Value.ofBool_inj, Cslib.Logic.Kleene.Value.ofBool_ne_unknown, Cslib.Logic.Kleene.Value.unknown_ne_ofBool, Cslib.Logic.Kleene.Value.ofBool_not, Cslib.Logic.Kleene.Value.ofBool_and, Cslib.Logic.Kleene.Value.ofBool_or, Cslib.Logic.Kleene.Value.InfoLE, Cslib.Logic.Kleene.Value.infoLE_def, Cslib.Logic.Kleene.Value.InfoLE.refl, Cslib.Logic.Kleene.Value.InfoLE.trans, Cslib.Logic.Kleene.Value.InfoLE.antisymm, Cslib.Logic.Kleene.Value.unknown_infoLE, Cslib.Logic.Kleene.Value.infoLE_unknown_iff, Cslib.Logic.Kleene.Value.ofBool_infoLE_iff, Cslib.Logic.Kleene.Value.true_infoLE_iff, Cslib.Logic.Kleene.Value.false_infoLE_iff, Cslib.Logic.Kleene.Value.InfoLE.compl, Cslib.Logic.Kleene.Value.InfoLE.inf, Cslib.Logic.Kleene.Value.InfoLE.sup, Cslib.Logic.Kleene.Value.infoLE_compl_of_extends, Cslib.Logic.Kleene.Value.eq_compl_of_extends, Cslib.Logic.Kleene.Value.infoLE_inf_of_extends, Cslib.Logic.Kleene.Value.infoLE_sup_of_extends, Cslib.Logic.Kleene.Value.toOption, Cslib.Logic.Kleene.Value.toOption_true, Cslib.Logic.Kleene.Value.toOption_false, Cslib.Logic.Kleene.Value.toOption_unknown, Cslib.Logic.Kleene.Value.toOption_ofBool, Cslib.Logic.Kleene.Value.toOption_symm_some, Cslib.Logic.Kleene.Value.toOption_symm_none, Cslib.Logic.Kleene.Value.toOption_eq_none_iff, Cslib.Logic.Kleene.Value.toOption_eq_some_iff, Cslib.Logic.Kleene.Value.toOption_compl, Cslib.Logic.Kleene.Value.toOption_symm_infoLE_iff
statement: formalized
proof: formalized
---

# Truth values of Kleene's strong three-valued logic

`Cslib.Logics.Kleene.Basic`, in [Cslib/Logics/Kleene/Basic.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean), by Jesse Alama.

> The truth values of Kleene's strong three-valued logic (K3) [Kleene1952], as an algebra: a bounded
> linear order `false < unknown < true`, the truth order, with a complement. Meet `⊓`, join `⊔` and
> complement `ᶜ` are Kleene's conjunction, disjunction and negation.
>
> These are also the truth values of SQL [Codd1979], where a comparison involving `NULL` evaluates
> to `unknown`, and `AND`, `OR` and `NOT` are the meet, join and complement defined here.
>
> In the information order `⊑`, `unknown` lies below both definite values, which are incomparable.
> Every operation is monotone in it, and `⊓`, `⊔` and `ᶜ` are the greatest monotone extensions of
> `&&`, `||` and `!`. Under `⊑`, `Kleene.Value` is the flat domain on `Bool`, so these results could
> be subsumed under a general development of domain theory.
>
> ## Main definitions
>
> - `Kleene.Value`: the three truth values.
> - `Compl Kleene.Value`: the complement, which swaps `true` and `false` and fixes `unknown`.
> - `Kleene.Value.ofBool`: the embedding of `Bool`.
> - `Kleene.Value.InfoLE`, written `⊑`: the information order.
> - `Kleene.Value.toOption`: the equivalence with `Option Bool`, `unknown` as `none`.
>
> ## Main results
>
> - `LinearOrder Kleene.Value`, `BoundedOrder Kleene.Value`: the truth order.
> - `Kleene.Value.compl_inf`, `Kleene.Value.compl_sup`: the De Morgan laws.
> - `Kleene.Value.ofBool_and` and friends: `ofBool` commutes with the operations.
> - `IsPartialOrder Kleene.Value Kleene.Value.InfoLE`, `Kleene.Value.InfoLE.inf` and friends: the
>   information order is a partial order in which every operation is monotone.
> - `Kleene.Value.infoLE_inf_of_extends` and friends: `⊓`, `⊔` and `ᶜ` are the greatest monotone
>   extensions of `&&`, `||` and `!`.
> - `Kleene.Value.eq_compl_of_extends`: `ᶜ` is the only monotone extension of `!`.
>
> ## References
>
> - [Kleene1952] S. C. Kleene, *Introduction to Metamathematics*, §64.
> - [Codd1979] E. F. Codd, *Extending the database relational model to capture more meaning*.

`Cslib.Logic.Kleene.Value` (inductive type, [line 60](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L60))

> A truth value of Kleene's strong three-valued logic.

```lean
inductive Value where
  | true
  | false
  | unknown
  deriving DecidableEq, Repr, Fintype
```

> ### The truth order

`Cslib.Logic.Kleene.Value.le_def` (theorem, [line 73](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L73))

```lean
theorem le_def {a b : Value} : a ≤ b ↔ a = b ∨ a = .false ∨ b = .true
```

`Cslib.Logic.Kleene.Value.top_eq_true` (theorem, [line 91](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L91))

```lean
theorem top_eq_true : (⊤ : Value) = .true
```

`Cslib.Logic.Kleene.Value.bot_eq_false` (theorem, [line 92](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L92))

```lean
theorem bot_eq_false : (⊥ : Value) = .false
```

`Cslib.Logic.Kleene.Value.false_lt_unknown` (theorem, [line 94](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L94))

```lean
theorem false_lt_unknown : (.false : Value) < .unknown
```

`Cslib.Logic.Kleene.Value.unknown_lt_true` (theorem, [line 96](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L96))

```lean
theorem unknown_lt_true : (.unknown : Value) < .true
```

> ### Meet and join

`Cslib.Logic.Kleene.Value.false_inf` (theorem, [line 100](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L100))

```lean
theorem false_inf (a : Value) : .false ⊓ a = .false
```

`Cslib.Logic.Kleene.Value.inf_false` (theorem, [line 101](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L101))

```lean
theorem inf_false (a : Value) : a ⊓ .false = .false
```

`Cslib.Logic.Kleene.Value.true_inf` (theorem, [line 102](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L102))

```lean
theorem true_inf (a : Value) : .true ⊓ a = a
```

`Cslib.Logic.Kleene.Value.inf_true` (theorem, [line 103](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L103))

```lean
theorem inf_true (a : Value) : a ⊓ .true = a
```

`Cslib.Logic.Kleene.Value.true_sup` (theorem, [line 105](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L105))

```lean
theorem true_sup (a : Value) : .true ⊔ a = .true
```

`Cslib.Logic.Kleene.Value.sup_true` (theorem, [line 106](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L106))

```lean
theorem sup_true (a : Value) : a ⊔ .true = .true
```

`Cslib.Logic.Kleene.Value.false_sup` (theorem, [line 107](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L107))

```lean
theorem false_sup (a : Value) : .false ⊔ a = a
```

`Cslib.Logic.Kleene.Value.sup_false` (theorem, [line 108](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L108))

```lean
theorem sup_false (a : Value) : a ⊔ .false = a
```

`Cslib.Logic.Kleene.Value.inf_eq_true_iff` (theorem, [line 110](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L110))

```lean
theorem inf_eq_true_iff {a b : Value} : a ⊓ b = .true ↔ a = .true ∧ b = .true
```

`Cslib.Logic.Kleene.Value.sup_eq_true_iff` (theorem, [line 113](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L113))

```lean
theorem sup_eq_true_iff {a b : Value} : a ⊔ b = .true ↔ a = .true ∨ b = .true
```

`Cslib.Logic.Kleene.Value.sup_eq_false_iff` (theorem, [line 116](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L116))

```lean
theorem sup_eq_false_iff {a b : Value} : a ⊔ b = .false ↔ a = .false ∧ b = .false
```

> ### Complement

`Cslib.Logic.Kleene.Value.compl_true` (theorem, [line 128](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L128))

```lean
theorem compl_true : (Value.true)ᶜ = .false
```

`Cslib.Logic.Kleene.Value.compl_false` (theorem, [line 129](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L129))

```lean
theorem compl_false : (Value.false)ᶜ = .true
```

`Cslib.Logic.Kleene.Value.compl_unknown` (theorem, [line 130](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L130))

```lean
theorem compl_unknown : (Value.unknown)ᶜ = .unknown
```

`Cslib.Logic.Kleene.Value.compl_compl` (theorem, [line 132](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L132))

```lean
protected theorem compl_compl (a : Value) : aᶜᶜ = a
```

`Cslib.Logic.Kleene.Value.compl_eq_true_iff` (theorem, [line 134](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L134))

```lean
theorem compl_eq_true_iff {a : Value} : aᶜ = .true ↔ a = .false
```

`Cslib.Logic.Kleene.Value.compl_eq_false_iff` (theorem, [line 136](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L136))

```lean
theorem compl_eq_false_iff {a : Value} : aᶜ = .false ↔ a = .true
```

`Cslib.Logic.Kleene.Value.compl_antitone` (theorem, [line 139](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L139))

> The complement reverses the truth order.

```lean
theorem compl_antitone : Antitone fun a : Value => aᶜ
```

`Cslib.Logic.Kleene.Value.compl_inf` (theorem, [line 141](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L141))

```lean
protected theorem compl_inf (a b : Value) : (a ⊓ b)ᶜ = aᶜ ⊔ bᶜ
```

`Cslib.Logic.Kleene.Value.compl_sup` (theorem, [line 142](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L142))

```lean
protected theorem compl_sup (a b : Value) : (a ⊔ b)ᶜ = aᶜ ⊓ bᶜ
```

> ### The embedding of `Bool`

`Cslib.Logic.Kleene.Value.ofBool` (definition, [line 147](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L147))

> The embedding of `Bool`.

```lean
def ofBool : Bool → Value
```

`Cslib.Logic.Kleene.Value.ofBool_true` (theorem, [line 151](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L151))

```lean
theorem ofBool_true : ofBool Bool.true = .true
```

`Cslib.Logic.Kleene.Value.ofBool_false` (theorem, [line 152](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L152))

```lean
theorem ofBool_false : ofBool Bool.false = .false
```

`Cslib.Logic.Kleene.Value.ofBool_injective` (theorem, [line 154](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L154))

```lean
theorem ofBool_injective : Function.Injective ofBool
```

`Cslib.Logic.Kleene.Value.ofBool_inj` (theorem, [line 156](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L156))

```lean
theorem ofBool_inj {a b : Bool} : ofBool a = ofBool b ↔ a = b
```

`Cslib.Logic.Kleene.Value.ofBool_ne_unknown` (theorem, [line 158](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L158))

```lean
theorem ofBool_ne_unknown (b : Bool) : ofBool b ≠ .unknown
```

`Cslib.Logic.Kleene.Value.unknown_ne_ofBool` (theorem, [line 159](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L159))

```lean
theorem unknown_ne_ofBool (b : Bool) : .unknown ≠ ofBool b
```

`Cslib.Logic.Kleene.Value.ofBool_not` (theorem, [line 162](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L162))

```lean
theorem ofBool_not (b : Bool) : ofBool (!b) = (ofBool b)ᶜ
```

`Cslib.Logic.Kleene.Value.ofBool_and` (theorem, [line 165](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L165))

```lean
theorem ofBool_and (a b : Bool) : ofBool (a && b) = ofBool a ⊓ ofBool b
```

`Cslib.Logic.Kleene.Value.ofBool_or` (theorem, [line 168](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L168))

```lean
theorem ofBool_or (a b : Bool) : ofBool (a || b) = ofBool a ⊔ ofBool b
```

> ### The information order

`Cslib.Logic.Kleene.Value.InfoLE` (definition, [line 174](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L174))

> The information order: `unknown` lies below every value, and the definite values are
> incomparable. It is distinct from the truth order `≤`.

```lean
def InfoLE (a b : Value) : Prop
```

`Cslib.Logic.Kleene.Value.infoLE_def` (theorem, [line 178](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L178))

```lean
theorem infoLE_def {a b : Value} : a ⊑ b ↔ a = .unknown ∨ a = b
```

`Cslib.Logic.Kleene.Value.InfoLE.refl` (theorem, [line 182](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L182))

```lean
protected theorem InfoLE.refl (a : Value) : a ⊑ a
```

`Cslib.Logic.Kleene.Value.InfoLE.trans` (theorem, [line 184](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L184))

```lean
protected theorem InfoLE.trans {a b c : Value} : a ⊑ b → b ⊑ c → a ⊑ c
```

`Cslib.Logic.Kleene.Value.InfoLE.antisymm` (theorem, [line 186](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L186))

```lean
protected theorem InfoLE.antisymm {a b : Value} : a ⊑ b → b ⊑ a → a = b
```

`Cslib.Logic.Kleene.Value.unknown_infoLE` (theorem, [line 194](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L194))

> `unknown` is the least informative value.

```lean
theorem unknown_infoLE (a : Value) : .unknown ⊑ a
```

`Cslib.Logic.Kleene.Value.infoLE_unknown_iff` (theorem, [line 196](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L196))

```lean
theorem infoLE_unknown_iff {a : Value} : a ⊑ .unknown ↔ a = .unknown
```

`Cslib.Logic.Kleene.Value.ofBool_infoLE_iff` (theorem, [line 200](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L200))

> Definite values are maximal in the information order.

```lean
theorem ofBool_infoLE_iff {x : Bool} {b : Value} : ofBool x ⊑ b ↔ b = ofBool x
```

`Cslib.Logic.Kleene.Value.true_infoLE_iff` (theorem, [line 203](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L203))

```lean
theorem true_infoLE_iff {b : Value} : .true ⊑ b ↔ b = .true
```

`Cslib.Logic.Kleene.Value.false_infoLE_iff` (theorem, [line 204](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L204))

```lean
theorem false_infoLE_iff {b : Value} : .false ⊑ b ↔ b = .false
```

> ### Monotonicity in the information order

`Cslib.Logic.Kleene.Value.InfoLE.compl` (theorem, [line 208](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L208))

```lean
protected theorem InfoLE.compl {a a' : Value} (h : a ⊑ a') : aᶜ ⊑ a'ᶜ
```

`Cslib.Logic.Kleene.Value.InfoLE.inf` (theorem, [line 210](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L210))

```lean
protected theorem InfoLE.inf {a a' b b' : Value} (ha : a ⊑ a') (hb : b ⊑ b') :
    a ⊓ b ⊑ a' ⊓ b'
```

`Cslib.Logic.Kleene.Value.InfoLE.sup` (theorem, [line 213](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L213))

```lean
protected theorem InfoLE.sup {a a' b b' : Value} (ha : a ⊑ a') (hb : b ⊑ b') :
    a ⊔ b ⊑ a' ⊔ b'
```

> ### Greatest monotone extensions

`Cslib.Logic.Kleene.Value.infoLE_compl_of_extends` (theorem, [line 220](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L220))

> The complement is the greatest extension of Boolean negation that is monotone in the
> information order.

```lean
theorem infoLE_compl_of_extends {f : Value → Value}
    (mono : ∀ {a a'}, a ⊑ a' → f a ⊑ f a')
    (ext : ∀ x : Bool, f (ofBool x) = ofBool (!x)) (a : Value) : f a ⊑ aᶜ
```

`Cslib.Logic.Kleene.Value.eq_compl_of_extends` (theorem, [line 228](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L228))

> The complement is the only extension of Boolean negation that is monotone in the information
> order.

```lean
theorem eq_compl_of_extends {f : Value → Value}
    (mono : ∀ {a a'}, a ⊑ a' → f a ⊑ f a')
    (ext : ∀ x : Bool, f (ofBool x) = ofBool (!x)) (a : Value) : f a = aᶜ
```

`Cslib.Logic.Kleene.Value.infoLE_inf_of_extends` (theorem, [line 236](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L236))

> The meet is the greatest extension of Boolean conjunction that is monotone in the information
> order.

```lean
theorem infoLE_inf_of_extends {f : Value → Value → Value}
    (mono : ∀ {a a' b b'}, a ⊑ a' → b ⊑ b' → f a b ⊑ f a' b')
    (ext : ∀ x y : Bool, f (ofBool x) (ofBool y) = ofBool (x && y))
    (a b : Value) : f a b ⊑ a ⊓ b
```

`Cslib.Logic.Kleene.Value.infoLE_sup_of_extends` (theorem, [line 246](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L246))

> The join is the greatest extension of Boolean disjunction that is monotone in the information
> order.

```lean
theorem infoLE_sup_of_extends {f : Value → Value → Value}
    (mono : ∀ {a a' b b'}, a ⊑ a' → b ⊑ b' → f a b ⊑ f a' b')
    (ext : ∀ x y : Bool, f (ofBool x) (ofBool y) = ofBool (x || y))
    (a b : Value) : f a b ⊑ a ⊔ b
```

> ### The equivalence with `Option Bool`

`Cslib.Logic.Kleene.Value.toOption` (definition, [line 257](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L257))

> `Kleene.Value` is `Option Bool`: the definite values as `some`, `unknown` as `none`.

```lean
def toOption : Value ≃ Option Bool
```

`Cslib.Logic.Kleene.Value.toOption_true` (theorem, [line 269](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L269))

```lean
theorem toOption_true : toOption .true = some Bool.true
```

`Cslib.Logic.Kleene.Value.toOption_false` (theorem, [line 270](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L270))

```lean
theorem toOption_false : toOption .false = some Bool.false
```

`Cslib.Logic.Kleene.Value.toOption_unknown` (theorem, [line 271](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L271))

```lean
theorem toOption_unknown : toOption .unknown = none
```

`Cslib.Logic.Kleene.Value.toOption_ofBool` (theorem, [line 272](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L272))

```lean
theorem toOption_ofBool (b : Bool) : toOption (ofBool b) = some b
```

`Cslib.Logic.Kleene.Value.toOption_symm_some` (theorem, [line 275](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L275))

```lean
theorem toOption_symm_some (b : Bool) :
    toOption.symm (some b) = ofBool b
```

`Cslib.Logic.Kleene.Value.toOption_symm_none` (theorem, [line 277](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L277))

```lean
theorem toOption_symm_none : toOption.symm none = .unknown
```

`Cslib.Logic.Kleene.Value.toOption_eq_none_iff` (theorem, [line 279](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L279))

```lean
theorem toOption_eq_none_iff {a : Value} : toOption a = none ↔ a = .unknown
```

`Cslib.Logic.Kleene.Value.toOption_eq_some_iff` (theorem, [line 282](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L282))

```lean
theorem toOption_eq_some_iff {a : Value} {b : Bool} :
    toOption a = some b ↔ a = ofBool b
```

`Cslib.Logic.Kleene.Value.toOption_compl` (theorem, [line 286](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L286))

```lean
theorem toOption_compl (a : Value) :
    toOption aᶜ = (toOption a).map Bool.not
```

`Cslib.Logic.Kleene.Value.toOption_symm_infoLE_iff` (theorem, [line 290](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean#L290))

> The information order, read through `toOption`.

```lean
theorem toOption_symm_infoLE_iff {o o' : Option Bool} :
    toOption.symm o ⊑ toOption.symm o' ↔ o = none ∨ o = o'
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Logics/Kleene/Basic.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Kleene/Basic.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Logics.Kleene.Basic.json)
