---
declaration: theorem
origin: cited
lean: TauCeti.subsingleton_relHomotopyGroup_notMem_affineOpen, TauCeti.subsingleton_relHomotopyGroup_complexProjectiveZeroLocus_notMem_affineOpen
statement: formalized
proof: formalized
---

# Relative homotopy Lefschetz theorem (Milnor, Theorem 7.4)

Let `X ⊆ ℂℙⁿ` be closed, with
affine part `X \ H_i ≅ Z` a holomorphically immersed complex manifold of complex dimension `d`, and
let `W` be a neighbourhood of `X ∩ H_i` in `X` whose inclusion `(X ∩ H_i) ↪ W` is a weak homotopy
equivalence. Then `π_{k+1}(X, X ∩ H_i, a₀) = 0` whenever `k + 1 < d`. No smoothness of `X` is
assumed along `X ∩ H_i`.

```lean
TauCeti.subsingleton_relHomotopyGroup_notMem_affineOpen.{v, u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [FiniteDimensional ℂ E] {n : ℕ} {J : Type v} [Finite J]
  {X : Set (Projectivization ℂ (Fin (n + 1) → ℂ))} (hX : IsClosed X) (i : Fin (n + 1))
  {Z : Set (Fin n → ℂ)}
  (hZ : ↑(Projectivization.affineChart i) '' (X ∩ Projectivization.affineOpen i) = Z)
  [ChartedSpace E ↑Z] [IsManifold (modelWithCornersSelf ℂ E) ↑⊤ ↑Z]
  (hZval :
    ContMDiff (modelWithCornersSelf ℂ E) (modelWithCornersSelf ℂ (Fin n → ℂ)) (↑⊤) Subtype.val)
  (hinj : ∀ (z : ↑Z), Function.Injective ⇑(mfderiv% Subtype.val z)) {W : Set ↑X}
  {hAW : {x | ↑x ∉ Projectivization.affineOpen i} ⊆ W}
  (hW : (ContinuousMap.inclusion hAW).IsWeakHomotopyEquivalence)
  (hW_nhds : W ∈ nhdsSet {x | ↑x ∉ Projectivization.affineOpen i})
  (hJ : Nat.card J + 1 < Module.finrank ℂ E) (a₀ : ↑{x | ↑x ∉ Projectivization.affineOpen i}) :
  Subsingleton
    (TauCeti.RelHomotopyGroup J
      { pair := TopPair.ofSubset {x | ↑x ∉ Projectivization.affineOpen i}, basepoint := a₀ })
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A maximal integral curve confined to a compact set is defined for all time](../../../part-01/geodesics-the-exponential-map-and-the-hopf-rinow/a-maximal-integral-curve-confined-to-a-compact-s.md)
- [The index bound for strongly `q`-pseudoconvex functions on a complex manifold](../../../part-01/complex-morse-theory-affine-topology-and-weak-le/the-index-bound-for-strongly-q-pseudoconvex-func.md)
- [The inverse function theorem for a converging family](../../../../analysis/part-03/calculus/part-01/the-inverse-function-theorem-for-a-converging-fa.md)
- [Milnor's cell attachment theorem](../part-03/milnors-cell-attachment-theorem.md)
- [ModelWithCorners.restrictScalars](../../../part-01/complex-manifolds-transport-quotients-bundles-an/modelwithcorners-restrictscalars.md)
- [Sard's lemma in equal dimensions](../../../../analysis/part-03/calculus/part-02/sards-lemma-in-equal-dimensions.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.subsingleton_relHomotopyGroup_notMem_affineOpen`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Projectivization/Lefschetz.html#TauCeti.subsingleton_relHomotopyGroup_notMem_affineOpen).

## Other forms

**Relative homotopy Lefschetz theorem for a projective zero locus.** Formalized in Tau Ceti as [`TauCeti.subsingleton_relHomotopyGroup_complexProjectiveZeroLocus_notMem_affineOpen`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Projectivization/Lefschetz.html#TauCeti.subsingleton_relHomotopyGroup_complexProjectiveZeroLocus_notMem_affineOpen).

```lean
TauCeti.subsingleton_relHomotopyGroup_complexProjectiveZeroLocus_notMem_affineOpen.{v, u_1} {n : ℕ}
  {ι : Type u_1} [Fintype ι] {p : ι → MvPolynomial (Fin (n + 1)) ℂ} {d : ι → ℕ} {J : Type v}
  [Finite J] (hp : ∀ (m : ι), (p m).IsHomogeneous (d m)) (i : Fin (n + 1))
  (hrank :
    ∀ z ∈ TauCeti.affineZeroLocus fun m => (TauCeti.dehomogenize i) (p m),
      Function.Surjective
        (TauCeti.jacobiMatrixAt (fun m => (TauCeti.dehomogenize i) (p m)) z).mulVec)
  {W : Set ↑(TauCeti.complexProjectiveZeroLocus p)}
  {hAW : {x | ↑x ∉ Projectivization.affineOpen i} ⊆ W}
  (hW : (ContinuousMap.inclusion hAW).IsWeakHomotopyEquivalence)
  (hW_nhds : W ∈ nhdsSet {x | ↑x ∉ Projectivization.affineOpen i})
  (hJ : Nat.card J + 1 < n - Fintype.card ι) (a₀ : ↑{x | ↑x ∉ Projectivization.affineOpen i}) :
  Subsingleton
    (TauCeti.RelHomotopyGroup J
      { pair := TopPair.ofSubset {x | ↑x ∉ Projectivization.affineOpen i}, basepoint := a₀ })
```

## Sources

- [Tau Ceti documentation: `TauCeti.subsingleton_relHomotopyGroup_notMem_affineOpen`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Projectivization/Lefschetz.html#TauCeti.subsingleton_relHomotopyGroup_notMem_affineOpen)
- [Source of `TauCeti.subsingleton_relHomotopyGroup_notMem_affineOpen` in TauCeti/Geometry/Manifold/Projectivization/Lefschetz.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Projectivization/Lefschetz.lean#L306)
