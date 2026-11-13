---
declaration: section
origin: cited
lean: AlgebraicGeometry.kummerSequence_shortExact_bigEtale, AlgebraicGeometry.kummerSequence_shortExact_smallEtale, AlgebraicGeometry.kummerSequence_shortExact_fppf, AlgebraicGeometry.kummerSequence_shortExact_syntomic, AlgebraicGeometry.pairIso_torsor, AlgebraicGeometry.scalarTranslate_pairIso, AlgebraicGeometry.pairIso_unitPair_iff, AlgebraicGeometry.exists_trivializedPower_sheaf_iff
statement: formalized
proof: formalized
---

# 59.28 Kummer theory

Section 59.28 of the Stacks Project, [Tag 03PK](https://stacks.math.columbia.edu/tag/03PK). 4 tags here are carried by 32 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03PL, a lemma

[Tag 03PL](https://stacks.math.columbia.edu/tag/03PL) in the Stacks Project.

**`AlgebraicGeometry.kummerSequence_shortExact_bigEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Etale.lean, line 526](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Etale.lean#L526). The attribute's comment: “big étale site”. References: SGA 1 XI (6.1), “exact sequence (big)”; SGA 4 XVIII (1.6.1), “m = O\_X (Y empty)”; SGA 4 IX (3.2), “big étale site”; SGA 4½ Arcata (2.2.5), “more general”; SGA 4½ Sommes trig (4.7), “special case”; SGA 7 IX (14.3), “special case”.

> The Kummer sequence of abelian sheaves on the big étale site is short exact
> when the exponent is invertible on the base.

```lean
public theorem kummerSequence_shortExact_bigEtale
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (n : ℕ) (hn : IsUnit (n : Scheme.Γ.obj (Opposite.op S))) :
    (kummerSequence (BigEtaleOver.topology B S hS)
      (BigEtaleOver.toScheme B S hS)
      (unitsPresheaf_isSheaf_bigEtale B S hS) n).ShortExact
```

**`AlgebraicGeometry.kummerSequence_shortExact_smallEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Etale.lean, line 547](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Etale.lean#L547). The attribute's comment: “small étale site”. References: SGA 4 IX (3.2); SGA 1 XI (6.1), “exact sequence (small)”; SGA 4½ Arcata (2.2.5); SGA 4½ Sommes trig (4.7), “special case”; SGA 7 IX (14.3), “special case”.

> The Kummer sequence of abelian sheaves on the small étale site is short exact
> when the exponent is invertible on the base.

```lean
public theorem kummerSequence_shortExact_smallEtale
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (n : ℕ) (hn : IsUnit (n : Scheme.Γ.obj (Opposite.op S))) :
    (kummerSequence (SmallEtale.topology B S hS)
      (SmallEtale.toScheme B S hS)
      (unitsPresheaf_isSheaf_smallEtale B S hS) n).ShortExact
```

## Tag 040N, a lemma

[Tag 040N](https://stacks.math.columbia.edu/tag/040N) in the Stacks Project.

**`AlgebraicGeometry.kummerSequence_shortExact_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/FppfAndSyntomic.lean, line 504](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/FppfAndSyntomic.lean#L504). The attribute's comment: “fppf Kummer sequence”. References: SGA 7 IX (14.3), “special case”; SGA 7 IX (9.4.3).

> **Stacks Project, Tag 040N (fppf).** The canonical Kummer complex of
> abelian sheaves on the big fppf site is short exact.

```lean
public theorem kummerSequence_shortExact_fppf
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (n : ℕ) (hn : 0 < n) :
    (kummerSequence (BigFppfOver.topology B S hS)
      (BigFppfOver.toScheme B S hS)
      (unitsPresheaf_isSheaf_fppf B S hS) n).ShortExact
```

**`AlgebraicGeometry.kummerSequence_shortExact_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/FppfAndSyntomic.lean, line 527](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/FppfAndSyntomic.lean#L527). The attribute's comment: “syntomic Kummer sequence”. References: SGA 7 IX (14.3), “special case”.

> **Stacks Project, Tag 040N (syntomic).** The canonical Kummer complex of
> abelian sheaves on the big syntomic site is short exact.

```lean
public theorem kummerSequence_shortExact_syntomic
    (B : BigSyntomicSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (n : ℕ) (hn : 0 < n) :
    (kummerSequence (BigSyntomicOver.topology B S hS)
      (BigSyntomicOver.toScheme B S hS)
      (unitsPresheaf_isSheaf_syntomic B S hS) n).ShortExact
```

## Tag 040P, an equation

[Tag 040P](https://stacks.math.columbia.edu/tag/040P) in the Stacks Project.

**`AlgebraicGeometry.pairIso_torsor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Basic.lean, line 682](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Basic.lean#L682). The attribute's comment: “every pair isomorphism is uniquely a scalar translate”.

> Once an isomorphism of pairs has been chosen, every other isomorphism is uniquely its scalar
> translate by a global `n`th root of unity.

```lean
public theorem pairIso_torsor (S : Scheme.{u}) (n : ℕ)
    (P Q : TrivializedPower S n) (φ : PairIso P Q) :
    ∀ ψ : PairIso P Q, ∃! a :
      (AlgebraicGeometry.rootsOfUnitySections n).obj (Opposite.op S),
      IsScalarTranslate a φ ψ
```

**`AlgebraicGeometry.scalarTranslate_pairIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Basic.lean, line 719](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Basic.lean#L719). The attribute's comment: “every global root gives a unique pair isomorphism”.

> Every global `n`th root of unity acts on a chosen isomorphism of pairs,
> giving a unique isomorphism whose sheaf map is its specified scalar translate.

```lean
public theorem scalarTranslate_pairIso (S : Scheme.{u}) (n : ℕ)
    (P Q : TrivializedPower S n) (φ : PairIso P Q) :
    ∀ a : (AlgebraicGeometry.rootsOfUnitySections n).obj (Opposite.op S),
      ∃! ψ : PairIso P Q, IsScalarTranslate a φ ψ
```

## Tag 040Q, a lemma

[Tag 040Q](https://stacks.math.columbia.edu/tag/040Q) in the Stacks Project.

**`AlgebraicGeometry.pairIso_unitPair_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Basic.lean, line 835](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Basic.lean#L835). The attribute's comment: “the pair side of the identification for pairs whose invertible sheaf is the structure sheaf: two such pairs are isomorphic exactly when their trivializing units agree modulo nth powers of global units, so the isomorphism classes of such pairs are the global units modulo nth powers; the cohomological side is AlgebraicGeometry.pairIso\_iff\_kummerBoundary\_eq”.

> Two pairs whose invertible sheaf is the structure sheaf are isomorphic exactly when their
> trivializing units differ by the `n`th power of a global unit; so the isomorphism classes of such
> pairs are the global units modulo `n`th powers.

```lean
public theorem pairIso_unitPair_iff (S : Scheme.{u}) (n : ℕ)
    (f g : (Scheme.Γ.obj (Opposite.op S))ˣ) :
    Nonempty (PairIso (unitPair S n f) (unitPair S n g)) ↔
      ∃ u : (Scheme.Γ.obj (Opposite.op S))ˣ, f = u ^ n * g
```

**`AlgebraicGeometry.exists_trivializedPower_sheaf_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Basic.lean, line 871](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Basic.lean#L871). The attribute's comment: “the invertible sheaves occurring in a pair are exactly those whose nth tensor power is trivial, with no restriction to the structure sheaf”.

> An invertible sheaf carries a trivialization of its `n`th tensor power exactly when that
> power is trivial; so the invertible sheaves of pairs are exactly those whose class in the Picard
> group is `n`-torsion.

```lean
public theorem exists_trivializedPower_sheaf_iff (S : Scheme.{u}) (n : ℕ)
    (L : SheafOfModules.{u} (ringSheaf S))
    (hL : IsInvertible S.presheaf (ringSheafCond S) L) :
    (∃ P : TrivializedPower S n, P.sheaf = L) ↔
      Nonempty (tensorPower S.presheaf (ringSheafCond S) L (n : ℤ) ≅
        SheafOfModules.unit (ringSheaf S))
```

**`AlgebraicGeometry.pairIso_iff_trivializationRatio_eq_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Basic.lean, line 1043](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Basic.lean#L1043). The attribute's comment: “the pair side for an arbitrary, possibly nontrivial, invertible sheaf: two pairs with the same invertible sheaf are isomorphic exactly when their trivializations differ by the nth power of a global unit, so the pairs with a given invertible sheaf form one coset of the nth powers in the global units”.

> Two pairs with the same, possibly nontrivial, invertible sheaf are isomorphic exactly when
> their trivializations differ by the `n`th power of a global unit.

```lean
public theorem pairIso_iff_trivializationRatio_eq_pow (S : Scheme.{u}) (n : ℕ)
    (L : SheafOfModules.{u} (ringSheaf S))
    [hL : IsInvertible S.presheaf (ringSheafCond S) L]
    (α β : tensorPower S.presheaf (ringSheafCond S) L (n : ℤ) ≅
      SheafOfModules.unit (ringSheaf S)) :
    Nonempty (PairIso ⟨L, hL, α⟩ ⟨L, hL, β⟩) ↔
      ∃ u : (Scheme.Γ.obj (Opposite.op S))ˣ, trivializationRatio S n α β = u ^ n
```

**`AlgebraicGeometry.exists_pairIso_unitPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Basic.lean, line 1081](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Basic.lean#L1081). The attribute's comment: “every pair whose invertible sheaf is isomorphic to the structure sheaf is isomorphic to a unit pair, so the trivial-invertible-sheaf case is not a restriction to the literal structure sheaf”.

> A pair whose invertible sheaf is isomorphic to the structure sheaf — not only equal to it —
> is isomorphic to the pair given by the structure sheaf and a global unit.

```lean
public theorem exists_pairIso_unitPair (S : Scheme.{u}) (n : ℕ) (P : TrivializedPower S n)
    (e : P.sheaf ≅ SheafOfModules.unit (ringSheaf S)) :
    ∃ f : (Scheme.Γ.obj (Opposite.op S))ˣ, Nonempty (PairIso P (unitPair S n f))
```

**`AlgebraicGeometry.basePairCohomologyClassHom_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Comparison040Q.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Comparison040Q.lean#L84). The attribute's comment: “the comparison homomorphism from the isomorphism classes of pairs to H^1 of the roots of unity is bijective. The group isomorphism the tag asserts is read off from this in AlgebraicGeometry.basePairClassesAddEquivH1, and the three statements of the tag -- etale for n invertible on the base, fppf and syntomic for n positive -- in the three declarations after it”.

> **The comparison homomorphism of Tag 040Q is bijective.**
>
> All six hypotheses of `Stacks.Kummer.bijective_of_comparison` are discharged from the library;
> see the head of this file.

```lean
public theorem basePairCohomologyClassHom_bijective
    (hroot : LocalRoots (BigFppfOver.baseRingedSite B S hS τ) n)
    (hSE : (kummerSequence (BigFppfOver.baseOverTopology B S hS τ)
      (BigFppfOver.toScheme B S hS) (unitsPresheaf_isSheaf_base B S hS τ) n).ShortExact)
    (hT : IsTerminal (C := BigFppfOver B S hS) (Over.mk (𝟙 (B.obj hS)))) :
    Function.Bijective (basePairCohomologyClassHom B S hS τ n hroot)
```

**`AlgebraicGeometry.pairClassesAddEquivH1Etale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Comparison040Q.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Comparison040Q.lean#L158). The attribute's comment: “the etale statement: for n invertible on S, H^1\_etale(S, mu\_n) is the group of pairs (L, alpha) up to isomorphism, as an isomorphism of abelian groups”.

> **Stacks Project, Tag 040Q, the étale statement.**  For `n` invertible on `S`,
> `H¹_étale(S, μ_n)` is the group of pairs `(ℒ, α)` — an invertible `𝒪_S`-module with a
> trivialization of its `n`-th tensor power — up to isomorphism.

```lean
public noncomputable def pairClassesAddEquivH1Etale
    (hn : IsUnit (n : Scheme.Γ.obj (op S))) :
    PairClasses S n ≃+
      Sheaf.H (rootsOfUnitySheaf (BigFppfOver.baseOverTopology B S hS .etale)
        (BigFppfOver.toScheme B S hS) (unitsPresheaf_isSheaf_base B S hS .etale) n) 1
```

**`AlgebraicGeometry.pairClassesAddEquivH1Fppf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Comparison040Q.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Comparison040Q.lean#L172). The attribute's comment: “the fppf statement: for every positive n, with no invertibility hypothesis, H^1\_fppf(S, mu\_n) is the group of pairs (L, alpha) up to isomorphism, as an isomorphism of abelian groups”.

> **Stacks Project, Tag 040Q, the fppf statement.**  For every positive `n`, with no
> invertibility hypothesis, `H¹_fppf(S, μ_n)` is the group of pairs `(ℒ, α)` up to
> isomorphism.

```lean
public noncomputable def pairClassesAddEquivH1Fppf (hn : 0 < n) :
    PairClasses S n ≃+
      Sheaf.H (rootsOfUnitySheaf (BigFppfOver.baseOverTopology B S hS .fppf)
        (BigFppfOver.toScheme B S hS) (unitsPresheaf_isSheaf_base B S hS .fppf) n) 1
```

**`AlgebraicGeometry.pairClassesAddEquivH1Syntomic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Comparison040Q.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/Comparison040Q.lean#L184). The attribute's comment: “the syntomic statement: for every positive n, with no invertibility hypothesis, H^1\_syntomic(S, mu\_n) is the group of pairs (L, alpha) up to isomorphism, as an isomorphism of abelian groups”.

> **Stacks Project, Tag 040Q, the syntomic statement.**  The same with fppf replaced by
> syntomic.

```lean
public noncomputable def pairClassesAddEquivH1Syntomic (hn : 0 < n) :
    PairClasses S n ≃+
      Sheaf.H (rootsOfUnitySheaf (BigFppfOver.baseOverTopology B S hS .syntomic)
        (BigFppfOver.toScheme B S hS) (unitsPresheaf_isSheaf_base B S hS .syntomic) n) 1
```

**`AlgebraicGeometry.basePairCohomologyClass_picard`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/ComparisonCompatibilities.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/ComparisonCompatibilities.lean#L277). The attribute's comment: “the comparison map from the isomorphism classes of pairs to H^1 of the roots of unity is compatible with the right-hand end of the two extensions: composed with the map to H^1 of the multiplicative group and the identification of that with the Picard group (Tag 03P8) it is the Picard class of the invertible sheaf of the pair. Injectivity and surjectivity of the comparison are not proved here, nor is the compatibility with the left-hand end”.

> **The comparison map of Tag 040Q is compatible with the Picard group**, read on the class of
> a pair: the image of the class of a pair `(ℒ, α)` in `H¹((Sch/S)_τ, μ_n)` is carried by
> `H¹(μ_n) ⟶ H¹(𝐆_m) = Pic(S)` to the Picard class of `ℒ`.
>
> This is `AlgebraicGeometry.trivializationTorsor_firstCohomologyMap` followed by
> `Stacks.Picard.AllTopologies.baseH1UnitsAddEquivSchemePicardGroup_symm_classOf`.

```lean
public theorem basePairCohomologyClass_picard
    (hroot : LocalRoots (BigFppfOver.baseRingedSite B S hS τ) n) (P : TrivializedPower S n) :
    Stacks.Picard.AllTopologies.baseH1UnitsAddEquivSchemePicardGroup B S hS τ
        (Sheaf.H.map (kernel.ι (powerSheaf (BigFppfOver.baseOverTopology B S hS τ)
            (BigFppfOver.toScheme B S hS) (unitsPresheaf_isSheaf_base B S hS τ) n)) 1
          (basePairCohomologyClassHom B S hS τ n hroot (pairClass P))) =
      pairSheafClassHom S n (pairClass P)
```

**`AlgebraicGeometry.baseAssociatedModule_map_scalarEnd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/ComparisonCompatibilities.lean, line 329](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/ComparisonCompatibilities.lean#L329). The attribute's comment: “the associated-module functor of Descent, Proposition 03DX carries multiplication by a global function of the base to multiplication by that same function over the terminal object of the big tau-site; this is one ingredient of the compatibility of the comparison map with the left-hand end of the two extensions, and neither that compatibility nor any other part of the tag is proved here”.

> **The associated-module functor carries multiplication by a global function of `S` to
> multiplication by that same global function**, read over the terminal object `S / S` of the big
> `τ`-site.
>
> The functor is the pullback along the morphism of ringed sites `((Sch/S)_τ, 𝒪) → (S_Zar, 𝒪_S)`,
> for which there is no formula on morphisms; the identity is obtained from the corresponding one
> for the *pushforward*, `Stacks.SheafOfModules.map_globalSectionToEnd`, through
> `CategoryTheory.Adjunction.map_endOfId`.  Its hypothesis is the square saying that the structure
> map of the morphism of sites carries the restrictions of `s` from the top open of `S` to the
> restrictions of `s` from `S / S`, and over the top open that map is the identification
> `Γ(S, ⊤) = Γ(⊤, ⊤)`.

```lean
public theorem baseAssociatedModule_map_scalarEnd
    (hT : IsTerminal (C := BigFppfOver B S hS) (Over.mk (𝟙 (B.obj hS))))
    (s : Scheme.Γ.obj (op S)) (M : SheafOfModules.{u} (ringSheaf S)) :
    (BigFppfOver.baseAssociatedModule B S hS τ).map (scalarEnd S s M) =
      Stacks.Cohomology.Torsors.Generators.scalarEndOfTerminal
        (BigFppfOver.baseRingedSite B S hS τ) hT s
        ((BigFppfOver.baseAssociatedModule B S hS τ).obj M)
```

**`AlgebraicGeometry.exists_unitPairTrivialization_eq_basePairTriv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/ComparisonCompatibilities.lean, line 574](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/ComparisonCompatibilities.lean#L574). The attribute's comment: “the transported trivialization of the unit pair of a global unit f is the site-level trivialization of the unit pair at c * f, for one global unit c independent of f; this is the identification the compatibility of the comparison map with the left-hand end of the two extensions needs, and that compatibility is proved below, not here”.

> **The transported trivialization of the unit pair is the site-level trivialization of the
> unit pair, after one fixed twist.**  There is a global unit `c` of `S`, independent of `f`, with
> `AlgebraicGeometry.basePairTriv` at the unit pair of `f` the comparison of the two structure
> sheaves followed by
> `Stacks.Cohomology.Torsors.Generators.unitPairTrivialization` at `c * f`.
>
> This is the identification the compatibility of the comparison map of Tag 040Q with the left-hand
> end of the two extensions was missing.

```lean
public theorem exists_unitPairTrivialization_eq_basePairTriv
    (hT : IsTerminal (C := BigFppfOver B S hS) (Over.mk (𝟙 (B.obj hS)))) :
    ∃ c : (Scheme.Γ.obj (op S))ˣ, ∀ f : (Scheme.Γ.obj (op S))ˣ,
      powerMap (BigFppfOver.baseRingedSite B S hS τ)
            (BigFppfOver.baseAssociatedModulePicardUnitIso B S hS τ) n ≪≫
          unitPairTrivialization (BigFppfOver.baseRingedSite B S hS τ) hT n (c * f) =
        basePairTriv B S hS τ n (unitPair S n f)
```

**`AlgebraicGeometry.exists_kummerBoundary_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/ExactSequence.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/ExactSequence.lean#L162). The attribute's comment: “the image of the pairs with trivial invertible sheaf in H^1 of the roots of unity is exactly the kernel of the map to H^1 of the multiplicative group; so the injection of pairIso\_iff\_kummerBoundary\_eq misses exactly the classes with nonzero image there”.

> **Stacks Project, Tag 040Q, the image of the pairs whose invertible sheaf is trivial.** A
> class in `H¹(S, μ_n)` is the class of such a pair — equivalently, a Kummer boundary — exactly
> when its image in `H¹(S, 𝐆_m)` vanishes. So the injection of
> `AlgebraicGeometry.pairIso_iff_kummerBoundary_eq` has for its image precisely the kernel of
> `H¹(S, μ_n) ⟶ H¹(S, 𝐆_m)`.

```lean
theorem exists_kummerBoundary_iff (x : Sheaf.H (kummerSequence J F hF n).X₁ 1) :
    (∃ a : (Scheme.Γ.obj (op (F.obj T)))ˣ, kummerBoundary J F hF n hS hT a = x) ↔
      Sheaf.H.map (kummerSequence J F hF n).f 1 x = 0
```

**`AlgebraicGeometry.exists_kummerFirstCohomologyMap_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/ExactSequence.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/ExactSequence.lean#L184). The attribute's comment: “the image of H^1 of the roots of unity in H^1 of the multiplicative group is exactly the n-torsion; with the kernel computed by exists\_kummerBoundary\_iff this presents H^1(S, mu\_n) as an extension of that n-torsion by the global units modulo nth powers. What remains between this and the full statement of 040Q is the abelian-group structure on AlgebraicGeometry.PairClasses, for which no AddCommGroup instance exists, together with the comparison homomorphism to H^1; Tag 03P8 is NOT the gap, being proved at Picard/MultiplicativeGroupFirstCohomology.lean:206”.

> **Stacks Project, Tag 040Q, the image of `H¹(S, μ_n)` in `H¹(S, 𝐆_m)`.** It is exactly the
> `n`-torsion subgroup, since the second map of the Kummer sequence induces multiplication by `n`
> on first cohomology.

```lean
theorem exists_kummerFirstCohomologyMap_iff (y : Sheaf.H (kummerSequence J F hF n).X₂ 1) :
    (∃ x : Sheaf.H (kummerSequence J F hF n).X₁ 1,
        Sheaf.H.map (kummerSequence J F hF n).f 1 x = y) ↔ n • y = 0
```

**`AlgebraicGeometry.forall_exists_kummerBoundary_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/ExactSequence.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/ExactSequence.lean#L201). The attribute's comment: “the obstruction to surjectivity: the pairs with trivial invertible sheaf exhaust H^1 of the roots of unity exactly when H^1 of the multiplicative group has no n-torsion, so the missing classes are measured by that torsion group”.

> **Stacks Project, Tag 040Q, the obstruction to surjectivity.** The pairs whose invertible
> sheaf is trivial exhaust `H¹(S, μ_n)` exactly when `H¹(S, 𝐆_m)` has no `n`-torsion. So the
> classes of Tag 040Q that the trivial-invertible-sheaf part misses are measured by that torsion
> group, and by Tag 03P8 it is the `n`-torsion of the Picard group.

```lean
theorem forall_exists_kummerBoundary_iff :
    (∀ x : Sheaf.H (kummerSequence J F hF n).X₁ 1,
        ∃ a : (Scheme.Γ.obj (op (F.obj T)))ˣ, kummerBoundary J F hF n hS hT a = x) ↔
      ∀ y : Sheaf.H (kummerSequence J F hF n).X₂ 1, n • y = 0 → y = 0
```

**`AlgebraicGeometry.pairIso_iff_kummerBoundary_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/FirstCohomologyOfRootsOfUnity.lean, line 359](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/FirstCohomologyOfRootsOfUnity.lean#L359). The attribute's comment: “the pairs whose invertible sheaf is trivial: the canonical injective homomorphism from the global units modulo nth powers into H^1 of the roots of unity, carrying a pair to the class of its torsor of trivializations, on any site over the base having a terminal object and a short exact Kummer sequence (by 040N and 03PL: fppf, syntomic, and etale for n invertible on the base); pairs with a nontrivial invertible sheaf, and surjectivity onto H^1, are not covered”. References: SGA 7 IX (9.4.3), “special case”.

> **Stacks Project, Tag 040Q, for the pairs with trivial invertible sheaf.** Two pairs whose
> invertible sheaf is the structure sheaf of the base are isomorphic as pairs exactly when they
> have the same class in the first cohomology of the sheaf of `n`th roots of unity. Together with
> `AlgebraicGeometry.kummerBoundary_mul` this is an injective homomorphism from the group of
> isomorphism classes of such pairs — the global units modulo `n`th powers — into `H¹(S, μ_n)`,
> and by `AlgebraicGeometry.terminalBoundary_eq_fiberTorsorClass` it carries a pair to the class
> of its torsor of trivializations.

```lean
theorem pairIso_iff_kummerBoundary_eq (f g : (Scheme.Γ.obj (op (F.obj T)))ˣ) :
    Nonempty (PairIso (unitPair (F.obj T) n f) (unitPair (F.obj T) n g)) ↔
      kummerBoundary J F hF n hS hT f = kummerBoundary J F hF n hS hT g
```

**`AlgebraicGeometry.pairIso_iff_kummerBoundary_eq_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/FirstCohomologyOfRootsOfUnity.lean, line 374](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/FirstCohomologyOfRootsOfUnity.lean#L374). The attribute's comment: “the fppf case of the trivial-invertible-sheaf part, with the terminal object and the short exactness of the Kummer sequence discharged”. References: SGA 7 IX (9.4.3), “special case”.

> **Stacks Project, Tag 040Q on the big fppf site.** The hypotheses of
> `AlgebraicGeometry.pairIso_iff_kummerBoundary_eq` hold on the big fppf site over `S`, with no
> assumption on `n` beyond positivity: the Kummer sequence is short exact there by Tag 040N, and
> `S / S` is the terminal object.

```lean
theorem pairIso_iff_kummerBoundary_eq_fppf (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (n : ℕ) (hn : 0 < n)
    [HasSheafify (BigFppfOver.topology B S hS) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (BigFppfOver.topology B S hS) AddCommGrpCat.{u})]
    (f g : (Scheme.Γ.obj (op S))ˣ) :
    Nonempty (PairIso (unitPair S n f) (unitPair S n g)) ↔
      kummerBoundary (BigFppfOver.topology B S hS) (BigFppfOver.toScheme B S hS)
          (unitsPresheaf_isSheaf_fppf B S hS) n
          (kummerSequence_shortExact_fppf B S hS n hn)
          (Over.mkIdTerminal : IsTerminal (Over.mk (𝟙 (B.obj hS)))) f =
        kummerBoundary (BigFppfOver.topology B S hS) (BigFppfOver.toScheme B S hS)
          (unitsPresheaf_isSheaf_fppf B S hS) n
          (kummerSequence_shortExact_fppf B S hS n hn)
          (Over.mkIdTerminal : IsTerminal (Over.mk (𝟙 (B.obj hS)))) g
```

**`AlgebraicGeometry.pairIso_iff_kummerBoundary_eq_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/FirstCohomologyOfRootsOfUnity.lean, line 395](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/FirstCohomologyOfRootsOfUnity.lean#L395). The attribute's comment: “the syntomic case of the trivial-invertible-sheaf part, with the terminal object and the short exactness of the Kummer sequence discharged”.

> **Stacks Project, Tag 040Q on the big syntomic site.**

```lean
theorem pairIso_iff_kummerBoundary_eq_syntomic (B : BigSyntomicSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (n : ℕ) (hn : 0 < n)
    [HasSheafify (BigSyntomicOver.topology B S hS) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (BigSyntomicOver.topology B S hS) AddCommGrpCat.{u})]
    (f g : (Scheme.Γ.obj (op S))ˣ) :
    Nonempty (PairIso (unitPair S n f) (unitPair S n g)) ↔
      kummerBoundary (BigSyntomicOver.topology B S hS) (BigSyntomicOver.toScheme B S hS)
          (unitsPresheaf_isSheaf_syntomic B S hS) n
          (kummerSequence_shortExact_syntomic B S hS n hn)
          (Over.mkIdTerminal : IsTerminal (Over.mk (𝟙 (B.obj S hS)))) f =
        kummerBoundary (BigSyntomicOver.topology B S hS) (BigSyntomicOver.toScheme B S hS)
          (unitsPresheaf_isSheaf_syntomic B S hS) n
          (kummerSequence_shortExact_syntomic B S hS n hn)
          (Over.mkIdTerminal : IsTerminal (Over.mk (𝟙 (B.obj S hS)))) g
```

**`AlgebraicGeometry.pairIso_iff_kummerBoundary_eq_bigEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/FirstCohomologyOfRootsOfUnity.lean, line 417](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/FirstCohomologyOfRootsOfUnity.lean#L417). The attribute's comment: “the big etale case of the trivial-invertible-sheaf part, for n invertible on the base, with the terminal object and the short exactness of the Kummer sequence discharged”.

> **Stacks Project, Tag 040Q on the big étale site**, for `n` invertible on `S`.

```lean
theorem pairIso_iff_kummerBoundary_eq_bigEtale (B : BigEtaleSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (n : ℕ) (hn : IsUnit (n : Scheme.Γ.obj (op S)))
    [HasSheafify (BigEtaleOver.topology B S hS) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (BigEtaleOver.topology B S hS) AddCommGrpCat.{u})]
    (f g : (Scheme.Γ.obj (op S))ˣ) :
    Nonempty (PairIso (unitPair S n f) (unitPair S n g)) ↔
      kummerBoundary (BigEtaleOver.topology B S hS) (BigEtaleOver.toScheme B S hS)
          (unitsPresheaf_isSheaf_bigEtale B S hS) n
          (kummerSequence_shortExact_bigEtale B S hS n hn)
          (Over.mkIdTerminal : IsTerminal (Over.mk (𝟙 (B.obj S hS)))) f =
        kummerBoundary (BigEtaleOver.topology B S hS) (BigEtaleOver.toScheme B S hS)
          (unitsPresheaf_isSheaf_bigEtale B S hS) n
          (kummerSequence_shortExact_bigEtale B S hS n hn)
          (Over.mkIdTerminal : IsTerminal (Over.mk (𝟙 (B.obj S hS)))) g
```

**`AlgebraicGeometry.pairIso_iff_kummerBoundary_eq_smallEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/FirstCohomologyOfRootsOfUnity.lean, line 438](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/FirstCohomologyOfRootsOfUnity.lean#L438). The attribute's comment: “the small etale case of the trivial-invertible-sheaf part, for n invertible on the base, with the terminal object and the short exactness of the Kummer sequence discharged”.

> **Stacks Project, Tag 040Q on the small étale site**, for `n` invertible on `S`.

```lean
theorem pairIso_iff_kummerBoundary_eq_smallEtale (B : BigEtaleSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (n : ℕ) (hn : IsUnit (n : Scheme.Γ.obj (op S)))
    [HasSheafify (SmallEtale.topology B S hS) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (SmallEtale.topology B S hS) AddCommGrpCat.{u})]
    (f g : (Scheme.Γ.obj (op S))ˣ) :
    Nonempty (PairIso (unitPair S n f) (unitPair S n g)) ↔
      kummerBoundary (SmallEtale.topology B S hS) (SmallEtale.toScheme B S hS)
          (unitsPresheaf_isSheaf_smallEtale B S hS) n
          (kummerSequence_shortExact_smallEtale B S hS n hn)
          (SmallEtale.finalIsTerminal B S hS) f =
        kummerBoundary (SmallEtale.topology B S hS) (SmallEtale.toScheme B S hS)
          (unitsPresheaf_isSheaf_smallEtale B S hS) n
          (kummerSequence_shortExact_smallEtale B S hS n hn)
          (SmallEtale.finalIsTerminal B S hS) g
```

**`AlgebraicGeometry.instAddCommGroupPairClasses`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/PairAddCommGroup.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/PairAddCommGroup.lean#L74). The attribute's comment: “the abelian-group structure on the isomorphism classes of pairs (L, alpha), with addition the tensor product of pairs, zero the structure sheaf with its canonical trivialization, and negation the inverse pair; this is the group the tag identifies with H^1 of the roots of unity, but the identification itself is not stated here”.

> **The isomorphism classes of pairs form an abelian group.** The
> addition is the tensor product of pairs, the zero is the structure sheaf with its canonical
> trivialization, and the negation is the inverse pair.

```lean
instance instAddCommGroupPairClasses (S : Scheme.{u}) (n : ℕ) :
    AddCommGroup (PairClasses S n)
```

**`AlgebraicGeometry.basePairTriv_tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/PairComparisonHom.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/PairComparisonHom.lean#L112). The attribute's comment: “the transport to the big tau-site carries the tensor product of pairs to the tensor product of pairs”.

> **The transported trivialization of a tensor product of pairs is the tensor product of the
> two transported trivializations**, on the big `τ`-site of `S`.
>
> This is part (4) of the second construction of Tag 040Q: it is
> `Stacks.SheafOfModules.TensorPowerTransport.transportTriv_tensor` at the associated-module functor
> of Descent, Proposition 03DX, whose four coherences are
> `AlgebraicGeometry.BigFppfOver.baseAssociatedModuleTensorIso'_natural`,
> `_associator`, `_braiding` and `_rightUnitor`.

```lean
public theorem basePairTriv_tensor (P Q : TrivializedPower S n) :
    letI := basePairSheaf_isInvertible B S hS τ n P
    letI := basePairSheaf_isInvertible B S hS τ n Q
    letI : IsInvertible (BigFppfOver.baseRingedSite B S hS τ).O.obj
        (Stacks.SheafOfModules.Tensor.ringSheaf (BigFppfOver.baseRingedSite B S hS τ).O).2
        ((BigFppfOver.baseAssociatedModule B S hS τ).obj
          ((((Stacks.SheafOfModules.Tensor.sheafTensor
            ⟨S.presheaf, Presheaf.isSheaf_of_isSheaf_comp _ S.presheaf
              (forget₂ CommRingCat RingCat) (ringSheafCond S)⟩).obj P.sheaf).obj Q.sheaf))) :=
      basePairSheaf_isInvertible B S hS τ n (tensorPair S n P Q)
    letI : IsInvertible (BigFppfOver.baseRingedSite B S hS τ).O.obj
        (Stacks.SheafOfModules.Tensor.ringSheaf (BigFppfOver.baseRingedSite B S hS τ).O).2
        (tensorSheafOfModules (BigFppfOver.baseRingedSite B S hS τ)
          ((BigFppfOver.baseAssociatedModule B S hS τ).obj P.sheaf)
          ((BigFppfOver.baseAssociatedModule B S hS τ).obj Q.sheaf)) :=
      Stacks.SheafOfModules.isInvertible_tensorSheaf
        (BigFppfOver.baseRingedSite B S hS τ).O.obj
        (Stacks.SheafOfModules.Tensor.ringSheaf (BigFppfOver.baseRingedSite B S hS τ).O).2
        (basePairSheaf B S hS τ n P) (basePairSheaf B S hS τ n Q)
    powerMap (BigFppfOver.baseRingedSite B S hS τ)
          (BigFppfOver.baseAssociatedModuleTensorIso' B S hS τ P.sheaf Q.sheaf) n ≪≫
        tensorTriv (BigFppfOver.baseRingedSite B S hS τ) (basePairSheaf B S hS τ n P)
          (basePairSheaf B S hS τ n Q) n (basePairTriv B S hS τ n P)
          (basePairTriv B S hS τ n Q) =
      basePairTriv B S hS τ n (tensorPair S n P Q)
```

**`AlgebraicGeometry.basePairClass_tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/PairComparisonHom.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/PairComparisonHom.lean#L159). The attribute's comment: “the torsor of trivializations of a tensor product of pairs”.

> **A tensor product of pairs has the torsor of trivializations of the tensor product of the
> two transported pairs.**  This is
> `AlgebraicGeometry.trivializationTorsor_class_eq_of_iso'` fed the object-level tensor comparison
> of the associated-module functor and `AlgebraicGeometry.basePairTriv_tensor`.

```lean
public theorem basePairClass_tensor (hroot : LocalRoots (BigFppfOver.baseRingedSite B S hS τ) n)
    (P Q : TrivializedPower S n) :
    Quotient.mk
          (torsorSetoid (rootsOfUnitySheaf (BigFppfOver.baseOverTopology B S hS τ)
            (BigFppfOver.toScheme B S hS) (unitsPresheaf_isSheaf_base B S hS τ) n))
          (trivializationTorsor (BigFppfOver.baseOverTopology B S hS τ)
            (BigFppfOver.toScheme B S hS) (BigFppfOver.baseRingedSite B S hS τ).O.property
            (unitsPresheaf_isSheaf_base B S hS τ) n
            (baseRingedSite_isLocallyRinged B S hS τ) hroot
            (basePairSheaf B S hS τ n (tensorPair S n P Q))
            (basePairSheaf_isInvertible B S hS τ n (tensorPair S n P Q))
            (basePairTriv B S hS τ n (tensorPair S n P Q))) =
      Quotient.mk
        (torsorSetoid (rootsOfUnitySheaf (BigFppfOver.baseOverTopology B S hS τ)
          (BigFppfOver.toScheme B S hS) (unitsPresheaf_isSheaf_base B S hS τ) n))
        (trivializationTorsor (BigFppfOver.baseOverTopology B S hS τ)
          (BigFppfOver.toScheme B S hS) (BigFppfOver.baseRingedSite B S hS τ).O.property
          (unitsPresheaf_isSheaf_base B S hS τ) n
          (baseRingedSite_isLocallyRinged B S hS τ) hroot
          (tensorSheafOfModules (BigFppfOver.baseRingedSite B S hS τ)
            (basePairSheaf B S hS τ n P) (basePairSheaf B S hS τ n Q))
          (Stacks.SheafOfModules.isInvertible_tensorSheaf
            (BigFppfOver.baseRingedSite B S hS τ).O.obj
            (Stacks.SheafOfModules.Tensor.ringSheaf (BigFppfOver.baseRingedSite B S hS τ).O).2
            (basePairSheaf B S hS τ n P) (basePairSheaf B S hS τ n Q))
          (tensorTriv (BigFppfOver.baseRingedSite B S hS τ) (basePairSheaf B S hS τ n P)
            (basePairSheaf B S hS τ n Q) n (basePairTriv B S hS τ n P)
            (basePairTriv B S hS τ n Q)))
```

**`AlgebraicGeometry.basePairCohomologyClass_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/PairComparisonHom.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/PairComparisonHom.lean#L207). The attribute's comment: “the comparison map is additive on classes of pairs”.

> **The comparison map of Tag 040Q is additive**, read on classes of pairs: the class of a
> tensor product of pairs is the sum of the two classes.

```lean
public theorem basePairCohomologyClass_add
    (hroot : LocalRoots (BigFppfOver.baseRingedSite B S hS τ) n) (P Q : TrivializedPower S n) :
    basePairCohomologyClass B S hS τ n hroot (pairClass P + pairClass Q) =
      basePairCohomologyClass B S hS τ n hroot (pairClass P) +
        basePairCohomologyClass B S hS τ n hroot (pairClass Q)
```

**`AlgebraicGeometry.basePairCohomologyClassHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/PairComparisonHom.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/PairComparisonHom.lean#L229). The attribute's comment: “the comparison map from the isomorphism classes of pairs to H^1 of the roots of unity as a homomorphism of abelian groups; injectivity and surjectivity are not proved here”.

> **The comparison map of Tag 040Q as a homomorphism of abelian groups**,
> `PairClasses S n →+ H¹((Sch/S)_τ, μ_n)`.  The addition of the source is the tensor product of
> pairs and that of the target is the addition of `Ext¹`; additivity is
> `AlgebraicGeometry.basePairCohomologyClass_add`, and the vanishing at the zero class follows from
> it, the two groups being groups.
>
> This is the map `Stacks.Kummer.bijective_of_comparison` consumes.

```lean
public def basePairCohomologyClassHom
    (hroot : LocalRoots (BigFppfOver.baseRingedSite B S hS τ) n) :
    PairClasses S n →+
      Sheaf.H (rootsOfUnitySheaf (BigFppfOver.baseOverTopology B S hS τ)
        (BigFppfOver.toScheme B S hS) (unitsPresheaf_isSheaf_base B S hS τ) n) 1
```

**`AlgebraicGeometry.pairSheafClassHom_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/PairExactSequence.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/PairExactSequence.lean#L141). The attribute's comment: “exactness in the middle of the pair side of the extension, as abelian groups: the kernel of the homomorphism from the isomorphism classes of pairs to the Picard group is the image of the homomorphism from the global units; neither the cohomology group nor the comparison with it occurs”.

> **Stacks Project, Tag 040Q, exactness in the middle of the pair side.** A class of pairs has
> trivial Picard class — that is, its invertible sheaf is isomorphic to the structure sheaf —
> exactly when it is the class of a pair coming from a global unit. The forward direction is
> `AlgebraicGeometry.exists_pairIso_unitPair`, that a pair whose invertible sheaf is merely
> isomorphic to the structure sheaf is isomorphic to a unit pair.

```lean
theorem pairSheafClassHom_eq_zero_iff (S : Scheme.{u}) (n : ℕ) (x : PairClasses S n) :
    pairSheafClassHom S n x = 0 ↔
      ∃ f : Additive (Scheme.Γ.obj (op S))ˣ, unitPairHom S n f = x
```

**`AlgebraicGeometry.exists_pairSheafClassHom_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/PairExactSequence.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/KummerTheory/PairExactSequence.lean#L161). The attribute's comment: “the image of the homomorphism from the isomorphism classes of pairs to the Picard group is exactly the n-torsion, as abelian groups; this is the surjectivity half of the pair side of the extension, and the cohomology group does not occur”.

> **Stacks Project, Tag 040Q, surjectivity of the pair side onto the torsion.** A Picard class
> is the Picard class of a class of pairs exactly when it is `n`-torsion. This is
> `AlgebraicGeometry.exists_trivializedPower_classOf_iff` read through the group of isomorphism
> classes of pairs.

```lean
theorem exists_pairSheafClassHom_eq_iff (S : Scheme.{u}) (n : ℕ)
    (c : PicardGroup S.presheaf (ringSheafCond S)) :
    (∃ x : PairClasses S n, pairSheafClassHom S n x = c) ↔ n • c = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.28, Tag 03PK](https://stacks.math.columbia.edu/tag/03PK)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
