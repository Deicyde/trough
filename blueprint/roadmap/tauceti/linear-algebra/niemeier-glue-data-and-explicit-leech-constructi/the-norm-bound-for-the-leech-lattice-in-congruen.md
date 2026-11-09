---
declaration: theorem
origin: cited
lean: TauCeti.BinaryGolay.thirtyTwo_le_sum_sq
statement: formalized
proof: formalized
---

# The norm bound for the Leech lattice in congruence coordinates

Let `m ∈ {0, 1}` and let
`b` be an integer vector reducing to a Golay codeword modulo two, and put `a = 2b + m 𝟙`. If
`∑ aᵢ ≡ 4m (mod 8)` and `a ≠ 0`, then `∑ aᵢ² ≥ 32`. These are the congruence conditions that
describe the Leech lattice in the coordinates `x = a / 2`, in which the halved dot product of `x`
with itself is `∑ aᵢ² / 8`; so the bound says that such an `x` has norm at least `4`.

```lean
TauCeti.BinaryGolay.thirtyTwo_le_sum_sq {m : ℤ} (hm : m = 0 ∨ m = 1) {b : Fin 24 → ℤ}
  (hb : (fun i => ↑(b i)) ∈ TauCeti.BinaryGolay.code) (hsum : ∑ i, (2 * b i + m) ≡ 4 * m [ZMOD 8])
  (hne : (fun i => 2 * b i + m) ≠ 0) : 32 ≤ ∑ i, (2 * b i + m) ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.BinaryGolay.thirtyTwo_le_sum_sq`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/ConstructionB/Golay.html#TauCeti.BinaryGolay.thirtyTwo_le_sum_sq).

## Sources

- [Tau Ceti documentation: `TauCeti.BinaryGolay.thirtyTwo_le_sum_sq`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/ConstructionB/Golay.html#TauCeti.BinaryGolay.thirtyTwo_le_sum_sq)
- [Source of `TauCeti.BinaryGolay.thirtyTwo_le_sum_sq` in TauCeti/LinearAlgebra/IntegralLattice/ConstructionB/Golay.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/IntegralLattice/ConstructionB/Golay.lean#L109)
- [Tau Ceti roadmap status: Niemeier glue data and explicit Leech constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Rank24LatticeConstructions/STATUS.md)
