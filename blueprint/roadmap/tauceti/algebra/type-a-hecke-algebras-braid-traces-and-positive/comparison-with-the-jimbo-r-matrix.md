---
declaration: theorem
origin: cited
lean: TauCeti.signedCheckedR_eq_jimboGenerator
statement: formalized
proof: formalized
---

# Comparison with the Jimbo R-matrix

If every letter is positive, the signed checked
R-matrix is the Jimbo R-matrix at the parameter `-s`, rescaled by `-s`, on the alphabet with the
reversed order: it is the conjugate of `(-s) • T_{-s}` on `(Fin n → ιᵒᵈ) →₀ R` by the relabelling
of words along `ι ≃ ιᵒᵈ`.

```lean
TauCeti.signedCheckedR_eq_jimboGenerator.{u_1, u_2} {R : Type u_1} [CommRing R] {ι : Type u_2}
  [LinearOrder ι] (pos : ι → Prop) [DecidablePred pos] {n : ℕ} (s : Rˣ) (hpos : ∀ (a : ι), pos a)
  (j k : Fin n) :
  TauCeti.signedCheckedR pos (↑s) j k =
    (Finsupp.domLCongr ((Equiv.refl (Fin n)).arrowCongr OrderDual.toDual)).symm.conj
      (-↑s • TauCeti.KnotTheory.jimboGenerator (-s) j k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.signedCheckedR_eq_jimboGenerator`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/SignedCheckedR.html#TauCeti.signedCheckedR_eq_jimboGenerator).

## Sources

- [Tau Ceti documentation: `TauCeti.signedCheckedR_eq_jimboGenerator`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/SignedCheckedR.html#TauCeti.signedCheckedR_eq_jimboGenerator)
- [Source of `TauCeti.signedCheckedR_eq_jimboGenerator` in TauCeti/Algebra/TypeAHeckeAlgebra/SignedCheckedR.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/TypeAHeckeAlgebra/SignedCheckedR.lean#L382)
- [Tau Ceti roadmap status: Type-A Hecke algebras, braid traces, and positive quotients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TypeAHeckeAlgebras/STATUS.md)
