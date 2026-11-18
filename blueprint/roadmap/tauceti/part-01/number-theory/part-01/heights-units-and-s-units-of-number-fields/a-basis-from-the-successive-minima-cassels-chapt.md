---
declaration: theorem
origin: cited
lean: ZLattice.exists_basis_mem_smul_successiveMin
statement: formalized
proof: formalized
---

# A basis from the successive minima (Cassels, Chapter V, Lemma 8)

For a discrete spanning
lattice `L` and a symmetric convex body `K` with `0` in its interior, some `ℤ`-basis `b` of `L` has
`b i ∈ (max 1 ((i + 1) / 2) * successiveMin L K i) • K` for every `i`. The factor is `1` for
`i ≤ 1`, and the product of the factors is `n! / 2 ^ (n - 1)`
(`TauCeti.prod_max_one_add_one_div_two`).

```lean
ZLattice.exists_basis_mem_smul_successiveMin.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {K : ConvexBody E} (L : Submodule ℤ E) [DiscreteTopology ↥L] [IsZLattice ℝ L]
  (hK : 0 ∈ interior ↑K) (hsymm : ∀ x ∈ K, -x ∈ K) :
  ∃ b,
    ∀ (i : Fin (Module.finrank ℝ E)),
      ↑(b i) ∈ (max 1 ((↑↑i + 1) / 2) * ZLattice.successiveMin L K i) • ↑K
```

## Depends on

- [ZLattice.successiveMin](zlattice-successivemin.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.exists_basis_mem_smul_successiveMin`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/SuccessiveMinima.html#ZLattice.exists_basis_mem_smul_successiveMin).

## Sources

- [Tau Ceti documentation: `ZLattice.exists_basis_mem_smul_successiveMin`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/SuccessiveMinima.html#ZLattice.exists_basis_mem_smul_successiveMin)
- [Source of `ZLattice.exists_basis_mem_smul_successiveMin` in TauCeti/Algebra/Module/ZLattice/SuccessiveMinima.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Module/ZLattice/SuccessiveMinima.lean#L587)
- [Tau Ceti roadmap status: Heights, units and S-units of number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/HeightsAndUnits/STATUS.md)
