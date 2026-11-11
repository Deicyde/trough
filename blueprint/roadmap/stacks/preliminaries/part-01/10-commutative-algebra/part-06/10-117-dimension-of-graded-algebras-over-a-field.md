---
declaration: section
origin: cited
lean: GradedAlgebra.irrelevant_isMaximal_and_ringKrullDim_eq_natDegree_add_one
statement: formalized
proof: formalized
---

# 10.117 Dimension of graded algebras over a field

Section 10.117 of the Stacks Project, [Tag 00P5](https://stacks.math.columbia.edu/tag/00P5). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00P6, a lemma

[Tag 00P6](https://stacks.math.columbia.edu/tag/00P6) in the Stacks Project.

**`GradedAlgebra.irrelevant_isMaximal_and_ringKrullDim_eq_natDegree_add_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/KrullDimension.lean, line 943](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GradedAlgebra/KrullDimension.lean#L943). The attribute's comment: “Items (1)-(4). `dim_x Spec(S)` is the height of the irrelevant ideal, and the convention `deg 0 = -1` is unfolded into the cases `P = 0`, `P ≠ 0`. See the module docstring.”. References: EGA IV (6.10.5), “special case”.

> **Stacks 00P6.** Let `k` be a field and let `S` be a graded `k`-algebra with `S_0 = k` that is
> generated over `k` by finitely many elements of degree `1`. Let `P ∈ ℚ[T]` be the polynomial with
> `dim_k S_d = P(d)` for all `d ≫ 0`. Then: (1) the irrelevant ideal `m = S_+` is maximal;
> (2) every minimal prime of `S` is homogeneous and contained in `S_+`; (3) `dim(S) = deg(P) + 1`,
> with `deg(0) = -1`, and this equals the dimension `dim_x Spec(S) = dim(S_m) = height(m)` of
> `Spec(S)` at the closed point `x` given by `m`; (4) the Hilbert function
> `d ↦ length_{S_m} (m^d S_m / m^{d + 1} S_m)` of the local ring `S_m` is the Hilbert function
> `d ↦ dim_k S_d` of `S`.

```lean
public theorem GradedAlgebra.irrelevant_isMaximal_and_ringKrullDim_eq_natDegree_add_one
    {k S : Type*} [Field k] [CommRing S] [Nontrivial S] [Algebra k S]
    (𝒜 : ℕ → Submodule k S) [GradedAlgebra 𝒜] (h0 : 𝒜 0 = 1)
    [Module.Finite k ↥(𝒜 1)] (hgen : Algebra.adjoin k (𝒜 1 : Set S) = ⊤)
    (P : ℚ[X]) (hP : ∀ᶠ d : ℕ in Filter.atTop, P.eval (d : ℚ) = Module.finrank k ↥(𝒜 d)) :
    ∃ hm : 𝒜₊.toIdeal.IsMaximal,
      letI := hm.isPrime
      (∀ p ∈ minimalPrimes S, Ideal.IsHomogeneous 𝒜 p ∧ p ≤ 𝒜₊.toIdeal) ∧
      (P = 0 → ringKrullDim S = 0) ∧
      (P ≠ 0 → ringKrullDim S = (P.natDegree + 1 : ℕ)) ∧
      ringKrullDim S = 𝒜₊.toIdeal.height ∧
      ∀ d : ℕ, Module.length (Localization.AtPrime (𝒜₊).toIdeal)
          (↥(IsLocalRing.maximalIdeal (Localization.AtPrime (𝒜₊).toIdeal) ^ d) ⧸
            (IsLocalRing.maximalIdeal (Localization.AtPrime (𝒜₊).toIdeal) ^ (d + 1)).submoduleOf
              (IsLocalRing.maximalIdeal (Localization.AtPrime (𝒜₊).toIdeal) ^ d))
        = Module.finrank k ↥(𝒜 d)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.117, Tag 00P5](https://stacks.math.columbia.edu/tag/00P5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
