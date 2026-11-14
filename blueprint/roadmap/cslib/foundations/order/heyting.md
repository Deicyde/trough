---
catalog: module
lean: WithBot.himp, WithBot.bot_himp, WithBot.coe_himp_bot, WithBot.coe_himp, WithBot.heytingAlgebra, WithTop.coheytingAlgebra, WithBot.compl_coe
statement: formalized
proof: formalized
---

# Utilities for Heyting algebras

`Cslib.Foundations.Order.Heyting`, in [Cslib/Foundations/Order/Heyting.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Heyting.lean), by Thomas Waring.

`WithBot.himp` (abbreviation, [line 23](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Heyting.lean#L23))

> Heyting implication for `WithBot α`. Not an instance to avoid diamonds arising from
> `LinearOrder.toBiheytingAlgebra`.

```lean
protected abbrev himp (α : Type*) [HImp α] [Top α] : HImp (WithBot α)
```

`WithBot.bot_himp` (lemma, [line 27](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Heyting.lean#L27))

```lean
lemma bot_himp {α : Type*} [HImp α] [Top α] (a : WithBot α) :
  letI := WithBot.himp α; ⊥ ⇨ a = ⊤
```

`WithBot.coe_himp_bot` (lemma, [line 31](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Heyting.lean#L31))

```lean
lemma coe_himp_bot {α : Type*} [HImp α] [Top α] (a : α) :
  letI := WithBot.himp α; (a : WithBot α) ⇨ ⊥ = ⊥
```

`WithBot.coe_himp` (lemma, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Heyting.lean#L35))

```lean
lemma coe_himp {α : Type*} [HImp α] [Top α] (a b : α) :
  letI := WithBot.himp α; ↑(a ⇨ b : α) = (a : WithBot α) ⇨ b
```

`WithBot.heytingAlgebra` (abbreviation, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Heyting.lean#L40))

> Heyting algebra structure on `WithBot α`. Not an instance to avoid diamonds arising from
> `LinearOrder.toBiheytingAlgebra`.

```lean
protected abbrev heytingAlgebra (α : Type*) [GeneralizedHeytingAlgebra α] :
    HeytingAlgebra (WithBot α)
```

`WithTop.coheytingAlgebra` (abbreviation, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Heyting.lean#L59))

> Coheyting algebra structure on `WithTop α`. Not an instance to avoid diamonds arising from
> `LinearOrder.toBiheytingAlgebra`.

```lean
protected abbrev _root_.WithTop.coheytingAlgebra (α : Type*) [GeneralizedCoheytingAlgebra α] :
    CoheytingAlgebra (WithTop α)
```

`WithBot.compl_coe` (lemma, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Heyting.lean#L76))

```lean
lemma compl_coe {α : Type*} [GeneralizedHeytingAlgebra α] (a : α) :
  letI := WithBot.heytingAlgebra α; (a : WithBot α)ᶜ = ⊥
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Order/Heyting.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Order/Heyting.lean)
