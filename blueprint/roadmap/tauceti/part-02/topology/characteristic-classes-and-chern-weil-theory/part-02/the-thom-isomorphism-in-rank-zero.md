---
declaration: theorem
origin: cited
lean: TauCeti.IsThomClass.bijective_thomMap_of_finrank_eq_zero, TauCeti.IsThomClass.bijective_thomMap_of_baseSet_eq_univ, TauCeti.IsThomClass.bijective_homologyThomMap, TauCeti.IsThomClass.bijective_homologyThomMap_of_biUnion_eq_univ, TauCeti.IsThomClass.bijective_thomMap, TauCeti.IsThomClass.bijective_pullbackCupRestrict_biUnion, TauCeti.IsThomClass.bijective_thomMap_of_biUnion_eq_univ, TauCeti.IsThomClass.bijective_pullbackCupRestrict_of_subset_baseSet
statement: formalized
proof: formalized
---

# The Thom isomorphism in rank zero

For a bundle of rank zero and a Thom class `u`, the Thom
map `a ↦ π^*a ⌣ u` is a bijection `Hᵖ(B; M) ≅ Hᵖ(E, E₀; M)` in every degree, for every `K`-module
`M` of coefficients.

```lean
TauCeti.IsThomClass.bijective_thomMap_of_finrank_eq_zero.{w, u_1} {B : Type w} [TopologicalSpace B]
  {F : Type u_1} [NormedAddCommGroup F] [NormedSpace ℝ F] {E : B → Type w}
  [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → Zero (E b)]
  [(b : B) → TopologicalSpace (E b)] [FiberBundle F E] {K : Type w} [CommRing K]
  (hF : Module.finrank ℝ F = 0)
  {u : ↑((TauCeti.thomPair F E).singularCohomology (↧K) K (↧K) (Module.finrank ℝ F))}
  (hu : TauCeti.IsThomClass F E u) (M : ModuleCat K) {p m : ℕ} (h : p + Module.finrank ℝ F = m) :
  Function.Bijective ⇑((TauCeti.thomMap F E M (Module.finrank ℝ F) p m h) u)
```

## Depends on

- [The Thom map](../part-01/the-thom-map.md)

## Proof depends on

- [The Mayer–Vietoris connecting morphism commutes with cup products](the-mayer-vietoris-connecting-morphism-commutes.md)
- [The relative universal coefficient theorem over a field](../../../../part-01/algebraic-topology/cohomology/the-relative-universal-coefficient-theorem-over.md)
- [The Thom isomorphism for a product bundle](../../../../part-01/algebraic-topology/cohomology/the-thom-isomorphism-for-a-product-bundle.md)
- [The universal coefficient theorem over a field](../../../../part-01/algebraic-topology/cohomology/the-universal-coefficient-theorem-over-a-field.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsThomClass.bijective_thomMap_of_finrank_eq_zero`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Thom/RankZero.html#TauCeti.IsThomClass.bijective_thomMap_of_finrank_eq_zero).

## Other forms

**The Thom isomorphism for a trivializable bundle.** Formalized in Tau Ceti as [`TauCeti.IsThomClass.bijective_thomMap_of_baseSet_eq_univ`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Thom/Isomorphism.html#TauCeti.IsThomClass.bijective_thomMap_of_baseSet_eq_univ).

```lean
TauCeti.IsThomClass.bijective_thomMap_of_baseSet_eq_univ.{w} {B : Type w} [TopologicalSpace B]
  {F : Type w} [NormedAddCommGroup F] [NormedSpace ℝ F] {E : B → Type w}
  [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → AddCommMonoid (E b)]
  [(b : B) → _root_.Module ℝ (E b)] [(b : B) → TopologicalSpace (E b)] [FiberBundle F E]
  {K : Type w} [CommRing K] (M : ModuleCat K)
  {u : ↑((TauCeti.thomPair F E).singularCohomology (↧K) K (↧K) (Module.finrank ℝ F))}
  (hu : TauCeti.IsThomClass F E u) (hF : 2 ≤ Module.finrank ℝ F)
  (e : Bundle.Trivialization F Bundle.TotalSpace.proj) [Bundle.Trivialization.IsLinear ℝ e]
  (he : e.baseSet = Set.univ) {p m : ℕ} (h : p + Module.finrank ℝ F = m) :
  Function.Bijective ⇑((TauCeti.thomMap F E M (Module.finrank ℝ F) p m h) u)
```

**The Thom isomorphism in homology over a compact base.** Formalized in Tau Ceti as [`TauCeti.IsThomClass.bijective_homologyThomMap`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Thom/Bijective.html#TauCeti.IsThomClass.bijective_homologyThomMap).

```lean
TauCeti.IsThomClass.bijective_homologyThomMap.{w} {B : Type w} [TopologicalSpace B] {F : Type w}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] {E : B → Type w}
  [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → AddCommMonoid (E b)]
  [(b : B) → _root_.Module ℝ (E b)] [(b : B) → TopologicalSpace (E b)] [FiberBundle F E]
  {K : Type w} [Field K] [CompactSpace B] [VectorBundle ℝ F E] (hF : 2 ≤ Module.finrank ℝ F)
  {u : ↑((TauCeti.thomPair F E).singularCohomology (↧K) K (↧K) (Module.finrank ℝ F))}
  (hu : TauCeti.IsThomClass F E u) {p m : ℕ} (h : Module.finrank ℝ F + p = m) :
  Function.Bijective
    ⇑(ModuleCat.Hom.hom ((TauCeti.homologyThomMap F E (↧K) (Module.finrank ℝ F) p m h) u))
```

**The Thom isomorphism in homology over a finitely trivialized base.** Formalized in Tau Ceti as [`TauCeti.IsThomClass.bijective_homologyThomMap_of_biUnion_eq_univ`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Thom/Bijective.html#TauCeti.IsThomClass.bijective_homologyThomMap_of_biUnion_eq_univ).

```lean
TauCeti.IsThomClass.bijective_homologyThomMap_of_biUnion_eq_univ.{w, u_1} {B : Type w}
  [TopologicalSpace B] {F : Type w} [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F]
  {E : B → Type w} [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → AddCommMonoid (E b)]
  [(b : B) → _root_.Module ℝ (E b)] [(b : B) → TopologicalSpace (E b)] [FiberBundle F E]
  {K : Type w} [Field K] (hF : 2 ≤ Module.finrank ℝ F)
  {u : ↑((TauCeti.thomPair F E).singularCohomology (↧K) K (↧K) (Module.finrank ℝ F))}
  (hu : TauCeti.IsThomClass F E u) {ι : Type u_1} (s : Finset ι) {W : ι → Set B}
  (hWo : ∀ i ∈ s, IsOpen (W i))
  (hWe : ∀ i ∈ s, ∃ e, ∃ (_ : Bundle.Trivialization.IsLinear ℝ e), W i ⊆ e.baseSet)
  (hW : ⋃ i ∈ s, W i = Set.univ) {p m : ℕ} (h : Module.finrank ℝ F + p = m) :
  Function.Bijective
    ⇑(ModuleCat.Hom.hom ((TauCeti.homologyThomMap F E (↧K) (Module.finrank ℝ F) p m h) u))
```

**The Thom isomorphism over a compact base.** Formalized in Tau Ceti as [`TauCeti.IsThomClass.bijective_thomMap`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Thom/Bijective.html#TauCeti.IsThomClass.bijective_thomMap).

```lean
TauCeti.IsThomClass.bijective_thomMap.{w} {B : Type w} [TopologicalSpace B] {F : Type w}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] {E : B → Type w}
  [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → AddCommMonoid (E b)]
  [(b : B) → _root_.Module ℝ (E b)] [(b : B) → TopologicalSpace (E b)] [FiberBundle F E]
  {K : Type w} [CommRing K] (M : ModuleCat K) [CompactSpace B] [VectorBundle ℝ F E]
  (hF : 2 ≤ Module.finrank ℝ F)
  {u : ↑((TauCeti.thomPair F E).singularCohomology (↧K) K (↧K) (Module.finrank ℝ F))}
  (hu : TauCeti.IsThomClass F E u) {p m : ℕ} (h : p + Module.finrank ℝ F = m) :
  Function.Bijective ⇑((TauCeti.thomMap F E M (Module.finrank ℝ F) p m h) u)
```

**The Thom isomorphism over a finite union of trivializing open sets.** Formalized in Tau Ceti as [`TauCeti.IsThomClass.bijective_pullbackCupRestrict_biUnion`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Thom/Bijective.html#TauCeti.IsThomClass.bijective_pullbackCupRestrict_biUnion).

```lean
TauCeti.IsThomClass.bijective_pullbackCupRestrict_biUnion.{w, u_1} {B : Type w} [TopologicalSpace B]
  {F : Type w} [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] {E : B → Type w}
  [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → AddCommMonoid (E b)]
  [(b : B) → _root_.Module ℝ (E b)] [(b : B) → TopologicalSpace (E b)] [FiberBundle F E]
  {K : Type w} [CommRing K] (M : ModuleCat K) (hF : 2 ≤ Module.finrank ℝ F)
  {u : ↑((TauCeti.thomPair F E).singularCohomology (↧K) K (↧K) (Module.finrank ℝ F))}
  (hu : TauCeti.IsThomClass F E u) {ι : Type u_1} (s : Finset ι) {W : ι → Set B}
  (hWo : ∀ i ∈ s, IsOpen (W i))
  (hWe : ∀ i ∈ s, ∃ e, ∃ (_ : Bundle.Trivialization.IsLinear ℝ e), W i ⊆ e.baseSet) {p m : ℕ}
  (h : p + Module.finrank ℝ F = m) :
  Function.Bijective
    ⇑((TopCat.pullbackCupRestrict
          (TopCat.ofHom { toFun := Bundle.TotalSpace.proj, continuous_toFun := ⋯ })
          (TauCeti.zeroSectionCompl F E) M (⋃ i ∈ s, W i) (Module.finrank ℝ F) p m h)
        u)
```

**The Thom isomorphism over a finitely trivialized base.** Formalized in Tau Ceti as [`TauCeti.IsThomClass.bijective_thomMap_of_biUnion_eq_univ`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Thom/Bijective.html#TauCeti.IsThomClass.bijective_thomMap_of_biUnion_eq_univ).

```lean
TauCeti.IsThomClass.bijective_thomMap_of_biUnion_eq_univ.{w, u_1} {B : Type w} [TopologicalSpace B]
  {F : Type w} [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] {E : B → Type w}
  [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → AddCommMonoid (E b)]
  [(b : B) → _root_.Module ℝ (E b)] [(b : B) → TopologicalSpace (E b)] [FiberBundle F E]
  {K : Type w} [CommRing K] (M : ModuleCat K) (hF : 2 ≤ Module.finrank ℝ F)
  {u : ↑((TauCeti.thomPair F E).singularCohomology (↧K) K (↧K) (Module.finrank ℝ F))}
  (hu : TauCeti.IsThomClass F E u) {ι : Type u_1} (s : Finset ι) {W : ι → Set B}
  (hWo : ∀ i ∈ s, IsOpen (W i))
  (hWe : ∀ i ∈ s, ∃ e, ∃ (_ : Bundle.Trivialization.IsLinear ℝ e), W i ⊆ e.baseSet)
  (hW : ⋃ i ∈ s, W i = Set.univ) {p m : ℕ} (h : p + Module.finrank ℝ F = m) :
  Function.Bijective ⇑((TauCeti.thomMap F E M (Module.finrank ℝ F) p m h) u)
```

**The Thom isomorphism over a trivializing set.** Formalized in Tau Ceti as [`TauCeti.IsThomClass.bijective_pullbackCupRestrict_of_subset_baseSet`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Thom/Isomorphism.html#TauCeti.IsThomClass.bijective_pullbackCupRestrict_of_subset_baseSet).

```lean
TauCeti.IsThomClass.bijective_pullbackCupRestrict_of_subset_baseSet.{w} {B : Type w}
  [TopologicalSpace B] {F : Type w} [NormedAddCommGroup F] [NormedSpace ℝ F] {E : B → Type w}
  [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → AddCommMonoid (E b)]
  [(b : B) → _root_.Module ℝ (E b)] [(b : B) → TopologicalSpace (E b)] [FiberBundle F E]
  {K : Type w} [CommRing K] (M : ModuleCat K)
  {u : ↑((TauCeti.thomPair F E).singularCohomology (↧K) K (↧K) (Module.finrank ℝ F))}
  (hu : TauCeti.IsThomClass F E u) (hF : 2 ≤ Module.finrank ℝ F)
  (e : Bundle.Trivialization F Bundle.TotalSpace.proj) [Bundle.Trivialization.IsLinear ℝ e]
  {W : Set B} (hW : W ⊆ e.baseSet) {p m : ℕ} (h : p + Module.finrank ℝ F = m) :
  Function.Bijective
    ⇑((TopCat.pullbackCupRestrict (TauCeti.thomPairProj F E) (TauCeti.zeroSectionCompl F E) M W
          (Module.finrank ℝ F) p m h)
        u)
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsThomClass.bijective_thomMap_of_finrank_eq_zero`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Thom/RankZero.html#TauCeti.IsThomClass.bijective_thomMap_of_finrank_eq_zero)
- [Source of `TauCeti.IsThomClass.bijective_thomMap_of_finrank_eq_zero` in TauCeti/Topology/VectorBundle/Thom/RankZero.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/VectorBundle/Thom/RankZero.lean#L141)
