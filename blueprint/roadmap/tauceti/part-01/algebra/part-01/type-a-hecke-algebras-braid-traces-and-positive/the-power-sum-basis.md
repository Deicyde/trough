---
declaration: def
origin: cited
lean: TauCeti.psumPartBasis
statement: formalized
---

# The power-sum basis

over a `ℚ`-algebra and in an alphabet of at least `n` letters, the
power-sum products `p_μ` of the partitions `μ` of `n` form a basis of the symmetric polynomials of
degree `n`.

```lean
TauCeti.psumPartBasis.{u_1, u_2} (σ : Type u_1) [Fintype σ] (R : Type u_2) [CommRing R]
  [Algebra ℚ R] {n : ℕ} (hn : n ≤ Fintype.card σ) :
  Module.Basis n.Partition R ↥(TauCeti.symmetricHomogeneousSubmodule σ R n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Newton's identities for a multiset](../../../ring-theory/part-01/multivariate-polynomials/newtons-identities-for-a-multiset.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.psumPartBasis`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/PowerSum/Basis.html#TauCeti.psumPartBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.psumPartBasis`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/PowerSum/Basis.html#TauCeti.psumPartBasis)
- [Source of `TauCeti.psumPartBasis` in TauCeti/RingTheory/MvPolynomial/Symmetric/PowerSum/Basis.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPolynomial/Symmetric/PowerSum/Basis.lean#L191)
- [Tau Ceti roadmap status: Type-A Hecke algebras, braid traces, and positive quotients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TypeAHeckeAlgebras/STATUS.md)
