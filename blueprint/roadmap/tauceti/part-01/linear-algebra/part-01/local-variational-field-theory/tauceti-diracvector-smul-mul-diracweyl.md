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
- [Source of `TauCeti.diracVector_smul_mul_diracWeyl` in TauCeti/LinearAlgebra/CliffordAlgebra/Dirac/ThreeOne.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/CliffordAlgebra/Dirac/ThreeOne.lean#L261)
- [Tau Ceti roadmap status: Local variational field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LocalVariationalFieldTheory/STATUS.md)
