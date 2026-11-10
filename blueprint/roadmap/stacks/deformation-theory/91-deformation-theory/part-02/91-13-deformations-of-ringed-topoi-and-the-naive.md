---
declaration: section
origin: cited
lean: Deformation.ToposThickening.ArbitrarySiteExtensionProblem.CompatibleFirstOrderThickening, Deformation.ToposThickening.RingedToposExtensionProblem.CompatibleFirstOrderThickening, Deformation.ToposThickening.LiftDiagram.translate_existsUnique, Deformation.ToposThickening.FirstOrderLiftDiagram.derivationEquivDifferentialsHom, Deformation.ToposThickening.FirstOrderLiftDiagram.translateHom_zero, Deformation.ToposThickening.FirstOrderLiftDiagram.translateHom_add, Deformation.ToposThickening.FirstOrderLiftDiagram.existsUnique_translateHom, Deformation.ToposThickening.RingedToposLiftDiagram.obstructionClass_eq_zero_iff
statement: formalized
proof: formalized
---

# 91.13 Deformations of ringed topoi and the naive cotangent complex

Section 91.13 of the Stacks Project, [Tag 08UE](https://stacks.math.columbia.edu/tag/08UE). 11 tags here are carried by 54 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08UF, an equation

[Tag 08UF](https://stacks.math.columbia.edu/tag/08UF) in the Stacks Project.

**`Deformation.ToposThickening.ArbitrarySiteExtensionProblem.CompatibleFirstOrderThickening`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/UniversalFirstOrder/ArbitrarySite.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/UniversalFirstOrder/ArbitrarySite.lean#L167). The attribute's comment: “arbitrary equivalent sites”.

> **Stacks 08UF on arbitrary equivalent sites.** A solution of the extension problem on a given
> thickened source ringed topos `X'`. The displayed diagram of sheaves is pulled back along the
> equivalence underlying `i`, and the invertible 2-morphism records the morphism of thickenings.

```lean
public structure CompatibleFirstOrderThickening
    (S : ArbitrarySiteExtensionProblem X B B')
    (X' : RingedTopos.{v''', u''', w'''})
    [X'.J.HasSheafCompose (forget RingCat.{w'''})]
    [X'.J.HasSheafCompose (forget₂ CommRingCat.{w'''} RingCat.{w'''})]
```

Declarations registered for the tag:

- [`Deformation.ToposThickening.RingedToposExtensionProblem.CompatibleFirstOrderThickening`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ExtensionProblem.lean#L127), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/ToposThickening/UniversalFirstOrder/ArbitrarySite.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/UniversalFirstOrder/ArbitrarySite.lean#L88) (StacksFrontier).

## Tag 08UG, a lemma

[Tag 08UG](https://stacks.math.columbia.edu/tag/08UG) in the Stacks Project.

**`Deformation.ToposThickening.LiftDiagram.translate_existsUnique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/LiftingBetweenThickenings.lean, line 649](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/LiftingBetweenThickenings.lean#L649). The attribute's comment: “clause (2): the lifts are a principal homogeneous space under Derivation”.

> **Stacks Project, Tag 08UG**, clause (2). The morphisms
> `(Sh(C'₂), O'₂) ⟶ (Sh(C'₁), O'₁)` fitting into the source's diagram compatibly with `ν` form a
> principal homogeneous space: any one of them is carried to any other by exactly one derivation
> of the diagram. Together with `translate_zero` and `translate_add` this is the free and
> transitive action of the source's clause (2), with the acting group written as the group of
> section-wise derivations out of `O'₁` rather than as
> `Hom_{O₁}(Ω_{O₁/O_{B₁}}, g_*G₂)`.

```lean
public theorem translate_existsUnique (p q : Lift D) :
    ∃! δ : Derivation D.toSituation, translate p δ = q
```

**`Deformation.ToposThickening.FirstOrderLiftDiagram.derivationEquivDifferentialsHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/LiftingDerivationGroup.lean, line 510](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/LiftingDerivationGroup.lean#L510). The attribute's comment: “clause (2): the identification of the acting group of `FirstOrderLiftDiagram.existsUnique_translateHom` with the first group of the source's display, Hom\_\{O\_1}(Omega\_\{O\_1/O\_\{B\_1}}, g\_* G\_2). Nothing assumed”.

> The derivations of the diagram, under which the lifts form a principal homogeneous space by
> `Deformation.ToposThickening.FirstOrderLiftDiagram.existsUnique_translateHom`, are the
> homomorphisms `Hom_{𝒪₁}(Ω_{𝒪₁/𝒪_{ℬ₁}}, g_*𝒢₂)`.

```lean
public noncomputable def derivationEquivDifferentialsHom :
    Derivation D.toSituation ≃+ (frontDifferentials D ⟶ pushedIdeal D)
```

**`Deformation.ToposThickening.FirstOrderLiftDiagram.translateHom_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/LiftingDerivationGroup.lean, line 530](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/LiftingDerivationGroup.lean#L530). The attribute's comment: “clause (2): triviality of the action of 0 in the principal homogeneous space structure under Hom\_\{O\_1}(Omega\_\{O\_1/O\_\{B\_1}}, g\_* G\_2)”.

> The zero homomorphism acts trivially on the lifts of the diagram.

```lean
public theorem translateHom_zero (p : D.Lift) : translateHom D p 0 = p
```

**`Deformation.ToposThickening.FirstOrderLiftDiagram.translateHom_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/LiftingDerivationGroup.lean, line 536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/LiftingDerivationGroup.lean#L536). The attribute's comment: “clause (2): additivity of the action in the principal homogeneous space structure under Hom\_\{O\_1}(Omega\_\{O\_1/O\_\{B\_1}}, g\_* G\_2)”.

> Translation of the lifts of the diagram is additive in the translating homomorphism.

```lean
public theorem translateHom_add (p : D.Lift) (a b : frontDifferentials D ⟶ pushedIdeal D) :
    translateHom D (translateHom D p a) b = translateHom D p (a + b)
```

**`Deformation.ToposThickening.FirstOrderLiftDiagram.existsUnique_translateHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/LiftingDerivationGroup.lean, line 547](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/LiftingDerivationGroup.lean#L547). The attribute's comment: “clause (2) in full, with nothing assumed: the morphisms fitting into the source's diagram compatibly with nu are a principal homogeneous space under the source's own acting group Hom\_\{O\_1}(Omega\_\{O\_1/O\_\{B\_1}}, g\_* G\_2), the underlying topoi identified as in the source's own reduction”.

> The morphisms `(Sh(𝒞'₂), 𝒪'₂) ⟶ (Sh(𝒞'₁), 𝒪'₁)` fitting into the diagram compatibly with `ν`
> form a principal homogeneous space under `Hom_{𝒪₁}(Ω_{𝒪₁/𝒪_{ℬ₁}}, g_*𝒢₂)`: any one of them is
> carried to any other by exactly one homomorphism.

```lean
public theorem existsUnique_translateHom (p q : D.Lift) :
    ∃! a : frontDifferentials D ⟶ pushedIdeal D, translateHom D p a = q
```

**`Deformation.ToposThickening.RingedToposLiftDiagram.obstructionClass_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/RingedToposLiftDiagramObstruction.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/RingedToposLiftDiagramObstruction.lean#L114). The attribute's comment: “clause (1) for genuine morphisms of ringed topoi between four arbitrary ringed topoi: the canonical class in Ext^1\_\{O\_2}(Lg^*NL\_\{O\_1/O\_\{B\_1}}, G\_2), Lg^* the derived pullback of 06YY, is zero exactly when a morphism (Sh(C'\_2), O'\_2) -> (Sh(C'\_1), O'\_1) fitting into (08UH) compatibly with nu exists”.

> **Stacks Project, Tag 08UG, clause (1).** For the diagram (08UH) of ringed topoi, whose
> horizontal arrows are first order thickenings, and a `g⁻¹𝒪₁`-linear map `ν : g⁻¹𝒢₁ ⟶ 𝒢₂` making
> (08UI) commute with front and back rows solutions of (08UF), the canonical element
> `obstructionClass D` of `Ext¹_{𝒪₂}(Lg^*NL_{𝒪₁/𝒪_{ℬ₁}}, 𝒢₂)` vanishes if and only if there is a
> morphism of ringed topoi `(Sh(𝒞'₂), 𝒪'₂) ⟶ (Sh(𝒞'₁), 𝒪'₁)` fitting into (08UH) compatibly
> with `ν`.

```lean
theorem obstructionClass_eq_zero_iff :
    obstructionClass D = 0 ↔ Nonempty (CompatibleLift D)
```

**`Deformation.ToposThickening.RingedToposLiftDiagram.pullbackDifferentialsHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/RingedToposLiftDiagramTorsor.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/RingedToposLiftDiagramTorsor.lean#L120). The attribute's comment: “clause (2), the first equality of the display: Hom\_\{O\_1}(Omega\_\{O\_1/O\_\{B\_1}}, g\_* G\_2) = Hom\_\{O\_2}(g^* Omega\_\{O\_1/O\_\{B\_1}}, G\_2), as an additive equivalence, for genuine morphisms of ringed topoi”.

> **The first equality of the display of Stacks 08UG, clause (2)**:
> `Hom_{𝒪₁}(Ω_{𝒪₁/𝒪_{ℬ₁}}, g_*𝒢₂) = Hom_{𝒪₂}(g^*Ω_{𝒪₁/𝒪_{ℬ₁}}, 𝒢₂)`, the adjunction `g^* ⊣ g_*` of
> sheaves of modules of Stacks 03D7.

```lean
def pullbackDifferentialsHomEquiv :
    (D.g.toRingedToposModulesHom.pullbackModules.obj (differentials₁ D) ⟶
      (show SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X₂.O) from D.S₂.G)) ≃+
      (differentials₁ D ⟶ pushedIdeal₁ D)
```

**`Deformation.ToposThickening.RingedToposLiftDiagram.extZeroEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/RingedToposLiftDiagramTorsor.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/RingedToposLiftDiagramTorsor.lean#L140). The attribute's comment: “clause (2), the second equality of the display: Ext^0\_\{O\_2}(Lg^* NL\_\{O\_1/O\_\{B\_1}}, G\_2) = Hom\_\{O\_1}(Omega\_\{O\_1/O\_\{B\_1}}, g\_* G\_2), as an additive equivalence, for genuine morphisms of ringed topoi”.

> **The second equality of the display of Stacks 08UG, clause (2)**:
> `Hom_{𝒪₁}(Ω_{𝒪₁/𝒪_{ℬ₁}}, g_*𝒢₂) = Ext⁰_{𝒪₂}(Lg^*NL_{𝒪₁/𝒪_{ℬ₁}}, 𝒢₂)`, as an additive
> equivalence: Stacks 0GQ8 in degree `0`, `Ext⁰(NL, 𝒢) = Hom(Ω, 𝒢)` on `𝒞₂`, and the identification
> `actingGroupEquiv`. `Lg^*` is the derived pullback of Tag 06YY, at the model
> `HasDerivedCategory.standard` at which it is constructed.

```lean
def extZeroEquiv :
    @DerivedCategory.Ext _ _ _ (HasDerivedCategory.standard _)
      ((Stacks.Cohomology.DerivedPullbackOfToposHom.derivedPullback D.g).obj
        ((@DerivedCategory.Q _ _ _ (HasDerivedCategory.standard _)).obj
          (Stacks.SheafOfModules.naiveCotangentComplex.{u, u, u, u} X₁.J
            ((inverseImageCommRingFunctor D.S₁.f.toToposHom).obj B₁.O) X₁.O
            D.S₁.f.fSharpInverseImage)))
      ((@DerivedCategory.singleFunctor _ _ _ (HasDerivedCategory.standard _) 0).obj D.S₂.G) 0 ≃+
      (differentials₁ D ⟶ pushedIdeal₁ D)
```

**`Deformation.ToposThickening.RingedToposLiftDiagram.translate_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/RingedToposLiftDiagramTorsor.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/RingedToposLiftDiagramTorsor.lean#L163). The attribute's comment: “clause (2), for genuine morphisms of ringed topoi: triviality of the action of 0 in the principal homogeneous space structure under Hom\_\{O\_1}(Omega\_\{O\_1/O\_\{B\_1}}, g\_* G\_2)”.

> **Stacks Project, Tag 08UG**, clause (2): the zero homomorphism acts trivially.

```lean
theorem translate_zero (p : CompatibleLift D) : translate D p 0 = p
```

**`Deformation.ToposThickening.RingedToposLiftDiagram.translate_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/RingedToposLiftDiagramTorsor.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/RingedToposLiftDiagramTorsor.lean#L170). The attribute's comment: “clause (2), for genuine morphisms of ringed topoi: additivity of the action in the principal homogeneous space structure under Hom\_\{O\_1}(Omega\_\{O\_1/O\_\{B\_1}}, g\_* G\_2)”.

> **Stacks Project, Tag 08UG**, clause (2): the action is additive.

```lean
theorem translate_add (p : CompatibleLift D) (a b : differentials₁ D ⟶ pushedIdeal₁ D) :
    translate D (translate D p a) b = translate D p (a + b)
```

**`Deformation.ToposThickening.RingedToposLiftDiagram.existsUnique_translate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/RingedToposLiftDiagramTorsor.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/RingedToposLiftDiagramTorsor.lean#L182). The attribute's comment: “clause (2) for genuine morphisms of ringed topoi between four arbitrary ringed topoi: the morphisms fitting into (08UH) compatibly with nu are a principal homogeneous space under Hom\_\{O\_1}(Omega\_\{O\_1/O\_\{B\_1}}, g\_* G\_2), with the action translate\_zero, translate\_add”.

> **Stacks Project, Tag 08UG**, clause (2). If there is a morphism of ringed topoi
> `(Sh(𝒞'₂), 𝒪'₂) ⟶ (Sh(𝒞'₁), 𝒪'₁)` fitting into (08UH) compatibly with `ν`, the set of all such
> morphisms is a principal homogeneous space under `Hom_{𝒪₁}(Ω_{𝒪₁/𝒪_{ℬ₁}}, g_*𝒢₂)`: any one of
> them is carried to any other by exactly one homomorphism.

```lean
theorem existsUnique_translate (p q : CompatibleLift D) :
    ∃! a : differentials₁ D ⟶ pushedIdeal₁ D, translate D p a = q
```

## Tag 08UH, an equation

[Tag 08UH](https://stacks.math.columbia.edu/tag/08UH) in the Stacks Project.

**`Deformation.ToposThickening.LiftDiagram`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/LiftingBetweenThickenings.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/LiftingBetweenThickenings.lean#L269). The attribute's comment: “the displayed commutative diagram of morphisms of ringed topoi, with the underlying topoi identified as in the source's convention and its own reduction”.

> **Stacks Project, Tag 08UH and Tag 08UI.** The displayed commutative diagram of morphisms of
> ringed topoi of [Stacks Project, Tag 08UG] together with its diagram of exact ideal rows: two
> layers, the comparison morphisms `g`, `gB`, `gB'` running from the index `1` layer to the index
> `2` layer (the direction of `g^{-1}` in the source, the underlying topoi being identified), and
> the comparison `ν` of the two ideal modules. The comparison of the two *thickened* sources is
> absent: producing it is the lifting problem of Tag 08UG.

```lean
public structure LiftDiagram
```

**`Deformation.ToposThickening.RingedToposLiftDiagram`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/RingedToposLiftDiagram.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/RingedToposLiftDiagram.lean#L260). The attribute's comment: “the commutative diagram of morphisms of ringed topoi, for genuine morphisms f₁, f₂, g, h between four arbitrary ringed topoi, each thickening presented on the site of its reduction as in the source's convention”.

> **The diagram of first order thickenings of ringed topoi and the diagram (08UI) of their
> ideals**, for genuine morphisms of ringed topoi.
>
> * `S₁`, `Q₁` are the front layer: the morphism `f₁ : (Sh(𝒞₁), 𝒪₁) ⟶ (Sh(ℬ₁), 𝒪_{ℬ₁})`, the first
>   order thickening `t₁` of the base, with `f₁⁻¹𝒥₁`, the ideal `𝒢₁` of `i₁`, and the front row of
>   (08UI), which is a solution of (08UF) — the thickening `𝒪'₁ ⟶ 𝒪₁` with its ideal `𝒢₁` and the
>   structure map `f₁⁻¹𝒪_{ℬ'₁} ⟶ 𝒪'₁` of `f'₁`.
> * `S₂`, `Q₂` are the back layer, the same data with index `2`.
> * `g : (Sh(𝒞₂), 𝒪₂) ⟶ (Sh(𝒞₁), 𝒪₁)` and `h : (Sh(ℬ₂), 𝒪_{ℬ₂}) ⟶ (Sh(ℬ₁), 𝒪_{ℬ₁})` are the two
>   oblique arrows of the reduced part, with `f₁ ∘ g = h ∘ f₂`.
> * `hB'` is the oblique arrow `h' : (Sh(ℬ'₂), 𝒪_{ℬ'₂}) ⟶ (Sh(ℬ'₁), 𝒪_{ℬ'₁})` of the thickened
>   bases; the underlying topoi being identified it induces `h` on the topoi, and it is recorded by
>   its comorphism `h⁻¹𝒪_{ℬ'₁} ⟶ 𝒪_{ℬ'₂}`. `hB'_reduction` is `t₁ ∘ h = h' ∘ t₂`.
> * `nu` is `ν : g⁻¹𝒢₁ ⟶ 𝒢₂`, linear over `g⁻¹𝒪₁`, and `nu_base` the commutativity of the left
>   square of (08UI); see the module docstring.
>
> The faces `f'ⱼ ∘ iⱼ = tⱼ ∘ fⱼ` of (08UH) are part of the solutions `Qⱼ`.

```lean
structure RingedToposLiftDiagram
```

## Tag 08UI, an equation

[Tag 08UI](https://stacks.math.columbia.edu/tag/08UI) in the Stacks Project.

**`Deformation.ToposThickening.LiftDiagram`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/LiftingBetweenThickenings.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/LiftingBetweenThickenings.lean#L269). The attribute's comment: “the displayed diagram of exact ideal rows: the two exact rows of each layer are the ideal sequences of its two first order thickenings, and the comparison ν of the two upper ideals is `nu`, compatible by `nu_base` with the two maps from the base ideals”.

> **Stacks Project, Tag 08UH and Tag 08UI.** The displayed commutative diagram of morphisms of
> ringed topoi of [Stacks Project, Tag 08UG] together with its diagram of exact ideal rows: two
> layers, the comparison morphisms `g`, `gB`, `gB'` running from the index `1` layer to the index
> `2` layer (the direction of `g^{-1}` in the source, the underlying topoi being identified), and
> the comparison `ν` of the two ideal modules. The comparison of the two *thickened* sources is
> absent: producing it is the lifting problem of Tag 08UG.

```lean
public structure LiftDiagram
```

## Tag 08UJ, a lemma

[Tag 08UJ](https://stacks.math.columbia.edu/tag/08UJ) in the Stacks Project.

**`Stacks.SheafOfModules.exists_presentation_conormalExtClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangentExtClass.lean, line 899](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangentExtClass.lean#L899).

> Let `A ⟶ B` be a homomorphism of sheaves of rings on a site, let `G` be a `B`-module and let
> `ξ` be a first Ext class of the naive cotangent complex `NL_{B/A}` with values in `G`. Then there
> is a map of sheaves of sets `α : E ⟶ B` presenting `B` over `A` for which `ξ`, viewed in
> `Ext¹_B(NL(α), G)` along the canonical comparison map, is the class of a homomorphism `I/I² ⟶ G`
> out of the conormal sheaf of the presentation.

```lean
theorem exists_presentation_conormalExtClass
    (ξ : DerivedCategory.Ext (DerivedCategory.Q.obj
        (naiveCotangentComplex.{v, u, max w u v, w} J A B a))
      ((DerivedCategory.singleFunctor _ 0).obj G) 1) :
    ∃ (E : Sheaf J (Type (max w u v))) (α : E.obj ⟶ underlyingPresheaf J B)
      (hsurj : Presheaf.IsLocallySurjective J (presentation J A B a E.obj α).hom),
      letI : Presheaf.IsLocallySurjective J (presentation J A B a E.obj α).hom := hsurj
      ∃ f : (presentationConormalSequence.{v, u, max w u v, w} J A B a E.obj α).X₁ ⟶ G,
        DerivedCategory.Q.map
            (naiveCotangentComplexComparison.{v, u, max w u v, w} J A B a E.obj α) ≫ ξ =
          presentationConormalExtClass.{v, u, w, t} J A B a E.obj α G f
```

## Tag 08UK, a lemma

[Tag 08UK](https://stacks.math.columbia.edu/tag/08UK) in the Stacks Project.

**`Deformation.ToposThickening.RingedToposExtensionProblem.exists_addTorsor_isomorphismClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SolutionClassesNaiveExtTorsor.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/SolutionClassesNaiveExtTorsor.lean#L91).

> **Stacks Project, Tag 08UK.** For the square-zero extension problem of [Stacks 08UF] — a
> first order thickening of `(Sh(ℬ), 𝒪_ℬ)` with ideal `𝒥`, a morphism of ringed topoi
> `f : (Sh(𝒞), 𝒪) ⟶ (Sh(ℬ), 𝒪_ℬ)`, an `𝒪`-module `𝒢` and `c : f⁻¹𝒥 ⟶ 𝒢` — if a solution exists,
> then the set of isomorphism classes of solutions is principal homogeneous under
> `Ext¹_𝒪(NL_{𝒪/𝒪_ℬ}, 𝒢)`.
>
> The structure is the source's: `ξ` carries the class of a solution `𝒪'` to the class of the
> pushout solution `𝒪'_ξ` of the proof, and it carries the class of `𝒪'₁` to the class of `𝒪'₂`
> exactly when the obstruction class `o(𝒪'₁, 𝒪'₂)` of [Stacks 08UG] is `ξ`.

```lean
theorem exists_addTorsor_isomorphismClasses (S : RingedToposExtensionProblem X B)
    (hne : Nonempty S.CompatibleFirstOrderThickening) :
    ∃ T : AddTorsor
        (Stacks.SheafOfModules.naiveCotangentExt.{u, u, u, u, t} X.J
          ((inverseImageCommRingFunctor S.f.toToposHom).obj B.O) X.O S.f.fSharpInverseImage S.G 1)
        (IsomorphismClasses S),
      (∀ (ξ : Stacks.SheafOfModules.naiveCotangentExt.{u, u, u, u, t} X.J
          ((inverseImageCommRingFunctor S.f.toToposHom).obj B.O) X.O S.f.fSharpInverseImage S.G 1)
          (P Q : S.CompatibleFirstOrderThickening),
        T.vadd ξ (Quotient.mk (isomorphicSetoid S) P) = Quotient.mk (isomorphicSetoid S) Q ↔
          pairObstruction P Q = ξ) ∧
      ∀ (ξ : Stacks.SheafOfModules.naiveCotangentExt.{u, u, u, u, t} X.J
          ((inverseImageCommRingFunctor S.f.toToposHom).obj B.O) X.O S.f.fSharpInverseImage S.G 1)
          (P : S.CompatibleFirstOrderThickening),
        T.vadd ξ (Quotient.mk (isomorphicSetoid S) P) =
          Quotient.mk (isomorphicSetoid S) (P.twist ξ)
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.isomorphic_iff_nonempty_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SolutionIsomorphism.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/SolutionIsomorphism.lean#L336). The attribute's comment: “the half asserting that the obstruction class of Stacks 08UG separates the isomorphism classes of solutions, namely that a morphism of solutions of the extension problem of Stacks 08UF is automatically an isomorphism; not the torsor half, which needs the pair-dependent presentation of the source's last paragraph and its omitted calculation”.

> **Stacks Project, Tag 08UK**, the half asserting that the obstruction class separates the
> isomorphism classes of solutions. Two solutions of the square-zero extension problem of
> [Stacks Project, Tag 08UF] are isomorphic exactly when there is a *morphism* of solutions
> between them: by `CompatibleFirstOrderThickening.Hom.isIso` every morphism of solutions is
> already invertible.
>
> This is the source's "clearly, this element is the obstruction to the existence of an
> isomorphism, hence separates the isomorphism classes" — the obstruction class of
> [Stacks Project, Tag 08UG], which obstructs a morphism `O'₁ ⟶ O'₂` fitting into the diagram
> (`Deformation.ToposThickening.LiftDiagram.liftingObstruction_eq_zero_iff`), thereby obstructs an
> isomorphism of solutions.
>
> The other half of the tag — that the isomorphism classes form a principal homogeneous space
> under `Ext¹_O(NL_{O/O_B}, G)` — is **not** claimed here; see the implementation notes of this
> file.

```lean
public theorem isomorphic_iff_nonempty_hom (P Q : S.CompatibleFirstOrderThickening) :
    CompatibleFirstOrderThickening.Isomorphic P Q ↔
      Nonempty (CompatibleFirstOrderThickening.Hom P Q)
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.isomorphismClasses_mk_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SolutionIsomorphism.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/SolutionIsomorphism.lean#L354). The attribute's comment: “the half asserting that the obstruction class of Stacks 08UG separates the isomorphism classes, stated for the quotient `IsomorphismClasses` itself: two solutions have the same isomorphism class exactly when a morphism of solutions joins them; not the torsor half”.

> **Stacks Project, Tag 08UK**, the half asserting that the obstruction class separates the
> isomorphism classes, stated for the set of isomorphism classes itself. Two solutions of the
> square-zero extension problem of [Stacks Project, Tag 08UF] have the same class in
> `CompatibleFirstOrderThickening.IsomorphismClasses S` exactly when there is a morphism of
> solutions between them, so the obstruction class of [Stacks Project, Tag 08UG] — which
> obstructs such a morphism — is a complete invariant of the isomorphism class.
>
> That these classes are moreover *principal homogeneous* under
> `Ext¹_O(NL_{O/O_B}, G)` is **not** claimed; see the implementation notes of this file.

```lean
public theorem isomorphismClasses_mk_eq_iff (P Q : S.CompatibleFirstOrderThickening) :
    (Quotient.mk (CompatibleFirstOrderThickening.isomorphicSetoid S) P :
        CompatibleFirstOrderThickening.IsomorphismClasses S) =
      Quotient.mk (CompatibleFirstOrderThickening.isomorphicSetoid S) Q ↔
      Nonempty (CompatibleFirstOrderThickening.Hom P Q)
```

**`Deformation.ToposThickening.LiftDiagram.liftingObstruction_eq_zero_iff_exists_isIso_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SolutionIsomorphism.lean, line 463](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/SolutionIsomorphism.lean#L463). The attribute's comment: “the half asserting that the obstruction class of Stacks 08UG separates the isomorphism classes, stated in the vocabulary of the diagram of that tag: when the two comparison maps of the diagram are bijective on sections the class vanishes exactly when an isomorphism fits into the diagram; the hypotheses carried are those of Stacks 08UG itself, and the torsor half of 08UK is not claimed”.

> **Stacks Project, Tag 08UK**, the half asserting that the obstruction class separates the
> isomorphism classes, in the vocabulary of the diagram of [Stacks Project, Tag 08UG]. When the
> two comparison maps of the diagram are bijective on sections — as they are for two solutions of
> one square-zero extension problem, where both are identities — the class of Step 1 of the proof
> of Tag 08UG vanishes if and only if there is an *isomorphism* `O'₁ ≅ O'₂` fitting into the
> diagram, and not merely a morphism.
>
> This is the source's "clearly, this element is the obstruction to the existence of an
> isomorphism, hence separates the isomorphism classes", combined with the vanishing criterion
> `Deformation.ToposThickening.LiftDiagram.liftingObstruction_eq_zero_iff` of Tag 08UG, whose
> hypotheses `P` and `ξ` are inherited verbatim. That criterion is stated for the factorizations
> of `ξ` through the degree `0` term and assumes nothing; the bijection `e` of Steps 1 to 3 of the
> source's proof, which identifies those factorizations with the lifts of the diagram, is carried
> here.

```lean
public theorem liftingObstruction_eq_zero_iff_exists_isIso_lift (D : LiftDiagram J)
    {single : M ⥤ T} [single.Full] [single.Faithful] [single.Additive]
    (hg : ∀ U : Cᵒᵖ, Function.Bijective (D.g.hom.app U))
    (hgs : Presheaf.IsLocallySurjective J D.g.hom)
    (hnu : ∀ U : Cᵒᵖ, Function.Bijective (D.nuSection (U := U)))
    (P : NaiveCotangentTwoTerm single) (G : M) (ξ : P.conormal ⟶ G)
    (e : D.Lift ≃ {θ : P.base ⟶ G // P.d ≫ θ = ξ}) :
    liftingObstruction P G ξ = 0 ↔ ∃ p : D.Lift, IsIso p.hom
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.CompatibleFirstOrderThickening.naiveIsomorphismClassesAddTorsor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SolutionIsomorphismClassesExt.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/SolutionIsomorphismClassesExt.lean#L86). The attribute's comment: “the half asserting that, if a solution exists, the set of isomorphism classes of solutions is principal homogeneous under Ext¹(NL\_f, G); the element separating two classes is their obstruction class”.

> **Stacks 08UK**, the torsor half: if the square-zero extension problem has a solution, the
> isomorphism classes of solutions are a principal homogeneous space under `Ext¹_O(NL_f, G)`.

```lean
noncomputable def naiveIsomorphismClassesAddTorsor [Nonempty S.CompatibleFirstOrderThickening] :
    AddTorsor (S.f.naiveCotangentExt (targetG S) 1) (IsomorphismClasses S)
```

## Tag 0GQ5, a lemma

[Tag 0GQ5](https://stacks.math.columbia.edu/tag/0GQ5) in the Stacks Project.

**`Deformation.ToposThickening.RingedToposExtensionProblem.classesEquivExt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SquareZeroExtensionClasses.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/SquareZeroExtensionClasses.lean#L152). The attribute's comment: “the bijection between isomorphism classes of square-zero extensions of 𝒪 by 𝒢 as f⁻¹𝒪\_ℬ-algebras and Ext¹ of a FIXED presentation α, carrying the four inputs of SolutionObstruction (xi, hxi, rep, pushout) and the lift bijection e of 08UG; identifying Ext¹(NL(α), 𝒢) with Ext¹(NL\_\{𝒪/𝒪\_ℬ}, 𝒢) is 08TY and 08TL, absent on a general site”.

> The isomorphism classes of square-zero extensions `0 ⟶ 𝒢 ⟶ 𝒪' ⟶ 𝒪 ⟶ 0` of `f⁻¹𝒪_ℬ`-algebras —
> equivalently, of first order thickenings over the base with an `𝒪`-module isomorphism
> `𝒢 ≅ Ker(i^♯)`, i.e. of solutions of the problem of [Stacks 08UF] whose base reduction is
> invertible — are in bijection with `Ext¹(NL(α), 𝒢)`.
>
> The bijection is the torsor of [Stacks 08UK] evaluated at the base point supplied by the trivial
> extension `𝒪 ⋉ 𝒢`: a class `q` goes to the obstruction class separating it from the class of
> `𝒪 ⋉ 𝒢`, and a class `ξ` of `Ext¹` goes to the class of the solution obtained from `𝒪 ⋉ 𝒢` by
> twisting with `ξ`. The five inputs — the four of
> `AlgebraicGeometry.RingedSpaceThickening.SolutionObstruction` and the lift bijection `e` of
> [Stacks 08UG] — remain hypotheses; see the implementation notes of this file.

```lean
def classesEquivExt (h : IsIso S.baseReduction) (P : NaiveCotangentTwoTerm single)
    (xi : S.CompatibleFirstOrderThickening → S.CompatibleFirstOrderThickening →
      (P.conormal ⟶ S.G))
    (hxi : ∀ Q₁ Q₂ Q₃ : S.CompatibleFirstOrderThickening,
      xi Q₁ Q₂ + xi Q₂ Q₃ = xi Q₁ Q₃)
    (rep : ∀ ξ : P.obj ⟶ (single.obj S.G)⟦(1 : ℤ)⟧,
      { δ : P.conormal ⟶ S.G // liftingObstruction P S.G δ = ξ })
    (pushout : ∀ (Q : S.CompatibleFirstOrderThickening) (δ : P.conormal ⟶ S.G),
      { Q' : S.CompatibleFirstOrderThickening // xi Q Q' = δ })
    (e : ∀ Q₁ Q₂ : S.CompatibleFirstOrderThickening,
      CompatibleFirstOrderThickening.Hom Q₁ Q₂ ≃
        { θ : P.base ⟶ S.G // P.d ≫ θ = xi Q₁ Q₂ }) :
    CompatibleFirstOrderThickening.IsomorphismClasses S ≃
      (P.obj ⟶ (single.obj S.G)⟦(1 : ℤ)⟧)
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.classesEquivExt_trivialSolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SquareZeroExtensionClasses.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/SquareZeroExtensionClasses.lean#L175). The attribute's comment: “that the bijection is canonical: the class of the trivial extension 𝒪 ⋉ 𝒢 goes to 0; the hypotheses carried are those of the bijection itself”.

> **The bijection `classesEquivExt` is the canonical one.** It carries the isomorphism class of
> the trivial square-zero extension `𝒪 ⋉ 𝒢` to `0`.

```lean
theorem classesEquivExt_trivialSolution (h : IsIso S.baseReduction)
    (P : NaiveCotangentTwoTerm single)
    (xi : S.CompatibleFirstOrderThickening → S.CompatibleFirstOrderThickening →
      (P.conormal ⟶ S.G))
    (hxi : ∀ Q₁ Q₂ Q₃ : S.CompatibleFirstOrderThickening,
      xi Q₁ Q₂ + xi Q₂ Q₃ = xi Q₁ Q₃)
    (rep : ∀ ξ : P.obj ⟶ (single.obj S.G)⟦(1 : ℤ)⟧,
      { δ : P.conormal ⟶ S.G // liftingObstruction P S.G δ = ξ })
    (pushout : ∀ (Q : S.CompatibleFirstOrderThickening) (δ : P.conormal ⟶ S.G),
      { Q' : S.CompatibleFirstOrderThickening // xi Q Q' = δ })
    (e : ∀ Q₁ Q₂ : S.CompatibleFirstOrderThickening,
      CompatibleFirstOrderThickening.Hom Q₁ Q₂ ≃
        { θ : P.base ⟶ S.G // P.d ≫ θ = xi Q₁ Q₂ }) :
    S.classesEquivExt h P xi hxi rep pushout e
        (Quotient.mk (CompatibleFirstOrderThickening.isomorphicSetoid S)
          (S.trivialSolution h)) = 0
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.squareZeroExtensionClassesEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SquareZeroExtensionNaiveExt.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/SquareZeroExtensionNaiveExt.lean#L230).

> **Stacks Project, Tag 0GQ5.** Let `f : (Sh(𝒞), 𝒪) ⟶ (Sh(ℬ), 𝒪_ℬ)` be a morphism of ringed
> topoi and `𝒢` an `𝒪`-module. The set of isomorphism classes of extensions of
> `f⁻¹𝒪_ℬ`-algebras `0 ⟶ 𝒢 ⟶ 𝒪' ⟶ 𝒪 ⟶ 0` with `𝒢` an ideal of square zero — the solutions of the
> problem `ofTrivialBase f 𝒢` — is canonically bijective to `Ext¹_𝒪(NL_{𝒪/𝒪_ℬ}, 𝒢)`.
>
> The bijection is the one of the source's proof: the torsor of [Stacks 08UK] under
> `Ext¹_𝒪(NL_{𝒪/𝒪_ℬ}, 𝒢)` with base point the trivial extension `𝒪 ⊕ 𝒢`. The class of `𝒪'` goes
> to the obstruction class `o(𝒪 ⊕ 𝒢, 𝒪')` (`squareZeroExtensionClassesEquiv_mk`), and `ξ` goes to
> the class of the pushout extension `(𝒪 ⊕ 𝒢)_ξ` (`squareZeroExtensionClassesEquiv_symm_apply`).

```lean
def squareZeroExtensionClassesEquiv :
    CompatibleFirstOrderThickening.IsomorphismClasses (ofTrivialBase f G) ≃
      Stacks.SheafOfModules.naiveCotangentExt.{u, u, u, u, t} X.J
        ((inverseImageCommRingFunctor f.toToposHom).obj B.O) X.O f.fSharpInverseImage G 1
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.squareZeroExtensionClassesEquiv_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SquareZeroExtensionNaiveExt.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/SquareZeroExtensionNaiveExt.lean#L241).

> **The bijection of [Stacks 0GQ5] is the canonical one**: it sends the isomorphism class of
> an extension `𝒪'` to the obstruction class `o(𝒪 ⊕ 𝒢, 𝒪')` of [Stacks 08UG] separating it from
> the trivial extension, that is the element of `Ext¹_𝒪(NL_{𝒪/𝒪_ℬ}, 𝒢)` carrying the class of
> `𝒪 ⊕ 𝒢` to that of `𝒪'` in the torsor of [Stacks 08UK].

```lean
theorem squareZeroExtensionClassesEquiv_mk
    (Q : (ofTrivialBase f G).CompatibleFirstOrderThickening) :
    squareZeroExtensionClassesEquiv f G
        (Quotient.mk (CompatibleFirstOrderThickening.isomorphicSetoid _) Q) =
      CompatibleFirstOrderThickening.pairObstruction
        ((ofTrivialBase f G).trivialSolution (IsIso.id B.O)) Q
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.trivialSolution`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/TrivialSquareZeroSolution.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/TrivialSquareZeroSolution.lean#L259). The attribute's comment: “the existence of a solution: the trivial extension 𝒪 ⋉ 𝒢; not the bijection with Ext¹, which needs the torsor statement of 08UK”. References: EGA 0 (18.2.3), “partial”.

> **The trivial square-zero extension is a solution** of the square-zero extension problem of
> [Stacks 08UF] whose base reduction is invertible: `𝒪' = 𝒪 ⋉ 𝒢`, with the projection as reduction,
> the inclusion `m ↦ (0, m)` as the identification of `𝒢` with the kernel, and the zero section
> composed with the structure map of `f` as the map from the inverse image of the thickened base.
>
> This is the existence of a solution in the proof of [Stacks 0GQ5] — the source's "a solution
> exists, take `𝒢 ⊕ 𝒪`". It is not the bijection with `Ext¹`, which needs the torsor statement of
> [Stacks 08UK]; see
> `StacksFrontier/Deformation/ToposThickening/SquareZeroExtensionClasses.lean`.

```lean
def trivialSolution (h : IsIso S.baseReduction) : S.CompatibleFirstOrderThickening
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.nonempty_compatibleFirstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/TrivialSquareZeroSolution.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/TrivialSquareZeroSolution.lean#L285). The attribute's comment: “the existence of a solution, as the base point the torsor of 08UK needs; not the bijection with Ext¹”.

> **A square-zero extension problem of ringed topoi whose bottom row is
> `0 ⟶ 0 ⟶ f⁻¹𝒪_B ⟶ f⁻¹𝒪_B ⟶ 0` has a solution**, namely the trivial extension `𝒪 ⋉ 𝒢`. This is
> the base point the torsor statement of [Stacks 08UK] needs in order to turn into the bijection of
> [Stacks 0GQ5].

```lean
theorem nonempty_compatibleFirstOrderThickening (h : IsIso S.baseReduction) :
    Nonempty S.CompatibleFirstOrderThickening
```

## Tag 0GQ6, a remark

[Tag 0GQ6](https://stacks.math.columbia.edu/tag/0GQ6) in the Stacks Project.

**`Deformation.ToposThickening.RingedToposExtensionProblem.CompatibleFirstOrderThickening.lift_comp_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ExtensionPresentation.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ExtensionPresentation.lean#L253). The attribute's comment: “the commutative diagram over 𝒪' ⟶ 𝒪 for ℰ underlying 𝒪' with α' the identity”.

> **Stacks Project, Tag 0GQ6**, the commutative diagram: `α'` followed by the reduction
> `𝒪' ⟶ 𝒪` is the presentation attached to `α`.

```lean
theorem lift_comp_reduction (base : inverseImageBaseRing S ⟶ P.extension)
    (hbase : base ≫ P.reduction = S.f.fSharpInverseImage) :
    P.lift base ≫ P.reduction = P.presentation
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.CompatibleFirstOrderThickening.presentation_isLocallySurjective`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ExtensionPresentation.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ExtensionPresentation.lean#L278). The attribute's comment: “surjectivity of f⁻¹𝒪\_ℬ[ℰ] ⟶ 𝒪, which is what makes NL(α) defined”.

> **Stacks Project, Tag 0GQ6**, surjectivity of `f⁻¹𝒪_ℬ[ℰ] ⟶ 𝒪`: the variables of the free
> algebra are all the local sections of `𝒪'`, and they already cover `𝒪` because the reduction
> does.

```lean
instance presentation_isLocallySurjective :
    Presheaf.IsLocallySurjective X.J P.presentation.hom
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.CompatibleFirstOrderThickening.exists_generators`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ExtensionPresentation.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ExtensionPresentation.lean#L294). The attribute's comment: “the choice of ℰ with α' : ℰ ⟶ 𝒪' and α : ℰ ⟶ 𝒪 making f⁻¹𝒪\_ℬ[ℰ] ⟶ 𝒪 surjective”.

> **Stacks Project, Tag 0GQ6**, the choice the source makes is possible: there are a sheaf of
> sets `ℰ` and maps `α' : ℰ ⟶ 𝒪'`, `α : ℰ ⟶ 𝒪` forming a commutative triangle over the reduction
> `𝒪' ⟶ 𝒪` for which `f⁻¹𝒪_ℬ[ℰ] ⟶ 𝒪` is surjective. The witness is the source's own: `ℰ` is the
> sheaf of sets underlying `𝒪'` and `α'` is the identity.

```lean
theorem exists_generators :
    ∃ (E : Functor X.Cᵒᵖ (Type u)) (α' : E ⟶ underlyingPresheaf X.J P.extension)
      (α : E ⟶ underlyingPresheaf X.J X.O),
      α' ≫ Functor.whiskerRight P.reduction.hom (forget CommRingCat.{u}) = α ∧
        Presheaf.IsLocallySurjective X.J
          (Stacks.SheafOfModules.presentation X.J (inverseImageBaseRing S) X.O
            S.f.fSharpInverseImage E α).hom
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.CompatibleFirstOrderThickening.conormalToIdeal`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ExtensionPresentation.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ExtensionPresentation.lean#L360). The attribute's comment: “the map 𝒥/𝒥² ⟶ 𝒢 determined by α'”.

> **Stacks Project, Tag 0GQ6**, the map `𝒥/𝒥² ⟶ 𝒢` determined by `α'`.

```lean
abbrev conormalToIdeal (base : inverseImageBaseRing S ⟶ P.extension)
    (hbase : base ≫ P.reduction = S.f.fSharpInverseImage) :
    conormalSheaf.{u, u, u, u} X.J
        (freeAlgebraSheaf X.J (inverseImageBaseRing S) P.generators) X.O P.presentation ⟶
      S.G
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.CompatibleFirstOrderThickening.extClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ExtensionPresentation.lean, line 403](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ExtensionPresentation.lean#L403). The attribute's comment: “the class in Ext¹\_𝒪(NL(α), 𝒢) that α' determines through the map 𝒥/𝒥² ⟶ 𝒢”.

> **Stacks Project, Tag 0GQ6**, the class in `Ext¹_𝒪(NL(α), 𝒢)` that `α'` determines: the
> first Ext class of the map `𝒥/𝒥² ⟶ 𝒢`.

```lean
def extClass (base : inverseImageBaseRing S ⟶ P.extension)
    (hbase : base ≫ P.reduction = S.f.fSharpInverseImage) :
    DerivedCategory.Ext (DerivedCategory.Q.obj P.naiveCotangentComplex)
      ((DerivedCategory.singleFunctor _ 0).obj S.G) 1
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.isLocallySurjective_presentation_of_isLocallySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ExtensionPresentationRemark.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ExtensionPresentationRemark.lean#L287).

> For any sheaf of sets `ℰ` with a surjection `α' : ℰ ⟶ 𝒪'`, the presentation
> `f⁻¹𝒪_ℬ[ℰ] ⟶ 𝒪` of `α = α'` followed by the reduction is surjective.

```lean
theorem isLocallySurjective_presentation_of_isLocallySurjective
    (Q : (ofTrivialBase f G).CompatibleFirstOrderThickening) (E : Functor X.Cᵒᵖ (Type u))
    (α' : E ⟶ underlyingPresheaf X.J Q.extension) [Presheaf.IsLocallySurjective X.J α'] :
    Presheaf.IsLocallySurjective X.J (Stacks.SheafOfModules.presentation X.J
      ((inverseImageCommRingFunctor f.toToposHom).obj B.O) X.O f.fSharpInverseImage E
        (α' ≫ Functor.whiskerRight Q.reduction.hom (forget CommRingCat.{u}))).hom
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.exists_generators_ofTrivialBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ExtensionPresentationRemark.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ExtensionPresentationRemark.lean#L308).

> For every extension `0 ⟶ 𝒢 ⟶ 𝒪' ⟶ 𝒪 ⟶ 0` of `f⁻¹𝒪_ℬ`-algebras there are a sheaf of sets
> `ℰ` and maps `α' : ℰ ⟶ 𝒪'`, `α : ℰ ⟶ 𝒪` forming a commutative triangle over `𝒪' ⟶ 𝒪` for which
> `f⁻¹𝒪_ℬ[ℰ] ⟶ 𝒪` is surjective; for instance `ℰ` the sheaf of sets underlying `𝒪'` and `α'` the
> identity.

```lean
theorem exists_generators_ofTrivialBase
    (Q : (ofTrivialBase f G).CompatibleFirstOrderThickening) :
    ∃ (E : Functor X.Cᵒᵖ (Type u)) (α' : E ⟶ underlyingPresheaf X.J Q.extension)
      (α : E ⟶ underlyingPresheaf X.J X.O),
      α' ≫ Functor.whiskerRight Q.reduction.hom (forget CommRingCat.{u}) = α ∧
        Presheaf.IsLocallySurjective X.J (Stacks.SheafOfModules.presentation X.J
          ((inverseImageCommRingFunctor f.toToposHom).obj B.O) X.O f.fSharpInverseImage E α).hom
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.squareZeroExtensionClassesEquiv_mk_eq_generators`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ExtensionPresentationRemark.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ExtensionPresentationRemark.lean#L378).

> Let `f : (Sh(𝒞), 𝒪) ⟶ (Sh(ℬ), 𝒪_ℬ)` be a morphism of ringed topoi, `𝒢` an `𝒪`-module and
> `0 ⟶ 𝒢 ⟶ 𝒪' ⟶ 𝒪 ⟶ 0` an extension of `f⁻¹𝒪_ℬ`-algebras with `𝒢` an ideal of square zero. Let
> `ℰ` be a sheaf of sets with a commutative diagram `α' : ℰ ⟶ 𝒪'`, `α : ℰ ⟶ 𝒪` over `𝒪' ⟶ 𝒪` such
> that `f⁻¹𝒪_ℬ[ℰ] ⟶ 𝒪` is surjective with kernel `𝒥`. The map `𝒥/𝒥² ⟶ 𝒢` determined by `α'` has a
> class in `Ext¹_𝒪(NL(α), 𝒢)`; transported along the isomorphism `NL(α) ≅ NL_{𝒪/𝒪_ℬ}` of
> [Stacks 08TY], it is the element of `Ext¹_𝒪(NL_{𝒪/𝒪_ℬ}, 𝒢)` corresponding to `𝒪'` under the
> bijection of [Stacks 0GQ5].

```lean
theorem squareZeroExtensionClassesEquiv_mk_eq_generators
    [HasDerivedCategory.{t} (Sheaf.targetModules.{u, u, u} X.J X.O)] :
    inv (DerivedCategory.Q.map
        (Stacks.SheafOfModules.naiveCotangentComplexComparison.{u, u, u, u} X.J
          ((inverseImageCommRingFunctor f.toToposHom).obj B.O) X.O f.fSharpInverseImage E α)) ≫
      Stacks.SheafOfModules.presentationConormalExtClass.{u, u, u, t} X.J
        ((inverseImageCommRingFunctor f.toToposHom).obj B.O) X.O f.fSharpInverseImage E α G
        (Q.generatorsConormalToIdeal (A := (inverseImageCommRingFunctor f.toToposHom).obj B.O)
          (a := f.fSharpInverseImage) (base := Q.baseMap) hα
        (baseMap_comp_reduction_ofTrivialBase Q)) =
      squareZeroExtensionClassesEquiv f G
        (Quotient.mk (CompatibleFirstOrderThickening.isomorphicSetoid _) Q)
```

## Tag 0GQ7, a lemma

[Tag 0GQ7](https://stacks.math.columbia.edu/tag/0GQ7) in the Stacks Project.

**`Deformation.ToposThickening.LiftingMorphismDerived.nonempty_compatibleMorphism_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/LiftingMorphismDerivedCriterion.lean, line 738](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/LiftingMorphismDerivedCriterion.lean#L738).

> Let `f : (Sh(𝒞), 𝒪_𝒞) ⟶ (Sh(ℬ), 𝒪_ℬ)` and `g : (Sh(𝒟), 𝒪_𝒟) ⟶ (Sh(𝒞), 𝒪_𝒞)` be morphisms of
> ringed topoi, `ℱ` an `𝒪_𝒞`-module, `𝒢` an `𝒪_𝒟`-module and `c : g^*ℱ ⟶ 𝒢` an `𝒪_𝒟`-linear map. Let
> `0 ⟶ ℱ ⟶ 𝒪_{𝒞'} ⟶ 𝒪_𝒞 ⟶ 0` be an extension of `f⁻¹𝒪_ℬ`-algebras (a solution `QC` of the problem of
> Stacks 0GQ5 for `f` and `ℱ`) corresponding to `ξ ∈ Ext¹_{𝒪_𝒞}(NL_{𝒪_𝒞/𝒪_ℬ}, ℱ)`, and
> `0 ⟶ 𝒢 ⟶ 𝒪_{𝒟'} ⟶ 𝒪_𝒟 ⟶ 0` an extension of `g⁻¹f⁻¹𝒪_ℬ`-algebras (a solution `QD` of the problem for
> `f ∘ g` and `𝒢`) corresponding to `ζ ∈ Ext¹_{𝒪_𝒟}(NL_{𝒪_𝒟/𝒪_ℬ}, 𝒢)`, the classes being those of
> Stacks 0GQ5. Then there is a morphism `g' : (Sh(𝒟), 𝒪_{𝒟'}) ⟶ (Sh(𝒞), 𝒪_{𝒞'})` of ringed topoi over
> `(Sh(ℬ), 𝒪_ℬ)` compatible with `g` and `c` if and only if `ξ` and `ζ` map to the same element of
> `Ext¹_{𝒪_𝒟}(Lg^*NL_{𝒪_𝒞/𝒪_ℬ}, 𝒢)`: `ξ` through `Lg^*` and `Lg^*ℱ ⟶ g^*ℱ ⟶ 𝒢` (`pullbackExtClass`),
> `ζ` through the canonical map `Lg^*NL_{𝒪_𝒞/𝒪_ℬ} ⟶ NL_{𝒪_𝒟/𝒪_ℬ}` (`restrictExtClass`).

```lean
theorem nonempty_compatibleMorphism_iff :
    Nonempty (CompatibleMorphism g QC QD c) ↔
      pullbackExtClass g c
          (RingedToposExtensionProblem.squareZeroExtensionClassesEquiv f F
            (Quotient.mk
              (RingedToposExtensionProblem.CompatibleFirstOrderThickening.isomorphicSetoid _)
              QC)) =
        restrictExtClass f g
          (RingedToposExtensionProblem.squareZeroExtensionClassesEquiv (f.comp g) G
            (Quotient.mk
              (RingedToposExtensionProblem.CompatibleFirstOrderThickening.isomorphicSetoid _)
              QD))
```

**`Deformation.ToposThickening.LiftDiagram.pulledNaiveCotangentComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/LiftingMorphismExtensionClasses.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/LiftingMorphismExtensionClasses.lean#L138). The attribute's comment: “the canonical comparison `g^*NL_{O_C/O_B} ⟶ NL_{O_D/O_B}` along which `ζ` is read, for the DEGREEWISE pullback, built from the base-change and relative maps of Tag 0E1Y with the topoi identified as in 08UG's own reduction. The derived pullback `Lg^*NL_{O_C/O_B}` of the source's statement is NOT used: the LEFT-DERIVED extension of scalars along `O_C ⟶ O_D` is absent from the library, degreewise extension of scalars being only right exact. Tag 08TZ is NOT the missing input and is NOT absent from the library: it is carried as `Stacks.SheafOfModules.inverseImageNaiveCotangentComplexIso`, and it is about the inverse image along a morphism of TOPOI, whereas both layers here live on the one site `J`”.

> The canonical comparison `g^*NL_{𝒪_𝒞/𝒪_ℬ} ⟶ NL_{𝒪_𝒟/𝒪_ℬ}`: the base-change map for
> `f⁻¹𝒪_ℬ ⟶ 𝒪_𝒞 ⟶ 𝒪_𝒟` followed by the relative map for `f⁻¹𝒪_ℬ ⟶ g⁻¹f⁻¹𝒪_ℬ ⟶ 𝒪_𝒟`.

```lean
def pulledNaiveCotangentComparison :
    D.pulledNaiveCotangentComplex ⟶ D.relativeNaiveCotangentComplex
```

**`Deformation.ToposThickening.LiftDiagram.restrictExtClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/LiftingMorphismExtensionClasses.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/LiftingMorphismExtensionClasses.lean#L172). The attribute's comment: “the map `Ext¹(NL_{O_D/O_B}, G) ⟶ Ext¹(g^*NL_{O_C/O_B}, G)` in which `ζ` is read, the second of the two maps the source's proof constructs. The first, through the derived pullback of Tag 06YY and `Lg^*F ⟶ g^*F ⟶ G`, is NOT constructed here”.

> The map `Ext¹_{𝒪_𝒟}(NL_{𝒪_𝒟/𝒪_ℬ}, 𝒢) ⟶ Ext¹_{𝒪_𝒟}(g^*NL_{𝒪_𝒞/𝒪_ℬ}, 𝒢)`: precomposition
> with the canonical comparison of the two naive cotangent complexes.

```lean
def restrictExtClass (ζ : D.relativeExtGroup) : D.pulledExtGroup
```

**`Deformation.ToposThickening.LiftDiagram.restrictExtClassHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/LiftingMorphismExtensionClasses.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/LiftingMorphismExtensionClasses.lean#L178). The attribute's comment: “the same map as an additive homomorphism; the first of the source's two maps is not constructed here”.

> The map in which `ζ` is read, as a homomorphism of the two `Ext` groups.

```lean
def restrictExtClassHom : D.relativeExtGroup →+ D.pulledExtGroup
```

**`Deformation.ToposThickening.LiftDiagram.nonempty_lift_iff_eq_restrictExtClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/LiftingMorphismExtensionClasses.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/LiftingMorphismExtensionClasses.lean#L213). The attribute's comment: “the equivalence, from clause (1) of Tag 08UG: a morphism of ringed topoi over the base compatible with `g` and `c` exists exactly when the two Ext¹ classes agree. THIS IS THE DEGREEWISE ANALOGUE, NOT THE SOURCE'S STATEMENT: the comparison group is `Ext¹(g^*NL, G)` rather than `Ext¹(Lg^*NL, G)`, the LEFT-DERIVED extension of scalars being absent from the library (NOT Tag 08TZ, which is carried as `Stacks.SheafOfModules.inverseImageNaiveCotangentComplexIso` and is about inverse images along a morphism of topoi, not about `Lg^*` on one site), and `ξ` is taken as its image there rather than mapped in. Carried: the two-term structure `P` with its identification `hP`, the bijection `e` (Steps 1 to 3 of the proof of 08UG), the Step 1 homomorphism `δ`, and `hcompat` -- the compatibility between the constructions in the proofs of Tags 0GQ5 and 08UG whose statement and proof THE SOURCE ITSELF OMITS, deferring to Tag 0GQ8. The same concession is made by the ringed-space twin Tag 0GQ1”.

> **Stacks Project, Tag 0GQ7.** A morphism `g' : (Sh(𝒟), 𝒪_{𝒟'}) ⟶ (Sh(𝒞), 𝒪_{𝒞'})` of ringed
> topoi over `(Sh(ℬ), 𝒪_ℬ)` compatible with `g` and the prescribed map `c` on the square-zero
> ideals exists if and only if the classes of the two extensions have the same image in
> `Ext¹_{𝒪_𝒟}(g^*NL_{𝒪_𝒞/𝒪_ℬ}, 𝒢)`.
>
> Those morphisms are the concrete type `LiftDiagram.Lift` of the diagram, identified by `e` with
> the factorizations of the difference homomorphism `δ` of Step 1 of the proof of **Stacks 08UG**
> through the degree `0` term of `g^*NL_{𝒪_𝒞/𝒪_ℬ}`; the hypothesis `hcompat` is the compatibility
> between the constructions in the proofs of **Stacks 0GQ5** and **Stacks 08UG**, which the source
> omits and defers to **Stacks 0GQ8**: the difference of the two classes is the obstruction class
> of **Stacks 08UG**.

```lean
theorem nonempty_lift_iff_eq_restrictExtClass
    (P : NaiveCotangentTwoTerm (DerivedCategory.singleFunctor
      (SheafOfModules.{max u v w} (Stacks.SheafOfModules.Tensor.ringSheaf D.back.O)) 0))
    (hP : P.obj = DerivedCategory.Q.obj D.pulledNaiveCotangentComplex)
    (δ : P.conormal ⟶ D.back.G)
    (e : D.Lift ≃ {θ : P.base ⟶ D.back.G // P.d ≫ θ = δ})
    (ξ : D.pulledExtGroup) (ζ : D.relativeExtGroup)
    (hcompat : eqToHom hP ≫ (ξ - D.restrictExtClass ζ) = P.conormalExtClass D.back.G δ) :
    Nonempty D.Lift ↔ ξ = D.restrictExtClass ζ
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.nonempty_lift_iff_eq_pullbackExtClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SolutionClassesDerivedExtFibre.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/SolutionClassesDerivedExtFibre.lean#L288). The attribute's comment: “the criterion for the DERIVED pullback Lf^*NL\_\{O\_B/O\_B'} of the source's statement, with the image of ξ the constructed map pullbackExtClass. Carried, exactly as in the degreewise form of this tag: the two-term structure P with hP, the bijection e of Steps 1 to 3 of 08UG, and hcompat, the 0GQ5/08UG compatibility whose statement and proof the source itself omits, deferring to Tag 0GQ8”.

> **Stacks Project, Tag 0GQ7** for the derived pullback of **Stacks 06YY**.  A lift compatible
> with `f` and the prescribed map `c` exists if and only if the class of the extension `𝒪'`,
> restricted along a comparison `q : Lf^*NL_{𝒪_ℬ/𝒪_{ℬ'}} ⟶ NL_{𝒪/𝒪_{ℬ'}}`, agrees with the image
> of `ξ ∈ Ext¹_{𝒪_ℬ}(NL_{𝒪_ℬ/𝒪_{ℬ'}}, 𝒥)` in `Ext¹_𝒪(Lf^*NL_{𝒪_ℬ/𝒪_{ℬ'}}, 𝒢)`.
>
> Unlike the degreewise form
> `Deformation.ToposThickening.LiftDiagram.nonempty_lift_iff_eq_restrictExtClass`, the comparison
> group here is the `Ext¹` of the *derived* pullback and the image of `ξ` is the constructed map
> `pullbackExtClass`, not a hypothesis.  The compatible lifts are identified by `e` with the
> factorizations of the difference homomorphism `δ` through the degree `0` term — Steps 1 to 3 of
> the proof of **Stacks 08UG** — and `hcompat` is the compatibility between the constructions in
> the proofs of **Stacks 0GQ5** and **Stacks 08UG** which the source omits, deferring to
> **Stacks 0GQ8**: the difference of the two classes is the obstruction class.

```lean
theorem nonempty_lift_iff_eq_pullbackExtClass
    {J : SheafOfModules.{max v' u' w'} (Stacks.SheafOfModules.Tensor.ringSheaf B.O)}
    (c : S.f.toModulesHom.pullbackModules.obj J ⟶ S.G)
    (q : S.derivedPullbackNaiveCotangent ⟶ S.relativeNaiveCotangentObj)
    (P : NaiveCotangentTwoTerm (DerivedCategory.singleFunctor
      (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0))
    (hP : P.obj = S.derivedPullbackNaiveCotangent)
    (δ : P.conormal ⟶ S.G) {Lift : Type*}
    (e : Lift ≃ {θ : P.base ⟶ S.G // P.d ≫ θ = δ})
    (xi : DerivedCategory.Ext S.baseNaiveCotangentObj
      ((DerivedCategory.singleFunctor _ 0).obj J) 1)
    (ζ : S.extOneRelativeNaiveCotangent)
    (hcompat : eqToHom hP ≫ (S.pullbackExtClass c xi - S.restrictDerivedExtClass q ζ) =
      P.conormalExtClass S.G δ) :
    Nonempty Lift ↔ S.pullbackExtClass c xi = S.restrictDerivedExtClass q ζ
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.isCompatibleWithIdealClass_iff_eq_pullbackExtClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SolutionClassesDerivedExtFibre.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/SolutionClassesDerivedExtFibre.lean#L357). The attribute's comment: “the criterion for the DERIVED pullback, read on isomorphism classes of extensions: this is the cutting-out condition of 0GQ9, proved rather than assumed. Carried are the two-term structure P with hP, the per-class bijections e of Steps 1 to 3 of 08UG, the per-class 0GQ5/08UG compatibilities that the source defers to 0GQ8, and the 0GQ5 bijection E”.

> **Stacks Project, Tag 0GQ7**, read on isomorphism classes: a class of square-zero extensions
> of `f⁻¹𝒪_{ℬ'}`-algebras induces the prescribed map `c` on the base ideal — equivalently, is a
> class of solutions of **Stacks 08UF** — exactly when its image under `E` restricts, along a
> comparison `q : Lf^*NL_{𝒪_ℬ/𝒪_{ℬ'}} ⟶ NL_{𝒪/𝒪_{ℬ'}}`, to the image of `ξ`.
>
> This is the cutting-out condition of **Stacks 0GQ9**, proved rather than assumed.  `E` is the
> bijection of **Stacks 0GQ5**, and `P`, `hP`, `δ`, `e` and `hcompat` are the inputs of the
> criterion for the derived pullback.

```lean
theorem isCompatibleWithIdealClass_iff_eq_pullbackExtClass
    {J : SheafOfModules.{max v' u' w'} (Stacks.SheafOfModules.Tensor.ringSheaf B.O)}
    (c : S.f.toModulesHom.pullbackModules.obj J ⟶ S.G)
    (E : CompatibleFirstOrderThickening.IsomorphismClasses S.squareZeroProblem ≃
      S.extOneRelativeNaiveCotangent)
    (q : S.derivedPullbackNaiveCotangent ⟶ S.relativeNaiveCotangentObj)
    (xi : DerivedCategory.Ext S.baseNaiveCotangentObj
      ((DerivedCategory.singleFunctor _ 0).obj J) 1)
    (P : NaiveCotangentTwoTerm (DerivedCategory.singleFunctor
      (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0))
    (hP : P.obj = S.derivedPullbackNaiveCotangent)
    (δ : CompatibleFirstOrderThickening.IsomorphismClasses S.squareZeroProblem →
      (P.conormal ⟶ S.G))
    (e : ∀ p : CompatibleFirstOrderThickening.IsomorphismClasses S.squareZeroProblem,
      S.CompatibleSolutionInClass p ≃ {θ : P.base ⟶ S.G // P.d ≫ θ = δ p})
    (hcompat : ∀ p : CompatibleFirstOrderThickening.IsomorphismClasses S.squareZeroProblem,
      eqToHom hP ≫ (S.pullbackExtClass c xi - S.restrictDerivedExtClass q (E p)) =
        P.conormalExtClass S.G (δ p))
    (p : CompatibleFirstOrderThickening.IsomorphismClasses S.squareZeroProblem) :
    S.IsCompatibleWithIdealClass p ↔
      S.restrictDerivedExtClass q (E p) = S.pullbackExtClass c xi
```

## Tag 0GQ8, a remark

[Tag 0GQ8](https://stacks.math.columbia.edu/tag/0GQ8) in the Stacks Project.

**`Deformation.ToposThickening.InverseImageExtension.Data.pullbackExtension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/InverseImageExtensionComparison.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/InverseImageExtensionComparison.lean#L324). The attribute's comment: “the pullback extension 𝒪'₂ = 𝒪\_\{𝒟'} ×\_\{𝒪\_𝒟} g⁻¹𝒪\_𝒞 along g^♯, with the second displayed diagram its projections. Carried: that 𝒢 is the square-zero ideal of 𝒪\_\{𝒟'} with its 𝒪\_𝒟-action (Data.ι, Data.inr\_mul\_inr, Data.smul\_inr). NOT carried: that g⁻¹𝒪\_\{𝒞'} is an extension of g⁻¹𝒪\_𝒞 by g⁻¹ℱ -- the ideal is the kernel ideal of g⁻¹(reduction) and local surjectivity is isLocallySurjective\_invImage\_map”.

> **Stacks 0GQ8, the second construction.**  Pulling the extension
> `0 ⟶ 𝒢 ⟶ 𝒪_{𝒟'} ⟶ 𝒪_𝒟 ⟶ 0` back along `g^♯ : g⁻¹𝒪_𝒞 ⟶ 𝒪_𝒟` gives an extension
> `0 ⟶ 𝒢 ⟶ 𝒪'₂ ⟶ g⁻¹𝒪_𝒞 ⟶ 0` of `g⁻¹f⁻¹𝒪_ℬ`-algebras, with
> `𝒪'₂ = 𝒪_{𝒟'} ×_{𝒪_𝒟} g⁻¹𝒪_𝒞` the fibre product of sheaves of rings and the remark's second
> displayed diagram its two projections.

```lean
def pullbackExtension :
    AlgebraExtension ((invImage g).obj (baseRing f)) ((invImage g).obj X.O) d.invBase
      d.G.val.presheaf
```

**`Deformation.ToposThickening.InverseImageExtension.Data.pushoutExtension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/InverseImageExtensionComparison.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/InverseImageExtensionComparison.lean#L340). The attribute's comment: “the pushout extension 𝒪'₁ of g⁻¹𝒪\_\{𝒞'} along c : g⁻¹ℱ ⟶ 𝒢, with the first displayed diagram its comparison with g⁻¹𝒪\_\{𝒞'}. Carried: that 𝒢 is the square-zero ideal of 𝒪\_\{𝒟'}. NOT carried: that g⁻¹𝒪\_\{𝒞'} is an extension of g⁻¹𝒪\_𝒞 by g⁻¹ℱ -- the ideal is the kernel ideal of g⁻¹(reduction), whose identification with g⁻¹ℱ is the left exactness of g⁻¹, and local surjectivity is isLocallySurjective\_invImage\_map”.

> **Stacks 0GQ8, the first construction.**  Pushing the extension
> `0 ⟶ g⁻¹ℱ ⟶ g⁻¹𝒪_{𝒞'} ⟶ g⁻¹𝒪_𝒞 ⟶ 0` out along `c : g⁻¹ℱ ⟶ 𝒢` gives an extension
> `0 ⟶ 𝒢 ⟶ 𝒪'₁ ⟶ g⁻¹𝒪_𝒞 ⟶ 0` of `g⁻¹f⁻¹𝒪_ℬ`-algebras, with the remark's first displayed diagram
> its comparison with `g⁻¹𝒪_{𝒞'}`.

```lean
def pushoutExtension [HasWeakSheafify Y.J CommRingCat.{u}]
    [Y.J.WEqualsLocallyBijective CommRingCat.{u}] :
    AlgebraExtension ((invImage g).obj (baseRing f)) ((invImage g).obj X.O) d.invBase
      d.G.val.presheaf
```

**`Deformation.ToposThickening.InverseImageExtension.Data.nonempty_compatibleHom_iff_isomorphic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/InverseImageExtensionComparison.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/InverseImageExtensionComparison.lean#L402). The attribute's comment: “the diagram chase: a morphism g' : (Sh(D), O\_\{D'}) ⟶ (Sh(C), O\_\{C'}) of ringed topoi over (Sh(B), O\_B) compatible with g and c exists iff 𝒪'₁ ≅ 𝒪'₂ as g⁻¹f⁻¹O\_B-algebra extensions of g⁻¹O\_C by 𝒢; g' is in comorphism form, a morphism of ringed topoi inducing g by Data.ringedToposHomEquiv and Data.compatibleRingedToposHom. Carried: 𝒢 is the square-zero ideal of O\_\{D'}. NOT included: the remark's second half, identifying 𝒪'₁ with ξ and 𝒪'₂ with ζ”.

> **Stacks Project, Tag 0GQ8, the criterion.**  A morphism
> `g' : (Sh(𝒟), 𝒪_{𝒟'}) ⟶ (Sh(𝒞), 𝒪_{𝒞'})` of ringed topoi over `(Sh(ℬ), 𝒪_ℬ)` compatible with
> `g` and `c` exists if and only if the pushout `𝒪'₁` and the pullback `𝒪'₂` are isomorphic as
> `g⁻¹f⁻¹𝒪_ℬ`-algebra extensions of `g⁻¹𝒪_𝒞` by `𝒢`.
>
> The morphisms `g'` are the comorphisms of `Data.CompatibleHom`, which really are morphisms of
> ringed topoi between the two thickenings by `Data.compatibleRingedToposHom`, with the three
> compatibilities of the source read off in `Data.compatibleRingedToposHom_base`,
> `Data.compatibleRingedToposHom_comp_p` and `Data.compatibleRingedToposHom_kernel`.

```lean
theorem nonempty_compatibleHom_iff_isomorphic [HasWeakSheafify Y.J CommRingCat.{u}]
    [Y.J.WEqualsLocallyBijective CommRingCat.{u}] :
    Nonempty d.CompatibleHom ↔
      AlgebraExtension.Isomorphic d.pushoutExtension d.pullbackExtension
```

**`Deformation.ToposThickening.InverseImageExtension.pushoutSolution`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/InverseImageExtensionSolutions.lean, line 597](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/InverseImageExtensionSolutions.lean#L597). The attribute's comment: “the first construction: the pushout O'\_1 of g⁻¹O\_\{C'} along c : g⁻¹F ⟶ G, an extension of g⁻¹O\_C by G as g⁻¹f⁻¹O\_B-algebras”.

> **Stacks 0GQ8, the pushout `𝒪'₁`, as a square-zero extension of `g⁻¹𝒪_𝒞` by `𝒢`**: a
> solution of `inverseImageProblem f g 𝒢`.

```lean
noncomputable def pushoutSolution : (inverseImageProblem f g G).CompatibleFirstOrderThickening
```

**`Deformation.ToposThickening.InverseImageExtension.pullbackSolution`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/InverseImageExtensionSolutions.lean, line 606](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/InverseImageExtensionSolutions.lean#L606). The attribute's comment: “the second construction: the pullback O'\_2 of O\_\{D'} along g^♯ : g⁻¹O\_C ⟶ O\_D, an extension of g⁻¹O\_C by G as g⁻¹f⁻¹O\_B-algebras”. References: EGA 0 (18.2.5), “more general”.

> **Stacks 0GQ8, the pullback `𝒪'₂ = 𝒪_{𝒟'} ×_{𝒪_𝒟} g⁻¹𝒪_𝒞`, as a square-zero extension of
> `g⁻¹𝒪_𝒞` by `𝒢`**: a solution of `inverseImageProblem f g 𝒢`.

```lean
noncomputable def pullbackSolution : (inverseImageProblem f g G).CompatibleFirstOrderThickening
```

**`Deformation.ToposThickening.InverseImageExtension.nonempty_compatibleMorphism_iff_isomorphic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/InverseImageExtensionSolutions.lean, line 750](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/InverseImageExtensionSolutions.lean#L750). The attribute's comment: “the diagram chase: a morphism g' over (Sh(B), O\_B) compatible with g and c exists iff O'\_1 and O'\_2 are isomorphic as g⁻¹f⁻¹O\_B-algebra extensions of g⁻¹O\_C by G”.

> **Stacks Project, Tag 0GQ8, the diagram chase.** A morphism
> `g' : (Sh(𝒟), 𝒪_{𝒟'}) ⟶ (Sh(𝒞), 𝒪_{𝒞'})` of ringed topoi over `(Sh(ℬ), 𝒪_ℬ)` compatible with `g`
> and `c` exists if and only if the pushout `𝒪'₁` and the pullback `𝒪'₂` are isomorphic as
> `g⁻¹f⁻¹𝒪_ℬ`-algebra extensions of `g⁻¹𝒪_𝒞` by `𝒢`.

```lean
theorem nonempty_compatibleMorphism_iff_isomorphic :
    Nonempty (CompatibleMorphism g QC QD c) ↔
      RingedToposExtensionProblem.CompatibleFirstOrderThickening.Isomorphic
        (pushoutSolution g QC QD c) (pullbackSolution g QC QD c)
```

**`Deformation.ToposThickening.LiftingMorphismDerived.rhoEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/LiftingMorphismDerivedRhoEquiv.lean, line 598](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/LiftingMorphismDerivedRhoEquiv.lean#L598).

> **The identification of Ext groups**
> `Ext¹_{𝒪_𝒟}(Lg^*NL_{𝒪_𝒞/𝒪_ℬ}, 𝒢) = Ext¹_{g⁻¹𝒪_𝒞}(NL_{g⁻¹𝒪_𝒞/g⁻¹f⁻¹𝒪_ℬ}, 𝒢)`, the base of the
> right-hand side read as `(f ∘ g)⁻¹𝒪_ℬ ≅ g⁻¹f⁻¹𝒪_ℬ`: the bijection `rhoClass`, which sends
> `e : Lg^*NL_{𝒪_𝒞/𝒪_ℬ} ⟶ 𝒢[1]` to the composite of the identification
> `NL_{g⁻¹𝒪_𝒞/g⁻¹f⁻¹𝒪_ℬ} ≅ g⁻¹NL_{𝒪_𝒞/𝒪_ℬ}` of Stacks 08TZ, the derived unit
> `g⁻¹NL_{𝒪_𝒞/𝒪_ℬ} ⟶ Lg^*NL_{𝒪_𝒞/𝒪_ℬ}` read over `g⁻¹𝒪_𝒞` (the tensor-hom adjunction along
> `g^♯`) and `e` read over `g⁻¹𝒪_𝒞`.

```lean
def rhoEquiv :
    DerivedCategory.Ext ((derivedPullback g).obj (DerivedCategory.Q.obj
        (Stacks.SheafOfModules.naiveCotangentComplex.{u, u, u, u} X.J
          ((inverseImageCommRingFunctor f.toToposHom).obj B.O) X.O f.fSharpInverseImage)))
      ((DerivedCategory.singleFunctor _ 0).obj G) 1 ≃
    DerivedCategory.Ext (DerivedCategory.Q.obj
        (Stacks.SheafOfModules.naiveCotangentComplex.{u, u, u, u} Y.J
        ((inverseImageCommRingFunctor (f.comp (toInverseImage g)).toToposHom).obj B.O)
        ((invImage g).obj X.O) (f.comp (toInverseImage g)).fSharpInverseImage))
      ((DerivedCategory.singleFunctor (SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf ((invImage g).obj X.O))) 0).obj
          (restrictedIdeal g G)) 1
```

**`Deformation.ToposThickening.LiftingMorphismDerived.rhoEquiv_extClass_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/LiftingMorphismDerivedRhoEquiv.lean, line 634](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/LiftingMorphismDerivedRhoEquiv.lean#L634).

> **The classes of `𝒪'₁` and `𝒪'₂`.** Under the identification `rhoEquiv` of
> `Ext¹_{𝒪_𝒟}(Lg^*NL_{𝒪_𝒞/𝒪_ℬ}, 𝒢)` with `Ext¹_{g⁻¹𝒪_𝒞}(NL_{g⁻¹𝒪_𝒞/g⁻¹f⁻¹𝒪_ℬ}, 𝒢)`, the image of
> `ξ` (the class of `QC`, through `Lg^*` and `Lg^*ℱ ⟶ g^*ℱ ⟶ 𝒢`) is the class (Stacks 0GQ5) of the
> pushout `𝒪'₁` of `g⁻¹𝒪_{𝒞'}` along `c`, and the image of `ζ` (the class of `QD`, through
> `Lg^*NL_{𝒪_𝒞/𝒪_ℬ} ⟶ NL_{𝒪_𝒟/𝒪_ℬ}`) is the class of the pullback `𝒪'₂` of `𝒪_{𝒟'}` along
> `g^♯`.

```lean
theorem rhoEquiv_extClass_eq :
    rhoEquiv g (pullbackExtClass g c
        (RingedToposExtensionProblem.squareZeroExtensionClassesEquiv f F
          (Quotient.mk
            (RingedToposExtensionProblem.CompatibleFirstOrderThickening.isomorphicSetoid _)
            QC))) =
      RingedToposExtensionProblem.squareZeroExtensionClassesEquiv (f.comp (toInverseImage g))
        (restrictedIdeal g G)
        (Quotient.mk (RingedToposExtensionProblem.CompatibleFirstOrderThickening.isomorphicSetoid _)
          (pushoutSolution g QC QD c)) ∧
    rhoEquiv g (restrictExtClass f g
        (RingedToposExtensionProblem.squareZeroExtensionClassesEquiv (f.comp g) G
          (Quotient.mk
            (RingedToposExtensionProblem.CompatibleFirstOrderThickening.isomorphicSetoid _)
            QD))) =
      RingedToposExtensionProblem.squareZeroExtensionClassesEquiv (f.comp (toInverseImage g))
        (restrictedIdeal g G)
        (Quotient.mk (RingedToposExtensionProblem.CompatibleFirstOrderThickening.isomorphicSetoid _)
          (pullbackSolution g QC QD c))
```

## Tag 0GQ9, a lemma

[Tag 0GQ9](https://stacks.math.columbia.edu/tag/0GQ9) in the Stacks Project.

**`Deformation.ToposThickening.RingedToposExtensionProblem.solutionEquivSquareZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SolutionClassesFibre.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/SolutionClassesFibre.lean#L236). The attribute's comment: “the step the source states as -- of course this is the same thing as saying that O' is a solution of 08UF: a solution of the problem of Tag 08UF is exactly a square-zero extension of f⁻¹O\_B'-algebras whose map from the thickened base induces the prescribed c on the base ideal. Fixed-site presentation of 08UF, as in Tag 0GQ5”.

> **The solutions of [Stacks 08UF] are exactly the square-zero extensions of
> `f⁻¹𝒪_{ℬ'}`-algebras that induce `c`.** The two solution types carry the same thickened
> structure sheaf, reduction, map from the thickened base and kernel identification.

```lean
def solutionEquivSquareZero :
    S.CompatibleFirstOrderThickening ≃
      { Q : S.squareZeroProblem.CompatibleFirstOrderThickening // S.IsCompatibleWithIdeal Q }
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.classesEquivFibre`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SolutionClassesFibre.lean, line 522](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/SolutionClassesFibre.lean#L522). The attribute's comment: “the canonical bijection between the isomorphism classes of solutions of the problem of 08UF and the fibre over 0 of `compatibilityObstruction` on Ext¹ of a FIXED presentation. Carried: ONLY the five inputs of Tag 0GQ5 at the trivial-ideal problem. The cutting-out condition is PROVED, not assumed: the obstruction is the sectionwise difference between the map a square-zero extension of f⁻¹O\_B'-algebras induces on f⁻¹J and the prescribed c, read in G, and it is shown to depend only on the Ext class. It is NOT the source's comparison map, whose target Ext¹(Lf^*NL\_\{O\_B/O\_B'}, G) needs the derived pullback Lf^*, absent from the library”.

> **Stacks Project, Tag 0GQ9.** The isomorphism classes of solutions of the square-zero
> extension problem of [Stacks 08UF] are canonically bijective to the fibre over `0` of the
> compatibility obstruction on the first `Ext` group of the presentation.
>
> The bijection is `classesEquivCompatible`, which identifies the solutions with the square-zero
> extensions of `f⁻¹𝒪_{ℬ'}`-algebras inducing `c`, followed by the bijection `classesEquivExt` of
> [Stacks 0GQ5] for the problem `squareZeroProblem` over the thickened base. That such an
> extension induces `c` exactly when its obstruction vanishes is
> `isCompatibleWithIdeal_iff_idealObstruction_eq_zero`, and the obstruction descends to `Ext¹`
> through `idealObstruction_of_iso`. The hypotheses are exactly those of `classesEquivExt`; see the
> implementation notes of this file.

```lean
def classesEquivFibre
    (P : NaiveCotangentTwoTerm single)
    (xi : S.squareZeroProblem.CompatibleFirstOrderThickening →
      S.squareZeroProblem.CompatibleFirstOrderThickening → (P.conormal ⟶ S.G))
    (hxi : ∀ Q₁ Q₂ Q₃ : S.squareZeroProblem.CompatibleFirstOrderThickening,
      xi Q₁ Q₂ + xi Q₂ Q₃ = xi Q₁ Q₃)
    (rep : ∀ ζ : P.obj ⟶ (single.obj S.G)⟦(1 : ℤ)⟧,
      { δ : P.conormal ⟶ S.G // liftingObstruction P S.G δ = ζ })
    (pushout : ∀ (Q : S.squareZeroProblem.CompatibleFirstOrderThickening)
        (δ : P.conormal ⟶ S.G),
      { Q' : S.squareZeroProblem.CompatibleFirstOrderThickening // xi Q Q' = δ })
    (ee : ∀ Q₁ Q₂ : S.squareZeroProblem.CompatibleFirstOrderThickening,
      CompatibleFirstOrderThickening.Hom Q₁ Q₂ ≃
        { θ : P.base ⟶ S.G // P.d ≫ θ = xi Q₁ Q₂ }) :
    CompatibleFirstOrderThickening.IsomorphismClasses S ≃
      { ζ : P.obj ⟶ (single.obj S.G)⟦(1 : ℤ)⟧ //
        S.compatibilityObstruction P xi hxi rep pushout ee ζ = 0 }
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.solutionClassesEquivDerivedExtFibre`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SolutionClassesNaiveExtFibre.lean, line 485](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/SolutionClassesNaiveExtFibre.lean#L485).

> **Stacks Project, Tag 0GQ9.** Let `t : (Sh(ℬ), 𝒪_ℬ) ⟶ (Sh(ℬ'), 𝒪_{ℬ'})`, `𝒥 = Ker(t^♯)`,
> `f : (Sh(𝒞), 𝒪) ⟶ (Sh(ℬ), 𝒪_ℬ)`, `𝒢` and `c : f⁻¹𝒥 ⟶ 𝒢` be as in (08UF) — the problem `S` —
> and let `ξ ∈ Ext¹_{𝒪_ℬ}(NL_{𝒪_ℬ/𝒪_{ℬ'}}, 𝒥)` be the element corresponding to the extension
> `𝒪_{ℬ'}` of `𝒪_ℬ` by `𝒥` via **Stacks 0GQ5** (`baseThickeningClass`). The set of isomorphism
> classes of solutions is canonically bijective to the fibre of
> `Ext¹_𝒪(NL_{𝒪/𝒪_{ℬ'}}, 𝒢) ⟶ Ext¹_𝒪(Lf^*NL_{𝒪_ℬ/𝒪_{ℬ'}}, 𝒢)` over the image of `ξ`
> (`derivedExtFibre`), `Lf^*` being the derived pullback of **Stacks 06YY**.
>
> The bijection is the one of the source's proof: the class of a solution `𝒪'` goes to the
> element of `Ext¹_𝒪(NL_{𝒪/𝒪_{ℬ'}}, 𝒢)` which **Stacks 0GQ5** for `t ∘ f` attaches to `𝒪'` as an
> extension of `(t ∘ f)⁻¹𝒪_{ℬ'}`-algebras (`solutionClassesEquivDerivedExtFibre_mk`); that the
> classes so obtained are exactly the fibre is **Stacks 0GQ7**.

```lean
def solutionClassesEquivDerivedExtFibre :
    CompatibleFirstOrderThickening.IsomorphismClasses S ≃ S.derivedExtFibre
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.solutionClassesEquivDerivedExtFibre_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SolutionClassesNaiveExtFibre.lean, line 496](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/SolutionClassesNaiveExtFibre.lean#L496).

> **The bijection of Stacks 0GQ9 is the canonical one**: the class of a solution `𝒪'` goes to
> the element of `Ext¹_𝒪(NL_{𝒪/𝒪_{ℬ'}}, 𝒢)` that **Stacks 0GQ5** for `t ∘ f` attaches to `𝒪'`,
> read as a square-zero extension of `(t ∘ f)⁻¹𝒪_{ℬ'}`-algebras.

```lean
theorem solutionClassesEquivDerivedExtFibre_mk (P : S.CompatibleFirstOrderThickening) :
    (S.solutionClassesEquivDerivedExtFibre (Quotient.mk _ P)).1 =
      squareZeroExtensionClassesEquiv S.compBase S.G
        (Quotient.mk (CompatibleFirstOrderThickening.isomorphicSetoid _) (S.toCompSolution P))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 91.13, Tag 08UE](https://stacks.math.columbia.edu/tag/08UE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
