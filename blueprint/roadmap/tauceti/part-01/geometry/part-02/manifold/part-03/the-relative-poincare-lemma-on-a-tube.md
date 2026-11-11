---
declaration: theorem
origin: cited
lean: Diffeomorph.exists_isSmoothForm_mextDeriv_eq_sub_mpullback, TauCeti.SmoothEmbedding.exists_isSmoothForm_relative_primitive, Diffeomorph.exists_isSmoothForm_relative_primitive, TauCeti.mextDeriv_vectorBundlePoincareHomotopy_of_mpullback_zeroSection_eq_zero
statement: formalized
proof: formalized
---

# The relative Poincaré lemma on a tube

Let `Φ` be a `C^n` diffeomorphism from the total
space of a `C^n` vector bundle onto `M`, such as a tubular neighbourhood, with zero-section
inclusion `i = Φ ∘ 0` and retraction `ρ = Φ ∘ 0 ∘ π ∘ Φ⁻¹` onto its image. Every closed `C^r`
form `η` of positive degree on `M`, with `1 ≤ r` and `r + 1 ≤ n`, has a `C^r` form `β` with
`d β = η - ρ^* η` that vanishes along `i` as a full ambient tensor.

```lean
Diffeomorph.exists_isSmoothForm_mextDeriv_eq_sub_mpullback.{u_1, u_2, u_3, u_4, u_5, u_6, u_7, u_8,
    u_9}
  {B : Type u_1} {FV : Type u_2} {V : B → Type u_3} [(b : B) → AddCommGroup (V b)]
  [(b : B) → _root_.Module ℝ (V b)] {EB : Type u_4} {HB : Type u_5} [NormedAddCommGroup EB]
  [NormedSpace ℝ EB] [TopologicalSpace HB] {IB : ModelWithCorners ℝ EB HB} [TopologicalSpace B]
  [ChartedSpace HB B] [NormedAddCommGroup FV] [NormedSpace ℝ FV] [(b : B) → TopologicalSpace (V b)]
  [TopologicalSpace (Bundle.TotalSpace FV V)] [FiberBundle FV V] {F : Type u_6}
  [NormedAddCommGroup F] [NormedSpace ℝ F] {k : ℕ} [VectorBundle ℝ FV V] [CompleteSpace F]
  {E : Type u_7} {H : Type u_8} {M : Type u_9} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I 2 M] {n : WithTop ℕ∞} [IsManifold IB n B] [ContMDiffVectorBundle n FV V IB]
  (Φ : Diffeomorph (IB.prod (modelWithCornersSelf ℝ FV)) I (Bundle.TotalSpace FV V) M n) {r : ℕ∞}
  (hr : 1 ≤ r) (hn : ↑r + 1 ≤ n) {η : TauCeti.RoughForm I M F (k + 1)}
  (hη : TauCeti.IsSmoothForm I (↑r) η) (hclosed : TauCeti.mextDeriv η = 0) :
  ∃ β,
    TauCeti.IsSmoothForm I (↑r) β ∧
      TauCeti.mextDeriv β =
          η -
            TauCeti.mpullback I I (⇑Φ ∘ Bundle.zeroSection FV V ∘ Bundle.TotalSpace.proj ∘ ⇑Φ.symm)
              η ∧
        ∀ (b : B), β (Φ (Bundle.zeroSection FV V b)) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The relative Poincaré identity](the-relative-poincare-identity.md)
- [Smooth tubular neighbourhood theorem](smooth-tubular-neighbourhood-theorem.md)

## Lean

Formalized in Tau Ceti as [`Diffeomorph.exists_isSmoothForm_mextDeriv_eq_sub_mpullback`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Relative.html#Diffeomorph.exists_isSmoothForm_mextDeriv_eq_sub_mpullback).

## Other forms

**The relative Poincaré lemma near an embedded submanifold.** Formalized in Tau Ceti as [`TauCeti.SmoothEmbedding.exists_isSmoothForm_relative_primitive`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/TubularNeighborhood/RelativePoincare.html#TauCeti.SmoothEmbedding.exists_isSmoothForm_relative_primitive).

```lean
TauCeti.SmoothEmbedding.exists_isSmoothForm_relative_primitive.{u_1, u_2, u_3, u_4, u_5, u_6, u_7}
  {E : Type u_1} {V : Type u_2} {H : Type u_3} {G : Type u_4} {M : Type u_5} {N : Type u_6}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [NormedAddCommGroup V]
  [NormedSpace ℝ V] [FiniteDimensional ℝ V] [TopologicalSpace H] [TopologicalSpace G]
  {I : ModelWithCorners ℝ E H} {J : ModelWithCorners ℝ V G} [I.Boundaryless] [J.Boundaryless]
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] [TopologicalSpace N]
  [ChartedSpace G N] [IsManifold J (↑⊤) N] [T2Space N] [SecondCountableTopology N] {F : Type u_7}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F]
  (f : TauCeti.SmoothEmbedding I J (↑⊤) M N) {O : Set N} (hO : IsOpen O) (hfO : Set.range ⇑f ⊆ O) :
  ∃ W,
    ↑W ⊆ O ∧
      ∃ (hfW : Set.range ⇑f ⊆ ↑W),
        ∀ {k : ℕ} {r : ℕ∞},
          1 ≤ r →
            ∀ {η : TauCeti.RoughForm J N F (k + 1)},
              TauCeti.IsSmoothForm J (↑r) η →
                TauCeti.mextDeriv η = 0 →
                  TauCeti.mpullback I J (⇑f) η = 0 →
                    ∃ β,
                      TauCeti.IsSmoothForm J (↑r) β ∧
                        TauCeti.mextDeriv β = TauCeti.mpullback J J Subtype.val η ∧
                          ∀ (x : M), β ⟨f x, ⋯⟩ = 0
```

**The relative Poincaré lemma on a tube, for forms restricting to zero on the core.** Formalized in Tau Ceti as [`Diffeomorph.exists_isSmoothForm_relative_primitive`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Relative.html#Diffeomorph.exists_isSmoothForm_relative_primitive).

```lean
Diffeomorph.exists_isSmoothForm_relative_primitive.{u_1, u_2, u_3, u_4, u_5, u_6, u_7, u_8, u_9}
  {B : Type u_1} {FV : Type u_2} {V : B → Type u_3} [(b : B) → AddCommGroup (V b)]
  [(b : B) → _root_.Module ℝ (V b)] {EB : Type u_4} {HB : Type u_5} [NormedAddCommGroup EB]
  [NormedSpace ℝ EB] [TopologicalSpace HB] {IB : ModelWithCorners ℝ EB HB} [TopologicalSpace B]
  [ChartedSpace HB B] [NormedAddCommGroup FV] [NormedSpace ℝ FV] [(b : B) → TopologicalSpace (V b)]
  [TopologicalSpace (Bundle.TotalSpace FV V)] [FiberBundle FV V] {F : Type u_6}
  [NormedAddCommGroup F] [NormedSpace ℝ F] {k : ℕ} [VectorBundle ℝ FV V] [CompleteSpace F]
  {E : Type u_7} {H : Type u_8} {M : Type u_9} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I 2 M] {n : WithTop ℕ∞} [IsManifold IB n B] [ContMDiffVectorBundle n FV V IB]
  (Φ : Diffeomorph (IB.prod (modelWithCornersSelf ℝ FV)) I (Bundle.TotalSpace FV V) M n) {r : ℕ∞}
  (hr : 1 ≤ r) (hn : ↑r + 1 ≤ n) {η : TauCeti.RoughForm I M F (k + 1)}
  (hη : TauCeti.IsSmoothForm I (↑r) η) (hclosed : TauCeti.mextDeriv η = 0)
  (hi : TauCeti.mpullback IB I (⇑Φ ∘ Bundle.zeroSection FV V) η = 0) :
  ∃ β,
    TauCeti.IsSmoothForm I (↑r) β ∧
      TauCeti.mextDeriv β = η ∧ ∀ (b : B), β (Φ (Bundle.zeroSection FV V b)) = 0
```

**The relative Poincaré lemma on the total space of a vector bundle.** Formalized in Tau Ceti as [`TauCeti.mextDeriv_vectorBundlePoincareHomotopy_of_mpullback_zeroSection_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Relative.html#TauCeti.mextDeriv_vectorBundlePoincareHomotopy_of_mpullback_zeroSection_eq_zero).

```lean
TauCeti.mextDeriv_vectorBundlePoincareHomotopy_of_mpullback_zeroSection_eq_zero.{u_1, u_2, u_3, u_4,
    u_5, u_6}
  {B : Type u_1} {FV : Type u_2} {V : B → Type u_3} [(b : B) → AddCommGroup (V b)]
  [(b : B) → _root_.Module ℝ (V b)] {EB : Type u_4} {HB : Type u_5} [NormedAddCommGroup EB]
  [NormedSpace ℝ EB] [TopologicalSpace HB] {IB : ModelWithCorners ℝ EB HB} [TopologicalSpace B]
  [ChartedSpace HB B] [NormedAddCommGroup FV] [NormedSpace ℝ FV] [(b : B) → TopologicalSpace (V b)]
  [TopologicalSpace (Bundle.TotalSpace FV V)] [FiberBundle FV V] {F : Type u_6}
  [NormedAddCommGroup F] [NormedSpace ℝ F] {k : ℕ} [VectorBundle ℝ FV V] [CompleteSpace F]
  [IsManifold IB 2 B] [ContMDiffVectorBundle 2 FV V IB]
  {η : TauCeti.RoughForm (IB.prod (modelWithCornersSelf ℝ FV)) (Bundle.TotalSpace FV V) F (k + 1)}
  (hη : TauCeti.IsSmoothForm (IB.prod (modelWithCornersSelf ℝ FV)) 1 η)
  (hclosed : TauCeti.mextDeriv η = 0)
  (hi :
    TauCeti.mpullback IB (IB.prod (modelWithCornersSelf ℝ FV)) (Bundle.zeroSection FV V) η = 0) :
  TauCeti.mextDeriv (TauCeti.vectorBundlePoincareHomotopy η) = η
```

## Sources

- [Tau Ceti documentation: `Diffeomorph.exists_isSmoothForm_mextDeriv_eq_sub_mpullback`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Relative.html#Diffeomorph.exists_isSmoothForm_mextDeriv_eq_sub_mpullback)
- [Source of `Diffeomorph.exists_isSmoothForm_mextDeriv_eq_sub_mpullback` in TauCeti/Geometry/Manifold/DifferentialForm/Relative.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/DifferentialForm/Relative.lean#L226)
