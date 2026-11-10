---
declaration: section
origin: cited
lean: CategoryTheory.GrothendieckTopology.Point.sheafFiberOverIso, CategoryTheory.FunctorToTypes.fromOverSubfunctor_injective, CategoryTheory.FunctorToTypes.exists_eq_fromOverSubfunctor, CategoryTheory.FunctorToTypes.fromOverSubfunctorEquiv, CategoryTheory.OverShriek.sheafFiberSigmaEquiv
statement: formalized
proof: formalized
---

# 7.35 Localization and points

Section 7.35 of the Stacks Project, [Tag 04EK](https://stacks.math.columbia.edu/tag/04EK). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04H2, a lemma

[Tag 04H2](https://stacks.math.columbia.edu/tag/04H2) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.Point.sheafFiberOverIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/LocalizedPoint.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/LocalizedPoint.lean#L107). References: SGA 4 IV (6.7), “point over (p,ξ), j\_X”; SGA 4 IV (11.3.5), “partial”.

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

**`CategoryTheory.FunctorToTypes.fromOverSubfunctor_injective`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/OverBijection.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/OverBijection.lean#L115). The attribute's comment: “injectivity of x ↦ q\_x”.

> **Stacks 04H3**, injectivity: distinct elements `x` of `u(U)` give distinct points `q_x` of
> `C/U`, because `x` is recovered from `v_x` as the unique section over the final object `U/U`.

```lean
lemma fromOverSubfunctor_injective :
    Function.Injective (fun x : F.obj X => fromOverSubfunctor F x)
```

**`CategoryTheory.FunctorToTypes.exists_eq_fromOverSubfunctor`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/OverBijection.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/OverBijection.lean#L127). The attribute's comment: “surjectivity of x ↦ q\_x, from the cartesian squares v(V/U) = u(V) ×\_\{u(U)} v(U/U)”.

> **Stacks 04H3**, surjectivity: a subfunctor of `Over.forget U ⋙ u` whose sections over the
> final object `U/U` form a singleton `{x}` and whose cartesian squares hold is `v_x`.  This is
> the last paragraph of Stacks' proof: "the top horizontal map gives a bijection
> `v(V/U) → {y ∈ u(V) | y ↦ x}`".

```lean
lemma exists_eq_fromOverSubfunctor {S : Subfunctor (Over.forget X ⋙ F)} (hS : IsFromOver F X S) :
    ∃ x : F.obj X, S = fromOverSubfunctor F x
```

**`CategoryTheory.FunctorToTypes.fromOverSubfunctorEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/OverBijection.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/OverBijection.lean#L150). The attribute's comment: “the correspondence u(U) ≃ subfunctors satisfying IsFromOver; the identification of those subfunctors with points of C/U over p is NOT proved (needs 00WJ, 00XM, 00YA)”.

> **Stacks 04H3.** The construction of Stacks 04H2 gives a one to one correspondence
> ```
>   u(U) ≃ {S : Subfunctor (Over.forget U ⋙ u) // IsFromOver u U S} ,   x ↦ v_x ,
> ```
> between the elements of `u(U)` and the subfunctors `S` of `Over.forget U ⋙ u` satisfying the two
> conditions of `IsFromOver`.
>
> WHAT THIS DOES *NOT* SAY. `IsFromOver` is the characterisation that Stacks' proof *derives* from
> `j_U ∘ q = p`; that derivation is **not** formalized here, so this equivalence is not yet an
> equivalence with "the fibre functors of the points of `C/U` lying over `p`". The missing step is
> to produce, from an isomorphism `j_U⁻¹ ⋙ q.sheafFiber ≅ p.sheafFiber` (the formalized reading of
> `j_U ∘ q = p`, cf. 04H2's `sheafFiberOverIso`), a subfunctor `S` with `IsFromOver u U S` and
> `S.toFunctor = q.fiber`. That needs exactness of sheafification (00WJ), the identification
> `(j_U⁻¹h_V)^# = j_U⁻¹(h_V^#)` (00XM) and `u(V) = p⁻¹(h_V^#)` (00YA), none of which is available in
> this repository. Until it lands, 04H3 is covered only up to that identification.

```lean
noncomputable def fromOverSubfunctorEquiv :
    F.obj X ≃ { S : Subfunctor (Over.forget X ⋙ F) // IsFromOver F X S }
```

## Tag 04H4, a lemma

[Tag 04H4](https://stacks.math.columbia.edu/tag/04H4) in the Stacks Project.

**`CategoryTheory.OverShriek.sheafFiberSigmaEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/OverShriekFiber.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/OverShriekFiber.lean#L203).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
