---
declaration: theorem
origin: cited
lean: TauCeti.harishChandraLinearIso_symm_mem_pbwFiltration
statement: formalized
proof: formalized
---

# The inverse linear Harish-Chandra isomorphism preserves degrees

a Weyl invariant has
degree at most `n` exactly when the corresponding central element has PBW degree at most `n`.

```lean
TauCeti.harishChandraLinearIso_symm_mem_pbwFiltration.{v} {K : Type} {L : Type v} [Field K]
  [CharZero K] [IsAlgClosed K] [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L]
  [FiniteDimensional K L] {H : LieSubalgebra K L} [H.IsCartanSubalgebra]
  [LieModule.IsTriangularizable K (↥H) L] (b : (LieAlgebra.IsKilling.rootSystem H).Base) {n : ℕ}
  (q : ↥(TauCeti.linearInvariants H)) :
  ↑((TauCeti.harishChandraLinearIso b).symm q) ∈
      TauCeti.UniversalEnvelopingAlgebra.pbwFiltration K L n ↔
    ↑q ∈ TauCeti.Algebra.wordFiltration (SymmetricAlgebra.ι K ↥H) n
```

## Depends on

- [The linear Harish-Chandra isomorphism `Z(U(L)) ≃ₐ[K] S(H)^W`](the-linear-harish-chandra-isomorphism-z-u-l-a-k.md)

## Proof depends on

- [The Cartan projection preserves a strict PBW degree bound](the-cartan-projection-preserves-a-strict-pbw-deg.md)
- [The Cartan projection restricts to the identity on `U(H)`](the-cartan-projection-restricts-to-the-identity.md)
- [Chevalley's restriction theorem, image form](chevalleys-restriction-theorem-image-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.harishChandraLinearIso_symm_mem_pbwFiltration`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.html#TauCeti.harishChandraLinearIso_symm_mem_pbwFiltration).

## Sources

- [Tau Ceti documentation: `TauCeti.harishChandraLinearIso_symm_mem_pbwFiltration`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.html#TauCeti.harishChandraLinearIso_symm_mem_pbwFiltration)
- [Source of `TauCeti.harishChandraLinearIso_symm_mem_pbwFiltration` in TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.lean#L135)
