---
declaration: theorem
origin: cited
lean: TauCeti.GaugeBasisExample.exists_basis_norm_le
statement: formalized
proof: formalized
---

# Cassels' basis lemma on `L`

Applied to the minima witnesses `e 0, …, e 4`, it gives a basis
`b` of `L` with `‖b i‖ ≤ max 1 ((i + 1) / 2)`.

```lean
TauCeti.GaugeBasisExample.exists_basis_norm_le :
  ∃ b, ∀ (i : Fin 5), ‖↑(b i)‖ ≤ max 1 ((↑↑i + 1) / 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GaugeBasisExample.exists_basis_norm_le`](https://taucetiproject.org/docs/TauCeti/Examples/Algebra/Module/ZLattice/GaugeBasis.html#TauCeti.GaugeBasisExample.exists_basis_norm_le).

## Sources

- [Tau Ceti documentation: `TauCeti.GaugeBasisExample.exists_basis_norm_le`](https://taucetiproject.org/docs/TauCeti/Examples/Algebra/Module/ZLattice/GaugeBasis.html#TauCeti.GaugeBasisExample.exists_basis_norm_le)
- [Source of `TauCeti.GaugeBasisExample.exists_basis_norm_le` in TauCeti/Examples/Algebra/Module/ZLattice/GaugeBasis.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Examples/Algebra/Module/ZLattice/GaugeBasis.lean#L235)
