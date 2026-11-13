---
declaration: section
origin: cited
lean: Stacks.Examples.ProjectivityNotLocalOnBase.not_isZariskiLocalAtTarget, Stacks.Examples.ProjectivityNotLocalOnBase.not_isZariskiLocalAtTarget_and_not_isLocalAtTarget_fpqc
statement: formalized
proof: formalized
---

# 110.67 Being projective is not local on the base

Section 110.67 of the Stacks Project, [Tag 08J0](https://stacks.math.columbia.edu/tag/08J0). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08J1, a lemma

[Tag 08J1](https://stacks.math.columbia.edu/tag/08J1) in the Stacks Project.

**`Stacks.Examples.ProjectivityNotLocalOnBase.not_isZariskiLocalAtTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Examples/ProjectivityNotLocalOnBase.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Examples/ProjectivityNotLocalOnBase.lean#L290). The attribute's comment: “the tag's two assertions REDUCED TO HIRONAKA'S EXAMPLE, which is NOT proved. The witness is the named hypothesis `ProperLocallyProjectiveNotProjective` (:220) -- a proper, Zariski-locally projective, non-projective morphism -- and it carries the whole content of the tag; `hRL` and `hBCL` are the source's own Tags 07RL and 0BCL (1), also carried. What IS proved unconditionally, and is the reason the reduction is exact rather than circular: `isLocallyProjective_iff_isProjective` (:192) shows that Zariski-locality of projectivity is precisely the collapse of Tag 01W8 (1) onto Tag 01W8 (3), i.e. of `IsProjective` onto `IsLocallyProjective`, so refuting locality is exactly exhibiting a morphism separating those two notions -- nothing more is needed and nothing less suffices. The fpqc assertions follow from the Zariski ones at :293, :301, :310 via `zariskiPrecoverage_le_fpqcPrecoverage`. Of the construction, step 3 is fully proved over any domain in `Examples/HironakaConicIntersection.lean`: the two conics meet exactly in the two points `P` and `Q` (`conicIdealC_sup_conicIdealD_eq_inf`, :366) and that intersection is reduced (`isRadical_conicIdealC_sup_conicIdealD`, :372). Absent: the conics as smooth closed subschemes of `P^3`, the two iterated blow-up towers and their gluing over `Y - P - Q`, Tags 01OE and 0BCL (1) for 01W8-projectivity, and the rational equivalences on the exceptional surface. Tag 02TI, which the degree argument consumes, IS present (`Stacks.Chow.firstChernCapFactorsEverywhere_iff_killsPrincipalDivisor`)”.

> **[Stacks, Tag 08J1], granted Hironaka's example and the two comparisons of Tags 07RL and
> 0BCL.** Neither projectivity nor quasi-projectivity is Zariski local on the base.

```lean
theorem not_isZariskiLocalAtTarget (hH : ProperLocallyProjectiveNotProjective.{u})
    (hRL : ProjectiveIsQuasiProjective.{u}) (hBCL : ProperQuasiProjectiveIsProjective.{u}) :
    ¬ IsZariskiLocalAtTarget projectiveProperty.{u} ∧
      ¬ IsZariskiLocalAtTarget quasiProjectiveProperty.{u}
```

**`Stacks.Examples.ProjectivityNotLocalOnBase.not_isZariskiLocalAtTarget_and_not_isLocalAtTarget_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Examples/ProjectivityNotLocalOnBaseUnconditional.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Examples/ProjectivityNotLocalOnBaseUnconditional.lean#L132).

> The properties "`f` is projective" and "`f` is quasi-projective" are not Zariski local on
> the base; a fortiori, they are not fpqc local on the base.
>
> The witness is Hironaka's example,
> `Stacks.Examples.ProjectivityNotLocalOnBase.properLocallyProjectiveNotProjective`.

```lean
theorem not_isZariskiLocalAtTarget_and_not_isLocalAtTarget_fpqc :
    (¬ IsZariskiLocalAtTarget projectiveProperty.{u} ∧
      ¬ IsZariskiLocalAtTarget quasiProjectiveProperty.{u}) ∧
    (¬ projectiveProperty.{u}.IsLocalAtTarget Scheme.fpqcPrecoverage ∧
      ¬ quasiProjectiveProperty.{u}.IsLocalAtTarget Scheme.fpqcPrecoverage)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.67, Tag 08J0](https://stacks.math.columbia.edu/tag/08J0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
