# Translation number defines a homeomorphism up to semiconjugacy

If two lifts of circle homeomorphisms have the same translation number, then they are
semiconjugate by a `CircleDeg1Lift`. This version uses assumptions `bijective f₁` and
`bijective f₂` to assume that `f₁` and `f₂` are homeomorphisms.

```lean
CircleDeg1Lift.semiconj_of_bijective_of_translationNumber_eq {f₁ f₂ : CircleDeg1Lift}
  (h₁ : Function.Bijective ⇑f₁) (h₂ : Function.Bijective ⇑f₂)
  (h : f₁.translationNumber = f₂.translationNumber) : ∃ F, Function.Semiconj ⇑F ⇑f₁ ⇑f₂
```

## Depends on

- [Translation number](translation-number.md)

## Proof depends on

- [Translation numbers define a group action up to semiconjugacy](translation-numbers-define-a-group-action-up-to.md)

## Sources

- [Mathlib documentation: `CircleDeg1Lift.semiconj_of_bijective_of_translationNumber_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Dynamics/Circle/RotationNumber/TranslationNumber.html#CircleDeg1Lift.semiconj_of_bijective_of_translationNumber_eq)
- [Source of `CircleDeg1Lift.semiconj_of_bijective_of_translationNumber_eq` in Mathlib/Dynamics/Circle/RotationNumber/TranslationNumber.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Dynamics/Circle/RotationNumber/TranslationNumber.lean#L884)
- [Mathlib overview: Dynamics › Circle dynamics](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L560)
