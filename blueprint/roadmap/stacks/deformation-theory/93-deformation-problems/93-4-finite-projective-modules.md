---
declaration: section
origin: cited
lean: Deformation.Examples.FiniteProjectiveModule.Family.projection_isCofiberedInGroupoids, Deformation.Examples.FiniteProjectiveModule.specialFiber, Deformation.Examples.FiniteProjectiveModule.family, Deformation.Examples.FiniteProjectiveModule.deformationCategory, Deformation.Examples.FiniteProjectiveModule.Family.satisfiesRS_projection, Deformation.Examples.FiniteProjectiveModule.isDeformationCategory_deformationCategory, Deformation.Examples.FiniteProjectiveModule.subsingleton_tangentSpace, Deformation.Examples.FiniteProjectiveModule.finiteDimensional_tangentSpace
statement: formalized
proof: formalized
---

# 93.4 Finite projective modules

Section 93.4 of the Stacks Project, [Tag 0DVN](https://stacks.math.columbia.edu/tag/0DVN). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D3I, an example

[Tag 0D3I](https://stacks.math.columbia.edu/tag/0D3I) in the Stacks Project.

**`Deformation.Examples.FiniteProjectiveModule.Family.projection_isCofiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/FiniteProjectiveCofibered.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/FiniteProjectiveCofibered.lean#L232).

> The projection from finite projective modules to their Artinian local base algebras is
> cofibered in groupoids.

```lean
public theorem projection_isCofiberedInGroupoids
    (𝓕 : FiniteProjectiveModule.Family.{u, w, t} (Λ := Λ) (k := k)) :
    letI := 𝓕.category
    IsCofiberedInGroupoids 𝓕.projection
```

**`Deformation.Examples.FiniteProjectiveModule.specialFiber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/FiniteProjectiveModules.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/FiniteProjectiveModules.lean#L158). The attribute's comment: “finite\_projective\_deformation\_category”.

> The pair `(k, V)` consisting of the residue field and a finite-dimensional `k`-vector
> space: the special-fibre object whose deformations are studied.

```lean
public noncomputable def specialFiber (V : Type t) [AddCommGroup V] [Module k V]
    [Module.Finite k V] : FiniteProjectiveModule.{u, w, w, t} (Λ := Λ) (k := k)
```

**`Deformation.Examples.FiniteProjectiveModule.family`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/FiniteProjectiveModules.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/FiniteProjectiveModules.lean#L301). The attribute's comment: “finite\_projective\_deformation\_category”.

> The chosen category of finite projective modules over the algebras of `𝒞_Λ`.

```lean
public noncomputable def family : Family.{u, w, t} (Λ := Λ) (k := k)
```

**`Deformation.Examples.FiniteProjectiveModule.deformationCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/FiniteProjectiveModules.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/FiniteProjectiveModules.lean#L307). The attribute's comment: “finite\_projective\_deformation\_category”.

> Deformations of a finite-dimensional `k`-vector space `V`: the objects of the category of
> finite projective modules lying over the special-fibre object `(k, V)`.

```lean
public abbrev deformationCategory (V : Type t) [AddCommGroup V] [Module k V]
    [Module.Finite k V]
```

## Tag 0DVP, a lemma

[Tag 0DVP](https://stacks.math.columbia.edu/tag/0DVP) in the Stacks Project.

**`Deformation.Examples.FiniteProjectiveModule.Family.satisfiesRS_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/FiniteProjectiveRimSchlessinger.lean, line 618](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/FiniteProjectiveRimSchlessinger.lean#L618). The attribute's comment: “Rim-Schlessinger condition”.

> Finite projective modules over Artinian local algebras satisfy the Rim–Schlessinger
> condition: a cospan whose second base morphism is surjective is covered by the Milnor patch of
> the two modules over the fibre product of the base algebras.

```lean
public theorem Family.satisfiesRS_projection
    (𝓕 : FiniteProjectiveModule.Family.{u, w, t} (Λ := Λ) (k := k)) :
    letI := 𝓕.category
    SatisfiesRS 𝓕.projection
```

**`Deformation.Examples.FiniteProjectiveModule.isDeformationCategory_deformationCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/FiniteProjectiveRimSchlessinger.lean, line 806](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/FiniteProjectiveRimSchlessinger.lean#L806). The attribute's comment: “deformation category”.

> Deformations of a finite-dimensional vector space form a deformation category.

```lean
public theorem isDeformationCategory_deformationCategory
    (V : Type t) [AddCommGroup V] [Module k V] [Module.Finite k V] :
    let 𝓕 : FiniteProjectiveModule.Family.{u, w, t} (Λ := Λ) (k := k) :=
      FiniteProjectiveModule.family (Λ := Λ) (k := k)
    letI := 𝓕.category
    IsDeformationCategory
      (objectsOverFunctor 𝓕.projection
        (FiniteProjectiveModule.specialFiber (Λ := Λ) (k := k) V))
```

## Tag 0DVQ, a lemma

[Tag 0DVQ](https://stacks.math.columbia.edu/tag/0DVQ) in the Stacks Project.

**`Deformation.Examples.FiniteProjectiveModule.subsingleton_tangentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/FiniteProjectiveTangentSpace.lean, line 489](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/FiniteProjectiveTangentSpace.lean#L489). The attribute's comment: “tangent\_space\_zero”.

> The tangent space of the deformation category of a finite-dimensional vector space has at
> most one element: it is the zero vector space.

```lean
public theorem subsingleton_tangentSpace
    (V : Type t) [AddCommGroup V] [Module k V] [Module.Finite k V] :
    let 𝓖 := FiniteProjectiveModule.family.{u, w, t} (Λ := Λ) (k := k)
    letI := 𝓖.category
    let p := objectsOverFunctor 𝓖.projection (specialFiber (Λ := Λ) (k := k) V)
    let 𝓕 := BasedCategory.ofFunctor p
    let hD := isDeformationCategory_deformationCategory (Λ := Λ) V
    let hS2 := Artin.schlessingerConditionS2_isomorphismClasses_of_isDeformationCategory 𝓕 hD
    letI : Fact (IsPredeformationCategory 𝓕.p) := ⟨hD.predeformation⟩
    letI : Fact (SchlessingerConditionS2
      (CategoryOfElements.π (isomorphismClasses 𝓕 hD.predeformation.cofibered))) := ⟨hS2⟩
    let T := artinianTangentSpace Λ k (isomorphismClasses 𝓕 hD.predeformation.cofibered)
    letI : AddCommGroup T := associatedTangentSpaceAddCommGroupUnlifted 𝓕
    letI : Module k T := associatedTangentSpaceModuleUnlifted 𝓕
    Subsingleton T
```

**`Deformation.Examples.FiniteProjectiveModule.finiteDimensional_tangentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/FiniteProjectiveTangentSpace.lean, line 549](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/FiniteProjectiveTangentSpace.lean#L549). The attribute's comment: “tangent\_space\_zero”.

> The tangent space of the deformation category of a finite-dimensional vector space is
> finite-dimensional, being the zero vector space.

```lean
public theorem finiteDimensional_tangentSpace
    (V : Type t) [AddCommGroup V] [Module k V] [Module.Finite k V] :
    let 𝓖 := FiniteProjectiveModule.family.{u, w, t} (Λ := Λ) (k := k)
    letI := 𝓖.category
    let p := objectsOverFunctor 𝓖.projection (specialFiber (Λ := Λ) (k := k) V)
    let 𝓕 := BasedCategory.ofFunctor p
    let hD := isDeformationCategory_deformationCategory (Λ := Λ) V
    let hS2 := Artin.schlessingerConditionS2_isomorphismClasses_of_isDeformationCategory 𝓕 hD
    letI : Fact (IsPredeformationCategory 𝓕.p) := ⟨hD.predeformation⟩
    letI : Fact (SchlessingerConditionS2
      (CategoryOfElements.π (isomorphismClasses 𝓕 hD.predeformation.cofibered))) := ⟨hS2⟩
    let T := artinianTangentSpace Λ k (isomorphismClasses 𝓕 hD.predeformation.cofibered)
    letI : AddCommGroup T := associatedTangentSpaceAddCommGroupUnlifted 𝓕
    letI : Module k T := associatedTangentSpaceModuleUnlifted 𝓕
    FiniteDimensional k T
```

**`Deformation.Examples.FiniteProjectiveModule.infinitesimalAutomorphismsEquivEnd`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/InfinitesimalAutomorphisms/Endomorphisms.lean, line 1043](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/InfinitesimalAutomorphisms/Endomorphisms.lean#L1043). The attribute's comment: “infinitesimal\_automorphisms”.

> Infinitesimal automorphisms of a finite-dimensional vector space are its
> linear endomorphisms, with composition corresponding to addition.

```lean
public noncomputable def infinitesimalAutomorphismsEquivEnd
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (V : Type t) [AddCommGroup V] [Module k V] [Module.Finite k V] :
    let 𝓖 := FiniteProjectiveModule.family.{u, w, t} (Λ := Λ) (k := k)
    letI := 𝓖.category
    let p := objectsOverFunctor 𝓖.projection
      (specialFiber (Λ := Λ) (k := k) V)
    let hD := isDeformationCategory_deformationCategory (Λ := Λ) (k := k) V
    let hp : IsPredeformationCategory p := hD.predeformation
    ∀ {Aε : ArtinianLocalAlgCat.{u, w, w} Λ k}
      {x₀ : p.Fiber (residueFieldObject.{u, w, w} Λ k)}
      {xε : p.Fiber Aε}
      (g : residueFieldObject.{u, w, w} Λ k ⟶ Aε)
      (e : Aε ⟶ residueFieldObject.{u, w, w} Λ k)
      (hpair : IsCanonicalDualNumberPair g e)
      (i : x₀.1 ⟶ xε.1) (hi : p.IsHomLift g i),
      let iε : Aε ≃ₐ[Λ] DualNumber k :=
        Classical.choose (Classical.choose_spec hpair)
      let M := xε.1.left
      let hbase : M.base = Aε := (𝓖.projection_obj xε.1.left).symm.trans xε.2
      let ε : M.base := (eqToHom hbase.symm).hom (iε.symm DualNumber.eps)
      let r := 𝓖.homEquiv M
        (specialFiber (Λ := Λ) (k := k) V) xε.1.hom
      { E : infinitesimalAutomorphismGroup hp g e hpair i hi ≃*
          Multiplicative (Module.End k V) //
        ∀ (γ : infinitesimalAutomorphismGroup hp g e hpair i hi) (m : M.carrier),
          let a := 𝓖.homEquiv M M γ.val.asIso.hom.val.left
          ∃ n : M.carrier,
            r.linear n = (Multiplicative.toAdd (E γ)) (r.linear m) ∧
              a.linear m = m + ε • n }
```

**`Deformation.Examples.FiniteProjectiveModule.exists_infinitesimalAutomorphismsLinearEquivEnd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/InfinitesimalAutomorphisms/Endomorphisms.lean, line 1082](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/InfinitesimalAutomorphisms/Endomorphisms.lean#L1082). The attribute's comment: “infinitesimal\_automorphisms”.

> The infinitesimal automorphism group of the deformations of `V` is the `k`-vector space
> `Module.End k V`, and is in particular finite-dimensional. The `k`-structure is the one of
> Stacks 06JV: its addition is composition of automorphisms, and multiplying by `c` scales the
> infinitesimal coordinate, which on the formula `γ(m) = m + ε·n` reads
> `(c · γ)(m) = m + ε·(cb · n)` for any element `cb` of the base reducing to `c`.

```lean
public theorem exists_infinitesimalAutomorphismsLinearEquivEnd
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (V : Type t) [AddCommGroup V] [Module k V] [Module.Finite k V] :
    let 𝓖 := FiniteProjectiveModule.family.{u, w, t} (Λ := Λ) (k := k)
    letI := 𝓖.category
    let p := objectsOverFunctor 𝓖.projection
      (specialFiber (Λ := Λ) (k := k) V)
    let hD := isDeformationCategory_deformationCategory (Λ := Λ) (k := k) V
    let hp : IsPredeformationCategory p := hD.predeformation
    ∀ {Aε : ArtinianLocalAlgCat.{u, w, w} Λ k}
      {x₀ : p.Fiber (residueFieldObject.{u, w, w} Λ k)}
      {xε : p.Fiber Aε}
      (g : residueFieldObject.{u, w, w} Λ k ⟶ Aε)
      (e : Aε ⟶ residueFieldObject.{u, w, w} Λ k)
      (hpair : IsCanonicalDualNumberPair g e)
      (i : x₀.1 ⟶ xε.1) (hi : p.IsHomLift g i),
      let iε : Aε ≃ₐ[Λ] DualNumber k :=
        Classical.choose (Classical.choose_spec hpair)
      let M := xε.1.left
      let hbase : M.base = Aε := (𝓖.projection_obj xε.1.left).symm.trans xε.2
      let ε : M.base := (eqToHom hbase.symm).hom (iε.symm DualNumber.eps)
      let r := 𝓖.homEquiv M
        (specialFiber (Λ := Λ) (k := k) V) xε.1.hom
      ∃ A : AddCommGroup (infinitesimalAutomorphismGroup hp g e hpair i hi),
        letI := A
        ∃ Mo : Module k (infinitesimalAutomorphismGroup hp g e hpair i hi),
          letI := Mo
          (∀ γ δ : infinitesimalAutomorphismGroup hp g e hpair i hi, γ + δ = γ * δ) ∧
          (∃ E : infinitesimalAutomorphismGroup hp g e hpair i hi ≃ₗ[k] Module.End k V,
            (∀ (γ : infinitesimalAutomorphismGroup hp g e hpair i hi) (m : M.carrier),
              ∃ n : M.carrier, r.linear n = E γ (r.linear m) ∧
                (𝓖.homEquiv M M γ.val.asIso.hom.val.left).linear m = m + ε • n) ∧
            ∀ (c : k) (cb : M.base), r.base.hom cb = c →
              ∀ (γ : infinitesimalAutomorphismGroup hp g e hpair i hi)
                (m n : M.carrier), r.linear n = E γ (r.linear m) →
                (𝓖.homEquiv M M γ.val.asIso.hom.val.left).linear m = m + ε • n →
                (𝓖.homEquiv M M (c • γ).val.asIso.hom.val.left).linear m =
                  m + ε • (cb • n)) ∧
          FiniteDimensional k (infinitesimalAutomorphismGroup hp g e hpair i hi)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 93.4, Tag 0DVN](https://stacks.math.columbia.edu/tag/0DVN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
