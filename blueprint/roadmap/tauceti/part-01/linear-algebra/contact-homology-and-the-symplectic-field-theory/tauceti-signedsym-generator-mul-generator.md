---
declaration: theorem
origin: cited
lean: TauCeti.SignedSym.generator_mul_generator
statement: formalized
proof: formalized
---

# TauCeti.SignedSym.generator_mul_generator

Homogeneous generators supercommute with the Koszul sign.

```lean
TauCeti.SignedSym.generator_mul_generator.{u, v} {R : Type u} [CommRing R] {V : Type v}
  [AddCommGroup V] [_root_.Module R V] (G : TauCeti.InternalGrading R V ℤ) {p q : ℤ} {x y : V}
  (hx : x ∈ G.piece ℤ p) (hy : y ∈ G.piece ℤ q) :
  (TauCeti.SignedSym.generator G) x * (TauCeti.SignedSym.generator G) y =
    ↑(p * q).negOnePow • ((TauCeti.SignedSym.generator G) y * (TauCeti.SignedSym.generator G) x)
```

## Depends on

- [TauCeti.SignedSym](tauceti-signedsym.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SignedSym.generator_mul_generator`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Basic.html#TauCeti.SignedSym.generator_mul_generator).

## Sources

- [Tau Ceti documentation: `TauCeti.SignedSym.generator_mul_generator`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Basic.html#TauCeti.SignedSym.generator_mul_generator)
- [Source of `TauCeti.SignedSym.generator_mul_generator` in TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Basic.lean#L74)
- [Tau Ceti roadmap status: Contact homology and the symplectic field theory formalism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SymplecticFieldTheory/STATUS.md)
