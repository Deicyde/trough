---
declaration: theorem
origin: cited
lean: TauCeti.ExactStructure.nonempty_iso_biprod_of_projective
statement: formalized
proof: formalized
---

# Schanuel's lemma

Two conflations `K ↪ Q ↠ X` and `K' ↪ Q' ↠ X` with projective middle
terms have stably isomorphic kernels: `K ⊞ Q' ≅ K' ⊞ Q`.

Both isomorphisms come from the pullback `Q ×_X Q'`, which base change exhibits at once as an
extension of `Q'` by `K` and as an extension of `Q` by `K'`; projectivity splits both.

```lean
TauCeti.ExactStructure.nonempty_iso_biprod_of_projective.{v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.Limits.HasZeroObject C] [CategoryTheory.Limits.HasBinaryBiproducts C]
  {E : TauCeti.ExactStructure C} {X K Q : C} {m : K ⟶ Q} {a : Q ⟶ X}
  {hm : CategoryTheory.CategoryStruct.comp m a = 0}
  (hc : E.Conflation { X₁ := K, X₂ := Q, X₃ := X, f := m, g := a, zero := hm })
  (hQ : E.isProjective Q) {K' Q' : C} {m' : K' ⟶ Q'} {a' : Q' ⟶ X}
  {hm' : CategoryTheory.CategoryStruct.comp m' a' = 0}
  (hc' : E.Conflation { X₁ := K', X₂ := Q', X₃ := X, f := m', g := a', zero := hm' })
  (hQ' : E.isProjective Q') : Nonempty (K ⊞ Q' ≅ K' ⊞ Q)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ExactStructure.nonempty_iso_biprod_of_projective`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/Projective.html#TauCeti.ExactStructure.nonempty_iso_biprod_of_projective).

## Sources

- [Tau Ceti documentation: `TauCeti.ExactStructure.nonempty_iso_biprod_of_projective`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/Projective.html#TauCeti.ExactStructure.nonempty_iso_biprod_of_projective)
- [Source of `TauCeti.ExactStructure.nonempty_iso_biprod_of_projective` in TauCeti/CategoryTheory/Exact/Projective.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Exact/Projective.lean#L456)
