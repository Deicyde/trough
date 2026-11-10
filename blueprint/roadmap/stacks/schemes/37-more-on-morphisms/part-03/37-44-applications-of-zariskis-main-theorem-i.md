---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsFinite.tfae_isProper_locallyQuasiFinite, AlgebraicGeometry.isFinite_iff_isProper_and_forall_finite_preimage_singleton, AlgebraicGeometry.isFinite_iff_isSeparated_universallyClosed_locallyOfFiniteType_and_finite_fibres
statement: formalized
proof: formalized
---

# 37.44 Applications of Zariski's Main Theorem, I

Section 37.44 of the Stacks Project, [Tag 0F2P](https://stacks.math.columbia.edu/tag/0F2P). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02LS, a lemma

[Tag 02LS](https://stacks.math.columbia.edu/tag/02LS) in the Stacks Project.

**`AlgebraicGeometry.IsFinite.tfae_isProper_locallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/FiniteIffQuasiFinite.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/FiniteIffQuasiFinite.lean#L51). References: EGA III (4.4.11), “more general”; EGA IV (18.12.4).

> For a morphism of schemes `f : X ⟶ S` the following are equivalent: `f` is finite; `f` is
> proper with finite fibres; `f` is proper and locally quasi-finite; `f` is universally closed,
> separated, locally of finite type and has finite fibres. The fibre over `s` is its underlying set
> `f ⁻¹' {s}`.

```lean
theorem IsFinite.tfae_isProper_locallyQuasiFinite {X S : Scheme.{u}} (f : X ⟶ S) :
    List.TFAE
      [IsFinite f,
        IsProper f ∧ ∀ s : S, (f ⁻¹' {s}).Finite,
        IsProper f ∧ LocallyQuasiFinite f,
        UniversallyClosed f ∧ IsSeparated f ∧ LocallyOfFiniteType f ∧
          ∀ s : S, (f ⁻¹' {s}).Finite]
```

**`AlgebraicGeometry.isFinite_iff_isProper_and_forall_finite_preimage_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/ProperFiniteFibre.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/ProperFiniteFibre.lean#L86). The attribute's comment: “condition (1) <=> condition (2): a morphism of schemes is finite exactly when it is proper with finite fibres. PROVED outright, with no hypothesis beyond the two sides of the equivalence: Mathlib's IsFinite.iff_isProper_and_locallyQuasiFinite is the tag's own (1) <=> (3), and locallyQuasiFinite_iff_finite_preimage_singleton turns local quasi-finiteness into finiteness of the fibres. Properness in Mathlib's sense contains universal closedness and therefore quasi-compactness, so the source's finite-type requirement is met.”. References: EGA III (4.4.11), “more general”; EGA III (4.4.2), “more general”; EGA IV (18.12.4).

> **[Stacks, Tag 02LS], condition (1) ⟺ condition (2).** A morphism of schemes is finite
> exactly when it is proper and all of its fibres are finite.
>
> The source's properness is `AlgebraicGeometry.IsProper`, which contains
> `AlgebraicGeometry.UniversallyClosed` and hence `AlgebraicGeometry.QuasiCompact`, so no further
> hypothesis is needed to pass between finiteness of the fibres and local quasi-finiteness.

```lean
theorem isFinite_iff_isProper_and_forall_finite_preimage_singleton {X S : Scheme.{u}}
    (f : X ⟶ S) :
    IsFinite f ↔ IsProper f ∧ ∀ s : S, (f ⁻¹' {s}).Finite
```

**`AlgebraicGeometry.isFinite_iff_isSeparated_universallyClosed_locallyOfFiniteType_and_finite_fibres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/ProperFiniteFibre.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/ProperFiniteFibre.lean#L100). The attribute's comment: “condition (1) <=> condition (4): a morphism of schemes is finite exactly when it is separated, universally closed, locally of finite type and has finite fibres. PROVED outright from condition (1) <=> condition (2) by unfolding Mathlib's IsProper into its three parents.”. References: EGA III (4.4.2), “more general”.

> **[Stacks, Tag 02LS], condition (1) ⟺ condition (4).** A morphism of schemes is finite
> exactly when it is separated, universally closed, locally of finite type and has finite fibres.
> This is the previous equivalence with `AlgebraicGeometry.IsProper` unfolded into its three
> parents.

```lean
theorem isFinite_iff_isSeparated_universallyClosed_locallyOfFiniteType_and_finite_fibres
    {X S : Scheme.{u}} (f : X ⟶ S) :
    IsFinite f ↔ (IsSeparated f ∧ UniversallyClosed f ∧ LocallyOfFiniteType f) ∧
      ∀ s : S, (f ⁻¹' {s}).Finite
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.44, Tag 0F2P](https://stacks.math.columbia.edu/tag/0F2P)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
