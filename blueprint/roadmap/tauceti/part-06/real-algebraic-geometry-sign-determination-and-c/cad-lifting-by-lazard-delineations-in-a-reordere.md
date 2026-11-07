---
declaration: theorem
origin: cited
lean: TauCeti.IsCAD.exists_isCAD_lazardValuation_eq_of_lazardDelineation_reindex
statement: formalized
proof: formalized
---

# CAD lifting by Lazard delineations in a reordered base

Suppose every cell `C` of a
cylindrical algebraic decomposition of `ℝ ^ n` is an analytic submanifold, and its reordering
`(· ∘ e.symm) ⁻¹' C` by a permutation `e` of the base coordinates carries a Lazard delineation
of a fixed polynomial family. Then the stacks of those delineations, pulled back to the
original cells, form a cylindrical algebraic decomposition of `ℝ ^ (n + 1)` with the original
decomposition as its projection.

Every lifted cell is an analytic submanifold. On it, every family member has constant Lazard
valuation when the base coordinates are read through `e` and the new coordinate is read last.

```lean
TauCeti.IsCAD.exists_isCAD_lazardValuation_eq_of_lazardDelineation_reindex.{u_1} {n : ℕ}
  {ι : Type u_1} {F : ι → MvPolynomial (Fin (n + 1)) ℝ} {𝓓 : Set (Set (Fin n → ℝ))}
  (h𝓓 : TauCeti.IsCAD n 𝓓) (e : Equiv.Perm (Fin n))
  (hanalytic : ∀ C ∈ 𝓓, ∃ d, TauCeti.IsAnalyticSubmanifold d C)
  (hD : ∀ C ∈ 𝓓, Nonempty (TauCeti.LazardDelineation F ((fun x => x ∘ ⇑(Equiv.symm e)) ⁻¹' C))) :
  ∃ 𝓒,
    TauCeti.IsCAD (n + 1) 𝓒 ∧
      Set.image Fin.tail '' 𝓒 = 𝓓 ∧
        (∀ E ∈ 𝓒, ∃ d, TauCeti.IsAnalyticSubmanifold d E) ∧
          ∀ (k : ι),
            ∀ E ∈ 𝓒,
              ∀ x ∈ E,
                ∀ y ∈ E,
                  (F k).lazardValuation (Fin.snoc (Fin.tail x ∘ ⇑e) (x 0)) =
                    (F k).lazardValuation (Fin.snoc (Fin.tail y ∘ ⇑e) (y 0))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsCAD.exists_isCAD_lazardValuation_eq_of_lazardDelineation_reindex`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/Lazard/Basic.html#TauCeti.IsCAD.exists_isCAD_lazardValuation_eq_of_lazardDelineation_reindex).

## Sources

- [Tau Ceti documentation: `TauCeti.IsCAD.exists_isCAD_lazardValuation_eq_of_lazardDelineation_reindex`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/Lazard/Basic.html#TauCeti.IsCAD.exists_isCAD_lazardValuation_eq_of_lazardDelineation_reindex)
- [Source of `TauCeti.IsCAD.exists_isCAD_lazardValuation_eq_of_lazardDelineation_reindex` in TauCeti/Geometry/RealAlgebraic/CAD/Lazard/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAlgebraic/CAD/Lazard/Basic.lean#L61)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RealAlgebraicGeometry/STATUS.md)
