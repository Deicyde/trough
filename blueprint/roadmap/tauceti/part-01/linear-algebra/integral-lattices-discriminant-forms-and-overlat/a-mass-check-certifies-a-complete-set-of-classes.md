---
declaration: theorem
origin: cited
lean: TauCeti.IntegralLattice.sum_inv_natCard_isometry_eq_mass_iff
statement: formalized
proof: formalized
---

# A mass check certifies a complete set of classes

Let each lattice in the genus of `L` have
a finite isometry group, as for a definite lattice. Then, for pairwise non-isometric lattices in
the genus, the reciprocal orders of their isometry groups sum to the mass exactly when their
number is the class number. In a genus with finitely many classes this says that they represent
every class: a missing class would contribute a positive term. For a genus with infinitely many
classes the mass and the class number are `0` by convention and both sides say that the family is
empty.

```lean
TauCeti.IntegralLattice.sum_inv_natCard_isometry_eq_mass_iff.{u, u_2} {V : Type u} [AddCommGroup V]
  [_root_.Module ℚ V] {L : TauCeti.IntegralLattice V} {ι : Type u_2} [Fintype ι]
  {f : ι → TauCeti.IntegralLattice V}
  (hO : ∀ (M : TauCeti.IntegralLattice V), L.SameGenus M → Finite (M.Isometry M))
  (hgen : ∀ (i : ι), L.SameGenus (f i)) (hf : Pairwise fun i j => IsEmpty ((f i).Isometry (f j))) :
  ∑ i, (↑(Nat.card ((f i).Isometry (f i))))⁻¹ = L.mass ↔ Nat.card ι = L.classNumber
```

## Depends on

- [TauCeti.IntegralLattice](tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.mass](tauceti-integrallattice-mass.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.sum_inv_natCard_isometry_eq_mass_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/Mass.html#TauCeti.IntegralLattice.sum_inv_natCard_isometry_eq_mass_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.sum_inv_natCard_isometry_eq_mass_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/Mass.html#TauCeti.IntegralLattice.sum_inv_natCard_isometry_eq_mass_iff)
- [Source of `TauCeti.IntegralLattice.sum_inv_natCard_isometry_eq_mass_iff` in TauCeti/NumberTheory/IntegralLattice/Mass.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/IntegralLattice/Mass.lean#L288)
- [Tau Ceti roadmap status: Integral lattices, discriminant forms, and overlattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/IntegralLattices/STATUS.md)
