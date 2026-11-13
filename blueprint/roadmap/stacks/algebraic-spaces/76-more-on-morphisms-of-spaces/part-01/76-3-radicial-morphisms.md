---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsRadicial, AlgebraicGeometry.Space.universallyInjective_of_isRadicial, AlgebraicGeometry.RationalGaloisQuotient.universallyInjective_galoisQuotientToBase, AlgebraicGeometry.RationalGaloisQuotient.not_isRadicial_galoisQuotientToBase, AlgebraicGeometry.RationalGaloisQuotient.universallyInjective_and_not_isRadicial, AlgebraicGeometry.RationalGaloisQuotient.exists_universallyInjective_not_isRadicial, AlgebraicGeometry.Space.isRadicial_of_universallyInjective_of_isDecent, AlgebraicGeometry.Space.isRadicial_of_universallyInjective_of_isQuasiSeparated
statement: formalized
proof: formalized
---

# 76.3 Radicial morphisms

Section 76.3 of the Stacks Project, [Tag 0480](https://stacks.math.columbia.edu/tag/0480). 6 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0481, a definition

[Tag 0481](https://stacks.math.columbia.edu/tag/0481) in the Stacks Project.

**`AlgebraicGeometry.Space.IsRadicial`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Radicial.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Radicial.lean#L154).

> **Stacks 0481.** A morphism of algebraic spaces over `S` is *radicial* if for every
> field `k` in the chosen site and every `k`-valued point of the target, the reduction of the
> fibre is either empty or is represented, over `Spec(k)`, by the spectrum of a purely
> inseparable extension of `k`.

```lean
def IsRadicial (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) : Prop
```

## Tag 0482, a lemma

[Tag 0482](https://stacks.math.columbia.edu/tag/0482) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyInjective_of_isRadicial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Radicial.lean, line 340](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Radicial.lean#L340). References: EGA I (3.5.11), “radicial => univ. inj.”.

> **Stacks 0482.** A radicial morphism of algebraic spaces is universally injective.
>
> On a field-valued point of the target the fibre's reduction is either empty, excluding the
> point, or the spectrum of a purely inseparable extension, and a scheme-theoretic section of
> such a spectrum over the base field is unique; two points of the fibre therefore agree.

```lean
theorem universallyInjective_of_isRadicial
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y)
    (hf : IsRadicial B S hS hX hY f) :
    UniversallyInjective B S hS f
```

## Tag 0483, an example

[Tag 0483](https://stacks.math.columbia.edu/tag/0483) in the Stacks Project.

**`AlgebraicGeometry.RationalGaloisQuotient.universallyInjective_galoisQuotientToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RationalGaloisQuotient.lean, line 350](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RationalGaloisQuotient.lean#L350). The attribute's comment: “universally injective”.

> **Stacks 0483.** The Galois quotient of `Spec ℚ̄` is universally injective over `Spec ℚ`,
> although it is not radicial.
>
> Universal injectivity is tested on field-valued points, so it suffices to make two sections
> of the quotient over the spectrum of a field agree over a further field spectrum. The
> projection of `Spec ℚ̄` onto the quotient is locally surjective, so after two successive
> restrictions both sections come from morphisms to `Spec ℚ̄`, that is from two `ℚ`-embeddings
> of `ℚ̄` into the field of the second restriction; those differ by an element of the Galois
> group, which is exactly what the quotient divides out.

```lean
theorem universallyInjective_galoisQuotientToBase :
    Space.UniversallyInjective B base hS (galoisQuotientToBase B hS hU)
```

**`AlgebraicGeometry.RationalGaloisQuotient.not_isRadicial_galoisQuotientToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RationalGaloisQuotientNotRadicial.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RationalGaloisQuotientNotRadicial.lean#L171). The attribute's comment: “not radicial”.

> **Stacks 0483.** The structure morphism of the Galois quotient of `Spec ℚ̄` to `Spec ℚ` is
> *not* radicial.
>
> Radicialness is tested at the field `ℚ` itself, on the terminal object of the site with the
> identity point of the base, so that the fibre is the quotient itself. Its reduction is not
> pointless, because the `ℚ̄`-valued point coming from the projection of `Spec ℚ̄` survives to
> the reduction; and it is not the spectrum of a purely inseparable extension `L` of `ℚ`
> either: `ℚ` is perfect, so the structure map `ℚ → L` is surjective, while a field algebraic
> over `ℚ` carrying a point of the quotient is a copy of `ℚ̄` or of the real algebraic numbers
> by `AlgebraicGeometry.RationalGaloisQuotient.fieldPoint_algEquiv_algebraicClosure_or_real`,
> and the structure map of `ℚ` into either of those is not surjective, both fields containing
> a square root of two.

```lean
theorem not_isRadicial_galoisQuotientToBase :
    ¬ Space.IsRadicial B base hS (isAlgebraicSpace_galoisQuotient B hS hU)
      (isAlgebraicSpace_yoneda B base hS (Over.mk (𝟙 (B.obj hS))))
      (galoisQuotientToBase B hS hU)
```

**`AlgebraicGeometry.RationalGaloisQuotient.universallyInjective_and_not_isRadicial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RationalGaloisQuotientNotRadicial.lean, line 213](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RationalGaloisQuotientNotRadicial.lean#L213). The attribute's comment: “the two halves together, over a big fppf site containing the two spectra”.

> **Stacks 0483.** The structure morphism of the Galois quotient of `Spec ℚ̄` to `Spec ℚ` is
> universally injective but is not radicial: for algebraic spaces, unlike for schemes,
> universal injectivity is strictly weaker than radicialness.
>
> This is the conjunction over a fixed big fppf site containing the two spectra;
> `AlgebraicGeometry.RationalGaloisQuotient.exists_universallyInjective_not_isRadicial`
> exhibits such a site and so asserts the non-equivalence outright.

```lean
theorem universallyInjective_and_not_isRadicial :
    Space.UniversallyInjective B base hS (galoisQuotientToBase B hS hU) ∧
      ¬ Space.IsRadicial B base hS (isAlgebraicSpace_galoisQuotient B hS hU)
        (isAlgebraicSpace_yoneda B base hS (Over.mk (𝟙 (B.obj hS))))
        (galoisQuotientToBase B hS hU)
```

**`AlgebraicGeometry.RationalGaloisQuotient.exists_universallyInjective_not_isRadicial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RationalGaloisQuotientNotRadicial.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RationalGaloisQuotientNotRadicial.lean#L234).

> **Stacks 0483.** Universal injectivity is not equivalent to radicialness for morphisms of
> algebraic spaces: there are a big fppf site over `Spec ℚ`, an algebraic space over `Spec ℚ` in
> it, and a structure morphism of that space to `Spec ℚ` which is universally injective and is
> not radicial.
>
> Nothing is assumed: the site is the one
> `AlgebraicGeometry.BigFppfSite.exists_containing` supplies for the two schemes `Spec ℚ` and
> `Spec ℚ̄`, and the space is the Galois quotient of `Spec ℚ̄`, so this is
> `AlgebraicGeometry.RationalGaloisQuotient.universallyInjective_and_not_isRadicial` with its
> site hypotheses discharged.

```lean
theorem exists_universallyInjective_not_isRadicial :
    ∃ (B : BigFppfSite.{0}) (hS : B.Contains base)
      (X : (BigFppfOver B base hS)ᵒᵖ ⥤ Type 0) (hX : IsAlgebraicSpace B base hS X)
      (f : X ⟶ yoneda.obj (Over.mk (𝟙 (B.obj hS)))),
      Space.UniversallyInjective B base hS f ∧
        ¬ Space.IsRadicial B base hS hX
          (isAlgebraicSpace_yoneda B base hS (Over.mk (𝟙 (B.obj hS)))) f
```

## Tag 0484, a lemma

[Tag 0484](https://stacks.math.columbia.edu/tag/0484) in the Stacks Project.

**`AlgebraicGeometry.Space.isRadicial_of_universallyInjective_of_isDecent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Radicial.lean, line 548](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Radicial.lean#L548). The attribute's comment: “part (1)”.

> **Stacks 0484, part (1).** A universally injective decent morphism of algebraic spaces over
> `S` is radicial.
>
> Over a field-valued point of the target the reduction of the fibre is a reduced decent algebraic
> space whose point set is a subsingleton, hence empty or the spectrum of a field by Stacks 047Z,
> and the resulting extension is purely inseparable because its spectrum map is again universally
> injective.

```lean
theorem isRadicial_of_universallyInjective_of_isDecent
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y)
    (hinj : UniversallyInjective B S hS f)
    (hdecent : IsDecent B S hS f) :
    IsRadicial B S hS hX hY f
```

**`AlgebraicGeometry.Space.isRadicial_of_universallyInjective_of_isQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Radicial.lean, line 591](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Radicial.lean#L591). The attribute's comment: “part (2)”.

> **Stacks 0484, part (2).** A universally injective quasi-separated morphism of algebraic
> spaces over `S` is radicial: a quasi-separated morphism is very reasonable, hence reasonable,
> hence decent.

```lean
theorem isRadicial_of_universallyInjective_of_isQuasiSeparated
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y)
    (hinj : UniversallyInjective B S hS f)
    (hqs : IsQuasiSeparated B S hS f) :
    IsRadicial B S hS hX hY f
```

**`AlgebraicGeometry.Space.isRadicial_of_universallyInjective_of_isLocallySeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Radicial.lean, line 610](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Radicial.lean#L610). The attribute's comment: “part (3)”.

> **Stacks 0484, part (3).** A universally injective locally separated morphism of algebraic
> spaces over `S` is radicial.
>
> Universal injectivity makes the relative diagonal surjective and local separatedness makes it an
> immersion, so it is a closed immersion; the morphism is therefore separated, in particular
> quasi-separated.

```lean
theorem isRadicial_of_universallyInjective_of_isLocallySeparated
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y)
    (hinj : UniversallyInjective B S hS f)
    (hls : IsLocallySeparated B S hS f) :
    IsRadicial B S hS hX hY f
```

## Tag 049E, a remark

[Tag 049E](https://stacks.math.columbia.edu/tag/049E) in the Stacks Project.

**`AlgebraicGeometry.RationalGaloisQuotient.isWeaklyRadicial_galoisQuotientBaseChangeToCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RationalGaloisQuotientBaseChange.lean, line 439](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RationalGaloisQuotientBaseChange.lean#L439). The attribute's comment: “the base change of Example 0483 to ℚ̄ is weakly radicial”.

> **Stacks 049E.** The base change `X_ℚ̄ ⟶ Spec ℚ̄` of the morphism of Stacks 0483 is weakly
> radicial.
>
> Over a field-valued point `Spec(K) ⟶ Spec ℚ̄` the fibre has a section, through the projection
> of `Spec ℚ̄` onto the Galois quotient; a section is a monomorphism, and it exhibits the trivial,
> purely inseparable, extension `K ⊂ K`. The point set of the fibre is a singleton because it
> receives the point of the section and because the base change of the universally injective
> morphism of Stacks 0483 is universally injective.

```lean
theorem isWeaklyRadicial_galoisQuotientBaseChangeToCover :
    Space.IsWeaklyRadicial B base hS (isAlgebraicSpace_galoisQuotientBaseChange B hS hU)
      (isAlgebraicSpace_yoneda B base hS _) (galoisQuotientBaseChangeToCover B hS hU)
```

**`AlgebraicGeometry.RationalGaloisQuotient.not_isRadicial_galoisQuotientBaseChangeToCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RationalGaloisQuotientBaseChange.lean, line 546](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RationalGaloisQuotientBaseChange.lean#L546). The attribute's comment: “the base change of Example 0483 to ℚ̄ is not radicial”.

> **Stacks 049E.** The base change `X_ℚ̄ ⟶ Spec ℚ̄` of the morphism of Stacks 0483 is not
> radicial.
>
> Were it radicial, the two projections `Spec ℚ̄ ×_ℚ Spec ℚ̄ ⟶ Spec ℚ̄`, which are morphisms from
> the reduced scheme `Spec(ℚ̄ ⊗_ℚ ℚ̄)`, would have the same image in the Galois quotient
> (`AlgebraicGeometry.RationalGaloisQuotient.galoisChart_eq_of_isRadicial`). The graph of the
> Galois action is the kernel pair of the projection of `Spec ℚ̄` onto its quotient, so the two
> projections would be related by a morphism `Spec(ℚ̄ ⊗_ℚ ℚ̄) ⟶ ∐_{g} Spec ℚ̄`, which by
> quasi-compactness forces the absolute Galois group of `ℚ` to be finite
> (`AlgebraicGeometry.RationalGaloisQuotient.finite_galoisGroup_of_rel`); it is not
> (`AlgebraicGeometry.RationalGaloisQuotient.infinite_galoisGroup`).

```lean
theorem not_isRadicial_galoisQuotientBaseChangeToCover :
    ¬ Space.IsRadicial B base hS (isAlgebraicSpace_galoisQuotientBaseChange B hS hU)
      (isAlgebraicSpace_yoneda B base hS _) (galoisQuotientBaseChangeToCover B hS hU)
```

**`AlgebraicGeometry.Space.IsWeaklyRadicial`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Radicial.lean, line 632](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Radicial.lean#L632). The attribute's comment: “the definition of a weakly radicial morphism”.

> **Stacks 049E.** A morphism of algebraic spaces over `S` is *weakly radicial* if for every
> field `K` in the chosen site and every `K`-valued point of the target, the point set of the fibre
> is a singleton and the fibre admits, over `Spec(K)`, a monomorphism from the spectrum of a purely
> inseparable extension of `K`.

```lean
def IsWeaklyRadicial (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (_hX : IsAlgebraicSpace B S hS X) (_hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.surjective_app_of_isWeaklyRadicial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Radicial.lean, line 706](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Radicial.lean#L706). The attribute's comment: “surjectivity on k-points for k algebraically closed”.

> **Stacks 049E.** A weakly radicial morphism of algebraic spaces over `S` is surjective on
> `k`-valued points for every algebraically closed field `k` in the chosen site.
>
> The fibre over a `k`-valued point of the target receives a monomorphism from the spectrum of a
> purely inseparable extension of `k`, and such an extension of an algebraically closed field is
> trivial; the induced morphism of field spectra is therefore an isomorphism, and inverting it
> produces a section of the fibre's projection, hence a `k`-valued point of the source over the
> given one.

```lean
theorem surjective_app_of_isWeaklyRadicial
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (hf : IsWeaklyRadicial B S hS hX hY f)
    (k : Type u) [Field k] [IsAlgClosed k] (hk : B.Contains (Spec (.of k)))
    (s : Spec (.of k) ⟶ S) :
    Function.Surjective (f.app (Opposite.op
      (Over.mk (⟨s⟩ : B.obj hk ⟶ B.obj hS) : BigFppfOver B S hS)))
```

**`AlgebraicGeometry.Space.isWeaklyRadicial_of_universallyInjective_of_hasPropertyBeta`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Radicial.lean, line 765](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Radicial.lean#L765). The attribute's comment: “corrected form of the analogue of 0484, with surjectivity added”.

> **Stacks 049E, the analogue of Stacks 0484.** A surjective, universally injective morphism
> of algebraic spaces over `S` with property `(β)` is weakly radicial.
>
> The source states this without the surjectivity hypothesis, and in that form it is false: a weakly
> radicial morphism is surjective (`AlgebraicGeometry.Space.isSurjective_of_isWeaklyRadicial`),
> while the inclusion of the empty scheme is universally injective and has property `(β)`, see
> `AlgebraicGeometry.Space.exists_universallyInjective_hasPropertyBeta_not_isWeaklyRadicial`.
>
> Over a field-valued point `Spec(K) ⟶ Y` the fibre has a subsingleton point set by universal
> injectivity and a nonempty one by surjectivity. Property `(β)` at its unique point is
> condition (1) of Stacks 03JU, which is equivalent to condition (4): a monomorphism from the
> spectrum of a field `L` representing the point. The composite `Spec(L) ⟶ Spec(K)` is
> universally injective, a monomorphism being universally injective, so `K ⊂ L` is purely
> inseparable, exactly as in the proof of Stacks 0484.

```lean
theorem isWeaklyRadicial_of_universallyInjective_of_hasPropertyBeta
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y)
    (hinj : UniversallyInjective B S hS f)
    (hbeta : HasPropertyBeta B S hS f)
    (hsurj : IsSurjective B S hS f) :
    IsWeaklyRadicial B S hS hX hY f
```

**`AlgebraicGeometry.Space.exists_universallyInjective_hasPropertyBeta_not_isWeaklyRadicial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Radicial.lean, line 823](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Radicial.lean#L823). The attribute's comment: “the analogue of Lemma 0484 without surjectivity is false: a counterexample”.

> **Stacks 049E, the analogue of Stacks 0484 as stated is false.** As soon as the site
> contains the spectrum of a field, there is a universally injective morphism of algebraic
> spaces with property `(β)` which is not weakly radicial: the inclusion into `Spec(K)` of the
> empty scheme. Its fibre over `Spec(K)` has no point, whereas a weakly radicial morphism has a
> one-point fibre over every field-valued point.
>
> The corrected statement, with surjectivity added, is
> `AlgebraicGeometry.Space.isWeaklyRadicial_of_universallyInjective_of_hasPropertyBeta`.

```lean
theorem exists_universallyInjective_hasPropertyBeta_not_isWeaklyRadicial
    (K : Type u) [Field K] (hK : B.Contains (Spec (.of K))) (s : Spec (.of K) ⟶ S) :
    ∃ (X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
      (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y),
      UniversallyInjective B S hS f ∧ HasPropertyBeta B S hS f ∧
        ¬ IsWeaklyRadicial B S hS hX hY f
```

## Tag 0AGE, a lemma

[Tag 0AGE](https://stacks.math.columbia.edu/tag/0AGE) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyInjective_of_injective_pointsMap_pullback_of_isEtale_yoneda`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjectiveEtaleCriterion.lean, line 451](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjectiveEtaleCriterion.lean#L451).

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is
> locally of finite type, and assume that for every étale morphism `V ⟶ Y` from a scheme `V` the
> map `|X ×_Y V| → |V|` is injective. Then `f` is universally injective.

```lean
theorem universallyInjective_of_injective_pointsMap_pullback_of_isEtale_yoneda
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f)
    (hinj : ∀ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y), IsEtale B S hS g →
      Function.Injective (pointsMap B S hS (pullback g f) (pullback.fst g f))) :
    UniversallyInjective B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.3, Tag 0480](https://stacks.math.columbia.edu/tag/0480)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
