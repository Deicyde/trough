---
declaration: theorem
origin: cited
lean: TauCeti.diracVector_smul_mul_diracWeyl
statement: formalized
proof: formalized
---

# TauCeti.diracVector_smul_mul_diracWeyl

Clifford multiplication is Spin-covariant: `C(s • v) ρ_W(s) = ρ_W(s) C(v)`.

```lean
TauCeti.diracVector_smul_mul_diracWeyl (s : ↥(spinGroup (TauCeti.realCliffordForm 3 1)))
  (v : Fin 4 → ℝ) :
  TauCeti.diracVector (s • v) * TauCeti.diracWeyl s = TauCeti.diracWeyl s * TauCeti.diracVector v
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.diracClifford_spinGroup](tauceti-diracclifford-spingroup.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.diracVector_smul_mul_diracWeyl`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Dirac/ThreeOne.html#TauCeti.diracVector_smul_mul_diracWeyl).

## Sources

- [Tau Ceti documentation: `TauCeti.diracVector_smul_mul_diracWeyl`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Dirac/ThreeOne.html#TauCeti.diracVector_smul_mul_diracWeyl)
- [Source of `TauCeti.diracVector_smul_mul_diracWeyl` in TauCeti/LinearAlgebra/CliffordAlgebra/Dirac/ThreeOne.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/CliffordAlgebra/Dirac/ThreeOne.lean#L261)
- [Tau Ceti roadmap status: Local variational field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LocalVariationalFieldTheory/STATUS.md)
