---
declaration: theorem
origin: cited
lean: TauCeti.Toric.IsLatticeRational.fg_comap_toAddSubmonoid, TauCeti.Toric.IsLatticeRational.fg_dualSemigroup
statement: formalized
proof: formalized
---

# Gordan's lemma for lattice points

The lattice points of a lattice-rational cone form a
finitely generated additive submonoid. The cone may contain lines.

```lean
TauCeti.Toric.IsLatticeRational.fg_comap_toAddSubmonoid.{u_1, u_2} {N : Type u_1} {V : Type u_2}
  [AddCommGroup N] [AddCommGroup V] [_root_.Module ℝ V] {i : N →+ V} {σ : PointedCone ℝ V}
  (hσ : TauCeti.Toric.IsLatticeRational i σ) (hi : TauCeti.Toric.IsIntegralLattice i) :
  (AddSubmonoid.comap i σ.toAddSubmonoid).FG
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Tucker's theorem](../../part-02/convex/tuckers-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Toric.IsLatticeRational.fg_comap_toAddSubmonoid`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Algebraic/Cone/Finiteness.html#TauCeti.Toric.IsLatticeRational.fg_comap_toAddSubmonoid).

## Other forms

**Gordan's lemma.** Formalized in Tau Ceti as [`TauCeti.Toric.IsLatticeRational.fg_dualSemigroup`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Algebraic/DualSemigroup/Finiteness.html#TauCeti.Toric.IsLatticeRational.fg_dualSemigroup).

```lean
TauCeti.Toric.IsLatticeRational.fg_dualSemigroup.{u_1, u_2} {N : Type u_1} {V : Type u_2}
  [AddCommGroup N] [AddCommGroup V] [_root_.Module ℝ V] {i : N →+ V} {σ : PointedCone ℝ V}
  (hσ : TauCeti.Toric.IsLatticeRational i σ) (hi : TauCeti.Toric.IsIntegralLattice i) :
  AddMonoid.FG ↥(TauCeti.Toric.dualSemigroup hi σ)
```

## Sources

- [Tau Ceti documentation: `TauCeti.Toric.IsLatticeRational.fg_comap_toAddSubmonoid`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Algebraic/Cone/Finiteness.html#TauCeti.Toric.IsLatticeRational.fg_comap_toAddSubmonoid)
- [Source of `TauCeti.Toric.IsLatticeRational.fg_comap_toAddSubmonoid` in TauCeti/Geometry/Toric/Algebraic/Cone/Finiteness.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Toric/Algebraic/Cone/Finiteness.lean#L95)
- [Tau Ceti roadmap status: Scattering diagrams, wall crossing and theta functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ScatteringDiagrams/STATUS.md)
