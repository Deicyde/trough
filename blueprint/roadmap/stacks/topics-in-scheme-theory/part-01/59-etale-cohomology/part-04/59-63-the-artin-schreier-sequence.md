---
declaration: section
origin: cited
lean: Stacks.ArtinSchreier.constantArtinSchreierSequence_shortExact, Stacks.ArtinSchreier.subsingleton_etaleH_constantZMod_of_topologicalKrullDim_le_unconditional, Stacks.ArtinSchreier.subsingleton_etaleH_constantZMod_of_isAffine_constantSequence, Stacks.ArtinSchreier.subsingleton_etaleH_constantZMod_of_topologicalKrullDim_le_constantSequence, fixedPoints_finiteDimensional_of_frobenius_semilinear, finrank_fixedPoints_le_of_frobenius_semilinear, frobeniusSemilinear_sub_id_surjective, AlgebraicGeometry.finiteDimensional_cohomologyOverField_of_finiteType_of_dimension_zero
statement: formalized
proof: formalized
---

# 59.63 The Artin-Schreier sequence

Section 59.63 of the Stacks Project, [Tag 0A3J](https://stacks.math.columbia.edu/tag/0A3J). 6 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A3J, the section

[Tag 0A3J](https://stacks.math.columbia.edu/tag/0A3J) in the Stacks Project.

**`Stacks.ArtinSchreier.constantArtinSchreierSequence_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/ConstantKernel.lean, line 404](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/ConstantKernel.lean#L404). References: SGA 1 XI (6.7); SGA 4 IX (3.5).

> **The Artin–Schreier sequence.** For a scheme `X` of characteristic `p`,
>
> `0 ⟶ 𝐙/p𝐙 ⟶ 𝐆_a ⟶ 𝐆_a ⟶ 0`
>
> is a short exact sequence of abelian sheaves on the small étale site of `X`, the second map being
> `x ↦ x ^ p - x`.

```lean
theorem constantArtinSchreierSequence_shortExact :
    (constantArtinSchreierSequence.{u, v} X hp hX).ShortExact
```

## Tag 0A3K, a lemma

[Tag 0A3K](https://stacks.math.columbia.edu/tag/0A3K) in the Stacks Project.

**`Stacks.ArtinSchreier.subsingleton_etaleH_constantZMod_of_topologicalKrullDim_le_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/ConstantCoefficientVanishingUnconditional.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/ConstantCoefficientVanishingUnconditional.lean#L48). The attribute's comment: “(2)”.

> Let `p` be a prime and let `S` be a quasi-compact and quasi-separated scheme of
> characteristic `p` and of dimension at most `d`. Then `H ^ q (S_étale, 𝐙/p𝐙) = 0` for every
> `q ≥ d + 2`. Only the upper bound on the dimension of `S` is needed.

```lean
public theorem subsingleton_etaleH_constantZMod_of_topologicalKrullDim_le_unconditional (p : ℕ)
    [Fact p.Prime] (S : Scheme.{u}) [CompactSpace S] [QuasiSeparatedSpace S]
    (hS : (p : Γ(S, ⊤)) = 0)
    [HasExt.{w} (Sheaf S.smallEtaleTopology AddCommGrpCat.{u + 1})]
    (d : ℕ) (hdim : topologicalKrullDim (S : Type u) ≤ (d : WithBot ℕ∞))
    (q : ℕ) (hq : d + 2 ≤ q) :
    Subsingleton (Sheaf.H.{w, u + 1} (etaleConstantZMod S p) q)
```

**`Stacks.ArtinSchreier.subsingleton_etaleH_constantZMod_of_isAffine_constantSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/ConstantSequenceDatum.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/ConstantSequenceDatum.lean#L199). The attribute's comment: “part (1)”.

> **[Stacks, Tag 0A3K] (1).** Let `p` be a prime and let `S` be an affine scheme on which `p`
> vanishes. Then `H ^ q (S_étale, 𝐙/p𝐙) = 0` for every `q ≥ 2`.
>
> The cohomology of the structure sheaf of an affine scheme vanishes in positive degree by
> [Stacks, Tag 01XB], so the Artin–Schreier degree shift applies with `n = 0`.

```lean
public theorem subsingleton_etaleH_constantZMod_of_isAffine_constantSequence (p : ℕ)
    [Fact p.Prime] (S : Scheme.{u}) [IsAffine S] (hS : (p : Γ(S, ⊤)) = 0)
    [HasExt.{w} (Sheaf S.smallEtaleTopology AddCommGrpCat.{u + 1})]
    (q : ℕ) (hq : 2 ≤ q) :
    Subsingleton (Sheaf.H.{w, u + 1} (etaleConstantZMod S p) q)
```

**`Stacks.ArtinSchreier.subsingleton_etaleH_constantZMod_of_topologicalKrullDim_le_constantSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/ConstantSequenceDatum.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/ConstantSequenceDatum.lean#L216). The attribute's comment: “part (2)”. References: SGA 4½ Arcata (4.4), “H^q(X\_0, special case”.

> **[Stacks, Tag 0A3K] (2).** Let `p` be a prime and let `S` be a quasi-compact and
> quasi-separated scheme on which `p` vanishes and of dimension at most `d`. Then
> `H ^ q (S_étale, 𝐙/p𝐙) = 0` for every `q ≥ d + 2`.
>
> The underlying space of `S` is spectral, so the cohomology of the structure sheaf vanishes above
> its dimension by [Stacks, Tag 0A3G], and the Artin–Schreier degree shift applies with `n = d`.

```lean
public theorem subsingleton_etaleH_constantZMod_of_topologicalKrullDim_le_constantSequence
    (p : ℕ) [Fact p.Prime] (S : Scheme.{u}) [CompactSpace S] [QuasiSeparatedSpace S]
    (hS : (p : Γ(S, ⊤)) = 0)
    [HasExt.{u} (Sheaf (Opens.grothendieckTopology (S : Type u)) AddCommGrpCat.{u})]
    [HasExt.{w} (Sheaf S.smallEtaleTopology AddCommGrpCat.{u + 1})]
    (d : ℕ) (hdim : topologicalKrullDim (S : Type u) ≤ (d : WithBot ℕ∞))
    (q : ℕ) (hq : d + 2 ≤ q) :
    Subsingleton (Sheaf.H.{w, u + 1} (etaleConstantZMod S p) q)
```

## Tag 0A3L, a lemma

[Tag 0A3L](https://stacks.math.columbia.edu/tag/0A3L) in the Stacks Project.

**`fixedPoints_finiteDimensional_of_frobenius_semilinear`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/FrobeniusFixedPoints.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/FrobeniusFixedPoints.lean#L145). The attribute's comment: “kernel\_bound”.

> The fixed points of a Frobenius-semilinear additive endomorphism of a
> finite-dimensional vector space are finite-dimensional over the prime field.

```lean
theorem fixedPoints_finiteDimensional_of_frobenius_semilinear
    (hF : ∀ (c : k) (x : V), F (c • x) = c ^ p • F x) :
    letI : Module (ZMod p) V :=
      Module.compHom V (ZMod.castHom (dvd_refl p) k)
    FiniteDimensional (ZMod p) (AddMonoidHom.ker (F - AddMonoidHom.id V))
```

**`finrank_fixedPoints_le_of_frobenius_semilinear`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/FrobeniusFixedPoints.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/FrobeniusFixedPoints.lean#L159). The attribute's comment: “kernel\_bound”.

> The dimension over the prime field of the fixed points of a
> Frobenius-semilinear additive endomorphism is at most the dimension of the
> original vector space.

```lean
theorem finrank_fixedPoints_le_of_frobenius_semilinear
    (hF : ∀ (c : k) (x : V), F (c • x) = c ^ p • F x) :
    letI : Module (ZMod p) V :=
      Module.compHom V (ZMod.castHom (dvd_refl p) k)
    Module.finrank (ZMod p) (AddMonoidHom.ker (F - AddMonoidHom.id V)) ≤
      Module.finrank k V
```

**`frobeniusSemilinear_sub_id_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/FrobeniusSurjectivity.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/FrobeniusSurjectivity.lean#L40). The attribute's comment: “surjectivity”. References: SGA 7 XXII (1.2), “alg. closed, q=p”.

> Let `V` be a finite-dimensional vector space over an algebraically closed field `k` of
> positive characteristic `p`. If the additive endomorphism `F` is Frobenius-semilinear, then
> `F - 1` is surjective.

```lean
public theorem frobeniusSemilinear_sub_id_surjective
    {p : ℕ} (k : Type*) [Field k] [IsAlgClosed k] [CharP k p] (hp : 0 < p)
    (V : Type*) [AddCommGroup V] [Module k V] [FiniteDimensional k V]
    (F : V →+ V) (hF : ∀ (a : k) (v : V), F (a • v) = a ^ p • F v) :
    Function.Surjective (fun v ↦ F v - v)
```

## Tag 0A3M, a lemma

[Tag 0A3M](https://stacks.math.columbia.edu/tag/0A3M) in the Stacks Project.

**`AlgebraicGeometry.finiteDimensional_cohomologyOverField_of_finiteType_of_dimension_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeCoherentFiniteness/Basic.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/TopDegreeCoherentFiniteness/Basic.lean#L96). The attribute's comment: “the case `dim X = 0`, in every degree and without the separatedness hypothesis”.

> For `X` of finite type over a field `k` with `dim(X) = 0` and `ℱ` coherent, every
> `Hⁿ(X, ℱ)` is a finite-dimensional `k`-vector space.

```lean
theorem finiteDimensional_cohomologyOverField_of_finiteType_of_dimension_zero
    [LocallyOfFiniteType f] [QuasiCompact f] (hdim : topologicalKrullDim (X : Type u) = 0)
    (F : X.Modules) [F.IsCoherent] (n : ℕ) :
    FiniteDimensional k (cohomologyOverField k f F n)
```

**`AlgebraicGeometry.finiteDimensional_topCohomology_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeCoherentFiniteness/Basic.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/TopDegreeCoherentFiniteness/Basic.lean#L120). The attribute's comment: “the case of an affine `X`”.

> Let `X` be an affine scheme separated and of finite type over a field `k`, let `ℱ` be a
> coherent `𝒪_X`-module and let `d = dim(X)`. Then `H^d(X, ℱ)` is a finite-dimensional `k`-vector
> space.

```lean
theorem finiteDimensional_topCohomology_of_isAffine [IsAffine X] [LocallyOfFiniteType f]
    [QuasiCompact f] [IsSeparated f] (F : X.Modules) [F.IsCoherent] (d : ℕ)
    (hd : topologicalKrullDim (X : Type u) = (d : WithBot ℕ∞)) :
    FiniteDimensional k (cohomologyOverField k f F d)
```

**`AlgebraicGeometry.finiteDimensional_cohomologyOverField_topologicalKrullDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeCoherentFiniteness/Full.lean, line 376](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/TopDegreeCoherentFiniteness/Full.lean#L376).

> **[Stacks, Tag 0A3M].** Let `X` be a separated scheme of finite type over a field `k` and let
> `ℱ` be a coherent `𝒪_X`-module. Then `dim_k H^d(X, ℱ) < ∞`, where `d = dim(X)`.

```lean
theorem finiteDimensional_cohomologyOverField_topologicalKrullDim (k : Type u) [Field k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f] [QuasiCompact f]
    [IsSeparated f] (F : X.Modules) (hF : _root_.SheafOfModules.IsCoherent F) (d : ℕ)
    (hd : topologicalKrullDim (X : Type u) = (d : WithBot ℕ∞)) :
    FiniteDimensional k (cohomologyOverField k f F d)
```

**`AlgebraicGeometry.TopDegreeFiniteness.finiteDimensional_topCohomology_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeCoherentFiniteness/General.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/TopDegreeCoherentFiniteness/General.lean#L293).

> Let `X` be a separated scheme of finite type over a field `k`, let `ℱ` be a coherent
> `𝒪_X`-module and let `d = dim(X)`. Then `H^d(X, ℱ)` is a finite-dimensional `k`-vector space.

```lean
theorem finiteDimensional_topCohomology_of_isSeparated {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] [QuasiCompact f] [IsSeparated f] (F : X.Modules) [F.IsCoherent]
    (d : ℕ) (hd : topologicalKrullDim X = (d : WithBot ℕ∞)) :
    FiniteDimensional k (cohomologyOverField k f F d)
```

**`AlgebraicGeometry.finiteDimensional_topCohomology_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeCoherentFiniteness/Separated.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/TopDegreeCoherentFiniteness/Separated.lean#L156). The attribute's comment: “the full statement: for X separated and of finite type over a field k, F a coherent O\_X-module and d = dim X, the k-vector space H^d(X, F) is finite-dimensional”.

> **[Stacks, Tag 0A3M].** Let `X` be a separated scheme of finite type over a field `k`, with
> structure morphism `f : X ⟶ Spec k`, let `ℱ` be a coherent `𝒪_X`-module and let `d = dim(X)`.
> Then `H^d(X, ℱ)` is a finite-dimensional `k`-vector space.
>
> Nagata's compactification theorem ([Stacks, Tag 0F41],
> `AlgebraicGeometry.hasCompactification_of_compactSpace_quasiSeparatedSpace`, applied over the
> affine base `Spec k`) factors `f` as a quasi-compact open immersion followed by a proper
> morphism, and `finiteDimensional_cohomologyOverField_of_isImmersion_of_isProper` applies.

```lean
theorem finiteDimensional_topCohomology_of_isSeparated {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] [QuasiCompact f] [IsSeparated f] (F : X.Modules) [F.IsCoherent]
    (d : ℕ) (hd : topologicalKrullDim (X : Type u) = (d : WithBot ℕ∞)) :
    FiniteDimensional k (cohomologyOverField k f F d)
```

## Tag 0A3N, a lemma

[Tag 0A3N](https://stacks.math.columbia.edu/tag/0A3N) in the Stacks Project.

**`Stacks.ArtinSchreier.subsingleton_etaleH_constantZMod_of_isAlgClosed_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/TopDegreeVanishingUnconditional.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/TopDegreeVanishingUnconditional.lean#L45). References: SGA 4½ Arcata (4.4), “special case”.

> Let `X` be separated and of finite type over an algebraically closed field `k` of
> characteristic `p > 0`, and let `d` be a natural number with `dim X ≤ d`. Then
> `H ^ q (X_étale, 𝐙/p𝐙) = 0` for every `q ≥ d + 1`.

```lean
public theorem subsingleton_etaleH_constantZMod_of_isAlgClosed_unconditional {p : ℕ} (hp : 0 < p)
    (k : Type u) [Field k] [IsAlgClosed k] [CharP k p] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [LocallyOfFiniteType f] [QuasiCompact f] [IsSeparated f]
    [HasExt.{w} (Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})]
    (d : ℕ) (hd : topologicalKrullDim (X : Type u) ≤ (d : WithBot ℕ∞))
    (q : ℕ) (hq : d + 1 ≤ q) :
    Subsingleton (Sheaf.H.{w, u + 1} (etaleConstantZMod X p) q)
```

## Tag 0A3P, a lemma

[Tag 0A3P](https://stacks.math.columbia.edu/tag/0A3P) in the Stacks Project.

**`Stacks.ArtinSchreier.finite_etaleH_constantZMod_of_isProper'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/ConstantCoefficientsUnconditional.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/ConstantCoefficientsUnconditional.lean#L69). The attribute's comment: “part (1)”.

> Let `X` be a scheme proper over an algebraically closed field `k` of characteristic `p > 0`.
> Then `H ^ q (X_étale, 𝐙/p𝐙)` is finite for every `q`.

```lean
theorem finite_etaleH_constantZMod_of_isProper' {p : ℕ} (hp : 0 < p) (k : Type u) [Field k]
    [IsAlgClosed k] [CharP k p] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f]
    [HasExt.{w} (Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})] (q : ℕ) :
    Finite (Sheaf.H.{w, u + 1} (etaleConstantZMod X p) q)
```

**`Stacks.ArtinSchreier.finite_etaleH_constantZMod_of_isProper_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/ProperConstantCoefficientsUnconditional.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/ProperConstantCoefficientsUnconditional.lean#L173). The attribute's comment: “part (1): H^q(X\_et, Z/pZ) is finite”.

> Let `X` be a scheme proper over an algebraically closed field `k` of characteristic `p > 0`.
> Then `H ^ q (X_étale, 𝐙/p𝐙)` is finite for every `q`.

```lean
public theorem finite_etaleH_constantZMod_of_isProper_unconditional (hp : 0 < p) [IsAlgClosed k]
    [CharP k p] [IsProper f] (q : ℕ) :
    Finite (Sheaf.H.{w, u + 1} (etaleConstantZMod X p) q)
```

**`Stacks.ArtinSchreier.bijective_etaleCohomologyBaseChangeMap_constantZMod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/ProperConstantCoefficientsUnconditional.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/ProperConstantCoefficientsUnconditional.lean#L302). The attribute's comment: “part (2): restriction to the scalar extension X\_\{k'} is bijective on H^q(X\_et, Z/pZ)”.

> Let `X` be proper over an algebraically closed field `k` of characteristic `p > 0`, and let
> `k'/k` be an extension of algebraically closed fields. Then the restriction map
> `H ^ q (X_étale, 𝐙/p𝐙) ⟶ H ^ q (X_{k'}, 𝐙/p𝐙)` to the scalar extension
> `X_{k'} = X ×_{Spec k} Spec k'` is bijective.

```lean
public theorem bijective_etaleCohomologyBaseChangeMap_constantZMod {p : ℕ} (hp : 0 < p)
    [IsAlgClosed k] [IsAlgClosed k'] [CharP k p] [IsProper f]
    [HasExt.{w} (Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})]
    [HasExt.{w} (Sheaf (scalarExtension k k' f).smallEtaleTopology AddCommGrpCat.{u + 1})]
    (q : ℕ) :
    Function.Bijective
      (etaleCohomologyBaseChangeMap.{u, 0, w} k k' f (etaleConstantZMod X p) q)
```

**`Stacks.ArtinSchreier.finite_etaleH_constantZMod_of_isProper_of_isAlgClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/ProperFiniteness.lean, line 36](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/ProperFiniteness.lean#L36). The attribute's comment: “part (1)”.

> **[Stacks, Tag 0A3P] (1).** Let `X` be a proper scheme over an algebraically closed field `k`
> of characteristic `p > 0`. Then `H ^ q (X_étale, 𝐙/p𝐙)` is finite for every `q`.

```lean
theorem finite_etaleH_constantZMod_of_isProper_of_isAlgClosed {p : ℕ} (hp : p.Prime)
    (k : Type u) [Field k] [IsAlgClosed k] [CharP k p] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f]
    [HasExt.{w} (Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})] (q : ℕ) :
    Finite (Sheaf.H.{w, u + 1} (etaleConstantZMod X p) q)
```

**`Stacks.ArtinSchreier.bijective_etaleCohomologyRestrictionMap_constantZMod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/ProperScalarExtension.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/ProperScalarExtension.lean#L166). The attribute's comment: “part (2)”.

> **[Stacks, Tag 0A3P] (2).** Let `k ⊆ k'` be an extension of algebraically closed fields of
> characteristic `p > 0` and let `X` be a proper scheme over `k`. Then restriction along
> `X_{k'} ⟶ X` is bijective on `H^q(X_étale, 𝐙/p𝐙)` for every `q`.
>
> The target of the restriction map is the cohomology of the inverse image of the constant sheaf,
> which is the constant sheaf `𝐙/p𝐙` on `X_{k'}` by
> `Stacks.EtaleCohomology.etaleAbelianInverseImageConstantIso`.

```lean
theorem bijective_etaleCohomologyRestrictionMap_constantZMod {p : ℕ} (hp : 0 < p)
    [IsAlgClosed k] [IsAlgClosed k'] [CharP k p] [IsProper f] (q : ℕ) :
    Function.Bijective (etaleCohomologyRestrictionMap.{u, 0, w} (scalarExtensionFst k k' f)
      (etaleConstantZMod X p) q)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.63, Tag 0A3J](https://stacks.math.columbia.edu/tag/0A3J)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
