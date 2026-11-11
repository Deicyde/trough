---
declaration: theorem
origin: cited
lean: IsSelfAdjoint.exists_hilbertBasis_forall_apply_eq_smul_of_hasCompactResolvent
statement: formalized
proof: formalized
---

# Orthonormal eigenbasis of a self-adjoint operator with compact resolvent

A self-adjoint
operator `A` with compact resolvent on a complex Hilbert space has a Hilbert basis consisting of
vectors in its domain which are eigenvectors of `A` with real eigenvalues.

```lean
IsSelfAdjoint.exists_hilbertBasis_forall_apply_eq_smul_of_hasCompactResolvent.{u_1} {H : Type u_1}
  [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H] {A : H →ₗ.[ℂ] H}
  (hA : IsSelfAdjoint A) (h : A.HasCompactResolvent) :
  ∃ κ b lam, ∀ (k : κ), ∃ (hk : b k ∈ A.domain), ↑A ⟨b k, hk⟩ = ↑(lam k) • b k
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsSelfAdjoint.exists_hilbertBasis_forall_apply_eq_smul_of_hasCompactResolvent`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/LinearPMap/Eigenbasis.html#IsSelfAdjoint.exists_hilbertBasis_forall_apply_eq_smul_of_hasCompactResolvent).

## Sources

- [Tau Ceti documentation: `IsSelfAdjoint.exists_hilbertBasis_forall_apply_eq_smul_of_hasCompactResolvent`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/LinearPMap/Eigenbasis.html#IsSelfAdjoint.exists_hilbertBasis_forall_apply_eq_smul_of_hasCompactResolvent)
- [Source of `IsSelfAdjoint.exists_hilbertBasis_forall_apply_eq_smul_of_hasCompactResolvent` in TauCeti/Analysis/InnerProductSpace/LinearPMap/Eigenbasis.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/LinearPMap/Eigenbasis.lean#L110)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
