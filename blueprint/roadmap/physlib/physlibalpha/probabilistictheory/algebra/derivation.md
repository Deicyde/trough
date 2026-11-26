---
declaration: module
origin: cited
lean: PhyslibAlpha.ProbabilisticTheory.IsDerivation, PhyslibAlpha.ProbabilisticTheory.IsDerivation.zero, PhyslibAlpha.ProbabilisticTheory.IsDerivation.add, PhyslibAlpha.ProbabilisticTheory.IsDerivation.neg, PhyslibAlpha.ProbabilisticTheory.IsDerivation.smul
statement: formalized
proof: formalized
---

# Derivations

The module `PhyslibAlpha.ProbabilisticTheory.Algebra.Derivation`, [PhyslibAlpha/ProbabilisticTheory/Algebra/Derivation.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Algebra/Derivation.lean): 5 declarations, 1 with a docstring.

> Derivations of a bilinear multiplication and their closure under linear operations.

## i. Overview

> A derivation of a multiplication is a linear map `D` with `D (a b) = D a b + a D b`. The notion only
> needs a bilinear product, so it covers associative and Jordan derivations alike. Derivations form a
> real vector space.

## ii. Key results

> - `IsDerivation` : derivations.
> - `IsDerivation.add`, `IsDerivation.smul` : derivations form a vector space.

## iv. References

> * None.

## A. The Leibniz rule

**`PhyslibAlpha.ProbabilisticTheory.IsDerivation`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Algebra/Derivation.lean#L49).

> `D` is a derivation of the multiplication on `E`: `D (a b) = D a b + a D b`. Only a
> multiplication and a real module structure are assumed, so that it applies to normed spaces with a
> separate product.

```lean
def IsDerivation {E : Type*} [Mul E] [AddCommGroup E] [Module ℝ E] (D : E →ₗ[ℝ] E) :
    Prop
```

## B. Closure properties

**`PhyslibAlpha.ProbabilisticTheory.IsDerivation.zero`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Algebra/Derivation.lean#L57).

```lean
lemma IsDerivation.zero : IsDerivation (0 : E →ₗ[ℝ] E)
```

**`PhyslibAlpha.ProbabilisticTheory.IsDerivation.add`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Algebra/Derivation.lean#L60).

```lean
lemma IsDerivation.add {D₁ D₂ : E →ₗ[ℝ] E} (h₁ : IsDerivation D₁) (h₂ : IsDerivation D₂) :
    IsDerivation (D₁ + D₂)
```

**`PhyslibAlpha.ProbabilisticTheory.IsDerivation.neg`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Algebra/Derivation.lean#L66).

```lean
lemma IsDerivation.neg {D : E →ₗ[ℝ] E} (h : IsDerivation D) : IsDerivation (-D)
```

**`PhyslibAlpha.ProbabilisticTheory.IsDerivation.smul`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Algebra/Derivation.lean#L71).

```lean
lemma IsDerivation.smul [SMulCommClass ℝ E E] [IsScalarTower ℝ E E] (c : ℝ) {D : E →ₗ[ℝ] E}
    (h : IsDerivation D) : IsDerivation (c • D)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Algebra/Derivation.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/Algebra/Derivation.lean)
