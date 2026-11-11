---
declaration: section
origin: cited
lean: Crystalline.DividedPowerDerivation, Crystalline.dividedPowerDifferentialsQuotientEquiv, Crystalline.dividedPowerDifferentialsDividedPowerPolynomialEquiv, Crystalline.dividedPowerDifferentialsPolynomialEquiv, Crystalline.Pushout.dividedPowerDifferentialsEquivDiagonalConormal, DividedPowers.isSubDPIdeal_ker, Crystalline.dividedPowerDifferentialsEquivDiagonalConormal, Crystalline.diagonalKernel_isSubDPIdeal
statement: formalized
proof: formalized
---

# 60.6 Module of differentials

Section 60.6 of the Stacks Project, [Tag 07HQ](https://stacks.math.columbia.edu/tag/07HQ). 10 tags here are carried by 22 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07HR, a definition

[Tag 07HR](https://stacks.math.columbia.edu/tag/07HR) in the Stacks Project.

**`Crystalline.DividedPowerDerivation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/DividedPowerDerivation.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/DividedPowerDerivation.lean#L101).

> A divided power `A`-derivation from a divided power ring `B` into a `B`-module `M`.
>
> It is an additive map satisfying the Leibniz rule, vanishing on the image of `A`, and
> sending `δ n x` to `δ (n - 1) x • D x` for every positive `n` and every `x` in the
> distinguished ideal.

```lean
public structure DividedPowerDerivation
    (A : Type u) [CommRing A]
    (B : DividedPowerRing.{v}) (f : A →+* B)
    (M : Type w) [AddCommGroup M] [Module B M]
    extends Derivation ℤ B M
```

## Tag 07HS, a lemma

[Tag 07HS](https://stacks.math.columbia.edu/tag/07HS) in the Stacks Project.

**`Crystalline.dividedPowerDifferentialsQuotientEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/DividedPowerDerivation.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/DividedPowerDerivation.lean#L405). The attribute's comment: “quotient”.

> The canonical quotient formula for divided power differentials.

```lean
public noncomputable def dividedPowerDifferentialsQuotientEquiv
    (K : Ideal B) (hK : DividedPowers.IsSubDPIdeal B.dividedPowers K) :
    let δ' := DividedPowers.Quotient.dividedPowers B.dividedPowers
      (J := K) (by simpa [inf_of_le_left hK.isSubideal] using hK)
    { e :
        (TensorProduct B (B ⧸ K)
          (dividedPowerDifferentials (A := A) B.dividedPowers) ⧸
          Submodule.span (B ⧸ K)
            (Set.range fun k : K ↦ TensorProduct.tmul B (1 : B ⧸ K)
              (dividedPowerDifferential (A := A) B.dividedPowers k)))
          ≃ₗ[B ⧸ K]
          dividedPowerDifferentials (A := A) δ' //
      ∀ b : B,
        e (Submodule.Quotient.mk
          (TensorProduct.tmul B (1 : B ⧸ K)
            (dividedPowerDifferential (A := A) B.dividedPowers b))) =
          dividedPowerDifferential (A := A) δ' (Ideal.Quotient.mk K b) }
```

**`Crystalline.dividedPowerDifferentialsDividedPowerPolynomialEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/DividedPowerPolynomialAlgebra.lean, line 721](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/DividedPowerPolynomialAlgebra.lean#L721). The attribute's comment: “divided\_power\_polynomial”.

> **The divided power polynomial decomposition of divided power differentials.**  For a divided
> power ring `(B, I, δ)` over `A` and the divided power polynomial algebra `P = B⟨x_w : w ∈ W⟩`
> with divided power ideal `IP + P₊`, one has
> `Ω¹_{P/A,δ'} = (P ⊗_B Ω¹_{B/A,δ}) ⊕ ⨁_w P · d x_w`, the isomorphism being characterized by its
> values on the differentials of coefficients and of variables.

```lean
public noncomputable def dividedPowerDifferentialsDividedPowerPolynomialEquiv
    {A : Type uA} [CommRing A] (B : DividedPowerRing.{uB}) [Algebra A B] (W : Type uW) :
    { e : dividedPowerDifferentials (A := A)
          (setIndexedDividedPowerPolynomialDividedPowers B W) ≃ₗ[
        setIndexedDividedPowerPolynomialAlgebra B W]
        ((setIndexedDividedPowerPolynomialAlgebra B W ⊗[B]
            dividedPowerDifferentials (A := A) B.dividedPowers) ×
          (W →₀ setIndexedDividedPowerPolynomialAlgebra B W)) //
      (∀ b : B, e (dividedPowerDifferential (A := A)
          (setIndexedDividedPowerPolynomialDividedPowers B W)
          (algebraMap (B : Type uB) (setIndexedDividedPowerPolynomialAlgebra B W) b)) =
        (1 ⊗ₜ[B] dividedPowerDifferential (A := A) B.dividedPowers b, 0)) ∧
      (∀ w : W, e (dividedPowerDifferential (A := A)
          (setIndexedDividedPowerPolynomialDividedPowers B W)
          (dividedPowerPolynomialVariable (B : Type uB) w)) = (0, Finsupp.single w 1)) }
```

**`Crystalline.dividedPowerDifferentialsPolynomialEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/PolynomialRing.lean, line 623](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/PolynomialRing.lean#L623). The attribute's comment: “polynomial”.

> The canonical polynomial decomposition of divided power differentials,
> characterized by the differentials of constants and of the polynomial variable.

```lean
public noncomputable def dividedPowerDifferentialsPolynomialEquiv
    (δ' : DividedPowers (B.ideal.map (Polynomial.C : B →+* B[X])))
    (_h : DividedPowers.IsDPMorphism B.dividedPowers δ'
      (Polynomial.C : B →+* B[X])) :
    { e : dividedPowerDifferentials (A := A) δ' ≃ₗ[B[X]]
        (TensorProduct B B[X] (dividedPowerDifferentials (A := A) B.dividedPowers) × B[X]) //
      (∀ b : B, e (dividedPowerDifferential (A := A) δ' (Polynomial.C b)) =
        (TensorProduct.tmul B (1 : B[X])
          (dividedPowerDifferential (A := A) B.dividedPowers b), 0)) ∧
      e (dividedPowerDifferential (A := A) δ' Polynomial.X) = (0, 1) }
```

## Tag 07HT, a lemma

[Tag 07HT](https://stacks.math.columbia.edu/tag/07HT) in the Stacks Project.

**`Crystalline.Pushout.dividedPowerDifferentialsEquivDiagonalConormal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/ModuleDifferentials/Diagonal.lean, line 899](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/ModuleDifferentials/Diagonal.lean#L899). The attribute's comment: “canonical identification”.

> Divided power differentials are canonically the conormal module of the diagonal,
> modulo the square of its kernel and divided powers of order at least two.

```lean
public noncomputable def dividedPowerDifferentialsEquivDiagonalConormal
    (h : IsPushout f f s₀ s₁) :
    letI : Algebra A B := f.toRingHom.toAlgebra
    {e : dividedPowerDifferentials (A := A) B.dividedPowers ≃ₗ[B] diagonalConormal h //
      ∀ b : B,
        e (dividedPowerDifferential (A := A) B.dividedPowers b) = diagonalDifference h b}
```

Declarations registered for the tag:

- [`DividedPowers.isSubDPIdeal_ker`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DividedPowers.isSubDPIdeal_ker#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Crystalline/ModuleDifferentials/Diagonal.lean, line 894](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/ModuleDifferentials/Diagonal.lean#L894) (StacksFrontier): “stability under divided powers”.

## Tag 07HV, a lemma

[Tag 07HV](https://stacks.math.columbia.edu/tag/07HV) in the Stacks Project.

**`Crystalline.dividedPowerDifferentialsEquivDiagonalConormal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/ModuleDifferentials/Thickening/ConormalEquiv.lean, line 672](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/ModuleDifferentials/Thickening/ConormalEquiv.lean#L672). The attribute's comment: “canonical identification”.

> A chosen identification of the divided power differentials of `X` with the diagonal
> conormal module, carrying `db` to `diagonalDifference h b`.

```lean
public noncomputable def dividedPowerDifferentialsEquivDiagonalConormal
    (h : IsColimit (BinaryCofan.mk s₀ s₁)) :
    letI : Algebra S.A X.1.ring := X.1.fromBase.toRingHom.toAlgebra
    {e : dividedPowerDifferentials (A := S.A) X.1.ring.dividedPowers ≃ₗ[X.1.ring]
        diagonalConormal h //
      ∀ b : X.1.ring,
        e (dividedPowerDifferential (A := S.A) X.1.ring.dividedPowers b) =
          diagonalDifference h b}
```

**`Crystalline.diagonalKernel_isSubDPIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/ModuleDifferentials/Thickening/DiagonalKernel.lean, line 569](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/ModuleDifferentials/Thickening/DiagonalKernel.lean#L569). The attribute's comment: “stability under divided powers”.

> The intersection of the diagonal ideal with the crystalline divided power ideal is
> stable under divided powers.

```lean
public theorem diagonalKernel_isSubDPIdeal
    (h : IsColimit (BinaryCofan.mk s₀ s₁)) :
    Y.1.ring.dividedPowers.IsSubDPIdeal (diagonalKernel h ⊓ Y.1.ring.ideal)
```

## Tag 07HW, a lemma

[Tag 07HW](https://stacks.math.columbia.edu/tag/07HW) in the Stacks Project.

**`Crystalline.dividedPowerEnvelopeDifferentialsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/ModuleDifferentials/Envelope.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/ModuleDifferentials/Envelope.lean#L62).

> The divided power differentials of a divided power envelope are canonically the
> base change of the ordinary Kähler differentials of the original algebra.  The
> displayed equation identifies the canonical equivalence on universal differentials.

```lean
public noncomputable def dividedPowerEnvelopeDifferentialsEquiv
    (A : DividedPowerRing.{u}) {B : Type u} [CommRing B]
    (f : A →+* B) (J : Ideal B) (hJ : A.ideal.map f ≤ J)
    (E : DividedPowerEnvelope A f J hJ) :
    letI : Algebra A B := f.toAlgebra
    letI : Algebra B E.object := E.algebraMap.toRingHom.toAlgebra
    letI : Algebra A E.object := E.structureMap.toRingHom.toAlgebra
    { e : dividedPowerDifferentials
          (A := A) E.object.dividedPowers ≃ₗ[E.object]
          TensorProduct B E.object (KaehlerDifferential A B) //
      ∀ b : B,
        e (dividedPowerDifferential
            (A := A) E.object.dividedPowers (E.algebraMap.toRingHom b)) =
          (1 : E.object) ⊗ₜ[B] KaehlerDifferential.D A B b }
```

## Tag 07HZ, a remark

[Tag 07HZ](https://stacks.math.columbia.edu/tag/07HZ) in the Stacks Project.

**`Crystalline.dividedPowerDifferentials`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/DeRham.lean, line 686](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/DeRham.lean#L686). The attribute's comment: “divided\_power\_de\_rham\_complex”.

> The module `Ω¹_{B/A,δ}` of divided power differentials.

```lean
public abbrev dividedPowerDifferentials : Type v
```

**`Crystalline.dividedPowerDifferentialForms`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/DeRham.lean, line 720](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/DeRham.lean#L720). The attribute's comment: “divided\_power\_de\_rham\_complex”.

> The module `Ωⁱ_{B/A,δ}`, the `i`-th exterior power of the module of divided
> power differentials.

```lean
public abbrev dividedPowerDifferentialForms (i : ℕ) : Type v
```

**`Crystalline.dividedPowerDeRhamComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/DeRham.lean, line 899](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/DeRham.lean#L899). The attribute's comment: “divided\_power\_de\_rham\_complex”.

> The canonical divided power de Rham complex.

```lean
public noncomputable def dividedPowerDeRhamComplex :
    DividedPowerDeRhamComplex (A := A) hJ
```

**`Crystalline.DividedPowerDeRhamComplex.unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/DeRham.lean, line 922](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/DeRham.lean#L922). The attribute's comment: “divided\_power\_de\_rham\_complex”.

> The generator formula uniquely determines the divided power de Rham complex.

```lean
public theorem DividedPowerDeRhamComplex.unique
    (C : DividedPowerDeRhamComplex (A := A) hJ) :
    C = dividedPowerDeRhamComplex (A := A) hJ
```

**`Crystalline.dividedPowerDifferentials_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/DividedPowerDerivation.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/DividedPowerDerivation.lean#L286). The attribute's comment: “the universal divided power derivation”.

> The quotient of Kähler differentials by the divided power relations represents
> divided-power-compatible `A`-derivations.

```lean
public theorem dividedPowerDifferentials_lift
    {M : Type w} [AddCommGroup M] [Module B M]
    (D : DividedPowerDerivation A B (algebraMap A B) M) :
    ∃! lift :
        dividedPowerDifferentials (A := A) B.dividedPowers →ₗ[B] M,
      ∀ b : B,
        lift (dividedPowerDifferential (A := A) B.dividedPowers b) = D b
```

**`Crystalline.dividedPowerDifferentials_generationHypothesis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/DividedPowerDerivation.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/DividedPowerDerivation.lean#L347). The attribute's comment: “descent of the de Rham differential”.

> The quotient projection satisfies the generation hypothesis for descending the de Rham
> differential to divided power differential forms.

```lean
public theorem dividedPowerDifferentials_generationHypothesis
    (S : SourceDeRham A B) :
    S.GenerationHypothesis
      (dividedPowerDifferentialRelations (A := A) B.dividedPowers).mkQ
```

## Tag 07I0, a remark

[Tag 07I0](https://stacks.math.columbia.edu/tag/07I0) in the Stacks Project.

**`Crystalline.Connection`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/Connection.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/Connection.lean#L251). The attribute's comment: “connection”.

> An additive connection on a `B`-module `M` relative to a map from the Kähler
> differentials of `B` over `A` to a `B`-module `Ω`.

```lean
public structure Connection
    (A B : Type*) [CommRing A] [CommRing B] [Algebra A B]
    {Omega : Type*} [AddCommGroup Omega] [Module B Omega]
    (pi : Ω[B⁄A] →ₗ[B] Omega)
    (M : Type*) [AddCommGroup M] [Module B M]
```

**`Crystalline.extendedConnection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/Connection.lean, line 606](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/Connection.lean#L606). The attribute's comment: “extended\_connection. The extension of a connection to M ⊗ ⋀^p Omega in every degree, with the displayed formula on pure tensors. The de Rham differentials of B over A are constructed, in Stacks.DeRham.DifferentialDescent.sourceDeRham, and SourceDeRham.eq\_sourceDeRham proves that term is the only one of SourceDeRham A B, so the binder S names the de Rham complex of 0FKF; its complex property d ∘ d = 0 follows from the defining rule on generators by comp\_eq\_zero\_of\_gen. The binders π, hπ, hgen are the quotient of the differentials that the tag itself fixes, by reference to 07HY”.

> A connection extends to the tensor products with all exterior powers of `Omega`. On a pure
> tensor its value is the wedge of the connection term with the form, plus the coefficient tensored
> with the descended de Rham differential of the form.
>
> `S` is not de Rham data: `Stacks.DeRham.DifferentialDescent.sourceDeRham` constructs the de Rham
> complex of `B` over `A` ([Stacks, Tag 0FKF]) and
> `Stacks.DeRham.DifferentialDescent.SourceDeRham.eq_sourceDeRham` proves it is the only term of
> `SourceDeRham A B`, so `S` names that complex; its square-zero property is derived from the
> defining rule on generators by `Stacks.DeRham.DifferentialDescent.comp_eq_zero_of_gen`.  The
> quotient `π : Ω[B⁄A] → Omega` with `hπ` and `hgen` is the setting [Stacks, Tag 07I0] itself
> fixes, by reference to [Stacks, Tag 07HY].

```lean
public noncomputable def extendedConnection
    (S : SourceDeRham A B) (π : Ω[B⁄A] →ₗ[B] Omega)
    (hπ : Function.Surjective π) (hgen : S.GenerationHypothesis π)
    (nabla : Connection A B π M) : ExtendedConnection S π nabla
```

**`Crystalline.Connection.IsIntegrable`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/Connection.lean, line 653](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/Connection.lean#L653). The attribute's comment: “integrable\_connection. Vanishing of the composite M → M ⊗ Ω^1 → M ⊗ Ω^2 of a connection with its own degree-one extension. As for extended\_connection, the de Rham differentials are constructed in Stacks.DeRham.DifferentialDescent.sourceDeRham and SourceDeRham.eq\_sourceDeRham proves the binder S admits that term alone”.

> A connection is integrable if its composite with its canonical extension from one-forms to
> two-forms is zero.
>
> As in `Crystalline.extendedConnection`, `S` is not de Rham data: it can only be
> `Stacks.DeRham.DifferentialDescent.sourceDeRham A B`, the de Rham complex of [Stacks, Tag 0FKF],
> by `Stacks.DeRham.DifferentialDescent.SourceDeRham.eq_sourceDeRham`.

```lean
public noncomputable def IsIntegrable
    (S : SourceDeRham A B) (pi : Ω[B⁄A] →ₗ[B] Omega)
    (hpi : Function.Surjective pi) (hgen : S.GenerationHypothesis pi)
    (nabla : Connection A B pi M) : Prop
```

**`Crystalline.extendedConnection_comp_self_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/DeRham.lean, line 601](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/DeRham.lean#L601). The attribute's comment: “connection\_de\_rham\_complex. The last clause of the tag: for an integrable connection the extended differentials compose to zero, so M ⊗ Ω^• is a complex. The de Rham differentials of B over A are constructed in Stacks.DeRham.DifferentialDescent.sourceDeRham and SourceDeRham.eq\_sourceDeRham proves the binder S admits that term alone”.

> The consecutive extended differentials of an integrable connection compose to zero, so an
> integrable connection makes `M ⊗_B Ω^•` a complex.
>
> `S` is not de Rham data: it can only be `Stacks.DeRham.DifferentialDescent.sourceDeRham A B`, the
> de Rham complex of [Stacks, Tag 0FKF], by
> `Stacks.DeRham.DifferentialDescent.SourceDeRham.eq_sourceDeRham`.

```lean
public theorem extendedConnection_comp_self_eq_zero
    (S : SourceDeRham A B) (pi : Ω[B⁄A] →ₗ[B] Omega)
    (hpi : Function.Surjective pi) (hgen : S.GenerationHypothesis pi)
    (nabla : Connection A B pi M)
    (hintegrable : Connection.IsIntegrable S pi hpi hgen nabla) (p : ℕ) :
    ((extendedConnection S pi hpi hgen nabla).toLinearMap (p + 1)).comp
      ((extendedConnection S pi hpi hgen nabla).toLinearMap p) = 0
```

## Tag 07KJ, a remark

[Tag 07KJ](https://stacks.math.columbia.edu/tag/07KJ) in the Stacks Project.

**`Crystalline.Connection.baseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChange.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChange.lean#L145). The attribute's comment: “base\_change\_connection”.

> Base change of a connection through a compatible commutative square of rings and modules of
> differentials.

```lean
public noncomputable def baseChange (nabla : Connection A B pi M)
    (hpsi : ∀ b : B, psi (pi (KaehlerDifferential.D A B b)) =
      pi' (KaehlerDifferential.D A' B' (algebraMap B B' b))) :
    Connection A' B' pi' (B' ⊗[B] M)
```

Declarations registered for the tag:

- [`Crystalline.baseChange_isIntegrable`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChange.lean#L913), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChange.lean, line 1109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChange.lean#L1109) (StacksFrontier): “integrability after base change”.
- [`Crystalline.existsUnique_baseChangeDeRhamMap`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChange.lean#L1011), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChange.lean, line 1110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChange.lean#L1110) (StacksFrontier): “canonical map of de Rham complexes”.

## Tag 07PY, an equation

[Tag 07PY](https://stacks.math.columbia.edu/tag/07PY) in the Stacks Project.

**`Crystalline.baseChange_isIntegrable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChange.lean, line 913](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChange.lean#L913). The attribute's comment: “integrability after base change”.

> An integrable connection remains integrable after the compatible base change.

```lean
public theorem baseChange_isIntegrable
    (hintegrable : Connection.IsIntegrable S pi hpi hgen nabla) :
    Connection.IsIntegrable S' pi' hpi' hgen'
      (Connection.baseChange psi nabla hpsi)
```

**`Crystalline.existsUnique_baseChangeDeRhamMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChange.lean, line 1011](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/BaseChange.lean#L1011). The attribute's comment: “canonical map of complexes”.

> The canonical degreewise map from a connection's de Rham complex to that of its base
> change is uniquely specified by its value on wedges of one-forms, and commutes with the
> extended differentials.

```lean
public theorem existsUnique_baseChangeDeRhamMap
    (_hintegrable : Connection.IsIntegrable S pi hpi hgen nabla) :
    ∃! c : ∀ p : ℕ,
      RestrictScalars A B (M ⊗[B] (⋀[B]^p Omega)) →ₗ[A]
        RestrictScalars A B' ((B' ⊗[B] M) ⊗[B'] (⋀[B']^p Omega')),
      (∀ (p : ℕ) (m : M) (omega : Fin p → Omega),
        c p (m ⊗ₜ[B] exteriorPower.ιMulti B p omega) =
          (1 ⊗ₜ[B] m) ⊗ₜ[B'] exteriorPower.ιMulti B' p (psi ∘ omega)) ∧
      (∀ (p : ℕ) (x : M ⊗[B] (⋀[B]^p Omega)),
        c (p + 1) ((extendedConnection S pi hpi hgen nabla).toLinearMap p x) =
          (extendedConnection S' pi' hpi' hgen'
            (Connection.baseChange psi nabla hpsi)).toLinearMap p (c p x))
```

## Tag 07KK, a lemma

[Tag 07KK](https://stacks.math.columbia.edu/tag/07KK) in the Stacks Project.

**`Crystalline.exists_dividedPowerDifferentialsCompletionEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/ModuleDifferentials/Completion.lean, line 722](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/ModuleDifferentials/Completion.lean#L722).

> Let `A → B` be a ring map, let `(J, δ)` be a divided power structure on `B`, let `p` be
> prime, let `A` be a `ℤ_(p)`-algebra and let `p` be nilpotent in `B / J`.  Then
> `lim\_e Ω\_\{B\_e/A, δ̄} = lim\_e Ω\_\{B/A, δ} / pᵉ Ω\_\{B/A, δ}
>   = lim\_e Ω\_\{B^∧/A, δ^∧} / pᵉ Ω\_\{B^∧/A, δ^∧}`.
>
> The conclusion is written out here, with no reference to
> `Crystalline.DifferentialsCompletionComparison`.  Beyond a level `N`, each `pᵉ B` lies in `J` and
> is stable under the divided powers of `δ` (`level`), so `B_e = B / pᵉ B` carries divided powers
> `δ̄` and the modules `Ω_{B_e/A, δ̄} = Crystalline.quotientDifferentials ..` form an inverse system
> whose transition maps are those induced on universal differentials (`transition`, and the first
> conjunct).  The second and third limits are Mathlib's `AdicCompletion`s of `Ω_{B/A, δ}` and of
> `Ω_{B^∧/A, δ^∧}`; `fromOriginal` and `fromCompletion` identify every level of their towers of
> quotients with that system, compatibly with all three families of transition maps, which is the
> first equality in the strong form of an isomorphism of inverse systems.  `limitEquiv` is the
> isomorphism of the second limit with the third that results, and the last conjunct says its
> component at each level `N + e` is `fromOriginal` followed by the inverse of `fromCompletion`.

```lean
public theorem exists_dividedPowerDifferentialsCompletionEquiv
    [Fact p.Prime] [Algebra (DividedPowers.IntegersAtPrime p) A]
    (hp : IsNilpotent (Ideal.Quotient.mk J (p : B))) :
    ∃ (N : ℕ)
      (level : ∀ e, N ≤ e → (DividedPowers.pAdicIdeal (A := B) p ^ e ≤ J) ∧
        delta.IsSubDPIdeal (DividedPowers.pAdicIdeal (A := B) p ^ e))
      (transition : ∀ e e' : ℕ, e ≤ e' →
        quotientDifferentials (A := A) J delta p (N + e')
            (level _ (Nat.le_add_right N e')).1 (level _ (Nat.le_add_right N e')).2 →+
          quotientDifferentials (A := A) J delta p (N + e)
            (level _ (Nat.le_add_right N e)).1 (level _ (Nat.le_add_right N e)).2)
      (fromOriginal : ∀ e : ℕ, differentialsModPow (A := A) J delta p (N + e) ≃ₗ[B]
        quotientDifferentials (A := A) J delta p (N + e)
          (level _ (Nat.le_add_right N e)).1 (level _ (Nat.le_add_right N e)).2)
      (fromCompletion : ∀ e : ℕ,
        completedDifferentialsModPow (A := A) J delta p hp (N + e) ≃+
          quotientDifferentials (A := A) J delta p (N + e)
            (level _ (Nat.le_add_right N e)).1 (level _ (Nat.le_add_right N e)).2)
      (limitEquiv : AdicCompletion (DividedPowers.pAdicIdeal (A := B) p)
            (dividedPowerDifferentials (A := A) delta) ≃+
          AdicCompletion
            (DividedPowers.pAdicIdeal
              (A := AdicCompletion (DividedPowers.pAdicIdeal (A := B) p) B) p)
            (dividedPowerDifferentials (A := A)
              (DividedPowers.completedDividedPowers J delta p hp).1)),
      (∀ (e e' : ℕ) (h : e ≤ e') (b : B),
          transition e e' h
              (dividedPowerDifferential (A := A)
                (DividedPowers.quotientDividedPowers J delta p (N + e')
                  (level _ (Nat.le_add_right N e')).1 (level _ (Nat.le_add_right N e')).2)
                (Ideal.Quotient.mk (DividedPowers.pAdicIdeal (A := B) p ^ (N + e')) b)) =
            dividedPowerDifferential (A := A)
              (DividedPowers.quotientDividedPowers J delta p (N + e)
                (level _ (Nat.le_add_right N e)).1 (level _ (Nat.le_add_right N e)).2)
              (Ideal.Quotient.mk (DividedPowers.pAdicIdeal (A := B) p ^ (N + e)) b)) ∧
      (∀ (e : ℕ) (b : B),
          fromOriginal e
              (Submodule.Quotient.mk (dividedPowerDifferential (A := A) delta b)) =
            dividedPowerDifferential (A := A)
              (DividedPowers.quotientDividedPowers J delta p (N + e)
                (level _ (Nat.le_add_right N e)).1 (level _ (Nat.le_add_right N e)).2)
              (Ideal.Quotient.mk (DividedPowers.pAdicIdeal (A := B) p ^ (N + e)) b)) ∧
      (∀ (e e' : ℕ) (h : e ≤ e')
          (omega : differentialsModPow (A := A) J delta p (N + e')),
          transition e e' h (fromOriginal e' omega) =
            fromOriginal e
              (AdicCompletion.transitionMap (DividedPowers.pAdicIdeal (A := B) p)
                (dividedPowerDifferentials (A := A) delta)
                (Nat.add_le_add_left h N) omega)) ∧
      (∀ (e : ℕ) (b : AdicCompletion (DividedPowers.pAdicIdeal (A := B) p) B),
          fromCompletion e
              (Submodule.Quotient.mk
                (dividedPowerDifferential (A := A)
                  (DividedPowers.completedDividedPowers J delta p hp).1 b)) =
            dividedPowerDifferential (A := A)
              (DividedPowers.quotientDividedPowers J delta p (N + e)
                (level _ (Nat.le_add_right N e)).1 (level _ (Nat.le_add_right N e)).2)
              (AdicCompletion.evalₐ (DividedPowers.pAdicIdeal (A := B) p) (N + e) b)) ∧
      (∀ (e : ℕ) (b : AdicCompletion (DividedPowers.pAdicIdeal (A := B) p) B)
          (omega : completedDifferentialsModPow (A := A) J delta p hp (N + e)),
          fromCompletion e (b • omega) =
            AdicCompletion.evalₐ (DividedPowers.pAdicIdeal (A := B) p) (N + e) b •
              fromCompletion e omega) ∧
      (∀ (e e' : ℕ) (h : e ≤ e')
          (omega : completedDifferentialsModPow (A := A) J delta p hp (N + e')),
          transition e e' h (fromCompletion e' omega) =
            fromCompletion e
              (AdicCompletion.transitionMap
                (DividedPowers.pAdicIdeal
                  (A := AdicCompletion (DividedPowers.pAdicIdeal (A := B) p) B) p)
                (dividedPowerDifferentials (A := A)
                  (DividedPowers.completedDividedPowers J delta p hp).1)
                (Nat.add_le_add_left h N) omega)) ∧
      (∀ (e : ℕ) (omega : AdicCompletion (DividedPowers.pAdicIdeal (A := B) p)
            (dividedPowerDifferentials (A := A) delta)),
          fromCompletion e
              (AdicCompletion.eval
                (DividedPowers.pAdicIdeal
                  (A := AdicCompletion (DividedPowers.pAdicIdeal (A := B) p) B) p)
                (dividedPowerDifferentials (A := A)
                  (DividedPowers.completedDividedPowers J delta p hp).1)
                (N + e) (limitEquiv omega)) =
            fromOriginal e
              (AdicCompletion.eval (DividedPowers.pAdicIdeal (A := B) p)
                (dividedPowerDifferentials (A := A) delta) (N + e) omega))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.6, Tag 07HQ](https://stacks.math.columbia.edu/tag/07HQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
