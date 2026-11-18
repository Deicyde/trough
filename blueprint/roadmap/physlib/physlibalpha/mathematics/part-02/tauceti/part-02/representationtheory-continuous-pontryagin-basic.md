---
declaration: module
origin: cited
lean: ContRepresentation.existsUnique_pontryaginDual_of_integratedOperatorL1
statement: formalized
proof: formalized
---

# Group characters detected by integrated operators

The module `PhyslibAlpha.Mathematics.TauCeti.RepresentationTheory.Continuous.Pontryagin.Basic`, [PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Pontryagin/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Pontryagin/Basic.lean): 1 declaration, 1 with a docstring.

> Let `π` be a strongly continuous unitary representation of an abelian group and let `A` be a
> complete star subalgebra containing its integrated operators.

## i. Overview

> Let `π` be a strongly continuous unitary representation of an abelian group and let `A` be a
> complete star subalgebra containing its integrated operators. Each character of `A` that is
> nonzero on some integrated operator determines a unique continuous group character `χ`, with
>
> `ω (π(g) π(f)) = χ(g) ω (π(f))`.
>
> The nonvanishing assumption is necessary: adjoining an identity to a nonunital algebra can
> introduce a character that annihilates all the integrated operators. On the other characters,
> the displayed equation identifies the spectral parameter as an element of the Pontryagin dual.
> It applies to all integrable weights, independently of the weight witnessing nonvanishing.
> The hypothesis on `A` is simply containment of the integrated form's range; translation
> invariance and norm continuity follow from the integrated form's existing translation API.

## ii. Key results

> This file proves the statement described in the overview.

## iv. References

> * G. B. Folland, *A Course in Abstract Harmonic Analysis*, second edition, §§3.2 and 4.4.

## A. Development

**`ContRepresentation.existsUnique_pontryaginDual_of_integratedOperatorL1`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Pontryagin/Basic.lean#L63).

> A nonvanishing character of an algebra containing the integrated form of a strongly
> continuous unitary representation detects a unique continuous group character. Its value is
> the multiplier on every integrated operator, independently of the witnessing weight.

```lean
lemma _root_.ContRepresentation.existsUnique_pontryaginDual_of_integratedOperatorL1
    (π : ContRepresentation ℂ (Multiplicative G) H)
    {hcont : ∀ v, Continuous fun g : G => π (.ofAdd g) v}
    (hbdd : ∃ C, ∀ g, ‖π g‖ ≤ C)
    (hπ : ContRepresentation.IsUnitary π)
    (A : StarSubalgebra ℂ (H →L[ℂ] H)) [CompleteSpace A] :
    ∀ (hA : ∀ f : G →₁[μ] ℂ, π.integratedOperatorL1 hcont hbdd μ f ∈ A)
    (ω : characterSpace ℂ A),
    (∃ f : G →₁[μ] ℂ, ω ⟨π.integratedOperatorL1 hcont hbdd μ f, hA f⟩ ≠ 0) →
    ∃! χ : PontryaginDual (Multiplicative G), ∀ (g : G) (f : G →₁[μ] ℂ),
      ω ⟨π.integratedOperatorL1 hcont hbdd μ
          (Lp.compMeasurePreserving (fun t => -g + t)
            (measurePreserving_add_left μ (-g)) f), hA _⟩ =
        (χ (.ofAdd g) : ℂ) * ω ⟨π.integratedOperatorL1 hcont hbdd μ f, hA f⟩
```

## Depends on

- [The integrated form of a strongly continuous representation](representationtheory-continuous-integrated-basic.md)

## Proof depends on

- [Characters from unitary multipliers](../part-01/analysis-cstaralgebra-unitarycharacter.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Pontryagin/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/RepresentationTheory/Continuous/Pontryagin/Basic.lean)
