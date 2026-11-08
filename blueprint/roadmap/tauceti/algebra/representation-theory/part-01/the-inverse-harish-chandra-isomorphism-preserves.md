---
declaration: theorem
origin: cited
lean: TauCeti.harishChandraIso_symm_mem_pbwFiltration
statement: formalized
proof: formalized
---

# The inverse Harish-Chandra isomorphism preserves degrees

a dot-invariant has degree at
most `n` exactly when the corresponding central element has PBW degree at most `n`.

```lean
TauCeti.harishChandraIso_symm_mem_pbwFiltration.{v} {K : Type} {L : Type v} [Field K] [CharZero K]
  [IsAlgClosed K] [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L] [FiniteDimensional K L]
  {H : LieSubalgebra K L} [H.IsCartanSubalgebra] [LieModule.IsTriangularizable K (↥H) L]
  (b : (LieAlgebra.IsKilling.rootSystem H).Base) {n : ℕ} (p : ↥(TauCeti.dotInvariants b)) :
  ↑((TauCeti.harishChandraIso b).symm p) ∈ TauCeti.UniversalEnvelopingAlgebra.pbwFiltration K L n ↔
    ↑p ∈ TauCeti.Algebra.wordFiltration (SymmetricAlgebra.ι K ↥H) n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cartan projection preserves a strict PBW degree bound](the-cartan-projection-preserves-a-strict-pbw-deg.md)
- [The Cartan projection restricts to the identity on `U(H)`](the-cartan-projection-restricts-to-the-identity.md)
- [Chevalley's restriction theorem, image form](chevalleys-restriction-theorem-image-form.md)
- [Harish-Chandra surjectivity with a degree bound](harish-chandra-surjectivity-with-a-degree-bound.md)
- [The linear-independence half of the Poincaré--Birkhoff--Witt theorem](../../lie/the-linear-independence-half-of-the-poincare-bir.md)
- [The Poincaré--Birkhoff--Witt theorem](../../lie/the-poincare-birkhoff-witt-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.harishChandraIso_symm_mem_pbwFiltration`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.html#TauCeti.harishChandraIso_symm_mem_pbwFiltration).

## Sources

- [Tau Ceti documentation: `TauCeti.harishChandraIso_symm_mem_pbwFiltration`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.html#TauCeti.harishChandraIso_symm_mem_pbwFiltration)
- [Source of `TauCeti.harishChandraIso_symm_mem_pbwFiltration` in TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.lean#L145)
