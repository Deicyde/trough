---
declaration: section
origin: cited
lean: Stacks.Topology.isIso_cohomologyOfGeneralizationsMap, Stacks.Topology.isIso_cohomologyOfComplementGeneralizationsMap, Stacks.Topology.higherDirectImageStalkIso, Stacks.CohomologyVanishing.cohomology_subsingleton_of_isProfiniteStacks, Stacks.CohomologyVanishing.isZero_abelianSheafCohomology_of_isProfiniteStacks, Stacks.CohomologyVanishing.cohomology_subsingleton_of_topologicalKrullDim_eq_zero, Stacks.CohomologyVanishing.subsingleton_sheafH_of_topologicalKrullDim_le, Stacks.CohomologyVanishing.subsingleton_sheafH_above_topologicalKrullDim
statement: formalized
proof: formalized
---

# 20.22 Cohomology on spectral spaces

Section 20.22 of the Stacks Project, [Tag 0A3C](https://stacks.math.columbia.edu/tag/0A3C). 4 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A3D, a lemma

[Tag 0A3D](https://stacks.math.columbia.edu/tag/0A3D) in the Stacks Project.

**`Stacks.Topology.isIso_cohomologyOfGeneralizationsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CompactSubset/GeneralizationsOfCohomology.lean, line 534](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CompactSubset/GeneralizationsOfCohomology.lean#L534). The attribute's comment: “cohomology\_of\_neighbourhoods”.

> Let `X` be a spectral space, let `F` be an abelian sheaf on `X`,
> let `E ⊆ X` be quasi-compact and let `W` be the set of points of `X` which specialize to a point
> of `E`. Then for every `p` the canonical map
>
> `colim_{E ⊆ U quasi-compact open} H^p(U, F) ⟶ H^p(W, F|_W)`
>
> is an isomorphism.

```lean
theorem isIso_cohomologyOfGeneralizationsMap (hE : IsCompact E)
    (F : Sheaf (Opens.grothendieckTopology X) AddCommGrpCat.{u}) (p : ℕ) :
    IsIso (cohomologyOfGeneralizationsMap E F p)
```

**`Stacks.Topology.isIso_cohomologyOfComplementGeneralizationsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CompactSubset/GeneralizationsOfComplementCohomology.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CompactSubset/GeneralizationsOfComplementCohomology.lean#L340). The attribute's comment: “cohomology\_of\_complements”.

> **[Stacks, Tag 0A3D] (2).** Let `X` be a spectral space, let `F` be an abelian sheaf on `X`,
> let `E ⊆ X` be quasi-compact and constructible and let `W` be the set of points of `X` which
> specialize to a point of `E`. Then for every `p` the canonical map
>
> `colim_{E ⊆ U quasi-compact open} H^p(U \ E, F|_{U \ E}) ⟶ H^p(W \ E, F|_{W \ E})`
>
> is an isomorphism.

```lean
theorem isIso_cohomologyOfComplementGeneralizationsMap (hE : Topology.IsConstructible E)
    (hEc : IsCompact E) (F : Sheaf (Opens.grothendieckTopology X) AddCommGrpCat.{u}) (p : ℕ) :
    IsIso (cohomologyOfComplementGeneralizationsMap E F p)
```

## Tag 0A3E, a lemma

[Tag 0A3E](https://stacks.math.columbia.edu/tag/0A3E) in the Stacks Project.

**`Stacks.Topology.higherDirectImageStalkIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CompactSubset/HigherDirectImageStalk.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CompactSubset/HigherDirectImageStalk.lean#L369).

> Let `f : X ⟶ Y` be a spectral map of spectral spaces, let `y` be a point of `Y`, let `E` be the
> set of points of `Y` specializing to `y` and let `F` be a sheaf of abelian groups on `X`. Then for
> every `p` the stalk at `y` of the `p`-th higher direct image of `F` is the `p`-th cohomology of the
> restriction of `F` to `f⁻¹(E)`:
>
> `(R^p f_* F)_y = H^p(f⁻¹(E), F|_{f⁻¹(E)})`.
>
> Here `f⁻¹(E)` is `Stacks.Topology.specializationFiber f y`, the set of points of `X` whose image
> specializes to `y`, and cohomology is the right derived functor of global sections.

```lean
def higherDirectImageStalkIso (hf : IsSpectralMap f) (p : ℕ)
    (F : Sheaf (Opens.grothendieckTopology X) AddCommGrpCat.{u}) :
    ((pushforwardSheafFunctor f).rightDerived p ⋙ sheafStalkFunctor y).obj F ≅
      ((sectionsFunctor (TopCat.of (specializationFiber f y))).rightDerived p).obj
        ((restrictionFunctor X (specializationFiber f y)).obj F)
```

## Tag 0A3F, a lemma

[Tag 0A3F](https://stacks.math.columbia.edu/tag/0A3F) in the Stacks Project.

**`Stacks.CohomologyVanishing.cohomology_subsingleton_of_isProfiniteStacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Vanishing/AboveTheDimension.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Vanishing/AboveTheDimension.lean#L352). The attribute's comment: “sheaf cohomology as Ext out of the constant sheaf”.

> **Stacks 0A3F.** On a profinite space every positive-degree sheaf cohomology group of every
> abelian sheaf vanishes.
>
> Global sections is exact on a profinite space, because local lifts along a cover may be refined
> to lifts along a *disjoint* finite clopen cover (Stacks 08ZZ) and those glue with no
> compatibility to check. Sheaf cohomology is `Ext` out of the constant sheaf `ℤ`, and the
> constant-sheaf functor is left adjoint to global sections, so exactness of global sections makes
> that constant sheaf projective and every `Ext` out of it vanishes in positive degree.
>
> This is the `Sheaf.H` (that is, `Ext`) formulation; the right-derived-functor formulation is
> `Stacks.CohomologyVanishing.isZero_abelianSheafCohomology_of_isProfiniteStacks`.

```lean
theorem cohomology_subsingleton_of_isProfiniteStacks
    [HasSheafify (Opens.grothendieckTopology X) AddCommGrpCat.{w}]
    [HasExt.{w'} (Sheaf (Opens.grothendieckTopology X) AddCommGrpCat.{w})]
    (hX : IsProfiniteStacks X)
    (F : Sheaf (Opens.grothendieckTopology X) AddCommGrpCat.{w})
    (q : ℕ) (hq : 0 < q) : Subsingleton (Sheaf.H.{w', w, u, u} F q)
```

**`Stacks.CohomologyVanishing.isZero_abelianSheafCohomology_of_isProfiniteStacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Vanishing/ProfiniteSpaces.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Vanishing/ProfiniteSpaces.lean#L184).

> **Stacks 0A3F.** If `X` is profinite, then every positive-degree cohomology group of
> every abelian sheaf on `X` is zero.

```lean
theorem isZero_abelianSheafCohomology_of_isProfiniteStacks
    [(Opens.grothendieckTopology X).WEqualsLocallyBijective AddCommGrpCat.{w}]
    (hX : IsProfiniteStacks X)
    (F : Sheaf (Opens.grothendieckTopology X) AddCommGrpCat.{w})
    (q : ℕ) (hq : 0 < q) :
    IsZero (abelianSheafCohomology q F)
```

## Tag 0A3G, a proposition

[Tag 0A3G](https://stacks.math.columbia.edu/tag/0A3G) in the Stacks Project.

**`Stacks.CohomologyVanishing.cohomology_subsingleton_of_topologicalKrullDim_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Vanishing/AboveTheDimension.lean, line 767](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Vanishing/AboveTheDimension.lean#L767). The attribute's comment: “clause (1) for dimension zero”.

> **Stacks 0A3G, clause (1) in dimension zero.** Let `X` be a spectral space of Krull dimension
> `0` and let `F` be an abelian sheaf on `X`. Then `H^q(X, F) = 0` for every `q > 0`.
>
> This is the base case of the induction on the dimension in Stacks 0A3G: a zero-dimensional spectral space is profinite
> (`isProfiniteStacks_of_topologicalKrullDim_eq_zero`), and on a profinite space positive-degree
> cohomology vanishes (`cohomology_subsingleton_of_isProfiniteStacks`).
>
> The hypotheses are satisfiable: `X = Spec R` for a zero-dimensional ring such as a field, a
> finite product of fields, or `ZMod 4`, has `topologicalKrullDim X = 0`, and the conclusion is
> then a genuine statement about every abelian sheaf on a nontrivial space.

```lean
theorem cohomology_subsingleton_of_topologicalKrullDim_eq_zero
    [HasSheafify (Opens.grothendieckTopology X) AddCommGrpCat.{w}]
    [HasExt.{w'} (Sheaf (Opens.grothendieckTopology X) AddCommGrpCat.{w})]
    (F : Sheaf (Opens.grothendieckTopology X) AddCommGrpCat.{w})
    (q : ℕ) (hX : topologicalKrullDim X = ((0 : ℕ) : WithBot ℕ∞)) (hq : 0 < q) :
    Subsingleton (Sheaf.H.{w', w, u, u} F q)
```

**`Stacks.CohomologyVanishing.subsingleton_sheafH_of_topologicalKrullDim_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Vanishing/SpectralSpaces.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Vanishing/SpectralSpaces.lean#L203). The attribute's comment: “clause (1): on a spectral space, sheaf cohomology vanishes above the dimension”.

> Let `Y` be a spectral space of Krull dimension at most `d` and let `G` be an abelian sheaf on
> `Y`. Then `H^q(Y, G) = 0` for every `q > d`.

```lean
theorem subsingleton_sheafH_of_topologicalKrullDim_le :
    ∀ (d : ℕ) (Y : Type u) [TopologicalSpace Y] [SpectralSpace Y]
      (_hs : HasSheafify (Opens.grothendieckTopology Y) AddCommGrpCat.{u})
      (_he : HasExt.{u} (Sheaf (Opens.grothendieckTopology Y) AddCommGrpCat.{u}))
      (G : Sheaf (Opens.grothendieckTopology Y) AddCommGrpCat.{u}) (q : ℕ),
      topologicalKrullDim Y ≤ (d : WithBot ℕ∞) → d < q →
        Subsingleton (Sheaf.H.{u, u, u, u} G q)
```

**`Stacks.CohomologyVanishing.subsingleton_sheafH_above_topologicalKrullDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Vanishing/SpectralSpaces.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Vanishing/SpectralSpaces.lean#L242). The attribute's comment: “clause (1): on a spectral space of Krull dimension at most d, sheaf cohomology vanishes in every degree above d. The same statement as the induction carrier subsingleton\_sheafH\_of\_topologicalKrullDim\_le, whose explicit HasSheafify and HasExt arguments are instance arguments here”.

> Let `Y` be a spectral space of Krull dimension at most `d` and let `G` be an abelian sheaf on
> `Y`. Then `H^q(Y, G) = 0` for every `q > d`.

```lean
theorem subsingleton_sheafH_above_topologicalKrullDim {Y : Type u} [TopologicalSpace Y]
    [SpectralSpace Y]
    [HasSheafify (Opens.grothendieckTopology Y) AddCommGrpCat.{u}]
    [HasExt.{u} (Sheaf (Opens.grothendieckTopology Y) AddCommGrpCat.{u})]
    (G : Sheaf (Opens.grothendieckTopology Y) AddCommGrpCat.{u}) (d q : ℕ)
    (hdim : topologicalKrullDim Y ≤ (d : WithBot ℕ∞)) (hq : d < q) :
    Subsingleton (Sheaf.H.{u, u, u, u} G q)
```

**`Stacks.CohomologyVanishing.surjective_cohomologyPresheaf_map_top_of_topologicalKrullDim_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Vanishing/SpectralSpaces.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Vanishing/SpectralSpaces.lean#L310). The attribute's comment: “clause (2): surjectivity of the restriction H^d(X,F) → H^d(U,F) for U quasi-compact open”.

> Let `X` be a spectral space of Krull dimension at most `d` and let `F` be an abelian sheaf on
> `X`. Then the restriction `H^d(X, F) → H^d(U, F)` is surjective for every quasi-compact open
> `U ⊆ X`.

```lean
theorem surjective_cohomologyPresheaf_map_top_of_topologicalKrullDim_le
    (F : Sheaf (Opens.grothendieckTopology X) AddCommGrpCat.{u}) (d : ℕ)
    (hdim : topologicalKrullDim X ≤ (d : WithBot ℕ∞)) (U : Opens X)
    (hU : IsCompact (U : Set X)) :
    Function.Surjective
      ((F.cohomologyPresheaf d).map (homOfLE (show U ≤ ⊤ from le_top)).op)
```

**`Stacks.CohomologyVanishing.subsingleton_sheafH_and_surjective_and_subsingleton_supported_of_topologicalKrullDim_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Vanishing/SpectralSpacesFullStatement.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Vanishing/SpectralSpacesFullStatement.lean#L91). The attribute's comment: “the whole proposition: (1) sheaf cohomology on a spectral space of Krull dimension d vanishes above degree d, (2) restriction to a quasi-compact open is surjective in degree d, and (3) cohomology with support in a constructible closed subset vanishes above degree d”.

> **[Stacks, Tag 0A3G].** Let `X` be a spectral space of Krull dimension `d` and let `F` be an
> abelian sheaf on `X`. Then
>
> 1. `H^q(X, F) = 0` for `q > d`;
> 2. `H^d(X, F) ⟶ H^d(U, F)` is surjective for every quasi-compact open `U ⊆ X`;
> 3. `H^q_Z(X, F) = 0` for `q > d` and every constructible closed subset `Z ⊆ X`.
>
> Cohomology is Mathlib's `CategoryTheory.Sheaf.H`, the `Ext`-groups out of the constant abelian
> sheaf `ℤ` on the site of opens; cohomology over an open is the value of
> `CategoryTheory.Sheaf.cohomologyPresheaf`, so that clause (2) is a statement about the restriction
> map of that presheaf; and cohomology with support in `Z` is the right derived functor of the
> sections over `X` of the subsheaf of sections supported on `Z`.
>
> Each clause is proved in the file named beside it below, where it is proved under the weaker
> hypothesis that `d` bounds the dimension rather than equalling it. Here they are put together
> under the source's hypothesis.

```lean
theorem subsingleton_sheafH_and_surjective_and_subsingleton_supported_of_topologicalKrullDim_eq
    {X : TopCat.{u}} [SpectralSpace X]
    (F : Sheaf (Opens.grothendieckTopology X) AddCommGrpCat.{u}) (d : ℕ)
    (hdim : topologicalKrullDim X = (d : WithBot ℕ∞)) :
    (∀ q : ℕ, d < q → Subsingleton (Sheaf.H.{u, u, u, u} F q)) ∧
      (∀ U : Opens X, IsCompact (U : Set X) → Function.Surjective
        ((F.cohomologyPresheaf d).map (homOfLE (show U ≤ ⊤ from le_top)).op)) ∧
      (∀ Z : Set X, IsClosed Z → IsConstructible Z → ∀ q : ℕ, d < q →
        Subsingleton (((supportedSectionsEvaluation Z ⊤).rightDerived q).obj F))
```

**`Stacks.CohomologyVanishing.subsingleton_rightDerived_supportedSections_of_topologicalKrullDim_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Vanishing/SpectralSupportVanishing.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Vanishing/SpectralSupportVanishing.lean#L130). The attribute's comment: “clause (3): cohomology with support in a constructible closed subset vanishes above the dimension”.

> **[Stacks, Tag 0A3G], clause (3).** Let `X` be a spectral space of Krull dimension at most
> `d`, let `F` be an abelian sheaf on `X` and let `Z` be a constructible closed subset of `X`.
> Then the cohomology of `F` with support in `Z` vanishes in every degree `q > d`.
>
> Cohomology with support in `Z` is the right derived functor of the sections over `X` of the
> subsheaf of sections supported on `Z`. The proof is the source's: the long exact sequence of the
> pair `(X, X ∖ Z)`, built on an injective resolution, together with clause (1) for `H^q(X, F)`
> and clause (2) for the surjectivity of `H^{q-1}(X, F) → H^{q-1}(X ∖ Z, F)`, the complement of a
> constructible closed set being a quasi-compact open.

```lean
theorem subsingleton_rightDerived_supportedSections_of_topologicalKrullDim_le
    [SpectralSpace X]
    (F : Sheaf (Opens.grothendieckTopology X) AddCommGrpCat.{u}) (d q : ℕ)
    (hdim : topologicalKrullDim X ≤ (d : WithBot ℕ∞)) (Z : Set X) (hZ : IsClosed Z)
    (hZc : IsConstructible Z) (hq : d < q) :
    Subsingleton (((supportedSectionsEvaluation Z ⊤).rightDerived q).obj F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.22, Tag 0A3C](https://stacks.math.columbia.edu/tag/0A3C)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
