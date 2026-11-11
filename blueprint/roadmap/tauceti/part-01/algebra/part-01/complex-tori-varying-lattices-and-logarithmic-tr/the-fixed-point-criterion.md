---
declaration: theorem
origin: cited
lean: AddEquiv.exists_affineEquiv_iterate_apply_eq_self_iff
statement: formalized
proof: formalized
---

# The fixed-point criterion

The `k`-th iterate of `x ↦ A x + t` has a fixed point exactly
when the `k`-th partial norm of `t` lies in the image of `1 - A^k`.

```lean
AddEquiv.exists_affineEquiv_iterate_apply_eq_self_iff.{u_1} {T : Type u_1} [AddCommGroup T]
  (A : T ≃+ T) (t : T) (k : ℕ) :
  (∃ x, (⇑(A.affineEquiv t))^[k] x = x) ↔ ∃ b, b - (⇑A)^[k] b = A.partialNorm k t
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AddEquiv.exists_affineEquiv_iterate_apply_eq_self_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Cyclic/Affine.html#AddEquiv.exists_affineEquiv_iterate_apply_eq_self_iff).

## Sources

- [Tau Ceti documentation: `AddEquiv.exists_affineEquiv_iterate_apply_eq_self_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Cyclic/Affine.html#AddEquiv.exists_affineEquiv_iterate_apply_eq_self_iff)
- [Source of `AddEquiv.exists_affineEquiv_iterate_apply_eq_self_iff` in TauCeti/RepresentationTheory/Cyclic/Affine.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Cyclic/Affine.lean#L483)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexTori/STATUS.md)
