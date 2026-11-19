---
declaration: theorem
origin: cited
lean: TauCeti.IsMorse.exists_criticalCount_mul_eq_finrank_add_coeff
statement: formalized
proof: formalized
---

# The coefficientwise Morse polynomial identity with module coefficients

There is one
polynomial `Q` with natural coefficients such that, in every degree, the critical count times
`dim V` is the dimension of singular homology plus the coefficient of `(1 + X) * Q`.
The equality is in `ℕ∞`, retaining the original critical counts rather than their `toNat` values.

```lean
TauCeti.IsMorse.exists_criticalCount_mul_eq_finrank_add_coeff.{u, u_1, u_2} {E : Type u_1}
  {H : Type u_2} {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [I.Boundaryless] [TopologicalSpace M] [ChartedSpace H M]
  [FiniteDimensional ℝ E] [IsManifold I (↑⊤) M] [T2Space M] [CompactSpace M] {f : M → ℝ}
  {k : Type u} [DivisionRing k] (hf : TauCeti.IsMorse I f) (V : ModuleCat k) [Module.Finite k ↑V] :
  ∃ Q,
    ∀ (j : ℕ),
      TauCeti.criticalCount I f j * ↑(Module.finrank k ↑V) =
        ↑(Module.finrank k
              ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) j).obj V).obj ↧M) +
            ((1 + Polynomial.X) * Q).coeff j)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Morse polynomial identity (`TauCeti.IsMorse.exists_criticalCount_eq_bettiNumber_add_coeff`)](../part-02/the-morse-polynomial-identity-tauceti-ismorse-ex.md)
- [The weak Morse inequalities](../part-02/the-weak-morse-inequalities.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_criticalCount_mul_eq_finrank_add_coeff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Polynomial.html#TauCeti.IsMorse.exists_criticalCount_mul_eq_finrank_add_coeff).

## Sources

- [Tau Ceti documentation: `TauCeti.IsMorse.exists_criticalCount_mul_eq_finrank_add_coeff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Polynomial.html#TauCeti.IsMorse.exists_criticalCount_mul_eq_finrank_add_coeff)
- [Source of `TauCeti.IsMorse.exists_criticalCount_mul_eq_finrank_add_coeff` in TauCeti/Geometry/Manifold/Morse/Polynomial.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Morse/Polynomial.lean#L48)
