---
declaration: theorem
origin: cited
lean: TauCeti.zeroExtendedFiniteSection_toeplitz_mul
statement: formalized
proof: formalized
---

# Widom's identity

For essentially bounded symbols `a` and `b`, the zero-extended finite
sections `Tₙ(·) = Pₙ T_(·) Pₙ` satisfy

  `Tₙ(ab) = Tₙ(a) Tₙ(b) + Pₙ C_a C_(b(-t)) Pₙ + Wₙ C_(a(-t)) C_b Wₙ`,

where `C` is the classical Hankel operator, `a(-t)` is the reflected symbol, and `Wₙ` reverses
the first `n + 1` Hardy coordinates.

```lean
TauCeti.zeroExtendedFiniteSection_toeplitz_mul
  (a b : ↥(MeasureTheory.Lp ℂ ⊤ AddCircle.haarAddCircle)) (n : ℕ) :
  (TauCeti.toeplitz (a * b)).zeroExtendedFiniteSection TauCeti.hardyBasis n =
    (TauCeti.toeplitz a).zeroExtendedFiniteSection TauCeti.hardyBasis n ∘SL
          (TauCeti.toeplitz b).zeroExtendedFiniteSection TauCeti.hardyBasis n +
        TauCeti.hardyBasis.finiteProjection n ∘SL
          TauCeti.classicalHankel a ∘SL
            TauCeti.classicalHankel ((MeasureTheory.Lp.compMeasurePreserving (fun t => -t) ⋯) b) ∘SL
              TauCeti.hardyBasis.finiteProjection n +
      TauCeti.hardyBasis.finiteReflection n ∘SL
        TauCeti.classicalHankel ((MeasureTheory.Lp.compMeasurePreserving (fun t => -t) ⋯) a) ∘SL
          TauCeti.classicalHankel b ∘SL TauCeti.hardyBasis.finiteReflection n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Classical Toeplitz product identity](../../part-03/fourier/part-01/classical-toeplitz-product-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.zeroExtendedFiniteSection_toeplitz_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Hardy/Widom.html#TauCeti.zeroExtendedFiniteSection_toeplitz_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.zeroExtendedFiniteSection_toeplitz_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Hardy/Widom.html#TauCeti.zeroExtendedFiniteSection_toeplitz_mul)
- [Source of `TauCeti.zeroExtendedFiniteSection_toeplitz_mul` in TauCeti/Analysis/Fourier/Hardy/Widom.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Fourier/Hardy/Widom.lean#L127)
