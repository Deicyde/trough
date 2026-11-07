---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.exists_abelianLayer_globalNormSubgroup_eq_of_pow_mem
statement: formalized
proof: formalized
---

# TauCeti.ClassFieldTheory.exists\_abelianLayer\_globalNormSubgroup\_eq\_of\_pow\_mem

**The Kummer case of global existence** (Milne VII, Lemma 9.3). Let `K` be a number field
containing the `p`-th roots of unity for a prime `p`. Every open subgroup of the idele class group
`C_K` containing the `p`-th powers is the norm subgroup of a finite abelian extension of `K`.

```lean
TauCeti.ClassFieldTheory.exists_abelianLayer_globalNormSubgroup_eq_of_pow_mem {K : Type} [Field K]
  [NumberField K] {p : ℕ} [Fact (Nat.Prime p)] [HasEnoughRootsOfUnity K p]
  {N : Subgroup (NumberField.IdeleClassGroup (NumberField.RingOfIntegers K) K)} (hN : IsOpen ↑N)
  (hpow : ∀ (c : NumberField.IdeleClassGroup (NumberField.RingOfIntegers K) K), c ^ p ∈ N) :
  ∃ V, V.IsAbelianClassFieldLayer ∧ TauCeti.ClassFieldTheory.globalNormSubgroup K V = N
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The global class formation](the-global-class-formation.md)
- [The local class formation](the-local-class-formation.md)
- [The norm index theorem](the-norm-index-theorem.md)
- [TauCeti.algebraicExtensionNormedField](../../part-04/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.ClassFormation.tateIso](tauceti-classfieldtheory-classformation-tateiso.md)
- [TauCeti.relDiscr](../../part-05/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)
- [TauCeti.semilocalEquiv](../../part-05/number-fields-ramification-frobenius-and-the-lmf/tauceti-semilocalequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.exists_abelianLayer_globalNormSubgroup_eq_of_pow_mem`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/GlobalExistence/Kummer.html#TauCeti.ClassFieldTheory.exists_abelianLayer_globalNormSubgroup_eq_of_pow_mem).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.exists_abelianLayer_globalNormSubgroup_eq_of_pow_mem`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/GlobalExistence/Kummer.html#TauCeti.ClassFieldTheory.exists_abelianLayer_globalNormSubgroup_eq_of_pow_mem)
- [Source of `TauCeti.ClassFieldTheory.exists_abelianLayer_globalNormSubgroup_eq_of_pow_mem` in TauCeti/NumberTheory/ClassFieldTheory/GlobalExistence/Kummer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/GlobalExistence/Kummer.lean#L124)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassFieldTheory/STATUS.md)
