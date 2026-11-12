---
catalog: module
lean: PFunctor.ext, PFunctor.const, PFunctor.const_apply, PFunctor.monomial, PFunctor.monomial_A, PFunctor.monomial_B, PFunctor.instZeroPFunctor, PFunctor.instIsEmptyZeroPFunctor, PFunctor.instOnePFunctor, PFunctor.instUniqueOneA, PFunctor.instIsEmptyOneB, PFunctor.C, PFunctor.linear, PFunctor.selfMonomial, PFunctor.purePower, PFunctor.y, PFunctor.C_pempty, PFunctor.C_punit, PFunctor.linear_punit, PFunctor.selfMonomial_punit, PFunctor.purePower_punit, PFunctor.add, PFunctor.instHAddPFunctor, PFunctor.add_eq_add, PFunctor.prod, PFunctor.instHMulPFunctor, PFunctor.prod_eq_mul, PFunctor.Unary, PFunctor.Unary.fun_eq_const, PFunctor.DecidableEqChildren, PFunctor.mkUnary
statement: formalized
proof: formalized
---

# Polynomial Functors

`Cslib.Foundations.Data.PFunctor.Basic`, in [Cslib/Foundations/Data/PFunctor/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean), by Fabrizio Montesi, Devon Tuma, Quang Dao.

> Definitions of common `PFunctor` constructions:
> - `monomial A B`: constant direction `B` for any shape `a : A`
> - `P + Q`: shapes are a disjoint sum, directions are defined by sum elimination on `a : P.A ⊕ Q.A`
> - `P * Q`: shapes are pairs of underlying shapes, directions are a disjoint sum over both shapes.
>
> Special cases `C`, `linear`, `selfMonomial`, `purePower`, the indeterminate `y`,
> and canonical choices of `0` and `1` are defined as abbreviations or instances over `monomial`.
> The scoped notations `A y^ B` and `y^ B` denote `monomial A B` and `purePower B`, respectively.
>
> The child-map API includes `const`, `Unary`, and `DecidableEqChildren`.

`PFunctor.ext` (theorem, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L36))

> Two polynomial functors are equal if their head types are equal and their child types
> agree over that equality.

```lean
theorem ext {P Q : PFunctor.{uA, uB}} (h : P.A = Q.A) (h' : ∀ a, P.B a = Q.B (h ▸ a)) :
    P = Q
```

`PFunctor.const` (definition, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L42))

> The constant child map for `a`.

```lean
def const {P : PFunctor} (a : P.A) (x : α) : P.B a → α
```

`PFunctor.const_apply` (theorem, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L45))

```lean
theorem const_apply {P : PFunctor} (a : P.A) (x : α) (i : P.B a) : PFunctor.const a x i = x
```

`PFunctor.monomial` (abbreviation, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L50))

> The monomial `PFunctor` with head type `A` and constant `B` for any `a : A`.

```lean
abbrev monomial (A : Type uA) (B : Type uB) : PFunctor
```

`PFunctor.monomial_A` (lemma, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L54))

```lean
lemma monomial_A (A : Type uA) (B : Type uB) : (monomial A B).A = A
```

`PFunctor.monomial_B` (lemma, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L56))

```lean
lemma monomial_B (A : Type uA) (B : Type uB) (a : (monomial A B).A) :
    (monomial A B).B a = B
```

`PFunctor.instZeroPFunctor` (instance, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L65))

> The zero polynomial functor, defined as `A = PEmpty` and `B _ = PEmpty`, is the identity with
> respect to sum (up to equivalence).

```lean
instance instZeroPFunctor : Zero PFunctor
```

`PFunctor.instIsEmptyZeroPFunctor` (instance, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L69))

```lean
instance instIsEmptyZeroPFunctor : IsEmpty (0 : PFunctor.{uA, 0}).A
```

`PFunctor.instOnePFunctor` (instance, [line 78](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L78))

> The unit polynomial functor, defined as `A = PUnit` and `B _ = PEmpty`, is the identity with
> respect to product (up to equivalence).

```lean
instance instOnePFunctor : One PFunctor
```

`PFunctor.instUniqueOneA` (instance, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L80))

```lean
instance instUniqueOneA : Unique (1 : PFunctor.{uA, 0}).A
```

`PFunctor.instIsEmptyOneB` (instance, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L82))

```lean
instance instIsEmptyOneB (a : (1 : PFunctor.{uA, uB}).A) : IsEmpty ((1 : PFunctor.{uA, uB}).B a)
```

`PFunctor.C` (abbreviation, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L88))

> The constant polynomial functor `P(y) = A y^ PEmpty = A`.

```lean
abbrev C (A : Type uA) : PFunctor
```

`PFunctor.linear` (abbreviation, [line 91](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L91))

> The linear polynomial functor `P(y) = A y`.

```lean
abbrev linear (A : Type uA) : PFunctor
```

`PFunctor.selfMonomial` (abbreviation, [line 94](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L94))

> The self-monomial polynomial functor `P(y) = S y^ S`.

```lean
abbrev selfMonomial (S : Type uA) : PFunctor.{uA, uA}
```

`PFunctor.purePower` (abbreviation, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L97))

> The pure-power polynomial functor `y^ B`, representable on `B`.

```lean
abbrev purePower (B : Type uB) : PFunctor
```

`PFunctor.y` (abbreviation, [line 103](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L103))

> The indeterminate polynomial functor `P(y) = y`, the identity with respect to
> composition and tensor product (up to equivalence).

```lean
abbrev y : PFunctor
```

`PFunctor.C_pempty` (lemma, [line 110](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L110))

```lean
lemma C_pempty : C PEmpty = 0
```

`PFunctor.C_punit` (lemma, [line 112](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L112))

```lean
lemma C_punit : C PUnit = 1
```

`PFunctor.linear_punit` (lemma, [line 114](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L114))

```lean
lemma linear_punit : linear PUnit = y
```

`PFunctor.selfMonomial_punit` (lemma, [line 116](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L116))

```lean
lemma selfMonomial_punit : selfMonomial PUnit = y
```

`PFunctor.purePower_punit` (lemma, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L118))

```lean
lemma purePower_punit : purePower PUnit = y
```

`PFunctor.add` (definition, [line 127](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L127))

> The sum of two polynomial functors `P` and `Q`, written as `P + Q`,
> defined as the sum of the head types and the dependent sum recursor for the child types.
>
> The child universes must agree. The named spelling `P.add Q` can elaborate in contexts where
> `P + Q` fails to infer universes, such as under `PFunctor.W`; see `CslibTests.PFunctor`.

```lean
def add (P : PFunctor.{uA₁, uB}) (Q : PFunctor.{uA₂, uB}) :
PFunctor.{max uA₁ uA₂, uB}
```

`PFunctor.instHAddPFunctor` (instance, [line 131](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L131))

```lean
instance instHAddPFunctor :
HAdd PFunctor.{uA₁, uB} PFunctor.{uA₂, uB} PFunctor.{max uA₁ uA₂, uB}
```

`PFunctor.add_eq_add` (lemma, [line 137](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L137))

```lean
lemma add_eq_add (P : PFunctor.{uA₁, uB}) (Q : PFunctor.{uA₂, uB}) :
P.add Q = P + Q
```

`PFunctor.prod` (definition, [line 146](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L146))

> The product of two polynomial functors `P` and `Q`, written as `P * Q`,
> defined as the product of the head types and the sum of the child types.

```lean
def prod (P : PFunctor.{uA₁, uB₁}) (Q : PFunctor.{uA₂, uB₂}) :
PFunctor.{max uA₁ uA₂, max uB₁ uB₂}
```

`PFunctor.instHMulPFunctor` (instance, [line 149](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L149))

```lean
instance instHMulPFunctor :
HMul PFunctor.{uA₁, uB₁} PFunctor.{uA₂, uB₂} PFunctor.{max uA₁ uA₂, max uB₁ uB₂}
```

`PFunctor.prod_eq_mul` (lemma, [line 153](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L153))

```lean
lemma prod_eq_mul (P : PFunctor.{uA₁, uB₁}) (Q : PFunctor.{uA₂, uB₂}) :
P.prod Q = P * Q
```

`PFunctor.Unary` (class, [line 161](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L161))

> A polynomial functor is unary if all child types have exactly one element.

```lean
class Unary (P : PFunctor) where
  unary (a : P.A) : Unique (P.B a)
```

`PFunctor.Unary.fun_eq_const` (theorem, [line 166](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L166))

```lean
theorem Unary.fun_eq_const [Unary P]
    (a : P.A) (f : P.B a → α) : f = fun _ => f default
```

`PFunctor.DecidableEqChildren` (class, [line 172](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L172))

> A polynomial functor has children with decidable equality.

```lean
class DecidableEqChildren (P : PFunctor) where
  decidableEq (a : P.A) : DecidableEq (P.B a)
```

`PFunctor.mkUnary` (abbreviation, [line 182](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean#L182))

> Constructs a unary polynomial functor.

```lean
abbrev mkUnary (A : Type*) : PFunctor
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Data/PFunctor/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Basic.lean)
