---
declaration: section
origin: cited
lean: PseudoTorsor, PseudoTorsor.Hom, PseudoTorsor.IsTorsor, trivialTorsor, trivialTorsor_isTorsor, isTrivial_iff_nonempty_globalSections, Stacks.Cohomology.Torsors.torsorIsoClassesEquivH1, Stacks.Cohomology.Torsors.torsorIsoClassesEquivH1_eq_boundary_iff
statement: formalized
proof: formalized
---

# 21.4 First cohomology and torsors

Section 21.4 of the Stacks Project, [Tag 03AG](https://stacks.math.columbia.edu/tag/03AG). 3 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03AH, a definition

[Tag 03AH](https://stacks.math.columbia.edu/tag/03AH) in the Stacks Project.

Declarations registered for the tag:

- [`PseudoTorsor`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/TrivialityAndGlobalSections.lean#L72), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/PseudoTorsors.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/PseudoTorsors.lean#L50) (StacksFrontier): “pseudo-torsor”.
- [`PseudoTorsor.Hom`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/TrivialityAndGlobalSections.lean#L97), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/PseudoTorsors.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/PseudoTorsors.lean#L51) (StacksFrontier): “morphism of pseudo-torsors”.
- [`PseudoTorsor.IsTorsor`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/TrivialityAndGlobalSections.lean#L118), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/PseudoTorsors.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/PseudoTorsors.lean#L52) (StacksFrontier): “torsor”.
- [`trivialTorsor`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/TrivialityAndGlobalSections.lean#L124), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/PseudoTorsors.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/PseudoTorsors.lean#L53) (StacksFrontier): “trivial torsor”.
- [`trivialTorsor_isTorsor`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/TrivialityAndGlobalSections.lean#L135), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/PseudoTorsors.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/PseudoTorsors.lean#L54) (StacksFrontier): “the trivial torsor is a torsor”.

## Tag 03AI, a lemma

[Tag 03AI](https://stacks.math.columbia.edu/tag/03AI) in the Stacks Project.

**`isTrivial_iff_nonempty_globalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/TrivialityAndGlobalSections.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/TrivialityAndGlobalSections.lean#L237). References: SGA 3 IV (5.1.4), “partial”; SGA 3 IV (5.1.5), “(ii)”.

> Let `G` be a sheaf of (possibly non-commutative) groups on a site `C` and `F` a `G`-torsor.
> Then `F` is trivial if and only if it has a global section, i.e. `Γ(C, F)` is nonempty
> (Stacks, Tag 03AI, Lemma 21.4.2).

```lean
theorem isTrivial_iff_nonempty_globalSections
    (F : PseudoTorsor (C := C) G) (hF : F.IsTorsor) :
    F.IsTrivial ↔ Nonempty (GlobalSections F.presheaf)
```

## Tag 03AJ, a lemma

[Tag 03AJ](https://stacks.math.columbia.edu/tag/03AJ) in the Stacks Project.

**`Stacks.Cohomology.Torsors.torsorIsoClassesEquivH1`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/FirstCohomology/EquivH1.lean, line 365](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/FirstCohomology/EquivH1.lean#L365). The attribute's comment: “the canonical bijection”. References: EGA IV (16.5.15), “abelian sheaf of groups”; SGA 4½ Cycle (1.1.1), “the bijection”; SGA 4½ Arcata (2.2.1), “H^1 = torsor classes”; SGA 4½ Cycle (1.1), “H^1 ≅ torsor classes”; SGA 4½ Arcata (1.6.6), “H¹ = torsor classes”.

> **Stacks Project, Tag 03AJ.** Isomorphism classes of torsors under an
> abelian sheaf are canonically in bijection with its first cohomology group.

```lean
public noncomputable def torsorIsoClassesEquivH1
    (H : Sheaf J AddCommGrpCat.{t}) :
    torsorIsoClasses H ≃ Sheaf.H H 1
```

**`Stacks.Cohomology.Torsors.torsorIsoClassesEquivH1_eq_boundary_iff`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/FirstCohomology/EquivH1.lean, line 377](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/FirstCohomology/EquivH1.lean#L377). The attribute's comment: “characterization by the boundary map and fiber torsor”. References: SGA 4½ Cycle (1.1.1), “normalization by ∂h”.

> The class of a torsor is the boundary of a global section precisely when
> the torsor is equivariantly isomorphic to its fiber in the middle sheaf of
> the short exact sequence. The embedding is required to be injective on
> sections and to have exactly that fiber as its image.

```lean
public lemma torsorIsoClassesEquivH1_eq_boundary_iff
    (S : ShortComplex (Sheaf J AddCommGrpCat.{t})) (hS : S.ShortExact)
    (q : (Functor.const Cᵒᵖ).obj (AddCommGrpCat.of (ULift.{t} ℤ)) ⟶ S.X₃.obj)
    (F : AbelianTorsor S.X₁) :
    torsorIsoClassesEquivH1 S.X₁ (Quotient.mk (torsorSetoid S.X₁) F) =
        (Abelian.Ext.mk₀ (((sheafificationAdjunction J AddCommGrpCat).homEquiv _ _).symm q)).comp
          hS.extClass (zero_add 1) ↔
      ∃ i : F.1.presheaf ⟶ S.X₂.obj ⋙ forget AddCommGrpCat,
        (∀ (U : Cᵒᵖ) (h : S.X₁.obj.obj U) (s : F.1.presheaf.obj U),
          let iU : F.1.presheaf.obj U → S.X₂.obj.obj U := i.app U
          iU (F.1.act U (Multiplicative.ofAdd h) s) = S.f.hom.app U h + iU s) ∧
        (∀ U : Cᵒᵖ, Function.Injective (i.app U)) ∧
        (∀ (U : Cᵒᵖ) (x : S.X₂.obj.obj U),
          S.g.hom.app U x = q.app U ⟨1⟩ ↔ ∃ s, i.app U s = x)
```

**`Stacks.Cohomology.Torsors.torsorIsoClassesEquivH1_trivial`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/FirstCohomology/EquivH1.lean, line 400](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/FirstCohomology/EquivH1.lean#L400). The attribute's comment: “normalization at the trivial torsor”.

> The trivial torsor corresponds to zero in first cohomology.

```lean
public lemma torsorIsoClassesEquivH1_trivial (H : Sheaf J AddCommGrpCat.{t}) :
    torsorIsoClassesEquivH1 H
      (Quotient.mk (torsorSetoid H)
        ⟨trivialTorsor (abelianSheafAsGroupSheaf H),
          trivialTorsor_isTorsor (abelianSheafAsGroupSheaf H)⟩) = 0
```

**`Stacks.Cohomology.Torsors.torsorIsoClassesEquivH1_naturality`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/FirstCohomology/EquivH1.lean, line 561](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/FirstCohomology/EquivH1.lean#L561). The attribute's comment: “naturality in the coefficient sheaf”.

```lean
public lemma torsorIsoClassesEquivH1_naturality
    {H H' : Sheaf J AddCommGrpCat.{t}} (φ : H ⟶ H')
    (F : AbelianTorsor H) (F' : AbelianTorsor H')
    (f : F.1.presheaf ⟶ F'.1.presheaf)
    (hf : ∀ (U : Cᵒᵖ) (h : H.obj.obj U) (s : F.1.presheaf.obj U),
      f.app U (F.1.act U (Multiplicative.ofAdd h) s) =
        F'.1.act U (Multiplicative.ofAdd (φ.hom.app U h)) (f.app U s)) :
    Sheaf.H.map φ 1 (torsorIsoClassesEquivH1 H (Quotient.mk (torsorSetoid H) F)) =
      torsorIsoClassesEquivH1 H' (Quotient.mk (torsorSetoid H') F')
```

**`Stacks.Cohomology.Torsors.instAddCommGroupTorsorIsoClasses`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/TorsorClassGroup.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/TorsorClassGroup.lean#L72). The attribute's comment: “the abelian-group structure on the isomorphism classes of torsors, with addition the contracted product and zero the trivial torsor”.

> **The isomorphism classes of torsors under an abelian sheaf form an abelian group.**  The
> addition is the contracted product and the zero is the trivial torsor, by
> `Stacks.Cohomology.Torsors.torsorIsoClasses_mk_add_of_equivariant` and
> `Stacks.Cohomology.Torsors.torsorIsoClasses_trivial_eq_zero`; the group laws themselves are
> those of `Ext¹`, carried across the bijection of Tag 03AJ.

```lean
public instance instAddCommGroupTorsorIsoClasses (H : Sheaf J AddCommGrpCat.{t}) :
    AddCommGroup (torsorIsoClasses H)
```

**`Stacks.Cohomology.Torsors.torsorIsoClassesAddEquivH1`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/TorsorClassGroup.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/TorsorClassGroup.lean#L82). The attribute's comment: “the canonical bijection as a group isomorphism, for the contracted product of torsors”. References: SGA 4½ Cycle (1.1.1), “as a group map”.

> **Stacks Project, Tag 03AJ as an isomorphism of abelian groups.**  The canonical bijection
> between the isomorphism classes of torsors under an abelian sheaf and its first cohomology group
> carries the contracted product of torsors to the addition of `Ext¹`.

```lean
public def torsorIsoClassesAddEquivH1 (H : Sheaf J AddCommGrpCat.{t}) :
    torsorIsoClasses H ≃+ Sheaf.H H 1
```

**`Stacks.Cohomology.Torsors.torsorIsoClasses_trivial_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/TorsorClassGroup.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/TorsorClassGroup.lean#L100). The attribute's comment: “the zero of the group of torsor classes is the trivial torsor”.

> **The zero of the group of torsor classes is the class of the trivial torsor.**  One of the
> two laws pinning the group structure of
> `Stacks.Cohomology.Torsors.instAddCommGroupTorsorIsoClasses`.

```lean
public theorem torsorIsoClasses_trivial_eq_zero (H : Sheaf J AddCommGrpCat.{t}) :
    (by exact (Quotient.mk (torsorSetoid H)
        ⟨trivialTorsor (abelianSheafAsGroupSheaf H),
          trivialTorsor_isTorsor (abelianSheafAsGroupSheaf H)⟩) : torsorIsoClasses H) = 0
```

**`Stacks.Cohomology.Torsors.torsorIsoClasses_mk_add_of_equivariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/TorsorClassGroup.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/TorsorClassGroup.lean#L116). The attribute's comment: “the addition of torsor classes is the contracted product of torsors”. References: SGA 4 XVIII (1.3.3), “partial”; SGA 4½ Sommes trig (1.3), “partial”.

> **The sum of two torsor classes is the class of their contracted product.**  A torsor `T`
> receiving a morphism out of the product of the presheaves of `F` and `G` which adds the two
> acting sections is precisely a torsor identified with the contracted product `F ∧_H G`, and its
> class is the sum of the two classes.  This is the second of the two laws pinning the group
> structure of `Stacks.Cohomology.Torsors.instAddCommGroupTorsorIsoClasses`, and together with
> `Stacks.Cohomology.Torsors.torsorIsoClasses_trivial_eq_zero` it determines the addition.

```lean
public theorem torsorIsoClasses_mk_add_of_equivariant (H : Sheaf J AddCommGrpCat.{t})
    (F G T : AbelianTorsor H)
    (f : Generators.productPresheaf' F.1.presheaf G.1.presheaf ⟶ T.1.presheaf)
    (hf : ∀ (U : Cᵒᵖ) (a b : H.obj.obj U) (s : F.1.presheaf.obj U) (t : G.1.presheaf.obj U),
      f.app U (F.1.act U (Multiplicative.ofAdd a) s,
          G.1.act U (Multiplicative.ofAdd b) t) =
        T.1.act U (Multiplicative.ofAdd (a + b)) (f.app U (s, t))) :
    (by exact Quotient.mk (torsorSetoid H) F : torsorIsoClasses H) +
        (by exact Quotient.mk (torsorSetoid H) G : torsorIsoClasses H) =
      Quotient.mk (torsorSetoid H) T
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.4, Tag 03AG](https://stacks.math.columbia.edu/tag/03AG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
