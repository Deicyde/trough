---
declaration: section
origin: cited
lean: Stacks.Models.nonempty_tensorPower_gcd_iso_unit_of_componentDegree_eq_zero, Stacks.Models.RegularProperModelSituation.picardNumericalTypeHom_spec, Stacks.Models.RegularProperModelSituation.picardTorsionSequence_exact, Stacks.Models.injOn_schemePullbackClass_specialFiberRedι_zsmulTorsion
statement: formalized
proof: formalized
---

# 55.13 Picard groups of models

Section 55.13 of the Stacks Project, [Tag 0CAA](https://stacks.math.columbia.edu/tag/0CAA). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CAB, a lemma

[Tag 0CAB](https://stacks.math.columbia.edu/tag/0CAB) in the Stacks Project.

**`Stacks.Models.nonempty_tensorPower_gcd_iso_unit_of_componentDegree_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/TrivialTensorPower.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/TrivialTensorPower.lean#L359). The attribute's comment: “at the irreducible components of the special fibre: an invertible module trivial on the generic fibre C and of degree zero on every component has trivial d-th tensor power, for d the greatest common divisor of the multiplicities”.

> **Stacks Project, Tag 0CAB.** Let `X ⟶ Spec(R)` be a regular proper model of a smooth
> projective curve `C` over the fraction field of a discrete valuation ring, write the special fibre
> as `X_k = Σ m_Z C_Z` over its irreducible components and put `d = gcd(m_Z)`. An invertible
> `𝒪_X`-module `ℒ` whose restriction to the generic fibre `C` is trivial and which has degree `0` on
> every component of the special fibre satisfies `ℒ^{⊗d} ≅ 𝒪_X`.
>
> Both hypotheses are the tag's own. Triviality on `C` is the vanishing of the class of `ℒ` in
> `Pic(C)`, and exactness of the sequence `0 ⟶ ℤ ⟶ ℤ^{⊕n} ⟶ Pic(X) ⟶ Pic(C) ⟶ 0` at `Pic(X)`,
> [Stacks, Tag 0C63], writes the class of `ℒ` as a combination `Σ a_Z[𝒪_X(C_Z)]`. The vanishing of
> the degrees then makes `(a_Z)` a rational multiple `q(m_Z)` by part (4) of [Stacks, Tag 0C66]. The
> greatest common divisor of the `m_Z` is an integral combination of them, so `dq` is an integer and
> `d · Σ a_Z[𝒪_X(C_Z)]` is an integral multiple of `Σ m_Z[𝒪_X(C_Z)]`, which vanishes because
> `Σ m_Z C_Z` is the special fibre and its invertible module is trivial.

```lean
theorem nonempty_tensorPower_gcd_iso_unit_of_componentDegree_eq_zero
    (L : SheafOfModules.{u} (Stacks.SheafOfModules.TensorSheafification.structureSheaf
      S.X.presheaf (structureIsSheaf S.X.toRingedSpace)))
    (hL : IsInvertible S.X.presheaf (structureIsSheaf S.X.toRingedSpace) L)
    (hgen : genericFiberPicardRestriction S
      (picardClass S.X.presheaf (structureIsSheaf S.X.toRingedSpace) L hL) = 0)
    (hdeg : ∀ Z, S.specialFiberComponentDegree Z L hL = 0) :
    Nonempty (tensorPower S.X.presheaf (structureIsSheaf S.X.toRingedSpace) L
        ((Finset.univ.gcd S.specialFiberMultiplicity : ℕ) : ℤ) ≅
      _root_.SheafOfModules.unit (Stacks.SheafOfModules.TensorSheafification.structureSheaf
        S.X.presheaf (structureIsSheaf S.X.toRingedSpace)))
```

## Tag 0CAC, a lemma

[Tag 0CAC](https://stacks.math.columbia.edu/tag/0CAC) in the Stacks Project.

**`Stacks.Models.RegularProperModelSituation.picardNumericalTypeHom_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ModelPicardNumericalType.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/ModelPicardNumericalType.lean#L284). The attribute's comment: “the canonical map Pic(C) -> Pic(T) and its kernel”.

> **Stacks Project, Tag 0CAC.** In the situation of [Stacks, Tag 0C61] let `T` be the
> numerical type associated to `X` ([Stacks, Tag 0CA5]). The canonical map
> `Stacks.Models.RegularProperModelSituation.picardNumericalTypeHom : Pic(C) ⟶ Pic(T)` sends the
> restriction of the class of an invertible module `ℒ` on `X` to the class of
> `(deg(ℒ|_{C₁})/w₁, …, deg(ℒ|_{Cₙ})/wₙ)`, and its kernel is exactly the classes of the invertible
> modules on `C` that are restrictions of invertible modules `ℒ` on `X` with
> `deg_{Cᵢ}(ℒ|_{Cᵢ}) = 0` for every `i`.

```lean
theorem picardNumericalTypeHom_spec :
    (∀ (L : S.X.Modules) (hL : Stacks.SheafOfModules.IsInvertible S.X.presheaf
        (structureSheafRing S.X.toRingedSpace).property L),
      S.picardNumericalTypeHom n e (genericFiberPicardRestriction S
          (Stacks.SheafOfModules.picardClass S.X.presheaf
            (Stacks.RingedSpace.structureIsSheaf S.X.toRingedSpace) L hL)) =
        Submodule.Quotient.mk (fun i =>
          S.specialFiberComponentDegree (S.associatedEnumeration n e i) L hL /
            (S.specialFiberComponentWeight (S.associatedEnumeration n e i) : ℤ))) ∧
    ∀ y : ofScheme S.C, S.picardNumericalTypeHom n e y = 0 ↔
      ∃ (L : S.X.Modules) (hL : Stacks.SheafOfModules.IsInvertible S.X.presheaf
          (structureSheafRing S.X.toRingedSpace).property L),
        genericFiberPicardRestriction S
            (Stacks.SheafOfModules.picardClass S.X.presheaf
              (Stacks.RingedSpace.structureIsSheaf S.X.toRingedSpace) L hL) = y ∧
          ∀ Z, S.specialFiberComponentDegree Z L hL = 0
```

## Tag 0CAD, a lemma

[Tag 0CAD](https://stacks.math.columbia.edu/tag/0CAD) in the Stacks Project.

**`Stacks.Models.RegularProperModelSituation.picardTorsionSequence_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/PicardTorsionSequence.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/PicardTorsionSequence.lean#L329). The attribute's comment: “the exact sequence 0 -> Pic(X)[h] -> Pic(C)[h] -> Pic(T)[h] for h prime to d = gcd(m_i), with T the numerical type associated to X”.

> **Stacks Project, Tag 0CAD.** In the situation of [Stacks, Tag 0C61] let
> `d = gcd(m₁, …, mₙ)` for the multiplicities `mᵢ` of the irreducible components of the special
> fibre, let `T` be the numerical type associated to `X` (through an enumeration `e` of the
> components), and let `h ≥ 1` be prime to `d`. Then
>
> `0 ⟶ Pic(X)[h] ⟶ Pic(C)[h] ⟶ Pic(T)[h]`
>
> is exact, where the first map is restriction to the generic fibre and the second is the
> canonical map of [Stacks, Tag 0CAC]: the first map is injective and the kernel of the second is
> the image of the first.

```lean
theorem picardTorsionSequence_exact (n : ℕ) (e : Fin n ≃ irreducibleComponents S.specialFiber)
    {h : ℕ} (hh : 1 ≤ h) (hcop : Nat.Coprime h (Finset.univ.gcd S.specialFiberMultiplicity)) :
    Function.Injective (S.picardTorsionRestriction (h : ℤ)) ∧
      Function.Exact (S.picardTorsionRestriction (h : ℤ))
        (S.picardTorsionToNumericalType n e (h : ℤ))
```

## Tag 0CAE, a lemma

[Tag 0CAE](https://stacks.math.columbia.edu/tag/0CAE) in the Stacks Project.

**`Stacks.Models.injOn_schemePullbackClass_specialFiberRedι_zsmulTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/PicardTorsionInjective.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/PicardTorsionInjective.lean#L406). The attribute's comment: “restriction Pic(X)[h] → Pic((X_k)_red)[h] is injective for h prime to the characteristic of k”.

> **Stacks Project, Tag 0CAE.** In Situation 0C61, let `h` be an integer prime to the
> characteristic of the residue field `k`. Then restriction of invertible modules
> `Pic(X)[h] ⟶ Pic((X_k)_red)[h]` is injective.
>
> The proof is the source's. For every truncation `X_n = X ×_{Spec R} Spec(R/π^{n+1})` the reduced
> special fibre `(X_k)_red ⟶ X_n` is a thickening, and restriction is injective on `h`-torsion along
> it by [Stacks, Tag 0C6S]: the units condition of that tag holds because the global functions on
> `(X_k)_red` form a field purely inseparable over `k`, the special fibre being geometrically
> connected. So an `h`-torsion class trivial on `(X_k)_red` is trivial on every `X_n`, and then
> trivial on `X` by the theorem on formal functions and the properness of `X ⟶ Spec(R)`.

```lean
theorem injOn_schemePullbackClass_specialFiberRedι_zsmulTorsion
    (S : RegularProperModelSituation.{u}) {h : ℤ} (hh : IsUnit ((h : ℤ) : S.k)) :
    Set.InjOn (schemePullbackClass S.specialFiberRedι) (zsmulTorsion (ofScheme S.X) h)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 55.13, Tag 0CAA](https://stacks.math.columbia.edu/tag/0CAA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
