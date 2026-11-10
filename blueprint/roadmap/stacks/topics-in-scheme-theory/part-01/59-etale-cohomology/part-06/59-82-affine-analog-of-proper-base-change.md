---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.exists_mono_comp_etaleAbelianInverseImage_eq_zero_of_torsion, Stacks.EtaleCohomology.isIso_globalSectionsSmallEtaleInverseImageComparison_of_zariskiBijective, exists_isClosed_partition, Stacks.bijective_globalSectionsRestriction_of_isConnected_inter_closure, Stacks.EtaleCohomology.isIso_globalSectionsComparison_quotient_of_henselianPair, Stacks.EtaleCohomology.etaleCohomologyRestrictionMap_bijective_of_henselianPair, Stacks.EtaleCohomology.subsingleton_H_closed_of_injective_of_affine_cover
statement: formalized
proof: formalized
---

# 59.82 Affine analog of proper base change

Section 59.82 of the Stacks Project, [Tag 09Z8](https://stacks.math.columbia.edu/tag/09Z8). 7 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09ZE, a lemma

[Tag 09ZE](https://stacks.math.columbia.edu/tag/09ZE) in the Stacks Project.

**`Stacks.EtaleCohomology.exists_mono_comp_etaleAbelianInverseImage_eq_zero_of_torsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AffineAnalogProper/TorsionEffacement.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AffineAnalogProper/TorsionEffacement.lean#L241).

> **Stacks 09ZE.** Let `X` be an affine scheme, `F` a torsion abelian sheaf on `X_étale`,
> `Z ⊂ X` a closed subscheme (`i : Z ⟶ X` a closed immersion) and `ξ ∈ H^q_ét(Z, F|_Z)` for some
> `q > 0`. Then there exists an injective map `F ⟶ F'` of torsion abelian sheaves on `X_étale` such
> that the image of `ξ` in `H^q_ét(Z, F'|_Z)` is zero.
>
> Restriction to `Z` is the inverse image `etaleAbelianInverseImage i`, and the image of `ξ` is its
> composite with the degree-zero class of `i⁻¹(F ⟶ F')`. Torsion is the local condition of
> Stacks 0DD7, `Stacks.Torsion.torsionSheafProperty`.

```lean
theorem exists_mono_comp_etaleAbelianInverseImage_eq_zero_of_torsion
    {X Z : Scheme.{u}} [IsAffine X] (i : Z ⟶ X) [IsClosedImmersion i]
    (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})
    (hF : Stacks.Torsion.torsionSheafProperty X.smallEtaleTopology F) (q : ℕ) (hq : 0 < q)
    (ξ : Sheaf.H.{u + 1} ((etaleAbelianInverseImage.{u, 0} i).obj F) q) :
    ∃ (F' : Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1}) (φ : F ⟶ F'), Mono φ ∧
      Stacks.Torsion.torsionSheafProperty X.smallEtaleTopology F' ∧
        ξ.comp (Ext.mk₀ ((etaleAbelianInverseImage.{u, 0} i).map φ)) (add_zero q) = 0
```

## Tag 09ZF, a lemma

[Tag 09ZF](https://stacks.math.columbia.edu/tag/09ZF) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_globalSectionsSmallEtaleInverseImageComparison_of_zariskiBijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GlobalSectionsClosed/FiniteSurjectiveDescent.lean, line 3312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GlobalSectionsClosed/FiniteSurjectiveDescent.lean#L3312). The attribute's comment: “the conclusion `Γ(X, ℱ) = Γ(Z, i⁻¹_{small}ℱ)` for every sheaf of sets on the small étale site of `X`, under the source's own hypotheses: `X` quasi-compact and quasi-separated, `i` a closed immersion, and the two Zariski hypotheses (1) and (2) of the tag”.

> **[Stacks, Tag 09ZF]** (Gabber).  Let `X` be a quasi-compact quasi-separated scheme and
> `i : Z ⟶ X` a closed immersion such that
>
> 1. for every sheaf of sets `ℱ` on the Zariski site of `X` the restriction
>    `Γ(X, ℱ) ⟶ Γ(Z, i⁻¹ℱ)` is bijective, and
> 2. the same holds for the base change `Z ×_X X' ⟶ X'` along every finite morphism `X' ⟶ X`.
>
> Then `Γ(X, ℱ) = Γ(Z, i⁻¹_{small}ℱ)` for every sheaf of sets `ℱ` on the small étale site of `X`:
> the canonical comparison
> `Stacks.EtaleCohomology.globalSectionsSmallEtaleInverseImageComparison` is an isomorphism.
>
> Injectivity uses only hypothesis (1):  a global section of `i⁻¹ℱ` is, near each point of `Z`,
> pulled back from a section of `ℱ` over an object of the small étale site of `X` whose open image
> is forced by (1) to be all of `X`.  Surjectivity is where (2) enters.  A global section `t` of
> `i⁻¹ℱ` is, on a covering family, pulled back from sections of `ℱ` over objects `W j` of the small
> étale site whose images cover `X`;  each `W j` is shrunk so that `V j ⟶ W j ×_X Z` is surjective;
> [Stacks, Tag 09Z0] produces a finite surjective `X' ⟶ X` factoring Zariski-locally through the
> family, so that over `X'` the pulled-back section lies in the Zariski subsheaf and (2) produces a
> section over `X'`;  and that section descends to `X` by the equalizer presentation of
> [Stacks, Tag 09Z3],
> `Stacks.EtaleCohomology.globalSectionsPullback_isEqualizer_of_isFinite_surjective`.
>
> Hypotheses (1) and (2) are asked only of those Zariski sheaves of sets whose values lie in the
> universe of the schemes themselves — `Stacks.EtaleCohomology.zariskiGlobalSectionsMapAt` at
> `Type u` — while the conclusion stays universe-polymorphic in the coefficients of the étale
> sheaf.  That is all the proof uses:  (1) is applied to the sheafification of a representable, and
> both (1) and (2) to the small model `Stacks.EtaleCohomology.smallSheafModel` of the subsheaf
> generated by a `u`-small family of local sections.  Both have `u`-small values, so the
> hypotheses are weaker than the source's, which quantifies over every sheaf of sets.

```lean
public theorem isIso_globalSectionsSmallEtaleInverseImageComparison_of_zariskiBijective
    {X Z : Scheme.{u}} (i : Z ⟶ X) [IsClosedImmersion i]
    [CompactSpace X] [QuasiSeparatedSpace X]
    (hZar : ∀ F : Sheaf (Opens.grothendieckTopology X.carrier)
      (Type u),
      Function.Bijective (zariskiGlobalSectionsMapAt i F))
    (hFinite : ∀ {Y : Scheme.{u}} (f : Y ⟶ X) [IsFinite f],
      ∀ F : Sheaf (Opens.grothendieckTopology Y.carrier)
        (Type u),
        Function.Bijective
          (zariskiGlobalSectionsMapAt (pullback.fst f i) F)) :
    IsIso (globalSectionsSmallEtaleInverseImageComparison.{u, v} i).val
```

## Tag 0CAM, a lemma

[Tag 0CAM](https://stacks.math.columbia.edu/tag/0CAM) in the Stacks Project.

**`exists_isClosed_partition`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AffineAnalogProper/SpectralPartition.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AffineAnalogProper/SpectralPartition.lean#L133).

> A partition of a closed subset `Z` into two relatively closed pieces extends to a
> partition of the ambient spectral space into two closed pieces, provided `Z` meets the
> closure of each point in a connected set.

```lean
public lemma exists_isClosed_partition
    {X : Type*} [TopologicalSpace X] [SpectralSpace X]
    {Z Z₁ Z₂ : Set X} (hZ : IsClosed Z)
    (hconnected : ∀ x : X, IsConnected (Z ∩ closure ({x} : Set X)))
    (hZ₁ : IsClosed ((Subtype.val : Z → X) ⁻¹' Z₁))
    (hZ₂ : IsClosed ((Subtype.val : Z → X) ⁻¹' Z₂))
    (hunion : Z₁ ∪ Z₂ = Z) (hdisjoint : Disjoint Z₁ Z₂) :
    ∃ X₁ X₂ : Set X,
      IsClosed X₁ ∧ IsClosed X₂ ∧ X₁ ∪ X₂ = univ ∧ Disjoint X₁ X₂ ∧
        Z₁ = Z ∩ X₁ ∧ Z₂ = Z ∩ X₂
```

## Tag 09ZG, a lemma

[Tag 09ZG](https://stacks.math.columbia.edu/tag/09ZG) in the Stacks Project.

**`Stacks.bijective_globalSectionsRestriction_of_isConnected_inter_closure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Spectral/ClosedSubsetGlobalSections.lean, line 1359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Spectral/ClosedSubsetGlobalSections.lean#L1359).

> **Stacks Project, Tag 09ZG.** Let `Z` be a closed subset of a spectral space `X` meeting the
> closure of every point of `X` in a connected set. Then restriction to `Z` is a bijection on global
> sections of every sheaf of sets on `X`.

```lean
theorem bijective_globalSectionsRestriction_of_isConnected_inter_closure
    {X : Type u} [TopologicalSpace X] [SpectralSpace X]
    (Z : Set X) (hZ : IsClosed Z)
    (hconn : ∀ x : X, IsConnected (Z ∩ closure ({x} : Set X)))
    (F : TopCat.Sheaf (Type u) (TopCat.of X)) :
    Function.Bijective (globalSectionsRestriction Z F)
```

## Tag 09ZH, a lemma

[Tag 09ZH](https://stacks.math.columbia.edu/tag/09ZH) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_globalSectionsComparison_quotient_of_henselianPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AffineAnalogProper/HenselianPairEtaleSections.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AffineAnalogProper/HenselianPairEtaleSections.lean#L66). The attribute's comment: “Γ(X, ℱ) = Γ(Z, ℱ|\_Z) for every sheaf of sets ℱ on the small étale site of X = Spec A, where (A, I) is a henselian pair and Z = Spec (A/I): the canonical comparison of global sections along Z ⟶ X is an isomorphism. The ring A is not assumed local”. References: SGA 4 XII (6.13), “special case”.

> **[Stacks, Tag 09ZH].** Let `(A, I)` be a henselian pair, let `X = Spec A` and let
> `Z = Spec (A ⧸ I)`. Then `Γ(X, ℱ) = Γ(Z, ℱ|_Z)` for every sheaf of sets `ℱ` on the small étale
> site of `X`: the canonical comparison of global sections along `Z ⟶ X` is an isomorphism.
>
> There is no hypothesis that `A` be local. The two Zariski inputs are hypotheses (1) and (2) of
> [Stacks, Tag 09ZF] for `Z ⟶ X`, and they hold at an arbitrary henselian pair:
> `Stacks.EtaleCohomology.bijective_zariskiGlobalSectionsMapAt_quotient_of_henselianPair` is (1),
> proved from [Stacks, Tag 09ZG] because `Spec A` is a spectral space in which `V(I)` meets the
> closure of every point in a connected set, and
> `Stacks.EtaleCohomology.bijective_zariskiGlobalSectionsMapAt_pullback_of_henselianPair` is (2),
> because a scheme finite over `Spec A` is the spectrum of an integral `A`-algebra `B` and
> `(B, IB)` is again a henselian pair.

```lean
public theorem isIso_globalSectionsComparison_quotient_of_henselianPair
    (h : HenselianPair A I) :
    IsIso (globalSectionsSmallEtaleInverseImageComparison.{u, v}
      (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I)))).val
```

## Tag 09ZI, a theorem

[Tag 09ZI](https://stacks.math.columbia.edu/tag/09ZI) in the Stacks Project.

**`Stacks.EtaleCohomology.etaleCohomologyRestrictionMap_bijective_of_henselianPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AffineAnalogProper/Gabber/Theorem.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AffineAnalogProper/Gabber/Theorem.lean#L189). The attribute's comment: “Gabber's theorem: for a henselian pair (A, I), every torsion abelian sheaf F on the small étale site of X = Spec A and every q, restriction H^q(X, F) → H^q(Z, F|\_Z) to Z = Spec (A/I) is bijective”. References: SGA 4 XII (6.13), “more general”.

> **Gabber's theorem.** Let `(A, I)` be a henselian pair, `X = Spec A` and
> `Z = Spec (A ⧸ I)`. For every torsion abelian sheaf `F` on `X_étale` and every `q ≥ 0` the
> restriction map `H^q_étale(X, F) → H^q_étale(Z, F|_Z)` is bijective.
>
> Torsion is the local condition of Stacks 0DD7, `Stacks.Torsion.torsionSheafProperty`: every
> section is annihilated by a positive integer after restriction along a covering. Cohomology is
> Mathlib's `CategoryTheory.Sheaf.H`, the restricted sheaf is the étale inverse image along
> `Spec (A ⧸ I) ⟶ Spec A`, and the map is
> `Stacks.EtaleCohomology.etaleCohomologyRestrictionMap`.

```lean
theorem etaleCohomologyRestrictionMap_bijective_of_henselianPair
    (F : Sheaf (Spec (.of A)).smallEtaleTopology AddCommGrpCat.{u + 1})
    (hF : Stacks.Torsion.torsionSheafProperty (Spec (.of A)).smallEtaleTopology F) (q : ℕ) :
    Function.Bijective (etaleCohomologyRestrictionMap.{u, 0, u + 1}
      (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I))) F q)
```

## Tag 0A51, a lemma

[Tag 0A51](https://stacks.math.columbia.edu/tag/0A51) in the Stacks Project.

**`Stacks.EtaleCohomology.subsingleton_H_closed_of_injective_of_affine_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AffineAnalogProper/InjectiveClosedVanishing.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AffineAnalogProper/InjectiveClosedVanishing.lean#L200). The attribute's comment: “X with affine diagonal covered by n + 1 affine opens, Z a closed subscheme, 𝒜 a torsion sheaf of rings on X\_et, ℐ an injective 𝒜-module: H^q\_et(Z, ℐ|\_Z) = 0 for q > n”.

> **[Stacks, Tag 0A51].** Let `X` be a scheme with affine diagonal which can be covered by
> `n + 1` affine opens, let `i : Z ⟶ X` be a closed immersion, let `𝒜` be a torsion sheaf of rings
> on `X_étale` and let `ℐ` be an injective sheaf of `𝒜`-modules on `X_étale`. Then
> `H^q_étale(Z, ℐ|_Z) = 0` for every `q > n`.
>
> Affine diagonal is `IsAffineHom (pullback.diagonal (terminal.from X))`, the diagonal of `X` over
> `Spec ℤ`. The sheaf `𝒜` is torsion in the sense of Stacks 0DD7: every local section of its
> underlying abelian sheaf is locally annihilated by a positive integer. The restriction `ℐ|_Z` is
> the étale inverse image along `i` of the underlying abelian sheaf of `ℐ`, and `H^q_étale` is its
> étale cohomology `CategoryTheory.Sheaf.H`.

```lean
theorem subsingleton_H_closed_of_injective_of_affine_cover {X Z : Scheme.{u}}
    [IsAffineHom (pullback.diagonal (terminal.from X))] (n : ℕ)
    (hX : ∃ U : Fin (n + 1) → X.Opens, (∀ k, IsAffineOpen (U k)) ∧ ⨆ k, U k = ⊤)
    (i : Z ⟶ X) [IsClosedImmersion i] (𝒜 : Sheaf X.smallEtaleTopology RingCat.{u + 1})
    (h𝒜 : Stacks.Torsion.torsionSheafProperty X.smallEtaleTopology
      ((sheafCompose X.smallEtaleTopology (forget₂ RingCat AddCommGrpCat)).obj 𝒜))
    (ℐ : SheafOfModules.{u + 1} 𝒜) [Injective ℐ] (q : ℕ) (hq : n < q) :
    Subsingleton (Sheaf.H.{u + 1} ((etaleAbelianInverseImage.{u, 0} i).obj
      ((SheafOfModules.toSheaf 𝒜).obj ℐ)) q)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.82, Tag 09Z8](https://stacks.math.columbia.edu/tag/09Z8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
