---
declaration: section
origin: cited
lean: AlgebraicGeometry.locallyFinite_irreducibleComponents_image, Stacks.Divisors.PrimeDivisor, Stacks.Divisors.WeilDivisor, AlgebraicGeometry.PrimeDivisor, AlgebraicGeometry.WeilDivisor, AlgebraicGeometry.Scheme.ord, AlgebraicGeometry.Scheme.ord_eq_ordHom_of_coheight_eq_one, irreducibleSetEquivPoints
statement: formalized
proof: formalized
---

# 31.27 Weil divisors

Section 31.27 of the Stacks Project, [Tag 0BE0](https://stacks.math.columbia.edu/tag/0BE0). 7 tags here are carried by 10 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BE1, a lemma

[Tag 0BE1](https://stacks.math.columbia.edu/tag/0BE1) in the Stacks Project.

**`AlgebraicGeometry.locallyFinite_irreducibleComponents_image`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/WeilDivisors.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/WeilDivisors.lean#L85).

> **Stacks 0BE1.** The images of the irreducible components of a closed subscheme of a locally
> Noetherian scheme form a locally finite family in the ambient scheme.

```lean
theorem locallyFinite_irreducibleComponents_image
    {X Z : Scheme} [IsLocallyNoetherian X] (i : Z ⟶ X) [IsClosedImmersion i] :
    LocallyFinite (fun C : irreducibleComponents Z ↦ i '' (C : Set Z))
```

## Tag 0BE2, a definition

[Tag 0BE2](https://stacks.math.columbia.edu/tag/0BE2) in the Stacks Project.

**`Stacks.Divisors.PrimeDivisor`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FirstChernClass/PrimeDivisor.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FirstChernClass/PrimeDivisor.lean#L87). The attribute's comment: “part (1): prime divisors”.

> **Stacks 0BE2 (1).** A prime divisor of `X` is an integral closed subscheme of codimension
> one, recorded by its ideal sheaf.

```lean
structure PrimeDivisor (X : Scheme.{u})
```

**`Stacks.Divisors.WeilDivisor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FirstChernClass/PrimeDivisor.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FirstChernClass/PrimeDivisor.lean#L180). The attribute's comment: “part (2): Weil divisors”.

> **Stacks 0BE2 (2).** The group `Div(X)` of Weil divisors: integer-valued coefficient
> families indexed by the prime divisors of `X` whose nonzero prime divisors form a locally finite
> collection of closed subsets of `X`.

```lean
def WeilDivisor (X : Scheme.{u}) : AddSubgroup (PrimeDivisor X → ℤ)
```

**`AlgebraicGeometry.PrimeDivisor`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/PrimeDivisor.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/PrimeDivisor.lean#L58). The attribute's comment: “part (1): prime divisors”.

> A prime divisor of a scheme is an integral closed subscheme of codimension one, presented by
> its ideal sheaf. The codimension is that of the closure in the ambient scheme of the image of the
> generic point of the subscheme.

```lean
structure PrimeDivisor (X : Scheme.{u})
```

**`AlgebraicGeometry.WeilDivisor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/PrimeDivisor.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/PrimeDivisor.lean#L90). The attribute's comment: “part (2): Weil divisors”.

> The Weil divisors of a scheme: the integral coefficient families indexed by prime divisors
> whose prime divisors with nonzero coefficient have locally finite supports. The additive group
> structure is the coefficientwise one.

```lean
def WeilDivisor (X : Scheme.{u}) : AddSubgroup (PrimeDivisor X → ℤ)
```

## Tag 02RJ, a definition

[Tag 02RJ](https://stacks.math.columbia.edu/tag/02RJ) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.ord`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.ord#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch31.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch31.lean#L30) (StacksFrontier): “the definition, indexed by the generic point ξ of Z (coheight ξ = 1)”.
- [`AlgebraicGeometry.Scheme.ord_eq_ordHom_of_coheight_eq_one`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.ord_eq_ordHom_of_coheight_eq_one#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch31.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch31.lean#L32) (StacksFrontier): “at a codimension-one point the value is ord of the stalk (Tag 02MD)”.
- [`irreducibleSetEquivPoints`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=irreducibleSetEquivPoints#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch31.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch31.lean#L34) (StacksFrontier): “prime divisors Z correspond to their generic points ξ, codim Z = coheight ξ”.

## Tag 02RL, a lemma

[Tag 02RL](https://stacks.math.columbia.edu/tag/02RL) in the Stacks Project.

**`Stacks.Chow.locallyFinite_closure_notMem_range_algebraMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Vocabulary/PrincipalCycle.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Vocabulary/PrincipalCycle.lean#L164). The attribute's comment: “the prime divisors with f ∉ O_{X,ξ}; no hypothesis f ≠ 0 needed”.

> **Stacks 02RL.** On a locally Noetherian integral scheme the prime divisors at whose generic
> point `ξ` a rational function `f` does not lie in the local ring `O_{X,ξ}` form a locally finite
> collection of closed subsets of `X`. A prime divisor is indexed by its generic point, so the
> collection is the family of closures of the codimension-one points `z` with `f ∉ O_{X,z}`.

```lean
theorem locallyFinite_closure_notMem_range_algebraMap (X : Scheme.{u}) [IsIntegral X]
    [IsLocallyNoetherian X] (f : X.functionField) :
    LocallyFinite fun z : {z : X // coheight z = 1 ∧
        f ∉ Set.range (algebraMap (X.presheaf.stalk z) X.functionField)} ↦
      closure ({(z : X)} : Set X)
```

**`Stacks.Chow.locallyFiniteSupport_ord`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Vocabulary/PrincipalCycle.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Vocabulary/PrincipalCycle.lean#L185). The attribute's comment: “the prime divisors with ord_Z(f) ≠ 0”.

> **Stacks 02RL.** On a locally Noetherian integral scheme the prime divisors along which a
> rational function `f` has nonzero order form a locally finite collection: the support of
> `z ↦ ord_z(f)` meets a neighbourhood of every point in a finite set.

```lean
theorem locallyFiniteSupport_ord (X : Scheme.{u}) [IsIntegral X] [IsLocallyNoetherian X]
    (f : X.functionField) : LocallyFiniteSupport (X.ord f)
```

## Tag 0BE3, a definition

[Tag 0BE3](https://stacks.math.columbia.edu/tag/0BE3) in the Stacks Project.

**`Stacks.Chow.principalCycle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Vocabulary/PrincipalCycle.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Vocabulary/PrincipalCycle.lean#L208). References: EGA IV (21.6.7), “partial”.

> **Stacks 0BE3.** The principal divisor `div(f) = ∑_Z ord_Z(f) [Z]` of a rational function on
> a locally Noetherian integral scheme, as an algebraic cycle: the integral closed subscheme
> `closure {z}` is indexed by its generic point `z`, and carries the coefficient `ord_z(f)`. Local
> finiteness of the family of prime divisors involved is Stacks 02RL.

```lean
def principalCycle (X : Scheme.{u}) [IsIntegral X] [IsLocallyNoetherian X]
    (f : X.functionField) : AlgebraicCycle X ℤ
```

## Tag 02RP, a lemma

[Tag 02RP](https://stacks.math.columbia.edu/tag/02RP) in the Stacks Project.

**`Stacks.Chow.principalCycle_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Vocabulary/PrincipalCycle.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Vocabulary/PrincipalCycle.lean#L232). References: EGA IV (21.1.3), “(21.1.3.1)”.

> **Stacks 02RP.** The principal divisor of a product of nonzero rational functions is the sum
> of the principal divisors.

```lean
theorem principalCycle_mul (X : Scheme.{u}) [IsIntegral X] [IsLocallyNoetherian X]
    {f g : X.functionField} (hf : f ≠ 0) (hg : g ≠ 0) :
    principalCycle X (f * g) = principalCycle X f + principalCycle X g
```

## Tag 0BE4, a definition

[Tag 0BE4](https://stacks.math.columbia.edu/tag/0BE4) in the Stacks Project.

**`AlgebraicGeometry.weilDivisorClassGroup`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/WeilDivisorClass/ClassGroup.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/WeilDivisorClass/ClassGroup.lean#L61).

> The Weil divisor class group `Cl(X)` of a locally Noetherian integral
> scheme: the group of Weil divisors modulo the subgroup of principal Weil divisors.

```lean
abbrev weilDivisorClassGroup : Type u
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.27, Tag 0BE0](https://stacks.math.columbia.edu/tag/0BE0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
