---
declaration: theorem
origin: cited
lean: TauCeti.isSolvable_gal_iff_exists_isRoot_specialize_quinticF20Spec
statement: formalized
proof: formalized
---

# The quintic resolvent solvability criterion

Let `f` be a monic irreducible separable
quintic over a field.  If the specialization of Dummit's `F₂₀` resolvent is separable, then
the polynomial Galois group is solvable if and only if that resolvent has a root in the base
field.

```lean
TauCeti.isSolvable_gal_iff_exists_isRoot_specialize_quinticF20Spec.{u} {F : Type u} [Field F]
  {f : Polynomial F} (hf : f.Monic) (hsep : f.Separable) (hirr : Irreducible f)
  (hdeg : f.natDegree = 5) (hres : TauCeti.ResolventSeparationEvidence TauCeti.quinticF20Spec f) :
  Group.IsSolvable f.Gal ↔ ∃ a, (TauCeti.quinticF20Spec.specialize F f).IsRoot a
```

## Depends on

- [Separation evidence for a specialized resolvent](separation-evidence-for-a-specialized-resolvent.md)
- [TauCeti.ResolventSpec](tauceti-resolventspec.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isSolvable_gal_iff_exists_isRoot_specialize_quinticF20Spec`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Resolvent/Quintic/Solvable.html#TauCeti.isSolvable_gal_iff_exists_isRoot_specialize_quinticF20Spec).

## Sources

- [Tau Ceti documentation: `TauCeti.isSolvable_gal_iff_exists_isRoot_specialize_quinticF20Spec`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Resolvent/Quintic/Solvable.html#TauCeti.isSolvable_gal_iff_exists_isRoot_specialize_quinticF20Spec)
- [Source of `TauCeti.isSolvable_gal_iff_exists_isRoot_specialize_quinticF20Spec` in TauCeti/FieldTheory/GaloisGroups/Resolvent/Quintic/Solvable.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/GaloisGroups/Resolvent/Quintic/Solvable.lean#L75)
- [Tau Ceti roadmap status: Galois groups of polynomials](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/PolynomialGaloisGroups/STATUS.md)
