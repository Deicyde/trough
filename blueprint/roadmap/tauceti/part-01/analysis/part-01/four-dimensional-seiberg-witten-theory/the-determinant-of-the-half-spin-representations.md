---
declaration: theorem
origin: cited
lean: CliffordAlgebra.det_spinCGroupHalfSpinRep
statement: formalized
proof: formalized
---

# The determinant of the half-spin representations of `Spinᶜ(4)` is the determinant character

on an eigenspace of `Γ` of complex dimension two, `x` acts with determinant
`det x`, which is `z²` at `x = [s, z]`.

```lean
CliffordAlgebra.det_spinCGroupHalfSpinRep.{u_1, u_2} {V : Type u_1} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [Fact (Module.finrank ℝ V = 4)] {Q : QuadraticForm ℝ V}
  (o : Orientation ℝ V (Fin 4)) {W : Type u_2} [AddCommGroup W] [_root_.Module ℂ W]
  (ρ : CliffordAlgebra Q →ₐ[ℝ] Module.End ℂ W) (ε : ℂ) (hQ₀ : Q ≠ 0)
  (hQ : ∀ (v : V), Q v = -‖v‖ ^ 2)
  (h₂ : Module.finrank ℂ ↥((ρ (CliffordAlgebra.chirality Q o)).eigenspace ε) = 2)
  (x : CliffordAlgebra.spinCGroup Q hQ₀) :
  LinearMap.det ((CliffordAlgebra.spinCGroupHalfSpinRep o ρ ε hQ₀) x) =
    ↑((CliffordAlgebra.spinCGroup.det Q hQ₀) x)
```

## Depends on

- [The group `Spinᶜ(Q)`](the-group-spinc-q.md)

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.det_spinCGroupHalfSpinRep`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/HalfSpin.html#CliffordAlgebra.det_spinCGroupHalfSpinRep).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.det_spinCGroupHalfSpinRep`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/HalfSpin.html#CliffordAlgebra.det_spinCGroupHalfSpinRep)
- [Source of `CliffordAlgebra.det_spinCGroupHalfSpinRep` in TauCeti/LinearAlgebra/CliffordAlgebra/Spin/HalfSpin.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/HalfSpin.lean#L287)
- [Tau Ceti roadmap status: Four-dimensional Seiberg–Witten theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SeibergWittenTheory/STATUS.md)
