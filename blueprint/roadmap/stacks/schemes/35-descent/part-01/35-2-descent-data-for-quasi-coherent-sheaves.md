---
declaration: section
origin: cited
lean: AlgebraicGeometry.QuasicoherentDescentData, AlgebraicGeometry.QuasicoherentDescentData.pullFunctor, AlgebraicGeometry.QuasicoherentDescentData.pullFunctor_comp_ι, AlgebraicGeometry.QuasicoherentDescentData.pullFunctorIsoOfEq, AlgebraicGeometry.canonicalDescentFunctor, AlgebraicGeometry.trivialDescentData, AlgebraicGeometry.trivialDescentComponentIso, AlgebraicGeometry.pullTrivialDescentIso
statement: formalized
proof: formalized
---

# 35.2 Descent data for quasi-coherent sheaves

Section 35.2 of the Stacks Project, [Tag 023A](https://stacks.math.columbia.edu/tag/023A). 4 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 023B, a definition

[Tag 023B](https://stacks.math.columbia.edu/tag/023B) in the Stacks Project.

**`AlgebraicGeometry.QuasicoherentDescentData`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/DescentData.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/DescentData.lean#L102).

> Descent data for quasicoherent sheaves relative to a family `f i : X i ⟶ S`.
>
> The underlying descent datum supplies the transition isomorphisms and their cocycle condition.
> Morphisms in this full subcategory are componentwise morphisms commuting with every transition
> isomorphism.  For chosen binary and triple fibre products,
> `Pseudofunctor.DescentData'.descentDataEquivalence` is component-preserving and identifies this
> with the full subcategory of the source's fibre-product presentation on quasicoherent objects.

```lean
abbrev QuasicoherentDescentData {I : Type v} {S : Scheme.{u}} {X : I → Scheme.{u}}
    (f : ∀ i, X i ⟶ S)
```

## Tag 023C, a lemma

[Tag 023C](https://stacks.math.columbia.edu/tag/023C) in the Stacks Project.

**`AlgebraicGeometry.QuasicoherentDescentData.pullFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/DescentData.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/DescentData.lean#L127). The attribute's comment: “part (2), the pullback functor”.

> Pullback along a morphism of families defines a functor on quasicoherent descent data.
>
> Its underlying functor is `Pseudofunctor.DescentData.pullFunctor`; quasicoherence of its
> components follows from preservation of quasicoherence by pullback.

```lean
noncomputable def pullFunctor (Φ : 𝒰.HomOver 𝒱 g) :
    QuasicoherentDescentData 𝒱.f ⥤ QuasicoherentDescentData 𝒰.f
```

**`AlgebraicGeometry.QuasicoherentDescentData.pullFunctor_comp_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/DescentData.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/DescentData.lean#L139). The attribute's comment: “part (1), the pulled-back descent datum”.

> After forgetting quasicoherence, `pullFunctor` is exactly the usual pullback functor on
> descent data.  Thus its objects have components `g_i^* F_{α(i)}` and the pulled-back transition
> isomorphisms, and its action on morphisms is componentwise pullback.

```lean
theorem pullFunctor_comp_ι (Φ : 𝒰.HomOver 𝒱 g) :
    pullFunctor Φ ⋙ ObjectProperty.ι _ = ObjectProperty.ι _ ⋙
        Pseudofunctor.DescentData.pullFunctor modulePullbackPseudofunctor
          (f := 𝒱.f) (p := g) (f' := 𝒰.f) (α := Φ.s₀) (p' := Φ.h₀) Φ.w₀
```

**`AlgebraicGeometry.QuasicoherentDescentData.pullFunctorIsoOfEq`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/DescentData.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/DescentData.lean#L148). The attribute's comment: “part (3), functorial isomorphism when the maps of targets agree”.

> Morphisms of families inducing the same morphism of targets give naturally isomorphic
> pullback functors on quasicoherent descent data.

```lean
noncomputable def pullFunctorIsoOfEq {g' : U ⟶ V} (Φ : 𝒰.HomOver 𝒱 g)
    (Φ' : 𝒰.HomOver 𝒱 g') (h : g = g') : pullFunctor Φ ≅ pullFunctor Φ'
```

## Tag 023D, a definition

[Tag 023D](https://stacks.math.columbia.edu/tag/023D) in the Stacks Project.

**`AlgebraicGeometry.canonicalDescentFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/DescentData.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/DescentData.lean#L172). The attribute's comment: “part (2)”.

> The functor sending a quasicoherent module on `S` to its canonical descent datum relative to
> the family `f i : X i ⟶ S`.

```lean
noncomputable def canonicalDescentFunctor {I : Type v} {S : Scheme.{u}}
    {X : I → Scheme.{u}} (f : ∀ i, X i ⟶ S) :
    Functor (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory
      (QuasicoherentDescentData f)
```

**`AlgebraicGeometry.trivialDescentData`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/DescentData.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/DescentData.lean#L194). The attribute's comment: “part (1)”.

> The trivial descent datum on a quasicoherent module, relative to the singleton family whose
> only morphism is the identity of the base scheme.

```lean
noncomputable abbrev trivialDescentData {S : Scheme.{u}}
    (M : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    QuasicoherentDescentData (PreZeroHypercover.singleton.{0} (𝟙 S)).f
```

**`AlgebraicGeometry.trivialDescentComponentIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/DescentData.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/DescentData.lean#L214). The attribute's comment: “part (1), identity comparison”.

> The sole component of the trivial descent datum is naturally isomorphic to the original
> quasicoherent module.

```lean
noncomputable def trivialDescentComponentIso {S : Scheme.{u}} :
    trivialDescentComponentFunctor (S := S) ≅
      (SheafOfModules.isQuasicoherent S.ringCatSheaf).ι
```

**`AlgebraicGeometry.pullTrivialDescentIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/DescentData.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/DescentData.lean#L292). The attribute's comment: “part (2), pullback of the trivial datum”.

> Pulling the trivial descent datum back along a family gives, naturally in the
> quasicoherent module, its canonical descent datum for that family.

```lean
noncomputable def pullTrivialDescentIso {S : Scheme.{u}} (𝒰 : PreZeroHypercover.{v} S) :
    canonicalDescentFunctor (PreZeroHypercover.singleton.{0} (𝟙 S)).f ⋙
        QuasicoherentDescentData.pullFunctor (toTrivialFamily 𝒰) ≅
      canonicalDescentFunctor 𝒰.f
```

**`AlgebraicGeometry.QuasicoherentDescentData.IsEffective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/DescentData.lean, line 324](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/DescentData.lean#L324). The attribute's comment: “part (3)”.

> A quasicoherent descent datum is effective if it is isomorphic to the canonical descent
> datum of a quasicoherent module on the target.

```lean
abbrev IsEffective (D : QuasicoherentDescentData f) : Prop
```

## Tag 023E, a lemma

[Tag 023E](https://stacks.math.columbia.edu/tag/023E) in the Stacks Project.

**`Stacks.Descent.isEffective_zariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/ZariskiEssSurj.lean, line 1215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/ZariskiEssSurj.lean#L1215). The attribute's comment: “zariski\_effectivity”.

> **The effectivity half of Stacks 023E.**  Every quasi-coherent descent datum for a family
> of open immersions whose images cover the target is effective.  This is
> `Stacks.Descent.isEffective_of_essSurj_zariski` with its standing essential-surjectivity
> hypothesis discharged by `Stacks.Descent.essSurj_toDescentData_zariski`; the full faithfulness
> half is `Stacks.Descent.nonempty_fullyFaithful_canonicalDescentFunctor_zariski`.

```lean
theorem isEffective_zariski {S : Scheme.{u}} {I : Type v} {Y : I → Scheme.{u}}
    (f : ∀ i, Y i ⟶ S) [∀ i, IsOpenImmersion (f i)] (hf : ⨆ i, (f i).opensRange = ⊤)
    (D : QuasicoherentDescentData f) : D.IsEffective
```

**`Stacks.Descent.nonempty_fullyFaithful_canonicalDescentFunctor_zariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/ZariskiGluing.lean, line 522](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/ZariskiGluing.lean#L522). The attribute's comment: “zariski\_full\_faithfulness”.

> **The full faithfulness half of Stacks 023E.**  For a family of open immersions whose images
> cover the target, the canonical descent functor of Stacks 023D on quasi-coherent modules is fully
> faithful.
>
> This is the full faithfulness clause of Stacks 023E; the effectivity clause is *not* proved
> here.

```lean
theorem nonempty_fullyFaithful_canonicalDescentFunctor_zariski
    (hf : ⨆ i, (f i).opensRange = ⊤) :
    Nonempty (canonicalDescentFunctor f).FullyFaithful
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.2, Tag 023A](https://stacks.math.columbia.edu/tag/023A)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
