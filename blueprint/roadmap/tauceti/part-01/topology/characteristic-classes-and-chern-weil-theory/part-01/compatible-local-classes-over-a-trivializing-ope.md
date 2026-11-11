---
declaration: theorem
origin: cited
lean: TauCeti.existsUnique_singularCohomology_thomPair_of_iUnion_eq_univ
statement: formalized
proof: formalized
---

# Compatible local classes over a trivializing open cover glue uniquely to the Thom pair

Let the open sets `W i` cover the base, each lying in the base set of a linear trivialization, and
let `u i ∈ Hʳ(E|_{W i}, E₀|_{W i}; R, M)`, `r = dim F` and `R` projective, have the same restriction
to the fibre pair `(E_b, E_b ∖ {0})` over every point `b` lying in two of the sets. Then there is a
unique class of `Hʳ(E, E₀; R, M)` whose restriction to the fibre over each `b ∈ W i` is that of
`u i`. The base need not be compact, Hausdorff or paracompact.

```lean
TauCeti.existsUnique_singularCohomology_thomPair_of_iUnion_eq_univ.{w, u_1} {B : Type w}
  [TopologicalSpace B] {F : Type w} [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F]
  {E : B → Type w} [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → AddCommMonoid (E b)]
  [(b : B) → _root_.Module ℝ (E b)] [(b : B) → TopologicalSpace (E b)] [FiberBundle F E]
  {ι : Type w} (W : ι → Set B) {k : Type u_1} [CommRing k] [CategoryTheory.Linear k (ModuleCat k)]
  (R M : ModuleCat k) [Module.Projective k ↑R] (hW : ⋃ i, W i = Set.univ)
  (hWo : ∀ (i : ι), IsOpen (W i))
  (hWe : ∀ (i : ι), ∃ e, ∃ (_ : Bundle.Trivialization.IsLinear ℝ e), W i ⊆ e.baseSet)
  (u : (i : ι) → ↑((TauCeti.thomPairOver F E (W i)).singularCohomology R k M (Module.finrank ℝ F)))
  (hu :
    ∀ (i j : ι) (b : B) (hi : b ∈ W i) (hj : b ∈ W j),
      (CategoryTheory.ConcreteCategory.hom
            (TopPair.singularCohomologyMap (TauCeti.fiberThomPairOverMap F E hi)
              (Module.finrank ℝ F)))
          (u i) =
        (CategoryTheory.ConcreteCategory.hom
            (TopPair.singularCohomologyMap (TauCeti.fiberThomPairOverMap F E hj)
              (Module.finrank ℝ F)))
          (u j)) :
  ∃! x,
    ∀ (i : ι) (b : B) (hb : b ∈ W i),
      (CategoryTheory.ConcreteCategory.hom
            (TopPair.singularCohomologyMap (TauCeti.fiberThomPairMap F E b) (Module.finrank ℝ F)))
          x =
        (CategoryTheory.ConcreteCategory.hom
            (TopPair.singularCohomologyMap (TauCeti.fiberThomPairOverMap F E hb)
              (Module.finrank ℝ F)))
          (u i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The relative universal coefficient theorem below the first non-projective homology, over any commutative ring `k`](../../../algebraic-topology/cohomology/the-relative-universal-coefficient-theorem-below.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.existsUnique_singularCohomology_thomPair_of_iUnion_eq_univ`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/MayerVietoris/DirectedUnion.html#TauCeti.existsUnique_singularCohomology_thomPair_of_iUnion_eq_univ).

## Sources

- [Tau Ceti documentation: `TauCeti.existsUnique_singularCohomology_thomPair_of_iUnion_eq_univ`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/MayerVietoris/DirectedUnion.html#TauCeti.existsUnique_singularCohomology_thomPair_of_iUnion_eq_univ)
- [Source of `TauCeti.existsUnique_singularCohomology_thomPair_of_iUnion_eq_univ` in TauCeti/Topology/VectorBundle/MayerVietoris/DirectedUnion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/VectorBundle/MayerVietoris/DirectedUnion.lean#L345)
- [Tau Ceti roadmap status: Characteristic classes and Chern–Weil theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CharacteristicClasses/STATUS.md)
