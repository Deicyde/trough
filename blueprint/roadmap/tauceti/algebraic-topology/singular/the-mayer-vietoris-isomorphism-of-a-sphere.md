---
declaration: theorem
origin: cited
lean: TauCeti.isIso_reducedMayerVietorisδ_sphere
statement: formalized
proof: formalized
---

# The Mayer–Vietoris isomorphism of a sphere

The reduced Mayer–Vietoris connecting
morphism `Hₖ₊₁(S) ⟶ H_redₖ(S ∖ {p, -p})` of the cover of the unit sphere `S` by the complements of
`p` and `-p` is an isomorphism in every degree, since both complements are contractible.

```lean
TauCeti.isIso_reducedMayerVietorisδ_sphere.{w, v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Limits.HasCoproducts C] [CategoryTheory.Abelian C] (R : C) {E : Type w}
  [NormedAddCommGroup E] [NormedSpace ℝ E] (p : ↑(Metric.sphere 0 1)) (k : ℕ) :
  CategoryTheory.IsIso (TopCat.reducedMayerVietorisδ R ⋯ ⋯ ⋯ k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The reduced Mayer–Vietoris connecting morphism is an isomorphism when both open sets are acyclic in the adjacent degrees](the-reduced-mayer-vietoris-connecting-morphism-i.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isIso_reducedMayerVietorisδ_sphere`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Sphere.html#TauCeti.isIso_reducedMayerVietoris%CE%B4_sphere).

## Sources

- [Tau Ceti documentation: `TauCeti.isIso_reducedMayerVietorisδ_sphere`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Sphere.html#TauCeti.isIso_reducedMayerVietoris%CE%B4_sphere)
- [Source of `TauCeti.isIso_reducedMayerVietorisδ_sphere` in TauCeti/AlgebraicTopology/Singular/Sphere.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Singular/Sphere.lean#L150)
