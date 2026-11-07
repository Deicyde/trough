---
declaration: theorem
origin: cited
lean: TauCeti.existsUnique_eq_smul_lazardCocycle
statement: formalized
proof: formalized
---

# TauCeti.existsUnique\_eq\_smul\_lazardCocycle

**The symmetric 2-cocycle lemma**, with uniqueness: for `n ≥ 2`, a homogeneous symmetric
additive 2-cocycle of degree `n` over any commutative ring is `r • C_n` for a unique `r`.

```lean
TauCeti.existsUnique_eq_smul_lazardCocycle.{u_1} {R : Type u_1} [CommRing R] {n : ℕ} (hn : 2 ≤ n)
  {f : MvPolynomial (Fin 2) R} (hh : f.IsHomogeneous n) (hs : f.IsSymmetric)
  (hf : f.IsAddCocycle₂) : ∃! r, f = r • TauCeti.lazardCocycle n R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.existsUnique_eq_smul_lazardCocycle`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/SymmetricCocycle/Classification.html#TauCeti.existsUnique_eq_smul_lazardCocycle).

## Sources

- [Tau Ceti documentation: `TauCeti.existsUnique_eq_smul_lazardCocycle`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/SymmetricCocycle/Classification.html#TauCeti.existsUnique_eq_smul_lazardCocycle)
- [Source of `TauCeti.existsUnique_eq_smul_lazardCocycle` in TauCeti/RingTheory/FormalGroup/SymmetricCocycle/Classification.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/FormalGroup/SymmetricCocycle/Classification.lean#L409)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
