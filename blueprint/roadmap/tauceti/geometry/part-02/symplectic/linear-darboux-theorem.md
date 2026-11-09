---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.exists_isSymplectomorphism
statement: formalized
proof: formalized
---

# Linear Darboux theorem

Two symplectic vector spaces of the same finite dimension are
linearly symplectomorphic.

```lean
TauCeti.SymplecticForm.exists_isSymplectomorphism.{u_1, u_2} {V : Type u_1} {W : Type u_2}
  [AddCommGroup V] [_root_.Module ℝ V] [AddCommGroup W] [_root_.Module ℝ W] [FiniteDimensional ℝ V]
  [FiniteDimensional ℝ W] (ω₁ : TauCeti.SymplecticForm V) (ω₂ : TauCeti.SymplecticForm W)
  (hdim : Module.finrank ℝ V = Module.finrank ℝ W) : ∃ e, ω₁.IsSymplectomorphism ω₂ e
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Witt's extension theorem](witts-extension-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.exists_isSymplectomorphism`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/WittExtension.html#TauCeti.SymplecticForm.exists_isSymplectomorphism).

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.exists_isSymplectomorphism`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/WittExtension.html#TauCeti.SymplecticForm.exists_isSymplectomorphism)
- [Source of `TauCeti.SymplecticForm.exists_isSymplectomorphism` in TauCeti/Geometry/Symplectic/WittExtension.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/WittExtension.lean#L222)
