---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.stringVec, PhyslibAlpha.Sl2.tensorF_stringVec, PhyslibAlpha.Sl2.tensorH_stringVec, PhyslibAlpha.Sl2.tensorE_stringVec_succ, PhyslibAlpha.Sl2.stringVec_ne_zero, PhyslibAlpha.Sl2.stringVec_eq_zero, PhyslibAlpha.Sl2.tensorE_stringVec_zero, PhyslibAlpha.Sl2.separator
statement: formalized
proof: formalized
---

# The equivariant Clebsch–Gordan decomposition

The module `PhyslibAlpha.Mathematics.RepresentationTheory.Sl2.TensorDecomposition`, [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean): 34 declarations (1 instance with no name), 18 with a docstring.

> Decomposes `V(m) ⊗ V(n)` into standard modules, compatibly with the diagonal `sl₂` action.

## i. Overview

> The lowering strings of the highest-weight vectors `hwVec m n k`, `k ≤ min m n`, are
> eigenvectors of one operator built from the Casimir element and the Cartan operator, with
> pairwise distinct eigenvalues. Hence they are linearly independent. Their number is
> `∑_k (m + n - 2k + 1) = (m + 1)(n + 1)`, so they form a basis of `V(m) ⊗ V(n)`. Sending the
> `l`-th vector of the `k`-th string to the coordinate vector `v_l` of the `k`-th summand gives a
> linear equivalence `V(m) ⊗ V(n) ≃ ⨁_k V(m + n - 2k)` that intertwines the diagonal raising,
> lowering and weight operators with the standard ones on each summand. This is the
> equivariant form of `clebsch_gordan`.

## ii. Key results

> - `stringVec_linearIndependent` shows that the lowering strings are linearly independent.
> - `tensorStringBasis` is the resulting basis of `V(m) ⊗ V(n)`.
> - `cgEquiv` is the Clebsch–Gordan equivalence `V(m) ⊗ V(n) ≃ ⨁_k V(m + n - 2k)`.
> - `cgEquiv_tensorE`, `cgEquiv_tensorF` and `cgEquiv_tensorH` show that it intertwines the
>   `sl₂` actions.

## iv. References

> - Mathlib, `Mathlib.Algebra.Lie.Sl2`.

## A. Lowering strings of the highest-weight vectors

**`PhyslibAlpha.Sl2.stringVec`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L67).

> The `l`-th vector `f^l w_k` of the lowering string of `hwVec m n k`.

```lean
def stringVec (m n k l : ℕ) : StandardSl2Module K m ⊗[K] StandardSl2Module K n
```

**`PhyslibAlpha.Sl2.tensorF_stringVec`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L71).

```lean
lemma tensorF_stringVec (k l : ℕ) :
    tensorF (K := K) m n (stringVec m n k l) = stringVec m n k (l + 1)
```

**`PhyslibAlpha.Sl2.tensorH_stringVec`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L81).

```lean
lemma tensorH_stringVec (l : ℕ) :
    tensorH (K := K) m n (stringVec m n k l) =
      (((m + n - 2 * k : ℕ) : K) - 2 * l) • stringVec m n k l
```

**`PhyslibAlpha.Sl2.tensorE_stringVec_succ`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L86).

```lean
lemma tensorE_stringVec_succ (l : ℕ) :
    tensorE (K := K) m n (stringVec m n k (l + 1)) =
      (((l : K) + 1) * (((m + n - 2 * k : ℕ) : K) - l)) • stringVec m n k l
```

**`PhyslibAlpha.Sl2.stringVec_ne_zero`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L91).

```lean
lemma stringVec_ne_zero {l : ℕ} (hl : l ≤ m + n - 2 * k) :
    stringVec (K := K) m n k l ≠ 0
```

**`PhyslibAlpha.Sl2.stringVec_eq_zero`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L95).

```lean
lemma stringVec_eq_zero {l : ℕ} (hl : m + n - 2 * k < l) :
    stringVec (K := K) m n k l = 0
```

**`PhyslibAlpha.Sl2.tensorE_stringVec_zero`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L100).

```lean
lemma tensorE_stringVec_zero : tensorE (K := K) m n (stringVec m n k 0) = 0
```

## B. Linear independence

### B.1. A separating operator

**`PhyslibAlpha.Sl2.separator`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L112).

> The operator `M (2EF + 2FE + H²) + H` with `M = 2(m + n) + 1`. The bracket is a multiple of
> the Casimir element, which distinguishes the strings; the weight `H` distinguishes the vectors
> within a string.

```lean
def separator (m n : ℕ) : Module.End K (StandardSl2Module K m ⊗[K] StandardSl2Module K n)
```

**`PhyslibAlpha.Sl2.sepVal`**, a def, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L119).

> The eigenvalue of `separator` on `stringVec m n k l`.

```lean
def sepVal (m n k l : ℕ) : K
```

**`PhyslibAlpha.Sl2.separator_stringVec`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L124).

```lean
lemma separator_stringVec {k : ℕ} (hmn : 0 < m + n) (hkm : k ≤ m) (hkn : k ≤ n) (l : ℕ) :
    separator (K := K) m n (stringVec m n k l) =
      sepVal (K := K) m n k l • stringVec m n k l
```

**`PhyslibAlpha.Sl2.StringIndex`**, an abbrev, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L149).

> Index set of the lowering strings: `k ≤ min m n` and `l ≤ m + n - 2k`.

```lean
abbrev StringIndex (m n : ℕ) : Type
```

**An instance with no name**, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L151).

```lean
instance : Nonempty (StringIndex m n)
```

**`PhyslibAlpha.Sl2.StringIndex.le_left`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L153).

```lean
lemma StringIndex.le_left (i : StringIndex m n) : (i.1 : ℕ) ≤ m
```

**`PhyslibAlpha.Sl2.StringIndex.le_right`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L157).

```lean
lemma StringIndex.le_right (i : StringIndex m n) : (i.1 : ℕ) ≤ n
```

**`PhyslibAlpha.Sl2.sepVal_int_injective`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L163).

> Integer core of `sepVal_injective`: with `M = 2s + 1`, the value `M N (N + 2) + N - 2l`
> determines `N` and `l`, provided `N ≤ s` and `l ≤ N`.

```lean
lemma sepVal_int_injective {s N N' l l' : ℕ} (hN : N ≤ s) (hN' : N' ≤ s) (hl : l ≤ N)
    (hl' : l' ≤ N')
    (h : (2 * s + 1 : ℤ) * (N * (N + 2)) + N - 2 * l =
      (2 * s + 1 : ℤ) * (N' * (N' + 2)) + N' - 2 * l') : N = N' ∧ l = l'
```

**`PhyslibAlpha.Sl2.sepVal_injective`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L183).

> The eigenvalues of `separator` on the lowering strings are pairwise distinct.

```lean
lemma sepVal_injective :
    Function.Injective (fun i : StringIndex m n => sepVal (K := K) m n i.1 i.2)
```

### B.2. The basis of lowering strings

**`PhyslibAlpha.Sl2.stringVec_linearIndependent`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L211).

> The lowering strings of the highest-weight vectors are linearly independent.

```lean
lemma stringVec_linearIndependent (hmn : 0 < m + n) :
    LinearIndependent K (fun i : StringIndex m n => stringVec (K := K) m n i.1 i.2)
```

**`PhyslibAlpha.Sl2.card_stringIndex`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L218).

```lean
lemma card_stringIndex : Fintype.card (StringIndex m n) = (m + 1) * (n + 1)
```

**`PhyslibAlpha.Sl2.finrank_standardSl2Module_tensor`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L224).

```lean
lemma finrank_standardSl2Module_tensor :
    Module.finrank K (StandardSl2Module K m ⊗[K] StandardSl2Module K n) = (m + 1) * (n + 1)
```

**`PhyslibAlpha.Sl2.tensorStringBasis`**, a def, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L229).

> The basis of `V(m) ⊗ V(n)` formed by the lowering strings of the highest-weight vectors.

```lean
def tensorStringBasis (hmn : 0 < m + n) :
    Module.Basis (StringIndex m n) K (StandardSl2Module K m ⊗[K] StandardSl2Module K n)
```

**`PhyslibAlpha.Sl2.tensorStringBasis_apply`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L234).

```lean
lemma tensorStringBasis_apply (hmn : 0 < m + n) (i : StringIndex m n) :
    tensorStringBasis (K := K) hmn i = stringVec m n i.1 i.2
```

## C. The decomposition

### C.1. The direct sum of standard modules

**`PhyslibAlpha.Sl2.CGSummand`**, an abbrev, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L243).

> The summand `V(m + n - 2k)` of the Clebsch–Gordan decomposition.

```lean
abbrev CGSummand (K : Type*) (m n : ℕ) (k : Fin (min m n + 1)) : Type _
```

**`PhyslibAlpha.Sl2.CGSum`**, an abbrev, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L247).

> The direct sum `⨁_k V(m + n - 2k)` of the Clebsch–Gordan decomposition.

```lean
abbrev CGSum (K : Type*) [Field K] (m n : ℕ) : Type _
```

**`PhyslibAlpha.Sl2.sumVec`**, a def, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L250).

> The coordinate vector `v_l` of the `k`-th summand of `CGSum`.

```lean
def sumVec (m n : ℕ) (k : Fin (min m n + 1)) (l : ℕ) : CGSum K m n
```

**`PhyslibAlpha.Sl2.sumEnd`**, a def, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L254).

> The endomorphism of `CGSum` acting by `A k` on the `k`-th summand.

```lean
def sumEnd (A : ∀ k, Module.End K (CGSummand K m n k)) : Module.End K (CGSum K m n)
```

**`PhyslibAlpha.Sl2.sumEnd_lof`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L258).

```lean
lemma sumEnd_lof (A : ∀ k, Module.End K (CGSummand K m n k)) (k : Fin (min m n + 1))
    (x : CGSummand K m n k) :
    sumEnd A (DirectSum.lof K _ (CGSummand K m n) k x) =
      DirectSum.lof K _ (CGSummand K m n) k (A k x)
```

**`PhyslibAlpha.Sl2.sumVec_linearIndependent`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L265).

```lean
lemma sumVec_linearIndependent :
    LinearIndependent K (fun i : StringIndex m n => sumVec (K := K) m n i.1 i.2)
```

**`PhyslibAlpha.Sl2.sumBasis`**, a def, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L277).

> The basis of `CGSum` formed by the coordinate vectors of the summands.

```lean
def sumBasis (m n : ℕ) : Module.Basis (StringIndex m n) K (CGSum K m n)
```

**`PhyslibAlpha.Sl2.sumBasis_apply`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L284).

```lean
lemma sumBasis_apply (i : StringIndex m n) : sumBasis (K := K) m n i = sumVec m n i.1 i.2
```

### C.2. The intertwining equivalence

**`PhyslibAlpha.Sl2.cgEquiv`**, a def, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L291).

> The Clebsch–Gordan equivalence `V(m) ⊗ V(n) ≃ ⨁_k V(m + n - 2k)`, sending the `l`-th
> vector of the `k`-th lowering string to the coordinate vector `v_l` of the `k`-th summand.

```lean
def cgEquiv (hmn : 0 < m + n) :
    (StandardSl2Module K m ⊗[K] StandardSl2Module K n) ≃ₗ[K] CGSum K m n
```

**`PhyslibAlpha.Sl2.cgEquiv_stringVec`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L296).

> `cgEquiv` on the lowering strings, for every `l : ℕ`.

```lean
lemma cgEquiv_stringVec (hmn : 0 < m + n) (k : Fin (min m n + 1)) (l : ℕ) :
    cgEquiv (K := K) hmn (stringVec m n k l) = sumVec m n k l
```

**`PhyslibAlpha.Sl2.cgEquiv_tensorF`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L308).

> `cgEquiv` intertwines the diagonal lowering operator with `ρF` on each summand.

```lean
lemma cgEquiv_tensorF (hmn : 0 < m + n) (x : StandardSl2Module K m ⊗[K] StandardSl2Module K n) :
    cgEquiv hmn (tensorF m n x) = sumEnd (fun _ => ρF) (cgEquiv hmn x)
```

**`PhyslibAlpha.Sl2.cgEquiv_tensorH`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L317).

> `cgEquiv` intertwines the diagonal weight operator with `ρH` on each summand.

```lean
lemma cgEquiv_tensorH (hmn : 0 < m + n) (x : StandardSl2Module K m ⊗[K] StandardSl2Module K n) :
    cgEquiv hmn (tensorH m n x) = sumEnd (fun _ => ρH) (cgEquiv hmn x)
```

**`PhyslibAlpha.Sl2.cgEquiv_tensorE`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean#L327).

> `cgEquiv` intertwines the diagonal raising operator with `ρE` on each summand.

```lean
lemma cgEquiv_tensorE (hmn : 0 < m + n) (x : StandardSl2Module K m ⊗[K] StandardSl2Module K n) :
    cgEquiv hmn (tensorE m n x) = sumEnd (fun _ => ρE) (cgEquiv hmn x)
```

## Depends on

- [Highest-weight vectors in tensor products of standard sl₂ modules](sl2-tensorhighestweight.md)

## Proof depends on

- [The Clebsch–Gordan dimension identity](sl2-clebschgordan.md)
- [Classification for two commuting sl₂ actions](sl2-commutingactions.md)

## Sources

- [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorDecomposition.lean)
