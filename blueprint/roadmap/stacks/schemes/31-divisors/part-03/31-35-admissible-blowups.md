---
declaration: section
origin: cited
lean: Stacks.Blowup.IsAdmissibleBlowup, Stacks.Blowup.IsAdmissibleBlowup.comp, Stacks.Blowup.exists_admissibleBlowup_isPullback, Stacks.Blowup.exists_admissibleBlowup_dominating, Stacks.Blowup.exists_admissibleBlowup_disjoint_open_cover, Stacks.Blowup.exists_admissibleBlowup_pairwise_disjoint_open_cover, Stacks.DenominatorBlowup.isAdmissibleBlowup_denominatorIdealData, Stacks.DenominatorBlowup.isSectionOver_and_isAdmissibleBlowup_and_exists_differenceTwist
statement: formalized
proof: formalized
---

# 31.35 Admissible blowups

Section 31.35 of the Stacks Project, [Tag 080J](https://stacks.math.columbia.edu/tag/080J). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 080K, a definition

[Tag 080K](https://stacks.math.columbia.edu/tag/080K) in the Stacks Project.

**`Stacks.Blowup.IsAdmissibleBlowup`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Admissible.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Admissible.lean#L80).

> A morphism `f : X' ⟶ X` is a **`U`-admissible blowup** if there is a quasi-coherent sheaf of
> ideals `I` on `X` whose closed subscheme is of finite presentation over `X` and supported away
> from `U`, together with an isomorphism of `X'` with the blowup of `X` in `I` carrying the blowup
> morphism to `f`.

```lean
abbrev IsAdmissibleBlowup (U : X.Opens) (f : X' ⟶ X) : Prop
```

## Tag 080L, a lemma

[Tag 080L](https://stacks.math.columbia.edu/tag/080L) in the Stacks Project.

**`Stacks.Blowup.IsAdmissibleBlowup.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/AdmissibleComposition.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/AdmissibleComposition.lean#L262).

> **Stacks Project, Tag 080L.** Let `X` be a quasi-compact and quasi-separated scheme and
> `U ⊆ X` an open subscheme. If `b : X' ⟶ X` is a `U`-admissible blowup and `b' : X'' ⟶ X'` is a
> `b⁻¹(U)`-admissible blowup, then the composite `b' ≫ b : X'' ⟶ X` is a `U`-admissible blowup.
>
> The single centre is the product of the first centre with the second-centre ideal of
> `Stacks.Blowup.exists_secondCentre`, and the two halves of [Stacks, Tag 080B] do the rest. The
> support clause that `…comp_of_secondCentreIdeal` asks for comes from
> `AlgebraicGeometry.supportSet_mul_eq_union_image` together with
> `AlgebraicGeometry.Scheme.IdealSheafData.support_mul`: the support of the product centre is the
> support of the first centre together with the image of the support of the second, and it
> contains the support of `J`.

```lean
theorem IsAdmissibleBlowup.comp [CompactSpace X] [QuasiSeparatedSpace X]
    (U : X.Opens) (b : X' ⟶ X) (b' : X'' ⟶ X')
    (hb : IsAdmissibleBlowup U b) (hb' : IsAdmissibleBlowup (b ⁻¹ᵁ U) b') :
    IsAdmissibleBlowup U (b' ≫ b)
```

## Tag 080M, a lemma

[Tag 080M](https://stacks.math.columbia.edu/tag/080M) in the Stacks Project.

**`Stacks.Blowup.exists_admissibleBlowup_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/AdmissibleExtension.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/AdmissibleExtension.lean#L402).

> **Stacks Project, Tag 080M.** A blowup admissible over the intersection of two quasi-compact
> opens extends to a blowup of the ambient scheme admissible over the first open, with its
> restriction to the second open given by a cartesian square.

```lean
public theorem exists_admissibleBlowup_isPullback
    {X V' : Scheme.{u}} [CompactSpace X] [QuasiSeparatedSpace X]
    (U V : X.Opens) (hU : IsCompact (U : Set X))
    (hV : IsCompact (V : Set X)) (b : V' ⟶ V.toScheme)
    (hb : IsAdmissibleBlowup (V.ι ⁻¹ᵁ U) b) :
    ∃ (X' : Scheme.{u}) (f : X' ⟶ X),
      IsAdmissibleBlowup U f ∧ ∃ g : V' ⟶ X', IsPullback b g V.ι f
```

## Tag 080N, a lemma

[Tag 080N](https://stacks.math.columbia.edu/tag/080N) in the Stacks Project.

**`Stacks.Blowup.exists_admissibleBlowup_dominating`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/AdmissibleDominating.lean, line 437](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/AdmissibleDominating.lean#L437).

> **Stacks Project, Tag 080N.** Let `U` be an open subscheme of a scheme `X` and let
> `b_i : Y_i ⟶ X`, `i ∈ ι`, be a finite family of `U`-admissible blowups. There is a `U`-admissible
> blowup `b : X' ⟶ X` which factors through every `b_i`, with each factor map `X' ⟶ Y_i` itself a
> `b_i⁻¹(U)`-admissible blowup.
>
> Take `X'` to be the blowup of `X` in the product `I = ∏ I_i` of the centres. The product is again
> of finite type and supported away from `U`, so `b` is `U`-admissible. Writing `I = I_i · J_i`,
> blowing up a product is blowing up the factors in succession (Stacks tag 080A), so `X'` is the
> blowup of `Y_i` in the inverse image of `J_i`; flat base change along the isomorphism
> `Y_i ≅ Bl_{I_i}(X)` (Stacks tag 0805) identifies that inverse image taken on `Y_i` with the one
> taken on `Bl_{I_i}(X)`. The inverse image of `J_i` on `Y_i` is again of finite type and supported
> away from `b_i⁻¹(U)`, so the factor map is `b_i⁻¹(U)`-admissible.

```lean
theorem exists_admissibleBlowup_dominating {X : Scheme.{u}} (U : X.Opens)
    {ι : Type*} [Finite ι] (Y : ι → Scheme.{u})
    (f : ∀ i, Y i ⟶ X)
    (hf : ∀ i, IsAdmissibleBlowup U (f i)) :
    ∃ (X' : Scheme.{u}) (b : X' ⟶ X),
      IsAdmissibleBlowup U b ∧
        ∃ g : ∀ i, X' ⟶ Y i,
          (∀ i, g i ≫ f i = b) ∧
            (∀ i, IsAdmissibleBlowup (f i ⁻¹ᵁ U) (g i))
```

## Tag 080P, a lemma

[Tag 080P](https://stacks.math.columbia.edu/tag/080P) in the Stacks Project.

**`Stacks.Blowup.exists_admissibleBlowup_disjoint_open_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/AdmissibleSeparation.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/AdmissibleSeparation.lean#L375).

> **Stacks Project, Tag 080P.** Let `X` be a quasi-compact and quasi-separated scheme and let
> `U, V` be disjoint quasi-compact open subschemes of `X`. Then there is a `U ∪ V`-admissible
> blowup `b : X' ⟶ X` such that `X'` is the disjoint union of two open subschemes `X' = X'₁ ⨿ X'₂`
> with `b⁻¹(U) ⊆ X'₁` and `b⁻¹(V) ⊆ X'₂`.

```lean
theorem exists_admissibleBlowup_disjoint_open_cover
    (X : Scheme.{u}) [CompactSpace X] [QuasiSeparatedSpace X]
    (U V : X.Opens) (hU : IsCompact (U : Set X))
    (hV : IsCompact (V : Set X)) (hUV : Disjoint U V) :
    ∃ (X' : Scheme.{u}) (b : X' ⟶ X) (U₁ U₂ : X'.Opens),
      IsAdmissibleBlowup (U ⊔ V) b ∧
        Disjoint U₁ U₂ ∧ U₁ ⊔ U₂ = ⊤ ∧
          b ⁻¹ᵁ U ≤ U₁ ∧ b ⁻¹ᵁ V ≤ U₂
```

**`Stacks.Blowup.exists_admissibleBlowup_pairwise_disjoint_open_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/AdmissibleSeparation.lean, line 476](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/AdmissibleSeparation.lean#L476). The attribute's comment: “stated for a finite family of pairwise disjoint quasi-compact opens; the source's two-piece statement is the case of a two-element index type”.

> **Stacks Project, Tag 080P for a finite family.** Let `X` be a quasi-compact and
> quasi-separated scheme and let `U_i`, `i ∈ ι`, be a finite family of pairwise disjoint
> quasi-compact open subschemes of `X`. Then there is a `⋃ U_i`-admissible blowup `b : X' ⟶ X`
> such that `X'` is the disjoint union of open subschemes `X'_i`, `i ∈ ι`, with
> `b⁻¹(U_i) ⊆ X'_i`.
>
> This is the form in which the source iterates Tag 080P: the decomposition of `U` into the
> finitely many loci where a locally constant invariant takes a fixed value is separated by a
> single blowup. The proof is that of the two-piece case verbatim. Choose quasi-coherent sheaves
> of ideals `ℐ_i` of finite type with `X ∖ U_i = V(ℐ_i)` and blow up `∑ ℐ_i`; the piece `X'_i` is
> the union of the affine charts of Stacks tag 0804 attached to the sections of `ℐ_i`. Two such
> pieces are disjoint because `ℐ_iℐ_j` is contained in the nilradical for `i ≠ j`, and they cover
> because over an affine open every section of `(∑ ℐ_i)(W)` is a sum of sections of the
> `ℐ_i(W)`.

```lean
theorem exists_admissibleBlowup_pairwise_disjoint_open_cover
    (X : Scheme.{u}) [CompactSpace X] [QuasiSeparatedSpace X]
    {ι : Type*} [Finite ι] (U : ι → X.Opens) (hU : ∀ i, IsCompact (U i : Set X))
    (hUd : Pairwise fun i j => Disjoint (U i) (U j)) :
    ∃ (X' : Scheme.{u}) (b : X' ⟶ X) (V : ι → X'.Opens),
      IsAdmissibleBlowup (⨆ i, U i) b ∧
        (Pairwise fun i j => Disjoint (V i) (V j)) ∧ ⨆ i, V i = ⊤ ∧
          ∀ i, b ⁻¹ᵁ U i ≤ V i
```

## Tag 0ESL, a lemma

[Tag 0ESL](https://stacks.math.columbia.edu/tag/0ESL) in the Stacks Project.

**`Stacks.DenominatorBlowup.isAdmissibleBlowup_denominatorIdealData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/DenominatorAdmissible.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/DenominatorAdmissible.lean#L210). The attribute's comment: “the blowup in the ideal of denominators is U-admissible”.

> Let `X` be a locally Noetherian scheme, `L` an invertible `𝒪_X`-module and `s` a regular
> meromorphic section of `L`.  Let `U ⊆ X` be the maximal open subscheme such that `s` corresponds
> to a section of `L` over `U`.  Then the blowup `b : X' ⟶ X` of `X` in the ideal of denominators
> of `s` is `U`-admissible.

```lean
theorem isAdmissibleBlowup_denominatorIdealData [IsLocallyNoetherian X]
    (_hs : IsRegularMeromorphicSection X.sheaf L s) :
    Stacks.Blowup.IsAdmissibleBlowup (sectionOpens L s)
      (Stacks.Blowup.blowUpToBase (denominatorIdealData X L s))
```

**`Stacks.DenominatorBlowup.isSectionOver_and_isAdmissibleBlowup_and_exists_differenceTwist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/DenominatorExceptionalDivisor.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/DenominatorExceptionalDivisor.lean#L303). The attribute's comment: “the whole statement: U is maximal, the blowup in the ideal of denominators is U-admissible, and there is an effective Cartier divisor D with b^* L = O(D - E) carrying the last clause in the form the source's own proof gives it, that b^* s is the regular global section of b^* L(E) whose zero scheme is D”.

> **Stacks Project, Tag 0ESL.**  Let `X` be a locally Noetherian scheme, `L` an invertible
> `𝒪_X`-module and `s` a regular meromorphic section of `L`.  Let `U ⊆ X` be the maximal open
> subscheme such that `s` corresponds to a section of `L` over `U`.  Then:
>
> * `U` really is maximal — `s` corresponds to a section of `L` over `U`, and every open subscheme
>   over which `s` corresponds to a section of `L` is contained in `U`;
> * the blowup `b : X' ⟶ X` of `X` in the ideal of denominators of `s` is `U`-admissible;
> * there is an effective Cartier divisor `D ⊆ X'` and an isomorphism `b^* L ≅ 𝒪_{X'}(D - E)`,
>   where `E ⊆ X'` is the exceptional divisor, through which the meromorphic section `b^* s`
>   corresponds to the meromorphic section `1_D ⊗ (1_E)^{-1}`.
>
> The three clauses are
> `Stacks.DenominatorBlowup.isSectionOver_sectionOpens` together with
> `Stacks.DenominatorBlowup.le_sectionOpens`,
> `Stacks.DenominatorBlowup.isAdmissibleBlowup_denominatorIdealData` carried from
> `Stacks.Blowup.blowUp` to `AlgebraicGeometry.blowUp` along
> `AlgebraicGeometry.blowUpIso` — the two constructions of the blowup are isomorphic over `X`, so
> the morphism `b` of the admissibility clause is the morphism `b` of the divisor clause — and
> `Stacks.DenominatorBlowup.exists_isEffectiveCartierDivisor_pullL_iso_differenceTwist`.
>
> The last clause is stated as in that theorem, as the conjunction of the identities that pin down
> `D`, the isomorphism and `b^* s` together; see its docstring and the implementation notes of
> `StacksFrontier/AlgebraicGeometry/Blowup/DenominatorExceptional.lean`.

```lean
theorem isSectionOver_and_isAdmissibleBlowup_and_exists_differenceTwist
    [IsLocallyNoetherian X] (hs : IsRegularMeromorphicSection X.sheaf L s) :
    (IsSectionOver L s (sectionOpens L s) ∧
        ∀ V : Opens X, IsSectionOver L s V → V ≤ sectionOpens L s) ∧
      Stacks.Blowup.IsAdmissibleBlowup (sectionOpens L s) (blowHom L s) ∧
      ∃ D : (blow L s).IdealSheafData, Stacks.Divisors.IsEffectiveCartierDivisor D ∧
        ∃ (i : pullL L s ≅ Stacks.Divisors.differenceTwist D (exceptional L s))
          (e : Stacks.Divisors.invertibleSheaf' D ≅ pullLTensorExceptionalTwist L s),
          i = untwistExceptional L s e ∧
          Scheme.Modules.Hom.app e.hom ⊤
              ((Stacks.Divisors.canonicalSection' D).eval (op ⊤)) =
            exceptionalTensorSection L s hL ∧
          ((pullLTensorExceptionalTwistIso L s).hom.val.app (op ⊤))
              (exceptionalTensorSection L s hL) = exceptionalHomSection L s hL ∧
          exceptionalToPullL L s hL ≫ DenominatorIdeal.toK (blow L s) (pullL L s) =
            exceptionalι L s ≫
              DenominatorIdeal.sectionMap (blow L s) (pullL L s) (pullS L s)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.35, Tag 080J](https://stacks.math.columbia.edu/tag/080J)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
