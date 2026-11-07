---
declaration: theorem
origin: cited
lean: Module.Basis.existsUnique_ringHom_nonneg
statement: formalized
proof: formalized
---

# The Frobenius–Perron character

A ring with a finite nonempty `ℤ`-basis with nonnegative
structure constants, such that every basis element occurs in `b j * ∑ i, b i` for every `j`, has
exactly one character to `ℝ` which is nonnegative on the basis.

```lean
Module.Basis.existsUnique_ringHom_nonneg.{u_1, u_2} {ι : Type u_1} {R : Type u_2} [Fintype ι]
  [Ring R] (b : Module.Basis ι ℤ R) (hb : ∀ (i j l : ι), 0 ≤ (b.repr (b i * b j)) l)
  (ht : ∀ (j l : ι), 0 < ∑ i, (b.repr (b j * b i)) l) [Nonempty ι] : ∃! χ, ∀ (i : ι), 0 ≤ χ (b i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Module.Basis.existsUnique_ringHom_nonneg`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Character.html#Module.Basis.existsUnique_ringHom_nonneg).

## Sources

- [Tau Ceti documentation: `Module.Basis.existsUnique_ringHom_nonneg`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Character.html#Module.Basis.existsUnique_ringHom_nonneg)
- [Source of `Module.Basis.existsUnique_ringHom_nonneg` in TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Character.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Character.lean#L190)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PivotalSpherical/STATUS.md)
