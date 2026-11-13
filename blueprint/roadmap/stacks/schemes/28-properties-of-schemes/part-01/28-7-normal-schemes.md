---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsNormal, AlgebraicGeometry.isNormal_tfae, AlgebraicGeometry.isNormal_open, AlgebraicGeometry.isReduced_of_isNormal, AlgebraicGeometry.isNormal_iff_forall_affineOpen_normal, AlgebraicGeometry.isNormal_iff_exists_iso_coproduct, AlgebraicGeometry.isNormal_iff_exists_iso_finite_coproduct_integral_normal, AlgebraicGeometry.isNormal_iff_exists_iso_coproduct_integral_normal
statement: formalized
proof: formalized
---

# 28.7 Normal schemes

Section 28.7 of the Stacks Project, [Tag 033H](https://stacks.math.columbia.edu/tag/033H). 8 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 033I, a definition

[Tag 033I](https://stacks.math.columbia.edu/tag/033I) in the Stacks Project.

**`AlgebraicGeometry.IsNormal`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Normal.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Normal.lean#L85).

> A scheme is normal if each stalk of its structure sheaf is a normal domain.

```lean
class IsNormal (X : Scheme.{u}) : Prop
```

## Tag 033J, a lemma

[Tag 033J](https://stacks.math.columbia.edu/tag/033J) in the Stacks Project.

**`AlgebraicGeometry.isNormal_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Normal.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Normal.lean#L157). The attribute's comment: “equivalent conditions”.

> **Stacks Project, Tag 033J.** Normality of a scheme is equivalent to normality of the
> section ring on every affine open, on one affine open covering, or to the existence of an
> open covering by normal open subschemes.

```lean
public theorem isNormal_tfae (X : Scheme.{u}) :
    List.TFAE [
      IsNormal X,
      ∀ U : X.affineOpens, IsNormalRing Γ(X, U),
      ∃ (I : Type u) (U : I → X.affineOpens),
        IsOpenCover (fun i ↦ (U i : X.Opens)) ∧
          ∀ i, IsNormalRing Γ(X, U i),
      ∃ (I : Type u) (U : I → X.Opens),
        IsOpenCover U ∧ ∀ i, IsNormal (U i).toScheme]
```

**`AlgebraicGeometry.isNormal_open`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Normal.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Normal.lean#L187). The attribute's comment: “open subschemes”.

> **Stacks Project, Tag 033J.** Every open subscheme of a normal scheme is normal.

```lean
public instance isNormal_open {X : Scheme.{u}} [IsNormal X]
    (U : X.Opens) : IsNormal U.toScheme
```

## Tag 033K, a lemma

[Tag 033K](https://stacks.math.columbia.edu/tag/033K) in the Stacks Project.

**`AlgebraicGeometry.isReduced_of_isNormal`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Normal.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Normal.lean#L193). References: EGA II (7.3.7), “partial”; EGA IV (20.4.12), “partial”.

> A normal scheme is reduced.

```lean
instance isReduced_of_isNormal (X : Scheme.{u}) [IsNormal X] : IsReduced X
```

## Tag 033L, a lemma

[Tag 033L](https://stacks.math.columbia.edu/tag/033L) in the Stacks Project.

**`AlgebraicGeometry.isNormal_iff_forall_affineOpen_normal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Normal.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Normal.lean#L199).

> **Stacks Project, Tag 033L.** An integral scheme is normal if and only if the ring of
> sections on every nonempty affine open is a normal domain.

```lean
public theorem isNormal_iff_forall_affineOpen_normal (X : Scheme.{u}) [IsIntegral X] :
    IsNormal X ↔
      ∀ U : X.affineOpens, ∀ _hU : Nonempty U.1,
        letI : IsDomain Γ(X, U.1) := IsIntegral.component_integral U.1
        IsIntegrallyClosed Γ(X, U.1)
```

## Tag 0357, a lemma

[Tag 0357](https://stacks.math.columbia.edu/tag/0357) in the Stacks Project.

**`AlgebraicGeometry.isNormal_iff_exists_iso_coproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Normal.lean, line 357](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Normal.lean#L357).

> A scheme whose quasi-compact open subspaces have finitely many irreducible components is
> normal if and only if it is isomorphic to a coproduct of normal integral schemes.

```lean
public theorem isNormal_iff_exists_iso_coproduct
    {X : Scheme.{u}}
    (hX : ∀ (U : X.Opens), IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    IsNormal X ↔
      ∃ (ι : Type u) (Y : ι → Scheme.{u})
          (_ : ∀ i, IsNormal (Y i)) (_ : ∀ i, IsIntegral (Y i)),
        Nonempty (X ≅ ∐ Y)
```

## Tag 033M, a lemma

[Tag 033M](https://stacks.math.columbia.edu/tag/033M) in the Stacks Project.

**`AlgebraicGeometry.isNormal_iff_exists_iso_finite_coproduct_integral_normal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/NormalCoproduct.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/NormalCoproduct.lean#L55).

> A Noetherian scheme is normal if and only if it is isomorphic to a finite coproduct of normal
> integral schemes.

```lean
public theorem isNormal_iff_exists_iso_finite_coproduct_integral_normal
    (X : Scheme.{u}) [IsNoetherian X] :
    IsNormal X ↔
      ∃ (ι : Type u) (_ : Finite ι) (Y : ι → Scheme.{u})
          (_ : ∀ i, IsNormal (Y i)) (_ : ∀ i, IsIntegral (Y i)),
        Nonempty (X ≅ ∐ Y)
```

## Tag 033N, a lemma

[Tag 033N](https://stacks.math.columbia.edu/tag/033N) in the Stacks Project.

**`AlgebraicGeometry.isNormal_iff_exists_iso_coproduct_integral_normal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/NormalCoproduct.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/NormalCoproduct.lean#L44).

> A locally Noetherian scheme is normal if and only if it is isomorphic to a coproduct of normal
> integral schemes.

```lean
public theorem isNormal_iff_exists_iso_coproduct_integral_normal
    (X : Scheme.{u}) [IsLocallyNoetherian X] :
    IsNormal X ↔
      ∃ (ι : Type u) (Y : ι → Scheme.{u})
          (_ : ∀ i, IsNormal (Y i)) (_ : ∀ i, IsIntegral (Y i)),
        Nonempty (X ≅ ∐ Y)
```

## Tag 0358, a lemma

[Tag 0358](https://stacks.math.columbia.edu/tag/0358) in the Stacks Project.

**`AlgebraicGeometry.normal_globalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Normal.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Normal.lean#L241). References: EGA II (8.8.6.1).

> The ring of global sections of an integral normal scheme is a normal domain.

```lean
theorem normal_globalSections (X : Scheme.{u}) [IsIntegral X] [IsNormal X] :
    IsIntegrallyClosed Γ(X, ⊤)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.7, Tag 033H](https://stacks.math.columbia.edu/tag/033H)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
