---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.formalBranches, AlgebraicGeometry.Stack.formalBranchComponent_surjective_and_canonical, AlgebraicGeometry.Stack.formalBranchMultiplicity, AlgebraicGeometry.Stack.componentMultiplicity_formalBranchComponent
statement: formalized
proof: formalized
---

# 107.4 Formal branches and multiplicities

Section 107.4 of the Stacks Project, [Tag 0DR9](https://stacks.math.columbia.edu/tag/0DR9). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DRA, a definition

[Tag 0DRA](https://stacks.math.columbia.edu/tag/0DRA) in the Stacks Project.

**`AlgebraicGeometry.Stack.formalBranches`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FormalBranches.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FormalBranches.lean#L94). The attribute's comment: “relative to a chosen versal ring”.

> **Stacks 0DRA.** The formal branches of `𝒳` through `x₀`, read off a versal ring `A` to `𝒳`
> at `x₀`: the irreducible components of `Spec A`, each recorded by its generic point, that is, the
> set of minimal primes of `A`.

```lean
def formalBranches
    (_hA : IsVersalRingAt D iΛ hiΛ x₀ hx₀ hfinite A) : Set (Ideal A)
```

## Tag 0DRB, a lemma

[Tag 0DRB](https://stacks.math.columbia.edu/tag/0DRB) in the Stacks Project.

**`AlgebraicGeometry.Stack.formalBranchComponent_surjective_and_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FormalBranchComponents.lean, line 1074](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FormalBranchComponents.lean#L1074).

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

**`AlgebraicGeometry.Stack.formalBranchMultiplicity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FormalBranches.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FormalBranches.lean#L140). The attribute's comment: “relative to a chosen versal ring”.

> **Stacks 0DRC.** The multiplicity of a formal branch of `𝒳` through `x₀`: the multiplicity of
> the corresponding irreducible component of `Spec A`, that is, the length over itself of the local
> ring of `Spec A` at the generic point of that component.

```lean
def formalBranchMultiplicity {p : Ideal A}
    (hp : p ∈ formalBranches D iΛ hiΛ x₀ hx₀ hfinite A hA) : ℕ∞
```

## Tag 0DRD, a lemma

[Tag 0DRD](https://stacks.math.columbia.edu/tag/0DRD) in the Stacks Project.

**`AlgebraicGeometry.Stack.componentMultiplicity_formalBranchComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FormalBranchMultiplicity.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FormalBranchMultiplicity.lean#L299).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
