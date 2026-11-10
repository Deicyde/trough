---
declaration: section
origin: cited
lean: AlgebraicGeometry.SheafOfModules.wedgeProduct, AlgebraicGeometry.SheafOfModules.wedgeProduct_summand_unit_apply, AlgebraicGeometry.SheafOfModules.deRhamCupProduct, AlgebraicGeometry.SheafOfModules.deRhamCupProduct_assoc, AlgebraicGeometry.SheafOfModules.deRhamCupProduct_comm, AlgebraicGeometry.SheafOfModules.deRhamCohomologyCup_assoc, AlgebraicGeometry.SheafOfModules.deRhamCohomologyCup_comm, AlgebraicGeometry.SheafOfModules.wedgeProduct_summand_assoc
statement: formalized
proof: formalized
---

# 50.4 Cup product

Section 50.4 of the Stacks Project, [Tag 0FM1](https://stacks.math.columbia.edu/tag/0FM1). 4 tags here are carried by 27 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FM2, an equation

[Tag 0FM2](https://stacks.math.columbia.edu/tag/0FM2) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.wedgeProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/CupProduct/WedgeProduct.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/CupProduct/WedgeProduct.lean#L227).

> **Stacks Project, Tag 0FM2.** The wedge product
> `∧ : Tot(Ω^• ⊗_A Ω^•) ⟶ Ω^•` of relative differential forms, as a morphism of complexes of
> sheaves of `A`-modules: on the `(p, q)` summand of the total complex it is wedge multiplication of
> a `p`-form by a `q`-form, and the graded Leibniz rule is exactly the statement that this family
> commutes with the differentials.

```lean
noncomputable def wedgeProduct : tensorSquare B D ⟶ deRhamComplex B D
```

**`AlgebraicGeometry.SheafOfModules.wedgeProduct_summand_unit_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/CupProduct/WedgeProduct.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/CupProduct/WedgeProduct.lean#L244).

> **Stacks Project, Tag 0FM2.** On the `(p, q)` summand of the total complex the wedge product
> sends a local pure tensor `ω ⊗ η` to the wedge product `ω ∧ η`.
>
> The two sides live in the exterior powers of degrees `((p + q : ℕ) : ℤ)` and `(p : ℤ) + q`, which
> is why this is a heterogeneous equality.

```lean
theorem wedgeProduct_summand_unit_apply (p q : ℕ) (U : (Opens X.carrier)ᵒᵖ)
    (ω : (deRhamTerm B p).val.obj U) (η : (deRhamTerm B q).val.obj U) :
    HEq ((HomologicalComplex.ιMapBifunctor
      (D := _root_.SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} A))
            (deRhamComplex B D) (deRhamComplex B D)
            (Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u} A) (ComplexShape.up ℕ) p q
              (p + q) rfl ≫
          (wedgeProduct B D).f (p + q)).val.app U
        (((PresheafOfModules.sheafificationAdjunction
          (R := Stacks.SheafOfModules.Tensor.ringSheaf A)
          (𝟙 (Stacks.SheafOfModules.Tensor.ringSheaf A).obj)).unit.app
          (PresheafOfModules.tensorObj ((deRhamTerm B p)).val ((deRhamTerm B q)).val)).app U
            (ω ⊗ₜ[A.obj.obj U] η)))
      ((B.exterior.mul (p : ℤ) (q : ℤ)).app U ω η)
```

## Tag 0FM3, a lemma

[Tag 0FM3](https://stacks.math.columbia.edu/tag/0FM3) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.deRhamCupProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/CupProduct/CupProductOnCohomology.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/CupProduct/CupProductOnCohomology.lean#L214). The attribute's comment: “the cup product on de Rham cohomology, from the wedge product of 0FM2”.

> **Stacks Project, Tag 0FM3.** The cup product
>
> `∪ : H^i_{dR}(X/S) × H^j_{dR}(X/S) ⟶ H^{i + j}_{dR}(X/S)`
>
> on relative de Rham cohomology: the cup product of Cohomology, Section 0FKU paired with the wedge
> product of Tag 0FM2. It is bilinear over the ring of global sections of the base ring sheaf.

```lean
noncomputable def deRhamCupProduct (i j : ℤ) :
    deRhamCohomology B D i → deRhamCohomology B D j → deRhamCohomology B D (i + j)
```

**`AlgebraicGeometry.SheafOfModules.deRhamCupProduct_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/CupProduct/CupProductOnCohomology.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/CupProduct/CupProductOnCohomology.lean#L249). The attribute's comment: “the cup product on de Rham cohomology is associative”.

> **Stacks Project, Tag 0FM3.** The cup product on `H^*_{dR}(X/S)` is **associative**. This is
> Cohomology, Lemma 0FP4 together with the associativity of the wedge product.

```lean
theorem deRhamCupProduct_assoc (i j k : ℤ) (ξ : deRhamCohomology B D i)
    (η : deRhamCohomology B D j) (ζ : deRhamCohomology B D k) :
    reindexDeRhamCohomology B D (add_assoc i j k)
        (deRhamCupProduct B D c (i + j) k (deRhamCupProduct B D c i j ξ η) ζ) =
      deRhamCupProduct B D c i (j + k) ξ (deRhamCupProduct B D c j k η ζ)
```

**`AlgebraicGeometry.SheafOfModules.deRhamCupProduct_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/CupProduct/CupProductOnCohomology.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/CupProduct/CupProductOnCohomology.lean#L260). The attribute's comment: “the cup product on de Rham cohomology is graded commutative, sign (-1)^(ij)”.

> **Stacks Project, Tag 0FM3.** The cup product on `H^*_{dR}(X/S)` is **graded commutative**:
> `ξ ∪ η = (-1)^{ij} η ∪ ξ` for `ξ` of degree `i` and `η` of degree `j`. This is Cohomology, Lemma
> 0FP5 together with the graded commutativity of the wedge product.

```lean
theorem deRhamCupProduct_comm (i j : ℤ) (ξ : deRhamCohomology B D i)
    (η : deRhamCohomology B D j) :
    deRhamCupProduct B D c i j ξ η =
      ((i * j).negOnePow : ℤ) • reindexDeRhamCohomology B D (add_comm j i)
        (deRhamCupProduct B D c j i η ξ)
```

**`AlgebraicGeometry.SheafOfModules.deRhamCohomologyCup_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/CupProduct/DeRhamCupProductLaws.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/CupProduct/DeRhamCupProductLaws.lean#L87). The attribute's comment: “the cup product on H^*_dR(X/S), the cup product of Cohomology Section 0FKU composed with the wedge product of 0FM2, is associative; no parameter, no hypothesis”.

> **Stacks Project, Tag 0FM3.** The cup product on `H^*_{dR}(X/S)` is **associative**:
> `(ξ ∪ η) ∪ ζ = ξ ∪ (η ∪ ζ)`, the left-hand side transported from degree `(i + j) + k` to degree
> `i + (j + k)`. This is Cohomology, Lemma 0FP4 together with the associativity of the wedge
> product.

```lean
theorem deRhamCohomologyCup_assoc (i j k : ℤ) (ξ : deRhamCohomology B D i)
    (η : deRhamCohomology B D j) (ζ : deRhamCohomology B D k) :
    reindexDeRhamCohomology B D (add_assoc i j k)
        (deRhamCohomologyCup B D (i + j) k (deRhamCohomologyCup B D i j ξ η) ζ) =
      deRhamCohomologyCup B D i (j + k) ξ (deRhamCohomologyCup B D j k η ζ)
```

**`AlgebraicGeometry.SheafOfModules.deRhamCohomologyCup_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/CupProduct/DeRhamCupProductLaws.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/CupProduct/DeRhamCupProductLaws.lean#L103). The attribute's comment: “the cup product on H^*_dR(X/S), the cup product of Cohomology Section 0FKU composed with the wedge product of 0FM2, is graded commutative with sign (-1)^(ij); no parameter, no hypothesis”.

> **Stacks Project, Tag 0FM3.** The cup product on `H^*_{dR}(X/S)` is **graded commutative**:
> `ξ ∪ η = (-1)^{ij} η ∪ ξ` for `ξ` of degree `i` and `η` of degree `j`, the right-hand side
> transported from degree `j + i` to degree `i + j`. This is Cohomology, Lemma 0FP5 together with
> the graded commutativity of the wedge product.

```lean
theorem deRhamCohomologyCup_comm (i j : ℤ) (ξ : deRhamCohomology B D i)
    (η : deRhamCohomology B D j) :
    deRhamCohomologyCup B D i j ξ η =
      ((i * j).negOnePow : ℤ) • reindexDeRhamCohomology B D (add_comm j i)
        (deRhamCohomologyCup B D j i η ξ)
```

**`AlgebraicGeometry.SheafOfModules.wedgeProduct_summand_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/CupProduct/GradedCommutativity.lean, line 430](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/CupProduct/GradedCommutativity.lean#L430). The attribute's comment: “the wedge product of 0FM2 is associative”.

> **Stacks Project, Tag 0FM3.** The wedge product of Tag 0FM2 is **associative** on the summands
> of the total complex: the two bracketings of a triple wedge of local forms agree.
>
> This is the associativity clause of the proof of Tag 0FM3, "the fact that `∧` is associative"; the
> associativity of the cup product on `H^*_{dR}` is this together with Cohomology, Tag 0FP4.

```lean
theorem wedgeProduct_summand_assoc (p q r : ℕ) (U : (Opens X.carrier)ᵒᵖ)
    (ω : (deRhamTerm B p).val.obj U) (η : (deRhamTerm B q).val.obj U)
    (ζ : (deRhamTerm B r).val.obj U) :
    HEq (summandValue B D (wedgeProduct B D) (p + q) r U
        (summandValue B D (wedgeProduct B D) p q U ω η) ζ)
      (summandValue B D (wedgeProduct B D) p (q + r) U ω
        (summandValue B D (wedgeProduct B D) q r U η ζ))
```

**`AlgebraicGeometry.SheafOfModules.wedgeProduct_summand_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/CupProduct/GradedCommutativity.lean, line 453](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/CupProduct/GradedCommutativity.lean#L453). The attribute's comment: “the wedge product of 0FM2 is graded commutative, with the sign (-1)^(pq)”.

> **Stacks Project, Tag 0FM3.** The wedge product of Tag 0FM2 is **graded commutative** on the
> summands of the total complex: on the local pure tensor `ω ⊗ η` of a `p`-form and a `q`-form its
> value is `(-1)^{pq}` times its value on `η ⊗ ω`.
>
> This is the graded commutativity clause of the proof of Tag 0FM3, "the fact that `∧` is graded
> commutative"; the graded commutativity of the cup product on `H^*_{dR}` is this together with
> Cohomology, Tag 0FP5.

```lean
theorem wedgeProduct_summand_comm (p q : ℕ) (U : (Opens X.carrier)ᵒᵖ)
    (ω : (deRhamTerm B p).val.obj U) (η : (deRhamTerm B q).val.obj U) :
    HEq (summandValue B D (wedgeProduct B D) p q U ω η)
      ((-1 : ℤ) ^ (p * q) • summandValue B D (wedgeProduct B D) q p U η ω)
```

## Tag 0FU6, a remark

[Tag 0FU6](https://stacks.math.columbia.edu/tag/0FU6) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.deRhamDifferentialGradedAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/Basic.lean, line 430](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/Basic.lean#L430). The attribute's comment: “relative_de_rham_dga”.

> The relative de Rham complex of `φ`, with wedge multiplication and the unit of the exterior
> algebra, as a sheaf of differential graded `A`-algebras.

```lean
noncomputable def deRhamDifferentialGradedAlgebra :
    _root_.SheafOfModules.DifferentialGradedAlgebra.{u, u} (underlyingRingSheaf A)
```

**`AlgebraicGeometry.SheafOfModules.deRhamDifferentialGradedAlgebra_complex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/Basic.lean, line 496](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/Basic.lean#L496). The attribute's comment: “relative_de_rham_dga”.

> The complex underlying the relative de Rham differential graded algebra is the relative de
> Rham complex, extended by zero to negative degrees.

```lean
theorem deRhamDifferentialGradedAlgebra_complex :
    (deRhamDifferentialGradedAlgebra B D).complex = deRhamComplexInt B D
```

**`AlgebraicGeometry.SheafOfModules.deRhamDifferentialGradedAlgebra_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/Basic.lean, line 502](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/Basic.lean#L502). The attribute's comment: “relative_de_rham_dga”.

> Multiplication in the relative de Rham differential graded algebra is wedge multiplication of
> differential forms, on every pair of homogeneous local sections.

```lean
theorem deRhamDifferentialGradedAlgebra_mul (p q : ℕ) (U : (Opens X.carrier)ᵒᵖ)
    (ω : ((deRhamDifferentialGradedAlgebra B D).complex.X (p : ℤ)).val.obj U)
    (η : ((deRhamDifferentialGradedAlgebra B D).complex.X (q : ℤ)).val.obj U)
    (ω' : (B.exteriorPower p).val.obj U) (η' : (B.exteriorPower q).val.obj U)
    (hω : HEq ω ω') (hη : HEq η η') :
    HEq (((deRhamDifferentialGradedAlgebra B D).mul (p : ℤ) (q : ℤ)).app U ω η)
      (formProduct B p q U ω' η')
```

**`AlgebraicGeometry.SheafOfModules.deRhamDifferentialGradedAlgebra_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/Basic.lean, line 515](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/Basic.lean#L515). The attribute's comment: “relative_de_rham_dga”.

> The unit of the relative de Rham differential graded algebra is the unit of the exterior
> algebra of `Ω`.

```lean
theorem deRhamDifferentialGradedAlgebra_one (U : (Opens X.carrier)ᵒᵖ) :
    HEq ((deRhamDifferentialGradedAlgebra B D).one.eval U) (B.exterior.one.eval U)
```

**`AlgebraicGeometry.SheafOfModules.summandValue_wedgeProduct_heq_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/RelativeCupProduct.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/RelativeCupProduct.lean#L128). The attribute's comment: “the multiplication of mu is that of the differential graded algebra”.

> **The multiplication `deRhamDerivedMul` is that of the differential graded algebra
> `Ω^•`** (the first assertion of Tag 0FU6, `deRhamDifferentialGradedAlgebra`): on the summand
> `Ω^p ⊗ Ω^q` of the total complex the wedge product of Tag 0FM2 underlying `deRhamDerivedMul`
> sends a local pure tensor `ω ⊗ η` to the product `ω · η` in the differential graded algebra.

```lean
theorem summandValue_wedgeProduct_heq_mul (p q : ℕ) (U : (Opens X.carrier)ᵒᵖ)
    (ω : (deRhamTerm B p).val.obj U) (η : (deRhamTerm B q).val.obj U)
    (x : ((deRhamDifferentialGradedAlgebra B D).complex.X (p : ℤ)).val.obj U)
    (y : ((deRhamDifferentialGradedAlgebra B D).complex.X (q : ℤ)).val.obj U)
    (hx : HEq x ω) (hy : HEq y η) :
    HEq (((deRhamDifferentialGradedAlgebra B D).mul (p : ℤ) (q : ℤ)).app U x y)
      (summandValue B D (wedgeProduct B D) p q U ω η)
```

**`AlgebraicGeometry.Scheme.deRhamRelativeCupProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/RelativeCupProduct.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/RelativeCupProduct.lean#L312). The attribute's comment: “the relative cup product mu of a commutative square”.

> **Stacks Project, Tag 0FU6: the relative cup product of a commutative square.**  For a
> commutative square of schemes
>
> ```
> X --f--> Y
> |p       |q
> v        v
> S --h--> T
> ```
>
> the relative cup product
> `μ : Rf_*Ω^•_{X/S} ⊗^𝐋_{q⁻¹𝒪_T} Rf_*Ω^•_{X/S} ⟶ Rf_*Ω^•_{X/S}` in `D(Y, q⁻¹𝒪_T)`: the relative cup
> product of Tag 0B68 for the morphism of ringed spaces `(X, p⁻¹𝒪_S) ⟶ (Y, q⁻¹𝒪_T)` of the square,
> followed by `Rf_*` of the wedge multiplication `Ω^•_{X/S} ⊗^𝐋 Ω^•_{X/S} ⟶ Ω^•_{X/S}` of the
> differential graded `p⁻¹𝒪_S`-algebra `Ω^•_{X/S}`.

```lean
noncomputable def deRhamRelativeCupProduct (w : f ≫ q = p ≫ h) :
    ((derivedTensorProductFunctor (SheafOfModules.baseRingedSpace (X := Y.toRingedSpace)
          ((TopCat.Sheaf.pullback CommRingCat.{u} q.base).obj T.sheaf)).sheaf).obj
        ((derivedPushforward (squareHom w)).obj (deRhamDerived p))).obj
        ((derivedPushforward (squareHom w)).obj (deRhamDerived p)) ⟶
      (derivedPushforward (squareHom w)).obj (deRhamDerived p)
```

**`AlgebraicGeometry.Scheme.deRhamRelativeCupProduct_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/RelativeCupProduct.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/RelativeCupProduct.lean#L324). The attribute's comment: “mu is associative”.

> **Stacks Project, Tag 0FU6: the relative cup product is associative**:
> `(μ ⊗ 1) ≫ μ = α ≫ (1 ⊗ μ) ≫ μ` in `D(Y, q⁻¹𝒪_T)`, where `α` is the associativity constraint of
> the derived tensor product (Tag 0FPB).

```lean
theorem deRhamRelativeCupProduct_assoc (w : f ≫ q = p ≫ h) :
    (Functor.uncurry.obj (derivedTensorProductFunctor
          (SheafOfModules.baseRingedSpace (X := Y.toRingedSpace)
            ((TopCat.Sheaf.pullback CommRingCat.{u} q.base).obj T.sheaf)).sheaf)).map
        (deRhamRelativeCupProduct w ×ₘ
          𝟙 ((derivedPushforward (squareHom w)).obj (deRhamDerived p))) ≫
        deRhamRelativeCupProduct w =
      derivedAssociator (SheafOfModules.baseRingedSpace (X := Y.toRingedSpace)
            ((TopCat.Sheaf.pullback CommRingCat.{u} q.base).obj T.sheaf))
          ((derivedPushforward (squareHom w)).obj (deRhamDerived p))
          ((derivedPushforward (squareHom w)).obj (deRhamDerived p))
          ((derivedPushforward (squareHom w)).obj (deRhamDerived p)) ≫
        (Functor.uncurry.obj (derivedTensorProductFunctor
            (SheafOfModules.baseRingedSpace (X := Y.toRingedSpace)
              ((TopCat.Sheaf.pullback CommRingCat.{u} q.base).obj T.sheaf)).sheaf)).map
          (𝟙 ((derivedPushforward (squareHom w)).obj (deRhamDerived p)) ×ₘ
            deRhamRelativeCupProduct w) ≫
          deRhamRelativeCupProduct w
```

**`AlgebraicGeometry.Scheme.lerayMap_deRhamRelativeCupProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/RelativeCupProduct.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/RelativeCupProduct.lean#L350). The attribute's comment: “mu induces the cup product on cohomology”.

> **Stacks Project, Tag 0FU6: the relative cup product induces the cup product on
> cohomology.**  For `ξ ∈ Hⁱ(Y, Rf_*Ω^•_{X/S})` and `η ∈ Hʲ(Y, Rf_*Ω^•_{X/S})`, the Leray
> identification `Hⁿ(Y, Rf_*Ω^•_{X/S}) = Hⁿ(X, Ω^•_{X/S}) = Hⁿ_{dR}(X/S)` carries
> `Hⁱ⁺ʲ(RΓ(Y, μ))(ξ ∪ η)` -- the cup product on `Y` followed by `μ` -- to the cup product
> `leray ξ ∪ leray η` on de Rham cohomology of Section 50.4 (Tag 0FM3, `deRhamCohomologyCup`).

```lean
theorem lerayMap_deRhamRelativeCupProduct (w : f ≫ q = p ≫ h) (i j : ℤ)
    (ξ : cohomologyModule ((derivedPushforward (squareHom w)).obj (deRhamDerived p)) i)
    (η : cohomologyModule ((derivedPushforward (squareHom w)).obj (deRhamDerived p)) j) :
    lerayMap (squareHom w) (deRhamDerived p) (i + j)
      (((DerivedCategory.homologyFunctor _ (i + j)).map
        ((baseSections (SheafOfModules.baseRingedSpace (X := Y.toRingedSpace)
            ((TopCat.Sheaf.pullback CommRingCat.{u} q.base).obj T.sheaf))).map
          (deRhamRelativeCupProduct w))).hom
        ((cupPairing (cupProductOnSpace (SheafOfModules.baseRingedSpace (X := Y.toRingedSpace)
            ((TopCat.Sheaf.pullback CommRingCat.{u} q.base).obj T.sheaf))) _ _ i j).hom
          (ξ ⊗ₜ η))) =
      SheafOfModules.deRhamCohomologyCup _ _ i j (lerayMap (squareHom w) (deRhamDerived p) i ξ)
        (lerayMap (squareHom w) (deRhamDerived p) j η)
```

## Tag 0FU7, a remark

[Tag 0FU7](https://stacks.math.columbia.edu/tag/0FU7) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.deRhamCohomologyCup_eq_deRhamClassMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/ClassMorphismCupProduct.lean, line 719](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/ClassMorphismCupProduct.lean#L719). The attribute's comment: “property (3): the morphism acts on cohomology by cup product with the class”.

> **Stacks Project, Tag 0FU7, property (3).** The morphism `ξ' : Ω^• ⟶ Ω^•[n]` attached to
> `ξ ∈ H^n_{dR}(X/S)` sends `η ∈ H^m_{dR}(X/S)` to `ξ ∪ η ∈ H^{n + m}_{dR}(X/S)`: the map `ξ'`
> induces on `H^m(X, -)`, read through `H^m(X, Ω^•[n]) = H^{n + m}_{dR}(X/S)`, is left cup product
> with `ξ` (the cup product of Tag 0FM3).

```lean
theorem deRhamCohomologyCup_eq_deRhamClassMorphism (n m : ℤ) (ξ : deRhamCohomology B D n)
    (η : deRhamCohomology B D m) :
    deRhamCohomologyCup B D n m ξ η =
      (deRhamShiftHomologyIso B D n m (n + m) rfl).hom
        ((DerivedCategory.homologyFunctor _ m).map
          ((derivedSectionsBase A).map (deRhamClassMorphism B D n ξ)) η)
```

**`AlgebraicGeometry.SheafOfModules.deRhamRelativeCupProduct_deRhamClassMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/ClassMorphismRelativeCupDeRham.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/ClassMorphismRelativeCupDeRham.lean#L90). The attribute's comment: “property (5): compatibility with the relative cup product of Remark 0FU6”.

> **Stacks Project, Tag 0FU7, property (5).** For a morphism of ringed spaces
> `f : (X, A) ⟶ (Y, 𝒪_Y)` (for a commutative square of schemes as in Remark 0FU6 this is
> `AlgebraicGeometry.Scheme.squareHom`, with `A = p⁻¹𝒪_S` and `𝒪_Y` replaced by `q⁻¹𝒪_T`) and
> `ξ ∈ H^n_{dR}`, the square
>
> `Rf_*Ω^• ⊗^𝐋 Rf_*Ω^• --μ--> Rf_*Ω^•`, `Rf_*Ω^•[n] ⊗^𝐋 Rf_*Ω^• --μ--> Rf_*Ω^•[n]`
>
> with vertical maps `Rf_*ξ' ⊗ 1` and `Rf_*ξ'` commutes in `D(Y)`. The top `μ` is the relative cup
> product `deRhamRelativeCupProduct` of Remark 0FU6; the bottom `μ` is the relative cup product
> followed by `Rf_*` of the multiplication `derivedShiftedMul` of the right differential graded
> module `Ω^•[n]`.

```lean
theorem deRhamRelativeCupProduct_deRhamClassMorphism (n : ℤ) (ξ : deRhamCohomology B D n) :
    Eq ((Functor.uncurry.obj
          (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor Y.sheaf)).map
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward F).map
          (deRhamClassMorphism B D n ξ) ×ₘ
          𝟙 ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward F).obj
            (DerivedCategory.Q.obj
              (deRhamDifferentialGradedAlgebra (X := X) (A := A) (φ := φ) B D).complex))) ≫
        Stacks.Cohomology.DerivedRelativeCupProduct.relativeCupProduct F
          ((DerivedCategory.Q.obj
            (deRhamDifferentialGradedAlgebra (X := X) (A := A) (φ := φ) B D).complex)⟦n⟧)
          (DerivedCategory.Q.obj
            (deRhamDifferentialGradedAlgebra (X := X) (A := A) (φ := φ) B D).complex) ≫
        (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward F).map
          (derivedShiftedMul (S := baseRingedSpace A)
            (deRhamDifferentialGradedAlgebra (X := X) (A := A) (φ := φ) B D) n))
      (deRhamRelativeCupProduct B D F ≫
        (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward F).map
          (deRhamClassMorphism B D n ξ))
```

**`AlgebraicGeometry.SheafOfModules.lift_and_unit_iff_eq_restrictShiftedHom_deRhamClassMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/ClassMorphismRestriction.lean, line 550](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/ClassMorphismRestriction.lean#L550). The attribute's comment: “property (4): the construction commutes with restriction to opens”.

> **Stacks Project, Tag 0FU7, property (4).** The construction of `ξ'` commutes with
> restriction to opens: for an open `U ⊆ X`, write `Ω^•_{U/S} = Ω^•_{X/S}|_U` for the restriction
> of the de Rham complex (a sheaf of differential graded algebras over the slice site at `U`) and
> `ξ|_U ∈ Hom_{D(f^{-1}𝒪_S|_U)}(f^{-1}𝒪_S|_U, Ω^•_{U/S}[n]) = H^n_{dR}(U/S)` for the restriction of
> `ξ`. A morphism `f : Ω^•_{U/S} ⟶ Ω^•_{U/S}[n]` of `D(f^{-1}𝒪_S|_U)` is the map corresponding to
> `ξ|_U` (it lifts to the derived category of right differential graded `Ω^•_{U/S}`-modules, and
> its value `f(1)` at the unit is `ξ|_U`) if and only if it is the restriction `ξ'|_U`.

```lean
theorem lift_and_unit_iff_eq_restrictShiftedHom_deRhamClassMorphism (n : ℤ)
    (ξ : deRhamCohomology B D n) (U : Opens X.carrier)
    (f : DerivedCategory.Q.obj (_root_.SheafOfModules.DifferentialGradedModule.regularModule
        (_root_.SheafOfModules.DifferentialGradedModule.dgaOver (X := baseSite A) U
          (deRhamDifferentialGradedAlgebra B D))).complex ⟶
      (DerivedCategory.Q.obj (_root_.SheafOfModules.DifferentialGradedModule.regularModule
        (_root_.SheafOfModules.DifferentialGradedModule.dgaOver (X := baseSite A) U
          (deRhamDifferentialGradedAlgebra B D))).complex)⟦n⟧) :
    ((∃ g' : (_root_.SheafOfModules.DifferentialGradedModule.toDerivedCategory.{u, u, u}
        (_root_.SheafOfModules.DifferentialGradedModule.dgaOver (X := baseSite A) U
          (deRhamDifferentialGradedAlgebra B D))).obj
        ((_root_.SheafOfModules.DifferentialGradedModule.HomotopyCategory.quotient
          (_root_.SheafOfModules.DifferentialGradedModule.dgaOver (X := baseSite A) U
            (deRhamDifferentialGradedAlgebra B D))).obj
          (_root_.SheafOfModules.DifferentialGradedModule.regularModule
            (_root_.SheafOfModules.DifferentialGradedModule.dgaOver (X := baseSite A) U
              (deRhamDifferentialGradedAlgebra B D)))) ⟶
      ((_root_.SheafOfModules.DifferentialGradedModule.toDerivedCategory.{u, u, u}
        (_root_.SheafOfModules.DifferentialGradedModule.dgaOver (X := baseSite A) U
          (deRhamDifferentialGradedAlgebra B D))).obj
        ((_root_.SheafOfModules.DifferentialGradedModule.HomotopyCategory.quotient
          (_root_.SheafOfModules.DifferentialGradedModule.dgaOver (X := baseSite A) U
            (deRhamDifferentialGradedAlgebra B D))).obj
          (_root_.SheafOfModules.DifferentialGradedModule.regularModule
            (_root_.SheafOfModules.DifferentialGradedModule.dgaOver (X := baseSite A) U
              (deRhamDifferentialGradedAlgebra B D)))))⟦n⟧,
        Eq (_root_.SheafOfModules.DifferentialGradedModule.derivedForgetShiftedHom
          (_root_.SheafOfModules.DifferentialGradedModule.dgaOver (X := baseSite A) U
            (deRhamDifferentialGradedAlgebra B D))
          (_root_.SheafOfModules.DifferentialGradedModule.regularModule
            (_root_.SheafOfModules.DifferentialGradedModule.dgaOver (X := baseSite A) U
              (deRhamDifferentialGradedAlgebra B D))) n g') f) ∧
      Eq (DerivedCategory.Q.map (_root_.SheafOfModules.DifferentialGradedModule.unitComplexRingHom
          (_root_.SheafOfModules.DifferentialGradedModule.dgaOver (X := baseSite A) U
            (deRhamDifferentialGradedAlgebra B D))) ≫ f)
        (DerivedCategory.Q.map
          (_root_.SheafOfModules.DifferentialGradedModule.structureSheafComplexOverHom
            (X := baseSite A) U) ≫
          _root_.SheafOfModules.DifferentialGradedModule.restrictShiftedHom (X := baseSite A) U n
            (deRhamDerivedClass B D n ξ))) ↔
      Eq f (_root_.SheafOfModules.DifferentialGradedModule.restrictShiftedHom (X := baseSite A) U n
        (deRhamClassMorphism B D n ξ))
```

**`AlgebraicGeometry.SheafOfModules.deRhamClassDerivedMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/ClassToDerivedMorphism.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/ClassToDerivedMorphism.lean#L197). The attribute's comment: “the morphism of D(f^{-1}O_S) attached to a de Rham class; the discussion of Differential Graded Sheaves Section 0FU3 is carried as the explicit named hypothesis DeRhamDerivedModuleCorrespondence, whose fields are the identification of Tag 0FTX for the regular module, the forgetful map on morphisms and the evaluation at the unit”.

> **Stacks Project, Tag 0FU7.** The morphism
>
> `ξ' : Ω^•_{X/S} ⟶ Ω^•_{X/S}[n]`
>
> in `D(f^{-1}𝒪_S)` attached to a relative de Rham cohomology class `ξ ∈ H^n_{dR}(X/S)`: the
> morphism of right differential graded `Ω^•_{X/S}`-modules which Tag 0FTX attaches to `ξ`, with its
> module structure forgotten.

```lean
noncomputable def deRhamClassDerivedMorphism (n : ℤ) (ξ : deRhamCohomology B D n) :
    deRhamDerivedObject B D ⟶ (deRhamDerivedObject B D)⟦n⟧
```

**`AlgebraicGeometry.SheafOfModules.exists_lift_deRhamClassDerivedMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/ClassToDerivedMorphism.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/ClassToDerivedMorphism.lean#L205). The attribute's comment: “property (1): the morphism lifts to the derived category of right differential graded modules; Section 0FU3 is carried as the hypothesis DeRhamDerivedModuleCorrespondence”.

> **Stacks Project, Tag 0FU7, property (1).** The morphism attached to a relative de Rham class
> lifts to a morphism in the derived category of right differential graded `Ω^•_{X/S}`-modules.

```lean
theorem exists_lift_deRhamClassDerivedMorphism (n : ℤ) (ξ : deRhamCohomology B D n) :
    ∃ g : deRhamDerivedRegular B D ⟶ deRhamDerivedRegularShift B D n,
      c.forget n g = deRhamClassDerivedMorphism B D c n ξ
```

**`AlgebraicGeometry.SheafOfModules.evalOne_deRhamClassDerivedMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/ClassToDerivedMorphism.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/ClassToDerivedMorphism.lean#L215). The attribute's comment: “property (2): the value of the morphism at the unit is the class it came from; Section 0FU3 is carried as the hypothesis DeRhamDerivedModuleCorrespondence”.

> **Stacks Project, Tag 0FU7, property (2).** The value at the unit of the morphism attached to
> a relative de Rham class `ξ` is `ξ` itself: `ξ'(1) = ξ` in
> `H^0(X, Ω^•_{X/S}[n]) = H^n_{dR}(X/S)`.

```lean
theorem evalOne_deRhamClassDerivedMorphism (n : ℤ) (ξ : deRhamCohomology B D n) :
    c.evalOne n (deRhamClassDerivedMorphism B D c n ξ) = ξ
```

**`AlgebraicGeometry.SheafOfModules.eq_deRhamClassDerivedMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/ClassToDerivedMorphism.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/ClassToDerivedMorphism.lean#L224). The attribute's comment: “uniqueness: properties (1) and (2) determine the morphism; Section 0FU3 is carried as the hypothesis DeRhamDerivedModuleCorrespondence”.

> **Stacks Project, Tag 0FU7.** A morphism `Ω^•_{X/S} ⟶ Ω^•_{X/S}[n]` of `D(f^{-1}𝒪_S)` which
> lifts to the derived category of right differential graded `Ω^•_{X/S}`-modules and whose value at
> the unit is `ξ` is the morphism attached to `ξ`.

```lean
theorem eq_deRhamClassDerivedMorphism (n : ℤ) (ξ : deRhamCohomology B D n)
    {f : deRhamDerivedObject B D ⟶ (deRhamDerivedObject B D)⟦n⟧}
    (hlift : ∃ g : deRhamDerivedRegular B D ⟶ deRhamDerivedRegularShift B D n, c.forget n g = f)
    (hev : c.evalOne n f = ξ) :
    f = deRhamClassDerivedMorphism B D c n ξ
```

**`AlgebraicGeometry.SheafOfModules.exists_lift_deRhamClassMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/DerivedModuleCorrespondence.lean, line 620](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/DerivedModuleCorrespondence.lean#L620). The attribute's comment: “property (1): the morphism lifts to the derived category of right differential graded modules”.

> **Stacks Project, Tag 0FU7, property (1).** `ξ'` lifts to a morphism of the derived category
> of right differential graded `Ω^•_{X/S}`-modules.

```lean
theorem exists_lift_deRhamClassMorphism (n : ℤ) (ξ : deRhamCohomology B D n) :
    ∃ g : deRhamDerivedRegular B D ⟶ (deRhamDerivedRegular B D)⟦n⟧,
      deRhamForgetHom B D n g = deRhamClassMorphism B D n ξ
```

**`AlgebraicGeometry.SheafOfModules.deRhamEvalOne_deRhamClassMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/DerivedModuleCorrespondence.lean, line 628](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/DerivedModuleCorrespondence.lean#L628). The attribute's comment: “property (2): the value of the morphism at the unit is the class”.

> **Stacks Project, Tag 0FU7, property (2).** `ξ'(1) = ξ` in
> `H^0(X, Ω^•_{X/S}[n]) = H^n_{dR}(X/S)`.

```lean
theorem deRhamEvalOne_deRhamClassMorphism (n : ℤ) (ξ : deRhamCohomology B D n) :
    deRhamEvalOne B D n (deRhamClassMorphism B D n ξ) = ξ
```

**`AlgebraicGeometry.SheafOfModules.existsUnique_deRhamClassMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/DerivedModuleCorrespondence.lean, line 647](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DifferentialGradedAlgebra/DerivedModuleCorrespondence.lean#L647). The attribute's comment: “existence and uniqueness: a class determines a unique morphism with properties (1) and (2)”.

> **Stacks Project, Tag 0FU7.** A class `ξ ∈ H^n_{dR}(X/S)` determines a unique morphism
> `ξ' : Ω^•_{X/S} ⟶ Ω^•_{X/S}[n]` of `D(f^{-1}𝒪_S)` with properties (1) and (2).

```lean
theorem existsUnique_deRhamClassMorphism (n : ℤ) (ξ : deRhamCohomology B D n) :
    ∃! f : deRhamDerivedObject B D ⟶ (deRhamDerivedObject B D)⟦n⟧,
      (∃ g : deRhamDerivedRegular B D ⟶ (deRhamDerivedRegular B D)⟦n⟧,
        deRhamForgetHom B D n g = f) ∧ deRhamEvalOne B D n f = ξ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.4, Tag 0FM1](https://stacks.math.columbia.edu/tag/0FM1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
