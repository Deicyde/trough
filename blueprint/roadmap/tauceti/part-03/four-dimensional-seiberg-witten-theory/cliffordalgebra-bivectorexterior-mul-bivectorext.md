---
declaration: theorem
origin: cited
lean: CliffordAlgebra.bivectorExterior_mul_bivectorExterior_add_swap
statement: formalized
proof: formalized
---

# CliffordAlgebra.bivectorExterior\_mul\_bivectorExterior\_add\_swap

**The anticommutator of two two-forms** in the Clifford algebra of an oriented four-space:
`c₂(α) c₂(β) + c₂(β) c₂(α) = -2 ⟪α, β⟫ - 2 ⟪⋆α, β⟫ Γ`. Since `α ∧ β = ⟪⋆α, β⟫ vol`, the
coefficient of `Γ` is minus twice the volume of `α ∧ β`.

```lean
CliffordAlgebra.bivectorExterior_mul_bivectorExterior_add_swap.{u_1} {V : Type u_1}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] {Q : QuadraticForm ℝ V}
  [Fact (Module.finrank ℝ V = 4)] (o : Orientation ℝ V (Fin 4)) (hQ : ∀ (v : V), Q v = -‖v‖ ^ 2)
  (hkl : 2 + 2 = Module.finrank ℝ V) (x y : ↥(⋀[ℝ]^2 V)) :
  (CliffordAlgebra.bivectorExterior Q) x * (CliffordAlgebra.bivectorExterior Q) y +
      (CliffordAlgebra.bivectorExterior Q) y * (CliffordAlgebra.bivectorExterior Q) x =
    (algebraMap ℝ (CliffordAlgebra Q)) (-2 * inner ℝ x y) -
      (2 * inner ℝ ((o.hodgeStar hkl) x) y) • CliffordAlgebra.chirality Q o
```

## Depends on

- [Orientation.hodgeStar](orientation-hodgestar.md)

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.bivectorExterior_mul_bivectorExterior_add_swap`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Chirality.html#CliffordAlgebra.bivectorExterior_mul_bivectorExterior_add_swap).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.bivectorExterior_mul_bivectorExterior_add_swap`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Chirality.html#CliffordAlgebra.bivectorExterior_mul_bivectorExterior_add_swap)
- [Source of `CliffordAlgebra.bivectorExterior_mul_bivectorExterior_add_swap` in TauCeti/LinearAlgebra/CliffordAlgebra/Chirality.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/CliffordAlgebra/Chirality.lean#L430)
- [Tau Ceti roadmap status: Four-dimensional Seiberg–Witten theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SeibergWittenTheory/STATUS.md)
