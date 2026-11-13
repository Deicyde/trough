---
declaration: module
origin: cited
lean: selfAdjoint.lieMul, selfAdjoint.val_lieMul, selfAdjoint.isSelfAdjoint_mul_iff_commute, selfAdjoint.mul_decomposition, selfAdjoint.lieMul_swap, selfAdjoint.lieMul_add_left, selfAdjoint.lieMul_add_right, selfAdjoint.lieMul_self
statement: formalized
proof: formalized
---

# The Lie bracket of observables

The module `PhyslibAlpha.ProbabilisticTheory.StarAlgebra.Lie`, [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean): 18 declarations, 8 with a docstring.

> The Lie bracket -(i / 2)(a b - b a) makes the observables a real Lie algebra.

## i. Overview

> The commutator of two self-adjoint elements is skew-adjoint, so `⁅a, b⁆ = -(i / 2)(a b - b a)` is
> self-adjoint. Together with the Jordan product it splits the product of observables, `a b = a ∘ b +
> i ⁅a, b⁆`, and it makes the observables a real Lie algebra. The bracket is a scoped instance on
> `selfAdjoint A`.

## ii. Key results

> - `selfAdjoint.lieMul` : the Lie bracket `-(i / 2)(a b - b a)`.
> - `selfAdjoint.isSelfAdjoint_mul_iff_commute` : `a b` is self-adjoint iff `a` and `b` commute.
> - `selfAdjoint.mul_decomposition` : `a b = a ∘ b + i ⁅a, b⁆`.
> - `selfAdjoint.leibniz_bracket` : the bracket satisfies the Leibniz rule.

## iv. References

> * None.

## A. The Lie bracket

**`selfAdjoint.lieMul`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean#L54).

> The Lie bracket `-(i / 2)(a b - b a)` of two self-adjoint elements, again self-adjoint.

```lean
noncomputable def lieMul (a b : selfAdjoint A) : selfAdjoint A
```

**`selfAdjoint.val_lieMul`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean#L64).

```lean
lemma val_lieMul (a b : selfAdjoint A) :
    ((lieMul a b : selfAdjoint A) : A) = (-(Complex.I / 2)) • ((a : A) * b - (b : A) * a)
```

**`selfAdjoint.isSelfAdjoint_mul_iff_commute`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean#L70).

> The product of two self-adjoint elements is self-adjoint iff they commute.

```lean
lemma isSelfAdjoint_mul_iff_commute (a b : selfAdjoint A) :
    IsSelfAdjoint ((a : A) * (b : A)) ↔ Commute (a : A) (b : A)
```

**`selfAdjoint.mul_decomposition`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean#L76).

> The ambient product of two self-adjoint elements splits into its normalized Jordan and Lie
> parts: `a * b = (a ∘ b) + i ⁅a, b⁆`.

```lean
lemma mul_decomposition (a b : selfAdjoint A) :
    (a : A) * b =
      (jordanMul a b : A) + Complex.I • ((lieMul a b : selfAdjoint A) : A)
```

## B. Antisymmetry and additivity

**`selfAdjoint.lieMul_swap`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean#L89).

> The Lie bracket is antisymmetric.

```lean
lemma lieMul_swap (a b : selfAdjoint A) : lieMul a b = -lieMul b a
```

**`selfAdjoint.lieMul_add_left`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean#L94).

```lean
lemma lieMul_add_left (a b c : selfAdjoint A) :
    lieMul (a + b) c = lieMul a c + lieMul b c
```

**`selfAdjoint.lieMul_add_right`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean#L101).

```lean
lemma lieMul_add_right (a b c : selfAdjoint A) :
    lieMul a (b + c) = lieMul a b + lieMul a c
```

**`selfAdjoint.lieMul_self`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean#L108).

```lean
lemma lieMul_self (a : selfAdjoint A) : lieMul a a = 0
```

**`selfAdjoint.instBracket`**, an instance, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean#L113).

> The Lie bracket as a scoped bracket on `selfAdjoint A`.

```lean
noncomputable scoped instance instBracket : Bracket (selfAdjoint A) (selfAdjoint A)
```

**`selfAdjoint.bracket_def`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean#L116).

```lean
lemma bracket_def (a b : selfAdjoint A) : ⁅a, b⁆ = lieMul a b
```

**`selfAdjoint.coe_bracket`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean#L118).

```lean
lemma coe_bracket (a b : selfAdjoint A) :
    ((⁅a, b⁆ : selfAdjoint A) : A) = (-(Complex.I / 2)) • ((a : A) * b - (b : A) * a)
```

## C. Lie ring

**`selfAdjoint.leibniz_bracket`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean#L128).

```lean
lemma leibniz_bracket (a b c : selfAdjoint A) :
    ⁅a, ⁅b, c⁆⁆ = ⁅⁅a, b⁆, c⁆ + ⁅b, ⁅a, c⁆⁆
```

**`selfAdjoint.instLieRing`**, an instance, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean#L138).

> The self-adjoint elements form a Lie ring under the Lie bracket.

```lean
noncomputable scoped instance instLieRing : LieRing (selfAdjoint A)
```

## D. Real Lie algebra

**`selfAdjoint.bracket_smul`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean#L146).

```lean
lemma bracket_smul (t : ℝ) (a b : selfAdjoint A) :
    ⁅a, t • b⁆ = t • ⁅a, b⁆
```

**`selfAdjoint.instLieAlgebra`**, an instance, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean#L154).

> The Lie bracket is compatible with the real scalar structure.

```lean
noncomputable scoped instance instLieAlgebra : LieAlgebra ℝ (selfAdjoint A)
```

## E. Elementary identities

**`selfAdjoint.bracket_one_right`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean#L162).

```lean
lemma bracket_one_right (a : selfAdjoint A) : ⁅a, (1 : selfAdjoint A)⁆ = 0
```

**`selfAdjoint.bracket_one_left`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean#L167).

```lean
lemma bracket_one_left (a : selfAdjoint A) : ⁅(1 : selfAdjoint A), a⁆ = 0
```

**`ProbabilisticTheory.Observable.lieMul`**, an abbrev, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean#L177).

> The Lie bracket of observables.

```lean
noncomputable abbrev Observable.lieMul {A : Type*} [Ring A] [StarRing A] [Module ℂ A]
    [StarModule ℂ A] (a b : Observable A) : Observable A
```

## Depends on

- [The Jordan product of observables](jordan.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Lie.lean)
