---
declaration: theorem
origin: cited
lean: AddEquiv.orderOf_affineEquiv_eq_iff
statement: formalized
proof: formalized
---

# AddEquiv.orderOf_affineEquiv_eq_iff

The exact order criterion: under a linear part of period dividing `m`, the affine equivalence
has exact order `m` exactly when its `m`-th partial norm vanishes and no smaller positive iterate
is the identity. For an affine equivalence the latter means that every iterate with `0 < k < m`
has a nontrivial linear part or a nonzero partial norm.

```lean
AddEquiv.orderOf_affineEquiv_eq_iff.{u_1} {T : Type u_1} [AddCommGroup T] (A : T ≃+ T) (t : T)
  (m : ℕ) (hm : 0 < m) (hA : (⇑A)^[m] = id) :
  orderOf (A.affineEquiv t) = m ↔
    A.partialNorm m t = 0 ∧ ∀ (k : ℕ), 0 < k → k < m → (⇑A)^[k] ≠ id ∨ A.partialNorm k t ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AddEquiv.orderOf_affineEquiv_eq_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Cyclic/Affine.html#AddEquiv.orderOf_affineEquiv_eq_iff).

## Sources

- [Tau Ceti documentation: `AddEquiv.orderOf_affineEquiv_eq_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Cyclic/Affine.html#AddEquiv.orderOf_affineEquiv_eq_iff)
- [Source of `AddEquiv.orderOf_affineEquiv_eq_iff` in TauCeti/RepresentationTheory/Cyclic/Affine.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Cyclic/Affine.lean#L423)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexTori/STATUS.md)
