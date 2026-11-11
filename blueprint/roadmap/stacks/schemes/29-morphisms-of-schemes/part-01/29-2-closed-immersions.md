---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.ClosedImmersionTFAE.closedImmersion_tfae, AlgebraicGeometry.IsClosedImmersion.lift, AlgebraicGeometry.IsClosedImmersion.lift_fac, AlgebraicGeometry.Scheme.Hom.le_ker_comp, AlgebraicGeometry.IsClosedImmersion.of_comp_isClosedImmersion, AlgebraicGeometry.IsClosedImmersion.isIso_lift, AlgebraicGeometry.IsClosedImmersion.isIso_of_ker_eq, AlgebraicGeometry.Scheme.Hom.ker_comp_of_isIso
statement: formalized
proof: formalized
---

# 29.2 Closed immersions

Section 29.2 of the Stacks Project, [Tag 01QN](https://stacks.math.columbia.edu/tag/01QN). 7 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 12 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01QO, a lemma

[Tag 01QO](https://stacks.math.columbia.edu/tag/01QO) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ClosedImmersionTFAE.closedImmersion_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedImmersionTFAE/Basic.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ClosedImmersionTFAE/Basic.lean#L163). References: EGA I (4.2.2), “(b) closed case”.

> The six equivalent descriptions of a closed immersion of schemes.

```lean
theorem closedImmersion_tfae {Z X : Scheme.{u}} (i : Z ⟶ X) :
    List.TFAE [
      IsClosedImmersion i,
      ∀ (U : X.Opens) (hU : IsAffineOpen U), IsQuotientOverAffineOpen i U hU,
      ∃ (𝒰 : Scheme.AffineOpenCover.{u} X), ∀ j : 𝒰.I₀,
        IsQuotientOverAffineOpen i (𝒰.f j).opensRange
          (isAffineOpen_opensRange (𝒰.f j)),
      Topology.IsClosedEmbedding i.base ∧
        Epi (SheafOfModules.unitToPushforwardObjUnit (structureSheafHom i.toLRSHom.toShHom)),
      (Topology.IsClosedEmbedding i.base ∧
        Epi (SheafOfModules.unitToPushforwardObjUnit (structureSheafHom i.toLRSHom.toShHom))) ∧
        (Stacks.ClosedImmersion.idealSheaf i.toLRSHom.toShHom).IsQuasicoherent,
      Stacks.ClosedImmersion.IsClosedImmersion i.toLRSHom.toShHom]
```

## Tag 01QP, a lemma

[Tag 01QP](https://stacks.math.columbia.edu/tag/01QP) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsClosedImmersion.lift`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsClosedImmersion.lift#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L196) (StacksFrontier): “part (1), `⇐`: the factorization `Z ⟶ Z'` when `I' ≤ I`”.
- [`AlgebraicGeometry.IsClosedImmersion.lift_fac`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsClosedImmersion.lift_fac#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L198) (StacksFrontier): “part (1), `⇐`: the lift factors `i` through `i'`”.
- [`AlgebraicGeometry.Scheme.Hom.le_ker_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.le_ker_comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L200) (StacksFrontier): “part (1), `⇒`: a factorization through `i'` forces `I' ≤ I`”.
- [`AlgebraicGeometry.IsClosedImmersion.of_comp_isClosedImmersion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsClosedImmersion.of_comp_isClosedImmersion#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L202) (StacksFrontier): “part (1), the factor `a` is a closed immersion”. References: EGA I (5.4.4), “special case”; EGA I (5.5.12), “(v), special case”.
- [`AlgebraicGeometry.IsClosedImmersion.isIso_lift`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsClosedImmersion.isIso_lift#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L204) (StacksFrontier): “part (2), `⇐`: equal ideal sheaves give an isomorphism over `X`”.
- [`AlgebraicGeometry.IsClosedImmersion.isIso_of_ker_eq`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsClosedImmersion.isIso_of_ker_eq#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L206) (StacksFrontier): “part (2), `⇐`: a map over `X` between equal ideal sheaves is an isomorphism”.
- [`AlgebraicGeometry.Scheme.Hom.ker_comp_of_isIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.ker_comp_of_isIso#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L208) (StacksFrontier): “part (2), `⇒`: an isomorphism over `X` preserves the ideal sheaf”.
- [`AlgebraicGeometry.IsClosedImmersion.overEquivIdealSheafData`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsClosedImmersion.overEquivIdealSheafData#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L210) (StacksFrontier): “closed subschemes of `X` are anti-equivalent to ideal sheaves”. References: EGA II (8.13.4), “partial”.

## Tag 01QQ, a lemma

[Tag 01QQ](https://stacks.math.columbia.edu/tag/01QQ) in the Stacks Project.

**`Stacks.Divisors.exists_isClosedImmersion_ker_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/QuasicoherentIdealSheafData/Basic.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/QuasicoherentIdealSheafData/Basic.lean#L165). The attribute's comment: “(2) implies (3), with the equality Ker(i^♯) = J recorded over affine opens only”.

> **Stacks Project, Tag 01QQ, the implication (2) ⇒ (3).** A quasi-coherent sheaf of ideals
> `J ⊆ 𝒪_X` on a scheme is the sheaf of ideals of a closed immersion of schemes: the closed
> subscheme cut out by `Stacks.Divisors.idealSheafDataOfSubmodule` has, on every affine open, kernel
> exactly `J`.
>
> The two remaining implications are proved in
> `StacksFrontier/AlgebraicGeometry/Divisors/QuasicoherentIdealSheafData/Equivalence.lean`, where
> `Stacks.Divisors.isQuasicoherent_ideal_tfae` assembles the whole tag: (1) ⇔ (2) is
> `Stacks.ClosedImmersion.isQuasicoherent_iff_localGenerators`, the sheaf-of-ideals half of Stacks
> Tag 01IN, and (3) ⇒ (2) is `Stacks.Divisors.isQuasicoherent_of_ker_app_eq`. Note that the latter
> is *not* just quasi-coherence of the kernel of a closed immersion, the other half of Tag 01IN:
> that statement is about the categorical kernel of `𝒪_X ⟶ i_* 𝒪_Z`, and the step it leaves open is
> the identification of a submodule `J` whose sections agree with the kernel's *with* that kernel.
>
> The equality of ideals below is recorded over affine opens only;
> `Stacks.Divisors.subschemeι_app_eq_zero_iff_mem_of_isQuasicoherent` upgrades it to every open,
> which is what the statement `Ker(i^♯) = 𝓘` of the tag asks for.

```lean
theorem exists_isClosedImmersion_ker_eq :
    ∃ (Z : Scheme.{u}) (i : Z ⟶ X), IsClosedImmersion i ∧
      ∀ U : X.affineOpens, RingHom.ker (i.app U.1).hom = J.obj (op U.1)
```

**`Stacks.Divisors.isQuasicoherent_ideal_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/QuasicoherentIdealSheafData/Equivalence.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/QuasicoherentIdealSheafData/Equivalence.lean#L124). The attribute's comment: “the full equivalence: (1) locally generated by sections, (2) quasi-coherent, (3) the kernel of a closed immersion of schemes”.

> For a sheaf of ideals `J ⊆ 𝒪_X` on a scheme the following are
> equivalent: `J` is locally generated by sections as a sheaf of `𝒪_X`-modules; `J` is
> quasi-coherent; and there is a closed immersion of schemes `i : Z ⟶ X` whose ideal sheaf
> `Ker(i^♯)` is `J`, in the sense that over every open the kernel of `i.app` is the ideal that `J`
> cuts out there.

```lean
theorem isQuasicoherent_ideal_tfae (J : (SheafOfModules.unit X.ringCatSheaf).Submodule) :
    List.TFAE [
      Nonempty (SheafOfModules.LocalGeneratorsData.{u} J.toSheafOfModules),
      (J.toSheafOfModules : X.Modules).IsQuasicoherent,
      ∃ (Z : Scheme.{u}) (i : Z ⟶ X), IsClosedImmersion i ∧
        ∀ V : X.Opens, RingHom.ker (i.app V).hom = J.obj (op V)]
```

## Tag 01QR, a lemma

[Tag 01QR](https://stacks.math.columbia.edu/tag/01QR) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsClosedImmersion.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsClosedImmersion.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L212) (StacksFrontier): “closed immersions are stable under base change”. References: EGA I (10.14.5), “(ii), ordinary schemes”; EGA I (4.3.1), “special case”; EGA I (4.3.2); EGA I (4.5.5), “(iii), special case”; EGA II (8.10.2), “j′ is a closed immersion”; EGA IV (17.13.1), “closed immersions”; EGA IV (2.7.1), “implication”; EGA IV (8.6.2), “more general”; SGA 1 VIII (5.5), “closed-immersion clause”; SGA 3 VIB (10.1), “partial”; SGA 4 XII (4.3), “Parenthetical clause”.

## Tag 01QS, a lemma

[Tag 01QS](https://stacks.math.columbia.edu/tag/01QS) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsClosedImmersion.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsClosedImmersion.comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L214) (StacksFrontier): “the composition”. References: EGA I (10.14.5), “(i), ordinary schemes”; EGA I (4.1.6); EGA I (4.2.5); EGA I (4.5.5), “(i), special case”.

## Tag 01QT, a lemma

[Tag 01QT](https://stacks.math.columbia.edu/tag/01QT) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsClosedImmersion.instIsAffineHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsClosedImmersion.instIsAffineHom#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L215) (StacksFrontier): “first step: a closed immersion is affine”. References: EGA I (4.2.3), “more general”; EGA II (1.2.2); EGA II (1.6.2); SGA 3 VIB (2.9.1), “special case”; SGA 3 XXV (4.3), “partial”.
- [`AlgebraicGeometry.instQuasiCompactOfIsAffineHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instQuasiCompactOfIsAffineHom#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L217) (StacksFrontier): “second step: an affine morphism is quasi-compact”. References: SGA 3 VIA (4.6), “partial”.

## Tag 01QU, a lemma

[Tag 01QU](https://stacks.math.columbia.edu/tag/01QU) in the Stacks Project.

**`AlgebraicGeometry.IsClosedImmersion.isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/ClosedImmersionSeparated.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/ClosedImmersionSeparated.lean#L33).

> A closed immersion of schemes is separated.

```lean
theorem IsClosedImmersion.isSeparated {X Y : Scheme.{u}} (f : X ⟶ Y) [IsClosedImmersion f] :
    IsSeparated f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.2, Tag 01QN](https://stacks.math.columbia.edu/tag/01QN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
