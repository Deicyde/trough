---
declaration: theorem
origin: cited
lean: TauCeti.TemperleyLieb.scalarTrace_cliffordAdjoint_mul_self
statement: formalized
proof: formalized
---

# Parseval identity for the Clifford scalar trace

in the ordered-product Majorana basis,
`scalarTrace (cliffordForm m) (cliffordAdjoint m a * a)` is the sum of squared moduli of the
coordinates of `a`.

```lean
TauCeti.TemperleyLieb.scalarTrace_cliffordAdjoint_mul_self (m : ℕ)
  (a : CliffordAlgebra (TauCeti.TemperleyLieb.cliffordForm m)) :
  (CliffordAlgebra.scalarTrace (TauCeti.TemperleyLieb.cliffordForm m))
      ((TauCeti.TemperleyLieb.cliffordAdjoint m) a * a) =
    ↑(((CliffordAlgebra.basis (TauCeti.TemperleyLieb.cliffordForm m) (Pi.basisFun ℂ (Fin m))).repr
            a).sum
        fun x z => Complex.normSq z)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Sesquilinear Parseval identity for the Clifford scalar trace](sesquilinear-parseval-identity-for-the-clifford.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TemperleyLieb.scalarTrace_cliffordAdjoint_mul_self`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/EvenClifford/Basic.html#TauCeti.TemperleyLieb.scalarTrace_cliffordAdjoint_mul_self).

## Sources

- [Tau Ceti documentation: `TauCeti.TemperleyLieb.scalarTrace_cliffordAdjoint_mul_self`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/EvenClifford/Basic.html#TauCeti.TemperleyLieb.scalarTrace_cliffordAdjoint_mul_self)
- [Source of `TauCeti.TemperleyLieb.scalarTrace_cliffordAdjoint_mul_self` in TauCeti/Algebra/TemperleyLieb/EvenClifford/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/TemperleyLieb/EvenClifford/Basic.lean#L552)
