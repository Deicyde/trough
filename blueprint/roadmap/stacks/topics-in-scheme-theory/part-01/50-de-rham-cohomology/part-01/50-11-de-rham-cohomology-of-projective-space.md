---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.ProjEulerSequence.exists_shortExact_eulerSequence, Stacks.AlgebraicGeometry.ProjectiveSpaceHodge.isZero_hodgeCohomology, Stacks.AlgebraicGeometry.ProjectiveSpaceHodge.nonempty_hodgeCohomology_diag_iso, Stacks.AlgebraicGeometry.ProjectiveSpaceHodge.free_hodgeCohomology_diag, Stacks.AlgebraicGeometry.ProjectiveSpaceHodge.isZero_twistedHodgeCohomology, Stacks.AlgebraicGeometry.ProjectiveSpaceHodge.exists_basis_chernPow, Stacks.AlgebraicGeometry.ProjectiveSpaceHodge.isZero_hodgeCohomology_of_ne_or_gt, Stacks.AlgebraicGeometry.ProjectiveSpaceHodge.isZero_projectiveHodgeCohomology
statement: formalized
proof: formalized
---

# 50.11 de Rham cohomology of projective space

Section 50.11 of the Stacks Project, [Tag 0FMG](https://stacks.math.columbia.edu/tag/0FMG). 4 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FMH, a lemma

[Tag 0FMH](https://stacks.math.columbia.edu/tag/0FMH) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjEulerSequence.exists_shortExact_eulerSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjEulerSequence/Exactness.lean, line 598](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjEulerSequence/Exactness.lean#L598). References: SGA 6 VIII (5.2), “special case”; SGA 7 XVII (5.1), “more general”.

> **There is a short exact sequence `0 ⟶ Ω ⟶ 𝒪(-1)^{⊕ (n+1)} ⟶ 𝒪 ⟶ 0`** on projective
> `n`-space over a commutative ring, with `Ω` the sheaf of differentials relative to the base.

```lean
theorem exists_shortExact_eulerSequence :
    ∃ (a : projDifferentials R n ⟶ twistMinusOneSum R n)
      (b : twistMinusOneSum R n ⟶ SheafOfModules.unit (projRingSheaf (polyGrading R n)))
      (h : a ≫ b = 0), (CategoryTheory.ShortComplex.mk a b h).ShortExact
```

## Tag 0FUK, a lemma

[Tag 0FUK](https://stacks.math.columbia.edu/tag/0FUK) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjectiveSpaceHodge.isZero_hodgeCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceHodgeCohomology.lean, line 681](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceHodgeCohomology.lean#L681). The attribute's comment: “clause (1)”.

> **Clause (1) of [Stacks, Tag 0FUK].** `H^q(ℙⁿ_A, Ωᵖ) = 0` unless `0 ≤ p = q ≤ n`.

```lean
theorem isZero_hodgeCohomology (p q : ℕ) (hpq : ¬(p = q ∧ p ≤ m + 1)) :
    IsZero (hodgeCohomology A m p q)
```

**`Stacks.AlgebraicGeometry.ProjectiveSpaceHodge.nonempty_hodgeCohomology_diag_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceHodgeCohomology.lean, line 693](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceHodgeCohomology.lean#L693). The attribute's comment: “clause (2), as an isomorphism with `A`”.

> **Clause (2) of [Stacks, Tag 0FUK].** For `0 ≤ p ≤ n` the `A`-module `H^p(ℙⁿ_A, Ωᵖ)` is
> isomorphic to `A`; its generator is, in the source, the `p`-fold boundary of
> `1 ∈ H⁰(ℙⁿ_A, 𝒪)`.

```lean
theorem nonempty_hodgeCohomology_diag_iso (p : ℕ) (hp : p ≤ m + 1) :
    Nonempty (hodgeCohomology A m p p ≅ ModuleCat.of A A)
```

**`Stacks.AlgebraicGeometry.ProjectiveSpaceHodge.free_hodgeCohomology_diag`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceHodgeCohomology.lean, line 701](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceHodgeCohomology.lean#L701). The attribute's comment: “clause (2), freeness”.

> **Clause (2) of [Stacks, Tag 0FUK], as freeness.** For `0 ≤ p ≤ n` the `A`-module
> `H^p(ℙⁿ_A, Ωᵖ)` is free, being isomorphic to `A`.

```lean
theorem free_hodgeCohomology_diag (p : ℕ) (hp : p ≤ m + 1) :
    Module.Free A ↥(hodgeCohomology A m p p)
```

**`Stacks.AlgebraicGeometry.ProjectiveSpaceHodge.isZero_twistedHodgeCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceHodgeCohomology.lean, line 748](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceHodgeCohomology.lean#L748). The attribute's comment: “clause (3)”.

> **Clause (3) of [Stacks, Tag 0FUK].** For `q > 0`, `k > 0` and arbitrary `p` we have
> `H^q(ℙⁿ_A, Ωᵖ(k)) = 0`.

```lean
theorem isZero_twistedHodgeCohomology (p : ℕ) {k : ℤ} (hk : 0 < k) {q : ℕ} (hq : 0 < q) :
    IsZero (twistedHodgeCohomology A m p k q)
```

## Tag 0FMI, a lemma

[Tag 0FMI](https://stacks.math.columbia.edu/tag/0FMI) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjectiveSpaceHodge.exists_basis_chernPow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceHodgeChernPowers.lean, line 512](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceHodgeChernPowers.lean#L512). The attribute's comment: “for 0 ≤ p ≤ n the A-module H^p(ℙⁿ\_A, Ω^p) is free of rank one with basis element c₁^\{Hodge}(𝒪(1))^p, the p-th cup power of the Hodge first Chern class of 𝒪(1)”.

> **[Stacks, Tag 0FMI], the basis.** For `0 ≤ p ≤ n` the `A`-module `Hᵖ(ℙⁿ_A, Ωᵖ)` is free of
> rank one with basis element `c₁^{Hodge}(𝒪(1))ᵖ`, the `p`-th cup power of the Hodge first Chern
> class of `𝒪(1)` (`hodgeChernPow`).
>
> The proof is the source's. In degree zero `H⁰(ℙⁿ_A, 𝒪) = A` carries the unit `1` as a basis. The
> boundary of `1` along the Euler sequence `0 ⟶ Ω ⟶ 𝒪(-1)^{⊕ (n+1)} ⟶ 𝒪 ⟶ 0` is
> `c₁^{Hodge}(𝒪(1))`, computed on Čech cocycles: both are the class of `d log(T_{i₁}/T_{i₀})` on the
> standard covering (`boundary_euler_one`). By [Stacks, Tag 07MC] applied to the filtration sequence
> `0 ⟶ Ω^{p+1} ⟶ ⋀^{p+1}(𝒪(-1)^{⊕ (n+1)}) ⟶ Ωᵖ ⟶ 0` and the Euler sequence, the boundary of the
> filtration sequence is, up to sign, the cup product with `c₁^{Hodge}(𝒪(1))`
> (`boundary_wedgeSC`); since the middle term is acyclic it is an isomorphism
> `Hᵖ(ℙⁿ_A, Ωᵖ) ≅ H^{p+1}(ℙⁿ_A, Ω^{p+1})` carrying `c₁^{Hodge}(𝒪(1))ᵖ` to
> `±c₁^{Hodge}(𝒪(1))^{p+1}`.

```lean
theorem exists_basis_chernPow (p : ℕ) (hp : p ≤ m + 1) :
    ∃ b : Module.Basis (Fin 1) A ↥(hodgeCohomology A m p p), b 0 = hodgeChernPow A m p
```

**`Stacks.AlgebraicGeometry.ProjectiveSpaceHodge.isZero_hodgeCohomology_of_ne_or_gt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceHodgeCohomology.lean, line 844](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceHodgeCohomology.lean#L844). The attribute's comment: “H^q(ℙⁿ\_A, Ω^p) = 0 unless 0 ≤ p = q ≤ n”.

> **[Stacks, Tag 0FMI], the vanishing.** `H^q(ℙⁿ_A, Ωᵖ) = 0` unless `0 ≤ p = q ≤ n`. The
> source quotes this from [Stacks, Tag 0FUK], and so does the proof. The basis assertion of
> [Stacks, Tag 0FMI] is `Stacks.AlgebraicGeometry.ProjectiveSpaceHodge.exists_basis_chernPow`.

```lean
theorem isZero_hodgeCohomology_of_ne_or_gt (p q : ℕ)
    (hpq : p ≠ q ∨ m + 1 < p) : IsZero (hodgeCohomology A m p q)
```

**`Stacks.AlgebraicGeometry.ProjectiveSpaceHodge.isZero_projectiveHodgeCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceHodgeEveryDimension.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceHodgeEveryDimension.lean#L131). The attribute's comment: “H^q(ℙⁿ\_A, Ω^p) = 0 unless 0 ≤ p = q ≤ n, for every n ≥ 0”.

> **[Stacks, Tag 0FMI], the vanishing, for every `n ≥ 0`.** `H^q(ℙⁿ_A, Ωᵖ) = 0` unless
> `0 ≤ p = q ≤ n`. For `n ≥ 1` it is clause (1) of [Stacks, Tag 0FUK]
> (`isZero_hodgeCohomology_of_ne_or_gt`); for `n = 0` it is
> `isZero_projectiveHodgeCohomology_zero`.

```lean
theorem isZero_projectiveHodgeCohomology (p q : ℕ) (hpq : p ≠ q ∨ n < p) :
    IsZero (projectiveHodgeCohomology A n p q)
```

**`Stacks.AlgebraicGeometry.ProjectiveSpaceHodge.exists_basis_projectiveHodgeChernPow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceHodgeEveryDimension.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceHodgeEveryDimension.lean#L146). The attribute's comment: “for 0 ≤ p ≤ n the A-module H^p(ℙⁿ\_A, Ω^p) is free of rank one with basis element c₁^\{Hodge}(𝒪(1))^p, for every n ≥ 0”.

> **[Stacks, Tag 0FMI], the basis, for every `n ≥ 0`.** For `0 ≤ p ≤ n` the `A`-module
> `Hᵖ(ℙⁿ_A, Ωᵖ)` is free of rank one with basis element `c₁^{Hodge}(𝒪(1))ᵖ`, the `p`-th cup power
> of the Hodge first Chern class of `𝒪(1)` (`projectiveHodgeChernPow`).
>
> For `n ≥ 1` this is `exists_basis_chernPow`, through `projectiveHodgeChernPow_succ`. For `n = 0`
> only `p = 0` occurs, and `c⁰ = 1` is a basis of `H⁰(ℙ⁰_A, 𝒪) = A`
> (`exists_basis_projectiveHodgeCohomology_unitForm`).

```lean
theorem exists_basis_projectiveHodgeChernPow (p : ℕ) (hp : p ≤ n) :
    ∃ b : Module.Basis (Fin 1) A ↥(projectiveHodgeCohomology A n p p),
      b 0 = projectiveHodgeChernPow A n p
```

## Tag 0FMJ, a lemma

[Tag 0FMJ](https://stacks.math.columbia.edu/tag/0FMJ) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjectiveSpaceDeRham.isZero_deRhamCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceDeRhamCohomology.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceDeRhamCohomology.lean#L267). The attribute's comment: “the vanishing in every degree other than 2i with 0 ≤ i ≤ n”.

> **[Stacks, Tag 0FMJ], the vanishing.** In every degree that is not `2i` for some
> `0 ≤ i ≤ n` the de Rham cohomology `H^•_dR(ℙⁿ_A/A)` of projective space vanishes.
>
> By [Stacks, Tag 0FMI] the Hodge cohomology `H^q(ℙⁿ_A, Ωᵖ)` vanishes unless `p = q ≤ n`, so the
> hypercohomology `H^k(ℙⁿ_A, Ωᵖ[-p])` of the graded pieces of the brutal filtration vanishes unless
> `k = 2p`, and the terms vanish above degree `n`; inductively along the brutal filtration the
> de Rham cohomology vanishes outside the degrees `2i`, `0 ≤ i ≤ n`.

```lean
theorem isZero_deRhamCohomology (i : ℤ) (hi : ∀ p : ℕ, p ≤ m + 1 → i ≠ 2 * p) :
    IsZero (deRhamCohomology A m i)
```

**`Stacks.AlgebraicGeometry.ProjectiveSpaceDeRham.exists_basis_chernPow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceDeRhamCohomology.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceDeRhamCohomology.lean#L290). The attribute's comment: “free of rank one with basis c₁^dR(𝒪(1))^i for 0 ≤ i ≤ n”.

> **[Stacks, Tag 0FMJ], the computation in degree `2i`.** For `0 ≤ i ≤ n` the `A`-module
> `H^{2i}_dR(ℙⁿ_A/A)` is free of rank one **with basis element `c₁^{dR}(𝒪(1))^i`**, the `i`-th cup
> power of the de Rham first Chern class of `𝒪(1)`.
>
> The Hodge-to-de Rham spectral sequence degenerates, which identifies `H^{2i}_dR(ℙⁿ_A/A)` with
> `Hⁱ(ℙⁿ_A, Ωⁱ)` (`deRhamCohomologyEquiv`); under it `c₁^{dR}(𝒪(1))^i` goes to a unit multiple of
> `c₁^{Hodge}(𝒪(1))^i` (`exists_gradedEquiv_gradedChernPow`), which is a basis by
> [Stacks, Tag 0FMI].

```lean
theorem exists_basis_chernPow (i : ℕ) (hi : i ≤ m + 1) :
    ∃ b : Module.Basis (Fin 1) A ↥(deRhamCohomology A m (2 * (i : ℤ))), b 0 = chernPow A m i
```

**`Stacks.AlgebraicGeometry.ProjectiveSpaceDeRham.exists_basis_and_isZero_projectiveDeRhamCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceDeRhamEveryDimension.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/ProjectiveSpaceDeRhamEveryDimension.lean#L165). The attribute's comment: “for 0 ≤ i ≤ n the A-module H^\{2i}\_dR(ℙⁿ\_A/A) is free of rank one with basis c₁^dR(𝒪(1))^i, and every other degree vanishes, for every n ≥ 0”.

> **[Stacks, Tag 0FMJ].** For every `n ≥ 0`: for `0 ≤ i ≤ n` the `A`-module
> `H^{2i}_dR(ℙⁿ_A/A)` is free of rank one with basis element `c₁^{dR}(𝒪(1))^i`, and in every
> other degree `k` the de Rham cohomology `H^k_dR(ℙⁿ_A/A)` vanishes.
>
> For `n ≥ 1` both parts are `exists_basis_chernPow` and `isZero_deRhamCohomology`. For `n = 0`
> they are `exists_basis_projectiveDeRhamChernPow_zero` and
> `isZero_projectiveDeRhamCohomology_zero`.

```lean
theorem exists_basis_and_isZero_projectiveDeRhamCohomology :
    (∀ i : ℕ, i ≤ n → ∃ b : Module.Basis (Fin 1) A ↥(projectiveDeRhamCohomology A n (2 * (i : ℤ))),
      b 0 = projectiveDeRhamChernPow A n i) ∧
    ∀ k : ℤ, (∀ i : ℕ, i ≤ n → k ≠ 2 * i) → IsZero (projectiveDeRhamCohomology A n k)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.11, Tag 0FMG](https://stacks.math.columbia.edu/tag/0FMG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
