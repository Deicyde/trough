---
declaration: theorem
origin: cited
lean: TauCeti.ExactStructure.exists_conflation_comp
statement: formalized
proof: formalized
---

# The Noether isomorphism for exact categories

Given conflations `X ⟶ Y ⟶ Z` and
`Y ⟶ W ⟶ V`, there is an object `Q` — the pushout of `Y ⟶ W` along `Y ⟶ Z` — which is at once
the cokernel of the composite inflation `X ⟶ W` and an extension of `V` by `Z`.

In the classical notation `Q ≅ W/X`, and the second conflation is
`Y/X ⟶ W/X ⟶ W/Y`. This is Bühler's Lemma 3.5, and it is exactly what an extension-closed
subcategory needs in order to inherit axiom E1.

```lean
TauCeti.ExactStructure.exists_conflation_comp.{v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Preadditive C] [CategoryTheory.Limits.HasZeroObject C]
  [CategoryTheory.Limits.HasBinaryBiproducts C] (E : TauCeti.ExactStructure C) {X Y Z W V : C}
  {i : X ⟶ Y} {p : Y ⟶ Z} {hip : CategoryTheory.CategoryStruct.comp i p = 0}
  (h₁ : E.Conflation { X₁ := X, X₂ := Y, X₃ := Z, f := i, g := p, zero := hip }) {j : Y ⟶ W}
  {v : W ⟶ V} {hjv : CategoryTheory.CategoryStruct.comp j v = 0}
  (h₂ : E.Conflation { X₁ := Y, X₂ := W, X₃ := V, f := j, g := v, zero := hjv }) :
  ∃ Q c α β,
    ∃ (hc : CategoryTheory.CategoryStruct.comp (CategoryTheory.CategoryStruct.comp i j) c = 0) (hβ :
      CategoryTheory.CategoryStruct.comp α β = 0),
      E.Conflation
          { X₁ := X, X₂ := W, X₃ := Q, f := CategoryTheory.CategoryStruct.comp i j, g := c,
            zero := hc } ∧
        E.Conflation { X₁ := Z, X₂ := Q, X₃ := V, f := α, g := β, zero := hβ } ∧
          CategoryTheory.CategoryStruct.comp j c = CategoryTheory.CategoryStruct.comp p α ∧
            CategoryTheory.CategoryStruct.comp c β = v
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ExactStructure.exists_conflation_comp`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/BaseChange.html#TauCeti.ExactStructure.exists_conflation_comp).

## Sources

- [Tau Ceti documentation: `TauCeti.ExactStructure.exists_conflation_comp`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/BaseChange.html#TauCeti.ExactStructure.exists_conflation_comp)
- [Source of `TauCeti.ExactStructure.exists_conflation_comp` in TauCeti/CategoryTheory/Exact/BaseChange.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/Exact/BaseChange.lean#L235)
