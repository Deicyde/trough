---
declaration: theorem
origin: cited
lean: TauCeti.FiniteQuadraticModule.exists_isometry_prod_pi_generators
statement: formalized
proof: formalized
---

# Nikulin's generator decomposition

A nondegenerate finite quadratic module is isometric to
an orthogonal sum of Nikulin's generators: odd cyclic modules `q_θ^{(p)}(p^k)` of odd prime-power
order `m = p^k` with `θ` prime to `m`, dyadic cyclic modules `q_η^{(2)}(2^{k+1})` with `η` odd, and
rank-two modules `u^{(2)}(2^{k+1})` and `v^{(2)}(2^{k+1})`.

```lean
TauCeti.FiniteQuadraticModule.exists_isometry_prod_pi_generators.{u}
  (A : TauCeti.FiniteQuadraticModule) (hA : A.IsNondegenerate) :
  ∃ a m,
    ∃ (hm : ∀ (i : Fin a), Odd (m i)),
      ∃ θ b k η c ku d kv,
        (∀ (i : Fin a), IsPrimePow (m i) ∧ IsCoprime (↑(m i)) (θ i)) ∧
          (∀ (i : Fin b), Odd (η i)) ∧
            Nonempty
              (((TauCeti.FiniteQuadraticModule.pi fun i =>
                        TauCeti.FiniteQuadraticModule.oddCyclic (m i) ⋯ (θ i)).prod
                    ((TauCeti.FiniteQuadraticModule.pi fun i =>
                          TauCeti.FiniteQuadraticModule.dyadicCyclic (k i + 1) (η i)).prod
                      ((TauCeti.FiniteQuadraticModule.pi fun i =>
                            TauCeti.FiniteQuadraticModule.dyadicU (ku i + 1)).prod
                        (TauCeti.FiniteQuadraticModule.pi fun i =>
                          TauCeti.FiniteQuadraticModule.dyadicV (kv i + 1))))).Isometry
                A)
```

## Depends on

- [TauCeti.FiniteQuadraticModule](../../number-theory/part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteQuadraticModule.exists_isometry_prod_pi_generators`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/FiniteBilinearModule/Decomposition.html#TauCeti.FiniteQuadraticModule.exists_isometry_prod_pi_generators).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteQuadraticModule.exists_isometry_prod_pi_generators`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/FiniteBilinearModule/Decomposition.html#TauCeti.FiniteQuadraticModule.exists_isometry_prod_pi_generators)
- [Source of `TauCeti.FiniteQuadraticModule.exists_isometry_prod_pi_generators` in TauCeti/LinearAlgebra/FiniteBilinearModule/Decomposition.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/FiniteBilinearModule/Decomposition.lean#L99)
