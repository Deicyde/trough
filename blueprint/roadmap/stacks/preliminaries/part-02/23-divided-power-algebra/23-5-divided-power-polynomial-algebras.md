---
declaration: section
origin: cited
lean: DividedPowers.dividedPowerPolynomialDividedPowers, DividedPowers.dividedPowerPolynomialDividedPowers_dpow_variable, DividedPowers.dividedPowerPolynomialCoefficient_isDPMorphism, DividedPowers.dividedPowerPolynomialDividedPowers_unique, DividedPowers.existsUnique_dPMorphism_from_dividedPowerPolynomial, DividedPowers.finiteStageMap_isDPMorphism, DividedPowers.setIndexedDividedPowerPolynomialDividedPowers, DividedPowers.finiteStageInclusion_isDPMorphism
statement: formalized
proof: formalized
---

# 23.5 Divided power polynomial algebras

Section 23.5 of the Stacks Project, [Tag 07H4](https://stacks.math.columbia.edu/tag/07H4). 4 tags here are carried by 21 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07H5, a lemma

[Tag 07H5](https://stacks.math.columbia.edu/tag/07H5) in the Stacks Project.

**`DividedPowers.dividedPowerPolynomialDividedPowers`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Polynomial/Basic.lean, line 1184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Polynomial/Basic.lean#L1184). The attribute's comment: “divided power structure”.

> The canonical divided power structure on the divided power ideal of a finite-variable
> divided power polynomial algebra.

```lean
public noncomputable def dividedPowerPolynomialDividedPowers (A : DividedPowerRing.{u})
    (ι : Type w) [Finite ι] : _root_.DividedPowers (dividedPowerPolynomialIdeal A.ideal ι)
```

**`DividedPowers.dividedPowerPolynomialDividedPowers_dpow_variable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Polynomial/Basic.lean, line 1197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Polynomial/Basic.lean#L1197). The attribute's comment: “value on variables”.

> The canonical divided powers send `xᵢ` to the distinguished monomial `xᵢ^[n]`.

```lean
public theorem dividedPowerPolynomialDividedPowers_dpow_variable
    (A : DividedPowerRing.{u}) (ι : Type w) [Finite ι] (i : ι) (n : ℕ) :
    (dividedPowerPolynomialDividedPowers A ι).dpow n
        (dividedPowerPolynomialVariable A i) =
      dividedPowerPolynomialVariableMonomial A i n
```

**`DividedPowers.dividedPowerPolynomialCoefficient_isDPMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Polynomial/Basic.lean, line 1207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Polynomial/Basic.lean#L1207). The attribute's comment: “coefficient morphism”.

> The coefficient map into the divided power polynomial algebra is a morphism of divided
> power rings.

```lean
public theorem dividedPowerPolynomialCoefficient_isDPMorphism
    (A : DividedPowerRing.{u}) (ι : Type w) [Finite ι] :
    _root_.DividedPowers.IsDPMorphism A.dividedPowers
      (dividedPowerPolynomialDividedPowers A ι)
      (algebraMap A (DividedPowerAlgebra A (ι →₀ A)))
```

**`DividedPowers.dividedPowerPolynomialDividedPowers_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Polynomial/Basic.lean, line 1224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Polynomial/Basic.lean#L1224). The attribute's comment: “uniqueness”.

> The canonical structure is the unique divided power structure which has the prescribed
> values on variables and makes the coefficient map a divided power morphism.

```lean
public theorem dividedPowerPolynomialDividedPowers_unique
    (A : DividedPowerRing.{u}) (ι : Type w) [Finite ι]
    (δ : _root_.DividedPowers (dividedPowerPolynomialIdeal A.ideal ι))
    (hvar : ∀ (i : ι) (n : ℕ),
      δ.dpow n (dividedPowerPolynomialVariable A i) =
        dividedPowerPolynomialVariableMonomial A i n)
    (hcoeff : _root_.DividedPowers.IsDPMorphism A.dividedPowers δ
      (algebraMap A (DividedPowerAlgebra A (ι →₀ A)))) :
    δ = dividedPowerPolynomialDividedPowers A ι
```

**`DividedPowers.existsUnique_dPMorphism_from_dividedPowerPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Polynomial/Basic.lean, line 1352](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Polynomial/Basic.lean#L1352). The attribute's comment: “universal property”.

> A divided power morphism on coefficients and one element of the target divided power ideal
> for each variable extend uniquely to the divided power polynomial algebra.

```lean
public theorem existsUnique_dPMorphism_from_dividedPowerPolynomial
    (A : DividedPowerRing.{u}) (ι : Type w) [Finite ι]
    (C : DividedPowerRing.{v})
    (f : _root_.DividedPowers.DPMorphism A.dividedPowers C.dividedPowers)
    (k : ι → C.ideal) :
    ∃! φ : _root_.DividedPowers.DPMorphism (dividedPowerPolynomialDividedPowers A ι)
        C.dividedPowers,
      (φ.comp (dividedPowerPolynomialCoefficientDPMorphism A ι) = f ∧
        ∀ i : ι, φ (dividedPowerPolynomialVariable A i) = (k i : C))
```

## Tag 07H6, a remark

[Tag 07H6](https://stacks.math.columbia.edu/tag/07H6) in the Stacks Project.

**`DividedPowers.finiteStageMap_isDPMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Polynomial/SetIndexed.lean, line 335](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Polynomial/SetIndexed.lean#L335). The attribute's comment: “compatible\_divided\_powers”.

> Transition maps between finite stages preserve the canonical divided powers.

```lean
public theorem finiteStageMap_isDPMorphism (A : DividedPowerRing.{u})
    {W : Type w} {E F : Finset W} (h : E ⊆ F) :
    _root_.DividedPowers.IsDPMorphism
      (dividedPowerPolynomialDividedPowers A E)
      (dividedPowerPolynomialDividedPowers A F)
      (finiteStageMap A h).toRingHom
```

**`DividedPowers.setIndexedDividedPowerPolynomialDividedPowers`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Polynomial/SetIndexed.lean, line 507](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Polynomial/SetIndexed.lean#L507). The attribute's comment: “compatible\_divided\_powers”.

> The divided powers on the distinguished ideal of the divided power polynomial algebra
> on an arbitrary type of variables, induced from all finite-variable subalgebras.

```lean
public noncomputable def setIndexedDividedPowerPolynomialDividedPowers
    (A : DividedPowerRing.{u}) (W : Type w) :
    _root_.DividedPowers (dividedPowerPolynomialIdeal A.ideal W)
```

**`DividedPowers.finiteStageInclusion_isDPMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Polynomial/SetIndexed.lean, line 678](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Polynomial/SetIndexed.lean#L678). The attribute's comment: “compatible\_divided\_powers”.

> Every finite-stage inclusion preserves divided powers induced on the colimit.

```lean
public theorem finiteStageInclusion_isDPMorphism (A : DividedPowerRing.{u})
    {W : Type w} (E : Finset W) :
    _root_.DividedPowers.IsDPMorphism
      (dividedPowerPolynomialDividedPowers A E)
      (setIndexedDividedPowerPolynomialDividedPowers A W)
      (finiteStageInclusion A E).toRingHom
```

**`DividedPowers.setIndexedDividedPowerPolynomialDividedPowers_dpow_variable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Polynomial/SetIndexed.lean, line 692](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Polynomial/SetIndexed.lean#L692). The attribute's comment: “compatible\_divided\_powers”.

> The induced divided powers send a variable to its divided power monomial.

```lean
public theorem setIndexedDividedPowerPolynomialDividedPowers_dpow_variable
    (A : DividedPowerRing.{u}) {W : Type w} (i : W) (n : ℕ) :
    (setIndexedDividedPowerPolynomialDividedPowers A W).dpow n
        (dividedPowerPolynomialVariable A i) =
      dividedPowerPolynomialVariableMonomial A i n
```

**`DividedPowers.setIndexedDividedPowerPolynomialCoefficient_isDPMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Polynomial/SetIndexed.lean, line 717](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Polynomial/SetIndexed.lean#L717). The attribute's comment: “compatible\_divided\_powers”.

> The coefficient map is a morphism of divided power rings.

```lean
public theorem setIndexedDividedPowerPolynomialCoefficient_isDPMorphism
    (A : DividedPowerRing.{u}) (W : Type w) :
    _root_.DividedPowers.IsDPMorphism A.dividedPowers
      (setIndexedDividedPowerPolynomialDividedPowers A W)
      (algebraMap A (setIndexedDividedPowerPolynomialAlgebra A W))
```

**`DividedPowers.setIndexedDividedPowerPolynomialDividedPowers_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Polynomial/SetIndexed.lean, line 760](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Polynomial/SetIndexed.lean#L760). The attribute's comment: “compatible\_divided\_powers”.

> Compatibility with every finite stage uniquely determines the induced divided powers.

```lean
public theorem setIndexedDividedPowerPolynomialDividedPowers_unique
    (A : DividedPowerRing.{u}) (W : Type w)
    (δ : _root_.DividedPowers (dividedPowerPolynomialIdeal A.ideal W))
    (hδ : ∀ E : Finset W,
      _root_.DividedPowers.IsDPMorphism (dividedPowerPolynomialDividedPowers A E) δ
        (finiteStageInclusion A E).toRingHom) :
    δ = setIndexedDividedPowerPolynomialDividedPowers A W
```

**`DividedPowers.existsUnique_dPMorphism_from_setIndexedDividedPowerPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Polynomial/SetIndexedUniversalProperty.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Polynomial/SetIndexedUniversalProperty.lean#L100). The attribute's comment: “set\_indexed\_universal\_property”.

> The universal property of a divided power polynomial algebra on an arbitrary type
> of variables: a coefficient morphism and arbitrary images in the target ideal admit
> exactly one extension as a divided power morphism.

```lean
public theorem existsUnique_dPMorphism_from_setIndexedDividedPowerPolynomial
    (A : DividedPowerRing.{u}) (W : Type w) (C : DividedPowerRing.{v})
    (f : _root_.DividedPowers.DPMorphism A.dividedPowers C.dividedPowers)
    (k : W → C.ideal) :
    ∃! φ : _root_.DividedPowers.DPMorphism
      (setIndexedDividedPowerPolynomialDividedPowers A W) C.dividedPowers,
      (φ.comp (setIndexedDividedPowerPolynomialCoefficientDPMorphism A W) = f ∧
        ∀ i : W, φ (dividedPowerPolynomialVariable A i) = (k i : C))
```

**`DividedPowers.finiteVariableInclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Polynomial/Stages.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Polynomial/Stages.lean#L78). The attribute's comment: “finite\_variable\_inclusion”.

> The canonical inclusion from the divided power polynomial algebra in `s` variables to
> the one in `t` variables.

```lean
public noncomputable def finiteVariableInclusion (A : Type u) [CommRing A]
    {s t : ℕ} (h : s ≤ t) :
    DividedPowerAlgebra A (Fin s →₀ A) →ₐ[A] DividedPowerAlgebra A (Fin t →₀ A)
```

**`DividedPowers.finiteVariableInclusion_variableMonomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Polynomial/Stages.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Polynomial/Stages.lean#L85). The attribute's comment: “finite\_variable\_inclusion”.

> The inclusion preserves each divided power monomial in an existing variable.

```lean
public theorem finiteVariableInclusion_variableMonomial (A : Type u) [CommRing A]
    {s t : ℕ} (h : s ≤ t) (i : Fin s) (n : ℕ) :
    finiteVariableInclusion A h (dividedPowerPolynomialVariableMonomial A i n) =
      dividedPowerPolynomialVariableMonomial A (Fin.castLE h i) n
```

**`DividedPowers.setIndexedDividedPowerPolynomialAlgebra`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Polynomial/Stages.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Polynomial/Stages.lean#L93). The attribute's comment: “set\_indexed\_divided\_power\_polynomial\_algebra”.

> The divided power polynomial algebra with one variable for each element of `W`.

```lean
public abbrev setIndexedDividedPowerPolynomialAlgebra
    (A : Type u) [CommRing A] (W : Type w)
```

**`DividedPowers.finiteStageMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Polynomial/Stages.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Polynomial/Stages.lean#L99). The attribute's comment: “set\_indexed\_divided\_power\_polynomial\_algebra”.

> The transition map between the finite-variable divided power polynomial algebras.

```lean
public noncomputable def finiteStageMap (A : Type u) [CommRing A] {W : Type w}
    {E F : Finset W} (h : E ⊆ F) :
    DividedPowerAlgebra A (E →₀ A) →ₐ[A] DividedPowerAlgebra A (F →₀ A)
```

**`DividedPowers.finiteStageInclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Polynomial/Stages.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Polynomial/Stages.lean#L107). The attribute's comment: “set\_indexed\_divided\_power\_polynomial\_algebra”.

> The canonical map from a finite-variable algebra into the set-indexed algebra.

```lean
public noncomputable def finiteStageInclusion (A : Type u) [CommRing A] {W : Type w}
    (E : Finset W) :
    DividedPowerAlgebra A (E →₀ A) →ₐ[A]
      setIndexedDividedPowerPolynomialAlgebra A W
```

**`DividedPowers.finiteStageInclusion_existsUnique_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/Polynomial/Stages.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Polynomial/Stages.lean#L178). The attribute's comment: “set\_indexed\_divided\_power\_polynomial\_algebra”.

> A compatible family of algebra maps out of all finite stages descends uniquely to the
> set-indexed divided power polynomial algebra.

```lean
public theorem finiteStageInclusion_existsUnique_lift (A : Type u) [CommRing A]
    (W : Type w) (B : Type*) [CommRing B] [Algebra A B]
    (f : (E : Finset W) → DividedPowerAlgebra A (E →₀ A) →ₐ[A] B)
    (hf : ∀ (E F : Finset W) (h : E ⊆ F),
      (f F).comp (finiteStageMap A h) = f E) :
    ∃! g : setIndexedDividedPowerPolynomialAlgebra A W →ₐ[A] B,
      ∀ E : Finset W, g.comp (finiteStageInclusion A E) = f E
```

Declarations registered for the tag:

- [`DividedPowers.dividedPowerPolynomialIdeal`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Polynomial/Basic.lean#L324), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/DividedPowers/Polynomial/Stages.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/Polynomial/Stages.lean#L251) (StacksFrontier): “set\_indexed\_divided\_power\_polynomial\_algebra”.

## Tag 07GS, a lemma

[Tag 07GS](https://stacks.math.columbia.edu/tag/07GS) in the Stacks Project.

**`DividedPowers.eq_iff_dpow_prime_eq`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/PrimeOperation/Classification.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/PrimeOperation/Classification.lean#L111). The attribute's comment: “uniqueness”.

> Over a `ℤ_(p)`-algebra, a divided power structure is determined by its `p`th operation.

```lean
public lemma eq_iff_dpow_prime_eq {A : Type*} [CommRing A] {I : Ideal A} (p : ℕ)
    (hp : p.Prime) (hA : ∀ n : ℕ, ¬p ∣ n → IsUnit (n : A))
    (γ γ' : _root_.DividedPowers I) :
    γ = γ' ↔ ∀ x : I, γ.dpow p x = γ'.dpow p x
```

**`DividedPowers.existsUnique_of_prime_operation`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/PrimeOperation/Classification.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/PrimeOperation/Classification.lean#L160). The attribute's comment: “existence”.

> A map satisfying the factorial, homogeneity, and addition identities for a `p`th divided
> power operation extends uniquely to a divided power structure.

```lean
public lemma existsUnique_of_prime_operation {A : Type*} [CommRing A] (I : Ideal A) (p : ℕ)
    (hp : p.Prime) (hA : ∀ n : ℕ, ¬p ∣ n → IsUnit (n : A)) (δ : I → I)
    (factorial_mul : ∀ x : I, (p.factorial : A) * (δ x : A) = (x : A) ^ p)
    (smul : ∀ (a : A) (x : I), δ (a • x) = a ^ p • δ x)
    (add : ∀ x y : I,
      (δ (x + y) : A) = (δ x : A) +
        ∑ ij ∈ (antidiagonal p).filter (fun ij ↦ ij.1 ≠ 0 ∧ ij.2 ≠ 0),
          factorialInverse p hp hA ij.1 * factorialInverse p hp hA ij.2 *
            (x : A) ^ ij.1 * (y : A) ^ ij.2 +
        (δ y : A)) :
    ∃! γ : _root_.DividedPowers I, ∀ x : I, γ.dpow p x = δ x
```

## Tag 0H87, a remark

[Tag 0H87](https://stacks.math.columbia.edu/tag/0H87) in the Stacks Project.

**`DividedPowers.factorial_mul_of_smul_add`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/PolynomialAlgebra.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DividedPowers/PolynomialAlgebra.lean#L235).

> Homogeneity and the divided-power addition law imply the factorial identity for the
> `p`th operation.

```lean
public lemma factorial_mul_of_smul_add {A : Type*} [CommRing A] (I : Ideal A) (p : ℕ)
    (hp : p.Prime) (hA : ∀ n : ℕ, ¬p ∣ n → IsUnit (n : A)) (δ : I → I)
    (smul : ∀ (a : A) (x : I), δ (a • x) = a ^ p • δ x)
    (add : ∀ x y : I,
      (δ (x + y) : A) = (δ x : A) +
        ∑ ij ∈ (antidiagonal p).filter (fun ij ↦ ij.1 ≠ 0 ∧ ij.2 ≠ 0),
          factorialInverse p hp hA ij.1 * factorialInverse p hp hA ij.2 *
            (x : A) ^ ij.1 * (y : A) ^ ij.2 +
        (δ y : A)) :
    ∀ x : I, (p.factorial : A) * (δ x : A) = (x : A) ^ p
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 23.5, Tag 07H4](https://stacks.math.columbia.edu/tag/07H4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
