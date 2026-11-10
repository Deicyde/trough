---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidInAlgebraicSpaces.inertiaGroupoid, AlgebraicGeometry.Stack.inertiaComparison_comp_toBase, AlgebraicGeometry.Stack.inertiaComparisonForgetfulIso, AlgebraicGeometry.Stack.isEquivalence_inertiaComparison, AlgebraicGeometry.Stack.inertiaQuotientStackSquare, AlgebraicGeometry.Stack.isTwoFibreProduct_inertiaQuotientStackSquare, AlgebraicGeometry.Stack.isTwoFibreProduct_quotientStackInertiaSquare, AlgebraicGeometry.Stack.isTwoFibreProduct_quotientStackInertiaSquareInGroupoids
statement: formalized
proof: formalized
---

# 78.26 Inertia and quotient stacks

Section 78.26 of the Stacks Project, [Tag 06PA](https://stacks.math.columbia.edu/tag/06PA). 2 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06PB, a lemma

[Tag 06PB](https://stacks.math.columbia.edu/tag/06PB) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.inertiaGroupoid`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/InertiaGroupoid.lean, line 890](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/InertiaGroupoid.lean#L890). The attribute's comment: “the groupoid (G, R', s', t', c')”.

> The groupoid `(G, R', s', t', c')` in algebraic spaces over `B` built from a groupoid
> `(U, R, s, t, c)` in algebraic spaces over `B`: its object space is the stabilizer `G/U`, its
> arrow space is `R' = R ×_{s, U} G`, and its source, target and composition are the morphisms
> `s'`, `t'` and `c'`.

```lean
noncomputable def inertiaGroupoid
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    GroupoidInAlgebraicSpaces C S hS B
```

**`AlgebraicGeometry.Stack.inertiaComparison_comp_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InertiaQuotientStackComparison.lean, line 1373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/InertiaQuotientStackComparison.lean#L1373). The attribute's comment: “second assertion: the comparison [G/R'] ⟶ I_{[U/R]} is over the site”.

> The comparison `[G/R'] ⟶ ℐ_{[U/R]}` composed with the structure functor of the inertia of
> `[U/R]` is the structure functor of `[G/R']`: it is a 1-morphism of categories over the big fppf
> site.

```lean
theorem inertiaComparison_comp_toBase (G : GroupoidInAlgebraicSpaces C S hS B) :
    (inertiaComparison G).toFunctor ⋙ RelativeInertia.toBase (quotientStack G).p =
      (quotientStack (inertiaGroupoid G)).p
```

**`AlgebraicGeometry.Stack.inertiaComparisonForgetfulIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InertiaQuotientStackComparison.lean, line 1382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/InertiaQuotientStackComparison.lean#L1382). The attribute's comment: “second assertion: the comparison is a 1-morphism over [U/R]”.

> Composing the comparison `[G/R'] ⟶ ℐ_{[U/R]}` with the forgetful 1-morphism `ℐ_{[U/R]} ⟶ [U/R]`
> gives the 1-morphism `[G/R'] ⟶ [U/R]` of Stacks 046Q induced by the forgetful morphism of groupoids
> `(G, R', s', t', c') ⟶ (U, R, s, t, c)`, by an isomorphism of functors.

```lean
noncomputable def inertiaComparisonForgetfulIso
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    ((inertiaComparison G).toFunctor ⋙ RelativeInertia.π (quotientStack G).p) ≅
      (quotientStackMap (inertiaForgetful G)).toFunctor
```

**`AlgebraicGeometry.Stack.isEquivalence_inertiaComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InertiaQuotientStackComparison.lean, line 1401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/InertiaQuotientStackComparison.lean#L1401). The attribute's comment: “second assertion: I_{[U/R]} = [G/R'], the comparison is an equivalence”.

> The underlying functor of the comparison `[G/R'] ⟶ ℐ_{[U/R]}` is an equivalence of categories:
> the quotient stack of the inertia groupoid `(G, R', s', t', c')` is the inertia stack of `[U/R]`.

```lean
theorem isEquivalence_inertiaComparison (G : GroupoidInAlgebraicSpaces C S hS B) :
    (inertiaComparison G).toFunctor.IsEquivalence
```

## Tag 06PC, a lemma

[Tag 06PC](https://stacks.math.columbia.edu/tag/06PC) in the Stacks Project.

**`AlgebraicGeometry.Stack.inertiaQuotientStackSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/InertiaQuotientStackSquare.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/InertiaQuotientStackSquare.lean#L116). The attribute's comment: “the canonical square, lower-left corner as the quotient stack [G/R'] of 06PB”.

> For a groupoid `(U, R, s, t, c)` in algebraic spaces over `B` with stabilizer group algebraic
> space `G/U` (Stacks 0448), the 2-commutative square
>
> ```
> 𝒮_G  ------>  𝒮_U
>  |             |
>  v             v
> [G/R'] ----> [U/R]
> ```
>
> of stacks in groupoids over the big fppf site: the apex is the stack `𝒮_G` of the stabilizer,
> the horizontal arrows are the 1-morphism of Stacks 0458 induced by `G → U` and the projection of
> Stacks 044R for the inertia groupoid `(G, R', s', t', c')` of Stacks 06PB, and the vertical
> arrows are that projection for `(U, R, s, t, c)` and the 1-morphism of Stacks 046Q induced by
> `AlgebraicGeometry.GroupoidInAlgebraicSpaces.inertiaForgetful`. The filler is the 2-isomorphism
> of Stacks 046Q.

```lean
noncomputable def inertiaQuotientStackSquare (G : GroupoidInAlgebraicSpaces C S hS B) :
    let J := BigFppfOver.topology C S hS
    let Q : StackInGroupoids (BigFppfOver C S hS) J :=
      ⟨quotientStack G, isStackInGroupoids_quotientStack G⟩
    let I : StackInGroupoids (BigFppfOver C S hS) J :=
      ⟨quotientStack (inertiaGroupoid G), isStackInGroupoids_quotientStack (inertiaGroupoid G)⟩
    let W : StackInGroupoids (BigFppfOver C S hS) J :=
      ⟨liftedFibredCategory G.objects, isStackInGroupoids_liftedFibredCategory G.objects⟩
    Bicategory.TwoCommSq
      (Bicategory.InducedBicategory.mkHom (liftedQuotientStackProjection G) : W ⟶ Q)
      (Bicategory.InducedBicategory.mkHom (quotientStackMap (inertiaForgetful G)) : I ⟶ Q)
```

**`AlgebraicGeometry.Stack.isTwoFibreProduct_inertiaQuotientStackSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/InertiaQuotientStackSquare.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/InertiaQuotientStackSquare.lean#L159). The attribute's comment: “that square is 2-cartesian, lower-left corner as the quotient stack [G/R'] of 06PB”.

> The square
>
> ```
> 𝒮_G  ------>  𝒮_U
>  |             |
>  v             v
> [G/R'] ----> [U/R]
> ```
>
> of `AlgebraicGeometry.Stack.inertiaQuotientStackSquare` is a 2-fibre product (Stacks 003Q) in the
> bicategory of stacks in groupoids over the big fppf site, i.e. the diagram is 2-cartesian.

```lean
noncomputable def isTwoFibreProduct_inertiaQuotientStackSquare
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    Bicategory.IsTwoFibreProduct (inertiaQuotientStackSquare G)
```

**`AlgebraicGeometry.Stack.isTwoFibreProduct_quotientStackInertiaSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InertiaQuotientStackSquareFibred.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/InertiaQuotientStackSquareFibred.lean#L249). The attribute's comment: “the canonical square with corners S_G, S_U, I_[U/R], [U/R] is 2-cartesian”.

> Assume `B → S` and `(U, R, s, t, c)` as in Stacks 044Q (1). Let `G/U` be the stabilizer group
> algebraic space of the groupoid `(U, R, s, t, c, e, i)` (Stacks 0448). Then the canonical diagram
>
> ```
> 𝒮_G  ------>  𝒮_U
>  |             |
>  v             v
> ℐ_{[U/R]} --> [U/R]
> ```
>
> of `AlgebraicGeometry.Stack.quotientStackInertiaSquare` is 2-cartesian, i.e. a 2-fibre product
> in the sense of Stacks 003Q, in the 2-category of categories fibred in groupoids over the big fppf
> site (Stacks 02XS).

```lean
noncomputable def isTwoFibreProduct_quotientStackInertiaSquare
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    Bicategory.IsTwoFibreProduct (quotientStackInertiaSquare G)
```

**`AlgebraicGeometry.Stack.isTwoFibreProduct_quotientStackInertiaSquareInGroupoids`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InertiaQuotientStackSquareFibred.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/InertiaQuotientStackSquareFibred.lean#L310). The attribute's comment: “that square, in the 2-category of stacks in groupoids, is 2-cartesian”.

> Assume `B → S` and `(U, R, s, t, c)` as in Stacks 044Q (1) and let `G/U` be the stabilizer
> group algebraic space of `(U, R, s, t, c, e, i)` (Stacks 0448). Then the canonical diagram
>
> ```
> 𝒮_G  ------>  𝒮_U
>  |             |
>  v             v
> ℐ_{[U/R]} --> [U/R]
> ```
>
> is 2-cartesian in the 2-category of stacks in groupoids over the big fppf site (Stacks 02ZK).

```lean
noncomputable def isTwoFibreProduct_quotientStackInertiaSquareInGroupoids
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    Bicategory.IsTwoFibreProduct (quotientStackInertiaSquareInGroupoids G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.26, Tag 06PA](https://stacks.math.columbia.edu/tag/06PA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
