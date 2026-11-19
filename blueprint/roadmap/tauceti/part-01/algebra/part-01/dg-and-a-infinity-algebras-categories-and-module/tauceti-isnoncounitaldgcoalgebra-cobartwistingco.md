---
declaration: def
origin: cited
lean: TauCeti.IsNonCounitalDGCoalgebra.cobarTwistingCochainEquiv
statement: formalized
---

# TauCeti.IsNonCounitalDGCoalgebra.cobarTwistingCochainEquiv

The **cobar universal property**: DG algebra maps `ΩC → A` correspond bijectively to
cohomological twisting cochains `C → A`. The forward map is negative restriction to
desuspended generators, and the inverse is the tensor-algebra extension of `-τ`.

```lean
TauCeti.IsNonCounitalDGCoalgebra.cobarTwistingCochainEquiv.{uR, uC, uA} {R : Type uR} {C : Type uC}
  {A : Type uA} [CommRing R] [AddCommGroup C] [_root_.Module R C] [Ring A] [Algebra R A]
  {G : TauCeti.InternalGrading R C ℤ} {Δ : C →ₗ[R] TensorProduct R C C} {dC : C →ₗ[R] C}
  {𝒜 : ℤ → Submodule R A} {dA : A →ₗ[R] A} [GradedAlgebra 𝒜]
  (hC : TauCeti.IsNonCounitalDGCoalgebra G Δ dC) (hA : TauCeti.IsDGAlgebra 𝒜 dA) :
  TauCeti.DGAlgHom ⋯ hA ≃ { τ // TauCeti.IsTwistingCochain G Δ dC 𝒜 dA τ }
```

## Depends on

- [TauCeti.instGradedAlgebraIntTensorAlgebraTensorAlgebraPiece](../../../linear-algebra/part-01/contact-homology-and-the-symplectic-field-theory/tauceti-instgradedalgebrainttensoralgebratensora.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsNonCounitalDGCoalgebra.cobarTwistingCochainEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/DG/Coalgebra/Cobar/TwistingCochain.html#TauCeti.IsNonCounitalDGCoalgebra.cobarTwistingCochainEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.IsNonCounitalDGCoalgebra.cobarTwistingCochainEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/DG/Coalgebra/Cobar/TwistingCochain.html#TauCeti.IsNonCounitalDGCoalgebra.cobarTwistingCochainEquiv)
- [Source of `TauCeti.IsNonCounitalDGCoalgebra.cobarTwistingCochainEquiv` in TauCeti/Algebra/Homology/DG/Coalgebra/Cobar/TwistingCochain.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Homology/DG/Coalgebra/Cobar/TwistingCochain.lean#L200)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DGAInfinity/STATUS.md)
