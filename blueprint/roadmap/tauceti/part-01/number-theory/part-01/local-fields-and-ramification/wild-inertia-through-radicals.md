---
declaration: theorem
origin: cited
lean: TauCeti.mem_wildInertiaSubgroup_iff_pow_eq
statement: formalized
proof: formalized
---

# Wild inertia, through radicals

An automorphism of `K^{alg}` lies in the wild inertia
subgroup exactly when it fixes every `m`-th root of every nonzero element of `K`, for `m` prime to
the residue characteristic.

```lean
TauCeti.mem_wildInertiaSubgroup_iff_pow_eq.{u_1} {K : Type u_1} [Field K] [ValuativeRel K]
  {σ : Field.absoluteGaloisGroup K} :
  σ ∈ TauCeti.wildInertiaSubgroup K ↔
    ∀ (m : ℕ),
      ¬ringChar (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer) ∣ m →
        ∀ (a : Kˣ) (x : AlgebraicClosure K),
          x ^ m = (algebraMap K (AlgebraicClosure K)) ↑a → σ x = x
```

## Depends on

- [The wild inertia subgroup](the-wild-inertia-subgroup.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mem_wildInertiaSubgroup_iff_pow_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/WildInertia.html#TauCeti.mem_wildInertiaSubgroup_iff_pow_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.mem_wildInertiaSubgroup_iff_pow_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/WildInertia.html#TauCeti.mem_wildInertiaSubgroup_iff_pow_eq)
- [Source of `TauCeti.mem_wildInertiaSubgroup_iff_pow_eq` in TauCeti/NumberTheory/LocalField/WildInertia.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LocalField/WildInertia.lean#L179)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/LocalFieldsRamification/STATUS.md)
