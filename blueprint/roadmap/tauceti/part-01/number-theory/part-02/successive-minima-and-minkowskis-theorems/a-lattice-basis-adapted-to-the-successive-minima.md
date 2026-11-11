---
declaration: theorem
origin: cited
lean: ZLattice.exists_basis_mem_flag_of_gauge_lt_successiveMin
statement: formalized
proof: formalized
---

# A lattice basis adapted to the successive minima (Cassels, Chapter VIII, Lemma 2)

For a
discrete spanning lattice `L` and a convex body `K` with `0` in its interior, some `ℤ`-basis `b` of
`L` has the following property: every vector of `L` of gauge less than the `i`-th minimum lies in
the span over `ℝ` of `b 0, …, b (i - 1)`, the flag `(b.ofZLatticeBasis ℝ L).flag i.castSucc`. The
body need not be symmetric. No bound on the gauges of the `b i` is claimed; for symmetric `K`,
`ZLattice.exists_basis_mem_smul_successiveMin` gives one.

```lean
ZLattice.exists_basis_mem_flag_of_gauge_lt_successiveMin.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {K : ConvexBody E} [FiniteDimensional ℝ E] (L : Submodule ℤ E)
  [DiscreteTopology ↥L] [IsZLattice ℝ L] (hK : 0 ∈ interior ↑K) :
  ∃ b,
    ∀ (i : Fin (Module.finrank ℝ E)),
      ∀ x ∈ L,
        gauge (↑K) x < ZLattice.successiveMin L K i →
          x ∈ (Module.Basis.ofZLatticeBasis ℝ L b).flag i.castSucc
```

## Depends on

- [ZLattice.successiveMin](../../part-01/heights-units-and-s-units-of-number-fields/zlattice-successivemin.md)

## Proof depends on

- [A real basis attaining the successive minima](a-real-basis-attaining-the-successive-minima.md)
- [Lattice basis with a prescribed flag](lattice-basis-with-a-prescribed-flag.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.exists_basis_mem_flag_of_gauge_lt_successiveMin`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/SuccessiveMinima.html#ZLattice.exists_basis_mem_flag_of_gauge_lt_successiveMin).

## Sources

- [Tau Ceti documentation: `ZLattice.exists_basis_mem_flag_of_gauge_lt_successiveMin`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/SuccessiveMinima.html#ZLattice.exists_basis_mem_flag_of_gauge_lt_successiveMin)
- [Source of `ZLattice.exists_basis_mem_flag_of_gauge_lt_successiveMin` in TauCeti/Algebra/Module/ZLattice/SuccessiveMinima.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Module/ZLattice/SuccessiveMinima.lean#L569)
- [Tau Ceti roadmap status: Successive minima and Minkowski's theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SuccessiveMinima/STATUS.md)
