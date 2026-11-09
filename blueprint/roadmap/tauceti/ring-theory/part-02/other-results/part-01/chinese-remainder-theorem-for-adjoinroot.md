---
declaration: def
origin: cited
lean: AdjoinRoot.equivPiFactors
statement: formalized
---

# Chinese Remainder Theorem for `AdjoinRoot`

for `f` nonzero and squarefree,
`K[X] ⧸ (f)` is the product of the fields `K[X] ⧸ (p)` over the monic irreducible factors `p`
of `f`.

```lean
AdjoinRoot.equivPiFactors.{u_1} {K : Type u_1} [Field K] {f : Polynomial K} (hf : f ≠ 0)
  (hsq : Squarefree f) : AdjoinRoot f ≃ₐ[K] (p : f.Factors) → AdjoinRoot ↑p
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AdjoinRoot.equivPiFactors`](https://taucetiproject.org/docs/TauCeti/RingTheory/AdjoinRoot/Factors.html#AdjoinRoot.equivPiFactors).

## Sources

- [Tau Ceti documentation: `AdjoinRoot.equivPiFactors`](https://taucetiproject.org/docs/TauCeti/RingTheory/AdjoinRoot/Factors.html#AdjoinRoot.equivPiFactors)
- [Source of `AdjoinRoot.equivPiFactors` in TauCeti/RingTheory/AdjoinRoot/Factors.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/AdjoinRoot/Factors.lean#L107)
