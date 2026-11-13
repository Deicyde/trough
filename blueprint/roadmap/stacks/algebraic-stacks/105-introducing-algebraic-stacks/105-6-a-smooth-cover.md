---
declaration: section
origin: cited
lean: AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.Δ_eq, AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.Δ_smul_eq, AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.base, AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.total, AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.embedding, AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.projection, AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.zero, AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.family
statement: formalized
proof: formalized
---

# 105.6 A smooth cover

Section 105.6 of the Stacks Project, [Tag 072S](https://stacks.math.columbia.edu/tag/072S). 2 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 072S, the section

[Tag 072S](https://stacks.math.columbia.edu/tag/072S) in the Stacks Project.

**`AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.Δ_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamily.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamily.lean#L88). The attribute's comment: “the discriminant Δ, written out”.

> The discriminant of a Weierstrass equation, written out as a polynomial in the five
> coefficients.

```lean
theorem Δ_eq {R : Type*} [CommRing R] (W : WeierstrassCurve R) :
    W.Δ = -W.a₆ * W.a₁ ^ 6 + W.a₄ * W.a₃ * W.a₁ ^ 5
      + ((-W.a₃ ^ 2 - 12 * W.a₆) * W.a₂ + W.a₄ ^ 2) * W.a₁ ^ 4
      + (8 * W.a₄ * W.a₃ * W.a₂ + (W.a₃ ^ 3 + 36 * W.a₆ * W.a₃)) * W.a₁ ^ 3
      + ((-8 * W.a₃ ^ 2 - 48 * W.a₆) * W.a₂ ^ 2 + 8 * W.a₄ ^ 2 * W.a₂
        + (-30 * W.a₄ * W.a₃ ^ 2 + 72 * W.a₆ * W.a₄)) * W.a₁ ^ 2
      + (16 * W.a₄ * W.a₃ * W.a₂ ^ 2 + (36 * W.a₃ ^ 3 + 144 * W.a₆ * W.a₃) * W.a₂
        - 96 * W.a₄ ^ 2 * W.a₃) * W.a₁
      + (-16 * W.a₃ ^ 2 - 64 * W.a₆) * W.a₂ ^ 3 + 16 * W.a₄ ^ 2 * W.a₂ ^ 2
      + (72 * W.a₄ * W.a₃ ^ 2 + 288 * W.a₆ * W.a₄) * W.a₂
      + (-27 * W.a₃ ^ 4 - 216 * W.a₆ * W.a₃ ^ 2 - 64 * W.a₄ ^ 3 - 432 * W.a₆ ^ 2)
```

**`AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.Δ_smul_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamily.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamily.lean#L106). The attribute's comment: “Δ is homogeneous of degree 12 for deg aᵢ = i”.

> The discriminant is homogeneous of degree `12` in the coefficients, where `aᵢ` has degree
> `i`: scaling `aᵢ` by `tⁱ` scales `Δ` by `t¹²`.

```lean
theorem Δ_smul_eq {R : Type*} [CommRing R] (t a₁ a₂ a₃ a₄ a₆ : R) :
    (⟨t * a₁, t ^ 2 * a₂, t ^ 3 * a₃, t ^ 4 * a₄, t ^ 6 * a₆⟩ : WeierstrassCurve R).Δ =
      t ^ 12 * (⟨a₁, a₂, a₃, a₄, a₆⟩ : WeierstrassCurve R).Δ
```

**`AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.base`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamily.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamily.lean#L130). The attribute's comment: “the Weierstrass scheme W”.

> The Weierstrass scheme `W = Spec(ℤ[a₁, a₂, a₃, a₄, a₆, 1/Δ])`.

```lean
abbrev base : Scheme.{u}
```

**`AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.total`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamily.lean, line 314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamily.lean#L314). The attribute's comment: “the plane cubic E\_W”.

> The plane cubic `E_W ⊂ P²_W` cut out by the Weierstrass equation over `W`.

```lean
abbrev total : Scheme.{u}
```

**`AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.embedding`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamily.lean, line 318](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamily.lean#L318). The attribute's comment: “E\_W is a closed subscheme of P²\_W”.

> The closed immersion of `E_W` into `P²_W`.

```lean
abbrev embedding : total.{u} ⟶ projectivePlane.{u}
```

**`AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.projection`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamily.lean, line 324](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamily.lean#L324). The attribute's comment: “the projection f\_W : E\_W → W”.

> The projection `f_W : E_W ⟶ W`.

```lean
abbrev projection : total.{u} ⟶ base.{u}
```

**`AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.zero`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamily.lean, line 328](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamily.lean#L328). The attribute's comment: “the section 0\_W = (0 : 1 : 0)”.

> The section `0_W : W ⟶ E_W` at infinity, the point `(0 : 1 : 0)`.

```lean
abbrev zero : base.{u} ⟶ total.{u}
```

**`AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.family`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamily.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamily.lean#L338). The attribute's comment: “the triple (E\_W, f\_W, 0\_W)”.

> The Weierstrass family `(E_W, f_W, 0_W)`: the plane cubic over
> `W = Spec(ℤ[a₁, a₂, a₃, a₄, a₆, 1/Δ])` with the section `(0 : 1 : 0)` at infinity.

```lean
abbrev family : PointedFamily base.{u}
```

**`AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.isElliptic_familyOf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamilyElliptic.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamilyElliptic.lean#L113). The attribute's comment: “E\_W over a ring with Δ invertible is an elliptic curve”.

> **Stacks Project, Tag 072S.** The plane cubic of a Weierstrass equation with invertible
> discriminant, with its section at infinity, is an elliptic curve over `Spec R`.

```lean
theorem isElliptic_familyOf [C.IsElliptic] : (familyOf C).IsElliptic
```

**`AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.isElliptic_family`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamilyElliptic.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamilyElliptic.lean#L124). The attribute's comment: “(E\_W, f\_W, 0\_W) is an elliptic curve”.

> **Stacks Project, Tag 072S.** The Weierstrass family `(E_W, f_W, 0_W)` over
> `W = Spec(ℤ[a₁, a₂, a₃, a₄, a₆, 1/Δ])` is an elliptic curve.

```lean
theorem isElliptic_family : family.{u}.IsElliptic
```

**`AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.finrank_structureSheafCohomology_projectionOf_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamilyFibres.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamilyFibres.lean#L228). The attribute's comment: “H⁰ of a fibre is one-dimensional”.

> **Over a field, the global functions on the plane cubic are the constants:**
> `dim_k H⁰(E, 𝒪_E) = 1`.

```lean
theorem finrank_structureSheafCohomology_projectionOf_zero :
    Module.finrank k (structureSheafCohomology (projectionOf C) 0) = 1
```

**`AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.genus_projectionOf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamilyFibres.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamilyFibres.lean#L241). The attribute's comment: “a fibre has genus one”.

> **Over a field, the plane cubic has genus one:** `(3 - 1)(3 - 2)/2 = 1`.

```lean
theorem genus_projectionOf : genus (projectionOf C) = 1
```

**`AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.isProper_projectionOf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamilyProper.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamilyProper.lean#L60). The attribute's comment: “f\_W is proper”.

> **The plane cubic of a Weierstrass equation is proper over the base.**

```lean
instance isProper_projectionOf : IsProper (projectionOf C)
```

**`AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.smoothOfRelativeDimension_projectionOf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamilySmooth.lean, line 417](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassFamilySmooth.lean#L417). The attribute's comment: “f\_W is smooth of relative dimension one”.

> **A Weierstrass cubic with invertible discriminant is smooth of relative dimension one over
> its base.**

```lean
theorem smoothOfRelativeDimension_projectionOf (hΔ : IsUnit W.Δ) :
    SmoothOfRelativeDimension 1 (projectionOf W)
```

## Tag 072T, a lemma

[Tag 072T](https://stacks.math.columbia.edu/tag/072T) in the Stacks Project.

**`AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.isSmooth_family`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassSmoothCover.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassSmoothCover.lean#L214). The attribute's comment: “the morphism W → M\_\{1,1} is smooth”.

> **Stacks Project, Tag 072T.** The morphism `W ⟶ 𝓜₁,₁` given by the Weierstrass family
> `(E_W, f_W, 0_W)` is smooth: for every elliptic curve `E'` over a scheme `S'` and every fibre
> product `P = W ×_{𝓜₁,₁} S'`, the projection `P ⟶ S'` is smooth. Over an open of `S'` on which
> `E'` has a Weierstrass equation, `P` is the base change of the smooth projection `H × W ⟶ W`,
> because `H × W` is the fibre product `W ×_{𝓜₁,₁} W`.

```lean
theorem isSmooth_family : family.{u}.IsSmooth isElliptic_family.{u}
```

**`AlgebraicGeometry.ModuliEllipticCurves.Weierstrass.isSurjective_family`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassSmoothCover.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/WeierstrassSmoothCover.lean#L225). The attribute's comment: “the morphism W → M\_\{1,1} is surjective”.

> **Stacks Project, Tag 072T.** The morphism `W ⟶ 𝓜₁,₁` given by the Weierstrass family
> `(E_W, f_W, 0_W)` is surjective: for every elliptic curve `E'` over a scheme `S'` and every fibre
> product `P = W ×_{𝓜₁,₁} S'`, the projection `P ⟶ S'` is surjective, because the fibre of `E'` at
> each point has a Weierstrass equation.

```lean
theorem isSurjective_family : family.{u}.IsSurjective isElliptic_family.{u}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 105.6, Tag 072S](https://stacks.math.columbia.edu/tag/072S)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
