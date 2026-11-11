---
declaration: theorem
origin: cited
lean: TauCeti.existsUnique_eq_smul_lazardCocycle
statement: formalized
proof: formalized
---

# The symmetric 2-cocycle lemma, with uniqueness

for `n ≥ 2`, a homogeneous symmetric
additive 2-cocycle of degree `n` over any commutative ring is `r • C_n` for a unique `r`.

```lean
TauCeti.existsUnique_eq_smul_lazardCocycle.{u_1} {R : Type u_1} [CommRing R] {n : ℕ} (hn : 2 ≤ n)
  {f : MvPolynomial (Fin 2) R} (hh : f.IsHomogeneous n) (hs : f.IsSymmetric)
  (hf : f.IsAddCocycle₂) : ∃! r, f = r • TauCeti.lazardCocycle n R
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Nakayama's lemma over `ℤ`](../../part-02/other-results/part-02/nakayamas-lemma-over-z.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.existsUnique_eq_smul_lazardCocycle`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/SymmetricCocycle/Classification.html#TauCeti.existsUnique_eq_smul_lazardCocycle).

## Sources

- [Tau Ceti documentation: `TauCeti.existsUnique_eq_smul_lazardCocycle`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/SymmetricCocycle/Classification.html#TauCeti.existsUnique_eq_smul_lazardCocycle)
- [Source of `TauCeti.existsUnique_eq_smul_lazardCocycle` in TauCeti/RingTheory/FormalGroup/SymmetricCocycle/Classification.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/FormalGroup/SymmetricCocycle/Classification.lean#L425)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
