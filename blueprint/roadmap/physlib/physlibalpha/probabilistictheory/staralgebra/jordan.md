---
declaration: module
origin: cited
lean: selfAdjoint.anticommutator, selfAdjoint.coe_anticommutator, selfAdjoint.jordanMul, selfAdjoint.val_jordanMul, selfAdjoint.jordanMul_comm, selfAdjoint.one_jordanMul, selfAdjoint.jordanMul_one, selfAdjoint.jordanMul_add_right
statement: formalized
proof: formalized
---

# The Jordan product of observables

The module `PhyslibAlpha.ProbabilisticTheory.StarAlgebra.Jordan`, [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean): 27 declarations, 20 with a docstring.

> The Jordan product ½ (a b + b a) makes the self-adjoint elements a commutative Jordan ring.

## i. Overview

> The product of two self-adjoint elements is self-adjoint only when they commute, but the symmetrized
> product `a ∘ b = ½ (a b + b a)` is always self-adjoint. It is commutative and satisfies the Jordan
> identity, so the observables form a Jordan algebra. The product is a scoped instance on `selfAdjoint
> A`, since for commutative `A` Mathlib already gives `selfAdjoint A` the ordinary product.

## ii. Key results

> - `selfAdjoint.jordanMul` : the Jordan product `½ (a b + b a)`.
> - `selfAdjoint.jordanMul_comm` : the Jordan product is commutative.
> - `selfAdjoint.jordanMul_jordanMul_jordanMul_self` : the Jordan identity.

## iv. References

> * None.

## A. The anticommutator

**`selfAdjoint.anticommutator`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L56).

> The unnormalized anticommutator, retained as a low-level formula while `jordanMul` is the
> canonical normalized Jordan product.

```lean
def anticommutator (a b : selfAdjoint A) : selfAdjoint A
```

**`selfAdjoint.coe_anticommutator`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L62).

```lean
lemma coe_anticommutator (a b : selfAdjoint A) :
    ((anticommutator a b : selfAdjoint A) : A) = (a : A) * (b : A) + (b : A) * (a : A)
```

## B. The normalized Jordan product

**`selfAdjoint.jordanMul`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L71).

> The normalized Jordan product of two self-adjoint elements,
> `a ∘ b := ½(ab + ba)`. It is self-adjoint regardless of whether `a` and `b` commute, since
> `star (a * b + b * a) = star b * star a + star a * star b = b * a + a * b`.

```lean
noncomputable def jordanMul (a b : selfAdjoint A) : selfAdjoint A
```

**`selfAdjoint.val_jordanMul`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L75).

```lean
lemma val_jordanMul (a b : selfAdjoint A) :
    ((jordanMul a b : selfAdjoint A) : A) =
      (2 : ℝ)⁻¹ • ((a : A) * (b : A) + (b : A) * (a : A))
```

**`selfAdjoint.jordanMul_comm`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L81).

> The Jordan product is commutative.

```lean
lemma jordanMul_comm (a b : selfAdjoint A) : jordanMul a b = jordanMul b a
```

**`selfAdjoint.one_jordanMul`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L86).

> The unit of the ambient algebra is a unit for the normalized Jordan product.

```lean
lemma one_jordanMul (a : selfAdjoint A) : jordanMul 1 a = a
```

**`selfAdjoint.jordanMul_one`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L94).

> The normalized Jordan product has the same unit in its right argument.

```lean
lemma jordanMul_one (a : selfAdjoint A) : jordanMul a 1 = a
```

## C. Additivity, scalars and the Jordan identity

**`selfAdjoint.jordanMul_add_right`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L100).

> The Jordan product distributes over addition in its right argument.

```lean
lemma jordanMul_add_right (a b c : selfAdjoint A) :
    jordanMul a (b + c) = jordanMul a b + jordanMul a c
```

**`selfAdjoint.jordanMul_add_left`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L107).

> The Jordan product distributes over addition in its left argument.

```lean
lemma jordanMul_add_left (a b c : selfAdjoint A) :
    jordanMul (a + b) c = jordanMul a c + jordanMul b c
```

**`selfAdjoint.anticommutator_smul_left`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L112).

```lean
lemma anticommutator_smul_left [SMulCommClass ℝ A A] [IsScalarTower ℝ A A]
    (c : ℝ) (a b : selfAdjoint A) :
    anticommutator (c • a) b = c • anticommutator a b
```

**`selfAdjoint.anticommutator_smul_right`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L118).

```lean
lemma anticommutator_smul_right [SMulCommClass ℝ A A] [IsScalarTower ℝ A A]
    (a : selfAdjoint A) (c : ℝ) (b : selfAdjoint A) :
    anticommutator a (c • b) = c • anticommutator a b
```

**`selfAdjoint.anticommutator_identity`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L125).

```lean
lemma anticommutator_identity (a b : selfAdjoint A) :
    anticommutator (anticommutator a b) (anticommutator a a) =
      anticommutator a (anticommutator b (anticommutator a a))
```

**`selfAdjoint.jordanMul_jordanMul_jordanMul_self`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L135).

> The Jordan identity: `∘`-multiplication by `a` and by `a ∘ a` commute, i.e.
> `(a ∘ b) ∘ (a ∘ a) = a ∘ (b ∘ (a ∘ a))`. This is the "weak associativity" law that survives
> symmetrization of a possibly non-commutative, associative product.

```lean
lemma jordanMul_jordanMul_jordanMul_self [SMulCommClass ℝ A A] [IsScalarTower ℝ A A]
    (a b : selfAdjoint A) :
    jordanMul (jordanMul a b) (jordanMul a a) = jordanMul a (jordanMul b (jordanMul a a))
```

## D. The Jordan product as a multiplication

**`selfAdjoint.instMul`**, an instance, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L145).

> The Jordan product as a scoped multiplication on `selfAdjoint A`.

```lean
noncomputable scoped instance instMul : Mul (selfAdjoint A)
```

**`selfAdjoint.mul_def`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L148).

```lean
lemma mul_def (a b : selfAdjoint A) : a * b = jordanMul a b
```

**`selfAdjoint.coe_mul`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L152).

> Coercing the canonical Jordan product back to the ambient algebra gives the normalized
> anticommutator.

```lean
lemma coe_mul (a b : selfAdjoint A) :
    ((a * b : selfAdjoint A) : A) =
      (2 : ℝ)⁻¹ • ((a : A) * (b : A) + (b : A) * (a : A))
```

**`selfAdjoint.jordanMul_smul_left`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L158).

> Real scalars pull out of the left argument of the normalized Jordan product.

```lean
lemma jordanMul_smul_left [SMulCommClass ℝ A A] [IsScalarTower ℝ A A]
    (c : ℝ) (a b : selfAdjoint A) : jordanMul (c • a) b = c • jordanMul a b
```

**`selfAdjoint.jordanMul_smul_right`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L165).

> Real scalars pull out of the right argument of the normalized Jordan product.

```lean
lemma jordanMul_smul_right [SMulCommClass ℝ A A] [IsScalarTower ℝ A A]
    (a : selfAdjoint A) (c : ℝ) (b : selfAdjoint A) :
    jordanMul a (c • b) = c • jordanMul a b
```

**`selfAdjoint.jordanMul_jordanMul_right`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L173).

> Expanding one right-nested Jordan product produces a common factor `1 / 4` and a nested
> unnormalized anticommutator. This is useful for associative calculations in concrete
> realizations while keeping the normalized Jordan product canonical.

```lean
lemma jordanMul_jordanMul_right [SMulCommClass ℝ A A] [IsScalarTower ℝ A A]
    (a b x : selfAdjoint A) :
    jordanMul a (jordanMul b x) =
      ((2 : ℝ)⁻¹ * (2 : ℝ)⁻¹) • anticommutator a (anticommutator b x)
```

## E. The Jordan ring structure

**`selfAdjoint.jordanMul_zero`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L186).

```lean
lemma jordanMul_zero (a : selfAdjoint A) : jordanMul a 0 = 0
```

**`selfAdjoint.instNonUnitalNonAssocCommRing`**, an instance, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L192).

> The normalized product gives the self-adjoint part its canonical commutative,
> nonassociative ring structure.

```lean
noncomputable scoped instance instNonUnitalNonAssocCommRing :
    NonUnitalNonAssocCommRing (selfAdjoint A)
```

**`selfAdjoint.instNonAssocRing`**, an instance, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L205).

> The canonical Jordan product is unital with the inherited self-adjoint unit. Bundling this as
> `NonAssocCommRing` prevents stronger layers from carrying an unrelated `One` plus duplicated unit
> laws.

```lean
noncomputable scoped instance instNonAssocRing : NonAssocRing (selfAdjoint A)
```

**`selfAdjoint.instNonAssocCommRing`**, an instance, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L221).

> The coherent unital commutative nonassociative ring structure on the self-adjoint part.

```lean
noncomputable scoped instance instNonAssocCommRing : NonAssocCommRing (selfAdjoint A)
```

**`selfAdjoint.instSMulCommClass`**, an instance, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L226).

> Real scalar multiplication commutes with Jordan multiplication.

```lean
scoped instance instSMulCommClass : SMulCommClass ℝ (selfAdjoint A) (selfAdjoint A)
```

**`selfAdjoint.instIsScalarTower`**, an instance, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L230).

> Real scalar multiplication is a tower over Jordan multiplication.

```lean
scoped instance instIsScalarTower : IsScalarTower ℝ (selfAdjoint A) (selfAdjoint A)
```

**`selfAdjoint.instIsCommJordan`**, an instance, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L236).

> The Jordan product makes `selfAdjoint A` a commutative Jordan ring, in the sense of mathlib's
> `IsCommJordan`: this is the connection from the abstract axioms in `Mathlib.Algebra.Jordan.Basic`
> to the self-adjoint elements of an associative `StarRing`.

```lean
scoped instance instIsCommJordan : IsCommJordan (selfAdjoint A)
```

## F. The Jordan product of observables

**`ProbabilisticTheory.Observable.jordanMul`**, an abbrev, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean#L248).

> The Jordan product of observables.

```lean
noncomputable abbrev Observable.jordanMul {A : Type*} [Ring A] [StarRing A] [Module ℝ A]
    [StarModule ℝ A] (a b : Observable A) :
    Observable A
```

## Depends on

- [Observables](observable.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Jordan.lean)
