---
declaration: module
origin: cited
lean: CommCStarAlgebra.character, CommCStarAlgebra.character_apply, CommCStarAlgebra.ext_character, CommCStarAlgebra.character_eq_re, CommCStarAlgebra.inf, CommCStarAlgebra.character_inf, CommCStarAlgebra.isSelfAdjoint_inf, CommCStarAlgebra.nonneg_iff_forall_character
statement: formalized
proof: formalized
---

# Commutative C⋆-algebras are classical

The module `PhyslibAlpha.ProbabilisticTheory.CStarAlgebra.Commutative`, [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Commutative.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Commutative.lean): 11 declarations, 8 with a docstring.

> The observables of a commutative C⋆-algebra form a classical system, via its characters.

## i. Overview

> A commutative C⋆-algebra is the algebra of continuous functions on its characters, the pure
> states. An observable is nonnegative exactly when every character assigns it a nonnegative value,
> and one observable lies below another exactly when every character says so. Minima can then be
> taken character by character, which gives the Riesz decomposition of the observables. So the
> self-adjoint part of a commutative C⋆-algebra is a classical system.

## ii. Key results

> - `CommCStarAlgebra.character` : a character as a star-algebra homomorphism.
> - `CommCStarAlgebra.nonneg_iff_forall_character` : characters detect positivity.
> - `CommCStarAlgebra.hasRieszDecomposition` : the observables have the Riesz decomposition.
> - `CommCStarAlgebra.isClassical` : the observables form a classical system.

## iv. References

> * None.

## A. Characters

**`CommCStarAlgebra.character`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Commutative.lean#L55).

> A character of a commutative C⋆-algebra, as a star-algebra homomorphism to `ℂ`.

```lean
noncomputable def character (χ : WeakDual.characterSpace ℂ A) : A →⋆ₐ[ℂ] ℂ
```

**`CommCStarAlgebra.character_apply`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Commutative.lean#L59).

```lean
lemma character_apply (χ : WeakDual.characterSpace ℂ A) (a : A) : character χ a = χ a
```

**`CommCStarAlgebra.ext_character`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Commutative.lean#L62).

> Characters separate the elements of a commutative C⋆-algebra.

```lean
lemma ext_character {a b : A} (h : ∀ χ : WeakDual.characterSpace ℂ A, χ a = χ b) : a = b
```

**`CommCStarAlgebra.character_eq_re`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Commutative.lean#L66).

> A character takes real values on self-adjoint elements.

```lean
lemma character_eq_re {a : A} (ha : IsSelfAdjoint a) (χ : WeakDual.characterSpace ℂ A) :
    χ a = ((χ a).re : ℂ)
```

**`CommCStarAlgebra.inf`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Commutative.lean#L73).

> The pointwise minimum of two self-adjoint elements, taken character by character.

```lean
noncomputable def inf (a b : A) : A
```

**`CommCStarAlgebra.character_inf`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Commutative.lean#L84).

```lean
lemma character_inf (a b : A) (χ : WeakDual.characterSpace ℂ A) :
    χ (inf a b) = ((min (χ a).re (χ b).re : ℝ) : ℂ)
```

**`CommCStarAlgebra.isSelfAdjoint_inf`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Commutative.lean#L90).

```lean
lemma isSelfAdjoint_inf (a b : A) : IsSelfAdjoint (inf a b)
```

## B. Order through characters

**`CommCStarAlgebra.nonneg_iff_forall_character`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Commutative.lean#L100).

> **Characters detect positivity.**

```lean
lemma nonneg_iff_forall_character {a : A} :
    0 ≤ a ↔ ∀ χ : WeakDual.characterSpace ℂ A, 0 ≤ χ a
```

**`CommCStarAlgebra.le_iff_forall_character`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Commutative.lean#L107).

> Characters detect the order between self-adjoint elements.

```lean
lemma le_iff_forall_character {a b : A} (ha : IsSelfAdjoint a) (hb : IsSelfAdjoint b) :
    a ≤ b ↔ ∀ χ : WeakDual.characterSpace ℂ A, (χ a).re ≤ (χ b).re
```

## C. Classicality

**`CommCStarAlgebra.hasRieszDecomposition`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Commutative.lean#L119).

> **Riesz decomposition.** A nonnegative observable below a sum of two nonnegative observables
> splits, character by character, into two pieces below the summands.

```lean
lemma hasRieszDecomposition : HasRieszDecomposition (selfAdjoint A)
```

**`CommCStarAlgebra.isClassical`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Commutative.lean#L138).

> **The observables of a commutative C⋆-algebra form a classical system.**

```lean
lemma isClassical : IsClassical (selfAdjoint A)
```

## Depends on

- [The observables of a C⋆-algebra](../../../physlib/probabilistictheory/cstaralgebra/orderunit.md)
- [Classical systems](../classical/basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Commutative.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Commutative.lean)
