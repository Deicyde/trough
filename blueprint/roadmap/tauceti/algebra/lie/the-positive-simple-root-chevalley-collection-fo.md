---
declaration: theorem
origin: cited
lean: TauCeti.G2ShortRoot.PrimeField.commutatorElement_positive_simple_eq_root_product, TauCeti.G2ShortRoot.IntegralToralClosure.commutatorElement_positive_simple_eq_root_product
statement: formalized
proof: formalized
---

# The positive-simple-root Chevalley collection formula over 𝔽₃

The four factors
have roots α₁+α₂, 2α₁+α₂, 3α₁+α₂, and 3α₁+2α₂, with their parameters normalized by
the displayed conjugating words. The formula includes nonreduced coefficient algebras.

```lean
TauCeti.G2ShortRoot.PrimeField.commutatorElement_positive_simple_eq_root_product.{v} (A : Type v)
  [CommRing A] [Algebra (ZMod 3) A] (a b : A) :
  have x := fun i t =>
    (TauCeti.G2ShortRoot.PrimeField.rootSubgroupPoints (Sum.inl i) A) (Multiplicative.ofAdd t);
  have n := fun i =>
    x i 1 *
        (TauCeti.G2ShortRoot.PrimeField.rootSubgroupPoints (Sum.inr i) A)
          (Multiplicative.ofAdd (-1)) *
      x i 1;
  ⁅x 0 a, x 1 b⁆ =
    n 1 * x 0 (-a * b) * (n 1)⁻¹ * (n 0 * n 1 * x 0 (a ^ 2 * b) * (n 0 * n 1)⁻¹) *
        (n 0 * x 1 (a ^ 3 * b) * (n 0)⁻¹) *
      (n 1 * n 0 * x 1 (2 * a ^ 3 * b ^ 2) * (n 1 * n 0)⁻¹)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.G2ShortRoot.PrimeField.commutatorElement_positive_simple_eq_root_product`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/G2/ShortRoot/PrimeField/RootRelations/Collection.html#TauCeti.G2ShortRoot.PrimeField.commutatorElement_positive_simple_eq_root_product).

## Other forms

**The positive-simple-root Chevalley collection formula in type G₂.** Formalized in Tau Ceti as [`TauCeti.G2ShortRoot.IntegralToralClosure.commutatorElement_positive_simple_eq_root_product`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/G2/ShortRoot/IntegralToralClosure/RootRelations/Collection.html#TauCeti.G2ShortRoot.IntegralToralClosure.commutatorElement_positive_simple_eq_root_product).

```lean
TauCeti.G2ShortRoot.IntegralToralClosure.commutatorElement_positive_simple_eq_root_product.{v}
  (A : Type v) [CommRing A] (a b : A) :
  have x := fun i t =>
    (TauCeti.G2ShortRoot.IntegralToralClosure.rootSubgroupPoints (Sum.inl i) A)
      (Multiplicative.ofAdd t);
  have n := fun i =>
    x i 1 *
        (TauCeti.G2ShortRoot.IntegralToralClosure.rootSubgroupPoints (Sum.inr i) A)
          (Multiplicative.ofAdd (-1)) *
      x i 1;
  ⁅x 0 a, x 1 b⁆ =
    n 1 * x 0 (-a * b) * (n 1)⁻¹ * (n 0 * n 1 * x 0 (a ^ 2 * b) * (n 0 * n 1)⁻¹) *
        (n 0 * x 1 (a ^ 3 * b) * (n 0)⁻¹) *
      (n 1 * n 0 * x 1 (2 * a ^ 3 * b ^ 2) * (n 1 * n 0)⁻¹)
```

## Sources

- [Tau Ceti documentation: `TauCeti.G2ShortRoot.PrimeField.commutatorElement_positive_simple_eq_root_product`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/G2/ShortRoot/PrimeField/RootRelations/Collection.html#TauCeti.G2ShortRoot.PrimeField.commutatorElement_positive_simple_eq_root_product)
- [Source of `TauCeti.G2ShortRoot.PrimeField.commutatorElement_positive_simple_eq_root_product` in TauCeti/Algebra/Lie/G2/ShortRoot/PrimeField/RootRelations/Collection.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/G2/ShortRoot/PrimeField/RootRelations/Collection.lean#L41)
