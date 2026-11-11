---
declaration: theorem
origin: cited
lean: TauCeti.diracGamma_mul_add_mul_swap
statement: formalized
proof: formalized
---

# TauCeti.diracGamma_mul_add_mul_swap

The Dirac anticommutation relations `{Γ^μ, Γ^ν} = 2 η^{μν}` for `η = diag(1, -1, -1, -1)`.

```lean
TauCeti.diracGamma_mul_add_mul_swap (μ ν : Fin 4) :
  TauCeti.diracGamma μ * TauCeti.diracGamma ν + TauCeti.diracGamma ν * TauCeti.diracGamma μ =
    (if μ = ν then 2 * ↑(TauCeti.realCliffordWeight 1 3 μ) else 0) • 1
```

## Depends on

- [TauCeti.timeFirstToNative](tauceti-timefirsttonative.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.diracGamma_mul_add_mul_swap`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Dirac/ThreeOne.html#TauCeti.diracGamma_mul_add_mul_swap).

## Sources

- [Tau Ceti documentation: `TauCeti.diracGamma_mul_add_mul_swap`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Dirac/ThreeOne.html#TauCeti.diracGamma_mul_add_mul_swap)
- [Source of `TauCeti.diracGamma_mul_add_mul_swap` in TauCeti/LinearAlgebra/CliffordAlgebra/Dirac/ThreeOne.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/CliffordAlgebra/Dirac/ThreeOne.lean#L349)
- [Tau Ceti roadmap status: Local variational field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LocalVariationalFieldTheory/STATUS.md)
