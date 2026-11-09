---
declaration: theorem
origin: cited
lean: TauCeti.wedgeForm_plucker
statement: formalized
proof: formalized
---

# Laplace's identity (Bombieri–Gubler (7.16))

the wedge of `p` forms takes the value
`det (l a (y b))` on the Plücker vector of `p` vectors `y`.

```lean
TauCeti.wedgeForm_plucker.{u_1, u_2} {R : Type u_1} [CommRing R] {ι : Type u_2} [LinearOrder ι]
  {p : ℕ} [Fintype ι] (l : Fin p → Module.Dual R (ι → R)) (y : Fin p → ι → R) :
  (TauCeti.wedgeForm l) (TauCeti.plucker y) = (Matrix.of fun a b => (l a) (y b)).det
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cauchy–Binet formula](the-cauchy-binet-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.wedgeForm_plucker`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/ExteriorPower/LinearForms.html#TauCeti.wedgeForm_plucker).

## Sources

- [Tau Ceti documentation: `TauCeti.wedgeForm_plucker`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/ExteriorPower/LinearForms.html#TauCeti.wedgeForm_plucker)
- [Source of `TauCeti.wedgeForm_plucker` in TauCeti/LinearAlgebra/ExteriorPower/LinearForms.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/ExteriorPower/LinearForms.lean#L113)
