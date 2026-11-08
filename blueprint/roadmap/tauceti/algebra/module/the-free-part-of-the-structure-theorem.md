---
declaration: theorem
origin: cited
lean: TauCeti.InternalGrading.exists_linearIndependent_isCompl_torsion
statement: formalized
proof: formalized
---

# The free part of the structure theorem

In a finitely generated graded `k[X]`-module over
a field on which `X` lowers degree by `d ≠ 0`, the torsion submodule has a complement spanned by a
`k[X]`-linearly independent family of homogeneous elements: `M` is its torsion submodule plus a
graded free module, one `X`-tower for each element of the family.

```lean
TauCeti.InternalGrading.exists_linearIndependent_isCompl_torsion.{u, u_1} {k : Type u_1}
  {M : Type u} [Field k] [AddCommGroup M] [_root_.Module k M] [_root_.Module (Polynomial k) M]
  [IsScalarTower k (Polynomial k) M] [Module.Finite (Polynomial k) M]
  {G : TauCeti.InternalGrading k M ℤ} {d : ℕ} (hd : d ≠ 0)
  (hX : ∀ ⦃p : ℤ⦄ ⦃x : M⦄, x ∈ G.piece ℤ p → Polynomial.X • x ∈ G.piece ℤ (p - ↑d)) :
  ∃ ι b deg,
    (∀ (i : ι), b i ∈ G.piece ℤ (deg i)) ∧
      LinearIndependent (Polynomial k) b ∧
        IsCompl (Submodule.torsion (Polynomial k) M) (Submodule.span (Polynomial k) (Set.range b))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.InternalGrading.exists_linearIndependent_isCompl_torsion`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/GradedModule/HomogeneousBasis.html#TauCeti.InternalGrading.exists_linearIndependent_isCompl_torsion).

## Sources

- [Tau Ceti documentation: `TauCeti.InternalGrading.exists_linearIndependent_isCompl_torsion`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/GradedModule/HomogeneousBasis.html#TauCeti.InternalGrading.exists_linearIndependent_isCompl_torsion)
- [Source of `TauCeti.InternalGrading.exists_linearIndependent_isCompl_torsion` in TauCeti/Algebra/Module/GradedModule/HomogeneousBasis.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Module/GradedModule/HomogeneousBasis.lean#L152)
