---
declaration: theorem
origin: cited
lean: TauCeti.conjTranspose_diracWeyl_mul_mul
statement: formalized
proof: formalized
---

# TauCeti.conjTranspose_diracWeyl_mul_mul

The Weyl action preserves the indefinite Hermitian pairing `H₀ = [[0, 1], [1, 0]]`:
`ρ_W(s)ᴴ H₀ ρ_W(s) = H₀`.

```lean
TauCeti.conjTranspose_diracWeyl_mul_mul (s : ↥(spinGroup (TauCeti.realCliffordForm 3 1))) :
  (TauCeti.diracWeyl s).conjTranspose * Matrix.fromBlocks 0 1 1 0 * TauCeti.diracWeyl s =
    Matrix.fromBlocks 0 1 1 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.conjTranspose_diracWeyl_mul_mul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Dirac/ThreeOne.html#TauCeti.conjTranspose_diracWeyl_mul_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.conjTranspose_diracWeyl_mul_mul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Dirac/ThreeOne.html#TauCeti.conjTranspose_diracWeyl_mul_mul)
- [Source of `TauCeti.conjTranspose_diracWeyl_mul_mul` in TauCeti/LinearAlgebra/CliffordAlgebra/Dirac/ThreeOne.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/CliffordAlgebra/Dirac/ThreeOne.lean#L280)
- [Tau Ceti roadmap status: Local variational field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LocalVariationalFieldTheory/STATUS.md)
