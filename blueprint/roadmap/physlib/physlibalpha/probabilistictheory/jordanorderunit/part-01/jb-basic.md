---
declaration: module
origin: cited
lean: ProbabilisticTheory.NormedJordanAlgebra, ProbabilisticTheory.JBAlgebra, ProbabilisticTheory.IsJBOrderUnit, ProbabilisticTheory.JBAlgebra.norm_mul_self_le_norm_mul_self_add_mul_self, ProbabilisticTheory.JBAlgebra.norm_mul_self_of_norm_eq_one, ProbabilisticTheory.JBAlgebra.eq_zero_of_mul_self_eq_zero, ProbabilisticTheory.JBAlgebra.mul_self_eq_zero_iff, ProbabilisticTheory.JBAlgebra.norm_eq_orderUnitNorm
statement: formalized
proof: formalized
---

# Normed Jordan algebras and JB-algebras

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.JB.Basic`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean): 25 declarations (6 instances with no name), 25 with a docstring.

> Normed Jordan algebras, JB-algebras and ordered JB-algebras, with their basic properties.

## i. Overview

> `JBAlgebra` is a Banach Jordan algebra satisfying the JB axioms
> (Hanche-Olsen–Størmer, *Jordan Operator Algebras*, Def. 3.1.1):
>
> - `‖a ∘ b‖ ≤ ‖a‖ ‖b‖`;
> - `‖a ∘ a‖ = ‖a‖ ^ 2`;
> - `‖a ∘ a‖ ≤ ‖a ∘ a + b ∘ b‖`.
>
> It carries no order. `IsJBOrderUnit` is the ordered version: an order-unit space whose order-unit
> norm is the given norm.
>
> `NormedJordanAlgebra` bundles the ring, module and metric structure of a normed Jordan algebra
> in one class, and `JBAlgebra` adds completeness and the JB axioms.

## ii. Key results

> - `NormedJordanAlgebra E` : a real normed unital Jordan algebra.
> - `JBAlgebra E` : a JB-algebra.
> - `JBAlgebra.norm_mul_self_le_norm_mul_self_add_mul_self` : monotonicity of the norm on sums of
>   squares.
> - `IsJBOrderUnit E` : a JB-algebra that is an order-unit space with the order-unit norm.
> - `JBAlgebra.mul_self_eq_zero_iff` : `a ∘ a = 0` iff `a = 0`.
> - `JBAlgebra.isClosed_nonneg` : the positive cone of an ordered JB-algebra is closed.
> - `JBAlgebra.instIsFormallyReal` : an ordered JB-algebra is formally real.

## iv. References

> * Hanche-Olsen–Størmer, *Jordan Operator Algebras*, Def. 3.1.1.

## A. Normed Jordan algebras

**`ProbabilisticTheory.NormedJordanAlgebra`**, a class, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L64).

> A real normed unital Jordan algebra.

```lean
class NormedJordanAlgebra (E : Type*) extends Norm E, MetricSpace E, NonAssocCommRing E,
    Module ℝ E where
  /-- The metric is induced by the additive norm. -/
  dist_eq : ∀ x y : E, dist x y = ‖-x + y‖
  /-- Real scalar multiplication is norm-bounded. -/
  norm_smul_le : ∀ (r : ℝ) (x : E), ‖r • x‖ ≤ ‖r‖ * ‖x‖
  /-- Real scalars commute with right Jordan multiplication. -/
  smul_comm : ∀ (r : ℝ) (x y : E), r • (x * y) = x * (r • y)
  /-- Real scalar multiplication is a tower over Jordan multiplication. -/
  smul_assoc : ∀ (r : ℝ) (x y : E), (r • x) * y = r • (x * y)
  /-- The commutative Jordan identity. -/
  jordan_identity : ∀ x y : E, x * y * (x * x) = x * (y * (x * x))
  /-- The Jordan product is norm-submultiplicative. -/
  norm_mul_le : ∀ x y : E, ‖x * y‖ ≤ ‖x‖ * ‖y‖
```

**An instance with no name**, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L82).

> The coherent additive metric structure underlying a normed Jordan algebra.

```lean
instance {E : Type*} [s : NormedJordanAlgebra E] : NormedAddCommGroup E
```

**An instance with no name**, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L85).

> The coherent real normed-space structure underlying a normed Jordan algebra.

```lean
instance {E : Type*} [s : NormedJordanAlgebra E] : NormedSpace ℝ E
```

**An instance with no name**, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L89).

> Scalar actions commute with Jordan multiplication.

```lean
instance {E : Type*} [s : NormedJordanAlgebra E] : SMulCommClass ℝ E E
```

**An instance with no name**, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L92).

> Scalar actions form a tower over Jordan multiplication.

```lean
instance {E : Type*} [s : NormedJordanAlgebra E] : IsScalarTower ℝ E E
```

**An instance with no name**, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L95).

> A normed Jordan algebra satisfies Mathlib's commutative Jordan predicate.

```lean
instance {E : Type*} [s : NormedJordanAlgebra E] : IsCommJordan E
```

## B. JB-algebras

**`ProbabilisticTheory.JBAlgebra`**, a class, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L101).

> A JB-algebra: a complete real normed Jordan algebra whose norm realizes squares exactly and is
> monotone under addition of squares. No order is chosen at this analytic level.

```lean
class JBAlgebra (E : Type*) [NormedJordanAlgebra E] : Prop extends CompleteSpace E where
  /-- Squares realize the norm exactly: the JB (Jordan–Banach) axiom. -/
  norm_mul_self : ∀ a : E, ‖a * a‖ = ‖a‖ ^ 2
  /-- Order-norm compatibility: a square's norm cannot exceed the norm of its sum with another
  square. -/
  norm_mul_self_le_add : ∀ a b : E, ‖a * a‖ ≤ ‖a * a + b * b‖
```

**`ProbabilisticTheory.IsJBOrderUnit`**, a class, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L110).

> A coherent ordered realization of a JB-algebra. It bundles the analytic Jordan algebra,
> order-unit structure, positive-square compatibility, and completeness without instance diamonds.

```lean
class IsJBOrderUnit (E : Type*) extends NormedJordanAlgebra E, IsJordanOrderUnit E,
    ArchimedeanOrderUnitSpace E, JBAlgebra E where
  norm_eq_orderUnitNorm : ∀ x : E, ‖x‖ = ArchimedeanOrderUnitSpace.orderUnitNorm x
```

## C. Basic consequences

**`ProbabilisticTheory.JBAlgebra.norm_mul_self_le_norm_mul_self_add_mul_self`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L123).

> `‖a ∘ a‖ ≤ ‖a ∘ a + b ∘ b‖`.

```lean
lemma norm_mul_self_le_norm_mul_self_add_mul_self (a b : E) : ‖a * a‖ ≤ ‖a * a + b * b‖
```

**`ProbabilisticTheory.JBAlgebra.norm_mul_self_of_norm_eq_one`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L127).

> The Jordan square of a norm-`1` element has norm `1`.

```lean
lemma norm_mul_self_of_norm_eq_one {a : E} (ha : ‖a‖ = 1) : ‖a * a‖ = 1
```

**`ProbabilisticTheory.JBAlgebra.eq_zero_of_mul_self_eq_zero`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L131).

> A Jordan square in a JB-algebra is zero only when its root is zero.

```lean
lemma eq_zero_of_mul_self_eq_zero {a : E} (ha : a * a = 0) : a = 0
```

**`ProbabilisticTheory.JBAlgebra.mul_self_eq_zero_iff`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L138).

> The zero-square criterion as an equivalence, convenient when transporting formal reality to
> subalgebras and quotients.

```lean
lemma mul_self_eq_zero_iff {a : E} : a * a = 0 ↔ a = 0
```

### C.1. Ordered JB-algebras

**`ProbabilisticTheory.JBAlgebra.norm_eq_orderUnitNorm`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L154).

> In an ordered JB realization, the analytic norm is exactly the order-unit norm.

```lean
lemma norm_eq_orderUnitNorm (x : E) : ‖x‖ = ArchimedeanOrderUnitSpace.orderUnitNorm x
```

**`ProbabilisticTheory.JBAlgebra.withOrderUnitNormIsometryEquiv`**, a def, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L158).

> The identity map from the order-unit-norm copy to a JB algebra is an isometry.

```lean
noncomputable def withOrderUnitNormIsometryEquiv : WithOrderUnitNorm E ≃ₗᵢ[ℝ] E
```

**An instance with no name**, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L163).

> A JB algebra is complete in its order-unit norm, since that norm is its JB norm.

```lean
instance : CompleteSpace (WithOrderUnitNorm E)
```

**`ProbabilisticTheory.JBAlgebra.norm_le_iff_order_bounds`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L169).

> A nonnegative scalar bounds the analytic JB norm exactly when its order-unit multiple bounds
> the observable on both sides. This is the public norm/order interface for an ordered JB algebra.

```lean
lemma norm_le_iff_order_bounds {x : E} {r : ℝ} (hr : 0 ≤ r) :
    ‖x‖ ≤ r ↔ -(r • (1 : E)) ≤ x ∧ x ≤ r • (1 : E)
```

**`ProbabilisticTheory.JBAlgebra.norm_le_one_of_zero_le_of_le_one`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L180).

> The unit interval is contained in the analytic closed unit ball of an ordered JB algebra.

```lean
lemma norm_le_one_of_zero_le_of_le_one {x : E} (hx : 0 ≤ x) (hxu : x ≤ 1) : ‖x‖ ≤ 1
```

**`ProbabilisticTheory.JBAlgebra.isClosed_nonneg`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L191).

> The positive cone is closed for the supplied JB norm.  This transports the order-unit
> closedness argument to the analytic norm through `norm_eq_orderUnitNorm`, and is the limit step
> needed by intrinsic square-root approximations.

```lean
lemma isClosed_nonneg : IsClosed {x : E | 0 ≤ x}
```

**`ProbabilisticTheory.JBAlgebra.isSumSq_nonneg`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L225).

> Every finite sum of Jordan squares is positive.

```lean
lemma isSumSq_nonneg {s : E} (hs : IsSumSq s) : 0 ≤ s
```

**`ProbabilisticTheory.JBAlgebra.no_mul_self_eq_neg_one`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L233).

> A JB-algebra has no square root of `-1`.  This elementary ordered consequence is the
> key algebraic obstruction separating the real JB one-generator algebra from arbitrary real
> uniform Banach algebras (where the real spectrum may be empty).

```lean
lemma no_mul_self_eq_neg_one [Nontrivial E] (a : E) : a * a ≠ -1
```

**`ProbabilisticTheory.JBAlgebra.add_mul_self_eq_zero_iff`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L244).

> A sum of two Jordan squares can vanish only when both roots vanish.  This is the
> two-square form of formal reality and is useful when analysing quadratic real factors in the
> one-generator resolvent.

```lean
lemma add_mul_self_eq_zero_iff {a b : E} :
    a * a + b * b = 0 ↔ a = 0 ∧ b = 0
```

**`ProbabilisticTheory.JBAlgebra.mul_self_add_one_ne_zero`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L255).

> The positive quadratic factor `a² + 1` cannot vanish in a nontrivial JB-algebra.

```lean
lemma mul_self_add_one_ne_zero [Nontrivial E] (a : E) : a * a + 1 ≠ 0
```

**`ProbabilisticTheory.JBAlgebra.instIsFormallyReal`**, an instance, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L261).

> A JB-algebra is formally real: a sum of squares vanishes only if every term does.

```lean
noncomputable instance instIsFormallyReal : IsFormallyReal E
```

**`ProbabilisticTheory.JBAlgebra.toWithOrderUnitNormLinearIsometryEquiv`**, a def, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L269).

> In an ordered JB-algebra the norm is the order-unit norm, as a linear isometric equivalence.

```lean
noncomputable def toWithOrderUnitNormLinearIsometryEquiv :
    E ≃ₗᵢ[ℝ] WithOrderUnitNorm E
```

**`ProbabilisticTheory.JBAlgebra.completeWithOrderUnitNorm`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean#L277).

> An ordered JB-algebra is complete for its order-unit norm.

```lean
lemma completeWithOrderUnitNorm : CompleteSpace (WithOrderUnitNorm E)
```

## Depends on

- [Jordan order-unit spaces](basic.md)
- [The canonical normed copy of an order-unit space](../../orderunit/normed.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Basic.lean)
