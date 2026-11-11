---
declaration: theorem
origin: cited
lean: Equiv.Perm.rsk_inv
statement: formalized
proof: formalized
---

# Schützenberger's symmetry theorem

The Robinson--Schensted correspondence of the
inverse permutation exchanges the insertion and recording tableaux.

```lean
Equiv.Perm.rsk_inv {n : ℕ} (σ : Equiv.Perm (Fin n)) :
  (TauCeti.rsk n) σ⁻¹ =
    ⟨((TauCeti.rsk n) σ).fst, (((TauCeti.rsk n) σ).snd.2, ((TauCeti.rsk n) σ).snd.1)⟩
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Equiv.Perm.rsk_inv`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Young/Schensted/Symmetry.html#Equiv.Perm.rsk_inv).

## Sources

- [Tau Ceti documentation: `Equiv.Perm.rsk_inv`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Young/Schensted/Symmetry.html#Equiv.Perm.rsk_inv)
- [Source of `Equiv.Perm.rsk_inv` in TauCeti/Combinatorics/Young/Schensted/Symmetry.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Young/Schensted/Symmetry.lean#L364)
