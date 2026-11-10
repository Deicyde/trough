---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.isPrimePowerTorsion_nontrivial_sheafH_smallEtalePushforwardAb_of_isLimit, Stacks.EtaleCohomology.isPrimePowerTorsion_nontrivial_sheafH_smallEtalePullbackAb_of_isLimit, Stacks.EtaleCohomology.exists_isPrimePowerTorsion_nontrivial_sheafH_iff_of_isLimit, AlgebraicGeometry.subsingleton_sheafH_iff_of_isMaximalProPSubgroup, AlgebraicGeometry.tfae_subsingleton_sheafH_of_isMaximalProPSubgroup, Stacks.GaloisCohomology.isZero_continuousGroupCohomology_units_of_forall_brauer, Stacks.GaloisCohomology.isMulCoboundary₂_of_brauerGroup_eq_one, Stacks.GaloisCohomology.isZero_continuousGroupCohomology_units
statement: formalized
proof: formalized
---

# 59.67 Galois cohomology

Section 59.67 of the Stacks Project, [Tag 0A2M](https://stacks.math.columbia.edu/tag/0A2M). 12 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DV7, a lemma

[Tag 0DV7](https://stacks.math.columbia.edu/tag/0DV7) in the Stacks Project.

**`Stacks.EtaleCohomology.isPrimePowerTorsion_nontrivial_sheafH_smallEtalePushforwardAb_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/FiniteEtaleLimit.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/FiniteEtaleLimit.lean#L104). The attribute's comment: “given F on X, take G = g_* F”.

> **[Stacks, Tag 0DV7], from the limit to the base.** For a directed limit `X = lim Xᵢ` of
> schemes finite over `S`, an `ℓ`-power torsion sheaf `F` on `X` with `Hⁿ(X, F) ≠ 0` gives the
> `ℓ`-power torsion sheaf `g_* F` on `S` with `Hⁿ(S, g_* F) ≠ 0`.

```lean
theorem isPrimePowerTorsion_nontrivial_sheafH_smallEtalePushforwardAb_of_isLimit
    [IsDirected I (· ≤ ·)] [Nonempty I] [∀ i, IsFinite (ι i)] (hc : IsLimit c) {ℓ : ℕ}
    {F : Sheaf (smallEtaleTopology c.pt) Ab.{u + 1}}
    (hF : Stacks.Torsion.IsPrimePowerTorsion (smallEtaleTopology c.pt) ℓ F) {n : ℕ}
    (hn : Nontrivial (Sheaf.H.{u + 1} F n)) :
    Stacks.Torsion.IsPrimePowerTorsion (smallEtaleTopology S) ℓ
        ((smallEtalePushforwardAb g).obj F) ∧
      Nontrivial (Sheaf.H.{u + 1} ((smallEtalePushforwardAb g).obj F) n)
```

**`Stacks.EtaleCohomology.isPrimePowerTorsion_nontrivial_sheafH_smallEtalePullbackAb_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/FiniteEtaleLimit.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/FiniteEtaleLimit.lean#L266). The attribute's comment: “given G on S, take F = g⁻¹ G”.

> **[Stacks, Tag 0DV7], from the base to the limit.** In the situation of
> `Stacks.EtaleCohomology.injective_etaleCohomologyPullback_of_isLimit`, an `ℓ`-power torsion sheaf
> `G` on `S` with `Hⁿ(S, G) ≠ 0` gives the `ℓ`-power torsion sheaf `g⁻¹ G` on `X` with
> `Hⁿ(X, g⁻¹ G) ≠ 0`.

```lean
theorem isPrimePowerTorsion_nontrivial_sheafH_smallEtalePullbackAb_of_isLimit
    [IsDirected I (· ≤ ·)] [Nonempty I] [CompactSpace S] [QuasiSeparatedSpace S]
    [∀ i, IsFinite (ι i)] [∀ i, Etale (ι i)] (d : Iᵒᵖ → ℕ)
    [∀ i, Stacks.Morphisms.IsFiniteLocallyFreeOfRank (ι i) (d i)] {ℓ : ℕ}
    (hd : ∀ i, (d i).Coprime ℓ) (hc : IsLimit c) {G : Sheaf (smallEtaleTopology S) Ab.{u + 1}}
    (hG : Stacks.Torsion.IsPrimePowerTorsion (smallEtaleTopology S) ℓ G) {n : ℕ}
    (hn : Nontrivial (Sheaf.H.{u + 1} G n)) :
    Stacks.Torsion.IsPrimePowerTorsion (smallEtaleTopology c.pt) ℓ
        ((smallEtalePullbackAb g).obj G) ∧
      Nontrivial (Sheaf.H.{u + 1} ((smallEtalePullbackAb g).obj G) n)
```

**`Stacks.EtaleCohomology.exists_isPrimePowerTorsion_nontrivial_sheafH_iff_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/FiniteEtaleLimit.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/FiniteEtaleLimit.lean#L288). The attribute's comment: “(1) ⇔ (2)”.

> **[Stacks, Tag 0DV7].** Let `S` be a quasi-compact and quasi-separated scheme and let
> `X = lim Xᵢ` be the limit of a directed system of `S`-schemes `ιᵢ : Xᵢ ⟶ S`, each finite étale of
> constant degree `dᵢ` prime to `ℓ`, with structure morphism `g : X ⟶ S`. Then there is an
> `ℓ`-power torsion sheaf `G` on `S_étale` with `Hⁿ(S, G) ≠ 0` if and only if there is an `ℓ`-power
> torsion sheaf `F` on `X_étale` with `Hⁿ(X, F) ≠ 0`.
>
> The source assumes that `ℓ` is prime and that `n > 0`; the proof uses neither.

```lean
theorem exists_isPrimePowerTorsion_nontrivial_sheafH_iff_of_isLimit [IsDirected I (· ≤ ·)]
    [Nonempty I] [CompactSpace S] [QuasiSeparatedSpace S] [∀ i, IsFinite (ι i)]
    [∀ i, Etale (ι i)] (d : Iᵒᵖ → ℕ) [∀ i, Stacks.Morphisms.IsFiniteLocallyFreeOfRank (ι i) (d i)]
    {ℓ : ℕ} (hd : ∀ i, (d i).Coprime ℓ) (hc : IsLimit c) (n : ℕ) :
    (∃ G : Sheaf (smallEtaleTopology S) Ab.{u + 1},
        Stacks.Torsion.IsPrimePowerTorsion (smallEtaleTopology S) ℓ G ∧
          Nontrivial (Sheaf.H.{u + 1} G n)) ↔
      ∃ F : Sheaf (smallEtaleTopology c.pt) Ab.{u + 1},
        Stacks.Torsion.IsPrimePowerTorsion (smallEtaleTopology c.pt) ℓ F ∧
          Nontrivial (Sheaf.H.{u + 1} F n)
```

## Tag 0DV8, a lemma

[Tag 0DV8](https://stacks.math.columbia.edu/tag/0DV8) in the Stacks Project.

**`AlgebraicGeometry.subsingleton_sheafH_iff_of_isMaximalProPSubgroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MaximalProEllVanishing.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MaximalProEllVanishing.lean#L139).

> **Stacks Project, Tag 0DV8.** Let `ℓ` be a prime, `K` a field with separable closure `Kˢᵉᵖ`,
> `H` a maximal pro-`ℓ` subgroup of `Gal(Kˢᵉᵖ/K)` and `L` its fixed field. Then
> `Hⁿ_ét(Spec K, 𝓕)` vanishes for every `ℓ`-power torsion abelian sheaf `𝓕` on the small étale
> site of `Spec K` if and only if `Hⁿ_ét(Spec L, ℤ/ℓℤ)` vanishes.

```lean
theorem subsingleton_sheafH_iff_of_isMaximalProPSubgroup (hℓ : ℓ.Prime) (n : ℕ)
    (hH : IsMaximalProPSubgroup ℓ H)
    [HasExt (Sheaf (Spec (.of K)).smallEtaleTopology AddCommGrpCat.{max (u + 1) v})]
    [HasExt (Sheaf (Spec (.of (fixedField H))).smallEtaleTopology
      AddCommGrpCat.{max (u + 1) v})] :
    (∀ 𝓕 : Sheaf (Spec (.of K)).smallEtaleTopology AddCommGrpCat.{max (u + 1) v},
      Stacks.Torsion.IsPrimePowerTorsion _ ℓ 𝓕 → Subsingleton (Sheaf.H 𝓕 n)) ↔
      Subsingleton (Sheaf.H ((constantSheaf (Spec (.of (fixedField H))).smallEtaleTopology
        AddCommGrpCat.{max (u + 1) v}).obj (AddCommGrpCat.of (ULift.{max (u + 1) v} (ZMod ℓ))))
          n)
```

## Tag 0DV9, a lemma

[Tag 0DV9](https://stacks.math.columbia.edu/tag/0DV9) in the Stacks Project.

**`AlgebraicGeometry.tfae_subsingleton_sheafH_of_isMaximalProPSubgroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MaximalProEllVanishing.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MaximalProEllVanishing.lean#L170). The attribute's comment: “both readings of `ℓ`-torsion: `ℓ`-power torsion (1) and killed by `ℓ` (2)”.

> **Stacks Project, Tag 0DV9.** Let `ℓ` be a prime, `K` a field with separable closure `Kˢᵉᵖ`,
> `H` a maximal pro-`ℓ` subgroup of `Gal(Kˢᵉᵖ/K)` and `L` its fixed field. The following are
> equivalent:
> 1. `H^q_ét(Spec K, 𝓕)` vanishes for every `q ≥ n` and every `ℓ`-power torsion abelian sheaf `𝓕`
>    on the small étale site of `Spec K`;
> 2. `H^q_ét(Spec K, 𝓕)` vanishes for every `q ≥ n` and every abelian sheaf `𝓕` on the small étale
>    site of `Spec K` killed by `ℓ`;
> 3. `Hⁿ_ét(Spec L, ℤ/ℓℤ)` vanishes.

```lean
theorem tfae_subsingleton_sheafH_of_isMaximalProPSubgroup (hℓ : ℓ.Prime) (n : ℕ)
    (hH : IsMaximalProPSubgroup ℓ H)
    [HasExt (Sheaf (Spec (.of K)).smallEtaleTopology AddCommGrpCat.{max (u + 1) v})]
    [HasExt (Sheaf (Spec (.of (fixedField H))).smallEtaleTopology
      AddCommGrpCat.{max (u + 1) v})] :
    List.TFAE [
      ∀ q, n ≤ q → ∀ 𝓕 : Sheaf (Spec (.of K)).smallEtaleTopology AddCommGrpCat.{max (u + 1) v},
        Stacks.Torsion.IsPrimePowerTorsion _ ℓ 𝓕 → Subsingleton (Sheaf.H 𝓕 q),
      ∀ q, n ≤ q → ∀ 𝓕 : Sheaf (Spec (.of K)).smallEtaleTopology AddCommGrpCat.{max (u + 1) v},
        ℓ • 𝟙 𝓕 = 0 → Subsingleton (Sheaf.H 𝓕 q),
      Subsingleton (Sheaf.H ((constantSheaf (Spec (.of (fixedField H))).smallEtaleTopology
        AddCommGrpCat.{max (u + 1) v}).obj (AddCommGrpCat.of (ULift.{max (u + 1) v} (ZMod ℓ))))
          n)]
```

## Tag 03R8, a proposition

[Tag 03R8](https://stacks.math.columbia.edu/tag/03R8) in the Stacks Project.

**`Stacks.GaloisCohomology.isZero_continuousGroupCohomology_units_of_forall_brauer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupVanishingAllDegrees.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupVanishingAllDegrees.lean#L68). The attribute's comment: “part (1) IN FULL, for the DERIVED-FUNCTOR groups continuousGroupCohomology of Stacks 04JR: H^q(Gal(Ω/K), Ωˣ) = 0 for EVERY q ≥ 1, where Ω is any separably closed field Galois over K, so at Ω = K^sep this is exactly the tag's part (1). The Brauer hypothesis is the source's own -- Br(K') = 0 for every finite extension K'/K -- and the degree range is the source's. Degrees one and two are the two earlier registrations in MultiplicativeGroupVanishingCriterion (Hilbert 90 through the degree-one comparison, and the crossed-product argument through the degree-two comparison, the latter needing only Br(K) = 0). Degrees q ≥ 3 are part (2), the registration in TorsionGaloisVanishing, through isZero_continuousGroupCohomology_of_forall_isAddTorsion: multiplication by a positive integer n on a discrete module has kernel and cokernel killed by n, so part (2) and two passes of the long exact sequence of the δ-functor of Stacks 010Q make it injective on H^q for q ≥ 3, while every class is killed by some positive integer by Stacks 0DV3 part (1). This registration is part (1); part (2) is the registration in TorsionGaloisVanishing and the degree-one and degree-two statements keep their own registrations in MultiplicativeGroupVanishingCriterion”. References: SGA 4½ Arcata (3.1.6).

> Let `Ω` be a separably closed Galois extension of a field `K` and assume `Br(K') = 0` for
> every finite extension `K'/K`. Then `H^q(Gal(Ω/K), Ωˣ) = 0` for every `q ≥ 1`, the group being
> the continuous group cohomology of the discrete Galois module
> `Stacks.GaloisCohomology.unitsContinuousGModule`.

```lean
theorem isZero_continuousGroupCohomology_units_of_forall_brauer (K Ω : Type u) [Field K]
    [Field Ω] [Algebra K Ω] [IsGalois K Ω] [IsSepClosed Ω]
    (hBr : ∀ (K' : Type u) [Field K'] [Algebra K K'] [Module.Finite K K']
      (y : BrauerGroup K'), y = 1)
    (q : ℕ) (hq : 1 ≤ q) :
    IsZero (continuousGroupCohomology.{u, u} Gal(Ω/K) q (unitsContinuousGModule K Ω))
```

**`Stacks.GaloisCohomology.isMulCoboundary₂_of_brauerGroup_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupVanishingCriterion.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupVanishingCriterion.lean#L211). The attribute's comment: “part (1) in degree two, in explicit cocycle form, UNCONDITIONAL -- nothing is carried. Under the tag's Brauer hypothesis every locally constant 2-cocycle of the Galois group with values in the units is a coboundary, which is the vanishing of H^2(Gal(Ω/K), Ωˣ); at Ω = K^sep this is the tag's degree-two case. Proved from isMulCoboundary₂_of_forall_finiteGalois fed with the crossed-product argument isMulCoboundary₂_of_brauer, whose premise the tag's hypothesis discharges at once since Br(K) = 0 forces every relative Brauer group Br(L/K) to vanish. The hypothesis used here is only Br(K) = 0, which is weaker than the tag's, and Ω is an arbitrary Galois extension rather than the separable closure, so this is more general than the tag's degree-two case rather than narrower. NOT proved here: the other degrees of part (1), for which see isZero_continuousGroupCohomology_units, and part (2)”.

> **Stacks Project, Tag 03R8, part (1) in degree two**, in explicit cocycle form and with no
> carried hypothesis: if `Br(K) = 0` then every locally constant `2`-cocycle on `Gal(Ω/K)` with
> values in `Ωˣ` is a coboundary, which is the vanishing of `H^2(Gal(Ω/K), Ωˣ)`. At `Ω = Kˢᵉᵖ` this
> is the degree-two case of the tag.
>
> The hypothesis is weaker than the tag's, which asks for the Brauer group of every finite
> extension of `K`: only `Br(K) = 0` is used, because it already makes every relative Brauer group
> `Br(L/K)` vanish, which is the premise of
> `Stacks.GaloisCohomology.isMulCoboundary₂_of_brauer` at each finite Galois subextension `L` of
> `Ω`.

```lean
theorem isMulCoboundary₂_of_brauerGroup_eq_one (hBr : ∀ y : BrauerGroup K, y = 1)
    (f : Gal(Ω/K) × Gal(Ω/K) → Ωˣ) (hloc : IsLocallyConstant f) (hf : IsMulCocycle₂ f) :
    IsMulCoboundary₂ f
```

**`Stacks.GaloisCohomology.isZero_continuousGroupCohomology_units`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupVanishingCriterion.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupVanishingCriterion.lean#L261). The attribute's comment: “part (1), the full degree range q ≥ 1, over three carried hypotheses, and for an arbitrary Galois extension Ω/K rather than only the separable closure. CARRIED as `h03QU₁` and `h03QU₂`: the comparison in degrees one and two between the explicit cocycle description of Galois cohomology and the derived-functor description continuousGroupCohomology of Stacks 04JR -- the two are not related anywhere in this library above degree zero, where the comparison is invariantsIsoZerothCohomology; this is the standard comparison of the standard complex with the right derived functor and not a Stacks tag of its own. CARRIED as `hhigh`: the vanishing in degrees q ≥ 3, which is the one part of part (1) assumed wholesale; the source gets it from part (2) of this tag together with the four-term sequence 0 → A → M → M ⊗ Q → B → 0, whose divisible-coefficient input IS proved (isZero_continuousGroupCohomology_of_module_rat, Stacks 0DV3 part (2)) but whose remaining ingredients -- part (2), the construction of M ⊗ Q as a discrete Galois module, and the long exact sequence of continuousGroupCohomology -- are not. PROVED: degrees one and two, where the cocycle premises of `h03QU₁` and `h03QU₂` are discharged from proved results -- Hilbert 90 for an infinite Galois extension (isMulCoboundary₁_of_isLocallyConstant_of_isMulCocycle₁, which needs no hypothesis) and the crossed-product argument (isMulCoboundary₂_of_brauerGroup_eq_one above), the latter consuming the Brauer hypothesis. So the hypothesis is genuinely used and the tag's content in degrees one and two is established, not assumed. Also PROVED, and new: the coefficient module itself, unitsContinuousGModule, the units of Ω as a discrete Galois module in the sense of Stacks 04JP, together with the continuity of the Galois action on them. NOT proved: part (2) of the tag, for which the library has none of the inputs -- see this file's module documentation”.

> **Stacks Project, Tag 03R8, part (1).** Let `K` be a field with `Br(K) = 0` and let `Ω/K` be
> a Galois extension. Then
>
> `H^q(Gal(Ω/K), Ωˣ) = 0` for every `q ≥ 1`,
>
> the groups being this library's continuous group cohomology of Stacks 04JR evaluated at the
> discrete Galois module `Stacks.GaloisCohomology.unitsContinuousGModule`. At `Ω = Kˢᵉᵖ` this is
> part (1) of the tag.
>
> Three inputs are carried. `h03QU₁` and `h03QU₂` are the comparison, in degrees one and two,
> between the cocycle description of Galois cohomology and the derived-functor description: the
> vanishing of the cocycle quotient implies the vanishing of `continuousGroupCohomology`. The two
> descriptions are not related anywhere in this library above degree zero. `hhigh` is the
> vanishing in degrees `q ≥ 3`, which the source deduces from part (2) of the tag through the
> four-term sequence `0 → A → M → M ⊗ 𝐐 → B → 0`; part (2) is not formalized here.
>
> What is proved is degrees one and two: in degree one the cocycle premise of `h03QU₁` is Hilbert's
> theorem 90 for an infinite Galois extension,
> `Stacks.GaloisCohomology.isMulCoboundary₁_of_isLocallyConstant_of_isMulCocycle₁`, which needs no
> hypothesis at all; in degree two it is
> `Stacks.GaloisCohomology.isMulCoboundary₂_of_brauerGroup_eq_one`, which consumes the Brauer
> hypothesis. So the Brauer hypothesis is genuinely used, and the tag's content in degrees one and
> two is established rather than assumed.

```lean
theorem isZero_continuousGroupCohomology_units (hBr : ∀ y : BrauerGroup K, y = 1)
    (h03QU₁ : (∀ f : Gal(Ω/K) → Ωˣ, IsLocallyConstant f → IsMulCocycle₁ f →
          IsMulCoboundary₁ f) →
        IsZero (continuousGroupCohomology.{u, u} Gal(Ω/K) 1 (unitsContinuousGModule K Ω)))
    (h03QU₂ : (∀ f : Gal(Ω/K) × Gal(Ω/K) → Ωˣ, IsLocallyConstant f → IsMulCocycle₂ f →
          IsMulCoboundary₂ f) →
        IsZero (continuousGroupCohomology.{u, u} Gal(Ω/K) 2 (unitsContinuousGModule K Ω)))
    (hhigh : ∀ q : ℕ, 3 ≤ q →
      IsZero (continuousGroupCohomology.{u, u} Gal(Ω/K) q (unitsContinuousGModule K Ω)))
    (q : ℕ) (hq : 1 ≤ q) :
    IsZero (continuousGroupCohomology.{u, u} Gal(Ω/K) q (unitsContinuousGModule K Ω))
```

**`Stacks.GaloisCohomology.isZero_continuousGroupCohomology_units_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupVanishingCriterionUnconditional.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupVanishingCriterionUnconditional.lean#L131). The attribute's comment: “part (1) at q = 1, for the derived-functor groups H^q(Gal(Ω/K), Ωˣ) of Stacks 04JR, with NO HYPOTHESIS WHATSOEVER -- STRONGER than the proposition at q = 1 in two independent ways. First, the proposition assumes Br(K') = 0 uniformly over every finite extension K'/K and this assumes nothing about Brauer groups at all: the cocycle statement at q = 1 is Hilbert 90 for an infinite Galois extension, namely isMulCoboundary₁_of_isLocallyConstant_of_isMulCocycle₁, which is unconditional, so the proposition's hypothesis is not used and is not needed. Second, Ω is an arbitrary Galois extension rather than the separable closure; at Ω = K^sep this is exactly the tag's q = 1 case. Nothing is carried: the comparison between the cocycle and derived-functor descriptions is Stacks.GroupCohomology.isZero_continuousGroupCohomology_one_of_forall_isCoboundary, which is a theorem, not a hypothesis. NOT proved here: the degrees q ≥ 2 of part (1) -- q = 2 is isZero_continuousGroupCohomology_units_two just below, over the tag's own hypothesis in the weaker form Br(K) = 0, and the degrees q ≥ 3 are isZero_continuousGroupCohomology_units_of_fourTerm and isZero_continuousGroupCohomology_units_of_annihilated, which still carry part (2) -- and part (2) itself”. References: SGA 4½ Arcata (1.5.3), “more general”.

> For a Galois extension `Ω/K`, the continuous group cohomology `H¹(Gal(Ω/K), Ωˣ)` of the
> discrete Galois module `Stacks.GaloisCohomology.unitsContinuousGModule` vanishes.

```lean
theorem isZero_continuousGroupCohomology_units_one :
    IsZero (continuousGroupCohomology.{u, u} Gal(Ω/K) 1 (unitsContinuousGModule K Ω))
```

**`Stacks.GaloisCohomology.isZero_continuousGroupCohomology_units_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupVanishingCriterionUnconditional.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupVanishingCriterionUnconditional.lean#L159). The attribute's comment: “part (1) at q = 2, for the derived-functor groups H^q(Gal(Ω/K), Ωˣ) of Stacks 04JR. Nothing is carried: no comparison between the cocycle and derived-functor descriptions is assumed, and the only hypothesis is Br(K) = 0. That is STRICTLY WEAKER than the proposition's own hypothesis, which assumes Br(K') = 0 uniformly over every finite extension K'/K -- Br(K) = 0 is one instance of it, and it already forces every relative Brauer group Br(L/K) to vanish, which is what the crossed-product argument needs at each finite Galois subextension. Ω is an arbitrary Galois extension rather than the separable closure, so this is more general than the tag's degree-two case in that respect too; at Ω = K^sep it is exactly that case. The cocycle input is isMulCoboundary₂_of_brauer, assembled by exists_isLocallyConstant_isMulCoboundary₂_of_forall_finiteGalois (which records that the trivialising 1-cochain, being inflated from a finite level, is locally constant -- strictly more than Mathlib's IsMulCoboundary₂ gives, and exactly what the comparison consumes); the comparison itself is Stacks.GroupCohomology.isZero_continuousGroupCohomology_two_of_forall_isCoboundary, which is a theorem, not a hypothesis. NOT proved here: q = 1 of part (1), which is isZero_continuousGroupCohomology_units_one above and needs no Brauer hypothesis at all; the degrees q >= 3, which are isZero_continuousGroupCohomology_units_of_fourTerm and isZero_continuousGroupCohomology_units_of_annihilated and still carry part (2); and part (2) itself”. References: SGA 4½ Arcata (3.1.6), “clause i), degree q=2”.

> Let `K` be a field with `Br(K) = 0` and let `Ω/K` be a Galois extension. Then the continuous
> group cohomology `H²(Gal(Ω/K), Ωˣ)` of the discrete Galois module
> `Stacks.GaloisCohomology.unitsContinuousGModule` vanishes.

```lean
theorem isZero_continuousGroupCohomology_units_two (hBr : ∀ y : BrauerGroup K, y = 1) :
    IsZero (continuousGroupCohomology.{u, u} Gal(Ω/K) 2 (unitsContinuousGModule K Ω))
```

**`Stacks.GaloisCohomology.isZero_continuousGroupCohomology_units_and_torsion_of_forall_brauer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/SeparableClosureVanishing.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/SeparableClosureVanishing.lean#L84). The attribute's comment: “the WHOLE proposition at Ω = K^sep: part (1) and part (2) together, as one statement, under exactly the source's hypothesis -- Br(K') = 0 for every finite extension K'/K. The first conjunct is H^q(Gal(K^sep/K), (K^sep)ˣ) = 0 for every q ≥ 1, at the discrete Galois module unitsContinuousGModule; the second is H^q(Gal(K^sep/K), M) = 0 for every torsion discrete Galois module M and every q ≥ 2. Both are values of the derived-functor groups continuousGroupCohomology of Stacks 04JR. This is an assembly of the two theorems of this chapter that each prove one part in full: isZero_continuousGroupCohomology_units_of_forall_brauer, in StacksFrontier.AlgebraicGeometry.EtaleCohomology.GaloisCohomology.MultiplicativeGroupVanishingAllDegrees, which takes the same Brauer hypothesis verbatim and gives every degree q ≥ 1; and isZero_continuousGroupCohomology_of_isAddTorsion, in StacksFrontier.AlgebraicGeometry.EtaleCohomology.GaloisCohomology.TorsionGaloisVanishing, which gives every degree q ≥ 2 for every torsion discrete module, and whose hypothesis -- Br(L) = 0 for the intermediate fields L of K^sep/K finite over K -- is an instance of the source's at K' = ↥L, every such L being a finite extension of K. Every clause of the proposition is established here. The per-part registrations elsewhere in the chapter are retained: part (1) in every degree in MultiplicativeGroupVanishingAllDegrees, part (2) in TorsionGaloisVanishing, and the degree-one and degree-two statements of part (1) in MultiplicativeGroupVanishingCriterion”. References: SGA 4½ Arcata (3.1.6).

> **Stacks Project, Tag 03R8.** Let `K` be a field with separable algebraic closure `Kˢᵉᵖ`,
> and assume that `Br(K') = 0` for every finite extension `K'/K`. Then
>
> 1. `H ^q(Gal(Kˢᵉᵖ/K), (Kˢᵉᵖ)ˣ) = 0` for every `q ≥ 1`, and
> 2. `H ^q(Gal(Kˢᵉᵖ/K), M) = 0` for every torsion discrete `Gal(Kˢᵉᵖ/K)`-module `M` and every
>    `q ≥ 2`,
>
> the groups being this library's continuous group cohomology of Stacks 04JR, and the module of
> the first conjunct being the discrete Galois module
> `Stacks.GaloisCohomology.unitsContinuousGModule`.

```lean
theorem isZero_continuousGroupCohomology_units_and_torsion_of_forall_brauer (K : Type u)
    [Field K]
    (hBr : ∀ (K' : Type u) [Field K'] [Algebra K K'] [Module.Finite K K']
      (y : BrauerGroup K'), y = 1) :
    (∀ q : ℕ, 1 ≤ q → IsZero (continuousGroupCohomology.{u, u} Gal(SeparableClosure K/K) q
        (unitsContinuousGModule K (SeparableClosure K)))) ∧
      ∀ (M : ContinuousGModule.{u, max u v} Gal(SeparableClosure K/K)),
        IsAddTorsion M.obj.obj.V → ∀ q : ℕ, 2 ≤ q →
          IsZero (continuousGroupCohomology.{u, v} Gal(SeparableClosure K/K) q M)
```

**`Stacks.GaloisCohomology.isZero_continuousGroupCohomology_of_isAddTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/TorsionGaloisVanishing.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/TorsionGaloisVanishing.lean#L60). The attribute's comment: “part (2) in full, for the DERIVED-FUNCTOR groups continuousGroupCohomology of Stacks 04JR: H^q(Gal(Ω/K), M) = 0 for EVERY torsion discrete Galois module M and EVERY q ≥ 2, where Ω is any separably closed field Galois over K, so at Ω = K^sep this is exactly the tag's part (2). The Brauer hypothesis is the one the source states, and in fact less: only the finite SEPARABLE extensions of K inside Ω are used, whereas the tag asks for every finite extension, so this statement implies the tag's rather than specialising it. The proof is the source's dévissage carried out on locally constant cochains. A locally constant 2-cocycle on a profinite group takes finitely many values, so it is a cocycle with values in a finite submodule; a finite module is reduced to a module killed by a prime p along its p-torsion subgroup; a finite module killed by p is handled over an open subgroup of index prime to p -- the preimage of a p-Sylow subgroup of a finite quotient -- where the action factors through a p-group and the module is filtered by copies of Z/p with trivial action, and the restriction-corestriction identity cor o res = n, written out on cochains, carries the trivialization back to the whole group; and Z/p with trivial action is the Kummer sequence of Stacks 03PL away from the characteristic and the Artin-Schreier sequence of Stacks 0A3J in the characteristic, each fed by the two degrees of part (1) proved in MultiplicativeGroupVanishingCriterion. Degrees above two come from dimension shifting along the module of locally constant functions into a torsion divisible hull, which is an injective object of the category of Stacks 04JP whose cokernel is again torsion. This registration is part (2); part (1) has its own three registrations in MultiplicativeGroupVanishingCriterion”. References: SGA 4½ Arcata (3.1.6), “more general”.

> If the Brauer group of every finite subextension of a separably closed Galois extension
> `Ω/K` vanishes, then `H^q(Gal(Ω/K), M) = 0` for every torsion discrete `Gal(Ω/K)`-module `M` and
> every `q ≥ 2`, the groups being the continuous group cohomology.

```lean
theorem isZero_continuousGroupCohomology_of_isAddTorsion (K Ω : Type u) [Field K] [Field Ω]
    [Algebra K Ω] [IsGalois K Ω] [IsSepClosed Ω]
    (hBr : ∀ L : IntermediateField K Ω, FiniteDimensional K L → ∀ y : BrauerGroup L, y = 1)
    (M : ContinuousGModule.{u, max u v} Gal(Ω/K)) (hM : IsAddTorsion M.obj.obj.V)
    (q : ℕ) (hq : 2 ≤ q) :
    IsZero (continuousGroupCohomology.{u, v} Gal(Ω/K) q M)
```

## Tag 03R9, a definition

[Tag 03R9](https://stacks.math.columbia.edu/tag/03R9) in the Stacks Project.

**`IsCField`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/CFields.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/CFields.lean#L40). References: SGA 4½ Arcata (3.2.1), “more general”.

> A field `K` is a \(C_r\) field if every homogeneous polynomial of degree
> `d ≥ 1` in `n` variables has a nonzero solution when `d ^ r < n`.
>
> The degree bound is `0 < d`, not `0 < d ^ r`. The two agree for every `r ≥ 1`, but at `r = 0`
> they do not: `d ^ 0 = 1` even for `d = 0`, so `0 < d ^ r` is satisfied by the constant
> polynomial `1`, which is homogeneous of degree `0` and has no nonzero root. With that spelling
> `IsCField K 0` is false for every field, which is not what \(C_0\) means.

```lean
abbrev IsCField (K : Type*) [Field K] (r : ℕ) : Prop
```

## Tag 03RA, an example

[Tag 03RA](https://stacks.math.columbia.edu/tag/03RA) in the Stacks Project.

**`exists_nonzero_common_zero_of_isHomogeneous`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/HomogeneousZeros.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/HomogeneousZeros.lean#L40). The attribute's comment: “an algebraically closed field is `C_r`: the one-polynomial case `s = 1`”.

> **Stacks Project, Tag 03RB.** Over an algebraically closed field, a family of `s < n`
> homogeneous polynomials of positive degree in `n` variables has a common nonzero zero.

```lean
lemma exists_nonzero_common_zero_of_isHomogeneous
    (k : Type*) [Field k] [IsAlgClosed k] {s n : ℕ}
    (d : Fin s → ℕ) (f : (i : Fin s) → MvPolynomial (Fin n) k)
    (hd : ∀ i, 0 < d i) (hf : ∀ i, (f i).IsHomogeneous (d i)) (hsn : s < n) :
    ∃ α : Fin n → k, α ≠ 0 ∧ ∀ i, MvPolynomial.eval α (f i) = 0
```

## Tag 03RB, a lemma

[Tag 03RB](https://stacks.math.columbia.edu/tag/03RB) in the Stacks Project.

**`exists_nonzero_common_zero_of_isHomogeneous`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/HomogeneousZeros.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/HomogeneousZeros.lean#L40).

> **Stacks Project, Tag 03RB.** Over an algebraically closed field, a family of `s < n`
> homogeneous polynomials of positive degree in `n` variables has a common nonzero zero.

```lean
lemma exists_nonzero_common_zero_of_isHomogeneous
    (k : Type*) [Field k] [IsAlgClosed k] {s n : ℕ}
    (d : Fin s → ℕ) (f : (i : Fin s) → MvPolynomial (Fin n) k)
    (hd : ∀ i, 0 < d i) (hf : ∀ i, (f i).IsHomogeneous (d i)) (hsn : s < n) :
    ∃ α : Fin n → k, α ≠ 0 ∧ ∀ i, MvPolynomial.eval α (f i) = 0
```

## Tag 03RC, a theorem

[Tag 03RC](https://stacks.math.columbia.edu/tag/03RC) in the Stacks Project.

**`brauerGroup_eq_one_of_isCField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/BrauerGroupCField.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/BrauerGroupCField.lean#L313). References: SGA 4½ Arcata (3.2.2).

> Every Brauer class over a C₁ field is trivial.

```lean
theorem brauerGroup_eq_one_of_isCField (K : Type u) [Field K]
    (hK : IsCField K 1) (x : BrauerGroup K) : x = 1
```

## Tag 03RE, a definition

[Tag 03RE](https://stacks.math.columbia.edu/tag/03RE) in the Stacks Project.

**`AlgebraicGeometry.IsCurve`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/Defs.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/Defs.lean#L46). The attribute's comment: “the curve clause”. References: EGA II (7.4.2), “special case”.

> **Stacks Project, Tag 0A23.** A curve over a field is a variety of Krull dimension one.

```lean
public class IsCurve (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) : Prop
    extends IsVariety k f
```

**`AlgebraicGeometry.IsVariety`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Basic.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Basic.lean#L50). The attribute's comment: “the variety clause”.

> A scheme over a field is a variety when it is integral and its structure morphism is
> separated and of finite type.

```lean
class IsVariety (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) : Prop
    extends IsIntegral X, IsSeparated f, LocallyOfFiniteType f, QuasiCompact f
```

## Tag 03RD, a theorem

[Tag 03RD](https://stacks.math.columbia.edu/tag/03RD) in the Stacks Project.

**`AlgebraicGeometry.isCField_functionField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/TsenFunctionField.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/TsenFunctionField.lean#L86).

> **Stacks Project, Tag 03RD (Tsen's theorem).** The function field of a variety of dimension
> `r` over an algebraically closed field `k` is a \(C_r\) field.

```lean
theorem isCField_functionField (k : Type u) [Field k] [IsAlgClosed k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsVariety k f] {r : ℕ} (hr : topologicalKrullDim X = r) :
    IsCField X.functionField r
```

## Tag 03RF, a lemma

[Tag 03RF](https://stacks.math.columbia.edu/tag/03RF) in the Stacks Project.

**`AlgebraicGeometry.brauerGroup_functionField_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/BrauerGroupFunctionField.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/BrauerGroupFunctionField.lean#L84). References: SGA 4½ Arcata (3.2.4), “q = 2 (Brauer group)”; SGA 4½ Arcata (3.2.2), “special case”.

> The Brauer group of the function field of a curve over an algebraically closed field is
> trivial.

```lean
theorem brauerGroup_functionField_eq_one (k : Type u) [Field k] [IsAlgClosed k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsCurve k f]
    (y : BrauerGroup X.functionField) : y = 1
```

## Tag 03RG, a lemma

[Tag 03RG](https://stacks.math.columbia.edu/tag/03RG) in the Stacks Project.

**`Stacks.EtaleCohomology.subsingleton_sheafH_multiplicativeSheaf_spec_of_trdeg_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupTranscendenceDegreeOneVanishing.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupTranscendenceDegreeOneVanishing.lean#L67). References: SGA 4½ Arcata (3.1.6), “clause i), special case”; SGA 4½ Arcata (3.2.4).

> **Stacks Project, Tag 03RG.** Let `k` be an algebraically closed field and `K/k` a field
> extension of transcendence degree one. Then
>
> `H^q_étale(Spec K, 𝐆_m) = 0` for every `q ≥ 1`.
>
> The criterion of Stacks 03R8 read through Stacks 03QU,
> `AlgebraicGeometry.subsingleton_sheafH_multiplicativeSheaf_of_forall_brauer`, reduces this to
> the triviality of the Brauer group of every finite extension `K'/K`; such a `K'` has
> transcendence degree one over `k`, so `Br(K') = 0` by
> `Stacks.EtaleCohomology.brauerGroup_eq_one_of_module_finite_of_trdeg_eq_one`.

```lean
theorem subsingleton_sheafH_multiplicativeSheaf_spec_of_trdeg_eq_one (k : Type u) [Field k]
    [IsAlgClosed k] (K : Type u) [Field K] [Algebra k K] (hK : Algebra.trdeg k K = 1)
    (q : ℕ) (hq : 1 ≤ q) :
    Subsingleton (Sheaf.H.{u + 1, u + 1}
      (Stacks.Kummer.multiplicativeSheaf.{u, u + 1} (Spec (.of K))) q)
```

**`Stacks.EtaleCohomology.subsingleton_sheafH_multiplicativeSheaf_of_trdeg_eq_one`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupTranscendenceDegreeOneVanishing.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupTranscendenceDegreeOneVanishing.lean#L110). The attribute's comment: “vanishing of the positive-degree étale cohomology of 𝐆_m over a transcendence-degree-one extension of an algebraically closed field, over Tag 03R8 and Tag 03QU as the hypothesis h03RG”.

> **Stacks Project, Tag 03RG**, under its earlier name: an alias of
> `Stacks.EtaleCohomology.subsingleton_sheafH_multiplicativeSheaf_spec_of_trdeg_eq_one`. Let `k`
> be an algebraically closed field and `K/k` a field extension of transcendence degree one. Then
> `H^q_étale(Spec K, 𝐆_m) = 0` for every `q ≥ 1`.

```lean
alias subsingleton_sheafH_multiplicativeSheaf_of_trdeg_eq_one
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.67, Tag 0A2M](https://stacks.math.columbia.edu/tag/0A2M)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
