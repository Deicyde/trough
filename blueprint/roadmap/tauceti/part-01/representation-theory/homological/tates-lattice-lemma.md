---
declaration: theorem
origin: cited
lean: TauCeti.TateCohomology.herbrandQuotient_eq_of_isBaseChange
statement: formalized
proof: formalized
---

# Tate's lattice lemma

Let `G` be a finite cyclic group, `K` a nontrivial commutative
`ℚ`-algebra (classically `ℝ`) and `ρ` a representation of `G` on a `K`-module `V`. If `M` and `N`
are integral representations of `G`, free over `ℤ` with `M` of finite rank, and `G`-equivariant
maps `i : M → V` and `j : N → V` exhibit `V` as the base change of `M` and of `N` to `K`, then `M`
and `N` have the same Herbrand quotient. The rank of `N` is then finite as well, being that of
`V`.

```lean
TauCeti.TateCohomology.herbrandQuotient_eq_of_isBaseChange.{u_1, u_2} {G : Type} [Group G]
  [Fintype G] [IsCyclic G] {K : Type u_1} {V : Type u_2} [CommRing K] [Nontrivial K] [Algebra ℚ K]
  [AddCommGroup V] [_root_.Module K V] (ρ : Representation K G V) {M N : Rep.{0, 0, 0} ℤ G}
  [Module.Free ℤ ↑M] [Module.Finite ℤ ↑M] [Module.Free ℤ ↑N] {i : ↑M →ₗ[ℤ] V} {j : ↑N →ₗ[ℤ] V}
  (hi : IsBaseChange K i) (hj : IsBaseChange K j)
  (hiG : ∀ (g : G) (x : ↑M), i ((M.ρ g) x) = (ρ g) (i x))
  (hjG : ∀ (g : G) (y : ↑N), j ((N.ρ g) y) = (ρ g) (j y)) :
  TauCeti.TateCohomology.herbrandQuotient M = TauCeti.TateCohomology.herbrandQuotient N
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TateCohomology.herbrandQuotient_eq_of_isBaseChange`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/TateCohomology/Lattice.html#TauCeti.TateCohomology.herbrandQuotient_eq_of_isBaseChange).

## Sources

- [Tau Ceti documentation: `TauCeti.TateCohomology.herbrandQuotient_eq_of_isBaseChange`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/TateCohomology/Lattice.html#TauCeti.TateCohomology.herbrandQuotient_eq_of_isBaseChange)
- [Source of `TauCeti.TateCohomology.herbrandQuotient_eq_of_isBaseChange` in TauCeti/RepresentationTheory/Homological/TateCohomology/Lattice.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Homological/TateCohomology/Lattice.lean#L58)
