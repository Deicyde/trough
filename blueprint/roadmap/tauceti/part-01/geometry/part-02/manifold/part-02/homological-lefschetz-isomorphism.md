---
declaration: theorem
origin: cited
lean: TauCeti.isIso_homologyMap_notMem_affineOpen, TauCeti.isIso_homologyMap_complexProjectiveZeroLocus_notMem_affineOpen
statement: formalized
proof: formalized
---

# Homological Lefschetz isomorphism

If `(X ∩ H_i) ↪ W` induces a singular homology
isomorphism in degree `k` on a neighbourhood `W` of `X ∩ H_i` in `X`, then `(X ∩ H_i) ↪ X` induces
an isomorphism `H_k(X ∩ H_i; R) ≅ H_k(X; R)` for `k + 1 < dim_ℂ Z`.

```lean
TauCeti.isIso_homologyMap_notMem_affineOpen.{v, w, u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] [FiniteDimensional ℂ E] {n : ℕ} {A_cat : Type v}
  [CategoryTheory.Category.{w, v} A_cat] [CategoryTheory.Abelian A_cat]
  [CategoryTheory.Limits.HasCoproducts A_cat] {X : Set (Projectivization ℂ (Fin (n + 1) → ℂ))}
  (hX : IsClosed X) (i : Fin (n + 1)) {Z : Set (Fin n → ℂ)}
  (hZ : ↑(Projectivization.affineChart i) '' (X ∩ Projectivization.affineOpen i) = Z)
  [ChartedSpace E ↑Z] [IsManifold (modelWithCornersSelf ℂ E) ↑⊤ ↑Z]
  (hZval :
    ContMDiff (modelWithCornersSelf ℂ E) (modelWithCornersSelf ℂ (Fin n → ℂ)) (↑⊤) Subtype.val)
  (hinj : ∀ (z : ↑Z), Function.Injective ⇑(mfderiv% Subtype.val z)) (R : A_cat) {k : ℕ} {W : Set ↑X}
  {hAW : {x | ↑x ∉ Projectivization.affineOpen i} ⊆ W}
  (hW :
    CategoryTheory.IsIso
      (SSet.homologyMap (TopCat.toSSet.map (TopCat.ofHom (ContinuousMap.inclusion hAW))) R k))
  (hW_nhds : W ∈ nhdsSet {x | ↑x ∉ Projectivization.affineOpen i})
  (hk : k + 1 < Module.finrank ℂ E) :
  CategoryTheory.IsIso
    (SSet.homologyMap
      (TopCat.toSSet.map
        (TopCat.ofHom (ContinuousMap.subtypeVal {x | ↑x ∉ Projectivization.affineOpen i})))
      R k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A maximal integral curve confined to a compact set is defined for all time](../../../part-01/geodesics-the-exponential-map-and-the-hopf-rinow/a-maximal-integral-curve-confined-to-a-compact-s.md)
- [The index bound for strongly `q`-pseudoconvex functions on a complex manifold](../../../part-01/complex-morse-theory-affine-topology-and-weak-le/the-index-bound-for-strongly-q-pseudoconvex-func.md)
- [The inverse function theorem for a converging family](../../../../analysis/part-03/calculus/part-01/the-inverse-function-theorem-for-a-converging-fa.md)
- [The Mayer–Vietoris isomorphism of a sphere](../../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [Milnor's cell attachment theorem](../part-03/milnors-cell-attachment-theorem.md)
- [ModelWithCorners.restrictScalars](../../../part-01/complex-manifolds-transport-quotients-bundles-an/modelwithcorners-restrictscalars.md)
- [The relative small-chain theorem](../../../../algebraic-topology/singular/the-relative-small-chain-theorem.md)
- [Sard's lemma in equal dimensions](../../../../analysis/part-03/calculus/part-02/sards-lemma-in-equal-dimensions.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isIso_homologyMap_notMem_affineOpen`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Projectivization/Lefschetz.html#TauCeti.isIso_homologyMap_notMem_affineOpen).

## Other forms

**Homological Lefschetz isomorphism for a projective zero locus.** Formalized in Tau Ceti as [`TauCeti.isIso_homologyMap_complexProjectiveZeroLocus_notMem_affineOpen`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Projectivization/Lefschetz.html#TauCeti.isIso_homologyMap_complexProjectiveZeroLocus_notMem_affineOpen).

```lean
TauCeti.isIso_homologyMap_complexProjectiveZeroLocus_notMem_affineOpen.{v, w, u_1} {n : ℕ}
  {ι : Type u_1} [Fintype ι] {p : ι → MvPolynomial (Fin (n + 1)) ℂ} {d : ι → ℕ} {A_cat : Type v}
  [CategoryTheory.Category.{w, v} A_cat] [CategoryTheory.Abelian A_cat]
  [CategoryTheory.Limits.HasCoproducts A_cat] (hp : ∀ (m : ι), (p m).IsHomogeneous (d m))
  (i : Fin (n + 1))
  (hrank :
    ∀ z ∈ TauCeti.affineZeroLocus fun m => (TauCeti.dehomogenize i) (p m),
      Function.Surjective
        (TauCeti.jacobiMatrixAt (fun m => (TauCeti.dehomogenize i) (p m)) z).mulVec)
  (R : A_cat) {k : ℕ} {W : Set ↑(TauCeti.complexProjectiveZeroLocus p)}
  {hAW : {x | ↑x ∉ Projectivization.affineOpen i} ⊆ W}
  (hW :
    CategoryTheory.IsIso
      (SSet.homologyMap (TopCat.toSSet.map (TopCat.ofHom (ContinuousMap.inclusion hAW))) R k))
  (hW_nhds : W ∈ nhdsSet {x | ↑x ∉ Projectivization.affineOpen i})
  (hk : k + 1 < n - Fintype.card ι) :
  CategoryTheory.IsIso
    (SSet.homologyMap
      (TopCat.toSSet.map
        (TopCat.ofHom (ContinuousMap.subtypeVal {x | ↑x ∉ Projectivization.affineOpen i})))
      R k)
```

## Sources

- [Tau Ceti documentation: `TauCeti.isIso_homologyMap_notMem_affineOpen`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Projectivization/Lefschetz.html#TauCeti.isIso_homologyMap_notMem_affineOpen)
- [Source of `TauCeti.isIso_homologyMap_notMem_affineOpen` in TauCeti/Geometry/Manifold/Projectivization/Lefschetz.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Projectivization/Lefschetz.lean#L361)
