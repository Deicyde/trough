---
declaration: theorem
origin: cited
lean: TauCeti.cyclicCohomology.oddPairing_matrixExtension_of_val_eq_fromBlocks_one
statement: formalized
proof: formalized
---

# Stabilization of the odd pairing

enlarging an invertible matrix `u` to the block diagonal
matrix `u ⊕ 1` does not change its odd pairing.

```lean
TauCeti.cyclicCohomology.oddPairing_matrixExtension_of_val_eq_fromBlocks_one.{u_1, u_2, u_3, u_4}
  {A : Type u_1} {M : Type u_2} [Ring A] [Algebra ℂ A] [AddCommGroup M] [_root_.Module ℂ M]
  {ι : Type u_3} {κ : Type u_4} [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ]
  {w : (Matrix (ι ⊕ κ) (ι ⊕ κ) A)ˣ} {u : (Matrix ι ι A)ˣ} (hw : ↑w = Matrix.fromBlocks (↑u) 0 0 1)
  (m : ℕ) (c : ↑(TauCeti.cyclicCohomology ℂ A M (2 * m + 1))) :
  (TauCeti.cyclicCohomology.oddPairing w m)
      ((TauCeti.cyclicCohomology.matrixExtension M (ι ⊕ κ) (2 * m + 1)) c) =
    (TauCeti.cyclicCohomology.oddPairing u m)
      ((TauCeti.cyclicCohomology.matrixExtension M ι (2 * m + 1)) c)
```

## Depends on

- [TauCeti.cyclicCohomology.matrixExtension](tauceti-cycliccohomology-matrixextension.md)
- [TauCeti.cyclicCohomology.oddPairing](tauceti-cycliccohomology-oddpairing.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.cyclicCohomology.oddPairing_matrixExtension_of_val_eq_fromBlocks_one`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/OddPairing/Basic.html#TauCeti.cyclicCohomology.oddPairing_matrixExtension_of_val_eq_fromBlocks_one).

## Sources

- [Tau Ceti documentation: `TauCeti.cyclicCohomology.oddPairing_matrixExtension_of_val_eq_fromBlocks_one`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/OddPairing/Basic.html#TauCeti.cyclicCohomology.oddPairing_matrixExtension_of_val_eq_fromBlocks_one)
- [Source of `TauCeti.cyclicCohomology.oddPairing_matrixExtension_of_val_eq_fromBlocks_one` in TauCeti/RingTheory/CyclicCohomology/OddPairing/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/CyclicCohomology/OddPairing/Basic.lean#L192)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
