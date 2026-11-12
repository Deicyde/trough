---
catalog: module
lean: HuntingtonAlgebra, HuntingtonAlgebra.compl_top, HuntingtonAlgebra.sup_compl, HuntingtonAlgebra.sup_comm, HuntingtonAlgebra.sup_assoc, HuntingtonAlgebra.compl_sup, HuntingtonAlgebra.compl_compl, HuntingtonAlgebra.compl_inj, HuntingtonAlgebra.huntington', HuntingtonAlgebra.top_sup_top, HuntingtonAlgebra.bot_sup_bot, HuntingtonAlgebra.bot_sup, HuntingtonAlgebra.sup_idem, HuntingtonAlgebra.sup_top, HuntingtonAlgebra.sup_compl_eq, HuntingtonAlgebra.inf_eq, HuntingtonAlgebra.inf_assoc, HuntingtonAlgebra.inf_comm, HuntingtonAlgebra.sup_inf_self, HuntingtonAlgebra.inf_sup_self, HuntingtonAlgebra.inf_compl, huntington
statement: formalized
proof: formalized
---

# Huntington's axioms for Boolean Algebras

`Cslib.Foundations.Order.Huntington`, in [Cslib/Foundations/Order/Huntington.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean), by Thomas Waring.

> In this file we derive an instance of Mathlib's `BooleanAlgebra` on an inhabited type, starting
> from operations of binary supremum `· ⊔ ·` and complementation `·ᶜ`, obeying the three axioms
> laid out in [Huntington1933a] and [Huntington1933b]:
>
> * Supremum is associative: `a ⊔ b ⊔ c = a ⊔ (b ⊔ c)`,
> * Supremum is commutative: `a ⊔ b = b ⊔ a`, and
> * Huntington's axiom: `(aᶜ ⊔ b)ᶜ ⊔ (aᶜ ⊔ bᶜ)ᶜ = a`.
>
> These axioms are packaged in the class `HuntingtonAlgebra`, which should only be used for its
> instance `HuntingtonAlgebra.instBooleanAlgebra`.
>
> ## References
>
> * [E. V. Huntington, "New Sets of Independent Postulates for the Algebra of Logic, With Special
>   Reference to Whitehead and Russell's Principia Mathematica"][Huntington1933a]
> * [E. V. Huntington, "Boolean Algebra. A Correction"][Huntington1933b]

`HuntingtonAlgebra` (class, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L35))

> A class for types obeying Huntington's axioms for Boolean algebras.

```lean
public class HuntingtonAlgebra (α : Type*) extends Max α, Compl α, Inhabited α,
    Std.Associative (α := α) (· ⊔ ·), Std.Commutative (α := α) (· ⊔ ·) where
  /-- Huntington's axiom. -/
  huntington (a b : α) : (aᶜ ⊔ b)ᶜ ⊔ (aᶜ ⊔ bᶜ)ᶜ = a
```

`HuntingtonAlgebra.compl_top` (lemma, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L49))

```lean
lemma compl_top : (⊤ : α)ᶜ = ⊥
```

`HuntingtonAlgebra.sup_compl` (lemma, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L51))

```lean
lemma sup_compl (a : α) : a ⊔ aᶜ = ⊤
```

`HuntingtonAlgebra.sup_comm` (lemma, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L57))

```lean
lemma sup_comm (a b : α) : a ⊔ b = b ⊔ a
```

`HuntingtonAlgebra.sup_assoc` (lemma, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L59))

```lean
lemma sup_assoc (a b c : α) : a ⊔ b ⊔ c = a ⊔ (b ⊔ c)
```

`HuntingtonAlgebra.compl_sup` (lemma, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L61))

```lean
lemma compl_sup (a : α) : aᶜ ⊔ a = ⊤
```

`HuntingtonAlgebra.compl_compl` (lemma, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L63))

```lean
lemma compl_compl (a : α) : aᶜᶜ = a
```

`HuntingtonAlgebra.compl_inj` (lemma, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L67))

```lean
lemma compl_inj : Function.Injective (·ᶜ : α → α)
```

`HuntingtonAlgebra.huntington'` (lemma, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L71))

```lean
lemma huntington' (a b : α) : (a ⊔ b)ᶜ ⊔ (a ⊔ bᶜ)ᶜ = aᶜ
```

`HuntingtonAlgebra.top_sup_top` (lemma, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L74))

```lean
lemma top_sup_top : (⊤ : α) ⊔ ⊤ = ⊤
```

`HuntingtonAlgebra.bot_sup_bot` (lemma, [line 81](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L81))

```lean
lemma bot_sup_bot : (⊥ : α) ⊔ ⊥ = ⊥
```

`HuntingtonAlgebra.bot_sup` (lemma, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L85))

```lean
lemma bot_sup (a : α) : ⊥ ⊔ a = a
```

`HuntingtonAlgebra.sup_idem` (lemma, [line 91](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L91))

```lean
lemma sup_idem (a : α) : a ⊔ a = a
```

`HuntingtonAlgebra.sup_top` (lemma, [line 98](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L98))

```lean
lemma sup_top (a : α) : a ⊔ ⊤ = ⊤
```

`HuntingtonAlgebra.sup_compl_eq` (lemma, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L101))

```lean
lemma sup_compl_eq (a b : α) : a ⊔ bᶜ = a ⊔ (a ⊔ b)ᶜ
```

`HuntingtonAlgebra.inf_eq` (lemma, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L107))

```lean
lemma inf_eq (a b : α) : a ⊓ b = (aᶜ ⊔ bᶜ)ᶜ
```

`HuntingtonAlgebra.inf_assoc` (lemma, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L109))

```lean
lemma inf_assoc (a b c : α) : a ⊓ b ⊓ c = a ⊓ (b ⊓ c)
```

`HuntingtonAlgebra.inf_comm` (lemma, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L111))

```lean
lemma inf_comm (a b : α) : a ⊓ b = b ⊓ a
```

`HuntingtonAlgebra.sup_inf_self` (lemma, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L113))

```lean
lemma sup_inf_self (a b : α) : a ⊔ (a ⊓ b) = a
```

`HuntingtonAlgebra.inf_sup_self` (lemma, [line 117](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L117))

```lean
lemma inf_sup_self (a b : α) : a ⊓ (a ⊔ b) = a
```

`HuntingtonAlgebra.inf_compl` (lemma, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L121))

```lean
lemma inf_compl (a : α) : a ⊓ aᶜ = ⊥
```

`huntington` (theorem, [line 143](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean#L143))

> Conversely, Boolean Algebras obey Huntington's axiom.

```lean
theorem huntington {α : Type*} [BooleanAlgebra α] (a b : α) : (aᶜ ⊔ b)ᶜ ⊔ (aᶜ ⊔ bᶜ)ᶜ = a
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Order/Huntington.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Huntington.lean)
