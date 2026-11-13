---
declaration: module
origin: cited
lean: ProbabilisticTheory.IsDerivation, ProbabilisticTheory.IsDerivation.zero, ProbabilisticTheory.IsDerivation.add, ProbabilisticTheory.IsDerivation.neg, ProbabilisticTheory.IsDerivation.smul
statement: formalized
proof: formalized
---

# Derivations

The module `PhyslibAlpha.ProbabilisticTheory.Algebra.Derivation`, [PhyslibAlpha/ProbabilisticTheory/Algebra/Derivation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Derivation.lean): 5 declarations, 1 with a docstring.

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

**`ProbabilisticTheory.IsDerivation`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Derivation.lean#L49).

> `D` is a derivation of the multiplication on `E`: `D (a b) = D a b + a D b`. Only a
> multiplication and a real module structure are assumed, so that it applies to normed spaces with a
> separate product.

```lean
def IsDerivation {E : Type*} [Mul E] [AddCommGroup E] [Module ℝ E] (D : E →ₗ[ℝ] E) :
    Prop
```

## B. Closure properties

**`ProbabilisticTheory.IsDerivation.zero`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Derivation.lean#L57).

```lean
lemma IsDerivation.zero : IsDerivation (0 : E →ₗ[ℝ] E)
```

**`ProbabilisticTheory.IsDerivation.add`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Derivation.lean#L60).

```lean
lemma IsDerivation.add {D₁ D₂ : E →ₗ[ℝ] E} (h₁ : IsDerivation D₁) (h₂ : IsDerivation D₂) :
    IsDerivation (D₁ + D₂)
```

**`ProbabilisticTheory.IsDerivation.neg`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Derivation.lean#L66).

```lean
lemma IsDerivation.neg {D : E →ₗ[ℝ] E} (h : IsDerivation D) : IsDerivation (-D)
```

**`ProbabilisticTheory.IsDerivation.smul`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Derivation.lean#L71).

```lean
lemma IsDerivation.smul [SMulCommClass ℝ E E] [IsScalarTower ℝ E E] (c : ℝ) {D : E →ₗ[ℝ] E}
    (h : IsDerivation D) : IsDerivation (c • D)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Algebra/Derivation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Algebra/Derivation.lean)
