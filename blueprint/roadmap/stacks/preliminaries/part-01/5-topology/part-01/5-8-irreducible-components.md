---
declaration: section
origin: cited
lean: irreducibleComponents_eq_range_of_irredundant_cover, ncard_irreducibleComponents_le_of_surjective, isGenericPoint_iff, kolmogorov_iff, local_quasiSober_iff, StacksSober, IsLocallyClosed.quasiSober, IsLocallyClosed.quasiSober_and_t0Space
statement: formalized
proof: formalized
---

# 5.8 Irreducible components

Section 5.8 of the Stacks Project, [Tag 004U](https://stacks.math.columbia.edu/tag/004U). 13 tags here are carried by 26 declarations of the repository (2 in StacksCore and 24 in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G2Y, a lemma

[Tag 0G2Y](https://stacks.math.columbia.edu/tag/0G2Y) in the Stacks Project.

**`irreducibleComponents_eq_range_of_irredundant_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/IrreducibleComponents.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/IrreducibleComponents.lean#L35). References: EGA 0 (2.1.7), “first assertion”.

> **Stacks 0G2Y**.
> Given an irredundant finite covering of `X` by irreducible closed subsets `T i` (`i : Fin n`),
> the set of irreducible components of `X` is exactly the image of `T`.

```lean
theorem irreducibleComponents_eq_range_of_irredundant_cover
    {n : ℕ} (T : Fin n → Set X)
    (hcov : ⋃ i, T i = (Set.univ : Set X))
    (hirr : ∀ i, IsIrreducible (T i))
    (hcl : ∀ i, IsClosed (T i))
    (hmin : ∀ i, ¬ T i ⊆ ⋃ j ∈ ({j | j ≠ i} : Set (Fin n)), T j) :
    irreducibleComponents X = Set.range T
```

## Tag 0GM2, a lemma

[Tag 0GM2](https://stacks.math.columbia.edu/tag/0GM2) in the Stacks Project.

**`ncard_irreducibleComponents_le_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/SurjectionComponents.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/SurjectionComponents.lean#L63).

> Let `f : X → Y` be a surjective, continuous map of topological spaces. If `X` has finitely
> many irreducible components, then `Y` has finitely many irreducible components and their number
> is at most that of `X`.

```lean
theorem ncard_irreducibleComponents_le_of_surjective
    {X Y : Type*} [TopologicalSpace X] [TopologicalSpace Y]
    (f : X → Y) (hf_cont : Continuous f) (hf_surj : Function.Surjective f)
    (hX : (irreducibleComponents X).Finite) :
    (irreducibleComponents Y).Finite ∧
      (irreducibleComponents Y).ncard ≤ (irreducibleComponents X).ncard
```

## Tag 004X, a definition

[Tag 004X](https://stacks.math.columbia.edu/tag/004X) in the Stacks Project.

**`isGenericPoint_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/Defs.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/Defs.lean#L70). The attribute's comment: “generic point”.

> A point `ξ` lies in `Z` with `Z = closure {ξ}` exactly when `ξ` is a generic point of `Z`.

```lean
theorem isGenericPoint_iff (Z : Set X) (ξ : X) :
    (ξ ∈ Z ∧ Z = closure {ξ}) ↔ IsGenericPoint ξ Z
```

**`kolmogorov_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/Defs.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/Defs.lean#L77). The attribute's comment: “Kolmogorov”. References: EGA 0 (2.1.3).

> A space in which any two distinct points are separated by a closed set is exactly a
> `T0Space`.

```lean
theorem kolmogorov_iff :
    (∀ x x' : X, x ≠ x' →
        ∃ C : Set X, IsClosed C ∧ ((x ∈ C) ↔ x' ∉ C)) ↔ T0Space X
```

**`local_quasiSober_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/Defs.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/Defs.lean#L93). The attribute's comment: “quasi-sober”.

> A space in which every irreducible closed subset `Z` admits some `ξ ∈ Z` with `Z = closure {ξ}`
> is exactly a `QuasiSober` space.

```lean
theorem local_quasiSober_iff :
    (∀ Z : Set X, IsIrreducible Z → IsClosed Z →
        ∃ ξ ∈ Z, Z = closure {ξ}) ↔ QuasiSober X
```

**`StacksSober`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/Defs.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/Defs.lean#L102). The attribute's comment: “sober”. References: SGA 4 IV (4.2.1), “sober definition”; SGA 4 VIII (7.9.3).

> A space is sober when every irreducible closed subset has a *unique* generic point.

```lean
def StacksSober (X : Type*) [TopologicalSpace X] : Prop
```

## Tag 0B31, a lemma

[Tag 0B31](https://stacks.math.columbia.edu/tag/0B31) in the Stacks Project.

**`IsLocallyClosed.quasiSober`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/LocallyClosed.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/LocallyClosed.lean#L35). The attribute's comment: “(2)”.

> **Stacks 0B31 (2).** A locally closed subspace of a quasi-sober space is quasi-sober.

```lean
theorem IsLocallyClosed.quasiSober [QuasiSober X] {Y : Set X} (hY : IsLocallyClosed Y) :
    QuasiSober Y
```

**`IsLocallyClosed.quasiSober_and_t0Space`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/LocallyClosed.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/LocallyClosed.lean#L44). The attribute's comment: “(3)”.

> **Stacks 0B31 (3).** A locally closed subspace of a sober space is sober, sobriety being
> `QuasiSober` together with `T0Space`.

```lean
theorem IsLocallyClosed.quasiSober_and_t0Space [QuasiSober X] [T0Space X] {Y : Set X}
    (hY : IsLocallyClosed Y) : QuasiSober Y ∧ T0Space Y
```

## Tag 06N9, a lemma

[Tag 06N9](https://stacks.math.columbia.edu/tag/06N9) in the Stacks Project.

**`kolmogorov_iff_of_locallyClosed_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/Local.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/Local.lean#L59). The attribute's comment: “(1)”.

> If a covering `U` of `X` consists of locally closed subsets, then `X` is Kolmogorov if and only
> if each `U i` is.

```lean
theorem kolmogorov_iff_of_locallyClosed_cover
    {I : Type*} (U : I → Set X)
    (hcov : ⋃ i, U i = Set.univ)
    (hlc : ∀ i, IsLocallyClosed (U i)) :
    T0Space X ↔ ∀ i, T0Space (U i)
```

**`quasiSober_iff_of_open_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/Local.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/Local.lean#L86). The attribute's comment: “(2)”.

> If a covering `U` of `X` consists of open subsets, then `X` is quasi-sober if and only if each
> `U i` is.

```lean
theorem quasiSober_iff_of_open_cover
    {I : Type*} (U : I → Set X)
    (hcov : ⋃ i, U i = Set.univ)
    (hopen : ∀ i, IsOpen (U i)) :
    QuasiSober X ↔ ∀ i, QuasiSober (U i)
```

**`sober_iff_of_open_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/Local.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/Local.lean#L96). The attribute's comment: “(3)”.

> If a covering `U` of `X` consists of open subsets, then `X` is sober if and only if each `U i`
> is.

```lean
theorem sober_iff_of_open_cover
    {I : Type*} (U : I → Set X)
    (hcov : ⋃ i, U i = Set.univ)
    (hopen : ∀ i, IsOpen (U i)) :
    StacksSober X ↔ ∀ i, StacksSober (U i)
```

## Tag 0B32, an example

[Tag 0B32](https://stacks.math.columbia.edu/tag/0B32) in the Stacks Project.

**`quasiSober_of_indiscreteTopology`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/Sober/Indiscrete.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Sober/Indiscrete.lean#L30). The attribute's comment: “quasi-sober”.

> **Stacks 0B32.** An indiscrete topological space with at least two points is
> quasi-sober: its only nonempty closed subset is the whole space, and every point is a
> generic point for it.

```lean
theorem quasiSober_of_indiscreteTopology (X : Type*) [TopologicalSpace X]
    [IndiscreteTopology X] [Nontrivial X] : QuasiSober X
```

**`not_t0Space_of_indiscreteTopology`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/Sober/Indiscrete.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Sober/Indiscrete.lean#L41). The attribute's comment: “not Kolmogorov”.

> **Stacks 0B32.** An indiscrete topological space with at least two points is not
> Kolmogorov: any two of its points are inseparable.

```lean
theorem not_t0Space_of_indiscreteTopology (X : Type*) [TopologicalSpace X]
    [IndiscreteTopology X] [Nontrivial X] : ¬ T0Space X
```

Declarations registered for the tag:

- [`Set.iUnion_of_singleton`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Set.iUnion_of_singleton#doc) registered with `add_to_stacks` in [StacksCore/Topology/Sober/Indiscrete.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Sober/Indiscrete.lean#L47) (StacksCore): “the singleton subspaces cover the space”.
- [`Subsingleton.discreteTopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Subsingleton.discreteTopology#doc) registered with `add_to_stacks` in [StacksCore/Topology/Sober/Indiscrete.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Sober/Indiscrete.lean#L48) (StacksCore): “the singleton subspaces are discrete”.

## Tag 0B33, an example

[Tag 0B33](https://stacks.math.columbia.edu/tag/0B33) in the Stacks Project.

**`t0Space_cofiniteTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/CofiniteExample.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/CofiniteExample.lean#L44). The attribute's comment: “Kolmogorov”.

> **Stacks 0B33** (Kolmogorov).
> An infinite set with the cofinite topology is Kolmogorov: its singletons are finite, hence
> closed, so the space is `T1Space` and a fortiori `T0Space`. Infiniteness is not needed here.

```lean
theorem t0Space_cofiniteTopology : T0Space (CofiniteTopology Y)
```

**`not_quasiSober_cofiniteTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/CofiniteExample.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/CofiniteExample.lean#L50). The attribute's comment: “not quasi-sober”.

> **Stacks 0B33** (not quasi-sober).
> An infinite set with the cofinite topology is not quasi-sober: the whole space is irreducible
> and closed, but the closure of a singleton is that singleton, so no point is generic for it.

```lean
theorem not_quasiSober_cofiniteTopology [Infinite Y] : ¬ QuasiSober (CofiniteTopology Y)
```

**`singleton_cover_cofiniteTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/CofiniteExample.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/CofiniteExample.lean#L65). The attribute's comment: “covering by discrete, hence sober, subspaces”.

> **Stacks 0B33** (covering by sober subspaces).
> The singletons of an infinite set with the cofinite topology cover it, and each singleton
> subspace is discrete and hence sober: it has exactly one point. So a space covered by sober
> subspaces need not be quasi-sober.

```lean
theorem singleton_cover_cofiniteTopology :
    (⋃ y : CofiniteTopology Y, ({y} : Set (CofiniteTopology Y))) = Set.univ ∧
      ∀ y : CofiniteTopology Y, DiscreteTopology ({y} : Set (CofiniteTopology Y)) ∧
        StacksSober ({y} : Set (CofiniteTopology Y))
```

## Tag 0B34, an example

[Tag 0B34](https://stacks.math.columbia.edu/tag/0B34) in the Stacks Project.

**`not_t0Space_sum_cofiniteTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/CounterexampleNeither.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/CounterexampleNeither.lean#L30).

> **Stacks 0B34.** The disjoint union of an indiscrete space with at least two points and
> an infinite set with the cofinite topology is not Kolmogorov.

```lean
theorem not_t0Space_sum_cofiniteTopology (X : Type*) [TopologicalSpace X]
    [IndiscreteTopology X] [Nontrivial X] (Y : Type*) [Infinite Y] :
    ¬ T0Space (X ⊕ CofiniteTopology Y)
```

**`not_quasiSober_sum_cofiniteTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/CounterexampleNeither.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/CounterexampleNeither.lean#L39).

> **Stacks 0B34.** The disjoint union of an indiscrete space with at least two points and
> an infinite set with the cofinite topology is not quasi-sober.

```lean
theorem not_quasiSober_sum_cofiniteTopology (X : Type*) [TopologicalSpace X]
    [IndiscreteTopology X] [Nontrivial X] (Y : Type*) [Infinite Y] :
    ¬ QuasiSober (X ⊕ CofiniteTopology Y)
```

## Tag 0B35, an example

[Tag 0B35](https://stacks.math.columbia.edu/tag/0B35) in the Stacks Project.

**`Stacks.Examples.SoberSubspace.unique_genericPoint_cofiniteAway`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/CounterexampleSubspace.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/CounterexampleSubspace.lean#L150).

> **Stacks 0B35.** The space `Z` with the topology `cofiniteAway Z z` is sober: every
> irreducible closed subset has a unique generic point.

```lean
theorem unique_genericPoint_cofiniteAway (Z : Type*) [Infinite Z] (z : Z) :
    letI : TopologicalSpace Z := cofiniteAway Z z
    ∀ {S : Set Z}, IsIrreducible S → IsClosed S → ∃! x, IsGenericPoint x S
```

**`Stacks.Examples.SoberSubspace.not_quasiSober_subtype_ne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/CounterexampleSubspace.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/CounterexampleSubspace.lean#L161).

> **Stacks 0B35.** The subspace `Z \ {z}` of the sober space `cofiniteAway Z z` is not
> quasi-sober: it is irreducible, yet all of its singletons are closed.

```lean
theorem not_quasiSober_subtype_ne (Z : Type*) [Infinite Z] (z : Z) :
    letI : TopologicalSpace Z := cofiniteAway Z z
    ¬ QuasiSober ({x : Z // x ≠ z})
```

## Tag 004Y, an example

[Tag 004Y](https://stacks.math.columbia.edu/tag/004Y) in the Stacks Project.

**`isIrreducible_iff_singleton_of_t2`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/Irreducible.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/Irreducible.lean#L67). The attribute's comment: “subset irreducible iff singleton”.

> **Stacks 004Y** (subset irreducible iff singleton).
> A subset `s` of a Hausdorff space `X` is irreducible if and only if `s` is a singleton.

```lean
theorem isIrreducible_iff_singleton_of_t2 (X : Type*) [TopologicalSpace X]
    [T2Space X] (s : Set X) :
    IsIrreducible s ↔ ∃ x : X, s = {x}
```

**`irreducibleSpace_iff_univ_singleton_of_t2`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/Irreducible.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/Irreducible.lean#L76). The attribute's comment: “space irreducible iff singleton”.

> **Stacks 004Y** (space irreducible iff singleton).
> A Hausdorff space `X` is irreducible as a space if and only if its underlying set is a
> singleton.

```lean
theorem irreducibleSpace_iff_univ_singleton_of_t2 (X : Type*)
    [TopologicalSpace X] [T2Space X] :
    IrreducibleSpace X ↔ ∃ x : X, (Set.univ : Set X) = {x}
```

**`sober_of_t2`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/Irreducible.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/Irreducible.lean#L98). The attribute's comment: “Hausdorff implies sober”. References: SGA 4 IV (4.2.1), “Hausdorff ⇒ sober”.

> **Stacks 004Y** (Hausdorff implies sober).
> A Hausdorff space is `T0` and quasi-sober, that is, sober.

```lean
theorem sober_of_t2 (X : Type*) [TopologicalSpace X] [T2Space X] :
    T0Space X ∧ QuasiSober X
```

## Tag 004Z, a lemma

[Tag 004Z](https://stacks.math.columbia.edu/tag/004Z) in the Stacks Project.

**`irreducibleSpace_of_continuous_of_dense_isIrreducible_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Irreducible/DenseFibres.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Irreducible/DenseFibres.lean#L106).

> **Stacks 004Z**.
> Let `f : X → Y` be a continuous map of topological spaces. Assume that (a) `Y` is irreducible,
> (b) `f` is open, and (c) there exists a dense collection of points `y ∈ Y` such that `f ⁻¹' {y}`
> is irreducible. Then `X` is irreducible.
>
> The continuity hypothesis (a) is recorded here because the source states it; the proof does not
> use it, see `irreducibleSpace_of_isOpenMap_of_dense_isIrreducible_fiber`.

```lean
theorem irreducibleSpace_of_continuous_of_dense_isIrreducible_fiber
    [IrreducibleSpace Y] {f : X → Y} (_hfcont : Continuous f) (hfopen : IsOpenMap f)
    (hfib : Dense {y : Y | IsIrreducible (f ⁻¹' {y})}) :
    IrreducibleSpace X
```

## Tag 0A2N, a lemma

[Tag 0A2N](https://stacks.math.columbia.edu/tag/0A2N) in the Stacks Project.

**`Soberification.exists_universal_quasiSober`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sober/Soberification.lean, line 484](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sober/Soberification.lean#L484). References: SGA 4 IV (4.2.1), “universal property”.

> For any topological space `X`, there is a canonical continuous map `c : X → X'` from `X`
> to a sober topological space `X'` which is universal among continuous maps from `X` to sober
> topological spaces. Moreover, the assignment `U' ↦ c⁻¹(U')` is a bijection between opens of `X'`
> and `X` which commutes with finite intersections and arbitrary unions. The image `c(X)` is a
> Kolmogorov (`T0`) topological space and the map `c : X → c(X)` is universal for maps of `X` into
> Kolmogorov spaces.

```lean
theorem exists_universal_quasiSober :
    -- Sober target with continuous canonical map and universal property
    ∃ (X' : Type u) (_ : TopologicalSpace X') (_ : QuasiSober X') (_ : T0Space X')
      (c' : X → X') (_ : Continuous c'),
        (-- Universal property among sober spaces
         (∀ (Y : Type u) [TopologicalSpace Y] [QuasiSober Y] [T0Space Y]
            (f : X → Y), Continuous f →
              ∃ f' : X' → Y, Continuous f' ∧ f' ∘ c' = f ∧
                ∀ g : X' → Y, Continuous g → g ∘ c' = f → g = f') ∧
         -- Bijection between opens, commuting with finite intersections and arbitrary unions
         (∃ φ : TopologicalSpace.Opens X' ≃ TopologicalSpace.Opens X,
            (∀ V : TopologicalSpace.Opens X', (φ V : Set X) = c' ⁻¹' (V : Set X')) ∧
            (φ ⊤ = ⊤) ∧
            (∀ V W : TopologicalSpace.Opens X', φ (V ⊓ W) = φ V ⊓ φ W) ∧
            (∀ {ι : Sort*} (V : ι → TopologicalSpace.Opens X'),
                φ (⨆ i, V i) = ⨆ i, φ (V i))) ∧
         -- c(X) is T0 (Kolmogorov)
         T0Space (Set.range c') ∧
         -- Universal property for c : X → c(X) into Kolmogorov spaces
         (∀ (Y : Type u) [TopologicalSpace Y] [T0Space Y] (f : X → Y),
            Continuous f →
              ∃ f' : Set.range c' → Y, Continuous f' ∧
                (∀ x : X, f' ⟨c' x, ⟨x, rfl⟩⟩ = f x) ∧
                ∀ g : Set.range c' → Y, Continuous g →
                  (∀ x : X, g ⟨c' x, ⟨x, rfl⟩⟩ = f x) → g = f'))
```

## Tag 0GM3, a lemma

[Tag 0GM3](https://stacks.math.columbia.edu/tag/0GM3) in the Stacks Project.

**`TopologicalSpace.exists_isConnected_sUnion_irreducibleComponents_sdiff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Connected/IrreducibleComponentRemoval.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Connected/IrreducibleComponentRemoval.lean#L146).

> **Stacks 0GM3.** Let `X` be a connected topological space with finitely many irreducible
> components, more than one of them. Then some irreducible component `Z` may be deleted so
> that the union of the remaining components is still connected.

```lean
theorem exists_isConnected_sUnion_irreducibleComponents_sdiff [ConnectedSpace X]
    (h_fin : (irreducibleComponents X).Finite)
    (h_gt : 1 < (irreducibleComponents X).ncard) :
    ∃ Z ∈ irreducibleComponents X,
      IsConnected (⋃₀ (irreducibleComponents X \ {Z}))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.8, Tag 004U](https://stacks.math.columbia.edu/tag/004U)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
