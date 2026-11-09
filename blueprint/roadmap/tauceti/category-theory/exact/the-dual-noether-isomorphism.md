---
declaration: theorem
origin: cited
lean: TauCeti.ExactStructure.exists_conflation_comp'
statement: formalized
proof: formalized
---

# The dual Noether isomorphism

Given conflations `X ⟶ Y ⟶ Z` and `V ⟶ W ⟶ Y`, the
pullback `Q` of `W ⟶ Y` along `X ⟶ Y` is at once the kernel of the composite deflation
`W ⟶ Z` and an extension of `X` by `V`.

```lean
TauCeti.ExactStructure.exists_conflation_comp'.{v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.Limits.HasZeroObject C] [CategoryTheory.Limits.HasBinaryBiproducts C]
  (E : TauCeti.ExactStructure C) {X Y Z W V : C} {i : X ⟶ Y} {p : Y ⟶ Z}
  {hip : CategoryTheory.CategoryStruct.comp i p = 0}
  (h₁ : E.Conflation { X₁ := X, X₂ := Y, X₃ := Z, f := i, g := p, zero := hip }) {v : V ⟶ W}
  {q : W ⟶ Y} {hvq : CategoryTheory.CategoryStruct.comp v q = 0}
  (h₂ : E.Conflation { X₁ := V, X₂ := W, X₃ := Y, f := v, g := q, zero := hvq }) :
  ∃ Q c α β,
    ∃ (hc : CategoryTheory.CategoryStruct.comp c (CategoryTheory.CategoryStruct.comp q p) = 0) (hβ :
      CategoryTheory.CategoryStruct.comp β α = 0),
      E.Conflation
          { X₁ := Q, X₂ := W, X₃ := Z, f := c, g := CategoryTheory.CategoryStruct.comp q p,
            zero := hc } ∧
        E.Conflation { X₁ := V, X₂ := Q, X₃ := X, f := β, g := α, zero := hβ } ∧
          CategoryTheory.CategoryStruct.comp c q = CategoryTheory.CategoryStruct.comp α i ∧
            CategoryTheory.CategoryStruct.comp β c = v
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ExactStructure.exists_conflation_comp'`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/BaseChange.html#TauCeti.ExactStructure.exists_conflation_comp').

## Sources

- [Tau Ceti documentation: `TauCeti.ExactStructure.exists_conflation_comp'`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/BaseChange.html#TauCeti.ExactStructure.exists_conflation_comp')
- [Source of `TauCeti.ExactStructure.exists_conflation_comp'` in TauCeti/CategoryTheory/Exact/BaseChange.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/Exact/BaseChange.lean#L257)
