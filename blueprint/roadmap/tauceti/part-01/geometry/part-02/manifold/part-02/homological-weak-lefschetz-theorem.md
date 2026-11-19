---
declaration: theorem
origin: cited
lean: TauCeti.isZero_singularHomology_notMem_affineOpen, TauCeti.isZero_singularHomology_complexProjectiveZeroLocus_notMem_affineOpen
statement: formalized
proof: formalized
---

# Homological weak Lefschetz theorem

If `(X ∩ H_i) ↪ W` induces singular homology
isomorphisms in degree `k` and (when `k > 0`) degree `k - 1` on a neighbourhood `W` of `X ∩ H_i` in
`X`, then the relative singular homology `H_k(X, X ∩ H_i; R)` vanishes for `k < dim_ℂ Z`, proved
directly from high-index Morse cell attachments on `X \ H_i`.

```lean
TauCeti.isZero_singularHomology_notMem_affineOpen.{v, w, u_1} {E : Type u_1} [NormedAddCommGroup E]
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
    ∀ (m : ℕ),
      m = k ∨ m + 1 = k →
        CategoryTheory.IsIso
          (SSet.homologyMap (TopCat.toSSet.map (TopCat.ofHom (ContinuousMap.inclusion hAW))) R m))
  (hW_nhds : W ∈ nhdsSet {x | ↑x ∉ Projectivization.affineOpen i}) (hk : k < Module.finrank ℂ E) :
  CategoryTheory.Limits.IsZero
    ((TopPair.ofSubset {x | ↑x ∉ Projectivization.affineOpen i}).singularHomology R k)
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

Formalized in Tau Ceti as [`TauCeti.isZero_singularHomology_notMem_affineOpen`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Projectivization/Lefschetz.html#TauCeti.isZero_singularHomology_notMem_affineOpen).

## Other forms

**Homological weak Lefschetz theorem for a projective zero locus.** Formalized in Tau Ceti as [`TauCeti.isZero_singularHomology_complexProjectiveZeroLocus_notMem_affineOpen`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Projectivization/Lefschetz.html#TauCeti.isZero_singularHomology_complexProjectiveZeroLocus_notMem_affineOpen).

```lean
TauCeti.isZero_singularHomology_complexProjectiveZeroLocus_notMem_affineOpen.{v, w, u_1} {n : ℕ}
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
    ∀ (m : ℕ),
      m = k ∨ m + 1 = k →
        CategoryTheory.IsIso
          (SSet.homologyMap (TopCat.toSSet.map (TopCat.ofHom (ContinuousMap.inclusion hAW))) R m))
  (hW_nhds : W ∈ nhdsSet {x | ↑x ∉ Projectivization.affineOpen i}) (hk : k < n - Fintype.card ι) :
  CategoryTheory.Limits.IsZero
    ((TopPair.ofSubset {x | ↑x ∉ Projectivization.affineOpen i}).singularHomology R k)
```

## Sources

- [Tau Ceti documentation: `TauCeti.isZero_singularHomology_notMem_affineOpen`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Projectivization/Lefschetz.html#TauCeti.isZero_singularHomology_notMem_affineOpen)
- [Source of `TauCeti.isZero_singularHomology_notMem_affineOpen` in TauCeti/Geometry/Manifold/Projectivization/Lefschetz.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Projectivization/Lefschetz.lean#L385)
