---
declaration: theorem
origin: cited
lean: CliffordAlgebra.trace_spinCGroupHalfSpinRep_one_sub_neg_one_mk_spinTorus
statement: formalized
proof: formalized
---

# The character of `W⁺ - W⁻` on the torus of `Spinᶜ(4)`

on two-dimensional half-spinors,
`tr ρ⁺ - tr ρ⁻ = z (w₁ - w₁⁻¹) (w₂ - w₂⁻¹)` at `[(w₁, w₂), z]`.

```lean
CliffordAlgebra.trace_spinCGroupHalfSpinRep_one_sub_neg_one_mk_spinTorus.{u_1, u_2} {V : Type u_1}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] {Q : QuadraticForm ℝ V}
  (b : OrthonormalBasis (Fin 4) ℝ V) (hQ : ∀ (v : V), Q v = -‖v‖ ^ 2)
  [Fact (Module.finrank ℝ V = 4)] {o : Orientation ℝ V (Fin 4)} {W : Type u_2} [AddCommGroup W]
  [_root_.Module ℂ W] (ρ : CliffordAlgebra Q →ₐ[ℝ] Module.End ℂ W) [FiniteDimensional ℂ W]
  (hb : b.toBasis.orientation = o) (hQ₀ : Q ≠ 0)
  (h₂ : Module.finrank ℂ ↥((ρ (CliffordAlgebra.chirality Q o)).eigenspace 1) = 2)
  (w₁ w₂ z : Circle) :
  (LinearMap.trace ℂ ↥((ρ (CliffordAlgebra.chirality Q o)).eigenspace 1))
        ((CliffordAlgebra.spinCGroupHalfSpinRep o ρ 1 hQ₀)
          ((CliffordAlgebra.spinCGroup.mk Q hQ₀) ((b.spinTorus hQ) (w₁, w₂), z))) -
      (LinearMap.trace ℂ ↥((ρ (CliffordAlgebra.chirality Q o)).eigenspace (-1)))
        ((CliffordAlgebra.spinCGroupHalfSpinRep o ρ (-1) hQ₀)
          ((CliffordAlgebra.spinCGroup.mk Q hQ₀) ((b.spinTorus hQ) (w₁, w₂), z))) =
    ↑z * (↑w₁ - (↑w₁)⁻¹) * (↑w₂ - (↑w₂)⁻¹)
```

## Depends on

- [The group `Spinᶜ(Q)`](the-group-spinc-q.md)

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.trace_spinCGroupHalfSpinRep_one_sub_neg_one_mk_spinTorus`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/TorusCharacter.html#CliffordAlgebra.trace_spinCGroupHalfSpinRep_one_sub_neg_one_mk_spinTorus).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.trace_spinCGroupHalfSpinRep_one_sub_neg_one_mk_spinTorus`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/TorusCharacter.html#CliffordAlgebra.trace_spinCGroupHalfSpinRep_one_sub_neg_one_mk_spinTorus)
- [Source of `CliffordAlgebra.trace_spinCGroupHalfSpinRep_one_sub_neg_one_mk_spinTorus` in TauCeti/LinearAlgebra/CliffordAlgebra/Spin/TorusCharacter.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/CliffordAlgebra/Spin/TorusCharacter.lean#L350)
- [Tau Ceti roadmap status: Four-dimensional Seiberg–Witten theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SeibergWittenTheory/STATUS.md)
