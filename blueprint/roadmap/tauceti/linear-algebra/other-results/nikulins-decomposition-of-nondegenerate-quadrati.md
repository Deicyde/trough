---
declaration: theorem
origin: cited
lean: TauCeti.FiniteQuadraticModule.exists_isometry_pi_oddCyclic
statement: formalized
proof: formalized
---

# Nikulin's decomposition of nondegenerate quadratic modules of odd order

A nondegenerate
finite quadratic module of odd order is isometric to an orthogonal sum of odd cyclic modules
`q_θ^{(p)}(p^k)`, each of odd prime-power order `m = p^k` with coefficient `θ` prime to `m`.

```lean
TauCeti.FiniteQuadraticModule.exists_isometry_pi_oddCyclic.{u} (A : TauCeti.FiniteQuadraticModule)
  (hA : A.IsNondegenerate) (hodd : Odd (Nat.card A.carrier)) :
  ∃ n m,
    ∃ (hm : ∀ (i : Fin n), Odd (m i)),
      ∃ θ,
        (∀ (i : Fin n), IsPrimePow (m i) ∧ IsCoprime (↑(m i)) (θ i)) ∧
          Nonempty
            ((TauCeti.FiniteQuadraticModule.pi fun i =>
                  TauCeti.FiniteQuadraticModule.oddCyclic (m i) ⋯ (θ i)).Isometry
              A)
```

## Depends on

- [TauCeti.FiniteQuadraticModule](../integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteQuadraticModule.exists_isometry_pi_oddCyclic`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/FiniteBilinearModule/OddCyclic/Decomposition.html#TauCeti.FiniteQuadraticModule.exists_isometry_pi_oddCyclic).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteQuadraticModule.exists_isometry_pi_oddCyclic`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/FiniteBilinearModule/OddCyclic/Decomposition.html#TauCeti.FiniteQuadraticModule.exists_isometry_pi_oddCyclic)
- [Source of `TauCeti.FiniteQuadraticModule.exists_isometry_pi_oddCyclic` in TauCeti/LinearAlgebra/FiniteBilinearModule/OddCyclic/Decomposition.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/FiniteBilinearModule/OddCyclic/Decomposition.lean#L104)
