---
declaration: theorem
origin: cited
lean: Submodule.orthogonalBilin_orthogonalBilin_topDualPairing_eq_topologicalClosure
statement: formalized
proof: formalized
---

# Norm double-annihilator theorem

The preannihilator of the continuous annihilator
of a subspace is its norm closure.

```lean
Submodule.orthogonalBilin_orthogonalBilin_topDualPairing_eq_topologicalClosure.{u_3, u_4}
  {𝕜 : Type u_3} [RCLike 𝕜] {E : Type u_4} [SeminormedAddCommGroup E] [NormedSpace 𝕜 E]
  (S : Submodule 𝕜 E) :
  Submodule.orthogonalBilin (topDualPairing 𝕜 E)
      (Submodule.orthogonalBilin (topDualPairing 𝕜 E).flip S) =
    S.topologicalClosure
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Submodule.orthogonalBilin_orthogonalBilin_topDualPairing_eq_topologicalClosure`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Annihilator.html#Submodule.orthogonalBilin_orthogonalBilin_topDualPairing_eq_topologicalClosure).

## Sources

- [Tau Ceti documentation: `Submodule.orthogonalBilin_orthogonalBilin_topDualPairing_eq_topologicalClosure`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Annihilator.html#Submodule.orthogonalBilin_orthogonalBilin_topDualPairing_eq_topologicalClosure)
- [Source of `Submodule.orthogonalBilin_orthogonalBilin_topDualPairing_eq_topologicalClosure` in TauCeti/Analysis/Normed/Module/Annihilator.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Module/Annihilator.lean#L125)
