---
declaration: section
origin: cited
lean: Stacks.Divisors.orderOfVanishingMeromorphic, AlgebraicGeometry.orderOfVanishingMeromorphicData, AlgebraicGeometry.orderOfVanishingMeromorphic, AlgebraicGeometry.locallyFinite_primeDivisors_not_representedAt, AlgebraicGeometry.locallyFinite_primeDivisors_orderOfVanishingMeromorphic_ne_zero, AlgebraicGeometry.existsUnique_meromorphicSectionRatio, AlgebraicGeometry.meromorphicWeilDivisor_eq_add_principalDivisor, AlgebraicGeometry.weilDivisorClassOfInvertibleSheaf
statement: formalized
proof: formalized
---

# 31.28 The Weil divisor class associated to an invertible module

Section 31.28 of the Stacks Project, [Tag 02SE](https://stacks.math.columbia.edu/tag/02SE). 8 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02SF, a definition

[Tag 02SF](https://stacks.math.columbia.edu/tag/02SF) in the Stacks Project.

**`Stacks.Divisors.orderOfVanishingMeromorphic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/MeromorphicCascade/OrderOfVanishing.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/MeromorphicCascade/OrderOfVanishing.lean#L75). References: EGA IV (21.6.7), “o\_x(f) = mult\_x(div f)”.

> **The order of vanishing of a regular meromorphic section along a prime divisor, Stacks
> 02SF.** The meromorphic section is a global section `s` of the sheaf `𝒦_X(L)` of meromorphic
> sections of `L`; its order along `Z` is the order of vanishing, in the local ring at the generic
> point of `Z`, of the rational function expressing the generic value of `s` in terms of a generator
> of the stalk of `L` there.
>
> `Stacks.Divisors.orderOfVanishingMeromorphic_eq` is the characterization, and it is what should be
> used rather than this definition.

```lean
def orderOfVanishingMeromorphic (X : Scheme.{u}) [IsLocallyNoetherian X] [IsIntegral X]
    (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : AlgebraicGeometry.MeromorphicSection X.sheaf L)
    (_hs : AlgebraicGeometry.IsRegularMeromorphicSection X.sheaf L s)
    (Z : PrimeDivisor X) : ℤ
```

**`AlgebraicGeometry.orderOfVanishingMeromorphicData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/OrderOfVanishingMeromorphic.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/OrderOfVanishingMeromorphic.lean#L95).

> A choice of the data provided by
> `AlgebraicGeometry.nonempty_orderOfVanishingMeromorphicData`: the quasi-coherence of `L`, the
> order of vanishing of the regular meromorphic section `s` along the prime divisor `Z`, and its
> characterization as the order of the coordinate of `s` with respect to any generator of `L` at
> the generic point of `Z`.

```lean
def orderOfVanishingMeromorphicData
    (X : Scheme.{u}) [IsLocallyNoetherian X] [IsIntegral X]
    (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : MeromorphicSection X.sheaf L)
    (_hs : IsRegularMeromorphicSection X.sheaf L s)
    (Z : PrimeDivisor X) :
    { q : PSigma (fun _ : L.IsQuasicoherent => ℤ) //
      letI : L.IsQuasicoherent := q.1
      let ξ := Z.genericPoint
      let R := X.presheaf.stalk ξ
      let K := X.functionField
      letI : Module R (L.presheaf.stalk ξ) :=
        PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
          (R := X.presheaf) L.val ξ
      letI : Module K (L.presheaf.stalk (genericPoint X)) :=
        PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
          (R := X.presheaf) L.val (genericPoint X)
      let isCoordinate := fun (m : L.presheaf.stalk ξ) (a : K) =>
        ((meromorphicSectionSheafIsoConstant X L).val.hom.val.app
          (op (⊤ : X.Opens))) (s.val (op ⊤)) =
          constantGenericStalkModuleSection X L ⊤
            (a • (L.presheaf.stalkSpecializes
              ((genericPoint_spec X).specializes trivial)) m)
      (∃ m : L.presheaf.stalk ξ,
        (Submodule.span R {m} = ⊤) ∧ (∃ a : K, isCoordinate m a)) ∧
      (∀ (m : L.presheaf.stalk ξ)
        (_ : Submodule.span R {m} = ⊤) (a : K),
        isCoordinate m a → q.2 = X.ord a ξ) }
```

**`AlgebraicGeometry.orderOfVanishingMeromorphic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/OrderOfVanishingMeromorphic.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/OrderOfVanishingMeromorphic.lean#L130).

> The order of vanishing along a prime divisor `Z` of a regular meromorphic section `s` of an
> invertible module `L` on a locally Noetherian integral scheme: the order in `𝒪_{X, ξ}` of the
> coordinate of `s` with respect to a generator of `L_ξ`, where `ξ` is the generic point of `Z`.

```lean
def orderOfVanishingMeromorphic
    (X : Scheme.{u}) [IsLocallyNoetherian X] [IsIntegral X]
    (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : MeromorphicSection X.sheaf L)
    (hs : IsRegularMeromorphicSection X.sheaf L s)
    (Z : PrimeDivisor X) : ℤ
```

## Tag 02SG, a lemma

[Tag 02SG](https://stacks.math.columbia.edu/tag/02SG) in the Stacks Project.

**`AlgebraicGeometry.locallyFinite_primeDivisors_not_representedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/PoleLocus.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/PoleLocus.lean#L164). The attribute's comment: “nonintegral\_stalk\_locus”.

> The prime divisors at whose generic point a meromorphic section of a quasi-coherent module
> on a locally Noetherian integral scheme is not an ordinary section form a locally finite
> collection of closed subsets.

```lean
theorem locallyFinite_primeDivisors_not_representedAt [IsLocallyNoetherian X] [IsIntegral X]
    (L : X.Modules)
    [L.IsQuasicoherent] (s : MeromorphicSection X.sheaf L) :
    LocallyFinite
      (fun Z : { Z : PrimeDivisor X // ¬ IsRepresentedAt L s Z.genericPoint } => Z.1.support)
```

**`AlgebraicGeometry.locallyFinite_primeDivisors_orderOfVanishingMeromorphic_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/PoleLocus.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/PoleLocus.lean#L198). The attribute's comment: “nonzero\_order\_locus”.

> The prime divisors along which a regular meromorphic section of an invertible module on a
> locally Noetherian integral scheme has nonzero order of vanishing form a locally finite
> collection of closed subsets; equivalently, the orders are the coefficients of a Weil divisor.

```lean
theorem locallyFinite_primeDivisors_orderOfVanishingMeromorphic_ne_zero :
    LocallyFinite (fun Z : PrimeDivisor X =>
      if orderOfVanishingMeromorphic X L s hs Z = 0 then ∅ else Z.support)
```

## Tag 02SH, a lemma

[Tag 02SH](https://stacks.math.columbia.edu/tag/02SH) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_meromorphicSectionRatio`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/SectionRatio.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/SectionRatio.lean#L154). The attribute's comment: “ratio”. References: EGA IV (20.1.8), “partial”.

> Two regular meromorphic sections of an invertible module on an integral scheme have a unique
> ratio in the units of the ring of rational functions.

```lean
theorem existsUnique_meromorphicSectionRatio
    (hs : IsRegularMeromorphicSection X.sheaf L s)
    (hs' : IsRegularMeromorphicSection X.sheaf L s') :
    ∃! f : (Stacks.Chow.rationalFunctions X)ˣ, IsMeromorphicSectionRatio X L s s' f
```

**`AlgebraicGeometry.meromorphicWeilDivisor_eq_add_principalDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/SectionRatio.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/SectionRatio.lean#L242). The attribute's comment: “divisor identity”.

> The Weil divisors of two regular meromorphic sections of an invertible
> module on a locally Noetherian integral scheme differ by the principal divisor of their ratio.

```lean
theorem meromorphicWeilDivisor_eq_add_principalDivisor [IsLocallyNoetherian X]
    (hs : IsRegularMeromorphicSection X.sheaf L s)
    (hs' : IsRegularMeromorphicSection X.sheaf L s') :
    weilDivisorOfMeromorphicSection X L s hs =
      weilDivisorOfMeromorphicSection X L s' hs' +
        principalDivisor X (meromorphicSectionRatio X L s s' hs hs')
```

## Tag 0BE6, a definition

[Tag 0BE6](https://stacks.math.columbia.edu/tag/0BE6) in the Stacks Project.

**`AlgebraicGeometry.weilDivisorClassOfInvertibleSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DivisorClass.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DivisorClass.lean#L47). The attribute's comment: “part (2): divisor class of an invertible sheaf”.

> The Weil divisor class of an invertible sheaf on a locally Noetherian integral scheme: the
> class in `Cl(X)` of the Weil divisor of a chosen regular meromorphic section of `L`.

```lean
def weilDivisorClassOfInvertibleSheaf : weilDivisorClassGroup X
```

**`AlgebraicGeometry.weilDivisorClassOfInvertibleSheaf_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DivisorClass.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/DivisorClass.lean#L56). The attribute's comment: “part (2): independence of the meromorphic section”.

> The Weil divisor of any regular meromorphic section of an invertible sheaf `L` has class
> `AlgebraicGeometry.weilDivisorClassOfInvertibleSheaf X L` in `Cl(X)`.

```lean
theorem weilDivisorClassOfInvertibleSheaf_eq (s : MeromorphicSection X.sheaf L)
    (hs : IsRegularMeromorphicSection X.sheaf L s) :
    weilDivisorClassOfInvertibleSheaf X L =
      ((weilDivisorOfMeromorphicSection X L s hs : WeilDivisor X) :
        weilDivisorClassGroup X)
```

**`AlgebraicGeometry.weilDivisorOfMeromorphicSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/PoleLocus.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/PoleLocus.lean#L241). The attribute's comment: “part (1): divisor of a meromorphic section”.

> The Weil divisor `div_L(s) = ∑_Z ord_{Z, L}(s) [Z]` of a regular meromorphic section of an
> invertible module on a locally Noetherian integral scheme.

```lean
def weilDivisorOfMeromorphicSection : WeilDivisor X
```

## Tag 02SL, a lemma

[Tag 02SL](https://stacks.math.columbia.edu/tag/02SL) in the Stacks Project.

**`AlgebraicGeometry.tensorMeromorphicSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TensorSection.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TensorSection.lean#L179). The attribute's comment: “tensor product of meromorphic sections”.

> **Stacks 02SL: the tensor product of two meromorphic sections.** The meromorphic section of
> `L ⊗_{𝒪_X} N` whose generic value is the pure tensor of the generic values of `s` and `t`. On an
> integral scheme this determines it, by Tag 01X5 part (2);
> `AlgebraicGeometry.meromorphicSectionSheafIsoConstant_tensorMeromorphicSection` is the resulting
> description on pure tensors of honest sections.

```lean
def tensorMeromorphicSection [L.IsQuasicoherent] [N.IsQuasicoherent]
    [(Scheme.Modules.tensorObj L N).IsQuasicoherent]
    (s : MeromorphicSection X.sheaf L) (t : MeromorphicSection X.sheaf N) :
    MeromorphicSection X.sheaf (Scheme.Modules.tensorObj L N)
```

**`AlgebraicGeometry.meromorphicSectionSheafIsoConstant_tensorMeromorphicSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TensorSection.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TensorSection.lean#L220). The attribute's comment: “pure-tensor characterization”.

> **Stacks 02SL: at the generic point the product is the pure tensor.** If the meromorphic
> sections `s` and `t` are, at the generic point, the germs of honest sections `m` of `L` and `n`
> of `N` over a neighbourhood `U` of it, then their product is the germ of the pure tensor
> `m ⊗ n`. This fixes the product and not merely its divisor: a meromorphic section on an integral
> scheme is determined by its generic germ.

```lean
theorem meromorphicSectionSheafIsoConstant_tensorMeromorphicSection
    [L.IsQuasicoherent] [N.IsQuasicoherent] [(Scheme.Modules.tensorObj L N).IsQuasicoherent]
    (s : MeromorphicSection X.sheaf L) (t : MeromorphicSection X.sheaf N)
    (U : X.Opens) (hU : genericPoint X ∈ U)
    (m : L.val.obj (op U)) (n : N.val.obj (op U))
    (hs : (meromorphicSectionSheafIsoConstant X L).val.hom.val.app (op (⊤ : X.Opens))
      (s.val (op ⊤)) =
        constantGenericStalkModuleSection X L ⊤ (L.presheaf.germ U (genericPoint X) hU m))
    (ht : (meromorphicSectionSheafIsoConstant X N).val.hom.val.app (op (⊤ : X.Opens))
      (t.val (op ⊤)) =
        constantGenericStalkModuleSection X N ⊤ (N.presheaf.germ U (genericPoint X) hU n)) :
    (meromorphicSectionSheafIsoConstant X (Scheme.Modules.tensorObj L N)).val.hom.val.app
        (op (⊤ : X.Opens)) ((tensorMeromorphicSection X L N s t).val (op ⊤)) =
      constantGenericStalkModuleSection X (Scheme.Modules.tensorObj L N) ⊤
        (PresheafOfModules.tensorSheafGerm X.sheaf L N (genericPoint X) U hU m n)
```

**`AlgebraicGeometry.isRegularMeromorphicSection_tensorMeromorphicSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TensorSection.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TensorSection.lean#L269). The attribute's comment: “nonzero product”. References: EGA IV (20.1.10), “integral; tensor clause”.

> **Stacks 02SL: a product of nonzero meromorphic sections is nonzero.** Regularity in the
> sense of Tag 02OX is injectivity of multiplication by the generic value. Writing the generic
> values of `s` and `t` as `a` and `b` times stalk bases of `L_η` and `N_η`, the generic value of
> the product is `a * b` times the product of those bases, which is a stalk basis of
> `(L ⊗_{𝒪_X} N)_η`; and `a * b` is nonzero in the function field.

```lean
theorem isRegularMeromorphicSection_tensorMeromorphicSection
    [SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    [SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property N]
    (s : MeromorphicSection X.sheaf L) (t : MeromorphicSection X.sheaf N)
    (hs : IsRegularMeromorphicSection X.sheaf L s)
    (ht : IsRegularMeromorphicSection X.sheaf N t) :
    IsRegularMeromorphicSection X.sheaf (Scheme.Modules.tensorObj L N)
      (tensorMeromorphicSection X L N s t)
```

**`AlgebraicGeometry.weilDivisorOfMeromorphicSection_tensorMeromorphicSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TensorSection.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TensorSection.lean#L357). The attribute's comment: “divisor additivity”.

> **Stacks 02SL: the divisor of a product is the sum of the divisors.** The Weil divisor of
> Tag 0BE6 part (1) is additive in the product of regular meromorphic sections of invertible
> modules, coefficient by coefficient.

```lean
theorem weilDivisorOfMeromorphicSection_tensorMeromorphicSection
    [SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    [SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property N]
    (s : MeromorphicSection X.sheaf L) (t : MeromorphicSection X.sheaf N)
    (hs : IsRegularMeromorphicSection X.sheaf L s)
    (ht : IsRegularMeromorphicSection X.sheaf N t) :
    weilDivisorOfMeromorphicSection X (Scheme.Modules.tensorObj L N)
        (tensorMeromorphicSection X L N s t)
        (isRegularMeromorphicSection_tensorMeromorphicSection X L N s t hs ht) =
      weilDivisorOfMeromorphicSection X L s hs + weilDivisorOfMeromorphicSection X N t ht
```

**`AlgebraicGeometry.weilDivisorClassOfInvertibleSheaf_tensorObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TensorSection.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TensorSection.lean#L378). The attribute's comment: “divisor-class additivity”.

> **Stacks 02SL: the divisor class of a tensor product is the sum of the divisor classes.**
> The Weil divisor class of Tag 0BE6 part (2) is additive in the tensor product of invertible
> modules: a regular meromorphic section of each factor exists by Tag 02OZ part (1), their
> product is a regular meromorphic section of the tensor product, and its divisor is the sum of
> their divisors. This is the input Tag 0BE7 needs, and it is supplied to it in
> `AlgebraicGeometry.picardToWeilDivisorClassGroup`.

```lean
theorem weilDivisorClassOfInvertibleSheaf_tensorObj
    [SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    [SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property N] :
    weilDivisorClassOfInvertibleSheaf X (Scheme.Modules.tensorObj L N) =
      weilDivisorClassOfInvertibleSheaf X L + weilDivisorClassOfInvertibleSheaf X N
```

## Tag 0BE7, an equation

[Tag 0BE7](https://stacks.math.columbia.edu/tag/0BE7) in the Stacks Project.

**`AlgebraicGeometry.picardToWeilDivisorClassGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/WeilDivisorClass/FirstChernClass.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/WeilDivisorClass/FirstChernClass.lean#L129).

> **Stacks 0BE7: the first Chern class.** On a locally Noetherian integral scheme the Weil
> divisor class of an invertible module defines a homomorphism from the Picard group to the Weil
> divisor class group. Additivity is the divisor-class additivity of Tag 02SL,
> `AlgebraicGeometry.weilDivisorClassOfInvertibleSheaf_tensorObj`, and well-definedness on
> isomorphism classes is `AlgebraicGeometry.weilDivisorClassOfInvertibleSheaf_congr`;
> `AlgebraicGeometry.weilDivisorClassOfPicardClass_picardClass` is the characterization of this
> homomorphism on the class of an invertible module.

```lean
def picardToWeilDivisorClassGroup :
    Stacks.SheafOfModules.PicardGroup X.sheaf.obj X.ringCatSheaf.property →+
      weilDivisorClassGroup X
```

## Tag 0BE8, a lemma

[Tag 0BE8](https://stacks.math.columbia.edu/tag/0BE8) in the Stacks Project.

**`AlgebraicGeometry.picardToWeilDivisorClassGroup_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/WeilDivisorClass/FirstChernClassInjective.lean, line 466](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/WeilDivisorClass/FirstChernClassInjective.lean#L466). References: EGA IV (21.6.10), “(i), integral case”; SGA 2 XI (3.8), “partial”.

> **Stacks 0BE8.** On a normal locally Noetherian integral scheme the first Chern class
> `Pic(X) → Cl(X)` of Tag 0BE7 is injective.
>
> The map is a group homomorphism, so it is enough that a Picard class in its kernel vanishes.
> Such a class is the Picard class of an invertible module `L`, whose image is the Weil divisor
> class of `L`, and
> `AlgebraicGeometry.nonempty_iso_unit_of_weilDivisorClassOfInvertibleSheaf_eq_zero` then makes
> `L` isomorphic to `𝒪_X`, which is triviality of the Picard class.

```lean
theorem picardToWeilDivisorClassGroup_injective [IsNormal X] :
    Function.Injective (picardToWeilDivisorClassGroup X)
```

## Tag 0BE9, a lemma

[Tag 0BE9](https://stacks.math.columbia.edu/tag/0BE9) in the Stacks Project.

**`AlgebraicGeometry.isNormal_of_forall_uniqueFactorizationMonoid_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/WeilDivisorClass/FirstChernClassBijective.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/WeilDivisorClass/FirstChernClassBijective.lean#L63). The attribute's comment: “(1) → (2): factorial local rings give a normal scheme”.

> A scheme whose local rings are unique factorization domains is normal: a unique
> factorization domain is integrally closed, which is Tag 0AFV.
>
> **Stacks 0BE9**, the normality half of the implication from condition (1) to condition (2).

```lean
theorem isNormal_of_forall_uniqueFactorizationMonoid_stalk
    (h : ∀ x : X, UniqueFactorizationMonoid (X.presheaf.stalk x)) : IsNormal X
```

**`AlgebraicGeometry.picardToWeilDivisorClassGroup_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/WeilDivisorClass/FirstChernClassBijective.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/WeilDivisorClass/FirstChernClassBijective.lean#L75). The attribute's comment: “final clause under (2): on a normal scheme a surjective c\_1 is bijective”.

> On a normal locally Noetherian integral scheme a surjective first Chern class
> `Pic(X) → Cl(X)` is bijective, since it is injective by Tag 0BE8.
>
> **Stacks 0BE9**, the final clause under condition (2).

```lean
theorem picardToWeilDivisorClassGroup_bijective [IsNormal X]
    (hsurj : Function.Surjective (picardToWeilDivisorClassGroup X)) :
    Function.Bijective (picardToWeilDivisorClassGroup X)
```

**`AlgebraicGeometry.forall_uniqueFactorizationMonoid_stalk_iff_isNormal_and_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/WeilDivisorClass/FirstChernClassBijective.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/WeilDivisorClass/FirstChernClassBijective.lean#L105). The attribute's comment: “the equivalence of conditions (1) and (2)”. References: SGA 2 XI (3.8), “partial”.

> **Stacks 0BE9.** For a locally Noetherian integral scheme the local rings are unique
> factorization domains exactly when the scheme is normal and the first Chern class
> `Pic(X) → Cl(X)` of Tag 0BE7 is surjective.
>
> Forwards, normality is `AlgebraicGeometry.isNormal_of_forall_uniqueFactorizationMonoid_stalk` and
> surjectivity is `AlgebraicGeometry.picardToWeilDivisorClassGroup_surjective`; backwards this is
> `AlgebraicGeometry.uniqueFactorizationMonoid_stalk_of_surjective_picardToWeilDivisorClassGroup`.

```lean
theorem forall_uniqueFactorizationMonoid_stalk_iff_isNormal_and_surjective :
    (∀ x : X, UniqueFactorizationMonoid (X.presheaf.stalk x)) ↔
      (IsNormal X ∧ Function.Surjective (picardToWeilDivisorClassGroup X))
```

**`AlgebraicGeometry.picardToWeilDivisorClassGroup_bijective_of_forall_uniqueFactorizationMonoid`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/WeilDivisorClass/FirstChernClassBijective.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/WeilDivisorClass/FirstChernClassBijective.lean#L123). The attribute's comment: “the isomorphism Pic(X) = Cl(X)”. References: EGA IV (21.6.10), “(i), injectivity, (ii)”; SGA 2 XI (3.7.1), “special case”; SGA 2 XI (3.8), “special case”.

> **Stacks 0BE9, the final clause.** On a locally Noetherian integral scheme whose local rings
> are unique factorization domains the first Chern class `Pic(X) → Cl(X)` is an isomorphism:
> factoriality makes `X` normal, so Tag 0BE8 gives injectivity, and
> `AlgebraicGeometry.picardToWeilDivisorClassGroup_surjective` gives surjectivity.

```lean
theorem picardToWeilDivisorClassGroup_bijective_of_forall_uniqueFactorizationMonoid
    (h : ∀ x : X, UniqueFactorizationMonoid (X.presheaf.stalk x)) :
    Function.Bijective (picardToWeilDivisorClassGroup X)
```

**`AlgebraicGeometry.forall_uniqueFactorizationMonoid_stalk_iff_isNormal_and_surjective_and_picardEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/WeilDivisorClass/FirstChernClassBijective.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/WeilDivisorClass/FirstChernClassBijective.lean#L155). The attribute's comment: “the full statement: (1) ⟺ (2), and in that case Pic(X) ≅ Cl(X)”. References: SGA 2 XI (3.7.1), “special case”; SGA 2 XI (3.8), “partial”.

> **Stacks 0BE9.** Let `X` be a locally Noetherian integral scheme and consider the first Chern
> class `Pic(X) → Cl(X)` of Tag 0BE7. The following are equivalent:
>
> 1. the local rings of `X` are unique factorization domains, and
> 2. `X` is normal and `Pic(X) → Cl(X)` is surjective.
>
> In this case `Pic(X) → Cl(X)` is an isomorphism.
>
> The equivalence is
> `AlgebraicGeometry.forall_uniqueFactorizationMonoid_stalk_iff_isNormal_and_surjective`, and the
> isomorphism is
> `AlgebraicGeometry.picardEquivWeilDivisorClassGroupOfForallUniqueFactorizationMonoid`, whose
> underlying map is the first Chern class.

```lean
theorem forall_uniqueFactorizationMonoid_stalk_iff_isNormal_and_surjective_and_picardEquiv :
    ((∀ x : X, UniqueFactorizationMonoid (X.presheaf.stalk x)) ↔
        IsNormal X ∧ Function.Surjective (picardToWeilDivisorClassGroup X)) ∧
      ((∀ x : X, UniqueFactorizationMonoid (X.presheaf.stalk x)) →
        ∃ e : Stacks.SheafOfModules.PicardGroup X.sheaf.obj X.ringCatSheaf.property ≃+
          weilDivisorClassGroup X, ∀ c, e c = picardToWeilDivisorClassGroup X c)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.28, Tag 02SE](https://stacks.math.columbia.edu/tag/02SE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
