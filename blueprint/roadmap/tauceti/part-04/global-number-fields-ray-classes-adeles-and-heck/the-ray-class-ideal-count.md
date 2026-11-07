---
declaration: theorem
origin: cited
lean: TauCeti.GlobalNumberFields.rayClassIdealCount
statement: formalized
proof: formalized
---

# The ray class ideal count

For every modulus `𝔪` there is a power saving `δ > 0` such
that, in each ray class `c` of `𝔪`, the number of nonzero integral ideals prime to `𝔪` of norm at
most `x` is `rayClassIdealMainTerm 𝔪 * x + O(x ^ (1 - δ))`.  One can take `δ = 1 / [K : ℚ]`;
for that explicit exponent, use `isBigO_rayClassIdealCountingFunction_sub` instead.

```lean
TauCeti.GlobalNumberFields.rayClassIdealCount.{u_1} {K : Type u_1} [Field K] [NumberField K]
  (𝔪 : TauCeti.GlobalNumberFields.Modulus K) :
  ∃ δ,
    0 < δ ∧
      ∀ (c : TauCeti.GlobalNumberFields.RayClassGroup 𝔪),
        (fun x =>
            ↑(TauCeti.GlobalNumberFields.rayClassIdealCountingFunction 𝔪 c x) -
              TauCeti.GlobalNumberFields.rayClassIdealMainTerm 𝔪 * x) =O[Filter.atTop]
          fun x => x ^ (1 - δ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GlobalNumberFields.rayClassIdealCount`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/RayClass/Count/Asymptotic.html#TauCeti.GlobalNumberFields.rayClassIdealCount).

## Sources

- [Tau Ceti documentation: `TauCeti.GlobalNumberFields.rayClassIdealCount`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/RayClass/Count/Asymptotic.html#TauCeti.GlobalNumberFields.rayClassIdealCount)
- [Source of `TauCeti.GlobalNumberFields.rayClassIdealCount` in TauCeti/NumberTheory/NumberField/Global/RayClass/Count/Asymptotic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/Global/RayClass/Count/Asymptotic.lean#L108)
- [Tau Ceti roadmap status: Global number fields, ray classes, adeles, and Hecke characters](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/GlobalNumberFields/STATUS.md)
