---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.formalBranches, AlgebraicGeometry.Stack.formalBranchesEquiv, AlgebraicGeometry.Stack.formalBranchComponent_surjective_and_canonical, AlgebraicGeometry.Stack.formalBranchMultiplicity, AlgebraicGeometry.Stack.formalBranchMultiplicity_independent, AlgebraicGeometry.Stack.formalBranchMultiplicity_independent_of_realization, MvPowerSeries.length_localization_minimalPrimesEquivOfRingEquiv, AlgebraicGeometry.Stack.componentMultiplicity_formalBranchComponent
statement: formalized
proof: formalized
---

# 107.4 Formal branches and multiplicities

Section 107.4 of the Stacks Project, [Tag 0DR9](https://stacks.math.columbia.edu/tag/0DR9). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DRA, a definition

[Tag 0DRA](https://stacks.math.columbia.edu/tag/0DRA) in the Stacks Project.

**`AlgebraicGeometry.Stack.formalBranches`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FormalBranches.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FormalBranches.lean#L107). The attribute's comment: “the irreducible components of Spec A for a versal ring A, recorded by their generic points”.

> **Stacks 0DRA.** The formal branches of `𝒳` through `x₀`, read off a versal ring `A` to `𝒳`
> at `x₀`: the irreducible components of `Spec A`, each recorded by its generic point, that is, the
> set of minimal primes of `A`. The identification of these sets for different versal rings, which
> the source uses to make the definition independent of `A`, is
> `AlgebraicGeometry.Stack.formalBranchesEquiv`.

```lean
def formalBranches
    (_hA : IsVersalRingAt D iΛ hiΛ x₀ hx₀ hfinite A) : Set (Ideal A)
```

**`AlgebraicGeometry.Stack.formalBranchesEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FormalBranchIdentification.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FormalBranchIdentification.lean#L191). The attribute's comment: “the identification of the formal branches read off two versal rings A, A' along a map A → A' compatible with the versal formal objects, independent of the map”.

> **Stacks 0DRA.** The formal branches of `𝒳` through `x₀` read off two versal rings
> `A = ξ.base` and `A' = ξ'.base` are identified along any map `A → A'` compatible with the versal
> formal objects (the base of a morphism `a : ξ ⟶ ξ'`), by `𝔭 ↦ a(𝔭)A'`. This is the procedure of
> the source, which uses the formally smooth comparison of Stacks 0DQX and 0DR1
> (`AlgebraicGeometry.Stack.exists_formallySmooth_comparison`); the identification does not depend
> on the map (`AlgebraicGeometry.Stack.formalBranchesEquiv_eq`) and is compatible with identities and
> composition (`AlgebraicGeometry.Stack.formalBranchesEquiv_refl`,
> `AlgebraicGeometry.Stack.formalBranchesEquiv_trans`), so the set of formal branches is
> independent of the choice of versal ring.

```lean
def formalBranchesEquiv (a : ξ ⟶ ξ') :
    formalBranches D iΛ hiΛ x₀ hx₀ hfinite ξ.base ⟨ξ, rfl, hξ⟩ ≃
      formalBranches D iΛ hiΛ x₀ hx₀ hfinite ξ'.base ⟨ξ', rfl, hξ'⟩
```

## Tag 0DRB, a lemma

[Tag 0DRB](https://stacks.math.columbia.edu/tag/0DRB) in the Stacks Project.

**`AlgebraicGeometry.Stack.formalBranchComponent_surjective_and_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FormalBranchComponents.lean, line 1077](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FormalBranchComponents.lean#L1077).

> **Stacks 0DRB.** In the situation of Definition 0DRA — an algebraic stack `𝒳` locally of
> finite type over a locally Noetherian scheme `S`, a point `x₀ : Spec k ⟶ 𝒳` with `k` of finite
> type over `S`, and a versal ring `A` to `𝒳` at `x₀`, the base of a versal formal object `ξ` with
> its morphism `y : Spec A ⟶ 𝒳` of Stacks 0DR1 — there is a canonical surjection from the formal
> branches of `𝒳` through `x₀` to the irreducible components of `|𝒳|` containing `x₀`.
>
> The map is `AlgebraicGeometry.Stack.formalBranchComponent`: a branch, recorded by its generic
> point `P`, goes to the closure of the image of `P` under `Spec A ⟶ 𝒳`
> (`AlgebraicGeometry.Stack.coe_formalBranchComponent`). The first conjunct is surjectivity. The
> second is canonicity: for any other versal formal object at `x₀`, for any presentation of `x₀`,
> with versal ring `A'` and realization `y'`, the two maps agree along the identification of the
> branches of `A` and `A'` by the faithfully flat comparison of part (1) of Stacks 0DR1, in
> whichever direction it goes.

```lean
theorem formalBranchComponent_surjective_and_canonical :
    Function.Surjective (formalBranchComponent D iΛ hiΛ x₀ hx₀ hfinite ξ hξ Ry) ∧
    ∀ (Λ' : Type u) [CommRing Λ'] [Algebra Λ' k]
      (iΛ' : Spec (.of Λ') ⟶ D.S) (hiΛ' : _root_.AlgebraicGeometry.IsOpenImmersion iΛ')
      (hx₀' : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
        Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ' k)) ≫ iΛ'))
      (hfinite' : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap Λ' k)) ≫ iΛ') ∧
        QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ' k)) ≫ iΛ'))
      (ξ' : Deformation.FormalObject (Deformation.Artin.predeformationCategory iΛ'
        (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) x₀ hx₀').projection)
      (hξ' : Deformation.IsVersal
        (Deformation.Artin.predeformationCategory_isPredeformationCategory
          D.B D.hS iΛ' D.𝒳.val.val.p x₀ hx₀' D.𝒳.val.property).cofibered ξ')
      (hA' : D.B.Contains (Spec (.of ξ'.base))) (y' : D.𝒳.val.val.obj)
      (hy' : D.𝒳.val.val.p.obj y' = Deformation.Artin.baseOver D.B D.S D.hS
        (Deformation.Artin.completeLocalAlgFormalBase iΛ' hfinite' ξ'.base) hA')
      (Ry' : (Deformation.Artin.FormalObject.ofPredeformation D.B D.S D.hS iΛ' D.𝒳.val.val.p
        x₀ hx₀' hfinite' ξ').Realization hA' y' hy'),
      (∃ φ : (ξ'.base : Type u) →+* ξ.base, Flat (Spec.map (CommRingCat.ofHom φ)) ∧
        Surjective (Spec.map (CommRingCat.ofHom φ)) ∧
        ∀ P, ∃ hP : P.1.comap φ ∈ formalBranches D iΛ' hiΛ' x₀ hx₀' hfinite' ξ'.base
            ⟨ξ', rfl, hξ'⟩,
          (formalBranchComponent D iΛ hiΛ x₀ hx₀ hfinite ξ hξ Ry P).1 =
            (formalBranchComponent D iΛ' hiΛ' x₀ hx₀' hfinite' ξ' hξ' Ry' ⟨_, hP⟩).1) ∨
      (∃ φ : (ξ.base : Type u) →+* ξ'.base, Flat (Spec.map (CommRingCat.ofHom φ)) ∧
        Surjective (Spec.map (CommRingCat.ofHom φ)) ∧
        ∀ P', ∃ hP : P'.1.comap φ ∈ formalBranches D iΛ hiΛ x₀ hx₀ hfinite ξ.base ⟨ξ, rfl, hξ⟩,
          (formalBranchComponent D iΛ' hiΛ' x₀ hx₀' hfinite' ξ' hξ' Ry' P').1 =
            (formalBranchComponent D iΛ hiΛ x₀ hx₀ hfinite ξ hξ Ry ⟨_, hP⟩).1)
```

## Tag 0DRC, a definition

[Tag 0DRC](https://stacks.math.columbia.edu/tag/0DRC) in the Stacks Project.

**`AlgebraicGeometry.Stack.formalBranchMultiplicity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FormalBranches.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FormalBranches.lean#L156). The attribute's comment: “the multiplicity of a formal branch, computed on a versal ring A; its independence of A is formalBranchMultiplicity\_independent”.

> **Stacks 0DRC.** The multiplicity of a formal branch of `𝒳` through `x₀`: the multiplicity of
> the corresponding irreducible component of `Spec A`, that is, the length over itself of the local
> ring of `Spec A` at the generic point of that component. The source takes `A` to be any versal
> ring; the value does not depend on that choice along the identification of branches
> (`AlgebraicGeometry.Stack.formalBranchMultiplicity_independent`).

```lean
def formalBranchMultiplicity {p : Ideal A}
    (hp : p ∈ formalBranches D iΛ hiΛ x₀ hx₀ hfinite A hA) : ℕ∞
```

**`AlgebraicGeometry.Stack.formalBranchMultiplicity_independent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FormalBranchMultiplicityIndependence.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FormalBranchMultiplicityIndependence.lean#L125). The attribute's comment: “the multiplicity is independent of the versal ring: for any two versal rings, the identification of branches along the comparison A ≅ A'[[t₁,…,t\_r]] preserves it”.

> **Stacks 0DRC, for any two versal rings.** Let `A` and `A'` be versal rings to `𝒳` at `x₀`,
> for any two presentations of `x₀` over affine opens of `S`. After possibly swapping them there is
> an isomorphism `A ≅ A'[[t₁, …, t_r]]` over `S` (Stacks 0DQX), and along the identification
> `𝔭 ↦ φ(𝔭) A` of formal branches it induces, multiplicities agree. Hence the multiplicity of a
> formal branch, `AlgebraicGeometry.Stack.formalBranchMultiplicity`, does not depend on the choice
> of versal ring.

```lean
theorem formalBranchMultiplicity_independent :
    (∃ r : ℕ, ∃ e : (A : Type u) ≃+* MvPowerSeries (Fin r) A',
      Spec.map (CommRingCat.ofHom e.toRingHom) ≫
          Spec.map (CommRingCat.ofHom (algebraMap Λ A)) ≫ iΛ =
        Spec.map (CommRingCat.ofHom (algebraMap Λ' (MvPowerSeries (Fin r) A'))) ≫ iΛ' ∧
      ∀ P, formalBranchMultiplicity D iΛ hiΛ x₀ hx₀ hfinite A hA
          (formalBranchesEquivOfRingEquiv D iΛ hiΛ iΛ' hiΛ' x₀ hx₀ hx₀' hfinite hfinite' A A'
            hA hA' e P).2 =
        formalBranchMultiplicity D iΛ' hiΛ' x₀ hx₀' hfinite' A' hA' P.2) ∨
    (∃ r : ℕ, ∃ e : (A' : Type u) ≃+* MvPowerSeries (Fin r) A,
      Spec.map (CommRingCat.ofHom e.toRingHom) ≫
          Spec.map (CommRingCat.ofHom (algebraMap Λ' A')) ≫ iΛ' =
        Spec.map (CommRingCat.ofHom (algebraMap Λ (MvPowerSeries (Fin r) A))) ≫ iΛ ∧
      ∀ P, formalBranchMultiplicity D iΛ' hiΛ' x₀ hx₀' hfinite' A' hA'
          (formalBranchesEquivOfRingEquiv D iΛ' hiΛ' iΛ hiΛ x₀ hx₀' hx₀ hfinite' hfinite A' A
            hA' hA e P).2 =
        formalBranchMultiplicity D iΛ hiΛ x₀ hx₀ hfinite A hA P.2)
```

**`AlgebraicGeometry.Stack.formalBranchMultiplicity_independent_of_realization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FormalBranchMultiplicityIndependence.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FormalBranchMultiplicityIndependence.lean#L159). The attribute's comment: “the multiplicity is independent of the versal ring, along the comparison A ≅ A'[[t₁,…,t\_r]] compatible with the versal formal objects (0DR1 (1)) identifying the branches”.

> **Stacks 0DRC, along the comparison compatible with the versal formal objects.** Let `ξ`, `ξ'`
> be versal formal objects at `x₀`, over the versal rings `A = ξ.base`, `A' = ξ'.base` and for any
> two presentations of `x₀`, with realizations `y : Spec A ⟶ 𝒳` and `y' : Spec A' ⟶ 𝒳` (the
> morphisms of Stacks 0DR1). After possibly swapping them there is an isomorphism
> `e : A ≅ A'[[t₁, …, t_r]]` over `S` together with a morphism `y ⟶ y'` lying over
> `Spec φ`, `φ : A' → A'[[t]] ≅ A` — the comparison of Stacks 0DR1 part (1) used by the source to
> identify the formal branches read off `A` and `A'` — and along that identification multiplicities
> agree.

```lean
theorem formalBranchMultiplicity_independent_of_realization
    (ξ : Deformation.FormalObject (Deformation.Artin.predeformationCategory iΛ
      (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) x₀ hx₀).projection)
    (hξ : Deformation.IsVersal (Deformation.Artin.predeformationCategory_isPredeformationCategory
      D.B D.hS iΛ D.𝒳.val.val.p x₀ hx₀ D.𝒳.val.property).cofibered ξ)
    (ξ' : Deformation.FormalObject (Deformation.Artin.predeformationCategory iΛ'
      (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) x₀ hx₀').projection)
    (hξ' : Deformation.IsVersal (Deformation.Artin.predeformationCategory_isPredeformationCategory
      D.B D.hS iΛ' D.𝒳.val.val.p x₀ hx₀' D.𝒳.val.property).cofibered ξ')
    {hB : D.B.Contains (Spec (.of ξ.base))} {hB' : D.B.Contains (Spec (.of ξ'.base))}
    {y y' : D.𝒳.val.val.obj}
    {hy : D.𝒳.val.val.p.obj y = Deformation.Artin.baseOver D.B D.S D.hS
      (Deformation.Artin.completeLocalAlgFormalBase iΛ hfinite ξ.base) hB}
    {hy' : D.𝒳.val.val.p.obj y' = Deformation.Artin.baseOver D.B D.S D.hS
      (Deformation.Artin.completeLocalAlgFormalBase iΛ' hfinite' ξ'.base) hB'}
    (Ry : (Deformation.Artin.FormalObject.ofPredeformation D.B D.S D.hS iΛ D.𝒳.val.val.p x₀ hx₀
      hfinite ξ).Realization hB y hy)
    (Ry' : (Deformation.Artin.FormalObject.ofPredeformation D.B D.S D.hS iΛ' D.𝒳.val.val.p x₀
      hx₀' hfinite' ξ').Realization hB' y' hy') :
    (∃ r : ℕ, ∃ e : (ξ.base : Type u) ≃+* MvPowerSeries (Fin r) ξ'.base,
      Spec.map (CommRingCat.ofHom e.toRingHom) ≫
          Spec.map (CommRingCat.ofHom (algebraMap Λ ξ.base)) ≫ iΛ =
        Spec.map (CommRingCat.ofHom (algebraMap Λ' (MvPowerSeries (Fin r) ξ'.base))) ≫ iΛ' ∧
      (∃ m : y ⟶ y', (BigFppfOver.toScheme D.B D.S D.hS).map
          (eqToHom hy.symm ≫ D.𝒳.val.val.p.map m ≫ eqToHom hy') =
        Spec.map (CommRingCat.ofHom (MvPowerSeries.ofRingEquivC e))) ∧
      ∀ P, formalBranchMultiplicity D iΛ hiΛ x₀ hx₀ hfinite ξ.base ⟨ξ, rfl, hξ⟩
          (formalBranchesEquivOfRingEquiv D iΛ hiΛ iΛ' hiΛ' x₀ hx₀ hx₀' hfinite hfinite' ξ.base
            ξ'.base ⟨ξ, rfl, hξ⟩ ⟨ξ', rfl, hξ'⟩ e P).2 =
        formalBranchMultiplicity D iΛ' hiΛ' x₀ hx₀' hfinite' ξ'.base ⟨ξ', rfl, hξ'⟩ P.2) ∨
    (∃ r : ℕ, ∃ e : (ξ'.base : Type u) ≃+* MvPowerSeries (Fin r) ξ.base,
      Spec.map (CommRingCat.ofHom e.toRingHom) ≫
          Spec.map (CommRingCat.ofHom (algebraMap Λ' ξ'.base)) ≫ iΛ' =
        Spec.map (CommRingCat.ofHom (algebraMap Λ (MvPowerSeries (Fin r) ξ.base))) ≫ iΛ ∧
      (∃ m : y' ⟶ y, (BigFppfOver.toScheme D.B D.S D.hS).map
          (eqToHom hy'.symm ≫ D.𝒳.val.val.p.map m ≫ eqToHom hy) =
        Spec.map (CommRingCat.ofHom (MvPowerSeries.ofRingEquivC e))) ∧
      ∀ P, formalBranchMultiplicity D iΛ' hiΛ' x₀ hx₀' hfinite' ξ'.base ⟨ξ', rfl, hξ'⟩
          (formalBranchesEquivOfRingEquiv D iΛ' hiΛ' iΛ hiΛ x₀ hx₀' hx₀ hfinite' hfinite ξ'.base
            ξ.base ⟨ξ', rfl, hξ'⟩ ⟨ξ, rfl, hξ⟩ e P).2 =
        formalBranchMultiplicity D iΛ hiΛ x₀ hx₀ hfinite ξ.base ⟨ξ, rfl, hξ⟩ P.2)
```

**`MvPowerSeries.length_localization_minimalPrimesEquivOfRingEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MvPowerSeries/MinimalPrimesLength.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/MvPowerSeries/MinimalPrimesLength.lean#L166). The attribute's comment: “Spec A[[t₁,…,t\_r]] → Spec A induces a bijection on irreducible components preserving multiplicities, which makes the multiplicity independent of the versal ring”.

> **Multiplicities along `A → A[[t₁, …, t_r]] ≅ B`.** A minimal prime `𝔭` of `A` and the
> corresponding minimal prime `φ(𝔭) B` of `B` have localizations of the same length: the
> irreducible components of `Spec A` and `Spec B` they cut out have the same multiplicity. This is
> the fact the source invokes, with its proof omitted, to make Stacks Definition 0DRC independent of
> the versal ring.

```lean
theorem length_localization_minimalPrimesEquivOfRingEquiv (P : minimalPrimes A) :
    letI : P.1.IsPrime := P.2.1.1
    letI : (minimalPrimesEquivOfRingEquiv e P).1.IsPrime :=
      (minimalPrimesEquivOfRingEquiv e P).2.1.1
    Module.length (Localization.AtPrime (minimalPrimesEquivOfRingEquiv e P).1)
        (Localization.AtPrime (minimalPrimesEquivOfRingEquiv e P).1) =
      Module.length (Localization.AtPrime P.1) (Localization.AtPrime P.1)
```

## Tag 0DRD, a lemma

[Tag 0DRD](https://stacks.math.columbia.edu/tag/0DRD) in the Stacks Project.

**`AlgebraicGeometry.Stack.componentMultiplicity_formalBranchComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FormalBranchMultiplicity.lean, line 299](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FormalBranchMultiplicity.lean#L299).

> **Stacks 0DRD.** Let `𝒳` be an algebraic stack locally of finite type over a locally
> Noetherian scheme `S` (the versal situation, **Stacks 0DQU**) and let `x₀ : Spec k ⟶ 𝒳` be a point
> with `k` a field of finite type over `S` and image `s ∈ S`. If `𝒪_{S,s}` is a G-ring, then the map
> of **Stacks 0DRB**, from the formal branches of `𝒳` through `x₀` (read off the versal ring `A` of a
> versal formal object `ξ` realized by `y` over `Spec A`) to the irreducible components of `|𝒳|`
> through `x₀`, preserves multiplicities: the multiplicity (**Stacks 0DR8**) of the component
> attached to a branch is the multiplicity of the branch (**Stacks 0DRC**).

```lean
theorem componentMultiplicity_formalBranchComponent (D : VersalSituation.{u, w})
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    (iΛ : Spec (.of Λ) ⟶ D.S) (hiΛ : _root_.AlgebraicGeometry.IsOpenImmersion iΛ)
    (x₀ : D.𝒳.val.val.obj)
    (hx₀ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType
        (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (ξ : Deformation.FormalObject (Deformation.Artin.predeformationCategory iΛ
      (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) x₀ hx₀).projection)
    (hξ : Deformation.IsVersal (Deformation.Artin.predeformationCategory_isPredeformationCategory
      D.B D.hS iΛ D.𝒳.val.val.p x₀ hx₀ D.𝒳.val.property).cofibered ξ)
    {hA : D.B.Contains (Spec (.of ξ.base))} {y : D.𝒳.val.val.obj}
    {hy : D.𝒳.val.val.p.obj y = Deformation.Artin.baseOver D.B D.S D.hS
      (Deformation.Artin.completeLocalAlgFormalBase iΛ hfinite ξ.base) hA}
    (Ry : (Deformation.Artin.FormalObject.ofPredeformation D.B D.S D.hS iΛ D.𝒳.val.val.p x₀ hx₀
      hfinite ξ).Realization hA y hy)
    (s : D.S) (hs : (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) (closedPoint k) = s)
    (hG : IsGRing (D.S.presheaf.stalk s))
    (P : formalBranches D iΛ hiΛ x₀ hx₀ hfinite ξ.base ⟨ξ, rfl, hξ⟩) :
    componentMultiplicity.{u, w} D.B D.S D.hS D.𝒳 D.hasLocallyNoetherianAtlas
        (formalBranchComponent D iΛ hiΛ x₀ hx₀ hfinite ξ hξ Ry P).1
        (formalBranchComponent D iΛ hiΛ x₀ hx₀ hfinite ξ hξ Ry P).2.1 =
      ((formalBranchMultiplicity D iΛ hiΛ x₀ hx₀ hfinite ξ.base ⟨ξ, rfl, hξ⟩ P.2).toNat : ℤ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 107.4, Tag 0DR9](https://stacks.math.columbia.edu/tag/0DR9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
