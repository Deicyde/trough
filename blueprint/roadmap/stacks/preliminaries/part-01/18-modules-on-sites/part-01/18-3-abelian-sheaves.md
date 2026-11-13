---
declaration: section
origin: cited
lean: Stacks.AbelianSheaves.kernelObjIso, Stacks.AbelianSheaves.mono_iff_presheaf_mono, Stacks.AbelianSheaves.mono_iff_injective, Stacks.AbelianSheaves.mono_iff_isLocallyInjective, Stacks.AbelianSheaves.cokernelSheafifyIso, Stacks.AbelianSheaves.epi_iff_isLocallySurjective, Stacks.AbelianSheaves.exact_iff_locallyLiftable, CategoryTheory.sheafIsAbelian
statement: formalized
proof: formalized
---

# 18.3 Abelian sheaves

Section 18.3 of the Stacks Project, [Tag 03CM](https://stacks.math.columbia.edu/tag/03CM). 2 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03CN, a lemma

[Tag 03CN](https://stacks.math.columbia.edu/tag/03CN) in the Stacks Project.

**`Stacks.AbelianSheaves.kernelObjIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/AbelianSheavesAbelian.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/AbelianSheavesAbelian.lean#L64). The attribute's comment: “(2) The kernel of a morphism of abelian sheaves is the kernel of the induced morphism of underlying presheaves.”.

> **The kernel of a morphism of abelian sheaves is its kernel as a morphism of presheaves.**
> The underlying presheaf of `kernel φ` is the presheaf kernel of `φ.hom`; the identification is
> compatible with the two canonical inclusions, see `kernelObjIso_hom_ι`.

```lean
noncomputable def kernelObjIso : (kernel φ).obj ≅ kernel φ.hom
```

**`Stacks.AbelianSheaves.mono_iff_presheaf_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/AbelianSheavesAbelian.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/AbelianSheavesAbelian.lean#L87). The attribute's comment: “(3) A morphism of abelian sheaves is injective in the sense of Homology, i.e. a monomorphism, exactly when it is a monomorphism of presheaves.”.

> **A morphism of abelian sheaves is a monomorphism exactly when the induced morphism of
> presheaves is one.**

```lean
theorem mono_iff_presheaf_mono : Mono φ ↔ Mono φ.hom
```

**`Stacks.AbelianSheaves.mono_iff_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/AbelianSheavesAbelian.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/AbelianSheavesAbelian.lean#L100). The attribute's comment: “(3) A morphism of abelian sheaves is injective in the sense of Homology, i.e. a monomorphism, exactly when it is injective as a map of presheaves: injective on the sections over every object of the site.”.

> **A morphism of abelian sheaves is a monomorphism exactly when it is injective on the
> sections over every object of the site**, that is, exactly when it is injective as a map of
> presheaves.

```lean
theorem mono_iff_injective : Mono φ ↔ ∀ U : Cᵒᵖ, Function.Injective (φ.hom.app U)
```

**`Stacks.AbelianSheaves.mono_iff_isLocallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/AbelianSheavesAbelian.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/AbelianSheavesAbelian.lean#L111). The attribute's comment: “(3) A morphism of abelian sheaves is injective in the sense of Homology, i.e. a monomorphism, exactly when it is injective as a map of sheaves.”.

> **A morphism of abelian sheaves is a monomorphism exactly when it is injective as a map of
> sheaves.** Injectivity of a map of sheaves is Mathlib's
> `CategoryTheory.Sheaf.IsLocallyInjective`.

```lean
theorem mono_iff_isLocallyInjective : Mono φ ↔ Sheaf.IsLocallyInjective φ
```

**`Stacks.AbelianSheaves.cokernelSheafifyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/AbelianSheavesAbelian.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/AbelianSheavesAbelian.lean#L182). The attribute's comment: “(4) The cokernel of a morphism of abelian sheaves is the sheafification of the cokernel of the induced morphism of underlying presheaves.”.

> **The cokernel of a morphism of abelian sheaves is the sheafification of its cokernel as a
> morphism of presheaves.**

```lean
noncomputable def cokernelSheafifyIso :
    (presheafToSheaf J AddCommGrpCat.{w}).obj (cokernel φ.hom) ≅ cokernel φ
```

**`Stacks.AbelianSheaves.epi_iff_isLocallySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/AbelianSheavesAbelian.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/AbelianSheavesAbelian.lean#L215). The attribute's comment: “(5) A morphism of abelian sheaves is surjective in the sense of Homology, i.e. an epimorphism, exactly when it is surjective as a map of sheaves.”.

> **A morphism of abelian sheaves is an epimorphism exactly when it is surjective as a map
> of sheaves**, i.e. locally surjective: every section of the target is, on the members of some
> covering, in the image.

```lean
theorem epi_iff_isLocallySurjective : Epi φ ↔ Sheaf.IsLocallySurjective φ
```

**`Stacks.AbelianSheaves.exact_iff_locallyLiftable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/AbelianSheavesAbelian.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/AbelianSheavesAbelian.lean#L311). The attribute's comment: “(6) A complex of abelian sheaves is exact at the middle term if and only if, for every object of the site and every section of the middle term over it mapping to zero, there is a covering of that object on which the section is in the image of the first map.”.

> **A complex of abelian sheaves is exact at its middle term exactly when the sections of
> that term killed by the second map lift locally through the first map.**

```lean
theorem exact_iff_locallyLiftable (S : ShortComplex (Sheaf J AddCommGrpCat.{w})) :
    S.Exact ↔ ∀ ⦃V : C⦄ (z : S.X₂.obj.obj (op V)), S.g.hom.app (op V) z = 0 →
      ∃ T : Sieve V, T ∈ J V ∧ ∀ ⦃W : C⦄ (p : W ⟶ V), T p →
        ∃ x : S.X₁.obj.obj (op W), S.f.hom.app (op W) x = S.X₂.obj.map p.op z
```

Declarations registered for the tag:

- [`CategoryTheory.sheafIsAbelian`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.sheafIsAbelian#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/AbelianSheavesAbelian.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/AbelianSheavesAbelian.lean#L47) (StacksFrontier): “(1) The category of abelian sheaves on a site is abelian. Mathlib proves this for sheaves valued in any abelian category admitting sheafification, by transfer along the sheafification adjunction, which is the argument of 03CN (1).”. References: SGA 4 II (6.7), “special case”; SGA 4 IV (11.1.2), “special case”; SGA 4½ Arcata (1.6.3), “more general”.

## Tag 03CO, a lemma

[Tag 03CO](https://stacks.math.columbia.edu/tag/03CO) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Sheaf.hasLimitsOfSize`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.hasLimitsOfSize#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch18.lean#L41) (StacksFrontier): “(1) limits exist”. References: EGA 0 (3.2.6), “partial”; SGA 3 IV (4.4.1), “(i)”; SGA 4 I (8.12.9), “partial”; SGA 4 II (4.1), “more general”; SGA 4 II (4.8), “more general”.
- [`CategoryTheory.Sheaf.instHasColimitsOfSize`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.instHasColimitsOfSize#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch18.lean#L42) (StacksFrontier): “(1) colimits exist”. References: SGA 3 IV (4.4.1), “(ii)”; SGA 4 II (4.1), “partial”; SGA 4 II (4.8), “more general”.
- [`CategoryTheory.Sheaf.createsLimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.createsLimits#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch18.lean#L43) (StacksFrontier): “(2) and (3): limits, finite direct sums among them, are those of presheaves”. References: EGA 0 (3.2.6), “more general”; SGA 3 IV (4.4.1), “more general”; SGA 4 II (4.1), “more general”.
- [`CategoryTheory.Sheaf.isColimitSheafifyCocone`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.isColimitSheafifyCocone#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch18.lean#L45) (StacksFrontier): “(4) a colimit is the sheafification of the presheaf colimit”. References: SGA 3 IV (4.4.1), “more general”; SGA 4 II (4.1), “partial”; SGA 4 II (5.3.1), “special case”.
- [`CategoryTheory.Sheaf.ab5ofSize`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.ab5ofSize#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch18.lean#L47) (StacksFrontier): “(5) filtered colimits are exact”. References: SGA 4 II (4.3), “more general”; SGA 4 II (6.7), “AB5, small constant ring”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.3, Tag 03CM](https://stacks.math.columbia.edu/tag/03CM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
