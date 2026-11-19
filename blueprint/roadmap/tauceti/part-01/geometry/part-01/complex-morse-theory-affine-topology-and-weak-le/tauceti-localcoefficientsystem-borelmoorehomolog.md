---
declaration: abbrev
origin: cited
lean: TauCeti.LocalCoefficientSystem.borelMooreHomology
statement: formalized
---

# TauCeti.LocalCoefficientSystem.borelMooreHomology

Borel–Moore homology of `X` with coefficients in the local coefficient system `L`: the
homology of the complex of locally finite singular chains.

```lean
TauCeti.LocalCoefficientSystem.borelMooreHomology.{u, v, w} {R : Type u} [Ring R] {X : TopCat}
  (L : TauCeti.LocalCoefficientSystem R X) (k : ℕ) : ModuleCat R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LocalCoefficientSystem.borelMooreHomology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Twisted/LocallyFinite/Basic.html#TauCeti.LocalCoefficientSystem.borelMooreHomology).

## Sources

- [Tau Ceti documentation: `TauCeti.LocalCoefficientSystem.borelMooreHomology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Twisted/LocallyFinite/Basic.html#TauCeti.LocalCoefficientSystem.borelMooreHomology)
- [Source of `TauCeti.LocalCoefficientSystem.borelMooreHomology` in TauCeti/AlgebraicTopology/Singular/Twisted/LocallyFinite/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Singular/Twisted/LocallyFinite/Basic.lean#L691)
- [Tau Ceti roadmap status: Complex Morse theory, affine topology and weak Lefschetz](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AffineMorseLefschetz/STATUS.md)
