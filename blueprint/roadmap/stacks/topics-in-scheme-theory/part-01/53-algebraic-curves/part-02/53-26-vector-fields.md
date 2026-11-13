---
declaration: section
origin: cited
lean: Stacks.Curves.SheafDerivation, Stacks.Curves.SheafDerivation.smoothCurve_genus_cases, Stacks.Curves.NodalVectorFields.range_branchPair, Stacks.Curves.SheafDerivation.eq_zero_of_hasAtWorstNodalSingularities
statement: formalized
proof: formalized
---

# 53.26 Vector fields

Section 53.26 of the Stacks Project, [Tag 0E66](https://stacks.math.columbia.edu/tag/0E66). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E66, the section

[Tag 0E66](https://stacks.math.columbia.edu/tag/0E66) in the Stacks Project.

**`Stacks.Curves.SheafDerivation`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/SheafDerivation.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/SheafDerivation.lean#L56).

> **Stacks 0E66.** `Der_k(𝒪_X, 𝒪_X)`: the `k`-linear derivations of the structure sheaf of a
> `k`-scheme `X` into itself. These are the vector fields on `X` of Section 53.26.

```lean
abbrev SheafDerivation (k : Type u) [Field k] (X : Scheme.{u}) [X.Over (Spec (.of k))]
```

## Tag 0E67, a lemma

[Tag 0E67](https://stacks.math.columbia.edu/tag/0E67) in the Stacks Project.

**`Stacks.Curves.SheafDerivation.smoothCurve_genus_cases`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VectorFieldsGenus.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/VectorFieldsGenus.lean#L65).

> **[Stacks, Tag 0E67]**: let `X` be a smooth proper curve of genus `g` over an algebraically
> closed field `k` (a curve is integral, so connected). If `g ≥ 2` then `Der_k(𝒪_X, 𝒪_X) = 0`; if
> `g = 1` a nonzero vector field fixes no closed point; if `g = 0` a nonzero vector field fixes at
> most two closed points.

```lean
theorem SheafDerivation.smoothCurve_genus_cases [IsAlgClosed k] (X : Scheme.{u})
    [X.Over (Spec (.of k))] [IsCurve k (X ↘ Spec (.of k))] [Smooth (X ↘ Spec (.of k))]
    [IsProper (X ↘ Spec (.of k))] :
    (2 ≤ genus (X ↘ Spec (.of k)) → ∀ D : SheafDerivation k X, D = 0) ∧
    (genus (X ↘ Spec (.of k)) = 1 → ∀ D : SheafDerivation k X, D ≠ 0 →
      ∀ (x : X) (hx : IsClosed ({x} : Set X)), ¬ D.Fixes x hx) ∧
    (genus (X ↘ Spec (.of k)) = 0 → ∀ D : SheafDerivation k X, D ≠ 0 →
      {x : X | ∃ hx : IsClosed ({x} : Set X), D.Fixes x hx}.encard ≤ 2)
```

## Tag 0E68, a lemma

[Tag 0E68](https://stacks.math.columbia.edu/tag/0E68) in the Stacks Project.

**`Stacks.Curves.NodalVectorFields.range_branchPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/NodalVectorFieldsEquivalence.lean, line 619](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/NodalVectorFieldsEquivalence.lean#L619).

> **Stacks Project, Tag 0E68.** Let `k` be an algebraically closed field, let `X` be a proper
> one-dimensional `k`-scheme with at worst nodal singularities, let `ν : X^ν ⟶ X` be its
> normalization and let `S ⊆ X^ν` be the set of points where `ν` is not an isomorphism: the points
> `y` such that `ν` restricts to an isomorphism over no open neighbourhood of `ν(y)`. Then
> ```
> Der_k(𝒪_X, 𝒪_X) = {D' ∈ Der_k(𝒪_{X^ν}, 𝒪_{X^ν}) | D' fixes every x^ν ∈ S},
> ```
> the equality being read through the injection `ν^♯` of `𝒪_X` into `ν_* 𝒪_{X^ν}`. The first
> clause says that every vector field `D` on `X` has a unique extension `D'` to `X^ν`, that is a
> vector field with `D' (ν^♯ s) = ν^♯ (D s)` for every local section `s`, and that `D'` fixes every
> point of `S`; the second says that every vector field on `X^ν` fixing every point of `S` is the
> extension of a unique vector field on `X`. "Fixes" is the notion of Section 53.26,
> `Stacks.Curves.SheafDerivationOf.Fixes`: the point is closed and its ideal sheaf is carried into
> itself.
>
> `S` is exactly the set of points above the nodes of `X`
> (`Stacks.Curves.not_exists_isIso_normalization_restrict_iff`): away from the nodes `X` is smooth,
> hence normal, and `ν` is an isomorphism over every normal open; over no neighbourhood of a node
> is it one, because the local ring at a node is not a normal domain. The points of `S` are closed
> (`Stacks.Curves.isClosed_singleton_of_isNode`).
>
> The normalization is formed with the finiteness of irreducible components of quasi-compact opens
> that every scheme locally of finite type over a field enjoys
> (`AlgebraicGeometry.finite_irreducibleComponents_of_locallyOfFiniteType`). The source also
> assumes `X` connected; the statement holds without it. The proof derives from properness and
> nodality what `Stacks.Curves.derivations_eq_normalization_derivations_fixing_nodes` needs: `X`
> is reduced (`Stacks.Curves.isReduced_of_hasAtWorstNodalSingularities`) and, being separated over
> the affine scheme `Spec k`, has affine diagonal. That lemma states the fixing condition on the
> stalks of `ν_* 𝒪_{X^ν}` at the nodes, and the two are exchanged by
> `Stacks.Curves.fixes_of_forall_fixes_stalkDerivation` and
> `Stacks.Curves.forall_fixes_stalkDerivation_of_forall_fixes`, `ν` being finite
> (`AlgebraicGeometry.isFinite_normalizationOverField`).

```lean
theorem NodalVectorFields.range_branchPair (hdim : topologicalKrullDim X = 1)
    (hnodal : HasAtWorstNodalSingularities k X) :
    (∀ D : SheafDerivationOf (X ↘ Spec (.of k)),
        ∃! D' : SheafDerivationOf (Scheme.normalization X
            (finite_irreducibleComponents_of_locallyOfFiniteType k (X ↘ Spec (.of k))) ≫
              (X ↘ Spec (.of k))),
          (∀ (U : X.Opens) (s : Γ(X, U)),
              D'.onSections ((Scheme.normalization X
                  (finite_irreducibleComponents_of_locallyOfFiniteType k
                    (X ↘ Spec (.of k)))).app U |>.hom s) =
                ((Scheme.normalization X
                  (finite_irreducibleComponents_of_locallyOfFiniteType k
                    (X ↘ Spec (.of k)))).app U).hom (D.onSections s)) ∧
            ∀ y : Scheme.normalizationScheme X
                (finite_irreducibleComponents_of_locallyOfFiniteType k (X ↘ Spec (.of k))),
              (¬ ∃ U : X.Opens,
                (Scheme.normalization X
                  (finite_irreducibleComponents_of_locallyOfFiniteType k
                    (X ↘ Spec (.of k)))).base y ∈ U ∧
                IsIso (Scheme.normalization X
                  (finite_irreducibleComponents_of_locallyOfFiniteType k
                    (X ↘ Spec (.of k))) ∣_ U)) →
              ∃ hy : IsClosed ({y} : Set _), D'.Fixes y hy) ∧
      ∀ D' : SheafDerivationOf (Scheme.normalization X
          (finite_irreducibleComponents_of_locallyOfFiniteType k (X ↘ Spec (.of k))) ≫
            (X ↘ Spec (.of k))),
        (∀ y : Scheme.normalizationScheme X
            (finite_irreducibleComponents_of_locallyOfFiniteType k (X ↘ Spec (.of k))),
          (¬ ∃ U : X.Opens,
            (Scheme.normalization X
              (finite_irreducibleComponents_of_locallyOfFiniteType k
                (X ↘ Spec (.of k)))).base y ∈ U ∧
            IsIso (Scheme.normalization X
              (finite_irreducibleComponents_of_locallyOfFiniteType k
                (X ↘ Spec (.of k))) ∣_ U)) →
          ∃ hy : IsClosed ({y} : Set _), D'.Fixes y hy) →
          ∃! D : SheafDerivationOf (X ↘ Spec (.of k)), ∀ (U : X.Opens) (s : Γ(X, U)),
            D'.onSections ((Scheme.normalization X
                (finite_irreducibleComponents_of_locallyOfFiniteType k
                  (X ↘ Spec (.of k)))).app U |>.hom s) =
              ((Scheme.normalization X
                (finite_irreducibleComponents_of_locallyOfFiniteType k
                  (X ↘ Spec (.of k)))).app U).hom (D.onSections s)
```

## Tag 0E69, a lemma

[Tag 0E69](https://stacks.math.columbia.edu/tag/0E69) in the Stacks Project.

**`Stacks.Curves.SheafDerivation.eq_zero_of_hasAtWorstNodalSingularities`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VectorFieldsGenus.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/VectorFieldsGenus.lean#L94).

> **[Stacks, Tag 0E69]**: let `X` be an at-worst-nodal, proper, connected, one-dimensional
> scheme over an algebraically closed field `k`, of genus at least two, with no rational tails and
> no rational bridges. Then `Der_k(𝒪_X, 𝒪_X) = 0`.

```lean
theorem SheafDerivation.eq_zero_of_hasAtWorstNodalSingularities (k : Type u) [Field k]
    [IsAlgClosed k] (X : Scheme.{u}) [X.Over (Spec (.of k))] [IsProper (X ↘ Spec (.of k))]
    [ConnectedSpace X] (hdim : topologicalKrullDim X = 1)
    (hnodal : HasAtWorstNodalSingularities k X) (hg : 2 ≤ genus (X ↘ Spec (.of k)))
    (htail : ∀ C : X.IdealSheafData, ¬ IsRationalTail k X C)
    (hbridge : ∀ C : X.IdealSheafData, ¬ IsRationalBridge k X C) (D : SheafDerivation k X) :
    D = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.26, Tag 0E66](https://stacks.math.columbia.edu/tag/0E66)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
