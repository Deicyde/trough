---
declaration: module
origin: cited
lean: IsSl2Triple.casimir, IsSl2Triple.toEnd_h_mul_e_sub, IsSl2Triple.toEnd_h_mul_f_sub, IsSl2Triple.toEnd_e_mul_f_sub, IsSl2Triple.commute_casimir_e, IsSl2Triple.commute_casimir_f, IsSl2Triple.commute_casimir_h, IsSl2Triple.casimir_symm
statement: formalized
proof: formalized
---

# The Casimir of an sl₂ triple

The module `PhyslibAlpha.Mathematics.RepresentationTheory.Sl2.Casimir`, [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean): 23 declarations, 23 with a docstring.

> An `sl₂` triple vanishes on the generalized kernel of its Casimir, a polynomial image of `M`.

## i. Overview

> Let `(h, e, f)` be an `sl₂` triple in a complex Lie algebra `L` acting on a finite-dimensional
> module `M`. The Casimir endomorphism `C = h² + 2h + 4fe` commutes with `e`, `f` and `h`, so its
> generalized kernel is stable under all three. On an irreducible representation of highest weight
> `n` the Casimir is the scalar `n² + 2n`, which vanishes only for the trivial representation. This
> file proves the corresponding statement without any appeal to complete reducibility. On the
> generalized kernel of `C`, the three generators act by zero.
>
> The argument works with eigenvalues of `h`. If `μ` is an eigenvalue of `h` and `μ + 2` is not,
> then an eigenvector for `μ` is killed by `e`. It is therefore a primitive vector, so `μ = n` is a
> natural number, and `C` acts on it by `n² + 2n`. Nilpotency of `C` forces `n = 0`. Walking up the
> chain `μ, μ + 2, …` shows that every eigenvalue of `h` is a non-positive even integer, and the
> same argument for the triple `(-h, f, e)`, which has the same Casimir, shows that it is also
> non-negative. So `h` has only the eigenvalue zero and is nilpotent. Since `h - 2` is then
> injective and `(h - 2)ᵏ e = e hᵏ`, the operator `e` vanishes, and likewise `f`. Finally
> `h = ⁅e, f⁆` vanishes too.
>
> Independently, for any endomorphism `C` of a finite-dimensional vector space, the projection onto
> the generalized kernel of `C` along the Fitting complement `⋂ₖ range Cᵏ` is `q(C)` for a polynomial
> `q` with constant term `1`. Combining the two, `q(C)` maps `M` onto the joint kernel of `e`, `f`
> and `h` and fixes it. Because `q(0) = 1`, the projection differs from the identity by a polynomial
> in the action of the Lie algebra without constant term.

## ii. Key results

> - `IsSl2Triple.casimir` : the Casimir endomorphism `h² + 2h + 4fe`.
> - `IsSl2Triple.commute_casimir_e`, `IsSl2Triple.commute_casimir_f`,
>   `IsSl2Triple.commute_casimir_h` : the Casimir commutes with the triple.
> - `IsSl2Triple.toEnd_eq_zero_of_isNilpotent_casimir` : a nilpotent Casimir forces the triple to
>   act by zero.
> - `IsSl2Triple.lie_eq_zero_of_mem_maxGenEigenspace` : the triple acts by zero on the generalized
>   kernel of the Casimir.
> - `Module.End.exists_polynomial_maxGenEigenspace_zero_proj` : the projection onto a generalized
>   kernel along the Fitting complement is a polynomial with constant term `1`.
> - `IsSl2Triple.exists_polynomial_casimir_proj` : a polynomial in the Casimir with constant term `1`
>   projects `M` onto the invariants of the triple.

## iv. References

> - J. E. Humphreys, Introduction to Lie Algebras and Representation Theory.

## A. The Casimir endomorphism

**`IsSl2Triple.casimir`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L98).

> The Casimir endomorphism `h² + 2h + 4fe` of the elements `h`, `e` and `f` acting on `M`.
> When `(h, e, f)` is an `sl₂` triple it commutes with all three, and on the irreducible
> representation of highest weight `n` it is the scalar `n² + 2n`.

```lean
def casimir (R M : Type*) {L : Type*} [CommRing R] [LieRing L] [LieAlgebra R L] [AddCommGroup M]
    [Module R M] [LieRingModule L M] [LieModule R L M] (h e f : L) : Module.End R M
```

### A.1. Commutation relations of the triple

**`IsSl2Triple.toEnd_h_mul_e_sub`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L112).

> The bracket `[h, e] = 2 e` on `M`.

```lean
lemma toEnd_h_mul_e_sub : toEnd ℂ L M h * toEnd ℂ L M e - toEnd ℂ L M e * toEnd ℂ L M h =
    2 • toEnd ℂ L M e
```

**`IsSl2Triple.toEnd_h_mul_f_sub`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L117).

> The bracket `[h, f] = -2 f` on `M`.

```lean
lemma toEnd_h_mul_f_sub : toEnd ℂ L M h * toEnd ℂ L M f - toEnd ℂ L M f * toEnd ℂ L M h =
    -(2 • toEnd ℂ L M f)
```

**`IsSl2Triple.toEnd_e_mul_f_sub`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L122).

> The bracket `[e, f] = h` on `M`.

```lean
lemma toEnd_e_mul_f_sub : toEnd ℂ L M e * toEnd ℂ L M f - toEnd ℂ L M f * toEnd ℂ L M e =
    toEnd ℂ L M h
```

### A.2. The Casimir commutes with the triple

**`IsSl2Triple.commute_casimir_e`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L133).

> The Casimir commutes with the action of `e`.

```lean
lemma commute_casimir_e : Commute (casimir ℂ M h e f) (toEnd ℂ L M e)
```

**`IsSl2Triple.commute_casimir_f`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L149).

> The Casimir commutes with the action of `f`.

```lean
lemma commute_casimir_f : Commute (casimir ℂ M h e f) (toEnd ℂ L M f)
```

**`IsSl2Triple.commute_casimir_h`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L165).

> The Casimir commutes with the action of `h`.

```lean
lemma commute_casimir_h : Commute (casimir ℂ M h e f) (toEnd ℂ L M h)
```

**`IsSl2Triple.casimir_symm`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L180).

> The triple `(-h, f, e)` has the same Casimir as `(h, e, f)`.

```lean
lemma casimir_symm : casimir ℂ M (-h) f e = casimir ℂ M h e f
```

## B. A nilpotent Casimir forces a trivial action

### B.1. Primitive vectors

**`IsSl2Triple.casimir_apply_of_hasPrimitiveVectorWith`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L198).

> The Casimir acts on a primitive vector of weight `μ` by the scalar `μ² + 2μ`.

```lean
lemma casimir_apply_of_hasPrimitiveVectorWith {m : M} {μ : ℂ} (P : t.HasPrimitiveVectorWith m μ) :
    casimir ℂ M h e f m = (μ ^ 2 + 2 * μ) • m
```

**`IsSl2Triple.eq_zero_of_hasPrimitiveVectorWith`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L207).

> If the Casimir is nilpotent, every primitive vector has weight zero.

```lean
lemma eq_zero_of_hasPrimitiveVectorWith (hC : IsNilpotent (casimir ℂ M h e f)) {m : M} {μ : ℂ}
    (P : t.HasPrimitiveVectorWith m μ) : μ = 0
```

### B.2. Eigenvalues of `h`

**`IsSl2Triple.eq_zero_of_not_hasEigenvalue_add_two`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L226).

> If the Casimir is nilpotent, an eigenvalue `μ` of `h` such that `μ + 2` is not an eigenvalue
> is zero, since its eigenvectors are primitive.

```lean
lemma eq_zero_of_not_hasEigenvalue_add_two (hC : IsNilpotent (casimir ℂ M h e f)) {μ : ℂ}
    (hμ : (toEnd ℂ L M h).HasEigenvalue μ) (hμ2 : ¬ (toEnd ℂ L M h).HasEigenvalue (μ + 2)) :
    μ = 0
```

**`IsSl2Triple.exists_nat_add_eq_zero`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L239).

> If the Casimir is nilpotent, every eigenvalue of `h` is a non-positive even integer.

```lean
lemma exists_nat_add_eq_zero (hC : IsNilpotent (casimir ℂ M h e f)) {μ : ℂ}
    (hμ : (toEnd ℂ L M h).HasEigenvalue μ) : ∃ n : ℕ, μ + 2 * n = 0
```

**`IsSl2Triple.hasEigenvalue_eq_zero`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L252).

> If the Casimir is nilpotent, the only eigenvalue of `h` is zero.

```lean
lemma hasEigenvalue_eq_zero (hC : IsNilpotent (casimir ℂ M h e f)) {μ : ℂ}
    (hμ : (toEnd ℂ L M h).HasEigenvalue μ) : μ = 0
```

**`IsSl2Triple.isNilpotent_toEnd_h`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L265).

> If the Casimir is nilpotent, so is the action of `h`.

```lean
lemma isNilpotent_toEnd_h (hC : IsNilpotent (casimir ℂ M h e f)) :
    IsNilpotent (toEnd ℂ L M h)
```

### B.3. Vanishing of the triple

**`IsSl2Triple.toEnd_e_eq_zero_of_isNilpotent`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L287).

> If `h` acts nilpotently, then `e` acts by zero, since `(h - 2)ᵏ e = e hᵏ` and `h - 2` is
> injective.

```lean
lemma toEnd_e_eq_zero_of_isNilpotent (hH : IsNilpotent (toEnd ℂ L M h)) :
    toEnd ℂ L M e = 0
```

**`IsSl2Triple.toEnd_eq_zero_of_isNilpotent_casimir`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L310).

> If the Casimir is nilpotent, then `e`, `f` and `h` all act by zero.

```lean
lemma toEnd_eq_zero_of_isNilpotent_casimir (hC : IsNilpotent (casimir ℂ M h e f)) :
    toEnd ℂ L M e = 0 ∧ toEnd ℂ L M f = 0 ∧ toEnd ℂ L M h = 0
```

### B.4. Endomorphisms satisfying the `sl₂` relations

**`Module.End.eq_zero_of_sl2_relations`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L333).

> Three endomorphisms `H`, `E`, `F` satisfying the `sl₂` relations, whose Casimir is nilpotent,
> all vanish. Unlike an `IsSl2Triple`, this allows `H = 0`, which is needed when restricting the
> action to an invariant subspace.

```lean
lemma eq_zero_of_sl2_relations {H E F : Module.End ℂ V} (hHE : H * E - E * H = 2 • E)
    (hHF : H * F - F * H = -(2 • F)) (hEF : E * F - F * E = H)
    (hC : IsNilpotent (H * H + 2 • H + 4 • (F * E))) : E = 0 ∧ F = 0 ∧ H = 0
```

## C. The generalized kernel of the Casimir

**`IsSl2Triple.lie_eq_zero_of_mem_maxGenEigenspace`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L363).

> The triple acts by zero on the generalized kernel of its Casimir.

```lean
lemma lie_eq_zero_of_mem_maxGenEigenspace {v : M}
    (hv : v ∈ (casimir ℂ M h e f).maxGenEigenspace 0) :
    ⁅e, v⁆ = 0 ∧ ⁅f, v⁆ = 0 ∧ ⁅h, v⁆ = 0
```

## D. The projection onto a generalized kernel

**`Module.End.mem_maxGenEigenspace_zero_iff`**, a lemma, [line 404](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L404).

> A vector lies in the generalized kernel of `C` if some power of `C` kills it.

```lean
lemma mem_maxGenEigenspace_zero_iff (C : Module.End K V) (v : V) :
    v ∈ C.maxGenEigenspace 0 ↔ ∃ k : ℕ, (C ^ k) v = 0
```

**`Module.End.pow_apply_eq_zero_of_isCoprime`**, a lemma, [line 410](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L410).

> If `Xᵇ g` annihilates `C` and `g` is coprime to `X`, then `Cᵇ` already kills every vector killed
> by some power of `C`.

```lean
lemma pow_apply_eq_zero_of_isCoprime {C : Module.End K V} {b k : ℕ} {g : K[X]}
    (hcop : IsCoprime X g) (hzero : aeval C (X ^ b * g) = 0) {v : V} (hv : (C ^ k) v = 0) :
    (C ^ b) v = 0
```

**`Module.End.exists_aeval_X_pow_mul_eq_zero`**, a lemma, [line 423](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L423).

> Every endomorphism of a finite-dimensional space is annihilated by a polynomial `Xᵇ g` with
> `0 < b` and `g` coprime to `X`.

```lean
lemma exists_aeval_X_pow_mul_eq_zero (C : Module.End K V) :
    ∃ (b : ℕ) (g : K[X]), 0 < b ∧ IsCoprime X g ∧ aeval C (X ^ b * g) = 0
```

**`Module.End.exists_polynomial_maxGenEigenspace_zero_proj`**, a lemma, [line 435](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L435).

> The projection onto the generalized kernel of `C` along the Fitting complement
> `⋂ₖ range Cᵏ` is `q(C)` for a polynomial `q` with constant term `1`.

```lean
lemma exists_polynomial_maxGenEigenspace_zero_proj (C : Module.End K V) :
    ∃ q : K[X], q.coeff 0 = 1 ∧ (∀ v ∈ C.maxGenEigenspace 0, aeval C q v = v) ∧
      (∀ v, aeval C q v ∈ C.maxGenEigenspace 0) ∧
      (∀ v ∈ ⨅ k : ℕ, LinearMap.range (C ^ k), aeval C q v = 0)
```

## E. The projection onto the invariants of the triple

**`IsSl2Triple.exists_polynomial_casimir_proj`**, a lemma, [line 475](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean#L475).

> There is a polynomial `q` with constant term `1` such that `q(C)`, for `C` the Casimir, maps
> `M` into the joint kernel of `e`, `f` and `h` and fixes every vector killed by `e` and `f`.

```lean
lemma exists_polynomial_casimir_proj :
    ∃ q : ℂ[X], q.coeff 0 = 1 ∧
      (∀ v, ⁅e, aeval (casimir ℂ M h e f) q v⁆ = 0 ∧ ⁅f, aeval (casimir ℂ M h e f) q v⁆ = 0 ∧
        ⁅h, aeval (casimir ℂ M h e f) q v⁆ = 0) ∧
      (∀ v : M, ⁅e, v⁆ = 0 → ⁅f, v⁆ = 0 → aeval (casimir ℂ M h e f) q v = v)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/Casimir.lean)
