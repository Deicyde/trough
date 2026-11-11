---
declaration: section
origin: cited
lean: DividedPowers.TateResolution.DividedPowerStructure, DividedPowers.TateResolution.ExteriorOddVariable.equiv, DividedPowers.TateResolution.isCompatibleWithDifferential_exteriorDividedPowerStructure, DividedPowers.TateResolution.existsUnique_oddVariableDividedPowerStructure, DividedPowers.TateResolution.oddVariableDividedPowerStructure_dpow, DividedPowers.TateResolution.OddVariableExtension, DividedPowers.TateResolution.OddVariableExtension.grade, DividedPowers.TateResolution.existsUnique_oddVariableExtension_ringHom
statement: formalized
proof: formalized
---

# 23.6 Tate resolutions

Section 23.6 of the Stacks Project, [Tag 09PF](https://stacks.math.columbia.edu/tag/09PF). 12 tags here are carried by 60 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09PG, a definition

[Tag 09PG](https://stacks.math.columbia.edu/tag/09PG) in the Stacks Project.

**`DividedPowers.TateResolution.DividedPowerStructure`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/Basic.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/Basic.lean#L148).

> A divided power structure on the positive even part of a strictly graded-commutative graded
> algebra.

```lean
public structure DividedPowerStructure (𝒜 : ℕ → Submodule R A) [GradedAlgebra 𝒜]
    [IsStrictlyGradedComm 𝒜]
```

## Tag 09PH, an example

[Tag 09PH](https://stacks.math.columbia.edu/tag/09PH) in the Stacks Project.

**`DividedPowers.TateResolution.ExteriorOddVariable.equiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/ExteriorDividedPowers.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/ExteriorDividedPowers.lean#L303). The attribute's comment: “exterior algebra as an iterated odd variable extension”.

> The odd-variable extension of `⋀[R] M` is `⋀[R] (M × R)`.

```lean
public noncomputable def equiv :
    OddVariableExtension (exteriorGrade R M) 1 ≃ₐ[R] ExteriorAlgebra R (M × R)
```

**`DividedPowers.TateResolution.isCompatibleWithDifferential_exteriorDividedPowerStructure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/ExteriorKoszulCompatibility.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/ExteriorKoszulCompatibility.lean#L300). The attribute's comment: “compatibility with the Koszul differential”.

> The divided powers of `⋀[R] (Fin r → R)` are compatible with contraction by every `R`-linear
> functional, hence with the Koszul differential of every finite sequence in `R`.

```lean
public theorem isCompatibleWithDifferential_exteriorDividedPowerStructure (r : ℕ) :
    ∀ φ : Module.Dual R (Fin r → R),
      IsCompatibleWithDifferential (exteriorDividedPowerStructure R r)
        (CliffordAlgebra.contractLeft φ)
```

**`DividedPowers.TateResolution.existsUnique_oddVariableDividedPowerStructure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariable/Existence.lean, line 654](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariable/Existence.lean#L654). The attribute's comment: “existence and uniqueness”.

> There is a unique divided power structure on an odd-variable extension which extends the
> given divided powers on the coefficient algebra.

```lean
public theorem existsUnique_oddVariableDividedPowerStructure
    (Aᵢ : ℕ → Submodule R A) [GradedAlgebra Aᵢ] [IsStrictlyGradedComm Aᵢ]
    (gamma : DividedPowerStructure Aᵢ) (d : ℕ) (hd : 0 < d) (hd_odd : Odd d) :
    ∃! delta : DividedPowerStructure (OddVariableExtension.grade Aᵢ d),
      IsOddVariableDividedPowerExtension Aᵢ d gamma delta
```

**`DividedPowers.TateResolution.oddVariableDividedPowerStructure_dpow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariable/Existence.lean, line 690](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariable/Existence.lean#L690). The attribute's comment: “divided power formula”.

> For `x` in the positive even part and `y` in the odd part, the `n`th divided power of
> `x + yT` is `gamma_n(x) + gamma_(n - 1)(x)yT`.

```lean
public theorem oddVariableDividedPowerStructure_dpow
    (Aᵢ : ℕ → Submodule R A) [GradedAlgebra Aᵢ] [IsStrictlyGradedComm Aᵢ]
    (gamma : DividedPowerStructure Aᵢ) (d : ℕ) (hd : 0 < d) (hd_odd : Odd d)
    (n : ℕ) (hn : n ≠ 0) (x y : A) (hx : x ∈ positiveEvenPart Aᵢ)
    (hy : y ∈ oddPart Aᵢ) :
    (oddVariableDividedPowerStructure Aᵢ gamma d hd hd_odd).dpow n
        (inclusion Aᵢ d x + inclusion Aᵢ d y * generator Aᵢ d) =
      inclusion Aᵢ d (gamma.dpow n x) +
        inclusion Aᵢ d (gamma.dpow (n - 1) x * y) * generator Aᵢ d
```

**`DividedPowers.TateResolution.OddVariableExtension`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariable/Extension.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariable/Extension.lean#L197). The attribute's comment: “odd\_variable\_extension”.

> The odd-variable extension `A⟨T⟩`.  Its elements are pairs `(a, b)`, written
> mathematically as `a + bT`.

```lean
public abbrev OddVariableExtension (Aᵢ : ℕ → Submodule R A) [GradedAlgebra Aᵢ] (d : ℕ)
```

**`DividedPowers.TateResolution.OddVariableExtension.grade`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariable/Extension.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariable/Extension.lean#L256). The attribute's comment: “odd\_variable\_extension”.

> The degree-`m` piece `A_m ⊕ A_{m-d}T` of the odd-variable extension.

```lean
public def grade (Aᵢ : ℕ → Submodule R A) [GradedAlgebra Aᵢ] (d m : ℕ) :
    Submodule R (OddVariableExtension Aᵢ d)
```

**`DividedPowers.TateResolution.existsUnique_oddVariableExtension_ringHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/VariableLift.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/VariableLift.lean#L222). The attribute's comment: “mapping property”.

> The mapping property of the odd variable extension of Tag 09PH, for ring homomorphisms. A
> ring homomorphism out of `B⟨T⟩` which preserves degrees is determined by, and may be prescribed
> by, its restriction to `B` together with the image of `T`.

```lean
public theorem existsUnique_oddVariableExtension_ringHom
    (h : B →+* D) (hgrade : ∀ (m : ℕ) (b : B), b ∈ ℬ m → h b ∈ 𝒟 m)
    (d : ℕ) (hodd : Odd d) (t : D) (ht : t ∈ 𝒟 d) :
    ∃! g : OddVariableExtension ℬ d →+* D,
      (∀ b : B, g (inclusion ℬ d b) = h b) ∧
      g (generator ℬ d) = t ∧
      (∀ (m : ℕ) (x : OddVariableExtension ℬ d), x ∈ grade ℬ d m → g x ∈ 𝒟 m)
```

**`DividedPowers.TateResolution.oddVariableExtension_ringHom_dpow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/VariableLift.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/VariableLift.lean#L311). The attribute's comment: “mapping property”.

> A degree-preserving ring homomorphism out of an odd variable extension which restricts to a
> divided-power compatible map on the coefficients is itself compatible with divided powers.

```lean
public theorem oddVariableExtension_ringHom_dpow
    (h : B →+* D) (hgrade : ∀ (m : ℕ) (b : B), b ∈ ℬ m → h b ∈ 𝒟 m)
    (hdpow : ∀ (n : ℕ) (b : B), b ∈ positiveEvenPart ℬ → δ.dpow n (h b) = h (β.dpow n b))
    (d : ℕ) (hd : 0 < d) (hodd : Odd d) (t : D) (ht : t ∈ 𝒟 d)
    (g : OddVariableExtension ℬ d →+* D)
    (hg1 : ∀ b : B, g (inclusion ℬ d b) = h b) (hg2 : g (generator ℬ d) = t)
    (n : ℕ) (x : OddVariableExtension ℬ d) (hx : x ∈ positiveEvenPart (grade ℬ d)) :
    δ.dpow n (g x) = g ((oddVariableDividedPowerStructure ℬ β d hd hodd).dpow n x)
```

## Tag 09PI, an example

[Tag 09PI](https://stacks.math.columbia.edu/tag/09PI) in the Stacks Project.

**`DividedPowers.TateResolution.EvenVariableAlgebra`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariable.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariable.lean#L62). The attribute's comment: “even\_variable\_algebra”.

> The algebra of finite divided-power polynomials in one even variable over `A`.
>
> The coefficient at `n` is the coefficient of the formal symbol `T⁽ⁿ⁾`.

```lean
public structure EvenVariableAlgebra (A : Type v) [Ring A]
```

**`DividedPowers.TateResolution.EvenVariableAlgebra.mul`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariable.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariable.lean#L131). The attribute's comment: “even\_variable\_algebra”.

> The binomially weighted convolution product.

```lean
public def mul (x y : EvenVariableAlgebra A) : EvenVariableAlgebra A
```

**`DividedPowers.TateResolution.EvenVariableAlgebra.grade`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariable.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariable.lean#L351). The attribute's comment: “even\_variable\_algebra”.

> The degree-`m` piece after adjoining an even variable of degree `d`.
>
> Its coefficient of `T⁽ⁿ⁾` lies in `𝒜 (m - n * d)` when `n * d ≤ m`, and is zero
> otherwise.

```lean
public def grade (𝒜 : ℕ → Submodule R A) (d m : ℕ) :
    Submodule R (EvenVariableAlgebra A)
```

**`DividedPowers.TateResolution.EvenVariableAlgebra.gradedAlgebra`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariable.lean, line 559](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariable.lean#L559). The attribute's comment: “even\_variable\_algebra”.

> The shifted homogeneous pieces give an internal grading of the coefficient algebra.

```lean
public instance gradedAlgebra (𝒜 : ℕ → Submodule R A) [GradedAlgebra 𝒜]
    (d : ℕ) : GradedAlgebra (grade 𝒜 d)
```

**`DividedPowers.TateResolution.EvenVariableAlgebra.strictlyGradedComm`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariable.lean, line 614](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariable.lean#L614). The attribute's comment: “even\_variable\_algebra”.

> An even variable preserves strict graded commutativity, including vanishing odd squares.

```lean
public instance strictlyGradedComm (𝒜 : ℕ → Submodule R A) [IsStrictlyGradedComm 𝒜]
    (d : ℕ) [Fact (Even d)] : IsStrictlyGradedComm (grade 𝒜 d)
```

**`DividedPowers.TateResolution.evenVariableDividedPowerStructure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariableDividedPowers/Structure.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariableDividedPowers/Structure.lean#L280). The attribute's comment: “even\_variable\_divided\_powers”.

> The divided-power structure on the algebra obtained by adjoining an even
> variable of positive degree.

```lean
public noncomputable def evenVariableDividedPowerStructure
    (d : ℕ) [Fact (Even d)] (hd : 0 < d)
    (γ : DividedPowerStructure 𝒜) :
    DividedPowerStructure (EvenVariableAlgebra.grade 𝒜 d)
```

**`DividedPowers.TateResolution.dpow_coeffEmbedding`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariableDividedPowers/Structure.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariableDividedPowers/Structure.lean#L393). The attribute's comment: “even\_variable\_divided\_powers”.

> The new divided powers restrict to the original structure on `A`.

```lean
public theorem dpow_coeffEmbedding
    (d : ℕ) [Fact (Even d)] (hd : 0 < d)
    (γ : DividedPowerStructure 𝒜) (n : ℕ) {x : A}
    (hx : x ∈ positiveEvenPart 𝒜) :
    (evenVariableDividedPowerStructure d hd γ).dpow n (coeffEmbedding x) =
      coeffEmbedding (γ.dpow n x)
```

**`DividedPowers.TateResolution.dpow_monomial_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariableDividedPowers/Structure.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariableDividedPowers/Structure.lean#L404). The attribute's comment: “even\_variable\_divided\_powers”.

> The divided powers of the formal monomial `T⁽ⁱ⁾`.

```lean
public theorem dpow_monomial_one
    (d : ℕ) [Fact (Even d)] (hd : 0 < d)
    (γ : DividedPowerStructure 𝒜) (n i : ℕ) (hi : 0 < i) :
    (evenVariableDividedPowerStructure d hd γ).dpow n (monomial i (1 : A)) =
      monomial (n * i) (dividedPowerMonomialCoefficient n i • (1 : A))
```

**`DividedPowers.TateResolution.dpow_positivePolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariableDividedPowers/Structure.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariableDividedPowers/Structure.lean#L432). The attribute's comment: “even\_variable\_divided\_powers”.

> The multinomial expansion for a finite sum of positive-exponent terms
> whose coefficients are even.

```lean
public theorem dpow_positivePolynomial
    (d : ℕ) [Fact (Even d)] (hd : 0 < d)
    (γ : DividedPowerStructure 𝒜) (n : ℕ)
    (x : EvenVariableAlgebra A)
    (hzero : x.coeff 0 = 0)
    (heven : ∀ i : ℕ, 0 < i → x.coeff i ∈
      evenPart 𝒜) :
    (evenVariableDividedPowerStructure d hd γ).dpow n x =
      positivePolynomialDividedPower n x
```

**`DividedPowers.TateResolution.dpow_coeff_add_positive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariableDividedPowers/Structure.lean, line 579](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariableDividedPowers/Structure.lean#L579). The attribute's comment: “even\_variable\_divided\_powers”.

> Adding a positive-even constant coefficient obeys the divided-power
> binomial formula.

```lean
public theorem dpow_coeff_add_positive
    (d : ℕ) [Fact (Even d)] (hd : 0 < d)
    (γ : DividedPowerStructure 𝒜) (n : ℕ)
    {x₀ : A} (hx₀ : x₀ ∈ positiveEvenPart 𝒜)
    (x : EvenVariableAlgebra A)
    (hzero : x.coeff 0 = 0)
    (heven : ∀ i : ℕ, 0 < i → x.coeff i ∈
      evenPart 𝒜) :
    (evenVariableDividedPowerStructure d hd γ).dpow n (coeffEmbedding x₀ + x) =
    ∑ ij ∈ Finset.antidiagonal n,
        coeffEmbedding (γ.dpow ij.1 x₀) *
      (evenVariableDividedPowerStructure d hd γ).dpow ij.2 x
```

**`DividedPowers.TateResolution.evenVariableDividedPowerStructure_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariableDividedPowers/Structure.lean, line 607](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariableDividedPowers/Structure.lean#L607). The attribute's comment: “even\_variable\_divided\_powers”.

> Compatibility and the formal-monomial rule determine the divided-power
> structure uniquely.

```lean
public theorem evenVariableDividedPowerStructure_unique
    (d : ℕ) [Fact (Even d)] (hd : 0 < d)
    (γ : DividedPowerStructure 𝒜)
    (δ : DividedPowerStructure (EvenVariableAlgebra.grade 𝒜 d))
    (hcompat : ∀ (n : ℕ) {x : A},
      x ∈ positiveEvenPart 𝒜 →
        δ.dpow n (coeffEmbedding x) = coeffEmbedding (γ.dpow n x))
    (hmonomial : ∀ (n i : ℕ), 0 < i →
      δ.dpow n (monomial i (1 : A)) =
        monomial (n * i) (dividedPowerMonomialCoefficient n i • (1 : A))) :
    δ = evenVariableDividedPowerStructure d hd γ
```

**`DividedPowers.TateResolution.evenVariableAlgebra_ringHom_dpow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariableLift.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariableLift.lean#L89). The attribute's comment: “mapping property”.

> A degree-preserving ring homomorphism out of an even variable algebra which restricts to a
> divided-power compatible map on the coefficients is itself compatible with divided powers.

```lean
public theorem evenVariableAlgebra_ringHom_dpow
    (h : B →+* D)
    (hdpow : ∀ (n : ℕ) (b : B), b ∈ positiveEvenPart ℬ → δ.dpow n (h b) = h (β.dpow n b))
    (d : ℕ) [Fact (Even d)] (hd : 0 < d) (t : D) (ht : t ∈ 𝒟 d)
    (g : EvenVariableAlgebra B →+* D)
    (hg1 : ∀ b : B, g (coeffEmbedding b) = h b)
    (hg2 : ∀ n : ℕ, g (monomial n (1 : B)) = δ.dpow n t)
    (hg3 : ∀ (m : ℕ) (x : EvenVariableAlgebra B),
      x ∈ EvenVariableAlgebra.grade ℬ d m → g x ∈ 𝒟 m)
    (n : ℕ) (x : EvenVariableAlgebra B)
    (hx : x ∈ positiveEvenPart (EvenVariableAlgebra.grade ℬ d)) :
    δ.dpow n (g x) = g ((evenVariableDividedPowerStructure d hd β).dpow n x)
```

**`DividedPowers.TateResolution.existsUnique_evenVariableAlgebra_ringHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/VariableLift.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/VariableLift.lean#L390). The attribute's comment: “mapping property”.

> The mapping property of the even variable algebra of Tag 09PI, for ring homomorphisms. A
> ring homomorphism out of `B⟨T⟩` is determined by, and may be prescribed by, its restriction to
> `B` together with a choice of images for the divided powers of `T`, which must be the divided
> powers of a single element of degree `d`.

```lean
public theorem existsUnique_evenVariableAlgebra_ringHom
    (h : B →+* D) (hgrade : ∀ (m : ℕ) (b : B), b ∈ ℬ m → h b ∈ 𝒟 m)
    (d : ℕ) (hd : 0 < d) (heven : Even d) (t : D) (ht : t ∈ 𝒟 d) :
    ∃! g : EvenVariableAlgebra B →+* D,
      (∀ b : B, g (coeffEmbedding b) = h b) ∧
      (∀ n : ℕ, g (monomial n (1 : B)) = δ.dpow n t) ∧
      (∀ (m : ℕ) (x : EvenVariableAlgebra B),
        x ∈ EvenVariableAlgebra.grade ℬ d m → g x ∈ 𝒟 m)
```

## Tag 0F4I, a remark

[Tag 0F4I](https://stacks.math.columbia.edu/tag/0F4I) in the Stacks Project.

**`DividedPowers.TateResolution.ringHom_dpow_of_finiteVariableStage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/GradedProduct.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/GradedProduct.lean#L153). The attribute's comment: “divided powers on a finite stage”.

> Compatibility with divided powers propagates from the coefficients and the adjoined variables
> to a whole finite variable stage. The argument is that the graph of the homomorphism is a subring
> of the product containing the images of the generators, and that finite variable stages of the
> product are stable under its divided powers.
>
> This supersedes the `private` `map_dpow_of_finiteVariableStage` of
> `StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableExtension/Construction.lean`,
> generalized from an algebra homomorphism to a ring homomorphism commuting with the structure
> maps.

```lean
public theorem ringHom_dpow_of_finiteVariableStage
    {R : Type u} {P : Type v} {C : Type z} {D : Type*} {J : Type w}
    [CommRing R] [Ring P] [Ring C] [Ring D]
    [Algebra R P] [Algebra R C] [Algebra R D]
    (Pᵢ : ℕ → Submodule R P) [GradedAlgebra Pᵢ]
    (Cᵢ : ℕ → Submodule R C) [GradedAlgebra Cᵢ] [IsStrictlyGradedComm Cᵢ]
    (Dᵢ : ℕ → Submodule R D) [GradedAlgebra Dᵢ] [IsStrictlyGradedComm Dᵢ]
    (δ : DividedPowerStructure Cᵢ) (ε : DividedPowerStructure Dᵢ)
    (ι : P →ₐ[R] C) (T : J → C) (S : Finset J) (d : ℕ)
    (hgrade : ∀ (m : ℕ) (a : P), a ∈ Pᵢ m → ι a ∈ Cᵢ m)
    (hT : ∀ j : J, T j ∈ Cᵢ d)
    (hclosed : ∀ (n : ℕ) (a : P), ι a ∈ positiveEvenPart Cᵢ →
      δ.dpow n (ι a) ∈ Set.range ι)
    (f : C →+* D) (hf : ∀ (m : ℕ) (x : C), x ∈ Cᵢ m → f x ∈ Dᵢ m)
    (hfalg : ∀ r : R, f (algebraMap R C r) = algebraMap R D r)
    (hcoeff : ∀ (n : ℕ) (a : P), ι a ∈ positiveEvenPart Cᵢ →
      ε.dpow n (f (ι a)) = f (δ.dpow n (ι a)))
    (hgen : ∀ (n : ℕ) (j : J), T j ∈ positiveEvenPart Cᵢ →
      ε.dpow n (f (T j)) = f (δ.dpow n (T j)))
    {x : C} (hx : x ∈ finiteVariableStage δ ι T S)
    (hp : x ∈ positiveEvenPart Cᵢ) (n : ℕ) :
    ε.dpow n (f x) = f (δ.dpow n x)
```

**`DividedPowers.TateResolution.finiteVariableStages_directedColimit_addHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableDerivation.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableDerivation.lean#L153). The attribute's comment: “directed colimit of finite stages, additively”.

> The additive analogue of `finiteVariableStages_directedColimit`: if the finite variable stages
> cover the extension, a family of additive maps out of them which agree wherever their arguments
> agree extends uniquely to an additive map out of the whole extension.

```lean
public theorem finiteVariableStages_directedColimit_addHom
    {R : Type u} {A : Type v} {C : Type z} {D : Type w} {J : Type*}
    [CommRing R] [Ring A] [Ring C] [AddCommGroup D] [Algebra R A] [Algebra R C]
    (Cᵢ : ℕ → Submodule R C) [GradedAlgebra Cᵢ]
    [IsStrictlyGradedComm Cᵢ] (δ : DividedPowerStructure Cᵢ)
    (ι : A →ₐ[R] C) (T : J → C)
    (hfinite : ∀ x : C, ∃ S : Finset J, x ∈ finiteVariableStage δ ι T S)
    (f : (S : Finset J) → finiteVariableStage δ ι T S →+ D)
    (hcompat : ∀ (S U : Finset J)
      (x : finiteVariableStage δ ι T S)
      (y : finiteVariableStage δ ι T U),
      (x : C) = (y : C) → f S x = f U y) :
    ∃! g : C →+ D,
      ∀ (S : Finset J) (x : finiteVariableStage δ ι T S),
        g (x : C) = f S x
```

**`DividedPowers.TateResolution.exists_gradedDividedPowerColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableExtension/Construction/DirectLimit.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableExtension/Construction/DirectLimit.lean#L299). The attribute's comment: “directed colimit of graded algebras with divided powers”.

> The colimit of a directed system of strictly graded-commutative nonnegatively graded
> algebras with divided powers on their positive even parts, indexed by an arbitrary nonempty
> directed preorder.
>
> The colimit is graded by the elements coming from a homogeneous element of some stage, carries
> the unique divided power structure for which every stage map preserves divided powers, and has
> both the algebra and the module universal property: the first produces maps of graded algebras
> with divided powers, the second — which is what a colimit of differentials needs, a differential
> being linear and not multiplicative — produces `R`-linear maps.  Every element of the colimit,
> homogeneous or not, comes from a stage, and two stage elements with the same image in the
> colimit already agree at a later stage.

```lean
public theorem exists_gradedDividedPowerColimit
    {R : Type u} [CommRing R] {I : Type w}
    [Preorder I] [IsDirectedOrder I] [Nonempty I]
    (B : I → Type v) [stageRing : ∀ S, Ring (B S)] [stageAlgebra : ∀ S, Algebra R (B S)]
    (Bᵢ : (S : I) → ℕ → Submodule R (B S))
    [stageGraded : ∀ S, GradedAlgebra (Bᵢ S)]
    [stageComm : ∀ S, IsStrictlyGradedComm (Bᵢ S)]
    (γ : (S : I) → DividedPowerStructure (Bᵢ S))
    (transition : ∀ {S T : I}, S ≤ T → B S →ₐ[R] B T)
    (htransition_self : ∀ (S : I) (x : B S), transition (le_refl S) x = x)
    (htransition_comp : ∀ {S T U : I} (h : S ≤ T) (h' : T ≤ U) (x : B S),
      transition h' (transition h x) = transition (h.trans h') x)
    (htransition_grade : ∀ {S T : I} (h : S ≤ T) (m : ℕ) (x : B S),
      x ∈ Bᵢ S m → transition h x ∈ Bᵢ T m)
    (htransition_dpow : ∀ {S T : I} (h : S ≤ T) (n : ℕ) (x : B S),
      x ∈ positiveEvenPart (Bᵢ S) →
        transition h ((γ S).dpow n x) = (γ T).dpow n (transition h x)) :
    ∃ (C : Type (max v w)) (ringC : Ring C),
      letI : Ring C := ringC
      ∃ algebraC : Algebra R C,
        letI : Algebra R C := algebraC
        ∃ (Cᵢ : ℕ → Submodule R C) (gradedC : GradedAlgebra Cᵢ),
          letI : GradedAlgebra Cᵢ := gradedC
          ∃ strictC : IsStrictlyGradedComm Cᵢ,
            letI : IsStrictlyGradedComm Cᵢ := strictC
            ∃ (δ : DividedPowerStructure Cᵢ) (incl : (S : I) → B S →ₐ[R] C),
              (∀ {S T : I} (h : S ≤ T) (x : B S), incl T (transition h x) = incl S x) ∧
              (∀ (S : I) (m : ℕ) (x : B S), x ∈ Bᵢ S m → incl S x ∈ Cᵢ m) ∧
              (∀ (m : ℕ) (x : C), x ∈ Cᵢ m →
                ∃ (S : I) (y : B S), y ∈ Bᵢ S m ∧ incl S y = x) ∧
              (∀ x : C, ∃ (S : I) (y : B S), incl S y = x) ∧
              (∀ (S : I) (n : ℕ) (x : B S), x ∈ positiveEvenPart (Bᵢ S) →
                δ.dpow n (incl S x) = incl S ((γ S).dpow n x)) ∧
              (∀ (S T : I) (x : B S) (y : B T), incl S x = incl T y →
                ∃ U : I, ∃ (hS : S ≤ U) (hT : T ≤ U),
                  transition hS x = transition hT y) ∧
              (∀ {D : Type z} [Ring D] [Algebra R D] (Dᵢ : ℕ → Submodule R D)
                  [GradedAlgebra Dᵢ] [IsStrictlyGradedComm Dᵢ]
                  (ε : DividedPowerStructure Dᵢ) (g : (S : I) → B S →ₐ[R] D),
                  (∀ {S T : I} (h : S ≤ T) (x : B S), g T (transition h x) = g S x) →
                  (∀ (S : I) (m : ℕ) (x : B S), x ∈ Bᵢ S m → g S x ∈ Dᵢ m) →
                  (∀ (S : I) (n : ℕ) (x : B S), x ∈ positiveEvenPart (Bᵢ S) →
                    ε.dpow n (g S x) = g S ((γ S).dpow n x)) →
                  ∃! F : C →ₐ[R] D,
                    (∀ (S : I) (x : B S), F (incl S x) = g S x) ∧
                    (∀ (m : ℕ) (x : C), x ∈ Cᵢ m → F x ∈ Dᵢ m) ∧
                    (∀ (n : ℕ) (x : C), x ∈ positiveEvenPart Cᵢ →
                      ε.dpow n (F x) = F (δ.dpow n x))) ∧
              ∀ {M : Type y} [AddCommGroup M] [Module R M] (g : (S : I) → B S →ₗ[R] M),
                  (∀ {S T : I} (h : S ≤ T) (x : B S), g T (transition h x) = g S x) →
                  ∃! F : C →ₗ[R] M, ∀ (S : I) (x : B S), F (incl S x) = g S x
```

**`DividedPowers.TateResolution.exists_setVariableDividedPowerExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableExtension/Construction/Existence.lean, line 414](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableExtension/Construction/Existence.lean#L414). The attribute's comment: “set-indexed construction”.

> A set of positive-degree variables has a free strictly graded-commutative algebra with
> divided powers over a graded divided-power algebra. Every element involves only finitely many
> variables (including their divided powers). The universal property fixes the coefficient and
> generator maps, and requires target maps to preserve grading and divided powers.

```lean
public theorem exists_setVariableDividedPowerExtension
    {R : Type u} {A : Type v} [CommRing R] [Ring A] [Algebra R A]
    (Aᵢ : ℕ → Submodule R A) [GradedAlgebra Aᵢ]
    [IsStrictlyGradedComm Aᵢ] (γ : DividedPowerStructure Aᵢ)
    (J : Type w) (deg : J → ℕ) (hdeg : ∀ j, 0 < deg j) :
    ∃ (C : Type (max u v w)) (ringC : Ring C),
      letI : Ring C := ringC
      ∃ (algebraC : Algebra R C),
        letI : Algebra R C := algebraC
        ∃ (Cᵢ : ℕ → Submodule R C) (gradedC : GradedAlgebra Cᵢ),
          letI : GradedAlgebra Cᵢ := gradedC
          ∃ (strictC : IsStrictlyGradedComm Cᵢ),
            letI : IsStrictlyGradedComm Cᵢ := strictC
            ∃ (δ : DividedPowerStructure Cᵢ) (ι : A →ₐ[R] C) (T : J → C),
              Function.Injective ι ∧
              (∀ (m : ℕ) (a : A), a ∈ Aᵢ m → ι a ∈ Cᵢ m) ∧
              (∀ (n : ℕ) (a : A), a ∈ positiveEvenPart Aᵢ →
                δ.dpow n (ι a) = ι (γ.dpow n a)) ∧
              (∀ j : J, T j ∈ Cᵢ (deg j)) ∧
              (∀ x : C, ∃ S : Finset J,
                x ∈ finiteVariableStage δ ι T S) ∧
              (∀ (S : Finset J) (j : J), j ∉ S →
                letI : DecidableEq J := Classical.decEq J
                ∃ (aS : Algebra R (finiteVariableStage δ ι T S)),
                  letI : Algebra R (finiteVariableStage δ ι T S) := aS
                  (∀ r : R, ((algebraMap R (finiteVariableStage δ ι T S) r :
                    finiteVariableStage δ ι T S) : C) = algebraMap R C r) ∧
                  ∃ (Sᵢ : ℕ → Submodule R (finiteVariableStage δ ι T S))
                    (gS : GradedAlgebra Sᵢ),
                    letI : GradedAlgebra Sᵢ := gS
                    ∃ (cS : IsStrictlyGradedComm Sᵢ),
                      letI : IsStrictlyGradedComm Sᵢ := cS
                      ∃ δS : DividedPowerStructure Sᵢ,
                      (∀ (n : ℕ) (b : finiteVariableStage δ ι T S),
                        b ∈ positiveEvenPart Sᵢ →
                          (δS.dpow n b : C) = δ.dpow n (b : C)) ∧
                      (∀ hodd : Odd (deg j),
                        ∃ e : OddVariableExtension Sᵢ (deg j) ≃+*
                            finiteVariableStage δ ι T (insert j S),
                          (∀ b : finiteVariableStage δ ι T S,
                            ((e (OddVariableExtension.inclusion
                              Sᵢ (deg j) b) : finiteVariableStage δ ι T (insert j S)) : C) = b) ∧
                          ((e (OddVariableExtension.generator
                            Sᵢ (deg j)) : finiteVariableStage δ ι T (insert j S)) : C) = T j ∧
                          (∀ (m : ℕ)
                            (x : OddVariableExtension Sᵢ (deg j)),
                            x ∈
                                OddVariableExtension.grade
                                  Sᵢ (deg j) m ↔
                              (e x : C) ∈ Cᵢ m) ∧
                          (∀ (n : ℕ)
                            (x : OddVariableExtension Sᵢ (deg j)),
                            x ∈ positiveEvenPart
                              (OddVariableExtension.grade Sᵢ (deg j)) →
                            δ.dpow n (e x : C) =
                              (e ((oddVariableDividedPowerStructure
                                Sᵢ δS (deg j) (hdeg j) hodd).dpow n x) : C))) ∧
                      (∀ heven : Even (deg j),
                        letI : Fact (Even (deg j)) := ⟨heven⟩
                        ∃ e : EvenVariableAlgebra
                            (finiteVariableStage δ ι T S) ≃+*
                            finiteVariableStage δ ι T (insert j S),
                          (∀ b : finiteVariableStage δ ι T S,
                            ((e (EvenVariableAlgebra.coeffEmbedding
                              b) :
                              finiteVariableStage δ ι T (insert j S)) : C) = b) ∧
                          ((e (EvenVariableAlgebra.monomial
                            1 1) : finiteVariableStage δ ι T (insert j S)) : C) = T j ∧
                          (∀ (m : ℕ)
                            (x : EvenVariableAlgebra
                              (finiteVariableStage δ ι T S)),
                            x ∈
                                EvenVariableAlgebra.grade
                                  Sᵢ (deg j) m ↔
                              (e x : C) ∈ Cᵢ m) ∧
                          (∀ (n : ℕ)
                            (x : EvenVariableAlgebra
                              (finiteVariableStage δ ι T S)),
                            x ∈ positiveEvenPart
                              (EvenVariableAlgebra.grade Sᵢ (deg j)) →
                            δ.dpow n (e x : C) =
                              (e ((evenVariableDividedPowerStructure (deg j) (hdeg j)
                                δS).dpow n x) : C)))) ∧
              (∀ {D : Type z} [Ring D] [Algebra R D]
                  (Dᵢ : ℕ → Submodule R D) [GradedAlgebra Dᵢ]
                  [IsStrictlyGradedComm Dᵢ] (ε : DividedPowerStructure Dᵢ)
                  (f : A →ₐ[R] D) (t : J → D),
                  (∀ (m : ℕ) (a : A), a ∈ Aᵢ m → f a ∈ Dᵢ m) →
                  (∀ (n : ℕ) (a : A), a ∈ positiveEvenPart Aᵢ →
                    ε.dpow n (f a) = f (γ.dpow n a)) →
                  (∀ j : J, t j ∈ Dᵢ (deg j)) →
                  ∃! g : C →ₐ[R] D,
                    (∀ a : A, g (ι a) = f a) ∧
                    (∀ j : J, g (T j) = t j) ∧
                    (∀ (m : ℕ) (x : C), x ∈ Cᵢ m → g x ∈ Dᵢ m) ∧
                    (∀ (n : ℕ) (x : C), x ∈ positiveEvenPart Cᵢ →
                      ε.dpow n (g x) = g (δ.dpow n x)))
```

**`DividedPowers.TateResolution.finiteVariableStage_insert`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableExtension/FiniteStage/DirectedColimit.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableExtension/FiniteStage/DirectedColimit.lean#L74). The attribute's comment: “finite iterated one-variable extensions”.

> A successor finite stage is obtained by adjoining its new variable and all of its
> divided powers to the preceding stage. For an odd-degree variable its positive divided
> powers vanish, recovering the exterior successor; in even degree this is the divided-power
> successor. Iterating this equation over an enumeration of a finite set gives the finite
> stages used in the directed colimit.

```lean
public theorem finiteVariableStage_insert
    {R : Type u} {A : Type v} {C : Type z} {J : Type w}
    [CommRing R] [Ring A] [Ring C] [Algebra R A] [Algebra R C]
    (Cᵢ : ℕ → Submodule R C) [GradedAlgebra Cᵢ]
    [IsStrictlyGradedComm Cᵢ] (δ : DividedPowerStructure Cᵢ)
    (ι : A →ₐ[R] C) (T : J → C) (S U : Finset J) (j : J)
    (hSU : S ⊆ U) (hj : j ∈ U)
    (hU : ∀ k : J, k ∈ U → (k ∈ S ∨ k = j)) :
    finiteVariableStage δ ι T U =
      Subring.closure
        ((finiteVariableStage δ ι T S : Set C) ∪
          {x : C | x = T j ∨ ∃ n : ℕ, x = δ.dpow n (T j)})
```

**`DividedPowers.TateResolution.finiteVariableStage_empty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableExtension/FiniteStage/DirectedColimit.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableExtension/FiniteStage/DirectedColimit.lean#L114). The attribute's comment: “initial finite stage”.

> The initial finite stage is generated by the coefficient algebra.

```lean
public theorem finiteVariableStage_empty
    {R : Type u} {A : Type v} {C : Type z} {J : Type w}
    [CommRing R] [Ring A] [Ring C] [Algebra R A] [Algebra R C]
    (Cᵢ : ℕ → Submodule R C) [GradedAlgebra Cᵢ]
    [IsStrictlyGradedComm Cᵢ] (δ : DividedPowerStructure Cᵢ)
    (ι : A →ₐ[R] C) (T : J → C) :
    finiteVariableStage δ ι T ∅ = Subring.closure (Set.range ι)
```

**`DividedPowers.TateResolution.finiteVariableStages_directedColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableExtension/FiniteStage/DirectedColimit.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableExtension/FiniteStage/DirectedColimit.lean#L141). The attribute's comment: “directed colimit of finite stages”.

> If the finite-variable stages cover the algebra, they present it as their directed colimit:
> a family of ring homomorphisms out of the stages which agree wherever their arguments agree in
> the ambient algebra extends uniquely to a ring homomorphism out of the whole algebra.

```lean
public theorem finiteVariableStages_directedColimit
    {R : Type u} {A : Type v} {C : Type z} {D : Type w} {J : Type*}
    [CommRing R] [Ring A] [Ring C] [Ring D] [Algebra R A] [Algebra R C]
    (Cᵢ : ℕ → Submodule R C) [GradedAlgebra Cᵢ]
    [IsStrictlyGradedComm Cᵢ] (δ : DividedPowerStructure Cᵢ)
    (ι : A →ₐ[R] C) (T : J → C)
    (hfinite : ∀ x : C, ∃ S : Finset J,
      x ∈ finiteVariableStage δ ι T S)
    (f : (S : Finset J) → finiteVariableStage δ ι T S →+* D)
    (hcompat : ∀ (S U : Finset J)
      (x : finiteVariableStage δ ι T S)
      (y : finiteVariableStage δ ι T U),
      (x : C) = (y : C) → f S x = f U y) :
    ∃! g : C →+* D,
      ∀ (S : Finset J) (x : finiteVariableStage δ ι T S),
        g (x : C) = f S x
```

**`DividedPowers.TateResolution.existsUnique_dividedPowerStructure_of_finiteStages`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableExtension/FiniteStage/DividedPowerStructure.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableExtension/FiniteStage/DividedPowerStructure.lean#L457). The attribute's comment: “finite-stage extension”.

> Let a directed system of strictly graded-commutative graded algebras with divided powers,
> indexed by a nonempty directed preorder, map compatibly to a strictly graded-commutative graded
> algebra `C` in such a way that homogeneous elements of `C` lift to some stage and two stage
> elements with the same image in `C` already agree at a later stage. Then `C` carries exactly one
> divided power structure for which every stage map preserves divided powers.
>
> The index order is an arbitrary nonempty directed one; the finite subsets of a set ordered by
> inclusion, which is the indexing of the set-variable construction of Tag 0F4I, are the special
> case `I = Finset J`, and an `ℕ`-indexed tower is the case `I = ℕ`.

```lean
public theorem existsUnique_dividedPowerStructure_of_finiteStages
    {R : Type u} [CommRing R] {I : Type w} [LE I] [IsDirectedOrder I] [Nonempty I]
    (B : I → Type v)
    [stageRing : ∀ S, Ring (B S)]
    [stageAlgebra : ∀ S, Algebra R (B S)]
    (Bᵢ : (S : I) → ℕ → Submodule R (B S))
    [stageGraded : ∀ S, GradedAlgebra (Bᵢ S)]
    [stageComm : ∀ S, IsStrictlyGradedComm (Bᵢ S)]
    (γ : (S : I) → DividedPowerStructure (Bᵢ S))
    {C : Type z} [Ring C] [Algebra R C]
    (Cᵢ : ℕ → Submodule R C) [GradedAlgebra Cᵢ] [IsStrictlyGradedComm Cᵢ]
    (transition : ∀ {S T : I}, S ≤ T → B S →ₐ[R] B T)
    (ι : (S : I) → B S →ₐ[R] C)
    (hι : ∀ {S T : I} (h : S ≤ T) (x : B S),
      ι T (transition h x) = ι S x)
    (hgrade : ∀ (S : I) (m : ℕ) (x : B S),
      x ∈ Bᵢ S m → ι S x ∈ Cᵢ m)
    (hgrade_lift : ∀ (m : ℕ) (x : C), x ∈ Cᵢ m →
      ∃ (S : I) (y : B S), y ∈ Bᵢ S m ∧ ι S y = x)
    (heq : ∀ (S T : I) (x : B S) (y : B T),
      ι S x = ι T y →
      ∃ U : I, ∃ (hS : S ≤ U) (hT : T ≤ U),
        transition hS x = transition hT y)
    (htransition_grade : ∀ {S T : I} (h : S ≤ T)
      (m : ℕ) (x : B S), x ∈ Bᵢ S m → transition h x ∈ Bᵢ T m)
    (htransition_dpow : ∀ {S T : I} (h : S ≤ T)
      (n : ℕ) (x : B S), x ∈ positiveEvenPart (Bᵢ S) →
        transition h ((γ S).dpow n x) = (γ T).dpow n (transition h x)) :
    ∃! δ : DividedPowerStructure Cᵢ,
      ∀ (S : I) (n : ℕ) (x : B S),
        x ∈ positiveEvenPart (Bᵢ S) →
          δ.dpow n (ι S x) = ι S ((γ S).dpow n x)
```

**`DividedPowers.TateResolution.finiteVariableStage_dpow_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableExtension/FiniteStage/DividedPowerStructure.lean, line 705](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableExtension/FiniteStage/DividedPowerStructure.lean#L705). The attribute's comment: “finite stages preserve divided powers”.

> Divided powers of elements supported on a finite set of homogeneous variables over a
> graded coefficient algebra are still supported on that set. The variables need not all have the
> same degree: each `T j` is homogeneous of its own degree `deg j`. The coefficient map preserves
> grading, as do the inclusions in the extensions of Tags 09PH and 09PI. Thus every
> finite-variable stage is a divided-power subalgebra.

```lean
public theorem finiteVariableStage_dpow_mem
    {R : Type u} {A : Type v} {C : Type z} {J : Type w}
    [CommRing R] [Ring A] [Ring C] [Algebra R A] [Algebra R C]
    (Aᵢ : ℕ → Submodule R A) [GradedAlgebra Aᵢ]
    (Cᵢ : ℕ → Submodule R C) [GradedAlgebra Cᵢ]
    [IsStrictlyGradedComm Cᵢ] (δ : DividedPowerStructure Cᵢ)
    (ι : A →ₐ[R] C) (T : J → C) (S : Finset J) (deg : J → ℕ)
    (hgrade : ∀ (m : ℕ) (a : A), a ∈ Aᵢ m → ι a ∈ Cᵢ m)
    (hT : ∀ j : J, T j ∈ Cᵢ (deg j))
    (hcoeff : ∀ (n : ℕ) (a : A), ι a ∈ positiveEvenPart Cᵢ →
      δ.dpow n (ι a) ∈ Set.range ι)
    (n : ℕ) (x : C)
    (hx : x ∈ finiteVariableStage δ ι T S)
    (hpositive : x ∈ positiveEvenPart Cᵢ) :
    δ.dpow n x ∈ finiteVariableStage δ ι T S
```

**`DividedPowers.TateResolution.dividedPowerStructure_unique_of_generators`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableExtension/FiniteStage/DividedPowerStructure.lean, line 1195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableExtension/FiniteStage/DividedPowerStructure.lean#L1195). The attribute's comment: “uniqueness”.

> On a set-indexed extension, divided powers are forced by their restriction to the
> coefficient algebra and by their values on the adjoined generators.

```lean
public theorem dividedPowerStructure_unique_of_generators
    {R : Type u} {A : Type v} {C : Type z} {J : Type w}
    [CommRing R] [Ring A] [Ring C] [Algebra R A] [Algebra R C]
    (Aᵢ : ℕ → Submodule R A) [GradedAlgebra Aᵢ]
    (d : ℕ) (hd : 0 < d)
    (Cᵢ : ℕ → Submodule R C) [GradedAlgebra Cᵢ]
    [IsStrictlyGradedComm Cᵢ]
    (δ ε : DividedPowerStructure Cᵢ) (ι : A →ₐ[R] C) (T : J → C)
    (hgrade : ∀ (m : ℕ) (a : A), a ∈ Aᵢ m → ι a ∈ Cᵢ m)
    (hT : ∀ j : J, T j ∈ Cᵢ d)
    (hfinite : ∀ x : C, ∃ S : Finset J, x ∈ finiteVariableStage δ ι T S)
    (hcoeff : ∀ (n : ℕ) (a : A), ι a ∈ positiveEvenPart Cᵢ →
      ε.dpow n (ι a) = δ.dpow n (ι a))
    (hgenerator : ∀ (n : ℕ) (j : J), T j ∈ positiveEvenPart Cᵢ →
      ε.dpow n (T j) = δ.dpow n (T j)) :
    ε = δ
```

## Tag 09PJ, a definition

[Tag 09PJ](https://stacks.math.columbia.edu/tag/09PJ) in the Stacks Project.

**`DividedPowers.TateResolution.IsCompatibleWithDifferential`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/Basic.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/Basic.lean#L261).

> A divided power structure is compatible with a differential if the differential of every
> positive divided power has the expected divided-power derivative.

```lean
public class IsCompatibleWithDifferential {𝒜 : ℕ → Submodule R A} [GradedAlgebra 𝒜]
    [IsStrictlyGradedComm 𝒜] (γ : DividedPowerStructure 𝒜) (d : A →ₗ[R] A) : Prop
```

## Tag 09PK, a lemma

[Tag 09PK](https://stacks.math.columbia.edu/tag/09PK) in the Stacks Project.

**`DividedPowers.TateResolution.dividedPowerStructureOnHomology_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/Homology/DividedPowerStructure.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/Homology/DividedPowerStructure.lean#L37).

> A surjective morphism from a positively acyclic divided-power DGA induces divided
> powers on the actual homology quotient of its target. The induced operations agree with
> the original operations on homogeneous cycles.

```lean
public theorem dividedPowerStructureOnHomology_of_surjective
    {R : Type u} {A : Type v} {B : Type w}
    [CommRing R] [Ring A] [Ring B]
    [Algebra R A] [Algebra R B]
    (𝒜 : ℕ → Submodule R A) (ℬ : ℕ → Submodule R B)
    [GradedAlgebra 𝒜] [GradedAlgebra ℬ]
    [IsStrictlyGradedComm 𝒜] [IsStrictlyGradedComm ℬ]
    (dA : A →ₗ[R] A) (dB : B →ₗ[R] B)
    [IsDifferentialGradedAlgebra 𝒜 dA] [IsDifferentialGradedAlgebra ℬ dB]
    (γA : DividedPowerStructure 𝒜) (γB : DividedPowerStructure ℬ)
    [IsCompatibleWithDifferential γA dA] [IsCompatibleWithDifferential γB dB]
    (f : A →ₐ[R] B)
    (hf_grade : ∀ {n : ℕ} {x : A}, x ∈ 𝒜 n → f x ∈ ℬ n)
    (hf_d : ∀ x : A, f (dA x) = dB (f x))
    (hf_dpow : ∀ {n : ℕ} {x : A}, x ∈ positiveEvenPart 𝒜 →
      f (γA.dpow n x) = γB.dpow n (f x))
    (hf_surjective : Function.Surjective f)
    (hA : ∀ {n : ℕ}, 0 < n → ∀ {x : A}, x ∈ 𝒜 n → dA x = 0 →
      ∃ z : A, z ∈ 𝒜 (n + 1) ∧ dA z = x)
    : ∃ hRing : Ring (Homology (𝒜 := ℬ) dB),
      letI : Ring (Homology (𝒜 := ℬ) dB) := hRing
      ∃ hAlgebra : Algebra R (Homology (𝒜 := ℬ) dB),
        letI : Algebra R (Homology (𝒜 := ℬ) dB) := hAlgebra
        letI : AddCommMonoid (Homology (𝒜 := ℬ) dB) := hRing.toAddCommMonoid
        letI : Module R (Homology (𝒜 := ℬ) dB) := Algebra.toModule
        let ℋ : ℕ → Submodule R (Homology (𝒜 := ℬ) dB) := fun n =>
          Submodule.span R {z | ∃ x : cycles dB, (x : B) ∈ ℬ n ∧
            (Submodule.Quotient.mk x : Homology (𝒜 := ℬ) dB) = z}
        ∃ hGraded : GradedAlgebra ℋ,
          letI : GradedAlgebra ℋ := hGraded
          ∃ hStrict : IsStrictlyGradedComm ℋ,
            letI : IsStrictlyGradedComm ℋ := hStrict
            ∃ γH : @DividedPowerStructure R (Homology (𝒜 := ℬ) dB)
                _ hRing hAlgebra ℋ hGraded hStrict,
              (Submodule.Quotient.mk (0 : cycles dB) :
                Homology (𝒜 := ℬ) dB) = 0 ∧
              (∀ x y : cycles dB,
                (Submodule.Quotient.mk (x + y) : Homology (𝒜 := ℬ) dB) =
                  Submodule.Quotient.mk x + Submodule.Quotient.mk y) ∧
              (∀ (r : R) (x : cycles dB),
                (Submodule.Quotient.mk (r • x) : Homology (𝒜 := ℬ) dB) =
                  r • (Submodule.Quotient.mk x : Homology (𝒜 := ℬ) dB)) ∧
              (∃ h1 : dB (1 : B) = 0,
                (Submodule.Quotient.mk (⟨1, h1⟩ : cycles dB) :
                  Homology (𝒜 := ℬ) dB) = 1) ∧
              (∀ {x y : B} (hx : dB x = 0) (hy : dB y = 0),
                ∃ hxy : dB (x * y) = 0,
                  (Submodule.Quotient.mk (⟨x * y, hxy⟩ : cycles dB) :
                    Homology (𝒜 := ℬ) dB) =
                    Submodule.Quotient.mk (⟨x, hx⟩ : cycles dB) *
                      Submodule.Quotient.mk (⟨y, hy⟩ : cycles dB)) ∧
              (∀ {n : ℕ} {x : B} (_hx : x ∈ positiveEvenPart ℬ)
                  (hd : dB x = 0),
                ∃ hγ : dB (γB.dpow n x) = 0,
                  γH.dpow n (Submodule.Quotient.mk (⟨x, hd⟩ : cycles dB)) =
                    Submodule.Quotient.mk (⟨γB.dpow n x, hγ⟩ : cycles dB))
```

## Tag 09PL, a lemma

[Tag 09PL](https://stacks.math.columbia.edu/tag/09PL) in the Stacks Project.

**`DividedPowers.TateResolution.exists_dividedPowerStructure_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/FlatTensor/DividedPowerStructure.lean, line 709](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/FlatTensor/DividedPowerStructure.lean#L709).

> Divided powers and their compatibility with the differential extend under arbitrary base
> change: for a ring map `R → R'`, the differential graded algebra `R' ⊗[R] A` with grading
> `(𝒜 i).baseChange R'` and differential `d.baseChange R'` carries divided powers `γ'` compatible
> with that differential, and `γ'ₙ (1 ⊗ₜ x) = 1 ⊗ₜ γₙ x` for `x` in the positive even part.

```lean
public theorem exists_dividedPowerStructure_baseChange
    {R : Type u} {R' : Type v} {A : Type w}
    [CommRing R] [CommRing R'] [Ring A] [Algebra R R'] [Algebra R A]
    (𝒜 : ℕ → Submodule R A) [GradedAlgebra 𝒜] [IsStrictlyGradedComm 𝒜]
    (γ : DividedPowerStructure 𝒜) (d : A →ₗ[R] A) [IsCompatibleWithDifferential γ d]
    (d_sq : d.comp d = 0)
    (d_grade_zero : ∀ x : A, x ∈ 𝒜 0 → d x = 0)
    (d_mem : ∀ (n : ℕ) (x : A), x ∈ 𝒜 (n + 1) → d x ∈ 𝒜 n)
    (d_mul : ∀ (i j : ℕ) (x y : A), x ∈ 𝒜 i → y ∈ 𝒜 j →
      d (x * y) = d x * y + (-1 : R) ^ i • (x * d y)) :
    let 𝒜' : ℕ → Submodule R' (R' ⊗[R] A) := fun i ↦ (𝒜 i).baseChange R'
    let d' := LinearMap.baseChange R' d
    ∃ hcomm : IsStrictlyGradedComm 𝒜',
      letI := hcomm
      ∃ γ' : DividedPowerStructure 𝒜',
        d'.comp d' = 0 ∧
          (∀ x : R' ⊗[R] A, x ∈ 𝒜' 0 → d' x = 0) ∧
          (∀ (n : ℕ) (x : R' ⊗[R] A), x ∈ 𝒜' (n + 1) → d' x ∈ 𝒜' n) ∧
          (∀ (i j : ℕ) (x y : R' ⊗[R] A), x ∈ 𝒜' i → y ∈ 𝒜' j →
            d' (x * y) = d' x * y + (-1 : R') ^ i • (x * d' y)) ∧
          IsCompatibleWithDifferential γ' d' ∧
          ∀ (n : ℕ) (x : A), x ∈ positiveEvenPart 𝒜 →
            γ'.dpow n (1 ⊗ₜ[R] x) = 1 ⊗ₜ[R] γ.dpow n x
```

## Tag 09PM, a lemma

[Tag 09PM](https://stacks.math.columbia.edu/tag/09PM) in the Stacks Project.

**`DividedPowers.TateResolution.existsUnique_differential_mixedDegreeSetVariableExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableDifferential.lean, line 645](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableDifferential.lean#L645). The attribute's comment: “set of variables of prescribed degrees”.

> A cycle of degree `deg j - 1` for each adjoined variable `j` determines the unique
> divided-power-compatible differential on an extension by a set of variables of degrees `deg`.
>
> The extension enters through the data and the properties that the set-indexed construction of
> Tag 0F4I produces: a grading- and divided-power-preserving coefficient map `ι`, variables `T`
> with `T j` homogeneous of degree `deg j`, the presentation of every element inside a
> finite-variable stage, and the universal mapping property.  This is Tag 09PM for a whole set of
> variables of arbitrary prescribed degrees at once, which is what an algebra with variables in
> every positive degree needs; its single-variable forms are
> `existsUnique_differential_oddVariableExtension` and
> `existsUnique_differential_evenVariableAlgebra`, and its form for the variables of a single
> degree, which needs no universal property, is
> `existsUnique_differential_setVariableExtension`.

```lean
public theorem existsUnique_differential_mixedDegreeSetVariableExtension
    (𝒜 : ℕ → Submodule R A) [GradedAlgebra 𝒜] [IsStrictlyGradedComm 𝒜]
    (γ : DividedPowerStructure 𝒜) (dA : A →ₗ[R] A)
    [IsDifferentialGradedAlgebra 𝒜 dA] [IsCompatibleWithDifferential γ dA]
    (𝒞 : ℕ → Submodule R C) [GradedAlgebra 𝒞] [IsStrictlyGradedComm 𝒞]
    (δ : DividedPowerStructure 𝒞) (ι : A →ₐ[R] C) (T : J → C) (deg : J → ℕ)
    (hdeg : ∀ j : J, 0 < deg j)
    (hι_grade : ∀ (m : ℕ) (a : A), a ∈ 𝒜 m → ι a ∈ 𝒞 m)
    (hι_dpow : ∀ (n : ℕ) (a : A), a ∈ positiveEvenPart 𝒜 → δ.dpow n (ι a) = ι (γ.dpow n a))
    (hT : ∀ j : J, T j ∈ 𝒞 (deg j))
    (hgen : ∀ x : C, ∃ S : Finset J, x ∈ finiteVariableStage δ ι T S)
    (huniv : ∀ {D : Type z} [Ring D] [Algebra R D]
        (𝒟 : ℕ → Submodule R D) [GradedAlgebra 𝒟] [IsStrictlyGradedComm 𝒟]
        (ε : DividedPowerStructure 𝒟) (f : A →ₐ[R] D) (t : J → D),
        (∀ (m : ℕ) (a : A), a ∈ 𝒜 m → f a ∈ 𝒟 m) →
        (∀ (n : ℕ) (a : A), a ∈ positiveEvenPart 𝒜 → ε.dpow n (f a) = f (γ.dpow n a)) →
        (∀ j : J, t j ∈ 𝒟 (deg j)) →
        ∃! g : C →ₐ[R] D,
          (∀ a : A, g (ι a) = f a) ∧ (∀ j : J, g (T j) = t j) ∧
            (∀ (m : ℕ) (x : C), x ∈ 𝒞 m → g x ∈ 𝒟 m) ∧
            (∀ (n : ℕ) (x : C), x ∈ positiveEvenPart 𝒞 → ε.dpow n (g x) = g (δ.dpow n x)))
    (e : J → A) (he_grade : ∀ j : J, e j ∈ 𝒜 (deg j - 1))
    (he_cycle : ∀ j : J, dA (e j) = 0) :
    ∃! dC : C →ₗ[R] C,
      IsDifferentialGradedAlgebra 𝒞 dC ∧ (∀ a : A, dC (ι a) = ι (dA a)) ∧
        (∀ j : J, dC (T j) = ι (e j)) ∧ IsCompatibleWithDifferential δ dC
```

**`DividedPowers.TateResolution.existsUnique_differential_setVariableExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableDifferential.lean, line 973](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/SetVariableDifferential.lean#L973). The attribute's comment: “set of variables”.

> **The differential of a set-variable divided power extension**, the set-indexed form of
> Tag 09PM. A differential on the coefficient algebra, compatible with its divided powers,
> together with a *cycle* of degree `d - 1` prescribed as the value on each adjoined variable of
> degree `d`, determines the unique divided-power-compatible differential on the extension.
>
> This is the inductive step of Tate's construction: at a stage whose cycles in degree `n` are to
> be killed, the variables adjoined in degree `n + 1` are indexed by those cycles, and the cycle
> condition is exactly what makes the extended operator square-zero.
>
> The variant for variables of arbitrary prescribed degrees, which instead needs the universal
> property of the extension, is
> `existsUnique_differential_mixedDegreeSetVariableExtension`.

```lean
public theorem existsUnique_differential_setVariableExtension
    (hC : IsSetVariableExtension Aᵢ γ Cᵢ δ ι T d hd)
    (dA : A →ₗ[R] A) [IsDifferentialGradedAlgebra Aᵢ dA] [IsCompatibleWithDifferential γ dA]
    (ev : J → A) (hev : ∀ j : J, ev j ∈ Aᵢ (d - 1)) (hcycle : ∀ j : J, dA (ev j) = 0) :
    ∃! D : C →ₗ[R] C,
      IsDifferentialGradedAlgebra Cᵢ D ∧ (∀ a : A, D (ι a) = ι (dA a)) ∧
        (∀ j : J, D (T j) = ι (ev j)) ∧ IsCompatibleWithDifferential δ D
```

**`DividedPowers.TateResolution.existsUnique_differential_oddVariableExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/VariableDifferential/ExistsUnique.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/VariableDifferential/ExistsUnique.lean#L410). The attribute's comment: “odd variable”.

> A closed element of degree `d - 1` determines the unique divided-power-compatible
> differential after adjoining an odd variable of degree `d`.

```lean
public theorem existsUnique_differential_oddVariableExtension
    {R : Type u} {A : Type v} [CommRing R] [Ring A] [Algebra R A]
    (𝒜 : ℕ → Submodule R A) [GradedAlgebra 𝒜] [IsStrictlyGradedComm 𝒜]
    (γ : DividedPowerStructure 𝒜) (dA : A →ₗ[R] A)
    [IsDifferentialGradedAlgebra 𝒜 dA] [IsCompatibleWithDifferential γ dA]
    (d : ℕ) (hd : 0 < d) (hd_odd : Odd d)
    (f : A) (hf_grade : f ∈ 𝒜 (d - 1)) (hf_cycle : dA f = 0) :
    ∃! dExt : OddVariableExtension 𝒜 d →ₗ[R] OddVariableExtension 𝒜 d,
      (IsDifferentialGradedAlgebra (OddVariableExtension.grade 𝒜 d) dExt ∧
        (∀ x : A, dExt (OddVariableExtension.inclusion 𝒜 d x) =
          OddVariableExtension.inclusion 𝒜 d (dA x)) ∧
        dExt (OddVariableExtension.generator 𝒜 d) =
          OddVariableExtension.inclusion 𝒜 d f ∧
        IsCompatibleWithDifferential
          (oddVariableDividedPowerStructure 𝒜 γ d hd hd_odd) dExt)
```

**`DividedPowers.TateResolution.existsUnique_differential_evenVariableAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/VariableDifferential/ExistsUnique.lean, line 445](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/VariableDifferential/ExistsUnique.lean#L445). The attribute's comment: “even variable”.

> A closed element of degree `d - 1` determines the unique divided-power-compatible
> differential after adjoining an even divided-power variable of degree `d`.

```lean
public theorem existsUnique_differential_evenVariableAlgebra
    {R : Type u} {A : Type v} [CommRing R] [Ring A] [Algebra R A]
    (𝒜 : ℕ → Submodule R A) [GradedAlgebra 𝒜] [IsStrictlyGradedComm 𝒜]
    (γ : DividedPowerStructure 𝒜) (dA : A →ₗ[R] A)
    [IsDifferentialGradedAlgebra 𝒜 dA] [IsCompatibleWithDifferential γ dA]
    (d : ℕ) [Fact (Even d)] (hd : 0 < d)
    (f : A) (hf_grade : f ∈ 𝒜 (d - 1)) (hf_cycle : dA f = 0) :
    ∃! dExt : EvenVariableAlgebra A →ₗ[R] EvenVariableAlgebra A,
      (IsDifferentialGradedAlgebra (EvenVariableAlgebra.grade 𝒜 d) dExt ∧
        (∀ x : A, dExt (EvenVariableAlgebra.coeffEmbedding x) =
          EvenVariableAlgebra.coeffEmbedding (dA x)) ∧
        dExt (EvenVariableAlgebra.monomial 1 1) =
          EvenVariableAlgebra.coeffEmbedding f ∧
        IsCompatibleWithDifferential
          (evenVariableDividedPowerStructure d hd γ) dExt)
```

**`DividedPowers.TateResolution.existsUnique_gradedDerivation_oddVariableExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/VariableDifferential/ExistsUnique.lean, line 500](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/VariableDifferential/ExistsUnique.lean#L500). The attribute's comment: “odd variable, as a graded derivation”.

> An element of degree `d - 1`, with no cycle condition imposed on it, determines the unique
> divided-power-compatible graded derivation on the algebra obtained by adjoining an odd variable of
> degree `d`. The extension is square-zero precisely when the prescribed value is a cycle, which is
> `existsUnique_differential_oddVariableExtension`; this form is what the square-zero lift of
> Tag 09PS needs, since there the lifted operator is not square-zero.

```lean
public theorem existsUnique_gradedDerivation_oddVariableExtension
    {R : Type u} {A : Type v} [CommRing R] [Ring A] [Algebra R A]
    (𝒜 : ℕ → Submodule R A) [GradedAlgebra 𝒜] [IsStrictlyGradedComm 𝒜]
    (γ : DividedPowerStructure 𝒜) (dA : A →ₗ[R] A)
    [IsGradedDerivation 𝒜 dA] [IsCompatibleWithDifferential γ dA]
    (d : ℕ) (hd : 0 < d) (hd_odd : Odd d)
    (f : A) (hf_grade : f ∈ 𝒜 (d - 1)) :
    ∃! dExt : OddVariableExtension 𝒜 d →ₗ[R] OddVariableExtension 𝒜 d,
      (IsGradedDerivation (OddVariableExtension.grade 𝒜 d) dExt ∧
        (∀ x : A, dExt (OddVariableExtension.inclusion 𝒜 d x) =
          OddVariableExtension.inclusion 𝒜 d (dA x)) ∧
        dExt (OddVariableExtension.generator 𝒜 d) =
          OddVariableExtension.inclusion 𝒜 d f ∧
        IsCompatibleWithDifferential
          (oddVariableDividedPowerStructure 𝒜 γ d hd hd_odd) dExt)
```

**`DividedPowers.TateResolution.existsUnique_gradedDerivation_evenVariableAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/VariableDifferential/ExistsUnique.lean, line 531](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/VariableDifferential/ExistsUnique.lean#L531). The attribute's comment: “even variable, as a graded derivation”.

> An element of degree `d - 1`, with no cycle condition imposed on it, determines the unique
> divided-power-compatible graded derivation on the algebra obtained by adjoining an even
> divided-power variable of degree `d`. The extension is square-zero precisely when the prescribed
> value is a cycle, which is `existsUnique_differential_evenVariableAlgebra`.

```lean
public theorem existsUnique_gradedDerivation_evenVariableAlgebra
    {R : Type u} {A : Type v} [CommRing R] [Ring A] [Algebra R A]
    (𝒜 : ℕ → Submodule R A) [GradedAlgebra 𝒜] [IsStrictlyGradedComm 𝒜]
    (γ : DividedPowerStructure 𝒜) (dA : A →ₗ[R] A)
    [IsGradedDerivation 𝒜 dA] [IsCompatibleWithDifferential γ dA]
    (d : ℕ) [Fact (Even d)] (hd : 0 < d)
    (f : A) (hf_grade : f ∈ 𝒜 (d - 1)) :
    ∃! dExt : EvenVariableAlgebra A →ₗ[R] EvenVariableAlgebra A,
      (IsGradedDerivation (EvenVariableAlgebra.grade 𝒜 d) dExt ∧
        (∀ x : A, dExt (EvenVariableAlgebra.coeffEmbedding x) =
          EvenVariableAlgebra.coeffEmbedding (dA x)) ∧
        dExt (EvenVariableAlgebra.monomial 1 1) =
          EvenVariableAlgebra.coeffEmbedding f ∧
        IsCompatibleWithDifferential
          (evenVariableDividedPowerStructure d hd γ) dExt)
```

## Tag 09PN, a lemma

[Tag 09PN](https://stacks.math.columbia.edu/tag/09PN) in the Stacks Project.

**`DividedPowers.TateResolution.finiteTateResolution`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/FiniteTateResolution.lean, line 524](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/FiniteTateResolution.lean#L524). The attribute's comment: “finite generators in each degree, for a prescribed presentation”.

> **Tate's resolution with finitely many generators in each degree, for a prescribed
> presentation.** Let `φ : R[xᵢ] → S` be a surjection from a polynomial ring whose coefficient ring
> is Noetherian, and let `s₀` be a finite generating family of `ker φ`. Then `φ` extends to a divided
> power differential graded algebra over `R`, free over `R` in every degree, which is a graded
> divided power polynomial algebra over `R[xᵢ]` on **finitely many variables in each degree**, and
> whose augmentation to `S` is a quasi-isomorphism.
>
> The algebra is the colimit of the degreewise finite tower over `R[xᵢ]` with `s₀` as the family of
> degree-zero cycles to be killed. Exactness in degree zero is `s₀` generating `ker φ`; exactness in
> positive degrees is that the finite family killed at each stage spans the cycles of its degree,
> which is `DividedPowers.TateResolution.hasFiniteSpanningCycles_finiteTateStage`. The finiteness of
> the index sets is `DividedPowers.TateResolution.finite_finiteTateIndex`.

```lean
public noncomputable def finiteTateResolution (φ : MvPolynomial σ R →ₐ[R] S)
    (hφ : Function.Surjective φ) (s₀ : Finset (resolutionCoefficientRing R S σ))
    (hs₀ : Ideal.span (↑s₀ : Set (resolutionCoefficientRing R S σ)) =
      RingHom.ker (resolutionPresentation φ))
    [IsNoetherianRing (resolutionCoefficientRing R S σ)] :
    Resolution R S σ φ
```

**`DividedPowers.TateResolution.finite_finiteTateResolution_polynomialIndices`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/FiniteTateResolution.lean, line 582](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/FiniteTateResolution.lean#L582). The attribute's comment: “finite generators in each degree, for a prescribed presentation”.

> The degreewise finite Tate resolution really is degreewise finite: it has finitely many
> variables in each degree, which is the finiteness assertion of Tag 09PN. The variables of degree
> `i + 1` are the family chosen at the stage `i` of the tower, which is finite by construction.

```lean
public theorem finite_finiteTateResolution_polynomialIndices (φ : MvPolynomial σ R →ₐ[R] S)
    (hφ : Function.Surjective φ) (s₀ : Finset (resolutionCoefficientRing R S σ))
    (hs₀ : Ideal.span (↑s₀ : Set (resolutionCoefficientRing R S σ)) =
      RingHom.ker (resolutionPresentation φ))
    [IsNoetherianRing (resolutionCoefficientRing R S σ)] (i : ℕ) :
    Finite ((finiteTateResolution φ hφ s₀ hs₀).polynomialIndices i)
```

**`DividedPowers.TateResolution.exists_finite_tateResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/FiniteTateResolution.lean, line 605](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/FiniteTateResolution.lean#L605). The attribute's comment: “finite generators in each degree”.

> **The finiteness half of Tag 09PN.** A Noetherian commutative ring `R` and an `R`-algebra `S`
> of finite type admit a surjection `φ : R[x₁, …, x_k] → S` from a polynomial ring in finitely many
> variables together with a Tate resolution of `S` along `φ` having **finitely many generators in
> each degree**.
>
> The presentation is a finite one, which exists because `S` is of finite type; its coefficient ring
> `R[x₁, …, x_k]` is Noetherian because `R` is, by `MvPolynomial.isNoetherianRing`, so its kernel is
> generated by a finite family, and
> `DividedPowers.TateResolution.finiteTateResolution` resolves that data.

```lean
public theorem exists_finite_tateResolution (R S : Type u) [CommRing R] [CommRing S]
    [Algebra R S] [IsNoetherianRing R] [Algebra.FiniteType R S] :
    ∃ (k : ℕ) (φ : MvPolynomial (Fin k) R →ₐ[R] S) (A : Resolution R S (Fin k) φ),
      Function.Surjective φ ∧ ∀ i : ℕ, Finite (A.polynomialIndices i)
```

**`DividedPowers.TateResolution.exists_boundary_of_gradeZero_combination`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/FiniteTateTower.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/FiniteTateTower.lean#L131). The attribute's comment: “a spanning family kills every cycle of its degree, degree-zero coefficients”.

> **A combination with coefficients of degree zero of cycles killed by variables is a
> boundary.** If the variable `T j` of degree `n + 1` has `v j` for boundary, then the boundary of
> the corresponding combination of the `T j` is the combination of the `v j`, by linearity of the
> differential over degree-zero coefficients, and that combination is homogeneous of degree `n + 1`.
>
> So a family of variables whose prescribed cycles *span* the cycles of a degree kills all of them.
> This is what makes the degreewise finite tower acyclic; the existence half of Tag 09PN instead
> prescribes every cycle individually, which is what costs it degreewise finiteness.

```lean
public theorem exists_boundary_of_gradeZero_combination {J : Type y} (v T : J → A) (n : ℕ)
    (hT : ∀ j : J, T j ∈ Aᵢ (n + 1)) (hdT : ∀ j : J, d (T j) = v j)
    (s : Finset J) (c : J → A) (hc : ∀ j : J, c j ∈ Aᵢ 0) :
    ∃ b : A, b ∈ Aᵢ (n + 1) ∧ d b = ∑ j ∈ s, c j * v j
```

**`DividedPowers.TateResolution.hasFiniteSpanningCycles_finiteTateStage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/FiniteTateTower.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/FiniteTateTower.lean#L402). The attribute's comment: “finitely many variables suffice at each step over a Noetherian base”.

> **Over a Noetherian coefficient ring every degree of every stage of the degreewise finite
> tower has a finite spanning family of cycles**, so the empty fallback of
> `DividedPowers.TateResolution.chosenCycleFinset` is never taken and the tower really does kill
> every cycle.
>
> This is where the two ingredients meet. The stage `N` is a graded divided power polynomial
> algebra over `P` by `DividedPowers.TateResolution.chainStagePresentation`, with finitely many
> variables in each degree because the index sets of the tower are finite unconditionally; so each of
> its homogeneous pieces is a finitely generated `P`-module by
> `DividedPowers.TateResolution.GradedDividedPowerPolynomial.fg_coefficientGrade`, and over the
> Noetherian ring `P` the submodule of cycles is finitely generated too, which is
> `DividedPowers.TateResolution.exists_finite_spanning_cycles`. Its coefficients lie in `P`, and the
> coefficient morphism carries `P` into degree zero, which is the spelling
> `DividedPowers.TateResolution.HasFiniteSpanningCycles` asks for.

```lean
public theorem hasFiniteSpanningCycles_finiteTateStage [IsNoetherianRing P] (N m : ℕ) :
    HasFiniteSpanningCycles
      (finiteTateStage (finiteTateBase.{u, v} (R := R) P s₀) N).datum m
```

**`DividedPowers.TateResolution.GradedDividedPowerPolynomial.free_grade`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/GradedBasis.lean, line 1080](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/GradedBasis.lean#L1080). The attribute's comment: “freeness of the homogeneous pieces”.

> Each homogeneous piece is free over the ground ring as soon as the coefficient algebra is.
> This is the `free` field of a Tate resolution, Tag 09PN.

```lean
public theorem free_grade (G : GradedDividedPowerPolynomial Aᵢ γ ι) [Module.Free R P] (n : ℕ) :
    Module.Free R ↥(Aᵢ n)
```

**`DividedPowers.TateResolution.GradedDividedPowerPolynomial.finite_grade`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/GradedBasis.lean, line 1089](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/GradedBasis.lean#L1089). The attribute's comment: “finiteness of the homogeneous pieces”.

> Each homogeneous piece is module finite over the ground ring as soon as the coefficient
> algebra is and there are only finitely many variables in each degree: there are then only
> finitely many monomials of each degree.

```lean
public theorem finite_grade (G : GradedDividedPowerPolynomial Aᵢ γ ι) [Module.Finite R P]
    [∀ i : ℕ, Finite (G.indices i)] (n : ℕ) : Module.Finite R ↥(Aᵢ n)
```

**`DividedPowers.TateResolution.existsUnique_gradedDividedPowerPolynomial_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/GradedPolynomialMap.lean, line 638](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/GradedPolynomialMap.lean#L638). The attribute's comment: “mapping property”.

> The mapping property of an iterated graded divided-power polynomial algebra.
> The target may live in a universe independent of the source and its variables.

```lean
public theorem existsUnique_gradedDividedPowerPolynomial_map
    {R : Type u} {P : Type v} {A : Type w} {D : Type z}
    [CommRing R] [Ring P] [Algebra R P] [Ring A] [Algebra R A]
    [Ring D] [Algebra R D]
    (Aᵢ : ℕ → Submodule R A) [GradedAlgebra Aᵢ]
    [IsStrictlyGradedComm Aᵢ] (γ : DividedPowerStructure Aᵢ)
    (ι : P →ₐ[R] A) (h : GradedDividedPowerPolynomial Aᵢ γ ι)
    (Dᵢ : ℕ → Submodule R D) [GradedAlgebra Dᵢ]
    [IsStrictlyGradedComm Dᵢ] (δ : DividedPowerStructure Dᵢ)
    (f : P →ₐ[R] D) (hf : ∀ p : P, f p ∈ Dᵢ 0)
    (t : (Σ n : ℕ, h.indices n) → D)
    (ht : ∀ j, t j ∈ Dᵢ (j.1 + 1)) :
    ∃! g : A →ₐ[R] D,
      (∀ p : P, g (ι p) = f p) ∧
      (∀ j : Σ n : ℕ, h.indices n, g (h.generator j) = t j) ∧
      (∀ (n : ℕ) (a : A), a ∈ Aᵢ n → g a ∈ Dᵢ n) ∧
      (∀ (n : ℕ) (a : A), a ∈ positiveEvenPart Aᵢ →
        g (γ.dpow n a) = δ.dpow n (g a))
```

**`DividedPowers.TateResolution.existsUnique_algEquiv_gradedDividedPowerPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/GradedPolynomialMap.lean, line 759](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/GradedPolynomialMap.lean#L759). The attribute's comment: “uniqueness of the presentation”.

> Two graded divided power polynomial algebras over the same coefficient algebra, whose index
> data are identified degreewise, are uniquely isomorphic over the coefficients and the variables,
> and the isomorphism preserves the grading and the divided powers in both directions. This is the
> form in which one recognises a graded divided power polynomial algebra as a base change of
> another.

```lean
public theorem existsUnique_algEquiv_gradedDividedPowerPolynomial
    {R : Type u} {P : Type v} {A : Type w} {A' : Type z}
    [CommRing R] [Ring P] [Algebra R P] [Ring A] [Algebra R A] [Ring A'] [Algebra R A']
    (Aᵢ : ℕ → Submodule R A) [GradedAlgebra Aᵢ] [IsStrictlyGradedComm Aᵢ]
    (γ : DividedPowerStructure Aᵢ) (ι : P →ₐ[R] A)
    (h : GradedDividedPowerPolynomial Aᵢ γ ι)
    (Aᵢ' : ℕ → Submodule R A') [GradedAlgebra Aᵢ'] [IsStrictlyGradedComm Aᵢ']
    (γ' : DividedPowerStructure Aᵢ') (ι' : P →ₐ[R] A')
    (h' : GradedDividedPowerPolynomial Aᵢ' γ' ι')
    (σ : (Σ n : ℕ, h.indices n) ≃ (Σ n : ℕ, h'.indices n))
    (hσ : ∀ j, (σ j).1 = j.1) :
    ∃! e : A ≃ₐ[R] A',
      (∀ p : P, e (ι p) = ι' p) ∧
      (∀ j, e (h.generator j) = h'.generator (σ j)) ∧
      (∀ (n : ℕ) (a : A), a ∈ Aᵢ n → e a ∈ Aᵢ' n) ∧
      (∀ (n : ℕ) (a : A), a ∈ positiveEvenPart Aᵢ → e (γ.dpow n a) = γ'.dpow n (e a)) ∧
      (∀ (n : ℕ) (a : A'), a ∈ Aᵢ' n → e.symm a ∈ Aᵢ n) ∧
      (∀ (n : ℕ) (a : A'), a ∈ positiveEvenPart Aᵢ' →
        e.symm (γ'.dpow n a) = γ.dpow n (e.symm a))
```

**`DividedPowers.TateResolution.exists_gradedDividedPowerPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/MixedDegreeConstruction.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/MixedDegreeConstruction.lean#L79). The attribute's comment: “graded divided power polynomial algebra over a prescribed degree-zero algebra”.

> A graded divided-power polynomial algebra exists over any prescribed commutative degree-zero
> algebra `P`, with one homogeneous variable of degree `n + 1` for each element of `indices n`.
> Its mapping property is `existsUnique_restrictedStageGradedDividedPowerPolynomial_map`.

```lean
public theorem exists_gradedDividedPowerPolynomial {R : Type u} [CommRing R] (P : Type v)
    [CommRing P] [Algebra R P] (indices : ℕ → Type (max u v w)) :
    ∃ (A : Type (max u v w)) (ringA : Ring A),
      letI : Ring A := ringA
      ∃ algebraA : Algebra R A,
        letI : Algebra R A := algebraA
        ∃ (Aᵢ : ℕ → Submodule R A) (gradedA : GradedAlgebra Aᵢ),
          letI : GradedAlgebra Aᵢ := gradedA
          ∃ strictA : IsStrictlyGradedComm Aᵢ,
            letI : IsStrictlyGradedComm Aᵢ := strictA
            ∃ (γ : DividedPowerStructure Aᵢ) (ι : P →ₐ[R] A)
              (h : RestrictedStageGradedDividedPowerPolynomial Aᵢ γ ι), h.indices = indices
```

**`DividedPowers.TateResolution.existsUnique_restrictedStageGradedDividedPowerPolynomial_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/MixedDegreePolynomial.lean, line 596](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/MixedDegreePolynomial.lean#L596). The attribute's comment: “mapping property of a graded divided-power polynomial algebra”.

> The mapping property of an iterated graded divided-power polynomial algebra: prescribing
> the values on the coefficient algebra and on the variables, subject to the degree conditions,
> determines a unique map of graded algebras with divided powers. The target may live in a
> universe independent of the source and its variables.
>
> The hypothesis is `RestrictedStageGradedDividedPowerPolynomial`, which also requires each
> stage's `R`-algebra structure to be restricted from the ambient algebra.
> `existsUnique_gradedDividedPowerPolynomial_map` of
> `StacksFrontier.RingTheory.DividedPowers.TateResolution.GradedPolynomialMap` has the identical
> conclusion under the hypothesis without that clause, so it is the stronger of the two; this one is
> the form that `exists_gradedDividedPowerPolynomial` applies, since Tag 0F4I's construction
> delivers the clause.

```lean
public theorem existsUnique_restrictedStageGradedDividedPowerPolynomial_map
    (γ : DividedPowerStructure Aᵢ) (ι : P →ₐ[R] A)
    (h : RestrictedStageGradedDividedPowerPolynomial Aᵢ γ ι)
    (δ : DividedPowerStructure Dᵢ) (f : P →ₐ[R] D) (hf : ∀ p : P, f p ∈ Dᵢ 0)
    (t : (Σ n : ℕ, h.indices n) → D) (ht : ∀ j, t j ∈ Dᵢ (j.1 + 1)) :
    ∃! g : A →ₐ[R] D,
      (∀ p : P, g (ι p) = f p) ∧
      (∀ j : Σ n : ℕ, h.indices n, g (h.generator j) = t j) ∧
      (∀ (n : ℕ) (a : A), a ∈ Aᵢ n → g a ∈ Dᵢ n) ∧
      (∀ (n : ℕ) (a : A), a ∈ positiveEvenPart Aᵢ →
        g (γ.dpow n a) = δ.dpow n (g a))
```

**`DividedPowers.TateResolution.exists_boundary_of_coefficient_combination`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/NoetherianCycles.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/NoetherianCycles.lean#L223). The attribute's comment: “a spanning family of variables kills every cycle of its degree”.

> **A combination of the cycles killed by the variables of degree `n + 1` is a boundary.** The
> boundary of the corresponding combination of the variables is it, by linearity of the differential
> over the coefficients, and that combination is homogeneous of degree `n + 1` because the
> coefficients are homogeneous of degree zero.
>
> So a family of variables whose prescribed cycles *span* the cycles of a degree kills all of them.
> This is what makes a degreewise finite Tate tower acyclic; the existence half of Tag 09PN instead
> prescribes every cycle individually, which costs it degreewise finiteness.

```lean
public theorem exists_boundary_of_coefficient_combination
    (h0 : ∀ p : P, algebraMap P A p ∈ Aᵢ 0) {J : Type*} (v T : J → A) (n : ℕ)
    (hT : ∀ j : J, T j ∈ Aᵢ (n + 1)) (hdT : ∀ j : J, d (T j) = v j)
    (s : Finset J) (c : J → P) :
    ∃ b : A, b ∈ Aᵢ (n + 1) ∧ d b = ∑ j ∈ s, c j • v j
```

**`DividedPowers.TateResolution.GradedDividedPowerPolynomial.fg_coefficientGrade`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/NoetherianCycles.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/NoetherianCycles.lean#L272). The attribute's comment: “finite generation of the homogeneous pieces over the coefficients”.

> **Each homogeneous piece is finitely generated over the coefficient algebra** as soon as the
> variables are finite in each degree: there are then only finitely many divided power monomials of
> each degree, and they span that degree over the coefficients.
>
> This is the coefficient-algebra analogue of
> `DividedPowers.TateResolution.GradedDividedPowerPolynomial.finite_grade`, and it is the form the
> finiteness half of Tag 09PN needs: there the coefficient algebra is a polynomial ring over the
> ground ring, hence not module finite over it, so `finite_grade` says nothing.

```lean
public theorem fg_coefficientGrade (G : GradedDividedPowerPolynomial Aᵢ γ ι)
    [∀ i : ℕ, Finite (G.indices i)] (h0 : ∀ p : P, algebraMap P A p ∈ Aᵢ 0)
    (hι : ∀ p : P, algebraMap P A p = ι p) (n : ℕ) :
    (coefficientGrade Aᵢ h0 n).FG
```

**`DividedPowers.TateResolution.exists_finite_spanning_cycles`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/NoetherianCycles.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/NoetherianCycles.lean#L315). The attribute's comment: “a finite generating family of the cycles of a degree”.

> **A finite family of degree-`n` cycles that every degree-`n` cycle is a combination of.**
>
> This is what lets the variables of degree `n + 1` of Tate's tower be finite in number: the
> existence half of Tag 09PN adjoins one variable for *every* cycle of degree `n`, which makes
> acyclicity free of a homology computation but makes the resolution infinite in each degree. Over a
> Noetherian coefficient algebra a finite family suffices, by
> `DividedPowers.TateResolution.exists_boundary_of_coefficient_combination`.

```lean
public theorem exists_finite_spanning_cycles (G : GradedDividedPowerPolynomial Aᵢ γ ι)
    [∀ i : ℕ, Finite (G.indices i)] [IsNoetherianRing P]
    (h0 : ∀ p : P, algebraMap P A p ∈ Aᵢ 0) (hι : ∀ p : P, algebraMap P A p = ι p) (n : ℕ) :
    ∃ s : Finset A, (∀ y ∈ s, y ∈ Aᵢ n ∧ d y = 0) ∧
      ∀ x : A, x ∈ Aᵢ n → d x = 0 → ∃ c : A → P, ∑ y ∈ s, c y • y = x
```

**`DividedPowers.TateResolution.chainStagePresentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/StagePresentation.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/StagePresentation.lean#L237). The attribute's comment: “each finite stage is a graded divided power polynomial algebra”.

> **The stage `N` of a chain of set-variable divided power extensions is a graded divided power
> polynomial algebra over the base of the chain**, on the variables of degrees `1, …, N`.
>
> This is `DividedPowers.TateResolution.gradedDividedPowerPolynomialOfMappingProperty` fed the two
> statements above. Its use is finiteness: the degree-`m` piece of the stage is spanned over the
> base by the divided power monomials of degree `m` in those variables, of which there are finitely
> many when the chain adjoins finitely many variables at each step.

```lean
public noncomputable def chainStagePresentation
    (hbase0 : ∀ p : (B 0).carrier, p ∈ (B 0).grade 0)
    (hbase : ∀ (E : GradedDPAlgebra.{u, v} R) (f : (B 0).carrier →ₐ[R] E.carrier),
      (∀ p : (B 0).carrier, f p ∈ E.grade 0) →
        ∃ F : GradedDPHom (B 0) E, ∀ p : (B 0).carrier, F.hom p = f p)
    (N : ℕ) :
    GradedDividedPowerPolynomial (B N).grade (B N).gamma (chainStageCoefficient B step N)
```

**`DividedPowers.TateResolution.tateResolution`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/TateColimitResolution.lean, line 499](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/TateColimitResolution.lean#L499). The attribute's comment: “resolution of any polynomial presentation”.

> **Tate's resolution of a prescribed polynomial presentation.** Every surjection
> `φ : R[xᵢ] → S` from a polynomial ring extends to a divided power differential graded algebra
> over `R`, free over `R` in every degree, whose degree-zero algebra is `R[xᵢ]` along `φ`, which is
> a graded divided power polynomial algebra over `R[xᵢ]`, and whose augmentation to `S` is a
> quasi-isomorphism: it kills the positive-degree part and every boundary, it is surjective, its
> degree-zero kernel is exactly the boundaries from degree one, and the complex is exact in every
> positive degree.
>
> The algebra is the colimit of Tate's tower over `R[xᵢ]` with `ker φ` as the ideal to be killed in
> degree one. Acyclicity is not a homology computation: the variables adjoined in degree `n + 1`
> are indexed by **all** cycles of degree `n`, with the boundary of a variable being the cycle
> indexing it, so a cycle of degree `n` is the boundary of its own variable by construction.

```lean
public noncomputable def tateResolution (φ : MvPolynomial σ R →ₐ[R] S)
    (hφ : Function.Surjective φ) : Resolution R S σ φ
```

## Tag 0BZ9, a lemma

[Tag 0BZ9](https://stacks.math.columbia.edu/tag/0BZ9) in the Stacks Project.

**`DividedPowers.TateResolution.exists_finite_tateResolution_of_pseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/PseudoCoherentTateResolution.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/PseudoCoherentTateResolution.lean#L78).

> **A pseudo-coherent ring map admits a Tate resolution with finitely many generators in each
> degree.** If `R → S` is pseudo-coherent then there are a surjection `φ : R[x₁, …, x_k] → S` from
> a polynomial ring in finitely many variables and a Tate resolution of `S` along `φ` whose
> variables are finite in number in every degree.
>
> This is the conclusion of Tag 09PN with its hypotheses — `R` Noetherian and `R → S` of finite
> type — replaced by pseudo-coherence of `R → S`.

```lean
public theorem exists_finite_tateResolution_of_pseudoCoherent
    (R S : Type u) [CommRing R] [CommRing S] [Algebra R S]
    [h : Algebra.PseudoCoherent R S] :
    ∃ (k : ℕ) (φ : MvPolynomial (Fin k) R →ₐ[R] S) (A : Resolution R S (Fin k) φ),
      Function.Surjective φ ∧ ∀ i : ℕ, Finite (A.polynomialIndices i)
```

## Tag 09PP, a lemma

[Tag 09PP](https://stacks.math.columbia.edu/tag/09PP) in the Stacks Project.

**`DividedPowers.TateResolution.exists_dividedPowerDGAMap_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/DividedPowerDGALift.lean, line 842](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/DividedPowerDGALift.lean#L842).

> A map from a graded divided-power polynomial DGA to a positively acyclic
> divided-power DGA lifting a prescribed map on zeroth homology.

```lean
public theorem exists_dividedPowerDGAMap_lift
    {R : Type u} {A : Type v} {B : Type w} {σ : Type z}
    [CommRing R] [Ring A] [Ring B] [Algebra R A] [Algebra R B]
    (𝒜 : ℕ → Submodule R A) (ℬ : ℕ → Submodule R B)
    [GradedAlgebra 𝒜] [GradedAlgebra ℬ]
    [IsStrictlyGradedComm 𝒜] [IsStrictlyGradedComm ℬ]
    (γA : DividedPowerStructure 𝒜) (γB : DividedPowerStructure ℬ)
    (dA : A →ₗ[R] A) (dB : B →ₗ[R] B)
    [IsDifferentialGradedAlgebra 𝒜 dA]
    [IsDifferentialGradedAlgebra ℬ dB]
    [IsCompatibleWithDifferential γA dA]
    [IsCompatibleWithDifferential γB dB]
    (ι : MvPolynomial σ R →ₐ[R] A)
    (hA : GradedDividedPowerPolynomial 𝒜 γA ι)
    (hB : ∀ (n : ℕ) (b : B), 0 < n → b ∈ ℬ n → dB b = 0 →
      ∃ c : B, c ∈ ℬ (n + 1) ∧ dB c = b)
    (φ₀ : zerothHomology 𝒜 dA →ₐ[R] zerothHomology ℬ dB) :
    ∃ φ : A →ₐ[R] B,
      (∀ (n : ℕ) (a : A), a ∈ 𝒜 n → φ a ∈ ℬ n) ∧
      (∀ a : A, φ (dA a) = dB (φ a)) ∧
      (∀ (n : ℕ) (a : A), a ∈ positiveEvenPart 𝒜 →
        φ (γA.dpow n a) = γB.dpow n (φ a)) ∧
      (∀ a : A,
        φ₀ ((zerothHomologyCongruence 𝒜 dA).mk' a) =
          (zerothHomologyCongruence ℬ dB).mk' (φ a))
```

## Tag 09PQ, a lemma

[Tag 09PQ](https://stacks.math.columbia.edu/tag/09PQ) in the Stacks Project.

**`DividedPowers.TateResolution.exists_dividedPowerStructure_torDirectSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/TorDividedPowerAlgebra.lean, line 1056](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/TorDividedPowerAlgebra.lean#L1056).

> **Divided powers on `Tor_*^R(S, T)`.** For a commutative ring `R` and commutative
> `R`-algebras `S` and `T`, the direct sum `⨁ n, Tor_n^R(S, T)` carries a ring structure, an
> `R`-algebra structure, a grading whose degree-`n` piece is the range of the `n`-th inclusion of
> the direct sum, a graded algebra structure for that grading, strict graded commutativity, and a
> divided power structure — with the addition and the scalar multiplication being the direct sum's
> own.
>
> The structure is the one transported along
> `DividedPowers.TateResolution.torDirectSumEquivHomology` from the induced structure on the
> homology of `T ⊗[R] A`, for `A` the Tate resolution of `S` along the tautological presentation:
> the class map `κ` of that identification, which sends a cycle of `T ⊗[R] A` to the element of the
> direct sum corresponding to its homology class, is unital and multiplicative, takes a cycle of
> degree `n` into the degree-`n` piece, and takes the divided powers of `T ⊗[R] A` to those of the
> direct sum. Those divided powers are in turn the base change of the divided powers of the Tate
> resolution.

```lean
public theorem exists_dividedPowerStructure_torDirectSum
    (R S T : Type u) [CommRing R] [CommRing S] [CommRing T] [Algebra R S] [Algebra R T] :
    ∃ Res : Resolution R S S (tautologicalPresentation R S),
      Res = tateResolution (tautologicalPresentation R S)
          (surjective_tautologicalPresentation R S) ∧
      (let ℬ : ℕ → Submodule R (T ⊗[R] Res.A) :=
         restrictGrade R fun i => (Res.grade i).baseChange T
       let dB : T ⊗[R] Res.A →ₗ[R] T ⊗[R] Res.A :=
         (LinearMap.baseChange T Res.differential).restrictScalars R
       ∃ hStrict : IsStrictlyGradedComm ℬ,
         letI := hStrict
         ∃ γB : DividedPowerStructure ℬ,
           IsCompatibleWithDifferential γB dB ∧
           (∀ (n : ℕ) (x : Res.A), x ∈ positiveEvenPart Res.grade →
             γB.dpow n (1 ⊗ₜ[R] x) = 1 ⊗ₜ[R] Res.gamma.dpow n x) ∧
           (let κ : cycles dB →ₗ[R] DirectSum ℕ fun n => torGraded R S T n :=
              directSumClass (torDirectSumEquivHomology Res T
                (surjective_tautologicalPresentation R S))
            ∃ hRing : Ring (DirectSum ℕ fun n => torGraded R S T n),
              ∃ hAlgebra : @Algebra R (DirectSum ℕ fun n => torGraded R S T n) _
                  hRing.toSemiring,
                hRing.toAddCommGroup =
                  (inferInstance : AddCommGroup (DirectSum ℕ fun n => torGraded R S T n)) ∧
                @Algebra.toSMul R (DirectSum ℕ fun n => torGraded R S T n) _
                    hRing.toSemiring hAlgebra =
                  (inferInstance : SMul R (DirectSum ℕ fun n => torGraded R S T n)) ∧
                (letI := hRing
                 letI := hAlgebra
                 letI : AddCommMonoid (DirectSum ℕ fun n => torGraded R S T n) :=
                   hRing.toAddCommMonoid
                 letI : Module R (DirectSum ℕ fun n => torGraded R S T n) := Algebra.toModule
                 ∃ 𝒟 : ℕ → Submodule R (DirectSum ℕ fun n => torGraded R S T n),
                   (∀ n, (𝒟 n : Set (DirectSum ℕ fun m => torGraded R S T m)) =
                     Set.range (DirectSum.lof R ℕ (fun m => torGraded R S T m) n)) ∧
                   ∃ hGraded : GradedAlgebra 𝒟,
                     letI := hGraded
                     ∃ hStrictD : IsStrictlyGradedComm 𝒟,
                       letI := hStrictD
                       ∃ γD : @DividedPowerStructure R
                           (DirectSum ℕ fun n => torGraded R S T n) _ hRing hAlgebra 𝒟
                           hGraded hStrictD,
                         (∀ (n : ℕ) (x : T ⊗[R] Res.A) (h : dB x = 0), x ∈ ℬ n →
                           κ ⟨x, h⟩ ∈ 𝒟 n) ∧
                         (∃ h1 : dB (1 : T ⊗[R] Res.A) = 0, κ ⟨1, h1⟩ = 1) ∧
                         (∀ {x y : T ⊗[R] Res.A} (hx : dB x = 0) (hy : dB y = 0),
                           ∃ hxy : dB (x * y) = 0,
                             κ ⟨x * y, hxy⟩ = κ ⟨x, hx⟩ * κ ⟨y, hy⟩) ∧
                         (∀ {n : ℕ} {x : T ⊗[R] Res.A}, x ∈ positiveEvenPart ℬ →
                           ∀ hd : dB x = 0,
                             ∃ hγ : dB (γB.dpow n x) = 0,
                               γD.dpow n (κ ⟨x, hd⟩) = κ ⟨γB.dpow n x, hγ⟩))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 23.6, Tag 09PF](https://stacks.math.columbia.edu/tag/09PF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
