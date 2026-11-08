---
declaration: theorem
origin: cited
lean: Submodule.exists_ne_zero_mem_intPoints_norm_le, NumberField.exists_ne_zero_int_vec_abs_le_of_house_le
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

- [The Cauchy–Binet formula](../../../../linear-algebra/other-results/the-cauchy-binet-formula.md)
- [Minkowski's second theorem, upper bound, in terms of the successive minima](../part-01/minkowskis-second-theorem-upper-bound-in-terms-o.md)
- [Vaaler's cube-slicing theorem](../part-01/vaalers-cube-slicing-theorem.md)
- [ZLattice.successiveMin](../part-01/zlattice-successivemin.md)

## Lean

Formalized in Tau Ceti as [`Submodule.exists_ne_zero_mem_intPoints_norm_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Arakelov/SiegelsLemma.html#Submodule.exists_ne_zero_mem_intPoints_norm_le).

## Other forms

**Siegel's lemma over a number field, with rational integer unknowns (Evertse, Theorem 3.20).** Formalized in Tau Ceti as [`NumberField.exists_ne_zero_int_vec_abs_le_of_house_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/SiegelsLemma.html#NumberField.exists_ne_zero_int_vec_abs_le_of_house_le).

```lean
NumberField.exists_ne_zero_int_vec_abs_le_of_house_le.{u_1, u_2, u_3} {K : Type u_1} [Field K]
  [NumberField K] {α : Type u_2} {β : Type u_3} [Fintype α] [Fintype β]
  (a : Matrix α β (NumberField.RingOfIntegers K)) {A : ℝ} (hA : 1 ≤ A)
  (hcard : Module.finrank ℚ K * Fintype.card α < Fintype.card β)
  (ha : ∀ (i : α) (j : β), NumberField.house ↑(a i j) ≤ A) :
  ∃ x,
    x ≠ 0 ∧
      (a.mulVec fun j => ↑(x j)) = 0 ∧
        ∀ (j : β),
          |↑(x j)| ≤
            (3 * ↑(Fintype.card β) * A) ^
              (↑(Module.finrank ℚ K) * ↑(Fintype.card α) /
                (↑(Fintype.card β) - ↑(Module.finrank ℚ K) * ↑(Fintype.card α)))
```

## Sources

- [Tau Ceti documentation: `Submodule.exists_ne_zero_mem_intPoints_norm_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Arakelov/SiegelsLemma.html#Submodule.exists_ne_zero_mem_intPoints_norm_le)
- [Source of `Submodule.exists_ne_zero_mem_intPoints_norm_le` in TauCeti/NumberTheory/Height/Arakelov/SiegelsLemma.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Height/Arakelov/SiegelsLemma.lean#L67)
