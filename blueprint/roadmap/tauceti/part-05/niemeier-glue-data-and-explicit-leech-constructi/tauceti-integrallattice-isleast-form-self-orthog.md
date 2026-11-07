---
declaration: theorem
origin: cited
lean: TauCeti.IntegralLattice.isLeast_form_self_orthogonalSum
statement: formalized
proof: formalized
---

# TauCeti.IntegralLattice.isLeast\_form\_self\_orthogonalSum

Attained least norms in two discriminant cosets add to the attained least norm of the
corresponding coset of the orthogonal sum.

```lean
TauCeti.IntegralLattice.isLeast_form_self_orthogonalSum.{u, v} {V : Type u} {W : Type v}
  [AddCommGroup V] [_root_.Module ℚ V] [AddCommGroup W] [_root_.Module ℚ W]
  (L : TauCeti.IntegralLattice V) (M : TauCeti.IntegralLattice W) {a : L.DiscriminantGroup}
  {b : M.DiscriminantGroup} {r s : ℚ}
  (hL : IsLeast {q | ∃ x, Submodule.Quotient.mk x = a ∧ (L.form ↑x) ↑x = q} r)
  (hM : IsLeast {q | ∃ y, Submodule.Quotient.mk y = b ∧ (M.form ↑y) ↑y = q} s) :
  IsLeast
    {q |
      ∃ x,
        Submodule.Quotient.mk x = (L.discriminantGroupOrthogonalSumEquiv M).symm (a, b) ∧
          ((L.orthogonalSum M).form ↑x) ↑x = q}
    (r + s)
```

## Depends on

- [TauCeti.IntegralLattice](../../part-04/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.isLeast_form_self_orthogonalSum`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Orthogonal/CosetMinimum.html#TauCeti.IntegralLattice.isLeast_form_self_orthogonalSum).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.isLeast_form_self_orthogonalSum`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Orthogonal/CosetMinimum.html#TauCeti.IntegralLattice.isLeast_form_self_orthogonalSum)
- [Source of `TauCeti.IntegralLattice.isLeast_form_self_orthogonalSum` in TauCeti/LinearAlgebra/IntegralLattice/Orthogonal/CosetMinimum.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/IntegralLattice/Orthogonal/CosetMinimum.lean#L76)
- [Tau Ceti roadmap status: Niemeier glue data and explicit Leech constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Rank24LatticeConstructions/STATUS.md)
