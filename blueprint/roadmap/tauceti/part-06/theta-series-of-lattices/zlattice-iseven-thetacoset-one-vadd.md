---
declaration: theorem
origin: cited
lean: ZLattice.IsEven.thetaCoset_one_vadd
statement: formalized
proof: formalized
---

# ZLattice.IsEven.thetaCoset_one_vadd

The translation law of the theta series of a coset of an even lattice: for `γ ∈ L^∨`,
`θ_{γ+L}(τ + 1) = e(q_L(γ)) θ_{γ+L}(τ)` with `e(q_L(γ)) = exp (π i ‖γ‖²)`.

```lean
ZLattice.IsEven.thetaCoset_one_vadd.{u_1} {E : Type u_1} [NormedAddCommGroup E] {L : Submodule ℤ E}
  [InnerProductSpace ℝ E] {γ : E} (hL : ZLattice.IsEven L) (hγ : γ ∈ ZLattice.dual L)
  (τ : UpperHalfPlane) :
  ZLattice.thetaCoset L γ (1 +ᵥ τ) =
    Complex.exp (↑Real.pi * Complex.I * ↑(‖γ‖ ^ 2)) * ZLattice.thetaCoset L γ τ
```

## Depends on

- [ZLattice.dual](zlattice-dual.md)
- [ZLattice.IsEven](zlattice-iseven.md)
- [ZLattice.thetaCoset](zlattice-thetacoset.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.IsEven.thetaCoset_one_vadd`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/Translation.html#ZLattice.IsEven.thetaCoset_one_vadd).

## Sources

- [Tau Ceti documentation: `ZLattice.IsEven.thetaCoset_one_vadd`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/Translation.html#ZLattice.IsEven.thetaCoset_one_vadd)
- [Source of `ZLattice.IsEven.thetaCoset_one_vadd` in TauCeti/NumberTheory/ModularForms/ThetaSeries/Translation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/ThetaSeries/Translation.lean#L156)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ThetaSeries/STATUS.md)
