---
declaration: theorem
origin: cited
lean: TauCeti.holomorphicStructureSheaf.restrictAlgHom_bijective_of_isDiscrete
statement: formalized
proof: formalized
---

# Hartogs' theorem for sections of the holomorphic structure sheaf

When
`2 ≤ Module.finrank ℂ E` and `V ≤ U` are open subsets of `X` such that `(U : Set X) \ (V : Set X)`
is discrete, restricting holomorphic sections from `U` to `V` is bijective.

```lean
TauCeti.holomorphicStructureSheaf.restrictAlgHom_bijective_of_isDiscrete.{u_1, u_2} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [FiniteDimensional ℂ E] {H : Type u_2}
  [TopologicalSpace H] (I : ModelWithCorners ℂ E H) [I.Boundaryless] {X : Type} [TopologicalSpace X]
  [ChartedSpace H X] [IsManifold I 1 X] (hE : 2 ≤ Module.finrank ℂ E)
  {U V : TopologicalSpace.Opens X} (h : V ≤ U) (hUV : IsDiscrete (↑U \ ↑V)) :
  Function.Bijective ⇑(TauCeti.holomorphicStructureSheaf.restrictAlgHom I h)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hartogs' extension theorem across a point on a complex manifold](../../../part-02/manifold/part-02/hartogs-extension-theorem-across-a-point-on-a-co.md)
- [Osgood's lemma](../../complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.holomorphicStructureSheaf.restrictAlgHom_bijective_of_isDiscrete`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/StructureSheaf/Hartogs.html#TauCeti.holomorphicStructureSheaf.restrictAlgHom_bijective_of_isDiscrete).

## Sources

- [Tau Ceti documentation: `TauCeti.holomorphicStructureSheaf.restrictAlgHom_bijective_of_isDiscrete`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/StructureSheaf/Hartogs.html#TauCeti.holomorphicStructureSheaf.restrictAlgHom_bijective_of_isDiscrete)
- [Source of `TauCeti.holomorphicStructureSheaf.restrictAlgHom_bijective_of_isDiscrete` in TauCeti/Geometry/Manifold/Complex/StructureSheaf/Hartogs.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Complex/StructureSheaf/Hartogs.lean#L60)
