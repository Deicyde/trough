---
declaration: section
origin: cited
lean: CategoryTheory.GrothendieckTopology.IsQuasiCompactObject, StacksProblem.finiteSubcovering_imp_finiteRefinement, StacksProblem.finiteRefinement_imp_quasiCompact, StacksProblem.exists_finiteRefinement_not_finiteSubcovering, StacksProblem.exists_quasiCompact_not_finiteRefinement, CategoryTheory.GrothendieckTopology.isQuasiCompactObject_iff_isQuasiCompact_sheafifiedYoneda, CategoryTheory.Sheaf.IsQuasiCompact, CategoryTheory.GrothendieckTopology.IsQuasiCompactTopos
statement: formalized
proof: formalized
---

# 7.17 Quasi-compact objects and colimits

Section 7.17 of the Stacks Project, [Tag 090G](https://stacks.math.columbia.edu/tag/090G). 10 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 090H, a definition

[Tag 090H](https://stacks.math.columbia.edu/tag/090H) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.IsQuasiCompactObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/QuasiCompact.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/QuasiCompact.lean#L46). The attribute's comment: “A quasi-compact object of a site: every covering is refined by one that factors through only finitely many of its members.”. References: SGA 4 VI (1.1); SGA 6 II (2.1.1).

> An object `U` of a site `C` is *quasi-compact* if every covering `𝒰 = {U i ⟶ U}` of `U`,
> given as a `PreZeroHypercover` whose generated sieve `sieve₀` belongs to `J`, admits a covering
> `𝒱 = {V j ⟶ U}` together with a morphism `φ : 𝒱 ⟶ 𝒰` over `𝟙 U` whose index map `φ.s₀` has
> finite image.

```lean
def IsQuasiCompactObject (J : GrothendieckTopology C) (U : C) : Prop
```

## Tag 0D05, a lemma

[Tag 0D05](https://stacks.math.columbia.edu/tag/0D05) in the Stacks Project.

**`StacksProblem.finiteSubcovering_imp_finiteRefinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/QuasiCompact/FiniteRefinements.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/QuasiCompact/FiniteRefinements.lean#L72). The attribute's comment: “(3)⇒(2)”.

> **Statement (A) — (3) ⇒ (2).** If `U` has the finite subcovering property,
> then `U` has the finite refinement property.

```lean
theorem finiteSubcovering_imp_finiteRefinement
    (K : Pretopology C) (U : C) (h : HasFiniteSubcovering K U) :
    HasFiniteRefinement K U
```

**`StacksProblem.finiteRefinement_imp_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/QuasiCompact/FiniteRefinements.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/QuasiCompact/FiniteRefinements.lean#L82). The attribute's comment: “(2)⇒(1)”.

> **Statement (B) — (2) ⇒ (1).** If `U` has the finite refinement property,
> then `U` is quasi-compact.

```lean
theorem finiteRefinement_imp_quasiCompact
    (K : Pretopology C) (U : C) (h : HasFiniteRefinement K U) :
    IsQuasiCompact K U
```

**`StacksProblem.exists_finiteRefinement_not_finiteSubcovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/QuasiCompact/FiniteRefinements.lean, line 519](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/QuasiCompact/FiniteRefinements.lean#L519). The attribute's comment: “(2)⇏(3)”.

> **Statement (D) — (2) ⇏ (3).** There exists a site (`C`, `K`, `U`) such that
> `U` has the finite refinement property but does not have the finite subcovering
> property.

```lean
theorem exists_finiteRefinement_not_finiteSubcovering :
    ∃ (C : Type) (_ : Category C) (_ : Limits.HasPullbacks C)
      (K : Pretopology C) (U : C), HasFiniteRefinement K U ∧ ¬ HasFiniteSubcovering K U
```

**`StacksProblem.exists_quasiCompact_not_finiteRefinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/QuasiCompact/FiniteRefinements.lean, line 736](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/QuasiCompact/FiniteRefinements.lean#L736). The attribute's comment: “(1)⇏(2)”.

> **Statement (C) — (1) ⇏ (2).** There exists a site (`C`, `K`, `U`) such that
> `U` is quasi-compact but does not have the finite refinement property.

```lean
theorem exists_quasiCompact_not_finiteRefinement :
    ∃ (C : Type) (_ : Category C) (_ : Limits.HasPullbacks C)
      (K : Pretopology C) (U : C), IsQuasiCompact K U ∧ ¬ HasFiniteRefinement K U
```

## Tag 0D06, a lemma

[Tag 0D06](https://stacks.math.columbia.edu/tag/0D06) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.isQuasiCompactObject_iff_isQuasiCompact_sheafifiedYoneda`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/QuasiCompact/ObjectsAndColimits.lean, line 927](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/QuasiCompact/ObjectsAndColimits.lean#L927). The attribute's comment: “An object of a site is quasi-compact if and only if the sheafification of the presheaf it represents is a quasi-compact object of the topos of sheaves of sets.”. References: SGA 4 VI (1.2).

> **Stacks 0D06.** Let `C` be a site and `U` an object of `C`. The following are equivalent:
>
> 1. `U` is a quasi-compact object of the site (Stacks 090H): every covering of `U` is refined by a
>    covering that factors through only finitely many of its members;
> 2. for every surjection of sheaves `∐_{i ∈ I} F i ⟶ h_U^#` there is a finite `T ⊆ I` for which
>    `∐_{i ∈ T} F i ⟶ h_U^#` is still surjective, i.e. `h_U^#` is a quasi-compact object of the
>    topos `Sh(C)` (Stacks 0D07).
>
> Here `h_U^# = (Sheaf.sheafifiedYoneda J).obj U` is the sheafification of the presheaf represented
> by `U`.

```lean
public theorem isQuasiCompactObject_iff_isQuasiCompact_sheafifiedYoneda {C : Type u}
    [Category.{v} C] (J : GrothendieckTopology C) (U : C) :
    J.IsQuasiCompactObject U ↔ Sheaf.IsQuasiCompact ((Sheaf.sheafifiedYoneda J).obj U)
```

## Tag 0D07, a definition

[Tag 0D07](https://stacks.math.columbia.edu/tag/0D07) in the Stacks Project.

**`CategoryTheory.Sheaf.IsQuasiCompact`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/QuasiCompact.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/QuasiCompact.lean#L76). The attribute's comment: “A quasi-compact object of the topos of sheaves of sets on a site.”. References: SGA 4 IV (8.7), “more general”; SGA 4 IX (1.2).

> An object `F` of the topos `Sh(C)` of sheaves of sets on a site is *quasi-compact* if for
> every locally surjective map `∐_{i ∈ I} G i ⟶ F` of sheaves there is a finite subset `T ⊆ I` for
> which `∐_{i ∈ T} G i ⟶ F` is still locally surjective.

```lean
def IsQuasiCompact (F : Sheaf J (Type max v u)) : Prop
```

**`CategoryTheory.GrothendieckTopology.IsQuasiCompactTopos`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/QuasiCompact.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/QuasiCompact.lean#L93). The attribute's comment: “A quasi-compact topos: its final object is a quasi-compact object.”. References: SGA 4 IV (8.7).

> The topos `Sh(C)` of sheaves of sets on a site is *quasi-compact* if its final object is a
> quasi-compact object.

```lean
def IsQuasiCompactTopos (J : GrothendieckTopology C) : Prop
```

## Tag 0GMP, a lemma

[Tag 0GMP](https://stacks.math.columbia.edu/tag/0GMP) in the Stacks Project.

**`CategoryTheory.Sheaf.isQuasiCompact_of_isLocallySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/QuasiCompact/LocallySurjectiveTransfer.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/QuasiCompact/LocallySurjectiveTransfer.lean#L176). The attribute's comment: “(2)”.

> Quasi-compactness of a sheaf of sets passes along a surjection `φ : F ⟶ G`.

```lean
theorem isQuasiCompact_of_isLocallySurjective {F G : Sheaf J (Type max u v)} (φ : F ⟶ G)
    (hφ : IsLocallySurjective φ) (hF : IsQuasiCompact F) :
    IsQuasiCompact G
```

**`CategoryTheory.Sheaf.isQuasiCompact_sheafifiedYoneda_of_isLocallySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/QuasiCompact/LocallySurjectiveTransfer.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/QuasiCompact/LocallySurjectiveTransfer.lean#L192). The attribute's comment: “(1)”.

> If `f : U ⟶ V` sheafifies to a surjection `h_U^# ⟶ h_V^#` of sheafified representables and
> `h_U^#` is quasi-compact, then so is `h_V^#`.

```lean
theorem isQuasiCompact_sheafifiedYoneda_of_isLocallySurjective {U V : C} (f : U ⟶ V)
    (hf : IsLocallySurjective ((sheafifiedYoneda J).map f))
    (hU : IsQuasiCompact ((sheafifiedYoneda J).obj U)) :
    IsQuasiCompact ((sheafifiedYoneda J).obj V)
```

## Tag 0GMQ, a lemma

[Tag 0GMQ](https://stacks.math.columbia.edu/tag/0GMQ) in the Stacks Project.

**`Sheaf.quasiCompact_coproduct_fin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/QuasiCompact/FiniteCoproducts.lean, line 400](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/QuasiCompact/FiniteCoproducts.lean#L400). References: SGA 4 VI (1.3), “special case”; SGA 4 VI (1.4), “partial”.

> **Stacks Tag 0GMQ, Lemma 7.17.6.**
>
> Let `C` be a site and let `n ≥ 1`. If `F : Fin n → Sh(C)` is a finite family of
> quasi-compact sheaves (quasi-compact objects of the topos `Sh(C)` in the sense of
> `Sheaf.QuasiCompact`), then their coproduct `∐ F` in `Sh(C)` is quasi-compact.
>
> The family is indexed by `Fin n` with `n ≥ 1`, the `0`-indexed form of the family
> `F_1, …, F_n` of the informal statement.

```lean
theorem Sheaf.quasiCompact_coproduct_fin
    {n : ℕ} (hn : 1 ≤ n) (F : Fin n → Sheaf J (Type max u v))
    [HasCoproduct F]
    (hF : ∀ i, Sheaf.QuasiCompact (F i)) :
    Sheaf.QuasiCompact (∐ F)
```

## Tag 0738, a lemma

[Tag 0738](https://stacks.math.columbia.edu/tag/0738) in the Stacks Project.

**`CategoryTheory.Sheaf.injective_and_bijective_colimit_post_sheafSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/QuasiCompact/ObjectsAndColimits.lean, line 699](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/QuasiCompact/ObjectsAndColimits.lean#L699). The attribute's comment: “Sections over U of a filtered colimit of sheaves of sets.”. References: SGA 4 VI (1.23), “(i) qc ⇒ inj”.

> **Stacks 0738.** Let `C` be a site, `F : I ⥤ Sheaf J (Type max u v)` a filtered diagram of
> sheaves of sets and `U` an object of `C`. For the canonical map
> `Ψ = colimit.post F ((sheafSections J _).obj (op U)) : colim_i F_i(U) ⟶ (colim_i F_i)(U)`:
>
> 1. if every transition map `F.map f` is a monomorphism, then `Ψ` is injective;
> 2. if `U` is quasi-compact (Stacks 090H), then `Ψ` is injective;
> 3. if `U` is quasi-compact and every transition map is a monomorphism, then `Ψ` is bijective;
> 4. if the coverings `{U_j ⟶ U}_{j ∈ J}` with `J` finite and all fibre products `U_j ×_U U_{j'}`
>    existing and quasi-compact are cofinal among the coverings of `U`, then `Ψ` is bijective.
>
> The four conjuncts are the four parts of the source, in order.

```lean
public theorem injective_and_bijective_colimit_post_sheafSections {C : Type u} [Category.{v} C]
    (J : GrothendieckTopology C) {I : Type w₁} [Category.{w₂} I] [IsFiltered I]
    [HasColimitsOfShape I (Type max u v)] (F : I ⥤ Sheaf J (Type max u v)) (U : C) :
    ((∀ (i j : I) (f : i ⟶ j), Mono (F.map f)) →
        Function.Injective (colimit.post F ((sheafSections J (Type max u v)).obj (op U)))) ∧
      (J.IsQuasiCompactObject U →
        Function.Injective (colimit.post F ((sheafSections J (Type max u v)).obj (op U)))) ∧
      (J.IsQuasiCompactObject U →
        (∀ (i j : I) (f : i ⟶ j), Mono (F.map f)) →
        Function.Bijective (colimit.post F ((sheafSections J (Type max u v)).obj (op U)))) ∧
      ((∀ S ∈ J U,
          ∃ 𝒱 : PreZeroHypercover.{max u v} U,
            Finite 𝒱.I₀ ∧
              𝒱.sieve₀ ∈ J U ∧
              𝒱.sieve₀ ≤ S ∧
              ∀ j j' : 𝒱.I₀,
                ∃ (W : C) (p : W ⟶ 𝒱.X j) (q : W ⟶ 𝒱.X j'),
                  IsPullback p q (𝒱.f j) (𝒱.f j') ∧ J.IsQuasiCompactObject W) →
        Function.Bijective (colimit.post F ((sheafSections J (Type max u v)).obj (op U))))
```

## Tag 0GMR, a lemma

[Tag 0GMR](https://stacks.math.columbia.edu/tag/0GMR) in the Stacks Project.

**`CategoryTheory.Sheaf.injective_and_bijective_colimit_post_globalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/QuasiCompact/ObjectsAndColimits.lean, line 2190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/QuasiCompact/ObjectsAndColimits.lean#L2190). The attribute's comment: “Global sections of a filtered colimit of sheaves of sets.”. References: SGA 4 VI (1.23), “(i) qc⇒inj, X terminal”.

> **Stacks 0GMR.** Let `C` be a site and `F : I ⥤ Sheaf J (Type max u v)` a filtered diagram
> of sheaves of sets. For the canonical map
> `Ψ = colimit.post F (Γ J _) : colim_i Γ(C, F i) ⟶ Γ(C, colim_i F i)`:
>
> 1. if every transition map `F.map f` is a monomorphism, then `Ψ` is injective;
> 2. if the topos `Sh(C)` is quasi-compact (Stacks 0D07), then `Ψ` is injective;
> 3. if the topos `Sh(C)` is quasi-compact and every transition map is a monomorphism, then `Ψ`
>    is bijective;
> 4. if there is a set `S` of sheaves such that every sheaf `G` surjecting onto the final sheaf
>    admits a map `K ⟶ G` from some `K ∈ S` which itself surjects onto the final sheaf, and such
>    that `K ⨯ K` is quasi-compact for every `K ∈ S`, then `Ψ` is bijective.
>
> The four conjuncts are the four parts of the source, in order.

```lean
public theorem injective_and_bijective_colimit_post_globalSections {C : Type u} [Category.{v} C]
    (J : GrothendieckTopology C) {I : Type w₁} [Category.{w₂} I] [IsFiltered I]
    [HasColimitsOfShape I (Type max u v)] (F : I ⥤ Sheaf J (Type max u v)) :
    ((∀ (i j : I) (f : i ⟶ j), Mono (F.map f)) →
        Function.Injective (colimit.post F (Γ J (Type max u v)))) ∧
      (J.IsQuasiCompactTopos → Function.Injective (colimit.post F (Γ J (Type max u v)))) ∧
      (J.IsQuasiCompactTopos →
        (∀ (i j : I) (f : i ⟶ j), Mono (F.map f)) →
        Function.Bijective (colimit.post F (Γ J (Type max u v)))) ∧
      ((∃ S : Set (Sheaf J (Type max u v)),
          (∀ G : Sheaf J (Type max u v),
              IsLocallySurjective (terminal.from G) →
                ∃ K ∈ S, Nonempty (K ⟶ G) ∧ IsLocallySurjective (terminal.from K)) ∧
            ∀ K ∈ S, IsQuasiCompact (K ⨯ K)) →
        Function.Bijective (colimit.post F (Γ J (Type max u v))))
```

## Tag 0GMS, a remark

[Tag 0GMS](https://stacks.math.columbia.edu/tag/0GMS) in the Stacks Project.

**`CategoryTheory.Sheaf.forall_exists_mem_coveringSetOfObjects_and_isQuasiCompact_prod_self_of_isQuasiCompactTopos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/QuasiCompact/CoveringSetFromCoversTop.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/QuasiCompact/CoveringSetFromCoversTop.lean#L135). The attribute's comment: “case (3)”.

> **Stacks 0GMS, case (3).** Let `C` be a site such that
>
> * (a) `Sh(C)` is quasi-compact (Stacks 0D07),
> * (b) every object of `C` has a covering whose members are quasi-compact objects (Stacks 090H),
> * (c) if `U` and `U'` are quasi-compact objects then the sheaf `h_U^# ⨯ h_{U'}^#` is
>   quasi-compact.
>
> Then the hypotheses of part (4) of Stacks 0GMR are satisfied by the set `S` of finite coproducts of
> the sheaves `h_U^#` for `U` a quasi-compact object of `C`, which is
> `CategoryTheory.Sheaf.coveringSetOfObjects J {U | J.IsQuasiCompactObject U}`: every sheaf of sets
> `G` surjecting onto the final sheaf receives a morphism from a member `K` of `S` with `K ⟶ *`
> surjective, and `K ⨯ K` is quasi-compact for every `K ∈ S`.
>
> The source states this without proof. *Proof.* For (4)(b), (c) is hypothesis (1)(b) of the remark
> for the set of quasi-compact objects, and
> `CategoryTheory.Sheaf.isQuasiCompact_prod_self_of_mem_coveringSetOfObjects` applies. For (4)(a),
> let `G ⟶ *` be surjective and index a family by the pairs `(U, s)` with `U` quasi-compact and
> `s ∈ G(U)`. These objects cover the final object: every object `W` has a covering on whose members
> `G` has a section, each member has a covering by quasi-compact objects by (b), and `G` has
> sections over these by restriction. So `∐_{(U, s)} h_U^# ⟶ *` is surjective
> (`isLocallySurjective_terminal_from_sigma_sheafifiedYoneda`); by (a) a finite subfamily is
> already surjective, its coproduct `K` lies in `S`, and the sections `s` give `K ⟶ G`.

```lean
theorem forall_exists_mem_coveringSetOfObjects_and_isQuasiCompact_prod_self_of_isQuasiCompactTopos
    (ha : J.IsQuasiCompactTopos)
    (hb : ∀ W : C, ∃ 𝒰 : PreZeroHypercover.{max u v} W,
      𝒰.sieve₀ ∈ J W ∧ ∀ i, J.IsQuasiCompactObject (𝒰.X i))
    (hc : ∀ U U' : C, J.IsQuasiCompactObject U → J.IsQuasiCompactObject U' →
      IsQuasiCompact ((sheafifiedYoneda J).obj U ⨯ (sheafifiedYoneda J).obj U')) :
    (∀ G : Sheaf J (Type max u v), IsLocallySurjective (terminal.from G) →
        ∃ K ∈ coveringSetOfObjects J {U | J.IsQuasiCompactObject U}, Nonempty (K ⟶ G) ∧
          IsLocallySurjective (terminal.from K)) ∧
      ∀ K ∈ coveringSetOfObjects J {U | J.IsQuasiCompactObject U}, IsQuasiCompact (K ⨯ K)
```

**`CategoryTheory.Sheaf.forall_exists_mem_coveringSetOfObjects_and_isQuasiCompact_prod_self_of_nonempty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/QuasiCompact/CoveringSetOfObjects.lean, line 463](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/QuasiCompact/CoveringSetOfObjects.lean#L463). The attribute's comment: “case (1)”.

> **Stacks 0GMS, case (1).** Let `C` be a site and `B ⊆ Ob(C)` a set of objects such that
>
> * (a) for every surjection `G ⟶ *` there are finitely many `U₁, …, U_m ∈ B` with `G(U_j)`
>   nonempty and `∐_j h_{U_j}^# ⟶ *` surjective,
> * (b) for `U, U' ∈ B` the sheaf `h_U^# ⨯ h_{U'}^#` is quasi-compact.
>
> Then the hypotheses of part (4) of Stacks 0GMR are satisfied by the set `S` of finite coproducts of
> the sheafified representables of members of `B`, i.e.
> `CategoryTheory.Sheaf.coveringSetOfObjects J B`: every sheaf of sets `G` surjecting onto the final
> sheaf receives a morphism from a member `K` of `S` with `K ⟶ *` surjective, and `K ⨯ K` is
> quasi-compact for every `K ∈ S`.
>
> The source states this without proof. *Proof.* For (4)(a), the coproduct `K = ∐_j h_{U_j}^#` of
> the family (a) provides lies in `S`, the chosen sections of `G` over the `U_j` give `K ⟶ G`
> (`CategoryTheory.Sheaf.sectionEquiv`), and `K ⟶ *` is surjective by (a). Clause (4)(b) is
> `isQuasiCompact_prod_self_of_mem_coveringSetOfObjects`.

```lean
theorem forall_exists_mem_coveringSetOfObjects_and_isQuasiCompact_prod_self_of_nonempty
    {B : Set C}
    (ha : ∀ G : Sheaf J (Type max u v), IsLocallySurjective (terminal.from G) →
      ∃ (ι : Type max u v) (_ : Finite ι) (U : ι → C), (∀ i, U i ∈ B) ∧
        (∀ i, Nonempty (G.obj.obj (op (U i)))) ∧
        IsLocallySurjective (terminal.from (∐ fun i => (sheafifiedYoneda J).obj (U i))))
    (hb : ∀ U ∈ B, ∀ U' ∈ B,
      IsQuasiCompact ((sheafifiedYoneda J).obj U ⨯ (sheafifiedYoneda J).obj U')) :
    (∀ G : Sheaf J (Type max u v), IsLocallySurjective (terminal.from G) →
        ∃ K ∈ coveringSetOfObjects J B, Nonempty (K ⟶ G) ∧
          IsLocallySurjective (terminal.from K)) ∧
      ∀ K ∈ coveringSetOfObjects J B, IsQuasiCompact (K ⨯ K)
```

**`CategoryTheory.Sheaf.forall_exists_mem_coveringSetOfObjects_and_isQuasiCompact_prod_self_of_finite_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/QuasiCompact/CoveringSetOfObjects.lean, line 499](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/QuasiCompact/CoveringSetOfObjects.lean#L499). The attribute's comment: “case (2)”.

> **Stacks 0GMS, case (2).** Let `C` be a site and `B ⊆ Ob(C)` a set of objects such that
>
> * (a) there are finitely many `U₁, …, U_m ∈ B` with `∐_j h_{U_j}^# ⟶ *` surjective,
> * (b) every covering of a member of `B` is refined by a finite covering by members of `B`,
> * (c) for `U, U' ∈ B` there are finitely many `V_1, …, V_m ∈ B` with morphisms `V_k ⟶ U` and
>   `V_k ⟶ U'` for which `∐_k h_{V_k}^# ⟶ h_U^# ⨯ h_{U'}^#` is surjective.
>
> Then the hypotheses of part (4) of Stacks 0GMR are satisfied by the set `S` of finite coproducts of
> the sheafified representables of members of `B`, i.e.
> `CategoryTheory.Sheaf.coveringSetOfObjects J B`: every sheaf of sets `G` surjecting onto the final
> sheaf receives a morphism from a member `K` of `S` with `K ⟶ *` surjective, and `K ⨯ K` is
> quasi-compact for every `K ∈ S`.
>
> The source states this without proof. Clause (4)(a) is `exists_mem_coveringSetOfObjects`, from (a)
> and (b). Clause (4)(b) is `isQuasiCompact_prod_self_of_mem_coveringSetOfObjects`, once (b) makes
> every member of `B` a quasi-compact object
> (`CategoryTheory.GrothendieckTopology.isQuasiCompactObject_of_exists_finite_refinement`) and (c)
> then makes `h_U^# ⨯ h_{U'}^#` quasi-compact
> (`isQuasiCompact_prod_sheafifiedYoneda_of_isLocallySurjective`).

```lean
theorem forall_exists_mem_coveringSetOfObjects_and_isQuasiCompact_prod_self_of_finite_refinement
    {B : Set C}
    (ha : ∃ (ι : Type max u v) (_ : Finite ι) (U : ι → C), (∀ i, U i ∈ B) ∧
      IsLocallySurjective (terminal.from (∐ fun i => (sheafifiedYoneda J).obj (U i))))
    (hb : ∀ U ∈ B, ∀ 𝒰 : PreZeroHypercover.{max u v} U, 𝒰.sieve₀ ∈ J U →
      ∃ (𝒱 : PreZeroHypercover.{max u v} U) (_ : 𝒱.Hom 𝒰),
        𝒱.sieve₀ ∈ J U ∧ Finite 𝒱.I₀ ∧ ∀ i, 𝒱.X i ∈ B)
    (hc : ∀ U ∈ B, ∀ U' ∈ B, ∃ (ι : Type max u v) (_ : Finite ι) (V : ι → C)
      (a : ∀ i, V i ⟶ U) (b : ∀ i, V i ⟶ U'), (∀ i, V i ∈ B) ∧
        IsLocallySurjective (Sigma.desc fun i =>
          prod.lift ((sheafifiedYoneda J).map (a i)) ((sheafifiedYoneda J).map (b i)))) :
    (∀ G : Sheaf J (Type max u v), IsLocallySurjective (terminal.from G) →
        ∃ K ∈ coveringSetOfObjects J B, Nonempty (K ⟶ G) ∧
          IsLocallySurjective (terminal.from K)) ∧
      ∀ K ∈ coveringSetOfObjects J B, IsQuasiCompact (K ⨯ K)
```

## Tag 0GS0, a lemma

[Tag 0GS0](https://stacks.math.columbia.edu/tag/0GS0) in the Stacks Project.

**`Stacks.Sites.ColimitCofinality.sections_commute_colimit_of_cofinality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/QuasiCompact/ColimitCofinality.lean, line 494](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/QuasiCompact/ColimitCofinality.lean#L494).

> **(Stacks 0GS0.) Sections commute with colimits along ordinals of large enough cofinality.**
>
> Let `𝒮` be a site (a small category `C` with covering families carrying explicit index sets and
> satisfying axioms (1)–(3); in particular all fiber products `U_i ×_X U_j` exist). Let `β` be an
> ordinal and `F : β.ToType ⥤ Sh(C)` a system of sheaves over `β` (a `β`-indexed direct system of
> sheaves of sets), whose colimit in `Sh(C)` exists (`Sh(C)` is cocomplete, Definition 3). Suppose
> the cofinality of `β` is large enough for `𝒮` (the pointwise bound `|I| < cf β` for every covering
> family). Then for every object `U` the canonical comparison map `c_U` is a bijection.

```lean
theorem sections_commute_colimit_of_cofinality
    {β : Ordinal.{u}} (F : β.ToType ⥤ 𝒮.Sheaf) [HasColimit F]
    (hβ : 𝒮.CofinalityLargeEnough β) (U : C) :
    Function.Bijective (⇑(𝒮.colimSectionsComparison F U))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.17, Tag 090G](https://stacks.math.columbia.edu/tag/090G)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
