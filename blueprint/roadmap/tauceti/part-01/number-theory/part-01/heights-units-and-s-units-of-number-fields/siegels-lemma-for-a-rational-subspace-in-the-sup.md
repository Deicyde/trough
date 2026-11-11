---
declaration: theorem
origin: cited
lean: Submodule.exists_ne_zero_mem_intPoints_norm_le
statement: formalized
proof: formalized
---

# Siegel's lemma for a rational subspace, in the sup norm

A nonzero subspace `V` of `ℚ^ι`
contains a nonzero integral point `z` whose sup norm is at most `H(V) ^ (1 / k)`, where `H(V)` is
the absolute Euclidean height of `V` and `k` its dimension.

```lean
Submodule.exists_ne_zero_mem_intPoints_norm_le.{u_1} {ι : Type u_1} [Fintype ι] [LinearOrder ι]
  {V : Submodule ℚ (ι → ℚ)} (hV : V ≠ ⊥) :
  ∃ z ∈ V.intPoints, z ≠ 0 ∧ ‖z‖ ≤ V.subspaceHeight ^ (↑(Module.finrank ℚ ↥V))⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cauchy–Binet formula](../../../linear-algebra/other-results/the-cauchy-binet-formula.md)
- [Minkowski's second theorem, upper bound, in terms of the successive minima](minkowskis-second-theorem-upper-bound-in-terms-o.md)
- [Vaaler's cube-slicing theorem](../../../measure-theory/measure/vaalers-cube-slicing-theorem.md)
- [ZLattice.successiveMin](zlattice-successivemin.md)

## Lean

Formalized in Tau Ceti as [`Submodule.exists_ne_zero_mem_intPoints_norm_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Arakelov/SiegelsLemma.html#Submodule.exists_ne_zero_mem_intPoints_norm_le).

## Sources

- [Tau Ceti documentation: `Submodule.exists_ne_zero_mem_intPoints_norm_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Arakelov/SiegelsLemma.html#Submodule.exists_ne_zero_mem_intPoints_norm_le)
- [Source of `Submodule.exists_ne_zero_mem_intPoints_norm_le` in TauCeti/NumberTheory/Height/Arakelov/SiegelsLemma.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Height/Arakelov/SiegelsLemma.lean#L67)
