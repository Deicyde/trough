---
declaration: theorem
origin: cited
lean: TauCeti.Toric.IsLatticeRational.fg_dualSemigroup
statement: formalized
proof: formalized
---

# Gordan's lemma

The dual semigroup of a lattice-rational cone in an integral lattice is
finitely generated. Salience is not required.

```lean
TauCeti.Toric.IsLatticeRational.fg_dualSemigroup.{u_1, u_2} {N : Type u_1} {V : Type u_2}
  [AddCommGroup N] [AddCommGroup V] [_root_.Module ℝ V] {i : N →+ V} {σ : PointedCone ℝ V}
  (hσ : TauCeti.Toric.IsLatticeRational i σ) (hi : TauCeti.Toric.IsIntegralLattice i) :
  AddMonoid.FG ↥(TauCeti.Toric.dualSemigroup hi σ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Toric.IsLatticeRational.fg_dualSemigroup`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Algebraic/DualSemigroup/Finiteness.html#TauCeti.Toric.IsLatticeRational.fg_dualSemigroup).

## Sources

- [Tau Ceti documentation: `TauCeti.Toric.IsLatticeRational.fg_dualSemigroup`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Algebraic/DualSemigroup/Finiteness.html#TauCeti.Toric.IsLatticeRational.fg_dualSemigroup)
- [Source of `TauCeti.Toric.IsLatticeRational.fg_dualSemigroup` in TauCeti/Geometry/Toric/Algebraic/DualSemigroup/Finiteness.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Toric/Algebraic/DualSemigroup/Finiteness.lean#L44)
