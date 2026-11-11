---
declaration: def
origin: cited
lean: TauCeti.SignedSym.liftEquiv
statement: formalized
---

# TauCeti.SignedSym.liftEquiv

The universal property, as an equivalence between compatible linear maps and algebra maps.

```lean
TauCeti.SignedSym.liftEquiv.{u, v, w} {R : Type u} [CommRing R] {V : Type v} [AddCommGroup V]
  [_root_.Module R V] (G : TauCeti.InternalGrading R V ℤ) {A : Type w} [Ring A] [Algebra R A] :
  { f //
      ∀ (p q : ℤ) (x y : V),
        x ∈ G.piece ℤ p → y ∈ G.piece ℤ q → f x * f y = ↑(p * q).negOnePow • (f y * f x) } ≃
    (TauCeti.SignedSym G →ₐ[R] A)
```

## Depends on

- [TauCeti.SignedSym](tauceti-signedsym.md)

## Proof depends on

- [TauCeti.SignedSym.generator_mul_generator](tauceti-signedsym-generator-mul-generator.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SignedSym.liftEquiv`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Basic.html#TauCeti.SignedSym.liftEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.SignedSym.liftEquiv`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Basic.html#TauCeti.SignedSym.liftEquiv)
- [Source of `TauCeti.SignedSym.liftEquiv` in TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Basic.lean#L136)
- [Tau Ceti roadmap status: Contact homology and the symplectic field theory formalism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SymplecticFieldTheory/STATUS.md)
