---
catalog: module
lean: HuntingtonAlgebra
statement: formalized
proof: formalized
---

# Huntington's axioms for Boolean Algebras

`Cslib.Foundations.Order.Huntington`, in [Cslib/Foundations/Order/Huntington.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Order/Huntington.lean), by Thomas Waring.

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

`HuntingtonAlgebra` (class, [line 35](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Order/Huntington.lean#L35))

> A class for types obeying Huntington's axioms for Boolean algebras.

```lean
public class HuntingtonAlgebra (α : Type*) extends Max α, Compl α, Inhabited α,
    Std.Associative (α := α) (· ⊔ ·), Std.Commutative (α := α) (· ⊔ ·) where
  /-- Huntington's axiom. -/
  huntington (a b : α) : (aᶜ ⊔ b)ᶜ ⊔ (aᶜ ⊔ bᶜ)ᶜ = a
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Order/Huntington.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Order/Huntington.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.Order.Huntington.json)
