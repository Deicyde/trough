---
declaration: module
origin: cited
lean: MonoidHom.existsUnique_pontryaginDual_of_unitary_translate
statement: formalized
proof: formalized
---

# Characters from unitary multipliers

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.CStarAlgebra.UnitaryCharacter`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/CStarAlgebra/UnitaryCharacter.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/CStarAlgebra/UnitaryCharacter.lean): 1 declaration, 1 with a docstring.

> A unitary representation need not be continuous in the norm of a C⋆-algebra.

## i. Overview

> A unitary representation need not be continuous in the norm of a C⋆-algebra. Nevertheless,
> a character of a subalgebra detects a continuous circle-valued character whenever it is nonzero
> on an operator whose translates are norm continuous and belong to the subalgebra. The resulting
> character describes every translate that belongs to the subalgebra, so it is independent of
> the operator used to detect it.
>
> This is the character-identification step in the spectral representation of a strongly
> continuous unitary representation, applied to a nonzero integrated operator.

## ii. Key results

> This file proves the statement described in the overview.

## iv. References

> * G. B. Folland, *A Course in Abstract Harmonic Analysis*, second edition, §4.4.

## A. Development

**`MonoidHom.existsUnique_pontryaginDual_of_unitary_translate`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/CStarAlgebra/UnitaryCharacter.lean#L53).

> A character nonzero on a commuting operator with norm-continuous unitary translates
> induces a unique continuous circle-valued character. It describes every translate in the subalgebra,
> not just the translates of the witnessing operator.

```lean
lemma _root_.MonoidHom.existsUnique_pontryaginDual_of_unitary_translate
    (ρ : G →* B) (hρ : ∀ g, ρ g ∈ unitary B)
    (A : StarSubalgebra ℂ B) [CompleteSpace A]
    (a : A) (hcomm : ∀ g, Commute (ρ g) (a : B))
    (hmem : ∀ g, ρ g * (a : B) ∈ A)
    (hcont : Continuous fun g => ρ g * (a : B))
    (ω : characterSpace ℂ A) (ha : ω a ≠ 0) :
    ∃! χ : PontryaginDual G,
      ∀ (g : G) (b : A) (hb : ρ g * (b : B) ∈ A),
        ω ⟨ρ g * (b : B), hb⟩ = (χ g : ℂ) * ω b
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/CStarAlgebra/UnitaryCharacter.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/CStarAlgebra/UnitaryCharacter.lean)
