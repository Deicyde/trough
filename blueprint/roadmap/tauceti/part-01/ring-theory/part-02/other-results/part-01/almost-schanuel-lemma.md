---
declaration: theorem
origin: cited
lean: TauCeti.Almost.BasicSetup.AlmostFP.exists_fg_smul_ker_le
statement: formalized
proof: formalized
---

# Almost Schanuel lemma

Let `N` be almost finitely presented and let `φ : Vⁿ → N` have
cokernel killed by a finitely generated ideal `J`. Then for every finitely generated `K ≤ m`, some
finitely generated submodule of `ker φ` contains `(J * K ^ 2) • ker φ`.

For the classical setup and `J = K = V` this says that a surjection from a finite free module onto
a finitely presented module has finitely generated kernel.

```lean
TauCeti.Almost.BasicSetup.AlmostFP.exists_fg_smul_ker_le.{u, u_2} {V : Type u} [CommRing V]
  {S : TauCeti.Almost.BasicSetup V} {N : Type u_2} [AddCommGroup N] [_root_.Module V N]
  (hN : S.AlmostFP N) {J K : Ideal V} (hJ : J.FG) (hK : K ≤ S.ideal) (hKfg : K.FG) {n : ℕ}
  (φ : (Fin n → V) →ₗ[V] N) (hφ : J • ⊤ ≤ φ.range) : ∃ L ≤ φ.ker, L.FG ∧ (J * K ^ 2) • φ.ker ≤ L
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Almost.BasicSetup.AlmostFP.exists_fg_smul_ker_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/Almost/Finiteness/Presentation.html#TauCeti.Almost.BasicSetup.AlmostFP.exists_fg_smul_ker_le).

## Sources

- [Tau Ceti documentation: `TauCeti.Almost.BasicSetup.AlmostFP.exists_fg_smul_ker_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/Almost/Finiteness/Presentation.html#TauCeti.Almost.BasicSetup.AlmostFP.exists_fg_smul_ker_le)
- [Source of `TauCeti.Almost.BasicSetup.AlmostFP.exists_fg_smul_ker_le` in TauCeti/RingTheory/Almost/Finiteness/Presentation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Almost/Finiteness/Presentation.lean#L100)
