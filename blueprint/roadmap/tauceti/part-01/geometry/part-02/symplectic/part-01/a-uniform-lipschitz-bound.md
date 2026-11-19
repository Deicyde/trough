---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.exists_forall_lipschitzOnWith_hamiltonianVectorField
statement: formalized
proof: formalized
---

# A uniform Lipschitz bound

For a jointly `C²`, `1`-periodic Hamiltonian family `H`, the
vector fields `X_{H_t}` are Lipschitz on every bounded set `s`, with a constant independent of
`t`.

```lean
TauCeti.SymplecticForm.exists_forall_lipschitzOnWith_hamiltonianVectorField.{u_2} {V : Type u_2}
  [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V] (ω : TauCeti.SymplecticForm V)
  {H : ℝ → V → ℝ} (hH : ContDiff ℝ 2 (Function.uncurry H)) (hHper : Function.Periodic H 1)
  {s : Set V} (hs : Bornology.IsBounded s) :
  ∃ L, ∀ (t : ℝ), LipschitzOnWith L (ω.hamiltonianVectorField (H t)) s
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.exists_forall_lipschitzOnWith_hamiltonianVectorField`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Variation.html#TauCeti.SymplecticForm.exists_forall_lipschitzOnWith_hamiltonianVectorField).

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.exists_forall_lipschitzOnWith_hamiltonianVectorField`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Variation.html#TauCeti.SymplecticForm.exists_forall_lipschitzOnWith_hamiltonianVectorField)
- [Source of `TauCeti.SymplecticForm.exists_forall_lipschitzOnWith_hamiltonianVectorField` in TauCeti/Geometry/Symplectic/Hamiltonian/Variation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Hamiltonian/Variation.lean#L58)
