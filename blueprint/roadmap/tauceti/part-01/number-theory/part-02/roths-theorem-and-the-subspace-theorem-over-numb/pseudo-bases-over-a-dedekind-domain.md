---
declaration: theorem
origin: cited
lean: Submodule.exists_pseudoBasis
statement: formalized
proof: formalized
---

# Pseudo-bases over a Dedekind domain

Let `R` be a Dedekind domain with fraction field
`K`. A finitely generated `R`-submodule `Λ` of a `K`-vector space `V` spanning `V` is
`⊕ i, J i • b i` for a `K`-basis `b` of `V` and nonzero ideals `J i` of `R`: a vector lies in `Λ`
exactly when its `i`-th coordinate in `b` lies in `J i` for every `i`. The basis may be indexed by
any finite type of cardinality `finrank K V`.

```lean
Submodule.exists_pseudoBasis.{u_1, u_2, u_3, u_4} {R : Type u_1} {K : Type u_2} {V : Type u_3}
  [CommRing R] [IsDedekindDomain R] [Field K] [Algebra R K] [IsFractionRing R K] [AddCommGroup V]
  [_root_.Module K V] [_root_.Module R V] [IsScalarTower R K V] {ι : Type u_4} [Finite ι]
  (Λ : Submodule R V) (hΛ : Λ.FG) (hspan : Submodule.span K ↑Λ = ⊤)
  (hι : Nat.card ι = Module.finrank K V) :
  ∃ b J,
    (∀ (i : ι), J i ≠ ⊥) ∧
      ∀ (x : V), x ∈ Λ ↔ ∀ (i : ι), (b.repr x) i ∈ IsLocalization.coeSubmodule K (J i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Submodule.exists_pseudoBasis`](https://taucetiproject.org/docs/TauCeti/RingTheory/DedekindDomain/PseudoBasis.html#Submodule.exists_pseudoBasis).

## Sources

- [Tau Ceti documentation: `Submodule.exists_pseudoBasis`](https://taucetiproject.org/docs/TauCeti/RingTheory/DedekindDomain/PseudoBasis.html#Submodule.exists_pseudoBasis)
- [Source of `Submodule.exists_pseudoBasis` in TauCeti/RingTheory/DedekindDomain/PseudoBasis.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/DedekindDomain/PseudoBasis.lean#L154)
- [Tau Ceti roadmap status: Roth's theorem and the Subspace Theorem over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SubspaceTheorem/STATUS.md)
