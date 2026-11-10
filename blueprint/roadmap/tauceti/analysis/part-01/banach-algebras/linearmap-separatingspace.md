---
declaration: def
origin: cited
lean: LinearMap.separatingSpace
statement: formalized
---

# LinearMap.separatingSpace

The *separating space* of a linear map `T : E →ₗ[R] F` between topological modules: the
vertical fibre over `0` of the closure of the graph of `T`. For first countable spaces it
consists of the limits of `T xₙ` along sequences `xₙ → 0`
(`LinearMap.mem_separatingSpace_iff_exists_seq`).

```lean
LinearMap.separatingSpace.{u_1, u_3, u_4} {R : Type u_1} {E : Type u_3} {F : Type u_4} [Ring R]
  [AddCommGroup E] [_root_.Module R E] [TopologicalSpace E] [IsTopologicalAddGroup E]
  [ContinuousConstSMul R E] [AddCommGroup F] [_root_.Module R F] [TopologicalSpace F]
  [IsTopologicalAddGroup F] [ContinuousConstSMul R F] (T : E →ₗ[R] F) : Submodule R F
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.separatingSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/SeparatingSpace.html#LinearMap.separatingSpace).

## Sources

- [Tau Ceti documentation: `LinearMap.separatingSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/SeparatingSpace.html#LinearMap.separatingSpace)
- [Source of `LinearMap.separatingSpace` in TauCeti/Analysis/Normed/Operator/SeparatingSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/SeparatingSpace.lean#L100)
- [Tau Ceti roadmap status: Banach algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BanachAlgebras/STATUS.md)
