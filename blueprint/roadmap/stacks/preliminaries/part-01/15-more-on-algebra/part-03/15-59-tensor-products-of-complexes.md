---
declaration: section
origin: cited
lean: TotalTensorComplex.cochainComplex_symmetricMonoidalCategory, TotalTensorComplex.tensorTotal_preserves_homotopy_and_descends, TotalTensorComplex.homotopyCategory_symmetricMonoidalCategory, TotalTensorComplex.tleft_isTriangulated, TotalTensorComplex.tright_isTriangulated
statement: formalized
proof: formalized
---

# 15.59 Tensor products of complexes

Section 15.59 of the Stacks Project, [Tag 0GWN](https://stacks.math.columbia.edu/tag/0GWN). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FNI, a lemma

[Tag 0FNI](https://stacks.math.columbia.edu/tag/0FNI) in the Stacks Project.

**`TotalTensorComplex.cochainComplex_symmetricMonoidalCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TensorComplex/Monoidal.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/TensorComplex/Monoidal.lean#L116).

> The category of cochain complexes of modules over a commutative ring, with tensor product
> given by the total complex of the degreewise tensor product, is symmetric monoidal. On the
> summand of bidegree `(p, q)`, its braiding is the ordinary symmetry of tensor products multiplied
> by the Koszul sign `(-1)^(p*q)`.

```lean
public theorem cochainComplex_symmetricMonoidalCategory (R : Type u) [CommRing R] :
    ∃ s : SymmetricCategory (CochainComplex (ModuleCat R) ℤ),
      ∀ (K L : CochainComplex (ModuleCat R) ℤ) (p q n : ℤ) (h : p + q = n),
        HomologicalComplex.ιTensorObj K L p q n h ≫
            (s.toBraidedCategory.braiding K L).hom.f n =
          ((p * q).negOnePow : ℤˣ) •
            ((β_ (K.X p) (L.X q)).hom ≫
              HomologicalComplex.ιTensorObj L K q p n (by simpa [add_comm] using h))
```

## Tag 064I, a lemma

[Tag 064I](https://stacks.math.columbia.edu/tag/064I) in the Stacks Project.

**`TotalTensorComplex.tensorTotal_preserves_homotopy_and_descends`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TensorComplex/Monoidal.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/TensorComplex/Monoidal.lean#L129). References: SGA 4½ Etat 0 (1.3.3), “tensor over ModuleCat R”.

> Tensoring with a fixed complex and taking the total complex preserves homotopic maps,
> and therefore induces an endofunctor of the homotopy category of complexes.

```lean
public theorem tensorTotal_preserves_homotopy_and_descends {R : Type u} [CommRing R]
    (P : CochainComplex (ModuleCat.{u} R) ℤ) :
    let T := (curriedTensor (ModuleCat.{u} R)).map₂CochainComplex.flip.obj P
    (∀ {L M : CochainComplex (ModuleCat.{u} R) ℤ} {f g : L ⟶ M},
      homotopic (ModuleCat.{u} R) (ComplexShape.up ℤ) f g →
        homotopic (ModuleCat.{u} R) (ComplexShape.up ℤ) (T.map f) (T.map g)) ∧
    ∃ T' : HomotopyCategory (ModuleCat.{u} R) (ComplexShape.up ℤ) ⥤
        HomotopyCategory (ModuleCat.{u} R) (ComplexShape.up ℤ),
      HomotopyCategory.quotient (ModuleCat.{u} R) (ComplexShape.up ℤ) ⋙ T' =
        T ⋙ HomotopyCategory.quotient (ModuleCat.{u} R) (ComplexShape.up ℤ)
```

## Tag 0GWP, a lemma

[Tag 0GWP](https://stacks.math.columbia.edu/tag/0GWP) in the Stacks Project.

**`TotalTensorComplex.homotopyCategory_symmetricMonoidalCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TensorComplex/Monoidal.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/TensorComplex/Monoidal.lean#L180).

> The homotopy category of cochain complexes of modules over a commutative ring is symmetric
> monoidal under the total tensor product. Its associator and Koszul braiding are induced from the
> corresponding canonical constraints on complexes.

```lean
public theorem homotopyCategory_symmetricMonoidalCategory (R : Type u) [CommRing R] :
    ∃ sC : SymmetricCategory (CochainComplex (ModuleCat.{u} R) ℤ),
      (∀ (K L : CochainComplex (ModuleCat.{u} R) ℤ) (p q n : ℤ) (h : p + q = n),
        HomologicalComplex.ιTensorObj K L p q n h ≫
            (sC.toBraidedCategory.braiding K L).hom.f n =
          ((p * q).negOnePow : ℤˣ) •
            ((β_ (K.X p) (L.X q)).hom ≫
              HomologicalComplex.ιTensorObj L K q p n (by simpa [add_comm] using h))) ∧
      letI := sC
      ∃ mK : MonoidalCategory
          (HomotopyCategory (ModuleCat.{u} R) (ComplexShape.up ℤ)),
        letI := mK
        ∃ sK : SymmetricCategory
            (HomotopyCategory (ModuleCat.{u} R) (ComplexShape.up ℤ)),
          letI := sK
          Nonempty
            (HomotopyCategory.quotient (ModuleCat.{u} R) (ComplexShape.up ℤ)).Braided
```

## Tag 064J, a lemma

[Tag 064J](https://stacks.math.columbia.edu/tag/064J) in the Stacks Project.

**`TotalTensorComplex.tleft_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TensorComplex/Monoidal.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/TensorComplex/Monoidal.lean#L261).

> Tensoring on the left with a fixed complex and totalizing is an exact functor of
> triangulated categories on the homotopy category.
>
> Stated for an arbitrary preadditive monoidal category whose tensor product is additive in each
> variable, which is the generality the statement holds in. Module categories are the case of
> interest, at any module universe: the instances above hold for `ModuleCat.{max u v} R` as well
> as for `ModuleCat.{u} R`.

```lean
public theorem tleft_isTriangulated (G : CochainComplex C ℤ) :
    ∃ e : (Tleft G).CommShift ℤ,
      @Functor.IsTriangulated _ _ _ _ _ _ (Tleft G) e _ _ _ _ _ _ _ _
```

**`TotalTensorComplex.tright_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TensorComplex/Monoidal.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/TensorComplex/Monoidal.lean#L270).

> Tensoring on the right with a fixed complex and totalizing is an exact functor of
> triangulated categories on the homotopy category. This is genuinely distinct from
> `tleft_isTriangulated`: the two differ by the Koszul sign in the commutativity constraint.

```lean
public theorem tright_isTriangulated (G : CochainComplex C ℤ) :
    ∃ e : (Tright G).CommShift ℤ,
      @Functor.IsTriangulated _ _ _ _ _ _ (Tright G) e _ _ _ _ _ _ _ _
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.59, Tag 0GWN](https://stacks.math.columbia.edu/tag/0GWN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
