---
declaration: theorem
origin: cited
lean: TauCeti.TemperleyLieb.scalarTrace_cliffordAdjoint_mul
statement: formalized
proof: formalized
---

# Sesquilinear Parseval identity for the Clifford scalar trace

in the ordered-product
Majorana basis, `scalarTrace (cliffordForm m) (cliffordAdjoint m a * b)` is
`∑_s conj (a_s) * b_s`.

```lean
TauCeti.TemperleyLieb.scalarTrace_cliffordAdjoint_mul (m : ℕ)
  (a b : CliffordAlgebra (TauCeti.TemperleyLieb.cliffordForm m)) :
  (CliffordAlgebra.scalarTrace (TauCeti.TemperleyLieb.cliffordForm m))
      ((TauCeti.TemperleyLieb.cliffordAdjoint m) a * b) =
    ((CliffordAlgebra.basis (TauCeti.TemperleyLieb.cliffordForm m) (Pi.basisFun ℂ (Fin m))).repr
          a).sum
      fun s z =>
      (starRingEnd ℂ) z *
        ((CliffordAlgebra.basis (TauCeti.TemperleyLieb.cliffordForm m) (Pi.basisFun ℂ (Fin m))).repr
            b)
          s
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TemperleyLieb.scalarTrace_cliffordAdjoint_mul`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/EvenClifford/Basic.html#TauCeti.TemperleyLieb.scalarTrace_cliffordAdjoint_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.TemperleyLieb.scalarTrace_cliffordAdjoint_mul`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/EvenClifford/Basic.html#TauCeti.TemperleyLieb.scalarTrace_cliffordAdjoint_mul)
- [Source of `TauCeti.TemperleyLieb.scalarTrace_cliffordAdjoint_mul` in TauCeti/Algebra/TemperleyLieb/EvenClifford/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/TemperleyLieb/EvenClifford/Basic.lean#L535)
