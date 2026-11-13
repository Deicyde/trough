---
declaration: section
origin: cited
lean: Deformation.ToposThickening.IsThickening, Deformation.ToposThickening.IdealOfThickening, Deformation.ToposThickening.IsThickening.of_firstOrderThickening, Deformation.ToposThickening.IsFirstOrderThickening, Deformation.ToposThickening.IsFirstOrderThickening.of_firstOrderThickening, Deformation.ToposThickening.MorphismOfThickenings, Deformation.ToposThickening.MorphismOfThickenings.firstOrderSurjection, Deformation.ToposThickening.MorphismOfThickenings.firstOrderSurjection_epi
statement: formalized
proof: formalized
---

# 91.9 Thickenings of ringed topoi

Section 91.9 of the Stacks Project, [Tag 08M6](https://stacks.math.columbia.edu/tag/08M6). 2 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08M7, a situation

[Tag 08M7](https://stacks.math.columbia.edu/tag/08M7) in the Stacks Project.

**`Deformation.ToposThickening.IsThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/MorphismOfThickenings.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/MorphismOfThickenings.lean#L119). The attribute's comment: “the horizontal arrows are thickenings”.

> **Stacks 08M7.** A thickening of ringed topoi: the underlying geometric morphism is an
> equivalence of topoi, the structure map is locally surjective, and its kernel ideal is locally
> nilpotent. This is the hypothesis the source places on the horizontal arrows of a morphism of
> thickenings.

```lean
def IsThickening (i : RingedToposHom X Y) : Prop
```

**`Deformation.ToposThickening.IdealOfThickening`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/MorphismOfThickenings.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/MorphismOfThickenings.lean#L127). The attribute's comment: “the defining ideal of a thickening”.

> **Stacks 08M7.** The defining ideal `I = Ker(i^♯) ⊂ O'` of a thickening `i`, presented as a
> sheaf of `O'`-modules together with an inclusion into `O'` whose sections are exactly the
> sections killed by the structure map.

```lean
structure IdealOfThickening (i : RingedToposHom X Y)
```

**`Deformation.ToposThickening.IsThickening.of_firstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/MorphismOfThickenings.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/MorphismOfThickenings.lean#L194). The attribute's comment: “a first order thickening is a thickening”.

> **Stacks 08M7.** A first order thickening of ringed topoi in the sense of Stacks 08MB is a
> thickening: its structure map is locally surjective by assumption and its square-zero kernel is
> in particular locally nilpotent.

```lean
theorem IsThickening.of_firstOrderThickening {i : RingedToposHom X Y}
    (h : FirstOrderThickening i) : IsThickening i
```

**`Deformation.ToposThickening.IsFirstOrderThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/MorphismOfThickenings.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/MorphismOfThickenings.lean#L203). The attribute's comment: “first order thickening, as a property”.

> **Stacks 08M7.** A first order thickening of ringed topoi, as a property of a morphism: a
> thickening whose kernel ideal is square zero. This is the predicate form of the structure
> `Deformation.ToposThickening.FirstOrderThickening` of Stacks 08MB, which in addition names the
> ideal.

```lean
def IsFirstOrderThickening (i : RingedToposHom X Y) : Prop
```

**`Deformation.ToposThickening.IsFirstOrderThickening.of_firstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/MorphismOfThickenings.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/MorphismOfThickenings.lean#L215). The attribute's comment: “08MB implies the property”.

> **Stacks 08M7.** A first order thickening in the sense of Stacks 08MB has the property of
> being a first order thickening: its kernel is the square-zero ideal it names.

```lean
theorem IsFirstOrderThickening.of_firstOrderThickening {i : RingedToposHom X Y}
    (h : FirstOrderThickening i) : IsFirstOrderThickening i
```

**`Deformation.ToposThickening.MorphismOfThickenings`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/MorphismOfThickenings.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/MorphismOfThickenings.lean#L236). The attribute's comment: “the commutative square”.

> **Stacks 08M7.** A morphism of thickenings of ringed topoi: a commutative square of
> morphisms of ringed topoi whose horizontal arrows `i` and `t` are thickenings, together with
> their defining ideals `I = Ker(i^♯) ⊂ O'` and `J = Ker(t^♯) ⊂ O_{B'}`.

```lean
structure MorphismOfThickenings
```

**`Deformation.ToposThickening.MorphismOfThickenings.firstOrderSurjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/MorphismOfThickeningsFirstOrder.lean, line 314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/MorphismOfThickeningsFirstOrder.lean#L314). The attribute's comment: “the first order reduction of the pullback of the lower ideal; the two upper topoi share their section universe, as the closed immersion carried by AlgebraicGeometry.ClosedRingedImmersion requires, the two lower ones staying independent”.

> **Stacks 08M7.** The canonical reduction map `(f')^*J ⟶ f^*J` of a morphism of thickenings of
> ringed topoi, with the target read as the `O'`-module `i_*f^*t^*J`: the unit of `i^* ⊣ i_*`,
> followed by the direct image of the canonical comparison
> `Deformation.ToposThickening.MorphismOfThickenings.pullbackComparison` of the two iterated
> pullbacks around the square.
>
> The map needs no hypothesis on the square. When the upper arrow is a first order thickening it
> is an epimorphism, by
> `Deformation.ToposThickening.MorphismOfThickenings.firstOrderSurjection_epi`.
>
> What is proved here is an epimorphism with a unique factorization, and not the source's
> assertion, which is an equality `(f')^*J = f^*J` of the two pullbacks. The equality is not
> available under the hypotheses of Situation 91.9.1. By
> `Deformation.ToposThickening.IsThickening.essImage_pushforwardModules_iff` this map is an
> isomorphism exactly when `I` annihilates `(f')^*J`; and what annihilates `(f')^*J` is the ideal
> `J·O'` generated by the image of `J` under `(f')^♯`, since a product of two sections of `J` is
> zero. So the source's equality amounts to `J·O' = I`, which is the strictness
> `Deformation.ToposThickening.MorphismOfThickenings.IsStrict` of Stacks 08M9 — a further
> hypothesis that Situation 91.9.1 does not make. The source also identifies the equivalent topoi
> of the two thickenings, which this development does not do. (That reading of the source's
> equality is a remark, not a formalized equivalence; nothing below depends on it.)
>
> Nothing of the tag is lost by proving the epimorphism instead. The source uses the equality only
> to turn the induced map `(f')^*J ⟶ I` into a map `f^*J ⟶ I`, and an epimorphism does exactly
> that: it admits at most one such map, and
> `Deformation.ToposThickening.MorphismOfThickenings.firstOrderIdealMap` exhibits one, so the
> source's map is obtained and is unique.

```lean
noncomputable def firstOrderSurjection :
    (pullbackModules D.f'.toModulesHom).obj D.idealJ.I ⟶ D.reducedPullbackIdeal
```

**`Deformation.ToposThickening.MorphismOfThickenings.firstOrderSurjection_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/MorphismOfThickeningsFirstOrder.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/MorphismOfThickeningsFirstOrder.lean#L330). The attribute's comment: “surjectivity of the first order reduction; the two upper topoi share their section universe, as the closed immersion carried by AlgebraicGeometry.ClosedRingedImmersion requires, the two lower ones staying independent”.

> **Stacks 08M7.** When both thickenings are first order the canonical reduction map
> `(f')^*J ⟶ f^*J` is surjective: the unit of `i^* ⊣ i_*` is an epimorphism at every module, and
> the second factor is the direct image of an isomorphism.
>
> First-orderness of `t` is not consumed: it is what makes `t^*J` the ideal `J` read on `Sh(B)`,
> and that identification is built into `reducedPullbackIdeal`.

```lean
theorem firstOrderSurjection_epi (hi : IsFirstOrderThickening D.i)
    (_ht : IsFirstOrderThickening D.t) : Epi D.firstOrderSurjection
```

**`Deformation.ToposThickening.MorphismOfThickenings.firstOrderIdealMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/MorphismOfThickeningsFirstOrder.lean, line 348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/MorphismOfThickeningsFirstOrder.lean#L348). The attribute's comment: “the first order factorization of the induced map of defining ideals; the two upper topoi share their section universe, as the closed immersion carried by AlgebraicGeometry.ClosedRingedImmersion requires, the two lower ones staying independent”.

> **Stacks 08M7.** When both thickenings are first order the induced map of defining ideals
> `(f')^*J ⟶ I` factors uniquely through the canonical reduction `(f')^*J ⟶ f^*J`, giving the
> source's map `f^*J ⟶ I`.
>
> The factorization exists because the unit of `i^* ⊣ i_*` at `I` is an isomorphism, `I` being
> annihilated by itself; it is unique because the reduction is an epimorphism.

```lean
noncomputable def firstOrderIdealMap (hi : IsFirstOrderThickening D.i)
    (ht : IsFirstOrderThickening D.t) :
    { g : D.reducedPullbackIdeal ⟶ D.idealI.I //
      D.firstOrderSurjection ≫ g = D.idealMap ∧
        ∀ g' : D.reducedPullbackIdeal ⟶ D.idealI.I,
          D.firstOrderSurjection ≫ g' = D.idealMap → g' = g }
```

**`Deformation.ToposThickening.MorphismOfThickenings.canonicalIdealMap_existsUnique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/MorphismOfThickeningsIdealMap.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/MorphismOfThickeningsIdealMap.lean#L248). The attribute's comment: “the canonical map of defining ideals”.

> **Stacks 08M7.** There is exactly one map of `O'`-modules `(f')^*J ⟶ I` whose composite into
> `O'` is the structure map of `f'` applied to the inclusion of `J`.
>
> Existence is the factorisation of
> `Stacks.SheafOfModules.existsUnique_factorThrough`: every local section of `(f')^*J`, read in
> `O'`, is killed by `i^♯`, hence lies in `I`. Uniqueness is the sectionwise injectivity of
> `I ⟶ O'`.

```lean
theorem canonicalIdealMap_existsUnique :
    ∃! φ : (D.f'.toModulesHom.pullbackModules).obj D.idealJ.I ⟶ D.idealI.I,
      D.IsCanonicalIdealMap φ
```

**`Deformation.ToposThickening.MorphismOfThickenings.idealMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/MorphismOfThickeningsIdealMap.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/MorphismOfThickeningsIdealMap.lean#L258). The attribute's comment: “the induced map of defining ideals”.

> **Stacks 08M7.** The induced map of defining ideals `(f')^*J ⟶ I` of a morphism of
> thickenings of ringed topoi.

```lean
noncomputable def idealMap : (D.f'.toModulesHom.pullbackModules).obj D.idealJ.I ⟶ D.idealI.I
```

**`Deformation.ToposThickening.MorphismOfThickenings.idealMap_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/MorphismOfThickeningsIdealMap.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/MorphismOfThickeningsIdealMap.lean#L264). The attribute's comment: “the induced map of defining ideals is the normalised one”.

> **Stacks 08M7.** The induced map of defining ideals has the normalisation that
> characterises it.

```lean
theorem idealMap_spec : D.IsCanonicalIdealMap D.idealMap
```

**`Deformation.ToposThickening.MorphismOfThickenings.homEquiv_idealMap_comp_incl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/MorphismOfThickeningsIdealMap.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/MorphismOfThickeningsIdealMap.lean#L276). The attribute's comment: “the induced map of defining ideals is the structure map of `f'` on `J`”.

> **Stacks 08M7.** The induced map of defining ideals, read on the target topos: its adjoint
> transpose, composed with the inclusion of `I` into `O'`, is the structure map of `f'` applied to
> the inclusion of `J` into `O_{B'}`. This is the source's own description of the map.

```lean
theorem homEquiv_idealMap_comp_incl :
    (pullbackAdjPushforwardModules D.f').homEquiv D.idealJ.I
        (SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf (J := X'.J)) X'.O))
        (D.idealMap ≫ D.idealI.incl) =
      D.idealJ.incl ≫ unitStructureMap D.f'
```

**`Deformation.ToposThickening.MorphismOfThickenings.pullbackComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/MorphismOfThickeningsIdealMap.lean, line 329](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/MorphismOfThickeningsIdealMap.lean#L329). The attribute's comment: “the canonical comparison of the two iterated pullbacks around the square”.

> **Stacks 08M7.** The canonical comparison of the two iterated pullbacks around the square:
> pulling back along `f'` and then `i` is pulling back along `t` and then `f`.
>
> Each side is a composite of left adjoints, so it is the mate of the corresponding comparison of
> iterated direct images, which is
> `AlgebraicGeometry.RingedToposHom.pushforwardModulesCompIso`; the two are then joined by the
> commutativity of the square, the pullback functor depending on the morphism of ringed topoi
> only through its value.

```lean
noncomputable def pullbackComparison :
    D.f'.toModulesHom.pullbackModules ⋙ D.i.toModulesHom.pullbackModules ≅
      D.t.toModulesHom.pullbackModules ⋙ D.f.toModulesHom.pullbackModules
```

## Tag 08M9, a definition

[Tag 08M9](https://stacks.math.columbia.edu/tag/08M9) in the Stacks Project.

**`Deformation.ToposThickening.MorphismOfThickenings.IsStrict`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/MorphismOfThickeningsIdealMap.lean, line 296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/MorphismOfThickeningsIdealMap.lean#L296). The attribute's comment: “strict morphism of thickenings”.

> **Stacks 08M9.** A morphism of thickenings of ringed topoi is *strict* when its induced map
> of defining ideals `(f')^*J ⟶ I` is surjective, i.e. an epimorphism of sheaves of
> `O'`-modules.

```lean
def IsStrict : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 91.9, Tag 08M6](https://stacks.math.columbia.edu/tag/08M6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
