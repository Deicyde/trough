---
declaration: def
origin: cited
lean: CliffordAlgebra.realCliffordSpinGroupEquivNeg
statement: formalized
---

# CliffordAlgebra.realCliffordSpinGroupEquivNeg

The Spin group of signature `(p, q)`, transported into the Clifford algebra of the negated
signature `(q, p)`. For `p = n` and `q = 0` this is the compact Spin group `Spin(n)` in the Clifford
algebra of the negative-definite coordinate form `realCliffordForm 0 n`.

```lean
CliffordAlgebra.realCliffordSpinGroupEquivNeg (p q : ℕ) :
  ↥(CliffordAlgebra.realCliffordSpinGroup p q) ≃* ↥(CliffordAlgebra.realCliffordSpinGroup q p)
```

## Depends on

- [CliffordAlgebra.spinGroupEquivNeg](cliffordalgebra-spingroupequivneg.md)

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.realCliffordSpinGroupEquivNeg`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/Real/Neg.html#CliffordAlgebra.realCliffordSpinGroupEquivNeg).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.realCliffordSpinGroupEquivNeg`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/Real/Neg.html#CliffordAlgebra.realCliffordSpinGroupEquivNeg)
- [Source of `CliffordAlgebra.realCliffordSpinGroupEquivNeg` in TauCeti/LinearAlgebra/CliffordAlgebra/Spin/Real/Neg.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/Real/Neg.lean#L72)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SpinGeometry/STATUS.md)
