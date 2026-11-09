---
declaration: theorem
origin: cited
lean: TauCeti.ReducedTensorWords.leibniz_gerstenhaberBracket
statement: formalized
proof: formalized
---

# The graded Jacobi identity for the Gerstenhaber bracket, in Leibniz form

bracketing with
`F` of degree `p` is a graded derivation of the bracket of `g` of degree `q` and `h` of
degree `r`,
`[F, [g, h]] = [[F, g], h] + (-1)^(p * q) • [g, [F, h]]`.

```lean
TauCeti.ReducedTensorWords.leibniz_gerstenhaberBracket.{uR, uM} {R : Type uR} {M : Type uM}
  [CommRing R] [AddCommGroup M] [_root_.Module R M] {G : TauCeti.InternalGrading R M ℤ}
  {F g h : TauCeti.ReducedTensorWords R M →ₗ[R] M} {p q r : ℤ}
  (hF : TauCeti.LinearMap.IsHomogeneous F (TauCeti.ReducedTensorWords.gradedPiece G) (G.piece ℤ) p)
  (hg : TauCeti.LinearMap.IsHomogeneous g (TauCeti.ReducedTensorWords.gradedPiece G) (G.piece ℤ) q)
  (hh :
    TauCeti.LinearMap.IsHomogeneous h (TauCeti.ReducedTensorWords.gradedPiece G) (G.piece ℤ) r) :
  TauCeti.ReducedTensorWords.gerstenhaberBracket G p (q + r) F
      (TauCeti.ReducedTensorWords.gerstenhaberBracket G q r g h) =
    TauCeti.ReducedTensorWords.gerstenhaberBracket G (p + q) r
        (TauCeti.ReducedTensorWords.gerstenhaberBracket G p q F g) h +
      TauCeti.negOnePowCast R (p * q) •
        TauCeti.ReducedTensorWords.gerstenhaberBracket G q (p + r) g
          (TauCeti.ReducedTensorWords.gerstenhaberBracket G p r F h)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ReducedTensorWords.leibniz_gerstenhaberBracket`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/TensorCoalgebra/Brace.html#TauCeti.ReducedTensorWords.leibniz_gerstenhaberBracket).

## Sources

- [Tau Ceti documentation: `TauCeti.ReducedTensorWords.leibniz_gerstenhaberBracket`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/TensorCoalgebra/Brace.html#TauCeti.ReducedTensorWords.leibniz_gerstenhaberBracket)
- [Source of `TauCeti.ReducedTensorWords.leibniz_gerstenhaberBracket` in TauCeti/LinearAlgebra/TensorCoalgebra/Brace.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/TensorCoalgebra/Brace.lean#L342)
