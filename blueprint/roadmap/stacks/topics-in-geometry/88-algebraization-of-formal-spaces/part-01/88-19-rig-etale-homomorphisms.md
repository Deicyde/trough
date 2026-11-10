---
declaration: section
origin: cited
lean: Rig.rigEtaleOver_iff_forall_idealOfDefinition, RingHom.IsRigEtale, Rig.rigEtale_propertyIsLocalNoetherian, TopologicalRing.rigEtale_completedTensorProduct_of_isAdic, Rig.rigEtale_comp, Rig.rigEtale_hasNoetherianCancellationProperty
statement: formalized
proof: formalized
---

# 88.19 Rig-étale homomorphisms

Section 88.19 of the Stacks Project, [Tag 0GCT](https://stacks.math.columbia.edu/tag/0GCT). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GCU, a lemma

[Tag 0GCU](https://stacks.math.columbia.edu/tag/0GCU) in the Stacks Project.

**`Rig.rigEtaleOver_iff_forall_idealOfDefinition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigSmooth.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/RigSmooth.lean#L220).

> **Stacks Project, Tag 0GCU.** For an adic morphism of topologically finite type between
> Noetherian adic rings, rig-étaleness over one ideal of definition is equivalent to
> rig-étaleness over every ideal of definition.

```lean
public theorem rigEtaleOver_iff_forall_idealOfDefinition
    {A : Type u} {B : Type v}
    [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [IsNoetherianRing A]
    [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [IsNoetherianRing B]
    (φ : A →+* B) (_hφ : Continuous φ)
    (_hA : TopologicalRing.IsAdic A) (_hB : TopologicalRing.IsAdic B) :
    (FiniteTypeAdicAlgebraForEveryIdeal φ ∧
      ∃ I : Ideal A, TopologicalRing.IsIdealOfDefinition I ∧ IsRigEtaleOver φ I) ↔
    (FiniteTypeAdicAlgebraForEveryIdeal φ ∧
      ∀ I : Ideal A, TopologicalRing.IsIdealOfDefinition I → IsRigEtaleOver φ I)
```

## Tag 0GCV, a definition

[Tag 0GCV](https://stacks.math.columbia.edu/tag/0GCV) in the Stacks Project.

**`RingHom.IsRigEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigSmooth.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/RigSmooth.lean#L277).

> **Stacks Project, Tag 0GCV.** A continuous homomorphism of Noetherian adic topological
> rings is *rig-étale* when it is adic of topologically finite type — condition (6) of Tag 0GBW
> — and makes its target rig-étale over some ideal of definition of its source.  By Tag 0GCU the
> choice of that ideal is immaterial.

```lean
public abbrev IsRigEtale {A : Type u} {B : Type v}
    [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [IsNoetherianRing A]
    [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [IsNoetherianRing B]
    (φ : A →+* B) : Prop
```

## Tag 0AQL, a lemma

[Tag 0AQL](https://stacks.math.columbia.edu/tag/0AQL) in the Stacks Project.

**`Rig.rigEtale_propertyIsLocalNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigEtaleIsLocal.lean, line 649](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/RigEtaleIsLocal.lean#L649).

> **Stacks 0AQL.** Rig-étaleness is a local property of arrows of `WAdm^Noeth`, in the sense
> of Situation 0CBA in the Noetherian form of Remark 0ANI: it ascends along a completed étale
> localization diagram, descends along one whose target-side horizontal map is faithfully flat,
> and is preserved by finite products of targets.

```lean
public theorem rigEtale_propertyIsLocalNoetherian :
    TopologicalRing.PropertyIsLocalNoetherian.{u}
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦
        RingHom.IsRigEtaleArrow φ)
```

## Tag 0GCW, a lemma

[Tag 0GCW](https://stacks.math.columbia.edu/tag/0GCW) in the Stacks Project.

**`TopologicalRing.rigEtale_completedTensorProduct_of_isAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigSmoothStability.lean, line 801](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/RigSmoothStability.lean#L801).

> Rig-étaleness (Tag 0GCV) is stable under base change by adic morphisms (Tag 0GBR) in the
> sense of Remark 0GBG: if `B → A` is rig-étale and `B → C` is adic, both arrows of
> `WAdm^{Noeth}`, then the completed tensor product `A ⊗̂_B C` is again Noetherian adic and
> rig-étale over `C`.

```lean
public theorem rigEtale_completedTensorProduct_of_isAdic
    {B A C : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B] [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing C] [TopologicalSpace C] [IsTopologicalRing C]
    [IsLinearTopology C C] [Algebra B A] [Algebra B C] [IsNoetherianRing B]
    [IsNoetherianRing A] [IsNoetherianRing C]
    (hB : TopologicalRing.IsAdic B) (hA : TopologicalRing.IsAdic A)
    (hC : TopologicalRing.IsAdic C)
    (hBA : Continuous (algebraMap B A)) (hBC : Continuous (algebraMap B C))
    (hP : RingHom.IsRigEtaleArrow (algebraMap B A))
    (hQ : RingHom.IsAdic (algebraMap B C)) :
    TopologicalRing.IsAdic (TopologicalRing.CompletedTensorProduct (R := B) (M := A) (N := C)) ∧
      IsNoetherianRing (TopologicalRing.CompletedTensorProduct (R := B) (M := A) (N := C)) ∧
      RingHom.IsRigEtaleArrow
        (algebraMap C (TopologicalRing.CompletedTensorProduct (R := B) (M := A) (N := C)))
```

## Tag 0GCX, a lemma

[Tag 0GCX](https://stacks.math.columbia.edu/tag/0GCX) in the Stacks Project.

**`Rig.rigEtale_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigSmoothStableUnderComposition.lean, line 615](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/RigSmoothStableUnderComposition.lean#L615).

> **Stacks Project, Tag 0GCX.**  Rig-étaleness of arrows of `WAdm^Noeth` is stable under
> composition in the sense of Formal Spaces Remark 0GBK: if `f : B →+* A` and `g : C →+* B` are
> continuous rig-étale homomorphisms of Noetherian adic topological rings, then so is `f ∘ g`.
>
> Condition (6) of Stacks 0GBW for the composite is
> `Rig.finiteTypeAdicAlgebraForEveryIdeal_comp`.  For rig-étaleness over an ideal of definition
> `I ⊆ C`, Stacks 0GCU moves both hypotheses onto `I` and onto `I B`, Stacks 0ALM presents `A`
> over `(C, I)` by combining the two presentations, and the two exactness statements of its
> six-term sequence at the middle complex `NL^∧_{A/C}` multiply the two annihilating ideals of
> condition (3) of Stacks 0AJU.

```lean
public theorem rigEtale_comp
    {A B C : Type u} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [IsNoetherianRing A]
    [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [IsNoetherianRing B]
    [CommRing C] [TopologicalSpace C] [IsTopologicalRing C] [IsLinearTopology C C]
    [IsNoetherianRing C]
    (hA : TopologicalRing.IsAdic A) (hB : TopologicalRing.IsAdic B)
    (hC : TopologicalRing.IsAdic C)
    (f : B →+* A) (g : C →+* B) (hf : Continuous f) (hg : Continuous g)
    (hPf : RingHom.IsRigEtale f) (hPg : RingHom.IsRigEtale g) :
    RingHom.IsRigEtale (f.comp g)
```

## Tag 0GCY, a lemma

[Tag 0GCY](https://stacks.math.columbia.edu/tag/0GCY) in the Stacks Project.

**`Rig.rigEtale_hasNoetherianCancellationProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigSmoothStableUnderComposition.lean, line 834](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/RigSmoothStableUnderComposition.lean#L834).

> **Stacks Project, Tag 0GCY.**  Rig-étaleness on arrows of `WAdm^Noeth` has the
> cancellation property of Formal Spaces Remark 0GBP: for `f : B →+* A` and `g : C →+* B`
> continuous homomorphisms of Noetherian adic topological rings, rig-étaleness of `g` and of
> `f ∘ g` implies rig-étaleness of `f`.
>
> Unlike the base-change bundle of Tag 0GCL and the composition bundle of Tag 0GBK, the
> cancellation predicate `TopologicalRing.HasNoetherianCancellationProperty` carries no locality
> field, so this bundle is exactly what Remark 0GBP defines and exactly what 0GCY asserts; the
> tag therefore sits on it.  Its content is `Rig.rigEtale_cancel`.

```lean
public theorem rigEtale_hasNoetherianCancellationProperty :
    TopologicalRing.HasNoetherianCancellationProperty.{u}
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦
        RingHom.IsRigEtaleArrow φ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.19, Tag 0GCT](https://stacks.math.columbia.edu/tag/0GCT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
