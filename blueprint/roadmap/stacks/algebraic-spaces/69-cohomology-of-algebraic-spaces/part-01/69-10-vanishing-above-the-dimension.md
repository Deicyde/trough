---
declaration: section
origin: cited
lean: AlgebraicGeometry.subsingleton_smallEtaleCohomology_quasicoherent_of_topologicalKrullDim_le, AlgebraicGeometry.Space.isZero_rightDerived_globalSectionsFunctor_of_dimension_le, AlgebraicGeometry.Space.surjective_cohomologyRestriction_of_dimension_le, AlgebraicGeometry.Space.isZero_rightDerived_globalSectionsAbRestrictionKer_of_dimension_le
statement: formalized
proof: formalized
---

# 69.10 Vanishing above the dimension

Section 69.10 of the Stacks Project, [Tag 0A4Q](https://stacks.math.columbia.edu/tag/0A4Q). 1 tag here is carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A4R, a lemma

[Tag 0A4R](https://stacks.math.columbia.edu/tag/0A4R) in the Stacks Project.

**`AlgebraicGeometry.subsingleton_smallEtaleCohomology_quasicoherent_of_topologicalKrullDim_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/VanishingAboveTheDimension.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/VanishingAboveTheDimension.lean#L261). The attribute's comment: “clause (1) for a scheme: for a quasi-compact quasi-separated scheme X of dimension at most d and a quasi-coherent module F, the small étale cohomology of the associated abelian sheaf Fᵃ vanishes above degree d”.

> **Stacks 0A4R, clause (1), for a quasi-compact quasi-separated scheme.** Let `X` be a
> quasi-compact quasi-separated scheme whose dimension — the Krull dimension of its underlying
> topological space — is at most `d`, and let `F` be a quasi-coherent `𝒪_X`-module. Then the
> small étale cohomology of the associated abelian sheaf `Fᵃ` of Stacks 03DU vanishes in every
> degree `q > d`.
>
> The proof is the base case of the source's induction. The space of `X` is spectral by
> Stacks 094L, so clause (1) of Stacks 0A3G makes the Zariski cohomology of the abelian sheaf
> underlying `F` vanish above `d`
> (`AlgebraicGeometry.subsingleton_zariskiCohomology_of_topologicalKrullDim_le`); Stacks 03P2 for
> `𝒞 = S_étale` — which is the comparison the source cites as Stacks 03DW, available here in all
> degrees — transports that vanishing to the small étale site.
>
> Quasi-coherence cannot be dropped: on `X = Spec ℝ`, which is zero-dimensional, the constant
> abelian sheaf `ℤ/2` on `X_étale` has `H^q(X_étale, ℤ/2) = ℤ/2` for every `q > 0`.

```lean
theorem subsingleton_smallEtaleCohomology_quasicoherent_of_topologicalKrullDim_le
    (X : Scheme.{u}) [CompactSpace X] [QuasiSeparatedSpace X] (F : X.Modules)
    [F.IsQuasicoherent] (d q : ℕ) (hdim : topologicalKrullDim X ≤ (d : WithBot ℕ∞))
    (hq : d < q) :
    Subsingleton (Sheaf.H' (smallEtaleAssociatedSheaf X F) q ((opensToEtale X).obj ⊤))
```

**`AlgebraicGeometry.Space.isZero_rightDerived_globalSectionsFunctor_of_dimension_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/VanishingAboveTheDimensionQcqs.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/VanishingAboveTheDimensionQcqs.lean#L120). The attribute's comment: “part (1)”.

> **Stacks 0A4R, clause (1).**  Let `S` be a scheme and `X` a quasi-compact quasi-separated
> algebraic space over `S` with `dim X ≤ d`, and let `F` be a quasi-coherent `𝒪_X`-module.  Then
> `Hᑫ(X, F) = 0` for every `q > d`.
>
> The dimension bound `d` ranges over `WithBot ℕ∞`, where the dimension of an algebraic space
> lives, so it covers every integer of the source: for `d = ⊤` there is nothing to prove, and a
> negative `d` (in particular `d = ⊥`) forces `X` to have no points, so that every module on `X`
> is zero.  For a natural number `d` this is the induction of Stacks 08GP along elementary
> distinguished squares,
> `AlgebraicGeometry.Space.isZero_rightDerived_globalSectionsAb_of_dimension_le`; the
> cohomology is that of the module over the global functions, and it vanishes exactly when the
> underlying abelian group does.

```lean
theorem isZero_rightDerived_globalSectionsFunctor_of_dimension_le (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (X : AlgebraicSpaces B S hS)
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1) (d : WithBot ℕ∞)
    (hdim : dimension B S hS X.1 X.2 ≤ d) (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : F.IsQuasicoherentOnSite) (q : ℕ) (hq : d < q) :
    IsZero (((globalSectionsFunctor.{u + 1, u, u, u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallEtaleRingedSite B S hS X.1 X.2).O)).rightDerived q).obj F)
```

**`AlgebraicGeometry.Space.surjective_cohomologyRestriction_of_dimension_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/VanishingAboveTheDimensionQcqs.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/VanishingAboveTheDimensionQcqs.lean#L162). The attribute's comment: “part (2)”.

> **Stacks 0A4R, clause (2).**  Let `S` be a scheme and `X` a quasi-compact quasi-separated
> algebraic space over `S` with `dim X ≤ d`, and let `F` be a quasi-coherent `𝒪_X`-module.  Then
> the restriction map `H^d(X, F) ⟶ H^d(U, F|_U)` is surjective for every quasi-compact open
> subspace `U` of `X`.
>
> The open subspace is given by an open immersion `j : U ⟶ X` from a quasi-compact algebraic
> space, which covers every quasi-compact open subspace (through its inclusion) and every space
> isomorphic to one; the restriction map is
> `AlgebraicGeometry.Space.cohomologyRestriction`, the right derived map of
> `Γ(X, -) ⟶ Γ(U, (-)|_U)`.  The bound `d` is a natural number: for a negative integer `d` the
> source's statement is about `H^d`, which is zero.  The proof is
> `AlgebraicGeometry.Space.epi_rightDerived_globalSectionsAbRestriction_of_dimension_le`, the
> induction of Stacks 08GP with the Mayer–Vietoris sequence of Stacks 08GW in place of the
> excision of Stacks 0A4P.

```lean
theorem surjective_cohomologyRestriction_of_dimension_le (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (X : AlgebraicSpaces B S hS)
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1) (d : ℕ)
    (hdim : dimension B S hS X.1 X.2 ≤ d) {U : AlgebraicSpaces B S hS} (j : U ⟶ X)
    (hj : IsOpenImmersion B S hS j.hom) (hUqc : IsQuasiCompactSpace B S hS U.1)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite) :
    Function.Surjective
      (cohomologyRestriction B S hS j (isEtale_of_isOpenImmersion B S hS hj) F d)
```

**`AlgebraicGeometry.Space.isZero_rightDerived_globalSectionsAbRestrictionKer_of_dimension_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/VanishingAboveTheDimensionQcqs.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/VanishingAboveTheDimensionQcqs.lean#L193). The attribute's comment: “part (3)”.

> **Stacks 0A4R, clause (3).**  Let `S` be a scheme and `X` a quasi-compact quasi-separated
> algebraic space over `S` with `dim X ≤ d`, and let `F` be a quasi-coherent `𝒪_X`-module.  Then
> `H^q_Z(X, F) = 0` for every `q > d` and every closed subspace `Z ⊆ X` whose complement is
> quasi-compact.
>
> The complement `U = X ∖ Z` is given by an open immersion `j : U ⟶ X` from a quasi-compact
> algebraic space, and `H^q_Z(X, -)` is the `q`-th right derived functor of
> `Γ_Z(X, -) = Ker(Γ(X, -) ⟶ Γ(U, (-)|_U))`,
> `AlgebraicGeometry.Space.globalSectionsAbRestrictionKer`; this depends on `Z` only through its
> open complement, which is how the source's `H^q_Z` depends on `Z`.  As in clause (1) the bound
> `d` ranges over `WithBot ℕ∞`; a negative `d` forces `X` to have no points.  For a natural number
> `d` the proof is the source's formal argument: in the long exact sequence of the pair
> `H^{q-1}(X, F) ⟶ H^{q-1}(U, F) ⟶ H^q_Z(X, F) ⟶ H^q(X, F)` the last group vanishes by
> clause (1), and the first map is onto, by clause (2) when `q - 1 = d` and because its target
> vanishes by clause (1) on the quasi-compact quasi-separated space `U` when `q - 1 > d`.

```lean
theorem isZero_rightDerived_globalSectionsAbRestrictionKer_of_dimension_le (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (X : AlgebraicSpaces B S hS)
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1) (d : WithBot ℕ∞)
    (hdim : dimension B S hS X.1 X.2 ≤ d) {U : AlgebraicSpaces B S hS} (j : U ⟶ X)
    (hj : IsOpenImmersion B S hS j.hom) (hUqc : IsQuasiCompactSpace B S hS U.1)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite) (q : ℕ) (hq : d < q) :
    IsZero (((globalSectionsAbRestrictionKer B S hS j
      (isEtale_of_isOpenImmersion B S hS hj)).rightDerived q).obj F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.10, Tag 0A4Q](https://stacks.math.columbia.edu/tag/0A4Q)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
