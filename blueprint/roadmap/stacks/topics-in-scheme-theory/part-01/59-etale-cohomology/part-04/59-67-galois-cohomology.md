---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.isPrimePowerTorsion_nontrivial_sheafH_smallEtalePushforwardAb_of_isLimit, Stacks.EtaleCohomology.isPrimePowerTorsion_nontrivial_sheafH_smallEtalePullbackAb_of_isLimit, Stacks.EtaleCohomology.exists_isPrimePowerTorsion_nontrivial_sheafH_iff_of_isLimit, AlgebraicGeometry.subsingleton_sheafH_iff_of_isMaximalProPSubgroup, AlgebraicGeometry.tfae_subsingleton_sheafH_of_isMaximalProPSubgroup, Stacks.GaloisCohomology.isZero_continuousGroupCohomology_units_of_forall_brauer, Stacks.GaloisCohomology.isZero_continuousGroupCohomology_units_and_torsion_of_forall_brauer, Stacks.GaloisCohomology.isZero_continuousGroupCohomology_of_isAddTorsion
statement: formalized
proof: formalized
---

# 59.67 Galois cohomology

Section 59.67 of the Stacks Project, [Tag 0A2M](https://stacks.math.columbia.edu/tag/0A2M). 12 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DV7, a lemma

[Tag 0DV7](https://stacks.math.columbia.edu/tag/0DV7) in the Stacks Project.

**`Stacks.EtaleCohomology.isPrimePowerTorsion_nontrivial_sheafH_smallEtalePushforwardAb_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/FiniteEtaleLimit.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/FiniteEtaleLimit.lean#L104). The attribute's comment: “given F on X, take G = g\_* F”.

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

**`Stacks.EtaleCohomology.isPrimePowerTorsion_nontrivial_sheafH_smallEtalePullbackAb_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/FiniteEtaleLimit.lean, line 266](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/FiniteEtaleLimit.lean#L266). The attribute's comment: “given G on S, take F = g⁻¹ G”.

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

**`Stacks.EtaleCohomology.exists_isPrimePowerTorsion_nontrivial_sheafH_iff_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/FiniteEtaleLimit.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/FiniteEtaleLimit.lean#L288). The attribute's comment: “(1) ⇔ (2)”.

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

**`AlgebraicGeometry.subsingleton_sheafH_iff_of_isMaximalProPSubgroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MaximalProEllVanishing.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MaximalProEllVanishing.lean#L139).

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

**`AlgebraicGeometry.tfae_subsingleton_sheafH_of_isMaximalProPSubgroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MaximalProEllVanishing.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MaximalProEllVanishing.lean#L170). The attribute's comment: “both readings of `ℓ`-torsion: `ℓ`-power torsion (1) and killed by `ℓ` (2)”.

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

**`Stacks.GaloisCohomology.isZero_continuousGroupCohomology_units_of_forall_brauer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupVanishingAllDegrees.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupVanishingAllDegrees.lean#L66). The attribute's comment: “part (1) in full, for the derived-functor groups continuousGroupCohomology of Stacks 04JR: H^q(Gal(Ω/K), Ωˣ) = 0 for every q ≥ 1, where Ω is any separably closed field Galois over K, so at Ω = K^sep this is exactly the tag's part (1). The hypothesis is the source's own, Br(K') = 0 for every finite extension K'/K, and the degree range is the source's. Degree one is isZero\_continuousGroupCohomology\_units\_one (Hilbert 90), degree two is isZero\_continuousGroupCohomology\_units\_two (the crossed-product argument, from Br(K) = 0), and the degrees q ≥ 3 come from part (2), isZero\_continuousGroupCohomology\_of\_isAddTorsion, through isZero\_continuousGroupCohomology\_of\_forall\_isAddTorsion: multiplication by a positive integer n on a discrete module has kernel and cokernel killed by n, so part (2) and two passes of the long exact sequence of the δ-functor of Stacks 010Q make it injective on H^q for q ≥ 3, while every class is killed by some positive integer by Stacks 0DV3 part (1). Both parts together, at Ω = K^sep, are isZero\_continuousGroupCohomology\_units\_and\_torsion\_of\_forall\_brauer”. References: SGA 4½ Arcata (3.1.6).

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

**`Stacks.GaloisCohomology.isZero_continuousGroupCohomology_units_and_torsion_of_forall_brauer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/SeparableClosureVanishing.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/SeparableClosureVanishing.lean#L77). The attribute's comment: “the whole proposition, parts (1) and (2) together in one statement, under the source's hypothesis Br(K') = 0 for every finite extension K'/K. The first conjunct is H^q(Gal(K^sep/K), (K^sep)ˣ) = 0 for every q ≥ 1, at the discrete Galois module unitsContinuousGModule; the second is H^q(Gal(K^sep/K), M) = 0 for every torsion discrete Galois module M and every q ≥ 2. Both are values of the derived-functor groups continuousGroupCohomology of Stacks 04JR. The first conjunct is isZero\_continuousGroupCohomology\_units\_of\_forall\_brauer at Ω = K^sep, which takes the same Brauer hypothesis verbatim; the second is isZero\_continuousGroupCohomology\_of\_isAddTorsion at Ω = K^sep, whose hypothesis -- Br(L) = 0 at the intermediate fields L of K^sep/K finite over K -- is the source's at K' = ↥L. Every clause of the proposition is established here”. References: SGA 4½ Arcata (3.1.6).

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

**`Stacks.GaloisCohomology.isZero_continuousGroupCohomology_of_isAddTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/TorsionGaloisVanishing.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/TorsionGaloisVanishing.lean#L60). The attribute's comment: “part (2) in full, for the derived-functor groups continuousGroupCohomology of Stacks 04JR: H^q(Gal(Ω/K), M) = 0 for every torsion discrete Galois module M and every q ≥ 2, where Ω is any separably closed field Galois over K, so at Ω = K^sep this is exactly the tag's part (2). The Brauer hypothesis asks for Br(L) = 0 at the intermediate fields L of Ω/K finite over K, each of which is a finite extension of K, so the source's hypothesis implies it and this statement implies the tag's part (2). The proof is the source's dévissage done on locally constant cochains. A locally constant 2-cocycle on a profinite group takes finitely many values, so it is a cocycle with values in a finite submodule; a finite module is reduced to a module killed by a prime p along its p-torsion subgroup; a finite module killed by p is handled over an open subgroup of index prime to p -- the preimage of a p-Sylow subgroup of a finite quotient -- where the action factors through a p-group and the module is filtered by copies of Z/p with trivial action, and the restriction-corestriction identity cor o res = n, written out on cochains, takes the trivialization back to the whole group; and Z/p with trivial action is the Kummer sequence of Stacks 03PL away from the characteristic and the Artin-Schreier sequence of Stacks 0A3J in the characteristic, each fed by degrees one and two of part (1). Degrees above two come from dimension shifting along the module of locally constant functions into a torsion divisible hull, which is an injective object of the category of Stacks 04JP whose cokernel is again torsion. Both parts together, at Ω = K^sep, are isZero\_continuousGroupCohomology\_units\_and\_torsion\_of\_forall\_brauer”. References: SGA 4½ Arcata (3.1.6), “more general”.

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

**`IsCField`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/CFields.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/CFields.lean#L40). References: SGA 4½ Arcata (3.2.1), “more general”.

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

**`exists_nonzero_common_zero_of_isHomogeneous`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/HomogeneousZeros.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/HomogeneousZeros.lean#L40). The attribute's comment: “an algebraically closed field is `C_r`: the one-polynomial case `s = 1`”.

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

**`exists_nonzero_common_zero_of_isHomogeneous`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/HomogeneousZeros.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/HomogeneousZeros.lean#L40).

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

**`brauerGroup_eq_one_of_isCField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/BrauerGroupCField.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/BrauerGroupCField.lean#L313). References: SGA 4½ Arcata (3.2.2).

> Every Brauer class over a C₁ field is trivial.

```lean
theorem brauerGroup_eq_one_of_isCField (K : Type u) [Field K]
    (hK : IsCField K 1) (x : BrauerGroup K) : x = 1
```

## Tag 03RE, a definition

[Tag 03RE](https://stacks.math.columbia.edu/tag/03RE) in the Stacks Project.

**`AlgebraicGeometry.IsCurve`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/Defs.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Curve/Defs.lean#L46). The attribute's comment: “the curve clause”. References: EGA II (7.4.2), “special case”.

> **Stacks Project, Tag 0A23.** A curve over a field is a variety of Krull dimension one.

```lean
public class IsCurve (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) : Prop
    extends IsVariety k f
```

**`AlgebraicGeometry.IsVariety`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Basic.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Defs/Basic.lean#L50). The attribute's comment: “the variety clause”.

> A scheme over a field is a variety when it is integral and its structure morphism is
> separated and of finite type.

```lean
class IsVariety (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) : Prop
    extends IsIntegral X, IsSeparated f, LocallyOfFiniteType f, QuasiCompact f
```

## Tag 03RD, a theorem

[Tag 03RD](https://stacks.math.columbia.edu/tag/03RD) in the Stacks Project.

**`AlgebraicGeometry.isCField_functionField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/TsenFunctionField.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/TsenFunctionField.lean#L86).

> **Stacks Project, Tag 03RD (Tsen's theorem).** The function field of a variety of dimension
> `r` over an algebraically closed field `k` is a \(C_r\) field.

```lean
theorem isCField_functionField (k : Type u) [Field k] [IsAlgClosed k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsVariety k f] {r : ℕ} (hr : topologicalKrullDim X = r) :
    IsCField X.functionField r
```

## Tag 03RF, a lemma

[Tag 03RF](https://stacks.math.columbia.edu/tag/03RF) in the Stacks Project.

**`AlgebraicGeometry.brauerGroup_functionField_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/BrauerGroupFunctionField.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/BrauerGroupFunctionField.lean#L84). References: SGA 4½ Arcata (3.2.4), “q = 2 (Brauer group)”; SGA 4½ Arcata (3.2.2), “special case”.

> The Brauer group of the function field of a curve over an algebraically closed field is
> trivial.

```lean
theorem brauerGroup_functionField_eq_one (k : Type u) [Field k] [IsAlgClosed k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsCurve k f]
    (y : BrauerGroup X.functionField) : y = 1
```

## Tag 03RG, a lemma

[Tag 03RG](https://stacks.math.columbia.edu/tag/03RG) in the Stacks Project.

**`Stacks.EtaleCohomology.subsingleton_sheafH_multiplicativeSheaf_spec_of_trdeg_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupTranscendenceDegreeOneVanishing.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupTranscendenceDegreeOneVanishing.lean#L67). References: SGA 4½ Arcata (3.1.6), “clause i), special case”; SGA 4½ Arcata (3.2.4).

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

**`Stacks.EtaleCohomology.subsingleton_sheafH_multiplicativeSheaf_of_trdeg_eq_one`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupTranscendenceDegreeOneVanishing.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GaloisCohomology/MultiplicativeGroupTranscendenceDegreeOneVanishing.lean#L110). The attribute's comment: “vanishing of the positive-degree étale cohomology of 𝐆\_m over a transcendence-degree-one extension of an algebraically closed field, proved from Tag 03R8 and Tag 03QU with no hypothesis beyond the tag's”.

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
