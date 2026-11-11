---
declaration: theorem
origin: cited
lean: ZLattice.exists_basis_gauge_eq_successiveMin
statement: formalized
proof: formalized
---

# A real basis attaining the successive minima

For a discrete spanning lattice `L` and a
convex body `K` with `0` in its interior, some basis `b` of `E` over `ℝ` consists of vectors of `L`
with `gauge K (b i) = successiveMin L K i`, so that `b i ∈ successiveMin L K i • K`, for every `i`.
Moreover every vector of `L` of gauge less than the `i`-th minimum lies in the flag
`b.flag i.castSucc`, the span of `b 0, …, b (i - 1)`. The body need not be symmetric, and `b` need
not be a `ℤ`-basis of `L`.

```lean
ZLattice.exists_basis_gauge_eq_successiveMin.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {K : ConvexBody E} (L : Submodule ℤ E) [DiscreteTopology ↥L] [IsZLattice ℝ L]
  (hK : 0 ∈ interior ↑K) :
  ∃ b,
    (∀ (i : Fin (Module.finrank ℝ E)), b i ∈ L) ∧
      (∀ (i : Fin (Module.finrank ℝ E)), gauge (↑K) (b i) = ZLattice.successiveMin L K i) ∧
        (∀ (i : Fin (Module.finrank ℝ E)), b i ∈ ZLattice.successiveMin L K i • ↑K) ∧
          ∀ (i : Fin (Module.finrank ℝ E)),
            ∀ x ∈ L, gauge (↑K) x < ZLattice.successiveMin L K i → x ∈ b.flag i.castSucc
```

## Depends on

- [ZLattice.successiveMin](../../part-01/heights-units-and-s-units-of-number-fields/zlattice-successivemin.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.exists_basis_gauge_eq_successiveMin`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/SuccessiveMinima.html#ZLattice.exists_basis_gauge_eq_successiveMin).

## Sources

- [Tau Ceti documentation: `ZLattice.exists_basis_gauge_eq_successiveMin`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/SuccessiveMinima.html#ZLattice.exists_basis_gauge_eq_successiveMin)
- [Source of `ZLattice.exists_basis_gauge_eq_successiveMin` in TauCeti/Algebra/Module/ZLattice/SuccessiveMinima.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Module/ZLattice/SuccessiveMinima.lean#L545)
- [Tau Ceti roadmap status: Successive minima and Minkowski's theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SuccessiveMinima/STATUS.md)
