---
declaration: theorem
origin: cited
lean: TauCeti.InternalGrading.exists_iSupIndep_iSup_span_singleton_eq_of_le_torsion
statement: formalized
proof: formalized
---

# The torsion part of the structure theorem

Let `X` lower degree by `d ≠ 0` in a finitely
generated graded `k[X]`-module over a field. Then every homogeneous `k[X]`-submodule `L` contained
in the torsion submodule is the independent sum of finitely many cyclic submodules `k[X] ∙ t i`,
where each `t i` is homogeneous with annihilator `(X ^ m i)` for some `m i ≠ 0`. Thus each summand
is isomorphic to `k[X] ⧸ (X ^ m i)` (`Ideal.quotTorsionOfEquivSpanSingleton`).

```lean
TauCeti.InternalGrading.exists_iSupIndep_iSup_span_singleton_eq_of_le_torsion.{u, u_1}
  {k : Type u_1} {M : Type u} [Field k] [AddCommGroup M] [_root_.Module k M]
  [_root_.Module (Polynomial k) M] [IsScalarTower k (Polynomial k) M]
  {G : TauCeti.InternalGrading k M ℤ} {d : ℕ} [Module.Finite (Polynomial k) M] (hd : d ≠ 0)
  (hX : ∀ ⦃p : ℤ⦄ ⦃x : M⦄, x ∈ G.piece ℤ p → Polynomial.X • x ∈ G.piece ℤ (p - ↑d))
  (L : Submodule (Polynomial k) M) (hL : DirectSum.SetLike.IsHomogeneous (G.piece ℤ) L)
  (hLT : L ≤ Submodule.torsion (Polynomial k) M) :
  ∃ ι,
    ∃ (_ : Finite ι),
      ∃ t deg m,
        (∀ (i : ι), t i ∈ G.piece ℤ (deg i)) ∧
          (∀ (i : ι), m i ≠ 0) ∧
            (∀ (i : ι), Ideal.torsionOf (Polynomial k) M (t i) = Ideal.span {Polynomial.X ^ m i}) ∧
              (iSupIndep fun i => Polynomial k ∙ t i) ∧ ⨆ i, Polynomial k ∙ t i = L
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.InternalGrading.exists_iSupIndep_iSup_span_singleton_eq_of_le_torsion`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/GradedModule/CyclicDecomposition.html#TauCeti.InternalGrading.exists_iSupIndep_iSup_span_singleton_eq_of_le_torsion).

## Sources

- [Tau Ceti documentation: `TauCeti.InternalGrading.exists_iSupIndep_iSup_span_singleton_eq_of_le_torsion`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/GradedModule/CyclicDecomposition.html#TauCeti.InternalGrading.exists_iSupIndep_iSup_span_singleton_eq_of_le_torsion)
- [Source of `TauCeti.InternalGrading.exists_iSupIndep_iSup_span_singleton_eq_of_le_torsion` in TauCeti/Algebra/Module/GradedModule/CyclicDecomposition.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Module/GradedModule/CyclicDecomposition.lean#L173)
