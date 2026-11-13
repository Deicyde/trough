---
declaration: section
origin: cited
lean: Stacks.Duality.DualizingBase, Stacks.Duality.UpperShriek.overlapCompareRestrict_cocycle, Stacks.Duality.Normalized.existsUnique_iso_nagata, Stacks.Duality.Normalized.exists_existsUnique_iso_nagata, Stacks.Duality.Normalized.exists_nagata, Stacks.Duality.isDualizingComplex_normalizedDualizingComplex, Stacks.Duality.existsUnique_iso_normalizedDualizingComplex, Stacks.Duality.existsUnique_iso_normalizedDualizingComplex_toNormalized
statement: formalized
proof: formalized
---

# 48.20 Glueing dualizing complexes

Section 48.20 of the Stacks Project, [Tag 0AU5](https://stacks.math.columbia.edu/tag/0AU5). 14 tags here are carried by 39 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AU4, a situation

[Tag 0AU4](https://stacks.math.columbia.edu/tag/0AU4) in the Stacks Project.

**`Stacks.Duality.DualizingBase`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GlueingDualizingComplexes.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GlueingDualizingComplexes.lean#L141). The attribute's comment: “the Situation: a Noetherian scheme with a chosen dualizing complex”.

> **Stacks Project, Tag 0AU4.** The standing situation of the section on glueing dualizing
> complexes: a Noetherian scheme `S` together with a dualizing complex `ω_S^•` on it, in the
> sense of [Stacks, Tag 0A87].

```lean
structure DualizingBase
```

## Tag 0AU6, an item

[Tag 0AU6](https://stacks.math.columbia.edu/tag/0AU6) in the Stacks Project.

**`Stacks.Duality.UpperShriek.overlapCompareRestrict_cocycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/NormalizedDualizingCocycle.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/NormalizedDualizingCocycle.lean#L249). The attribute's comment: “item (3) of the discussion before Definition 0AUA: the cocycle condition phi\_ik = phi\_jk after phi\_ij for the canonical comparisons of the local models, restricted to the triple overlap U\_i cap U\_j cap U\_k. RESTRICTED only in that the upper-shriek formalism of Stacks 0A9Y/0ATX/0ATY is the parameter UpperShriek, as in 0AUB and 0AUC; the coherence 0ATY, which the source cites for item (3), is its factorIso\_assoc field”.

> **Stacks Project, Tag 0AU6.** In Situation [Stacks, Tag 0AU4] let `X` be of finite type over
> `S` and let `𝒰 : X = ⋃ U_i` be a finite covering of `X` by opens separated and of finite type
> over `S`. Let `ω_i^•` be the local models and `φ_{ij} : ω_i^•|_{U_i ∩ U_j} ≅ ω_j^•|_{U_i ∩ U_j}`
> the canonical comparisons of the discussion preceding Definition [Stacks, Tag 0AUA]. Then for
> all `i, j, k`
>
> `φ_{ik}|_{U_i ∩ U_j ∩ U_k} = φ_{jk}|_{U_i ∩ U_j ∩ U_k} ∘ φ_{ij}|_{U_i ∩ U_j ∩ U_k}`
>
> in `D(𝒪_{U_i ∩ U_j ∩ U_k})`. Composition is written left to right, so the right hand side
> below reads `φ_{ij}` followed by `φ_{jk}`.
>
> The restrictions are `Stacks.Duality.UpperShriek.overlapCompareRestrict`, i.e. the conjugation
> of `Stacks.Duality.UpperShriek.restrictCompare`; the proof identifies all three with
> comparisons built directly on the triple overlap
> (`Stacks.Duality.UpperShriek.overlapCompareRestrict_eq`, which is the coherence
> [Stacks, Tag 0ATY]) and then cancels
> (`Stacks.Duality.UpperShriek.localCompare_trans`).

```lean
theorem overlapCompareRestrict_cocycle (𝒰 : SeparatedCovering p ι) (i j k : ι) :
    A.overlapCompareRestrict hp ωS 𝒰 i k (𝒰.U i ⊓ 𝒰.U j ⊓ 𝒰.U k)
        (le_inf (inf_le_left.trans inf_le_left) inf_le_right) =
      A.overlapCompareRestrict hp ωS 𝒰 i j (𝒰.U i ⊓ 𝒰.U j ⊓ 𝒰.U k) inf_le_left ≪≫
        A.overlapCompareRestrict hp ωS 𝒰 j k (𝒰.U i ⊓ 𝒰.U j ⊓ 𝒰.U k)
          (le_inf (inf_le_left.trans inf_le_right) inf_le_right)
```

## Tag 0AU7, a lemma

[Tag 0AU7](https://stacks.math.columbia.edu/tag/0AU7) in the Stacks Project.

**`Stacks.Duality.Normalized.existsUnique_iso_nagata`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedExistenceNagata.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedExistenceNagata.lean#L55).

> **[Stacks, Tag 0AU7]** In Situation 0AU4, let `X` be of finite type over `S` and `𝒰` a finite
> open covering of `X` by schemes separated over `S`. A dualizing complex normalized relative to
> `ω_S^•` and `𝒰` is unique up to unique isomorphism: for two of them, `(K, α_i)` and `(K', α'_i)`,
> exactly one isomorphism `K ≅ K'` carries `α_i` to `α'_i` on every member.

```lean
theorem existsUnique_iso_nagata
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj) {ι : Type w}
    {𝒰 : SeparatedCovering p ι} (𝒩 𝒩' : Normalized UpperShriek.nagata hp ωS 𝒰) :
    ∃! e : 𝒩.complex ≅ 𝒩'.complex, ∀ i,
      (UpperShriek.nagata.shriek (𝒰.U i).ι (hp.isShriekable_ι _)).mapIso e ≪≫
        𝒩'.localIso i = 𝒩.localIso i
```

## Tag 0AU8, a lemma

[Tag 0AU8](https://stacks.math.columbia.edu/tag/0AU8) in the Stacks Project.

**`Stacks.Duality.Normalized.exists_existsUnique_iso_nagata`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedExistenceNagata.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedExistenceNagata.lean#L69).

> **[Stacks, Tag 0AU8]** In Situation 0AU4, let `X` be of finite type over `S` and `𝒰`, `𝒱` two
> finite open coverings of `X` by schemes separated over `S`. If `(K, α_i)` is a dualizing complex
> normalized relative to `ω_S^•` and `𝒰`, there is a dualizing complex `(K', α'_j)` normalized
> relative to `ω_S^•` and `𝒱`, and the two are canonically isomorphic: exactly one isomorphism
> `K ≅ K'` carries the restriction of `α_i` to `U_i ∩ V_j` to that of `α'_j`, for all `i`, `j`.

```lean
theorem exists_existsUnique_iso_nagata
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj)
    {ι J : Type w} {𝒰 : SeparatedCovering p ι} (𝒱 : SeparatedCovering p J)
    (𝒩 : Normalized UpperShriek.nagata hp ωS 𝒰) :
    ∃ 𝒩' : Normalized UpperShriek.nagata hp ωS 𝒱,
      (haveI := hp.source_noetherian; IsDualizingComplex 𝒩'.complex.obj.obj) ∧
      ∃! e : 𝒩.complex ≅ 𝒩'.complex, ∀ i j,
        (UpperShriek.nagata.shriek (𝒰.U i ⊓ 𝒱.U j).ι (hp.isShriekable_ι _)).mapIso e ≪≫
          UpperShriek.nagata.restrictLocalIso hp ωS 𝒩'.complex
            (inf_le_right : 𝒰.U i ⊓ 𝒱.U j ≤ 𝒱.U j) (𝒱.shriekable j) (𝒩'.localIso j) =
        UpperShriek.nagata.restrictLocalIso hp ωS 𝒩.complex
          (inf_le_left : 𝒰.U i ⊓ 𝒱.U j ≤ 𝒰.U i) (𝒰.shriekable i) (𝒩.localIso i)
```

## Tag 0AU9, a lemma

[Tag 0AU9](https://stacks.math.columbia.edu/tag/0AU9) in the Stacks Project.

**`Stacks.Duality.Normalized.exists_nagata`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedExistenceNagata.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedExistenceNagata.lean#L87).

> **[Stacks, Tag 0AU9]** In Situation 0AU4, let `X` be of finite type over `S` and `𝒰` a finite
> open covering of `X` by schemes separated over `S`. Then there exists a dualizing complex
> normalized relative to `ω_S^•` and `𝒰`.

```lean
theorem exists_nagata
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj)
    {ι : Type w} (𝒰 : SeparatedCovering p ι) :
    ∃ 𝒩 : Normalized UpperShriek.nagata hp ωS 𝒰,
      haveI := hp.source_noetherian; IsDualizingComplex 𝒩.complex.obj.obj
```

## Tag 0AUA, a definition

[Tag 0AUA](https://stacks.math.columbia.edu/tag/0AUA) in the Stacks Project.

**`Stacks.Duality.isDualizingComplex_normalizedDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/NormalizedDualizingComplexNagata.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/NormalizedDualizingComplexNagata.lean#L55). The attribute's comment: “ω\_X^• is a dualizing complex on X”.

> **[Stacks, Tag 0AUA], `ω_X^•` is a dualizing complex.** Let `S` be Noetherian with a
> dualizing complex `ω_S^•` and `X` of finite type over `S`. The dualizing complex `ω_X^•`
> normalized relative to `ω_S^•` is a dualizing complex on `X`.

```lean
theorem isDualizingComplex_normalizedDualizingComplex :
    haveI := hp.source_noetherian
    IsDualizingComplex (normalizedDualizingComplex hp ωS hωS).complex.obj.obj
```

**`Stacks.Duality.existsUnique_iso_normalizedDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/NormalizedDualizingComplexNagata.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/NormalizedDualizingComplexNagata.lean#L66). The attribute's comment: “the pair (ω\_X^•, α\_U) is unique up to unique isomorphism”.

> **[Stacks, Tag 0AUA], uniqueness up to unique isomorphism.** Let `S` be Noetherian with a
> dualizing complex `ω_S^•` and `X` of finite type over `S`. For any complex `K` on `X` with
> isomorphisms `β_U : K|_U ≅ (U → S)^! ω_S^•` for the opens `U ⊆ X` separated over `S`,
> compatible with restriction, exactly one isomorphism `K ≅ ω_X^•` carries `β_U` to the
> isomorphism `α_U` of `ω_X^•` for every such `U`.

```lean
theorem existsUnique_iso_normalizedDualizingComplex
    (𝒦 : NormalizedOnOpens UpperShriek.nagata hp ωS) :
    ∃! e : 𝒦.complex ≅ (normalizedDualizingComplex hp ωS hωS).complex,
      ∀ (W : X.Opens) (hW : IsShriekable (W.ι ≫ p)),
        (UpperShriek.nagata.shriek W.ι (hp.isShriekable_ι W)).mapIso e ≪≫
          (normalizedDualizingComplex hp ωS hωS).localIso W hW = 𝒦.localIso W hW
```

**`Stacks.Duality.existsUnique_iso_normalizedDualizingComplex_toNormalized`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/NormalizedDualizingComplexNagata.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/NormalizedDualizingComplexNagata.lean#L82). The attribute's comment: “(ω\_X^•, α\_\{U\_i}) is normalized relative to ω\_S^• and every finite covering by opens separated over S”.

> **[Stacks, Tag 0AUA], normalized relative to every covering.** Let `S` be Noetherian with a
> dualizing complex `ω_S^•`, `X` of finite type over `S` and `𝒰 : X = ⋃ U_i` a finite open
> covering by opens separated over `S`. Then `(ω_X^•, α_{U_i})` is a dualizing complex normalized
> relative to `ω_S^•` and `𝒰` (`Stacks.Duality.NormalizedOnOpens.toNormalized`), and it is the one
> up to unique isomorphism: for every dualizing complex `(K, β_i)` normalized relative to `ω_S^•`
> and `𝒰`, exactly one isomorphism `K ≅ ω_X^•` carries `β_i` to `α_{U_i}` for all `i`.

```lean
theorem existsUnique_iso_normalizedDualizingComplex_toNormalized {ι : Type w}
    (𝒰 : SeparatedCovering p ι) (𝒩 : Normalized UpperShriek.nagata hp ωS 𝒰) :
    ∃! e : 𝒩.complex ≅ ((normalizedDualizingComplex hp ωS hωS).toNormalized 𝒰).complex,
      ∀ i, (UpperShriek.nagata.shriek (𝒰.U i).ι (hp.isShriekable_ι _)).mapIso e ≪≫
          ((normalizedDualizingComplex hp ωS hωS).toNormalized 𝒰).localIso i = 𝒩.localIso i
```

**`Stacks.Duality.normalizedDualizingComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedExistenceNagata.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedExistenceNagata.lean#L104).

> **[Stacks, Tag 0AUA]** Let `S` be Noetherian with a dualizing complex `ω_S^•` and `X` of finite
> type over `S`. The dualizing complex `ω_X^•` normalized relative to `ω_S^•`: a complex on `X` with
> isomorphisms `α_W : ω_X^•|_W ≅ (W → S)^! ω_S^•` for every open `W` separated over `S`,
> compatible with restriction. It is unique up to unique isomorphism
> (`Stacks.Duality.NormalizedOnOpens.existsUnique_iso_ofCompactifications`) and normalized relative
> to `ω_S^•` and every finite covering of `X` by opens separated over `S`
> (`Stacks.Duality.NormalizedOnOpens.toNormalized`).

```lean
def normalizedDualizingComplex {X S : Scheme.{u}} {p : X ⟶ S}
    (hp : IsFiniteTypeOverNoetherian p) (ωS : quasiCoherentDerivedCategoryPlusOfModel S)
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj) :
    NormalizedOnOpens UpperShriek.nagata hp ωS
```

## Tag 0AUB, a lemma

[Tag 0AUB](https://stacks.math.columbia.edu/tag/0AUB) in the Stacks Project.

**`Stacks.Duality.exists_normalized_of_normalized`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/NormalizedDualizingTransitivity.lean, line 592](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/NormalizedDualizingTransitivity.lean#L592). The attribute's comment: “assuming the upper-shriek formalism of Stacks 0A9E/0ATX/0ATY as the parameter UpperShriek, pending its landing”.

> **[Stacks, Tag 0AUB]** Let `S` be a Noetherian scheme carrying `ω_S^•`, let `q : Y ⟶ S`
> and `p = f ≫ q : X ⟶ S` be of finite type, and let `𝒱` and `𝒰` be coverings of `Y` and of
> `X` by opens separated and of finite type over `S`, with each `U_k` carried by `f` into
> `V_{idx k}`. If `ω_X^•` is normalized relative to `ω_S^•` and `𝒰`, and `ω_Y^•` is normalized
> relative to `ω_S^•` and `𝒱`, then `ω_X^•` is normalized relative to `ω_Y^•` and `𝒰` read over
> `Y`.
>
> Normalization here is the primitive notion of the text of [Stacks, Tag 0AU5] -- the pair
> `(K, α_i)` -- rather than the covering-free Definition [Stacks, Tag 0AUA], and it is the
> notion the proof of 0AUB manipulates. That `ω_X^•` is again dualizing is not part of the
> statement because `Normalized` does not record dualizing-ness; it is [Stacks, Tag 0AU8].

```lean
theorem exists_normalized_of_normalized {𝒟 : Scheme.{u} → Type v}
    [∀ X : Scheme.{u}, Category.{v'} (𝒟 X)] (A : UpperShriek 𝒟) {X Y S : Scheme.{u}}
    {f : X ⟶ Y} {q : Y ⟶ S} {p : X ⟶ S} (hpe : f ≫ q = p)
    (hp : IsFiniteTypeOverNoetherian p) (hq : IsFiniteTypeOverNoetherian q) (ωS : 𝒟 S)
    {ι : Type w} {J : Type w'} (𝒰 : SeparatedCovering p ι) (𝒱 : SeparatedCovering q J)
    (idx : ι → J) (hle : ∀ k, 𝒰.U k ≤ f ⁻¹ᵁ 𝒱.U (idx k)) (𝒩X : Normalized A hp ωS 𝒰)
    (𝒩Y : Normalized A hq ωS 𝒱) :
    ∃ 𝒩 : Normalized A (hp.of_comp' hq hpe) 𝒩Y.complex (𝒰.overMid 𝒱 hp hq hpe idx hle),
      𝒩.complex = 𝒩X.complex
```

**`Stacks.Duality.NormalizedOnOpens.exists_relative_nagata`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedProperNagata.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedProperNagata.lean#L59).

> **[Stacks, Tag 0AUB]** In Situation 0AU4, let `f : X ⟶ Y` be a morphism of schemes of finite
> type over `S` and `ω_X^•`, `ω_Y^•` dualizing complexes normalized relative to `ω_S^•`. Then
> `ω_X^•` is a dualizing complex normalized relative to `ω_Y^•`: `ω_Y^•` and `ω_X^•` are dualizing,
> so `(Y, ω_Y^•)` is again as in Situation 0AU4, and `ω_X^•` carries isomorphisms
> `ω_X^•|_W ≅ (W → Y)^! ω_Y^•` for every open `W` separated over `Y`, compatible with restriction.

```lean
theorem exists_relative_nagata
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj)
    (𝒦X : NormalizedOnOpens UpperShriek.nagata hp ωS)
    (𝒦Y : NormalizedOnOpens UpperShriek.nagata hq ωS) :
    (haveI := hq.source_noetherian; IsDualizingComplex 𝒦Y.complex.obj.obj) ∧
    (haveI := hp.source_noetherian; IsDualizingComplex 𝒦X.complex.obj.obj) ∧
    ∃ 𝒦 : NormalizedOnOpens UpperShriek.nagata (hp.of_comp' hq hpe) 𝒦Y.complex,
      𝒦.complex = 𝒦X.complex
```

## Tag 0AUC, a lemma

[Tag 0AUC](https://stacks.math.columbia.edu/tag/0AUC) in the Stacks Project.

**`Stacks.Duality.NormalizedOnOpens.existsUnique_iso_shriekOfIsOpenImmersion_nagata`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/NormalizedOnOpensOpenImmersion.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/NormalizedOnOpensOpenImmersion.lean#L172). The attribute's comment: “S Noetherian with dualizing complex ω\_S, X → Y an open immersion of schemes of finite type over S; the unique isomorphism ω\_X^• ≅ j^! ω\_Y^• compatible with the normalizations”.

> **[Stacks, Tag 0AUC], canonicity.** In Situation 0AU4, let `j : X ⟶ Y` be an open immersion
> of schemes of finite type over `S` and `ω_X^•`, `ω_Y^•` dualizing complexes normalized relative to
> `ω_S^•`. Exactly one isomorphism `ω_X^• ≅ j^! ω_Y^•` carries the normalization `α_W` of `ω_X^•`
> to that of `j^! ω_Y^•` (`shriekOfIsOpenImmersion`) for every open `W ⊆ X` separated over `S`.

```lean
theorem existsUnique_iso_shriekOfIsOpenImmersion_nagata
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj)
    (𝒦X : NormalizedOnOpens UpperShriek.nagata hp ωS)
    (𝒦Y : NormalizedOnOpens UpperShriek.nagata hq ωS) :
    ∃! e : 𝒦X.complex ≅
        (UpperShriek.nagata.shriek j (hq.isShriekable_of_isOpenImmersion j)).obj 𝒦Y.complex,
      ∀ (W : X.Opens) (hW : IsShriekable (W.ι ≫ p)),
        (UpperShriek.nagata.shriek W.ι (hp.isShriekable_ι W)).mapIso e ≪≫
          (𝒦Y.shriekOfIsOpenImmersion hpe hp).localIso W hW = 𝒦X.localIso W hW
```

**`Stacks.Duality.NormalizedOnOpens.isoDerivedRestrictNagata`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/NormalizedOnOpensOpenImmersion.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/NormalizedOnOpensOpenImmersion.lean#L191). The attribute's comment: “the resulting canonical isomorphism ω\_X^• ≅ ω\_Y^•|\_X in D(O\_X)”.

> **[Stacks, Tag 0AUC]** In Situation 0AU4, let `j : X ⟶ Y` be an open immersion of schemes of
> finite type over `S` and `ω_X^•`, `ω_Y^•` dualizing complexes normalized relative to `ω_S^•`.
> The canonical isomorphism `ω_X^• ≅ ω_Y^•|_X` in `D(𝒪_X)`: the unique isomorphism
> `ω_X^• ≅ j^! ω_Y^•` compatible with the normalizations
> (`existsUnique_iso_shriekOfIsOpenImmersion_nagata`), followed by `j^! = j^*`
> ([Stacks, Tag 0AU0]).

```lean
def isoDerivedRestrictNagata
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj)
    (𝒦X : NormalizedOnOpens UpperShriek.nagata hp ωS)
    (𝒦Y : NormalizedOnOpens UpperShriek.nagata hq ωS) :
    𝒦X.complex.obj.obj ≅
      (Scheme.Modules.restrictFunctor j).mapDerivedCategory.obj 𝒦Y.complex.obj.obj
```

**`Stacks.Duality.NormalizedOnOpens.isoDerivedRestrictNagata_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/NormalizedOnOpensOpenImmersion.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/NormalizedOnOpensOpenImmersion.lean#L206). The attribute's comment: “the canonical isomorphism ω\_X^• ≅ ω\_Y^•|\_X is characterized through j^! = j^*”.

> **[Stacks, Tag 0AUC], the canonical isomorphism is characterised by the normalizations**:
> for any isomorphism `e : ω_X^• ≅ j^! ω_Y^•` compatible with the normalizations on every open of
> `X` separated over `S`, `isoDerivedRestrictNagata` is `e` followed by `j^! = j^*`.

```lean
theorem isoDerivedRestrictNagata_eq
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj)
    (𝒦X : NormalizedOnOpens UpperShriek.nagata hp ωS)
    (𝒦Y : NormalizedOnOpens UpperShriek.nagata hq ωS)
    (e : 𝒦X.complex ≅
      (UpperShriek.nagata.shriek j (hq.isShriekable_of_isOpenImmersion j)).obj 𝒦Y.complex)
    (he : ∀ (W : X.Opens) (hW : IsShriekable (W.ι ≫ p)),
      (UpperShriek.nagata.shriek W.ι (hp.isShriekable_ι W)).mapIso e ≪≫
        (𝒦Y.shriekOfIsOpenImmersion hpe hp).localIso W hW = 𝒦X.localIso W hW) :
    isoDerivedRestrictNagata hpe hωS 𝒦X 𝒦Y =
      (ObjectProperty.ι _ ⋙ ObjectProperty.ι _).mapIso e ≪≫
        UpperShriek.shriekObjIsoDerivedRestrict nagataCompactification j
          (hq.isShriekable_of_isOpenImmersion j) 𝒦Y.complex
```

## Tag 0AUD, a lemma

[Tag 0AUD](https://stacks.math.columbia.edu/tag/0AUD) in the Stacks Project.

**`Stacks.Duality.dualizingIsoRightAdjointObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GlueingDualizingComplexes.lean, line 404](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GlueingDualizingComplexes.lean#L404). The attribute's comment: “RESTRICTED: the upper shriek formalism is a parameter, normalization is taken in the separated form omega\_X = p^! omega\_S, and the identification of f^! with the right adjoint, which is the only place properness is used, is a hypothesis”.

> **Stacks Project, Tag 0AUD.** Let `f : X ⟶ Y` be a morphism of schemes of finite type over
> the base of [Stacks, Tag 0AU4], with structure morphisms `q : Y ⟶ S` and `p : X ⟶ S` and
> `f ≫ q = p`. Let `a` be the right adjoint of `Rf_*` of [Stacks, Tag 0A9E]. If `ω_X^•` and
> `ω_Y^•` are normalized relative to `ω_S^•`, there is a canonical isomorphism
> `a(ω_Y^•) ≅ ω_X^•`.
>
> This is the argument of the source in the case where the schemes are separated over `S`: there
> `ω_X^• = p^!ω_S^•` and `ω_Y^• = q^!ω_S^•`, the properness of `f` enters only through the
> identification of `f^!` with `a`, and the composition comparison `f^! ∘ q^! ≅ p^!` — the
> `factorIso` field of `Stacks.Duality.UpperShriek` — finishes it.

```lean
def dualizingIsoRightAdjointObj (A : UpperShriek 𝒟) {X Y S : Scheme.{u}}
    {f : X ⟶ Y} {q : Y ⟶ S} {p : X ⟶ S} (hfq : f ≫ q = p)
    (hf : IsShriekable f) (hq : IsShriekable q) (hp : IsShriekable p)
    {a : 𝒟 Y ⥤ 𝒟 X} (hfa : A.shriek f hf ≅ a)
    (ωS : 𝒟 S) {ωX : 𝒟 X} {ωY : 𝒟 Y}
    (nX : ωX ≅ (A.shriek p hp).obj ωS) (nY : ωY ≅ (A.shriek q hq).obj ωS) :
    a.obj ωY ≅ ωX
```

**`Stacks.Duality.NormalizedOnOpens.twistedInverseImageObjIsoNagata`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedProperNagata.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedProperNagata.lean#L92).

> **[Stacks, Tag 0AUD]** In Situation 0AU4, let `f : X ⟶ Y` be a proper morphism of schemes of
> finite type over `S`, `ω_X^•`, `ω_Y^•` the dualizing complexes normalized relative to `ω_S^•`,
> and `a` the right adjoint of `Rf_*` ([Stacks, Tag 0A9E]). Then there is a canonical isomorphism
> `a(ω_Y^•) ≅ ω_X^•`.

```lean
def twistedInverseImageObjIsoNagata
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj) [IsProper f]
    (𝒦X : NormalizedOnOpens UpperShriek.nagata hp ωS)
    (𝒦Y : NormalizedOnOpens UpperShriek.nagata hq ωS) :
    haveI := hq.source_noetherian
    haveI := hp.source_noetherian
    (twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
        𝒦Y.complex.obj ≅ 𝒦X.complex.obj
```

## Tag 0AUE, a lemma

[Tag 0AUE](https://stacks.math.columbia.edu/tag/0AUE) in the Stacks Project.

**`Stacks.Duality.normalizedUpperShriek`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleOverField.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingModuleOverField.lean#L167). The attribute's comment: “the closing remark, first half only: for X separated over the base the complex p^! omega\_S^bullet is normalized relative to omega\_S^bullet. The second half of the remark, f\_new^! K = f^! K, is NOT carried, and neither are parts (1), (3), (5), (6); parts (2) and (4) are elsewhere. RESTRICTED: the upper-shriek formalism of Stacks 0A9Y/0ATX/0ATY is the parameter UpperShriek, pending its landing”.

> **[Stacks, Tag 0AUE], the closing remark on the separated case.** Let `X` be separated and
> of finite type over a Noetherian scheme `S` with structure morphism `p`, and let `ω_S^•` be a
> complex on `S`. Then `p^!ω_S^•` is normalized relative to `ω_S^•`: its restriction to each
> member of a covering of `X` by opens separated over `S` is canonically the local model there,
> compatibly on overlaps.

```lean
def normalizedUpperShriek {ι : Type w} (𝒰 : SeparatedCovering p ι) : Normalized A hp ωS 𝒰
```

**`Stacks.Duality.fNewShriekObjIsoDualizing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/NewShriekNormalizedComplex.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/NewShriekNormalizedComplex.lean#L131). The attribute's comment: “part (4): omega\_X is f\_new^! of omega\_Y for a finite-type morphism over the base. RESTRICTED: the closed monoidal structure on the derived categories is an instance argument, and the two inputs the source names are hypotheses -- the identification R Hom(omega\_Y, omega\_Y) = O\_Y coming from omega\_Y being dualizing, and the unit half Lf^* O\_Y = O\_X of the monoidality of the derived pullback”.

> **Stacks Project, Tag 0AUE, part (4).** Let `f : X ⟶ Y` be a morphism of schemes of finite
> type over the base of [Stacks, Tag 0AU4] and let `ω_X^•` and `ω_Y^•` be the complexes
> normalized relative to `ω_S^•`, [Stacks, Tag 0AU5]. Then
>
> `f_new^! ω_Y^• ≅ ω_X^•`.
>
> The computation is the source's: `D_Y(ω_Y^•) ≅ 𝒪_Y` because `ω_Y^•` is dualizing, `Lf^*` carries
> the unit to the unit, and `D_X(𝒪_X) ≅ ω_X^•` by `Stacks.Duality.relativeDualObjUnit`. The
> statement is not an identity by definition: `Stacks.Duality.fNewShriek` unfolds the left hand
> side to `R𝓗om(Lf^* R𝓗om(ω_Y^•, ω_Y^•), ω_X^•)`, and the three steps above are what turn that
> into `ω_X^•`.

```lean
def fNewShriekObjIsoDualizing (f : X ⟶ Y) (ωX : DerivedCategory X.Modules)
    (ωY : DerivedCategory Y.Modules)
    (eY : (relativeDual ωY).obj (op ωY) ≅ 𝟙_ (DerivedCategory Y.Modules))
    (ef : (derivedPullback f).obj (𝟙_ (DerivedCategory Y.Modules)) ≅
      𝟙_ (DerivedCategory X.Modules)) :
    (fNewShriek f ωX ωY).obj ωY ≅ ωX
```

**`Stacks.Duality.fNewShriekStructureObjIsoDualizing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/NewShriekNormalizedComplex.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/NewShriekNormalizedComplex.lean#L163). The attribute's comment: “part (2): omega\_X is the new twisted inverse image of omega\_S along the structure morphism. RESTRICTED: the closed monoidal structure on the derived categories is an instance argument, and the identification R Hom(omega\_S, omega\_S) = O\_S implied by B.isDualizing together with the unit half Lpi^* O\_S = O\_X of the monoidality of the derived pullback are hypotheses”.

> **Stacks Project, Tag 0AUE, part (2).** For a scheme `X` of finite type over the base of
> [Stacks, Tag 0AU4], with structure morphism `π : X ⟶ S`, the complex normalized relative to
> `ω_S^•` is what `π_new^!` does to `ω_S^•`:
>
> `ω_X^• ≅ (X → S)_new^! ω_S^•`.
>
> This is `Stacks.Duality.fNewShriekObjIsoDualizing` at the structure morphism, read in the
> vocabulary of the Situation: the two inputs become `D_S(ω_S^•) ≅ 𝒪_S`, which is the homothety
> condition of the dualizing complex `B.isDualizing` names, and `Lπ^* 𝒪_S ≅ 𝒪_X`.

```lean
def fNewShriekStructureObjIsoDualizing
    (eS : (relativeDual B.dualizing).obj (op B.dualizing) ≅
      𝟙_ (DerivedCategory B.scheme.Modules))
    (ep : (derivedPullback Xb.str).obj (𝟙_ (DerivedCategory B.scheme.Modules)) ≅
      𝟙_ (DerivedCategory Xb.scheme.Modules)) :
    (fNewShriek Xb.str Xb.dualizing B.dualizing).obj B.dualizing ≅ Xb.dualizing
```

**`Stacks.Duality.existsUnique_iso_upperShriekPlus_of_isSeparated_nagata`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekNormalizedNagata.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekNormalizedNagata.lean#L135). The attribute's comment: “the closing remark, first half: omega\_X = (X -> S)^! omega\_S for X separated over S”.

> **[Stacks, Tag 0AUE], the closing remark, first half.** In Situation 0AU4, if `X` is
> separated over `S`, with structure morphism `p`, the dualizing complex `ω_X^•` normalized
> relative to `ω_S^•` is canonically isomorphic to `p^! ω_S^•`, for the upper shriek functor `p^!`
> of any compactification `j` of `p` ([Stacks, Tag 0A9Y]): exactly one isomorphism
> `ω_X^• ≅ p^!_j ω_S^•` carries the normalization `α_W` of `ω_X^•` to the canonical
> `(p^! ω_S^•)|_W ≅ (W → S)^! ω_S^•` for every open `W` separated over `S`.

```lean
theorem existsUnique_iso_upperShriekPlus_of_isSeparated_nagata {X S : Scheme.{u}} {p : X ⟶ S}
    {hp : IsFiniteTypeOverNoetherian p} {ωS : quasiCoherentDerivedCategoryPlusOfModel S}
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj) [IsSeparated p]
    (𝒦 : NormalizedOnOpens UpperShriek.nagata hp ωS) (j : CompactificationOf (Over.mk p)) :
    haveI := hp.base_noetherian
    ∃! e : 𝒦.complex ≅ (upperShriekPlus (ftsHomOf p
        (isShriekable_of_isSeparated_of_isFiniteTypeOverNoetherian hp).separatedFiniteType
        (isSeparatedFiniteType_id S) (Category.comp_id p)) j).obj ωS,
      ∀ (W : X.Opens) (hW : IsShriekable (W.ι ≫ p)),
        (UpperShriek.nagata.shriek W.ι (hp.isShriekable_ι W)).mapIso
            (e ≪≫ (DominatingCompactification.upperShriekPlusIso (ftsHomOf p
              (isShriekable_of_isSeparated_of_isFiniteTypeOverNoetherian hp).separatedFiniteType
              (isSeparatedFiniteType_id S) (Category.comp_id p)) j
              (nagataCompactification p
                (isShriekable_of_isSeparated_of_isFiniteTypeOverNoetherian hp))).app ωS) ≪≫
          upperShriekLocalIso UpperShriek.nagata hp
            (isShriekable_of_isSeparated_of_isFiniteTypeOverNoetherian hp) ωS hW =
        𝒦.localIso W hW
```

**`Stacks.Duality.NormalizedOnOpens.fNewShriekObjIsoNagata`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekNormalizedNagata.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekNormalizedNagata.lean#L167). The attribute's comment: “part (4)”.

> **[Stacks, Tag 0AUE] part (4).** In Situation 0AU4, let `f : X ⟶ Y` be a morphism of schemes
> of finite type over `S` and `ω_X^•`, `ω_Y^•` the dualizing complexes normalized relative to
> `ω_S^•` (for the upper shriek functors of Nagata compactifications). Then
> `ω_X^• ≅ f_new^! ω_Y^•`.

```lean
def fNewShriekObjIsoNagata (f : X ⟶ Y)
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj)
    (𝒦X : NormalizedOnOpens UpperShriek.nagata hp ωS)
    (𝒦Y : NormalizedOnOpens UpperShriek.nagata hq ωS) :
    stdComplex nagataCompactification 𝒦X ≅
      (fNewShriekStd f (stdComplex nagataCompactification 𝒦X)
        (stdComplex nagataCompactification 𝒦Y)).obj (stdComplex nagataCompactification 𝒦Y)
```

**`Stacks.Duality.NormalizedOnOpens.fNewShriekStructureObjIsoNagata`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekNormalizedNagata.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekNormalizedNagata.lean#L187). The attribute's comment: “part (2)”.

> **[Stacks, Tag 0AUE] part (2).** In Situation 0AU4, for `X` of finite type over `S` with
> structure morphism `p : X ⟶ S` and `ω_X^•` the dualizing complex normalized relative to `ω_S^•`,
> `ω_X^• ≅ (X → S)_new^! ω_S^•`, where `(X → S)_new^!` is formed with `ω_S^•` itself as the
> normalized complex of `S`.

```lean
def fNewShriekStructureObjIsoNagata
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj)
    (𝒦X : NormalizedOnOpens UpperShriek.nagata hp ωS) :
    stdComplex nagataCompactification 𝒦X ≅
      (fNewShriekStd p (stdComplex nagataCompactification 𝒦X) (baseStdComplex ωS)).obj
        (baseStdComplex ωS)
```

**`Stacks.Duality.NormalizedOnOpens.coherentDuality_spec_nagata`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekNormalizedNagata.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekNormalizedNagata.lean#L203). The attribute's comment: “part (3)”.

> **[Stacks, Tag 0AUE] part (3).** In Situation 0AU4, for `X` of finite type over `S` and
> `ω_X^•` normalized relative to `ω_S^•`, the duality `D_X = R𝓗om(-, ω_X^•)` is an involution of
> `D_Coh(𝒪_X)`: it carries `D_Coh(𝒪_X)` into itself, is an anti-equivalence of it with
> `id ≅ D_X ∘ D_X` given by biduality, exchanges `D^+_Coh` and `D^-_Coh`, and is an
> anti-equivalence of `D^b_Coh(𝒪_X)`.

```lean
theorem coherentDuality_spec_nagata
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj)
    (𝒦 : NormalizedOnOpens UpperShriek.nagata hp ωS) :
    haveI := hp.source_noetherian
    cohStd X (stdComplex nagataCompactification 𝒦) ∧
    (∀ M : Std X, cohStd X M →
      cohStd X ((dualInto (stdComplex nagataCompactification 𝒦)).obj (op M))) ∧
    (coherentDuality X
      (isDualizing_stdComplex nagataCompactification hωS 𝒦)).IsEquivalence ∧
    IsIso (coherentBiduality X
      (isDualizing_stdComplex nagataCompactification hωS 𝒦)) ∧
    (∀ M : Std X, cohStd X M →
      (plusCoh X M ↔
        minusCoh X ((dualInto (stdComplex nagataCompactification 𝒦)).obj (op M))) ∧
      (minusCoh X M ↔
        plusCoh X ((dualInto (stdComplex nagataCompactification 𝒦)).obj (op M)))) ∧
    (boundedCoherentDuality X
      (isDualizing_stdComplex nagataCompactification hωS 𝒦)).IsEquivalence
```

**`Stacks.Duality.NormalizedOnOpens.fNewShriekPlusCohNagata_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekNormalizedNagata.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekNormalizedNagata.lean#L245). The attribute's comment: “part (5)”.

> **[Stacks, Tag 0AUE] part (5).** In Situation 0AU4, for a morphism `f : X ⟶ Y` of schemes of
> finite type over `S`, `f_new^!` is a functor `D^+_Coh(𝒪_Y) ⥤ D^+_Coh(𝒪_X)` and
> `f_new^! M = D_X(Lf^* D_Y(M))` for `M ∈ D^+_Coh(𝒪_Y)`: for such `M` the complex
> `D_X(Lf^* D_Y(M))` lies in `D^+_Coh(𝒪_X)`, and it is the value of `f_new^!` at `M`.

```lean
theorem fNewShriekPlusCohNagata_obj (f : X ⟶ Y)
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj)
    (𝒦X : NormalizedOnOpens UpperShriek.nagata hp ωS)
    (𝒦Y : NormalizedOnOpens UpperShriek.nagata hq ωS) (M : (plusCoh Y).FullSubcategory) :
    plusCoh X ((dualInto (stdComplex nagataCompactification 𝒦X)).obj (op ((pull f).obj
        ((dualInto (stdComplex nagataCompactification 𝒦Y)).obj (op M.obj))))) ∧
      ((fNewShriekPlusCohNagata f hωS 𝒦X 𝒦Y).obj M).obj =
        (dualInto (stdComplex nagataCompactification 𝒦X)).obj (op ((pull f).obj
          ((dualInto (stdComplex nagataCompactification 𝒦Y)).obj (op M.obj))))
```

**`Stacks.Duality.NormalizedOnOpens.fNewShriekIsoRightAdjointNagata`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekNormalizedNagata.lean, line 263](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekNormalizedNagata.lean#L263). The attribute's comment: “part (6), first assertion”.

> **[Stacks, Tag 0AUE] part (6), first assertion.** In Situation 0AU4, for a proper morphism
> `f : X ⟶ Y` of schemes of finite type over `S` and the dualizing complexes `ω_X^•`, `ω_Y^•`
> normalized relative to `ω_S^•`, `f_new^!` is isomorphic to the restriction to `D^+_Coh(𝒪_Y)` of
> the right adjoint `a` of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` ([Stacks, Tag 0A9E]).

```lean
def fNewShriekIsoRightAdjointNagata
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj) [IsProper f]
    (𝒦X : NormalizedOnOpens UpperShriek.nagata hp ωS)
    (𝒦Y : NormalizedOnOpens UpperShriek.nagata hq ωS) :
    haveI := hq.source_noetherian
    haveI := hp.source_noetherian
    (plusCoh Y).ι ⋙ fNewShriekStd f (stdComplex nagataCompactification 𝒦X)
        (stdComplex nagataCompactification 𝒦Y) ≅
      ObjectProperty.ιOfLE plusCoh_le_qcoh ⋙ rightAdjointStd f
```

**`Stacks.Duality.NormalizedOnOpens.fNewShriekSheafHomIsoNagata`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekNormalizedNagata.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekNormalizedNagata.lean#L279). The attribute's comment: “part (6), the isomorphism Rf\_* RHom(K, f\_new^! M) = RHom(Rf\_* K, M)”.

> **[Stacks, Tag 0AUE] part (6), the duality isomorphism.** In Situation 0AU4, for a proper
> morphism `f : X ⟶ Y` of schemes of finite type over `S`, `K ∈ D^-_Coh(𝒪_X)` and
> `M ∈ D^+_Coh(𝒪_Y)`, there is a canonical isomorphism
> `Rf_* R𝓗om(K, f_new^! M) ≅ R𝓗om(Rf_* K, M)`.

```lean
def fNewShriekSheafHomIsoNagata
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj) [IsProper f]
    (𝒦X : NormalizedOnOpens UpperShriek.nagata hp ωS)
    (𝒦Y : NormalizedOnOpens UpperShriek.nagata hq ωS)
    (K : Std X) (hK : haveI := hp.source_noetherian; minusCoh X K)
    (M : (plusCoh Y).FullSubcategory) :
    (push f).obj (((sheafHom X).obj (op K)).obj
        ((fNewShriekStd f (stdComplex nagataCompactification 𝒦X)
          (stdComplex nagataCompactification 𝒦Y)).obj M.obj)) ≅
      ((sheafHom Y).obj (op ((push f).obj K))).obj M.obj
```

**`Stacks.Duality.NormalizedOnOpens.sheafHomDualizingIsoOfMinusCohNagata`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekNormalizedNagata.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekNormalizedNagata.lean#L295). The attribute's comment: “part (6), the isomorphism Rf\_* RHom(K, omega\_X) = RHom(Rf\_* K, omega\_Y)”.

> **[Stacks, Tag 0AUE] part (6), the duality for the dualizing complexes.** In Situation 0AU4,
> for a proper morphism `f : X ⟶ Y` of schemes of finite type over `S` and `K ∈ D^-_Coh(𝒪_X)`,
> `Rf_* R𝓗om(K, ω_X^•) ≅ R𝓗om(Rf_* K, ω_Y^•)`.

```lean
def sheafHomDualizingIsoOfMinusCohNagata
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj) [IsProper f]
    (𝒦X : NormalizedOnOpens UpperShriek.nagata hp ωS)
    (𝒦Y : NormalizedOnOpens UpperShriek.nagata hq ωS)
    (K : Std X) (hK : haveI := hp.source_noetherian; minusCoh X K) :
    (push f).obj (((sheafHom X).obj (op K)).obj (stdComplex nagataCompactification 𝒦X)) ≅
      ((sheafHom Y).obj (op ((push f).obj K))).obj (stdComplex nagataCompactification 𝒦Y)
```

**`Stacks.Duality.NormalizedOnOpens.upperShriekStdIsoFNewShriekNagata`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekNormalizedNagata.lean, line 310](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekNormalizedNagata.lean#L310). The attribute's comment: “the closing remark, second half: f\_new^! K = f^! K for K in D^+\_Coh”.

> **[Stacks, Tag 0AUE], the closing remark, `f_new^! = f^!`.** In Situation 0AU4, let
> `f : X ⟶ Y` be a separated morphism of schemes of finite type over `S` (for instance a morphism
> between schemes separated over `S`) and `ω_X^•`, `ω_Y^•` the dualizing complexes normalized
> relative to `ω_S^•`. For every compactification `j` of `f`, the upper shriek functor `f^!` of
> `j` ([Stacks, Tag 0A9Y]) satisfies `f^! K ≅ f_new^! K`, naturally in `K ∈ D^+_Coh(𝒪_Y)`.

```lean
def upperShriekStdIsoFNewShriekNagata
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj) [IsSeparated f]
    (𝒦X : NormalizedOnOpens UpperShriek.nagata hp ωS)
    (𝒦Y : NormalizedOnOpens UpperShriek.nagata hq ωS)
    (j : CompactificationOf (Over.mk f)) :
    haveI := hq.source_noetherian
    UpperShriekDuality.upperShriekStd (ftsHomSelf (isShriekable_of_isSeparated hpe hp hq)) j ≅
      (plusCoh Y).ι ⋙ fNewShriekStd f (stdComplex nagataCompactification 𝒦X)
        (stdComplex nagataCompactification 𝒦Y)
```

**`Stacks.Duality.newShriekPseudofunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekPseudofunctorNagata.lean, line 365](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekPseudofunctorNagata.lean#L365). The attribute's comment: “part (1)”.

> In Situation [Stacks, Tag 0AU4], let `ω_X^•` be the dualizing complex
> normalized relative to `ω_S^•` of each scheme `X` of finite type over `S`. The functors
> `f_new^! = D_X ∘ Lf^* ∘ D_Y : D^+_Coh(𝒪_Y) ⥤ D^+_Coh(𝒪_X)` and the arrows
> `(g ∘ f)_new^! ⟶ f_new^! ∘ g_new^!` turn `D^+_Coh` into a pseudofunctor from the category of
> schemes of finite type over `S` to the 2-category of categories: `X ↦ D^+_Coh(𝒪_X)`,
> `f ↦ f_new^!`, with `mapComp` the inverse of the comparison
> `f_new^! ∘ g_new^! ⟶ (g ∘ f)_new^!` given by the biduality `η_Y` ([Stacks, Tag 0A89]) and
> `mapId` the inverse of `η_X : id ⟶ (id_X)_new^!`
> (`Stacks.Duality.NewShriekPseudofunctor.comp`, `Stacks.Duality.NewShriekPseudofunctor.unit`,
> `Stacks.Duality.newShriekPseudofunctor_map_obj_obj`).

```lean
def newShriekPseudofunctor {S : Scheme.{u}} [IsNoetherian S]
    (ωS : quasiCoherentDerivedCategoryPlusOfModel S) (hωS : IsDualizingComplex ωS.obj.obj) :
    Pseudofunctor (LocallyDiscrete (SchemesOfFiniteTypeOver S)ᵒᵖ) Cat
```

## Tag 0BV3, a remark

[Tag 0BV3](https://stacks.math.columbia.edu/tag/0BV3) in the Stacks Project.

**`Stacks.Duality.fNewShriekTwistIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GlueingDualizingComplexes.lean, line 304](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GlueingDualizingComplexes.lean#L304). The attribute's comment: “RESTRICTED: the closed symmetric monoidal structure on the derived categories is an instance argument; the invertible twist with a chosen two-sided inverse, the identification of the twisted normalized complexes, and the compatibility of the derived pullback with the twist are hypotheses”.

> **Stacks Project, Tag 0BV3.** `f_new^!` does not depend on the choice of the dualizing
> complex on the base.
>
> Let `f : X ⟶ Y` be a morphism of schemes of finite type over the base of [Stacks, Tag 0AU4].
> Replacing `ω_S^•` by a second dualizing complex replaces it by `ω_S^• ⊗ ℒ` for an invertible
> `ℒ` in `D(𝒪_S)` ([Stacks, Tag 0ATP]), and the complexes normalized relative to it by the twists
> `ω_X^• ⊗ Lπ_X^*ℒ` and `ω_Y^• ⊗ Lπ_Y^*ℒ` ([Stacks, Tag 0A9T]). This says that the two resulting
> functors `f_new^!` are canonically isomorphic — an isomorphism of functors, not merely a family
> of isomorphisms of objects.
>
> The computation is the one sketched in the source. The twist passes through the target variable
> of `R𝓗om` by `Stacks.Duality.relativeDualTwistTargetIso`, is carried across `Lf^*` by `tw`, and
> cancels against the outer twist by `Stacks.Duality.relativeDualTwistCancelIso`; each of those is
> natural in the contravariant variable because it comes from
> `Stacks.Duality.parametrizedRightAdjointUniq`. The source's `p^!` does not appear: it is one
> route to the middle step and is not needed.

```lean
def fNewShriekTwistIso (f : X ⟶ Y)
    {ωX ωX' : DerivedCategory X.Modules} {ωY ωY' : DerivedCategory Y.Modules}
    {LX : DerivedCategory X.Modules} (hX : HasInverse LX)
    {LY : DerivedCategory Y.Modules} (hY : HasInverse LY)
    (eX : ωX' ≅ ωX ⊗ LX) (eY : ωY' ≅ ωY ⊗ LY)
    (tw : tensorRight LY ⋙ derivedPullback f ≅ derivedPullback f ⋙ tensorRight LX) :
    fNewShriek f ωX' ωY' ≅ fNewShriek f ωX ωY
```

**`Stacks.Duality.NormalizedOnOpens.fNewShriekIndependenceIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedTwist.lean, line 916](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedTwist.lean#L916).

> **Stacks Project, Tag 0BV3.** Let `S` be a Noetherian scheme with a dualizing complex `ω_S^•`
> and let `f : X ⟶ Y` be a morphism of schemes of finite type over `S`. Then the functor
>
> `f_new^! = D_X ∘ Lf^* ∘ D_Y : D^+_Coh(𝒪_Y) ⥤ D(𝒪_X)`
>
> of [Stacks, Tag 0AUE], formed with the dualizing complexes `ω_X^•`, `ω_Y^•` normalized relative to
> `ω_S^•`, does not depend on `ω_S^•` up to canonical isomorphism: for a second dualizing complex
> `ω_S'^•` on `S`, with `ω_X'^•`, `ω_Y'^•` normalized relative to it, the two functors are
> isomorphic. (It takes values in `D^+_Coh(𝒪_X)`, `Stacks.Duality.plusCoh_fNewShriek`.)
>
> The proof: `ω_X'^• ≅ f_new^! ω_Y'^•` (`stdComplexIsoFNewShriek`), and then
> `Stacks.Duality.fNewShriekStdIsoOfIso`, which uses that `R𝓗om(ω_Y'^•, ω_Y^•)` is invertible
> ([Stacks, Tag 0ATP]).

```lean
def fNewShriekIndependenceIso (hpe : f ≫ q = p)
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj)
    (hωS' : haveI := hp.base_noetherian; IsDualizingComplex ωS'.obj.obj)
    (𝒦X : NormalizedOnOpens (UpperShriek.ofCompactifications c) hp ωS)
    (𝒦Y : NormalizedOnOpens (UpperShriek.ofCompactifications c) hq ωS)
    (𝒦X' : NormalizedOnOpens (UpperShriek.ofCompactifications c) hp ωS')
    (𝒦Y' : NormalizedOnOpens (UpperShriek.ofCompactifications c) hq ωS') :
    (plusCoh Y).ι ⋙ fNewShriekStd f (stdComplex c 𝒦X') (stdComplex c 𝒦Y') ≅
      (plusCoh Y).ι ⋙ fNewShriekStd f (stdComplex c 𝒦X) (stdComplex c 𝒦Y)
```

## Tag 0B6X, an example

[Tag 0B6X](https://stacks.math.columbia.edu/tag/0B6X) in the Stacks Project.

**`Stacks.Duality.NormalizedOnOpens.sheafHomDualizingIsoNagata`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekProperQCohNagata.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NewShriekProperQCohNagata.lean#L51).

> **[Stacks, Tag 0B6X], the second isomorphism.** In Situation 0AU4, for a proper `f : X ⟶ Y` of
> schemes of finite type over `S`, the dualizing complexes `ω_X^•`, `ω_Y^•` normalized relative to
> `ω_S^•` and every `L` in `D_QCoh(𝒪_X)`, `Rf_* R𝓗om(L, ω_X^•) ≅ R𝓗om(Rf_* L, ω_Y^•)`: the sheafy
> trace map at `ω_Y^•` composed with `a(ω_Y^•) ≅ ω_X^•` ([Stacks, Tag 0AUD]).

```lean
def sheafHomDualizingIsoNagata
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj) [IsProper f]
    (𝒦X : NormalizedOnOpens UpperShriek.nagata hp ωS)
    (𝒦Y : NormalizedOnOpens UpperShriek.nagata hq ωS)
    (L : Std X) (hL : qcoh X L) :
    (push f).obj (((sheafHom X).obj (op L)).obj (stdComplex nagataCompactification 𝒦X)) ≅
      ((sheafHom Y).obj (op ((push f).obj L))).obj (stdComplex nagataCompactification 𝒦Y)
```

**`Stacks.Duality.NormalizedOnOpens.traceNagata`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedProperNagata.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedProperNagata.lean#L107).

> **[Stacks, Tag 0B6X], the trace map.** In Situation 0AU4, for a proper `f : X ⟶ Y` of schemes
> of finite type over `S` and the dualizing complexes `ω_X^•`, `ω_Y^•` normalized relative to
> `ω_S^•`, the canonical arrow `Tr_f : Rf_* ω_X^• ⟶ ω_Y^•`: the trace map of
> [Stacks, Section 0AWG] read through `a(ω_Y^•) ≅ ω_X^•` ([Stacks, Tag 0AUD]).

```lean
def traceNagata
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj) [IsProper f]
    (𝒦X : NormalizedOnOpens UpperShriek.nagata hp ωS)
    (𝒦Y : NormalizedOnOpens UpperShriek.nagata hq ωS) :
    haveI := hq.source_noetherian
    haveI := hp.source_noetherian
    (quasiCoherentDerivedPushforward f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
        𝒦X.complex.obj ⟶ 𝒦Y.complex.obj
```

**`Stacks.Duality.NormalizedOnOpens.homEquivNagata`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedProperNagata.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedProperNagata.lean#L122).

> **[Stacks, Tag 0B6X], the first isomorphism.** In Situation 0AU4, for a proper `f : X ⟶ Y` of
> schemes of finite type over `S`, the dualizing complexes `ω_X^•`, `ω_Y^•` normalized relative to
> `ω_S^•` and `L` in `D_QCoh(𝒪_X)`, `Hom_X(L, ω_X^•) = Hom_Y(Rf_* L, ω_Y^•)`; it sends `u` to
> `Tr_f ∘ Rf_* u` (`homEquivNagata_apply`).

```lean
def homEquivNagata
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj) [IsProper f]
    (𝒦X : NormalizedOnOpens UpperShriek.nagata hp ωS)
    (𝒦Y : NormalizedOnOpens UpperShriek.nagata hq ωS)
    (L : quasiCoherentDerivedCategory X) :
    haveI := hq.source_noetherian
    haveI := hp.source_noetherian
    (L ⟶ 𝒦X.complex.obj) ≃
      ((quasiCoherentDerivedPushforward f
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj L ⟶ 𝒦Y.complex.obj)
```

**`Stacks.Duality.NormalizedOnOpens.homEquivNagata_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedProperNagata.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedProperNagata.lean#L137).

> **[Stacks, Tag 0B6X], the first isomorphism is produced by the trace map**:
> `homEquivNagata` sends `u : L ⟶ ω_X^•` to `Tr_f ∘ Rf_* u`.

```lean
theorem homEquivNagata_apply
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj) [IsProper f]
    (𝒦X : NormalizedOnOpens UpperShriek.nagata hp ωS)
    (𝒦Y : NormalizedOnOpens UpperShriek.nagata hq ωS)
    (L : quasiCoherentDerivedCategory X) (u : L ⟶ 𝒦X.complex.obj) :
    haveI := hq.source_noetherian
    haveI := hp.source_noetherian
    homEquivNagata hpe hωS 𝒦X 𝒦Y L u =
      (quasiCoherentDerivedPushforward f
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).map u ≫
        traceNagata hpe hωS 𝒦X 𝒦Y
```

## Tag 0AX4, a remark

[Tag 0AX4](https://stacks.math.columbia.edu/tag/0AX4) in the Stacks Project.

**`Stacks.Duality.NormalizedOnOpens.exists_finitePushforwardIso_trace_nagata`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/FiniteDualizingComplexNagata.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/FiniteDualizingComplexNagata.lean#L54).

> **[Stacks, Tag 0AX4]** Let `S` be Noetherian with a dualizing complex `ω_S^•`, `f : X ⟶ Y` a
> finite morphism of schemes of finite type over `S`, and `ω_X^•`, `ω_Y^•` the dualizing complexes
> normalized relative to `ω_S^•`. Then `R𝓗om(f_* 𝒪_X, ω_Y^•)` lies in `D⁺_QCoh(f_* 𝒪_X)` and
> `f_* ω_X^• ≅ R𝓗om(f_* 𝒪_X, ω_Y^•)` there, by an isomorphism through which the trace map
> `Tr_f : Rf_* ω_X^• ⟶ ω_Y^•` of [Stacks, Tag 0B6X] is
> `Rf_* ω_X^• = f_* ω_X^• = R𝓗om(f_* 𝒪_X, ω_Y^•) ⟶ ω_Y^•`, evaluation at `1` (the counit of
> `res ⊣ R𝓗om(f_* 𝒪_X, -)`).

```lean
theorem exists_finitePushforwardIso_trace_nagata
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj) [IsFinite f]
    (𝒦X : NormalizedOnOpens UpperShriek.nagata hp ωS)
    (𝒦Y : NormalizedOnOpens UpperShriek.nagata hq ωS) :
    haveI := hq.source_noetherian
    haveI := hp.source_noetherian
    DerivedCategoryB.derivedCategoryBPlus
        (SheafOfModules.isQuasicoherent (pushforwardRing f.base X.ringCatSheaf))
        (((structureSheafModelEquiv Y).inverse ⋙ derivedHomSheaf f ⋙
          (pushforwardRingModelEquiv f).functor).obj 𝒦Y.complex.obj.obj) ∧
      ∃ e : ((derivedQuasicoherentPushforwardOverRingEquivalence f).functor.obj
          𝒦X.complex.obj).obj ≅ ((structureSheafModelEquiv Y).inverse ⋙ derivedHomSheaf f ⋙
            (pushforwardRingModelEquiv f).functor).obj 𝒦Y.complex.obj.obj,
        (ObjectProperty.ι _).map (traceOfCompactifications nagataCompactification hpe hωS 𝒦X 𝒦Y) =
          (derivedPushforwardOverRingCompRestrictScalarsIso.{u} f).hom.app
              𝒦X.complex.obj.obj ≫
            (scalarRestriction f).mapDerivedCategory.map e.hom ≫
            (scalarRestrictionAdjunctionLS f).counit.app 𝒦Y.complex.obj.obj
```

## Tag 0B6W, a remark

[Tag 0B6W](https://stacks.math.columbia.edu/tag/0B6W) in the Stacks Project.

**`Stacks.Duality.NormalizedOnOpens.twistedInverseImageObjIsoPullbackTensorOfFlat`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/NormalizedFlatProperPullbackTensor.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/NormalizedFlatProperPullbackTensor.lean#L63). The attribute's comment: “the second canonical isomorphism a(ω\_Y^•) = Lf^* ω\_Y^• ⊗ ω\_\{X/Y}^•”.

> **[Stacks, Remark 0B6W], the second canonical isomorphism.** For a flat proper morphism
> `f : X ⟶ Y` of schemes of finite type over a Noetherian `S`, with `a` the right adjoint of
> `Rf_*`, there is a canonical isomorphism `a(K) ≅ Lf^* K ⊗ᴸ a(𝒪_Y)` for `K ∈ D⁺_QCoh(𝒪_Y)`: through
> `a = f^!` (at the Nagata compactification of `f`) it is the inverse of `μ_{f,K}`
> ([Stacks, Tag 0B6U] (e)).

```lean
def twistedInverseImageObjIsoPullbackTensorOfFlat [IsProper f] [Flat f]
    (K : quasiCoherentDerivedCategoryPlusOfModel Y) :
    haveI := hq.source_noetherian
    haveI := hp.source_noetherian
    (twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj K.obj ≅
      ((quasiCoherentDerivedTensor X).obj ((quasiCoherentDerivedPullback' f).obj K.obj)).obj
        ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
          (DerivedPushforward.derivedStructureSheaf Y))
```

**`Stacks.Duality.NormalizedOnOpens.isoPullbackTensorOfFlatNagata`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/NormalizedFlatProperPullbackTensor.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/NormalizedFlatProperPullbackTensor.lean#L99). The attribute's comment: “ω\_X^• = a(ω\_Y^•) = Lf^* ω\_Y^• ⊗ ω\_\{X/Y}^• in D(O\_X)”.

> **[Stacks, Remark 0B6W].** Let `f : X ⟶ Y` be a flat proper morphism of schemes of finite type
> over `S`, where `S` is Noetherian with a dualizing complex `ω_S^•`, and `ω_X^•`, `ω_Y^•` the
> dualizing complexes normalized relative to `ω_S^•`. With `a` the right adjoint of `Rf_*` and
> `ω_{X/Y}^• = a(𝒪_Y)` the relative dualizing complex, the canonical isomorphism
> `ω_X^• ≅ a(ω_Y^•) ≅ Lf^* ω_Y^• ⊗ᴸ ω_{X/Y}^•` in `D(𝒪_X)`: the inverse of
> `Stacks.Duality.twistedInverseImageObjIsoNagata` ([Stacks, Tag 0AUD]) followed by
> `twistedInverseImageObjIsoPullbackTensorOfFlat`.

```lean
def isoPullbackTensorOfFlatNagata
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj) [IsProper f] [Flat f]
    (𝒦X : NormalizedOnOpens UpperShriek.nagata hp ωS)
    (𝒦Y : NormalizedOnOpens UpperShriek.nagata hq ωS) :
    haveI := hq.source_noetherian
    haveI := hp.source_noetherian
    𝒦X.complex.obj ≅ ((quasiCoherentDerivedTensor X).obj
        ((quasiCoherentDerivedPullback' f).obj 𝒦Y.complex.obj)).obj
          ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
            (DerivedPushforward.derivedStructureSheaf Y))
```

**`Stacks.Duality.NormalizedOnOpens.nonempty_iso_pullback_tensor_of_flat_nagata`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedCohenMacaulayNagata.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedCohenMacaulayNagata.lean#L51).

> **[Stacks, Tag 0B6W]** Let `f : X ⟶ Y` be a flat proper morphism of schemes of finite type over
> `S`, where `S` is Noetherian with a dualizing complex `ω_S^•`, and `ω_X^•`, `ω_Y^•` the dualizing
> complexes normalized relative to `ω_S^•`. With `a` the right adjoint of `Rf_*` and
> `ω_{X/Y}^• = a(𝒪_Y)` the relative dualizing complex,
> `ω_X^• ≅ a(ω_Y^•) ≅ Lf^* ω_Y^• ⊗ᴸ ω_{X/Y}^•` in `D(𝒪_X)`.

```lean
theorem nonempty_iso_pullback_tensor_of_flat_nagata
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj) [IsProper f] [Flat f]
    (𝒦X : NormalizedOnOpens UpperShriek.nagata hp ωS)
    (𝒦Y : NormalizedOnOpens UpperShriek.nagata hq ωS) :
    haveI := hq.source_noetherian
    haveI := hp.source_noetherian
    Nonempty (𝒦X.complex.obj ≅ ((quasiCoherentDerivedTensor X).obj
        ((quasiCoherentDerivedPullback' f).obj 𝒦Y.complex.obj)).obj
          ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
            (DerivedPushforward.derivedStructureSheaf Y)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.20, Tag 0AU5](https://stacks.math.columbia.edu/tag/0AU5)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
