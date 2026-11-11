---
declaration: theorem
origin: cited
lean: Submodule.exists_basis_intPoints_prod_norm_le_subspaceHeight
statement: formalized
proof: formalized
---

# A basis of the integral points of small sup norm

For a subspace `V` of `ℚ^ι` of dimension
`k`, the integral points `V ∩ ℤ^ι` have a `ℤ`-basis `b` with
`∏ l, ‖b l‖ ≤ k! / 2 ^ (k - 1) * H(V)`, where `‖b l‖ = max_i |b l i|` is the sup norm and `H(V)`
is the absolute Euclidean height of `V`. Unlike the independent points of
`Submodule.exists_linearIndependent_intPoints_prod_norm_le`, these vectors span the whole of
`V ∩ ℤ^ι`, not only a sublattice of finite index.

```lean
Submodule.exists_basis_intPoints_prod_norm_le_subspaceHeight.{u_1} {ι : Type u_1} [Fintype ι]
  [LinearOrder ι] (V : Submodule ℚ (ι → ℚ)) :
  ∃ b,
    ∏ l, ‖↑(b l)‖ ≤
      ↑(Module.finrank ℚ ↥V).factorial / 2 ^ (Module.finrank ℚ ↥V - 1) * V.subspaceHeight
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A basis from the successive minima (Cassels, Chapter V, Lemma 8)](a-basis-from-the-successive-minima-cassels-chapt.md)
- [The Cauchy–Binet formula](../../../linear-algebra/other-results/the-cauchy-binet-formula.md)
- [Minkowski's second theorem, upper bound, in terms of the successive minima](minkowskis-second-theorem-upper-bound-in-terms-o.md)
- [Vaaler's cube-slicing theorem](../../../measure-theory/measure/vaalers-cube-slicing-theorem.md)
- [ZLattice.successiveMin](zlattice-successivemin.md)

## Lean

Formalized in Tau Ceti as [`Submodule.exists_basis_intPoints_prod_norm_le_subspaceHeight`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Arakelov/BombieriVaaler.html#Submodule.exists_basis_intPoints_prod_norm_le_subspaceHeight).

## Sources

- [Tau Ceti documentation: `Submodule.exists_basis_intPoints_prod_norm_le_subspaceHeight`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Arakelov/BombieriVaaler.html#Submodule.exists_basis_intPoints_prod_norm_le_subspaceHeight)
- [Source of `Submodule.exists_basis_intPoints_prod_norm_le_subspaceHeight` in TauCeti/NumberTheory/Height/Arakelov/BombieriVaaler.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Height/Arakelov/BombieriVaaler.lean#L127)
- [Tau Ceti roadmap status: Heights, units and S-units of number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/HeightsAndUnits/STATUS.md)
