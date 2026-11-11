---
declaration: theorem
origin: cited
lean: TauCeti.cartanMatrix_det_eq_one_or_neg_one
statement: formalized
proof: formalized
---

# Cartan-matrix unimodularity

If every finitely generated module admits a finite resolution
by finitely generated projectives, the Cartan determinant is `1` or `-1`. No positivity of its
sign is asserted.

```lean
TauCeti.cartanMatrix_det_eq_one_or_neg_one.{u, v} {R : Type u} [Ring R] [IsArtinianRing R]
  {I : Type v} [Fintype I] [DecidableEq I]
  (P : I → (TauCeti.finiteProjectiveModules R).FullSubcategory) (S : I → FGModuleCat R)
  [∀ (i : I), IsSimpleModule R ↑(S i)]
  (hind : ∀ (i : I), TauCeti.IsIndecomposableModule R ↑(P i).obj)
  (hPnoniso : Pairwise fun i j => IsEmpty (↑(P i).obj ≃ₗ[R] ↑(P j).obj))
  (hPexhaustive : TauCeti.IsExhaustiveIndecomposableProjectiveFamily P)
  (hSnoniso : Pairwise fun i j => IsEmpty (↑(S i) ≃ₗ[R] ↑(S j)))
  (hSexhaustive : TauCeti.IsExhaustiveSimpleFamily S)
  (h :
    ModuleCat.isFG R ≤
      (TauCeti.ExactStructure.abelian (ModuleCat R)).admitsFiniteResolution
        (TauCeti.finiteProjectiveModules R)) :
  (TauCeti.cartanMatrix P S hind hPnoniso hPexhaustive hSnoniso hSexhaustive).det = 1 ∨
    (TauCeti.cartanMatrix P S hind hPnoniso hPexhaustive hSnoniso hSexhaustive).det = -1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Krull-Schmidt theorem](../../../ring-theory/part-01/krull-schmidt/the-krull-schmidt-theorem.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)
- [The resolution theorem for modules](../category/the-resolution-theorem-for-modules.md)
- [The resolution theorem for modules admitting finite resolutions by finitely generated projectives](../category/the-resolution-theorem-for-modules-admitting-fin.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.cartanMatrix_det_eq_one_or_neg_one`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/GrothendieckGroup/UnimodularCartanMatrix.html#TauCeti.cartanMatrix_det_eq_one_or_neg_one).

## Sources

- [Tau Ceti documentation: `TauCeti.cartanMatrix_det_eq_one_or_neg_one`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/GrothendieckGroup/UnimodularCartanMatrix.html#TauCeti.cartanMatrix_det_eq_one_or_neg_one)
- [Source of `TauCeti.cartanMatrix_det_eq_one_or_neg_one` in TauCeti/RepresentationTheory/GrothendieckGroup/UnimodularCartanMatrix.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/GrothendieckGroup/UnimodularCartanMatrix.lean#L149)
- [Tau Ceti roadmap status: Grothendieck groups, Cartan maps, and Euler forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GrothendieckEulerForms/STATUS.md)
