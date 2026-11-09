---
declaration: theorem
origin: cited
lean: NumberField.nonempty_algEquiv_iff_of_squarefree
statement: formalized
proof: formalized
---

# The squarefree radicand is an isomorphism invariant

Two quadratic fields presented by
square roots of squarefree integers `d` and `e` are `ℚ`-isomorphic exactly when `d = e`. Taking
`L = K` and the identity shows that the squarefree radicand of a quadratic field does not depend on
the presentation.

```lean
NumberField.nonempty_algEquiv_iff_of_squarefree.{u_1, u_2} {K : Type u_1} {L : Type u_2} [Field K]
  [NumberField K] [Field L] [NumberField L] {d e : ℤ} (hK : Module.finrank ℚ K = 2)
  (hL : Module.finrank ℚ L = 2) {θ : NumberField.RingOfIntegers K}
  {η : NumberField.RingOfIntegers L} (hθ : minpoly ℤ θ = Polynomial.X ^ 2 - Polynomial.C d)
  (hη : minpoly ℤ η = Polynomial.X ^ 2 - Polynomial.C e) (hd : Squarefree d) (he : Squarefree e) :
  Nonempty (K ≃ₐ[ℚ] L) ↔ d = e
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NumberField.nonempty_algEquiv_iff_of_squarefree`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Quadratic/Radicand.html#NumberField.nonempty_algEquiv_iff_of_squarefree).

## Sources

- [Tau Ceti documentation: `NumberField.nonempty_algEquiv_iff_of_squarefree`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Quadratic/Radicand.html#NumberField.nonempty_algEquiv_iff_of_squarefree)
- [Source of `NumberField.nonempty_algEquiv_iff_of_squarefree` in TauCeti/NumberTheory/NumberField/Quadratic/Radicand.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/Quadratic/Radicand.lean#L61)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
