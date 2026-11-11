---
declaration: def
origin: cited
lean: TauCeti.Floer.pairOfPantsPerturbation
statement: formalized
---

# TauCeti.Floer.pairOfPantsPerturbation

The Hamiltonian perturbation one-form on the pair of pants given by period-one Hamiltonians
`H q` on its three ends. At `w ∈ ℂ` and `x ∈ M` it is the covector
`∑ q, β(±s_q(w)) H_q(t_q(w), x) dt_q`, where `(s_q, t_q)` are the coordinates of the end `q`,
the sign is that of the end, and `β` is the smooth transition from `0` on `(-∞, 1]` to `1` on
`[2, ∞)`.

```lean
TauCeti.Floer.pairOfPantsPerturbation.{u_1} {M : Type u_1}
  (H : TauCeti.ThricePuncturedSphere.Puncture → ℝ → M → ℝ) (w : ℂ) (x : M) : ℂ →L[ℝ] ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Floer.pairOfPantsPerturbation`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/PairOfPants/Basic.html#TauCeti.Floer.pairOfPantsPerturbation).

## Sources

- [Tau Ceti documentation: `TauCeti.Floer.pairOfPantsPerturbation`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/PairOfPants/Basic.html#TauCeti.Floer.pairOfPantsPerturbation)
- [Source of `TauCeti.Floer.pairOfPantsPerturbation` in TauCeti/Geometry/Symplectic/Floer/PairOfPants/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Floer/PairOfPants/Basic.lean#L74)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
