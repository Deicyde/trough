---
declaration: theorem
origin: cited
lean: TauCeti.jacobiMatrixAt_mulVec_self
statement: formalized
proof: formalized
---

# Euler's identity (`TauCeti.jacobiMatrixAt_mulVec_self`)

**Euler's identity** for the Jacobian matrix of a family of homogeneous polynomials: applied
to the point itself, it returns each equation's value scaled by its degree.

```lean
TauCeti.jacobiMatrixAt_mulVec_self.{u_1, u_2, u_3} {R : Type u_1} {σ : Type u_2} {ι : Type u_3}
  [CommSemiring R] [Fintype σ] {p : ι → MvPolynomial σ R} {d : ι → ℕ}
  (hp : ∀ (i : ι), (p i).IsHomogeneous (d i)) (v : σ → R) :
  (TauCeti.jacobiMatrixAt p v).mulVec v = fun i => d i • (MvPolynomial.eval v) (p i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.jacobiMatrixAt_mulVec_self`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Jacobian/Basic.html#TauCeti.jacobiMatrixAt_mulVec_self).

## Sources

- [Tau Ceti documentation: `TauCeti.jacobiMatrixAt_mulVec_self`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Jacobian/Basic.html#TauCeti.jacobiMatrixAt_mulVec_self)
- [Source of `TauCeti.jacobiMatrixAt_mulVec_self` in TauCeti/RingTheory/MvPolynomial/Jacobian/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPolynomial/Jacobian/Basic.lean#L88)
