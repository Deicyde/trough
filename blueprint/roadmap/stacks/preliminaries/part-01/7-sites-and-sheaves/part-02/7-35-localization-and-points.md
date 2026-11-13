---
declaration: section
origin: cited
lean: CategoryTheory.GrothendieckTopology.Point.sheafFiberOverIso, CategoryTheory.GrothendieckTopology.Point.OverPoint.existsUnique_nonempty_iso_ofFiber, CategoryTheory.GrothendieckTopology.Point.OverPoint.fiberEquivOverPoint, CategoryTheory.OverShriek.sheafFiberSigmaEquiv
statement: formalized
proof: formalized
---

# 7.35 Localization and points

Section 7.35 of the Stacks Project, [Tag 04EK](https://stacks.math.columbia.edu/tag/04EK). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04H2, a lemma

[Tag 04H2](https://stacks.math.columbia.edu/tag/04H2) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.Point.sheafFiberOverIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/LocalizedPoint.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/LocalizedPoint.lean#L107). References: SGA 4 IV (6.7), “point over (p,ξ), j\_X”; SGA 4 IV (11.3.5), “partial”.

> **Stacks 04H2.** The point `q = Φ.over x` of the localized site `C/U` lies above the point
> `Φ` of `C`: for every sheaf `F` on `C` the stalk of `F` at `Φ` agrees with the stalk of its
> restriction `j_U⁻¹F = F.over U` at `q`.  In other words the triangle formed by `q`, `Φ` and the
> localization morphism `j_U : Sh(C/U) ⟶ Sh(C)` commutes.

```lean
noncomputable def sheafFiberOverIso :
    J.overPullback A X ⋙ (Φ.over x).sheafFiber ≅ Φ.sheafFiber
```

## Tag 04H3, a lemma

[Tag 04H3](https://stacks.math.columbia.edu/tag/04H3) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.Point.OverPoint.existsUnique_nonempty_iso_ofFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/OverPoint.lean, line 483](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/OverPoint.lean#L483).

> **Stacks 04H3.** Let `p` be a point of the site `C` with fibre functor `u`, and `U` an object
> of `C`.  Every point `q` of `C/U` lying over `p` (a point of `C/U` with an identification
> `j_U ∘ q = p`) is isomorphic over `p` to the point `q_x` of Stacks 04H2 for exactly one
> `x ∈ u(U)`.

```lean
theorem existsUnique_nonempty_iso_ofFiber (q : OverPoint Φ U) :
    ∃! x : Φ.fiber.obj U, Nonempty (q ≅ ofFiber x)
```

**`CategoryTheory.GrothendieckTopology.Point.OverPoint.fiberEquivOverPoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/OverPoint.lean, line 493](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/OverPoint.lean#L493).

> **Stacks 04H3.** Let `p` be a point of the site `C` with fibre functor `u`, and `U` an object
> of `C`.  The construction `x ↦ q_x` of Stacks 04H2 is a one to one correspondence between the
> elements `x ∈ u(U)` and the points `q` of `C/U` lying over `p`, up to isomorphism of points over
> `p`.

```lean
noncomputable def fiberEquivOverPoint :
    Φ.fiber.obj U ≃ _root_.Quotient (isIsomorphicSetoid (OverPoint Φ U))
```

## Tag 04H4, a lemma

[Tag 04H4](https://stacks.math.columbia.edu/tag/04H4) in the Stacks Project.

**`CategoryTheory.OverShriek.sheafFiberSigmaEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/OverShriekFiber.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/OverShriekFiber.lean#L203).

> **Stacks 04H4.** Let `C` be a site, `p` a point of `C` given by `u : C ⥤ Set`, and `U` an
> object of `C`.  For any sheaf `F` on `C/U`,
> ```
>   (j_{U!}F)_p = ∐_x F_{q_x} ,
> ```
> the coproduct being over the points `q_x` of `C/U` attached to the elements `x` of `u(U)` as in
> Stacks 04H2.
>
> Here `j_{U!}` is `(Over.forget U).sheafPullback`, the left adjoint of the restriction
> `j_U⁻¹ = GrothendieckTopology.overPullback`, and the coproduct is the sigma type, which is the
> coproduct in `Type v`.  The proof combines the presheaf-level statement
> `presheafFiberSigmaEquiv` with Stacks 03CD (`OverShriek.sheafifyIso`: `j_{U!}` of a sheafification
> is the sheafification of the coproduct presheaf) and Stacks 00Y8 (`Point.presheafFiber` and
> `Point.sheafFiber` agree across sheafification).

```lean
def sheafFiberSigmaEquiv (F : Sheaf (J.over U) (Type v)) :
    (Σ x : Φ.fiber.obj U, (Φ.over x).sheafFiber.obj F) ≃
      Φ.sheafFiber.obj (((Over.forget U).sheafPullback (Type v) (J.over U) J).obj F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.35, Tag 04EK](https://stacks.math.columbia.edu/tag/04EK)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
