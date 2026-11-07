---
declaration: theorem
origin: cited
lean: TauCeti.GraphTwistedIndex.steinberg_eq_graphAut_comp_frobenius
statement: formalized
proof: formalized
---

# The Steinberg endomorphism is the graph automorphism composed with the Frobenius

,
uniformly in the thirteen ordinary and graph-twisted families. On the nine untwisted ones the
graph factor is trivial and the composite is the Frobenius itself, which is
`TauCeti.GraphTwistedIndex.steinberg_eq_frobenius`.

```lean
TauCeti.GraphTwistedIndex.steinberg_eq_graphAut_comp_frobenius (d : TauCeti.GraphTwistedIndex) :
  d.steinberg = (MulEquiv.toMonoidHom d.graphAut).comp d.frobenius
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GraphTwistedIndex.steinberg_eq_graphAut_comp_frobenius`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/CFSG/Assembly/GraphTwisted.html#TauCeti.GraphTwistedIndex.steinberg_eq_graphAut_comp_frobenius).

## Sources

- [Tau Ceti documentation: `TauCeti.GraphTwistedIndex.steinberg_eq_graphAut_comp_frobenius`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/CFSG/Assembly/GraphTwisted.html#TauCeti.GraphTwistedIndex.steinberg_eq_graphAut_comp_frobenius)
- [Source of `TauCeti.GraphTwistedIndex.steinberg_eq_graphAut_comp_frobenius` in TauCeti/GroupTheory/SpecificGroups/CFSG/Assembly/GraphTwisted.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/SpecificGroups/CFSG/Assembly/GraphTwisted.lean#L1070)
- [Tau Ceti roadmap status: Stating the classification of finite simple groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CFSGStatement/STATUS.md)
